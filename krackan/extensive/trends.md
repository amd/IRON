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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 <b>(+22.82%)</b></td><td>0.04 <b>(+30.82%)</b></td><td>0.05 <b>(+39.55%)</b></td><td>0.04 <b>(+26.78%)</b></td><td>0.01 <b>(+22.22%)</b></td><td>173.70 <b>(-21.12%)</b></td><td>142.38 <b>(-23.54%)</b></td><td>134.90 <b>(-28.32%)</b></td><td>106.30 (-18.61%)</td><td>29.66 (-17.95%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>220.20 (n/a)</td><td>186.22 (n/a)</td><td>188.20 (n/a)</td><td>130.60 (n/a)</td><td>36.14 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+9.37%)</td><td>0.04 (+15.55%)</td><td>0.04 (+15.25%)</td><td>0.03 <b>(+33.44%)</b></td><td>0.01 <b>(-20.79%)</b></td><td>230.20 <b>(-25.04%)</b></td><td>173.46 (-16.30%)</td><td>165.80 (-13.24%)</td><td>141.40 (-8.54%)</td><td>34.36 <b>(-44.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>307.10 (n/a)</td><td>207.24 (n/a)</td><td>191.10 (n/a)</td><td>154.60 (n/a)</td><td>61.75 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (+6.60%)</td><td>0.04 (+7.59%)</td><td>0.03 (-2.06%)</td><td>0.03 <b>(+69.67%)</b></td><td>0.01 <b>(-30.79%)</b></td><td>213.30 <b>(-41.06%)</b></td><td>177.30 (-14.28%)</td><td>175.60 (+2.15%)</td><td>129.70 (-6.22%)</td><td>30.95 <b>(-65.31%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>361.90 (n/a)</td><td>206.84 (n/a)</td><td>171.90 (n/a)</td><td>138.30 (n/a)</td><td>89.21 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (+2.67%)</td><td>0.03 (+7.26%)</td><td>0.04 (+19.21%)</td><td>0.02 <b>(-21.33%)</b></td><td>0.01 (+19.42%)</td><td>332.70 <b>(+27.13%)</b></td><td>198.46 (-2.18%)</td><td>174.90 (-16.07%)</td><td>125.40 (-2.64%)</td><td>79.11 <b>(+66.38%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>261.70 (n/a)</td><td>202.88 (n/a)</td><td>208.40 (n/a)</td><td>128.80 (n/a)</td><td>47.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-8.10%)</td><td>0.04 (+10.87%)</td><td>0.04 (+9.07%)</td><td>0.03 (+18.24%)</td><td>0.01 <b>(-27.72%)</b></td><td>183.70 (-15.42%)</td><td>153.78 (-12.02%)</td><td>165.30 (-8.32%)</td><td>123.50 (+8.81%)</td><td>26.42 <b>(-32.61%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>174.78 (n/a)</td><td>180.30 (n/a)</td><td>113.50 (n/a)</td><td>39.20 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 <b>(+21.73%)</b></td><td>0.04 <b>(+27.66%)</b></td><td>0.04 <b>(+30.83%)</b></td><td>0.03 <b>(+24.99%)</b></td><td>0.01 <b>(+27.10%)</b></td><td>185.00 (-19.98%)</td><td>151.14 <b>(-21.58%)</b></td><td>140.30 <b>(-23.54%)</b></td><td>130.30 (-17.84%)</td><td>23.30 (-17.28%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>231.20 (n/a)</td><td>192.74 (n/a)</td><td>183.50 (n/a)</td><td>158.60 (n/a)</td><td>28.17 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+5.71%)</td><td>0.03 (-3.32%)</td><td>0.03 (-11.00%)</td><td>0.03 (+3.42%)</td><td>0.01 (+5.20%)</td><td>243.20 (-3.30%)</td><td>206.20 (+3.38%)</td><td>207.40 (+12.35%)</td><td>158.10 (-5.39%)</td><td>30.93 (-7.68%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.50 (n/a)</td><td>199.46 (n/a)</td><td>184.60 (n/a)</td><td>167.10 (n/a)</td><td>33.50 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 <b>(+34.43%)</b></td><td>0.04 <b>(+21.96%)</b></td><td>0.03 (+16.76%)</td><td>0.03 (+5.71%)</td><td>0.01 <b>(+158.88%)</b></td><td>211.50 (-5.41%)</td><td>172.86 (-16.69%)</td><td>179.40 (-14.37%)</td><td>138.80 <b>(-25.62%)</b></td><td>27.66 <b>(+80.52%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>223.60 (n/a)</td><td>207.48 (n/a)</td><td>209.50 (n/a)</td><td>186.60 (n/a)</td><td>15.32 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (+2.08%)</td><td>0.08 (+13.50%)</td><td>0.07 (+6.21%)</td><td>0.07 <b>(+41.88%)</b></td><td>0.01 <b>(-23.45%)</b></td><td>179.90 <b>(-29.53%)</b></td><td>155.46 (-14.24%)</td><td>164.50 (-5.84%)</td><td>128.10 (-1.99%)</td><td>23.04 <b>(-49.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>255.30 (n/a)</td><td>181.28 (n/a)</td><td>174.70 (n/a)</td><td>130.70 (n/a)</td><td>45.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (-3.21%)</td><td>0.07 (-9.69%)</td><td>0.07 (-1.45%)</td><td>0.03 <b>(-52.28%)</b></td><td>0.03 <b>(+57.51%)</b></td><td>379.60 <b>(+109.61%)</b></td><td>201.78 <b>(+25.94%)</b></td><td>174.60 (+1.45%)</td><td>116.10 (+3.29%)</td><td>103.95 <b>(+265.54%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>181.10 (n/a)</td><td>160.22 (n/a)</td><td>172.10 (n/a)</td><td>112.40 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (+5.70%)</td><td>0.08 (+5.97%)</td><td>0.08 (+5.09%)</td><td>0.07 (-0.22%)</td><td>0.01 (+5.35%)</td><td>184.10 (+0.22%)</td><td>149.38 (-5.59%)</td><td>151.30 (-4.84%)</td><td>120.10 (-5.43%)</td><td>23.80 (-1.34%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>158.22 (n/a)</td><td>159.00 (n/a)</td><td>127.00 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (+4.35%)</td><td>0.08 (+8.72%)</td><td>0.08 (+7.95%)</td><td>0.07 <b>(+26.00%)</b></td><td>0.01 (-17.49%)</td><td>172.10 <b>(-20.62%)</b></td><td>150.86 (-9.74%)</td><td>158.00 (-7.39%)</td><td>114.10 (-4.20%)</td><td>22.43 <b>(-37.95%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>216.80 (n/a)</td><td>167.14 (n/a)</td><td>170.60 (n/a)</td><td>119.10 (n/a)</td><td>36.14 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (+1.06%)</td><td>0.08 (+3.64%)</td><td>0.07 (+5.70%)</td><td>0.06 (-5.26%)</td><td>0.01 (+8.32%)</td><td>205.10 (+5.56%)</td><td>167.58 (-3.03%)</td><td>170.60 (-5.43%)</td><td>128.30 (-1.00%)</td><td>29.01 (+15.90%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.30 (n/a)</td><td>172.82 (n/a)</td><td>180.40 (n/a)</td><td>129.60 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 <b>(+60.69%)</b></td><td>0.09 <b>(+46.85%)</b></td><td>0.09 <b>(+52.64%)</b></td><td>0.07 <b>(+32.42%)</b></td><td>0.01 <b>(+163.85%)</b></td><td>174.20 <b>(-24.49%)</b></td><td>142.02 <b>(-30.85%)</b></td><td>135.50 <b>(-34.51%)</b></td><td>113.80 <b>(-37.78%)</b></td><td>23.76 <b>(+25.59%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>205.38 (n/a)</td><td>206.90 (n/a)</td><td>182.90 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (+13.82%)</td><td>0.06 (+2.93%)</td><td>0.06 (+3.26%)</td><td>0.05 (-5.28%)</td><td>0.01 <b>(+159.28%)</b></td><td>235.10 (+5.57%)</td><td>200.32 (-1.74%)</td><td>193.30 (-3.20%)</td><td>172.20 (-12.14%)</td><td>26.47 <b>(+140.64%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>222.70 (n/a)</td><td>203.86 (n/a)</td><td>199.70 (n/a)</td><td>196.00 (n/a)</td><td>11.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (+14.38%)</td><td>0.06 (-0.98%)</td><td>0.06 (-12.69%)</td><td>0.05 (-2.87%)</td><td>0.01 <b>(+51.52%)</b></td><td>229.80 (+2.96%)</td><td>195.40 (+2.65%)</td><td>214.40 (+14.53%)</td><td>140.50 (-12.57%)</td><td>36.35 <b>(+35.07%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>223.20 (n/a)</td><td>190.36 (n/a)</td><td>187.20 (n/a)</td><td>160.70 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (+2.82%)</td><td>0.13 (-7.70%)</td><td>0.14 (+0.13%)</td><td>0.07 <b>(-46.35%)</b></td><td>0.04 <b>(+162.27%)</b></td><td>377.00 <b>(+86.36%)</b></td><td>209.72 <b>(+21.99%)</b></td><td>171.70 (-0.12%)</td><td>141.80 (-2.74%)</td><td>97.99 <b>(+374.39%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.30 (n/a)</td><td>171.92 (n/a)</td><td>171.90 (n/a)</td><td>145.80 (n/a)</td><td>20.66 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 <b>(-20.83%)</b></td><td>0.17 (-0.13%)</td><td>0.16 (-5.38%)</td><td>0.15 <b>(+21.59%)</b></td><td>0.02 <b>(-61.84%)</b></td><td>163.90 (-17.76%)</td><td>148.06 (-4.14%)</td><td>151.30 (+5.66%)</td><td>131.30 <b>(+26.25%)</b></td><td>14.68 <b>(-60.82%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>199.30 (n/a)</td><td>154.46 (n/a)</td><td>143.20 (n/a)</td><td>104.00 (n/a)</td><td>37.48 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (+19.21%)</td><td>0.16 (+1.91%)</td><td>0.15 (-5.79%)</td><td>0.13 (-3.18%)</td><td>0.03 <b>(+95.09%)</b></td><td>195.50 (+3.28%)</td><td>161.18 (+0.65%)</td><td>159.80 (+6.11%)</td><td>118.80 (-16.16%)</td><td>33.58 <b>(+73.15%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>189.30 (n/a)</td><td>160.14 (n/a)</td><td>150.60 (n/a)</td><td>141.70 (n/a)</td><td>19.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (+11.74%)</td><td>0.15 (-1.11%)</td><td>0.14 (-8.10%)</td><td>0.14 (+2.23%)</td><td>0.03 <b>(+47.72%)</b></td><td>177.80 (-2.15%)</td><td>163.04 (+2.30%)</td><td>174.90 (+8.84%)</td><td>118.20 (-10.52%)</td><td>25.37 <b>(+27.72%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.70 (n/a)</td><td>159.38 (n/a)</td><td>160.70 (n/a)</td><td>132.10 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (-1.25%)</td><td>0.15 (+7.64%)</td><td>0.15 <b>(+22.74%)</b></td><td>0.09 (-13.55%)</td><td>0.04 <b>(+26.30%)</b></td><td>261.30 (+15.67%)</td><td>181.66 (-3.92%)</td><td>159.50 (-18.54%)</td><td>130.50 (+1.24%)</td><td>55.97 <b>(+55.37%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>225.90 (n/a)</td><td>189.08 (n/a)</td><td>195.80 (n/a)</td><td>128.90 (n/a)</td><td>36.02 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 <b>(+36.44%)</b></td><td>0.15 (+14.26%)</td><td>0.13 (-0.43%)</td><td>0.11 (-5.34%)</td><td>0.04 <b>(+425.56%)</b></td><td>214.60 (+5.66%)</td><td>176.30 (-8.54%)</td><td>196.30 (+0.46%)</td><td>130.80 <b>(-26.68%)</b></td><td>40.30 <b>(+298.33%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>192.76 (n/a)</td><td>195.40 (n/a)</td><td>178.40 (n/a)</td><td>10.12 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 <b>(+24.21%)</b></td><td>0.14 (+11.10%)</td><td>0.15 (+19.53%)</td><td>0.08 <b>(-29.72%)</b></td><td>0.03 <b>(+234.52%)</b></td><td>307.90 <b>(+42.28%)</b></td><td>193.00 (-3.87%)</td><td>168.80 (-16.31%)</td><td>143.10 (-19.47%)</td><td>66.11 <b>(+299.70%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>200.78 (n/a)</td><td>201.70 (n/a)</td><td>177.70 (n/a)</td><td>16.54 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (+10.95%)</td><td>0.13 (+9.36%)</td><td>0.14 (+18.08%)</td><td>0.11 (+1.14%)</td><td>0.02 <b>(+39.35%)</b></td><td>230.70 (-1.16%)</td><td>187.92 (-7.79%)</td><td>179.20 (-15.35%)</td><td>159.20 (-9.85%)</td><td>30.38 <b>(+25.40%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>233.40 (n/a)</td><td>203.80 (n/a)</td><td>211.70 (n/a)</td><td>176.60 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.38 (-9.58%)</td><td>0.31 (+3.58%)</td><td>0.28 (-3.10%)</td><td>0.24 <b>(+24.09%)</b></td><td>0.07 <b>(-24.52%)</b></td><td>206.20 (-19.42%)</td><td>166.94 (-6.55%)</td><td>175.30 (+3.18%)</td><td>128.00 (+10.63%)</td><td>34.28 <b>(-34.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>255.90 (n/a)</td><td>178.64 (n/a)</td><td>169.90 (n/a)</td><td>115.70 (n/a)</td><td>52.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.35 (-6.24%)</td><td>0.31 (+5.38%)</td><td>0.32 (+19.70%)</td><td>0.25 (+12.41%)</td><td>0.04 <b>(-28.34%)</b></td><td>194.30 (-11.03%)</td><td>163.80 (-6.58%)</td><td>152.10 (-16.43%)</td><td>139.00 (+6.68%)</td><td>23.79 <b>(-30.29%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>218.40 (n/a)</td><td>175.34 (n/a)</td><td>182.00 (n/a)</td><td>130.30 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.39 <b>(+20.67%)</b></td><td>0.31 (+16.23%)</td><td>0.30 (+14.59%)</td><td>0.27 (+12.59%)</td><td>0.05 <b>(+42.16%)</b></td><td>185.30 (-11.17%)</td><td>162.22 (-13.52%)</td><td>165.30 (-12.72%)</td><td>127.30 (-17.12%)</td><td>21.46 (+3.94%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>208.60 (n/a)</td><td>187.58 (n/a)</td><td>189.40 (n/a)</td><td>153.60 (n/a)</td><td>20.65 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (-15.37%)</td><td>0.30 (+0.29%)</td><td>0.30 (+5.56%)</td><td>0.28 (+12.00%)</td><td>0.01 <b>(-72.02%)</b></td><td>174.80 (-10.68%)</td><td>163.96 (-1.94%)</td><td>161.40 (-5.28%)</td><td>156.30 (+18.14%)</td><td>7.29 <b>(-70.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>195.70 (n/a)</td><td>167.20 (n/a)</td><td>170.40 (n/a)</td><td>132.30 (n/a)</td><td>24.38 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 <b>(-32.10%)</b></td><td>0.22 <b>(-25.27%)</b></td><td>0.22 <b>(-27.58%)</b></td><td>0.18 (-1.33%)</td><td>0.03 <b>(-60.04%)</b></td><td>271.50 (+1.38%)</td><td>229.52 <b>(+28.65%)</b></td><td>218.60 <b>(+38.09%)</b></td><td>205.60 <b>(+47.28%)</b></td><td>28.61 <b>(-44.09%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>267.80 (n/a)</td><td>178.40 (n/a)</td><td>158.30 (n/a)</td><td>139.60 (n/a)</td><td>51.18 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 <b>(-29.43%)</b></td><td>0.26 (-13.55%)</td><td>0.26 (+10.61%)</td><td>0.24 (+9.50%)</td><td>0.02 <b>(-79.22%)</b></td><td>206.20 (-8.68%)</td><td>191.16 (+7.55%)</td><td>189.50 (-9.59%)</td><td>170.30 <b>(+41.68%)</b></td><td>14.32 <b>(-72.22%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>225.80 (n/a)</td><td>177.74 (n/a)</td><td>209.60 (n/a)</td><td>120.20 (n/a)</td><td>51.54 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 <b>(-26.21%)</b></td><td>0.23 (-8.87%)</td><td>0.24 (-1.42%)</td><td>0.16 (+4.29%)</td><td>0.05 <b>(-49.12%)</b></td><td>303.20 (-4.11%)</td><td>219.98 (+3.23%)</td><td>208.20 (+1.41%)</td><td>170.50 <b>(+35.53%)</b></td><td>50.05 <b>(-31.09%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.39 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>316.20 (n/a)</td><td>213.10 (n/a)</td><td>205.30 (n/a)</td><td>125.80 (n/a)</td><td>72.62 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 <b>(-26.73%)</b></td><td>0.24 (-7.40%)</td><td>0.25 (-15.89%)</td><td>0.22 <b>(+34.75%)</b></td><td>0.02 <b>(-76.18%)</b></td><td>225.50 <b>(-25.80%)</b></td><td>207.26 (-0.25%)</td><td>198.90 (+18.89%)</td><td>193.20 <b>(+36.44%)</b></td><td>16.62 <b>(-76.25%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.29 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>303.90 (n/a)</td><td>207.78 (n/a)</td><td>167.30 (n/a)</td><td>141.60 (n/a)</td><td>69.98 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (-1.98%)</td><td>0.02 <b>(+26.70%)</b></td><td>0.02 <b>(+52.28%)</b></td><td>0.01 <b>(+25.24%)</b></td><td>0.00 <b>(-31.52%)</b></td><td>178.00 <b>(-20.14%)</b></td><td>139.82 <b>(-23.40%)</b></td><td>127.30 <b>(-34.35%)</b></td><td>120.20 (+1.95%)</td><td>23.65 <b>(-41.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>222.90 (n/a)</td><td>182.54 (n/a)</td><td>193.90 (n/a)</td><td>117.90 (n/a)</td><td>40.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (+3.19%)</td><td>0.02 <b>(+46.29%)</b></td><td>0.02 <b>(+41.81%)</b></td><td>0.02 <b>(+95.90%)</b></td><td>0.00 <b>(-52.86%)</b></td><td>163.70 <b>(-48.94%)</b></td><td>132.90 <b>(-39.73%)</b></td><td>122.80 <b>(-29.51%)</b></td><td>117.70 (-3.05%)</td><td>19.41 <b>(-78.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>320.60 (n/a)</td><td>220.52 (n/a)</td><td>174.20 (n/a)</td><td>121.40 (n/a)</td><td>91.59 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 <b>(-27.01%)</b></td><td>0.01 (-14.36%)</td><td>0.01 (-5.70%)</td><td>0.01 (-14.50%)</td><td>0.00 <b>(-42.84%)</b></td><td>226.90 (+16.96%)</td><td>189.70 (+15.25%)</td><td>179.60 (+6.02%)</td><td>160.10 <b>(+36.95%)</b></td><td>27.70 (-3.07%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>194.00 (n/a)</td><td>164.60 (n/a)</td><td>169.40 (n/a)</td><td>116.90 (n/a)</td><td>28.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (-0.50%)</td><td>0.01 (+0.86%)</td><td>0.01 (-2.85%)</td><td>0.01 (+15.16%)</td><td>0.00 (-10.15%)</td><td>232.00 (-13.17%)</td><td>186.42 (-2.55%)</td><td>191.50 (+2.90%)</td><td>125.80 (+0.56%)</td><td>38.20 <b>(-24.53%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>267.20 (n/a)</td><td>191.30 (n/a)</td><td>186.10 (n/a)</td><td>125.10 (n/a)</td><td>50.62 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (-13.49%)</td><td>0.01 (-15.59%)</td><td>0.01 (-12.62%)</td><td>0.01 <b>(-26.18%)</b></td><td>0.00 (-16.75%)</td><td>290.70 <b>(+35.46%)</b></td><td>202.54 (+19.14%)</td><td>198.10 (+14.44%)</td><td>151.10 (+15.61%)</td><td>53.57 <b>(+38.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>214.60 (n/a)</td><td>170.00 (n/a)</td><td>173.10 (n/a)</td><td>130.70 (n/a)</td><td>38.69 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (-15.29%)</td><td>0.01 (-13.36%)</td><td>0.01 (-12.37%)</td><td>0.01 <b>(-22.41%)</b></td><td>0.00 (+5.39%)</td><td>256.20 <b>(+28.87%)</b></td><td>187.06 (+16.82%)</td><td>175.90 (+14.15%)</td><td>157.20 (+18.02%)</td><td>39.42 <b>(+64.12%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>198.80 (n/a)</td><td>160.12 (n/a)</td><td>154.10 (n/a)</td><td>133.20 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (+17.19%)</td><td>0.02 (-3.32%)</td><td>0.01 (-13.35%)</td><td>0.01 <b>(-21.39%)</b></td><td>0.00 <b>(+122.14%)</b></td><td>233.30 <b>(+27.21%)</b></td><td>173.90 (+7.96%)</td><td>176.10 (+15.40%)</td><td>123.80 (-14.68%)</td><td>44.45 <b>(+137.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>183.40 (n/a)</td><td>161.08 (n/a)</td><td>152.60 (n/a)</td><td>145.10 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (+2.28%)</td><td>0.01 (+4.22%)</td><td>0.01 (+7.63%)</td><td>0.01 (+9.15%)</td><td>0.00 (-13.05%)</td><td>225.60 (-8.37%)</td><td>189.64 (-4.57%)</td><td>180.10 (-7.12%)</td><td>168.80 (-2.26%)</td><td>23.37 <b>(-21.60%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>246.20 (n/a)</td><td>198.72 (n/a)</td><td>193.90 (n/a)</td><td>172.70 (n/a)</td><td>29.81 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (-15.21%)</td><td>0.03 (-16.69%)</td><td>0.03 <b>(-33.75%)</b></td><td>0.03 (+12.95%)</td><td>0.01 <b>(-33.55%)</b></td><td>205.30 (-11.47%)</td><td>174.92 (+15.78%)</td><td>192.60 <b>(+50.94%)</b></td><td>131.30 (+17.86%)</td><td>33.01 <b>(-32.01%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>151.08 (n/a)</td><td>127.60 (n/a)</td><td>111.40 (n/a)</td><td>48.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 <b>(+26.05%)</b></td><td>0.03 (+10.10%)</td><td>0.04 (+7.76%)</td><td>0.02 (-18.48%)</td><td>0.01 <b>(+122.62%)</b></td><td>261.40 <b>(+22.67%)</b></td><td>162.98 (-3.53%)</td><td>147.80 (-7.22%)</td><td>116.20 <b>(-20.68%)</b></td><td>57.27 <b>(+121.53%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>168.94 (n/a)</td><td>159.30 (n/a)</td><td>146.50 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (-19.50%)</td><td>0.03 (-18.94%)</td><td>0.03 <b>(-21.20%)</b></td><td>0.02 <b>(-24.20%)</b></td><td>0.01 (-9.37%)</td><td>223.70 <b>(+31.90%)</b></td><td>178.54 <b>(+24.11%)</b></td><td>181.80 <b>(+26.87%)</b></td><td>142.50 <b>(+24.24%)</b></td><td>31.98 <b>(+46.57%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>169.60 (n/a)</td><td>143.86 (n/a)</td><td>143.30 (n/a)</td><td>114.70 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+19.72%)</td><td>0.03 (+5.96%)</td><td>0.03 (-5.43%)</td><td>0.03 <b>(+36.16%)</b></td><td>0.01 (-0.07%)</td><td>197.40 <b>(-26.56%)</b></td><td>175.62 (-7.12%)</td><td>184.20 (+5.74%)</td><td>130.30 (-16.47%)</td><td>26.15 <b>(-42.85%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.80 (n/a)</td><td>189.08 (n/a)</td><td>174.20 (n/a)</td><td>156.00 (n/a)</td><td>45.75 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (-4.45%)</td><td>0.03 (+1.12%)</td><td>0.03 (-15.98%)</td><td>0.02 (-6.46%)</td><td>0.01 <b>(+22.46%)</b></td><td>228.80 (+6.92%)</td><td>179.18 (+1.77%)</td><td>207.30 (+19.00%)</td><td>123.00 (+4.68%)</td><td>50.46 <b>(+36.02%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>176.06 (n/a)</td><td>174.20 (n/a)</td><td>117.50 (n/a)</td><td>37.10 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 <b>(-23.73%)</b></td><td>0.03 (-11.99%)</td><td>0.03 (-14.76%)</td><td>0.02 (-10.83%)</td><td>0.01 <b>(-28.25%)</b></td><td>227.90 (+12.16%)</td><td>187.92 (+12.58%)</td><td>204.30 (+17.28%)</td><td>149.50 <b>(+31.14%)</b></td><td>35.47 (+4.85%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>166.92 (n/a)</td><td>174.20 (n/a)</td><td>114.00 (n/a)</td><td>33.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (-0.67%)</td><td>0.03 (+7.84%)</td><td>0.03 (+4.00%)</td><td>0.03 (+19.74%)</td><td>0.00 <b>(-24.44%)</b></td><td>184.50 (-16.48%)</td><td>170.20 (-8.70%)</td><td>182.00 (-3.86%)</td><td>132.40 (+0.68%)</td><td>22.06 <b>(-34.28%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>186.42 (n/a)</td><td>189.30 (n/a)</td><td>131.50 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 <b>(+30.57%)</b></td><td>0.03 (+13.84%)</td><td>0.03 (+3.89%)</td><td>0.02 (+12.07%)</td><td>0.01 <b>(+118.32%)</b></td><td>224.80 (-10.79%)</td><td>194.04 (-10.67%)</td><td>208.90 (-3.73%)</td><td>149.20 <b>(-23.41%)</b></td><td>32.38 <b>(+48.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.00 (n/a)</td><td>217.22 (n/a)</td><td>217.00 (n/a)</td><td>194.80 (n/a)</td><td>21.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 <b>(+46.13%)</b></td><td>0.06 <b>(+30.51%)</b></td><td>0.06 (+3.67%)</td><td>0.05 <b>(+73.34%)</b></td><td>0.01 (+15.97%)</td><td>214.50 <b>(-42.32%)</b></td><td>174.12 <b>(-25.82%)</b></td><td>187.10 (-3.56%)</td><td>126.60 <b>(-31.57%)</b></td><td>35.32 <b>(-55.30%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>371.90 (n/a)</td><td>234.74 (n/a)</td><td>194.00 (n/a)</td><td>185.00 (n/a)</td><td>79.02 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (+0.47%)</td><td>0.05 (-19.66%)</td><td>0.06 (-9.33%)</td><td>0.03 <b>(-42.46%)</b></td><td>0.02 <b>(+262.05%)</b></td><td>313.00 <b>(+73.79%)</b></td><td>225.14 <b>(+36.09%)</b></td><td>178.50 (+10.32%)</td><td>151.70 (-0.46%)</td><td>78.78 <b>(+563.42%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>180.10 (n/a)</td><td>165.44 (n/a)</td><td>161.80 (n/a)</td><td>152.40 (n/a)</td><td>11.87 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (-16.51%)</td><td>0.06 (-0.37%)</td><td>0.06 (-5.83%)</td><td>0.06 <b>(+30.68%)</b></td><td>0.01 <b>(-62.99%)</b></td><td>184.70 <b>(-23.49%)</b></td><td>168.80 (-3.62%)</td><td>172.70 (+6.15%)</td><td>149.00 (+19.77%)</td><td>14.37 <b>(-66.61%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>241.40 (n/a)</td><td>175.14 (n/a)</td><td>162.70 (n/a)</td><td>124.40 (n/a)</td><td>43.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 (-15.43%)</td><td>0.05 <b>(-20.87%)</b></td><td>0.06 (+3.32%)</td><td>0.03 <b>(-47.91%)</b></td><td>0.02 <b>(+25.26%)</b></td><td>366.80 <b>(+91.94%)</b></td><td>227.34 <b>(+42.34%)</b></td><td>176.90 (-3.23%)</td><td>131.10 (+18.21%)</td><td>107.83 <b>(+181.93%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>191.10 (n/a)</td><td>159.72 (n/a)</td><td>182.80 (n/a)</td><td>110.90 (n/a)</td><td>38.25 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (+16.07%)</td><td>0.06 (-7.23%)</td><td>0.06 (-7.34%)</td><td>0.05 <b>(-27.43%)</b></td><td>0.02 <b>(+173.39%)</b></td><td>232.90 <b>(+37.81%)</b></td><td>174.64 (+12.35%)</td><td>168.80 (+7.93%)</td><td>119.50 (-13.90%)</td><td>41.29 <b>(+218.59%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>169.00 (n/a)</td><td>155.44 (n/a)</td><td>156.40 (n/a)</td><td>138.80 (n/a)</td><td>12.96 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-3.09%)</td><td>0.05 (-4.59%)</td><td>0.06 (-2.39%)</td><td>0.04 (-6.91%)</td><td>0.01 (+10.81%)</td><td>237.00 (+7.43%)</td><td>194.76 (+5.30%)</td><td>190.40 (+2.48%)</td><td>162.50 (+3.17%)</td><td>29.36 <b>(+22.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>184.96 (n/a)</td><td>185.80 (n/a)</td><td>157.50 (n/a)</td><td>23.90 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (-4.55%)</td><td>0.06 (+7.22%)</td><td>0.05 (-1.10%)</td><td>0.05 <b>(+25.49%)</b></td><td>0.01 <b>(-32.76%)</b></td><td>201.80 <b>(-20.33%)</b></td><td>180.76 (-8.61%)</td><td>193.20 (+1.10%)</td><td>152.40 (+4.74%)</td><td>22.28 <b>(-43.54%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>253.30 (n/a)</td><td>197.78 (n/a)</td><td>191.10 (n/a)</td><td>145.50 (n/a)</td><td>39.47 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (+17.47%)</td><td>0.05 (+2.02%)</td><td>0.05 (+4.03%)</td><td>0.03 <b>(-26.54%)</b></td><td>0.01 <b>(+132.84%)</b></td><td>350.80 <b>(+36.13%)</b></td><td>234.12 (+2.73%)</td><td>222.20 (-3.89%)</td><td>172.80 (-14.88%)</td><td>68.35 <b>(+189.00%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>257.70 (n/a)</td><td>227.90 (n/a)</td><td>231.20 (n/a)</td><td>203.00 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 <b>(+20.43%)</b></td><td>0.15 <b>(+35.74%)</b></td><td>0.17 <b>(+44.47%)</b></td><td>0.10 <b>(+65.05%)</b></td><td>0.03 (-0.03%)</td><td>215.60 <b>(-39.42%)</b></td><td>147.32 <b>(-29.65%)</b></td><td>126.40 <b>(-30.78%)</b></td><td>124.40 (-16.96%)</td><td>38.98 <b>(-53.06%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>355.90 (n/a)</td><td>209.40 (n/a)</td><td>182.60 (n/a)</td><td>149.80 (n/a)</td><td>83.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (+7.38%)</td><td>0.13 (+18.62%)</td><td>0.14 <b>(+38.96%)</b></td><td>0.09 (-0.36%)</td><td>0.03 <b>(+21.80%)</b></td><td>239.00 (+0.34%)</td><td>167.78 (-14.45%)</td><td>152.20 <b>(-28.00%)</b></td><td>128.90 (-6.86%)</td><td>44.71 (+17.20%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>238.20 (n/a)</td><td>196.12 (n/a)</td><td>211.40 (n/a)</td><td>138.40 (n/a)</td><td>38.15 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (+1.39%)</td><td>0.13 (+2.18%)</td><td>0.14 (+15.36%)</td><td>0.10 (-6.73%)</td><td>0.02 (+5.89%)</td><td>218.90 (+7.25%)</td><td>166.58 (-1.59%)</td><td>153.90 (-13.30%)</td><td>130.20 (-1.36%)</td><td>34.01 (+15.08%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.10 (n/a)</td><td>169.28 (n/a)</td><td>177.50 (n/a)</td><td>132.00 (n/a)</td><td>29.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (-12.27%)</td><td>0.13 (+2.94%)</td><td>0.14 (+17.56%)</td><td>0.09 (-14.87%)</td><td>0.03 (-6.17%)</td><td>232.50 (+17.48%)</td><td>164.92 (-2.18%)</td><td>150.30 (-14.94%)</td><td>126.70 (+13.94%)</td><td>44.51 <b>(+23.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>197.90 (n/a)</td><td>168.60 (n/a)</td><td>176.70 (n/a)</td><td>111.20 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (+13.21%)</td><td>0.13 (+4.68%)</td><td>0.13 (+6.50%)</td><td>0.09 <b>(-20.49%)</b></td><td>0.03 <b>(+157.56%)</b></td><td>234.10 <b>(+25.79%)</b></td><td>170.38 (-0.75%)</td><td>163.80 (-6.08%)</td><td>132.80 (-11.64%)</td><td>41.89 <b>(+177.38%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>186.10 (n/a)</td><td>171.66 (n/a)</td><td>174.40 (n/a)</td><td>150.30 (n/a)</td><td>15.10 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 <b>(+22.82%)</b></td><td>0.12 (+1.94%)</td><td>0.11 (-3.02%)</td><td>0.09 (-18.00%)</td><td>0.03 <b>(+185.29%)</b></td><td>237.00 <b>(+21.98%)</b></td><td>183.76 (+2.33%)</td><td>191.00 (+3.08%)</td><td>126.30 (-18.57%)</td><td>43.18 <b>(+183.00%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>194.30 (n/a)</td><td>179.58 (n/a)</td><td>185.30 (n/a)</td><td>155.10 (n/a)</td><td>15.26 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 <b>(+54.91%)</b></td><td>0.13 <b>(+37.55%)</b></td><td>0.13 <b>(+44.09%)</b></td><td>0.10 (+16.17%)</td><td>0.03 <b>(+232.69%)</b></td><td>206.60 (-13.92%)</td><td>163.98 <b>(-24.72%)</b></td><td>157.90 <b>(-30.59%)</b></td><td>126.50 <b>(-35.43%)</b></td><td>37.34 <b>(+88.08%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>240.00 (n/a)</td><td>217.84 (n/a)</td><td>227.50 (n/a)</td><td>195.90 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (+17.42%)</td><td>0.09 (+5.42%)</td><td>0.09 (-5.15%)</td><td>0.07 (+16.82%)</td><td>0.02 <b>(+25.44%)</b></td><td>294.70 (-14.41%)</td><td>229.90 (-4.84%)</td><td>233.10 (+5.43%)</td><td>176.30 (-14.83%)</td><td>50.49 (-12.95%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>344.30 (n/a)</td><td>241.60 (n/a)</td><td>221.10 (n/a)</td><td>207.00 (n/a)</td><td>58.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.90 (n/a)</td><td>145.80 (n/a)</td><td>154.00 (n/a)</td><td>111.20 (n/a)</td><td>32.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>158.44 (n/a)</td><td>154.60 (n/a)</td><td>130.10 (n/a)</td><td>30.92 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>160.32 (n/a)</td><td>140.10 (n/a)</td><td>120.80 (n/a)</td><td>40.63 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.20 (n/a)</td><td>171.84 (n/a)</td><td>181.40 (n/a)</td><td>105.80 (n/a)</td><td>55.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>148.10 (n/a)</td><td>136.50 (n/a)</td><td>131.80 (n/a)</td><td>21.29 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>245.80 (n/a)</td><td>168.78 (n/a)</td><td>157.30 (n/a)</td><td>129.40 (n/a)</td><td>44.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>158.62 (n/a)</td><td>152.10 (n/a)</td><td>129.90 (n/a)</td><td>31.32 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>158.00 (n/a)</td><td>157.60 (n/a)</td><td>131.60 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>170.10 (n/a)</td><td>149.74 (n/a)</td><td>157.50 (n/a)</td><td>122.80 (n/a)</td><td>19.25 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>228.20 (n/a)</td><td>156.24 (n/a)</td><td>137.20 (n/a)</td><td>131.70 (n/a)</td><td>40.96 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>174.20 (n/a)</td><td>148.12 (n/a)</td><td>157.70 (n/a)</td><td>109.20 (n/a)</td><td>25.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>194.50 (n/a)</td><td>159.70 (n/a)</td><td>160.70 (n/a)</td><td>129.10 (n/a)</td><td>26.20 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.38 (+0.22%)</td><td>0.28 (-4.08%)</td><td>0.27 (-12.09%)</td><td>0.22 (+1.77%)</td><td>0.06 (+0.25%)</td><td>222.40 (-1.77%)</td><td>179.54 (+4.11%)</td><td>183.40 (+13.77%)</td><td>129.80 (-0.23%)</td><td>34.54 (-4.78%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>226.40 (n/a)</td><td>172.46 (n/a)</td><td>161.20 (n/a)</td><td>130.10 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>205.40 (n/a)</td><td>175.44 (n/a)</td><td>166.30 (n/a)</td><td>155.50 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>217.70 (n/a)</td><td>177.90 (n/a)</td><td>175.20 (n/a)</td><td>154.10 (n/a)</td><td>25.78 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>272.50 (n/a)</td><td>192.46 (n/a)</td><td>209.80 (n/a)</td><td>119.20 (n/a)</td><td>63.75 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>152.26 (n/a)</td><td>148.50 (n/a)</td><td>120.60 (n/a)</td><td>26.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>155.40 (n/a)</td><td>153.50 (n/a)</td><td>114.90 (n/a)</td><td>38.96 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>155.72 (n/a)</td><td>161.00 (n/a)</td><td>115.70 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>176.22 (n/a)</td><td>178.40 (n/a)</td><td>136.90 (n/a)</td><td>25.86 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>246.20 (n/a)</td><td>165.94 (n/a)</td><td>165.70 (n/a)</td><td>111.60 (n/a)</td><td>53.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>141.14 (n/a)</td><td>134.40 (n/a)</td><td>116.30 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>362.80 (n/a)</td><td>206.40 (n/a)</td><td>205.10 (n/a)</td><td>118.70 (n/a)</td><td>97.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>197.06 (n/a)</td><td>193.90 (n/a)</td><td>169.50 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>217.00 (n/a)</td><td>169.34 (n/a)</td><td>167.80 (n/a)</td><td>129.10 (n/a)</td><td>38.97 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>232.90 (n/a)</td><td>164.00 (n/a)</td><td>172.60 (n/a)</td><td>104.80 (n/a)</td><td>51.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>223.00 (n/a)</td><td>152.36 (n/a)</td><td>133.00 (n/a)</td><td>109.40 (n/a)</td><td>44.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>332.40 (n/a)</td><td>178.92 (n/a)</td><td>143.60 (n/a)</td><td>116.90 (n/a)</td><td>87.90 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>214.80 (n/a)</td><td>171.74 (n/a)</td><td>154.80 (n/a)</td><td>137.70 (n/a)</td><td>35.04 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>205.30 (n/a)</td><td>159.26 (n/a)</td><td>165.10 (n/a)</td><td>123.40 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>248.80 (n/a)</td><td>178.72 (n/a)</td><td>160.90 (n/a)</td><td>148.20 (n/a)</td><td>41.45 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.94 (+14.82%)</td><td>14.45 (+10.47%)</td><td>14.60 (+12.23%)</td><td>12.84 (+0.88%)</td><td>1.10 <b>(+135.51%)</b></td><td>4337.50 (-0.87%)</td><td>3872.72 (-9.13%)</td><td>3815.50 (-10.90%)</td><td>3495.50 (-12.91%)</td><td>302.53 <b>(+105.27%)</b></td><td>15358.90 (+14.82%)</td><td>13929.05 (+10.47%)</td><td>14070.66 (+12.23%)</td><td>12377.40 (+0.88%)</td><td>1063.59 <b>(+135.51%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.88 (n/a)</td><td>13.08 (n/a)</td><td>13.01 (n/a)</td><td>12.73 (n/a)</td><td>0.47 (n/a)</td><td>4375.60 (n/a)</td><td>4262.04 (n/a)</td><td>4282.20 (n/a)</td><td>4013.70 (n/a)</td><td>147.38 (n/a)</td><td>13375.96 (n/a)</td><td>12609.11 (n/a)</td><td>12537.33 (n/a)</td><td>12269.77 (n/a)</td><td>451.61 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.67 (-19.78%)</td><td>14.91 (-14.53%)</td><td>14.95 (-15.61%)</td><td>14.23 (+0.23%)</td><td>0.64 <b>(-71.32%)</b></td><td>921.00 (-0.23%)</td><td>880.08 (+15.56%)</td><td>876.80 (+18.49%)</td><td>836.70 <b>(+24.66%)</b></td><td>37.50 <b>(-63.89%)</b></td><td>10266.29 (-19.78%)</td><td>9774.58 (-14.53%)</td><td>9796.37 (-15.61%)</td><td>9326.72 (+0.23%)</td><td>416.40 <b>(-71.32%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>19.53 (n/a)</td><td>17.45 (n/a)</td><td>17.71 (n/a)</td><td>14.20 (n/a)</td><td>2.22 (n/a)</td><td>923.10 (n/a)</td><td>761.58 (n/a)</td><td>740.00 (n/a)</td><td>671.20 (n/a)</td><td>103.86 (n/a)</td><td>12798.33 (n/a)</td><td>11436.87 (n/a)</td><td>11608.38 (n/a)</td><td>9305.08 (n/a)</td><td>1452.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.19 (-0.82%)</td><td>13.88 (-1.50%)</td><td>14.09 (-0.26%)</td><td>12.58 (-3.02%)</td><td>1.05 <b>(+26.01%)</b></td><td>4426.50 (+3.11%)</td><td>4031.60 (+1.71%)</td><td>3954.60 (+0.26%)</td><td>3666.30 (+0.82%)</td><td>308.75 <b>(+31.87%)</b></td><td>14643.24 (-0.82%)</td><td>13378.71 (-1.50%)</td><td>13575.69 (-0.26%)</td><td>12128.60 (-3.02%)</td><td>1016.38 <b>(+26.01%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>15.32 (n/a)</td><td>14.09 (n/a)</td><td>14.12 (n/a)</td><td>12.98 (n/a)</td><td>0.84 (n/a)</td><td>4292.80 (n/a)</td><td>3963.70 (n/a)</td><td>3944.30 (n/a)</td><td>3636.40 (n/a)</td><td>234.13 (n/a)</td><td>14763.92 (n/a)</td><td>13582.66 (n/a)</td><td>13611.25 (n/a)</td><td>12506.20 (n/a)</td><td>806.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>16.93 (-14.16%)</td><td>14.88 (-15.71%)</td><td>14.36 <b>(-22.97%)</b></td><td>12.69 (-12.19%)</td><td>1.92 (-11.96%)</td><td>1407.10 (+13.89%)</td><td>1216.16 (+18.64%)</td><td>1243.90 <b>(+29.82%)</b></td><td>1055.10 (+16.50%)</td><td>155.65 (+13.78%)</td><td>12721.00 (-14.16%)</td><td>11183.56 (-15.71%)</td><td>10789.74 <b>(-22.97%)</b></td><td>9538.75 (-12.19%)</td><td>1442.75 (-11.96%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>19.72 (n/a)</td><td>17.65 (n/a)</td><td>18.64 (n/a)</td><td>14.45 (n/a)</td><td>2.18 (n/a)</td><td>1235.50 (n/a)</td><td>1025.10 (n/a)</td><td>958.20 (n/a)</td><td>905.70 (n/a)</td><td>136.80 (n/a)</td><td>14818.88 (n/a)</td><td>13267.55 (n/a)</td><td>14007.85 (n/a)</td><td>10863.18 (n/a)</td><td>1638.74 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>10.61 (-2.50%)</td><td>10.58 (+0.17%)</td><td>10.58 (+1.28%)</td><td>10.54 (+1.00%)</td><td>0.03 <b>(-85.26%)</b></td><td>7774.50 (-0.99%)</td><td>7742.78 (-0.20%)</td><td>7744.10 (-1.26%)</td><td>7719.90 (+2.56%)</td><td>20.95 <b>(-85.03%)</b></td><td>13908.69 (-2.50%)</td><td>13867.74 (+0.17%)</td><td>13865.35 (+1.28%)</td><td>13811.09 (+1.00%)</td><td>37.46 <b>(-85.26%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>10.88 (n/a)</td><td>10.56 (n/a)</td><td>10.45 (n/a)</td><td>10.43 (n/a)</td><td>0.19 (n/a)</td><td>7851.90 (n/a)</td><td>7758.22 (n/a)</td><td>7842.90 (n/a)</td><td>7527.10 (n/a)</td><td>139.97 (n/a)</td><td>14264.96 (n/a)</td><td>13843.69 (n/a)</td><td>13690.61 (n/a)</td><td>13674.91 (n/a)</td><td>254.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>14.74 <b>(-32.12%)</b></td><td>12.42 <b>(-28.98%)</b></td><td>11.34 <b>(-36.76%)</b></td><td>10.29 <b>(-22.39%)</b></td><td>2.10 <b>(-31.45%)</b></td><td>2089.80 <b>(+28.85%)</b></td><td>1769.32 <b>(+40.32%)</b></td><td>1895.00 <b>(+58.13%)</b></td><td>1458.30 <b>(+47.33%)</b></td><td>287.80 <b>(+24.07%)</b></td><td>11780.94 <b>(-32.12%)</b></td><td>9927.67 <b>(-28.98%)</b></td><td>9065.90 <b>(-36.76%)</b></td><td>8220.95 <b>(-22.39%)</b></td><td>1677.22 <b>(-31.45%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>21.72 (n/a)</td><td>17.49 (n/a)</td><td>17.94 (n/a)</td><td>13.25 (n/a)</td><td>3.06 (n/a)</td><td>1621.90 (n/a)</td><td>1260.90 (n/a)</td><td>1198.40 (n/a)</td><td>989.80 (n/a)</td><td>231.98 (n/a)</td><td>17356.72 (n/a)</td><td>13979.64 (n/a)</td><td>14335.34 (n/a)</td><td>10592.15 (n/a)</td><td>2446.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>11.02 (-11.48%)</td><td>10.71 (-13.87%)</td><td>10.73 (-13.66%)</td><td>10.38 (-16.42%)</td><td>0.29 <b>(+2297.75%)</b></td><td>7892.00 (+19.65%)</td><td>7656.36 (+16.17%)</td><td>7634.40 (+15.82%)</td><td>7432.60 (+12.96%)</td><td>209.71 <b>(+3151.52%)</b></td><td>14446.46 (-11.48%)</td><td>14032.61 (-13.87%)</td><td>14064.60 (-13.66%)</td><td>13605.49 (-16.42%)</td><td>383.64 <b>(+2298.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>12.45 (n/a)</td><td>12.43 (n/a)</td><td>12.43 (n/a)</td><td>12.42 (n/a)</td><td>0.01 (n/a)</td><td>6595.80 (n/a)</td><td>6590.46 (n/a)</td><td>6591.50 (n/a)</td><td>6579.60 (n/a)</td><td>6.45 (n/a)</td><td>16319.37 (n/a)</td><td>16292.42 (n/a)</td><td>16289.85 (n/a)</td><td>16279.14 (n/a)</td><td>16.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.55 (-3.40%)</td><td>3.32 (-11.80%)</td><td>3.14 (-4.38%)</td><td>2.75 (-7.10%)</td><td>0.71 (-15.97%)</td><td>500.00 (+7.64%)</td><td>426.90 (+12.43%)</td><td>437.90 (+4.56%)</td><td>302.60 (+3.52%)</td><td>74.21 (-6.98%)</td><td>887.14 (-3.40%)</td><td>647.79 (-11.80%)</td><td>612.96 (-4.38%)</td><td>536.90 (-7.10%)</td><td>137.60 (-15.97%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.71 (n/a)</td><td>3.77 (n/a)</td><td>3.29 (n/a)</td><td>2.96 (n/a)</td><td>0.84 (n/a)</td><td>464.50 (n/a)</td><td>379.70 (n/a)</td><td>418.80 (n/a)</td><td>292.30 (n/a)</td><td>79.78 (n/a)</td><td>918.40 (n/a)</td><td>734.44 (n/a)</td><td>641.02 (n/a)</td><td>577.94 (n/a)</td><td>163.75 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.28 (-19.03%)</td><td>3.62 (-12.32%)</td><td>3.60 (-8.01%)</td><td>2.91 (-18.98%)</td><td>0.50 <b>(-27.32%)</b></td><td>472.20 <b>(+23.42%)</b></td><td>385.98 (+13.67%)</td><td>382.60 (+8.72%)</td><td>321.80 <b>(+23.53%)</b></td><td>55.56 (+13.12%)</td><td>834.29 (-19.03%)</td><td>706.58 (-12.32%)</td><td>701.65 (-8.01%)</td><td>568.42 (-18.98%)</td><td>97.12 <b>(-27.32%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.28 (n/a)</td><td>4.13 (n/a)</td><td>3.91 (n/a)</td><td>3.60 (n/a)</td><td>0.69 (n/a)</td><td>382.60 (n/a)</td><td>339.56 (n/a)</td><td>351.90 (n/a)</td><td>260.50 (n/a)</td><td>49.12 (n/a)</td><td>1030.40 (n/a)</td><td>805.89 (n/a)</td><td>762.75 (n/a)</td><td>701.61 (n/a)</td><td>133.62 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.11 (-11.62%)</td><td>5.16 (+8.19%)</td><td>4.40 (+19.04%)</td><td>3.52 (-2.12%)</td><td>1.91 <b>(-22.58%)</b></td><td>391.10 (+2.17%)</td><td>293.42 (-11.15%)</td><td>312.50 (-16.02%)</td><td>169.70 (+13.13%)</td><td>92.52 (-8.28%)</td><td>1581.41 (-11.62%)</td><td>1006.42 (+8.19%)</td><td>858.87 (+19.04%)</td><td>686.32 (-2.12%)</td><td>371.91 <b>(-22.58%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.17 (n/a)</td><td>4.77 (n/a)</td><td>3.70 (n/a)</td><td>3.60 (n/a)</td><td>2.46 (n/a)</td><td>382.80 (n/a)</td><td>330.24 (n/a)</td><td>372.10 (n/a)</td><td>150.00 (n/a)</td><td>100.87 (n/a)</td><td>1789.38 (n/a)</td><td>930.20 (n/a)</td><td>721.49 (n/a)</td><td>701.21 (n/a)</td><td>480.38 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.83 <b>(-20.78%)</b></td><td>4.70 (+3.15%)</td><td>4.84 <b>(+23.87%)</b></td><td>3.41 (-6.10%)</td><td>0.94 <b>(-40.27%)</b></td><td>403.20 (+6.50%)</td><td>303.26 (-6.23%)</td><td>284.20 (-19.26%)</td><td>235.90 <b>(+26.22%)</b></td><td>65.75 (-15.07%)</td><td>1137.73 <b>(-20.78%)</b></td><td>916.55 (+3.15%)</td><td>944.59 <b>(+23.87%)</b></td><td>665.70 (-6.10%)</td><td>183.52 <b>(-40.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.36 (n/a)</td><td>4.56 (n/a)</td><td>3.91 (n/a)</td><td>3.63 (n/a)</td><td>1.58 (n/a)</td><td>378.60 (n/a)</td><td>323.42 (n/a)</td><td>352.00 (n/a)</td><td>186.90 (n/a)</td><td>77.41 (n/a)</td><td>1436.14 (n/a)</td><td>888.57 (n/a)</td><td>762.58 (n/a)</td><td>708.95 (n/a)</td><td>307.25 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.80 (-15.34%)</td><td>3.42 (-10.91%)</td><td>3.31 (-10.97%)</td><td>3.15 (-2.40%)</td><td>0.25 <b>(-52.53%)</b></td><td>436.60 (+2.46%)</td><td>404.32 (+11.00%)</td><td>415.40 (+12.33%)</td><td>362.40 (+18.12%)</td><td>29.01 <b>(-42.31%)</b></td><td>740.80 (-15.34%)</td><td>666.77 (-10.91%)</td><td>646.21 (-10.97%)</td><td>614.79 (-2.40%)</td><td>49.54 <b>(-52.53%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.49 (n/a)</td><td>3.84 (n/a)</td><td>3.72 (n/a)</td><td>3.23 (n/a)</td><td>0.54 (n/a)</td><td>426.10 (n/a)</td><td>364.24 (n/a)</td><td>369.80 (n/a)</td><td>306.80 (n/a)</td><td>50.29 (n/a)</td><td>875.06 (n/a)</td><td>748.42 (n/a)</td><td>725.81 (n/a)</td><td>629.92 (n/a)</td><td>104.36 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.21 (-11.17%)</td><td>3.85 (+3.44%)</td><td>3.28 (-0.86%)</td><td>2.90 (-4.67%)</td><td>1.11 (-8.15%)</td><td>473.90 (+4.91%)</td><td>380.62 (-3.21%)</td><td>419.80 (+0.86%)</td><td>264.40 (+12.61%)</td><td>100.36 (+10.85%)</td><td>1015.40 (-11.17%)</td><td>750.61 (+3.44%)</td><td>639.44 (-0.86%)</td><td>566.48 (-4.67%)</td><td>215.76 (-8.15%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.86 (n/a)</td><td>3.72 (n/a)</td><td>3.31 (n/a)</td><td>3.05 (n/a)</td><td>1.20 (n/a)</td><td>451.70 (n/a)</td><td>393.26 (n/a)</td><td>416.20 (n/a)</td><td>234.80 (n/a)</td><td>90.54 (n/a)</td><td>1143.08 (n/a)</td><td>725.65 (n/a)</td><td>644.97 (n/a)</td><td>594.23 (n/a)</td><td>234.90 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.74 (-0.99%)</td><td>3.65 (+3.76%)</td><td>3.21 (+1.16%)</td><td>2.93 (-7.47%)</td><td>0.77 (+7.37%)</td><td>469.30 (+8.06%)</td><td>389.94 (-3.00%)</td><td>428.60 (-1.15%)</td><td>290.30 (+0.97%)</td><td>75.27 (+17.15%)</td><td>924.55 (-0.99%)</td><td>711.31 (+3.76%)</td><td>626.31 (+1.16%)</td><td>571.96 (-7.47%)</td><td>149.25 (+7.37%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.79 (n/a)</td><td>3.51 (n/a)</td><td>3.17 (n/a)</td><td>3.17 (n/a)</td><td>0.71 (n/a)</td><td>434.30 (n/a)</td><td>401.98 (n/a)</td><td>433.60 (n/a)</td><td>287.50 (n/a)</td><td>64.25 (n/a)</td><td>933.76 (n/a)</td><td>685.56 (n/a)</td><td>619.12 (n/a)</td><td>618.11 (n/a)</td><td>139.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.18 <b>(-52.87%)</b></td><td>1.09 <b>(-50.78%)</b></td><td>1.10 <b>(-50.64%)</b></td><td>0.99 <b>(-46.03%)</b></td><td>0.07 <b>(-75.08%)</b></td><td>403.70 <b>(+85.27%)</b></td><td>368.84 <b>(+101.24%)</b></td><td>365.40 <b>(+102.55%)</b></td><td>339.20 <b>(+112.13%)</b></td><td>23.07 (-1.20%)</td><td>98.92 <b>(-52.87%)</b></td><td>91.25 <b>(-50.78%)</b></td><td>91.83 <b>(-50.64%)</b></td><td>83.12 <b>(-46.03%)</b></td><td>5.62 <b>(-75.08%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>2.51 (n/a)</td><td>2.22 (n/a)</td><td>2.23 (n/a)</td><td>1.84 (n/a)</td><td>0.27 (n/a)</td><td>217.90 (n/a)</td><td>183.28 (n/a)</td><td>180.40 (n/a)</td><td>159.90 (n/a)</td><td>23.35 (n/a)</td><td>209.87 (n/a)</td><td>185.39 (n/a)</td><td>186.02 (n/a)</td><td>154.01 (n/a)</td><td>22.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.77 (+9.39%)</td><td>6.08 (+7.64%)</td><td>5.27 (-0.52%)</td><td>4.61 (-11.69%)</td><td>1.56 <b>(+91.20%)</b></td><td>419.10 (+13.24%)</td><td>334.38 (-3.66%)</td><td>366.90 (+0.52%)</td><td>248.70 (-8.60%)</td><td>80.25 <b>(+91.05%)</b></td><td>1619.01 (+9.39%)</td><td>1266.37 (+7.64%)</td><td>1097.54 (-0.52%)</td><td>960.72 (-11.69%)</td><td>324.78 <b>(+91.20%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.11 (n/a)</td><td>5.65 (n/a)</td><td>5.30 (n/a)</td><td>5.22 (n/a)</td><td>0.82 (n/a)</td><td>370.10 (n/a)</td><td>347.10 (n/a)</td><td>365.00 (n/a)</td><td>272.10 (n/a)</td><td>42.01 (n/a)</td><td>1480.03 (n/a)</td><td>1176.49 (n/a)</td><td>1103.27 (n/a)</td><td>1087.83 (n/a)</td><td>169.87 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>19.22 (+8.82%)</td><td>14.87 (+6.72%)</td><td>14.77 (+5.97%)</td><td>10.58 (-6.12%)</td><td>3.16 <b>(+30.54%)</b></td><td>520.40 (+6.51%)</td><td>384.72 (-4.84%)</td><td>372.80 (-5.64%)</td><td>286.40 (-8.09%)</td><td>86.78 <b>(+30.64%)</b></td><td>7499.38 (+8.82%)</td><td>5799.70 (+6.72%)</td><td>5760.42 (+5.97%)</td><td>4126.44 (-6.12%)</td><td>1232.29 <b>(+30.54%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>17.67 (n/a)</td><td>13.93 (n/a)</td><td>13.93 (n/a)</td><td>11.27 (n/a)</td><td>2.42 (n/a)</td><td>488.60 (n/a)</td><td>404.28 (n/a)</td><td>395.10 (n/a)</td><td>311.60 (n/a)</td><td>66.42 (n/a)</td><td>6891.53 (n/a)</td><td>5434.72 (n/a)</td><td>5435.83 (n/a)</td><td>4395.28 (n/a)</td><td>944.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>10.07 (-11.38%)</td><td>7.92 (-10.42%)</td><td>7.59 (-8.16%)</td><td>6.40 (-18.19%)</td><td>1.36 (-6.50%)</td><td>859.80 <b>(+22.23%)</b></td><td>710.54 (+12.02%)</td><td>725.20 (+8.89%)</td><td>546.70 (+12.84%)</td><td>114.04 <b>(+28.85%)</b></td><td>3928.22 (-11.38%)</td><td>3089.62 (-10.42%)</td><td>2961.22 (-8.16%)</td><td>2497.66 (-18.19%)</td><td>530.56 (-6.50%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.36 (n/a)</td><td>8.84 (n/a)</td><td>8.27 (n/a)</td><td>7.83 (n/a)</td><td>1.45 (n/a)</td><td>703.40 (n/a)</td><td>634.28 (n/a)</td><td>666.00 (n/a)</td><td>484.50 (n/a)</td><td>88.50 (n/a)</td><td>4432.74 (n/a)</td><td>3449.01 (n/a)</td><td>3224.37 (n/a)</td><td>3053.19 (n/a)</td><td>567.45 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>11.46 (-2.67%)</td><td>9.85 (+2.41%)</td><td>9.40 (+0.55%)</td><td>8.07 (-5.43%)</td><td>1.45 (+10.63%)</td><td>718.30 (+5.74%)</td><td>599.10 (-1.96%)</td><td>617.30 (-0.55%)</td><td>506.30 (+2.74%)</td><td>88.63 (+17.51%)</td><td>4771.68 (-2.67%)</td><td>4103.73 (+2.41%)</td><td>3913.66 (+0.55%)</td><td>3363.49 (-5.43%)</td><td>603.56 (+10.63%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.77 (n/a)</td><td>9.62 (n/a)</td><td>9.34 (n/a)</td><td>8.54 (n/a)</td><td>1.31 (n/a)</td><td>679.30 (n/a)</td><td>611.08 (n/a)</td><td>620.70 (n/a)</td><td>492.80 (n/a)</td><td>75.42 (n/a)</td><td>4902.37 (n/a)</td><td>4007.19 (n/a)</td><td>3892.06 (n/a)</td><td>3556.53 (n/a)</td><td>545.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.90 (n/a)</td><td>172.94 (n/a)</td><td>179.70 (n/a)</td><td>129.50 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>264.90 (n/a)</td><td>179.94 (n/a)</td><td>174.30 (n/a)</td><td>124.70 (n/a)</td><td>53.70 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.00 (n/a)</td><td>179.76 (n/a)</td><td>189.30 (n/a)</td><td>133.30 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.80 (n/a)</td><td>178.38 (n/a)</td><td>174.10 (n/a)</td><td>135.00 (n/a)</td><td>35.45 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>169.70 (n/a)</td><td>159.70 (n/a)</td><td>156.00 (n/a)</td><td>154.70 (n/a)</td><td>6.50 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.00 (n/a)</td><td>190.24 (n/a)</td><td>192.10 (n/a)</td><td>173.10 (n/a)</td><td>11.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.80 (n/a)</td><td>155.72 (n/a)</td><td>146.20 (n/a)</td><td>126.70 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.90 (n/a)</td><td>207.16 (n/a)</td><td>197.80 (n/a)</td><td>185.40 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.60 (n/a)</td><td>155.92 (n/a)</td><td>146.00 (n/a)</td><td>141.40 (n/a)</td><td>17.34 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>162.64 (n/a)</td><td>169.10 (n/a)</td><td>125.60 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.40 (n/a)</td><td>151.20 (n/a)</td><td>151.00 (n/a)</td><td>130.70 (n/a)</td><td>14.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.20 (n/a)</td><td>149.58 (n/a)</td><td>151.30 (n/a)</td><td>110.90 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>147.06 (n/a)</td><td>133.50 (n/a)</td><td>114.50 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.50 (n/a)</td><td>189.00 (n/a)</td><td>194.70 (n/a)</td><td>127.00 (n/a)</td><td>43.41 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.40 (n/a)</td><td>182.72 (n/a)</td><td>177.70 (n/a)</td><td>130.20 (n/a)</td><td>41.27 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.50 (n/a)</td><td>206.74 (n/a)</td><td>206.70 (n/a)</td><td>170.70 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.40 (n/a)</td><td>154.46 (n/a)</td><td>153.20 (n/a)</td><td>126.70 (n/a)</td><td>18.70 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>174.70 (n/a)</td><td>159.24 (n/a)</td><td>166.40 (n/a)</td><td>129.90 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>172.00 (n/a)</td><td>157.92 (n/a)</td><td>168.50 (n/a)</td><td>129.00 (n/a)</td><td>18.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.00 (n/a)</td><td>168.54 (n/a)</td><td>166.80 (n/a)</td><td>117.80 (n/a)</td><td>35.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.20 (n/a)</td><td>157.58 (n/a)</td><td>163.70 (n/a)</td><td>130.00 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>188.00 (n/a)</td><td>149.14 (n/a)</td><td>161.90 (n/a)</td><td>112.80 (n/a)</td><td>31.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>181.10 (n/a)</td><td>166.58 (n/a)</td><td>175.10 (n/a)</td><td>138.40 (n/a)</td><td>18.49 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>320.90 (n/a)</td><td>245.64 (n/a)</td><td>218.50 (n/a)</td><td>181.50 (n/a)</td><td>62.36 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>205.90 (n/a)</td><td>156.78 (n/a)</td><td>155.80 (n/a)</td><td>122.40 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>175.60 (n/a)</td><td>157.50 (n/a)</td><td>171.00 (n/a)</td><td>116.90 (n/a)</td><td>24.82 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.10 (n/a)</td><td>173.96 (n/a)</td><td>173.60 (n/a)</td><td>129.50 (n/a)</td><td>33.73 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>209.20 (n/a)</td><td>159.98 (n/a)</td><td>145.00 (n/a)</td><td>120.70 (n/a)</td><td>34.88 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>210.60 (n/a)</td><td>173.56 (n/a)</td><td>184.30 (n/a)</td><td>139.50 (n/a)</td><td>29.11 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>297.90 (n/a)</td><td>206.74 (n/a)</td><td>175.50 (n/a)</td><td>144.70 (n/a)</td><td>63.21 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>270.40 (n/a)</td><td>190.20 (n/a)</td><td>184.60 (n/a)</td><td>133.40 (n/a)</td><td>52.22 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>258.70 (n/a)</td><td>215.34 (n/a)</td><td>209.40 (n/a)</td><td>194.20 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.16 (+0.96%)</td><td>4.12 (+0.24%)</td><td>4.11 (-0.04%)</td><td>4.10 (+0.22%)</td><td>0.02 <b>(+118.83%)</b></td><td>19174.90 (-0.22%)</td><td>19092.26 (-0.23%)</td><td>19125.20 (+0.04%)</td><td>18920.30 (-0.95%)</td><td>100.39 <b>(+116.00%)</b></td><td>2837.54 (+0.96%)</td><td>2812.04 (+0.24%)</td><td>2807.14 (-0.04%)</td><td>2799.86 (+0.22%)</td><td>14.87 <b>(+118.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>4.09 (n/a)</td><td>0.01 (n/a)</td><td>19217.40 (n/a)</td><td>19137.12 (n/a)</td><td>19117.60 (n/a)</td><td>19101.60 (n/a)</td><td>46.47 (n/a)</td><td>2810.60 (n/a)</td><td>2805.40 (n/a)</td><td>2808.25 (n/a)</td><td>2793.67 (n/a)</td><td>6.79 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.78 (+12.52%)</td><td>4.06 (-1.87%)</td><td>4.16 (-0.52%)</td><td>3.54 (-10.59%)</td><td>0.53 <b>(+349.36%)</b></td><td>2659.90 (+11.85%)</td><td>2348.86 (+3.22%)</td><td>2263.10 (+0.52%)</td><td>1967.80 (-11.12%)</td><td>303.78 <b>(+359.14%)</b></td><td>1879.94 (+12.52%)</td><td>1596.46 (-1.87%)</td><td>1634.63 (-0.52%)</td><td>1390.81 (-10.59%)</td><td>208.64 <b>(+349.36%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.25 (n/a)</td><td>4.14 (n/a)</td><td>4.18 (n/a)</td><td>3.95 (n/a)</td><td>0.12 (n/a)</td><td>2378.10 (n/a)</td><td>2275.52 (n/a)</td><td>2251.30 (n/a)</td><td>2214.10 (n/a)</td><td>66.16 (n/a)</td><td>1670.84 (n/a)</td><td>1626.81 (n/a)</td><td>1643.18 (n/a)</td><td>1555.60 (n/a)</td><td>46.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.14 (+2.17%)</td><td>0.97 (-1.86%)</td><td>0.97 (-4.96%)</td><td>0.82 (-3.91%)</td><td>0.12 (-7.55%)</td><td>270.30 (+4.08%)</td><td>230.30 (+1.71%)</td><td>227.30 (+5.23%)</td><td>194.40 (-2.11%)</td><td>27.39 (-6.59%)</td><td>48.55 (+2.17%)</td><td>41.44 (-1.86%)</td><td>41.51 (-4.96%)</td><td>34.91 (-3.91%)</td><td>4.91 (-7.55%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.11 (n/a)</td><td>0.99 (n/a)</td><td>1.02 (n/a)</td><td>0.85 (n/a)</td><td>0.12 (n/a)</td><td>259.70 (n/a)</td><td>226.42 (n/a)</td><td>216.00 (n/a)</td><td>198.60 (n/a)</td><td>29.32 (n/a)</td><td>47.51 (n/a)</td><td>42.22 (n/a)</td><td>43.68 (n/a)</td><td>36.33 (n/a)</td><td>5.31 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.10 (-1.57%)</td><td>0.93 (-0.80%)</td><td>0.93 (+0.04%)</td><td>0.69 (-4.71%)</td><td>0.16 (+6.20%)</td><td>320.50 (+4.94%)</td><td>245.26 (+1.27%)</td><td>236.60 (-0.04%)</td><td>200.30 (+1.62%)</td><td>46.96 (+13.53%)</td><td>47.12 (-1.57%)</td><td>39.51 (-0.80%)</td><td>39.88 (+0.04%)</td><td>29.44 (-4.71%)</td><td>6.83 (+6.20%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.12 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.72 (n/a)</td><td>0.15 (n/a)</td><td>305.40 (n/a)</td><td>242.18 (n/a)</td><td>236.70 (n/a)</td><td>197.10 (n/a)</td><td>41.36 (n/a)</td><td>47.87 (n/a)</td><td>39.83 (n/a)</td><td>39.87 (n/a)</td><td>30.90 (n/a)</td><td>6.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.53 (-0.01%)</td><td>0.53 (+0.01%)</td><td>0.53 (-0.01%)</td><td>0.53 (+0.03%)</td><td>0.00 (-16.40%)</td><td>47871.60 (-0.03%)</td><td>47818.72 (-0.01%)</td><td>47811.10 (+0.01%)</td><td>47790.30 (+0.01%)</td><td>32.90 (-16.43%)</td><td>359.48 (-0.01%)</td><td>359.27 (+0.01%)</td><td>359.33 (-0.01%)</td><td>358.87 (+0.03%)</td><td>0.25 (-16.41%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47886.40 (n/a)</td><td>47822.90 (n/a)</td><td>47807.80 (n/a)</td><td>47785.20 (n/a)</td><td>39.36 (n/a)</td><td>359.52 (n/a)</td><td>359.24 (n/a)</td><td>359.35 (n/a)</td><td>358.76 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (+2.23%)</td><td>0.21 (+0.95%)</td><td>0.21 (+0.46%)</td><td>0.21 (+0.98%)</td><td>0.00 <b>(+62.04%)</b></td><td>119356.50 (-0.98%)</td><td>118029.34 (-0.93%)</td><td>118313.40 (-0.46%)</td><td>115300.50 (-2.18%)</td><td>1649.36 <b>(+56.77%)</b></td><td>149.00 (+2.23%)</td><td>145.58 (+0.95%)</td><td>145.21 (+0.46%)</td><td>143.94 (+0.98%)</td><td>2.06 <b>(+62.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120532.20 (n/a)</td><td>119139.60 (n/a)</td><td>118855.20 (n/a)</td><td>117869.20 (n/a)</td><td>1052.06 (n/a)</td><td>145.75 (n/a)</td><td>144.21 (n/a)</td><td>144.54 (n/a)</td><td>142.53 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.91 (-0.28%)</td><td>0.90 (+0.01%)</td><td>0.90 (-0.16%)</td><td>0.90 (+1.05%)</td><td>0.00 <b>(-57.98%)</b></td><td>28013.00 (-1.03%)</td><td>27890.30 (-0.02%)</td><td>27918.40 (+0.16%)</td><td>27749.80 (+0.28%)</td><td>104.00 <b>(-58.34%)</b></td><td>619.10 (-0.28%)</td><td>615.99 (+0.01%)</td><td>615.36 (-0.16%)</td><td>613.28 (+1.05%)</td><td>2.30 <b>(-57.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28305.80 (n/a)</td><td>27895.02 (n/a)</td><td>27874.90 (n/a)</td><td>27673.00 (n/a)</td><td>249.63 (n/a)</td><td>620.82 (n/a)</td><td>615.92 (n/a)</td><td>616.32 (n/a)</td><td>606.94 (n/a)</td><td>5.47 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.68 (+3.84%)</td><td>3.57 (+3.54%)</td><td>3.63 (+5.54%)</td><td>3.42 (+1.66%)</td><td>0.12 <b>(+78.32%)</b></td><td>7348.10 (-1.64%)</td><td>7062.72 (-3.36%)</td><td>6936.60 (-5.25%)</td><td>6847.00 (-3.70%)</td><td>236.27 <b>(+69.31%)</b></td><td>2509.11 (+3.84%)</td><td>2434.62 (+3.54%)</td><td>2476.68 (+5.54%)</td><td>2338.00 (+1.66%)</td><td>80.55 <b>(+78.32%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.54 (n/a)</td><td>3.44 (n/a)</td><td>3.44 (n/a)</td><td>3.37 (n/a)</td><td>0.07 (n/a)</td><td>7470.40 (n/a)</td><td>7308.22 (n/a)</td><td>7320.60 (n/a)</td><td>7109.90 (n/a)</td><td>139.55 (n/a)</td><td>2416.33 (n/a)</td><td>2351.45 (n/a)</td><td>2346.77 (n/a)</td><td>2299.71 (n/a)</td><td>45.17 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.02 (-1.90%)</td><td>2.83 (-0.93%)</td><td>2.84 (-0.04%)</td><td>2.65 (-2.34%)</td><td>0.13 (-5.63%)</td><td>9482.30 (+2.39%)</td><td>8917.86 (+0.92%)</td><td>8847.90 (+0.04%)</td><td>8343.40 (+1.94%)</td><td>422.01 (-1.52%)</td><td>2059.10 (-1.90%)</td><td>1929.92 (-0.93%)</td><td>1941.68 (-0.04%)</td><td>1811.78 (-2.34%)</td><td>91.65 (-5.63%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.07 (n/a)</td><td>2.85 (n/a)</td><td>2.85 (n/a)</td><td>2.72 (n/a)</td><td>0.14 (n/a)</td><td>9260.60 (n/a)</td><td>8836.42 (n/a)</td><td>8844.50 (n/a)</td><td>8184.80 (n/a)</td><td>428.53 (n/a)</td><td>2098.99 (n/a)</td><td>1947.98 (n/a)</td><td>1942.43 (n/a)</td><td>1855.16 (n/a)</td><td>97.11 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.34 (+1.05%)</td><td>3.24 (+1.33%)</td><td>3.23 (+1.62%)</td><td>3.15 (+0.60%)</td><td>0.08 <b>(+26.27%)</b></td><td>7985.90 (-0.60%)</td><td>7772.20 (-1.29%)</td><td>7791.20 (-1.59%)</td><td>7541.70 (-1.04%)</td><td>196.73 <b>(+24.57%)</b></td><td>2277.97 (+1.05%)</td><td>2211.56 (+1.33%)</td><td>2205.04 (+1.62%)</td><td>2151.28 (+0.60%)</td><td>56.11 <b>(+26.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.30 (n/a)</td><td>3.20 (n/a)</td><td>3.18 (n/a)</td><td>3.13 (n/a)</td><td>0.07 (n/a)</td><td>8034.10 (n/a)</td><td>7874.08 (n/a)</td><td>7917.20 (n/a)</td><td>7620.90 (n/a)</td><td>157.92 (n/a)</td><td>2254.30 (n/a)</td><td>2182.54 (n/a)</td><td>2169.95 (n/a)</td><td>2138.37 (n/a)</td><td>44.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.80 (-0.00%)</td><td>0.80 (+0.06%)</td><td>0.80 (+0.11%)</td><td>0.80 (+0.04%)</td><td>0.00 <b>(-29.73%)</b></td><td>94862.30 (-0.04%)</td><td>94788.88 (-0.06%)</td><td>94774.00 (-0.11%)</td><td>94764.40 (+0.00%)</td><td>41.49 <b>(-29.80%)</b></td><td>725.16 (-0.00%)</td><td>724.97 (+0.06%)</td><td>725.09 (+0.11%)</td><td>724.41 (+0.04%)</td><td>0.32 <b>(-29.73%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94896.00 (n/a)</td><td>94846.72 (n/a)</td><td>94882.90 (n/a)</td><td>94763.80 (n/a)</td><td>59.10 (n/a)</td><td>725.17 (n/a)</td><td>724.53 (n/a)</td><td>724.26 (n/a)</td><td>724.16 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.73 (+0.00%)</td><td>0.73 (-0.04%)</td><td>0.73 (-0.02%)</td><td>0.73 (-0.14%)</td><td>0.00 <b>(+687.17%)</b></td><td>103452.50 (+0.14%)</td><td>103342.00 (+0.04%)</td><td>103327.40 (+0.02%)</td><td>103283.80 (-0.00%)</td><td>66.30 <b>(+684.92%)</b></td><td>665.35 (+0.00%)</td><td>664.97 (-0.04%)</td><td>665.07 (-0.02%)</td><td>664.26 (-0.14%)</td><td>0.43 <b>(+686.76%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103308.60 (n/a)</td><td>103301.58 (n/a)</td><td>103303.80 (n/a)</td><td>103287.30 (n/a)</td><td>8.45 (n/a)</td><td>665.32 (n/a)</td><td>665.23 (n/a)</td><td>665.22 (n/a)</td><td>665.19 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.69 (-0.14%)</td><td>0.68 (-0.23%)</td><td>0.68 (-0.09%)</td><td>0.68 (-0.56%)</td><td>0.00 <b>(+91.82%)</b></td><td>110981.20 (+0.56%)</td><td>110395.54 (+0.23%)</td><td>110241.30 (+0.09%)</td><td>110044.10 (+0.14%)</td><td>367.25 <b>(+93.22%)</b></td><td>624.47 (-0.14%)</td><td>622.49 (-0.23%)</td><td>623.36 (-0.09%)</td><td>619.20 (-0.56%)</td><td>2.07 <b>(+91.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110361.70 (n/a)</td><td>110143.68 (n/a)</td><td>110140.70 (n/a)</td><td>109885.60 (n/a)</td><td>190.07 (n/a)</td><td>625.37 (n/a)</td><td>623.91 (n/a)</td><td>623.92 (n/a)</td><td>622.67 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>2.80 (+0.03%)</td><td>2.79 (+0.19%)</td><td>2.80 (+0.06%)</td><td>2.79 (+0.81%)</td><td>0.00 <b>(-71.94%)</b></td><td>37590.40 (-0.80%)</td><td>37521.32 (-0.19%)</td><td>37497.20 (-0.06%)</td><td>37482.10 (-0.03%)</td><td>47.10 <b>(-72.19%)</b></td><td>2864.68 (+0.03%)</td><td>2861.69 (+0.19%)</td><td>2863.52 (+0.06%)</td><td>2856.42 (+0.81%)</td><td>3.59 <b>(-71.94%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>2.79 (n/a)</td><td>2.77 (n/a)</td><td>0.01 (n/a)</td><td>37893.70 (n/a)</td><td>37594.00 (n/a)</td><td>37518.10 (n/a)</td><td>37492.60 (n/a)</td><td>169.39 (n/a)</td><td>2863.88 (n/a)</td><td>2856.20 (n/a)</td><td>2861.93 (n/a)</td><td>2833.56 (n/a)</td><td>12.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.44 (-2.56%)</td><td>6.85 (-0.86%)</td><td>6.80 (+1.00%)</td><td>6.45 (-0.44%)</td><td>0.37 (-17.60%)</td><td>1381.70 (+0.44%)</td><td>1304.98 (+0.78%)</td><td>1311.70 (-0.99%)</td><td>1197.40 (+2.62%)</td><td>67.64 (-14.99%)</td><td>448.36 (-2.56%)</td><td>412.32 (-0.86%)</td><td>409.30 (+1.00%)</td><td>388.55 (-0.44%)</td><td>22.16 (-17.60%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.64 (n/a)</td><td>6.90 (n/a)</td><td>6.73 (n/a)</td><td>6.48 (n/a)</td><td>0.45 (n/a)</td><td>1375.60 (n/a)</td><td>1294.94 (n/a)</td><td>1324.80 (n/a)</td><td>1166.80 (n/a)</td><td>79.56 (n/a)</td><td>460.13 (n/a)</td><td>415.91 (n/a)</td><td>405.23 (n/a)</td><td>390.28 (n/a)</td><td>26.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>6.86 (-0.75%)</td><td>6.46 (-0.13%)</td><td>6.78 (-0.18%)</td><td>5.06 (-4.73%)</td><td>0.78 (+17.15%)</td><td>1760.30 (+4.97%)</td><td>1399.52 (+0.57%)</td><td>1315.40 (+0.18%)</td><td>1299.00 (+0.75%)</td><td>201.82 <b>(+23.68%)</b></td><td>413.28 (-0.75%)</td><td>389.04 (-0.13%)</td><td>408.14 (-0.18%)</td><td>304.99 (-4.73%)</td><td>47.04 (+17.15%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>6.91 (n/a)</td><td>6.47 (n/a)</td><td>6.79 (n/a)</td><td>5.31 (n/a)</td><td>0.67 (n/a)</td><td>1677.00 (n/a)</td><td>1391.62 (n/a)</td><td>1313.00 (n/a)</td><td>1289.30 (n/a)</td><td>163.18 (n/a)</td><td>416.39 (n/a)</td><td>389.54 (n/a)</td><td>408.88 (n/a)</td><td>320.13 (n/a)</td><td>40.15 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.04 (-0.41%)</td><td>6.03 (-7.13%)</td><td>6.19 (-2.57%)</td><td>4.59 <b>(-25.13%)</b></td><td>0.89 <b>(+121.84%)</b></td><td>1939.80 <b>(+33.56%)</b></td><td>1507.34 (+9.53%)</td><td>1439.80 (+2.63%)</td><td>1265.30 (+0.42%)</td><td>255.13 <b>(+206.81%)</b></td><td>424.31 (-0.41%)</td><td>363.41 (-7.13%)</td><td>372.88 (-2.57%)</td><td>276.76 <b>(-25.13%)</b></td><td>53.88 <b>(+121.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.07 (n/a)</td><td>6.50 (n/a)</td><td>6.35 (n/a)</td><td>6.14 (n/a)</td><td>0.40 (n/a)</td><td>1452.40 (n/a)</td><td>1376.16 (n/a)</td><td>1402.90 (n/a)</td><td>1260.00 (n/a)</td><td>83.16 (n/a)</td><td>426.07 (n/a)</td><td>391.30 (n/a)</td><td>382.69 (n/a)</td><td>369.65 (n/a)</td><td>24.29 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.08 (-0.14%)</td><td>8.01 (+3.58%)</td><td>8.02 (+2.85%)</td><td>7.89 (+7.71%)</td><td>0.07 <b>(-79.58%)</b></td><td>4419.90 (-7.16%)</td><td>4353.46 (-3.62%)</td><td>4345.70 (-2.77%)</td><td>4312.40 (+0.14%)</td><td>39.87 <b>(-80.98%)</b></td><td>497.98 (-0.14%)</td><td>493.32 (+3.58%)</td><td>494.16 (+2.85%)</td><td>485.87 (+7.71%)</td><td>4.48 <b>(-79.58%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>8.10 (n/a)</td><td>7.73 (n/a)</td><td>7.80 (n/a)</td><td>7.32 (n/a)</td><td>0.36 (n/a)</td><td>4760.80 (n/a)</td><td>4516.76 (n/a)</td><td>4469.70 (n/a)</td><td>4306.30 (n/a)</td><td>209.64 (n/a)</td><td>498.68 (n/a)</td><td>476.26 (n/a)</td><td>480.46 (n/a)</td><td>451.07 (n/a)</td><td>21.94 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.89 (+3.65%)</td><td>7.51 (+0.60%)</td><td>7.62 (+0.33%)</td><td>6.74 (-4.00%)</td><td>0.45 <b>(+76.89%)</b></td><td>5174.10 (+4.17%)</td><td>4653.72 (-0.38%)</td><td>4577.30 (-0.33%)</td><td>4418.60 (-3.52%)</td><td>298.75 <b>(+79.66%)</b></td><td>486.01 (+3.65%)</td><td>462.88 (+0.60%)</td><td>469.16 (+0.33%)</td><td>415.05 (-4.00%)</td><td>27.69 <b>(+76.89%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.61 (n/a)</td><td>7.47 (n/a)</td><td>7.59 (n/a)</td><td>7.02 (n/a)</td><td>0.25 (n/a)</td><td>4967.20 (n/a)</td><td>4671.68 (n/a)</td><td>4592.30 (n/a)</td><td>4579.80 (n/a)</td><td>166.28 (n/a)</td><td>468.90 (n/a)</td><td>460.12 (n/a)</td><td>467.62 (n/a)</td><td>432.33 (n/a)</td><td>15.65 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.53 (+0.61%)</td><td>7.17 (-1.50%)</td><td>7.24 (-2.25%)</td><td>6.84 (-1.67%)</td><td>0.31 <b>(+31.37%)</b></td><td>5099.20 (+1.70%)</td><td>4873.00 (+1.59%)</td><td>4812.90 (+2.30%)</td><td>4629.50 (-0.61%)</td><td>213.48 <b>(+34.11%)</b></td><td>463.87 (+0.61%)</td><td>441.37 (-1.50%)</td><td>446.20 (-2.25%)</td><td>421.14 (-1.67%)</td><td>19.25 <b>(+31.37%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.49 (n/a)</td><td>7.27 (n/a)</td><td>7.41 (n/a)</td><td>6.95 (n/a)</td><td>0.24 (n/a)</td><td>5014.10 (n/a)</td><td>4796.78 (n/a)</td><td>4704.60 (n/a)</td><td>4657.70 (n/a)</td><td>159.19 (n/a)</td><td>461.06 (n/a)</td><td>448.08 (n/a)</td><td>456.46 (n/a)</td><td>428.29 (n/a)</td><td>14.65 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.80 (+0.02%)</td><td>0.80 (+0.03%)</td><td>0.80 (+0.04%)</td><td>0.80 (+0.08%)</td><td>0.00 <b>(-35.94%)</b></td><td>94145.60 (-0.08%)</td><td>94072.40 (-0.03%)</td><td>94061.90 (-0.04%)</td><td>94029.70 (-0.02%)</td><td>45.38 <b>(-36.00%)</b></td><td>730.83 (+0.02%)</td><td>730.50 (+0.03%)</td><td>730.58 (+0.04%)</td><td>729.93 (+0.08%)</td><td>0.35 <b>(-35.94%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94221.60 (n/a)</td><td>94104.32 (n/a)</td><td>94096.90 (n/a)</td><td>94046.20 (n/a)</td><td>70.91 (n/a)</td><td>730.70 (n/a)</td><td>730.25 (n/a)</td><td>730.31 (n/a)</td><td>729.34 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.74 (-0.37%)</td><td>0.74 (-0.04%)</td><td>0.74 (-0.03%)</td><td>0.74 (+0.13%)</td><td>0.00 <b>(-80.14%)</b></td><td>102681.90 (-0.13%)</td><td>102610.86 (+0.04%)</td><td>102616.80 (+0.03%)</td><td>102554.40 (+0.37%)</td><td>47.61 <b>(-80.09%)</b></td><td>670.08 (-0.37%)</td><td>669.71 (-0.04%)</td><td>669.67 (-0.03%)</td><td>669.25 (+0.13%)</td><td>0.31 <b>(-80.14%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102813.10 (n/a)</td><td>102566.84 (n/a)</td><td>102587.50 (n/a)</td><td>102173.60 (n/a)</td><td>239.13 (n/a)</td><td>672.58 (n/a)</td><td>670.00 (n/a)</td><td>669.86 (n/a)</td><td>668.39 (n/a)</td><td>1.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.71 (+0.05%)</td><td>0.71 (+0.00%)</td><td>0.71 (+0.10%)</td><td>0.71 (-0.32%)</td><td>0.00 <b>(+332.53%)</b></td><td>106350.70 (+0.32%)</td><td>105972.72 (-0.00%)</td><td>105887.70 (-0.10%)</td><td>105838.30 (-0.05%)</td><td>212.63 <b>(+333.70%)</b></td><td>649.29 (+0.05%)</td><td>648.47 (+0.00%)</td><td>648.98 (+0.10%)</td><td>646.16 (-0.32%)</td><td>1.30 <b>(+332.53%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106015.00 (n/a)</td><td>105977.22 (n/a)</td><td>105989.60 (n/a)</td><td>105896.00 (n/a)</td><td>49.03 (n/a)</td><td>648.93 (n/a)</td><td>648.44 (n/a)</td><td>648.36 (n/a)</td><td>648.21 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.85 (-10.88%)</td><td>3.30 (-12.51%)</td><td>3.14 (-15.15%)</td><td>2.97 (-9.33%)</td><td>0.39 (+0.48%)</td><td>2716.10 (+10.29%)</td><td>2471.42 (+14.55%)</td><td>2570.40 (+17.85%)</td><td>2095.80 (+12.21%)</td><td>277.92 <b>(+26.03%)</b></td><td>1008.63 (-10.88%)</td><td>864.51 (-12.51%)</td><td>822.41 (-15.15%)</td><td>778.28 (-9.33%)</td><td>102.09 (+0.48%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.32 (n/a)</td><td>3.77 (n/a)</td><td>3.70 (n/a)</td><td>3.27 (n/a)</td><td>0.39 (n/a)</td><td>2462.80 (n/a)</td><td>2157.44 (n/a)</td><td>2181.00 (n/a)</td><td>1867.80 (n/a)</td><td>220.52 (n/a)</td><td>1131.76 (n/a)</td><td>988.10 (n/a)</td><td>969.24 (n/a)</td><td>858.34 (n/a)</td><td>101.60 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.50 (-5.97%)</td><td>0.40 (+9.66%)</td><td>0.37 (+11.08%)</td><td>0.30 (-0.44%)</td><td>0.08 (-9.88%)</td><td>4179.50 (+0.44%)</td><td>3254.68 (-9.28%)</td><td>3390.70 (-9.97%)</td><td>2505.10 (+6.35%)</td><td>693.60 (-2.48%)</td><td>26.79 (-5.97%)</td><td>21.39 (+9.66%)</td><td>19.79 (+11.08%)</td><td>16.06 (-0.44%)</td><td>4.58 (-9.88%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.53 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.09 (n/a)</td><td>4161.00 (n/a)</td><td>3587.54 (n/a)</td><td>3766.30 (n/a)</td><td>2355.50 (n/a)</td><td>711.21 (n/a)</td><td>28.49 (n/a)</td><td>19.51 (n/a)</td><td>17.82 (n/a)</td><td>16.13 (n/a)</td><td>5.08 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.11 (-7.91%)</td><td>4.45 (-4.78%)</td><td>4.78 (+2.21%)</td><td>3.55 (+1.19%)</td><td>0.70 (-6.03%)</td><td>1874.90 (-1.18%)</td><td>1527.30 (+4.83%)</td><td>1390.30 (-2.17%)</td><td>1301.70 (+8.59%)</td><td>255.91 (-2.60%)</td><td>1578.92 (-7.91%)</td><td>1374.52 (-4.78%)</td><td>1478.21 (+2.21%)</td><td>1096.15 (+1.19%)</td><td>215.91 (-6.03%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.55 (n/a)</td><td>4.67 (n/a)</td><td>4.68 (n/a)</td><td>3.51 (n/a)</td><td>0.74 (n/a)</td><td>1897.20 (n/a)</td><td>1456.92 (n/a)</td><td>1421.10 (n/a)</td><td>1198.70 (n/a)</td><td>262.75 (n/a)</td><td>1714.56 (n/a)</td><td>1443.48 (n/a)</td><td>1446.24 (n/a)</td><td>1083.28 (n/a)</td><td>229.77 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.43 (n/a)</td><td>12.77 (n/a)</td><td>13.24 (n/a)</td><td>10.94 (n/a)</td><td>1.03 (n/a)</td><td>13.42 (n/a)</td><td>12.76 (n/a)</td><td>13.23 (n/a)</td><td>10.94 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>24.46 (-0.57%)</td><td>23.08 (-2.83%)</td><td>23.87 (+1.71%)</td><td>19.88 (-13.81%)</td><td>1.88 <b>(+174.64%)</b></td><td>24.44 (-0.57%)</td><td>23.07 (-2.83%)</td><td>23.86 (+1.71%)</td><td>19.87 (-13.81%)</td><td>1.88 <b>(+174.64%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>24.60 (n/a)</td><td>23.75 (n/a)</td><td>23.47 (n/a)</td><td>23.07 (n/a)</td><td>0.69 (n/a)</td><td>24.58 (n/a)</td><td>23.74 (n/a)</td><td>23.45 (n/a)</td><td>23.05 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>42.71 (+2.09%)</td><td>40.71 (+1.93%)</td><td>40.80 (+0.50%)</td><td>38.57 (+8.92%)</td><td>1.63 <b>(-37.06%)</b></td><td>42.69 (+2.09%)</td><td>40.68 (+1.93%)</td><td>40.78 (+0.50%)</td><td>38.55 (+8.92%)</td><td>1.63 <b>(-37.06%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>41.84 (n/a)</td><td>39.94 (n/a)</td><td>40.60 (n/a)</td><td>35.41 (n/a)</td><td>2.59 (n/a)</td><td>41.81 (n/a)</td><td>39.91 (n/a)</td><td>40.58 (n/a)</td><td>35.39 (n/a)</td><td>2.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>44.72 (+3.91%)</td><td>43.24 (+7.15%)</td><td>42.61 (+5.67%)</td><td>42.37 (+13.62%)</td><td>1.07 <b>(-51.50%)</b></td><td>44.69 (+3.91%)</td><td>43.21 (+7.15%)</td><td>42.59 (+5.67%)</td><td>42.34 (+13.62%)</td><td>1.07 <b>(-51.50%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>43.04 (n/a)</td><td>40.35 (n/a)</td><td>40.33 (n/a)</td><td>37.29 (n/a)</td><td>2.20 (n/a)</td><td>43.01 (n/a)</td><td>40.33 (n/a)</td><td>40.30 (n/a)</td><td>37.27 (n/a)</td><td>2.20 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.27 (n/a)</td><td>12.55 (n/a)</td><td>12.79 (n/a)</td><td>11.06 (n/a)</td><td>0.89 (n/a)</td><td>13.27 (n/a)</td><td>12.54 (n/a)</td><td>12.78 (n/a)</td><td>11.05 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>24.76 (-0.81%)</td><td>24.30 (-0.06%)</td><td>24.16 (-0.32%)</td><td>24.06 (+2.21%)</td><td>0.29 <b>(-44.15%)</b></td><td>24.75 (-0.81%)</td><td>24.28 (-0.06%)</td><td>24.15 (-0.32%)</td><td>24.05 (+2.21%)</td><td>0.29 <b>(-44.15%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>24.96 (n/a)</td><td>24.31 (n/a)</td><td>24.24 (n/a)</td><td>23.54 (n/a)</td><td>0.53 (n/a)</td><td>24.95 (n/a)</td><td>24.30 (n/a)</td><td>24.23 (n/a)</td><td>23.53 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>39.63 (-3.57%)</td><td>37.58 (-2.09%)</td><td>38.53 (+0.27%)</td><td>32.42 (-10.21%)</td><td>2.94 <b>(+60.71%)</b></td><td>39.60 (-3.57%)</td><td>37.56 (-2.09%)</td><td>38.51 (+0.27%)</td><td>32.40 (-10.21%)</td><td>2.94 <b>(+60.71%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>41.09 (n/a)</td><td>38.38 (n/a)</td><td>38.43 (n/a)</td><td>36.10 (n/a)</td><td>1.83 (n/a)</td><td>41.07 (n/a)</td><td>38.36 (n/a)</td><td>38.40 (n/a)</td><td>36.08 (n/a)</td><td>1.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>43.67 (-3.80%)</td><td>42.55 (-2.30%)</td><td>42.53 (-4.26%)</td><td>41.02 (-0.73%)</td><td>1.05 <b>(-44.90%)</b></td><td>43.64 (-3.80%)</td><td>42.52 (-2.30%)</td><td>42.50 (-4.26%)</td><td>40.99 (-0.73%)</td><td>1.05 <b>(-44.90%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>45.39 (n/a)</td><td>43.55 (n/a)</td><td>44.42 (n/a)</td><td>41.32 (n/a)</td><td>1.90 (n/a)</td><td>45.36 (n/a)</td><td>43.53 (n/a)</td><td>44.39 (n/a)</td><td>41.29 (n/a)</td><td>1.90 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>9.33 (-3.53%)</td><td>9.08 (+1.28%)</td><td>9.06 (+1.26%)</td><td>8.78 (+7.98%)</td><td>0.23 <b>(-59.16%)</b></td><td>9.31 (-3.53%)</td><td>9.06 (+1.28%)</td><td>9.04 (+1.26%)</td><td>8.76 (+7.98%)</td><td>0.23 <b>(-59.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.67 (n/a)</td><td>8.96 (n/a)</td><td>8.95 (n/a)</td><td>8.13 (n/a)</td><td>0.55 (n/a)</td><td>9.65 (n/a)</td><td>8.95 (n/a)</td><td>8.93 (n/a)</td><td>8.12 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.89 (-13.46%)</td><td>0.85 (-7.26%)</td><td>0.84 (-9.26%)</td><td>0.81 (+4.58%)</td><td>0.03 <b>(-67.31%)</b></td><td>0.88 (-13.46%)</td><td>0.84 (-7.26%)</td><td>0.83 (-9.26%)</td><td>0.80 (+4.58%)</td><td>0.03 <b>(-67.31%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.03 (n/a)</td><td>0.92 (n/a)</td><td>0.93 (n/a)</td><td>0.77 (n/a)</td><td>0.09 (n/a)</td><td>1.01 (n/a)</td><td>0.90 (n/a)</td><td>0.91 (n/a)</td><td>0.76 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.39 (+5.04%)</td><td>1.24 (+9.10%)</td><td>1.32 (+17.16%)</td><td>0.91 (-3.68%)</td><td>0.20 <b>(+22.00%)</b></td><td>1.37 (+5.04%)</td><td>1.23 (+9.10%)</td><td>1.31 (+17.16%)</td><td>0.90 (-3.68%)</td><td>0.20 <b>(+22.00%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.32 (n/a)</td><td>1.14 (n/a)</td><td>1.13 (n/a)</td><td>0.94 (n/a)</td><td>0.16 (n/a)</td><td>1.30 (n/a)</td><td>1.12 (n/a)</td><td>1.11 (n/a)</td><td>0.93 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>17.32 (-8.33%)</td><td>16.69 (-3.77%)</td><td>16.65 (-7.52%)</td><td>16.07 (+6.39%)</td><td>0.52 <b>(-70.25%)</b></td><td>17.12 (-8.33%)</td><td>16.50 (-3.77%)</td><td>16.46 (-7.52%)</td><td>15.88 (+6.39%)</td><td>0.51 <b>(-70.25%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>18.89 (n/a)</td><td>17.34 (n/a)</td><td>18.01 (n/a)</td><td>15.10 (n/a)</td><td>1.74 (n/a)</td><td>18.67 (n/a)</td><td>17.14 (n/a)</td><td>17.80 (n/a)</td><td>14.93 (n/a)</td><td>1.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.72 (-2.92%)</td><td>13.50 (+2.16%)</td><td>13.50 (+1.40%)</td><td>13.26 (+9.63%)</td><td>0.19 <b>(-73.65%)</b></td><td>13.48 (-2.92%)</td><td>13.27 (+2.16%)</td><td>13.26 (+1.40%)</td><td>13.03 (+9.63%)</td><td>0.19 <b>(-73.65%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>14.14 (n/a)</td><td>13.22 (n/a)</td><td>13.31 (n/a)</td><td>12.10 (n/a)</td><td>0.74 (n/a)</td><td>13.89 (n/a)</td><td>12.98 (n/a)</td><td>13.08 (n/a)</td><td>11.88 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.74 (-16.01%)</td><td>7.83 (-6.57%)</td><td>7.70 (-2.06%)</td><td>7.18 (-6.08%)</td><td>0.57 <b>(-50.27%)</b></td><td>8.59 (-16.01%)</td><td>7.70 (-6.57%)</td><td>7.57 (-2.06%)</td><td>7.06 (-6.08%)</td><td>0.56 <b>(-50.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>10.40 (n/a)</td><td>8.38 (n/a)</td><td>7.86 (n/a)</td><td>7.65 (n/a)</td><td>1.15 (n/a)</td><td>10.22 (n/a)</td><td>8.24 (n/a)</td><td>7.73 (n/a)</td><td>7.51 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>6.88 (+13.30%)</td><td>5.67 (-0.28%)</td><td>5.80 (-1.55%)</td><td>4.48 (-11.87%)</td><td>0.88 <b>(+112.98%)</b></td><td>6.77 (+13.30%)</td><td>5.58 (-0.28%)</td><td>5.71 (-1.55%)</td><td>4.41 (-11.87%)</td><td>0.87 <b>(+112.98%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>6.07 (n/a)</td><td>5.68 (n/a)</td><td>5.90 (n/a)</td><td>5.09 (n/a)</td><td>0.41 (n/a)</td><td>5.97 (n/a)</td><td>5.59 (n/a)</td><td>5.80 (n/a)</td><td>5.01 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.24 (n/a)</td><td>12.03 (n/a)</td><td>11.97 (n/a)</td><td>10.51 (n/a)</td><td>1.03 (n/a)</td><td>13.23 (n/a)</td><td>12.02 (n/a)</td><td>11.96 (n/a)</td><td>10.50 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.27 (n/a)</td><td>12.06 (n/a)</td><td>11.89 (n/a)</td><td>10.79 (n/a)</td><td>1.03 (n/a)</td><td>13.26 (n/a)</td><td>12.06 (n/a)</td><td>11.88 (n/a)</td><td>10.78 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.50 (n/a)</td><td>177.84 (n/a)</td><td>171.50 (n/a)</td><td>130.80 (n/a)</td><td>36.14 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>155.20 (n/a)</td><td>139.26 (n/a)</td><td>151.40 (n/a)</td><td>110.50 (n/a)</td><td>20.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.70 (n/a)</td><td>147.20 (n/a)</td><td>151.20 (n/a)</td><td>127.70 (n/a)</td><td>18.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.90 (n/a)</td><td>175.26 (n/a)</td><td>157.70 (n/a)</td><td>147.10 (n/a)</td><td>33.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.90 (n/a)</td><td>180.00 (n/a)</td><td>187.40 (n/a)</td><td>143.10 (n/a)</td><td>21.65 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.30 (n/a)</td><td>162.72 (n/a)</td><td>151.80 (n/a)</td><td>128.30 (n/a)</td><td>31.20 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.40 (n/a)</td><td>203.08 (n/a)</td><td>206.10 (n/a)</td><td>172.70 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>344.90 (n/a)</td><td>230.74 (n/a)</td><td>216.10 (n/a)</td><td>167.90 (n/a)</td><td>67.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.70 (n/a)</td><td>155.12 (n/a)</td><td>149.10 (n/a)</td><td>123.00 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>176.56 (n/a)</td><td>172.30 (n/a)</td><td>148.20 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.10 (n/a)</td><td>173.56 (n/a)</td><td>163.30 (n/a)</td><td>149.50 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>170.76 (n/a)</td><td>169.60 (n/a)</td><td>150.20 (n/a)</td><td>20.36 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>158.82 (n/a)</td><td>163.90 (n/a)</td><td>128.40 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.70 (n/a)</td><td>171.82 (n/a)</td><td>183.40 (n/a)</td><td>127.40 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.20 (n/a)</td><td>181.98 (n/a)</td><td>187.00 (n/a)</td><td>124.00 (n/a)</td><td>46.46 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>339.60 (n/a)</td><td>213.78 (n/a)</td><td>169.40 (n/a)</td><td>159.30 (n/a)</td><td>77.01 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>160.66 (n/a)</td><td>152.90 (n/a)</td><td>144.00 (n/a)</td><td>19.88 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>228.20 (n/a)</td><td>189.28 (n/a)</td><td>198.70 (n/a)</td><td>149.60 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>212.70 (n/a)</td><td>150.76 (n/a)</td><td>144.10 (n/a)</td><td>100.20 (n/a)</td><td>46.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>240.00 (n/a)</td><td>172.34 (n/a)</td><td>176.90 (n/a)</td><td>110.30 (n/a)</td><td>48.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>176.90 (n/a)</td><td>136.12 (n/a)</td><td>137.10 (n/a)</td><td>103.20 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>228.70 (n/a)</td><td>173.94 (n/a)</td><td>147.50 (n/a)</td><td>144.00 (n/a)</td><td>39.74 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.50 (n/a)</td><td>195.86 (n/a)</td><td>208.20 (n/a)</td><td>124.80 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>344.50 (n/a)</td><td>255.56 (n/a)</td><td>231.70 (n/a)</td><td>219.40 (n/a)</td><td>52.23 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>362.10 (n/a)</td><td>226.66 (n/a)</td><td>193.60 (n/a)</td><td>183.50 (n/a)</td><td>76.02 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>192.94 (n/a)</td><td>191.20 (n/a)</td><td>174.70 (n/a)</td><td>17.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>311.30 (n/a)</td><td>197.14 (n/a)</td><td>179.60 (n/a)</td><td>146.30 (n/a)</td><td>66.48 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>233.10 (n/a)</td><td>196.36 (n/a)</td><td>187.70 (n/a)</td><td>176.00 (n/a)</td><td>22.31 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>237.90 (n/a)</td><td>174.16 (n/a)</td><td>167.60 (n/a)</td><td>137.40 (n/a)</td><td>38.20 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>242.80 (n/a)</td><td>194.64 (n/a)</td><td>190.40 (n/a)</td><td>138.00 (n/a)</td><td>40.99 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>192.60 (n/a)</td><td>176.02 (n/a)</td><td>176.80 (n/a)</td><td>159.60 (n/a)</td><td>15.66 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>335.30 (n/a)</td><td>258.66 (n/a)</td><td>272.60 (n/a)</td><td>191.50 (n/a)</td><td>56.26 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (+0.00%)</td><td>0.03 (-3.12%)</td><td>0.02 (-8.39%)</td><td>0.02 (+11.13%)</td><td>0.00 <b>(-28.80%)</b></td><td>178.50 (-10.03%)</td><td>165.40 (+1.86%)</td><td>173.80 (+9.17%)</td><td>134.20 (+0.00%)</td><td>18.59 <b>(-35.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.40 (n/a)</td><td>162.38 (n/a)</td><td>159.20 (n/a)</td><td>134.20 (n/a)</td><td>28.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-6.06%)</td><td>0.03 (-3.94%)</td><td>0.02 (-13.73%)</td><td>0.02 <b>(+28.26%)</b></td><td>0.00 <b>(-50.24%)</b></td><td>177.40 <b>(-22.06%)</b></td><td>158.52 (+0.09%)</td><td>166.10 (+15.91%)</td><td>132.70 (+6.42%)</td><td>17.58 <b>(-58.78%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.60 (n/a)</td><td>158.38 (n/a)</td><td>143.30 (n/a)</td><td>124.70 (n/a)</td><td>42.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+19.31%)</td><td>0.03 (+14.81%)</td><td>0.03 (+8.51%)</td><td>0.03 (+19.07%)</td><td>0.00 (+16.86%)</td><td>157.80 (-16.02%)</td><td>137.02 (-12.97%)</td><td>137.30 (-7.85%)</td><td>114.60 (-16.23%)</td><td>16.05 (-19.12%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>157.44 (n/a)</td><td>149.00 (n/a)</td><td>136.80 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-2.78%)</td><td>0.03 (-11.20%)</td><td>0.03 (-2.60%)</td><td>0.01 <b>(-40.42%)</b></td><td>0.01 <b>(+70.27%)</b></td><td>289.70 <b>(+67.84%)</b></td><td>177.68 <b>(+21.07%)</b></td><td>146.70 (+2.66%)</td><td>127.10 (+2.83%)</td><td>67.49 <b>(+194.13%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.60 (n/a)</td><td>146.76 (n/a)</td><td>142.90 (n/a)</td><td>123.60 (n/a)</td><td>22.94 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+7.92%)</td><td>0.03 <b>(+24.25%)</b></td><td>0.03 <b>(+21.59%)</b></td><td>0.02 <b>(+35.86%)</b></td><td>0.01 <b>(-20.12%)</b></td><td>200.00 <b>(-26.42%)</b></td><td>145.94 <b>(-23.76%)</b></td><td>132.00 (-17.76%)</td><td>112.50 (-7.33%)</td><td>34.92 <b>(-47.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>271.80 (n/a)</td><td>191.42 (n/a)</td><td>160.50 (n/a)</td><td>121.40 (n/a)</td><td>66.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (+17.95%)</td><td>0.03 (+15.23%)</td><td>0.02 (+10.64%)</td><td>0.02 (+11.93%)</td><td>0.00 <b>(+48.82%)</b></td><td>193.90 (-10.65%)</td><td>160.34 (-12.46%)</td><td>164.50 (-9.62%)</td><td>129.90 (-15.21%)</td><td>26.44 (+11.13%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.00 (n/a)</td><td>183.16 (n/a)</td><td>182.00 (n/a)</td><td>153.20 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (+15.24%)</td><td>0.03 (+10.16%)</td><td>0.02 (-6.72%)</td><td>0.02 <b>(+50.11%)</b></td><td>0.00 (-19.29%)</td><td>171.10 <b>(-33.40%)</b></td><td>152.38 (-11.93%)</td><td>164.60 (+7.23%)</td><td>121.30 (-13.23%)</td><td>22.01 <b>(-54.32%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>256.90 (n/a)</td><td>173.02 (n/a)</td><td>153.50 (n/a)</td><td>139.80 (n/a)</td><td>48.17 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (-2.71%)</td><td>0.02 (+6.70%)</td><td>0.02 (+6.61%)</td><td>0.02 <b>(+29.96%)</b></td><td>0.00 <b>(-47.23%)</b></td><td>211.20 <b>(-23.03%)</b></td><td>191.42 (-8.05%)</td><td>182.20 (-6.18%)</td><td>176.50 (+2.80%)</td><td>15.86 <b>(-59.49%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>274.40 (n/a)</td><td>208.18 (n/a)</td><td>194.20 (n/a)</td><td>171.70 (n/a)</td><td>39.15 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-6.80%)</td><td>0.05 (-5.02%)</td><td>0.05 (-0.84%)</td><td>0.04 (+3.23%)</td><td>0.01 <b>(-31.30%)</b></td><td>191.70 (-3.13%)</td><td>167.10 (+3.30%)</td><td>163.40 (+0.80%)</td><td>131.10 (+7.28%)</td><td>24.08 <b>(-29.57%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>161.76 (n/a)</td><td>162.10 (n/a)</td><td>122.20 (n/a)</td><td>34.19 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (+10.85%)</td><td>0.06 (+9.97%)</td><td>0.05 (+3.34%)</td><td>0.04 (+10.80%)</td><td>0.01 (+12.93%)</td><td>182.30 (-9.75%)</td><td>149.72 (-9.01%)</td><td>156.60 (-3.21%)</td><td>116.80 (-9.81%)</td><td>26.28 (-9.35%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>164.54 (n/a)</td><td>161.80 (n/a)</td><td>129.50 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 (+17.81%)</td><td>0.06 (-0.69%)</td><td>0.05 (-6.38%)</td><td>0.04 (-11.47%)</td><td>0.01 <b>(+98.93%)</b></td><td>191.30 (+12.93%)</td><td>149.96 (+3.45%)</td><td>154.80 (+6.83%)</td><td>108.90 (-15.12%)</td><td>31.42 <b>(+89.77%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.40 (n/a)</td><td>144.96 (n/a)</td><td>144.90 (n/a)</td><td>128.30 (n/a)</td><td>16.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-9.65%)</td><td>0.06 (+12.80%)</td><td>0.06 (+9.55%)</td><td>0.05 <b>(+85.19%)</b></td><td>0.01 <b>(-68.84%)</b></td><td>173.80 <b>(-45.99%)</b></td><td>147.72 <b>(-20.89%)</b></td><td>145.10 (-8.74%)</td><td>134.80 (+10.67%)</td><td>15.32 <b>(-81.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>321.80 (n/a)</td><td>186.72 (n/a)</td><td>159.00 (n/a)</td><td>121.80 (n/a)</td><td>81.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-4.60%)</td><td>0.06 (+4.58%)</td><td>0.06 (+13.01%)</td><td>0.05 (+12.39%)</td><td>0.01 <b>(-37.55%)</b></td><td>172.80 (-11.02%)</td><td>142.82 (-5.98%)</td><td>138.70 (-11.54%)</td><td>128.20 (+4.82%)</td><td>17.34 <b>(-39.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.20 (n/a)</td><td>151.90 (n/a)</td><td>156.80 (n/a)</td><td>122.30 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-5.89%)</td><td>0.05 (-1.86%)</td><td>0.05 (-17.28%)</td><td>0.05 (+16.04%)</td><td>0.01 <b>(-32.93%)</b></td><td>175.70 (-13.79%)</td><td>153.44 (-0.47%)</td><td>164.30 <b>(+20.90%)</b></td><td>127.50 (+6.25%)</td><td>21.41 <b>(-39.85%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>154.16 (n/a)</td><td>135.90 (n/a)</td><td>120.00 (n/a)</td><td>35.60 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-13.32%)</td><td>0.05 (-5.35%)</td><td>0.05 (-8.86%)</td><td>0.05 <b>(+22.01%)</b></td><td>0.01 <b>(-56.16%)</b></td><td>177.60 (-18.04%)</td><td>158.02 (+1.70%)</td><td>154.00 (+9.76%)</td><td>136.50 (+15.38%)</td><td>16.43 <b>(-58.63%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>155.38 (n/a)</td><td>140.30 (n/a)</td><td>118.30 (n/a)</td><td>39.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-6.28%)</td><td>0.05 (-3.39%)</td><td>0.05 (-9.97%)</td><td>0.04 (+4.44%)</td><td>0.01 (-19.61%)</td><td>189.90 (-4.24%)</td><td>165.12 (+2.43%)</td><td>171.60 (+11.07%)</td><td>138.20 (+6.72%)</td><td>25.43 (-19.38%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>161.20 (n/a)</td><td>154.50 (n/a)</td><td>129.50 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-0.11%)</td><td>0.05 (+7.23%)</td><td>0.05 (+6.60%)</td><td>0.05 (+15.18%)</td><td>0.00 <b>(-46.68%)</b></td><td>177.20 (-13.18%)</td><td>167.56 (-7.35%)</td><td>169.90 (-6.18%)</td><td>154.90 (+0.13%)</td><td>8.65 <b>(-53.71%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>180.86 (n/a)</td><td>181.10 (n/a)</td><td>154.70 (n/a)</td><td>18.69 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (-10.18%)</td><td>0.04 (-8.03%)</td><td>0.04 (-3.35%)</td><td>0.03 (-19.41%)</td><td>0.01 <b>(+20.26%)</b></td><td>289.60 <b>(+24.08%)</b></td><td>227.00 (+9.75%)</td><td>213.10 (+3.45%)</td><td>195.20 (+11.35%)</td><td>36.51 <b>(+74.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.40 (n/a)</td><td>206.84 (n/a)</td><td>206.00 (n/a)</td><td>175.30 (n/a)</td><td>20.97 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 <b>(-27.54%)</b></td><td>0.09 (-9.64%)</td><td>0.09 (-1.71%)</td><td>0.08 (-2.94%)</td><td>0.01 <b>(-55.94%)</b></td><td>214.00 (+3.03%)</td><td>187.92 (+8.24%)</td><td>179.50 (+1.76%)</td><td>169.60 <b>(+38.00%)</b></td><td>20.46 <b>(-35.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.70 (n/a)</td><td>173.62 (n/a)</td><td>176.40 (n/a)</td><td>122.90 (n/a)</td><td>31.53 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (-6.05%)</td><td>0.10 (+1.70%)</td><td>0.10 (-0.24%)</td><td>0.07 (+7.82%)</td><td>0.02 (-15.84%)</td><td>224.10 (-7.24%)</td><td>163.50 (-3.08%)</td><td>160.00 (+0.19%)</td><td>129.30 (+6.51%)</td><td>36.65 (-17.71%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>241.60 (n/a)</td><td>168.70 (n/a)</td><td>159.70 (n/a)</td><td>121.40 (n/a)</td><td>44.54 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (+5.93%)</td><td>0.10 (-4.06%)</td><td>0.09 (-8.31%)</td><td>0.08 (+5.18%)</td><td>0.02 (+8.12%)</td><td>207.20 (-4.95%)</td><td>176.86 (+4.26%)</td><td>180.30 (+9.07%)</td><td>122.70 (-5.62%)</td><td>32.32 (-6.94%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>218.00 (n/a)</td><td>169.64 (n/a)</td><td>165.30 (n/a)</td><td>130.00 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (-10.16%)</td><td>0.09 (-7.60%)</td><td>0.09 (-3.66%)</td><td>0.06 (-16.13%)</td><td>0.02 (-3.36%)</td><td>255.30 (+19.19%)</td><td>188.02 (+9.11%)</td><td>173.50 (+3.77%)</td><td>140.90 (+11.30%)</td><td>43.49 <b>(+31.63%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.20 (n/a)</td><td>172.32 (n/a)</td><td>167.20 (n/a)</td><td>126.60 (n/a)</td><td>33.04 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (+8.66%)</td><td>0.10 (-0.25%)</td><td>0.10 (-1.92%)</td><td>0.08 (-6.45%)</td><td>0.01 <b>(+76.26%)</b></td><td>194.90 (+6.85%)</td><td>169.70 (+1.23%)</td><td>171.90 (+1.96%)</td><td>136.00 (-7.98%)</td><td>21.92 <b>(+72.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>167.64 (n/a)</td><td>168.60 (n/a)</td><td>147.80 (n/a)</td><td>12.73 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (-10.43%)</td><td>0.09 (-11.93%)</td><td>0.08 (-19.62%)</td><td>0.07 (-15.55%)</td><td>0.01 (+2.42%)</td><td>229.60 (+18.41%)</td><td>190.00 (+14.03%)</td><td>193.10 <b>(+24.42%)</b></td><td>162.70 (+11.67%)</td><td>27.82 <b>(+30.85%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>166.62 (n/a)</td><td>155.20 (n/a)</td><td>145.70 (n/a)</td><td>21.26 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 <b>(+29.55%)</b></td><td>0.10 <b>(+22.66%)</b></td><td>0.09 (+1.66%)</td><td>0.09 <b>(+65.37%)</b></td><td>0.02 (+8.92%)</td><td>189.80 <b>(-39.52%)</b></td><td>169.24 <b>(-20.38%)</b></td><td>187.20 (-1.63%)</td><td>122.20 <b>(-22.85%)</b></td><td>29.42 <b>(-50.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>313.80 (n/a)</td><td>212.56 (n/a)</td><td>190.30 (n/a)</td><td>158.40 (n/a)</td><td>59.88 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (+2.57%)</td><td>0.09 (+4.20%)</td><td>0.09 (+7.59%)</td><td>0.08 (+5.29%)</td><td>0.01 (-15.92%)</td><td>214.20 (-5.01%)</td><td>189.22 (-4.44%)</td><td>182.80 (-7.02%)</td><td>166.70 (-2.46%)</td><td>20.23 <b>(-21.71%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>198.02 (n/a)</td><td>196.60 (n/a)</td><td>170.90 (n/a)</td><td>25.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (+4.81%)</td><td>0.21 (+6.42%)</td><td>0.19 (+7.95%)</td><td>0.18 <b>(+20.87%)</b></td><td>0.04 <b>(-20.67%)</b></td><td>183.20 (-17.29%)</td><td>157.48 (-8.06%)</td><td>168.60 (-7.36%)</td><td>123.60 (-4.63%)</td><td>26.75 <b>(-33.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>221.50 (n/a)</td><td>171.28 (n/a)</td><td>182.00 (n/a)</td><td>129.60 (n/a)</td><td>40.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (+10.37%)</td><td>0.22 (+7.19%)</td><td>0.25 (+5.46%)</td><td>0.16 (+9.50%)</td><td>0.05 (+10.86%)</td><td>202.80 (-8.69%)</td><td>153.94 (-6.51%)</td><td>130.90 (-5.21%)</td><td>116.40 (-9.35%)</td><td>40.02 (-5.68%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>222.10 (n/a)</td><td>164.66 (n/a)</td><td>138.10 (n/a)</td><td>128.40 (n/a)</td><td>42.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (-9.01%)</td><td>0.22 (+3.54%)</td><td>0.22 (+3.78%)</td><td>0.20 (+8.82%)</td><td>0.02 <b>(-52.82%)</b></td><td>166.40 (-8.12%)</td><td>147.86 (-4.83%)</td><td>146.00 (-3.69%)</td><td>136.30 (+9.83%)</td><td>11.14 <b>(-52.12%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>181.10 (n/a)</td><td>155.36 (n/a)</td><td>151.60 (n/a)</td><td>124.10 (n/a)</td><td>23.27 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (-2.87%)</td><td>0.20 (+0.04%)</td><td>0.20 (-3.81%)</td><td>0.19 (+10.32%)</td><td>0.01 <b>(-48.27%)</b></td><td>174.60 (-9.35%)</td><td>163.14 (-0.66%)</td><td>164.70 (+3.98%)</td><td>155.00 (+2.92%)</td><td>8.22 <b>(-52.24%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>192.60 (n/a)</td><td>164.22 (n/a)</td><td>158.40 (n/a)</td><td>150.60 (n/a)</td><td>17.21 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (+1.89%)</td><td>0.20 (+4.25%)</td><td>0.20 (+12.20%)</td><td>0.18 (+5.02%)</td><td>0.02 <b>(-29.90%)</b></td><td>179.00 (-4.79%)</td><td>163.20 (-4.64%)</td><td>163.80 (-10.88%)</td><td>144.70 (-1.83%)</td><td>12.66 <b>(-35.06%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.00 (n/a)</td><td>171.14 (n/a)</td><td>183.80 (n/a)</td><td>147.40 (n/a)</td><td>19.50 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (-5.85%)</td><td>0.21 (-1.98%)</td><td>0.21 (-0.18%)</td><td>0.16 (-6.33%)</td><td>0.03 (-0.73%)</td><td>209.50 (+6.78%)</td><td>160.96 (+2.31%)</td><td>153.90 (+0.20%)</td><td>137.00 (+6.28%)</td><td>28.07 (+14.89%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.20 (n/a)</td><td>157.32 (n/a)</td><td>153.60 (n/a)</td><td>128.90 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (-8.58%)</td><td>0.16 (-6.25%)</td><td>0.18 (+0.84%)</td><td>0.10 <b>(-30.22%)</b></td><td>0.04 <b>(+37.16%)</b></td><td>339.30 <b>(+43.29%)</b></td><td>212.82 (+11.61%)</td><td>185.50 (-0.86%)</td><td>165.20 (+9.40%)</td><td>72.00 <b>(+123.43%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.80 (n/a)</td><td>190.68 (n/a)</td><td>187.10 (n/a)</td><td>151.00 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (-15.49%)</td><td>0.03 (-16.76%)</td><td>0.02 <b>(-20.90%)</b></td><td>0.02 (-9.10%)</td><td>0.01 (-17.86%)</td><td>227.40 (+10.01%)</td><td>170.68 (+19.26%)</td><td>165.30 <b>(+26.47%)</b></td><td>117.00 (+18.30%)</td><td>46.11 (+7.05%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>143.12 (n/a)</td><td>130.70 (n/a)</td><td>98.90 (n/a)</td><td>43.07 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+0.80%)</td><td>0.03 (-5.22%)</td><td>0.03 (+3.55%)</td><td>0.02 <b>(-23.65%)</b></td><td>0.01 <b>(+56.68%)</b></td><td>208.90 <b>(+30.97%)</b></td><td>153.42 (+10.23%)</td><td>141.50 (-3.41%)</td><td>107.20 (-0.83%)</td><td>43.70 <b>(+107.06%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>159.50 (n/a)</td><td>139.18 (n/a)</td><td>146.50 (n/a)</td><td>108.10 (n/a)</td><td>21.10 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.00 (+0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 (-0.01%)</td><td>0.00 (n/a)</td><td>4745965.30 (+0.01%)</td><td>4745778.00 (+0.00%)</td><td>4745778.00 (+0.00%)</td><td>4745590.70 (-0.00%)</td><td>264.88 (n/a)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4745612.50 (n/a)</td><td>4745612.50 (n/a)</td><td>4745612.50 (n/a)</td><td>4745612.50 (n/a)</td><td>0.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (-13.19%)</td><td>0.02 (-7.30%)</td><td>0.02 (-16.65%)</td><td>0.02 (+18.46%)</td><td>0.00 <b>(-61.07%)</b></td><td>226.70 (-15.57%)</td><td>210.08 (+4.52%)</td><td>209.40 <b>(+20.00%)</b></td><td>185.00 (+15.19%)</td><td>17.39 <b>(-61.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>268.50 (n/a)</td><td>201.00 (n/a)</td><td>174.50 (n/a)</td><td>160.60 (n/a)</td><td>45.54 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-14.44%)</td><td>0.02 <b>(-24.61%)</b></td><td>0.02 <b>(-34.58%)</b></td><td>0.02 <b>(-28.90%)</b></td><td>0.01 <b>(+35.41%)</b></td><td>232.70 <b>(+40.60%)</b></td><td>181.74 <b>(+36.44%)</b></td><td>190.50 <b>(+52.89%)</b></td><td>137.80 (+16.88%)</td><td>41.61 <b>(+112.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>165.50 (n/a)</td><td>133.20 (n/a)</td><td>124.60 (n/a)</td><td>117.90 (n/a)</td><td>19.59 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-18.23%)</td><td>0.02 <b>(-24.17%)</b></td><td>0.02 <b>(-37.38%)</b></td><td>0.01 (+9.49%)</td><td>0.01 <b>(-42.86%)</b></td><td>344.10 (-8.65%)</td><td>221.66 (+17.62%)</td><td>205.20 <b>(+59.69%)</b></td><td>145.60 <b>(+22.25%)</b></td><td>74.36 <b>(-32.43%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>376.70 (n/a)</td><td>188.46 (n/a)</td><td>128.50 (n/a)</td><td>119.10 (n/a)</td><td>110.04 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 <b>(-25.31%)</b></td><td>0.02 (-10.97%)</td><td>0.02 (-2.04%)</td><td>0.02 (-3.83%)</td><td>0.00 <b>(-68.27%)</b></td><td>190.90 (+3.98%)</td><td>175.60 (+9.98%)</td><td>176.30 (+2.08%)</td><td>158.70 <b>(+33.92%)</b></td><td>11.56 <b>(-55.42%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.60 (n/a)</td><td>159.66 (n/a)</td><td>172.70 (n/a)</td><td>118.50 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-4.38%)</td><td>0.02 (-9.87%)</td><td>0.02 (-17.44%)</td><td>0.02 (-0.55%)</td><td>0.01 <b>(-28.52%)</b></td><td>205.00 (+0.54%)</td><td>169.20 (+7.92%)</td><td>169.30 <b>(+21.10%)</b></td><td>123.20 (+4.58%)</td><td>30.67 <b>(-28.19%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>156.78 (n/a)</td><td>139.80 (n/a)</td><td>117.80 (n/a)</td><td>42.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-1.12%)</td><td>0.03 (-2.86%)</td><td>0.02 (-10.86%)</td><td>0.02 (+14.91%)</td><td>0.01 (-8.99%)</td><td>193.90 (-12.97%)</td><td>165.86 (+1.82%)</td><td>179.70 (+12.17%)</td><td>121.30 (+1.17%)</td><td>30.69 <b>(-20.50%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>162.90 (n/a)</td><td>160.20 (n/a)</td><td>119.90 (n/a)</td><td>38.60 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 <b>(-26.14%)</b></td><td>0.02 (-13.74%)</td><td>0.02 (-17.50%)</td><td>0.02 <b>(+27.07%)</b></td><td>0.00 <b>(-79.43%)</b></td><td>194.70 <b>(-21.33%)</b></td><td>178.84 (+8.82%)</td><td>177.10 <b>(+21.22%)</b></td><td>163.80 <b>(+35.37%)</b></td><td>11.18 <b>(-78.23%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.50 (n/a)</td><td>164.34 (n/a)</td><td>146.10 (n/a)</td><td>121.00 (n/a)</td><td>51.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-12.11%)</td><td>0.02 (-11.13%)</td><td>0.02 (-15.14%)</td><td>0.02 (-7.20%)</td><td>0.00 <b>(-31.02%)</b></td><td>258.10 (+7.72%)</td><td>190.40 (+10.19%)</td><td>179.90 (+17.89%)</td><td>149.70 (+13.75%)</td><td>40.98 (-12.10%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.60 (n/a)</td><td>172.80 (n/a)</td><td>152.60 (n/a)</td><td>131.60 (n/a)</td><td>46.62 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-16.70%)</td><td>0.02 (-14.64%)</td><td>0.02 <b>(-23.88%)</b></td><td>0.02 (+3.54%)</td><td>0.00 <b>(-39.28%)</b></td><td>229.30 (-3.41%)</td><td>203.60 (+14.37%)</td><td>220.00 <b>(+31.34%)</b></td><td>159.60 (+20.00%)</td><td>29.33 <b>(-29.89%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>178.02 (n/a)</td><td>167.50 (n/a)</td><td>133.00 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-19.09%)</td><td>0.02 <b>(-22.01%)</b></td><td>0.02 <b>(-29.86%)</b></td><td>0.01 (-9.00%)</td><td>0.01 <b>(-24.79%)</b></td><td>299.90 (+9.89%)</td><td>223.16 <b>(+26.05%)</b></td><td>240.90 <b>(+42.54%)</b></td><td>161.80 <b>(+23.61%)</b></td><td>57.76 (-0.54%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>272.90 (n/a)</td><td>177.04 (n/a)</td><td>169.00 (n/a)</td><td>130.90 (n/a)</td><td>58.08 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (+3.22%)</td><td>0.02 (-10.33%)</td><td>0.02 (-17.96%)</td><td>0.02 (-10.62%)</td><td>0.01 (+8.78%)</td><td>269.00 (+11.90%)</td><td>197.16 (+12.66%)</td><td>192.60 <b>(+21.90%)</b></td><td>125.00 (-3.10%)</td><td>51.80 (+13.11%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>175.00 (n/a)</td><td>158.00 (n/a)</td><td>129.00 (n/a)</td><td>45.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 <b>(+50.06%)</b></td><td>0.02 <b>(+33.52%)</b></td><td>0.02 (+15.49%)</td><td>0.02 <b>(+26.29%)</b></td><td>0.01 <b>(+100.88%)</b></td><td>216.50 <b>(-20.78%)</b></td><td>176.52 <b>(-23.43%)</b></td><td>195.80 (-13.40%)</td><td>125.90 <b>(-33.39%)</b></td><td>38.58 (+4.68%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>273.30 (n/a)</td><td>230.54 (n/a)</td><td>226.10 (n/a)</td><td>189.00 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 <b>(-22.80%)</b></td><td>0.02 (+5.60%)</td><td>0.03 (+12.08%)</td><td>0.02 <b>(+31.17%)</b></td><td>0.00 <b>(-67.20%)</b></td><td>195.20 <b>(-23.75%)</b></td><td>168.34 (-11.41%)</td><td>163.20 (-10.77%)</td><td>147.80 <b>(+29.54%)</b></td><td>17.96 <b>(-66.63%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>256.00 (n/a)</td><td>190.02 (n/a)</td><td>182.90 (n/a)</td><td>114.10 (n/a)</td><td>53.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-16.77%)</td><td>0.05 (-4.61%)</td><td>0.05 (-13.91%)</td><td>0.04 <b>(+23.19%)</b></td><td>0.01 <b>(-55.97%)</b></td><td>195.30 (-18.83%)</td><td>171.46 (-1.21%)</td><td>175.70 (+16.20%)</td><td>138.50 <b>(+20.12%)</b></td><td>21.55 <b>(-59.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>240.60 (n/a)</td><td>173.56 (n/a)</td><td>151.20 (n/a)</td><td>115.30 (n/a)</td><td>52.63 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-5.04%)</td><td>0.05 (-2.30%)</td><td>0.05 (-0.63%)</td><td>0.04 (+4.90%)</td><td>0.01 (-13.67%)</td><td>191.20 (-4.69%)</td><td>161.68 (+1.76%)</td><td>157.70 (+0.64%)</td><td>130.70 (+5.32%)</td><td>23.83 (-13.29%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>158.88 (n/a)</td><td>156.70 (n/a)</td><td>124.10 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-11.53%)</td><td>0.04 (+3.24%)</td><td>0.04 (+9.24%)</td><td>0.04 <b>(+49.98%)</b></td><td>0.01 <b>(-52.67%)</b></td><td>230.10 <b>(-33.34%)</b></td><td>200.54 (-8.84%)</td><td>191.30 (-8.47%)</td><td>175.10 (+13.04%)</td><td>25.56 <b>(-65.44%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>345.20 (n/a)</td><td>219.98 (n/a)</td><td>209.00 (n/a)</td><td>154.90 (n/a)</td><td>73.97 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-3.99%)</td><td>0.04 (-7.44%)</td><td>0.04 (-5.01%)</td><td>0.03 (-12.62%)</td><td>0.01 <b>(+20.82%)</b></td><td>234.50 (+14.45%)</td><td>193.96 (+9.40%)</td><td>192.00 (+5.26%)</td><td>145.50 (+4.15%)</td><td>35.52 <b>(+48.42%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>177.30 (n/a)</td><td>182.40 (n/a)</td><td>139.70 (n/a)</td><td>23.94 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 <b>(-20.83%)</b></td><td>0.04 (-13.41%)</td><td>0.04 (-11.93%)</td><td>0.04 (-9.64%)</td><td>0.00 <b>(-45.87%)</b></td><td>232.70 (+10.65%)</td><td>198.88 (+14.01%)</td><td>199.50 (+13.55%)</td><td>177.50 <b>(+26.24%)</b></td><td>21.78 <b>(-24.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>174.44 (n/a)</td><td>175.70 (n/a)</td><td>140.60 (n/a)</td><td>28.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (-17.58%)</td><td>0.05 (-2.48%)</td><td>0.05 (+5.59%)</td><td>0.03 (-13.36%)</td><td>0.01 <b>(-23.53%)</b></td><td>248.30 (+15.38%)</td><td>175.08 (+1.76%)</td><td>168.20 (-5.29%)</td><td>144.60 <b>(+21.31%)</b></td><td>42.54 (+8.42%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>172.06 (n/a)</td><td>177.60 (n/a)</td><td>119.20 (n/a)</td><td>39.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 <b>(-26.37%)</b></td><td>0.04 (+0.19%)</td><td>0.05 (+14.00%)</td><td>0.03 (+18.21%)</td><td>0.01 <b>(-52.17%)</b></td><td>251.90 (-15.41%)</td><td>193.62 (-5.71%)</td><td>178.10 (-12.31%)</td><td>166.20 <b>(+35.78%)</b></td><td>35.46 <b>(-43.26%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.80 (n/a)</td><td>205.34 (n/a)</td><td>203.10 (n/a)</td><td>122.40 (n/a)</td><td>62.49 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (+18.12%)</td><td>0.05 (+18.36%)</td><td>0.05 <b>(+29.51%)</b></td><td>0.04 <b>(+21.78%)</b></td><td>0.01 (-5.91%)</td><td>184.20 (-17.88%)</td><td>157.56 (-16.48%)</td><td>159.00 <b>(-22.78%)</b></td><td>123.80 (-15.32%)</td><td>23.16 <b>(-34.44%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>188.64 (n/a)</td><td>205.90 (n/a)</td><td>146.20 (n/a)</td><td>35.33 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-12.01%)</td><td>0.04 (-9.79%)</td><td>0.05 (-7.37%)</td><td>0.03 (-18.41%)</td><td>0.01 (+18.23%)</td><td>247.30 <b>(+22.55%)</b></td><td>190.00 (+12.52%)</td><td>181.40 (+7.98%)</td><td>155.00 (+13.64%)</td><td>38.80 <b>(+62.69%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>168.86 (n/a)</td><td>168.00 (n/a)</td><td>136.40 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-19.71%)</td><td>0.05 (-15.98%)</td><td>0.04 (-17.31%)</td><td>0.03 <b>(-25.50%)</b></td><td>0.01 (+4.43%)</td><td>241.00 <b>(+34.26%)</b></td><td>185.66 <b>(+20.34%)</b></td><td>182.20 <b>(+20.90%)</b></td><td>157.50 <b>(+24.60%)</b></td><td>34.18 <b>(+74.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>154.28 (n/a)</td><td>150.70 (n/a)</td><td>126.40 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-16.01%)</td><td>0.04 <b>(-21.26%)</b></td><td>0.04 <b>(-22.30%)</b></td><td>0.03 <b>(-21.36%)</b></td><td>0.01 (+2.72%)</td><td>253.30 <b>(+27.16%)</b></td><td>212.58 <b>(+27.74%)</b></td><td>207.00 <b>(+28.65%)</b></td><td>177.70 (+19.10%)</td><td>30.36 <b>(+54.07%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>166.42 (n/a)</td><td>160.90 (n/a)</td><td>149.20 (n/a)</td><td>19.70 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 <b>(-27.79%)</b></td><td>0.04 <b>(-20.99%)</b></td><td>0.05 (-17.55%)</td><td>0.02 (+9.83%)</td><td>0.01 <b>(-41.99%)</b></td><td>369.60 (-8.94%)</td><td>214.96 (+12.86%)</td><td>175.40 <b>(+21.22%)</b></td><td>154.90 <b>(+38.43%)</b></td><td>87.91 <b>(-27.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>405.90 (n/a)</td><td>190.46 (n/a)</td><td>144.70 (n/a)</td><td>111.90 (n/a)</td><td>122.04 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 <b>(+33.52%)</b></td><td>0.04 (-8.00%)</td><td>0.04 <b>(-20.71%)</b></td><td>0.03 <b>(-28.84%)</b></td><td>0.02 <b>(+163.16%)</b></td><td>306.80 <b>(+40.48%)</b></td><td>210.14 (+18.91%)</td><td>214.30 <b>(+26.13%)</b></td><td>111.90 <b>(-25.10%)</b></td><td>69.72 <b>(+158.98%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>176.72 (n/a)</td><td>169.90 (n/a)</td><td>149.40 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 <b>(-23.68%)</b></td><td>0.05 (-10.22%)</td><td>0.05 (-10.88%)</td><td>0.04 (+9.97%)</td><td>0.00 <b>(-70.54%)</b></td><td>189.30 (-9.08%)</td><td>174.92 (+7.92%)</td><td>177.80 (+12.18%)</td><td>157.50 <b>(+31.03%)</b></td><td>11.75 <b>(-65.20%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>162.08 (n/a)</td><td>158.50 (n/a)</td><td>120.20 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (+0.05%)</td><td>0.04 (-7.79%)</td><td>0.04 (-13.05%)</td><td>0.04 (-6.57%)</td><td>0.01 <b>(+20.39%)</b></td><td>219.50 (+7.02%)</td><td>189.92 (+9.22%)</td><td>193.70 (+15.02%)</td><td>148.00 (-0.07%)</td><td>29.14 <b>(+28.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>173.88 (n/a)</td><td>168.40 (n/a)</td><td>148.10 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-12.00%)</td><td>0.04 (-16.77%)</td><td>0.04 <b>(-20.67%)</b></td><td>0.04 (-8.30%)</td><td>0.01 <b>(-24.44%)</b></td><td>221.10 (+9.08%)</td><td>190.50 (+19.54%)</td><td>189.20 <b>(+26.05%)</b></td><td>161.80 (+13.62%)</td><td>22.59 (-8.47%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.70 (n/a)</td><td>159.36 (n/a)</td><td>150.10 (n/a)</td><td>142.40 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (+10.65%)</td><td>0.10 (+3.83%)</td><td>0.11 (+12.61%)</td><td>0.08 (-15.80%)</td><td>0.02 <b>(+94.09%)</b></td><td>213.20 (+18.77%)</td><td>164.22 (-0.50%)</td><td>152.30 (-11.20%)</td><td>122.60 (-9.65%)</td><td>38.66 <b>(+112.34%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>165.04 (n/a)</td><td>171.50 (n/a)</td><td>135.70 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (+16.13%)</td><td>0.09 (+10.16%)</td><td>0.10 <b>(+21.23%)</b></td><td>0.06 (-8.70%)</td><td>0.02 <b>(+27.53%)</b></td><td>259.10 (+9.56%)</td><td>181.04 (-7.63%)</td><td>170.70 (-17.54%)</td><td>132.20 (-13.88%)</td><td>47.28 <b>(+27.01%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.50 (n/a)</td><td>196.00 (n/a)</td><td>207.00 (n/a)</td><td>153.50 (n/a)</td><td>37.22 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (-12.21%)</td><td>0.08 (-8.88%)</td><td>0.07 (-6.16%)</td><td>0.06 (-2.68%)</td><td>0.02 (-16.49%)</td><td>274.80 (+2.77%)</td><td>215.52 (+8.83%)</td><td>220.00 (+6.59%)</td><td>167.40 (+13.88%)</td><td>46.66 (-3.28%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>267.40 (n/a)</td><td>198.04 (n/a)</td><td>206.40 (n/a)</td><td>147.00 (n/a)</td><td>48.25 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (-15.26%)</td><td>0.08 (-8.09%)</td><td>0.08 (-10.15%)</td><td>0.07 (-3.66%)</td><td>0.01 <b>(-39.04%)</b></td><td>238.30 (+3.79%)</td><td>212.70 (+7.55%)</td><td>215.20 (+11.27%)</td><td>183.90 (+18.04%)</td><td>22.76 <b>(-26.95%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>197.76 (n/a)</td><td>193.40 (n/a)</td><td>155.80 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (-1.48%)</td><td>0.10 (+3.99%)</td><td>0.10 (+10.13%)</td><td>0.08 (-0.03%)</td><td>0.01 (-16.96%)</td><td>199.40 (+0.05%)</td><td>163.14 (-4.48%)</td><td>160.80 (-9.20%)</td><td>133.30 (+1.52%)</td><td>23.58 (-14.96%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.30 (n/a)</td><td>170.80 (n/a)</td><td>177.10 (n/a)</td><td>131.30 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (-12.63%)</td><td>0.10 (-14.47%)</td><td>0.10 (-18.58%)</td><td>0.08 (-19.49%)</td><td>0.02 (+8.09%)</td><td>216.80 <b>(+24.24%)</b></td><td>165.34 (+18.64%)</td><td>169.00 <b>(+22.82%)</b></td><td>124.60 (+14.52%)</td><td>35.91 <b>(+52.20%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>174.50 (n/a)</td><td>139.36 (n/a)</td><td>137.60 (n/a)</td><td>108.80 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 <b>(-31.48%)</b></td><td>0.09 <b>(-20.70%)</b></td><td>0.09 <b>(-21.90%)</b></td><td>0.08 (-14.76%)</td><td>0.01 <b>(-60.00%)</b></td><td>204.60 (+17.32%)</td><td>179.88 <b>(+23.37%)</b></td><td>182.30 <b>(+28.02%)</b></td><td>157.70 <b>(+46.02%)</b></td><td>18.23 <b>(-32.88%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>174.40 (n/a)</td><td>145.80 (n/a)</td><td>142.40 (n/a)</td><td>108.00 (n/a)</td><td>27.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (-19.42%)</td><td>0.10 (-7.65%)</td><td>0.10 (-1.49%)</td><td>0.09 (+1.68%)</td><td>0.01 <b>(-50.99%)</b></td><td>183.00 (-1.61%)</td><td>166.44 (+6.03%)</td><td>167.90 (+1.51%)</td><td>138.60 <b>(+24.08%)</b></td><td>17.04 <b>(-38.77%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.00 (n/a)</td><td>156.98 (n/a)</td><td>165.40 (n/a)</td><td>111.70 (n/a)</td><td>27.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (-6.95%)</td><td>0.10 (-6.05%)</td><td>0.09 (-10.83%)</td><td>0.09 (+10.29%)</td><td>0.01 <b>(-33.48%)</b></td><td>192.10 (-9.30%)</td><td>170.54 (+4.65%)</td><td>173.80 (+12.13%)</td><td>140.00 (+7.44%)</td><td>21.24 <b>(-35.07%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.80 (n/a)</td><td>162.96 (n/a)</td><td>155.00 (n/a)</td><td>130.30 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 <b>(-24.68%)</b></td><td>0.10 (-11.65%)</td><td>0.10 <b>(-20.10%)</b></td><td>0.10 (+17.12%)</td><td>0.01 <b>(-79.42%)</b></td><td>171.10 (-14.58%)</td><td>159.70 (+7.09%)</td><td>160.60 <b>(+25.18%)</b></td><td>148.10 <b>(+32.83%)</b></td><td>9.48 <b>(-77.08%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>200.30 (n/a)</td><td>149.12 (n/a)</td><td>128.30 (n/a)</td><td>111.50 (n/a)</td><td>41.35 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (+2.55%)</td><td>0.10 (-2.95%)</td><td>0.09 (-13.29%)</td><td>0.07 (-16.92%)</td><td>0.03 <b>(+22.85%)</b></td><td>243.40 <b>(+20.38%)</b></td><td>174.10 (+5.45%)</td><td>182.50 (+15.36%)</td><td>122.20 (-2.47%)</td><td>47.65 <b>(+36.94%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.20 (n/a)</td><td>165.10 (n/a)</td><td>158.20 (n/a)</td><td>125.30 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 <b>(+32.10%)</b></td><td>0.10 (-0.04%)</td><td>0.09 (-9.86%)</td><td>0.08 (-4.45%)</td><td>0.03 <b>(+225.68%)</b></td><td>197.00 (+4.68%)</td><td>173.88 (+3.73%)</td><td>182.80 (+10.92%)</td><td>114.10 <b>(-24.29%)</b></td><td>34.00 <b>(+149.03%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>167.62 (n/a)</td><td>164.80 (n/a)</td><td>150.70 (n/a)</td><td>13.65 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (-18.32%)</td><td>0.09 (-4.69%)</td><td>0.09 (-3.63%)</td><td>0.08 (+15.41%)</td><td>0.01 <b>(-69.75%)</b></td><td>207.10 (-13.35%)</td><td>191.62 (+1.89%)</td><td>189.80 (+3.77%)</td><td>177.10 <b>(+22.48%)</b></td><td>12.22 <b>(-67.90%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.00 (n/a)</td><td>188.06 (n/a)</td><td>182.90 (n/a)</td><td>144.60 (n/a)</td><td>38.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (+2.49%)</td><td>0.09 (-2.65%)</td><td>0.09 (+1.23%)</td><td>0.07 (-15.55%)</td><td>0.02 <b>(+57.22%)</b></td><td>220.00 (+18.41%)</td><td>178.74 (+4.27%)</td><td>174.40 (-1.19%)</td><td>140.20 (-2.44%)</td><td>30.20 <b>(+85.51%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.80 (n/a)</td><td>171.42 (n/a)</td><td>176.50 (n/a)</td><td>143.70 (n/a)</td><td>16.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (+8.44%)</td><td>0.09 (-0.28%)</td><td>0.09 (+1.43%)</td><td>0.08 (-2.73%)</td><td>0.01 <b>(+62.62%)</b></td><td>199.80 (+2.78%)</td><td>177.84 (+1.08%)</td><td>173.40 (-1.37%)</td><td>147.40 (-7.82%)</td><td>22.32 <b>(+58.14%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>175.94 (n/a)</td><td>175.80 (n/a)</td><td>159.90 (n/a)</td><td>14.11 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 <b>(-24.28%)</b></td><td>0.09 (-11.89%)</td><td>0.09 (+1.42%)</td><td>0.08 (+1.47%)</td><td>0.01 <b>(-69.43%)</b></td><td>200.10 (-1.43%)</td><td>186.28 (+10.55%)</td><td>181.80 (-1.41%)</td><td>173.20 <b>(+32.01%)</b></td><td>12.94 <b>(-58.94%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.00 (n/a)</td><td>168.50 (n/a)</td><td>184.40 (n/a)</td><td>131.20 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.32 <b>(+36.25%)</b></td><td>0.20 (+3.22%)</td><td>0.19 (+0.34%)</td><td>0.14 <b>(-21.13%)</b></td><td>0.07 <b>(+192.26%)</b></td><td>241.40 <b>(+26.79%)</b></td><td>176.10 (+5.07%)</td><td>173.90 (-0.34%)</td><td>103.90 <b>(-26.62%)</b></td><td>56.59 <b>(+177.15%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>190.40 (n/a)</td><td>167.60 (n/a)</td><td>174.50 (n/a)</td><td>141.60 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (-3.32%)</td><td>0.20 (+2.09%)</td><td>0.21 (+6.16%)</td><td>0.14 (-5.52%)</td><td>0.04 (+6.10%)</td><td>237.80 (+5.88%)</td><td>168.36 (-1.32%)</td><td>154.30 (-5.80%)</td><td>140.20 (+3.47%)</td><td>40.18 (+16.95%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.60 (n/a)</td><td>170.62 (n/a)</td><td>163.80 (n/a)</td><td>135.50 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (-2.13%)</td><td>0.15 (-8.22%)</td><td>0.16 (-8.23%)</td><td>0.11 <b>(-25.31%)</b></td><td>0.03 <b>(+32.34%)</b></td><td>311.40 <b>(+33.88%)</b></td><td>224.24 (+11.37%)</td><td>208.70 (+8.98%)</td><td>173.30 (+2.18%)</td><td>52.48 <b>(+82.55%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>232.60 (n/a)</td><td>201.34 (n/a)</td><td>191.50 (n/a)</td><td>169.60 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (+3.02%)</td><td>0.18 (+2.64%)</td><td>0.19 (-6.90%)</td><td>0.16 (+15.99%)</td><td>0.02 <b>(-44.19%)</b></td><td>199.10 (-13.77%)</td><td>179.04 (-4.36%)</td><td>175.80 (+7.46%)</td><td>156.50 (-2.92%)</td><td>16.32 <b>(-52.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>230.90 (n/a)</td><td>187.20 (n/a)</td><td>163.60 (n/a)</td><td>161.20 (n/a)</td><td>34.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 <b>(-34.67%)</b></td><td>0.18 <b>(-22.33%)</b></td><td>0.17 (-17.89%)</td><td>0.16 (-7.89%)</td><td>0.02 <b>(-64.14%)</b></td><td>206.80 (+8.56%)</td><td>189.20 <b>(+24.23%)</b></td><td>189.30 <b>(+21.81%)</b></td><td>155.90 <b>(+53.14%)</b></td><td>20.59 <b>(-39.29%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>190.50 (n/a)</td><td>152.30 (n/a)</td><td>155.40 (n/a)</td><td>101.80 (n/a)</td><td>33.91 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (-17.43%)</td><td>0.19 <b>(-22.09%)</b></td><td>0.19 <b>(-24.93%)</b></td><td>0.13 <b>(-24.85%)</b></td><td>0.03 (-4.33%)</td><td>243.30 <b>(+33.02%)</b></td><td>180.72 <b>(+29.51%)</b></td><td>176.90 <b>(+33.21%)</b></td><td>144.40 <b>(+21.04%)</b></td><td>37.88 <b>(+52.06%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>182.90 (n/a)</td><td>139.54 (n/a)</td><td>132.80 (n/a)</td><td>119.30 (n/a)</td><td>24.91 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (+1.22%)</td><td>0.22 (-8.01%)</td><td>0.20 (-17.59%)</td><td>0.19 (-4.47%)</td><td>0.04 <b>(+20.87%)</b></td><td>176.30 (+4.69%)</td><td>151.88 (+9.72%)</td><td>166.30 <b>(+21.39%)</b></td><td>115.00 (-1.20%)</td><td>26.23 <b>(+26.03%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>168.40 (n/a)</td><td>138.42 (n/a)</td><td>137.00 (n/a)</td><td>116.40 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (+12.09%)</td><td>0.21 (-8.91%)</td><td>0.20 (-18.75%)</td><td>0.18 (-8.44%)</td><td>0.05 <b>(+60.67%)</b></td><td>183.30 (+9.24%)</td><td>160.26 (+12.35%)</td><td>167.10 <b>(+23.14%)</b></td><td>106.40 (-10.81%)</td><td>31.04 <b>(+49.45%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>167.80 (n/a)</td><td>142.64 (n/a)</td><td>135.70 (n/a)</td><td>119.30 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (+2.70%)</td><td>0.22 (-7.05%)</td><td>0.22 (-17.90%)</td><td>0.15 (+3.43%)</td><td>0.06 (-11.39%)</td><td>216.40 (-3.31%)</td><td>158.50 (+5.34%)</td><td>151.50 <b>(+21.78%)</b></td><td>105.50 (-2.59%)</td><td>40.06 (-17.98%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>223.80 (n/a)</td><td>150.46 (n/a)</td><td>124.40 (n/a)</td><td>108.30 (n/a)</td><td>48.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (-18.40%)</td><td>0.20 (-7.45%)</td><td>0.22 (+4.93%)</td><td>0.09 <b>(-22.82%)</b></td><td>0.06 (-8.94%)</td><td>357.10 <b>(+29.57%)</b></td><td>191.24 (+11.86%)</td><td>146.70 (-4.74%)</td><td>131.50 <b>(+22.55%)</b></td><td>94.17 <b>(+47.43%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>275.60 (n/a)</td><td>170.96 (n/a)</td><td>154.00 (n/a)</td><td>107.30 (n/a)</td><td>63.87 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (-12.90%)</td><td>0.19 (-17.81%)</td><td>0.19 (-18.13%)</td><td>0.11 <b>(-38.01%)</b></td><td>0.05 <b>(+43.39%)</b></td><td>298.10 <b>(+61.31%)</b></td><td>184.02 <b>(+28.67%)</b></td><td>170.60 <b>(+22.12%)</b></td><td>138.70 (+14.82%)</td><td>65.72 <b>(+164.64%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>184.80 (n/a)</td><td>143.02 (n/a)</td><td>139.70 (n/a)</td><td>120.80 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.30 <b>(+20.17%)</b></td><td>0.19 (-7.40%)</td><td>0.19 (-9.72%)</td><td>0.09 <b>(-43.21%)</b></td><td>0.07 <b>(+96.64%)</b></td><td>353.60 <b>(+76.10%)</b></td><td>195.20 <b>(+21.29%)</b></td><td>174.00 (+10.76%)</td><td>110.80 (-16.75%)</td><td>92.75 <b>(+215.11%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>200.80 (n/a)</td><td>160.94 (n/a)</td><td>157.10 (n/a)</td><td>133.10 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (-10.39%)</td><td>0.19 (-6.29%)</td><td>0.18 (-18.96%)</td><td>0.16 <b>(+24.15%)</b></td><td>0.03 <b>(-40.43%)</b></td><td>205.80 (-19.45%)</td><td>176.52 (+2.34%)</td><td>183.20 <b>(+23.45%)</b></td><td>147.30 (+11.59%)</td><td>27.58 <b>(-47.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>255.50 (n/a)</td><td>172.48 (n/a)</td><td>148.40 (n/a)</td><td>132.00 (n/a)</td><td>52.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (-4.29%)</td><td>0.18 (-13.81%)</td><td>0.15 <b>(-22.10%)</b></td><td>0.12 <b>(-33.42%)</b></td><td>0.06 <b>(+42.64%)</b></td><td>267.70 <b>(+50.22%)</b></td><td>193.48 <b>(+22.36%)</b></td><td>211.90 <b>(+28.35%)</b></td><td>119.20 (+4.47%)</td><td>57.48 <b>(+125.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>178.20 (n/a)</td><td>158.12 (n/a)</td><td>165.10 (n/a)</td><td>114.10 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (-16.21%)</td><td>0.17 (-14.69%)</td><td>0.16 (-17.50%)</td><td>0.16 (-7.68%)</td><td>0.02 <b>(-27.28%)</b></td><td>206.50 (+8.34%)</td><td>191.96 (+16.82%)</td><td>205.30 <b>(+21.19%)</b></td><td>168.20 (+19.38%)</td><td>18.99 (-4.07%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>190.60 (n/a)</td><td>164.32 (n/a)</td><td>169.40 (n/a)</td><td>140.90 (n/a)</td><td>19.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (+4.22%)</td><td>0.18 (-6.00%)</td><td>0.17 (-13.14%)</td><td>0.15 (-4.95%)</td><td>0.03 (+8.78%)</td><td>225.10 (+5.24%)</td><td>190.90 (+6.68%)</td><td>188.20 (+15.11%)</td><td>144.00 (-4.06%)</td><td>30.60 (+5.77%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.90 (n/a)</td><td>178.94 (n/a)</td><td>163.50 (n/a)</td><td>150.10 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.18 (-0.02%)</td><td>0.18 (-0.17%)</td><td>0.18 (-0.32%)</td><td>0.18 (-0.08%)</td><td>0.00 (+15.18%)</td><td>47732.40 (+0.08%)</td><td>47614.52 (+0.17%)</td><td>47663.00 (+0.32%)</td><td>47448.20 (+0.02%)</td><td>120.89 (+15.32%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47694.40 (n/a)</td><td>47534.64 (n/a)</td><td>47511.00 (n/a)</td><td>47437.30 (n/a)</td><td>104.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.18 (+0.05%)</td><td>0.18 (+0.18%)</td><td>0.18 (+0.06%)</td><td>0.18 (+0.43%)</td><td>0.00 <b>(-56.04%)</b></td><td>47611.10 (-0.42%)</td><td>47527.62 (-0.18%)</td><td>47537.20 (-0.06%)</td><td>47451.90 (-0.05%)</td><td>64.62 <b>(-56.25%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47813.60 (n/a)</td><td>47612.50 (n/a)</td><td>47565.10 (n/a)</td><td>47475.80 (n/a)</td><td>147.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (-0.00%)</td><td>0.11 (-0.02%)</td><td>0.11 (-0.01%)</td><td>0.11 (-0.01%)</td><td>0.00 (+18.30%)</td><td>375918.30 (+0.01%)</td><td>375630.62 (+0.02%)</td><td>375603.10 (+0.01%)</td><td>375270.50 (+0.00%)</td><td>276.35 (+18.32%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>375870.80 (n/a)</td><td>375543.56 (n/a)</td><td>375548.50 (n/a)</td><td>375256.10 (n/a)</td><td>233.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (+17.75%)</td><td>0.15 (+12.74%)</td><td>0.14 (+7.07%)</td><td>0.13 <b>(+23.28%)</b></td><td>0.02 (+10.39%)</td><td>193.50 (-18.90%)</td><td>170.78 (-11.52%)</td><td>176.10 (-6.63%)</td><td>145.70 (-15.04%)</td><td>19.88 <b>(-25.76%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>238.60 (n/a)</td><td>193.02 (n/a)</td><td>188.60 (n/a)</td><td>171.50 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (+6.69%)</td><td>0.28 (+3.13%)</td><td>0.31 (+8.52%)</td><td>0.21 (-10.50%)</td><td>0.04 <b>(+96.01%)</b></td><td>230.00 (+11.76%)</td><td>179.42 (-1.35%)</td><td>160.30 (-7.82%)</td><td>156.80 (-6.28%)</td><td>32.13 <b>(+100.99%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>205.80 (n/a)</td><td>181.88 (n/a)</td><td>173.90 (n/a)</td><td>167.30 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>12.93 (-0.27%)</td><td>12.66 (+0.15%)</td><td>12.78 (+0.46%)</td><td>12.24 (-0.57%)</td><td>0.30 (+8.18%)</td><td>856.50 (+0.56%)</td><td>828.34 (-0.14%)</td><td>820.60 (-0.45%)</td><td>811.20 (+0.27%)</td><td>19.83 (+8.49%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>12.96 (n/a)</td><td>12.65 (n/a)</td><td>12.72 (n/a)</td><td>12.31 (n/a)</td><td>0.28 (n/a)</td><td>851.70 (n/a)</td><td>829.54 (n/a)</td><td>824.30 (n/a)</td><td>809.00 (n/a)</td><td>18.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (-13.57%)</td><td>0.26 (+2.68%)</td><td>0.27 (+9.89%)</td><td>0.22 (+17.90%)</td><td>0.04 <b>(-39.82%)</b></td><td>190.40 (-15.15%)</td><td>159.98 (-5.46%)</td><td>150.70 (-9.05%)</td><td>131.80 (+15.72%)</td><td>24.54 <b>(-38.42%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>224.40 (n/a)</td><td>169.22 (n/a)</td><td>165.70 (n/a)</td><td>113.90 (n/a)</td><td>39.85 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+2.58%)</td><td>0.03 (+4.67%)</td><td>0.03 (+2.50%)</td><td>0.03 <b>(+24.83%)</b></td><td>0.00 <b>(-42.07%)</b></td><td>190.90 (-19.86%)</td><td>169.04 (-6.94%)</td><td>170.60 (-2.46%)</td><td>141.80 (-2.54%)</td><td>18.08 <b>(-54.08%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.20 (n/a)</td><td>181.64 (n/a)</td><td>174.90 (n/a)</td><td>145.50 (n/a)</td><td>39.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-7.51%)</td><td>0.03 (+11.62%)</td><td>0.03 (+18.17%)</td><td>0.03 (+18.92%)</td><td>0.00 <b>(-72.01%)</b></td><td>157.60 (-15.90%)</td><td>148.96 (-11.50%)</td><td>146.00 (-15.36%)</td><td>145.30 (+8.11%)</td><td>5.29 <b>(-73.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.40 (n/a)</td><td>168.32 (n/a)</td><td>172.50 (n/a)</td><td>134.40 (n/a)</td><td>20.31 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-8.21%)</td><td>0.04 (-7.55%)</td><td>0.03 (-12.37%)</td><td>0.02 (-17.76%)</td><td>0.01 (+2.29%)</td><td>254.60 <b>(+21.59%)</b></td><td>178.04 (+9.85%)</td><td>184.50 (+14.10%)</td><td>126.60 (+8.95%)</td><td>51.86 <b>(+30.44%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>162.08 (n/a)</td><td>161.70 (n/a)</td><td>116.20 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+2.40%)</td><td>0.03 (-6.08%)</td><td>0.02 (-3.99%)</td><td>0.02 <b>(-23.14%)</b></td><td>0.01 <b>(+34.78%)</b></td><td>231.70 <b>(+30.10%)</b></td><td>168.28 (+9.34%)</td><td>164.40 (+4.12%)</td><td>115.40 (-2.37%)</td><td>41.51 <b>(+70.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.10 (n/a)</td><td>153.90 (n/a)</td><td>157.90 (n/a)</td><td>118.20 (n/a)</td><td>24.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (-2.99%)</td><td>0.03 (-3.67%)</td><td>0.03 (-3.75%)</td><td>0.03 (+14.49%)</td><td>0.01 <b>(-20.59%)</b></td><td>194.50 (-12.62%)</td><td>162.52 (+2.05%)</td><td>163.10 (+3.89%)</td><td>129.40 (+3.11%)</td><td>27.21 <b>(-29.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>159.26 (n/a)</td><td>157.00 (n/a)</td><td>125.50 (n/a)</td><td>38.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-12.78%)</td><td>0.02 (-5.42%)</td><td>0.02 (-4.55%)</td><td>0.02 (+9.32%)</td><td>0.00 <b>(-47.86%)</b></td><td>177.60 (-8.55%)</td><td>165.10 (+4.10%)</td><td>172.60 (+4.80%)</td><td>145.50 (+14.66%)</td><td>14.52 <b>(-44.47%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.20 (n/a)</td><td>158.60 (n/a)</td><td>164.70 (n/a)</td><td>126.90 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-14.58%)</td><td>0.03 (-7.41%)</td><td>0.03 (-1.73%)</td><td>0.02 (-3.73%)</td><td>0.00 <b>(-36.79%)</b></td><td>210.00 (+3.86%)</td><td>178.56 (+6.22%)</td><td>170.90 (+1.79%)</td><td>155.20 (+17.04%)</td><td>25.19 <b>(-24.11%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>168.10 (n/a)</td><td>167.90 (n/a)</td><td>132.60 (n/a)</td><td>33.20 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-19.10%)</td><td>0.02 (-5.76%)</td><td>0.02 (-8.14%)</td><td>0.02 (+9.80%)</td><td>0.00 <b>(-52.57%)</b></td><td>194.80 (-8.93%)</td><td>170.52 (+3.52%)</td><td>167.30 (+8.85%)</td><td>153.90 <b>(+23.61%)</b></td><td>17.72 <b>(-47.72%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.90 (n/a)</td><td>164.72 (n/a)</td><td>153.70 (n/a)</td><td>124.50 (n/a)</td><td>33.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+2.80%)</td><td>0.03 (+1.00%)</td><td>0.03 (+5.69%)</td><td>0.02 (-4.86%)</td><td>0.01 (+4.67%)</td><td>214.70 (+5.09%)</td><td>167.26 (-0.56%)</td><td>173.10 (-5.41%)</td><td>117.40 (-2.73%)</td><td>40.72 (+5.69%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>168.20 (n/a)</td><td>183.00 (n/a)</td><td>120.70 (n/a)</td><td>38.52 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 <b>(-21.09%)</b></td><td>0.02 (-8.62%)</td><td>0.02 (-10.23%)</td><td>0.02 (-2.22%)</td><td>0.00 <b>(-53.20%)</b></td><td>210.30 (+2.29%)</td><td>170.00 (+5.56%)</td><td>167.80 (+11.42%)</td><td>148.90 <b>(+26.72%)</b></td><td>24.05 <b>(-40.43%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>161.04 (n/a)</td><td>150.60 (n/a)</td><td>117.50 (n/a)</td><td>40.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (+2.76%)</td><td>0.03 (+10.16%)</td><td>0.03 (+13.22%)</td><td>0.02 <b>(+27.81%)</b></td><td>0.00 <b>(-54.13%)</b></td><td>190.80 <b>(-21.74%)</b></td><td>180.44 (-10.61%)</td><td>183.50 (-11.69%)</td><td>162.40 (-2.64%)</td><td>10.71 <b>(-65.15%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.80 (n/a)</td><td>201.86 (n/a)</td><td>207.80 (n/a)</td><td>166.80 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (+14.00%)</td><td>0.02 (-13.47%)</td><td>0.02 <b>(-26.06%)</b></td><td>0.02 (-0.36%)</td><td>0.01 <b>(+21.85%)</b></td><td>221.80 (+0.41%)</td><td>177.86 (+16.80%)</td><td>175.80 <b>(+35.23%)</b></td><td>113.00 (-12.27%)</td><td>41.17 (+3.70%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>152.28 (n/a)</td><td>130.00 (n/a)</td><td>128.80 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 <b>(+28.47%)</b></td><td>0.02 (+10.25%)</td><td>0.02 (-8.45%)</td><td>0.02 <b>(+32.94%)</b></td><td>0.01 <b>(+29.40%)</b></td><td>238.90 <b>(-24.78%)</b></td><td>193.70 (-9.69%)</td><td>210.60 (+9.23%)</td><td>134.00 <b>(-22.18%)</b></td><td>41.16 <b>(-29.59%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>317.60 (n/a)</td><td>214.48 (n/a)</td><td>192.80 (n/a)</td><td>172.20 (n/a)</td><td>58.46 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (+0.28%)</td><td>0.02 (-5.22%)</td><td>0.02 (-7.37%)</td><td>0.02 (-11.24%)</td><td>0.00 (+17.61%)</td><td>234.00 (+12.66%)</td><td>189.26 (+6.36%)</td><td>194.20 (+7.95%)</td><td>150.50 (-0.27%)</td><td>31.92 <b>(+32.64%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.70 (n/a)</td><td>177.94 (n/a)</td><td>179.90 (n/a)</td><td>150.90 (n/a)</td><td>24.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 <b>(+64.52%)</b></td><td>0.03 (+16.44%)</td><td>0.02 (+1.72%)</td><td>0.02 (-9.08%)</td><td>0.01 <b>(+369.64%)</b></td><td>236.30 (+9.96%)</td><td>178.36 (-6.91%)</td><td>185.90 (-1.69%)</td><td>102.30 <b>(-39.22%)</b></td><td>52.70 <b>(+208.36%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.90 (n/a)</td><td>191.60 (n/a)</td><td>189.10 (n/a)</td><td>168.30 (n/a)</td><td>17.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (+0.92%)</td><td>0.02 (-7.20%)</td><td>0.02 (-14.63%)</td><td>0.01 (-19.31%)</td><td>0.00 <b>(+59.79%)</b></td><td>277.50 <b>(+23.94%)</b></td><td>214.58 (+9.82%)</td><td>219.30 (+17.15%)</td><td>169.40 (-0.88%)</td><td>41.18 <b>(+95.14%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.90 (n/a)</td><td>195.40 (n/a)</td><td>187.20 (n/a)</td><td>170.90 (n/a)</td><td>21.10 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-16.17%)</td><td>0.05 (+2.48%)</td><td>0.05 (+0.87%)</td><td>0.04 <b>(+71.99%)</b></td><td>0.01 <b>(-56.50%)</b></td><td>225.90 <b>(-41.87%)</b></td><td>181.06 (-13.77%)</td><td>179.00 (-0.83%)</td><td>154.50 (+19.31%)</td><td>29.18 <b>(-71.85%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>388.60 (n/a)</td><td>209.98 (n/a)</td><td>180.50 (n/a)</td><td>129.50 (n/a)</td><td>103.65 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 <b>(-20.62%)</b></td><td>0.08 (-6.35%)</td><td>0.08 (-6.69%)</td><td>0.06 <b>(+50.48%)</b></td><td>0.01 <b>(-55.15%)</b></td><td>198.40 <b>(-33.56%)</b></td><td>164.26 (-3.49%)</td><td>162.20 (+7.20%)</td><td>128.00 <b>(+25.98%)</b></td><td>26.10 <b>(-65.24%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>298.60 (n/a)</td><td>170.20 (n/a)</td><td>151.30 (n/a)</td><td>101.60 (n/a)</td><td>75.08 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 <b>(+24.74%)</b></td><td>0.06 <b>(+40.09%)</b></td><td>0.06 <b>(+58.67%)</b></td><td>0.05 <b>(+70.27%)</b></td><td>0.01 <b>(-29.85%)</b></td><td>169.70 <b>(-41.26%)</b></td><td>148.10 <b>(-30.91%)</b></td><td>140.60 <b>(-36.98%)</b></td><td>132.30 (-19.87%)</td><td>17.43 <b>(-65.64%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.90 (n/a)</td><td>214.36 (n/a)</td><td>223.10 (n/a)</td><td>165.10 (n/a)</td><td>50.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 (-13.52%)</td><td>0.06 (-14.03%)</td><td>0.07 (-6.63%)</td><td>0.05 <b>(-20.00%)</b></td><td>0.01 (+14.75%)</td><td>211.10 <b>(+24.99%)</b></td><td>164.86 (+18.81%)</td><td>152.80 (+7.08%)</td><td>124.00 (+15.56%)</td><td>38.60 <b>(+72.39%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>168.90 (n/a)</td><td>138.76 (n/a)</td><td>142.70 (n/a)</td><td>107.30 (n/a)</td><td>22.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (+10.77%)</td><td>0.06 (+11.60%)</td><td>0.06 (+9.14%)</td><td>0.04 (+11.22%)</td><td>0.01 <b>(+24.00%)</b></td><td>187.50 (-10.07%)</td><td>151.84 (-9.93%)</td><td>145.00 (-8.34%)</td><td>123.60 (-9.72%)</td><td>27.51 (-0.25%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>168.58 (n/a)</td><td>158.20 (n/a)</td><td>136.90 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (+16.41%)</td><td>0.07 (-7.00%)</td><td>0.06 (-19.70%)</td><td>0.05 (-3.04%)</td><td>0.02 <b>(+43.34%)</b></td><td>202.30 (+3.11%)</td><td>167.52 (+10.82%)</td><td>181.00 <b>(+24.48%)</b></td><td>96.60 (-14.13%)</td><td>42.41 <b>(+22.14%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>196.20 (n/a)</td><td>151.16 (n/a)</td><td>145.40 (n/a)</td><td>112.50 (n/a)</td><td>34.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 <b>(+51.70%)</b></td><td>0.05 <b>(+24.02%)</b></td><td>0.05 (-2.99%)</td><td>0.04 (+9.29%)</td><td>0.02 <b>(+136.13%)</b></td><td>215.60 (-8.49%)</td><td>164.94 (-15.42%)</td><td>181.70 (+3.12%)</td><td>109.10 <b>(-34.08%)</b></td><td>45.96 <b>(+39.11%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.60 (n/a)</td><td>195.00 (n/a)</td><td>176.20 (n/a)</td><td>165.50 (n/a)</td><td>33.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 <b>(+25.52%)</b></td><td>0.06 (+17.03%)</td><td>0.05 (+3.12%)</td><td>0.05 <b>(+28.82%)</b></td><td>0.01 <b>(+32.29%)</b></td><td>193.30 <b>(-22.37%)</b></td><td>160.52 (-14.46%)</td><td>172.10 (-3.04%)</td><td>121.00 <b>(-20.34%)</b></td><td>28.90 <b>(-21.61%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>249.00 (n/a)</td><td>187.66 (n/a)</td><td>177.50 (n/a)</td><td>151.90 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (+4.11%)</td><td>0.05 (-3.49%)</td><td>0.05 (-1.85%)</td><td>0.04 (-13.41%)</td><td>0.01 <b>(+54.49%)</b></td><td>219.40 (+15.47%)</td><td>182.56 (+5.64%)</td><td>181.20 (+1.91%)</td><td>135.70 (-3.96%)</td><td>34.63 <b>(+74.34%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>172.82 (n/a)</td><td>177.80 (n/a)</td><td>141.30 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (+8.06%)</td><td>0.05 (-6.12%)</td><td>0.05 (-14.16%)</td><td>0.03 <b>(+39.55%)</b></td><td>0.01 (-9.40%)</td><td>274.40 <b>(-28.34%)</b></td><td>200.42 (-0.26%)</td><td>185.70 (+16.50%)</td><td>127.60 (-7.40%)</td><td>56.86 <b>(-44.42%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>382.90 (n/a)</td><td>200.94 (n/a)</td><td>159.40 (n/a)</td><td>137.80 (n/a)</td><td>102.30 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (+16.01%)</td><td>0.05 (-6.18%)</td><td>0.04 (-19.33%)</td><td>0.04 (-10.06%)</td><td>0.01 <b>(+120.26%)</b></td><td>213.00 (+11.17%)</td><td>187.94 (+9.79%)</td><td>206.30 <b>(+23.98%)</b></td><td>127.20 (-13.76%)</td><td>36.20 <b>(+108.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>171.18 (n/a)</td><td>166.40 (n/a)</td><td>147.50 (n/a)</td><td>17.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (-11.04%)</td><td>0.05 (-0.82%)</td><td>0.05 (-7.78%)</td><td>0.04 <b>(+20.76%)</b></td><td>0.00 <b>(-67.88%)</b></td><td>204.90 (-17.18%)</td><td>189.80 (-1.52%)</td><td>191.90 (+8.42%)</td><td>177.30 (+12.43%)</td><td>10.69 <b>(-70.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>247.40 (n/a)</td><td>192.72 (n/a)</td><td>177.00 (n/a)</td><td>157.70 (n/a)</td><td>36.18 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (+2.03%)</td><td>0.05 (+12.92%)</td><td>0.05 (+4.12%)</td><td>0.04 <b>(+44.12%)</b></td><td>0.01 <b>(-37.06%)</b></td><td>193.10 <b>(-30.59%)</b></td><td>169.04 (-14.63%)</td><td>165.90 (-3.94%)</td><td>145.90 (-2.01%)</td><td>22.39 <b>(-57.40%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.20 (n/a)</td><td>198.00 (n/a)</td><td>172.70 (n/a)</td><td>148.90 (n/a)</td><td>52.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (+12.99%)</td><td>0.04 (+4.04%)</td><td>0.05 <b>(+24.14%)</b></td><td>0.02 <b>(-32.73%)</b></td><td>0.01 <b>(+232.54%)</b></td><td>372.80 <b>(+48.64%)</b></td><td>230.02 (+4.44%)</td><td>178.00 (-19.46%)</td><td>173.40 (-11.49%)</td><td>86.43 <b>(+321.65%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>250.80 (n/a)</td><td>220.24 (n/a)</td><td>221.00 (n/a)</td><td>195.90 (n/a)</td><td>20.50 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (-7.01%)</td><td>0.04 (-2.13%)</td><td>0.04 (+7.01%)</td><td>0.03 <b>(-21.61%)</b></td><td>0.01 <b>(+29.46%)</b></td><td>315.50 <b>(+27.58%)</b></td><td>233.24 (+3.81%)</td><td>217.50 (-6.53%)</td><td>197.10 (+7.59%)</td><td>46.91 <b>(+89.63%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>247.30 (n/a)</td><td>224.68 (n/a)</td><td>232.70 (n/a)</td><td>183.20 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (+7.18%)</td><td>0.10 (-3.41%)</td><td>0.09 (-19.91%)</td><td>0.08 (-1.53%)</td><td>0.02 <b>(+37.60%)</b></td><td>194.70 (+1.56%)</td><td>164.28 (+4.74%)</td><td>178.50 <b>(+24.83%)</b></td><td>129.70 (-6.69%)</td><td>29.15 <b>(+29.25%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>156.84 (n/a)</td><td>143.00 (n/a)</td><td>139.00 (n/a)</td><td>22.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (-18.48%)</td><td>0.13 (-9.78%)</td><td>0.12 (-19.40%)</td><td>0.12 (+1.84%)</td><td>0.02 <b>(-40.51%)</b></td><td>210.70 (-1.82%)</td><td>186.10 (+8.42%)</td><td>199.20 <b>(+24.11%)</b></td><td>158.80 <b>(+22.63%)</b></td><td>25.18 <b>(-32.06%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.60 (n/a)</td><td>171.64 (n/a)</td><td>160.50 (n/a)</td><td>129.50 (n/a)</td><td>37.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 <b>(-21.72%)</b></td><td>0.10 (-12.87%)</td><td>0.09 (-8.21%)</td><td>0.08 (-0.89%)</td><td>0.01 <b>(-43.08%)</b></td><td>206.30 (+0.88%)</td><td>175.26 (+11.96%)</td><td>178.70 (+8.96%)</td><td>144.40 <b>(+27.67%)</b></td><td>26.47 <b>(-26.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>204.50 (n/a)</td><td>156.54 (n/a)</td><td>164.00 (n/a)</td><td>113.10 (n/a)</td><td>35.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (-15.12%)</td><td>0.13 (+4.17%)</td><td>0.13 <b>(+23.20%)</b></td><td>0.10 (+10.12%)</td><td>0.01 <b>(-50.35%)</b></td><td>195.90 (-9.18%)</td><td>163.54 (-6.79%)</td><td>154.40 (-18.82%)</td><td>145.00 (+17.79%)</td><td>20.17 <b>(-45.63%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>215.70 (n/a)</td><td>175.46 (n/a)</td><td>190.20 (n/a)</td><td>123.10 (n/a)</td><td>37.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 <b>(+26.80%)</b></td><td>0.11 (+14.07%)</td><td>0.10 (+5.34%)</td><td>0.09 <b>(+21.73%)</b></td><td>0.02 <b>(+34.71%)</b></td><td>173.70 (-17.87%)</td><td>153.48 (-12.04%)</td><td>165.80 (-5.04%)</td><td>110.50 <b>(-21.18%)</b></td><td>25.36 (-14.44%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.50 (n/a)</td><td>174.48 (n/a)</td><td>174.60 (n/a)</td><td>140.20 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (-0.00%)</td><td>0.13 (-0.06%)</td><td>0.12 (-7.11%)</td><td>0.12 <b>(+20.64%)</b></td><td>0.01 <b>(-28.80%)</b></td><td>172.30 (-17.12%)</td><td>157.80 (-1.24%)</td><td>165.70 (+7.67%)</td><td>133.00 (+0.00%)</td><td>16.11 <b>(-43.28%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>207.90 (n/a)</td><td>159.78 (n/a)</td><td>153.90 (n/a)</td><td>133.00 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (+2.90%)</td><td>0.10 (-4.59%)</td><td>0.10 (-2.57%)</td><td>0.08 (-11.53%)</td><td>0.02 <b>(+55.39%)</b></td><td>209.30 (+13.07%)</td><td>168.76 (+7.63%)</td><td>163.90 (+2.63%)</td><td>122.90 (-2.85%)</td><td>37.87 <b>(+78.61%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.10 (n/a)</td><td>156.80 (n/a)</td><td>159.70 (n/a)</td><td>126.50 (n/a)</td><td>21.20 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 <b>(-23.23%)</b></td><td>0.11 (-2.29%)</td><td>0.11 (-4.26%)</td><td>0.10 <b>(+27.35%)</b></td><td>0.00 <b>(-84.95%)</b></td><td>177.60 <b>(-21.49%)</b></td><td>165.14 (-3.33%)</td><td>162.80 (+4.43%)</td><td>161.10 <b>(+30.23%)</b></td><td>7.03 <b>(-84.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>226.20 (n/a)</td><td>170.82 (n/a)</td><td>155.90 (n/a)</td><td>123.70 (n/a)</td><td>46.45 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (-18.96%)</td><td>0.10 <b>(-20.49%)</b></td><td>0.10 (-18.16%)</td><td>0.08 <b>(-22.88%)</b></td><td>0.02 <b>(-28.40%)</b></td><td>215.60 <b>(+29.72%)</b></td><td>174.22 <b>(+25.03%)</b></td><td>169.40 <b>(+22.22%)</b></td><td>135.10 <b>(+23.38%)</b></td><td>29.35 (+11.89%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>166.20 (n/a)</td><td>139.34 (n/a)</td><td>138.60 (n/a)</td><td>109.50 (n/a)</td><td>26.23 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 <b>(+33.40%)</b></td><td>0.13 (+19.95%)</td><td>0.14 <b>(+28.63%)</b></td><td>0.10 (+4.89%)</td><td>0.03 <b>(+195.80%)</b></td><td>181.80 (-4.67%)</td><td>145.76 (-14.02%)</td><td>127.40 <b>(-22.27%)</b></td><td>117.50 <b>(-25.06%)</b></td><td>32.10 <b>(+118.07%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>169.52 (n/a)</td><td>163.90 (n/a)</td><td>156.80 (n/a)</td><td>14.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (+4.80%)</td><td>0.09 (-19.58%)</td><td>0.08 <b>(-29.01%)</b></td><td>0.05 <b>(-38.91%)</b></td><td>0.03 <b>(+76.34%)</b></td><td>310.20 <b>(+63.69%)</b></td><td>210.40 <b>(+34.34%)</b></td><td>218.40 <b>(+40.90%)</b></td><td>116.80 (-4.58%)</td><td>69.89 <b>(+164.63%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.50 (n/a)</td><td>156.62 (n/a)</td><td>155.00 (n/a)</td><td>122.40 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (+16.01%)</td><td>0.09 (+11.03%)</td><td>0.10 (+13.83%)</td><td>0.06 (-2.05%)</td><td>0.03 <b>(+36.66%)</b></td><td>308.30 (+2.09%)</td><td>199.24 (-7.31%)</td><td>166.00 (-12.17%)</td><td>140.80 (-13.83%)</td><td>66.78 <b>(+21.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>302.00 (n/a)</td><td>214.96 (n/a)</td><td>189.00 (n/a)</td><td>163.40 (n/a)</td><td>55.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (+6.73%)</td><td>0.10 (-1.36%)</td><td>0.10 (+2.48%)</td><td>0.07 (-5.60%)</td><td>0.02 <b>(+48.41%)</b></td><td>225.60 (+5.92%)</td><td>173.00 (+3.68%)</td><td>159.00 (-2.45%)</td><td>129.90 (-6.28%)</td><td>40.26 <b>(+45.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>166.86 (n/a)</td><td>163.00 (n/a)</td><td>138.60 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (+1.45%)</td><td>0.09 (-6.05%)</td><td>0.09 (-7.83%)</td><td>0.07 (-18.51%)</td><td>0.01 <b>(+86.17%)</b></td><td>232.60 <b>(+22.74%)</b></td><td>190.36 (+7.77%)</td><td>189.90 (+8.51%)</td><td>156.40 (-1.45%)</td><td>27.61 <b>(+126.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.50 (n/a)</td><td>176.64 (n/a)</td><td>175.00 (n/a)</td><td>158.70 (n/a)</td><td>12.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (+8.27%)</td><td>0.09 (-8.29%)</td><td>0.08 (-18.26%)</td><td>0.07 (-9.38%)</td><td>0.02 <b>(+57.69%)</b></td><td>239.10 (+10.34%)</td><td>199.60 (+11.51%)</td><td>218.30 <b>(+22.30%)</b></td><td>139.60 (-7.67%)</td><td>40.14 <b>(+58.79%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>179.00 (n/a)</td><td>178.50 (n/a)</td><td>151.20 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (-18.51%)</td><td>0.17 (-17.55%)</td><td>0.18 (-7.31%)</td><td>0.09 <b>(-44.73%)</b></td><td>0.04 <b>(+38.69%)</b></td><td>358.70 <b>(+80.98%)</b></td><td>214.42 <b>(+29.31%)</b></td><td>186.20 (+7.94%)</td><td>164.30 <b>(+22.70%)</b></td><td>81.77 <b>(+221.70%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>198.20 (n/a)</td><td>165.82 (n/a)</td><td>172.50 (n/a)</td><td>133.90 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (-19.15%)</td><td>0.19 (-13.09%)</td><td>0.19 (-7.56%)</td><td>0.16 (-9.32%)</td><td>0.02 <b>(-42.91%)</b></td><td>206.60 (+10.30%)</td><td>175.52 (+13.87%)</td><td>171.80 (+8.19%)</td><td>155.70 <b>(+23.67%)</b></td><td>19.20 <b>(-20.12%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>187.30 (n/a)</td><td>154.14 (n/a)</td><td>158.80 (n/a)</td><td>125.90 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (-5.38%)</td><td>0.25 (+3.99%)</td><td>0.25 (+1.83%)</td><td>0.16 <b>(+22.31%)</b></td><td>0.06 (-14.91%)</td><td>251.30 (-18.25%)</td><td>175.94 (-7.04%)</td><td>163.40 (-1.80%)</td><td>132.80 (+5.73%)</td><td>48.15 <b>(-30.90%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>307.40 (n/a)</td><td>189.26 (n/a)</td><td>166.40 (n/a)</td><td>125.60 (n/a)</td><td>69.68 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (-9.34%)</td><td>0.19 (-14.11%)</td><td>0.18 (-16.01%)</td><td>0.17 (+4.18%)</td><td>0.03 <b>(-31.74%)</b></td><td>192.00 (-4.00%)</td><td>172.36 (+14.66%)</td><td>177.70 (+19.02%)</td><td>136.10 (+10.29%)</td><td>22.28 <b>(-27.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>200.00 (n/a)</td><td>150.32 (n/a)</td><td>149.30 (n/a)</td><td>123.40 (n/a)</td><td>30.92 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (-1.90%)</td><td>0.26 (-3.85%)</td><td>0.26 (-11.46%)</td><td>0.23 <b>(+29.62%)</b></td><td>0.03 <b>(-45.29%)</b></td><td>179.60 <b>(-22.85%)</b></td><td>156.54 (+0.33%)</td><td>156.80 (+12.97%)</td><td>131.10 (+1.94%)</td><td>17.62 <b>(-59.25%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>232.80 (n/a)</td><td>156.02 (n/a)</td><td>138.80 (n/a)</td><td>128.60 (n/a)</td><td>43.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 <b>(-23.43%)</b></td><td>0.20 (-7.52%)</td><td>0.19 (-13.94%)</td><td>0.16 (+5.36%)</td><td>0.04 <b>(-45.58%)</b></td><td>207.40 (-5.08%)</td><td>165.44 (+2.82%)</td><td>171.90 (+16.15%)</td><td>129.20 <b>(+30.64%)</b></td><td>31.54 <b>(-35.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>218.50 (n/a)</td><td>160.90 (n/a)</td><td>148.00 (n/a)</td><td>98.90 (n/a)</td><td>48.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (-3.99%)</td><td>0.23 (-2.24%)</td><td>0.24 (+12.12%)</td><td>0.16 (-15.91%)</td><td>0.05 (+6.36%)</td><td>234.80 (+18.95%)</td><td>166.90 (+3.60%)</td><td>152.70 (-10.81%)</td><td>132.00 (+4.10%)</td><td>41.51 <b>(+36.89%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>197.40 (n/a)</td><td>161.10 (n/a)</td><td>171.20 (n/a)</td><td>126.80 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (-11.49%)</td><td>0.18 <b>(-20.87%)</b></td><td>0.18 <b>(-30.72%)</b></td><td>0.16 (-9.43%)</td><td>0.04 (-15.47%)</td><td>205.10 (+10.45%)</td><td>181.64 <b>(+25.88%)</b></td><td>186.10 <b>(+44.38%)</b></td><td>132.20 (+12.99%)</td><td>28.87 (+1.56%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>185.70 (n/a)</td><td>144.30 (n/a)</td><td>128.90 (n/a)</td><td>117.00 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (+1.66%)</td><td>0.23 (+8.15%)</td><td>0.23 (+11.04%)</td><td>0.18 (+5.36%)</td><td>0.03 (+7.42%)</td><td>207.20 (-5.08%)</td><td>165.38 (-7.47%)</td><td>156.90 (-9.98%)</td><td>151.50 (-1.69%)</td><td>23.60 (-0.84%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>218.30 (n/a)</td><td>178.74 (n/a)</td><td>174.30 (n/a)</td><td>154.10 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 <b>(-24.94%)</b></td><td>0.17 (-17.98%)</td><td>0.17 <b>(-20.34%)</b></td><td>0.15 (-4.05%)</td><td>0.02 <b>(-51.93%)</b></td><td>214.00 (+4.24%)</td><td>189.60 (+19.14%)</td><td>191.60 <b>(+25.56%)</b></td><td>160.30 <b>(+33.25%)</b></td><td>22.05 <b>(-33.45%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.30 (n/a)</td><td>159.14 (n/a)</td><td>152.60 (n/a)</td><td>120.30 (n/a)</td><td>33.14 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 <b>(-35.83%)</b></td><td>0.20 (-5.99%)</td><td>0.20 (+1.61%)</td><td>0.16 <b>(+52.35%)</b></td><td>0.03 <b>(-68.78%)</b></td><td>214.60 <b>(-34.37%)</b></td><td>180.00 (-7.49%)</td><td>172.50 (-1.54%)</td><td>148.70 <b>(+55.87%)</b></td><td>27.87 <b>(-67.39%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.36 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>327.00 (n/a)</td><td>194.58 (n/a)</td><td>175.20 (n/a)</td><td>95.40 (n/a)</td><td>85.46 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 <b>(-25.38%)</b></td><td>0.18 (-16.02%)</td><td>0.15 <b>(-26.68%)</b></td><td>0.11 <b>(-28.14%)</b></td><td>0.06 (-15.99%)</td><td>312.00 <b>(+39.16%)</b></td><td>206.96 <b>(+21.33%)</b></td><td>216.70 <b>(+36.38%)</b></td><td>130.60 <b>(+34.09%)</b></td><td>75.61 <b>(+43.54%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>224.20 (n/a)</td><td>170.58 (n/a)</td><td>158.90 (n/a)</td><td>97.40 (n/a)</td><td>52.68 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (+3.58%)</td><td>0.20 (+12.52%)</td><td>0.22 <b>(+24.50%)</b></td><td>0.16 (+8.17%)</td><td>0.03 (-10.22%)</td><td>213.00 (-7.55%)</td><td>172.76 (-11.58%)</td><td>161.20 (-19.68%)</td><td>155.70 (-3.47%)</td><td>23.91 (-18.52%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>230.40 (n/a)</td><td>195.38 (n/a)</td><td>200.70 (n/a)</td><td>161.30 (n/a)</td><td>29.34 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.18 (+0.73%)</td><td>0.16 (+0.58%)</td><td>0.15 (-13.14%)</td><td>0.14 <b>(+43.45%)</b></td><td>0.02 <b>(-51.10%)</b></td><td>226.60 <b>(-30.28%)</b></td><td>206.82 (-4.69%)</td><td>216.10 (+15.13%)</td><td>177.40 (-0.73%)</td><td>20.86 <b>(-66.40%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>325.00 (n/a)</td><td>217.00 (n/a)</td><td>187.70 (n/a)</td><td>178.70 (n/a)</td><td>62.08 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (-1.08%)</td><td>0.14 (-1.77%)</td><td>0.13 (-2.42%)</td><td>0.12 (-9.03%)</td><td>0.02 <b>(+34.20%)</b></td><td>172.00 (+9.97%)</td><td>144.88 (+2.80%)</td><td>152.10 (+2.42%)</td><td>120.20 (+1.09%)</td><td>22.69 <b>(+45.23%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>156.40 (n/a)</td><td>140.94 (n/a)</td><td>148.50 (n/a)</td><td>118.90 (n/a)</td><td>15.62 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (+6.53%)</td><td>0.13 (-1.75%)</td><td>0.12 (-11.78%)</td><td>0.12 (+4.54%)</td><td>0.02 (+5.87%)</td><td>176.40 (-4.34%)</td><td>158.82 (+1.74%)</td><td>170.50 (+13.36%)</td><td>120.80 (-6.14%)</td><td>22.61 (-7.92%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>184.40 (n/a)</td><td>156.10 (n/a)</td><td>150.40 (n/a)</td><td>128.70 (n/a)</td><td>24.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (-11.75%)</td><td>0.11 (-16.10%)</td><td>0.12 (-7.90%)</td><td>0.08 (-17.08%)</td><td>0.03 (+5.00%)</td><td>248.10 <b>(+20.61%)</b></td><td>190.62 <b>(+21.91%)</b></td><td>170.60 (+8.52%)</td><td>135.20 (+13.33%)</td><td>52.80 <b>(+53.33%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>205.70 (n/a)</td><td>156.36 (n/a)</td><td>157.20 (n/a)</td><td>119.30 (n/a)</td><td>34.44 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (+1.03%)</td><td>0.12 (-6.48%)</td><td>0.11 (-16.92%)</td><td>0.08 <b>(-20.26%)</b></td><td>0.04 <b>(+68.01%)</b></td><td>257.60 <b>(+25.41%)</b></td><td>186.12 (+12.53%)</td><td>191.10 <b>(+20.34%)</b></td><td>129.00 (-1.00%)</td><td>55.43 <b>(+98.30%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>205.40 (n/a)</td><td>165.40 (n/a)</td><td>158.80 (n/a)</td><td>130.30 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (+0.49%)</td><td>0.13 (-13.37%)</td><td>0.11 <b>(-22.34%)</b></td><td>0.10 <b>(-25.37%)</b></td><td>0.03 <b>(+68.54%)</b></td><td>211.50 <b>(+33.95%)</b></td><td>168.28 (+19.18%)</td><td>185.00 <b>(+28.74%)</b></td><td>122.00 (-0.49%)</td><td>37.98 <b>(+120.31%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>157.90 (n/a)</td><td>141.20 (n/a)</td><td>143.70 (n/a)</td><td>122.60 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (-11.04%)</td><td>0.12 (-10.11%)</td><td>0.12 (-8.74%)</td><td>0.09 (-3.32%)</td><td>0.02 <b>(-25.86%)</b></td><td>218.70 (+3.45%)</td><td>179.92 (+9.85%)</td><td>169.50 (+9.57%)</td><td>141.50 (+12.39%)</td><td>30.15 (-13.73%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>211.40 (n/a)</td><td>163.78 (n/a)</td><td>154.70 (n/a)</td><td>125.90 (n/a)</td><td>34.95 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 <b>(+25.28%)</b></td><td>0.12 (+14.51%)</td><td>0.11 (+7.72%)</td><td>0.10 (+10.78%)</td><td>0.02 <b>(+109.84%)</b></td><td>196.90 (-9.72%)</td><td>173.28 (-11.83%)</td><td>182.60 (-7.17%)</td><td>141.90 <b>(-20.19%)</b></td><td>22.18 <b>(+49.95%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>196.54 (n/a)</td><td>196.70 (n/a)</td><td>177.80 (n/a)</td><td>14.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 <b>(+21.25%)</b></td><td>0.12 (+1.48%)</td><td>0.11 (-0.49%)</td><td>0.08 (-18.75%)</td><td>0.03 <b>(+120.17%)</b></td><td>253.70 <b>(+23.10%)</b></td><td>185.80 (+2.02%)</td><td>186.70 (+0.48%)</td><td>133.90 (-17.55%)</td><td>44.31 <b>(+129.86%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>206.10 (n/a)</td><td>182.12 (n/a)</td><td>185.80 (n/a)</td><td>162.40 (n/a)</td><td>19.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.18 (-19.81%)</td><td>0.14 (-9.02%)</td><td>0.13 (-6.77%)</td><td>0.12 (-9.03%)</td><td>0.02 <b>(-39.29%)</b></td><td>210.10 (+9.94%)</td><td>177.10 (+7.66%)</td><td>184.50 (+7.27%)</td><td>136.90 <b>(+24.68%)</b></td><td>27.67 (-17.32%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>191.10 (n/a)</td><td>164.50 (n/a)</td><td>172.00 (n/a)</td><td>109.80 (n/a)</td><td>33.47 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (-12.46%)</td><td>0.14 (-11.54%)</td><td>0.16 (-5.77%)</td><td>0.10 (-11.53%)</td><td>0.03 (-6.00%)</td><td>239.60 (+13.07%)</td><td>178.10 (+13.74%)</td><td>155.00 (+6.09%)</td><td>141.10 (+14.25%)</td><td>45.33 <b>(+21.45%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>211.90 (n/a)</td><td>156.58 (n/a)</td><td>146.10 (n/a)</td><td>123.50 (n/a)</td><td>37.33 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (-0.04%)</td><td>0.15 (-0.45%)</td><td>0.16 (-2.58%)</td><td>0.11 (-0.25%)</td><td>0.04 (-0.55%)</td><td>220.10 (+0.23%)</td><td>169.34 (+0.39%)</td><td>155.80 (+2.70%)</td><td>128.80 (+0.08%)</td><td>41.24 (-0.95%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>219.60 (n/a)</td><td>168.68 (n/a)</td><td>151.70 (n/a)</td><td>128.70 (n/a)</td><td>41.63 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (+1.86%)</td><td>0.17 <b>(+24.57%)</b></td><td>0.16 <b>(+41.66%)</b></td><td>0.14 <b>(+40.28%)</b></td><td>0.03 <b>(-28.17%)</b></td><td>178.60 <b>(-28.70%)</b></td><td>148.12 <b>(-23.01%)</b></td><td>152.20 <b>(-29.41%)</b></td><td>120.30 (-1.88%)</td><td>25.68 <b>(-50.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>250.50 (n/a)</td><td>192.40 (n/a)</td><td>215.60 (n/a)</td><td>122.60 (n/a)</td><td>51.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (+9.88%)</td><td>0.17 (+1.38%)</td><td>0.16 (-1.15%)</td><td>0.13 (-6.79%)</td><td>0.04 <b>(+49.26%)</b></td><td>194.20 (+7.29%)</td><td>153.90 (+0.58%)</td><td>158.20 (+1.22%)</td><td>110.60 (-8.97%)</td><td>31.51 <b>(+45.91%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.00 (n/a)</td><td>153.02 (n/a)</td><td>156.30 (n/a)</td><td>121.50 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (+6.02%)</td><td>0.15 (+5.53%)</td><td>0.14 (+13.11%)</td><td>0.11 (-7.38%)</td><td>0.04 <b>(+25.84%)</b></td><td>225.30 (+7.95%)</td><td>170.58 (-3.10%)</td><td>174.70 (-11.59%)</td><td>116.80 (-5.73%)</td><td>46.30 <b>(+26.07%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>208.70 (n/a)</td><td>176.04 (n/a)</td><td>197.60 (n/a)</td><td>123.90 (n/a)</td><td>36.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (-2.62%)</td><td>0.16 (+9.68%)</td><td>0.16 (+10.04%)</td><td>0.13 <b>(+20.57%)</b></td><td>0.02 <b>(-38.12%)</b></td><td>185.10 (-17.03%)</td><td>156.78 (-11.15%)</td><td>155.10 (-9.14%)</td><td>130.30 (+2.68%)</td><td>19.82 <b>(-47.57%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>223.10 (n/a)</td><td>176.46 (n/a)</td><td>170.70 (n/a)</td><td>126.90 (n/a)</td><td>37.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 <b>(+37.36%)</b></td><td>0.16 <b>(+23.80%)</b></td><td>0.15 <b>(+25.51%)</b></td><td>0.13 (+11.30%)</td><td>0.02 <b>(+119.41%)</b></td><td>190.70 (-10.13%)</td><td>161.24 (-18.24%)</td><td>163.40 <b>(-20.33%)</b></td><td>125.70 <b>(-27.17%)</b></td><td>23.15 <b>(+39.37%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>197.20 (n/a)</td><td>205.10 (n/a)</td><td>172.60 (n/a)</td><td>16.61 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (+4.62%)</td><td>0.12 (-4.71%)</td><td>0.12 (-6.18%)</td><td>0.11 (-9.87%)</td><td>0.01 <b>(+118.59%)</b></td><td>172.20 (+10.95%)</td><td>154.62 (+5.56%)</td><td>156.20 (+6.55%)</td><td>131.80 (-4.42%)</td><td>14.49 <b>(+127.86%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>155.20 (n/a)</td><td>146.48 (n/a)</td><td>146.60 (n/a)</td><td>137.90 (n/a)</td><td>6.36 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (-11.06%)</td><td>0.14 (+2.51%)</td><td>0.14 (+16.92%)</td><td>0.12 <b>(+20.86%)</b></td><td>0.01 <b>(-60.00%)</b></td><td>151.90 (-17.22%)</td><td>136.98 (-6.29%)</td><td>136.00 (-14.52%)</td><td>119.20 (+12.45%)</td><td>13.02 <b>(-61.88%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>183.50 (n/a)</td><td>146.18 (n/a)</td><td>159.10 (n/a)</td><td>106.00 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (-2.33%)</td><td>0.10 (-17.79%)</td><td>0.10 <b>(-25.22%)</b></td><td>0.07 <b>(-33.42%)</b></td><td>0.03 <b>(+76.60%)</b></td><td>251.80 <b>(+50.24%)</b></td><td>187.18 <b>(+26.95%)</b></td><td>191.70 <b>(+33.78%)</b></td><td>131.30 (+2.34%)</td><td>48.34 <b>(+164.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>167.60 (n/a)</td><td>147.44 (n/a)</td><td>143.30 (n/a)</td><td>128.30 (n/a)</td><td>18.25 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (+2.20%)</td><td>0.12 (-6.28%)</td><td>0.12 (-13.66%)</td><td>0.09 (-12.59%)</td><td>0.02 <b>(+20.84%)</b></td><td>197.90 (+14.46%)</td><td>155.54 (+7.95%)</td><td>149.70 (+15.78%)</td><td>123.40 (-2.14%)</td><td>30.68 <b>(+36.14%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>172.90 (n/a)</td><td>144.08 (n/a)</td><td>129.30 (n/a)</td><td>126.10 (n/a)</td><td>22.54 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (-13.72%)</td><td>0.12 (-2.14%)</td><td>0.13 (+7.03%)</td><td>0.11 (-5.65%)</td><td>0.01 <b>(-38.28%)</b></td><td>171.70 (+5.99%)</td><td>151.02 (+1.34%)</td><td>146.10 (-6.59%)</td><td>133.20 (+15.93%)</td><td>15.01 <b>(-22.09%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>162.00 (n/a)</td><td>149.02 (n/a)</td><td>156.40 (n/a)</td><td>114.90 (n/a)</td><td>19.27 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (+4.33%)</td><td>0.10 (+4.20%)</td><td>0.12 <b>(+22.12%)</b></td><td>0.08 (-2.18%)</td><td>0.03 <b>(+38.22%)</b></td><td>243.00 (+2.23%)</td><td>185.68 (-1.66%)</td><td>157.30 (-18.12%)</td><td>139.70 (-4.12%)</td><td>47.71 <b>(+40.40%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>237.70 (n/a)</td><td>188.82 (n/a)</td><td>192.10 (n/a)</td><td>145.70 (n/a)</td><td>33.98 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (-11.76%)</td><td>0.11 (-3.39%)</td><td>0.11 (+1.07%)</td><td>0.08 (-1.17%)</td><td>0.01 <b>(-33.51%)</b></td><td>223.70 (+1.18%)</td><td>177.78 (+2.08%)</td><td>165.80 (-1.07%)</td><td>160.90 (+13.31%)</td><td>26.46 <b>(-21.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>221.10 (n/a)</td><td>174.16 (n/a)</td><td>167.60 (n/a)</td><td>142.00 (n/a)</td><td>33.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (+9.39%)</td><td>0.11 (+2.01%)</td><td>0.11 (+0.34%)</td><td>0.10 (+11.18%)</td><td>0.02 (+3.45%)</td><td>177.70 (-10.07%)</td><td>162.62 (-2.13%)</td><td>169.10 (-0.35%)</td><td>129.60 (-8.54%)</td><td>19.27 (-15.29%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>197.60 (n/a)</td><td>166.16 (n/a)</td><td>169.70 (n/a)</td><td>141.70 (n/a)</td><td>22.75 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.59 <b>(-26.15%)</b></td><td>0.56 (-16.10%)</td><td>0.56 <b>(-21.82%)</b></td><td>0.53 (+9.86%)</td><td>0.02 <b>(-80.63%)</b></td><td>184.70 (-8.97%)</td><td>176.32 (+15.74%)</td><td>176.80 <b>(+27.93%)</b></td><td>167.60 <b>(+35.49%)</b></td><td>7.45 <b>(-76.49%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.79 (n/a)</td><td>0.67 (n/a)</td><td>0.71 (n/a)</td><td>0.48 (n/a)</td><td>0.12 (n/a)</td><td>202.90 (n/a)</td><td>152.34 (n/a)</td><td>138.20 (n/a)</td><td>123.70 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.81 (+12.02%)</td><td>0.75 <b>(+26.34%)</b></td><td>0.75 <b>(+24.99%)</b></td><td>0.69 <b>(+51.21%)</b></td><td>0.04 <b>(-55.98%)</b></td><td>142.90 <b>(-33.84%)</b></td><td>132.04 <b>(-22.48%)</b></td><td>131.60 <b>(-20.00%)</b></td><td>121.40 (-10.74%)</td><td>7.72 <b>(-74.26%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.72 (n/a)</td><td>0.59 (n/a)</td><td>0.60 (n/a)</td><td>0.46 (n/a)</td><td>0.10 (n/a)</td><td>216.00 (n/a)</td><td>170.34 (n/a)</td><td>164.50 (n/a)</td><td>136.00 (n/a)</td><td>29.99 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.87 <b>(+26.87%)</b></td><td>0.71 (+18.85%)</td><td>0.69 (+8.71%)</td><td>0.58 <b>(+20.89%)</b></td><td>0.10 (+19.82%)</td><td>169.80 (-17.29%)</td><td>141.40 (-15.99%)</td><td>142.50 (-8.01%)</td><td>113.20 <b>(-21.17%)</b></td><td>20.07 <b>(-23.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.68 (n/a)</td><td>0.59 (n/a)</td><td>0.63 (n/a)</td><td>0.48 (n/a)</td><td>0.09 (n/a)</td><td>205.30 (n/a)</td><td>168.32 (n/a)</td><td>154.90 (n/a)</td><td>143.60 (n/a)</td><td>26.10 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.81 (-16.54%)</td><td>0.64 (+2.59%)</td><td>0.72 (+12.65%)</td><td>0.46 <b>(+26.07%)</b></td><td>0.16 <b>(-40.05%)</b></td><td>214.70 <b>(-20.69%)</b></td><td>160.86 (-11.48%)</td><td>137.20 (-11.20%)</td><td>121.80 (+19.88%)</td><td>42.28 <b>(-45.49%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.97 (n/a)</td><td>0.63 (n/a)</td><td>0.64 (n/a)</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>270.70 (n/a)</td><td>181.72 (n/a)</td><td>154.50 (n/a)</td><td>101.60 (n/a)</td><td>77.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.67 (+11.86%)</td><td>0.49 (-1.12%)</td><td>0.48 (-0.77%)</td><td>0.19 <b>(-54.32%)</b></td><td>0.19 <b>(+163.83%)</b></td><td>385.90 <b>(+118.89%)</b></td><td>184.64 <b>(+21.75%)</b></td><td>152.60 (+0.79%)</td><td>110.10 (-10.56%)</td><td>114.46 <b>(+442.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.60 (n/a)</td><td>0.49 (n/a)</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.07 (n/a)</td><td>176.30 (n/a)</td><td>151.66 (n/a)</td><td>151.40 (n/a)</td><td>123.10 (n/a)</td><td>21.08 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.56 (-4.25%)</td><td>0.46 (-2.21%)</td><td>0.46 (+8.80%)</td><td>0.35 (-10.69%)</td><td>0.10 (+4.43%)</td><td>210.90 (+11.94%)</td><td>165.68 (+3.03%)</td><td>159.90 (-8.10%)</td><td>130.50 (+4.48%)</td><td>36.37 (+19.75%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.59 (n/a)</td><td>0.47 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.10 (n/a)</td><td>188.40 (n/a)</td><td>160.80 (n/a)</td><td>174.00 (n/a)</td><td>124.90 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.60 (+19.17%)</td><td>0.47 (+6.68%)</td><td>0.41 (-8.13%)</td><td>0.36 (+10.60%)</td><td>0.10 <b>(+40.69%)</b></td><td>203.80 (-9.58%)</td><td>163.42 (-5.15%)</td><td>178.20 (+8.86%)</td><td>122.20 (-16.07%)</td><td>34.11 (+4.69%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>225.40 (n/a)</td><td>172.30 (n/a)</td><td>163.70 (n/a)</td><td>145.60 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.63 <b>(+36.84%)</b></td><td>0.40 (+3.58%)</td><td>0.36 (-10.55%)</td><td>0.28 (-3.82%)</td><td>0.13 <b>(+107.47%)</b></td><td>267.30 (+3.97%)</td><td>198.06 (+1.30%)</td><td>203.10 (+11.78%)</td><td>117.80 <b>(-26.92%)</b></td><td>54.47 <b>(+46.37%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.06 (n/a)</td><td>257.10 (n/a)</td><td>195.52 (n/a)</td><td>181.70 (n/a)</td><td>161.20 (n/a)</td><td>37.21 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.34 (+6.77%)</td><td>0.25 (-7.40%)</td><td>0.26 (-5.55%)</td><td>0.16 (-13.16%)</td><td>0.06 <b>(+28.41%)</b></td><td>229.20 (+15.18%)</td><td>157.86 (+10.65%)</td><td>144.40 (+5.94%)</td><td>109.40 (-6.34%)</td><td>44.76 <b>(+37.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>199.00 (n/a)</td><td>142.66 (n/a)</td><td>136.30 (n/a)</td><td>116.80 (n/a)</td><td>32.66 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (+1.75%)</td><td>0.22 (-8.52%)</td><td>0.20 (-17.10%)</td><td>0.17 (-15.19%)</td><td>0.05 <b>(+75.31%)</b></td><td>214.50 (+17.92%)</td><td>174.90 (+11.94%)</td><td>181.90 <b>(+20.62%)</b></td><td>133.10 (-1.70%)</td><td>34.72 <b>(+100.00%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>181.90 (n/a)</td><td>156.24 (n/a)</td><td>150.80 (n/a)</td><td>135.40 (n/a)</td><td>17.36 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (-1.46%)</td><td>0.23 (+1.85%)</td><td>0.22 (+6.76%)</td><td>0.19 (-5.22%)</td><td>0.04 (-5.64%)</td><td>195.50 (+5.50%)</td><td>163.90 (-1.94%)</td><td>165.90 (-6.32%)</td><td>125.90 (+1.45%)</td><td>25.20 (+0.27%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>185.30 (n/a)</td><td>167.14 (n/a)</td><td>177.10 (n/a)</td><td>124.10 (n/a)</td><td>25.14 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (-5.90%)</td><td>0.23 (+0.26%)</td><td>0.22 (-5.58%)</td><td>0.20 <b>(+22.28%)</b></td><td>0.03 <b>(-40.64%)</b></td><td>183.80 (-18.20%)</td><td>164.92 (-3.05%)</td><td>168.00 (+5.93%)</td><td>136.40 (+6.23%)</td><td>20.50 <b>(-47.95%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>224.70 (n/a)</td><td>170.10 (n/a)</td><td>158.60 (n/a)</td><td>128.40 (n/a)</td><td>39.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (+19.78%)</td><td>0.23 (+6.30%)</td><td>0.22 (+2.40%)</td><td>0.17 (-0.08%)</td><td>0.04 <b>(+63.05%)</b></td><td>214.90 (+0.09%)</td><td>168.04 (-4.39%)</td><td>166.70 (-2.34%)</td><td>129.40 (-16.52%)</td><td>32.68 <b>(+35.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>214.70 (n/a)</td><td>175.76 (n/a)</td><td>170.70 (n/a)</td><td>155.00 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (+1.41%)</td><td>0.19 (-18.67%)</td><td>0.17 <b>(-28.37%)</b></td><td>0.12 <b>(-33.18%)</b></td><td>0.07 <b>(+62.50%)</b></td><td>315.00 <b>(+49.64%)</b></td><td>213.36 <b>(+31.72%)</b></td><td>215.30 <b>(+39.62%)</b></td><td>125.60 (-1.34%)</td><td>71.55 <b>(+131.83%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>210.50 (n/a)</td><td>161.98 (n/a)</td><td>154.20 (n/a)</td><td>127.30 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (-6.87%)</td><td>0.23 (-3.95%)</td><td>0.23 (+3.91%)</td><td>0.19 (-8.49%)</td><td>0.05 (-9.21%)</td><td>195.90 (+9.26%)</td><td>164.00 (+4.01%)</td><td>160.20 (-3.73%)</td><td>119.70 (+7.35%)</td><td>29.21 (+7.71%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>179.30 (n/a)</td><td>157.68 (n/a)</td><td>166.40 (n/a)</td><td>111.50 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (+2.67%)</td><td>0.23 (+0.73%)</td><td>0.23 (-3.72%)</td><td>0.21 <b>(+42.54%)</b></td><td>0.02 <b>(-48.92%)</b></td><td>179.10 <b>(-29.85%)</b></td><td>161.58 (-4.65%)</td><td>159.50 (+3.84%)</td><td>137.20 (-2.56%)</td><td>16.28 <b>(-66.34%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>255.30 (n/a)</td><td>169.46 (n/a)</td><td>153.60 (n/a)</td><td>140.80 (n/a)</td><td>48.35 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.33 (-9.52%)</td><td>0.25 (-17.90%)</td><td>0.21 <b>(-27.28%)</b></td><td>0.18 <b>(-30.53%)</b></td><td>0.07 <b>(+72.20%)</b></td><td>228.70 <b>(+43.93%)</b></td><td>174.20 <b>(+27.56%)</b></td><td>193.20 <b>(+37.51%)</b></td><td>125.90 (+10.54%)</td><td>45.95 <b>(+159.62%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>158.90 (n/a)</td><td>136.56 (n/a)</td><td>140.50 (n/a)</td><td>113.90 (n/a)</td><td>17.70 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (-12.92%)</td><td>0.23 (-9.70%)</td><td>0.22 (-13.19%)</td><td>0.19 (-0.33%)</td><td>0.05 <b>(-26.07%)</b></td><td>220.30 (+0.32%)</td><td>180.68 (+8.94%)</td><td>183.80 (+15.16%)</td><td>131.80 (+14.91%)</td><td>31.72 (-16.84%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>219.60 (n/a)</td><td>165.86 (n/a)</td><td>159.60 (n/a)</td><td>114.70 (n/a)</td><td>38.15 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (-15.44%)</td><td>0.25 (-6.09%)</td><td>0.25 (-2.58%)</td><td>0.21 (+5.62%)</td><td>0.03 <b>(-44.26%)</b></td><td>192.80 (-5.30%)</td><td>167.10 (+4.40%)</td><td>162.20 (+2.66%)</td><td>141.30 (+18.24%)</td><td>19.52 <b>(-37.06%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>203.60 (n/a)</td><td>160.06 (n/a)</td><td>158.00 (n/a)</td><td>119.50 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (-17.27%)</td><td>0.26 (-6.21%)</td><td>0.26 (-1.08%)</td><td>0.22 (+1.79%)</td><td>0.03 <b>(-55.69%)</b></td><td>183.20 (-1.77%)</td><td>161.46 (+3.85%)</td><td>160.10 (+1.14%)</td><td>145.40 <b>(+20.86%)</b></td><td>16.20 <b>(-48.49%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>186.50 (n/a)</td><td>155.48 (n/a)</td><td>158.30 (n/a)</td><td>120.30 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (+4.13%)</td><td>0.24 (-0.29%)</td><td>0.25 (+5.48%)</td><td>0.19 (-1.41%)</td><td>0.04 <b>(+29.49%)</b></td><td>212.40 (+1.43%)</td><td>176.88 (+1.26%)</td><td>161.10 (-5.24%)</td><td>145.60 (-3.96%)</td><td>30.95 <b>(+30.41%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>209.40 (n/a)</td><td>174.68 (n/a)</td><td>170.00 (n/a)</td><td>151.60 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (-11.43%)</td><td>0.24 (-4.96%)</td><td>0.24 (+0.46%)</td><td>0.20 (-12.27%)</td><td>0.03 (-13.00%)</td><td>203.30 (+14.02%)</td><td>172.90 (+5.17%)</td><td>173.30 (-0.46%)</td><td>153.00 (+12.92%)</td><td>20.38 (+10.19%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>178.30 (n/a)</td><td>164.40 (n/a)</td><td>174.10 (n/a)</td><td>135.50 (n/a)</td><td>18.49 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (+10.44%)</td><td>0.25 (+9.14%)</td><td>0.25 (+18.01%)</td><td>0.20 (-4.34%)</td><td>0.04 <b>(+27.42%)</b></td><td>209.50 (+4.49%)</td><td>165.76 (-7.71%)</td><td>161.80 (-15.24%)</td><td>133.60 (-9.42%)</td><td>27.39 <b>(+22.61%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>200.50 (n/a)</td><td>179.60 (n/a)</td><td>190.90 (n/a)</td><td>147.50 (n/a)</td><td>22.33 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 <b>(-26.04%)</b></td><td>0.24 (+1.21%)</td><td>0.23 (+15.27%)</td><td>0.21 <b>(+23.12%)</b></td><td>0.03 <b>(-62.80%)</b></td><td>196.10 (-18.77%)</td><td>174.24 (-8.26%)</td><td>179.00 (-13.23%)</td><td>140.60 <b>(+35.19%)</b></td><td>22.97 <b>(-57.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.39 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>241.40 (n/a)</td><td>189.92 (n/a)</td><td>206.30 (n/a)</td><td>104.00 (n/a)</td><td>53.47 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (+1.18%)</td><td>0.20 <b>(-24.26%)</b></td><td>0.20 <b>(-24.80%)</b></td><td>0.13 <b>(-42.75%)</b></td><td>0.07 <b>(+154.92%)</b></td><td>259.40 <b>(+74.68%)</b></td><td>191.44 <b>(+44.13%)</b></td><td>173.30 <b>(+33.00%)</b></td><td>113.10 (-1.14%)</td><td>63.59 <b>(+360.75%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>148.50 (n/a)</td><td>132.82 (n/a)</td><td>130.30 (n/a)</td><td>114.40 (n/a)</td><td>13.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (-17.98%)</td><td>0.18 <b>(-31.63%)</b></td><td>0.19 <b>(-30.11%)</b></td><td>0.09 <b>(-52.31%)</b></td><td>0.06 <b>(+37.52%)</b></td><td>372.10 <b>(+109.75%)</b></td><td>214.90 <b>(+59.37%)</b></td><td>183.00 <b>(+43.08%)</b></td><td>137.80 <b>(+21.95%)</b></td><td>91.24 <b>(+265.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>177.40 (n/a)</td><td>134.84 (n/a)</td><td>127.90 (n/a)</td><td>113.00 (n/a)</td><td>24.97 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (-0.04%)</td><td>0.23 (+3.12%)</td><td>0.22 (+11.37%)</td><td>0.19 (-0.44%)</td><td>0.05 (-1.89%)</td><td>184.90 (+0.49%)</td><td>157.52 (-3.05%)</td><td>158.60 (-10.19%)</td><td>113.70 (+0.09%)</td><td>29.66 (+0.59%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>184.00 (n/a)</td><td>162.48 (n/a)</td><td>176.60 (n/a)</td><td>113.60 (n/a)</td><td>29.48 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (+3.16%)</td><td>0.24 (+8.68%)</td><td>0.25 (+10.62%)</td><td>0.17 (-0.80%)</td><td>0.05 (+6.79%)</td><td>206.20 (+0.78%)</td><td>152.44 (-7.70%)</td><td>137.60 (-9.59%)</td><td>121.90 (-3.10%)</td><td>33.79 (+3.41%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>204.60 (n/a)</td><td>165.16 (n/a)</td><td>152.20 (n/a)</td><td>125.80 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.26 (+5.42%)</td><td>0.21 (+0.23%)</td><td>0.20 (-2.56%)</td><td>0.18 (+0.84%)</td><td>0.03 <b>(+23.20%)</b></td><td>193.50 (-0.82%)</td><td>171.60 (+0.34%)</td><td>174.00 (+2.65%)</td><td>133.00 (-5.14%)</td><td>24.72 (+16.35%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>195.10 (n/a)</td><td>171.02 (n/a)</td><td>169.50 (n/a)</td><td>140.20 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (-0.34%)</td><td>0.23 (+8.97%)</td><td>0.24 (+13.97%)</td><td>0.14 (-1.92%)</td><td>0.06 (+17.06%)</td><td>243.10 (+1.93%)</td><td>164.32 (-6.72%)</td><td>145.20 (-12.27%)</td><td>126.50 (+0.40%)</td><td>48.81 (+17.16%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>238.50 (n/a)</td><td>176.16 (n/a)</td><td>165.50 (n/a)</td><td>126.00 (n/a)</td><td>41.66 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (+3.71%)</td><td>0.26 <b>(+27.32%)</b></td><td>0.27 <b>(+26.93%)</b></td><td>0.19 <b>(+42.75%)</b></td><td>0.04 <b>(-36.20%)</b></td><td>180.20 <b>(-29.97%)</b></td><td>138.44 <b>(-25.18%)</b></td><td>130.70 <b>(-21.27%)</b></td><td>121.40 (-3.50%)</td><td>23.74 <b>(-56.47%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>257.30 (n/a)</td><td>185.02 (n/a)</td><td>166.00 (n/a)</td><td>125.80 (n/a)</td><td>54.53 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.30 <b>(+34.21%)</b></td><td>0.22 (+17.00%)</td><td>0.22 (+15.05%)</td><td>0.19 (+13.70%)</td><td>0.05 <b>(+79.99%)</b></td><td>183.60 (-12.07%)</td><td>159.38 (-13.33%)</td><td>160.80 (-13.08%)</td><td>114.70 <b>(-25.52%)</b></td><td>26.99 (+13.84%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>208.80 (n/a)</td><td>183.90 (n/a)</td><td>185.00 (n/a)</td><td>154.00 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.02 (-2.13%)</td><td>0.87 <b>(+20.80%)</b></td><td>0.94 <b>(+34.94%)</b></td><td>0.67 <b>(+25.29%)</b></td><td>0.15 <b>(-22.94%)</b></td><td>197.00 <b>(-20.18%)</b></td><td>155.18 (-19.30%)</td><td>140.00 <b>(-25.93%)</b></td><td>128.70 (+2.14%)</td><td>29.33 <b>(-35.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.04 (n/a)</td><td>0.72 (n/a)</td><td>0.69 (n/a)</td><td>0.53 (n/a)</td><td>0.20 (n/a)</td><td>246.80 (n/a)</td><td>192.30 (n/a)</td><td>189.00 (n/a)</td><td>126.00 (n/a)</td><td>45.52 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.88 <b>(+20.55%)</b></td><td>0.72 (+6.40%)</td><td>0.76 (+8.92%)</td><td>0.49 (-17.90%)</td><td>0.16 <b>(+202.93%)</b></td><td>265.60 <b>(+21.83%)</b></td><td>190.46 (-2.10%)</td><td>173.10 (-8.17%)</td><td>148.40 (-17.00%)</td><td>48.24 <b>(+204.30%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.73 (n/a)</td><td>0.68 (n/a)</td><td>0.70 (n/a)</td><td>0.60 (n/a)</td><td>0.05 (n/a)</td><td>218.00 (n/a)</td><td>194.54 (n/a)</td><td>188.50 (n/a)</td><td>178.80 (n/a)</td><td>15.85 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.17 <b>(+52.99%)</b></td><td>0.83 <b>(+23.99%)</b></td><td>0.81 (+9.79%)</td><td>0.46 (+10.67%)</td><td>0.26 <b>(+76.78%)</b></td><td>286.40 (-9.65%)</td><td>174.38 (-15.89%)</td><td>161.10 (-8.93%)</td><td>111.80 <b>(-34.66%)</b></td><td>66.70 (+7.31%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.77 (n/a)</td><td>0.67 (n/a)</td><td>0.74 (n/a)</td><td>0.41 (n/a)</td><td>0.15 (n/a)</td><td>317.00 (n/a)</td><td>207.32 (n/a)</td><td>176.90 (n/a)</td><td>171.10 (n/a)</td><td>62.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (+13.00%)</td><td>0.03 <b>(+21.43%)</b></td><td>0.03 <b>(+30.01%)</b></td><td>0.02 <b>(+23.65%)</b></td><td>0.00 <b>(+25.07%)</b></td><td>176.80 (-19.12%)</td><td>144.70 (-17.43%)</td><td>129.40 <b>(-23.07%)</b></td><td>123.60 (-11.52%)</td><td>26.28 (-11.57%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.60 (n/a)</td><td>175.24 (n/a)</td><td>168.20 (n/a)</td><td>139.70 (n/a)</td><td>29.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 <b>(+44.02%)</b></td><td>0.02 (+9.56%)</td><td>0.02 (+3.39%)</td><td>0.02 (-15.18%)</td><td>0.01 <b>(+166.35%)</b></td><td>245.70 (+17.90%)</td><td>176.56 (-3.62%)</td><td>170.00 (-3.30%)</td><td>111.10 <b>(-30.56%)</b></td><td>49.20 <b>(+110.13%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>183.20 (n/a)</td><td>175.80 (n/a)</td><td>160.00 (n/a)</td><td>23.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-19.55%)</td><td>0.02 (-2.95%)</td><td>0.02 (+7.86%)</td><td>0.02 (+0.77%)</td><td>0.00 <b>(-35.76%)</b></td><td>206.40 (-0.77%)</td><td>176.46 (+1.59%)</td><td>165.60 (-7.28%)</td><td>152.80 <b>(+24.33%)</b></td><td>26.09 (-16.41%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>173.70 (n/a)</td><td>178.60 (n/a)</td><td>122.90 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.68 (-19.26%)</td><td>12.56 (-3.90%)</td><td>12.47 (-2.29%)</td><td>11.59 (+16.53%)</td><td>0.98 <b>(-61.72%)</b></td><td>181.10 (-14.17%)</td><td>167.84 (+1.49%)</td><td>168.30 (+2.37%)</td><td>153.40 <b>(+23.81%)</b></td><td>13.02 <b>(-58.86%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>16.94 (n/a)</td><td>13.07 (n/a)</td><td>12.76 (n/a)</td><td>9.94 (n/a)</td><td>2.56 (n/a)</td><td>211.00 (n/a)</td><td>165.38 (n/a)</td><td>164.40 (n/a)</td><td>123.90 (n/a)</td><td>31.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.86 (-3.80%)</td><td>0.74 (-5.82%)</td><td>0.73 (-6.96%)</td><td>0.68 (+5.16%)</td><td>0.07 <b>(-26.58%)</b></td><td>195.60 (-4.91%)</td><td>179.12 (+5.51%)</td><td>181.70 (+7.51%)</td><td>152.90 (+3.94%)</td><td>16.18 <b>(-28.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.90 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.64 (n/a)</td><td>0.10 (n/a)</td><td>205.70 (n/a)</td><td>169.76 (n/a)</td><td>169.00 (n/a)</td><td>147.10 (n/a)</td><td>22.78 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.19 <b>(+28.11%)</b></td><td>0.97 (+16.93%)</td><td>0.99 (+16.95%)</td><td>0.67 (+0.30%)</td><td>0.19 <b>(+91.51%)</b></td><td>196.80 (-0.25%)</td><td>141.52 (-12.36%)</td><td>134.10 (-14.48%)</td><td>110.70 <b>(-21.99%)</b></td><td>33.16 <b>(+52.29%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.93 (n/a)</td><td>0.83 (n/a)</td><td>0.84 (n/a)</td><td>0.67 (n/a)</td><td>0.10 (n/a)</td><td>197.30 (n/a)</td><td>161.48 (n/a)</td><td>156.80 (n/a)</td><td>141.90 (n/a)</td><td>21.77 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.80 (-9.76%)</td><td>0.75 (+3.71%)</td><td>0.76 (+9.97%)</td><td>0.68 (+12.62%)</td><td>0.04 <b>(-61.31%)</b></td><td>194.30 (-11.24%)</td><td>176.80 (-5.14%)</td><td>173.20 (-9.03%)</td><td>166.00 (+10.81%)</td><td>10.84 <b>(-61.59%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.88 (n/a)</td><td>0.72 (n/a)</td><td>0.69 (n/a)</td><td>0.60 (n/a)</td><td>0.11 (n/a)</td><td>218.90 (n/a)</td><td>186.38 (n/a)</td><td>190.40 (n/a)</td><td>149.80 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.87 (+17.17%)</td><td>0.77 (+14.05%)</td><td>0.83 <b>(+20.06%)</b></td><td>0.62 (+11.37%)</td><td>0.13 <b>(+74.64%)</b></td><td>212.90 (-10.24%)</td><td>175.96 (-11.19%)</td><td>159.20 (-16.69%)</td><td>151.00 (-14.64%)</td><td>30.42 <b>(+30.58%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.69 (n/a)</td><td>0.56 (n/a)</td><td>0.07 (n/a)</td><td>237.20 (n/a)</td><td>198.14 (n/a)</td><td>191.10 (n/a)</td><td>176.90 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.98 (+2.20%)</td><td>0.79 (+1.57%)</td><td>0.83 (+9.54%)</td><td>0.53 (-12.15%)</td><td>0.16 <b>(+25.67%)</b></td><td>248.00 (+13.87%)</td><td>173.94 (+0.28%)</td><td>159.40 (-8.71%)</td><td>135.40 (-2.17%)</td><td>43.20 <b>(+46.61%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.95 (n/a)</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.61 (n/a)</td><td>0.13 (n/a)</td><td>217.80 (n/a)</td><td>173.46 (n/a)</td><td>174.60 (n/a)</td><td>138.40 (n/a)</td><td>29.47 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (-5.20%)</td><td>0.02 (-9.49%)</td><td>0.02 (-9.11%)</td><td>0.02 (-12.65%)</td><td>0.01 (+8.37%)</td><td>243.00 (+14.51%)</td><td>189.64 (+12.12%)</td><td>168.60 (+10.05%)</td><td>145.40 (+5.52%)</td><td>47.25 <b>(+34.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.20 (n/a)</td><td>169.14 (n/a)</td><td>153.20 (n/a)</td><td>137.80 (n/a)</td><td>35.19 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (+0.63%)</td><td>0.02 (-6.72%)</td><td>0.02 (-9.44%)</td><td>0.02 (-18.54%)</td><td>0.01 <b>(+67.63%)</b></td><td>241.70 <b>(+22.75%)</b></td><td>185.66 (+11.25%)</td><td>183.10 (+10.43%)</td><td>133.00 (-0.67%)</td><td>46.87 <b>(+108.62%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.90 (n/a)</td><td>166.88 (n/a)</td><td>165.80 (n/a)</td><td>133.90 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.00 (-2.17%)</td><td>0.00 (+0.94%)</td><td>0.00 (+4.76%)</td><td>0.00 (+0.00%)</td><td>0.00 (-8.71%)</td><td>1018.78 (-1.28%)</td><td>950.14 (-1.42%)</td><td>932.59 (-3.41%)</td><td>902.06 (+0.44%)</td><td>46.82 (-2.32%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1032.02 (n/a)</td><td>963.81 (n/a)</td><td>965.48 (n/a)</td><td>898.11 (n/a)</td><td>47.93 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.01 (+0.00%)</td><td>0.01 (+2.02%)</td><td>0.01 (+1.25%)</td><td>0.01 (+6.76%)</td><td>0.00 <b>(-40.71%)</b></td><td>1038.05 (-6.75%)</td><td>1009.52 (-2.51%)</td><td>1005.71 (-2.22%)</td><td>973.09 (+0.09%)</td><td>26.86 <b>(-46.86%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1113.23 (n/a)</td><td>1035.52 (n/a)</td><td>1028.52 (n/a)</td><td>972.24 (n/a)</td><td>50.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.97 (-3.28%)</td><td>0.96 (-0.30%)</td><td>0.96 (+0.73%)</td><td>0.95 (+0.42%)</td><td>0.01 <b>(-66.63%)</b></td><td>2205.59 (-0.43%)</td><td>2183.91 (+0.26%)</td><td>2177.48 (-0.73%)</td><td>2164.45 (+3.39%)</td><td>16.71 <b>(-65.51%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.00 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2215.08 (n/a)</td><td>2178.21 (n/a)</td><td>2193.44 (n/a)</td><td>2093.42 (n/a)</td><td>48.46 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.93 (+16.71%)</td><td>4.94 (+6.65%)</td><td>4.43 (-5.63%)</td><td>4.11 (+3.18%)</td><td>0.86 <b>(+114.23%)</b></td><td>255.20 (-3.08%)</td><td>217.16 (-4.61%)</td><td>236.80 (+5.95%)</td><td>177.00 (-14.29%)</td><td>36.14 <b>(+69.67%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.08 (n/a)</td><td>4.64 (n/a)</td><td>4.69 (n/a)</td><td>3.98 (n/a)</td><td>0.40 (n/a)</td><td>263.30 (n/a)</td><td>227.66 (n/a)</td><td>223.50 (n/a)</td><td>206.50 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.82 (-1.63%)</td><td>4.70 (-3.32%)</td><td>4.62 (-4.25%)</td><td>3.90 (-4.33%)</td><td>0.70 (-5.46%)</td><td>269.00 (+4.51%)</td><td>226.78 (+3.29%)</td><td>226.90 (+4.47%)</td><td>180.20 (+1.64%)</td><td>31.77 (-1.96%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.91 (n/a)</td><td>4.86 (n/a)</td><td>4.83 (n/a)</td><td>4.07 (n/a)</td><td>0.74 (n/a)</td><td>257.40 (n/a)</td><td>219.56 (n/a)</td><td>217.20 (n/a)</td><td>177.30 (n/a)</td><td>32.41 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>6.74 <b>(+28.78%)</b></td><td>4.82 (+2.57%)</td><td>4.48 (-4.78%)</td><td>3.77 (-7.58%)</td><td>1.16 <b>(+172.76%)</b></td><td>278.40 (+8.20%)</td><td>226.42 (+0.76%)</td><td>234.00 (+5.03%)</td><td>155.60 <b>(-22.36%)</b></td><td>46.59 <b>(+121.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.23 (n/a)</td><td>4.70 (n/a)</td><td>4.71 (n/a)</td><td>4.07 (n/a)</td><td>0.42 (n/a)</td><td>257.30 (n/a)</td><td>224.72 (n/a)</td><td>222.80 (n/a)</td><td>200.40 (n/a)</td><td>21.07 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.28 (+11.36%)</td><td>5.39 (-1.17%)</td><td>5.20 (-1.03%)</td><td>4.41 (-8.08%)</td><td>1.11 <b>(+62.46%)</b></td><td>238.00 (+8.78%)</td><td>200.02 (+2.91%)</td><td>201.70 (+1.05%)</td><td>144.00 (-10.17%)</td><td>34.74 <b>(+54.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>6.54 (n/a)</td><td>5.46 (n/a)</td><td>5.25 (n/a)</td><td>4.79 (n/a)</td><td>0.68 (n/a)</td><td>218.80 (n/a)</td><td>194.36 (n/a)</td><td>199.60 (n/a)</td><td>160.30 (n/a)</td><td>22.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.75 (+0.99%)</td><td>7.77 (-1.86%)</td><td>7.77 (-2.12%)</td><td>6.79 (-5.55%)</td><td>0.69 (+16.94%)</td><td>308.70 (+5.86%)</td><td>271.54 (+2.11%)</td><td>269.90 (+2.20%)</td><td>239.80 (-0.95%)</td><td>24.51 <b>(+22.86%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>8.66 (n/a)</td><td>7.92 (n/a)</td><td>7.94 (n/a)</td><td>7.19 (n/a)</td><td>0.59 (n/a)</td><td>291.60 (n/a)</td><td>265.94 (n/a)</td><td>264.10 (n/a)</td><td>242.10 (n/a)</td><td>19.95 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.12 (-6.42%)</td><td>7.53 (-2.36%)</td><td>7.52 (-2.67%)</td><td>6.99 (+2.11%)</td><td>0.42 <b>(-36.89%)</b></td><td>300.10 (-2.09%)</td><td>279.08 (+2.06%)</td><td>279.10 (+2.76%)</td><td>258.10 (+6.87%)</td><td>15.69 <b>(-34.00%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>8.68 (n/a)</td><td>7.72 (n/a)</td><td>7.72 (n/a)</td><td>6.84 (n/a)</td><td>0.67 (n/a)</td><td>306.50 (n/a)</td><td>273.46 (n/a)</td><td>271.60 (n/a)</td><td>241.50 (n/a)</td><td>23.77 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.23 (-3.27%)</td><td>7.95 (+2.33%)</td><td>7.86 (+1.16%)</td><td>7.67 (+7.07%)</td><td>0.25 <b>(-52.21%)</b></td><td>273.40 (-6.63%)</td><td>264.00 (-2.55%)</td><td>267.00 (-1.15%)</td><td>254.80 (+3.41%)</td><td>8.24 <b>(-54.34%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>8.51 (n/a)</td><td>7.77 (n/a)</td><td>7.77 (n/a)</td><td>7.16 (n/a)</td><td>0.52 (n/a)</td><td>292.80 (n/a)</td><td>270.90 (n/a)</td><td>270.10 (n/a)</td><td>246.40 (n/a)</td><td>18.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>10.26 (+9.48%)</td><td>9.29 (+15.99%)</td><td>9.47 <b>(+23.34%)</b></td><td>7.83 (+3.04%)</td><td>1.05 <b>(+36.93%)</b></td><td>267.90 (-2.93%)</td><td>228.22 (-13.42%)</td><td>221.40 (-18.90%)</td><td>204.30 (-8.67%)</td><td>27.06 <b>(+21.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.38 (n/a)</td><td>8.01 (n/a)</td><td>7.68 (n/a)</td><td>7.60 (n/a)</td><td>0.77 (n/a)</td><td>276.00 (n/a)</td><td>263.60 (n/a)</td><td>273.00 (n/a)</td><td>223.70 (n/a)</td><td>22.36 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>9.71 (-13.03%)</td><td>8.16 (-10.60%)</td><td>7.68 (-10.56%)</td><td>7.07 (-3.71%)</td><td>1.06 <b>(-38.36%)</b></td><td>296.70 (+3.85%)</td><td>260.40 (+10.20%)</td><td>273.00 (+11.79%)</td><td>216.00 (+14.95%)</td><td>31.97 <b>(-25.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.16 (n/a)</td><td>9.12 (n/a)</td><td>8.59 (n/a)</td><td>7.34 (n/a)</td><td>1.71 (n/a)</td><td>285.70 (n/a)</td><td>236.30 (n/a)</td><td>244.20 (n/a)</td><td>187.90 (n/a)</td><td>43.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>11.26 (+14.64%)</td><td>9.36 (+6.63%)</td><td>9.73 (+1.19%)</td><td>7.78 (+7.65%)</td><td>1.45 (+9.96%)</td><td>269.60 (-7.13%)</td><td>228.56 (-6.21%)</td><td>215.60 (-1.19%)</td><td>186.30 (-12.74%)</td><td>35.58 (-8.43%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.82 (n/a)</td><td>8.77 (n/a)</td><td>9.61 (n/a)</td><td>7.23 (n/a)</td><td>1.32 (n/a)</td><td>290.30 (n/a)</td><td>243.70 (n/a)</td><td>218.20 (n/a)</td><td>213.50 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>12.19 (+2.52%)</td><td>11.41 (+2.41%)</td><td>11.62 (+3.26%)</td><td>10.17 (+0.41%)</td><td>0.80 (+19.38%)</td><td>412.50 (-0.41%)</td><td>369.02 (-2.25%)</td><td>360.90 (-3.17%)</td><td>344.00 (-2.47%)</td><td>27.12 (+15.88%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.89 (n/a)</td><td>11.14 (n/a)</td><td>11.26 (n/a)</td><td>10.13 (n/a)</td><td>0.67 (n/a)</td><td>414.20 (n/a)</td><td>377.52 (n/a)</td><td>372.70 (n/a)</td><td>352.70 (n/a)</td><td>23.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.12 (+11.69%)</td><td>12.00 (+8.26%)</td><td>11.94 (+5.16%)</td><td>11.01 (+11.50%)</td><td>0.80 (+11.95%)</td><td>381.00 (-10.31%)</td><td>350.78 (-7.63%)</td><td>351.30 (-4.93%)</td><td>319.70 (-10.45%)</td><td>23.24 (-11.56%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.75 (n/a)</td><td>11.08 (n/a)</td><td>11.35 (n/a)</td><td>9.87 (n/a)</td><td>0.72 (n/a)</td><td>424.80 (n/a)</td><td>379.76 (n/a)</td><td>369.50 (n/a)</td><td>357.00 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>12.86 (-3.01%)</td><td>11.67 (-2.86%)</td><td>11.28 (-5.22%)</td><td>10.79 (+6.30%)</td><td>0.84 <b>(-34.67%)</b></td><td>388.90 (-5.93%)</td><td>360.76 (+2.37%)</td><td>371.80 (+5.54%)</td><td>326.10 (+3.10%)</td><td>25.43 <b>(-36.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.26 (n/a)</td><td>12.02 (n/a)</td><td>11.90 (n/a)</td><td>10.15 (n/a)</td><td>1.29 (n/a)</td><td>413.40 (n/a)</td><td>352.42 (n/a)</td><td>352.30 (n/a)</td><td>316.30 (n/a)</td><td>39.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>14.54 (+8.22%)</td><td>13.05 (+2.38%)</td><td>12.68 (-0.58%)</td><td>11.93 (-2.86%)</td><td>1.04 <b>(+118.31%)</b></td><td>351.50 (+2.96%)</td><td>323.02 (-1.94%)</td><td>330.80 (+0.58%)</td><td>288.40 (-7.62%)</td><td>25.08 <b>(+106.24%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.44 (n/a)</td><td>12.75 (n/a)</td><td>12.75 (n/a)</td><td>12.29 (n/a)</td><td>0.48 (n/a)</td><td>341.40 (n/a)</td><td>329.42 (n/a)</td><td>328.90 (n/a)</td><td>312.20 (n/a)</td><td>12.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.07 (+18.79%)</td><td>13.25 (+11.06%)</td><td>13.07 (+10.25%)</td><td>11.87 (+7.72%)</td><td>1.26 <b>(+96.23%)</b></td><td>353.40 (-7.17%)</td><td>318.76 (-9.54%)</td><td>320.90 (-9.30%)</td><td>278.30 (-15.82%)</td><td>29.50 <b>(+53.03%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>12.69 (n/a)</td><td>11.93 (n/a)</td><td>11.86 (n/a)</td><td>11.02 (n/a)</td><td>0.64 (n/a)</td><td>380.70 (n/a)</td><td>352.38 (n/a)</td><td>353.80 (n/a)</td><td>330.60 (n/a)</td><td>19.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>14.49 (-0.27%)</td><td>13.28 (+9.97%)</td><td>12.91 (+8.74%)</td><td>12.47 <b>(+31.71%)</b></td><td>0.92 <b>(-52.37%)</b></td><td>336.40 <b>(-24.08%)</b></td><td>317.12 (-10.64%)</td><td>324.90 (-8.04%)</td><td>289.40 (+0.28%)</td><td>21.35 <b>(-63.73%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>14.53 (n/a)</td><td>12.07 (n/a)</td><td>11.87 (n/a)</td><td>9.47 (n/a)</td><td>1.92 (n/a)</td><td>443.10 (n/a)</td><td>354.86 (n/a)</td><td>353.30 (n/a)</td><td>288.60 (n/a)</td><td>58.87 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.75 (+9.76%)</td><td>15.10 (+12.46%)</td><td>15.31 (+10.04%)</td><td>13.64 (+11.29%)</td><td>0.84 (-10.81%)</td><td>307.40 (-10.14%)</td><td>278.44 (-11.19%)</td><td>274.00 (-9.12%)</td><td>266.30 (-8.86%)</td><td>16.57 <b>(-26.61%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>14.35 (n/a)</td><td>13.43 (n/a)</td><td>13.91 (n/a)</td><td>12.26 (n/a)</td><td>0.94 (n/a)</td><td>342.10 (n/a)</td><td>313.52 (n/a)</td><td>301.50 (n/a)</td><td>292.20 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.80 (+6.30%)</td><td>11.52 (-3.37%)</td><td>11.72 (-1.35%)</td><td>8.97 (-14.46%)</td><td>2.01 <b>(+117.46%)</b></td><td>467.70 (+16.90%)</td><td>373.48 (+5.63%)</td><td>357.80 (+1.36%)</td><td>304.00 (-5.94%)</td><td>68.03 <b>(+135.89%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>12.98 (n/a)</td><td>11.92 (n/a)</td><td>11.88 (n/a)</td><td>10.48 (n/a)</td><td>0.92 (n/a)</td><td>400.10 (n/a)</td><td>353.56 (n/a)</td><td>353.00 (n/a)</td><td>323.20 (n/a)</td><td>28.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.53 (+7.60%)</td><td>2.76 (+5.90%)</td><td>2.67 (+7.42%)</td><td>2.39 (+9.91%)</td><td>0.46 (+12.93%)</td><td>219.30 (-9.04%)</td><td>193.66 (-5.39%)</td><td>196.60 (-6.91%)</td><td>148.60 (-7.01%)</td><td>28.67 (-2.44%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.28 (n/a)</td><td>2.61 (n/a)</td><td>2.48 (n/a)</td><td>2.17 (n/a)</td><td>0.41 (n/a)</td><td>241.10 (n/a)</td><td>204.70 (n/a)</td><td>211.20 (n/a)</td><td>159.80 (n/a)</td><td>29.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.31 (-9.00%)</td><td>4.32 (-17.68%)</td><td>4.57 (-13.25%)</td><td>3.23 <b>(-29.78%)</b></td><td>0.83 <b>(+60.71%)</b></td><td>325.00 <b>(+42.42%)</b></td><td>250.70 <b>(+24.38%)</b></td><td>229.60 (+15.26%)</td><td>197.50 (+9.91%)</td><td>51.12 <b>(+154.99%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.84 (n/a)</td><td>5.24 (n/a)</td><td>5.26 (n/a)</td><td>4.59 (n/a)</td><td>0.51 (n/a)</td><td>228.20 (n/a)</td><td>201.56 (n/a)</td><td>199.20 (n/a)</td><td>179.70 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.57 (-8.16%)</td><td>7.90 (+3.54%)</td><td>8.16 (+4.91%)</td><td>6.76 (+9.94%)</td><td>0.77 <b>(-33.93%)</b></td><td>310.10 (-9.06%)</td><td>267.56 (-4.43%)</td><td>256.90 (-4.68%)</td><td>244.60 (+8.86%)</td><td>27.67 <b>(-34.99%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.33 (n/a)</td><td>7.63 (n/a)</td><td>7.78 (n/a)</td><td>6.15 (n/a)</td><td>1.16 (n/a)</td><td>341.00 (n/a)</td><td>279.96 (n/a)</td><td>269.50 (n/a)</td><td>224.70 (n/a)</td><td>42.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.50 <b>(+24.29%)</b></td><td>3.25 (+8.57%)</td><td>2.69 (-6.60%)</td><td>2.60 (+5.85%)</td><td>0.86 <b>(+71.18%)</b></td><td>201.70 (-5.53%)</td><td>169.88 (-5.25%)</td><td>195.20 (+7.08%)</td><td>116.40 (-19.56%)</td><td>39.69 <b>(+34.50%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.62 (n/a)</td><td>2.99 (n/a)</td><td>2.88 (n/a)</td><td>2.46 (n/a)</td><td>0.50 (n/a)</td><td>213.50 (n/a)</td><td>179.30 (n/a)</td><td>182.30 (n/a)</td><td>144.70 (n/a)</td><td>29.51 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (-14.10%)</td><td>0.21 (-7.22%)</td><td>0.20 (-15.98%)</td><td>0.19 (+12.54%)</td><td>0.02 <b>(-67.48%)</b></td><td>172.40 (-11.13%)</td><td>158.90 (+3.54%)</td><td>160.10 (+19.03%)</td><td>140.40 (+16.42%)</td><td>12.10 <b>(-67.58%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>194.00 (n/a)</td><td>153.46 (n/a)</td><td>134.50 (n/a)</td><td>120.60 (n/a)</td><td>37.31 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (-9.66%)</td><td>0.19 (+1.72%)</td><td>0.20 (-0.05%)</td><td>0.16 (+12.93%)</td><td>0.02 <b>(-48.19%)</b></td><td>202.50 (-11.42%)</td><td>170.64 (-4.86%)</td><td>163.60 (+0.06%)</td><td>147.50 (+10.65%)</td><td>21.06 <b>(-50.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>228.60 (n/a)</td><td>179.36 (n/a)</td><td>163.50 (n/a)</td><td>133.30 (n/a)</td><td>42.52 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.56 (+8.61%)</td><td>0.44 (+13.81%)</td><td>0.41 (+3.00%)</td><td>0.33 (+10.07%)</td><td>0.09 (+5.01%)</td><td>196.00 (-9.13%)</td><td>154.50 (-12.45%)</td><td>160.70 (-2.90%)</td><td>118.00 (-7.96%)</td><td>30.47 (-14.80%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>215.70 (n/a)</td><td>176.48 (n/a)</td><td>165.50 (n/a)</td><td>128.20 (n/a)</td><td>35.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.44 (-13.48%)</td><td>0.38 (-6.53%)</td><td>0.40 (-5.88%)</td><td>0.31 (+2.35%)</td><td>0.06 <b>(-27.86%)</b></td><td>213.70 (-2.29%)</td><td>174.16 (+5.54%)</td><td>162.90 (+6.19%)</td><td>148.30 (+15.59%)</td><td>27.92 (-19.97%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>218.70 (n/a)</td><td>165.02 (n/a)</td><td>153.40 (n/a)</td><td>128.30 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.50 (+7.19%)</td><td>0.41 (+19.34%)</td><td>0.46 <b>(+23.95%)</b></td><td>0.31 <b>(+79.93%)</b></td><td>0.09 (-17.07%)</td><td>211.40 <b>(-44.41%)</b></td><td>167.04 <b>(-22.13%)</b></td><td>142.60 (-19.34%)</td><td>130.40 (-6.72%)</td><td>39.83 <b>(-58.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.37 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>380.30 (n/a)</td><td>214.52 (n/a)</td><td>176.80 (n/a)</td><td>139.80 (n/a)</td><td>95.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.04 (-1.80%)</td><td>0.82 (-1.38%)</td><td>0.83 (+11.33%)</td><td>0.69 (+0.26%)</td><td>0.14 (-18.88%)</td><td>190.70 (-0.26%)</td><td>162.28 (+0.37%)</td><td>157.40 (-10.16%)</td><td>126.50 (+1.77%)</td><td>24.97 (-17.37%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.05 (n/a)</td><td>0.84 (n/a)</td><td>0.75 (n/a)</td><td>0.69 (n/a)</td><td>0.17 (n/a)</td><td>191.20 (n/a)</td><td>161.68 (n/a)</td><td>175.20 (n/a)</td><td>124.30 (n/a)</td><td>30.22 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.04 (+1.24%)</td><td>0.91 (+14.58%)</td><td>0.88 (+2.60%)</td><td>0.81 <b>(+129.42%)</b></td><td>0.09 <b>(-67.11%)</b></td><td>161.20 <b>(-56.40%)</b></td><td>145.42 <b>(-24.07%)</b></td><td>148.60 (-2.56%)</td><td>125.70 (-1.26%)</td><td>13.18 <b>(-86.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.03 (n/a)</td><td>0.79 (n/a)</td><td>0.86 (n/a)</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>369.70 (n/a)</td><td>191.52 (n/a)</td><td>152.50 (n/a)</td><td>127.30 (n/a)</td><td>100.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.22 (+7.76%)</td><td>0.87 (+2.01%)</td><td>0.78 (+4.91%)</td><td>0.62 (-6.96%)</td><td>0.24 (+13.25%)</td><td>210.20 (+7.52%)</td><td>159.24 (-0.91%)</td><td>167.40 (-4.67%)</td><td>107.40 (-7.17%)</td><td>40.40 (+11.00%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.13 (n/a)</td><td>0.85 (n/a)</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.21 (n/a)</td><td>195.50 (n/a)</td><td>160.70 (n/a)</td><td>175.60 (n/a)</td><td>115.70 (n/a)</td><td>36.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.10 <b>(+43.76%)</b></td><td>0.85 <b>(+29.72%)</b></td><td>0.84 <b>(+34.00%)</b></td><td>0.61 (+4.93%)</td><td>0.20 <b>(+160.21%)</b></td><td>214.40 (-4.67%)</td><td>161.04 <b>(-20.18%)</b></td><td>156.10 <b>(-25.38%)</b></td><td>119.60 <b>(-30.47%)</b></td><td>38.67 <b>(+71.88%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.76 (n/a)</td><td>0.66 (n/a)</td><td>0.63 (n/a)</td><td>0.58 (n/a)</td><td>0.08 (n/a)</td><td>224.90 (n/a)</td><td>201.76 (n/a)</td><td>209.20 (n/a)</td><td>172.00 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (+0.02%)</td><td>0.10 (+2.88%)</td><td>0.10 (+2.48%)</td><td>0.09 (+8.47%)</td><td>0.01 (-16.26%)</td><td>180.20 (-7.83%)</td><td>160.60 (-3.58%)</td><td>160.40 (-2.37%)</td><td>129.40 (+0.00%)</td><td>20.77 <b>(-23.32%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.50 (n/a)</td><td>166.56 (n/a)</td><td>164.30 (n/a)</td><td>129.40 (n/a)</td><td>27.08 (n/a)</td>
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
