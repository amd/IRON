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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (+0.75%)</td><td>0.04 (-2.47%)</td><td>0.04 (-12.98%)</td><td>0.03 (+0.53%)</td><td>0.01 <b>(+25.01%)</b></td><td>209.80 (-0.52%)</td><td>165.42 (+3.72%)</td><td>175.00 (+14.90%)</td><td>127.30 (-0.78%)</td><td>35.40 (+14.85%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>159.48 (n/a)</td><td>152.30 (n/a)</td><td>128.30 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (-2.63%)</td><td>0.04 (+11.15%)</td><td>0.04 <b>(+20.86%)</b></td><td>0.03 (+9.29%)</td><td>0.01 (-12.36%)</td><td>195.60 (-8.47%)</td><td>154.74 (-10.91%)</td><td>148.10 (-17.26%)</td><td>117.90 (+2.70%)</td><td>31.88 (-12.09%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>173.68 (n/a)</td><td>179.00 (n/a)</td><td>114.80 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (-18.55%)</td><td>0.03 (-18.28%)</td><td>0.03 <b>(-26.27%)</b></td><td>0.03 (-3.90%)</td><td>0.00 <b>(-50.42%)</b></td><td>216.10 (+4.04%)</td><td>191.40 (+19.76%)</td><td>185.70 <b>(+35.65%)</b></td><td>166.50 <b>(+22.79%)</b></td><td>22.31 <b>(-33.59%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>159.82 (n/a)</td><td>136.90 (n/a)</td><td>135.60 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (+9.88%)</td><td>0.04 (+7.02%)</td><td>0.04 (+8.27%)</td><td>0.03 (-3.46%)</td><td>0.01 <b>(+22.93%)</b></td><td>211.90 (+3.62%)</td><td>163.36 (-5.84%)</td><td>154.60 (-7.65%)</td><td>134.30 (-9.01%)</td><td>30.83 (+16.89%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>173.50 (n/a)</td><td>167.40 (n/a)</td><td>147.60 (n/a)</td><td>26.38 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (+12.33%)</td><td>0.03 (+0.46%)</td><td>0.03 (-6.32%)</td><td>0.03 (-7.20%)</td><td>0.01 <b>(+149.49%)</b></td><td>216.80 (+7.81%)</td><td>185.28 (+1.05%)</td><td>195.10 (+6.73%)</td><td>151.30 (-11.00%)</td><td>27.22 <b>(+135.67%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.10 (n/a)</td><td>183.36 (n/a)</td><td>182.80 (n/a)</td><td>170.00 (n/a)</td><td>11.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 <b>(-33.60%)</b></td><td>0.03 (-19.14%)</td><td>0.03 (-19.55%)</td><td>0.03 (-5.84%)</td><td>0.01 <b>(-53.36%)</b></td><td>217.80 (+6.19%)</td><td>183.90 (+15.67%)</td><td>196.00 <b>(+24.29%)</b></td><td>125.90 <b>(+50.60%)</b></td><td>36.25 <b>(-26.34%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>205.10 (n/a)</td><td>158.98 (n/a)</td><td>157.70 (n/a)</td><td>83.60 (n/a)</td><td>49.21 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 <b>(+24.48%)</b></td><td>0.03 (-1.72%)</td><td>0.03 (-8.37%)</td><td>0.02 (-15.71%)</td><td>0.01 <b>(+129.30%)</b></td><td>294.90 (+18.62%)</td><td>218.60 (+6.00%)</td><td>222.60 (+9.17%)</td><td>147.00 (-19.67%)</td><td>54.18 <b>(+111.84%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.60 (n/a)</td><td>206.22 (n/a)</td><td>203.90 (n/a)</td><td>183.00 (n/a)</td><td>25.58 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-8.41%)</td><td>0.03 (-16.75%)</td><td>0.03 (-18.97%)</td><td>0.02 <b>(-23.00%)</b></td><td>0.01 <b>(+26.09%)</b></td><td>284.70 <b>(+29.82%)</b></td><td>231.94 <b>(+21.95%)</b></td><td>234.80 <b>(+23.38%)</b></td><td>176.50 (+9.22%)</td><td>42.07 <b>(+77.41%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>219.30 (n/a)</td><td>190.20 (n/a)</td><td>190.30 (n/a)</td><td>161.60 (n/a)</td><td>23.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (-9.21%)</td><td>0.07 (-9.08%)</td><td>0.07 (-4.45%)</td><td>0.05 <b>(-23.51%)</b></td><td>0.01 <b>(+42.34%)</b></td><td>252.10 <b>(+30.76%)</b></td><td>188.34 (+12.05%)</td><td>168.90 (+4.65%)</td><td>159.30 (+10.09%)</td><td>38.52 <b>(+104.83%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>168.08 (n/a)</td><td>161.40 (n/a)</td><td>144.70 (n/a)</td><td>18.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 <b>(-23.03%)</b></td><td>0.06 <b>(-20.27%)</b></td><td>0.06 (-16.71%)</td><td>0.06 (-14.38%)</td><td>0.01 <b>(-39.90%)</b></td><td>217.40 (+16.76%)</td><td>196.66 <b>(+24.63%)</b></td><td>193.70 <b>(+20.01%)</b></td><td>171.20 <b>(+29.89%)</b></td><td>19.00 (-7.56%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.20 (n/a)</td><td>157.80 (n/a)</td><td>161.40 (n/a)</td><td>131.80 (n/a)</td><td>20.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (+1.87%)</td><td>0.08 (-4.52%)</td><td>0.07 (-4.82%)</td><td>0.07 (-0.46%)</td><td>0.02 (+8.73%)</td><td>187.10 (+0.43%)</td><td>161.34 (+5.04%)</td><td>166.20 (+5.06%)</td><td>118.10 (-1.83%)</td><td>26.04 (+4.25%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.30 (n/a)</td><td>153.60 (n/a)</td><td>158.20 (n/a)</td><td>120.30 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (+8.21%)</td><td>0.07 (-7.88%)</td><td>0.06 (-16.20%)</td><td>0.06 (+4.97%)</td><td>0.01 (+3.66%)</td><td>217.50 (-4.73%)</td><td>185.26 (+8.29%)</td><td>190.00 (+19.27%)</td><td>141.10 (-7.60%)</td><td>28.15 (-12.68%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.30 (n/a)</td><td>171.08 (n/a)</td><td>159.30 (n/a)</td><td>152.70 (n/a)</td><td>32.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (+6.05%)</td><td>0.08 (+3.71%)</td><td>0.08 (+5.12%)</td><td>0.06 (+6.63%)</td><td>0.01 (-9.89%)</td><td>191.20 (-6.18%)</td><td>157.28 (-4.31%)</td><td>159.40 (-4.84%)</td><td>124.60 (-5.68%)</td><td>26.02 (-17.92%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>164.36 (n/a)</td><td>167.50 (n/a)</td><td>132.10 (n/a)</td><td>31.71 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (-6.35%)</td><td>0.07 (-6.93%)</td><td>0.07 (+1.70%)</td><td>0.05 <b>(-26.76%)</b></td><td>0.01 <b>(+50.08%)</b></td><td>255.20 <b>(+36.54%)</b></td><td>189.30 (+9.90%)</td><td>173.40 (-1.64%)</td><td>152.20 (+6.81%)</td><td>40.45 <b>(+125.46%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>172.24 (n/a)</td><td>176.30 (n/a)</td><td>142.50 (n/a)</td><td>17.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 <b>(-45.19%)</b></td><td>0.06 <b>(-28.12%)</b></td><td>0.06 <b>(-20.69%)</b></td><td>0.04 <b>(-29.81%)</b></td><td>0.01 <b>(-56.54%)</b></td><td>290.50 <b>(+42.47%)</b></td><td>216.24 <b>(+34.66%)</b></td><td>199.40 <b>(+26.04%)</b></td><td>175.40 <b>(+82.52%)</b></td><td>47.90 (+16.32%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>203.90 (n/a)</td><td>160.58 (n/a)</td><td>158.20 (n/a)</td><td>96.10 (n/a)</td><td>41.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (+6.06%)</td><td>0.06 (-7.98%)</td><td>0.06 (-9.01%)</td><td>0.04 <b>(-31.45%)</b></td><td>0.02 <b>(+169.73%)</b></td><td>298.20 <b>(+45.89%)</b></td><td>205.36 (+14.82%)</td><td>194.10 (+9.91%)</td><td>149.50 (-5.74%)</td><td>59.89 <b>(+265.07%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>178.86 (n/a)</td><td>176.60 (n/a)</td><td>158.60 (n/a)</td><td>16.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (+1.18%)</td><td>0.15 (-9.53%)</td><td>0.14 (-12.20%)</td><td>0.11 <b>(-20.55%)</b></td><td>0.03 <b>(+38.31%)</b></td><td>219.60 <b>(+25.85%)</b></td><td>169.98 (+12.79%)</td><td>171.00 (+13.92%)</td><td>124.30 (-1.19%)</td><td>35.64 <b>(+69.76%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>174.50 (n/a)</td><td>150.70 (n/a)</td><td>150.10 (n/a)</td><td>125.80 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (-9.09%)</td><td>0.16 (+4.58%)</td><td>0.16 (+17.13%)</td><td>0.10 <b>(-23.37%)</b></td><td>0.04 (+0.93%)</td><td>234.80 <b>(+30.52%)</b></td><td>159.78 (-2.81%)</td><td>150.50 (-14.59%)</td><td>125.00 (+10.04%)</td><td>43.57 <b>(+52.70%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>179.90 (n/a)</td><td>164.40 (n/a)</td><td>176.20 (n/a)</td><td>113.60 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (-6.46%)</td><td>0.13 (-2.63%)</td><td>0.13 (-0.69%)</td><td>0.10 <b>(+26.24%)</b></td><td>0.03 (-16.90%)</td><td>244.70 <b>(-20.78%)</b></td><td>195.84 (-0.26%)</td><td>183.80 (+0.71%)</td><td>149.30 (+6.87%)</td><td>45.71 <b>(-30.80%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>308.90 (n/a)</td><td>196.36 (n/a)</td><td>182.50 (n/a)</td><td>139.70 (n/a)</td><td>66.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.17 (-7.99%)</td><td>0.15 (+9.24%)</td><td>0.15 (-2.07%)</td><td>0.11 <b>(+45.93%)</b></td><td>0.02 <b>(-44.45%)</b></td><td>220.90 <b>(-31.46%)</b></td><td>170.48 (-14.71%)</td><td>168.70 (+2.12%)</td><td>143.30 (+8.73%)</td><td>30.31 <b>(-59.39%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>322.30 (n/a)</td><td>199.88 (n/a)</td><td>165.20 (n/a)</td><td>131.80 (n/a)</td><td>74.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (+6.72%)</td><td>0.13 <b>(+20.32%)</b></td><td>0.13 (+15.31%)</td><td>0.11 <b>(+67.12%)</b></td><td>0.01 <b>(-45.04%)</b></td><td>221.10 <b>(-40.15%)</b></td><td>188.66 <b>(-20.96%)</b></td><td>189.30 (-13.28%)</td><td>169.30 (-6.31%)</td><td>21.38 <b>(-71.41%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>369.40 (n/a)</td><td>238.70 (n/a)</td><td>218.30 (n/a)</td><td>180.70 (n/a)</td><td>74.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 <b>(+44.12%)</b></td><td>0.14 <b>(+26.04%)</b></td><td>0.13 <b>(+26.23%)</b></td><td>0.10 (-0.27%)</td><td>0.03 <b>(+215.77%)</b></td><td>244.00 (+0.25%)</td><td>187.48 (-17.65%)</td><td>189.40 <b>(-20.75%)</b></td><td>137.50 <b>(-30.59%)</b></td><td>43.34 <b>(+115.16%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>243.40 (n/a)</td><td>227.66 (n/a)</td><td>239.00 (n/a)</td><td>198.10 (n/a)</td><td>20.14 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 <b>(-23.61%)</b></td><td>0.11 <b>(-21.43%)</b></td><td>0.11 (-16.24%)</td><td>0.08 <b>(-31.27%)</b></td><td>0.02 (+12.39%)</td><td>305.10 <b>(+45.49%)</b></td><td>237.60 <b>(+28.79%)</b></td><td>214.20 (+19.40%)</td><td>209.10 <b>(+30.85%)</b></td><td>40.86 <b>(+112.19%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>184.48 (n/a)</td><td>179.40 (n/a)</td><td>159.80 (n/a)</td><td>19.26 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (+6.03%)</td><td>0.13 (-3.42%)</td><td>0.12 (-6.32%)</td><td>0.10 (-11.98%)</td><td>0.02 <b>(+38.71%)</b></td><td>246.40 (+13.60%)</td><td>199.46 (+4.82%)</td><td>196.70 (+6.73%)</td><td>151.00 (-5.68%)</td><td>34.35 <b>(+43.60%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.90 (n/a)</td><td>190.28 (n/a)</td><td>184.30 (n/a)</td><td>160.10 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.39 (+5.64%)</td><td>0.27 (-3.71%)</td><td>0.25 (-8.44%)</td><td>0.18 (+0.14%)</td><td>0.08 (+5.68%)</td><td>271.40 (-0.11%)</td><td>197.14 (+4.08%)</td><td>196.60 (+9.22%)</td><td>126.60 (-5.38%)</td><td>54.51 (-1.04%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>271.70 (n/a)</td><td>189.42 (n/a)</td><td>180.00 (n/a)</td><td>133.80 (n/a)</td><td>55.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 <b>(-32.69%)</b></td><td>0.26 (-18.74%)</td><td>0.25 (-7.79%)</td><td>0.25 (-2.98%)</td><td>0.01 <b>(-85.37%)</b></td><td>200.30 (+3.03%)</td><td>192.00 (+18.86%)</td><td>194.20 (+8.43%)</td><td>182.10 <b>(+48.53%)</b></td><td>7.45 <b>(-77.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>194.40 (n/a)</td><td>161.54 (n/a)</td><td>179.10 (n/a)</td><td>122.60 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.37 (-0.97%)</td><td>0.29 (-4.58%)</td><td>0.29 (+3.51%)</td><td>0.21 <b>(-21.75%)</b></td><td>0.06 <b>(+31.34%)</b></td><td>235.70 <b>(+27.82%)</b></td><td>176.66 (+6.74%)</td><td>167.70 (-3.40%)</td><td>134.30 (+0.98%)</td><td>37.42 <b>(+71.70%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>184.40 (n/a)</td><td>165.50 (n/a)</td><td>173.60 (n/a)</td><td>133.00 (n/a)</td><td>21.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.40 (+4.12%)</td><td>0.31 (+1.57%)</td><td>0.30 (-4.97%)</td><td>0.23 (-1.52%)</td><td>0.07 <b>(+23.90%)</b></td><td>210.10 (+1.55%)</td><td>167.88 (-0.01%)</td><td>164.50 (+5.25%)</td><td>122.20 (-3.93%)</td><td>39.42 <b>(+21.71%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>206.90 (n/a)</td><td>167.90 (n/a)</td><td>156.30 (n/a)</td><td>127.20 (n/a)</td><td>32.39 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.39 (-10.58%)</td><td>0.27 (-8.94%)</td><td>0.27 (-0.35%)</td><td>0.18 (-17.91%)</td><td>0.08 (-6.98%)</td><td>269.90 <b>(+21.80%)</b></td><td>194.06 (+10.92%)</td><td>183.40 (+0.38%)</td><td>126.00 (+11.80%)</td><td>52.85 <b>(+31.08%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>221.60 (n/a)</td><td>174.96 (n/a)</td><td>182.70 (n/a)</td><td>112.70 (n/a)</td><td>40.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 <b>(-30.14%)</b></td><td>0.26 (-11.83%)</td><td>0.26 (+4.00%)</td><td>0.23 (+17.57%)</td><td>0.02 <b>(-73.49%)</b></td><td>217.20 (-14.96%)</td><td>194.06 (+5.93%)</td><td>189.40 (-3.86%)</td><td>170.70 <b>(+43.08%)</b></td><td>18.08 <b>(-66.79%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>255.40 (n/a)</td><td>183.20 (n/a)</td><td>197.00 (n/a)</td><td>119.30 (n/a)</td><td>54.43 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.43 <b>(+39.28%)</b></td><td>0.30 (+14.02%)</td><td>0.29 (+7.82%)</td><td>0.22 (+0.01%)</td><td>0.08 <b>(+118.45%)</b></td><td>225.30 (+0.00%)</td><td>172.68 (-9.25%)</td><td>169.90 (-7.26%)</td><td>114.40 <b>(-28.23%)</b></td><td>40.55 <b>(+51.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>225.30 (n/a)</td><td>190.28 (n/a)</td><td>183.20 (n/a)</td><td>159.40 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (+0.93%)</td><td>0.27 (+15.23%)</td><td>0.28 <b>(+31.61%)</b></td><td>0.22 <b>(+21.07%)</b></td><td>0.04 <b>(-30.91%)</b></td><td>220.00 (-17.42%)</td><td>182.40 (-15.33%)</td><td>174.80 <b>(-24.00%)</b></td><td>152.10 (-0.91%)</td><td>26.66 <b>(-42.71%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>266.40 (n/a)</td><td>215.42 (n/a)</td><td>230.00 (n/a)</td><td>153.50 (n/a)</td><td>46.54 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 <b>(-21.15%)</b></td><td>0.02 (-10.34%)</td><td>0.01 (-9.05%)</td><td>0.01 (-7.68%)</td><td>0.00 <b>(-41.67%)</b></td><td>205.00 (+8.29%)</td><td>172.90 (+10.10%)</td><td>176.10 (+9.99%)</td><td>149.70 <b>(+26.86%)</b></td><td>21.58 (-18.59%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>189.30 (n/a)</td><td>157.04 (n/a)</td><td>160.10 (n/a)</td><td>118.00 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (-16.50%)</td><td>0.02 (-5.06%)</td><td>0.02 (-5.66%)</td><td>0.01 (+7.08%)</td><td>0.00 <b>(-58.49%)</b></td><td>178.10 (-6.61%)</td><td>167.10 (+2.96%)</td><td>169.30 (+6.01%)</td><td>145.70 (+19.82%)</td><td>13.27 <b>(-54.87%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>190.70 (n/a)</td><td>162.30 (n/a)</td><td>159.70 (n/a)</td><td>121.60 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 <b>(-31.56%)</b></td><td>0.01 <b>(-29.38%)</b></td><td>0.01 <b>(-33.70%)</b></td><td>0.01 (-19.34%)</td><td>0.00 <b>(-47.31%)</b></td><td>215.30 <b>(+23.95%)</b></td><td>191.60 <b>(+39.65%)</b></td><td>197.60 <b>(+50.84%)</b></td><td>157.70 <b>(+46.02%)</b></td><td>25.00 (-4.23%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.70 (n/a)</td><td>137.20 (n/a)</td><td>131.00 (n/a)</td><td>108.00 (n/a)</td><td>26.11 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (-2.50%)</td><td>0.01 (-13.88%)</td><td>0.01 <b>(-20.74%)</b></td><td>0.01 (-14.67%)</td><td>0.00 (-4.21%)</td><td>236.80 (+17.17%)</td><td>185.78 (+16.29%)</td><td>186.10 <b>(+26.17%)</b></td><td>130.90 (+2.51%)</td><td>37.64 (+11.23%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>202.10 (n/a)</td><td>159.76 (n/a)</td><td>147.50 (n/a)</td><td>127.70 (n/a)</td><td>33.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (-10.43%)</td><td>0.01 (-14.24%)</td><td>0.01 <b>(-20.05%)</b></td><td>0.01 <b>(+24.43%)</b></td><td>0.00 <b>(-43.26%)</b></td><td>205.20 (-19.62%)</td><td>190.64 (+12.00%)</td><td>202.90 <b>(+25.09%)</b></td><td>146.30 (+11.68%)</td><td>25.21 <b>(-49.95%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>255.30 (n/a)</td><td>170.22 (n/a)</td><td>162.20 (n/a)</td><td>131.00 (n/a)</td><td>50.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (-2.06%)</td><td>0.01 (+0.61%)</td><td>0.01 (-1.03%)</td><td>0.01 (+9.68%)</td><td>0.00 <b>(-31.45%)</b></td><td>205.70 (-8.82%)</td><td>181.98 (-2.13%)</td><td>192.00 (+1.00%)</td><td>153.00 (+2.14%)</td><td>22.33 <b>(-35.03%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>225.60 (n/a)</td><td>185.94 (n/a)</td><td>190.10 (n/a)</td><td>149.80 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (-13.22%)</td><td>0.02 (-2.96%)</td><td>0.02 (-9.31%)</td><td>0.01 (+18.13%)</td><td>0.00 <b>(-56.40%)</b></td><td>198.90 (-15.33%)</td><td>174.98 (-0.43%)</td><td>172.20 (+10.31%)</td><td>154.50 (+15.21%)</td><td>17.63 <b>(-57.86%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>234.90 (n/a)</td><td>175.74 (n/a)</td><td>156.10 (n/a)</td><td>134.10 (n/a)</td><td>41.85 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (+2.59%)</td><td>0.01 (-2.51%)</td><td>0.01 (+11.23%)</td><td>0.01 <b>(-25.23%)</b></td><td>0.00 <b>(+83.04%)</b></td><td>313.40 <b>(+33.76%)</b></td><td>229.34 (+6.73%)</td><td>207.90 (-10.12%)</td><td>171.90 (-2.55%)</td><td>60.41 <b>(+135.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>234.30 (n/a)</td><td>214.88 (n/a)</td><td>231.30 (n/a)</td><td>176.40 (n/a)</td><td>25.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (-16.56%)</td><td>0.03 (-15.61%)</td><td>0.03 (-16.46%)</td><td>0.03 (-11.81%)</td><td>0.00 <b>(-32.14%)</b></td><td>201.70 (+13.38%)</td><td>171.30 (+17.55%)</td><td>170.20 (+19.69%)</td><td>142.50 (+19.85%)</td><td>21.86 (-8.20%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>177.90 (n/a)</td><td>145.72 (n/a)</td><td>142.20 (n/a)</td><td>118.90 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-13.03%)</td><td>0.03 (-13.19%)</td><td>0.03 <b>(-20.37%)</b></td><td>0.02 (-3.09%)</td><td>0.00 (-11.21%)</td><td>219.10 (+3.15%)</td><td>197.70 (+15.02%)</td><td>208.00 <b>(+25.60%)</b></td><td>171.70 (+14.93%)</td><td>24.08 (+1.04%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.40 (n/a)</td><td>171.88 (n/a)</td><td>165.60 (n/a)</td><td>149.40 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-11.78%)</td><td>0.03 (-17.13%)</td><td>0.02 <b>(-31.36%)</b></td><td>0.02 (-5.09%)</td><td>0.01 (-5.32%)</td><td>249.40 (+5.37%)</td><td>209.22 <b>(+20.80%)</b></td><td>228.20 <b>(+45.63%)</b></td><td>163.20 (+13.33%)</td><td>41.03 (+8.79%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.70 (n/a)</td><td>173.20 (n/a)</td><td>156.70 (n/a)</td><td>144.00 (n/a)</td><td>37.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (+15.06%)</td><td>0.03 (+9.15%)</td><td>0.03 (-6.63%)</td><td>0.03 <b>(+24.38%)</b></td><td>0.01 (-2.94%)</td><td>183.40 (-19.60%)</td><td>162.22 (-9.19%)</td><td>172.90 (+7.13%)</td><td>129.20 (-13.11%)</td><td>23.27 <b>(-31.66%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>178.64 (n/a)</td><td>161.40 (n/a)</td><td>148.70 (n/a)</td><td>34.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 <b>(-22.34%)</b></td><td>0.03 (-16.13%)</td><td>0.03 (-5.97%)</td><td>0.03 (-8.51%)</td><td>0.00 <b>(-60.98%)</b></td><td>199.10 (+9.34%)</td><td>176.36 (+15.71%)</td><td>174.50 (+6.34%)</td><td>151.80 <b>(+28.75%)</b></td><td>18.10 <b>(-43.91%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>152.42 (n/a)</td><td>164.10 (n/a)</td><td>117.90 (n/a)</td><td>32.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-15.58%)</td><td>0.03 (-2.36%)</td><td>0.03 (+0.50%)</td><td>0.03 (+8.27%)</td><td>0.00 <b>(-64.67%)</b></td><td>196.60 (-7.66%)</td><td>184.88 (+0.93%)</td><td>186.70 (-0.53%)</td><td>169.60 (+18.44%)</td><td>9.96 <b>(-60.37%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>183.18 (n/a)</td><td>187.70 (n/a)</td><td>143.20 (n/a)</td><td>25.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 <b>(+45.15%)</b></td><td>0.03 (+3.09%)</td><td>0.03 (-4.51%)</td><td>0.02 <b>(-20.08%)</b></td><td>0.01 <b>(+230.00%)</b></td><td>253.80 <b>(+25.15%)</b></td><td>175.82 (+4.12%)</td><td>167.00 (+4.70%)</td><td>107.50 <b>(-31.09%)</b></td><td>54.24 <b>(+178.46%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>202.80 (n/a)</td><td>168.86 (n/a)</td><td>159.50 (n/a)</td><td>156.00 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+8.82%)</td><td>0.03 (+5.29%)</td><td>0.03 (+11.63%)</td><td>0.02 (+8.04%)</td><td>0.00 (+16.40%)</td><td>223.20 (-7.42%)</td><td>195.22 (-4.75%)</td><td>189.60 (-10.40%)</td><td>156.70 (-8.09%)</td><td>27.77 (+1.71%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.10 (n/a)</td><td>204.96 (n/a)</td><td>211.60 (n/a)</td><td>170.50 (n/a)</td><td>27.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (+9.70%)</td><td>0.07 (-2.91%)</td><td>0.06 (-13.14%)</td><td>0.05 (+2.03%)</td><td>0.02 <b>(+36.37%)</b></td><td>214.70 (-2.01%)</td><td>170.92 (+5.47%)</td><td>176.50 (+15.13%)</td><td>111.30 (-8.85%)</td><td>43.95 <b>(+21.64%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>162.06 (n/a)</td><td>153.30 (n/a)</td><td>122.10 (n/a)</td><td>36.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (-15.83%)</td><td>0.06 (-19.02%)</td><td>0.06 <b>(-23.20%)</b></td><td>0.04 <b>(-31.45%)</b></td><td>0.01 (+15.33%)</td><td>276.50 <b>(+45.83%)</b></td><td>195.02 <b>(+26.93%)</b></td><td>190.70 <b>(+30.26%)</b></td><td>150.10 (+18.75%)</td><td>51.77 <b>(+94.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>153.64 (n/a)</td><td>146.40 (n/a)</td><td>126.40 (n/a)</td><td>26.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (+14.37%)</td><td>0.06 (-6.32%)</td><td>0.06 (-10.49%)</td><td>0.05 (-18.23%)</td><td>0.01 <b>(+121.61%)</b></td><td>223.30 <b>(+22.29%)</b></td><td>171.54 (+9.79%)</td><td>170.70 (+11.71%)</td><td>123.80 (-12.51%)</td><td>35.34 <b>(+128.28%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>156.24 (n/a)</td><td>152.80 (n/a)</td><td>141.50 (n/a)</td><td>15.48 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (-15.31%)</td><td>0.07 (-16.16%)</td><td>0.07 (-3.96%)</td><td>0.05 <b>(-23.47%)</b></td><td>0.01 (-11.70%)</td><td>203.60 <b>(+30.68%)</b></td><td>162.68 (+19.81%)</td><td>154.50 (+4.18%)</td><td>127.60 (+18.04%)</td><td>29.65 <b>(+37.35%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>155.80 (n/a)</td><td>135.78 (n/a)</td><td>148.30 (n/a)</td><td>108.10 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 <b>(-22.70%)</b></td><td>0.06 (-10.78%)</td><td>0.06 (-13.23%)</td><td>0.05 (+15.49%)</td><td>0.00 <b>(-70.82%)</b></td><td>191.90 (-13.40%)</td><td>175.64 (+8.67%)</td><td>177.70 (+15.24%)</td><td>162.20 <b>(+29.35%)</b></td><td>11.24 <b>(-68.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>161.62 (n/a)</td><td>154.20 (n/a)</td><td>125.40 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 <b>(-20.55%)</b></td><td>0.05 (-19.43%)</td><td>0.05 <b>(-20.36%)</b></td><td>0.05 (-18.33%)</td><td>0.01 <b>(-29.34%)</b></td><td>213.00 <b>(+22.48%)</b></td><td>194.22 <b>(+23.79%)</b></td><td>196.90 <b>(+25.57%)</b></td><td>162.20 <b>(+25.83%)</b></td><td>19.16 (+7.07%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>173.90 (n/a)</td><td>156.90 (n/a)</td><td>156.80 (n/a)</td><td>128.90 (n/a)</td><td>17.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (-7.38%)</td><td>0.06 (-6.80%)</td><td>0.06 (-11.18%)</td><td>0.05 (-18.76%)</td><td>0.01 (+18.50%)</td><td>215.70 <b>(+23.12%)</b></td><td>168.52 (+8.71%)</td><td>175.40 (+12.58%)</td><td>133.40 (+8.02%)</td><td>32.48 <b>(+54.87%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>175.20 (n/a)</td><td>155.02 (n/a)</td><td>155.80 (n/a)</td><td>123.50 (n/a)</td><td>20.97 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (-1.91%)</td><td>0.05 (-7.79%)</td><td>0.05 (-12.86%)</td><td>0.04 (-16.51%)</td><td>0.01 <b>(+30.09%)</b></td><td>248.50 (+19.82%)</td><td>202.28 (+9.36%)</td><td>202.80 (+14.77%)</td><td>169.80 (+1.92%)</td><td>29.70 <b>(+59.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>184.96 (n/a)</td><td>176.70 (n/a)</td><td>166.60 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (+1.98%)</td><td>0.13 (-14.35%)</td><td>0.12 (-19.82%)</td><td>0.09 <b>(-22.80%)</b></td><td>0.03 <b>(+50.38%)</b></td><td>225.80 <b>(+29.47%)</b></td><td>173.98 (+19.82%)</td><td>175.80 <b>(+24.68%)</b></td><td>119.10 (-1.98%)</td><td>37.79 <b>(+83.34%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>174.40 (n/a)</td><td>145.20 (n/a)</td><td>141.00 (n/a)</td><td>121.50 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 <b>(-31.55%)</b></td><td>0.11 (-18.59%)</td><td>0.10 <b>(-21.04%)</b></td><td>0.09 <b>(+49.45%)</b></td><td>0.01 <b>(-69.70%)</b></td><td>233.70 <b>(-33.08%)</b></td><td>199.58 (+7.54%)</td><td>203.10 <b>(+26.62%)</b></td><td>170.90 <b>(+46.19%)</b></td><td>26.09 <b>(-72.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>349.20 (n/a)</td><td>185.58 (n/a)</td><td>160.40 (n/a)</td><td>116.90 (n/a)</td><td>94.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 <b>(-23.29%)</b></td><td>0.11 <b>(-26.42%)</b></td><td>0.11 <b>(-29.34%)</b></td><td>0.07 <b>(-40.61%)</b></td><td>0.02 (-10.49%)</td><td>297.40 <b>(+68.40%)</b></td><td>201.74 <b>(+38.82%)</b></td><td>187.70 <b>(+41.55%)</b></td><td>151.60 <b>(+30.35%)</b></td><td>55.63 <b>(+101.33%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>176.60 (n/a)</td><td>145.32 (n/a)</td><td>132.60 (n/a)</td><td>116.30 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 <b>(-23.33%)</b></td><td>0.11 (-17.09%)</td><td>0.10 <b>(-22.39%)</b></td><td>0.10 (-4.98%)</td><td>0.01 <b>(-53.07%)</b></td><td>214.90 (+5.24%)</td><td>198.52 (+18.80%)</td><td>209.40 <b>(+28.86%)</b></td><td>179.10 <b>(+30.44%)</b></td><td>17.68 <b>(-36.33%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.20 (n/a)</td><td>167.10 (n/a)</td><td>162.50 (n/a)</td><td>137.30 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 <b>(-40.48%)</b></td><td>0.11 (-9.48%)</td><td>0.11 (+9.74%)</td><td>0.10 (+19.35%)</td><td>0.01 <b>(-78.51%)</b></td><td>214.20 (-16.20%)</td><td>191.78 (+0.19%)</td><td>183.00 (-8.91%)</td><td>172.00 <b>(+67.97%)</b></td><td>18.99 <b>(-68.66%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>255.60 (n/a)</td><td>191.42 (n/a)</td><td>200.90 (n/a)</td><td>102.40 (n/a)</td><td>60.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 <b>(-29.43%)</b></td><td>0.11 <b>(-23.53%)</b></td><td>0.11 (-17.37%)</td><td>0.09 <b>(-26.24%)</b></td><td>0.01 <b>(-35.10%)</b></td><td>239.80 <b>(+35.56%)</b></td><td>198.22 <b>(+30.46%)</b></td><td>188.00 <b>(+20.98%)</b></td><td>176.40 <b>(+41.69%)</b></td><td>24.79 <b>(+28.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>176.90 (n/a)</td><td>151.94 (n/a)</td><td>155.40 (n/a)</td><td>124.50 (n/a)</td><td>19.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (-11.75%)</td><td>0.12 (-5.93%)</td><td>0.11 (-4.90%)</td><td>0.09 (-10.90%)</td><td>0.03 (+2.81%)</td><td>241.80 (+12.26%)</td><td>185.56 (+7.31%)</td><td>188.70 (+5.18%)</td><td>144.80 (+13.30%)</td><td>41.27 <b>(+27.78%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>215.40 (n/a)</td><td>172.92 (n/a)</td><td>179.40 (n/a)</td><td>127.80 (n/a)</td><td>32.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (+2.62%)</td><td>0.10 (+9.50%)</td><td>0.10 (+5.15%)</td><td>0.09 <b>(+47.54%)</b></td><td>0.01 <b>(-67.62%)</b></td><td>233.60 <b>(-32.21%)</b></td><td>214.52 (-11.57%)</td><td>208.00 (-4.89%)</td><td>205.00 (-2.52%)</td><td>11.98 <b>(-79.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>344.60 (n/a)</td><td>242.60 (n/a)</td><td>218.70 (n/a)</td><td>210.30 (n/a)</td><td>57.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>161.52 (n/a)</td><td>163.90 (n/a)</td><td>119.30 (n/a)</td><td>38.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.00 (n/a)</td><td>166.92 (n/a)</td><td>147.20 (n/a)</td><td>139.00 (n/a)</td><td>40.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>219.40 (n/a)</td><td>197.76 (n/a)</td><td>206.00 (n/a)</td><td>153.50 (n/a)</td><td>26.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>220.30 (n/a)</td><td>196.60 (n/a)</td><td>212.10 (n/a)</td><td>159.90 (n/a)</td><td>27.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>349.90 (n/a)</td><td>209.72 (n/a)</td><td>177.90 (n/a)</td><td>145.60 (n/a)</td><td>80.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>182.80 (n/a)</td><td>187.40 (n/a)</td><td>134.80 (n/a)</td><td>29.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>222.20 (n/a)</td><td>208.48 (n/a)</td><td>205.10 (n/a)</td><td>195.50 (n/a)</td><td>12.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>211.10 (n/a)</td><td>184.10 (n/a)</td><td>193.60 (n/a)</td><td>127.70 (n/a)</td><td>33.26 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.60 (n/a)</td><td>177.78 (n/a)</td><td>188.00 (n/a)</td><td>137.10 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.40 (n/a)</td><td>172.26 (n/a)</td><td>173.00 (n/a)</td><td>132.60 (n/a)</td><td>25.82 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>196.10 (n/a)</td><td>163.50 (n/a)</td><td>156.20 (n/a)</td><td>124.60 (n/a)</td><td>28.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>199.94 (n/a)</td><td>197.30 (n/a)</td><td>177.40 (n/a)</td><td>16.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.35 (+0.93%)</td><td>0.30 (+3.19%)</td><td>0.29 (+4.70%)</td><td>0.27 <b>(+21.29%)</b></td><td>0.03 <b>(-38.32%)</b></td><td>182.10 (-17.53%)</td><td>164.14 (-4.78%)</td><td>167.10 (-4.51%)</td><td>139.20 (-0.93%)</td><td>15.88 <b>(-50.03%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>220.80 (n/a)</td><td>172.38 (n/a)</td><td>175.00 (n/a)</td><td>140.50 (n/a)</td><td>31.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>202.20 (n/a)</td><td>168.26 (n/a)</td><td>176.00 (n/a)</td><td>138.90 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>235.90 (n/a)</td><td>188.98 (n/a)</td><td>193.30 (n/a)</td><td>141.40 (n/a)</td><td>35.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>217.20 (n/a)</td><td>191.06 (n/a)</td><td>201.40 (n/a)</td><td>163.20 (n/a)</td><td>23.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>218.80 (n/a)</td><td>172.62 (n/a)</td><td>177.80 (n/a)</td><td>128.60 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.10 (n/a)</td><td>183.96 (n/a)</td><td>189.70 (n/a)</td><td>137.30 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.40 (n/a)</td><td>214.28 (n/a)</td><td>226.20 (n/a)</td><td>158.20 (n/a)</td><td>34.85 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.00 (n/a)</td><td>207.48 (n/a)</td><td>225.60 (n/a)</td><td>152.70 (n/a)</td><td>35.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>176.32 (n/a)</td><td>191.30 (n/a)</td><td>131.20 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>284.70 (n/a)</td><td>203.00 (n/a)</td><td>186.40 (n/a)</td><td>161.90 (n/a)</td><td>47.49 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>195.64 (n/a)</td><td>188.60 (n/a)</td><td>168.20 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>225.50 (n/a)</td><td>208.92 (n/a)</td><td>213.30 (n/a)</td><td>185.60 (n/a)</td><td>15.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>191.70 (n/a)</td><td>163.26 (n/a)</td><td>174.80 (n/a)</td><td>112.90 (n/a)</td><td>33.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>326.40 (n/a)</td><td>194.56 (n/a)</td><td>169.10 (n/a)</td><td>133.20 (n/a)</td><td>78.43 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>377.80 (n/a)</td><td>204.18 (n/a)</td><td>174.10 (n/a)</td><td>110.60 (n/a)</td><td>105.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>237.50 (n/a)</td><td>188.00 (n/a)</td><td>203.00 (n/a)</td><td>119.00 (n/a)</td><td>44.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>212.20 (n/a)</td><td>173.58 (n/a)</td><td>173.90 (n/a)</td><td>133.60 (n/a)</td><td>37.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>194.70 (n/a)</td><td>163.34 (n/a)</td><td>171.70 (n/a)</td><td>128.70 (n/a)</td><td>30.38 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>219.30 (n/a)</td><td>183.98 (n/a)</td><td>199.80 (n/a)</td><td>125.90 (n/a)</td><td>36.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>15.53 (+10.52%)</td><td>13.98 (+3.16%)</td><td>14.03 (+2.54%)</td><td>12.15 (-4.64%)</td><td>1.29 <b>(+160.60%)</b></td><td>4585.70 (+4.87%)</td><td>4012.56 (-2.49%)</td><td>3969.70 (-2.48%)</td><td>3586.40 (-9.52%)</td><td>382.14 <b>(+146.55%)</b></td><td>14969.60 (+10.52%)</td><td>13474.14 (+3.16%)</td><td>13524.37 (+2.54%)</td><td>11707.40 (-4.64%)</td><td>1241.99 <b>(+160.60%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>14.05 (n/a)</td><td>13.55 (n/a)</td><td>13.69 (n/a)</td><td>12.74 (n/a)</td><td>0.49 (n/a)</td><td>4372.80 (n/a)</td><td>4115.06 (n/a)</td><td>4070.60 (n/a)</td><td>3963.70 (n/a)</td><td>154.99 (n/a)</td><td>13544.75 (n/a)</td><td>13060.86 (n/a)</td><td>13189.13 (n/a)</td><td>12277.48 (n/a)</td><td>476.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>20.17 (-9.04%)</td><td>17.80 (-0.59%)</td><td>17.37 (+1.43%)</td><td>15.91 (-1.86%)</td><td>1.72 <b>(-29.10%)</b></td><td>823.80 (+1.90%)</td><td>741.64 (+0.05%)</td><td>754.70 (-1.41%)</td><td>649.70 (+9.93%)</td><td>70.02 (-18.91%)</td><td>13221.24 (-9.04%)</td><td>11667.47 (-0.59%)</td><td>11381.81 (+1.43%)</td><td>10427.74 (-1.86%)</td><td>1127.33 <b>(-29.10%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>22.18 (n/a)</td><td>17.91 (n/a)</td><td>17.12 (n/a)</td><td>16.21 (n/a)</td><td>2.43 (n/a)</td><td>808.40 (n/a)</td><td>741.26 (n/a)</td><td>765.50 (n/a)</td><td>591.00 (n/a)</td><td>86.35 (n/a)</td><td>14535.78 (n/a)</td><td>11736.57 (n/a)</td><td>11221.59 (n/a)</td><td>10625.40 (n/a)</td><td>1589.93 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>15.07 (+0.22%)</td><td>13.81 (+1.08%)</td><td>13.93 (+0.22%)</td><td>12.10 (-3.49%)</td><td>1.08 (+10.53%)</td><td>4605.30 (+3.61%)</td><td>4053.84 (-0.96%)</td><td>3998.90 (-0.22%)</td><td>3695.60 (-0.22%)</td><td>335.93 (+15.66%)</td><td>14527.40 (+0.22%)</td><td>13312.50 (+1.08%)</td><td>13425.36 (+0.22%)</td><td>11657.66 (-3.49%)</td><td>1043.25 (+10.53%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>15.04 (n/a)</td><td>13.67 (n/a)</td><td>13.90 (n/a)</td><td>12.53 (n/a)</td><td>0.98 (n/a)</td><td>4444.70 (n/a)</td><td>4092.98 (n/a)</td><td>4007.60 (n/a)</td><td>3703.70 (n/a)</td><td>290.44 (n/a)</td><td>14495.65 (n/a)</td><td>13170.40 (n/a)</td><td>13396.37 (n/a)</td><td>12078.88 (n/a)</td><td>943.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>19.07 (-5.61%)</td><td>17.01 (+4.31%)</td><td>17.16 (+3.58%)</td><td>12.99 (+6.64%)</td><td>2.45 (-15.25%)</td><td>1375.00 (-6.23%)</td><td>1070.06 (-4.86%)</td><td>1040.50 (-3.45%)</td><td>936.30 (+5.94%)</td><td>178.61 (-16.58%)</td><td>14334.57 (-5.61%)</td><td>12787.54 (+4.31%)</td><td>12899.96 (+3.58%)</td><td>9761.02 (+6.64%)</td><td>1841.05 (-15.25%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>20.21 (n/a)</td><td>16.31 (n/a)</td><td>16.57 (n/a)</td><td>12.18 (n/a)</td><td>2.89 (n/a)</td><td>1466.30 (n/a)</td><td>1124.74 (n/a)</td><td>1077.70 (n/a)</td><td>883.80 (n/a)</td><td>214.11 (n/a)</td><td>15186.66 (n/a)</td><td>12258.77 (n/a)</td><td>12454.38 (n/a)</td><td>9153.61 (n/a)</td><td>2172.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>11.00 (-0.48%)</td><td>10.59 (-1.61%)</td><td>10.54 (-2.87%)</td><td>10.21 (-1.22%)</td><td>0.30 (+2.84%)</td><td>8022.90 (+1.23%)</td><td>7740.14 (+1.64%)</td><td>7775.30 (+2.96%)</td><td>7448.40 (+0.48%)</td><td>217.77 (+4.47%)</td><td>14415.72 (-0.48%)</td><td>13881.19 (-1.61%)</td><td>13809.72 (-2.87%)</td><td>13383.46 (-1.22%)</td><td>391.72 (+2.84%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>11.05 (n/a)</td><td>10.76 (n/a)</td><td>10.85 (n/a)</td><td>10.34 (n/a)</td><td>0.29 (n/a)</td><td>7925.10 (n/a)</td><td>7615.18 (n/a)</td><td>7552.00 (n/a)</td><td>7412.70 (n/a)</td><td>208.44 (n/a)</td><td>14485.09 (n/a)</td><td>14108.34 (n/a)</td><td>14217.92 (n/a)</td><td>13548.54 (n/a)</td><td>380.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>20.26 (+2.44%)</td><td>17.55 (+1.19%)</td><td>18.44 (+1.10%)</td><td>12.26 (-4.60%)</td><td>3.08 (+15.75%)</td><td>1753.80 (+4.82%)</td><td>1263.96 (-0.33%)</td><td>1165.90 (-1.09%)</td><td>1061.00 (-2.39%)</td><td>278.59 (+19.48%)</td><td>16191.39 (+2.44%)</td><td>14024.24 (+1.19%)</td><td>14735.68 (+1.10%)</td><td>9795.52 (-4.60%)</td><td>2464.39 (+15.75%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>19.78 (n/a)</td><td>17.34 (n/a)</td><td>18.24 (n/a)</td><td>12.85 (n/a)</td><td>2.66 (n/a)</td><td>1673.20 (n/a)</td><td>1268.10 (n/a)</td><td>1178.70 (n/a)</td><td>1087.00 (n/a)</td><td>233.17 (n/a)</td><td>15805.24 (n/a)</td><td>13859.40 (n/a)</td><td>14574.81 (n/a)</td><td>10267.89 (n/a)</td><td>2129.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>12.51 (-0.56%)</td><td>12.18 (-0.63%)</td><td>12.36 (-0.46%)</td><td>11.20 (-5.31%)</td><td>0.55 <b>(+72.88%)</b></td><td>7311.00 (+5.61%)</td><td>6736.34 (+0.75%)</td><td>6629.40 (+0.47%)</td><td>6546.50 (+0.56%)</td><td>323.93 <b>(+84.29%)</b></td><td>16401.82 (-0.56%)</td><td>15967.33 (-0.63%)</td><td>16196.72 (-0.46%)</td><td>14686.61 (-5.31%)</td><td>723.28 <b>(+72.88%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>12.58 (n/a)</td><td>12.26 (n/a)</td><td>12.41 (n/a)</td><td>11.83 (n/a)</td><td>0.32 (n/a)</td><td>6922.70 (n/a)</td><td>6685.92 (n/a)</td><td>6598.70 (n/a)</td><td>6510.00 (n/a)</td><td>175.77 (n/a)</td><td>16493.74 (n/a)</td><td>16068.54 (n/a)</td><td>16272.08 (n/a)</td><td>15510.45 (n/a)</td><td>418.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.90 (+0.46%)</td><td>3.90 (+12.84%)</td><td>4.15 <b>(+31.07%)</b></td><td>2.99 (-0.44%)</td><td>0.81 (+0.43%)</td><td>460.70 (+0.44%)</td><td>365.64 (-11.24%)</td><td>331.20 <b>(-23.72%)</b></td><td>280.80 (-0.46%)</td><td>77.78 (+5.27%)</td><td>956.06 (+0.46%)</td><td>760.64 (+12.84%)</td><td>810.37 <b>(+31.07%)</b></td><td>582.65 (-0.44%)</td><td>157.02 (+0.43%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>4.88 (n/a)</td><td>3.46 (n/a)</td><td>3.17 (n/a)</td><td>3.00 (n/a)</td><td>0.80 (n/a)</td><td>458.70 (n/a)</td><td>411.92 (n/a)</td><td>434.20 (n/a)</td><td>282.10 (n/a)</td><td>73.89 (n/a)</td><td>951.71 (n/a)</td><td>674.09 (n/a)</td><td>618.27 (n/a)</td><td>585.23 (n/a)</td><td>156.35 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>6.75 (+14.25%)</td><td>4.39 (+6.30%)</td><td>3.87 (+6.34%)</td><td>3.56 <b>(+70.61%)</b></td><td>1.34 (-14.55%)</td><td>387.00 <b>(-41.38%)</b></td><td>331.54 (-13.32%)</td><td>355.40 (-5.95%)</td><td>204.00 (-12.45%)</td><td>74.21 <b>(-56.59%)</b></td><td>1316.13 (+14.25%)</td><td>856.05 (+6.30%)</td><td>755.29 (+6.34%)</td><td>693.69 <b>(+70.61%)</b></td><td>260.72 (-14.55%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.91 (n/a)</td><td>4.13 (n/a)</td><td>3.64 (n/a)</td><td>2.08 (n/a)</td><td>1.56 (n/a)</td><td>660.20 (n/a)</td><td>382.50 (n/a)</td><td>377.90 (n/a)</td><td>233.00 (n/a)</td><td>170.95 (n/a)</td><td>1151.92 (n/a)</td><td>805.31 (n/a)</td><td>710.28 (n/a)</td><td>406.60 (n/a)</td><td>305.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.19 (-3.88%)</td><td>5.11 (+6.74%)</td><td>4.05 (+6.37%)</td><td>3.56 (-3.99%)</td><td>1.91 (-8.60%)</td><td>386.80 (+4.17%)</td><td>295.48 (-7.21%)</td><td>339.80 (-6.00%)</td><td>168.00 (+4.02%)</td><td>89.50 (+0.42%)</td><td>1597.83 (-3.88%)</td><td>997.05 (+6.74%)</td><td>789.99 (+6.37%)</td><td>694.03 (-3.99%)</td><td>373.44 (-8.60%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.52 (n/a)</td><td>4.79 (n/a)</td><td>3.81 (n/a)</td><td>3.71 (n/a)</td><td>2.09 (n/a)</td><td>371.30 (n/a)</td><td>318.44 (n/a)</td><td>361.50 (n/a)</td><td>161.50 (n/a)</td><td>89.12 (n/a)</td><td>1662.38 (n/a)</td><td>934.09 (n/a)</td><td>742.65 (n/a)</td><td>722.89 (n/a)</td><td>408.58 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>6.83 (-2.74%)</td><td>4.52 (-1.20%)</td><td>4.14 (-1.20%)</td><td>3.65 (+5.90%)</td><td>1.31 (-8.00%)</td><td>377.30 (-5.56%)</td><td>320.64 (+0.20%)</td><td>332.80 (+1.22%)</td><td>201.60 (+2.80%)</td><td>69.60 (-10.64%)</td><td>1331.70 (-2.74%)</td><td>881.25 (-1.20%)</td><td>806.57 (-1.20%)</td><td>711.51 (+5.90%)</td><td>255.69 (-8.00%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>7.02 (n/a)</td><td>4.57 (n/a)</td><td>4.19 (n/a)</td><td>3.44 (n/a)</td><td>1.42 (n/a)</td><td>399.50 (n/a)</td><td>320.00 (n/a)</td><td>328.80 (n/a)</td><td>196.10 (n/a)</td><td>77.89 (n/a)</td><td>1369.20 (n/a)</td><td>891.99 (n/a)</td><td>816.35 (n/a)</td><td>671.88 (n/a)</td><td>277.92 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.40 <b>(-28.38%)</b></td><td>3.61 (-18.36%)</td><td>3.45 (-18.97%)</td><td>3.25 (+0.40%)</td><td>0.45 <b>(-62.17%)</b></td><td>422.80 (-0.40%)</td><td>385.06 (+17.10%)</td><td>398.40 <b>(+23.42%)</b></td><td>312.70 <b>(+39.60%)</b></td><td>42.45 <b>(-49.59%)</b></td><td>858.35 <b>(-28.38%)</b></td><td>704.89 (-18.36%)</td><td>673.80 (-18.97%)</td><td>634.88 (+0.40%)</td><td>88.34 <b>(-62.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.14 (n/a)</td><td>4.43 (n/a)</td><td>4.26 (n/a)</td><td>3.24 (n/a)</td><td>1.20 (n/a)</td><td>424.50 (n/a)</td><td>328.84 (n/a)</td><td>322.80 (n/a)</td><td>224.00 (n/a)</td><td>84.22 (n/a)</td><td>1198.45 (n/a)</td><td>863.38 (n/a)</td><td>831.53 (n/a)</td><td>632.35 (n/a)</td><td>233.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>6.43 (+14.44%)</td><td>4.60 (+11.01%)</td><td>4.48 <b>(+28.14%)</b></td><td>3.27 (+3.08%)</td><td>1.30 (+9.72%)</td><td>421.30 (-2.99%)</td><td>318.80 (-9.83%)</td><td>306.90 <b>(-21.97%)</b></td><td>214.10 (-12.61%)</td><td>87.08 (-5.86%)</td><td>1253.98 (+14.44%)</td><td>896.59 (+11.01%)</td><td>874.66 <b>(+28.14%)</b></td><td>637.17 (+3.08%)</td><td>254.06 (+9.72%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.62 (n/a)</td><td>4.14 (n/a)</td><td>3.50 (n/a)</td><td>3.17 (n/a)</td><td>1.19 (n/a)</td><td>434.30 (n/a)</td><td>353.54 (n/a)</td><td>393.30 (n/a)</td><td>245.00 (n/a)</td><td>92.49 (n/a)</td><td>1095.77 (n/a)</td><td>807.64 (n/a)</td><td>682.60 (n/a)</td><td>618.14 (n/a)</td><td>231.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.81 <b>(-28.69%)</b></td><td>4.04 (-10.60%)</td><td>3.91 (-13.39%)</td><td>3.17 (+7.51%)</td><td>0.63 <b>(-61.17%)</b></td><td>434.30 (-6.98%)</td><td>347.56 (+2.87%)</td><td>351.90 (+15.45%)</td><td>286.10 <b>(+40.25%)</b></td><td>56.87 <b>(-52.36%)</b></td><td>938.21 <b>(-28.69%)</b></td><td>788.20 (-10.60%)</td><td>762.71 (-13.39%)</td><td>618.11 (+7.51%)</td><td>122.60 <b>(-61.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.75 (n/a)</td><td>4.52 (n/a)</td><td>4.51 (n/a)</td><td>2.95 (n/a)</td><td>1.62 (n/a)</td><td>466.90 (n/a)</td><td>337.86 (n/a)</td><td>304.80 (n/a)</td><td>204.00 (n/a)</td><td>119.36 (n/a)</td><td>1315.69 (n/a)</td><td>881.65 (n/a)</td><td>880.61 (n/a)</td><td>574.94 (n/a)</td><td>315.75 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>2.39 (+0.66%)</td><td>1.73 (-11.86%)</td><td>1.60 (-15.34%)</td><td>1.43 (-18.48%)</td><td>0.40 <b>(+62.93%)</b></td><td>281.20 <b>(+22.69%)</b></td><td>240.88 (+16.30%)</td><td>251.30 (+18.15%)</td><td>167.70 (-0.65%)</td><td>46.26 <b>(+102.35%)</b></td><td>200.06 (+0.66%)</td><td>144.35 (-11.86%)</td><td>133.54 (-15.34%)</td><td>119.33 (-18.48%)</td><td>33.13 <b>(+62.93%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>2.38 (n/a)</td><td>1.96 (n/a)</td><td>1.89 (n/a)</td><td>1.75 (n/a)</td><td>0.24 (n/a)</td><td>229.20 (n/a)</td><td>207.12 (n/a)</td><td>212.70 (n/a)</td><td>168.80 (n/a)</td><td>22.86 (n/a)</td><td>198.75 (n/a)</td><td>163.78 (n/a)</td><td>157.74 (n/a)</td><td>146.38 (n/a)</td><td>20.34 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.58 (-1.54%)</td><td>6.26 (+4.24%)</td><td>5.33 (+5.28%)</td><td>4.92 (-1.93%)</td><td>1.60 (+0.84%)</td><td>392.70 (+1.97%)</td><td>323.98 (-3.83%)</td><td>362.60 (-5.00%)</td><td>225.40 (+1.58%)</td><td>73.94 (+4.34%)</td><td>1786.40 (-1.54%)</td><td>1303.35 (+4.24%)</td><td>1110.55 (+5.28%)</td><td>1025.35 (-1.93%)</td><td>333.50 (+0.84%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.71 (n/a)</td><td>6.00 (n/a)</td><td>5.06 (n/a)</td><td>5.02 (n/a)</td><td>1.59 (n/a)</td><td>385.10 (n/a)</td><td>336.88 (n/a)</td><td>381.70 (n/a)</td><td>221.90 (n/a)</td><td>70.86 (n/a)</td><td>1814.39 (n/a)</td><td>1250.36 (n/a)</td><td>1054.88 (n/a)</td><td>1045.52 (n/a)</td><td>330.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>18.84 (+2.62%)</td><td>15.09 (-0.52%)</td><td>15.97 (+4.20%)</td><td>11.05 (-9.09%)</td><td>3.06 (+9.81%)</td><td>498.10 (+10.00%)</td><td>378.02 (+1.31%)</td><td>344.70 (-4.01%)</td><td>292.20 (-2.54%)</td><td>81.98 (+17.81%)</td><td>7350.22 (+2.62%)</td><td>5885.64 (-0.52%)</td><td>6230.80 (+4.20%)</td><td>4311.19 (-9.09%)</td><td>1193.83 (+9.81%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>18.36 (n/a)</td><td>15.17 (n/a)</td><td>15.33 (n/a)</td><td>12.16 (n/a)</td><td>2.79 (n/a)</td><td>452.80 (n/a)</td><td>373.14 (n/a)</td><td>359.10 (n/a)</td><td>299.80 (n/a)</td><td>69.59 (n/a)</td><td>7162.36 (n/a)</td><td>5916.33 (n/a)</td><td>5979.50 (n/a)</td><td>4742.37 (n/a)</td><td>1087.14 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>11.28 (+5.30%)</td><td>8.76 (-2.62%)</td><td>8.34 (+1.33%)</td><td>7.52 (-1.81%)</td><td>1.45 (-1.25%)</td><td>732.50 (+1.85%)</td><td>640.14 (+2.52%)</td><td>659.90 (-1.32%)</td><td>488.10 (-5.04%)</td><td>90.67 (-6.69%)</td><td>4399.51 (+5.30%)</td><td>3418.50 (-2.62%)</td><td>3254.37 (+1.33%)</td><td>2931.86 (-1.81%)</td><td>566.10 (-1.25%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>10.71 (n/a)</td><td>9.00 (n/a)</td><td>8.23 (n/a)</td><td>7.65 (n/a)</td><td>1.47 (n/a)</td><td>719.20 (n/a)</td><td>624.38 (n/a)</td><td>668.70 (n/a)</td><td>514.00 (n/a)</td><td>97.17 (n/a)</td><td>4178.02 (n/a)</td><td>3510.64 (n/a)</td><td>3211.53 (n/a)</td><td>2985.83 (n/a)</td><td>573.26 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.38 (-13.18%)</td><td>10.70 (-0.50%)</td><td>9.48 (-1.62%)</td><td>8.90 (+2.48%)</td><td>2.20 (-19.27%)</td><td>651.30 (-2.43%)</td><td>559.56 (-0.49%)</td><td>611.60 (+1.65%)</td><td>433.50 (+15.17%)</td><td>107.54 (-6.64%)</td><td>5573.12 (-13.18%)</td><td>4458.42 (-0.50%)</td><td>3949.94 (-1.62%)</td><td>3709.27 (+2.48%)</td><td>917.12 (-19.27%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>15.41 (n/a)</td><td>10.76 (n/a)</td><td>9.64 (n/a)</td><td>8.69 (n/a)</td><td>2.73 (n/a)</td><td>667.50 (n/a)</td><td>562.32 (n/a)</td><td>601.70 (n/a)</td><td>376.40 (n/a)</td><td>115.19 (n/a)</td><td>6419.10 (n/a)</td><td>4480.63 (n/a)</td><td>4014.88 (n/a)</td><td>3619.53 (n/a)</td><td>1135.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.80 (n/a)</td><td>180.28 (n/a)</td><td>182.40 (n/a)</td><td>148.70 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>162.04 (n/a)</td><td>166.10 (n/a)</td><td>118.70 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.20 (n/a)</td><td>155.50 (n/a)</td><td>164.90 (n/a)</td><td>116.20 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>174.08 (n/a)</td><td>191.70 (n/a)</td><td>118.00 (n/a)</td><td>44.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>179.86 (n/a)</td><td>158.60 (n/a)</td><td>133.20 (n/a)</td><td>45.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>184.84 (n/a)</td><td>197.10 (n/a)</td><td>146.50 (n/a)</td><td>24.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>286.60 (n/a)</td><td>219.94 (n/a)</td><td>211.90 (n/a)</td><td>162.50 (n/a)</td><td>44.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.90 (n/a)</td><td>222.54 (n/a)</td><td>228.80 (n/a)</td><td>195.30 (n/a)</td><td>18.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>161.04 (n/a)</td><td>166.70 (n/a)</td><td>114.30 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>174.38 (n/a)</td><td>163.50 (n/a)</td><td>148.50 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>175.90 (n/a)</td><td>176.80 (n/a)</td><td>136.30 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>183.16 (n/a)</td><td>193.20 (n/a)</td><td>143.20 (n/a)</td><td>30.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>177.86 (n/a)</td><td>206.80 (n/a)</td><td>122.70 (n/a)</td><td>45.91 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.30 (n/a)</td><td>190.18 (n/a)</td><td>178.80 (n/a)</td><td>146.90 (n/a)</td><td>42.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>288.20 (n/a)</td><td>193.34 (n/a)</td><td>190.20 (n/a)</td><td>109.40 (n/a)</td><td>63.46 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.60 (n/a)</td><td>209.80 (n/a)</td><td>229.90 (n/a)</td><td>131.30 (n/a)</td><td>44.14 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.10 (n/a)</td><td>170.36 (n/a)</td><td>172.70 (n/a)</td><td>146.50 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>243.10 (n/a)</td><td>176.02 (n/a)</td><td>184.00 (n/a)</td><td>105.30 (n/a)</td><td>49.49 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>244.50 (n/a)</td><td>189.86 (n/a)</td><td>176.70 (n/a)</td><td>159.10 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.10 (n/a)</td><td>168.76 (n/a)</td><td>179.10 (n/a)</td><td>127.70 (n/a)</td><td>29.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>238.80 (n/a)</td><td>184.02 (n/a)</td><td>177.70 (n/a)</td><td>143.40 (n/a)</td><td>37.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>270.80 (n/a)</td><td>198.98 (n/a)</td><td>178.90 (n/a)</td><td>152.20 (n/a)</td><td>46.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>183.48 (n/a)</td><td>181.50 (n/a)</td><td>167.20 (n/a)</td><td>13.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>263.90 (n/a)</td><td>208.18 (n/a)</td><td>201.20 (n/a)</td><td>166.20 (n/a)</td><td>39.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>240.80 (n/a)</td><td>173.46 (n/a)</td><td>169.80 (n/a)</td><td>128.80 (n/a)</td><td>44.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>287.20 (n/a)</td><td>213.38 (n/a)</td><td>202.60 (n/a)</td><td>139.00 (n/a)</td><td>54.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>207.50 (n/a)</td><td>167.16 (n/a)</td><td>179.20 (n/a)</td><td>117.30 (n/a)</td><td>34.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>201.70 (n/a)</td><td>186.12 (n/a)</td><td>193.80 (n/a)</td><td>150.50 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.60 (n/a)</td><td>178.86 (n/a)</td><td>197.20 (n/a)</td><td>147.90 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>208.30 (n/a)</td><td>176.40 (n/a)</td><td>202.90 (n/a)</td><td>109.40 (n/a)</td><td>42.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>310.20 (n/a)</td><td>215.46 (n/a)</td><td>199.60 (n/a)</td><td>158.80 (n/a)</td><td>57.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>322.70 (n/a)</td><td>266.42 (n/a)</td><td>281.30 (n/a)</td><td>204.20 (n/a)</td><td>57.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.12 (+0.09%)</td><td>4.11 (+0.05%)</td><td>4.11 (+0.16%)</td><td>4.10 (-0.09%)</td><td>0.01 (+18.80%)</td><td>19199.20 (+0.09%)</td><td>19135.78 (-0.05%)</td><td>19131.60 (-0.16%)</td><td>19086.00 (-0.09%)</td><td>41.33 (+18.87%)</td><td>2812.91 (+0.09%)</td><td>2805.60 (+0.05%)</td><td>2806.20 (+0.16%)</td><td>2796.32 (-0.09%)</td><td>6.05 (+18.80%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.10 (n/a)</td><td>4.10 (n/a)</td><td>0.01 (n/a)</td><td>19181.20 (n/a)</td><td>19144.58 (n/a)</td><td>19162.00 (n/a)</td><td>19103.20 (n/a)</td><td>34.77 (n/a)</td><td>2810.37 (n/a)</td><td>2804.31 (n/a)</td><td>2801.75 (n/a)</td><td>2798.95 (n/a)</td><td>5.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.81 (+8.31%)</td><td>4.20 (+2.71%)</td><td>4.20 (+0.17%)</td><td>3.57 (-5.01%)</td><td>0.44 <b>(+57.45%)</b></td><td>2632.80 (+5.28%)</td><td>2259.78 (-2.13%)</td><td>2238.20 (-0.17%)</td><td>1956.80 (-7.68%)</td><td>242.14 <b>(+53.08%)</b></td><td>1890.52 (+8.31%)</td><td>1651.74 (+2.71%)</td><td>1652.81 (+0.17%)</td><td>1405.09 (-5.01%)</td><td>172.44 <b>(+57.45%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>4.44 (n/a)</td><td>4.09 (n/a)</td><td>4.19 (n/a)</td><td>3.76 (n/a)</td><td>0.28 (n/a)</td><td>2500.80 (n/a)</td><td>2308.92 (n/a)</td><td>2241.90 (n/a)</td><td>2119.50 (n/a)</td><td>158.18 (n/a)</td><td>1745.41 (n/a)</td><td>1608.21 (n/a)</td><td>1650.08 (n/a)</td><td>1479.26 (n/a)</td><td>109.52 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.57 <b>(+70.81%)</b></td><td>1.14 <b>(+50.75%)</b></td><td>1.15 <b>(+58.19%)</b></td><td>0.87 <b>(+34.82%)</b></td><td>0.29 <b>(+165.82%)</b></td><td>255.00 <b>(-25.85%)</b></td><td>203.54 <b>(-31.32%)</b></td><td>192.60 <b>(-36.79%)</b></td><td>140.80 <b>(-41.43%)</b></td><td>49.96 <b>(+21.34%)</b></td><td>67.05 <b>(+70.81%)</b></td><td>48.79 <b>(+50.75%)</b></td><td>48.99 <b>(+58.19%)</b></td><td>37.00 <b>(+34.82%)</b></td><td>12.55 <b>(+165.82%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.92 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.64 (n/a)</td><td>0.11 (n/a)</td><td>343.90 (n/a)</td><td>296.36 (n/a)</td><td>304.70 (n/a)</td><td>240.40 (n/a)</td><td>41.18 (n/a)</td><td>39.25 (n/a)</td><td>32.37 (n/a)</td><td>30.97 (n/a)</td><td>27.45 (n/a)</td><td>4.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.61 (+8.26%)</td><td>1.15 (+9.77%)</td><td>1.15 (+10.36%)</td><td>0.68 (+5.10%)</td><td>0.33 (+10.33%)</td><td>325.90 (-4.85%)</td><td>208.46 (-8.32%)</td><td>191.50 (-9.41%)</td><td>137.30 (-7.60%)</td><td>70.32 (-1.05%)</td><td>68.75 (+8.26%)</td><td>48.93 (+9.77%)</td><td>49.27 (+10.36%)</td><td>28.96 (+5.10%)</td><td>14.19 (+10.33%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.49 (n/a)</td><td>1.04 (n/a)</td><td>1.05 (n/a)</td><td>0.65 (n/a)</td><td>0.30 (n/a)</td><td>342.50 (n/a)</td><td>227.38 (n/a)</td><td>211.40 (n/a)</td><td>148.60 (n/a)</td><td>71.07 (n/a)</td><td>63.50 (n/a)</td><td>44.57 (n/a)</td><td>44.65 (n/a)</td><td>27.55 (n/a)</td><td>12.86 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.53 (+0.79%)</td><td>0.53 (+0.20%)</td><td>0.53 (+0.02%)</td><td>0.53 (-0.02%)</td><td>0.00 <b>(+248.86%)</b></td><td>47903.50 (+0.02%)</td><td>47730.36 (-0.20%)</td><td>47782.10 (-0.02%)</td><td>47406.00 (-0.78%)</td><td>189.04 <b>(+245.87%)</b></td><td>362.40 (+0.79%)</td><td>359.94 (+0.20%)</td><td>359.55 (+0.02%)</td><td>358.63 (-0.02%)</td><td>1.43 <b>(+248.87%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47895.20 (n/a)</td><td>47824.58 (n/a)</td><td>47791.50 (n/a)</td><td>47779.90 (n/a)</td><td>54.66 (n/a)</td><td>359.56 (n/a)</td><td>359.23 (n/a)</td><td>359.48 (n/a)</td><td>358.70 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (-2.20%)</td><td>0.21 (-0.36%)</td><td>0.21 (+0.45%)</td><td>0.21 (-0.46%)</td><td>0.00 <b>(-56.63%)</b></td><td>119615.70 (+0.46%)</td><td>118446.96 (+0.35%)</td><td>118137.00 (-0.45%)</td><td>117832.80 (+2.25%)</td><td>709.85 <b>(-55.35%)</b></td><td>145.80 (-2.20%)</td><td>145.05 (-0.36%)</td><td>145.42 (+0.45%)</td><td>143.63 (-0.46%)</td><td>0.86 <b>(-56.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119062.40 (n/a)</td><td>118038.30 (n/a)</td><td>118672.90 (n/a)</td><td>115245.00 (n/a)</td><td>1589.81 (n/a)</td><td>149.07 (n/a)</td><td>145.57 (n/a)</td><td>144.77 (n/a)</td><td>144.29 (n/a)</td><td>1.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.91 (+0.01%)</td><td>0.90 (+0.40%)</td><td>0.90 (+0.61%)</td><td>0.90 (+0.49%)</td><td>0.01 <b>(-25.68%)</b></td><td>28018.10 (-0.49%)</td><td>27820.66 (-0.40%)</td><td>27836.40 (-0.61%)</td><td>27545.10 (-0.01%)</td><td>171.85 <b>(-26.02%)</b></td><td>623.70 (+0.01%)</td><td>617.54 (+0.40%)</td><td>617.17 (+0.61%)</td><td>613.17 (+0.49%)</td><td>3.83 <b>(-25.68%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28155.80 (n/a)</td><td>27932.04 (n/a)</td><td>28006.20 (n/a)</td><td>27548.30 (n/a)</td><td>232.30 (n/a)</td><td>623.63 (n/a)</td><td>615.09 (n/a)</td><td>613.43 (n/a)</td><td>610.17 (n/a)</td><td>5.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.66 (+0.12%)</td><td>3.52 (-2.98%)</td><td>3.47 (-4.76%)</td><td>3.41 (-4.65%)</td><td>0.11 <b>(+194.27%)</b></td><td>7384.80 (+4.87%)</td><td>7159.96 (+3.14%)</td><td>7262.80 (+5.00%)</td><td>6867.40 (-0.12%)</td><td>219.42 <b>(+207.98%)</b></td><td>2501.66 (+0.12%)</td><td>2401.26 (-2.98%)</td><td>2365.45 (-4.76%)</td><td>2326.39 (-4.65%)</td><td>74.43 <b>(+194.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.66 (n/a)</td><td>3.63 (n/a)</td><td>3.64 (n/a)</td><td>3.57 (n/a)</td><td>0.04 (n/a)</td><td>7041.70 (n/a)</td><td>6942.06 (n/a)</td><td>6916.80 (n/a)</td><td>6875.40 (n/a)</td><td>71.24 (n/a)</td><td>2498.75 (n/a)</td><td>2474.96 (n/a)</td><td>2483.80 (n/a)</td><td>2439.73 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.23 (+12.16%)</td><td>3.03 (+5.91%)</td><td>3.09 (+7.81%)</td><td>2.76 (-2.08%)</td><td>0.18 <b>(+658.84%)</b></td><td>9118.70 (+2.12%)</td><td>8331.60 (-5.29%)</td><td>8139.50 (-7.25%)</td><td>7793.00 (-10.84%)</td><td>524.07 <b>(+592.72%)</b></td><td>2204.52 (+12.16%)</td><td>2068.35 (+5.91%)</td><td>2110.67 (+7.81%)</td><td>1884.04 (-2.08%)</td><td>126.18 <b>(+658.83%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>2.88 (n/a)</td><td>2.86 (n/a)</td><td>2.87 (n/a)</td><td>2.82 (n/a)</td><td>0.02 (n/a)</td><td>8929.30 (n/a)</td><td>8797.16 (n/a)</td><td>8775.60 (n/a)</td><td>8740.60 (n/a)</td><td>75.65 (n/a)</td><td>1965.53 (n/a)</td><td>1953.00 (n/a)</td><td>1957.69 (n/a)</td><td>1923.99 (n/a)</td><td>16.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.32 (-0.89%)</td><td>3.24 (+0.71%)</td><td>3.24 (+1.70%)</td><td>3.18 (+2.02%)</td><td>0.06 <b>(-33.83%)</b></td><td>7903.10 (-1.98%)</td><td>7768.00 (-0.73%)</td><td>7764.40 (-1.67%)</td><td>7591.40 (+0.90%)</td><td>136.69 <b>(-34.23%)</b></td><td>2263.07 (-0.89%)</td><td>2212.17 (+0.71%)</td><td>2212.65 (+1.70%)</td><td>2173.81 (+2.02%)</td><td>39.03 <b>(-33.83%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.34 (n/a)</td><td>3.22 (n/a)</td><td>3.19 (n/a)</td><td>3.12 (n/a)</td><td>0.09 (n/a)</td><td>8062.50 (n/a)</td><td>7825.28 (n/a)</td><td>7896.40 (n/a)</td><td>7524.00 (n/a)</td><td>207.84 (n/a)</td><td>2283.34 (n/a)</td><td>2196.68 (n/a)</td><td>2175.65 (n/a)</td><td>2130.83 (n/a)</td><td>58.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.80 (+0.03%)</td><td>0.80 (-0.01%)</td><td>0.80 (+0.00%)</td><td>0.80 (-0.08%)</td><td>0.00 <b>(+304.82%)</b></td><td>94875.30 (+0.08%)</td><td>94803.16 (+0.01%)</td><td>94788.40 (-0.00%)</td><td>94742.10 (-0.03%)</td><td>51.97 <b>(+304.68%)</b></td><td>725.33 (+0.03%)</td><td>724.87 (-0.01%)</td><td>724.98 (+0.00%)</td><td>724.31 (-0.08%)</td><td>0.40 <b>(+304.96%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94803.80 (n/a)</td><td>94791.32 (n/a)</td><td>94790.70 (n/a)</td><td>94770.90 (n/a)</td><td>12.84 (n/a)</td><td>725.11 (n/a)</td><td>724.96 (n/a)</td><td>724.96 (n/a)</td><td>724.86 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.73 (+0.00%)</td><td>0.73 (-0.03%)</td><td>0.73 (-0.00%)</td><td>0.73 (-0.14%)</td><td>0.00 <b>(+121.39%)</b></td><td>103544.20 (+0.14%)</td><td>103344.94 (+0.03%)</td><td>103303.10 (+0.00%)</td><td>103272.80 (-0.00%)</td><td>112.14 <b>(+121.71%)</b></td><td>665.42 (+0.00%)</td><td>664.95 (-0.03%)</td><td>665.22 (-0.00%)</td><td>663.67 (-0.14%)</td><td>0.72 <b>(+121.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103403.40 (n/a)</td><td>103317.64 (n/a)</td><td>103301.80 (n/a)</td><td>103272.90 (n/a)</td><td>50.58 (n/a)</td><td>665.42 (n/a)</td><td>665.13 (n/a)</td><td>665.23 (n/a)</td><td>664.58 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.69 (-0.53%)</td><td>0.68 (-0.30%)</td><td>0.68 (-0.18%)</td><td>0.68 (-0.24%)</td><td>0.00 <b>(-30.57%)</b></td><td>110890.90 (+0.24%)</td><td>110384.38 (+0.30%)</td><td>110272.00 (+0.18%)</td><td>110040.60 (+0.53%)</td><td>340.79 <b>(-30.02%)</b></td><td>624.49 (-0.53%)</td><td>622.55 (-0.30%)</td><td>623.18 (-0.18%)</td><td>619.70 (-0.24%)</td><td>1.92 <b>(-30.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110624.80 (n/a)</td><td>110052.98 (n/a)</td><td>110068.60 (n/a)</td><td>109462.70 (n/a)</td><td>486.97 (n/a)</td><td>627.79 (n/a)</td><td>624.43 (n/a)</td><td>624.33 (n/a)</td><td>621.19 (n/a)</td><td>2.76 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>2.83 (-0.08%)</td><td>2.81 (+0.16%)</td><td>2.80 (-0.04%)</td><td>2.80 (+0.01%)</td><td>0.02 (+12.50%)</td><td>37508.50 (-0.01%)</td><td>37346.58 (-0.16%)</td><td>37496.70 (+0.04%)</td><td>37101.40 (+0.08%)</td><td>212.50 (+12.67%)</td><td>2894.07 (-0.08%)</td><td>2875.15 (+0.16%)</td><td>2863.57 (-0.04%)</td><td>2862.66 (+0.01%)</td><td>16.39 (+12.50%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>2.83 (n/a)</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>0.01 (n/a)</td><td>37513.10 (n/a)</td><td>37406.38 (n/a)</td><td>37482.80 (n/a)</td><td>37070.70 (n/a)</td><td>188.61 (n/a)</td><td>2896.47 (n/a)</td><td>2870.54 (n/a)</td><td>2864.63 (n/a)</td><td>2862.31 (n/a)</td><td>14.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.59 (-5.25%)</td><td>7.03 (-2.59%)</td><td>6.94 (-2.32%)</td><td>6.49 (-3.42%)</td><td>0.47 (-0.32%)</td><td>1373.20 (+3.54%)</td><td>1271.68 (+2.69%)</td><td>1283.70 (+2.38%)</td><td>1174.60 (+5.53%)</td><td>85.43 (+9.81%)</td><td>457.06 (-5.25%)</td><td>423.71 (-2.59%)</td><td>418.22 (-2.32%)</td><td>390.96 (-3.42%)</td><td>28.59 (-0.32%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.01 (n/a)</td><td>7.22 (n/a)</td><td>7.11 (n/a)</td><td>6.72 (n/a)</td><td>0.48 (n/a)</td><td>1326.20 (n/a)</td><td>1238.34 (n/a)</td><td>1253.90 (n/a)</td><td>1113.00 (n/a)</td><td>77.80 (n/a)</td><td>482.37 (n/a)</td><td>434.98 (n/a)</td><td>428.17 (n/a)</td><td>404.82 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.04 (+1.93%)</td><td>6.00 (-10.07%)</td><td>6.24 (-7.76%)</td><td>4.87 <b>(-24.27%)</b></td><td>1.04 <b>(+361.30%)</b></td><td>1830.50 <b>(+32.05%)</b></td><td>1522.66 (+13.91%)</td><td>1429.30 (+8.41%)</td><td>1266.30 (-1.89%)</td><td>272.81 <b>(+500.72%)</b></td><td>423.98 (+1.93%)</td><td>361.53 (-10.07%)</td><td>375.62 (-7.76%)</td><td>293.30 <b>(-24.27%)</b></td><td>62.51 <b>(+361.30%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.91 (n/a)</td><td>6.67 (n/a)</td><td>6.76 (n/a)</td><td>6.43 (n/a)</td><td>0.22 (n/a)</td><td>1386.20 (n/a)</td><td>1336.68 (n/a)</td><td>1318.40 (n/a)</td><td>1290.70 (n/a)</td><td>45.41 (n/a)</td><td>415.95 (n/a)</td><td>402.01 (n/a)</td><td>407.23 (n/a)</td><td>387.29 (n/a)</td><td>13.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.11 (-1.30%)</td><td>6.64 (+5.96%)</td><td>6.78 (+3.42%)</td><td>5.73 <b>(+21.03%)</b></td><td>0.54 <b>(-42.11%)</b></td><td>1556.80 (-17.37%)</td><td>1350.30 (-7.02%)</td><td>1314.80 (-3.31%)</td><td>1253.30 (+1.32%)</td><td>119.99 <b>(-52.38%)</b></td><td>428.36 (-1.30%)</td><td>399.90 (+5.96%)</td><td>408.32 (+3.42%)</td><td>344.87 <b>(+21.03%)</b></td><td>32.50 <b>(-42.11%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>7.20 (n/a)</td><td>6.27 (n/a)</td><td>6.55 (n/a)</td><td>4.73 (n/a)</td><td>0.93 (n/a)</td><td>1884.10 (n/a)</td><td>1452.28 (n/a)</td><td>1359.80 (n/a)</td><td>1237.00 (n/a)</td><td>251.98 (n/a)</td><td>433.99 (n/a)</td><td>377.42 (n/a)</td><td>394.80 (n/a)</td><td>284.95 (n/a)</td><td>56.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.49 (+3.29%)</td><td>8.08 (-0.54%)</td><td>7.99 (-1.88%)</td><td>7.93 (-1.07%)</td><td>0.23 <b>(+157.74%)</b></td><td>4398.80 (+1.08%)</td><td>4315.42 (+0.59%)</td><td>4366.20 (+1.92%)</td><td>4104.60 (-3.18%)</td><td>119.74 <b>(+151.16%)</b></td><td>523.19 (+3.29%)</td><td>497.95 (-0.54%)</td><td>491.84 (-1.88%)</td><td>488.20 (-1.07%)</td><td>14.31 <b>(+157.74%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.22 (n/a)</td><td>8.13 (n/a)</td><td>8.14 (n/a)</td><td>8.01 (n/a)</td><td>0.09 (n/a)</td><td>4351.70 (n/a)</td><td>4289.94 (n/a)</td><td>4284.00 (n/a)</td><td>4239.60 (n/a)</td><td>47.68 (n/a)</td><td>506.52 (n/a)</td><td>500.63 (n/a)</td><td>501.29 (n/a)</td><td>493.48 (n/a)</td><td>5.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.65 (+0.66%)</td><td>7.31 (-1.68%)</td><td>7.13 (-5.99%)</td><td>7.04 (+1.91%)</td><td>0.29 (-1.97%)</td><td>4954.60 (-1.88%)</td><td>4776.40 (+1.70%)</td><td>4888.20 (+6.37%)</td><td>4556.90 (-0.66%)</td><td>189.82 (-4.98%)</td><td>471.26 (+0.66%)</td><td>450.18 (-1.68%)</td><td>439.32 (-5.99%)</td><td>433.43 (+1.91%)</td><td>18.12 (-1.97%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>7.60 (n/a)</td><td>7.43 (n/a)</td><td>7.59 (n/a)</td><td>6.90 (n/a)</td><td>0.30 (n/a)</td><td>5049.40 (n/a)</td><td>4696.68 (n/a)</td><td>4595.40 (n/a)</td><td>4587.20 (n/a)</td><td>199.77 (n/a)</td><td>468.14 (n/a)</td><td>457.86 (n/a)</td><td>467.31 (n/a)</td><td>425.30 (n/a)</td><td>18.49 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.50 (-3.92%)</td><td>7.18 (-4.41%)</td><td>7.23 (-3.81%)</td><td>6.77 (-2.56%)</td><td>0.33 (-5.99%)</td><td>5152.70 (+2.62%)</td><td>4865.86 (+4.60%)</td><td>4822.10 (+3.96%)</td><td>4650.50 (+4.08%)</td><td>225.20 (+0.00%)</td><td>461.77 (-3.92%)</td><td>442.09 (-4.41%)</td><td>445.34 (-3.81%)</td><td>416.77 (-2.56%)</td><td>20.26 (-5.99%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>7.80 (n/a)</td><td>7.51 (n/a)</td><td>7.52 (n/a)</td><td>6.94 (n/a)</td><td>0.35 (n/a)</td><td>5021.10 (n/a)</td><td>4651.92 (n/a)</td><td>4638.40 (n/a)</td><td>4468.40 (n/a)</td><td>225.20 (n/a)</td><td>480.60 (n/a)</td><td>462.47 (n/a)</td><td>462.98 (n/a)</td><td>427.69 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.81 (+0.43%)</td><td>0.80 (+0.07%)</td><td>0.80 (+0.03%)</td><td>0.80 (-0.11%)</td><td>0.00 <b>(+479.53%)</b></td><td>94231.80 (+0.11%)</td><td>93999.78 (-0.07%)</td><td>94021.30 (-0.03%)</td><td>93644.30 (-0.42%)</td><td>216.62 <b>(+477.30%)</b></td><td>733.84 (+0.43%)</td><td>731.06 (+0.07%)</td><td>730.89 (+0.03%)</td><td>729.26 (-0.11%)</td><td>1.69 <b>(+479.49%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94132.60 (n/a)</td><td>94066.16 (n/a)</td><td>94052.30 (n/a)</td><td>94043.70 (n/a)</td><td>37.52 (n/a)</td><td>730.72 (n/a)</td><td>730.54 (n/a)</td><td>730.65 (n/a)</td><td>730.03 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.74 (-0.02%)</td><td>0.74 (+0.02%)</td><td>0.74 (-0.01%)</td><td>0.74 (+0.14%)</td><td>0.00 <b>(-71.77%)</b></td><td>102625.40 (-0.14%)</td><td>102595.94 (-0.02%)</td><td>102600.60 (+0.01%)</td><td>102568.10 (+0.02%)</td><td>25.37 <b>(-71.79%)</b></td><td>669.99 (-0.02%)</td><td>669.81 (+0.02%)</td><td>669.78 (-0.01%)</td><td>669.61 (+0.14%)</td><td>0.17 <b>(-71.77%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102771.50 (n/a)</td><td>102615.00 (n/a)</td><td>102592.60 (n/a)</td><td>102552.40 (n/a)</td><td>89.95 (n/a)</td><td>670.09 (n/a)</td><td>669.68 (n/a)</td><td>669.83 (n/a)</td><td>668.66 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.71 (+0.29%)</td><td>0.71 (+0.18%)</td><td>0.71 (+0.11%)</td><td>0.71 (+0.20%)</td><td>0.00 <b>(+40.64%)</b></td><td>105944.90 (-0.20%)</td><td>105854.18 (-0.18%)</td><td>105917.90 (-0.11%)</td><td>105618.90 (-0.28%)</td><td>137.05 <b>(+39.91%)</b></td><td>650.64 (+0.29%)</td><td>649.19 (+0.18%)</td><td>648.80 (+0.11%)</td><td>648.63 (+0.20%)</td><td>0.84 <b>(+40.64%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106155.80 (n/a)</td><td>106042.76 (n/a)</td><td>106033.50 (n/a)</td><td>105920.00 (n/a)</td><td>97.96 (n/a)</td><td>648.79 (n/a)</td><td>648.04 (n/a)</td><td>648.09 (n/a)</td><td>647.35 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.80 (+0.06%)</td><td>3.58 (+1.20%)</td><td>3.66 (+0.02%)</td><td>3.23 (+0.16%)</td><td>0.23 (-16.40%)</td><td>2492.20 (-0.16%)</td><td>2259.54 (-1.34%)</td><td>2204.60 (-0.02%)</td><td>2119.30 (-0.06%)</td><td>153.13 (-17.29%)</td><td>997.46 (+0.06%)</td><td>938.87 (+1.20%)</td><td>958.88 (+0.02%)</td><td>848.21 (+0.16%)</td><td>61.28 (-16.40%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.80 (n/a)</td><td>3.54 (n/a)</td><td>3.66 (n/a)</td><td>3.23 (n/a)</td><td>0.28 (n/a)</td><td>2496.30 (n/a)</td><td>2290.22 (n/a)</td><td>2205.00 (n/a)</td><td>2120.50 (n/a)</td><td>185.13 (n/a)</td><td>996.88 (n/a)</td><td>927.76 (n/a)</td><td>958.69 (n/a)</td><td>846.83 (n/a)</td><td>73.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.51 <b>(+27.24%)</b></td><td>0.36 (+3.69%)</td><td>0.35 (-2.98%)</td><td>0.27 (-10.24%)</td><td>0.09 <b>(+101.30%)</b></td><td>4581.20 (+11.41%)</td><td>3578.10 (-0.67%)</td><td>3599.10 (+3.07%)</td><td>2421.60 <b>(-21.41%)</b></td><td>771.59 <b>(+65.89%)</b></td><td>27.71 <b>(+27.24%)</b></td><td>19.58 (+3.69%)</td><td>18.65 (-2.98%)</td><td>14.65 (-10.24%)</td><td>4.87 <b>(+101.30%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.04 (n/a)</td><td>4112.20 (n/a)</td><td>3602.30 (n/a)</td><td>3491.80 (n/a)</td><td>3081.30 (n/a)</td><td>465.11 (n/a)</td><td>21.78 (n/a)</td><td>18.88 (n/a)</td><td>19.22 (n/a)</td><td>16.32 (n/a)</td><td>2.42 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.56 (+3.40%)</td><td>4.51 (+3.51%)</td><td>4.89 (+8.55%)</td><td>3.52 (+4.03%)</td><td>0.88 (+8.81%)</td><td>1887.40 (-3.87%)</td><td>1523.54 (-3.05%)</td><td>1360.90 (-7.88%)</td><td>1195.80 (-3.29%)</td><td>308.21 (+3.10%)</td><td>1718.64 (+3.40%)</td><td>1392.73 (+3.51%)</td><td>1510.14 (+8.55%)</td><td>1088.93 (+4.03%)</td><td>271.80 (+8.81%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.38 (n/a)</td><td>4.35 (n/a)</td><td>4.50 (n/a)</td><td>3.39 (n/a)</td><td>0.81 (n/a)</td><td>1963.40 (n/a)</td><td>1571.54 (n/a)</td><td>1477.30 (n/a)</td><td>1236.50 (n/a)</td><td>298.93 (n/a)</td><td>1662.12 (n/a)</td><td>1345.49 (n/a)</td><td>1391.20 (n/a)</td><td>1046.78 (n/a)</td><td>249.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.31 (n/a)</td><td>12.06 (n/a)</td><td>11.72 (n/a)</td><td>10.96 (n/a)</td><td>1.10 (n/a)</td><td>13.31 (n/a)</td><td>12.06 (n/a)</td><td>11.71 (n/a)</td><td>10.95 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>24.17 (-2.61%)</td><td>23.32 (+1.05%)</td><td>23.70 (-1.10%)</td><td>22.28 (+17.15%)</td><td>0.83 <b>(-64.32%)</b></td><td>24.15 (-2.61%)</td><td>23.31 (+1.05%)</td><td>23.69 (-1.10%)</td><td>22.27 (+17.15%)</td><td>0.83 <b>(-64.32%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>24.82 (n/a)</td><td>23.08 (n/a)</td><td>23.96 (n/a)</td><td>19.02 (n/a)</td><td>2.32 (n/a)</td><td>24.80 (n/a)</td><td>23.06 (n/a)</td><td>23.95 (n/a)</td><td>19.01 (n/a)</td><td>2.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>40.95 (-1.10%)</td><td>39.31 (+5.59%)</td><td>38.95 (-1.60%)</td><td>37.60 <b>(+42.63%)</b></td><td>1.51 <b>(-75.82%)</b></td><td>40.92 (-1.10%)</td><td>39.28 (+5.59%)</td><td>38.92 (-1.60%)</td><td>37.58 <b>(+42.63%)</b></td><td>1.51 <b>(-75.82%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>41.40 (n/a)</td><td>37.23 (n/a)</td><td>39.58 (n/a)</td><td>26.36 (n/a)</td><td>6.25 (n/a)</td><td>41.38 (n/a)</td><td>37.20 (n/a)</td><td>39.55 (n/a)</td><td>26.35 (n/a)</td><td>6.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>44.48 (-0.14%)</td><td>41.64 (-0.09%)</td><td>41.48 (-1.24%)</td><td>39.92 (+6.05%)</td><td>1.81 <b>(-27.63%)</b></td><td>44.45 (-0.14%)</td><td>41.62 (-0.09%)</td><td>41.46 (-1.24%)</td><td>39.90 (+6.05%)</td><td>1.81 <b>(-27.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>44.54 (n/a)</td><td>41.68 (n/a)</td><td>42.00 (n/a)</td><td>37.64 (n/a)</td><td>2.50 (n/a)</td><td>44.51 (n/a)</td><td>41.65 (n/a)</td><td>41.98 (n/a)</td><td>37.62 (n/a)</td><td>2.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>12.02 (n/a)</td><td>11.41 (n/a)</td><td>11.79 (n/a)</td><td>10.58 (n/a)</td><td>0.66 (n/a)</td><td>12.02 (n/a)</td><td>11.40 (n/a)</td><td>11.79 (n/a)</td><td>10.57 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>24.82 (-0.89%)</td><td>23.78 (-3.41%)</td><td>24.04 (-2.84%)</td><td>22.03 (-8.16%)</td><td>1.05 <b>(+167.39%)</b></td><td>24.81 (-0.89%)</td><td>23.77 (-3.41%)</td><td>24.03 (-2.84%)</td><td>22.02 (-8.16%)</td><td>1.05 <b>(+167.39%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>25.05 (n/a)</td><td>24.62 (n/a)</td><td>24.75 (n/a)</td><td>23.99 (n/a)</td><td>0.39 (n/a)</td><td>25.03 (n/a)</td><td>24.61 (n/a)</td><td>24.73 (n/a)</td><td>23.98 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>41.96 (-0.43%)</td><td>36.79 (-6.63%)</td><td>39.63 (+0.54%)</td><td>23.63 <b>(-33.70%)</b></td><td>7.44 <b>(+190.61%)</b></td><td>41.93 (-0.43%)</td><td>36.76 (-6.63%)</td><td>39.61 (+0.54%)</td><td>23.62 <b>(-33.70%)</b></td><td>7.43 <b>(+190.61%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>42.14 (n/a)</td><td>39.40 (n/a)</td><td>39.42 (n/a)</td><td>35.64 (n/a)</td><td>2.56 (n/a)</td><td>42.11 (n/a)</td><td>39.37 (n/a)</td><td>39.40 (n/a)</td><td>35.62 (n/a)</td><td>2.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>45.14 (+1.44%)</td><td>40.10 (-4.20%)</td><td>42.21 (+2.28%)</td><td>27.76 <b>(-31.61%)</b></td><td>7.00 <b>(+329.01%)</b></td><td>45.11 (+1.44%)</td><td>40.07 (-4.20%)</td><td>42.18 (+2.28%)</td><td>27.75 <b>(-31.61%)</b></td><td>7.00 <b>(+329.01%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>44.50 (n/a)</td><td>41.85 (n/a)</td><td>41.27 (n/a)</td><td>40.60 (n/a)</td><td>1.63 (n/a)</td><td>44.47 (n/a)</td><td>41.83 (n/a)</td><td>41.24 (n/a)</td><td>40.57 (n/a)</td><td>1.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.07 (-8.34%)</td><td>8.34 (-8.42%)</td><td>8.12 (-13.53%)</td><td>7.79 (+1.94%)</td><td>0.56 <b>(-40.62%)</b></td><td>9.05 (-8.34%)</td><td>8.32 (-8.42%)</td><td>8.10 (-13.53%)</td><td>7.78 (+1.94%)</td><td>0.56 <b>(-40.62%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>9.89 (n/a)</td><td>9.10 (n/a)</td><td>9.39 (n/a)</td><td>7.64 (n/a)</td><td>0.94 (n/a)</td><td>9.87 (n/a)</td><td>9.09 (n/a)</td><td>9.37 (n/a)</td><td>7.63 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.06 (+5.02%)</td><td>0.98 (+8.01%)</td><td>0.97 (+7.71%)</td><td>0.88 (+8.29%)</td><td>0.08 (-2.26%)</td><td>1.05 (+5.02%)</td><td>0.96 (+8.01%)</td><td>0.96 (+7.71%)</td><td>0.86 (+8.29%)</td><td>0.08 (-2.26%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.01 (n/a)</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.81 (n/a)</td><td>0.08 (n/a)</td><td>1.00 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.80 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.32 (-3.01%)</td><td>1.19 (+2.40%)</td><td>1.22 (+3.60%)</td><td>1.06 (+5.88%)</td><td>0.13 (-4.39%)</td><td>1.31 (-3.01%)</td><td>1.18 (+2.40%)</td><td>1.20 (+3.60%)</td><td>1.04 (+5.88%)</td><td>0.13 (-4.39%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.36 (n/a)</td><td>1.16 (n/a)</td><td>1.17 (n/a)</td><td>1.00 (n/a)</td><td>0.13 (n/a)</td><td>1.35 (n/a)</td><td>1.15 (n/a)</td><td>1.16 (n/a)</td><td>0.99 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>17.62 (-7.25%)</td><td>16.14 (-2.46%)</td><td>15.78 (-7.43%)</td><td>15.55 (+13.58%)</td><td>0.85 <b>(-56.52%)</b></td><td>17.42 (-7.25%)</td><td>15.95 (-2.46%)</td><td>15.60 (-7.43%)</td><td>15.37 (+13.58%)</td><td>0.84 <b>(-56.52%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>19.00 (n/a)</td><td>16.55 (n/a)</td><td>17.05 (n/a)</td><td>13.69 (n/a)</td><td>1.95 (n/a)</td><td>18.78 (n/a)</td><td>16.35 (n/a)</td><td>16.85 (n/a)</td><td>13.53 (n/a)</td><td>1.93 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.96 (+2.10%)</td><td>13.48 (+2.79%)</td><td>13.34 (-1.31%)</td><td>13.01 (+6.61%)</td><td>0.39 <b>(-44.56%)</b></td><td>13.71 (+2.10%)</td><td>13.25 (+2.79%)</td><td>13.10 (-1.31%)</td><td>12.79 (+6.61%)</td><td>0.38 <b>(-44.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.67 (n/a)</td><td>13.12 (n/a)</td><td>13.51 (n/a)</td><td>12.21 (n/a)</td><td>0.70 (n/a)</td><td>13.43 (n/a)</td><td>12.89 (n/a)</td><td>13.28 (n/a)</td><td>11.99 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.21 (+2.33%)</td><td>8.01 (+1.03%)</td><td>7.82 (-2.25%)</td><td>7.27 (+10.36%)</td><td>0.81 (-5.96%)</td><td>9.05 (+2.33%)</td><td>7.87 (+1.03%)</td><td>7.68 (-2.25%)</td><td>7.14 (+10.36%)</td><td>0.80 (-5.96%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>9.00 (n/a)</td><td>7.93 (n/a)</td><td>8.00 (n/a)</td><td>6.59 (n/a)</td><td>0.86 (n/a)</td><td>8.84 (n/a)</td><td>7.79 (n/a)</td><td>7.86 (n/a)</td><td>6.47 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>6.02 (-13.33%)</td><td>5.40 (-8.82%)</td><td>5.59 (-3.66%)</td><td>4.17 (-17.32%)</td><td>0.73 (-17.07%)</td><td>5.92 (-13.33%)</td><td>5.31 (-8.82%)</td><td>5.50 (-3.66%)</td><td>4.10 (-17.32%)</td><td>0.72 (-17.07%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.94 (n/a)</td><td>5.92 (n/a)</td><td>5.81 (n/a)</td><td>5.04 (n/a)</td><td>0.88 (n/a)</td><td>6.83 (n/a)</td><td>5.83 (n/a)</td><td>5.71 (n/a)</td><td>4.96 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.47 (n/a)</td><td>13.02 (n/a)</td><td>13.07 (n/a)</td><td>12.59 (n/a)</td><td>0.32 (n/a)</td><td>13.46 (n/a)</td><td>13.01 (n/a)</td><td>13.06 (n/a)</td><td>12.58 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.18 (n/a)</td><td>12.32 (n/a)</td><td>12.57 (n/a)</td><td>10.49 (n/a)</td><td>1.11 (n/a)</td><td>13.17 (n/a)</td><td>12.31 (n/a)</td><td>12.56 (n/a)</td><td>10.48 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.10 (n/a)</td><td>162.22 (n/a)</td><td>164.80 (n/a)</td><td>144.90 (n/a)</td><td>15.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>149.92 (n/a)</td><td>161.60 (n/a)</td><td>108.60 (n/a)</td><td>34.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.80 (n/a)</td><td>168.60 (n/a)</td><td>171.80 (n/a)</td><td>137.20 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.10 (n/a)</td><td>169.68 (n/a)</td><td>162.00 (n/a)</td><td>152.90 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.10 (n/a)</td><td>185.62 (n/a)</td><td>179.80 (n/a)</td><td>128.20 (n/a)</td><td>42.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.10 (n/a)</td><td>189.08 (n/a)</td><td>181.80 (n/a)</td><td>132.90 (n/a)</td><td>51.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.00 (n/a)</td><td>184.44 (n/a)</td><td>192.10 (n/a)</td><td>149.10 (n/a)</td><td>27.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>341.60 (n/a)</td><td>219.48 (n/a)</td><td>184.10 (n/a)</td><td>174.80 (n/a)</td><td>70.29 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>178.92 (n/a)</td><td>174.40 (n/a)</td><td>146.30 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.10 (n/a)</td><td>174.20 (n/a)</td><td>167.60 (n/a)</td><td>162.60 (n/a)</td><td>13.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>306.30 (n/a)</td><td>189.24 (n/a)</td><td>182.30 (n/a)</td><td>100.90 (n/a)</td><td>76.21 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>184.56 (n/a)</td><td>202.70 (n/a)</td><td>124.30 (n/a)</td><td>42.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>180.52 (n/a)</td><td>183.00 (n/a)</td><td>154.30 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.10 (n/a)</td><td>188.52 (n/a)</td><td>185.70 (n/a)</td><td>164.90 (n/a)</td><td>17.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>198.44 (n/a)</td><td>208.00 (n/a)</td><td>171.60 (n/a)</td><td>17.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>203.08 (n/a)</td><td>206.60 (n/a)</td><td>159.00 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>179.16 (n/a)</td><td>172.10 (n/a)</td><td>161.20 (n/a)</td><td>18.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.60 (n/a)</td><td>190.76 (n/a)</td><td>190.50 (n/a)</td><td>135.70 (n/a)</td><td>37.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>240.10 (n/a)</td><td>174.14 (n/a)</td><td>181.90 (n/a)</td><td>119.60 (n/a)</td><td>45.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>173.70 (n/a)</td><td>169.20 (n/a)</td><td>147.60 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.00 (n/a)</td><td>184.60 (n/a)</td><td>201.50 (n/a)</td><td>129.30 (n/a)</td><td>33.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>184.66 (n/a)</td><td>185.30 (n/a)</td><td>159.40 (n/a)</td><td>24.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.00 (n/a)</td><td>182.36 (n/a)</td><td>189.30 (n/a)</td><td>135.80 (n/a)</td><td>33.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>316.50 (n/a)</td><td>269.82 (n/a)</td><td>268.20 (n/a)</td><td>230.70 (n/a)</td><td>33.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>237.30 (n/a)</td><td>198.58 (n/a)</td><td>187.90 (n/a)</td><td>171.10 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>264.70 (n/a)</td><td>209.70 (n/a)</td><td>195.50 (n/a)</td><td>184.20 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>189.30 (n/a)</td><td>151.72 (n/a)</td><td>137.90 (n/a)</td><td>123.10 (n/a)</td><td>30.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>214.60 (n/a)</td><td>177.20 (n/a)</td><td>190.70 (n/a)</td><td>109.60 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.40 (n/a)</td><td>172.88 (n/a)</td><td>180.00 (n/a)</td><td>130.60 (n/a)</td><td>24.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>207.10 (n/a)</td><td>183.00 (n/a)</td><td>177.50 (n/a)</td><td>150.50 (n/a)</td><td>23.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>371.80 (n/a)</td><td>241.44 (n/a)</td><td>217.40 (n/a)</td><td>152.20 (n/a)</td><td>84.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>203.70 (n/a)</td><td>203.10 (n/a)</td><td>189.50 (n/a)</td><td>12.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+0.18%)</td><td>0.02 (-5.77%)</td><td>0.03 (-1.84%)</td><td>0.02 (-12.61%)</td><td>0.01 <b>(+21.69%)</b></td><td>234.70 (+14.43%)</td><td>171.62 (+7.92%)</td><td>158.60 (+1.86%)</td><td>124.80 (-0.16%)</td><td>40.64 <b>(+38.90%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.10 (n/a)</td><td>159.02 (n/a)</td><td>155.70 (n/a)</td><td>125.00 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 <b>(+23.56%)</b></td><td>0.03 (+10.85%)</td><td>0.03 <b>(+23.44%)</b></td><td>0.02 <b>(-28.41%)</b></td><td>0.01 <b>(+187.07%)</b></td><td>258.20 <b>(+39.64%)</b></td><td>160.28 (-2.75%)</td><td>139.80 (-19.00%)</td><td>115.70 (-19.09%)</td><td>58.40 <b>(+230.26%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.90 (n/a)</td><td>164.82 (n/a)</td><td>172.60 (n/a)</td><td>143.00 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+4.85%)</td><td>0.03 (+8.99%)</td><td>0.02 (+0.66%)</td><td>0.02 <b>(+22.82%)</b></td><td>0.00 (-9.64%)</td><td>203.80 (-18.58%)</td><td>163.78 (-9.61%)</td><td>168.70 (-0.71%)</td><td>129.60 (-4.57%)</td><td>28.84 <b>(-32.42%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>250.30 (n/a)</td><td>181.20 (n/a)</td><td>169.90 (n/a)</td><td>135.80 (n/a)</td><td>42.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 <b>(+41.01%)</b></td><td>0.03 <b>(+21.14%)</b></td><td>0.03 <b>(+21.29%)</b></td><td>0.02 (-2.28%)</td><td>0.01 <b>(+141.44%)</b></td><td>222.10 (+2.35%)</td><td>151.90 (-14.21%)</td><td>139.90 (-17.51%)</td><td>111.80 <b>(-29.06%)</b></td><td>41.61 <b>(+79.18%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.00 (n/a)</td><td>177.06 (n/a)</td><td>169.60 (n/a)</td><td>157.60 (n/a)</td><td>23.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-11.50%)</td><td>0.02 (-7.50%)</td><td>0.02 (-5.30%)</td><td>0.01 <b>(-35.53%)</b></td><td>0.01 <b>(+24.66%)</b></td><td>371.90 <b>(+55.09%)</b></td><td>199.42 (+17.11%)</td><td>168.30 (+5.58%)</td><td>140.50 (+13.03%)</td><td>97.27 <b>(+124.92%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.80 (n/a)</td><td>170.28 (n/a)</td><td>159.40 (n/a)</td><td>124.30 (n/a)</td><td>43.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-16.22%)</td><td>0.02 (-14.03%)</td><td>0.02 (-12.14%)</td><td>0.01 <b>(-27.56%)</b></td><td>0.00 (+4.17%)</td><td>284.50 <b>(+38.04%)</b></td><td>198.92 (+18.57%)</td><td>187.70 (+13.83%)</td><td>155.70 (+19.31%)</td><td>49.98 <b>(+80.76%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.10 (n/a)</td><td>167.76 (n/a)</td><td>164.90 (n/a)</td><td>130.50 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-9.88%)</td><td>0.02 (-5.76%)</td><td>0.02 (+10.71%)</td><td>0.02 (-10.27%)</td><td>0.00 (-19.92%)</td><td>232.80 (+11.44%)</td><td>180.90 (+5.47%)</td><td>166.60 (-9.70%)</td><td>146.00 (+10.94%)</td><td>34.36 (+2.16%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>171.52 (n/a)</td><td>184.50 (n/a)</td><td>131.60 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 <b>(+20.58%)</b></td><td>0.02 (+1.29%)</td><td>0.02 (+2.38%)</td><td>0.01 (-15.08%)</td><td>0.01 <b>(+54.73%)</b></td><td>301.20 (+17.75%)</td><td>211.24 (+2.15%)</td><td>208.40 (-2.34%)</td><td>140.40 (-17.07%)</td><td>58.43 <b>(+57.26%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>255.80 (n/a)</td><td>206.80 (n/a)</td><td>213.40 (n/a)</td><td>169.30 (n/a)</td><td>37.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (-19.86%)</td><td>0.05 (-10.15%)</td><td>0.05 <b>(-20.10%)</b></td><td>0.04 <b>(+69.22%)</b></td><td>0.01 <b>(-63.86%)</b></td><td>206.60 <b>(-40.90%)</b></td><td>175.16 (-4.11%)</td><td>164.40 <b>(+25.11%)</b></td><td>146.80 <b>(+24.72%)</b></td><td>26.91 <b>(-72.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>349.60 (n/a)</td><td>182.66 (n/a)</td><td>131.40 (n/a)</td><td>117.70 (n/a)</td><td>98.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (+16.64%)</td><td>0.06 (+8.88%)</td><td>0.05 (-7.94%)</td><td>0.05 (+19.77%)</td><td>0.01 (+1.63%)</td><td>178.70 (-16.50%)</td><td>145.94 (-8.96%)</td><td>149.90 (+8.62%)</td><td>115.00 (-14.31%)</td><td>25.61 <b>(-26.61%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>160.30 (n/a)</td><td>138.00 (n/a)</td><td>134.20 (n/a)</td><td>34.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (-8.91%)</td><td>0.05 (-5.39%)</td><td>0.05 (-1.42%)</td><td>0.04 (-1.70%)</td><td>0.01 <b>(-33.38%)</b></td><td>207.90 (+1.71%)</td><td>175.32 (+4.23%)</td><td>180.10 (+1.41%)</td><td>147.40 (+9.75%)</td><td>23.51 <b>(-23.84%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>168.20 (n/a)</td><td>177.60 (n/a)</td><td>134.30 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+4.02%)</td><td>0.05 (+11.02%)</td><td>0.05 (+11.06%)</td><td>0.05 <b>(+25.08%)</b></td><td>0.00 <b>(-34.25%)</b></td><td>169.10 <b>(-20.05%)</b></td><td>154.86 (-11.07%)</td><td>158.90 (-9.97%)</td><td>138.00 (-3.83%)</td><td>13.93 <b>(-49.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>174.14 (n/a)</td><td>176.50 (n/a)</td><td>143.50 (n/a)</td><td>27.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (-13.60%)</td><td>0.05 (-7.63%)</td><td>0.05 (-19.12%)</td><td>0.04 (+9.04%)</td><td>0.00 <b>(-61.11%)</b></td><td>183.90 (-8.33%)</td><td>166.84 (+5.39%)</td><td>171.20 <b>(+23.70%)</b></td><td>150.90 (+15.72%)</td><td>13.36 <b>(-59.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>158.30 (n/a)</td><td>138.40 (n/a)</td><td>130.40 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+11.36%)</td><td>0.05 (-2.90%)</td><td>0.05 (+6.94%)</td><td>0.03 <b>(-37.68%)</b></td><td>0.01 <b>(+237.02%)</b></td><td>286.80 <b>(+60.49%)</b></td><td>184.14 (+10.62%)</td><td>162.40 (-6.51%)</td><td>133.90 (-10.19%)</td><td>62.51 <b>(+387.68%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.70 (n/a)</td><td>166.46 (n/a)</td><td>173.70 (n/a)</td><td>149.10 (n/a)</td><td>12.82 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (-6.62%)</td><td>0.05 (+2.14%)</td><td>0.05 (-1.58%)</td><td>0.04 (+19.64%)</td><td>0.00 <b>(-62.93%)</b></td><td>194.30 (-16.43%)</td><td>178.78 (-4.80%)</td><td>177.10 (+1.61%)</td><td>162.70 (+7.11%)</td><td>12.58 <b>(-67.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.50 (n/a)</td><td>187.80 (n/a)</td><td>174.30 (n/a)</td><td>151.90 (n/a)</td><td>38.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (-17.92%)</td><td>0.04 (-7.60%)</td><td>0.04 (-2.04%)</td><td>0.03 (-8.39%)</td><td>0.01 <b>(-23.29%)</b></td><td>259.90 (+9.16%)</td><td>198.52 (+7.68%)</td><td>182.90 (+2.06%)</td><td>175.00 <b>(+21.87%)</b></td><td>34.96 (+2.96%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.10 (n/a)</td><td>184.36 (n/a)</td><td>179.20 (n/a)</td><td>143.60 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 <b>(-36.19%)</b></td><td>0.05 (-12.49%)</td><td>0.05 (-6.02%)</td><td>0.04 (+1.17%)</td><td>0.01 <b>(-69.03%)</b></td><td>220.40 (-1.17%)</td><td>182.66 (+7.92%)</td><td>180.30 (+6.37%)</td><td>158.50 <b>(+56.78%)</b></td><td>22.96 <b>(-48.02%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>223.00 (n/a)</td><td>169.26 (n/a)</td><td>169.50 (n/a)</td><td>101.10 (n/a)</td><td>44.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (+10.44%)</td><td>0.04 (+3.52%)</td><td>0.04 (+8.66%)</td><td>0.03 (-9.71%)</td><td>0.01 <b>(+81.41%)</b></td><td>251.30 (+10.75%)</td><td>204.32 (-1.89%)</td><td>198.80 (-7.96%)</td><td>169.90 (-9.43%)</td><td>34.60 <b>(+82.22%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>226.90 (n/a)</td><td>208.26 (n/a)</td><td>216.00 (n/a)</td><td>187.60 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (+0.06%)</td><td>0.11 (-4.53%)</td><td>0.11 (-7.95%)</td><td>0.07 (-19.38%)</td><td>0.02 <b>(+44.45%)</b></td><td>226.10 <b>(+24.03%)</b></td><td>160.40 (+7.49%)</td><td>149.00 (+8.60%)</td><td>127.50 (-0.08%)</td><td>40.09 <b>(+78.43%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>182.30 (n/a)</td><td>149.22 (n/a)</td><td>137.20 (n/a)</td><td>127.60 (n/a)</td><td>22.47 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 <b>(-21.18%)</b></td><td>0.09 (-8.35%)</td><td>0.09 (-7.51%)</td><td>0.09 (-1.38%)</td><td>0.00 <b>(-71.85%)</b></td><td>181.70 (+1.40%)</td><td>175.16 (+7.80%)</td><td>176.80 (+8.07%)</td><td>164.90 <b>(+26.94%)</b></td><td>7.23 <b>(-63.34%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.20 (n/a)</td><td>162.48 (n/a)</td><td>163.60 (n/a)</td><td>129.90 (n/a)</td><td>19.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (+8.75%)</td><td>0.10 (+5.10%)</td><td>0.10 (+7.34%)</td><td>0.09 (+0.34%)</td><td>0.02 <b>(+30.02%)</b></td><td>185.00 (-0.32%)</td><td>161.38 (-4.15%)</td><td>159.90 (-6.82%)</td><td>123.30 (-8.05%)</td><td>24.49 <b>(+20.95%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.60 (n/a)</td><td>168.36 (n/a)</td><td>171.60 (n/a)</td><td>134.10 (n/a)</td><td>20.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (+3.51%)</td><td>0.10 (+1.50%)</td><td>0.09 (+0.69%)</td><td>0.08 (+3.47%)</td><td>0.03 (+10.30%)</td><td>210.20 (-3.31%)</td><td>171.56 (-0.72%)</td><td>179.90 (-0.72%)</td><td>111.50 (-3.38%)</td><td>39.53 (+6.61%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>217.40 (n/a)</td><td>172.80 (n/a)</td><td>181.20 (n/a)</td><td>115.40 (n/a)</td><td>37.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 <b>(-28.23%)</b></td><td>0.09 <b>(-25.83%)</b></td><td>0.09 <b>(-22.35%)</b></td><td>0.08 <b>(-28.17%)</b></td><td>0.02 (-14.59%)</td><td>216.70 <b>(+39.18%)</b></td><td>183.10 <b>(+35.79%)</b></td><td>174.80 <b>(+28.81%)</b></td><td>150.60 <b>(+39.32%)</b></td><td>31.33 <b>(+70.82%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>155.70 (n/a)</td><td>134.84 (n/a)</td><td>135.70 (n/a)</td><td>108.10 (n/a)</td><td>18.34 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 <b>(+37.25%)</b></td><td>0.10 <b>(+21.89%)</b></td><td>0.10 <b>(+23.05%)</b></td><td>0.07 <b>(+54.02%)</b></td><td>0.03 (+17.01%)</td><td>244.80 <b>(-35.07%)</b></td><td>174.78 <b>(-20.78%)</b></td><td>158.40 (-18.73%)</td><td>116.10 <b>(-27.12%)</b></td><td>48.51 <b>(-46.00%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>377.00 (n/a)</td><td>220.64 (n/a)</td><td>194.90 (n/a)</td><td>159.30 (n/a)</td><td>89.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 <b>(+24.20%)</b></td><td>0.10 (+13.51%)</td><td>0.09 (+2.05%)</td><td>0.08 (+2.30%)</td><td>0.03 <b>(+87.29%)</b></td><td>216.90 (-2.25%)</td><td>168.28 (-9.28%)</td><td>176.20 (-2.00%)</td><td>124.00 (-19.53%)</td><td>40.09 <b>(+42.54%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>185.50 (n/a)</td><td>179.80 (n/a)</td><td>154.10 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (-3.81%)</td><td>0.08 (+1.83%)</td><td>0.07 (-1.24%)</td><td>0.07 (+12.39%)</td><td>0.01 <b>(-27.94%)</b></td><td>234.40 (-11.04%)</td><td>219.32 (-2.67%)</td><td>230.50 (+1.23%)</td><td>183.20 (+3.91%)</td><td>21.62 <b>(-31.60%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>263.50 (n/a)</td><td>225.34 (n/a)</td><td>227.70 (n/a)</td><td>176.30 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (-7.53%)</td><td>0.19 (-12.51%)</td><td>0.18 <b>(-22.36%)</b></td><td>0.16 (+4.47%)</td><td>0.04 <b>(-20.42%)</b></td><td>202.90 (-4.25%)</td><td>174.48 (+12.86%)</td><td>178.70 <b>(+28.84%)</b></td><td>133.40 (+8.10%)</td><td>29.58 (-17.32%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>211.90 (n/a)</td><td>154.60 (n/a)</td><td>138.70 (n/a)</td><td>123.40 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (-3.73%)</td><td>0.17 (-16.71%)</td><td>0.15 <b>(-28.20%)</b></td><td>0.11 <b>(-27.80%)</b></td><td>0.05 <b>(+26.52%)</b></td><td>290.00 <b>(+38.49%)</b></td><td>205.46 <b>(+24.37%)</b></td><td>212.20 <b>(+39.24%)</b></td><td>131.70 (+3.86%)</td><td>57.82 <b>(+77.07%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>209.40 (n/a)</td><td>165.20 (n/a)</td><td>152.40 (n/a)</td><td>126.80 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (-16.99%)</td><td>0.18 (-8.84%)</td><td>0.18 (-8.32%)</td><td>0.14 (+4.75%)</td><td>0.03 <b>(-34.88%)</b></td><td>231.80 (-4.53%)</td><td>189.48 (+7.35%)</td><td>186.60 (+9.06%)</td><td>155.60 <b>(+20.43%)</b></td><td>30.87 <b>(-26.59%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>242.80 (n/a)</td><td>176.50 (n/a)</td><td>171.10 (n/a)</td><td>129.20 (n/a)</td><td>42.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (-3.36%)</td><td>0.19 (-1.06%)</td><td>0.19 (-3.37%)</td><td>0.16 (+0.27%)</td><td>0.02 <b>(-25.39%)</b></td><td>198.90 (-0.25%)</td><td>172.30 (+0.63%)</td><td>169.20 (+3.49%)</td><td>156.20 (+3.44%)</td><td>15.89 <b>(-21.60%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>199.40 (n/a)</td><td>171.22 (n/a)</td><td>163.50 (n/a)</td><td>151.00 (n/a)</td><td>20.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (+5.37%)</td><td>0.18 (+6.01%)</td><td>0.21 <b>(+32.95%)</b></td><td>0.12 <b>(-21.71%)</b></td><td>0.05 <b>(+83.96%)</b></td><td>284.80 <b>(+27.71%)</b></td><td>197.02 (-0.70%)</td><td>158.30 <b>(-24.80%)</b></td><td>146.90 (-5.10%)</td><td>60.89 <b>(+123.94%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>223.00 (n/a)</td><td>198.40 (n/a)</td><td>210.50 (n/a)</td><td>154.80 (n/a)</td><td>27.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (-14.91%)</td><td>0.19 (+2.30%)</td><td>0.21 <b>(+40.91%)</b></td><td>0.12 (+6.35%)</td><td>0.05 <b>(-36.59%)</b></td><td>265.90 (-5.98%)</td><td>184.82 (-9.45%)</td><td>157.50 <b>(-29.05%)</b></td><td>130.10 (+17.52%)</td><td>55.25 <b>(-29.78%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>282.80 (n/a)</td><td>204.10 (n/a)</td><td>222.00 (n/a)</td><td>110.70 (n/a)</td><td>78.68 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 <b>(+24.76%)</b></td><td>0.15 (+5.06%)</td><td>0.16 (+17.39%)</td><td>0.10 <b>(-21.89%)</b></td><td>0.04 <b>(+231.47%)</b></td><td>335.70 <b>(+28.03%)</b></td><td>242.30 (+2.18%)</td><td>200.40 (-14.80%)</td><td>168.70 (-19.82%)</td><td>77.44 <b>(+251.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>262.20 (n/a)</td><td>237.12 (n/a)</td><td>235.20 (n/a)</td><td>210.40 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-14.30%)</td><td>0.03 (-5.80%)</td><td>0.02 (-5.53%)</td><td>0.02 (-12.34%)</td><td>0.01 (-5.90%)</td><td>197.50 (+14.10%)</td><td>161.74 (+6.80%)</td><td>172.30 (+5.84%)</td><td>123.10 (+16.68%)</td><td>34.15 <b>(+26.60%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>173.10 (n/a)</td><td>151.44 (n/a)</td><td>162.80 (n/a)</td><td>105.50 (n/a)</td><td>26.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+5.83%)</td><td>0.02 (-3.47%)</td><td>0.02 (-8.86%)</td><td>0.02 (-12.11%)</td><td>0.00 <b>(+46.97%)</b></td><td>211.20 (+13.79%)</td><td>175.02 (+4.39%)</td><td>173.00 (+9.70%)</td><td>148.20 (-5.48%)</td><td>23.05 <b>(+61.30%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.60 (n/a)</td><td>167.66 (n/a)</td><td>157.70 (n/a)</td><td>156.80 (n/a)</td><td>14.29 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (+7.33%)</td><td>0.02 <b>(+23.68%)</b></td><td>0.02 (+19.12%)</td><td>0.02 <b>(+44.02%)</b></td><td>0.00 <b>(-28.25%)</b></td><td>225.30 <b>(-30.55%)</b></td><td>189.90 <b>(-21.24%)</b></td><td>193.10 (-16.04%)</td><td>165.70 (-6.86%)</td><td>24.60 <b>(-54.94%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>324.40 (n/a)</td><td>241.10 (n/a)</td><td>230.00 (n/a)</td><td>177.90 (n/a)</td><td>54.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (-11.63%)</td><td>0.02 (-7.94%)</td><td>0.02 (-7.23%)</td><td>0.02 (-4.82%)</td><td>0.00 <b>(-31.62%)</b></td><td>234.50 (+5.06%)</td><td>208.82 (+7.81%)</td><td>210.90 (+7.82%)</td><td>175.10 (+13.19%)</td><td>21.66 <b>(-20.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.20 (n/a)</td><td>193.70 (n/a)</td><td>195.60 (n/a)</td><td>154.70 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-13.88%)</td><td>0.03 (-9.04%)</td><td>0.02 (+6.19%)</td><td>0.02 (+1.96%)</td><td>0.01 <b>(-36.20%)</b></td><td>200.60 (-1.96%)</td><td>169.76 (+5.35%)</td><td>170.50 (-5.80%)</td><td>118.20 (+16.11%)</td><td>33.67 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>161.14 (n/a)</td><td>181.00 (n/a)</td><td>101.80 (n/a)</td><td>46.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+1.38%)</td><td>0.03 (+13.73%)</td><td>0.03 (+17.36%)</td><td>0.02 <b>(+28.99%)</b></td><td>0.00 <b>(-35.00%)</b></td><td>164.60 <b>(-22.47%)</b></td><td>149.50 (-13.73%)</td><td>149.50 (-14.77%)</td><td>124.40 (-1.35%)</td><td>15.90 <b>(-48.94%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.30 (n/a)</td><td>173.30 (n/a)</td><td>175.40 (n/a)</td><td>126.10 (n/a)</td><td>31.14 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+0.97%)</td><td>0.03 (+16.18%)</td><td>0.03 (+19.85%)</td><td>0.02 (+19.00%)</td><td>0.01 (-8.62%)</td><td>186.60 (-15.98%)</td><td>144.78 (-14.94%)</td><td>138.70 (-16.60%)</td><td>119.40 (-1.00%)</td><td>28.08 <b>(-24.37%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.10 (n/a)</td><td>170.20 (n/a)</td><td>166.30 (n/a)</td><td>120.60 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+10.38%)</td><td>0.02 (+6.12%)</td><td>0.02 (+1.10%)</td><td>0.02 (-1.61%)</td><td>0.00 <b>(+44.14%)</b></td><td>231.10 (+1.63%)</td><td>174.22 (-4.39%)</td><td>176.90 (-1.12%)</td><td>141.40 (-9.42%)</td><td>36.26 <b>(+29.43%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.40 (n/a)</td><td>182.22 (n/a)</td><td>178.90 (n/a)</td><td>156.10 (n/a)</td><td>28.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+4.75%)</td><td>0.02 (+16.70%)</td><td>0.02 (+15.85%)</td><td>0.02 (+19.15%)</td><td>0.01 (-2.49%)</td><td>239.50 (-16.05%)</td><td>178.48 (-15.68%)</td><td>167.80 (-13.64%)</td><td>122.40 (-4.52%)</td><td>49.24 <b>(-20.85%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>285.30 (n/a)</td><td>211.68 (n/a)</td><td>194.30 (n/a)</td><td>128.20 (n/a)</td><td>62.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-12.70%)</td><td>0.02 (-3.43%)</td><td>0.02 (+5.35%)</td><td>0.02 (-4.34%)</td><td>0.00 <b>(-32.12%)</b></td><td>193.90 (+4.53%)</td><td>168.24 (+2.20%)</td><td>168.10 (-5.08%)</td><td>133.50 (+14.59%)</td><td>23.17 (-18.13%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>164.62 (n/a)</td><td>177.10 (n/a)</td><td>116.50 (n/a)</td><td>28.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+6.67%)</td><td>0.02 (-17.60%)</td><td>0.02 <b>(-21.21%)</b></td><td>0.02 <b>(-27.81%)</b></td><td>0.01 <b>(+154.97%)</b></td><td>232.40 <b>(+38.50%)</b></td><td>198.46 <b>(+25.50%)</b></td><td>209.80 <b>(+26.92%)</b></td><td>133.20 (-6.26%)</td><td>38.20 <b>(+213.89%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>167.80 (n/a)</td><td>158.14 (n/a)</td><td>165.30 (n/a)</td><td>142.10 (n/a)</td><td>12.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-14.64%)</td><td>0.02 (-3.87%)</td><td>0.02 (-4.79%)</td><td>0.02 <b>(+50.61%)</b></td><td>0.00 <b>(-64.09%)</b></td><td>201.90 <b>(-33.59%)</b></td><td>182.76 (-4.27%)</td><td>184.00 (+5.02%)</td><td>153.50 (+17.18%)</td><td>20.21 <b>(-71.31%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>304.00 (n/a)</td><td>190.92 (n/a)</td><td>175.20 (n/a)</td><td>131.00 (n/a)</td><td>70.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (+1.29%)</td><td>0.02 (-9.80%)</td><td>0.02 (-3.12%)</td><td>0.01 <b>(-30.92%)</b></td><td>0.00 <b>(+116.20%)</b></td><td>308.70 <b>(+44.73%)</b></td><td>222.46 (+14.84%)</td><td>199.40 (+3.21%)</td><td>169.00 (-1.29%)</td><td>53.84 <b>(+215.69%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.30 (n/a)</td><td>193.72 (n/a)</td><td>193.20 (n/a)</td><td>171.20 (n/a)</td><td>17.06 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (+1.71%)</td><td>0.02 (+1.98%)</td><td>0.02 (+9.75%)</td><td>0.02 (-10.00%)</td><td>0.00 <b>(+32.47%)</b></td><td>237.10 (+11.11%)</td><td>199.88 (-1.12%)</td><td>194.20 (-8.87%)</td><td>164.20 (-1.68%)</td><td>29.33 <b>(+46.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.40 (n/a)</td><td>202.14 (n/a)</td><td>213.10 (n/a)</td><td>167.00 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 <b>(+30.96%)</b></td><td>0.02 (+13.84%)</td><td>0.02 (+8.15%)</td><td>0.02 (+2.56%)</td><td>0.00 <b>(+106.48%)</b></td><td>218.90 (-2.49%)</td><td>176.82 (-10.27%)</td><td>187.30 (-7.55%)</td><td>129.50 <b>(-23.64%)</b></td><td>33.64 <b>(+52.10%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.50 (n/a)</td><td>197.06 (n/a)</td><td>202.60 (n/a)</td><td>169.60 (n/a)</td><td>22.11 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 <b>(+33.48%)</b></td><td>0.02 <b>(+23.23%)</b></td><td>0.02 (+14.96%)</td><td>0.02 <b>(+27.62%)</b></td><td>0.00 <b>(+73.25%)</b></td><td>194.60 <b>(-21.63%)</b></td><td>173.76 (-18.30%)</td><td>183.00 (-13.02%)</td><td>138.60 <b>(-25.12%)</b></td><td>23.33 (+1.10%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.30 (n/a)</td><td>212.68 (n/a)</td><td>210.40 (n/a)</td><td>185.10 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 <b>(+37.65%)</b></td><td>0.05 (+12.42%)</td><td>0.05 (+0.08%)</td><td>0.04 (+4.90%)</td><td>0.01 <b>(+123.52%)</b></td><td>200.20 (-4.67%)</td><td>161.54 (-8.53%)</td><td>166.60 (-0.06%)</td><td>112.90 <b>(-27.35%)</b></td><td>33.85 <b>(+51.92%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>176.60 (n/a)</td><td>166.70 (n/a)</td><td>155.40 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (-4.88%)</td><td>0.05 (-3.05%)</td><td>0.06 (+0.17%)</td><td>0.04 (+1.14%)</td><td>0.01 <b>(-23.02%)</b></td><td>206.30 (-1.10%)</td><td>160.56 (+1.04%)</td><td>144.00 (-0.14%)</td><td>125.60 (+5.10%)</td><td>34.30 (-19.23%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>158.90 (n/a)</td><td>144.20 (n/a)</td><td>119.50 (n/a)</td><td>42.46 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 <b>(-37.66%)</b></td><td>0.04 <b>(-26.62%)</b></td><td>0.04 <b>(-22.61%)</b></td><td>0.02 <b>(-34.02%)</b></td><td>0.01 <b>(-38.57%)</b></td><td>340.40 <b>(+51.56%)</b></td><td>234.12 <b>(+36.13%)</b></td><td>212.20 <b>(+29.23%)</b></td><td>190.90 <b>(+60.42%)</b></td><td>61.05 <b>(+56.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.60 (n/a)</td><td>171.98 (n/a)</td><td>164.20 (n/a)</td><td>119.00 (n/a)</td><td>39.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 <b>(-29.20%)</b></td><td>0.04 <b>(-20.49%)</b></td><td>0.04 (-19.69%)</td><td>0.04 (-8.48%)</td><td>0.00 <b>(-62.67%)</b></td><td>231.10 (+9.27%)</td><td>217.48 <b>(+23.46%)</b></td><td>227.70 <b>(+24.56%)</b></td><td>190.30 <b>(+41.28%)</b></td><td>17.23 <b>(-41.54%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>176.16 (n/a)</td><td>182.80 (n/a)</td><td>134.70 (n/a)</td><td>29.47 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (-4.07%)</td><td>0.05 (-2.22%)</td><td>0.05 (-3.79%)</td><td>0.04 (-5.12%)</td><td>0.01 (+0.47%)</td><td>213.50 (+5.38%)</td><td>162.20 (+2.61%)</td><td>171.00 (+3.95%)</td><td>121.70 (+4.20%)</td><td>38.49 (+8.00%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>158.08 (n/a)</td><td>164.50 (n/a)</td><td>116.80 (n/a)</td><td>35.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (+8.08%)</td><td>0.06 (+9.93%)</td><td>0.06 <b>(+23.54%)</b></td><td>0.04 (+12.13%)</td><td>0.01 (-1.79%)</td><td>183.40 (-10.84%)</td><td>151.52 (-9.50%)</td><td>137.60 (-19.06%)</td><td>121.90 (-7.44%)</td><td>29.29 (-14.13%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>167.42 (n/a)</td><td>170.00 (n/a)</td><td>131.70 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+11.28%)</td><td>0.05 (+7.28%)</td><td>0.05 (-0.69%)</td><td>0.04 (+13.78%)</td><td>0.01 (+1.98%)</td><td>197.90 (-12.12%)</td><td>175.18 (-7.08%)</td><td>180.30 (+0.73%)</td><td>143.20 (-10.16%)</td><td>22.06 <b>(-20.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>188.52 (n/a)</td><td>179.00 (n/a)</td><td>159.40 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (-13.60%)</td><td>0.05 (-6.26%)</td><td>0.05 (-1.46%)</td><td>0.04 (-14.88%)</td><td>0.01 (-12.81%)</td><td>209.00 (+17.48%)</td><td>170.28 (+6.92%)</td><td>169.40 (+1.44%)</td><td>125.00 (+15.74%)</td><td>35.99 <b>(+23.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.90 (n/a)</td><td>159.26 (n/a)</td><td>167.00 (n/a)</td><td>108.00 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 <b>(-30.58%)</b></td><td>0.04 (-9.70%)</td><td>0.04 (+8.28%)</td><td>0.04 (+3.81%)</td><td>0.01 <b>(-62.53%)</b></td><td>231.10 (-3.67%)</td><td>195.62 (+3.83%)</td><td>195.90 (-7.68%)</td><td>167.10 <b>(+44.05%)</b></td><td>27.53 <b>(-49.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>239.90 (n/a)</td><td>188.40 (n/a)</td><td>212.20 (n/a)</td><td>116.00 (n/a)</td><td>54.58 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (-7.66%)</td><td>0.05 (-0.67%)</td><td>0.05 (-5.44%)</td><td>0.04 (+2.71%)</td><td>0.01 (-11.56%)</td><td>190.30 (-2.61%)</td><td>171.66 (+0.44%)</td><td>181.10 (+5.72%)</td><td>147.20 (+8.31%)</td><td>21.20 (-5.18%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>170.90 (n/a)</td><td>171.30 (n/a)</td><td>135.90 (n/a)</td><td>22.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+4.61%)</td><td>0.05 (+3.52%)</td><td>0.05 (-1.21%)</td><td>0.04 (+4.90%)</td><td>0.01 (-5.19%)</td><td>210.60 (-4.71%)</td><td>179.22 (-3.86%)</td><td>175.80 (+1.27%)</td><td>142.40 (-4.43%)</td><td>25.94 (-16.73%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>186.42 (n/a)</td><td>173.60 (n/a)</td><td>149.00 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+9.05%)</td><td>0.05 (-2.33%)</td><td>0.04 (-7.94%)</td><td>0.04 (-0.80%)</td><td>0.01 <b>(+45.25%)</b></td><td>211.60 (+0.81%)</td><td>182.94 (+3.19%)</td><td>184.90 (+8.64%)</td><td>146.00 (-8.29%)</td><td>25.42 <b>(+30.75%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.90 (n/a)</td><td>177.28 (n/a)</td><td>170.20 (n/a)</td><td>159.20 (n/a)</td><td>19.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+9.70%)</td><td>0.05 (+1.17%)</td><td>0.04 (-2.18%)</td><td>0.04 (-7.79%)</td><td>0.01 <b>(+69.52%)</b></td><td>211.20 (+8.42%)</td><td>177.60 (-0.11%)</td><td>182.20 (+2.24%)</td><td>145.80 (-8.87%)</td><td>25.37 <b>(+66.02%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>194.80 (n/a)</td><td>177.80 (n/a)</td><td>178.20 (n/a)</td><td>160.00 (n/a)</td><td>15.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+7.65%)</td><td>0.05 (+3.24%)</td><td>0.05 (-1.50%)</td><td>0.04 (+1.11%)</td><td>0.01 (+15.67%)</td><td>220.80 (-1.08%)</td><td>172.28 (-2.59%)</td><td>173.20 (+1.52%)</td><td>129.50 (-7.10%)</td><td>34.78 (+5.36%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.20 (n/a)</td><td>176.86 (n/a)</td><td>170.60 (n/a)</td><td>139.40 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (-6.62%)</td><td>0.05 (-5.81%)</td><td>0.04 (-11.58%)</td><td>0.04 (-10.99%)</td><td>0.01 (+6.84%)</td><td>207.00 (+12.32%)</td><td>178.38 (+6.71%)</td><td>191.90 (+13.08%)</td><td>142.30 (+7.07%)</td><td>26.91 <b>(+28.19%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.30 (n/a)</td><td>167.16 (n/a)</td><td>169.70 (n/a)</td><td>132.90 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 <b>(-33.27%)</b></td><td>0.04 <b>(-22.42%)</b></td><td>0.04 <b>(-25.50%)</b></td><td>0.04 (+18.54%)</td><td>0.00 <b>(-72.57%)</b></td><td>204.30 (-15.65%)</td><td>186.16 <b>(+21.32%)</b></td><td>182.10 <b>(+34.29%)</b></td><td>169.50 <b>(+49.87%)</b></td><td>16.61 <b>(-67.34%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.20 (n/a)</td><td>153.44 (n/a)</td><td>135.60 (n/a)</td><td>113.10 (n/a)</td><td>50.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (-16.18%)</td><td>0.09 (-18.73%)</td><td>0.09 (-7.53%)</td><td>0.07 <b>(-24.51%)</b></td><td>0.02 <b>(-21.03%)</b></td><td>239.60 <b>(+32.45%)</b></td><td>192.46 <b>(+22.66%)</b></td><td>190.30 (+8.13%)</td><td>138.00 (+19.27%)</td><td>36.52 (+17.64%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.90 (n/a)</td><td>156.90 (n/a)</td><td>176.00 (n/a)</td><td>115.70 (n/a)</td><td>31.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (-5.38%)</td><td>0.09 (-6.48%)</td><td>0.09 (-3.66%)</td><td>0.08 (+0.86%)</td><td>0.01 (-12.19%)</td><td>214.40 (-0.88%)</td><td>189.02 (+6.66%)</td><td>182.70 (+3.81%)</td><td>164.10 (+5.67%)</td><td>22.84 (-6.37%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.30 (n/a)</td><td>177.22 (n/a)</td><td>176.00 (n/a)</td><td>155.30 (n/a)</td><td>24.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 <b>(+21.34%)</b></td><td>0.07 (+7.54%)</td><td>0.07 (-2.77%)</td><td>0.06 (+7.54%)</td><td>0.01 <b>(+37.33%)</b></td><td>281.10 (-6.98%)</td><td>228.32 (-6.41%)</td><td>231.50 (+2.89%)</td><td>177.70 (-17.58%)</td><td>37.10 (+3.81%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>302.20 (n/a)</td><td>243.96 (n/a)</td><td>225.00 (n/a)</td><td>215.60 (n/a)</td><td>35.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (-13.83%)</td><td>0.08 (-11.45%)</td><td>0.08 (-4.93%)</td><td>0.05 <b>(-32.28%)</b></td><td>0.01 <b>(+38.75%)</b></td><td>312.00 <b>(+47.66%)</b></td><td>222.34 (+15.89%)</td><td>204.20 (+5.20%)</td><td>182.50 (+16.09%)</td><td>52.40 <b>(+146.69%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>191.86 (n/a)</td><td>194.10 (n/a)</td><td>157.20 (n/a)</td><td>21.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (-19.93%)</td><td>0.08 <b>(-21.16%)</b></td><td>0.08 <b>(-23.01%)</b></td><td>0.07 <b>(-21.73%)</b></td><td>0.01 (-14.98%)</td><td>233.80 <b>(+27.76%)</b></td><td>198.78 <b>(+27.05%)</b></td><td>202.30 <b>(+29.85%)</b></td><td>170.70 <b>(+24.87%)</b></td><td>26.04 <b>(+35.19%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.00 (n/a)</td><td>156.46 (n/a)</td><td>155.80 (n/a)</td><td>136.70 (n/a)</td><td>19.26 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 <b>(-23.90%)</b></td><td>0.08 (-11.17%)</td><td>0.08 (-1.40%)</td><td>0.06 <b>(-20.60%)</b></td><td>0.01 <b>(-36.01%)</b></td><td>255.70 <b>(+25.96%)</b></td><td>205.10 (+11.93%)</td><td>196.00 (+1.45%)</td><td>182.00 <b>(+31.41%)</b></td><td>29.17 (+10.30%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.00 (n/a)</td><td>183.24 (n/a)</td><td>193.20 (n/a)</td><td>138.50 (n/a)</td><td>26.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (+9.55%)</td><td>0.09 (-14.02%)</td><td>0.08 (-17.97%)</td><td>0.05 <b>(-30.23%)</b></td><td>0.03 <b>(+49.82%)</b></td><td>298.40 <b>(+43.32%)</b></td><td>207.36 <b>(+23.37%)</b></td><td>215.00 <b>(+21.95%)</b></td><td>115.20 (-8.72%)</td><td>65.67 <b>(+88.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.20 (n/a)</td><td>168.08 (n/a)</td><td>176.30 (n/a)</td><td>126.20 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (+10.09%)</td><td>0.10 (+0.73%)</td><td>0.11 (+14.74%)</td><td>0.06 <b>(-25.85%)</b></td><td>0.03 <b>(+54.07%)</b></td><td>258.60 <b>(+34.90%)</b></td><td>169.06 (+3.83%)</td><td>153.00 (-12.82%)</td><td>117.30 (-9.14%)</td><td>53.70 <b>(+99.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>191.70 (n/a)</td><td>162.82 (n/a)</td><td>175.50 (n/a)</td><td>129.10 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (+4.63%)</td><td>0.10 (+3.00%)</td><td>0.09 (-3.00%)</td><td>0.09 (+11.54%)</td><td>0.02 (-12.15%)</td><td>191.60 (-10.34%)</td><td>161.62 (-4.30%)</td><td>174.90 (+3.13%)</td><td>122.30 (-4.38%)</td><td>30.76 <b>(-23.13%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.70 (n/a)</td><td>168.88 (n/a)</td><td>169.60 (n/a)</td><td>127.90 (n/a)</td><td>40.02 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (-15.90%)</td><td>0.09 (-12.56%)</td><td>0.09 <b>(-22.22%)</b></td><td>0.08 (+1.70%)</td><td>0.01 <b>(-51.10%)</b></td><td>215.60 (-1.69%)</td><td>187.04 (+11.17%)</td><td>187.50 <b>(+28.60%)</b></td><td>161.40 (+18.94%)</td><td>22.08 <b>(-42.88%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.30 (n/a)</td><td>168.24 (n/a)</td><td>145.80 (n/a)</td><td>135.70 (n/a)</td><td>38.66 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 <b>(-25.00%)</b></td><td>0.09 (-3.34%)</td><td>0.09 (+0.18%)</td><td>0.08 (+13.39%)</td><td>0.01 <b>(-71.07%)</b></td><td>204.70 (-11.81%)</td><td>182.36 (-0.04%)</td><td>176.00 (-0.17%)</td><td>171.60 <b>(+33.33%)</b></td><td>13.36 <b>(-65.20%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.10 (n/a)</td><td>182.44 (n/a)</td><td>176.30 (n/a)</td><td>128.70 (n/a)</td><td>38.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 <b>(-26.39%)</b></td><td>0.10 (-9.17%)</td><td>0.10 (-7.40%)</td><td>0.09 (+2.54%)</td><td>0.01 <b>(-70.01%)</b></td><td>190.70 (-2.51%)</td><td>171.24 (+6.59%)</td><td>165.30 (+7.97%)</td><td>159.70 <b>(+35.80%)</b></td><td>12.85 <b>(-61.59%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.60 (n/a)</td><td>160.66 (n/a)</td><td>153.10 (n/a)</td><td>117.60 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (+7.86%)</td><td>0.09 (+7.55%)</td><td>0.08 (+1.92%)</td><td>0.07 (-2.32%)</td><td>0.02 <b>(+21.54%)</b></td><td>240.30 (+2.39%)</td><td>188.20 (-6.20%)</td><td>193.70 (-1.87%)</td><td>141.80 (-7.26%)</td><td>37.26 (+14.22%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>200.64 (n/a)</td><td>197.40 (n/a)</td><td>152.90 (n/a)</td><td>32.62 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (-3.96%)</td><td>0.09 (-1.90%)</td><td>0.09 (-5.82%)</td><td>0.07 (-5.17%)</td><td>0.01 (-16.48%)</td><td>234.70 (+5.48%)</td><td>188.82 (+1.53%)</td><td>182.30 (+6.17%)</td><td>164.30 (+4.19%)</td><td>27.02 (-6.78%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>185.98 (n/a)</td><td>171.70 (n/a)</td><td>157.70 (n/a)</td><td>28.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 <b>(+24.30%)</b></td><td>0.09 (-4.68%)</td><td>0.08 (-14.12%)</td><td>0.07 (-14.07%)</td><td>0.03 <b>(+166.95%)</b></td><td>228.40 (+16.35%)</td><td>197.70 (+9.87%)</td><td>211.50 (+16.46%)</td><td>122.20 (-19.50%)</td><td>43.92 <b>(+143.85%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.30 (n/a)</td><td>179.94 (n/a)</td><td>181.60 (n/a)</td><td>151.80 (n/a)</td><td>18.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (-11.98%)</td><td>0.09 (-8.19%)</td><td>0.09 (-10.87%)</td><td>0.08 (-0.33%)</td><td>0.01 <b>(-40.18%)</b></td><td>205.20 (+0.29%)</td><td>176.92 (+6.67%)</td><td>173.70 (+12.21%)</td><td>149.70 (+13.67%)</td><td>23.65 <b>(-32.85%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.60 (n/a)</td><td>165.86 (n/a)</td><td>154.80 (n/a)</td><td>131.70 (n/a)</td><td>35.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (-11.75%)</td><td>0.17 (-19.65%)</td><td>0.18 (-11.11%)</td><td>0.09 <b>(-48.27%)</b></td><td>0.05 <b>(+39.76%)</b></td><td>383.30 <b>(+93.39%)</b></td><td>219.20 <b>(+35.33%)</b></td><td>179.60 (+12.46%)</td><td>146.60 (+13.29%)</td><td>94.63 <b>(+227.54%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>198.20 (n/a)</td><td>161.98 (n/a)</td><td>159.70 (n/a)</td><td>129.40 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.23 (-11.16%)</td><td>0.18 (-16.83%)</td><td>0.18 (-19.75%)</td><td>0.15 (+6.29%)</td><td>0.03 <b>(-33.33%)</b></td><td>215.30 (-5.94%)</td><td>184.46 (+17.30%)</td><td>183.10 <b>(+24.64%)</b></td><td>141.10 (+12.61%)</td><td>29.33 <b>(-30.46%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>228.90 (n/a)</td><td>157.26 (n/a)</td><td>146.90 (n/a)</td><td>125.30 (n/a)</td><td>42.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 <b>(+20.58%)</b></td><td>0.15 (+11.03%)</td><td>0.16 (+16.94%)</td><td>0.10 (-15.31%)</td><td>0.03 <b>(+195.85%)</b></td><td>317.40 (+18.08%)</td><td>223.84 (-6.83%)</td><td>203.20 (-14.51%)</td><td>180.90 (-17.09%)</td><td>54.29 <b>(+198.62%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>268.80 (n/a)</td><td>240.26 (n/a)</td><td>237.70 (n/a)</td><td>218.20 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.23 <b>(+36.63%)</b></td><td>0.18 (+17.38%)</td><td>0.17 (+11.22%)</td><td>0.15 (-0.32%)</td><td>0.04 <b>(+368.73%)</b></td><td>224.40 (+0.31%)</td><td>185.34 (-11.82%)</td><td>190.30 (-10.11%)</td><td>141.20 <b>(-26.80%)</b></td><td>38.75 <b>(+249.36%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>210.18 (n/a)</td><td>211.70 (n/a)</td><td>192.90 (n/a)</td><td>11.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 <b>(-20.87%)</b></td><td>0.18 (-14.29%)</td><td>0.16 (-14.63%)</td><td>0.13 <b>(-27.00%)</b></td><td>0.05 <b>(-21.41%)</b></td><td>259.80 <b>(+37.03%)</b></td><td>190.74 (+17.12%)</td><td>200.80 (+17.15%)</td><td>129.10 <b>(+26.32%)</b></td><td>48.85 <b>(+40.10%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>189.60 (n/a)</td><td>162.86 (n/a)</td><td>171.40 (n/a)</td><td>102.20 (n/a)</td><td>34.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (-15.90%)</td><td>0.18 (-7.57%)</td><td>0.18 (+0.58%)</td><td>0.16 (+2.83%)</td><td>0.02 <b>(-58.20%)</b></td><td>211.30 (-2.76%)</td><td>183.60 (+4.73%)</td><td>179.40 (-0.61%)</td><td>161.00 (+18.91%)</td><td>19.35 <b>(-50.01%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.30 (n/a)</td><td>175.30 (n/a)</td><td>180.50 (n/a)</td><td>135.40 (n/a)</td><td>38.71 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.24 (-5.75%)</td><td>0.19 (-15.94%)</td><td>0.18 <b>(-22.82%)</b></td><td>0.16 (-12.46%)</td><td>0.03 (+18.10%)</td><td>201.30 (+14.25%)</td><td>174.78 (+19.99%)</td><td>185.70 <b>(+29.59%)</b></td><td>137.90 (+6.08%)</td><td>27.23 <b>(+44.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>176.20 (n/a)</td><td>145.66 (n/a)</td><td>143.30 (n/a)</td><td>130.00 (n/a)</td><td>18.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 <b>(+32.02%)</b></td><td>0.19 (+6.62%)</td><td>0.19 (+12.37%)</td><td>0.09 <b>(-42.13%)</b></td><td>0.08 <b>(+299.18%)</b></td><td>353.60 <b>(+72.74%)</b></td><td>203.44 (+8.93%)</td><td>175.40 (-11.01%)</td><td>123.40 <b>(-24.25%)</b></td><td>96.46 <b>(+397.45%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.70 (n/a)</td><td>186.76 (n/a)</td><td>197.10 (n/a)</td><td>162.90 (n/a)</td><td>19.39 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 <b>(+37.53%)</b></td><td>0.20 (+9.93%)</td><td>0.19 (-3.42%)</td><td>0.15 (-1.95%)</td><td>0.06 <b>(+184.72%)</b></td><td>225.50 (+1.99%)</td><td>172.66 (-3.66%)</td><td>175.90 (+3.59%)</td><td>118.90 <b>(-27.28%)</b></td><td>49.31 <b>(+106.86%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.10 (n/a)</td><td>179.22 (n/a)</td><td>169.80 (n/a)</td><td>163.50 (n/a)</td><td>23.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 <b>(+41.30%)</b></td><td>0.21 (+6.71%)</td><td>0.19 (-4.72%)</td><td>0.17 (-4.69%)</td><td>0.05 <b>(+371.15%)</b></td><td>189.70 (+4.92%)</td><td>161.32 (-3.16%)</td><td>173.40 (+4.90%)</td><td>111.90 <b>(-29.22%)</b></td><td>30.52 <b>(+239.38%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>180.80 (n/a)</td><td>166.58 (n/a)</td><td>165.30 (n/a)</td><td>158.10 (n/a)</td><td>8.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.24 <b>(+31.93%)</b></td><td>0.20 <b>(+21.24%)</b></td><td>0.19 (+19.96%)</td><td>0.16 (+9.13%)</td><td>0.04 <b>(+111.72%)</b></td><td>210.40 (-8.36%)</td><td>168.50 (-15.94%)</td><td>171.90 (-16.67%)</td><td>134.00 <b>(-24.17%)</b></td><td>31.49 <b>(+45.95%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>229.60 (n/a)</td><td>200.46 (n/a)</td><td>206.30 (n/a)</td><td>176.70 (n/a)</td><td>21.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (-0.72%)</td><td>0.18 (-0.74%)</td><td>0.18 (+0.40%)</td><td>0.15 (-6.37%)</td><td>0.01 <b>(+43.03%)</b></td><td>215.70 (+6.78%)</td><td>185.78 (+1.07%)</td><td>180.00 (-0.39%)</td><td>174.80 (+0.69%)</td><td>16.97 <b>(+54.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>183.82 (n/a)</td><td>180.70 (n/a)</td><td>173.60 (n/a)</td><td>11.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 <b>(-29.18%)</b></td><td>0.18 (-11.00%)</td><td>0.18 (+1.05%)</td><td>0.14 (-0.99%)</td><td>0.02 <b>(-56.47%)</b></td><td>240.00 (+1.01%)</td><td>190.46 (+7.64%)</td><td>182.70 (-1.03%)</td><td>162.40 <b>(+41.22%)</b></td><td>30.00 <b>(-35.31%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>237.60 (n/a)</td><td>176.94 (n/a)</td><td>184.60 (n/a)</td><td>115.00 (n/a)</td><td>46.38 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (+6.11%)</td><td>0.18 (+4.35%)</td><td>0.17 (-1.32%)</td><td>0.14 (-2.15%)</td><td>0.03 <b>(+39.14%)</b></td><td>226.00 (+2.22%)</td><td>186.44 (-3.13%)</td><td>195.70 (+1.35%)</td><td>148.00 (-5.73%)</td><td>31.08 <b>(+35.30%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.10 (n/a)</td><td>192.46 (n/a)</td><td>193.10 (n/a)</td><td>157.00 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (-5.73%)</td><td>0.19 (+1.79%)</td><td>0.16 (-2.35%)</td><td>0.15 (-1.14%)</td><td>0.05 (-6.67%)</td><td>219.60 (+1.15%)</td><td>183.92 (-1.85%)</td><td>207.30 (+2.42%)</td><td>123.30 (+6.02%)</td><td>43.76 (+5.64%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>217.10 (n/a)</td><td>187.38 (n/a)</td><td>202.40 (n/a)</td><td>116.30 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (-3.70%)</td><td>0.17 (+2.38%)</td><td>0.17 (-6.89%)</td><td>0.16 (+15.05%)</td><td>0.02 <b>(-34.84%)</b></td><td>205.50 (-13.07%)</td><td>190.10 (-3.27%)</td><td>198.10 (+7.43%)</td><td>172.40 (+3.86%)</td><td>16.19 <b>(-42.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>236.40 (n/a)</td><td>196.52 (n/a)</td><td>184.40 (n/a)</td><td>166.00 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (+0.01%)</td><td>0.18 (+0.04%)</td><td>0.18 (-0.05%)</td><td>0.18 (+0.22%)</td><td>0.00 <b>(-33.95%)</b></td><td>47657.80 (-0.22%)</td><td>47518.84 (-0.04%)</td><td>47498.90 (+0.05%)</td><td>47442.40 (-0.01%)</td><td>87.50 <b>(-34.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47761.80 (n/a)</td><td>47536.14 (n/a)</td><td>47475.10 (n/a)</td><td>47446.10 (n/a)</td><td>132.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (+0.72%)</td><td>0.18 (+0.17%)</td><td>0.18 (+0.08%)</td><td>0.18 (+0.01%)</td><td>0.00 <b>(+335.58%)</b></td><td>47543.40 (-0.01%)</td><td>47420.28 (-0.17%)</td><td>47477.10 (-0.08%)</td><td>47106.80 (-0.72%)</td><td>180.34 <b>(+332.14%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47546.90 (n/a)</td><td>47501.00 (n/a)</td><td>47513.20 (n/a)</td><td>47446.90 (n/a)</td><td>41.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (+0.07%)</td><td>0.11 (+0.01%)</td><td>0.11 (+0.02%)</td><td>0.11 (-0.04%)</td><td>0.00 <b>(+159.36%)</b></td><td>375750.70 (+0.04%)</td><td>375436.24 (-0.01%)</td><td>375432.80 (-0.02%)</td><td>375076.90 (-0.07%)</td><td>247.27 <b>(+159.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>375603.20 (n/a)</td><td>375485.50 (n/a)</td><td>375497.30 (n/a)</td><td>375340.30 (n/a)</td><td>95.39 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (-5.98%)</td><td>0.14 (-2.16%)</td><td>0.14 (-0.66%)</td><td>0.11 (-2.15%)</td><td>0.03 (-13.16%)</td><td>228.30 (+2.19%)</td><td>182.60 (+1.65%)</td><td>181.40 (+0.67%)</td><td>136.90 (+6.29%)</td><td>32.96 (-4.15%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>223.40 (n/a)</td><td>179.64 (n/a)</td><td>180.20 (n/a)</td><td>128.80 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.30 (+6.67%)</td><td>0.27 (+2.01%)</td><td>0.26 (-3.59%)</td><td>0.22 (-3.79%)</td><td>0.03 <b>(+55.58%)</b></td><td>221.50 (+3.94%)</td><td>185.12 (-1.31%)</td><td>185.50 (+3.69%)</td><td>164.70 (-6.26%)</td><td>23.21 <b>(+49.67%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>213.10 (n/a)</td><td>187.58 (n/a)</td><td>178.90 (n/a)</td><td>175.70 (n/a)</td><td>15.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.46 (+0.76%)</td><td>12.67 (-0.16%)</td><td>12.51 (-1.18%)</td><td>12.24 (+1.84%)</td><td>0.49 (-3.43%)</td><td>856.40 (-1.80%)</td><td>828.46 (+0.15%)</td><td>838.00 (+1.20%)</td><td>779.00 (-0.75%)</td><td>31.30 (-5.98%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.36 (n/a)</td><td>12.69 (n/a)</td><td>12.66 (n/a)</td><td>12.02 (n/a)</td><td>0.51 (n/a)</td><td>872.10 (n/a)</td><td>827.18 (n/a)</td><td>828.10 (n/a)</td><td>784.90 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (+7.38%)</td><td>0.26 (+8.48%)</td><td>0.24 (+6.80%)</td><td>0.23 (+15.63%)</td><td>0.04 (-3.11%)</td><td>176.10 (-13.51%)</td><td>160.60 (-8.23%)</td><td>167.40 (-6.38%)</td><td>126.00 (-6.87%)</td><td>19.90 <b>(-22.03%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>203.60 (n/a)</td><td>175.00 (n/a)</td><td>178.80 (n/a)</td><td>135.30 (n/a)</td><td>25.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (+7.06%)</td><td>0.04 (+18.56%)</td><td>0.03 <b>(+21.21%)</b></td><td>0.03 <b>(+33.52%)</b></td><td>0.01 (-13.75%)</td><td>177.80 <b>(-25.07%)</b></td><td>143.70 (-17.55%)</td><td>146.40 (-17.47%)</td><td>111.60 (-6.61%)</td><td>25.90 <b>(-39.52%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>174.28 (n/a)</td><td>177.40 (n/a)</td><td>119.50 (n/a)</td><td>42.82 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-8.14%)</td><td>0.02 (-2.16%)</td><td>0.02 (-11.42%)</td><td>0.02 <b>(+63.66%)</b></td><td>0.00 <b>(-43.98%)</b></td><td>220.50 <b>(-38.90%)</b></td><td>182.98 (-7.19%)</td><td>184.20 (+12.87%)</td><td>146.30 (+8.85%)</td><td>32.03 <b>(-65.50%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>360.90 (n/a)</td><td>197.16 (n/a)</td><td>163.20 (n/a)</td><td>134.40 (n/a)</td><td>92.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (+19.25%)</td><td>0.04 (+9.15%)</td><td>0.04 (+2.32%)</td><td>0.03 (+10.18%)</td><td>0.01 <b>(+23.64%)</b></td><td>205.50 (-9.23%)</td><td>159.92 (-8.09%)</td><td>154.80 (-2.27%)</td><td>131.80 (-16.16%)</td><td>28.25 (-4.97%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>226.40 (n/a)</td><td>174.00 (n/a)</td><td>158.40 (n/a)</td><td>157.20 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 <b>(-24.13%)</b></td><td>0.02 (-10.22%)</td><td>0.02 (+0.39%)</td><td>0.02 (+4.95%)</td><td>0.00 <b>(-61.32%)</b></td><td>180.80 (-4.74%)</td><td>168.00 (+7.35%)</td><td>172.80 (-0.40%)</td><td>140.40 <b>(+31.71%)</b></td><td>16.71 <b>(-51.31%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>156.50 (n/a)</td><td>173.50 (n/a)</td><td>106.60 (n/a)</td><td>34.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (+3.65%)</td><td>0.03 (+13.82%)</td><td>0.03 (-0.05%)</td><td>0.02 <b>(+72.73%)</b></td><td>0.01 <b>(-33.60%)</b></td><td>209.60 <b>(-42.12%)</b></td><td>168.30 (-19.66%)</td><td>170.20 (+0.06%)</td><td>128.40 (-3.53%)</td><td>32.25 <b>(-64.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>362.10 (n/a)</td><td>209.48 (n/a)</td><td>170.10 (n/a)</td><td>133.10 (n/a)</td><td>91.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-14.92%)</td><td>0.02 (+2.01%)</td><td>0.02 (+17.04%)</td><td>0.02 (-3.88%)</td><td>0.01 <b>(-28.11%)</b></td><td>247.90 (+4.03%)</td><td>172.66 (-3.95%)</td><td>165.20 (-14.54%)</td><td>137.80 (+17.58%)</td><td>43.92 (-7.83%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>179.76 (n/a)</td><td>193.30 (n/a)</td><td>117.20 (n/a)</td><td>47.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-10.82%)</td><td>0.03 (-6.39%)</td><td>0.03 (-7.34%)</td><td>0.02 (+4.56%)</td><td>0.00 <b>(-34.57%)</b></td><td>208.90 (-4.35%)</td><td>177.50 (+5.43%)</td><td>179.60 (+7.93%)</td><td>151.70 (+12.12%)</td><td>21.14 <b>(-31.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>168.36 (n/a)</td><td>166.40 (n/a)</td><td>135.30 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 <b>(-24.78%)</b></td><td>0.02 <b>(-20.11%)</b></td><td>0.02 <b>(-23.07%)</b></td><td>0.02 (-9.14%)</td><td>0.00 <b>(-52.74%)</b></td><td>230.50 (+10.02%)</td><td>191.60 <b>(+20.40%)</b></td><td>178.30 <b>(+29.96%)</b></td><td>160.90 <b>(+32.98%)</b></td><td>30.19 <b>(-31.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>159.14 (n/a)</td><td>137.20 (n/a)</td><td>121.00 (n/a)</td><td>43.93 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 <b>(+25.25%)</b></td><td>0.03 (+4.89%)</td><td>0.03 (+6.59%)</td><td>0.02 (-9.56%)</td><td>0.01 <b>(+123.15%)</b></td><td>211.60 (+10.61%)</td><td>167.92 (+0.11%)</td><td>160.40 (-6.20%)</td><td>107.10 <b>(-20.19%)</b></td><td>44.19 <b>(+108.87%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.30 (n/a)</td><td>167.74 (n/a)</td><td>171.00 (n/a)</td><td>134.20 (n/a)</td><td>21.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-15.52%)</td><td>0.03 (-4.60%)</td><td>0.02 (-9.06%)</td><td>0.02 <b>(+33.96%)</b></td><td>0.00 <b>(-54.53%)</b></td><td>186.70 <b>(-25.35%)</b></td><td>163.86 (-0.24%)</td><td>167.40 (+9.91%)</td><td>139.90 (+18.36%)</td><td>18.82 <b>(-62.43%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.10 (n/a)</td><td>164.26 (n/a)</td><td>152.30 (n/a)</td><td>118.20 (n/a)</td><td>50.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-10.02%)</td><td>0.03 (-0.38%)</td><td>0.03 (+1.48%)</td><td>0.02 (+6.13%)</td><td>0.00 <b>(-31.26%)</b></td><td>203.70 (-5.78%)</td><td>176.08 (-1.15%)</td><td>168.70 (-1.46%)</td><td>144.70 (+11.14%)</td><td>24.69 <b>(-26.49%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>178.12 (n/a)</td><td>171.20 (n/a)</td><td>130.20 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-5.33%)</td><td>0.02 (-4.42%)</td><td>0.02 (-4.47%)</td><td>0.02 (+1.23%)</td><td>0.00 (-11.04%)</td><td>224.10 (-1.23%)</td><td>184.38 (+4.23%)</td><td>178.30 (+4.70%)</td><td>162.10 (+5.60%)</td><td>25.65 (-10.97%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.90 (n/a)</td><td>176.90 (n/a)</td><td>170.30 (n/a)</td><td>153.50 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 <b>(-22.29%)</b></td><td>0.02 (-11.45%)</td><td>0.02 (-8.96%)</td><td>0.02 (-6.26%)</td><td>0.00 <b>(-52.24%)</b></td><td>225.10 (+6.68%)</td><td>205.84 (+11.34%)</td><td>212.20 (+9.83%)</td><td>180.60 <b>(+28.63%)</b></td><td>18.50 <b>(-33.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>184.88 (n/a)</td><td>193.20 (n/a)</td><td>140.40 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (+3.28%)</td><td>0.02 (+1.56%)</td><td>0.02 (+4.93%)</td><td>0.02 (-1.29%)</td><td>0.00 (+5.08%)</td><td>217.10 (+1.31%)</td><td>175.90 (-1.35%)</td><td>175.70 (-4.72%)</td><td>133.70 (-3.19%)</td><td>31.98 (+3.15%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.30 (n/a)</td><td>178.30 (n/a)</td><td>184.40 (n/a)</td><td>138.10 (n/a)</td><td>31.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 <b>(+21.88%)</b></td><td>0.02 (-0.75%)</td><td>0.02 (-5.01%)</td><td>0.02 (-2.81%)</td><td>0.01 <b>(+82.49%)</b></td><td>215.30 (+2.87%)</td><td>193.80 (+2.75%)</td><td>206.10 (+5.26%)</td><td>134.70 (-17.97%)</td><td>33.38 <b>(+51.32%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.30 (n/a)</td><td>188.62 (n/a)</td><td>195.80 (n/a)</td><td>164.20 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (-11.91%)</td><td>0.02 (+0.31%)</td><td>0.02 (+2.71%)</td><td>0.02 (+15.82%)</td><td>0.00 <b>(-59.51%)</b></td><td>238.70 (-13.67%)</td><td>224.14 (-1.88%)</td><td>221.70 (-2.64%)</td><td>203.70 (+13.55%)</td><td>13.99 <b>(-59.69%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>276.50 (n/a)</td><td>228.44 (n/a)</td><td>227.70 (n/a)</td><td>179.40 (n/a)</td><td>34.70 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (-18.92%)</td><td>0.05 (+0.03%)</td><td>0.05 (+0.19%)</td><td>0.04 (-0.29%)</td><td>0.01 <b>(-40.49%)</b></td><td>221.10 (+0.32%)</td><td>179.82 (-2.29%)</td><td>180.30 (-0.17%)</td><td>153.90 <b>(+23.32%)</b></td><td>27.75 <b>(-27.15%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.40 (n/a)</td><td>184.04 (n/a)</td><td>180.60 (n/a)</td><td>124.80 (n/a)</td><td>38.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 <b>(-22.58%)</b></td><td>0.08 (+9.15%)</td><td>0.07 (+12.37%)</td><td>0.06 <b>(+64.16%)</b></td><td>0.02 <b>(-53.17%)</b></td><td>197.20 <b>(-39.08%)</b></td><td>157.64 <b>(-20.25%)</b></td><td>169.00 (-11.01%)</td><td>123.30 <b>(+29.25%)</b></td><td>31.59 <b>(-63.98%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>323.70 (n/a)</td><td>197.66 (n/a)</td><td>189.90 (n/a)</td><td>95.40 (n/a)</td><td>87.71 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (-15.90%)</td><td>0.05 (-9.10%)</td><td>0.05 (-11.03%)</td><td>0.04 (+15.67%)</td><td>0.00 <b>(-66.26%)</b></td><td>186.20 (-13.56%)</td><td>172.66 (+7.28%)</td><td>171.60 (+12.38%)</td><td>160.00 (+18.96%)</td><td>11.24 <b>(-65.61%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>160.94 (n/a)</td><td>152.70 (n/a)</td><td>134.50 (n/a)</td><td>32.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (-18.49%)</td><td>0.06 (-8.95%)</td><td>0.05 (-12.83%)</td><td>0.05 (+14.04%)</td><td>0.00 <b>(-57.38%)</b></td><td>208.60 (-12.32%)</td><td>185.06 (+6.92%)</td><td>188.30 (+14.75%)</td><td>168.00 <b>(+22.72%)</b></td><td>16.58 <b>(-56.60%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>237.90 (n/a)</td><td>173.08 (n/a)</td><td>164.10 (n/a)</td><td>136.90 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (-14.35%)</td><td>0.05 (+5.50%)</td><td>0.05 (+2.99%)</td><td>0.04 <b>(+54.11%)</b></td><td>0.01 <b>(-50.35%)</b></td><td>212.20 <b>(-35.09%)</b></td><td>166.96 (-13.63%)</td><td>160.00 (-2.91%)</td><td>135.70 (+16.78%)</td><td>29.34 <b>(-63.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>326.90 (n/a)</td><td>193.30 (n/a)</td><td>164.80 (n/a)</td><td>116.20 (n/a)</td><td>80.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (+0.86%)</td><td>0.07 (+16.04%)</td><td>0.06 (+0.97%)</td><td>0.05 <b>(+32.25%)</b></td><td>0.01 <b>(-20.86%)</b></td><td>190.20 <b>(-24.40%)</b></td><td>159.26 (-17.09%)</td><td>175.20 (-0.96%)</td><td>119.30 (-0.83%)</td><td>31.48 <b>(-42.93%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>251.60 (n/a)</td><td>192.08 (n/a)</td><td>176.90 (n/a)</td><td>120.30 (n/a)</td><td>55.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 <b>(-29.16%)</b></td><td>0.05 (-17.67%)</td><td>0.05 (-13.48%)</td><td>0.04 (-10.43%)</td><td>0.00 <b>(-64.98%)</b></td><td>192.30 (+11.67%)</td><td>177.84 (+18.97%)</td><td>179.20 (+15.54%)</td><td>155.60 <b>(+41.20%)</b></td><td>13.71 <b>(-45.14%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.20 (n/a)</td><td>149.48 (n/a)</td><td>155.10 (n/a)</td><td>110.20 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+5.98%)</td><td>0.05 (+3.38%)</td><td>0.05 (-3.64%)</td><td>0.05 (+12.98%)</td><td>0.00 (-10.34%)</td><td>182.70 (-11.48%)</td><td>170.98 (-3.48%)</td><td>175.20 (+3.73%)</td><td>155.60 (-5.64%)</td><td>12.63 <b>(-25.74%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.40 (n/a)</td><td>177.14 (n/a)</td><td>168.90 (n/a)</td><td>164.90 (n/a)</td><td>17.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+12.00%)</td><td>0.05 (+1.96%)</td><td>0.05 (+1.52%)</td><td>0.04 (+0.76%)</td><td>0.01 <b>(+32.16%)</b></td><td>197.30 (-0.75%)</td><td>170.28 (-1.10%)</td><td>169.00 (-1.46%)</td><td>128.50 (-10.70%)</td><td>27.95 (+16.76%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>172.18 (n/a)</td><td>171.50 (n/a)</td><td>143.90 (n/a)</td><td>23.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (-1.93%)</td><td>0.06 (+9.75%)</td><td>0.06 (+12.81%)</td><td>0.05 (+18.98%)</td><td>0.01 <b>(-34.23%)</b></td><td>177.30 (-15.93%)</td><td>157.64 (-10.46%)</td><td>155.50 (-11.40%)</td><td>131.90 (+1.93%)</td><td>17.84 <b>(-42.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>176.06 (n/a)</td><td>175.50 (n/a)</td><td>129.40 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (-1.30%)</td><td>0.04 (-9.62%)</td><td>0.04 (-15.44%)</td><td>0.04 (-10.33%)</td><td>0.01 (+17.34%)</td><td>213.50 (+11.55%)</td><td>185.08 (+11.11%)</td><td>188.40 (+18.27%)</td><td>153.70 (+1.32%)</td><td>21.80 <b>(+31.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.40 (n/a)</td><td>166.58 (n/a)</td><td>159.30 (n/a)</td><td>151.70 (n/a)</td><td>16.61 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (+6.22%)</td><td>0.04 (+6.03%)</td><td>0.04 (-0.16%)</td><td>0.04 <b>(+42.77%)</b></td><td>0.01 <b>(-37.02%)</b></td><td>239.90 <b>(-29.96%)</b></td><td>205.16 (-9.41%)</td><td>207.30 (+0.19%)</td><td>168.60 (-5.86%)</td><td>26.89 <b>(-59.83%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>342.50 (n/a)</td><td>226.48 (n/a)</td><td>206.90 (n/a)</td><td>179.10 (n/a)</td><td>66.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (+5.40%)</td><td>0.05 (-1.46%)</td><td>0.04 (-15.38%)</td><td>0.03 (+14.86%)</td><td>0.01 (+0.57%)</td><td>249.10 (-12.93%)</td><td>183.94 (+0.14%)</td><td>193.40 (+18.14%)</td><td>137.40 (-5.11%)</td><td>44.96 <b>(-22.69%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>286.10 (n/a)</td><td>183.68 (n/a)</td><td>163.70 (n/a)</td><td>144.80 (n/a)</td><td>58.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (+7.08%)</td><td>0.04 (+3.07%)</td><td>0.04 (+2.61%)</td><td>0.04 (-0.90%)</td><td>0.00 <b>(+60.37%)</b></td><td>213.70 (+0.90%)</td><td>198.06 (-2.72%)</td><td>202.00 (-2.56%)</td><td>175.10 (-6.56%)</td><td>14.43 <b>(+49.51%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.80 (n/a)</td><td>203.60 (n/a)</td><td>207.30 (n/a)</td><td>187.40 (n/a)</td><td>9.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (-6.48%)</td><td>0.04 (+1.37%)</td><td>0.04 (-0.62%)</td><td>0.04 <b>(+34.92%)</b></td><td>0.00 <b>(-49.04%)</b></td><td>227.70 <b>(-25.88%)</b></td><td>213.88 (-4.58%)</td><td>222.80 (+0.63%)</td><td>177.20 (+6.94%)</td><td>20.95 <b>(-60.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.20 (n/a)</td><td>224.14 (n/a)</td><td>221.40 (n/a)</td><td>165.70 (n/a)</td><td>53.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (-14.36%)</td><td>0.09 (-11.36%)</td><td>0.09 (-11.55%)</td><td>0.08 (+1.41%)</td><td>0.01 <b>(-36.98%)</b></td><td>197.00 (-1.40%)</td><td>175.90 (+11.27%)</td><td>180.40 (+13.03%)</td><td>143.20 (+16.80%)</td><td>19.78 <b>(-29.65%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.80 (n/a)</td><td>158.08 (n/a)</td><td>159.60 (n/a)</td><td>122.60 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (-16.38%)</td><td>0.13 (-11.14%)</td><td>0.13 (-2.41%)</td><td>0.08 <b>(-36.68%)</b></td><td>0.03 (+5.76%)</td><td>319.70 <b>(+57.88%)</b></td><td>202.52 (+16.73%)</td><td>182.80 (+2.47%)</td><td>149.60 (+19.58%)</td><td>67.29 <b>(+111.99%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>202.50 (n/a)</td><td>173.50 (n/a)</td><td>178.40 (n/a)</td><td>125.10 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (-0.98%)</td><td>0.09 (-8.73%)</td><td>0.10 (-6.79%)</td><td>0.05 (-11.87%)</td><td>0.03 (+0.86%)</td><td>334.30 (+13.48%)</td><td>198.96 (+11.21%)</td><td>159.60 (+7.26%)</td><td>136.20 (+1.04%)</td><td>79.72 (+19.00%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>294.60 (n/a)</td><td>178.90 (n/a)</td><td>148.80 (n/a)</td><td>134.80 (n/a)</td><td>66.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (-2.80%)</td><td>0.11 (-9.81%)</td><td>0.11 (-8.30%)</td><td>0.09 (-9.64%)</td><td>0.02 (+19.19%)</td><td>225.00 (+10.67%)</td><td>189.20 (+12.14%)</td><td>184.30 (+9.05%)</td><td>138.60 (+2.90%)</td><td>34.29 <b>(+36.65%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>203.30 (n/a)</td><td>168.72 (n/a)</td><td>169.00 (n/a)</td><td>134.70 (n/a)</td><td>25.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (-3.72%)</td><td>0.11 (-14.77%)</td><td>0.10 <b>(-21.67%)</b></td><td>0.09 (+0.01%)</td><td>0.02 (-15.65%)</td><td>180.80 (+0.00%)</td><td>158.38 (+16.34%)</td><td>162.10 <b>(+27.64%)</b></td><td>117.50 (+3.80%)</td><td>24.17 (-14.34%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.80 (n/a)</td><td>136.14 (n/a)</td><td>127.00 (n/a)</td><td>113.20 (n/a)</td><td>28.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (+2.43%)</td><td>0.11 (+2.72%)</td><td>0.11 (+3.31%)</td><td>0.10 (+0.64%)</td><td>0.02 (+6.23%)</td><td>214.30 (-0.65%)</td><td>186.60 (-2.55%)</td><td>193.60 (-3.20%)</td><td>154.40 (-2.40%)</td><td>24.97 (+2.44%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>191.48 (n/a)</td><td>200.00 (n/a)</td><td>158.20 (n/a)</td><td>24.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 <b>(-32.85%)</b></td><td>0.08 <b>(-23.72%)</b></td><td>0.08 (-18.05%)</td><td>0.06 <b>(-27.01%)</b></td><td>0.01 <b>(-44.65%)</b></td><td>252.80 <b>(+36.94%)</b></td><td>197.30 <b>(+29.68%)</b></td><td>194.10 <b>(+22.00%)</b></td><td>168.50 <b>(+48.98%)</b></td><td>33.10 (+15.75%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>184.60 (n/a)</td><td>152.14 (n/a)</td><td>159.10 (n/a)</td><td>113.10 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (-10.57%)</td><td>0.10 (-4.90%)</td><td>0.10 (-7.65%)</td><td>0.09 (+1.39%)</td><td>0.01 <b>(-49.10%)</b></td><td>199.10 (-1.34%)</td><td>184.72 (+4.10%)</td><td>188.00 (+8.29%)</td><td>165.30 (+11.84%)</td><td>12.67 <b>(-45.49%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>177.44 (n/a)</td><td>173.60 (n/a)</td><td>147.80 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (-8.19%)</td><td>0.08 (-10.63%)</td><td>0.08 (-14.70%)</td><td>0.07 (-15.66%)</td><td>0.01 (-5.50%)</td><td>236.30 (+18.56%)</td><td>196.62 (+12.07%)</td><td>197.10 (+17.25%)</td><td>164.70 (+8.93%)</td><td>25.94 <b>(+20.31%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.30 (n/a)</td><td>175.44 (n/a)</td><td>168.10 (n/a)</td><td>151.20 (n/a)</td><td>21.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 <b>(-42.24%)</b></td><td>0.09 <b>(-20.45%)</b></td><td>0.08 (-6.65%)</td><td>0.07 (-12.50%)</td><td>0.01 <b>(-68.85%)</b></td><td>252.30 (+14.27%)</td><td>219.94 (+18.20%)</td><td>219.00 (+7.14%)</td><td>179.30 <b>(+73.24%)</b></td><td>30.95 <b>(-34.49%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>220.80 (n/a)</td><td>186.08 (n/a)</td><td>204.40 (n/a)</td><td>103.50 (n/a)</td><td>47.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (+15.44%)</td><td>0.10 (+8.25%)</td><td>0.09 (-8.06%)</td><td>0.09 <b>(+50.10%)</b></td><td>0.02 (-19.17%)</td><td>188.20 <b>(-33.38%)</b></td><td>171.30 (-10.76%)</td><td>178.40 (+8.78%)</td><td>127.70 (-13.36%)</td><td>24.76 <b>(-55.11%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>282.50 (n/a)</td><td>191.96 (n/a)</td><td>164.00 (n/a)</td><td>147.40 (n/a)</td><td>55.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 <b>(-30.34%)</b></td><td>0.08 (-8.61%)</td><td>0.07 (-12.70%)</td><td>0.07 <b>(+21.86%)</b></td><td>0.01 <b>(-56.01%)</b></td><td>252.20 (-17.96%)</td><td>222.32 (+3.03%)</td><td>245.00 (+14.54%)</td><td>182.10 <b>(+43.61%)</b></td><td>34.56 <b>(-46.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>307.40 (n/a)</td><td>215.78 (n/a)</td><td>213.90 (n/a)</td><td>126.80 (n/a)</td><td>64.35 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (-11.66%)</td><td>0.09 (-8.80%)</td><td>0.09 <b>(-21.41%)</b></td><td>0.07 (+18.54%)</td><td>0.02 <b>(-31.26%)</b></td><td>243.50 (-15.63%)</td><td>184.48 (+3.73%)</td><td>191.60 <b>(+27.22%)</b></td><td>128.80 (+13.18%)</td><td>42.80 <b>(-37.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>288.60 (n/a)</td><td>177.84 (n/a)</td><td>150.60 (n/a)</td><td>113.80 (n/a)</td><td>68.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (-1.34%)</td><td>0.08 (+1.55%)</td><td>0.07 (-12.24%)</td><td>0.06 <b>(+20.37%)</b></td><td>0.02 <b>(-30.80%)</b></td><td>307.00 (-16.91%)</td><td>236.86 (-6.57%)</td><td>235.40 (+13.94%)</td><td>171.40 (+1.36%)</td><td>48.04 <b>(-44.11%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>369.50 (n/a)</td><td>253.52 (n/a)</td><td>206.60 (n/a)</td><td>169.10 (n/a)</td><td>85.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (-11.41%)</td><td>0.07 (-6.97%)</td><td>0.07 (+1.01%)</td><td>0.06 (-9.35%)</td><td>0.01 <b>(-25.01%)</b></td><td>254.50 (+10.32%)</td><td>224.04 (+7.21%)</td><td>219.20 (-0.99%)</td><td>205.50 (+12.91%)</td><td>20.39 (-6.55%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>208.98 (n/a)</td><td>221.40 (n/a)</td><td>182.00 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 <b>(+35.08%)</b></td><td>0.19 (-3.23%)</td><td>0.18 (-11.03%)</td><td>0.11 <b>(-39.66%)</b></td><td>0.06 <b>(+606.83%)</b></td><td>295.30 <b>(+65.71%)</b></td><td>188.72 (+12.78%)</td><td>186.10 (+12.38%)</td><td>117.40 <b>(-25.98%)</b></td><td>65.98 <b>(+784.36%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>178.20 (n/a)</td><td>167.34 (n/a)</td><td>165.60 (n/a)</td><td>158.60 (n/a)</td><td>7.46 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.24 (-7.77%)</td><td>0.21 (-8.81%)</td><td>0.21 (-6.85%)</td><td>0.16 <b>(-23.60%)</b></td><td>0.04 <b>(+63.19%)</b></td><td>206.30 <b>(+30.90%)</b></td><td>162.74 (+11.76%)</td><td>159.20 (+7.35%)</td><td>134.10 (+8.41%)</td><td>30.06 <b>(+132.19%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>157.60 (n/a)</td><td>145.62 (n/a)</td><td>148.30 (n/a)</td><td>123.70 (n/a)</td><td>12.95 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.26 (-1.85%)</td><td>0.21 (-5.21%)</td><td>0.22 (+6.48%)</td><td>0.15 (-19.93%)</td><td>0.05 <b>(+39.14%)</b></td><td>279.40 <b>(+24.90%)</b></td><td>202.86 (+8.54%)</td><td>185.80 (-6.11%)</td><td>156.00 (+1.89%)</td><td>51.96 <b>(+78.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>223.70 (n/a)</td><td>186.90 (n/a)</td><td>197.90 (n/a)</td><td>153.10 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (-19.50%)</td><td>0.18 <b>(-20.27%)</b></td><td>0.19 (-19.79%)</td><td>0.15 (-11.96%)</td><td>0.03 <b>(-29.46%)</b></td><td>212.90 (+13.55%)</td><td>179.88 <b>(+24.57%)</b></td><td>173.20 <b>(+24.60%)</b></td><td>148.90 <b>(+24.29%)</b></td><td>24.39 (-3.99%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>187.50 (n/a)</td><td>144.40 (n/a)</td><td>139.00 (n/a)</td><td>119.80 (n/a)</td><td>25.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (+2.76%)</td><td>0.25 (+6.48%)</td><td>0.24 (+3.61%)</td><td>0.22 (+16.21%)</td><td>0.04 (-15.69%)</td><td>186.90 (-13.95%)</td><td>166.30 (-7.11%)</td><td>169.30 (-3.48%)</td><td>129.90 (-2.70%)</td><td>22.15 <b>(-30.07%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>217.20 (n/a)</td><td>179.02 (n/a)</td><td>175.40 (n/a)</td><td>133.50 (n/a)</td><td>31.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.26 (-2.07%)</td><td>0.20 (-6.87%)</td><td>0.19 (-7.26%)</td><td>0.16 (+7.33%)</td><td>0.04 (-11.71%)</td><td>201.20 (-6.85%)</td><td>170.82 (+6.36%)</td><td>170.80 (+7.83%)</td><td>127.40 (+2.08%)</td><td>28.21 (-18.76%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.00 (n/a)</td><td>160.60 (n/a)</td><td>158.40 (n/a)</td><td>124.80 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.26 (+16.67%)</td><td>0.20 (+0.98%)</td><td>0.19 (+1.26%)</td><td>0.15 (-7.26%)</td><td>0.04 <b>(+89.18%)</b></td><td>239.80 (+7.82%)</td><td>195.96 (+1.54%)</td><td>190.30 (-1.19%)</td><td>140.90 (-14.29%)</td><td>39.81 <b>(+76.77%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>222.40 (n/a)</td><td>192.98 (n/a)</td><td>192.60 (n/a)</td><td>164.40 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.24 (+7.00%)</td><td>0.19 (-1.81%)</td><td>0.17 (-12.32%)</td><td>0.16 (+7.70%)</td><td>0.04 (+9.49%)</td><td>204.00 (-7.15%)</td><td>177.02 (+2.02%)</td><td>193.70 (+14.08%)</td><td>134.80 (-6.52%)</td><td>30.06 (-3.00%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.70 (n/a)</td><td>173.52 (n/a)</td><td>169.80 (n/a)</td><td>144.20 (n/a)</td><td>30.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (+0.92%)</td><td>0.21 (-0.77%)</td><td>0.20 (-10.39%)</td><td>0.17 (+4.15%)</td><td>0.04 (-0.62%)</td><td>214.10 (-3.99%)</td><td>178.76 (+0.54%)</td><td>186.30 (+11.62%)</td><td>131.10 (-0.91%)</td><td>33.35 (-6.99%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>223.00 (n/a)</td><td>177.80 (n/a)</td><td>166.90 (n/a)</td><td>132.30 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (-1.04%)</td><td>0.18 (-9.15%)</td><td>0.17 (-13.31%)</td><td>0.15 (-0.43%)</td><td>0.03 (-4.51%)</td><td>224.40 (+0.45%)</td><td>189.90 (+9.83%)</td><td>188.50 (+15.36%)</td><td>153.30 (+1.05%)</td><td>26.78 (-6.78%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>223.40 (n/a)</td><td>172.90 (n/a)</td><td>163.40 (n/a)</td><td>151.70 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (+4.18%)</td><td>0.17 (-2.96%)</td><td>0.16 (-1.45%)</td><td>0.12 <b>(-28.02%)</b></td><td>0.04 <b>(+136.18%)</b></td><td>301.80 <b>(+38.95%)</b></td><td>215.78 (+6.89%)</td><td>213.30 (+1.47%)</td><td>168.90 (-3.98%)</td><td>52.97 <b>(+216.38%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>217.20 (n/a)</td><td>201.88 (n/a)</td><td>210.20 (n/a)</td><td>175.90 (n/a)</td><td>16.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (+1.55%)</td><td>0.16 (-1.09%)</td><td>0.18 (+7.92%)</td><td>0.11 (-12.15%)</td><td>0.04 <b>(+35.34%)</b></td><td>301.80 (+13.84%)</td><td>212.24 (+4.17%)</td><td>178.70 (-7.31%)</td><td>162.60 (-1.51%)</td><td>61.17 <b>(+49.78%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>265.10 (n/a)</td><td>203.74 (n/a)</td><td>192.80 (n/a)</td><td>165.10 (n/a)</td><td>40.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (+4.99%)</td><td>0.18 (+0.03%)</td><td>0.17 (-2.78%)</td><td>0.15 (-8.67%)</td><td>0.02 <b>(+119.92%)</b></td><td>227.60 (+9.53%)</td><td>200.32 (+0.92%)</td><td>206.40 (+2.84%)</td><td>173.30 (-4.73%)</td><td>23.88 <b>(+126.10%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>198.50 (n/a)</td><td>200.70 (n/a)</td><td>181.90 (n/a)</td><td>10.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (-3.98%)</td><td>0.15 (-9.47%)</td><td>0.14 (-10.67%)</td><td>0.12 (-18.66%)</td><td>0.02 <b>(+51.51%)</b></td><td>267.90 <b>(+22.95%)</b></td><td>227.18 (+11.64%)</td><td>231.20 (+11.96%)</td><td>183.70 (+4.20%)</td><td>31.36 <b>(+94.82%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>203.50 (n/a)</td><td>206.50 (n/a)</td><td>176.30 (n/a)</td><td>16.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (-12.12%)</td><td>0.12 (-8.25%)</td><td>0.12 (-7.88%)</td><td>0.10 <b>(+27.73%)</b></td><td>0.02 <b>(-45.90%)</b></td><td>198.90 <b>(-21.69%)</b></td><td>172.84 (+4.01%)</td><td>168.40 (+8.58%)</td><td>140.30 (+13.79%)</td><td>25.35 <b>(-51.47%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>254.00 (n/a)</td><td>166.18 (n/a)</td><td>155.10 (n/a)</td><td>123.30 (n/a)</td><td>52.23 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (-7.76%)</td><td>0.13 (+14.24%)</td><td>0.14 <b>(+21.79%)</b></td><td>0.10 <b>(+32.01%)</b></td><td>0.02 <b>(-40.06%)</b></td><td>195.30 <b>(-24.24%)</b></td><td>154.82 (-15.29%)</td><td>145.50 (-17.89%)</td><td>142.10 (+8.47%)</td><td>22.69 <b>(-51.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>257.80 (n/a)</td><td>182.76 (n/a)</td><td>177.20 (n/a)</td><td>131.00 (n/a)</td><td>46.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.17 (-5.05%)</td><td>0.13 (-9.22%)</td><td>0.13 <b>(-22.55%)</b></td><td>0.11 (+4.67%)</td><td>0.03 (-19.81%)</td><td>193.80 (-4.44%)</td><td>156.20 (+8.43%)</td><td>161.10 <b>(+29.09%)</b></td><td>121.60 (+5.28%)</td><td>29.42 (-19.95%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>202.80 (n/a)</td><td>144.06 (n/a)</td><td>124.80 (n/a)</td><td>115.50 (n/a)</td><td>36.75 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (-17.09%)</td><td>0.12 (-14.46%)</td><td>0.14 (-10.08%)</td><td>0.06 <b>(-36.76%)</b></td><td>0.04 (+7.88%)</td><td>370.00 <b>(+58.12%)</b></td><td>190.94 <b>(+26.63%)</b></td><td>146.10 (+11.19%)</td><td>129.00 <b>(+20.67%)</b></td><td>101.68 <b>(+105.00%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>234.00 (n/a)</td><td>150.78 (n/a)</td><td>131.40 (n/a)</td><td>106.90 (n/a)</td><td>49.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 <b>(-27.48%)</b></td><td>0.11 <b>(-22.99%)</b></td><td>0.12 <b>(-27.30%)</b></td><td>0.06 <b>(-22.28%)</b></td><td>0.03 <b>(-28.92%)</b></td><td>365.40 <b>(+28.66%)</b></td><td>207.06 <b>(+28.59%)</b></td><td>174.30 <b>(+37.57%)</b></td><td>152.90 <b>(+37.87%)</b></td><td>89.37 <b>(+26.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>284.00 (n/a)</td><td>161.02 (n/a)</td><td>126.70 (n/a)</td><td>110.90 (n/a)</td><td>70.91 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.17 <b>(+24.50%)</b></td><td>0.13 (-1.43%)</td><td>0.12 (-6.12%)</td><td>0.09 (-19.85%)</td><td>0.03 <b>(+276.03%)</b></td><td>220.40 <b>(+24.73%)</b></td><td>167.48 (+5.31%)</td><td>165.90 (+6.48%)</td><td>121.30 (-19.67%)</td><td>37.41 <b>(+269.67%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>176.70 (n/a)</td><td>159.04 (n/a)</td><td>155.80 (n/a)</td><td>151.00 (n/a)</td><td>10.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (-10.39%)</td><td>0.12 (+4.80%)</td><td>0.12 (+11.50%)</td><td>0.10 (+4.67%)</td><td>0.01 <b>(-37.71%)</b></td><td>199.80 (-4.45%)</td><td>175.28 (-5.66%)</td><td>168.60 (-10.32%)</td><td>159.30 (+11.63%)</td><td>17.97 <b>(-34.16%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>209.10 (n/a)</td><td>185.80 (n/a)</td><td>188.00 (n/a)</td><td>142.70 (n/a)</td><td>27.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (+15.99%)</td><td>0.11 (+4.55%)</td><td>0.11 (-2.32%)</td><td>0.08 (-3.85%)</td><td>0.03 <b>(+61.55%)</b></td><td>252.40 (+4.00%)</td><td>197.72 (-1.71%)</td><td>191.10 (+2.41%)</td><td>141.00 (-13.81%)</td><td>47.68 <b>(+45.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>242.70 (n/a)</td><td>201.16 (n/a)</td><td>186.60 (n/a)</td><td>163.60 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (-10.31%)</td><td>0.15 (-10.95%)</td><td>0.14 <b>(-20.56%)</b></td><td>0.13 (-7.91%)</td><td>0.02 (-10.01%)</td><td>186.80 (+8.60%)</td><td>164.26 (+12.25%)</td><td>178.80 <b>(+25.92%)</b></td><td>132.40 (+11.54%)</td><td>24.28 (+7.33%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>172.00 (n/a)</td><td>146.34 (n/a)</td><td>142.00 (n/a)</td><td>118.70 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (-15.01%)</td><td>0.14 (-5.95%)</td><td>0.14 (-4.29%)</td><td>0.12 (+17.06%)</td><td>0.02 <b>(-53.77%)</b></td><td>205.60 (-14.55%)</td><td>175.90 (+2.29%)</td><td>178.60 (+4.44%)</td><td>155.00 (+17.69%)</td><td>21.10 <b>(-52.82%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>240.60 (n/a)</td><td>171.96 (n/a)</td><td>171.00 (n/a)</td><td>131.70 (n/a)</td><td>44.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (-0.94%)</td><td>0.15 (-13.29%)</td><td>0.14 (-17.12%)</td><td>0.09 <b>(-37.73%)</b></td><td>0.04 <b>(+173.20%)</b></td><td>259.40 <b>(+60.62%)</b></td><td>178.90 <b>(+21.42%)</b></td><td>172.70 <b>(+20.60%)</b></td><td>133.90 (+0.98%)</td><td>50.52 <b>(+335.38%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>161.50 (n/a)</td><td>147.34 (n/a)</td><td>143.20 (n/a)</td><td>132.60 (n/a)</td><td>11.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (+1.15%)</td><td>0.14 (-18.19%)</td><td>0.14 <b>(-20.43%)</b></td><td>0.12 <b>(-22.74%)</b></td><td>0.03 <b>(+80.44%)</b></td><td>211.60 <b>(+29.42%)</b></td><td>178.84 <b>(+25.22%)</b></td><td>175.10 <b>(+25.70%)</b></td><td>128.30 (-1.16%)</td><td>33.36 <b>(+132.39%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>163.50 (n/a)</td><td>142.82 (n/a)</td><td>139.30 (n/a)</td><td>129.80 (n/a)</td><td>14.35 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (+15.97%)</td><td>0.16 (-8.82%)</td><td>0.14 <b>(-26.08%)</b></td><td>0.13 (-6.60%)</td><td>0.04 <b>(+65.59%)</b></td><td>191.80 (+7.03%)</td><td>158.72 (+12.63%)</td><td>172.80 <b>(+35.21%)</b></td><td>109.40 (-13.79%)</td><td>34.89 <b>(+54.67%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>179.20 (n/a)</td><td>140.92 (n/a)</td><td>127.80 (n/a)</td><td>126.90 (n/a)</td><td>22.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (+1.79%)</td><td>0.16 (+1.71%)</td><td>0.18 (+12.57%)</td><td>0.12 (+3.58%)</td><td>0.04 (+6.89%)</td><td>206.60 (-3.46%)</td><td>157.92 (-1.25%)</td><td>139.70 (-11.13%)</td><td>122.30 (-1.77%)</td><td>37.14 (+3.76%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.00 (n/a)</td><td>159.92 (n/a)</td><td>157.20 (n/a)</td><td>124.50 (n/a)</td><td>35.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.17 (+11.02%)</td><td>0.14 (+0.94%)</td><td>0.15 (+5.38%)</td><td>0.12 (-8.95%)</td><td>0.02 <b>(+170.07%)</b></td><td>204.00 (+9.80%)</td><td>172.84 (+0.56%)</td><td>161.50 (-5.11%)</td><td>145.20 (-9.93%)</td><td>25.78 <b>(+171.05%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>185.80 (n/a)</td><td>171.88 (n/a)</td><td>170.20 (n/a)</td><td>161.20 (n/a)</td><td>9.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (+4.99%)</td><td>0.16 (+5.75%)</td><td>0.16 (+10.74%)</td><td>0.12 (+10.74%)</td><td>0.03 (+9.68%)</td><td>204.30 (-9.72%)</td><td>164.16 (-5.22%)</td><td>153.30 (-9.66%)</td><td>124.90 (-4.73%)</td><td>34.27 (-3.54%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>226.30 (n/a)</td><td>173.20 (n/a)</td><td>169.70 (n/a)</td><td>131.10 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (-4.19%)</td><td>0.12 (+0.29%)</td><td>0.11 (-8.18%)</td><td>0.11 (+8.98%)</td><td>0.02 (-10.31%)</td><td>170.80 (-8.22%)</td><td>153.76 (-0.68%)</td><td>166.50 (+8.97%)</td><td>130.90 (+4.39%)</td><td>19.77 (-14.54%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>186.10 (n/a)</td><td>154.82 (n/a)</td><td>152.80 (n/a)</td><td>125.40 (n/a)</td><td>23.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (-19.55%)</td><td>0.11 (-15.90%)</td><td>0.11 <b>(-22.27%)</b></td><td>0.09 (-4.23%)</td><td>0.02 <b>(-41.04%)</b></td><td>211.30 (+4.40%)</td><td>169.20 (+16.26%)</td><td>167.90 <b>(+28.66%)</b></td><td>138.30 <b>(+24.26%)</b></td><td>26.58 <b>(-24.36%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>202.40 (n/a)</td><td>145.54 (n/a)</td><td>130.50 (n/a)</td><td>111.30 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (+7.45%)</td><td>0.13 (+7.52%)</td><td>0.14 (+5.16%)</td><td>0.10 (-4.06%)</td><td>0.02 (+19.46%)</td><td>181.90 (+4.24%)</td><td>143.74 (-6.58%)</td><td>136.20 (-4.89%)</td><td>129.10 (-6.92%)</td><td>21.54 (+18.41%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>174.50 (n/a)</td><td>153.86 (n/a)</td><td>143.20 (n/a)</td><td>138.70 (n/a)</td><td>18.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (+0.98%)</td><td>0.13 (+1.73%)</td><td>0.13 (-0.49%)</td><td>0.11 (+2.81%)</td><td>0.02 (+16.92%)</td><td>171.00 (-2.73%)</td><td>148.02 (-1.40%)</td><td>146.60 (+0.48%)</td><td>129.30 (-0.92%)</td><td>18.99 (+10.30%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>150.12 (n/a)</td><td>145.90 (n/a)</td><td>130.50 (n/a)</td><td>17.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (+1.60%)</td><td>0.12 (-5.13%)</td><td>0.12 (-7.17%)</td><td>0.08 (-19.87%)</td><td>0.02 <b>(+43.86%)</b></td><td>241.60 <b>(+24.79%)</b></td><td>166.62 (+8.32%)</td><td>153.70 (+7.71%)</td><td>130.10 (-1.59%)</td><td>43.73 <b>(+81.10%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>193.60 (n/a)</td><td>153.82 (n/a)</td><td>142.70 (n/a)</td><td>132.20 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (-0.86%)</td><td>0.11 (-6.02%)</td><td>0.10 <b>(-28.48%)</b></td><td>0.09 <b>(+33.12%)</b></td><td>0.03 (-14.13%)</td><td>205.90 <b>(-24.88%)</b></td><td>170.88 (+2.62%)</td><td>188.40 <b>(+39.76%)</b></td><td>128.30 (+0.86%)</td><td>38.41 <b>(-37.68%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>274.10 (n/a)</td><td>166.52 (n/a)</td><td>134.80 (n/a)</td><td>127.20 (n/a)</td><td>61.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 <b>(+35.84%)</b></td><td>0.09 (+5.40%)</td><td>0.09 (-2.33%)</td><td>0.06 (+3.07%)</td><td>0.03 <b>(+82.04%)</b></td><td>284.70 (-2.97%)</td><td>208.78 (-1.98%)</td><td>202.30 (+2.43%)</td><td>132.80 <b>(-26.39%)</b></td><td>55.15 <b>(+21.14%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>293.40 (n/a)</td><td>213.00 (n/a)</td><td>197.50 (n/a)</td><td>180.40 (n/a)</td><td>45.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 <b>(+47.48%)</b></td><td>0.12 <b>(+29.78%)</b></td><td>0.11 (+12.32%)</td><td>0.08 <b>(+35.51%)</b></td><td>0.03 <b>(+65.06%)</b></td><td>221.40 <b>(-26.20%)</b></td><td>167.20 <b>(-22.20%)</b></td><td>174.90 (-10.99%)</td><td>120.70 <b>(-32.15%)</b></td><td>38.70 <b>(-21.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>300.00 (n/a)</td><td>214.90 (n/a)</td><td>196.50 (n/a)</td><td>177.90 (n/a)</td><td>49.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.67 (-9.44%)</td><td>0.58 (-4.42%)</td><td>0.59 (+3.06%)</td><td>0.48 (-10.89%)</td><td>0.07 (-14.06%)</td><td>206.80 (+12.21%)</td><td>170.54 (+4.55%)</td><td>165.90 (-2.98%)</td><td>146.40 (+10.41%)</td><td>22.23 (+10.12%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.74 (n/a)</td><td>0.61 (n/a)</td><td>0.57 (n/a)</td><td>0.53 (n/a)</td><td>0.08 (n/a)</td><td>184.30 (n/a)</td><td>163.12 (n/a)</td><td>171.00 (n/a)</td><td>132.60 (n/a)</td><td>20.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.77 (+3.59%)</td><td>0.61 (+1.33%)</td><td>0.58 (-5.29%)</td><td>0.47 (+1.18%)</td><td>0.11 (-9.85%)</td><td>207.60 (-1.14%)</td><td>164.72 (-2.16%)</td><td>168.40 (+5.58%)</td><td>127.30 (-3.49%)</td><td>30.19 (-15.42%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.62 (n/a)</td><td>0.47 (n/a)</td><td>0.13 (n/a)</td><td>210.00 (n/a)</td><td>168.36 (n/a)</td><td>159.50 (n/a)</td><td>131.90 (n/a)</td><td>35.69 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.74 (-10.13%)</td><td>0.59 (-10.29%)</td><td>0.59 (-10.18%)</td><td>0.47 (-8.79%)</td><td>0.10 <b>(-28.24%)</b></td><td>211.30 (+9.65%)</td><td>170.26 (+9.93%)</td><td>166.90 (+11.34%)</td><td>133.00 (+11.30%)</td><td>28.68 (-13.51%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.82 (n/a)</td><td>0.66 (n/a)</td><td>0.66 (n/a)</td><td>0.51 (n/a)</td><td>0.14 (n/a)</td><td>192.70 (n/a)</td><td>154.88 (n/a)</td><td>149.90 (n/a)</td><td>119.50 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.93 (+17.83%)</td><td>0.70 (+16.41%)</td><td>0.67 (+18.87%)</td><td>0.52 <b>(+20.58%)</b></td><td>0.16 (+2.58%)</td><td>190.50 (-17.07%)</td><td>146.84 (-15.20%)</td><td>147.60 (-15.85%)</td><td>105.70 (-15.10%)</td><td>31.54 <b>(-27.36%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.79 (n/a)</td><td>0.60 (n/a)</td><td>0.56 (n/a)</td><td>0.43 (n/a)</td><td>0.15 (n/a)</td><td>229.70 (n/a)</td><td>173.16 (n/a)</td><td>175.40 (n/a)</td><td>124.50 (n/a)</td><td>43.42 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.58 (+1.71%)</td><td>0.45 (-2.19%)</td><td>0.47 (+8.49%)</td><td>0.31 (-7.70%)</td><td>0.10 (-0.71%)</td><td>236.80 (+8.33%)</td><td>169.34 (+2.66%)</td><td>156.50 (-7.83%)</td><td>127.60 (-1.69%)</td><td>41.00 (+12.92%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.57 (n/a)</td><td>0.46 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>218.60 (n/a)</td><td>164.96 (n/a)</td><td>169.80 (n/a)</td><td>129.80 (n/a)</td><td>36.31 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.56 (-2.02%)</td><td>0.49 (+13.93%)</td><td>0.49 (+19.92%)</td><td>0.42 <b>(+34.23%)</b></td><td>0.05 <b>(-48.51%)</b></td><td>174.50 <b>(-25.49%)</b></td><td>150.92 (-15.28%)</td><td>149.00 (-16.62%)</td><td>131.60 (+2.09%)</td><td>16.50 <b>(-60.48%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.57 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>234.20 (n/a)</td><td>178.14 (n/a)</td><td>178.70 (n/a)</td><td>128.90 (n/a)</td><td>41.75 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.53 (-14.32%)</td><td>0.45 (-2.96%)</td><td>0.43 (-7.04%)</td><td>0.37 (+2.38%)</td><td>0.06 <b>(-40.56%)</b></td><td>200.90 (-2.29%)</td><td>168.12 (+0.76%)</td><td>171.00 (+7.61%)</td><td>138.90 (+16.72%)</td><td>23.33 <b>(-33.21%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.62 (n/a)</td><td>0.46 (n/a)</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.10 (n/a)</td><td>205.60 (n/a)</td><td>166.86 (n/a)</td><td>158.90 (n/a)</td><td>119.00 (n/a)</td><td>34.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.57 (+19.07%)</td><td>0.43 (-1.64%)</td><td>0.40 (-11.06%)</td><td>0.32 (-6.60%)</td><td>0.09 <b>(+66.47%)</b></td><td>229.30 (+7.10%)</td><td>179.98 (+3.89%)</td><td>184.10 (+12.46%)</td><td>129.20 (-16.05%)</td><td>37.44 <b>(+48.51%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>214.10 (n/a)</td><td>173.24 (n/a)</td><td>163.70 (n/a)</td><td>153.90 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 (-3.84%)</td><td>0.24 (+0.52%)</td><td>0.22 (-19.89%)</td><td>0.19 <b>(+46.19%)</b></td><td>0.04 <b>(-42.03%)</b></td><td>194.20 <b>(-31.57%)</b></td><td>160.62 (-8.01%)</td><td>167.30 <b>(+24.85%)</b></td><td>126.20 (+4.04%)</td><td>28.57 <b>(-58.74%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>283.80 (n/a)</td><td>174.60 (n/a)</td><td>134.00 (n/a)</td><td>121.30 (n/a)</td><td>69.23 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 (+1.00%)</td><td>0.22 (-5.87%)</td><td>0.25 (+5.38%)</td><td>0.12 <b>(-44.04%)</b></td><td>0.07 <b>(+136.96%)</b></td><td>308.40 <b>(+78.68%)</b></td><td>182.58 (+16.98%)</td><td>147.20 (-5.15%)</td><td>126.70 (-1.02%)</td><td>75.67 <b>(+319.47%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>172.60 (n/a)</td><td>156.08 (n/a)</td><td>155.20 (n/a)</td><td>128.00 (n/a)</td><td>18.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.31 (+6.00%)</td><td>0.25 (-4.15%)</td><td>0.28 (+3.91%)</td><td>0.17 <b>(-24.32%)</b></td><td>0.06 <b>(+123.32%)</b></td><td>216.20 <b>(+32.15%)</b></td><td>153.36 (+9.29%)</td><td>129.80 (-3.71%)</td><td>119.60 (-5.68%)</td><td>42.74 <b>(+174.13%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>163.60 (n/a)</td><td>140.32 (n/a)</td><td>134.80 (n/a)</td><td>126.80 (n/a)</td><td>15.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (-5.53%)</td><td>0.24 (-11.14%)</td><td>0.23 (-11.15%)</td><td>0.18 <b>(-25.95%)</b></td><td>0.04 <b>(+103.95%)</b></td><td>200.30 <b>(+35.06%)</b></td><td>159.44 (+14.99%)</td><td>160.80 (+12.53%)</td><td>130.40 (+5.84%)</td><td>29.08 <b>(+185.45%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>148.30 (n/a)</td><td>138.66 (n/a)</td><td>142.90 (n/a)</td><td>123.20 (n/a)</td><td>10.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (+17.45%)</td><td>0.21 (-2.61%)</td><td>0.22 (+4.82%)</td><td>0.16 (-19.53%)</td><td>0.05 <b>(+250.55%)</b></td><td>229.90 <b>(+24.27%)</b></td><td>183.60 (+6.52%)</td><td>167.20 (-4.62%)</td><td>133.80 (-14.83%)</td><td>40.38 <b>(+284.20%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>172.36 (n/a)</td><td>175.30 (n/a)</td><td>157.10 (n/a)</td><td>10.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (-10.64%)</td><td>0.20 (-12.90%)</td><td>0.19 (-16.86%)</td><td>0.16 (-16.65%)</td><td>0.02 <b>(+25.75%)</b></td><td>227.20 (+19.96%)</td><td>190.78 (+15.51%)</td><td>193.00 <b>(+20.25%)</b></td><td>169.00 (+11.92%)</td><td>23.84 <b>(+63.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>189.40 (n/a)</td><td>165.16 (n/a)</td><td>160.50 (n/a)</td><td>151.00 (n/a)</td><td>14.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.26 (-19.77%)</td><td>0.20 (-7.67%)</td><td>0.21 (-0.48%)</td><td>0.17 (+8.68%)</td><td>0.04 <b>(-41.20%)</b></td><td>218.70 (-7.99%)</td><td>185.08 (+4.61%)</td><td>176.80 (+0.51%)</td><td>140.10 <b>(+24.64%)</b></td><td>32.65 <b>(-29.10%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>237.70 (n/a)</td><td>176.92 (n/a)</td><td>175.90 (n/a)</td><td>112.40 (n/a)</td><td>46.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.31 (+8.26%)</td><td>0.22 (+3.82%)</td><td>0.19 (-7.04%)</td><td>0.18 <b>(+24.69%)</b></td><td>0.05 (-2.91%)</td><td>210.10 (-19.81%)</td><td>177.78 (-5.42%)</td><td>190.00 (+7.59%)</td><td>119.60 (-7.64%)</td><td>34.52 <b>(-31.85%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>262.00 (n/a)</td><td>187.96 (n/a)</td><td>176.60 (n/a)</td><td>129.50 (n/a)</td><td>50.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (-17.34%)</td><td>0.20 <b>(-24.23%)</b></td><td>0.21 (-18.41%)</td><td>0.11 <b>(-45.72%)</b></td><td>0.06 (+2.44%)</td><td>360.80 <b>(+84.18%)</b></td><td>220.40 <b>(+38.76%)</b></td><td>196.70 <b>(+22.55%)</b></td><td>147.50 <b>(+21.00%)</b></td><td>81.92 <b>(+144.55%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>195.90 (n/a)</td><td>158.84 (n/a)</td><td>160.50 (n/a)</td><td>121.90 (n/a)</td><td>33.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (+1.28%)</td><td>0.26 (+0.30%)</td><td>0.27 (-1.06%)</td><td>0.21 (-1.69%)</td><td>0.04 (+14.76%)</td><td>194.20 (+1.68%)</td><td>159.12 (+0.26%)</td><td>153.60 (+1.05%)</td><td>129.20 (-1.22%)</td><td>27.60 (+14.54%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>191.00 (n/a)</td><td>158.70 (n/a)</td><td>152.00 (n/a)</td><td>130.80 (n/a)</td><td>24.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (+6.45%)</td><td>0.28 (+1.54%)</td><td>0.30 (+2.73%)</td><td>0.23 (+13.01%)</td><td>0.04 (-1.66%)</td><td>178.20 (-11.48%)</td><td>148.50 (-1.97%)</td><td>135.30 (-2.66%)</td><td>126.40 (-6.09%)</td><td>22.90 (-18.73%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>201.30 (n/a)</td><td>151.48 (n/a)</td><td>139.00 (n/a)</td><td>134.60 (n/a)</td><td>28.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (-1.03%)</td><td>0.27 (-5.79%)</td><td>0.27 (-12.47%)</td><td>0.19 (+10.77%)</td><td>0.05 <b>(-24.52%)</b></td><td>212.40 (-9.73%)</td><td>156.78 (+3.42%)</td><td>149.70 (+14.27%)</td><td>129.90 (+1.01%)</td><td>32.64 <b>(-30.28%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>235.30 (n/a)</td><td>151.60 (n/a)</td><td>131.00 (n/a)</td><td>128.60 (n/a)</td><td>46.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.41 (+8.59%)</td><td>0.27 (+4.09%)</td><td>0.24 (-2.78%)</td><td>0.18 (+4.39%)</td><td>0.09 <b>(+20.01%)</b></td><td>229.80 (-4.21%)</td><td>164.60 (-2.29%)</td><td>173.50 (+2.85%)</td><td>99.80 (-7.93%)</td><td>49.98 (+4.71%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>239.90 (n/a)</td><td>168.46 (n/a)</td><td>168.70 (n/a)</td><td>108.40 (n/a)</td><td>47.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.37 <b>(+45.56%)</b></td><td>0.29 <b>(+44.25%)</b></td><td>0.30 <b>(+53.33%)</b></td><td>0.22 (+19.62%)</td><td>0.06 <b>(+94.48%)</b></td><td>188.20 (-16.39%)</td><td>143.74 <b>(-29.50%)</b></td><td>135.20 <b>(-34.78%)</b></td><td>111.30 <b>(-31.30%)</b></td><td>29.08 (+14.47%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>225.10 (n/a)</td><td>203.88 (n/a)</td><td>207.30 (n/a)</td><td>162.00 (n/a)</td><td>25.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.35 (+7.67%)</td><td>0.29 (+11.51%)</td><td>0.31 (+19.95%)</td><td>0.20 (-1.21%)</td><td>0.05 <b>(+26.44%)</b></td><td>200.90 (+1.21%)</td><td>147.70 (-9.28%)</td><td>134.30 (-16.64%)</td><td>118.20 (-7.15%)</td><td>32.12 <b>(+23.41%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>198.50 (n/a)</td><td>162.80 (n/a)</td><td>161.10 (n/a)</td><td>127.30 (n/a)</td><td>26.03 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.31 (-4.06%)</td><td>0.26 (+8.11%)</td><td>0.27 (+14.38%)</td><td>0.21 (+17.37%)</td><td>0.04 <b>(-30.45%)</b></td><td>196.00 (-14.82%)</td><td>157.30 (-9.39%)</td><td>149.70 (-12.56%)</td><td>133.10 (+4.23%)</td><td>23.79 <b>(-37.11%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>230.10 (n/a)</td><td>173.60 (n/a)</td><td>171.20 (n/a)</td><td>127.70 (n/a)</td><td>37.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 (-0.08%)</td><td>0.22 (-4.24%)</td><td>0.20 (-14.29%)</td><td>0.19 (+15.99%)</td><td>0.04 (-15.97%)</td><td>180.00 (-13.79%)</td><td>160.84 (+2.79%)</td><td>173.30 (+16.62%)</td><td>118.30 (+0.08%)</td><td>26.28 <b>(-27.55%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>208.80 (n/a)</td><td>156.48 (n/a)</td><td>148.60 (n/a)</td><td>118.20 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.31 (+15.22%)</td><td>0.21 (+0.79%)</td><td>0.23 (+18.76%)</td><td>0.10 <b>(-43.27%)</b></td><td>0.09 <b>(+103.70%)</b></td><td>346.50 <b>(+76.25%)</b></td><td>193.82 (+13.58%)</td><td>154.60 (-15.80%)</td><td>110.60 (-13.19%)</td><td>95.60 <b>(+211.41%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>196.60 (n/a)</td><td>170.64 (n/a)</td><td>183.60 (n/a)</td><td>127.40 (n/a)</td><td>30.70 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (+5.69%)</td><td>0.25 (+6.74%)</td><td>0.26 (+5.65%)</td><td>0.20 <b>(+42.21%)</b></td><td>0.04 <b>(-27.97%)</b></td><td>177.00 <b>(-29.68%)</b></td><td>144.52 (-9.97%)</td><td>133.80 (-5.31%)</td><td>123.70 (-5.43%)</td><td>23.78 <b>(-53.73%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>251.70 (n/a)</td><td>160.52 (n/a)</td><td>141.30 (n/a)</td><td>130.80 (n/a)</td><td>51.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (+1.77%)</td><td>0.24 (-2.78%)</td><td>0.25 (+2.73%)</td><td>0.17 (-16.94%)</td><td>0.04 <b>(+70.42%)</b></td><td>199.60 <b>(+20.46%)</b></td><td>149.62 (+4.78%)</td><td>139.00 (-2.66%)</td><td>127.90 (-1.69%)</td><td>29.12 <b>(+105.60%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>165.70 (n/a)</td><td>142.80 (n/a)</td><td>142.80 (n/a)</td><td>130.10 (n/a)</td><td>14.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (+9.29%)</td><td>0.24 (+1.70%)</td><td>0.26 (+10.06%)</td><td>0.17 (-14.96%)</td><td>0.04 <b>(+146.35%)</b></td><td>200.40 (+17.61%)</td><td>152.34 (+0.79%)</td><td>136.30 (-9.13%)</td><td>129.30 (-8.49%)</td><td>30.87 <b>(+160.50%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>170.40 (n/a)</td><td>151.14 (n/a)</td><td>150.00 (n/a)</td><td>141.30 (n/a)</td><td>11.85 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (+8.48%)</td><td>0.20 (+11.60%)</td><td>0.20 (+7.97%)</td><td>0.18 <b>(+30.71%)</b></td><td>0.02 <b>(-42.87%)</b></td><td>190.30 <b>(-23.51%)</b></td><td>175.02 (-11.89%)</td><td>175.20 (-7.40%)</td><td>154.90 (-7.85%)</td><td>13.73 <b>(-59.38%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>248.80 (n/a)</td><td>198.64 (n/a)</td><td>189.20 (n/a)</td><td>168.10 (n/a)</td><td>33.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.30 (+19.74%)</td><td>0.23 (+7.54%)</td><td>0.21 (+2.36%)</td><td>0.17 (+0.95%)</td><td>0.06 <b>(+97.61%)</b></td><td>207.90 (-0.95%)</td><td>162.44 (-3.39%)</td><td>163.70 (-2.33%)</td><td>117.00 (-16.43%)</td><td>41.94 <b>(+60.34%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>209.90 (n/a)</td><td>168.14 (n/a)</td><td>167.60 (n/a)</td><td>140.00 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (-11.56%)</td><td>0.23 (-3.84%)</td><td>0.24 (+19.77%)</td><td>0.15 (+3.92%)</td><td>0.07 <b>(-24.95%)</b></td><td>226.70 (-3.78%)</td><td>162.52 (+0.27%)</td><td>142.90 (-16.53%)</td><td>107.70 (+13.13%)</td><td>47.79 (-14.87%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.37 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>235.60 (n/a)</td><td>162.08 (n/a)</td><td>171.20 (n/a)</td><td>95.20 (n/a)</td><td>56.14 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.89 (-17.56%)</td><td>0.78 (-14.22%)</td><td>0.76 (-11.24%)</td><td>0.70 (-1.76%)</td><td>0.07 <b>(-57.56%)</b></td><td>188.20 (+1.78%)</td><td>170.12 (+14.13%)</td><td>172.30 (+12.69%)</td><td>147.10 <b>(+21.37%)</b></td><td>14.74 <b>(-46.62%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.08 (n/a)</td><td>0.90 (n/a)</td><td>0.86 (n/a)</td><td>0.71 (n/a)</td><td>0.17 (n/a)</td><td>184.90 (n/a)</td><td>149.06 (n/a)</td><td>152.90 (n/a)</td><td>121.20 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.14 (+4.31%)</td><td>0.88 (+1.43%)</td><td>0.90 (+6.14%)</td><td>0.61 (+0.80%)</td><td>0.19 (-9.26%)</td><td>214.90 (-0.83%)</td><td>155.34 (-2.28%)</td><td>145.30 (-5.77%)</td><td>115.40 (-4.15%)</td><td>36.80 (-8.79%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.09 (n/a)</td><td>0.87 (n/a)</td><td>0.85 (n/a)</td><td>0.60 (n/a)</td><td>0.21 (n/a)</td><td>216.70 (n/a)</td><td>158.96 (n/a)</td><td>154.20 (n/a)</td><td>120.40 (n/a)</td><td>40.34 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.93 (-12.79%)</td><td>0.78 (-4.85%)</td><td>0.78 (-14.63%)</td><td>0.64 <b>(+79.59%)</b></td><td>0.11 <b>(-60.57%)</b></td><td>204.30 <b>(-44.32%)</b></td><td>170.36 (-9.10%)</td><td>167.00 (+17.11%)</td><td>140.60 (+14.68%)</td><td>25.16 <b>(-75.49%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.07 (n/a)</td><td>0.82 (n/a)</td><td>0.92 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>366.90 (n/a)</td><td>187.42 (n/a)</td><td>142.60 (n/a)</td><td>122.60 (n/a)</td><td>102.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-14.67%)</td><td>0.02 (-11.15%)</td><td>0.02 (-0.13%)</td><td>0.02 (-5.86%)</td><td>0.00 <b>(-39.99%)</b></td><td>204.80 (+6.22%)</td><td>175.68 (+9.68%)</td><td>179.50 (+0.11%)</td><td>135.00 (+17.19%)</td><td>26.48 <b>(-27.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>160.18 (n/a)</td><td>179.30 (n/a)</td><td>115.20 (n/a)</td><td>36.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-12.28%)</td><td>0.02 (-9.84%)</td><td>0.02 (-5.13%)</td><td>0.02 (-15.37%)</td><td>0.00 (+6.13%)</td><td>212.70 (+18.17%)</td><td>175.20 (+11.52%)</td><td>171.10 (+5.36%)</td><td>151.50 (+14.00%)</td><td>25.76 <b>(+41.66%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.00 (n/a)</td><td>157.10 (n/a)</td><td>162.40 (n/a)</td><td>132.90 (n/a)</td><td>18.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-5.63%)</td><td>0.02 (-6.48%)</td><td>0.02 (-3.54%)</td><td>0.02 (-18.71%)</td><td>0.01 (+14.70%)</td><td>231.50 <b>(+23.01%)</b></td><td>176.32 (+8.58%)</td><td>178.70 (+3.65%)</td><td>136.50 (+5.98%)</td><td>39.72 <b>(+43.76%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.20 (n/a)</td><td>162.38 (n/a)</td><td>172.40 (n/a)</td><td>128.80 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.93 <b>(-22.78%)</b></td><td>12.23 (-16.02%)</td><td>13.10 (-6.87%)</td><td>8.38 <b>(-31.13%)</b></td><td>2.24 (-1.95%)</td><td>250.40 <b>(+45.16%)</b></td><td>177.58 <b>(+21.00%)</b></td><td>160.20 (+7.37%)</td><td>150.70 <b>(+29.58%)</b></td><td>41.41 <b>(+90.67%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>18.04 (n/a)</td><td>14.57 (n/a)</td><td>14.06 (n/a)</td><td>12.17 (n/a)</td><td>2.29 (n/a)</td><td>172.50 (n/a)</td><td>146.76 (n/a)</td><td>149.20 (n/a)</td><td>116.30 (n/a)</td><td>21.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.97 (-8.81%)</td><td>0.84 (+0.41%)</td><td>0.81 (+3.52%)</td><td>0.77 (+18.22%)</td><td>0.08 <b>(-53.12%)</b></td><td>170.70 (-15.41%)</td><td>159.00 (-2.85%)</td><td>163.50 (-3.37%)</td><td>136.00 (+9.68%)</td><td>13.63 <b>(-56.79%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.06 (n/a)</td><td>0.83 (n/a)</td><td>0.78 (n/a)</td><td>0.65 (n/a)</td><td>0.17 (n/a)</td><td>201.80 (n/a)</td><td>163.66 (n/a)</td><td>169.20 (n/a)</td><td>124.00 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.09 (+1.87%)</td><td>0.90 (-0.93%)</td><td>0.92 (-0.31%)</td><td>0.68 (-7.35%)</td><td>0.15 (-0.17%)</td><td>192.90 (+7.89%)</td><td>149.56 (+1.11%)</td><td>144.20 (+0.35%)</td><td>121.70 (-1.85%)</td><td>27.26 (+8.99%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.07 (n/a)</td><td>0.91 (n/a)</td><td>0.92 (n/a)</td><td>0.74 (n/a)</td><td>0.15 (n/a)</td><td>178.80 (n/a)</td><td>147.92 (n/a)</td><td>143.70 (n/a)</td><td>124.00 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.95 (-12.53%)</td><td>0.80 (+9.98%)</td><td>0.78 (+5.70%)</td><td>0.64 <b>(+86.77%)</b></td><td>0.13 <b>(-51.94%)</b></td><td>206.00 <b>(-46.45%)</b></td><td>169.40 (-19.55%)</td><td>168.40 (-5.39%)</td><td>139.70 (+14.32%)</td><td>27.73 <b>(-72.77%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.08 (n/a)</td><td>0.72 (n/a)</td><td>0.74 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>384.70 (n/a)</td><td>210.56 (n/a)</td><td>178.00 (n/a)</td><td>122.20 (n/a)</td><td>101.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.04 (-4.15%)</td><td>0.83 (-0.12%)</td><td>0.77 (-2.93%)</td><td>0.74 (+9.52%)</td><td>0.13 <b>(-22.40%)</b></td><td>179.40 (-8.66%)</td><td>161.62 (-1.08%)</td><td>171.10 (+3.01%)</td><td>127.40 (+4.26%)</td><td>22.05 <b>(-25.39%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.08 (n/a)</td><td>0.83 (n/a)</td><td>0.80 (n/a)</td><td>0.67 (n/a)</td><td>0.16 (n/a)</td><td>196.40 (n/a)</td><td>163.38 (n/a)</td><td>166.10 (n/a)</td><td>122.20 (n/a)</td><td>29.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.03 (-5.43%)</td><td>0.81 (-0.73%)</td><td>0.75 (+8.49%)</td><td>0.59 (+5.28%)</td><td>0.18 <b>(-28.85%)</b></td><td>225.30 (-5.02%)</td><td>169.40 (-2.61%)</td><td>175.10 (-7.84%)</td><td>127.80 (+5.71%)</td><td>38.37 <b>(-24.70%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.09 (n/a)</td><td>0.82 (n/a)</td><td>0.70 (n/a)</td><td>0.56 (n/a)</td><td>0.25 (n/a)</td><td>237.20 (n/a)</td><td>173.94 (n/a)</td><td>190.00 (n/a)</td><td>120.90 (n/a)</td><td>50.95 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (+10.51%)</td><td>0.03 <b>(+25.14%)</b></td><td>0.03 <b>(+27.76%)</b></td><td>0.02 <b>(+59.29%)</b></td><td>0.01 (-18.83%)</td><td>176.70 <b>(-37.23%)</b></td><td>145.84 <b>(-23.26%)</b></td><td>138.50 <b>(-21.75%)</b></td><td>116.40 (-9.49%)</td><td>26.53 <b>(-53.92%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>281.50 (n/a)</td><td>190.04 (n/a)</td><td>177.00 (n/a)</td><td>128.60 (n/a)</td><td>57.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (-1.61%)</td><td>0.02 (-10.41%)</td><td>0.02 (-13.55%)</td><td>0.02 (-10.81%)</td><td>0.00 (+3.80%)</td><td>233.60 (+12.15%)</td><td>181.74 (+12.16%)</td><td>180.30 (+15.65%)</td><td>142.60 (+1.64%)</td><td>33.38 (+19.80%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.30 (n/a)</td><td>162.04 (n/a)</td><td>155.90 (n/a)</td><td>140.30 (n/a)</td><td>27.86 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.00 (+4.65%)</td><td>0.00 (+0.47%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.44%)</td><td>0.00 <b>(+103.10%)</b></td><td>1011.98 (+0.65%)</td><td>957.96 (-1.01%)</td><td>955.36 (-0.65%)</td><td>904.46 (-4.35%)</td><td>38.34 <b>(+52.94%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1005.48 (n/a)</td><td>967.69 (n/a)</td><td>961.58 (n/a)</td><td>945.62 (n/a)</td><td>25.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.01 (+0.00%)</td><td>0.01 (-0.99%)</td><td>0.01 (+0.00%)</td><td>0.01 (-6.33%)</td><td>0.00 <b>(+79.28%)</b></td><td>1109.84 (+7.09%)</td><td>1029.68 (+1.71%)</td><td>1017.14 (+0.45%)</td><td>978.12 (+0.74%)</td><td>48.63 <b>(+84.05%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1036.40 (n/a)</td><td>1012.41 (n/a)</td><td>1012.55 (n/a)</td><td>970.95 (n/a)</td><td>26.42 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.00 (-2.25%)</td><td>0.97 (-0.61%)</td><td>0.96 (+0.05%)</td><td>0.95 (-0.88%)</td><td>0.02 <b>(-29.75%)</b></td><td>2212.87 (+0.88%)</td><td>2168.52 (+0.59%)</td><td>2176.37 (-0.05%)</td><td>2105.11 (+2.30%)</td><td>40.44 <b>(-27.39%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.02 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.03 (n/a)</td><td>2193.55 (n/a)</td><td>2155.83 (n/a)</td><td>2177.52 (n/a)</td><td>2057.87 (n/a)</td><td>55.70 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.82 (-3.25%)</td><td>4.75 (-12.33%)</td><td>4.67 (-14.37%)</td><td>3.90 (-18.49%)</td><td>0.70 <b>(+53.79%)</b></td><td>268.70 <b>(+22.69%)</b></td><td>224.66 (+15.32%)</td><td>224.60 (+16.80%)</td><td>180.10 (+3.33%)</td><td>31.75 <b>(+92.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.02 (n/a)</td><td>5.41 (n/a)</td><td>5.45 (n/a)</td><td>4.79 (n/a)</td><td>0.45 (n/a)</td><td>219.00 (n/a)</td><td>194.82 (n/a)</td><td>192.30 (n/a)</td><td>174.30 (n/a)</td><td>16.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.90 (-6.71%)</td><td>4.63 (+0.80%)</td><td>4.65 (-0.24%)</td><td>4.24 (+6.84%)</td><td>0.28 <b>(-53.49%)</b></td><td>247.00 (-6.40%)</td><td>227.02 (-1.84%)</td><td>225.50 (+0.22%)</td><td>214.20 (+7.21%)</td><td>13.77 <b>(-54.33%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.25 (n/a)</td><td>4.60 (n/a)</td><td>4.66 (n/a)</td><td>3.97 (n/a)</td><td>0.59 (n/a)</td><td>263.90 (n/a)</td><td>231.28 (n/a)</td><td>225.00 (n/a)</td><td>199.80 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.72 (+4.92%)</td><td>5.21 (+5.83%)</td><td>5.36 (+7.11%)</td><td>4.62 <b>(+20.86%)</b></td><td>0.43 <b>(-34.29%)</b></td><td>227.00 (-17.27%)</td><td>202.54 (-6.53%)</td><td>195.80 (-6.63%)</td><td>183.30 (-4.68%)</td><td>17.15 <b>(-48.72%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.45 (n/a)</td><td>4.92 (n/a)</td><td>5.00 (n/a)</td><td>3.82 (n/a)</td><td>0.65 (n/a)</td><td>274.40 (n/a)</td><td>216.70 (n/a)</td><td>209.70 (n/a)</td><td>192.30 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.83 (+13.49%)</td><td>5.10 (+14.12%)</td><td>5.18 <b>(+20.40%)</b></td><td>4.39 (+15.25%)</td><td>0.54 (+4.74%)</td><td>238.60 (-13.24%)</td><td>207.38 (-12.53%)</td><td>202.50 (-16.97%)</td><td>179.80 (-11.91%)</td><td>22.27 (-19.06%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.14 (n/a)</td><td>4.47 (n/a)</td><td>4.30 (n/a)</td><td>3.81 (n/a)</td><td>0.52 (n/a)</td><td>275.00 (n/a)</td><td>237.10 (n/a)</td><td>243.90 (n/a)</td><td>204.10 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.95 (+3.76%)</td><td>8.28 (+3.35%)</td><td>8.63 (+11.83%)</td><td>7.51 (+1.04%)</td><td>0.67 (+19.31%)</td><td>279.10 (-1.03%)</td><td>254.72 (-3.10%)</td><td>242.90 (-10.57%)</td><td>234.40 (-3.62%)</td><td>20.99 (+16.50%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.62 (n/a)</td><td>8.01 (n/a)</td><td>7.72 (n/a)</td><td>7.44 (n/a)</td><td>0.56 (n/a)</td><td>282.00 (n/a)</td><td>262.86 (n/a)</td><td>271.60 (n/a)</td><td>243.20 (n/a)</td><td>18.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.12 (+6.56%)</td><td>8.43 (+9.32%)</td><td>8.42 (+7.69%)</td><td>7.27 (+8.07%)</td><td>0.75 (-3.66%)</td><td>288.60 (-7.47%)</td><td>250.30 (-8.68%)</td><td>248.90 (-7.16%)</td><td>230.00 (-6.16%)</td><td>23.73 (-16.22%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.56 (n/a)</td><td>7.72 (n/a)</td><td>7.82 (n/a)</td><td>6.72 (n/a)</td><td>0.78 (n/a)</td><td>311.90 (n/a)</td><td>274.10 (n/a)</td><td>268.10 (n/a)</td><td>245.10 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.93 (+0.32%)</td><td>8.42 (+4.79%)</td><td>8.69 (+10.68%)</td><td>7.84 (+8.73%)</td><td>0.51 <b>(-34.60%)</b></td><td>267.30 (-8.05%)</td><td>249.90 (-5.00%)</td><td>241.20 (-9.66%)</td><td>234.90 (-0.34%)</td><td>15.27 <b>(-38.91%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.90 (n/a)</td><td>8.03 (n/a)</td><td>7.85 (n/a)</td><td>7.21 (n/a)</td><td>0.77 (n/a)</td><td>290.70 (n/a)</td><td>263.06 (n/a)</td><td>267.00 (n/a)</td><td>235.70 (n/a)</td><td>25.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.54 (-13.52%)</td><td>8.85 (+4.46%)</td><td>8.80 (+10.62%)</td><td>8.25 (+13.05%)</td><td>0.46 <b>(-69.79%)</b></td><td>254.20 (-11.55%)</td><td>237.48 (-6.21%)</td><td>238.30 (-9.60%)</td><td>219.80 (+15.68%)</td><td>12.25 <b>(-69.05%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>11.03 (n/a)</td><td>8.47 (n/a)</td><td>7.95 (n/a)</td><td>7.30 (n/a)</td><td>1.53 (n/a)</td><td>287.40 (n/a)</td><td>253.20 (n/a)</td><td>263.60 (n/a)</td><td>190.00 (n/a)</td><td>39.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>10.02 (-12.10%)</td><td>8.45 (-7.15%)</td><td>8.41 (-0.98%)</td><td>6.80 (-17.12%)</td><td>1.16 (-12.80%)</td><td>308.50 <b>(+20.65%)</b></td><td>252.18 (+7.80%)</td><td>249.20 (+0.97%)</td><td>209.30 (+13.81%)</td><td>36.11 <b>(+22.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>11.40 (n/a)</td><td>9.10 (n/a)</td><td>8.50 (n/a)</td><td>8.20 (n/a)</td><td>1.33 (n/a)</td><td>255.70 (n/a)</td><td>233.94 (n/a)</td><td>246.80 (n/a)</td><td>183.90 (n/a)</td><td>29.46 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>10.08 (-18.66%)</td><td>7.86 (-16.42%)</td><td>8.01 (-6.93%)</td><td>5.95 <b>(-22.01%)</b></td><td>1.57 <b>(-21.26%)</b></td><td>352.50 <b>(+28.23%)</b></td><td>275.52 (+19.53%)</td><td>261.70 (+7.43%)</td><td>208.10 <b>(+22.92%)</b></td><td>55.18 <b>(+24.47%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>12.39 (n/a)</td><td>9.40 (n/a)</td><td>8.61 (n/a)</td><td>7.63 (n/a)</td><td>1.99 (n/a)</td><td>274.90 (n/a)</td><td>230.50 (n/a)</td><td>243.60 (n/a)</td><td>169.30 (n/a)</td><td>44.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>12.48 (+12.90%)</td><td>10.69 (+0.57%)</td><td>10.14 (-4.27%)</td><td>9.85 (-2.80%)</td><td>1.08 <b>(+194.22%)</b></td><td>426.00 (+2.87%)</td><td>395.14 (+0.08%)</td><td>413.70 (+4.47%)</td><td>336.20 (-11.41%)</td><td>36.52 <b>(+166.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>11.05 (n/a)</td><td>10.63 (n/a)</td><td>10.59 (n/a)</td><td>10.13 (n/a)</td><td>0.37 (n/a)</td><td>414.10 (n/a)</td><td>394.82 (n/a)</td><td>396.00 (n/a)</td><td>379.50 (n/a)</td><td>13.70 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>12.84 (+2.46%)</td><td>11.56 (+1.16%)</td><td>12.09 (+8.45%)</td><td>9.72 (-9.44%)</td><td>1.32 <b>(+90.68%)</b></td><td>431.50 (+10.41%)</td><td>366.84 (-0.33%)</td><td>346.90 (-7.79%)</td><td>326.70 (-2.39%)</td><td>44.28 <b>(+106.90%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>12.53 (n/a)</td><td>11.43 (n/a)</td><td>11.15 (n/a)</td><td>10.73 (n/a)</td><td>0.69 (n/a)</td><td>390.80 (n/a)</td><td>368.04 (n/a)</td><td>376.20 (n/a)</td><td>334.70 (n/a)</td><td>21.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.09 (-6.31%)</td><td>12.01 (+2.15%)</td><td>11.80 (+5.92%)</td><td>11.35 (+7.60%)</td><td>0.70 <b>(-50.46%)</b></td><td>369.50 (-7.07%)</td><td>350.20 (-2.90%)</td><td>355.50 (-5.60%)</td><td>320.40 (+6.73%)</td><td>19.76 <b>(-50.93%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.97 (n/a)</td><td>11.76 (n/a)</td><td>11.14 (n/a)</td><td>10.55 (n/a)</td><td>1.42 (n/a)</td><td>397.60 (n/a)</td><td>360.66 (n/a)</td><td>376.60 (n/a)</td><td>300.20 (n/a)</td><td>40.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>14.30 (+8.19%)</td><td>13.35 (+11.02%)</td><td>13.05 (+3.38%)</td><td>12.66 <b>(+36.94%)</b></td><td>0.70 <b>(-56.09%)</b></td><td>331.30 <b>(-26.96%)</b></td><td>314.76 (-11.22%)</td><td>321.50 (-3.25%)</td><td>293.30 (-7.56%)</td><td>16.08 <b>(-71.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.22 (n/a)</td><td>12.03 (n/a)</td><td>12.62 (n/a)</td><td>9.25 (n/a)</td><td>1.58 (n/a)</td><td>453.60 (n/a)</td><td>354.54 (n/a)</td><td>332.30 (n/a)</td><td>317.30 (n/a)</td><td>55.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>15.07 (+10.97%)</td><td>13.63 (+7.49%)</td><td>14.33 (+14.73%)</td><td>11.30 (-3.18%)</td><td>1.61 <b>(+100.17%)</b></td><td>371.30 (+3.28%)</td><td>311.42 (-6.13%)</td><td>292.80 (-12.83%)</td><td>278.30 (-9.88%)</td><td>39.55 <b>(+86.89%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.58 (n/a)</td><td>12.68 (n/a)</td><td>12.49 (n/a)</td><td>11.67 (n/a)</td><td>0.81 (n/a)</td><td>359.50 (n/a)</td><td>331.76 (n/a)</td><td>335.90 (n/a)</td><td>308.80 (n/a)</td><td>21.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>14.44 (-0.76%)</td><td>13.12 (+5.98%)</td><td>13.21 (+2.33%)</td><td>11.30 (+16.01%)</td><td>1.20 <b>(-37.50%)</b></td><td>371.30 (-13.79%)</td><td>321.94 (-6.91%)</td><td>317.40 (-2.28%)</td><td>290.50 (+0.76%)</td><td>31.02 <b>(-45.64%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>14.55 (n/a)</td><td>12.38 (n/a)</td><td>12.91 (n/a)</td><td>9.74 (n/a)</td><td>1.91 (n/a)</td><td>430.70 (n/a)</td><td>345.82 (n/a)</td><td>324.80 (n/a)</td><td>288.30 (n/a)</td><td>57.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>14.75 (+8.32%)</td><td>13.67 (+12.31%)</td><td>13.85 (+9.57%)</td><td>12.35 <b>(+33.05%)</b></td><td>0.87 <b>(-48.72%)</b></td><td>339.60 <b>(-24.83%)</b></td><td>307.90 (-12.28%)</td><td>302.90 (-8.74%)</td><td>284.40 (-7.66%)</td><td>20.10 <b>(-65.15%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.62 (n/a)</td><td>12.17 (n/a)</td><td>12.64 (n/a)</td><td>9.28 (n/a)</td><td>1.69 (n/a)</td><td>451.80 (n/a)</td><td>351.00 (n/a)</td><td>331.90 (n/a)</td><td>308.00 (n/a)</td><td>57.68 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>14.68 (+0.99%)</td><td>13.15 (+2.78%)</td><td>12.95 (+0.67%)</td><td>12.10 <b>(+23.06%)</b></td><td>0.97 <b>(-48.34%)</b></td><td>346.80 (-18.73%)</td><td>320.38 (-4.20%)</td><td>323.80 (-0.67%)</td><td>285.80 (-0.97%)</td><td>22.85 <b>(-58.96%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>14.53 (n/a)</td><td>12.79 (n/a)</td><td>12.86 (n/a)</td><td>9.83 (n/a)</td><td>1.89 (n/a)</td><td>426.70 (n/a)</td><td>334.42 (n/a)</td><td>326.00 (n/a)</td><td>288.60 (n/a)</td><td>55.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.08 (-7.21%)</td><td>2.76 (-9.67%)</td><td>2.66 (-14.36%)</td><td>2.54 (-8.37%)</td><td>0.21 (-0.67%)</td><td>206.10 (+9.11%)</td><td>191.02 (+10.76%)</td><td>196.90 (+16.79%)</td><td>170.00 (+7.80%)</td><td>13.92 (+15.22%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.32 (n/a)</td><td>3.05 (n/a)</td><td>3.11 (n/a)</td><td>2.78 (n/a)</td><td>0.21 (n/a)</td><td>188.90 (n/a)</td><td>172.46 (n/a)</td><td>168.60 (n/a)</td><td>157.70 (n/a)</td><td>12.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.58 (-8.77%)</td><td>5.18 (+4.86%)</td><td>5.05 (+5.29%)</td><td>4.91 (+15.35%)</td><td>0.29 <b>(-59.86%)</b></td><td>213.70 (-13.31%)</td><td>202.80 (-5.88%)</td><td>207.50 (-5.03%)</td><td>188.00 (+9.62%)</td><td>11.05 <b>(-61.34%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.12 (n/a)</td><td>4.94 (n/a)</td><td>4.80 (n/a)</td><td>4.25 (n/a)</td><td>0.72 (n/a)</td><td>246.50 (n/a)</td><td>215.46 (n/a)</td><td>218.50 (n/a)</td><td>171.50 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.10 (+6.08%)</td><td>8.08 (+1.05%)</td><td>8.01 (+1.05%)</td><td>7.20 (-3.36%)</td><td>0.74 <b>(+74.53%)</b></td><td>291.20 (+3.45%)</td><td>261.28 (-0.62%)</td><td>261.80 (-1.06%)</td><td>230.40 (-5.77%)</td><td>23.50 <b>(+70.34%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.58 (n/a)</td><td>7.99 (n/a)</td><td>7.93 (n/a)</td><td>7.45 (n/a)</td><td>0.42 (n/a)</td><td>281.50 (n/a)</td><td>262.92 (n/a)</td><td>264.60 (n/a)</td><td>244.50 (n/a)</td><td>13.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.52 (-2.35%)</td><td>3.11 (-0.71%)</td><td>3.23 (+2.62%)</td><td>2.62 (+9.14%)</td><td>0.41 (-9.72%)</td><td>200.10 (-8.38%)</td><td>171.24 (+0.25%)</td><td>162.10 (-2.58%)</td><td>149.00 (+2.41%)</td><td>23.40 (-17.10%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.60 (n/a)</td><td>3.13 (n/a)</td><td>3.15 (n/a)</td><td>2.40 (n/a)</td><td>0.45 (n/a)</td><td>218.40 (n/a)</td><td>170.82 (n/a)</td><td>166.40 (n/a)</td><td>145.50 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 <b>(-27.14%)</b></td><td>0.17 <b>(-24.06%)</b></td><td>0.17 <b>(-33.03%)</b></td><td>0.15 (-6.11%)</td><td>0.02 <b>(-56.81%)</b></td><td>225.60 (+6.52%)</td><td>190.24 <b>(+26.32%)</b></td><td>189.40 <b>(+49.37%)</b></td><td>155.00 <b>(+37.17%)</b></td><td>26.53 <b>(-37.30%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>211.80 (n/a)</td><td>150.60 (n/a)</td><td>126.80 (n/a)</td><td>113.00 (n/a)</td><td>42.31 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.23 (+1.79%)</td><td>0.18 (-4.52%)</td><td>0.20 (+12.89%)</td><td>0.13 <b>(-22.84%)</b></td><td>0.05 <b>(+55.97%)</b></td><td>261.00 <b>(+29.59%)</b></td><td>189.76 (+8.62%)</td><td>166.20 (-11.41%)</td><td>139.90 (-1.76%)</td><td>50.98 <b>(+102.69%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>201.40 (n/a)</td><td>174.70 (n/a)</td><td>187.60 (n/a)</td><td>142.40 (n/a)</td><td>25.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.50 (-7.25%)</td><td>0.40 (-3.20%)</td><td>0.36 (-4.16%)</td><td>0.33 (+16.61%)</td><td>0.08 <b>(-26.70%)</b></td><td>200.10 (-14.23%)</td><td>169.26 (+0.61%)</td><td>180.60 (+4.33%)</td><td>130.00 (+7.79%)</td><td>31.01 <b>(-30.77%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.11 (n/a)</td><td>233.30 (n/a)</td><td>168.24 (n/a)</td><td>173.10 (n/a)</td><td>120.60 (n/a)</td><td>44.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.40 <b>(-20.24%)</b></td><td>0.34 (-13.14%)</td><td>0.33 (-14.28%)</td><td>0.26 (-6.50%)</td><td>0.06 <b>(-37.86%)</b></td><td>256.80 (+6.96%)</td><td>198.10 (+12.53%)</td><td>195.90 (+16.68%)</td><td>165.80 <b>(+25.32%)</b></td><td>36.86 (-16.65%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.09 (n/a)</td><td>240.10 (n/a)</td><td>176.04 (n/a)</td><td>167.90 (n/a)</td><td>132.30 (n/a)</td><td>44.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.58 <b>(+28.21%)</b></td><td>0.39 (-4.95%)</td><td>0.29 <b>(-28.72%)</b></td><td>0.27 <b>(-23.37%)</b></td><td>0.15 <b>(+336.69%)</b></td><td>238.90 <b>(+30.48%)</b></td><td>189.14 (+16.58%)</td><td>228.00 <b>(+40.31%)</b></td><td>113.00 <b>(-22.02%)</b></td><td>63.29 <b>(+356.25%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.45 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.03 (n/a)</td><td>183.10 (n/a)</td><td>162.24 (n/a)</td><td>162.50 (n/a)</td><td>144.90 (n/a)</td><td>13.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.49 <b>(+46.10%)</b></td><td>0.94 (+10.92%)</td><td>0.84 (-0.03%)</td><td>0.70 (-0.92%)</td><td>0.31 <b>(+135.76%)</b></td><td>188.30 (+0.91%)</td><td>149.04 (-5.41%)</td><td>156.60 (+0.00%)</td><td>87.90 <b>(-31.54%)</b></td><td>37.12 <b>(+51.47%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.02 (n/a)</td><td>0.85 (n/a)</td><td>0.84 (n/a)</td><td>0.70 (n/a)</td><td>0.13 (n/a)</td><td>186.60 (n/a)</td><td>157.56 (n/a)</td><td>156.60 (n/a)</td><td>128.40 (n/a)</td><td>24.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.33 <b>(+21.64%)</b></td><td>0.88 (+1.95%)</td><td>0.72 (-14.35%)</td><td>0.59 (-17.00%)</td><td>0.34 <b>(+129.05%)</b></td><td>222.10 <b>(+20.44%)</b></td><td>165.94 (+7.10%)</td><td>181.60 (+16.78%)</td><td>98.50 (-17.78%)</td><td>56.80 <b>(+130.77%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.09 (n/a)</td><td>0.86 (n/a)</td><td>0.84 (n/a)</td><td>0.71 (n/a)</td><td>0.15 (n/a)</td><td>184.40 (n/a)</td><td>154.94 (n/a)</td><td>155.50 (n/a)</td><td>119.80 (n/a)</td><td>24.62 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.37 <b>(+41.31%)</b></td><td>0.78 (-8.74%)</td><td>0.75 (-8.08%)</td><td>0.42 <b>(-47.69%)</b></td><td>0.36 <b>(+371.90%)</b></td><td>314.70 <b>(+91.19%)</b></td><td>195.68 <b>(+26.69%)</b></td><td>175.70 (+8.79%)</td><td>95.50 <b>(-29.21%)</b></td><td>80.61 <b>(+516.42%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.97 (n/a)</td><td>0.85 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.08 (n/a)</td><td>164.60 (n/a)</td><td>154.46 (n/a)</td><td>161.50 (n/a)</td><td>134.90 (n/a)</td><td>13.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.71 <b>(-28.55%)</b></td><td>0.61 <b>(-26.22%)</b></td><td>0.63 <b>(-23.90%)</b></td><td>0.50 <b>(-26.74%)</b></td><td>0.09 <b>(-30.57%)</b></td><td>262.60 <b>(+36.49%)</b></td><td>218.96 <b>(+35.34%)</b></td><td>208.40 <b>(+31.40%)</b></td><td>184.10 <b>(+40.00%)</b></td><td>33.46 <b>(+32.24%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.00 (n/a)</td><td>0.83 (n/a)</td><td>0.83 (n/a)</td><td>0.68 (n/a)</td><td>0.13 (n/a)</td><td>192.40 (n/a)</td><td>161.78 (n/a)</td><td>158.60 (n/a)</td><td>131.50 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (+6.11%)</td><td>0.10 (+14.92%)</td><td>0.10 (+4.81%)</td><td>0.10 <b>(+40.91%)</b></td><td>0.01 <b>(-66.92%)</b></td><td>164.60 <b>(-29.05%)</b></td><td>157.56 (-15.50%)</td><td>162.00 (-4.59%)</td><td>145.00 (-5.72%)</td><td>8.42 <b>(-77.80%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.00 (n/a)</td><td>186.46 (n/a)</td><td>169.80 (n/a)</td><td>153.80 (n/a)</td><td>37.94 (n/a)</td>
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
