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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (+5.40%)</td><td>0.04 (-10.31%)</td><td>0.03 <b>(-20.54%)</b></td><td>0.03 (-18.95%)</td><td>0.01 <b>(+86.62%)</b></td><td>228.30 <b>(+23.41%)</b></td><td>179.22 (+16.71%)</td><td>197.60 <b>(+25.78%)</b></td><td>124.20 (-5.19%)</td><td>47.03 <b>(+117.35%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>153.56 (n/a)</td><td>157.10 (n/a)</td><td>131.00 (n/a)</td><td>21.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(-20.39%)</b></td><td>0.03 <b>(-26.03%)</b></td><td>0.03 <b>(-26.22%)</b></td><td>0.03 <b>(-32.43%)</b></td><td>0.01 <b>(+20.91%)</b></td><td>228.40 <b>(+48.02%)</b></td><td>185.06 <b>(+37.02%)</b></td><td>185.40 <b>(+35.53%)</b></td><td>148.00 <b>(+25.64%)</b></td><td>30.19 <b>(+124.70%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>154.30 (n/a)</td><td>135.06 (n/a)</td><td>136.80 (n/a)</td><td>117.80 (n/a)</td><td>13.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (+2.91%)</td><td>0.04 (+2.74%)</td><td>0.04 (+12.14%)</td><td>0.03 (+5.50%)</td><td>0.01 (-6.08%)</td><td>200.20 (-5.21%)</td><td>167.64 (-3.27%)</td><td>165.20 (-10.85%)</td><td>124.30 (-2.89%)</td><td>29.72 (-13.04%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>173.30 (n/a)</td><td>185.30 (n/a)</td><td>128.00 (n/a)</td><td>34.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (-0.39%)</td><td>0.04 (-0.55%)</td><td>0.04 (+5.34%)</td><td>0.03 (-13.38%)</td><td>0.01 <b>(+67.35%)</b></td><td>190.80 (+15.43%)</td><td>154.54 (+3.16%)</td><td>144.00 (-5.08%)</td><td>123.80 (+0.41%)</td><td>33.70 <b>(+94.74%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>165.30 (n/a)</td><td>149.80 (n/a)</td><td>151.70 (n/a)</td><td>123.30 (n/a)</td><td>17.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (-11.39%)</td><td>0.04 (-1.10%)</td><td>0.04 (+7.90%)</td><td>0.03 (+7.10%)</td><td>0.00 <b>(-44.86%)</b></td><td>196.80 (-6.64%)</td><td>169.72 (-0.82%)</td><td>166.70 (-7.34%)</td><td>147.80 (+12.82%)</td><td>18.68 <b>(-40.85%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>171.12 (n/a)</td><td>179.90 (n/a)</td><td>131.00 (n/a)</td><td>31.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (-12.53%)</td><td>0.04 (-1.52%)</td><td>0.03 (+18.60%)</td><td>0.03 (-3.18%)</td><td>0.01 <b>(-41.91%)</b></td><td>223.30 (+3.28%)</td><td>177.28 (-1.58%)</td><td>176.00 (-15.67%)</td><td>150.00 (+14.33%)</td><td>29.69 <b>(-31.59%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>180.12 (n/a)</td><td>208.70 (n/a)</td><td>131.20 (n/a)</td><td>43.39 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (-19.44%)</td><td>0.03 (-6.15%)</td><td>0.03 (-3.60%)</td><td>0.03 (+12.44%)</td><td>0.00 <b>(-63.79%)</b></td><td>210.10 (-11.09%)</td><td>181.22 (+2.73%)</td><td>179.10 (+3.77%)</td><td>165.80 <b>(+24.10%)</b></td><td>17.12 <b>(-58.89%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>176.40 (n/a)</td><td>172.60 (n/a)</td><td>133.60 (n/a)</td><td>41.63 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (+7.73%)</td><td>0.03 (-7.66%)</td><td>0.03 (-18.41%)</td><td>0.02 (-12.16%)</td><td>0.01 <b>(+88.36%)</b></td><td>252.70 (+13.83%)</td><td>204.02 (+11.39%)</td><td>213.80 <b>(+22.59%)</b></td><td>154.40 (-7.21%)</td><td>43.89 <b>(+93.32%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>222.00 (n/a)</td><td>183.16 (n/a)</td><td>174.40 (n/a)</td><td>166.40 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (+6.20%)</td><td>0.08 (+15.90%)</td><td>0.09 (+17.87%)</td><td>0.06 (+12.37%)</td><td>0.01 (-12.95%)</td><td>202.80 (-11.01%)</td><td>151.94 (-15.02%)</td><td>143.40 (-15.15%)</td><td>120.70 (-5.78%)</td><td>30.49 <b>(-26.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>227.90 (n/a)</td><td>178.80 (n/a)</td><td>169.00 (n/a)</td><td>128.10 (n/a)</td><td>41.20 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (+8.25%)</td><td>0.08 (+2.71%)</td><td>0.10 (+14.66%)</td><td>0.05 <b>(-21.18%)</b></td><td>0.02 <b>(+110.97%)</b></td><td>233.20 <b>(+26.88%)</b></td><td>156.28 (+2.47%)</td><td>126.60 (-12.81%)</td><td>122.90 (-7.66%)</td><td>48.33 <b>(+137.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.80 (n/a)</td><td>152.52 (n/a)</td><td>145.20 (n/a)</td><td>133.10 (n/a)</td><td>20.34 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 <b>(+26.63%)</b></td><td>0.07 (+14.69%)</td><td>0.07 (+1.68%)</td><td>0.07 <b>(+25.73%)</b></td><td>0.01 <b>(+26.32%)</b></td><td>188.20 <b>(-20.49%)</b></td><td>171.80 (-12.90%)</td><td>182.00 (-1.67%)</td><td>124.70 <b>(-21.03%)</b></td><td>26.70 <b>(-24.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.70 (n/a)</td><td>197.24 (n/a)</td><td>185.10 (n/a)</td><td>157.90 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (-5.33%)</td><td>0.07 (-5.13%)</td><td>0.07 (+1.83%)</td><td>0.05 (-9.22%)</td><td>0.01 (-12.17%)</td><td>236.70 (+10.14%)</td><td>175.12 (+5.10%)</td><td>164.70 (-1.79%)</td><td>133.40 (+5.62%)</td><td>38.05 (+6.15%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>214.90 (n/a)</td><td>166.62 (n/a)</td><td>167.70 (n/a)</td><td>126.30 (n/a)</td><td>35.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (-6.88%)</td><td>0.07 (-6.67%)</td><td>0.07 (+11.67%)</td><td>0.04 (-14.88%)</td><td>0.02 (-2.52%)</td><td>274.70 (+17.49%)</td><td>199.38 (+8.29%)</td><td>176.40 (-10.46%)</td><td>149.80 (+7.46%)</td><td>53.39 <b>(+28.49%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.80 (n/a)</td><td>184.12 (n/a)</td><td>197.00 (n/a)</td><td>139.40 (n/a)</td><td>41.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (-15.54%)</td><td>0.07 (-8.48%)</td><td>0.06 (-4.65%)</td><td>0.06 (-0.88%)</td><td>0.01 <b>(-38.21%)</b></td><td>218.20 (+0.88%)</td><td>189.74 (+7.34%)</td><td>192.00 (+4.92%)</td><td>151.90 (+18.39%)</td><td>25.32 <b>(-26.18%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>216.30 (n/a)</td><td>176.76 (n/a)</td><td>183.00 (n/a)</td><td>128.30 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (-4.04%)</td><td>0.06 (-15.86%)</td><td>0.06 <b>(-23.74%)</b></td><td>0.05 (+12.80%)</td><td>0.01 (-16.26%)</td><td>245.80 (-11.36%)</td><td>208.54 (+16.11%)</td><td>215.40 <b>(+31.10%)</b></td><td>141.80 (+4.19%)</td><td>42.08 <b>(-25.95%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>277.30 (n/a)</td><td>179.60 (n/a)</td><td>164.30 (n/a)</td><td>136.10 (n/a)</td><td>56.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (+0.55%)</td><td>0.06 (+2.35%)</td><td>0.06 (-3.56%)</td><td>0.06 <b>(+26.01%)</b></td><td>0.01 <b>(-30.79%)</b></td><td>221.40 <b>(-20.65%)</b></td><td>199.74 (-4.80%)</td><td>214.40 (+3.73%)</td><td>156.40 (-0.57%)</td><td>26.87 <b>(-45.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>279.00 (n/a)</td><td>209.82 (n/a)</td><td>206.70 (n/a)</td><td>157.30 (n/a)</td><td>48.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (+4.46%)</td><td>0.16 (+1.15%)</td><td>0.17 (+11.90%)</td><td>0.11 (-10.19%)</td><td>0.04 <b>(+33.02%)</b></td><td>233.40 (+11.35%)</td><td>167.26 (+1.73%)</td><td>143.70 (-10.63%)</td><td>124.50 (-4.30%)</td><td>47.92 <b>(+43.70%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>209.60 (n/a)</td><td>164.42 (n/a)</td><td>160.80 (n/a)</td><td>130.10 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (-17.75%)</td><td>0.14 (-3.89%)</td><td>0.14 (-3.25%)</td><td>0.12 <b>(+32.54%)</b></td><td>0.02 <b>(-61.38%)</b></td><td>203.30 <b>(-24.56%)</b></td><td>175.46 (-1.93%)</td><td>173.90 (+3.39%)</td><td>149.80 <b>(+21.59%)</b></td><td>19.36 <b>(-65.43%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>269.50 (n/a)</td><td>178.92 (n/a)</td><td>168.20 (n/a)</td><td>123.20 (n/a)</td><td>56.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (-17.69%)</td><td>0.14 (-8.84%)</td><td>0.15 (+1.04%)</td><td>0.12 (+8.83%)</td><td>0.01 <b>(-53.91%)</b></td><td>197.20 (-8.11%)</td><td>174.14 (+6.90%)</td><td>164.30 (-1.02%)</td><td>158.20 <b>(+21.51%)</b></td><td>18.40 <b>(-46.88%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.60 (n/a)</td><td>162.90 (n/a)</td><td>166.00 (n/a)</td><td>130.20 (n/a)</td><td>34.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (+6.62%)</td><td>0.14 (-3.35%)</td><td>0.14 (-5.96%)</td><td>0.10 <b>(-21.97%)</b></td><td>0.03 <b>(+91.40%)</b></td><td>235.50 <b>(+28.20%)</b></td><td>176.18 (+6.43%)</td><td>180.10 (+6.32%)</td><td>133.70 (-6.18%)</td><td>38.74 <b>(+131.05%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>183.70 (n/a)</td><td>165.54 (n/a)</td><td>169.40 (n/a)</td><td>142.50 (n/a)</td><td>16.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (+2.68%)</td><td>0.15 (+1.77%)</td><td>0.15 (+5.72%)</td><td>0.09 <b>(-21.59%)</b></td><td>0.03 <b>(+51.01%)</b></td><td>276.90 <b>(+27.54%)</b></td><td>178.60 (+2.16%)</td><td>163.50 (-5.38%)</td><td>142.20 (-2.60%)</td><td>56.02 <b>(+94.82%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.10 (n/a)</td><td>174.82 (n/a)</td><td>172.80 (n/a)</td><td>146.00 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (-8.81%)</td><td>0.13 (+1.37%)</td><td>0.14 (+9.38%)</td><td>0.11 (+5.61%)</td><td>0.01 <b>(-31.79%)</b></td><td>217.40 (-5.27%)</td><td>186.30 (-2.15%)</td><td>175.10 (-8.56%)</td><td>171.70 (+9.71%)</td><td>19.19 <b>(-29.15%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>229.50 (n/a)</td><td>190.40 (n/a)</td><td>191.50 (n/a)</td><td>156.50 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (-18.01%)</td><td>0.14 (-3.80%)</td><td>0.15 (+6.92%)</td><td>0.13 (+2.77%)</td><td>0.01 <b>(-64.75%)</b></td><td>189.80 (-2.72%)</td><td>170.98 (+2.13%)</td><td>168.90 (-6.48%)</td><td>162.30 <b>(+21.94%)</b></td><td>11.02 <b>(-57.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>167.42 (n/a)</td><td>180.60 (n/a)</td><td>133.10 (n/a)</td><td>26.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (+2.12%)</td><td>0.13 (-5.30%)</td><td>0.12 (-13.22%)</td><td>0.11 (+7.35%)</td><td>0.02 (-3.28%)</td><td>217.10 (-6.86%)</td><td>190.60 (+5.27%)</td><td>196.70 (+15.23%)</td><td>159.90 (-2.08%)</td><td>25.18 (-13.92%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>233.10 (n/a)</td><td>181.06 (n/a)</td><td>170.70 (n/a)</td><td>163.30 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.38 (+12.89%)</td><td>0.33 <b>(+22.61%)</b></td><td>0.32 (+14.55%)</td><td>0.27 <b>(+35.26%)</b></td><td>0.04 (-14.27%)</td><td>181.10 <b>(-26.05%)</b></td><td>148.96 (-19.77%)</td><td>151.50 (-12.73%)</td><td>128.80 (-11.42%)</td><td>20.92 <b>(-45.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>244.90 (n/a)</td><td>185.66 (n/a)</td><td>173.60 (n/a)</td><td>145.40 (n/a)</td><td>38.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (-10.02%)</td><td>0.29 (-7.26%)</td><td>0.30 (-5.90%)</td><td>0.24 (-7.00%)</td><td>0.04 <b>(-32.52%)</b></td><td>207.90 (+7.55%)</td><td>171.14 (+6.64%)</td><td>164.90 (+6.25%)</td><td>144.90 (+11.20%)</td><td>23.08 (-18.78%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>193.30 (n/a)</td><td>160.48 (n/a)</td><td>155.20 (n/a)</td><td>130.30 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (-9.21%)</td><td>0.30 (-3.50%)</td><td>0.28 (-4.79%)</td><td>0.28 (+6.70%)</td><td>0.03 <b>(-35.36%)</b></td><td>174.30 (-6.29%)</td><td>162.92 (+2.67%)</td><td>173.60 (+5.02%)</td><td>145.30 (+10.16%)</td><td>15.23 <b>(-32.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>186.00 (n/a)</td><td>158.68 (n/a)</td><td>165.30 (n/a)</td><td>131.90 (n/a)</td><td>22.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.42 (+14.80%)</td><td>0.29 (-4.51%)</td><td>0.27 (-5.59%)</td><td>0.23 (+0.42%)</td><td>0.08 <b>(+39.22%)</b></td><td>211.00 (-0.42%)</td><td>175.96 (+6.78%)</td><td>180.40 (+5.93%)</td><td>116.10 (-12.84%)</td><td>38.82 <b>(+22.80%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>211.90 (n/a)</td><td>164.78 (n/a)</td><td>170.30 (n/a)</td><td>133.20 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.35 (+8.06%)</td><td>0.28 (-1.39%)</td><td>0.28 (-1.25%)</td><td>0.19 <b>(-20.12%)</b></td><td>0.06 <b>(+103.38%)</b></td><td>262.80 <b>(+25.14%)</b></td><td>186.28 (+5.21%)</td><td>175.20 (+1.27%)</td><td>142.00 (-7.49%)</td><td>48.01 <b>(+133.22%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>210.00 (n/a)</td><td>177.06 (n/a)</td><td>173.00 (n/a)</td><td>153.50 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 <b>(-25.07%)</b></td><td>0.24 (-19.11%)</td><td>0.27 (-6.10%)</td><td>0.16 <b>(-33.26%)</b></td><td>0.05 (-3.47%)</td><td>300.30 <b>(+49.85%)</b></td><td>211.94 <b>(+26.00%)</b></td><td>184.80 (+6.51%)</td><td>174.50 <b>(+33.41%)</b></td><td>52.37 <b>(+97.22%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>200.40 (n/a)</td><td>168.20 (n/a)</td><td>173.50 (n/a)</td><td>130.80 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 <b>(-24.28%)</b></td><td>0.27 (-8.87%)</td><td>0.29 (-2.19%)</td><td>0.21 (+13.91%)</td><td>0.04 <b>(-47.71%)</b></td><td>238.10 (-12.21%)</td><td>187.32 (+4.91%)</td><td>167.50 (+2.20%)</td><td>163.80 <b>(+32.10%)</b></td><td>31.93 <b>(-42.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>271.20 (n/a)</td><td>178.56 (n/a)</td><td>163.90 (n/a)</td><td>124.00 (n/a)</td><td>55.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (+13.29%)</td><td>0.27 (+7.28%)</td><td>0.24 (-8.72%)</td><td>0.20 (+12.10%)</td><td>0.06 (+19.44%)</td><td>241.70 (-10.81%)</td><td>192.08 (-6.51%)</td><td>206.00 (+9.57%)</td><td>144.70 (-11.71%)</td><td>39.32 (-8.69%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>271.00 (n/a)</td><td>205.46 (n/a)</td><td>188.00 (n/a)</td><td>163.90 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 <b>(+29.78%)</b></td><td>0.02 <b>(+20.49%)</b></td><td>0.02 (+19.19%)</td><td>0.01 <b>(+25.90%)</b></td><td>0.00 <b>(+38.94%)</b></td><td>197.30 <b>(-20.57%)</b></td><td>162.70 (-16.71%)</td><td>157.50 (-16.09%)</td><td>122.20 <b>(-22.95%)</b></td><td>28.34 (-16.97%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>248.40 (n/a)</td><td>195.34 (n/a)</td><td>187.70 (n/a)</td><td>158.60 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 <b>(-29.54%)</b></td><td>0.02 (+0.31%)</td><td>0.01 (+4.19%)</td><td>0.01 <b>(+34.08%)</b></td><td>0.00 <b>(-65.47%)</b></td><td>207.20 <b>(-25.44%)</b></td><td>176.36 (-8.56%)</td><td>182.80 (-3.99%)</td><td>148.10 <b>(+41.99%)</b></td><td>23.71 <b>(-61.73%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>277.90 (n/a)</td><td>192.86 (n/a)</td><td>190.40 (n/a)</td><td>104.30 (n/a)</td><td>61.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (-14.21%)</td><td>0.01 (+2.74%)</td><td>0.01 (+6.80%)</td><td>0.01 (-2.84%)</td><td>0.00 <b>(-32.62%)</b></td><td>234.30 (+2.94%)</td><td>180.72 (-4.63%)</td><td>180.40 (-6.38%)</td><td>141.90 (+16.60%)</td><td>34.71 (-14.83%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>227.60 (n/a)</td><td>189.50 (n/a)</td><td>192.70 (n/a)</td><td>121.70 (n/a)</td><td>40.76 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.01 (-10.96%)</td><td>0.01 (+2.80%)</td><td>0.01 (+0.21%)</td><td>0.01 <b>(+71.49%)</b></td><td>0.00 <b>(-68.39%)</b></td><td>225.40 <b>(-41.68%)</b></td><td>198.16 (-11.49%)</td><td>195.60 (-0.20%)</td><td>175.80 (+12.33%)</td><td>18.44 <b>(-80.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>386.50 (n/a)</td><td>223.88 (n/a)</td><td>196.00 (n/a)</td><td>156.50 (n/a)</td><td>93.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 <b>(+64.18%)</b></td><td>0.02 (+15.44%)</td><td>0.01 (-9.54%)</td><td>0.01 <b>(+24.45%)</b></td><td>0.01 <b>(+143.88%)</b></td><td>208.90 (-19.62%)</td><td>176.02 (-9.23%)</td><td>195.80 (+10.56%)</td><td>100.80 <b>(-39.09%)</b></td><td>44.66 (+15.15%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>259.90 (n/a)</td><td>193.92 (n/a)</td><td>177.10 (n/a)</td><td>165.50 (n/a)</td><td>38.78 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.01 (+1.18%)</td><td>0.01 (+0.82%)</td><td>0.01 (-2.91%)</td><td>0.01 (+6.05%)</td><td>0.00 <b>(-28.84%)</b></td><td>221.90 (-5.69%)</td><td>200.28 (-1.29%)</td><td>197.30 (+2.97%)</td><td>181.90 (-1.20%)</td><td>14.89 <b>(-32.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>235.30 (n/a)</td><td>202.90 (n/a)</td><td>191.60 (n/a)</td><td>184.10 (n/a)</td><td>22.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (-6.18%)</td><td>0.01 (-1.84%)</td><td>0.01 (-7.66%)</td><td>0.01 (-8.01%)</td><td>0.00 (+5.91%)</td><td>219.90 (+8.70%)</td><td>184.64 (+2.69%)</td><td>204.20 (+8.27%)</td><td>139.70 (+6.64%)</td><td>35.52 <b>(+26.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>179.80 (n/a)</td><td>188.60 (n/a)</td><td>131.00 (n/a)</td><td>28.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (-2.34%)</td><td>0.01 (+2.42%)</td><td>0.01 (-7.18%)</td><td>0.01 (+10.55%)</td><td>0.00 (-17.07%)</td><td>252.30 (-9.54%)</td><td>221.24 (-3.39%)</td><td>238.30 (+7.73%)</td><td>171.80 (+2.38%)</td><td>32.68 <b>(-22.95%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>278.90 (n/a)</td><td>229.00 (n/a)</td><td>221.20 (n/a)</td><td>167.80 (n/a)</td><td>42.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(+27.68%)</b></td><td>0.03 (+8.46%)</td><td>0.03 (+0.51%)</td><td>0.02 (+3.92%)</td><td>0.00 <b>(+114.19%)</b></td><td>220.40 (-3.80%)</td><td>187.26 (-6.44%)</td><td>192.00 (-0.47%)</td><td>141.80 <b>(-21.66%)</b></td><td>28.42 <b>(+53.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.10 (n/a)</td><td>200.14 (n/a)</td><td>192.90 (n/a)</td><td>181.00 (n/a)</td><td>18.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-6.57%)</td><td>0.03 (-5.55%)</td><td>0.03 (-10.79%)</td><td>0.03 (+7.24%)</td><td>0.00 <b>(-49.41%)</b></td><td>197.90 (-6.78%)</td><td>182.86 (+4.42%)</td><td>187.00 (+12.11%)</td><td>161.30 (+7.03%)</td><td>13.92 <b>(-49.25%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.30 (n/a)</td><td>175.12 (n/a)</td><td>166.80 (n/a)</td><td>150.70 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (-15.78%)</td><td>0.03 (-11.05%)</td><td>0.03 (-12.49%)</td><td>0.02 (-13.53%)</td><td>0.00 <b>(-27.00%)</b></td><td>226.10 (+15.65%)</td><td>175.94 (+11.61%)</td><td>171.50 (+14.26%)</td><td>145.10 (+18.74%)</td><td>30.30 (+1.80%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>157.64 (n/a)</td><td>150.10 (n/a)</td><td>122.20 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-10.89%)</td><td>0.03 (-1.87%)</td><td>0.03 (+5.82%)</td><td>0.02 (+5.29%)</td><td>0.01 <b>(-25.33%)</b></td><td>266.60 (-5.06%)</td><td>202.90 (-0.34%)</td><td>200.00 (-5.48%)</td><td>153.70 (+12.19%)</td><td>43.52 (-19.50%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>280.80 (n/a)</td><td>203.60 (n/a)</td><td>211.60 (n/a)</td><td>137.00 (n/a)</td><td>54.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(+25.67%)</b></td><td>0.03 (+3.74%)</td><td>0.03 (-8.77%)</td><td>0.02 (-2.25%)</td><td>0.01 <b>(+37.32%)</b></td><td>238.50 (+2.27%)</td><td>177.00 (-1.87%)</td><td>167.90 (+9.60%)</td><td>118.30 <b>(-20.44%)</b></td><td>44.88 (+12.31%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>180.38 (n/a)</td><td>153.20 (n/a)</td><td>148.70 (n/a)</td><td>39.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-15.73%)</td><td>0.03 (-15.87%)</td><td>0.03 (-19.84%)</td><td>0.02 (-11.61%)</td><td>0.00 <b>(-24.78%)</b></td><td>236.80 (+13.14%)</td><td>197.38 (+18.22%)</td><td>200.60 <b>(+24.75%)</b></td><td>164.60 (+18.67%)</td><td>28.68 (+0.25%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>166.96 (n/a)</td><td>160.80 (n/a)</td><td>138.70 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-1.24%)</td><td>0.03 (-2.63%)</td><td>0.03 (-3.56%)</td><td>0.03 (+10.49%)</td><td>0.00 <b>(-30.35%)</b></td><td>205.80 (-9.50%)</td><td>184.62 (+1.57%)</td><td>177.70 (+3.68%)</td><td>158.60 (+1.21%)</td><td>19.98 <b>(-33.87%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.40 (n/a)</td><td>181.76 (n/a)</td><td>171.40 (n/a)</td><td>156.70 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(+34.47%)</b></td><td>0.03 (+3.39%)</td><td>0.02 (-6.98%)</td><td>0.02 (-13.06%)</td><td>0.01 <b>(+99.28%)</b></td><td>280.80 (+14.99%)</td><td>206.64 (+1.58%)</td><td>218.50 (+7.53%)</td><td>125.40 <b>(-25.67%)</b></td><td>57.10 <b>(+67.04%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.20 (n/a)</td><td>203.42 (n/a)</td><td>203.20 (n/a)</td><td>168.70 (n/a)</td><td>34.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 <b>(-26.20%)</b></td><td>0.06 (-13.09%)</td><td>0.05 (-19.76%)</td><td>0.05 (-13.00%)</td><td>0.01 <b>(-31.44%)</b></td><td>217.60 (+14.95%)</td><td>176.98 (+13.52%)</td><td>196.00 <b>(+24.60%)</b></td><td>135.50 <b>(+35.50%)</b></td><td>37.19 (+5.54%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>189.30 (n/a)</td><td>155.90 (n/a)</td><td>157.30 (n/a)</td><td>100.00 (n/a)</td><td>35.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 <b>(-30.91%)</b></td><td>0.05 (-18.34%)</td><td>0.06 (-18.51%)</td><td>0.04 (-2.28%)</td><td>0.01 <b>(-58.33%)</b></td><td>239.90 (+2.35%)</td><td>195.58 (+16.76%)</td><td>182.10 <b>(+22.71%)</b></td><td>168.20 <b>(+44.75%)</b></td><td>29.51 <b>(-39.19%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>234.40 (n/a)</td><td>167.50 (n/a)</td><td>148.40 (n/a)</td><td>116.20 (n/a)</td><td>48.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (-15.30%)</td><td>0.06 <b>(-23.34%)</b></td><td>0.06 <b>(-35.84%)</b></td><td>0.04 (-10.65%)</td><td>0.01 <b>(-29.10%)</b></td><td>235.70 (+11.92%)</td><td>184.06 <b>(+27.89%)</b></td><td>182.40 <b>(+55.90%)</b></td><td>131.40 (+18.06%)</td><td>41.13 (-4.55%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>210.60 (n/a)</td><td>143.92 (n/a)</td><td>117.00 (n/a)</td><td>111.30 (n/a)</td><td>43.09 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (-16.95%)</td><td>0.06 (-16.35%)</td><td>0.05 (-18.63%)</td><td>0.05 (-4.51%)</td><td>0.01 <b>(-30.01%)</b></td><td>233.00 (+4.72%)</td><td>181.16 (+16.68%)</td><td>192.70 <b>(+22.90%)</b></td><td>129.80 <b>(+20.41%)</b></td><td>40.13 (-11.60%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>222.50 (n/a)</td><td>155.26 (n/a)</td><td>156.80 (n/a)</td><td>107.80 (n/a)</td><td>45.40 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 <b>(-21.25%)</b></td><td>0.06 (-10.89%)</td><td>0.06 (-2.77%)</td><td>0.05 (+0.33%)</td><td>0.01 <b>(-51.55%)</b></td><td>221.60 (-0.36%)</td><td>188.16 (+6.95%)</td><td>188.90 (+2.83%)</td><td>149.00 <b>(+26.92%)</b></td><td>29.25 <b>(-40.13%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>222.40 (n/a)</td><td>175.94 (n/a)</td><td>183.70 (n/a)</td><td>117.40 (n/a)</td><td>48.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (-1.15%)</td><td>0.05 (-8.87%)</td><td>0.05 (+3.04%)</td><td>0.03 <b>(-35.54%)</b></td><td>0.01 <b>(+73.77%)</b></td><td>328.00 <b>(+55.16%)</b></td><td>221.88 (+14.93%)</td><td>197.30 (-2.95%)</td><td>159.00 (+1.21%)</td><td>64.71 <b>(+181.22%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>193.06 (n/a)</td><td>203.30 (n/a)</td><td>157.10 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 <b>(-20.83%)</b></td><td>0.05 (-8.01%)</td><td>0.05 (-11.63%)</td><td>0.05 <b>(+52.53%)</b></td><td>0.00 <b>(-77.35%)</b></td><td>217.40 <b>(-34.42%)</b></td><td>203.16 (+0.55%)</td><td>200.70 (+13.20%)</td><td>188.80 <b>(+26.29%)</b></td><td>13.63 <b>(-81.71%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>331.50 (n/a)</td><td>202.04 (n/a)</td><td>177.30 (n/a)</td><td>149.50 (n/a)</td><td>74.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (-8.14%)</td><td>0.05 (-3.53%)</td><td>0.05 (-2.13%)</td><td>0.03 (+16.37%)</td><td>0.01 <b>(-25.79%)</b></td><td>326.50 (-14.06%)</td><td>228.78 (-0.57%)</td><td>208.50 (+2.16%)</td><td>176.40 (+8.82%)</td><td>58.80 <b>(-32.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>379.90 (n/a)</td><td>230.08 (n/a)</td><td>204.10 (n/a)</td><td>162.10 (n/a)</td><td>86.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (+12.14%)</td><td>0.12 (-4.41%)</td><td>0.12 (-8.51%)</td><td>0.10 <b>(-21.88%)</b></td><td>0.02 <b>(+282.05%)</b></td><td>219.80 <b>(+28.01%)</b></td><td>173.98 (+7.49%)</td><td>173.00 (+9.36%)</td><td>137.90 (-10.80%)</td><td>33.23 <b>(+330.88%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>171.70 (n/a)</td><td>161.86 (n/a)</td><td>158.20 (n/a)</td><td>154.60 (n/a)</td><td>7.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (-18.73%)</td><td>0.12 <b>(-20.73%)</b></td><td>0.12 <b>(-23.27%)</b></td><td>0.10 (-1.88%)</td><td>0.02 <b>(-29.12%)</b></td><td>216.50 (+1.93%)</td><td>177.40 <b>(+23.88%)</b></td><td>170.10 <b>(+30.34%)</b></td><td>139.20 <b>(+23.08%)</b></td><td>34.44 (-13.36%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>212.40 (n/a)</td><td>143.20 (n/a)</td><td>130.50 (n/a)</td><td>113.10 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (-9.08%)</td><td>0.13 (+13.61%)</td><td>0.14 <b>(+32.59%)</b></td><td>0.10 (+8.13%)</td><td>0.02 <b>(-34.55%)</b></td><td>202.60 (-7.49%)</td><td>158.22 (-13.77%)</td><td>146.30 <b>(-24.55%)</b></td><td>143.30 (+10.06%)</td><td>25.07 <b>(-32.84%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>219.00 (n/a)</td><td>183.48 (n/a)</td><td>193.90 (n/a)</td><td>130.20 (n/a)</td><td>37.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (-19.20%)</td><td>0.11 (-18.37%)</td><td>0.10 (-13.23%)</td><td>0.08 <b>(-23.33%)</b></td><td>0.03 (-12.30%)</td><td>253.00 <b>(+30.41%)</b></td><td>202.72 <b>(+23.59%)</b></td><td>202.20 (+15.28%)</td><td>146.10 <b>(+23.81%)</b></td><td>46.11 <b>(+42.88%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>194.00 (n/a)</td><td>164.02 (n/a)</td><td>175.40 (n/a)</td><td>118.00 (n/a)</td><td>32.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 <b>(-33.96%)</b></td><td>0.10 <b>(-28.18%)</b></td><td>0.09 <b>(-30.71%)</b></td><td>0.09 <b>(-24.04%)</b></td><td>0.02 <b>(-43.13%)</b></td><td>237.10 <b>(+31.65%)</b></td><td>206.34 <b>(+37.80%)</b></td><td>222.00 <b>(+44.34%)</b></td><td>158.30 <b>(+51.48%)</b></td><td>32.96 (+18.94%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>180.10 (n/a)</td><td>149.74 (n/a)</td><td>153.80 (n/a)</td><td>104.50 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (-2.75%)</td><td>0.10 (-0.28%)</td><td>0.10 (-2.25%)</td><td>0.07 (-8.19%)</td><td>0.03 (+13.81%)</td><td>307.10 (+8.94%)</td><td>215.50 (+2.64%)</td><td>204.30 (+2.30%)</td><td>146.30 (+2.88%)</td><td>66.19 <b>(+27.85%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>281.90 (n/a)</td><td>209.96 (n/a)</td><td>199.70 (n/a)</td><td>142.20 (n/a)</td><td>51.78 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (-0.47%)</td><td>0.11 (+13.78%)</td><td>0.10 (+5.99%)</td><td>0.10 <b>(+29.87%)</b></td><td>0.02 <b>(-24.42%)</b></td><td>216.30 <b>(-23.00%)</b></td><td>189.86 (-13.86%)</td><td>201.10 (-5.63%)</td><td>157.40 (+0.51%)</td><td>27.14 <b>(-41.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>280.90 (n/a)</td><td>220.42 (n/a)</td><td>213.10 (n/a)</td><td>156.60 (n/a)</td><td>46.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (-9.53%)</td><td>0.09 (-0.88%)</td><td>0.09 (-4.31%)</td><td>0.09 <b>(+42.09%)</b></td><td>0.01 <b>(-67.20%)</b></td><td>239.50 <b>(-29.62%)</b></td><td>223.00 (-4.28%)</td><td>227.80 (+4.50%)</td><td>194.60 (+10.57%)</td><td>16.91 <b>(-74.72%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>340.30 (n/a)</td><td>232.96 (n/a)</td><td>218.00 (n/a)</td><td>176.00 (n/a)</td><td>66.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>183.00 (n/a)</td><td>166.22 (n/a)</td><td>180.30 (n/a)</td><td>140.60 (n/a)</td><td>21.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.20 (n/a)</td><td>170.82 (n/a)</td><td>170.30 (n/a)</td><td>153.50 (n/a)</td><td>15.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>220.20 (n/a)</td><td>167.54 (n/a)</td><td>164.70 (n/a)</td><td>134.80 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>346.50 (n/a)</td><td>212.98 (n/a)</td><td>180.70 (n/a)</td><td>167.70 (n/a)</td><td>75.09 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.60 (n/a)</td><td>156.10 (n/a)</td><td>160.60 (n/a)</td><td>129.00 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>169.30 (n/a)</td><td>147.16 (n/a)</td><td>147.90 (n/a)</td><td>112.70 (n/a)</td><td>23.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>184.00 (n/a)</td><td>177.56 (n/a)</td><td>178.80 (n/a)</td><td>165.60 (n/a)</td><td>7.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>177.48 (n/a)</td><td>175.60 (n/a)</td><td>154.40 (n/a)</td><td>16.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>232.20 (n/a)</td><td>172.00 (n/a)</td><td>167.60 (n/a)</td><td>129.60 (n/a)</td><td>37.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>184.60 (n/a)</td><td>158.28 (n/a)</td><td>149.80 (n/a)</td><td>135.90 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>304.60 (n/a)</td><td>202.86 (n/a)</td><td>183.60 (n/a)</td><td>141.10 (n/a)</td><td>63.68 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>211.90 (n/a)</td><td>175.56 (n/a)</td><td>172.20 (n/a)</td><td>144.10 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 <b>(-20.83%)</b></td><td>0.27 (-18.69%)</td><td>0.27 <b>(-26.71%)</b></td><td>0.22 (-2.99%)</td><td>0.03 <b>(-49.37%)</b></td><td>223.80 (+3.04%)</td><td>184.88 (+19.73%)</td><td>180.70 <b>(+36.38%)</b></td><td>163.10 <b>(+26.34%)</b></td><td>25.11 <b>(-33.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.37 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>217.20 (n/a)</td><td>154.42 (n/a)</td><td>132.50 (n/a)</td><td>129.10 (n/a)</td><td>37.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>226.50 (n/a)</td><td>191.06 (n/a)</td><td>191.70 (n/a)</td><td>148.70 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.02 (n/a)</td><td>191.20 (n/a)</td><td>172.70 (n/a)</td><td>173.20 (n/a)</td><td>157.90 (n/a)</td><td>13.34 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>227.60 (n/a)</td><td>195.46 (n/a)</td><td>210.70 (n/a)</td><td>129.20 (n/a)</td><td>40.28 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>178.60 (n/a)</td><td>167.70 (n/a)</td><td>172.10 (n/a)</td><td>154.70 (n/a)</td><td>11.82 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>255.90 (n/a)</td><td>202.84 (n/a)</td><td>187.00 (n/a)</td><td>151.80 (n/a)</td><td>46.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>224.40 (n/a)</td><td>178.92 (n/a)</td><td>184.50 (n/a)</td><td>137.60 (n/a)</td><td>34.46 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>364.80 (n/a)</td><td>221.94 (n/a)</td><td>199.20 (n/a)</td><td>154.70 (n/a)</td><td>82.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>163.00 (n/a)</td><td>167.70 (n/a)</td><td>137.70 (n/a)</td><td>15.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>176.46 (n/a)</td><td>177.80 (n/a)</td><td>152.10 (n/a)</td><td>15.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>189.04 (n/a)</td><td>204.40 (n/a)</td><td>142.40 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.40 (n/a)</td><td>196.90 (n/a)</td><td>205.10 (n/a)</td><td>141.80 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>185.86 (n/a)</td><td>180.40 (n/a)</td><td>171.40 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>222.20 (n/a)</td><td>190.96 (n/a)</td><td>201.20 (n/a)</td><td>146.60 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>245.00 (n/a)</td><td>177.88 (n/a)</td><td>165.20 (n/a)</td><td>148.20 (n/a)</td><td>38.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>232.20 (n/a)</td><td>194.82 (n/a)</td><td>203.80 (n/a)</td><td>150.60 (n/a)</td><td>32.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>188.60 (n/a)</td><td>171.48 (n/a)</td><td>174.10 (n/a)</td><td>149.00 (n/a)</td><td>15.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>224.60 (n/a)</td><td>176.14 (n/a)</td><td>166.20 (n/a)</td><td>160.70 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>249.80 (n/a)</td><td>220.08 (n/a)</td><td>228.10 (n/a)</td><td>176.80 (n/a)</td><td>29.87 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/flm/dequant</summary>


### test_e4b_gate_up_interleaved[iter0]

_No metrics available._


### test_e4b_gate_up_interleaved[iter1]

_No metrics available._


### test_e4b_gate_up_interleaved[iter2]

_No metrics available._


### test_e4b_gate_up_interleaved[iter3]

_No metrics available._


### test_e4b_gate_up_interleaved[iter4]

_No metrics available._


### test_e4b_shapes[K_10240-N_2560]

_No metrics available._


### test_e4b_shapes[K_2560-N_10240]

_No metrics available._


### test_e4b_shapes[K_2560-N_2560]

_No metrics available._


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


### test_large_k_shapes[K_12288-N_1536]

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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>15.97 (+1.76%)</td><td>14.58 (+0.13%)</td><td>14.52 (+1.21%)</td><td>13.20 (-6.45%)</td><td>0.99 <b>(+51.38%)</b></td><td>4220.70 (+6.90%)</td><td>3836.04 (+0.09%)</td><td>3837.30 (-1.20%)</td><td>3488.30 (-1.74%)</td><td>262.95 <b>(+59.93%)</b></td><td>15390.58 (+1.76%)</td><td>14047.81 (+0.13%)</td><td>13990.69 (+1.21%)</td><td>12720.09 (-6.45%)</td><td>957.15 <b>(+51.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>15.69 (n/a)</td><td>14.56 (n/a)</td><td>14.34 (n/a)</td><td>14.11 (n/a)</td><td>0.66 (n/a)</td><td>3948.40 (n/a)</td><td>3832.66 (n/a)</td><td>3883.80 (n/a)</td><td>3549.90 (n/a)</td><td>164.41 (n/a)</td><td>15123.75 (n/a)</td><td>14029.48 (n/a)</td><td>13823.24 (n/a)</td><td>13597.35 (n/a)</td><td>632.29 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>16.28 (-4.25%)</td><td>14.65 (-3.42%)</td><td>14.32 (-3.32%)</td><td>13.27 (+0.23%)</td><td>1.20 <b>(-22.50%)</b></td><td>988.00 (-0.22%)</td><td>899.16 (+3.23%)</td><td>915.00 (+3.44%)</td><td>804.90 (+4.42%)</td><td>72.36 (-18.80%)</td><td>10671.63 (-4.25%)</td><td>9603.68 (-3.42%)</td><td>9387.68 (-3.32%)</td><td>8694.53 (+0.23%)</td><td>784.83 <b>(-22.50%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>17.01 (n/a)</td><td>15.17 (n/a)</td><td>14.82 (n/a)</td><td>13.24 (n/a)</td><td>1.55 (n/a)</td><td>990.20 (n/a)</td><td>871.06 (n/a)</td><td>884.60 (n/a)</td><td>770.80 (n/a)</td><td>89.11 (n/a)</td><td>11144.79 (n/a)</td><td>9944.09 (n/a)</td><td>9710.24 (n/a)</td><td>8674.62 (n/a)</td><td>1012.66 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>15.36 (+10.55%)</td><td>13.90 (+2.52%)</td><td>14.14 (+2.95%)</td><td>12.84 (+0.32%)</td><td>1.07 <b>(+133.10%)</b></td><td>4337.50 (-0.32%)</td><td>4027.08 (-2.09%)</td><td>3938.70 (-2.86%)</td><td>3627.20 (-9.55%)</td><td>305.88 <b>(+113.61%)</b></td><td>14801.36 (+10.55%)</td><td>13393.81 (+2.52%)</td><td>13630.68 (+2.95%)</td><td>12377.36 (+0.32%)</td><td>1027.16 <b>(+133.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>13.89 (n/a)</td><td>13.56 (n/a)</td><td>13.74 (n/a)</td><td>12.80 (n/a)</td><td>0.46 (n/a)</td><td>4351.40 (n/a)</td><td>4113.10 (n/a)</td><td>4054.70 (n/a)</td><td>4010.00 (n/a)</td><td>143.20 (n/a)</td><td>13388.41 (n/a)</td><td>13064.97 (n/a)</td><td>13240.69 (n/a)</td><td>12337.75 (n/a)</td><td>440.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>16.95 (-1.08%)</td><td>15.59 (+13.61%)</td><td>15.21 (+1.74%)</td><td>14.35 <b>(+35.49%)</b></td><td>1.14 <b>(-60.53%)</b></td><td>1244.20 <b>(-26.20%)</b></td><td>1150.02 (-14.88%)</td><td>1174.50 (-1.71%)</td><td>1053.50 (+1.08%)</td><td>83.30 <b>(-72.01%)</b></td><td>12739.75 (-1.08%)</td><td>11720.46 (+13.61%)</td><td>11427.50 (+1.74%)</td><td>10787.06 <b>(+35.49%)</b></td><td>859.81 <b>(-60.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>17.14 (n/a)</td><td>13.73 (n/a)</td><td>14.95 (n/a)</td><td>10.59 (n/a)</td><td>2.90 (n/a)</td><td>1685.90 (n/a)</td><td>1351.00 (n/a)</td><td>1194.90 (n/a)</td><td>1042.20 (n/a)</td><td>297.57 (n/a)</td><td>12878.48 (n/a)</td><td>10316.73 (n/a)</td><td>11232.49 (n/a)</td><td>7961.28 (n/a)</td><td>2178.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>11.80 (+4.96%)</td><td>11.09 (+2.03%)</td><td>11.12 (+3.39%)</td><td>10.63 (+0.91%)</td><td>0.46 <b>(+37.01%)</b></td><td>7703.70 (-0.90%)</td><td>7396.62 (-1.93%)</td><td>7366.90 (-3.28%)</td><td>6944.90 (-4.72%)</td><td>301.55 <b>(+29.95%)</b></td><td>15460.94 (+4.96%)</td><td>14536.37 (+2.03%)</td><td>14575.14 (+3.39%)</td><td>13937.95 (+0.91%)</td><td>604.64 <b>(+37.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>11.24 (n/a)</td><td>10.87 (n/a)</td><td>10.75 (n/a)</td><td>10.54 (n/a)</td><td>0.34 (n/a)</td><td>7774.00 (n/a)</td><td>7542.14 (n/a)</td><td>7617.00 (n/a)</td><td>7289.10 (n/a)</td><td>232.06 (n/a)</td><td>14730.86 (n/a)</td><td>14247.47 (n/a)</td><td>14096.67 (n/a)</td><td>13812.04 (n/a)</td><td>441.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>15.74 (-2.85%)</td><td>13.92 (-0.54%)</td><td>14.75 (-0.94%)</td><td>11.14 (+2.45%)</td><td>2.02 (-16.52%)</td><td>1930.10 (-2.39%)</td><td>1572.94 (-0.22%)</td><td>1457.10 (+0.95%)</td><td>1365.70 (+2.94%)</td><td>245.27 (-15.93%)</td><td>12579.82 (-2.85%)</td><td>11122.86 (-0.54%)</td><td>11790.67 (-0.94%)</td><td>8901.24 (+2.45%)</td><td>1612.69 (-16.52%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>16.20 (n/a)</td><td>13.99 (n/a)</td><td>14.89 (n/a)</td><td>10.87 (n/a)</td><td>2.42 (n/a)</td><td>1977.30 (n/a)</td><td>1576.44 (n/a)</td><td>1443.40 (n/a)</td><td>1326.70 (n/a)</td><td>291.75 (n/a)</td><td>12948.95 (n/a)</td><td>11183.02 (n/a)</td><td>11902.20 (n/a)</td><td>8688.66 (n/a)</td><td>1931.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>10.40 (-5.12%)</td><td>10.30 (-4.02%)</td><td>10.37 (-4.82%)</td><td>10.00 (-4.08%)</td><td>0.17 <b>(-36.87%)</b></td><td>8190.30 (+4.25%)</td><td>7952.88 (+4.16%)</td><td>7897.60 (+5.06%)</td><td>7876.00 (+5.40%)</td><td>133.61 <b>(-30.62%)</b></td><td>13633.05 (-5.12%)</td><td>13504.28 (-4.02%)</td><td>13595.82 (-4.82%)</td><td>13109.88 (-4.08%)</td><td>222.05 <b>(-36.87%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>10.96 (n/a)</td><td>10.73 (n/a)</td><td>10.90 (n/a)</td><td>10.43 (n/a)</td><td>0.27 (n/a)</td><td>7856.40 (n/a)</td><td>7635.42 (n/a)</td><td>7517.00 (n/a)</td><td>7472.80 (n/a)</td><td>192.57 (n/a)</td><td>14368.68 (n/a)</td><td>14069.73 (n/a)</td><td>14284.11 (n/a)</td><td>13667.07 (n/a)</td><td>351.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.65 (+2.86%)</td><td>3.37 (-12.57%)</td><td>3.11 <b>(-20.02%)</b></td><td>2.89 (-3.01%)</td><td>0.74 <b>(+23.68%)</b></td><td>476.60 (+3.09%)</td><td>420.82 (+15.55%)</td><td>442.50 <b>(+25.04%)</b></td><td>295.80 (-2.79%)</td><td>74.16 <b>(+20.73%)</b></td><td>907.42 (+2.86%)</td><td>658.00 (-12.57%)</td><td>606.70 <b>(-20.02%)</b></td><td>563.17 (-3.01%)</td><td>143.40 <b>(+23.68%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.52 (n/a)</td><td>3.86 (n/a)</td><td>3.89 (n/a)</td><td>2.98 (n/a)</td><td>0.59 (n/a)</td><td>462.30 (n/a)</td><td>364.20 (n/a)</td><td>353.90 (n/a)</td><td>304.30 (n/a)</td><td>61.43 (n/a)</td><td>882.20 (n/a)</td><td>752.56 (n/a)</td><td>758.54 (n/a)</td><td>580.64 (n/a)</td><td>115.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>6.29 (+8.01%)</td><td>4.19 (-8.46%)</td><td>3.73 (-9.76%)</td><td>3.50 (-3.96%)</td><td>1.19 (+18.32%)</td><td>393.00 (+4.11%)</td><td>345.22 (+10.52%)</td><td>368.90 (+10.81%)</td><td>218.60 (-7.41%)</td><td>72.38 (+11.88%)</td><td>1227.77 (+8.01%)</td><td>816.28 (-8.46%)</td><td>727.72 (-9.76%)</td><td>683.01 (-3.96%)</td><td>231.84 (+18.32%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>5.83 (n/a)</td><td>4.57 (n/a)</td><td>4.13 (n/a)</td><td>3.65 (n/a)</td><td>1.00 (n/a)</td><td>377.50 (n/a)</td><td>312.36 (n/a)</td><td>332.90 (n/a)</td><td>236.10 (n/a)</td><td>64.69 (n/a)</td><td>1136.76 (n/a)</td><td>891.69 (n/a)</td><td>806.39 (n/a)</td><td>711.15 (n/a)</td><td>195.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>6.33 (+14.16%)</td><td>4.19 (-1.88%)</td><td>3.57 (-9.23%)</td><td>3.39 (-0.03%)</td><td>1.24 <b>(+45.28%)</b></td><td>406.10 (+0.05%)</td><td>346.98 (+4.44%)</td><td>385.40 (+10.18%)</td><td>217.50 (-12.40%)</td><td>78.13 <b>(+27.11%)</b></td><td>1234.33 (+14.16%)</td><td>816.64 (-1.88%)</td><td>696.51 (-9.23%)</td><td>661.07 (-0.03%)</td><td>241.01 <b>(+45.28%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>5.54 (n/a)</td><td>4.27 (n/a)</td><td>3.93 (n/a)</td><td>3.39 (n/a)</td><td>0.85 (n/a)</td><td>405.90 (n/a)</td><td>332.22 (n/a)</td><td>349.80 (n/a)</td><td>248.30 (n/a)</td><td>61.47 (n/a)</td><td>1081.25 (n/a)</td><td>832.29 (n/a)</td><td>767.36 (n/a)</td><td>661.28 (n/a)</td><td>165.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.96 (+8.68%)</td><td>4.46 (-10.89%)</td><td>3.70 (-8.45%)</td><td>3.31 (-9.75%)</td><td>1.97 <b>(+25.20%)</b></td><td>415.80 (+10.79%)</td><td>343.02 (+16.14%)</td><td>371.90 (+9.22%)</td><td>173.00 (-7.98%)</td><td>97.31 <b>(+20.64%)</b></td><td>1551.84 (+8.68%)</td><td>868.98 (-10.89%)</td><td>721.82 (-8.45%)</td><td>645.54 (-9.75%)</td><td>383.54 <b>(+25.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.32 (n/a)</td><td>5.00 (n/a)</td><td>4.04 (n/a)</td><td>3.67 (n/a)</td><td>1.57 (n/a)</td><td>375.30 (n/a)</td><td>295.34 (n/a)</td><td>340.50 (n/a)</td><td>188.00 (n/a)</td><td>80.65 (n/a)</td><td>1427.86 (n/a)</td><td>975.18 (n/a)</td><td>788.43 (n/a)</td><td>715.27 (n/a)</td><td>306.35 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>5.13 (-2.59%)</td><td>3.86 (-4.22%)</td><td>3.42 (+5.01%)</td><td>3.06 (-4.14%)</td><td>0.87 <b>(-21.60%)</b></td><td>449.30 (+4.32%)</td><td>370.44 (+2.42%)</td><td>402.50 (-4.78%)</td><td>268.50 (+2.68%)</td><td>75.62 (-16.26%)</td><td>999.83 (-2.59%)</td><td>752.06 (-4.22%)</td><td>666.94 (+5.01%)</td><td>597.45 (-4.14%)</td><td>169.02 <b>(-21.60%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>5.26 (n/a)</td><td>4.03 (n/a)</td><td>3.26 (n/a)</td><td>3.20 (n/a)</td><td>1.11 (n/a)</td><td>430.70 (n/a)</td><td>361.70 (n/a)</td><td>422.70 (n/a)</td><td>261.50 (n/a)</td><td>90.29 (n/a)</td><td>1026.45 (n/a)</td><td>785.23 (n/a)</td><td>635.10 (n/a)</td><td>623.27 (n/a)</td><td>215.61 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>5.52 (+16.84%)</td><td>4.04 (+7.87%)</td><td>3.56 (+4.98%)</td><td>2.88 (-1.73%)</td><td>1.22 <b>(+35.14%)</b></td><td>477.60 (+1.75%)</td><td>365.20 (-4.92%)</td><td>386.80 (-4.73%)</td><td>249.20 (-14.42%)</td><td>103.37 (+17.95%)</td><td>1077.21 (+16.84%)</td><td>788.37 (+7.87%)</td><td>694.02 (+4.98%)</td><td>562.03 (-1.73%)</td><td>237.54 <b>(+35.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.73 (n/a)</td><td>3.75 (n/a)</td><td>3.39 (n/a)</td><td>2.93 (n/a)</td><td>0.90 (n/a)</td><td>469.40 (n/a)</td><td>384.10 (n/a)</td><td>406.00 (n/a)</td><td>291.20 (n/a)</td><td>87.63 (n/a)</td><td>921.94 (n/a)</td><td>730.85 (n/a)</td><td>661.12 (n/a)</td><td>571.93 (n/a)</td><td>175.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.98 (-1.18%)</td><td>3.38 (-10.35%)</td><td>2.99 (-18.31%)</td><td>2.83 (-6.68%)</td><td>0.90 (+17.92%)</td><td>486.60 (+7.16%)</td><td>425.58 (+13.17%)</td><td>460.80 <b>(+22.42%)</b></td><td>276.40 (+1.17%)</td><td>85.30 <b>(+27.24%)</b></td><td>971.02 (-1.18%)</td><td>658.87 (-10.35%)</td><td>582.55 (-18.31%)</td><td>551.67 (-6.68%)</td><td>175.97 (+17.92%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>5.04 (n/a)</td><td>3.77 (n/a)</td><td>3.66 (n/a)</td><td>3.03 (n/a)</td><td>0.77 (n/a)</td><td>454.10 (n/a)</td><td>376.04 (n/a)</td><td>376.40 (n/a)</td><td>273.20 (n/a)</td><td>67.04 (n/a)</td><td>982.60 (n/a)</td><td>734.90 (n/a)</td><td>713.15 (n/a)</td><td>591.18 (n/a)</td><td>149.23 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.30 <b>(+24.50%)</b></td><td>1.29 (-0.43%)</td><td>1.03 (-5.25%)</td><td>0.90 (-14.77%)</td><td>0.58 <b>(+67.12%)</b></td><td>445.70 (+17.32%)</td><td>348.06 (+7.15%)</td><td>391.20 (+5.53%)</td><td>174.40 (-19.71%)</td><td>106.64 <b>(+46.02%)</b></td><td>192.36 <b>(+24.50%)</b></td><td>107.98 (-0.43%)</td><td>85.77 (-5.25%)</td><td>75.29 (-14.77%)</td><td>48.32 <b>(+67.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.85 (n/a)</td><td>1.30 (n/a)</td><td>1.08 (n/a)</td><td>1.06 (n/a)</td><td>0.35 (n/a)</td><td>379.90 (n/a)</td><td>324.84 (n/a)</td><td>370.70 (n/a)</td><td>217.20 (n/a)</td><td>73.03 (n/a)</td><td>154.50 (n/a)</td><td>108.45 (n/a)</td><td>90.52 (n/a)</td><td>88.33 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.91 (-2.53%)</td><td>5.51 (-17.43%)</td><td>4.85 <b>(-25.10%)</b></td><td>4.62 (-19.01%)</td><td>1.37 <b>(+51.73%)</b></td><td>418.30 <b>(+23.47%)</b></td><td>365.28 <b>(+24.25%)</b></td><td>398.60 <b>(+33.53%)</b></td><td>244.30 (+2.60%)</td><td>70.96 <b>(+90.77%)</b></td><td>1648.09 (-2.53%)</td><td>1146.56 (-17.43%)</td><td>1010.27 <b>(-25.10%)</b></td><td>962.63 (-19.01%)</td><td>286.31 <b>(+51.73%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>8.12 (n/a)</td><td>6.67 (n/a)</td><td>6.48 (n/a)</td><td>5.71 (n/a)</td><td>0.91 (n/a)</td><td>338.80 (n/a)</td><td>293.98 (n/a)</td><td>298.50 (n/a)</td><td>238.10 (n/a)</td><td>37.20 (n/a)</td><td>1690.80 (n/a)</td><td>1388.55 (n/a)</td><td>1348.84 (n/a)</td><td>1188.59 (n/a)</td><td>188.70 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>16.26 (+0.56%)</td><td>12.31 (-0.51%)</td><td>11.20 (-2.12%)</td><td>10.64 (-2.52%)</td><td>2.31 (+6.77%)</td><td>517.30 (+2.58%)</td><td>457.84 (+0.86%)</td><td>491.30 (+2.16%)</td><td>338.60 (-0.56%)</td><td>72.35 (+9.77%)</td><td>6342.34 (+0.56%)</td><td>4803.61 (-0.51%)</td><td>4370.89 (-2.12%)</td><td>4150.97 (-2.52%)</td><td>900.80 (+6.77%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>16.17 (n/a)</td><td>12.38 (n/a)</td><td>11.45 (n/a)</td><td>10.92 (n/a)</td><td>2.16 (n/a)</td><td>504.30 (n/a)</td><td>453.94 (n/a)</td><td>480.90 (n/a)</td><td>340.50 (n/a)</td><td>65.91 (n/a)</td><td>6307.06 (n/a)</td><td>4828.36 (n/a)</td><td>4465.40 (n/a)</td><td>4258.09 (n/a)</td><td>843.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>10.61 (+5.79%)</td><td>7.77 (-6.13%)</td><td>7.95 (-0.75%)</td><td>4.25 <b>(-42.75%)</b></td><td>2.27 <b>(+119.67%)</b></td><td>1296.00 <b>(+74.69%)</b></td><td>775.64 (+15.39%)</td><td>692.70 (+0.76%)</td><td>518.90 (-5.47%)</td><td>300.01 <b>(+297.89%)</b></td><td>4138.63 (+5.79%)</td><td>3032.77 (-6.13%)</td><td>3100.17 (-0.75%)</td><td>1657.05 <b>(-42.75%)</b></td><td>886.50 <b>(+119.67%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>10.03 (n/a)</td><td>8.28 (n/a)</td><td>8.01 (n/a)</td><td>7.42 (n/a)</td><td>1.03 (n/a)</td><td>741.90 (n/a)</td><td>672.18 (n/a)</td><td>687.50 (n/a)</td><td>548.90 (n/a)</td><td>75.40 (n/a)</td><td>3912.01 (n/a)</td><td>3230.95 (n/a)</td><td>3123.71 (n/a)</td><td>2894.64 (n/a)</td><td>403.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>11.54 (-6.26%)</td><td>9.23 (+0.15%)</td><td>8.55 (-3.64%)</td><td>6.29 <b>(+20.59%)</b></td><td>2.25 (-19.24%)</td><td>921.60 (-17.08%)</td><td>661.78 (-3.98%)</td><td>678.00 (+3.78%)</td><td>502.60 (+6.66%)</td><td>172.37 <b>(-32.27%)</b></td><td>4806.78 (-6.26%)</td><td>3842.72 (+0.15%)</td><td>3563.36 (-3.64%)</td><td>2621.46 <b>(+20.59%)</b></td><td>938.27 (-19.24%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>12.31 (n/a)</td><td>9.21 (n/a)</td><td>8.88 (n/a)</td><td>5.22 (n/a)</td><td>2.79 (n/a)</td><td>1111.40 (n/a)</td><td>689.18 (n/a)</td><td>653.30 (n/a)</td><td>471.20 (n/a)</td><td>254.51 (n/a)</td><td>5127.52 (n/a)</td><td>3837.10 (n/a)</td><td>3698.00 (n/a)</td><td>2173.85 (n/a)</td><td>1161.77 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.30 (n/a)</td><td>165.90 (n/a)</td><td>165.60 (n/a)</td><td>144.60 (n/a)</td><td>14.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.40 (n/a)</td><td>175.20 (n/a)</td><td>173.10 (n/a)</td><td>160.30 (n/a)</td><td>17.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.70 (n/a)</td><td>171.64 (n/a)</td><td>159.70 (n/a)</td><td>139.90 (n/a)</td><td>39.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.70 (n/a)</td><td>171.22 (n/a)</td><td>173.90 (n/a)</td><td>154.40 (n/a)</td><td>10.41 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>244.70 (n/a)</td><td>178.46 (n/a)</td><td>168.20 (n/a)</td><td>138.20 (n/a)</td><td>42.60 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.50 (n/a)</td><td>155.56 (n/a)</td><td>152.40 (n/a)</td><td>130.00 (n/a)</td><td>25.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>192.12 (n/a)</td><td>202.30 (n/a)</td><td>131.10 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>364.90 (n/a)</td><td>221.82 (n/a)</td><td>196.70 (n/a)</td><td>169.60 (n/a)</td><td>81.37 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.30 (n/a)</td><td>179.30 (n/a)</td><td>170.30 (n/a)</td><td>126.20 (n/a)</td><td>60.04 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.30 (n/a)</td><td>151.86 (n/a)</td><td>154.40 (n/a)</td><td>125.50 (n/a)</td><td>20.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>177.90 (n/a)</td><td>181.90 (n/a)</td><td>128.70 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>159.62 (n/a)</td><td>165.60 (n/a)</td><td>115.40 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>300.80 (n/a)</td><td>191.84 (n/a)</td><td>166.60 (n/a)</td><td>144.90 (n/a)</td><td>63.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>230.20 (n/a)</td><td>165.78 (n/a)</td><td>134.70 (n/a)</td><td>115.20 (n/a)</td><td>52.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>156.10 (n/a)</td><td>156.20 (n/a)</td><td>131.20 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.00 (n/a)</td><td>197.46 (n/a)</td><td>213.30 (n/a)</td><td>155.80 (n/a)</td><td>30.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.90 (n/a)</td><td>158.46 (n/a)</td><td>131.70 (n/a)</td><td>130.00 (n/a)</td><td>39.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.10 (n/a)</td><td>158.70 (n/a)</td><td>152.90 (n/a)</td><td>120.60 (n/a)</td><td>37.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>280.80 (n/a)</td><td>199.80 (n/a)</td><td>172.80 (n/a)</td><td>129.10 (n/a)</td><td>62.36 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>177.30 (n/a)</td><td>149.48 (n/a)</td><td>153.80 (n/a)</td><td>124.40 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.00 (n/a)</td><td>165.66 (n/a)</td><td>167.50 (n/a)</td><td>131.10 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>165.66 (n/a)</td><td>172.60 (n/a)</td><td>130.00 (n/a)</td><td>33.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>155.62 (n/a)</td><td>163.10 (n/a)</td><td>129.40 (n/a)</td><td>20.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>248.20 (n/a)</td><td>202.26 (n/a)</td><td>193.50 (n/a)</td><td>170.10 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>234.50 (n/a)</td><td>164.86 (n/a)</td><td>139.40 (n/a)</td><td>128.20 (n/a)</td><td>44.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>179.10 (n/a)</td><td>141.18 (n/a)</td><td>129.80 (n/a)</td><td>109.70 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>187.40 (n/a)</td><td>157.64 (n/a)</td><td>173.70 (n/a)</td><td>117.70 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.80 (n/a)</td><td>154.50 (n/a)</td><td>143.70 (n/a)</td><td>120.60 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>177.60 (n/a)</td><td>159.02 (n/a)</td><td>165.60 (n/a)</td><td>130.10 (n/a)</td><td>18.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>211.70 (n/a)</td><td>180.76 (n/a)</td><td>172.50 (n/a)</td><td>146.20 (n/a)</td><td>26.35 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.50 (n/a)</td><td>161.70 (n/a)</td><td>150.60 (n/a)</td><td>127.10 (n/a)</td><td>35.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>233.30 (n/a)</td><td>195.88 (n/a)</td><td>188.80 (n/a)</td><td>172.60 (n/a)</td><td>23.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.12 (-0.06%)</td><td>4.12 (+0.03%)</td><td>4.11 (+0.01%)</td><td>4.11 (+0.10%)</td><td>0.00 <b>(-37.42%)</b></td><td>19125.60 (-0.10%)</td><td>19111.06 (-0.03%)</td><td>19119.50 (-0.01%)</td><td>19091.00 (+0.06%)</td><td>15.01 <b>(-37.33%)</b></td><td>2812.16 (-0.06%)</td><td>2809.22 (+0.03%)</td><td>2807.98 (+0.01%)</td><td>2807.08 (+0.10%)</td><td>2.21 <b>(-37.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>0.01 (n/a)</td><td>19144.70 (n/a)</td><td>19117.32 (n/a)</td><td>19120.60 (n/a)</td><td>19078.90 (n/a)</td><td>23.96 (n/a)</td><td>2813.96 (n/a)</td><td>2808.30 (n/a)</td><td>2807.82 (n/a)</td><td>2804.28 (n/a)</td><td>3.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.96 (+1.67%)</td><td>4.30 (-0.30%)</td><td>4.11 (-2.14%)</td><td>3.54 (-13.28%)</td><td>0.59 <b>(+82.83%)</b></td><td>2654.00 (+15.32%)</td><td>2223.12 (+1.43%)</td><td>2289.60 (+2.19%)</td><td>1896.70 (-1.64%)</td><td>308.99 <b>(+106.54%)</b></td><td>1950.41 (+1.67%)</td><td>1689.64 (-0.30%)</td><td>1615.75 (-2.14%)</td><td>1393.89 (-13.28%)</td><td>231.24 <b>(+82.83%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.88 (n/a)</td><td>4.31 (n/a)</td><td>4.20 (n/a)</td><td>4.09 (n/a)</td><td>0.32 (n/a)</td><td>2301.50 (n/a)</td><td>2191.86 (n/a)</td><td>2240.50 (n/a)</td><td>1928.30 (n/a)</td><td>149.60 (n/a)</td><td>1918.46 (n/a)</td><td>1694.68 (n/a)</td><td>1651.16 (n/a)</td><td>1607.40 (n/a)</td><td>126.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.37 <b>(+32.34%)</b></td><td>1.13 (+19.06%)</td><td>1.20 <b>(+23.62%)</b></td><td>0.93 (+13.85%)</td><td>0.19 <b>(+137.56%)</b></td><td>237.20 (-12.18%)</td><td>200.00 (-14.58%)</td><td>184.70 (-19.13%)</td><td>161.80 <b>(-24.43%)</b></td><td>34.18 <b>(+60.58%)</b></td><td>58.33 <b>(+32.34%)</b></td><td>48.28 (+19.06%)</td><td>51.08 <b>(+23.62%)</b></td><td>39.78 (+13.85%)</td><td>8.09 <b>(+137.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.03 (n/a)</td><td>0.95 (n/a)</td><td>0.97 (n/a)</td><td>0.82 (n/a)</td><td>0.08 (n/a)</td><td>270.10 (n/a)</td><td>234.14 (n/a)</td><td>228.40 (n/a)</td><td>214.10 (n/a)</td><td>21.29 (n/a)</td><td>44.07 (n/a)</td><td>40.56 (n/a)</td><td>41.32 (n/a)</td><td>34.94 (n/a)</td><td>3.41 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.21 (-11.80%)</td><td>0.96 (-11.72%)</td><td>0.98 (-3.42%)</td><td>0.68 <b>(-31.39%)</b></td><td>0.20 <b>(+20.31%)</b></td><td>324.20 <b>(+45.77%)</b></td><td>239.40 (+15.73%)</td><td>224.70 (+3.55%)</td><td>182.30 (+13.37%)</td><td>53.47 <b>(+106.29%)</b></td><td>51.77 (-11.80%)</td><td>40.89 (-11.72%)</td><td>41.99 (-3.42%)</td><td>29.11 <b>(-31.39%)</b></td><td>8.36 <b>(+20.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.38 (n/a)</td><td>1.09 (n/a)</td><td>1.02 (n/a)</td><td>0.99 (n/a)</td><td>0.16 (n/a)</td><td>222.40 (n/a)</td><td>206.86 (n/a)</td><td>217.00 (n/a)</td><td>160.80 (n/a)</td><td>25.92 (n/a)</td><td>58.70 (n/a)</td><td>46.31 (n/a)</td><td>43.48 (n/a)</td><td>42.43 (n/a)</td><td>6.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.53 (-0.13%)</td><td>0.53 (-0.11%)</td><td>0.53 (-0.15%)</td><td>0.53 (-0.02%)</td><td>0.00 <b>(-25.24%)</b></td><td>47899.50 (+0.02%)</td><td>47854.86 (+0.11%)</td><td>47867.60 (+0.15%)</td><td>47799.00 (+0.13%)</td><td>43.63 <b>(-25.12%)</b></td><td>359.42 (-0.13%)</td><td>359.00 (-0.11%)</td><td>358.90 (-0.15%)</td><td>358.67 (-0.02%)</td><td>0.33 <b>(-25.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47889.00 (n/a)</td><td>47803.18 (n/a)</td><td>47794.80 (n/a)</td><td>47737.90 (n/a)</td><td>58.27 (n/a)</td><td>359.88 (n/a)</td><td>359.39 (n/a)</td><td>359.45 (n/a)</td><td>358.74 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (-0.10%)</td><td>0.21 (+0.08%)</td><td>0.21 (+0.29%)</td><td>0.21 (+0.22%)</td><td>0.00 (-18.38%)</td><td>119617.60 (-0.22%)</td><td>118702.54 (-0.08%)</td><td>118601.60 (-0.29%)</td><td>117885.90 (+0.10%)</td><td>641.77 (-18.44%)</td><td>145.73 (-0.10%)</td><td>144.73 (+0.08%)</td><td>144.85 (+0.29%)</td><td>143.62 (+0.22%)</td><td>0.78 (-18.38%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119879.90 (n/a)</td><td>118794.58 (n/a)</td><td>118943.30 (n/a)</td><td>117766.70 (n/a)</td><td>786.91 (n/a)</td><td>145.88 (n/a)</td><td>144.62 (n/a)</td><td>144.44 (n/a)</td><td>143.31 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.91 (-1.44%)</td><td>0.90 (-0.63%)</td><td>0.90 (+0.13%)</td><td>0.90 (-0.28%)</td><td>0.01 <b>(-49.84%)</b></td><td>28064.50 (+0.28%)</td><td>27897.58 (+0.62%)</td><td>27883.10 (-0.13%)</td><td>27641.60 (+1.46%)</td><td>169.82 <b>(-49.01%)</b></td><td>621.52 (-1.44%)</td><td>615.84 (-0.63%)</td><td>616.14 (+0.13%)</td><td>612.16 (-0.28%)</td><td>3.76 <b>(-49.84%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.92 (n/a)</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.01 (n/a)</td><td>27987.30 (n/a)</td><td>27725.10 (n/a)</td><td>27918.80 (n/a)</td><td>27242.80 (n/a)</td><td>333.07 (n/a)</td><td>630.62 (n/a)</td><td>619.72 (n/a)</td><td>615.35 (n/a)</td><td>613.85 (n/a)</td><td>7.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>3.71 (+1.61%)</td><td>3.54 (-1.15%)</td><td>3.47 (-2.51%)</td><td>3.42 (-1.94%)</td><td>0.13 <b>(+85.31%)</b></td><td>7361.70 (+1.98%)</td><td>7125.80 (+1.24%)</td><td>7254.70 (+2.57%)</td><td>6779.30 (-1.59%)</td><td>252.44 <b>(+86.48%)</b></td><td>2534.15 (+1.61%)</td><td>2413.40 (-1.15%)</td><td>2368.10 (-2.50%)</td><td>2333.69 (-1.94%)</td><td>86.87 <b>(+85.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>3.65 (n/a)</td><td>3.58 (n/a)</td><td>3.56 (n/a)</td><td>3.49 (n/a)</td><td>0.07 (n/a)</td><td>7218.80 (n/a)</td><td>7038.80 (n/a)</td><td>7073.00 (n/a)</td><td>6888.80 (n/a)</td><td>135.37 (n/a)</td><td>2493.89 (n/a)</td><td>2441.46 (n/a)</td><td>2428.94 (n/a)</td><td>2379.88 (n/a)</td><td>46.88 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>3.25 (+0.67%)</td><td>3.14 (+6.02%)</td><td>3.19 (+10.82%)</td><td>2.97 (+9.06%)</td><td>0.12 <b>(-48.10%)</b></td><td>8482.30 (-8.31%)</td><td>8012.64 (-6.00%)</td><td>7897.80 (-9.76%)</td><td>7741.80 (-0.66%)</td><td>303.12 <b>(-52.21%)</b></td><td>2219.11 (+0.67%)</td><td>2146.50 (+6.02%)</td><td>2175.28 (+10.82%)</td><td>2025.39 (+9.06%)</td><td>79.26 <b>(-48.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>3.23 (n/a)</td><td>2.97 (n/a)</td><td>2.88 (n/a)</td><td>2.72 (n/a)</td><td>0.22 (n/a)</td><td>9250.60 (n/a)</td><td>8523.76 (n/a)</td><td>8752.30 (n/a)</td><td>7793.60 (n/a)</td><td>634.23 (n/a)</td><td>2204.36 (n/a)</td><td>2024.61 (n/a)</td><td>1962.89 (n/a)</td><td>1857.16 (n/a)</td><td>152.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>3.35 (+0.02%)</td><td>3.22 (-0.16%)</td><td>3.19 (-0.15%)</td><td>3.17 (+0.41%)</td><td>0.07 (-6.80%)</td><td>7947.10 (-0.41%)</td><td>7820.18 (+0.15%)</td><td>7900.20 (+0.15%)</td><td>7521.60 (-0.02%)</td><td>176.61 (-7.34%)</td><td>2284.08 (+0.02%)</td><td>2197.78 (-0.16%)</td><td>2174.61 (-0.15%)</td><td>2161.77 (+0.41%)</td><td>50.83 (-6.79%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>3.35 (n/a)</td><td>3.22 (n/a)</td><td>3.19 (n/a)</td><td>3.15 (n/a)</td><td>0.08 (n/a)</td><td>7979.50 (n/a)</td><td>7808.40 (n/a)</td><td>7888.50 (n/a)</td><td>7522.80 (n/a)</td><td>190.61 (n/a)</td><td>2283.71 (n/a)</td><td>2201.25 (n/a)</td><td>2177.84 (n/a)</td><td>2153.00 (n/a)</td><td>54.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.80 (+0.42%)</td><td>0.80 (+0.09%)</td><td>0.80 (+0.01%)</td><td>0.80 (+0.00%)</td><td>0.00 <b>(+457.26%)</b></td><td>94826.00 (-0.00%)</td><td>94701.80 (-0.09%)</td><td>94763.70 (-0.01%)</td><td>94360.60 (-0.42%)</td><td>192.68 <b>(+454.76%)</b></td><td>728.26 (+0.42%)</td><td>725.64 (+0.09%)</td><td>725.17 (+0.01%)</td><td>724.69 (+0.00%)</td><td>1.48 <b>(+457.27%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94827.90 (n/a)</td><td>94789.48 (n/a)</td><td>94770.20 (n/a)</td><td>94756.80 (n/a)</td><td>34.73 (n/a)</td><td>725.22 (n/a)</td><td>724.97 (n/a)</td><td>725.12 (n/a)</td><td>724.68 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.73 (-0.36%)</td><td>0.73 (-0.17%)</td><td>0.73 (-0.01%)</td><td>0.73 (-0.26%)</td><td>0.00 <b>(-20.16%)</b></td><td>103568.50 (+0.26%)</td><td>103372.72 (+0.17%)</td><td>103281.90 (+0.01%)</td><td>103256.70 (+0.36%)</td><td>143.44 (-19.67%)</td><td>665.52 (-0.36%)</td><td>664.77 (-0.17%)</td><td>665.36 (-0.01%)</td><td>663.52 (-0.26%)</td><td>0.92 <b>(-20.16%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103301.80 (n/a)</td><td>103201.70 (n/a)</td><td>103272.60 (n/a)</td><td>102883.20 (n/a)</td><td>178.55 (n/a)</td><td>667.94 (n/a)</td><td>665.88 (n/a)</td><td>665.42 (n/a)</td><td>665.23 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.69 (+0.15%)</td><td>0.68 (-0.10%)</td><td>0.68 (-0.24%)</td><td>0.68 (-0.12%)</td><td>0.00 <b>(+78.98%)</b></td><td>110872.90 (+0.12%)</td><td>110614.24 (+0.10%)</td><td>110681.80 (+0.24%)</td><td>110181.70 (-0.15%)</td><td>293.31 <b>(+78.96%)</b></td><td>623.69 (+0.15%)</td><td>621.26 (-0.10%)</td><td>620.87 (-0.24%)</td><td>619.80 (-0.12%)</td><td>1.65 <b>(+78.99%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110738.80 (n/a)</td><td>110505.02 (n/a)</td><td>110417.10 (n/a)</td><td>110342.80 (n/a)</td><td>163.90 (n/a)</td><td>622.78 (n/a)</td><td>621.87 (n/a)</td><td>622.36 (n/a)</td><td>620.55 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.80 (+0.05%)</td><td>2.80 (+0.17%)</td><td>2.80 (+0.04%)</td><td>2.79 (+0.33%)</td><td>0.00 <b>(-63.53%)</b></td><td>37530.60 (-0.32%)</td><td>37500.48 (-0.17%)</td><td>37514.60 (-0.04%)</td><td>37469.90 (-0.05%)</td><td>27.91 <b>(-63.68%)</b></td><td>2865.61 (+0.05%)</td><td>2863.28 (+0.17%)</td><td>2862.20 (+0.04%)</td><td>2860.98 (+0.33%)</td><td>2.13 <b>(-63.54%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>2.79 (n/a)</td><td>2.78 (n/a)</td><td>0.01 (n/a)</td><td>37652.70 (n/a)</td><td>37563.62 (n/a)</td><td>37531.40 (n/a)</td><td>37490.00 (n/a)</td><td>76.84 (n/a)</td><td>2864.08 (n/a)</td><td>2858.47 (n/a)</td><td>2860.91 (n/a)</td><td>2851.70 (n/a)</td><td>5.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.39 (-3.63%)</td><td>6.78 (-7.53%)</td><td>6.59 (-10.54%)</td><td>6.47 (-6.13%)</td><td>0.39 <b>(+37.74%)</b></td><td>1377.00 (+6.52%)</td><td>1317.86 (+8.28%)</td><td>1353.20 (+11.79%)</td><td>1205.30 (+3.76%)</td><td>71.99 <b>(+51.32%)</b></td><td>445.43 (-3.63%)</td><td>408.40 (-7.53%)</td><td>396.74 (-10.54%)</td><td>389.88 (-6.13%)</td><td>23.28 <b>(+37.74%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.67 (n/a)</td><td>7.33 (n/a)</td><td>7.36 (n/a)</td><td>6.89 (n/a)</td><td>0.28 (n/a)</td><td>1292.70 (n/a)</td><td>1217.10 (n/a)</td><td>1210.50 (n/a)</td><td>1161.60 (n/a)</td><td>47.58 (n/a)</td><td>462.19 (n/a)</td><td>441.63 (n/a)</td><td>443.50 (n/a)</td><td>415.32 (n/a)</td><td>16.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.17 (+5.68%)</td><td>6.85 (+5.01%)</td><td>6.95 (+6.38%)</td><td>6.43 (+3.27%)</td><td>0.29 (+18.42%)</td><td>1385.40 (-3.17%)</td><td>1302.72 (-4.74%)</td><td>1281.60 (-5.99%)</td><td>1242.40 (-5.37%)</td><td>56.42 (+9.00%)</td><td>432.13 (+5.68%)</td><td>412.72 (+5.01%)</td><td>418.89 (+6.38%)</td><td>387.52 (+3.27%)</td><td>17.55 (+18.42%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>6.79 (n/a)</td><td>6.52 (n/a)</td><td>6.54 (n/a)</td><td>6.23 (n/a)</td><td>0.25 (n/a)</td><td>1430.70 (n/a)</td><td>1367.54 (n/a)</td><td>1363.30 (n/a)</td><td>1312.90 (n/a)</td><td>51.76 (n/a)</td><td>408.91 (n/a)</td><td>393.02 (n/a)</td><td>393.79 (n/a)</td><td>375.25 (n/a)</td><td>14.82 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>6.56 (-8.19%)</td><td>6.14 (-3.22%)</td><td>6.34 (-2.84%)</td><td>4.94 (+3.64%)</td><td>0.68 <b>(-26.18%)</b></td><td>1802.90 (-3.52%)</td><td>1468.64 (+2.42%)</td><td>1405.00 (+2.92%)</td><td>1358.40 (+8.92%)</td><td>188.70 <b>(-24.07%)</b></td><td>395.22 (-8.19%)</td><td>369.75 (-3.22%)</td><td>382.11 (-2.84%)</td><td>297.78 (+3.64%)</td><td>40.90 <b>(-26.18%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.15 (n/a)</td><td>6.34 (n/a)</td><td>6.53 (n/a)</td><td>4.77 (n/a)</td><td>0.92 (n/a)</td><td>1868.60 (n/a)</td><td>1433.90 (n/a)</td><td>1365.10 (n/a)</td><td>1247.10 (n/a)</td><td>248.50 (n/a)</td><td>430.50 (n/a)</td><td>382.06 (n/a)</td><td>393.29 (n/a)</td><td>287.31 (n/a)</td><td>55.40 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>8.38 (+3.44%)</td><td>8.01 (+0.18%)</td><td>7.96 (-0.38%)</td><td>7.61 (-3.94%)</td><td>0.29 <b>(+293.03%)</b></td><td>4580.30 (+4.10%)</td><td>4359.12 (-0.08%)</td><td>4382.40 (+0.38%)</td><td>4158.20 (-3.32%)</td><td>157.25 <b>(+295.44%)</b></td><td>516.45 (+3.44%)</td><td>493.15 (+0.18%)</td><td>490.02 (-0.38%)</td><td>468.86 (-3.94%)</td><td>17.73 <b>(+293.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>8.11 (n/a)</td><td>7.99 (n/a)</td><td>7.99 (n/a)</td><td>7.92 (n/a)</td><td>0.07 (n/a)</td><td>4399.90 (n/a)</td><td>4362.74 (n/a)</td><td>4365.90 (n/a)</td><td>4301.10 (n/a)</td><td>39.76 (n/a)</td><td>499.28 (n/a)</td><td>492.26 (n/a)</td><td>491.88 (n/a)</td><td>488.08 (n/a)</td><td>4.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.63 (-2.01%)</td><td>7.42 (-2.17%)</td><td>7.57 (-2.09%)</td><td>6.82 (-3.24%)</td><td>0.34 (+9.03%)</td><td>5115.80 (+3.35%)</td><td>4708.62 (+2.26%)</td><td>4602.90 (+2.13%)</td><td>4567.60 (+2.04%)</td><td>230.70 (+15.32%)</td><td>470.15 (-2.00%)</td><td>456.90 (-2.17%)</td><td>466.55 (-2.09%)</td><td>419.77 (-3.24%)</td><td>21.09 (+9.03%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.79 (n/a)</td><td>7.58 (n/a)</td><td>7.74 (n/a)</td><td>7.04 (n/a)</td><td>0.31 (n/a)</td><td>4950.20 (n/a)</td><td>4604.64 (n/a)</td><td>4506.90 (n/a)</td><td>4476.10 (n/a)</td><td>200.04 (n/a)</td><td>479.77 (n/a)</td><td>467.05 (n/a)</td><td>476.49 (n/a)</td><td>433.81 (n/a)</td><td>19.35 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.51 (+0.07%)</td><td>7.08 (-2.12%)</td><td>6.81 (-6.90%)</td><td>6.75 (-0.92%)</td><td>0.40 <b>(+45.12%)</b></td><td>5166.60 (+0.93%)</td><td>4938.84 (+2.30%)</td><td>5120.50 (+7.41%)</td><td>4641.00 (-0.07%)</td><td>270.67 <b>(+45.24%)</b></td><td>462.72 (+0.07%)</td><td>435.88 (-2.12%)</td><td>419.39 (-6.90%)</td><td>415.65 (-0.92%)</td><td>24.36 <b>(+45.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.51 (n/a)</td><td>7.23 (n/a)</td><td>7.31 (n/a)</td><td>6.81 (n/a)</td><td>0.27 (n/a)</td><td>5118.80 (n/a)</td><td>4827.90 (n/a)</td><td>4767.20 (n/a)</td><td>4644.40 (n/a)</td><td>186.37 (n/a)</td><td>462.39 (n/a)</td><td>445.33 (n/a)</td><td>450.47 (n/a)</td><td>419.53 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.81 (+0.28%)</td><td>0.80 (+0.11%)</td><td>0.80 (-0.01%)</td><td>0.80 (+0.20%)</td><td>0.00 <b>(+36.55%)</b></td><td>94080.30 (-0.20%)</td><td>94005.30 (-0.11%)</td><td>94074.80 (+0.01%)</td><td>93779.10 (-0.28%)</td><td>129.27 <b>(+35.93%)</b></td><td>732.78 (+0.28%)</td><td>731.02 (+0.11%)</td><td>730.48 (-0.01%)</td><td>730.43 (+0.20%)</td><td>1.01 <b>(+36.55%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94272.40 (n/a)</td><td>94105.52 (n/a)</td><td>94069.10 (n/a)</td><td>94038.90 (n/a)</td><td>95.10 (n/a)</td><td>730.76 (n/a)</td><td>730.24 (n/a)</td><td>730.52 (n/a)</td><td>728.95 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.74 (-0.03%)</td><td>0.74 (-0.08%)</td><td>0.74 (-0.06%)</td><td>0.73 (-0.17%)</td><td>0.00 <b>(+156.71%)</b></td><td>102812.60 (+0.17%)</td><td>102669.42 (+0.08%)</td><td>102650.20 (+0.06%)</td><td>102584.50 (+0.03%)</td><td>96.62 <b>(+157.44%)</b></td><td>669.88 (-0.03%)</td><td>669.33 (-0.08%)</td><td>669.45 (-0.06%)</td><td>668.40 (-0.17%)</td><td>0.63 <b>(+156.68%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102636.90 (n/a)</td><td>102587.46 (n/a)</td><td>102587.70 (n/a)</td><td>102549.70 (n/a)</td><td>37.53 (n/a)</td><td>670.11 (n/a)</td><td>669.86 (n/a)</td><td>669.86 (n/a)</td><td>669.54 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.71 (+0.07%)</td><td>0.71 (+0.03%)</td><td>0.71 (+0.03%)</td><td>0.71 (+0.02%)</td><td>0.00 <b>(+20.19%)</b></td><td>106004.10 (-0.02%)</td><td>105911.72 (-0.03%)</td><td>105927.70 (-0.03%)</td><td>105795.60 (-0.07%)</td><td>85.67 <b>(+20.07%)</b></td><td>649.55 (+0.07%)</td><td>648.84 (+0.03%)</td><td>648.74 (+0.03%)</td><td>648.27 (+0.02%)</td><td>0.53 <b>(+20.19%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106028.50 (n/a)</td><td>105947.80 (n/a)</td><td>105963.00 (n/a)</td><td>105870.10 (n/a)</td><td>71.35 (n/a)</td><td>649.09 (n/a)</td><td>648.62 (n/a)</td><td>648.52 (n/a)</td><td>648.12 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.32 (+0.61%)</td><td>3.84 (+7.00%)</td><td>3.74 (+2.42%)</td><td>3.33 (+9.98%)</td><td>0.43 (-17.34%)</td><td>2421.40 (-9.07%)</td><td>2121.78 (-7.17%)</td><td>2154.80 (-2.37%)</td><td>1865.80 (-0.61%)</td><td>238.65 <b>(-27.78%)</b></td><td>1132.97 (+0.61%)</td><td>1006.49 (+7.00%)</td><td>981.02 (+2.42%)</td><td>873.03 (+9.98%)</td><td>113.45 (-17.34%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.29 (n/a)</td><td>3.59 (n/a)</td><td>3.65 (n/a)</td><td>3.03 (n/a)</td><td>0.52 (n/a)</td><td>2663.00 (n/a)</td><td>2285.68 (n/a)</td><td>2207.00 (n/a)</td><td>1877.20 (n/a)</td><td>330.47 (n/a)</td><td>1126.11 (n/a)</td><td>940.66 (n/a)</td><td>957.85 (n/a)</td><td>793.82 (n/a)</td><td>137.25 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.51 <b>(+22.64%)</b></td><td>0.39 (+13.99%)</td><td>0.33 (-2.59%)</td><td>0.31 (+0.67%)</td><td>0.10 <b>(+142.37%)</b></td><td>4038.50 (-0.67%)</td><td>3316.88 (-8.83%)</td><td>3784.50 (+2.66%)</td><td>2450.10 (-18.46%)</td><td>778.30 <b>(+94.73%)</b></td><td>27.39 <b>(+22.64%)</b></td><td>21.25 (+13.99%)</td><td>17.73 (-2.59%)</td><td>16.62 (+0.67%)</td><td>5.42 <b>(+142.37%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.04 (n/a)</td><td>4065.60 (n/a)</td><td>3638.26 (n/a)</td><td>3686.50 (n/a)</td><td>3004.70 (n/a)</td><td>399.69 (n/a)</td><td>22.33 (n/a)</td><td>18.64 (n/a)</td><td>18.20 (n/a)</td><td>16.51 (n/a)</td><td>2.23 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>6.40 (-6.92%)</td><td>4.53 (-7.96%)</td><td>4.58 (-5.06%)</td><td>3.28 (+1.18%)</td><td>1.21 (-6.03%)</td><td>2027.30 (-1.16%)</td><td>1548.76 (+8.33%)</td><td>1451.30 (+5.33%)</td><td>1039.60 (+7.43%)</td><td>385.62 (-1.11%)</td><td>1976.94 (-6.92%)</td><td>1399.94 (-7.96%)</td><td>1416.09 (-5.06%)</td><td>1013.77 (+1.18%)</td><td>374.56 (-6.03%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>6.87 (n/a)</td><td>4.92 (n/a)</td><td>4.83 (n/a)</td><td>3.24 (n/a)</td><td>1.29 (n/a)</td><td>2051.10 (n/a)</td><td>1429.70 (n/a)</td><td>1377.90 (n/a)</td><td>967.70 (n/a)</td><td>389.97 (n/a)</td><td>2123.91 (n/a)</td><td>1521.03 (n/a)</td><td>1491.60 (n/a)</td><td>1001.99 (n/a)</td><td>398.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>13.50 (n/a)</td><td>12.78 (n/a)</td><td>13.05 (n/a)</td><td>11.49 (n/a)</td><td>0.77 (n/a)</td><td>13.49 (n/a)</td><td>12.78 (n/a)</td><td>13.04 (n/a)</td><td>11.48 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>25.36 (+0.94%)</td><td>23.94 (-2.01%)</td><td>23.83 (-3.29%)</td><td>22.11 (-5.09%)</td><td>1.26 <b>(+78.01%)</b></td><td>25.35 (+0.94%)</td><td>23.92 (-2.01%)</td><td>23.81 (-3.29%)</td><td>22.10 (-5.09%)</td><td>1.26 <b>(+78.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>25.13 (n/a)</td><td>24.43 (n/a)</td><td>24.64 (n/a)</td><td>23.30 (n/a)</td><td>0.71 (n/a)</td><td>25.11 (n/a)</td><td>24.41 (n/a)</td><td>24.62 (n/a)</td><td>23.29 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>41.56 (-1.98%)</td><td>39.86 (-0.12%)</td><td>39.60 (+0.87%)</td><td>38.84 (+2.85%)</td><td>1.06 <b>(-41.46%)</b></td><td>41.53 (-1.98%)</td><td>39.83 (-0.12%)</td><td>39.58 (+0.87%)</td><td>38.82 (+2.85%)</td><td>1.06 <b>(-41.46%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>42.40 (n/a)</td><td>39.91 (n/a)</td><td>39.26 (n/a)</td><td>37.77 (n/a)</td><td>1.81 (n/a)</td><td>42.37 (n/a)</td><td>39.88 (n/a)</td><td>39.24 (n/a)</td><td>37.74 (n/a)</td><td>1.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>44.49 (-1.19%)</td><td>42.99 (-0.25%)</td><td>43.34 (+1.06%)</td><td>40.63 (+0.08%)</td><td>1.47 <b>(-22.64%)</b></td><td>44.46 (-1.19%)</td><td>42.96 (-0.25%)</td><td>43.31 (+1.06%)</td><td>40.61 (+0.08%)</td><td>1.47 <b>(-22.64%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>45.03 (n/a)</td><td>43.10 (n/a)</td><td>42.89 (n/a)</td><td>40.60 (n/a)</td><td>1.90 (n/a)</td><td>45.00 (n/a)</td><td>43.07 (n/a)</td><td>42.86 (n/a)</td><td>40.58 (n/a)</td><td>1.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>13.60 (n/a)</td><td>12.95 (n/a)</td><td>13.18 (n/a)</td><td>11.41 (n/a)</td><td>0.89 (n/a)</td><td>13.59 (n/a)</td><td>12.94 (n/a)</td><td>13.17 (n/a)</td><td>11.40 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>24.80 (+2.21%)</td><td>24.66 (+3.43%)</td><td>24.70 (+3.99%)</td><td>24.48 (+4.48%)</td><td>0.12 <b>(-68.93%)</b></td><td>24.78 (+2.21%)</td><td>24.64 (+3.43%)</td><td>24.68 (+3.99%)</td><td>24.47 (+4.48%)</td><td>0.12 <b>(-68.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>24.26 (n/a)</td><td>23.84 (n/a)</td><td>23.75 (n/a)</td><td>23.43 (n/a)</td><td>0.40 (n/a)</td><td>24.25 (n/a)</td><td>23.82 (n/a)</td><td>23.73 (n/a)</td><td>23.42 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>41.56 (+4.52%)</td><td>40.19 (+4.13%)</td><td>40.29 (+4.25%)</td><td>39.15 (+4.52%)</td><td>1.05 (+15.17%)</td><td>41.54 (+4.52%)</td><td>40.16 (+4.13%)</td><td>40.27 (+4.25%)</td><td>39.13 (+4.52%)</td><td>1.05 (+15.17%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>39.76 (n/a)</td><td>38.59 (n/a)</td><td>38.65 (n/a)</td><td>37.46 (n/a)</td><td>0.91 (n/a)</td><td>39.74 (n/a)</td><td>38.57 (n/a)</td><td>38.63 (n/a)</td><td>37.44 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>46.41 (+3.68%)</td><td>44.00 (+5.50%)</td><td>43.77 (+8.19%)</td><td>40.56 (+1.49%)</td><td>2.24 (+6.56%)</td><td>46.38 (+3.68%)</td><td>43.97 (+5.50%)</td><td>43.75 (+8.19%)</td><td>40.53 (+1.49%)</td><td>2.24 (+6.56%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>44.76 (n/a)</td><td>41.71 (n/a)</td><td>40.46 (n/a)</td><td>39.96 (n/a)</td><td>2.10 (n/a)</td><td>44.74 (n/a)</td><td>41.68 (n/a)</td><td>40.44 (n/a)</td><td>39.94 (n/a)</td><td>2.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>9.27 (+6.47%)</td><td>8.33 (-0.75%)</td><td>8.40 (-1.98%)</td><td>7.43 (-2.84%)</td><td>0.71 <b>(+66.93%)</b></td><td>9.26 (+6.47%)</td><td>8.31 (-0.75%)</td><td>8.39 (-1.98%)</td><td>7.41 (-2.84%)</td><td>0.71 <b>(+66.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>8.71 (n/a)</td><td>8.39 (n/a)</td><td>8.57 (n/a)</td><td>7.65 (n/a)</td><td>0.43 (n/a)</td><td>8.69 (n/a)</td><td>8.37 (n/a)</td><td>8.55 (n/a)</td><td>7.63 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.05 (-1.57%)</td><td>0.88 (-3.66%)</td><td>0.81 (-9.39%)</td><td>0.77 (-5.05%)</td><td>0.12 <b>(+23.98%)</b></td><td>1.03 (-1.57%)</td><td>0.86 (-3.66%)</td><td>0.79 (-9.39%)</td><td>0.76 (-5.05%)</td><td>0.12 <b>(+23.98%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.06 (n/a)</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.81 (n/a)</td><td>0.10 (n/a)</td><td>1.05 (n/a)</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.80 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.14 (-12.37%)</td><td>1.07 (-2.47%)</td><td>1.08 (-1.50%)</td><td>1.01 (+12.96%)</td><td>0.05 <b>(-67.03%)</b></td><td>1.13 (-12.37%)</td><td>1.06 (-2.47%)</td><td>1.07 (-1.50%)</td><td>1.00 (+12.96%)</td><td>0.05 <b>(-67.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.31 (n/a)</td><td>1.10 (n/a)</td><td>1.10 (n/a)</td><td>0.89 (n/a)</td><td>0.15 (n/a)</td><td>1.29 (n/a)</td><td>1.09 (n/a)</td><td>1.09 (n/a)</td><td>0.88 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>17.55 (-4.94%)</td><td>16.65 (+5.27%)</td><td>17.17 (+7.57%)</td><td>15.56 (+16.43%)</td><td>0.94 <b>(-55.11%)</b></td><td>17.35 (-4.93%)</td><td>16.46 (+5.27%)</td><td>16.97 (+7.57%)</td><td>15.38 (+16.43%)</td><td>0.93 <b>(-55.11%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>18.46 (n/a)</td><td>15.82 (n/a)</td><td>15.96 (n/a)</td><td>13.36 (n/a)</td><td>2.09 (n/a)</td><td>18.25 (n/a)</td><td>15.63 (n/a)</td><td>15.77 (n/a)</td><td>13.21 (n/a)</td><td>2.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>13.28 (+2.25%)</td><td>13.14 (+5.01%)</td><td>13.21 (+3.78%)</td><td>12.84 (+11.97%)</td><td>0.17 <b>(-71.31%)</b></td><td>13.04 (+2.25%)</td><td>12.91 (+5.01%)</td><td>12.97 (+3.78%)</td><td>12.62 (+11.97%)</td><td>0.17 <b>(-71.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>12.99 (n/a)</td><td>12.52 (n/a)</td><td>12.73 (n/a)</td><td>11.47 (n/a)</td><td>0.60 (n/a)</td><td>12.76 (n/a)</td><td>12.30 (n/a)</td><td>12.50 (n/a)</td><td>11.27 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.36 (-4.29%)</td><td>7.15 (+8.19%)</td><td>7.27 (+7.08%)</td><td>6.85 <b>(+32.84%)</b></td><td>0.23 <b>(-76.94%)</b></td><td>7.23 (-4.29%)</td><td>7.02 (+8.19%)</td><td>7.15 (+7.08%)</td><td>6.73 <b>(+32.84%)</b></td><td>0.23 <b>(-76.94%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.69 (n/a)</td><td>6.61 (n/a)</td><td>6.79 (n/a)</td><td>5.16 (n/a)</td><td>1.00 (n/a)</td><td>7.56 (n/a)</td><td>6.49 (n/a)</td><td>6.68 (n/a)</td><td>5.07 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>5.86 (-10.84%)</td><td>5.16 (-7.46%)</td><td>4.96 (-12.63%)</td><td>4.75 <b>(+24.51%)</b></td><td>0.47 <b>(-58.05%)</b></td><td>5.77 (-10.84%)</td><td>5.08 (-7.46%)</td><td>4.88 (-12.63%)</td><td>4.67 <b>(+24.51%)</b></td><td>0.46 <b>(-58.05%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>6.57 (n/a)</td><td>5.58 (n/a)</td><td>5.67 (n/a)</td><td>3.81 (n/a)</td><td>1.12 (n/a)</td><td>6.47 (n/a)</td><td>5.49 (n/a)</td><td>5.58 (n/a)</td><td>3.75 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>13.39 (n/a)</td><td>12.76 (n/a)</td><td>12.95 (n/a)</td><td>12.08 (n/a)</td><td>0.63 (n/a)</td><td>13.38 (n/a)</td><td>12.75 (n/a)</td><td>12.94 (n/a)</td><td>12.08 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>13.25 (n/a)</td><td>12.25 (n/a)</td><td>12.51 (n/a)</td><td>11.05 (n/a)</td><td>0.94 (n/a)</td><td>13.25 (n/a)</td><td>12.24 (n/a)</td><td>12.50 (n/a)</td><td>11.05 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.70 (n/a)</td><td>179.68 (n/a)</td><td>181.80 (n/a)</td><td>173.10 (n/a)</td><td>5.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.00 (n/a)</td><td>167.82 (n/a)</td><td>176.40 (n/a)</td><td>121.20 (n/a)</td><td>37.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.90 (n/a)</td><td>159.14 (n/a)</td><td>158.90 (n/a)</td><td>132.10 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.50 (n/a)</td><td>165.68 (n/a)</td><td>156.30 (n/a)</td><td>141.30 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.70 (n/a)</td><td>177.50 (n/a)</td><td>169.40 (n/a)</td><td>148.20 (n/a)</td><td>32.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>262.20 (n/a)</td><td>199.42 (n/a)</td><td>206.20 (n/a)</td><td>154.50 (n/a)</td><td>42.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>307.60 (n/a)</td><td>211.32 (n/a)</td><td>177.00 (n/a)</td><td>149.80 (n/a)</td><td>67.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.50 (n/a)</td><td>213.80 (n/a)</td><td>217.60 (n/a)</td><td>182.90 (n/a)</td><td>22.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>154.20 (n/a)</td><td>156.20 (n/a)</td><td>116.30 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>180.14 (n/a)</td><td>178.60 (n/a)</td><td>163.90 (n/a)</td><td>15.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.80 (n/a)</td><td>189.34 (n/a)</td><td>179.70 (n/a)</td><td>168.30 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.30 (n/a)</td><td>177.04 (n/a)</td><td>169.40 (n/a)</td><td>116.30 (n/a)</td><td>46.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.20 (n/a)</td><td>165.68 (n/a)</td><td>166.90 (n/a)</td><td>133.50 (n/a)</td><td>34.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.20 (n/a)</td><td>191.28 (n/a)</td><td>185.70 (n/a)</td><td>133.90 (n/a)</td><td>38.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>185.24 (n/a)</td><td>195.40 (n/a)</td><td>146.40 (n/a)</td><td>23.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>187.92 (n/a)</td><td>187.70 (n/a)</td><td>160.10 (n/a)</td><td>27.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>187.70 (n/a)</td><td>170.68 (n/a)</td><td>171.70 (n/a)</td><td>147.80 (n/a)</td><td>14.63 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.50 (n/a)</td><td>172.10 (n/a)</td><td>164.60 (n/a)</td><td>136.10 (n/a)</td><td>36.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>168.68 (n/a)</td><td>174.00 (n/a)</td><td>134.20 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>168.42 (n/a)</td><td>172.90 (n/a)</td><td>147.40 (n/a)</td><td>18.16 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.40 (n/a)</td><td>160.56 (n/a)</td><td>172.10 (n/a)</td><td>130.50 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.30 (n/a)</td><td>177.82 (n/a)</td><td>186.70 (n/a)</td><td>139.40 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.20 (n/a)</td><td>189.12 (n/a)</td><td>187.00 (n/a)</td><td>145.50 (n/a)</td><td>32.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>203.98 (n/a)</td><td>192.70 (n/a)</td><td>187.60 (n/a)</td><td>18.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>345.40 (n/a)</td><td>217.76 (n/a)</td><td>197.90 (n/a)</td><td>142.70 (n/a)</td><td>78.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>298.60 (n/a)</td><td>233.16 (n/a)</td><td>207.00 (n/a)</td><td>177.90 (n/a)</td><td>52.76 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.40 (n/a)</td><td>168.62 (n/a)</td><td>165.20 (n/a)</td><td>137.40 (n/a)</td><td>34.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>209.30 (n/a)</td><td>169.74 (n/a)</td><td>172.30 (n/a)</td><td>109.50 (n/a)</td><td>40.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>321.60 (n/a)</td><td>237.54 (n/a)</td><td>237.90 (n/a)</td><td>160.90 (n/a)</td><td>71.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>200.90 (n/a)</td><td>188.80 (n/a)</td><td>187.90 (n/a)</td><td>168.00 (n/a)</td><td>13.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>196.52 (n/a)</td><td>199.00 (n/a)</td><td>183.70 (n/a)</td><td>7.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>264.30 (n/a)</td><td>241.02 (n/a)</td><td>232.20 (n/a)</td><td>219.70 (n/a)</td><td>19.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (+17.85%)</td><td>0.03 (+11.98%)</td><td>0.03 (+8.70%)</td><td>0.02 (+11.54%)</td><td>0.01 <b>(+38.22%)</b></td><td>198.70 (-10.33%)</td><td>151.66 (-9.78%)</td><td>147.50 (-7.99%)</td><td>116.70 (-15.19%)</td><td>32.72 (+1.88%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.60 (n/a)</td><td>168.10 (n/a)</td><td>160.30 (n/a)</td><td>137.60 (n/a)</td><td>32.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(+25.75%)</b></td><td>0.03 (+4.85%)</td><td>0.03 (-2.41%)</td><td>0.02 (+11.93%)</td><td>0.01 <b>(+71.60%)</b></td><td>174.70 (-10.64%)</td><td>156.42 (-3.38%)</td><td>163.00 (+2.45%)</td><td>113.10 <b>(-20.46%)</b></td><td>24.87 (+18.12%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.50 (n/a)</td><td>161.90 (n/a)</td><td>159.10 (n/a)</td><td>142.20 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (+10.79%)</td><td>0.03 (+9.85%)</td><td>0.03 (+17.49%)</td><td>0.02 (+15.36%)</td><td>0.00 (-14.69%)</td><td>181.30 (-13.34%)</td><td>162.42 (-9.80%)</td><td>161.90 (-14.88%)</td><td>132.60 (-9.73%)</td><td>19.35 <b>(-32.73%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.20 (n/a)</td><td>180.06 (n/a)</td><td>190.20 (n/a)</td><td>146.90 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-12.72%)</td><td>0.02 (+5.87%)</td><td>0.02 (+13.31%)</td><td>0.02 <b>(+25.16%)</b></td><td>0.00 <b>(-50.57%)</b></td><td>192.30 <b>(-20.11%)</b></td><td>167.92 (-9.55%)</td><td>171.30 (-11.75%)</td><td>134.90 (+14.52%)</td><td>20.70 <b>(-53.97%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.70 (n/a)</td><td>185.64 (n/a)</td><td>194.10 (n/a)</td><td>117.80 (n/a)</td><td>44.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (+11.43%)</td><td>0.03 (+4.29%)</td><td>0.02 (-1.70%)</td><td>0.02 (+14.32%)</td><td>0.01 (+17.33%)</td><td>197.20 (-12.55%)</td><td>168.38 (-3.96%)</td><td>173.10 (+1.70%)</td><td>117.60 (-10.23%)</td><td>30.59 (-11.07%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.50 (n/a)</td><td>175.32 (n/a)</td><td>170.20 (n/a)</td><td>131.00 (n/a)</td><td>34.39 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-9.94%)</td><td>0.03 (+3.42%)</td><td>0.02 (+4.28%)</td><td>0.02 (+8.02%)</td><td>0.00 <b>(-40.57%)</b></td><td>176.00 (-7.42%)</td><td>162.94 (-4.58%)</td><td>171.70 (-4.08%)</td><td>140.40 (+11.08%)</td><td>16.12 <b>(-36.21%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.10 (n/a)</td><td>170.76 (n/a)</td><td>179.00 (n/a)</td><td>126.40 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-19.52%)</td><td>0.02 (+0.08%)</td><td>0.02 (+9.08%)</td><td>0.02 (+12.37%)</td><td>0.00 <b>(-57.49%)</b></td><td>201.80 (-11.02%)</td><td>180.40 (-3.98%)</td><td>189.70 (-8.31%)</td><td>158.40 <b>(+24.24%)</b></td><td>19.72 <b>(-54.59%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.80 (n/a)</td><td>187.88 (n/a)</td><td>206.90 (n/a)</td><td>127.50 (n/a)</td><td>43.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (-10.33%)</td><td>0.02 (-5.03%)</td><td>0.02 (-7.93%)</td><td>0.02 (-0.94%)</td><td>0.00 <b>(-48.64%)</b></td><td>236.10 (+0.94%)</td><td>210.46 (+4.33%)</td><td>206.20 (+8.58%)</td><td>196.70 (+11.51%)</td><td>15.16 <b>(-41.86%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.90 (n/a)</td><td>201.72 (n/a)</td><td>189.90 (n/a)</td><td>176.40 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (-11.97%)</td><td>0.05 (+3.67%)</td><td>0.05 (+3.80%)</td><td>0.04 (+3.58%)</td><td>0.01 <b>(-25.07%)</b></td><td>194.10 (-3.48%)</td><td>163.58 (-4.99%)</td><td>174.60 (-3.64%)</td><td>131.00 (+13.62%)</td><td>28.38 (-17.85%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.10 (n/a)</td><td>172.18 (n/a)</td><td>181.20 (n/a)</td><td>115.30 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 <b>(+26.90%)</b></td><td>0.06 <b>(+24.15%)</b></td><td>0.06 <b>(+21.89%)</b></td><td>0.05 <b>(+34.21%)</b></td><td>0.01 (-5.37%)</td><td>151.20 <b>(-25.52%)</b></td><td>137.64 (-19.97%)</td><td>135.20 (-17.96%)</td><td>119.10 <b>(-21.18%)</b></td><td>13.17 <b>(-43.33%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>171.98 (n/a)</td><td>164.80 (n/a)</td><td>151.10 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (-5.61%)</td><td>0.05 <b>(+20.07%)</b></td><td>0.06 <b>(+42.04%)</b></td><td>0.04 <b>(+31.65%)</b></td><td>0.01 <b>(-29.86%)</b></td><td>193.50 <b>(-24.06%)</b></td><td>153.56 (-19.91%)</td><td>144.00 <b>(-29.58%)</b></td><td>122.60 (+5.87%)</td><td>30.37 <b>(-40.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.80 (n/a)</td><td>191.74 (n/a)</td><td>204.50 (n/a)</td><td>115.80 (n/a)</td><td>50.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 <b>(-23.10%)</b></td><td>0.06 (+4.23%)</td><td>0.06 <b>(+27.32%)</b></td><td>0.05 <b>(+36.97%)</b></td><td>0.00 <b>(-76.31%)</b></td><td>165.40 <b>(-27.01%)</b></td><td>147.14 (-13.32%)</td><td>146.70 <b>(-21.47%)</b></td><td>133.10 <b>(+30.11%)</b></td><td>12.92 <b>(-77.64%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>226.60 (n/a)</td><td>169.76 (n/a)</td><td>186.80 (n/a)</td><td>102.30 (n/a)</td><td>57.76 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (-14.54%)</td><td>0.05 (+4.72%)</td><td>0.05 <b>(+25.00%)</b></td><td>0.04 (+6.42%)</td><td>0.01 <b>(-38.69%)</b></td><td>206.20 (-6.02%)</td><td>164.24 (-7.50%)</td><td>151.90 (-19.97%)</td><td>135.60 (+17.10%)</td><td>29.12 <b>(-32.36%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.40 (n/a)</td><td>177.56 (n/a)</td><td>189.80 (n/a)</td><td>115.80 (n/a)</td><td>43.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (+0.74%)</td><td>0.05 (-6.12%)</td><td>0.04 (-12.34%)</td><td>0.04 (-0.64%)</td><td>0.01 (+14.64%)</td><td>213.00 (+0.66%)</td><td>177.30 (+7.74%)</td><td>184.10 (+14.06%)</td><td>117.20 (-0.76%)</td><td>38.50 (+15.50%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>164.56 (n/a)</td><td>161.40 (n/a)</td><td>118.10 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (+2.40%)</td><td>0.05 (+4.97%)</td><td>0.04 (-4.99%)</td><td>0.04 (-0.13%)</td><td>0.01 (+17.49%)</td><td>204.90 (+0.15%)</td><td>172.64 (-3.47%)</td><td>198.20 (+5.26%)</td><td>121.20 (-2.42%)</td><td>38.92 <b>(+20.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>178.84 (n/a)</td><td>188.30 (n/a)</td><td>124.20 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 <b>(+28.33%)</b></td><td>0.05 (+19.81%)</td><td>0.05 (+15.86%)</td><td>0.04 (+18.76%)</td><td>0.01 <b>(+42.34%)</b></td><td>198.00 (-15.82%)</td><td>171.82 (-16.10%)</td><td>176.80 (-13.67%)</td><td>131.10 <b>(-22.06%)</b></td><td>27.41 (-8.15%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.20 (n/a)</td><td>204.80 (n/a)</td><td>204.80 (n/a)</td><td>168.20 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 <b>(+20.64%)</b></td><td>0.05 (+14.50%)</td><td>0.05 (+11.57%)</td><td>0.04 (+17.51%)</td><td>0.01 <b>(+22.17%)</b></td><td>205.40 (-14.91%)</td><td>177.46 (-12.63%)</td><td>181.90 (-10.35%)</td><td>130.00 (-17.09%)</td><td>28.85 (-17.33%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.40 (n/a)</td><td>203.12 (n/a)</td><td>202.90 (n/a)</td><td>156.80 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(-41.18%)</b></td><td>0.04 (-13.82%)</td><td>0.04 (+6.11%)</td><td>0.04 (+0.65%)</td><td>0.00 <b>(-84.45%)</b></td><td>223.40 (-0.62%)</td><td>210.20 (+8.99%)</td><td>207.60 (-5.76%)</td><td>195.50 <b>(+70.00%)</b></td><td>12.49 <b>(-73.39%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>192.86 (n/a)</td><td>220.30 (n/a)</td><td>115.00 (n/a)</td><td>46.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 <b>(+21.03%)</b></td><td>0.11 (+16.40%)</td><td>0.10 (+4.49%)</td><td>0.09 <b>(+35.59%)</b></td><td>0.03 (+16.52%)</td><td>173.20 <b>(-26.24%)</b></td><td>148.64 (-14.66%)</td><td>163.20 (-4.28%)</td><td>104.20 (-17.43%)</td><td>30.64 <b>(-27.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.80 (n/a)</td><td>174.18 (n/a)</td><td>170.50 (n/a)</td><td>126.20 (n/a)</td><td>42.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (+12.31%)</td><td>0.11 (+6.17%)</td><td>0.10 (-5.99%)</td><td>0.09 (+1.80%)</td><td>0.03 <b>(+59.26%)</b></td><td>177.50 (-1.77%)</td><td>150.72 (-3.80%)</td><td>167.60 (+6.35%)</td><td>110.10 (-10.99%)</td><td>31.09 <b>(+43.63%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.70 (n/a)</td><td>156.68 (n/a)</td><td>157.60 (n/a)</td><td>123.70 (n/a)</td><td>21.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (+18.71%)</td><td>0.11 (+1.86%)</td><td>0.10 (-2.98%)</td><td>0.09 (-9.22%)</td><td>0.02 <b>(+215.20%)</b></td><td>182.90 (+10.18%)</td><td>156.48 (-0.22%)</td><td>158.40 (+3.06%)</td><td>125.00 (-15.71%)</td><td>22.81 <b>(+189.84%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>166.00 (n/a)</td><td>156.82 (n/a)</td><td>153.70 (n/a)</td><td>148.30 (n/a)</td><td>7.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (-2.43%)</td><td>0.11 (+12.89%)</td><td>0.11 (+12.44%)</td><td>0.09 <b>(+22.33%)</b></td><td>0.02 (-18.33%)</td><td>192.50 (-18.26%)</td><td>156.40 (-13.31%)</td><td>156.00 (-11.06%)</td><td>119.70 (+2.48%)</td><td>30.91 <b>(-28.84%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>235.50 (n/a)</td><td>180.42 (n/a)</td><td>175.40 (n/a)</td><td>116.80 (n/a)</td><td>43.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 <b>(+30.04%)</b></td><td>0.10 (+6.52%)</td><td>0.10 (-2.03%)</td><td>0.09 (+1.28%)</td><td>0.02 <b>(+119.46%)</b></td><td>190.20 (-1.30%)</td><td>165.54 (-4.36%)</td><td>168.20 (+2.06%)</td><td>121.90 <b>(-23.09%)</b></td><td>27.72 <b>(+65.11%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.70 (n/a)</td><td>173.08 (n/a)</td><td>164.80 (n/a)</td><td>158.50 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 <b>(+21.98%)</b></td><td>0.11 (+18.41%)</td><td>0.11 <b>(+29.48%)</b></td><td>0.08 (+7.67%)</td><td>0.03 <b>(+53.48%)</b></td><td>216.20 (-7.13%)</td><td>160.88 (-13.03%)</td><td>152.40 <b>(-22.76%)</b></td><td>113.00 (-18.00%)</td><td>45.88 (+19.56%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.80 (n/a)</td><td>184.98 (n/a)</td><td>197.30 (n/a)</td><td>137.80 (n/a)</td><td>38.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (+12.49%)</td><td>0.12 (+18.31%)</td><td>0.11 <b>(+26.65%)</b></td><td>0.08 (+3.48%)</td><td>0.03 <b>(+22.13%)</b></td><td>201.60 (-3.36%)</td><td>151.20 (-14.31%)</td><td>150.60 <b>(-21.03%)</b></td><td>102.40 (-11.03%)</td><td>40.39 (+6.97%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>208.60 (n/a)</td><td>176.46 (n/a)</td><td>190.70 (n/a)</td><td>115.10 (n/a)</td><td>37.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 <b>(+45.65%)</b></td><td>0.09 (+14.55%)</td><td>0.08 (+11.10%)</td><td>0.07 (+9.83%)</td><td>0.03 <b>(+107.41%)</b></td><td>218.80 (-8.95%)</td><td>193.52 (-9.72%)</td><td>213.70 (-9.98%)</td><td>118.30 <b>(-31.34%)</b></td><td>42.44 <b>(+24.71%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.30 (n/a)</td><td>214.36 (n/a)</td><td>237.40 (n/a)</td><td>172.30 (n/a)</td><td>34.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (+15.09%)</td><td>0.20 (+0.59%)</td><td>0.19 (-6.38%)</td><td>0.16 (-3.62%)</td><td>0.04 <b>(+81.25%)</b></td><td>200.10 (+3.79%)</td><td>170.32 (+1.10%)</td><td>176.40 (+6.78%)</td><td>127.50 (-13.09%)</td><td>28.84 <b>(+61.65%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>192.80 (n/a)</td><td>168.46 (n/a)</td><td>165.20 (n/a)</td><td>146.70 (n/a)</td><td>17.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.24 (+7.86%)</td><td>0.21 (+3.49%)</td><td>0.22 (+10.16%)</td><td>0.18 (-2.74%)</td><td>0.03 <b>(+82.99%)</b></td><td>183.90 (+2.85%)</td><td>159.32 (-2.41%)</td><td>150.90 (-9.21%)</td><td>136.10 (-7.29%)</td><td>21.25 <b>(+79.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>163.26 (n/a)</td><td>166.20 (n/a)</td><td>146.80 (n/a)</td><td>11.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 (+5.35%)</td><td>0.21 <b>(+20.54%)</b></td><td>0.22 (+14.56%)</td><td>0.17 <b>(+50.53%)</b></td><td>0.03 <b>(-38.19%)</b></td><td>197.40 <b>(-33.56%)</b></td><td>161.62 <b>(-20.68%)</b></td><td>151.80 (-12.71%)</td><td>141.00 (-5.11%)</td><td>22.79 <b>(-61.55%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>297.10 (n/a)</td><td>203.76 (n/a)</td><td>173.90 (n/a)</td><td>148.60 (n/a)</td><td>59.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.24 (-4.99%)</td><td>0.19 (-2.76%)</td><td>0.18 (-7.72%)</td><td>0.14 (+3.15%)</td><td>0.04 (-5.45%)</td><td>226.90 (-3.08%)</td><td>178.26 (+2.46%)</td><td>183.30 (+8.40%)</td><td>134.90 (+5.23%)</td><td>36.34 (-5.76%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>234.10 (n/a)</td><td>173.98 (n/a)</td><td>169.10 (n/a)</td><td>128.20 (n/a)</td><td>38.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 (-12.01%)</td><td>0.18 (+5.92%)</td><td>0.18 <b>(+28.70%)</b></td><td>0.15 (+9.50%)</td><td>0.03 <b>(-39.50%)</b></td><td>222.50 (-8.66%)</td><td>183.50 (-9.21%)</td><td>180.00 <b>(-22.31%)</b></td><td>143.20 (+13.65%)</td><td>31.69 <b>(-37.71%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>243.60 (n/a)</td><td>202.12 (n/a)</td><td>231.70 (n/a)</td><td>126.00 (n/a)</td><td>50.88 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (+9.87%)</td><td>0.20 (+10.15%)</td><td>0.18 (+2.12%)</td><td>0.16 (+11.45%)</td><td>0.05 <b>(+23.95%)</b></td><td>207.20 (-10.30%)</td><td>170.98 (-8.54%)</td><td>177.40 (-2.10%)</td><td>131.20 (-8.95%)</td><td>37.36 (-1.19%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>231.00 (n/a)</td><td>186.94 (n/a)</td><td>181.20 (n/a)</td><td>144.10 (n/a)</td><td>37.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (-15.34%)</td><td>0.15 (+3.48%)</td><td>0.15 (+4.89%)</td><td>0.14 <b>(+49.95%)</b></td><td>0.01 <b>(-67.05%)</b></td><td>236.80 <b>(-33.30%)</b></td><td>221.52 (-8.57%)</td><td>221.70 (-4.69%)</td><td>192.70 (+18.15%)</td><td>17.59 <b>(-74.75%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>355.00 (n/a)</td><td>242.28 (n/a)</td><td>232.60 (n/a)</td><td>163.10 (n/a)</td><td>69.66 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-12.99%)</td><td>0.02 (-9.65%)</td><td>0.02 (-12.33%)</td><td>0.02 (-10.07%)</td><td>0.00 (-9.13%)</td><td>207.60 (+11.19%)</td><td>168.86 (+10.77%)</td><td>176.90 (+14.06%)</td><td>137.30 (+14.99%)</td><td>29.78 (+13.09%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.70 (n/a)</td><td>152.44 (n/a)</td><td>155.10 (n/a)</td><td>119.40 (n/a)</td><td>26.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-12.14%)</td><td>0.02 (-11.17%)</td><td>0.02 (-7.54%)</td><td>0.02 <b>(-28.63%)</b></td><td>0.00 <b>(+24.24%)</b></td><td>235.50 <b>(+40.10%)</b></td><td>179.32 (+14.68%)</td><td>176.00 (+8.17%)</td><td>141.40 (+13.76%)</td><td>36.71 <b>(+101.72%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>168.10 (n/a)</td><td>156.36 (n/a)</td><td>162.70 (n/a)</td><td>124.30 (n/a)</td><td>18.20 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 <b>(-22.46%)</b></td><td>0.02 <b>(-27.34%)</b></td><td>0.02 <b>(-30.20%)</b></td><td>0.02 <b>(-21.27%)</b></td><td>0.00 <b>(-35.49%)</b></td><td>272.20 <b>(+27.02%)</b></td><td>239.06 <b>(+36.75%)</b></td><td>236.70 <b>(+43.28%)</b></td><td>192.70 <b>(+28.98%)</b></td><td>30.52 (+6.22%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.30 (n/a)</td><td>174.82 (n/a)</td><td>165.20 (n/a)</td><td>149.40 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 <b>(-22.96%)</b></td><td>0.02 (-15.62%)</td><td>0.02 (-15.89%)</td><td>0.02 (-1.26%)</td><td>0.00 <b>(-57.92%)</b></td><td>238.10 (+1.28%)</td><td>210.16 (+15.31%)</td><td>209.40 (+18.84%)</td><td>179.50 <b>(+29.79%)</b></td><td>21.15 <b>(-45.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.10 (n/a)</td><td>182.26 (n/a)</td><td>176.20 (n/a)</td><td>138.30 (n/a)</td><td>38.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 <b>(-34.28%)</b></td><td>0.02 <b>(-27.46%)</b></td><td>0.02 (-19.59%)</td><td>0.01 <b>(-39.29%)</b></td><td>0.00 <b>(-31.19%)</b></td><td>288.30 <b>(+64.74%)</b></td><td>212.70 <b>(+38.62%)</b></td><td>196.30 <b>(+24.40%)</b></td><td>175.70 <b>(+52.25%)</b></td><td>43.88 <b>(+79.71%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.00 (n/a)</td><td>153.44 (n/a)</td><td>157.80 (n/a)</td><td>115.40 (n/a)</td><td>24.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 <b>(-21.85%)</b></td><td>0.02 (-11.42%)</td><td>0.02 (-6.64%)</td><td>0.02 (-12.89%)</td><td>0.00 <b>(-44.57%)</b></td><td>223.00 (+14.77%)</td><td>190.74 (+11.57%)</td><td>190.40 (+7.15%)</td><td>162.00 <b>(+27.96%)</b></td><td>21.91 (-15.24%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.30 (n/a)</td><td>170.96 (n/a)</td><td>177.70 (n/a)</td><td>126.60 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-1.55%)</td><td>0.02 (-3.44%)</td><td>0.02 (-4.56%)</td><td>0.02 (+1.47%)</td><td>0.00 (-16.63%)</td><td>208.40 (-1.42%)</td><td>182.00 (+3.01%)</td><td>175.10 (+4.79%)</td><td>153.00 (+1.59%)</td><td>23.70 (-14.69%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.40 (n/a)</td><td>176.68 (n/a)</td><td>167.10 (n/a)</td><td>150.60 (n/a)</td><td>27.78 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-17.20%)</td><td>0.02 (-10.06%)</td><td>0.02 (-18.95%)</td><td>0.02 (+9.95%)</td><td>0.00 <b>(-49.82%)</b></td><td>200.50 (-9.03%)</td><td>179.46 (+7.87%)</td><td>185.80 <b>(+23.37%)</b></td><td>147.90 <b>(+20.73%)</b></td><td>20.78 <b>(-46.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.40 (n/a)</td><td>166.36 (n/a)</td><td>150.60 (n/a)</td><td>122.50 (n/a)</td><td>38.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 <b>(-23.87%)</b></td><td>0.02 (-16.71%)</td><td>0.02 (-8.96%)</td><td>0.02 (-13.27%)</td><td>0.00 <b>(-44.18%)</b></td><td>239.20 (+15.28%)</td><td>212.32 (+18.23%)</td><td>216.50 (+9.84%)</td><td>178.10 <b>(+31.34%)</b></td><td>27.48 (-15.76%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.50 (n/a)</td><td>179.58 (n/a)</td><td>197.10 (n/a)</td><td>135.60 (n/a)</td><td>32.62 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-8.75%)</td><td>0.02 (-6.64%)</td><td>0.02 (+1.93%)</td><td>0.02 (-4.17%)</td><td>0.01 (-16.47%)</td><td>204.20 (+4.34%)</td><td>175.24 (+6.27%)</td><td>176.80 (-1.89%)</td><td>124.80 (+9.57%)</td><td>31.31 (-4.91%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>164.90 (n/a)</td><td>180.20 (n/a)</td><td>113.90 (n/a)</td><td>32.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-1.92%)</td><td>0.03 (-4.52%)</td><td>0.03 (-1.17%)</td><td>0.02 (-3.53%)</td><td>0.00 (-14.10%)</td><td>191.50 (+3.63%)</td><td>160.00 (+4.09%)</td><td>162.00 (+1.19%)</td><td>123.80 (+1.98%)</td><td>25.04 (-9.65%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>153.72 (n/a)</td><td>160.10 (n/a)</td><td>121.40 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 <b>(-29.27%)</b></td><td>0.02 (-9.28%)</td><td>0.02 (+2.29%)</td><td>0.02 <b>(+43.32%)</b></td><td>0.00 <b>(-64.69%)</b></td><td>231.40 <b>(-30.22%)</b></td><td>177.92 (-2.91%)</td><td>167.20 (-2.22%)</td><td>154.30 <b>(+41.43%)</b></td><td>30.93 <b>(-64.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>331.60 (n/a)</td><td>183.26 (n/a)</td><td>171.00 (n/a)</td><td>109.10 (n/a)</td><td>88.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-3.41%)</td><td>0.02 (+19.11%)</td><td>0.02 (+10.93%)</td><td>0.02 <b>(+78.54%)</b></td><td>0.00 <b>(-39.18%)</b></td><td>205.20 <b>(-43.98%)</b></td><td>176.62 <b>(-22.59%)</b></td><td>187.80 (-9.84%)</td><td>135.50 (+3.59%)</td><td>30.12 <b>(-64.88%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>366.30 (n/a)</td><td>228.16 (n/a)</td><td>208.30 (n/a)</td><td>130.80 (n/a)</td><td>85.76 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-16.05%)</td><td>0.02 <b>(-21.57%)</b></td><td>0.02 <b>(-31.55%)</b></td><td>0.02 (-5.76%)</td><td>0.00 <b>(-41.78%)</b></td><td>219.90 (+6.08%)</td><td>185.32 <b>(+24.54%)</b></td><td>184.50 <b>(+46.08%)</b></td><td>146.30 (+19.14%)</td><td>26.83 <b>(-26.36%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>148.80 (n/a)</td><td>126.30 (n/a)</td><td>122.80 (n/a)</td><td>36.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 <b>(-28.51%)</b></td><td>0.02 <b>(-27.61%)</b></td><td>0.02 <b>(-28.77%)</b></td><td>0.02 <b>(-26.02%)</b></td><td>0.00 <b>(-31.79%)</b></td><td>235.20 <b>(+35.17%)</b></td><td>202.14 <b>(+37.94%)</b></td><td>197.50 <b>(+40.37%)</b></td><td>181.80 <b>(+39.85%)</b></td><td>22.49 <b>(+27.15%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.00 (n/a)</td><td>146.54 (n/a)</td><td>140.70 (n/a)</td><td>130.00 (n/a)</td><td>17.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-13.32%)</td><td>0.02 <b>(-27.42%)</b></td><td>0.02 <b>(-31.52%)</b></td><td>0.02 <b>(-39.59%)</b></td><td>0.00 <b>(+97.14%)</b></td><td>256.30 <b>(+65.46%)</b></td><td>198.72 <b>(+42.21%)</b></td><td>199.30 <b>(+46.11%)</b></td><td>147.70 (+15.39%)</td><td>42.25 <b>(+272.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>154.90 (n/a)</td><td>139.74 (n/a)</td><td>136.40 (n/a)</td><td>128.00 (n/a)</td><td>11.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (-15.34%)</td><td>0.05 (-11.29%)</td><td>0.05 (-13.27%)</td><td>0.04 (+12.24%)</td><td>0.01 <b>(-49.14%)</b></td><td>207.40 (-10.91%)</td><td>171.98 (+8.55%)</td><td>173.20 (+15.31%)</td><td>146.70 (+18.12%)</td><td>23.78 <b>(-46.48%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>158.44 (n/a)</td><td>150.20 (n/a)</td><td>124.20 (n/a)</td><td>44.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 <b>(-42.00%)</b></td><td>0.05 <b>(-25.20%)</b></td><td>0.05 (-18.39%)</td><td>0.04 (-11.25%)</td><td>0.01 <b>(-66.48%)</b></td><td>228.70 (+12.66%)</td><td>184.16 <b>(+27.43%)</b></td><td>176.00 <b>(+22.56%)</b></td><td>162.70 <b>(+72.53%)</b></td><td>26.56 <b>(-33.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>203.00 (n/a)</td><td>144.52 (n/a)</td><td>143.60 (n/a)</td><td>94.30 (n/a)</td><td>39.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (+2.68%)</td><td>0.04 (+7.35%)</td><td>0.03 (-4.26%)</td><td>0.03 <b>(+25.79%)</b></td><td>0.00 <b>(-57.04%)</b></td><td>253.70 <b>(-20.50%)</b></td><td>232.48 (-8.67%)</td><td>235.80 (+4.43%)</td><td>213.90 (-2.60%)</td><td>15.16 <b>(-66.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.10 (n/a)</td><td>254.56 (n/a)</td><td>225.80 (n/a)</td><td>219.60 (n/a)</td><td>44.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (-13.88%)</td><td>0.04 (-6.13%)</td><td>0.04 (-5.15%)</td><td>0.04 (-0.13%)</td><td>0.00 <b>(-44.71%)</b></td><td>231.10 (+0.13%)</td><td>208.38 (+5.67%)</td><td>208.00 (+5.42%)</td><td>188.60 (+16.13%)</td><td>15.84 <b>(-34.92%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>197.20 (n/a)</td><td>197.30 (n/a)</td><td>162.40 (n/a)</td><td>24.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (+2.61%)</td><td>0.05 (-16.48%)</td><td>0.04 <b>(-23.89%)</b></td><td>0.04 <b>(-22.00%)</b></td><td>0.01 <b>(+82.76%)</b></td><td>211.40 <b>(+28.20%)</b></td><td>176.72 <b>(+23.17%)</b></td><td>190.70 <b>(+31.43%)</b></td><td>122.30 (-2.55%)</td><td>34.94 <b>(+124.50%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>164.90 (n/a)</td><td>143.48 (n/a)</td><td>145.10 (n/a)</td><td>125.50 (n/a)</td><td>15.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 <b>(-27.65%)</b></td><td>0.05 (-12.30%)</td><td>0.05 (+3.05%)</td><td>0.04 (-2.16%)</td><td>0.00 <b>(-75.67%)</b></td><td>190.90 (+2.19%)</td><td>176.48 (+9.76%)</td><td>179.10 (-2.93%)</td><td>161.90 <b>(+38.14%)</b></td><td>11.51 <b>(-66.68%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.80 (n/a)</td><td>160.78 (n/a)</td><td>184.50 (n/a)</td><td>117.20 (n/a)</td><td>34.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (-17.47%)</td><td>0.04 (-17.05%)</td><td>0.05 (-15.19%)</td><td>0.03 <b>(-25.97%)</b></td><td>0.01 (-4.33%)</td><td>258.00 <b>(+35.08%)</b></td><td>189.38 <b>(+21.90%)</b></td><td>169.60 (+17.94%)</td><td>154.60 <b>(+21.16%)</b></td><td>42.21 <b>(+56.27%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>155.36 (n/a)</td><td>143.80 (n/a)</td><td>127.60 (n/a)</td><td>27.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 <b>(+22.17%)</b></td><td>0.05 (+10.01%)</td><td>0.05 (+4.10%)</td><td>0.04 (+12.34%)</td><td>0.01 <b>(+34.33%)</b></td><td>214.50 (-11.00%)</td><td>166.28 (-8.35%)</td><td>171.60 (-3.97%)</td><td>116.30 (-18.16%)</td><td>36.10 (-5.03%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.00 (n/a)</td><td>181.42 (n/a)</td><td>178.70 (n/a)</td><td>142.10 (n/a)</td><td>38.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (+15.82%)</td><td>0.05 <b>(+20.26%)</b></td><td>0.06 <b>(+30.40%)</b></td><td>0.04 (+3.96%)</td><td>0.01 <b>(+60.76%)</b></td><td>219.60 (-3.81%)</td><td>156.22 (-15.04%)</td><td>132.40 <b>(-23.29%)</b></td><td>130.40 (-13.64%)</td><td>38.67 <b>(+29.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.30 (n/a)</td><td>183.88 (n/a)</td><td>172.60 (n/a)</td><td>151.00 (n/a)</td><td>29.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (+19.79%)</td><td>0.05 (-1.41%)</td><td>0.05 (-8.41%)</td><td>0.04 (-16.33%)</td><td>0.01 <b>(+136.81%)</b></td><td>233.30 (+19.52%)</td><td>179.02 (+6.17%)</td><td>180.40 (+9.20%)</td><td>122.10 (-16.54%)</td><td>45.79 <b>(+136.46%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.20 (n/a)</td><td>168.62 (n/a)</td><td>165.20 (n/a)</td><td>146.30 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (+7.70%)</td><td>0.04 (-3.00%)</td><td>0.04 (-10.45%)</td><td>0.03 (-13.30%)</td><td>0.01 <b>(+56.01%)</b></td><td>250.10 (+15.36%)</td><td>191.02 (+5.73%)</td><td>197.00 (+11.68%)</td><td>135.90 (-7.11%)</td><td>42.70 <b>(+65.40%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>180.66 (n/a)</td><td>176.40 (n/a)</td><td>146.30 (n/a)</td><td>25.82 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (-14.65%)</td><td>0.05 (-10.67%)</td><td>0.04 (-7.56%)</td><td>0.04 (-5.30%)</td><td>0.01 <b>(-25.24%)</b></td><td>227.60 (+5.57%)</td><td>185.02 (+10.78%)</td><td>185.70 (+8.15%)</td><td>150.60 (+17.11%)</td><td>32.03 (-7.53%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>167.02 (n/a)</td><td>171.70 (n/a)</td><td>128.60 (n/a)</td><td>34.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 <b>(-23.46%)</b></td><td>0.04 (-12.18%)</td><td>0.04 (+0.10%)</td><td>0.03 (-0.87%)</td><td>0.01 <b>(-56.71%)</b></td><td>235.10 (+0.86%)</td><td>196.38 (+9.56%)</td><td>193.70 (-0.10%)</td><td>166.40 <b>(+30.61%)</b></td><td>25.93 <b>(-41.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.10 (n/a)</td><td>179.24 (n/a)</td><td>193.90 (n/a)</td><td>127.40 (n/a)</td><td>44.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (+15.65%)</td><td>0.04 (-3.45%)</td><td>0.04 (-4.24%)</td><td>0.04 (-16.82%)</td><td>0.01 <b>(+177.80%)</b></td><td>232.10 <b>(+20.20%)</b></td><td>193.16 (+6.21%)</td><td>194.20 (+4.46%)</td><td>141.40 (-13.52%)</td><td>34.55 <b>(+183.51%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.10 (n/a)</td><td>181.86 (n/a)</td><td>185.90 (n/a)</td><td>163.50 (n/a)</td><td>12.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (+9.97%)</td><td>0.04 (-7.83%)</td><td>0.04 (-12.00%)</td><td>0.03 (-14.98%)</td><td>0.01 <b>(+143.47%)</b></td><td>243.70 (+17.62%)</td><td>209.82 (+10.32%)</td><td>217.70 (+13.62%)</td><td>160.00 (-9.09%)</td><td>31.07 <b>(+153.19%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>207.20 (n/a)</td><td>190.20 (n/a)</td><td>191.60 (n/a)</td><td>176.00 (n/a)</td><td>12.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 <b>(+23.23%)</b></td><td>0.05 (+2.04%)</td><td>0.04 (-4.62%)</td><td>0.03 (-8.66%)</td><td>0.01 <b>(+142.00%)</b></td><td>239.90 (+9.49%)</td><td>188.70 (+0.97%)</td><td>191.90 (+4.86%)</td><td>137.70 (-18.86%)</td><td>39.82 <b>(+109.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.10 (n/a)</td><td>186.88 (n/a)</td><td>183.00 (n/a)</td><td>169.70 (n/a)</td><td>19.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (-8.87%)</td><td>0.10 (-7.07%)</td><td>0.09 (-3.84%)</td><td>0.07 (-12.11%)</td><td>0.02 (-6.15%)</td><td>218.80 (+13.78%)</td><td>178.50 (+8.12%)</td><td>185.30 (+3.98%)</td><td>121.00 (+9.70%)</td><td>38.61 <b>(+20.78%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>192.30 (n/a)</td><td>165.10 (n/a)</td><td>178.20 (n/a)</td><td>110.30 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (-13.66%)</td><td>0.09 (-4.67%)</td><td>0.10 (+11.29%)</td><td>0.07 (-17.98%)</td><td>0.02 (-12.06%)</td><td>239.90 <b>(+21.90%)</b></td><td>181.98 (+5.11%)</td><td>170.60 (-10.16%)</td><td>153.90 (+15.80%)</td><td>34.76 <b>(+24.33%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>173.14 (n/a)</td><td>189.90 (n/a)</td><td>132.90 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (+11.76%)</td><td>0.08 (+3.69%)</td><td>0.07 (-3.57%)</td><td>0.07 (+2.96%)</td><td>0.01 <b>(+117.48%)</b></td><td>236.70 (-2.87%)</td><td>215.32 (-2.76%)</td><td>227.30 (+3.70%)</td><td>187.80 (-10.49%)</td><td>24.48 <b>(+85.89%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>243.70 (n/a)</td><td>221.44 (n/a)</td><td>219.20 (n/a)</td><td>209.80 (n/a)</td><td>13.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (+12.83%)</td><td>0.09 <b>(+23.79%)</b></td><td>0.09 <b>(+26.84%)</b></td><td>0.09 <b>(+46.00%)</b></td><td>0.00 <b>(-60.28%)</b></td><td>188.80 <b>(-31.52%)</b></td><td>179.92 <b>(-20.55%)</b></td><td>179.00 <b>(-21.15%)</b></td><td>168.30 (-11.37%)</td><td>8.51 <b>(-75.50%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>275.70 (n/a)</td><td>226.46 (n/a)</td><td>227.00 (n/a)</td><td>189.90 (n/a)</td><td>34.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (+19.00%)</td><td>0.11 (+8.62%)</td><td>0.11 (+8.13%)</td><td>0.09 (+13.50%)</td><td>0.02 <b>(+37.50%)</b></td><td>178.20 (-11.91%)</td><td>155.00 (-7.33%)</td><td>152.90 (-7.50%)</td><td>116.90 (-15.96%)</td><td>24.96 (+2.00%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>167.26 (n/a)</td><td>165.30 (n/a)</td><td>139.10 (n/a)</td><td>24.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (-0.11%)</td><td>0.11 (-3.42%)</td><td>0.11 (+4.93%)</td><td>0.07 <b>(-25.86%)</b></td><td>0.03 <b>(+111.82%)</b></td><td>221.70 <b>(+34.94%)</b></td><td>161.22 (+8.71%)</td><td>143.00 (-4.67%)</td><td>122.70 (+0.08%)</td><td>44.90 <b>(+186.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>164.30 (n/a)</td><td>148.30 (n/a)</td><td>150.00 (n/a)</td><td>122.60 (n/a)</td><td>15.67 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (-8.42%)</td><td>0.11 (-1.61%)</td><td>0.10 (-1.82%)</td><td>0.08 (-4.49%)</td><td>0.02 (-13.59%)</td><td>202.10 (+4.72%)</td><td>155.72 (+1.09%)</td><td>156.70 (+1.82%)</td><td>127.10 (+9.19%)</td><td>30.28 (-2.78%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.00 (n/a)</td><td>154.04 (n/a)</td><td>153.90 (n/a)</td><td>116.40 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (-9.98%)</td><td>0.11 (+5.94%)</td><td>0.11 (+14.10%)</td><td>0.08 (-4.42%)</td><td>0.02 (-16.39%)</td><td>204.40 (+4.61%)</td><td>152.96 (-6.04%)</td><td>146.90 (-12.35%)</td><td>131.10 (+11.10%)</td><td>29.90 (+0.65%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.40 (n/a)</td><td>162.80 (n/a)</td><td>167.60 (n/a)</td><td>118.00 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (-2.27%)</td><td>0.10 (-4.85%)</td><td>0.11 (+3.71%)</td><td>0.07 (-11.46%)</td><td>0.03 (+15.25%)</td><td>224.40 (+12.93%)</td><td>168.18 (+7.92%)</td><td>148.70 (-3.57%)</td><td>120.90 (+2.37%)</td><td>51.02 <b>(+39.07%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>198.70 (n/a)</td><td>155.84 (n/a)</td><td>154.20 (n/a)</td><td>118.10 (n/a)</td><td>36.68 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (-5.52%)</td><td>0.12 (+15.03%)</td><td>0.11 (+13.43%)</td><td>0.11 <b>(+41.22%)</b></td><td>0.01 <b>(-58.98%)</b></td><td>152.80 <b>(-29.19%)</b></td><td>139.08 (-17.18%)</td><td>143.60 (-11.85%)</td><td>124.50 (+5.87%)</td><td>12.84 <b>(-70.41%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>215.80 (n/a)</td><td>167.94 (n/a)</td><td>162.90 (n/a)</td><td>117.60 (n/a)</td><td>43.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (+5.44%)</td><td>0.10 (+0.78%)</td><td>0.10 (-8.20%)</td><td>0.07 (+11.39%)</td><td>0.02 (+7.42%)</td><td>228.20 (-10.23%)</td><td>173.36 (-0.98%)</td><td>168.80 (+8.90%)</td><td>124.80 (-5.17%)</td><td>42.64 (-11.18%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>254.20 (n/a)</td><td>175.08 (n/a)</td><td>155.00 (n/a)</td><td>131.60 (n/a)</td><td>48.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 <b>(+42.95%)</b></td><td>0.11 (+12.32%)</td><td>0.10 (-0.76%)</td><td>0.08 (-2.28%)</td><td>0.03 <b>(+136.98%)</b></td><td>209.80 (+2.34%)</td><td>158.52 (-6.39%)</td><td>158.90 (+0.76%)</td><td>100.60 <b>(-30.04%)</b></td><td>43.56 <b>(+68.49%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>169.34 (n/a)</td><td>157.70 (n/a)</td><td>143.80 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 <b>(+22.31%)</b></td><td>0.10 <b>(+22.61%)</b></td><td>0.10 (+16.15%)</td><td>0.08 <b>(+29.92%)</b></td><td>0.02 <b>(+23.86%)</b></td><td>216.50 <b>(-23.04%)</b></td><td>165.26 (-18.64%)</td><td>164.10 (-13.90%)</td><td>122.90 (-18.28%)</td><td>38.23 <b>(-24.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>281.30 (n/a)</td><td>203.12 (n/a)</td><td>190.60 (n/a)</td><td>150.40 (n/a)</td><td>50.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 <b>(+22.68%)</b></td><td>0.09 (+5.93%)</td><td>0.09 (-4.95%)</td><td>0.07 (+2.76%)</td><td>0.02 <b>(+55.73%)</b></td><td>237.30 (-2.67%)</td><td>181.76 (-3.88%)</td><td>185.10 (+5.23%)</td><td>129.20 (-18.54%)</td><td>39.76 (+19.45%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>243.80 (n/a)</td><td>189.10 (n/a)</td><td>175.90 (n/a)</td><td>158.60 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (-13.33%)</td><td>0.09 (-1.78%)</td><td>0.09 (+15.56%)</td><td>0.06 (-17.61%)</td><td>0.02 (+3.09%)</td><td>270.20 <b>(+21.38%)</b></td><td>200.72 (+3.54%)</td><td>174.10 (-13.47%)</td><td>156.00 (+15.38%)</td><td>51.22 <b>(+49.08%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.60 (n/a)</td><td>193.86 (n/a)</td><td>201.20 (n/a)</td><td>135.20 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.12 (+11.52%)</td><td>0.10 (-0.84%)</td><td>0.10 (+3.16%)</td><td>0.06 <b>(-27.80%)</b></td><td>0.02 <b>(+284.02%)</b></td><td>252.50 <b>(+38.51%)</b></td><td>176.14 (+5.05%)</td><td>159.50 (-3.04%)</td><td>141.40 (-10.28%)</td><td>45.03 <b>(+382.64%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>167.68 (n/a)</td><td>164.50 (n/a)</td><td>157.60 (n/a)</td><td>9.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (-4.81%)</td><td>0.21 (+2.59%)</td><td>0.20 (+8.38%)</td><td>0.17 (+10.96%)</td><td>0.04 <b>(-20.42%)</b></td><td>193.20 (-9.89%)</td><td>164.04 (-4.07%)</td><td>160.60 (-7.75%)</td><td>123.90 (+5.09%)</td><td>29.18 <b>(-22.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>214.40 (n/a)</td><td>171.00 (n/a)</td><td>174.10 (n/a)</td><td>117.90 (n/a)</td><td>37.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (-11.28%)</td><td>0.19 (-14.93%)</td><td>0.18 (-17.67%)</td><td>0.16 (-12.17%)</td><td>0.04 (-14.56%)</td><td>210.30 (+13.86%)</td><td>177.50 (+17.29%)</td><td>185.50 <b>(+21.48%)</b></td><td>131.50 (+12.68%)</td><td>31.21 (+8.50%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>184.70 (n/a)</td><td>151.34 (n/a)</td><td>152.70 (n/a)</td><td>116.70 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (-16.80%)</td><td>0.15 <b>(-21.19%)</b></td><td>0.14 <b>(-24.38%)</b></td><td>0.11 (-17.71%)</td><td>0.03 (-18.65%)</td><td>286.30 <b>(+21.52%)</b></td><td>232.66 <b>(+26.62%)</b></td><td>235.90 <b>(+32.23%)</b></td><td>167.70 <b>(+20.22%)</b></td><td>43.72 (+15.36%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>235.60 (n/a)</td><td>183.74 (n/a)</td><td>178.40 (n/a)</td><td>139.50 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (-16.97%)</td><td>0.15 (-10.85%)</td><td>0.15 (-6.23%)</td><td>0.14 (-3.73%)</td><td>0.01 <b>(-48.62%)</b></td><td>241.90 (+3.86%)</td><td>215.12 (+10.97%)</td><td>212.20 (+6.69%)</td><td>196.20 <b>(+20.44%)</b></td><td>18.13 <b>(-34.95%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>193.86 (n/a)</td><td>198.90 (n/a)</td><td>162.90 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (-11.60%)</td><td>0.19 (-10.22%)</td><td>0.18 (-1.89%)</td><td>0.16 (-7.28%)</td><td>0.04 <b>(-27.53%)</b></td><td>202.10 (+7.84%)</td><td>178.38 (+9.70%)</td><td>187.00 (+1.91%)</td><td>131.30 (+13.09%)</td><td>27.36 (-17.39%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>187.40 (n/a)</td><td>162.60 (n/a)</td><td>183.50 (n/a)</td><td>116.10 (n/a)</td><td>33.11 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (+17.10%)</td><td>0.20 <b>(+20.94%)</b></td><td>0.19 (+4.73%)</td><td>0.18 <b>(+97.22%)</b></td><td>0.03 <b>(-44.83%)</b></td><td>183.10 <b>(-49.29%)</b></td><td>162.58 <b>(-24.52%)</b></td><td>168.10 (-4.49%)</td><td>128.40 (-14.57%)</td><td>20.42 <b>(-76.78%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>361.10 (n/a)</td><td>215.40 (n/a)</td><td>176.00 (n/a)</td><td>150.30 (n/a)</td><td>87.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (+16.92%)</td><td>0.18 (-2.94%)</td><td>0.17 (-6.18%)</td><td>0.14 (-6.43%)</td><td>0.04 <b>(+86.86%)</b></td><td>230.80 (+6.90%)</td><td>192.46 (+5.70%)</td><td>196.30 (+6.57%)</td><td>130.20 (-14.45%)</td><td>37.62 <b>(+62.73%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.90 (n/a)</td><td>182.08 (n/a)</td><td>184.20 (n/a)</td><td>152.20 (n/a)</td><td>23.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (-8.12%)</td><td>0.19 (+5.20%)</td><td>0.18 (+5.37%)</td><td>0.14 <b>(+62.30%)</b></td><td>0.04 <b>(-41.66%)</b></td><td>228.30 <b>(-38.40%)</b></td><td>177.90 (-15.12%)</td><td>181.10 (-5.08%)</td><td>126.50 (+8.86%)</td><td>36.29 <b>(-62.94%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>370.60 (n/a)</td><td>209.60 (n/a)</td><td>190.80 (n/a)</td><td>116.20 (n/a)</td><td>97.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (-8.84%)</td><td>0.18 (+2.89%)</td><td>0.16 (+4.06%)</td><td>0.14 <b>(+59.22%)</b></td><td>0.04 <b>(-38.06%)</b></td><td>226.60 <b>(-37.18%)</b></td><td>191.04 (-11.60%)</td><td>200.20 (-3.89%)</td><td>130.10 (+9.70%)</td><td>36.76 <b>(-59.46%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>360.70 (n/a)</td><td>216.12 (n/a)</td><td>208.30 (n/a)</td><td>118.60 (n/a)</td><td>90.66 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (+4.60%)</td><td>0.16 (-12.30%)</td><td>0.17 (-7.23%)</td><td>0.09 <b>(-42.36%)</b></td><td>0.05 <b>(+87.75%)</b></td><td>372.80 <b>(+73.48%)</b></td><td>221.68 <b>(+23.29%)</b></td><td>191.10 (+7.78%)</td><td>147.90 (-4.40%)</td><td>87.22 <b>(+241.16%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>214.90 (n/a)</td><td>179.80 (n/a)</td><td>177.30 (n/a)</td><td>154.70 (n/a)</td><td>25.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (-10.04%)</td><td>0.20 (-2.53%)</td><td>0.18 (-0.79%)</td><td>0.17 (-4.81%)</td><td>0.04 (-19.18%)</td><td>197.00 (+5.07%)</td><td>166.78 (+1.84%)</td><td>177.30 (+0.80%)</td><td>130.50 (+11.16%)</td><td>27.53 (-6.31%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>187.50 (n/a)</td><td>163.76 (n/a)</td><td>175.90 (n/a)</td><td>117.40 (n/a)</td><td>29.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (-8.96%)</td><td>0.20 (+6.37%)</td><td>0.20 (+16.80%)</td><td>0.16 (+13.77%)</td><td>0.04 <b>(-32.28%)</b></td><td>203.90 (-12.11%)</td><td>166.96 (-8.77%)</td><td>167.00 (-14.40%)</td><td>132.10 (+9.81%)</td><td>29.43 <b>(-34.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>232.00 (n/a)</td><td>183.02 (n/a)</td><td>195.10 (n/a)</td><td>120.30 (n/a)</td><td>44.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (-17.27%)</td><td>0.18 (+5.56%)</td><td>0.19 (+19.54%)</td><td>0.12 (-0.77%)</td><td>0.04 <b>(-31.79%)</b></td><td>265.40 (+0.76%)</td><td>190.34 (-8.28%)</td><td>172.90 (-16.31%)</td><td>151.90 <b>(+20.84%)</b></td><td>46.87 (-19.23%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>263.40 (n/a)</td><td>207.52 (n/a)</td><td>206.60 (n/a)</td><td>125.70 (n/a)</td><td>58.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 (-2.85%)</td><td>0.19 (-2.14%)</td><td>0.22 (+8.30%)</td><td>0.13 (-14.49%)</td><td>0.05 <b>(+31.03%)</b></td><td>244.80 (+16.91%)</td><td>178.58 (+4.76%)</td><td>146.00 (-7.65%)</td><td>143.20 (+2.95%)</td><td>47.27 <b>(+51.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>209.40 (n/a)</td><td>170.46 (n/a)</td><td>158.10 (n/a)</td><td>139.10 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 <b>(-22.69%)</b></td><td>0.15 <b>(-27.06%)</b></td><td>0.16 <b>(-23.06%)</b></td><td>0.10 <b>(-32.31%)</b></td><td>0.03 (-4.66%)</td><td>312.80 <b>(+47.76%)</b></td><td>232.02 <b>(+39.28%)</b></td><td>209.90 <b>(+29.97%)</b></td><td>177.50 <b>(+29.37%)</b></td><td>52.32 <b>(+83.21%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>211.70 (n/a)</td><td>166.58 (n/a)</td><td>161.50 (n/a)</td><td>137.20 (n/a)</td><td>28.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 <b>(+22.16%)</b></td><td>0.20 (+17.63%)</td><td>0.19 (+17.71%)</td><td>0.16 (+7.36%)</td><td>0.03 <b>(+54.07%)</b></td><td>199.40 (-6.87%)</td><td>168.84 (-14.22%)</td><td>173.70 (-15.06%)</td><td>130.00 (-18.14%)</td><td>25.76 (+17.44%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.10 (n/a)</td><td>196.82 (n/a)</td><td>204.50 (n/a)</td><td>158.80 (n/a)</td><td>21.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (+0.11%)</td><td>0.16 (+0.01%)</td><td>0.16 (+0.00%)</td><td>0.16 (-0.01%)</td><td>0.00 <b>(+100.65%)</b></td><td>52614.80 (+0.01%)</td><td>52567.40 (-0.01%)</td><td>52572.20 (-0.00%)</td><td>52474.10 (-0.11%)</td><td>57.56 <b>(+100.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52611.10 (n/a)</td><td>52570.46 (n/a)</td><td>52573.00 (n/a)</td><td>52531.10 (n/a)</td><td>28.70 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52619.90 (n/a)</td><td>52582.96 (n/a)</td><td>52605.30 (n/a)</td><td>52480.40 (n/a)</td><td>58.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>415780.90 (n/a)</td><td>415611.84 (n/a)</td><td>415573.80 (n/a)</td><td>415540.90 (n/a)</td><td>97.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (+2.67%)</td><td>0.19 (+8.39%)</td><td>0.19 (+7.09%)</td><td>0.15 (+10.66%)</td><td>0.02 <b>(-22.90%)</b></td><td>159.80 (-9.62%)</td><td>133.92 (-8.47%)</td><td>131.60 (-6.60%)</td><td>121.50 (-2.57%)</td><td>15.32 <b>(-30.86%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>176.80 (n/a)</td><td>146.32 (n/a)</td><td>140.90 (n/a)</td><td>124.70 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.42 (+3.17%)</td><td>0.33 (-3.78%)</td><td>0.32 (-16.56%)</td><td>0.28 (+6.10%)</td><td>0.06 (-10.24%)</td><td>177.30 (-5.79%)</td><td>150.26 (+3.10%)</td><td>154.90 (+19.80%)</td><td>117.80 (-3.12%)</td><td>24.79 (-16.76%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>188.20 (n/a)</td><td>145.74 (n/a)</td><td>129.30 (n/a)</td><td>121.60 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>13.41 (-1.63%)</td><td>13.01 (-0.79%)</td><td>12.93 (-2.18%)</td><td>12.64 (+0.83%)</td><td>0.29 <b>(-35.43%)</b></td><td>829.70 (-0.82%)</td><td>806.60 (+0.74%)</td><td>810.70 (+2.23%)</td><td>782.10 (+1.66%)</td><td>17.92 <b>(-35.19%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>13.63 (n/a)</td><td>13.11 (n/a)</td><td>13.22 (n/a)</td><td>12.53 (n/a)</td><td>0.45 (n/a)</td><td>836.60 (n/a)</td><td>800.64 (n/a)</td><td>793.00 (n/a)</td><td>769.30 (n/a)</td><td>27.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (+4.43%)</td><td>0.25 (-6.95%)</td><td>0.24 <b>(-21.17%)</b></td><td>0.19 (-4.83%)</td><td>0.05 (-10.99%)</td><td>211.50 (+5.07%)</td><td>166.58 (+6.43%)</td><td>170.70 <b>(+26.82%)</b></td><td>121.10 (-4.27%)</td><td>33.02 (-11.79%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>201.30 (n/a)</td><td>156.52 (n/a)</td><td>134.60 (n/a)</td><td>126.50 (n/a)</td><td>37.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 <b>(-22.57%)</b></td><td>0.03 <b>(-28.21%)</b></td><td>0.03 <b>(-28.82%)</b></td><td>0.02 <b>(-38.03%)</b></td><td>0.01 (-1.08%)</td><td>291.30 <b>(+61.39%)</b></td><td>199.70 <b>(+42.89%)</b></td><td>180.50 <b>(+40.47%)</b></td><td>147.80 <b>(+29.20%)</b></td><td>54.42 <b>(+111.90%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>139.76 (n/a)</td><td>128.50 (n/a)</td><td>114.40 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-12.19%)</td><td>0.02 (-3.92%)</td><td>0.02 (-7.16%)</td><td>0.02 (+2.94%)</td><td>0.00 <b>(-37.00%)</b></td><td>222.60 (-2.84%)</td><td>186.34 (+1.54%)</td><td>185.00 (+7.75%)</td><td>149.20 (+13.89%)</td><td>28.18 <b>(-32.94%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.10 (n/a)</td><td>183.52 (n/a)</td><td>171.70 (n/a)</td><td>131.00 (n/a)</td><td>42.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (-10.61%)</td><td>0.04 (-16.20%)</td><td>0.04 <b>(-23.76%)</b></td><td>0.03 (-8.88%)</td><td>0.01 (-14.41%)</td><td>237.70 (+9.74%)</td><td>179.38 (+18.64%)</td><td>174.60 <b>(+31.18%)</b></td><td>121.70 (+11.86%)</td><td>48.82 (+6.59%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>151.20 (n/a)</td><td>133.10 (n/a)</td><td>108.80 (n/a)</td><td>45.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(+33.04%)</b></td><td>0.02 (+3.80%)</td><td>0.02 (+3.93%)</td><td>0.01 <b>(-24.72%)</b></td><td>0.01 <b>(+163.47%)</b></td><td>279.90 <b>(+32.84%)</b></td><td>191.42 (+2.98%)</td><td>180.70 (-3.73%)</td><td>116.20 <b>(-24.79%)</b></td><td>58.91 <b>(+157.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>185.88 (n/a)</td><td>187.70 (n/a)</td><td>154.50 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-12.39%)</td><td>0.03 (-7.62%)</td><td>0.03 (+3.09%)</td><td>0.02 (-5.62%)</td><td>0.00 <b>(-38.11%)</b></td><td>241.10 (+5.93%)</td><td>194.04 (+5.93%)</td><td>185.10 (-3.04%)</td><td>158.40 (+14.20%)</td><td>31.35 <b>(-22.79%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.60 (n/a)</td><td>183.18 (n/a)</td><td>190.90 (n/a)</td><td>138.70 (n/a)</td><td>40.61 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (+0.73%)</td><td>0.03 (-8.75%)</td><td>0.02 (-14.84%)</td><td>0.01 <b>(-26.57%)</b></td><td>0.01 <b>(+31.48%)</b></td><td>301.70 <b>(+36.15%)</b></td><td>184.14 (+17.03%)</td><td>175.60 (+17.38%)</td><td>106.00 (-0.75%)</td><td>74.05 <b>(+79.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>157.34 (n/a)</td><td>149.60 (n/a)</td><td>106.80 (n/a)</td><td>41.34 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (+3.83%)</td><td>0.03 (-10.13%)</td><td>0.03 (-4.16%)</td><td>0.02 <b>(-20.38%)</b></td><td>0.01 <b>(+45.77%)</b></td><td>242.00 <b>(+25.58%)</b></td><td>186.84 (+16.76%)</td><td>168.90 (+4.39%)</td><td>113.80 (-3.64%)</td><td>54.94 <b>(+84.74%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.70 (n/a)</td><td>160.02 (n/a)</td><td>161.80 (n/a)</td><td>118.10 (n/a)</td><td>29.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-8.05%)</td><td>0.03 (-3.31%)</td><td>0.02 (-2.31%)</td><td>0.02 (+7.44%)</td><td>0.01 (-10.20%)</td><td>209.50 (-6.93%)</td><td>170.44 (+2.75%)</td><td>168.20 (+2.37%)</td><td>124.80 (+8.81%)</td><td>38.73 (-5.55%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.10 (n/a)</td><td>165.88 (n/a)</td><td>164.30 (n/a)</td><td>114.70 (n/a)</td><td>41.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 <b>(-22.08%)</b></td><td>0.02 (-9.29%)</td><td>0.02 (-1.66%)</td><td>0.02 (-4.92%)</td><td>0.00 <b>(-55.58%)</b></td><td>216.00 (+5.16%)</td><td>187.72 (+8.48%)</td><td>184.40 (+1.71%)</td><td>172.00 <b>(+28.36%)</b></td><td>17.07 <b>(-38.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.40 (n/a)</td><td>173.04 (n/a)</td><td>181.30 (n/a)</td><td>134.00 (n/a)</td><td>27.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-6.58%)</td><td>0.02 (-8.15%)</td><td>0.02 (-12.99%)</td><td>0.02 (-12.18%)</td><td>0.01 (+5.71%)</td><td>218.40 (+13.87%)</td><td>176.66 (+10.03%)</td><td>181.40 (+14.88%)</td><td>125.80 (+7.06%)</td><td>37.50 <b>(+30.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>160.56 (n/a)</td><td>157.90 (n/a)</td><td>117.50 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-1.35%)</td><td>0.03 (-10.01%)</td><td>0.03 (-9.47%)</td><td>0.02 (-18.11%)</td><td>0.01 <b>(+31.02%)</b></td><td>232.40 <b>(+22.12%)</b></td><td>181.84 (+13.01%)</td><td>173.20 (+10.46%)</td><td>136.80 (+1.41%)</td><td>36.39 <b>(+62.09%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.30 (n/a)</td><td>160.90 (n/a)</td><td>156.80 (n/a)</td><td>134.90 (n/a)</td><td>22.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-6.64%)</td><td>0.02 (-12.03%)</td><td>0.02 (-8.02%)</td><td>0.02 (-13.03%)</td><td>0.01 (+12.64%)</td><td>233.40 (+15.03%)</td><td>185.14 (+15.51%)</td><td>171.10 (+8.70%)</td><td>130.90 (+7.12%)</td><td>41.69 <b>(+41.95%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.90 (n/a)</td><td>160.28 (n/a)</td><td>157.40 (n/a)</td><td>122.20 (n/a)</td><td>29.37 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-0.57%)</td><td>0.02 (+6.54%)</td><td>0.02 (+3.40%)</td><td>0.02 <b>(+44.12%)</b></td><td>0.00 <b>(-46.88%)</b></td><td>207.30 <b>(-30.60%)</b></td><td>193.16 (-9.34%)</td><td>205.80 (-3.29%)</td><td>163.10 (+0.55%)</td><td>19.52 <b>(-63.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>298.70 (n/a)</td><td>213.06 (n/a)</td><td>212.80 (n/a)</td><td>162.20 (n/a)</td><td>52.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-4.79%)</td><td>0.02 (-8.81%)</td><td>0.02 (-11.81%)</td><td>0.02 (-13.70%)</td><td>0.00 <b>(+54.67%)</b></td><td>223.70 (+15.85%)</td><td>189.62 (+11.14%)</td><td>195.50 (+13.40%)</td><td>158.30 (+5.04%)</td><td>30.17 <b>(+83.40%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.10 (n/a)</td><td>170.62 (n/a)</td><td>172.40 (n/a)</td><td>150.70 (n/a)</td><td>16.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (-4.07%)</td><td>0.02 (+4.68%)</td><td>0.02 (+7.51%)</td><td>0.02 (+12.41%)</td><td>0.00 <b>(-27.15%)</b></td><td>217.20 (-11.06%)</td><td>192.32 (-5.84%)</td><td>203.70 (-6.99%)</td><td>161.50 (+4.26%)</td><td>25.03 <b>(-32.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.20 (n/a)</td><td>204.24 (n/a)</td><td>219.00 (n/a)</td><td>154.90 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (-0.03%)</td><td>0.02 (-11.83%)</td><td>0.02 (-13.37%)</td><td>0.02 (-14.61%)</td><td>0.00 <b>(+43.44%)</b></td><td>258.00 (+17.11%)</td><td>225.08 (+14.51%)</td><td>219.00 (+15.38%)</td><td>179.90 (+0.00%)</td><td>31.38 <b>(+70.11%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.30 (n/a)</td><td>196.56 (n/a)</td><td>189.80 (n/a)</td><td>179.90 (n/a)</td><td>18.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (+6.44%)</td><td>0.06 (+2.24%)</td><td>0.06 (+7.73%)</td><td>0.04 (-3.80%)</td><td>0.01 <b>(+35.43%)</b></td><td>183.40 (+3.97%)</td><td>143.16 (-1.20%)</td><td>130.60 (-7.18%)</td><td>119.60 (-6.05%)</td><td>25.43 <b>(+32.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.40 (n/a)</td><td>144.90 (n/a)</td><td>140.70 (n/a)</td><td>127.30 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 <b>(-35.32%)</b></td><td>0.06 <b>(-27.75%)</b></td><td>0.06 <b>(-20.93%)</b></td><td>0.04 <b>(-39.82%)</b></td><td>0.01 <b>(-32.76%)</b></td><td>345.20 <b>(+66.12%)</b></td><td>219.16 <b>(+39.97%)</b></td><td>194.90 <b>(+26.48%)</b></td><td>174.40 <b>(+54.61%)</b></td><td>71.13 <b>(+81.58%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>207.80 (n/a)</td><td>156.58 (n/a)</td><td>154.10 (n/a)</td><td>112.80 (n/a)</td><td>39.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (+3.29%)</td><td>0.06 <b>(+29.25%)</b></td><td>0.06 <b>(+48.92%)</b></td><td>0.04 <b>(+35.88%)</b></td><td>0.01 <b>(-26.59%)</b></td><td>182.60 <b>(-26.40%)</b></td><td>147.68 <b>(-25.29%)</b></td><td>135.10 <b>(-32.85%)</b></td><td>118.20 (-3.19%)</td><td>26.52 <b>(-44.66%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.10 (n/a)</td><td>197.68 (n/a)</td><td>201.20 (n/a)</td><td>122.10 (n/a)</td><td>47.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (+16.65%)</td><td>0.06 (-5.01%)</td><td>0.06 (+1.77%)</td><td>0.03 <b>(-46.48%)</b></td><td>0.02 <b>(+179.57%)</b></td><td>358.20 <b>(+86.85%)</b></td><td>200.82 (+18.58%)</td><td>170.70 (-1.78%)</td><td>123.80 (-14.27%)</td><td>92.38 <b>(+375.39%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>169.36 (n/a)</td><td>173.80 (n/a)</td><td>144.40 (n/a)</td><td>19.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (+5.55%)</td><td>0.06 (+2.29%)</td><td>0.06 (+2.62%)</td><td>0.05 (+1.34%)</td><td>0.01 (+14.62%)</td><td>167.70 (-1.29%)</td><td>148.66 (-2.03%)</td><td>146.80 (-2.59%)</td><td>122.00 (-5.21%)</td><td>17.65 (+5.64%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.90 (n/a)</td><td>151.74 (n/a)</td><td>150.70 (n/a)</td><td>128.70 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (-11.21%)</td><td>0.07 (+2.98%)</td><td>0.06 (+2.60%)</td><td>0.06 <b>(+30.81%)</b></td><td>0.01 <b>(-50.78%)</b></td><td>182.00 <b>(-23.56%)</b></td><td>159.46 (-7.88%)</td><td>159.40 (-2.51%)</td><td>128.10 (+12.57%)</td><td>20.40 <b>(-58.55%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>238.10 (n/a)</td><td>173.10 (n/a)</td><td>163.50 (n/a)</td><td>113.80 (n/a)</td><td>49.23 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (-16.64%)</td><td>0.05 (+0.01%)</td><td>0.05 (-6.77%)</td><td>0.04 <b>(+33.68%)</b></td><td>0.01 <b>(-58.97%)</b></td><td>206.50 <b>(-25.18%)</b></td><td>178.70 (-6.21%)</td><td>174.70 (+7.24%)</td><td>150.50 <b>(+20.02%)</b></td><td>21.69 <b>(-63.80%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>276.00 (n/a)</td><td>190.54 (n/a)</td><td>162.90 (n/a)</td><td>125.40 (n/a)</td><td>59.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (-1.69%)</td><td>0.06 (+8.68%)</td><td>0.05 (+12.03%)</td><td>0.04 (+4.60%)</td><td>0.01 (+2.45%)</td><td>212.60 (-4.36%)</td><td>169.86 (-7.83%)</td><td>173.40 (-10.76%)</td><td>130.80 (+1.71%)</td><td>35.43 (+2.28%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>184.28 (n/a)</td><td>194.30 (n/a)</td><td>128.60 (n/a)</td><td>34.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (-1.81%)</td><td>0.05 (+12.08%)</td><td>0.05 <b>(+21.05%)</b></td><td>0.05 <b>(+22.72%)</b></td><td>0.00 <b>(-46.27%)</b></td><td>177.10 (-18.54%)</td><td>159.10 (-12.38%)</td><td>156.60 (-17.36%)</td><td>144.90 (+1.83%)</td><td>13.67 <b>(-55.18%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>181.58 (n/a)</td><td>189.50 (n/a)</td><td>142.30 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (-8.37%)</td><td>0.05 (-5.77%)</td><td>0.05 (+0.86%)</td><td>0.03 <b>(-27.69%)</b></td><td>0.01 (+10.38%)</td><td>292.70 <b>(+38.33%)</b></td><td>202.36 (+8.69%)</td><td>192.60 (-0.87%)</td><td>146.60 (+9.16%)</td><td>54.44 <b>(+78.15%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>186.18 (n/a)</td><td>194.30 (n/a)</td><td>134.30 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (+13.92%)</td><td>0.05 (+11.90%)</td><td>0.05 (+19.91%)</td><td>0.04 <b>(+25.21%)</b></td><td>0.01 (+0.35%)</td><td>222.10 <b>(-20.14%)</b></td><td>177.60 (-12.23%)</td><td>178.60 (-16.62%)</td><td>120.50 (-12.24%)</td><td>36.71 <b>(-31.86%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.10 (n/a)</td><td>202.34 (n/a)</td><td>214.20 (n/a)</td><td>137.30 (n/a)</td><td>53.88 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(-31.47%)</b></td><td>0.04 (-12.80%)</td><td>0.04 (-3.03%)</td><td>0.03 (+13.35%)</td><td>0.01 <b>(-55.00%)</b></td><td>309.50 (-11.77%)</td><td>232.16 (+7.36%)</td><td>209.80 (+3.10%)</td><td>205.20 <b>(+45.95%)</b></td><td>44.46 <b>(-44.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>350.80 (n/a)</td><td>216.24 (n/a)</td><td>203.50 (n/a)</td><td>140.60 (n/a)</td><td>80.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (+1.80%)</td><td>0.05 (-3.22%)</td><td>0.05 (-1.70%)</td><td>0.04 (-10.68%)</td><td>0.01 <b>(+31.12%)</b></td><td>210.20 (+11.99%)</td><td>170.48 (+4.24%)</td><td>169.50 (+1.74%)</td><td>137.60 (-1.78%)</td><td>26.28 <b>(+45.82%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.70 (n/a)</td><td>163.54 (n/a)</td><td>166.60 (n/a)</td><td>140.10 (n/a)</td><td>18.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(-24.10%)</b></td><td>0.04 (-4.69%)</td><td>0.04 (-3.15%)</td><td>0.04 <b>(+28.49%)</b></td><td>0.00 <b>(-74.18%)</b></td><td>247.00 <b>(-22.18%)</b></td><td>220.68 (+0.29%)</td><td>215.40 (+3.26%)</td><td>211.50 <b>(+31.69%)</b></td><td>14.87 <b>(-74.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>317.40 (n/a)</td><td>220.04 (n/a)</td><td>208.60 (n/a)</td><td>160.60 (n/a)</td><td>58.20 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 <b>(-32.57%)</b></td><td>0.04 (-12.57%)</td><td>0.04 (-9.74%)</td><td>0.04 (+14.19%)</td><td>0.00 <b>(-91.02%)</b></td><td>208.70 (-12.42%)</td><td>203.96 (+8.70%)</td><td>204.80 (+10.76%)</td><td>195.80 <b>(+48.33%)</b></td><td>5.28 <b>(-88.61%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>187.64 (n/a)</td><td>184.90 (n/a)</td><td>132.00 (n/a)</td><td>46.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 <b>(-20.01%)</b></td><td>0.09 (-11.72%)</td><td>0.09 (-13.31%)</td><td>0.07 (+1.39%)</td><td>0.01 <b>(-57.07%)</b></td><td>220.50 (-1.39%)</td><td>193.36 (+11.13%)</td><td>190.90 (+15.35%)</td><td>179.00 <b>(+25.00%)</b></td><td>16.76 <b>(-47.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.60 (n/a)</td><td>174.00 (n/a)</td><td>165.50 (n/a)</td><td>143.20 (n/a)</td><td>31.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (-17.76%)</td><td>0.15 (-7.64%)</td><td>0.14 (-1.40%)</td><td>0.12 (+2.27%)</td><td>0.02 <b>(-45.54%)</b></td><td>201.90 (-2.23%)</td><td>168.90 (+4.79%)</td><td>174.50 (+1.45%)</td><td>134.50 <b>(+21.61%)</b></td><td>25.14 <b>(-35.21%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>206.50 (n/a)</td><td>161.18 (n/a)</td><td>172.00 (n/a)</td><td>110.60 (n/a)</td><td>38.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (+2.19%)</td><td>0.10 (-0.81%)</td><td>0.10 (+12.00%)</td><td>0.07 (-5.68%)</td><td>0.02 (-4.26%)</td><td>220.60 (+6.01%)</td><td>175.84 (+0.57%)</td><td>170.90 (-10.71%)</td><td>129.30 (-2.12%)</td><td>33.50 (-1.82%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.10 (n/a)</td><td>174.84 (n/a)</td><td>191.40 (n/a)</td><td>132.10 (n/a)</td><td>34.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (-9.32%)</td><td>0.11 (-8.14%)</td><td>0.11 (-7.77%)</td><td>0.09 (-15.75%)</td><td>0.02 (-2.54%)</td><td>239.90 (+18.70%)</td><td>183.48 (+9.47%)</td><td>180.40 (+8.41%)</td><td>146.80 (+10.29%)</td><td>36.57 <b>(+27.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>167.60 (n/a)</td><td>166.40 (n/a)</td><td>133.10 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 <b>(-53.06%)</b></td><td>0.08 <b>(-25.32%)</b></td><td>0.08 (-14.22%)</td><td>0.08 (+6.84%)</td><td>0.01 <b>(-88.48%)</b></td><td>215.40 (-6.39%)</td><td>198.18 <b>(+20.65%)</b></td><td>194.50 (+16.61%)</td><td>181.40 <b>(+112.91%)</b></td><td>12.95 <b>(-75.05%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>230.10 (n/a)</td><td>164.26 (n/a)</td><td>166.80 (n/a)</td><td>85.20 (n/a)</td><td>51.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (-8.22%)</td><td>0.12 (-13.40%)</td><td>0.11 <b>(-21.61%)</b></td><td>0.11 (-12.90%)</td><td>0.03 (+8.94%)</td><td>194.10 (+14.85%)</td><td>170.46 (+16.66%)</td><td>191.80 <b>(+27.53%)</b></td><td>129.70 (+8.99%)</td><td>31.58 <b>(+39.40%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>169.00 (n/a)</td><td>146.12 (n/a)</td><td>150.40 (n/a)</td><td>119.00 (n/a)</td><td>22.66 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 <b>(+61.35%)</b></td><td>0.10 <b>(+23.23%)</b></td><td>0.09 (+14.39%)</td><td>0.08 (+2.86%)</td><td>0.03 <b>(+302.92%)</b></td><td>213.10 (-2.78%)</td><td>173.34 (-14.90%)</td><td>180.90 (-12.61%)</td><td>109.00 <b>(-38.03%)</b></td><td>39.21 <b>(+134.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.20 (n/a)</td><td>203.68 (n/a)</td><td>207.00 (n/a)</td><td>175.90 (n/a)</td><td>16.76 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (-7.80%)</td><td>0.11 (+5.61%)</td><td>0.12 (+8.54%)</td><td>0.09 <b>(+26.38%)</b></td><td>0.02 <b>(-24.60%)</b></td><td>208.90 <b>(-20.90%)</b></td><td>167.76 (-7.98%)</td><td>160.30 (-7.82%)</td><td>134.50 (+8.47%)</td><td>32.17 <b>(-36.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>264.10 (n/a)</td><td>182.30 (n/a)</td><td>173.90 (n/a)</td><td>124.00 (n/a)</td><td>50.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 <b>(-24.41%)</b></td><td>0.08 (-15.13%)</td><td>0.09 (-6.77%)</td><td>0.06 (-9.65%)</td><td>0.01 <b>(-48.97%)</b></td><td>256.70 (+10.69%)</td><td>198.28 (+13.95%)</td><td>189.30 (+7.25%)</td><td>168.70 <b>(+32.31%)</b></td><td>35.64 <b>(-21.85%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>231.90 (n/a)</td><td>174.00 (n/a)</td><td>176.50 (n/a)</td><td>127.50 (n/a)</td><td>45.60 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (+3.33%)</td><td>0.11 (-0.96%)</td><td>0.12 (+3.48%)</td><td>0.08 (-8.51%)</td><td>0.02 <b>(+42.96%)</b></td><td>223.10 (+9.31%)</td><td>168.98 (+2.96%)</td><td>155.30 (-3.36%)</td><td>132.60 (-3.21%)</td><td>37.43 <b>(+49.28%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>204.10 (n/a)</td><td>164.12 (n/a)</td><td>160.70 (n/a)</td><td>137.00 (n/a)</td><td>25.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (+5.29%)</td><td>0.09 (-7.75%)</td><td>0.07 (-13.68%)</td><td>0.07 (-17.94%)</td><td>0.03 <b>(+46.19%)</b></td><td>250.50 <b>(+21.84%)</b></td><td>201.46 (+12.62%)</td><td>218.80 (+15.89%)</td><td>124.60 (-4.96%)</td><td>51.57 <b>(+68.70%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.60 (n/a)</td><td>178.88 (n/a)</td><td>188.80 (n/a)</td><td>131.10 (n/a)</td><td>30.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (-2.05%)</td><td>0.09 (+8.69%)</td><td>0.09 (+9.05%)</td><td>0.08 (+10.95%)</td><td>0.01 <b>(-25.48%)</b></td><td>228.70 (-9.85%)</td><td>193.44 (-9.29%)</td><td>193.20 (-8.31%)</td><td>161.50 (+2.09%)</td><td>26.24 <b>(-32.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>253.70 (n/a)</td><td>213.24 (n/a)</td><td>210.70 (n/a)</td><td>158.20 (n/a)</td><td>38.61 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.12 (+18.38%)</td><td>0.09 (+5.00%)</td><td>0.08 (-5.90%)</td><td>0.08 (+0.93%)</td><td>0.02 <b>(+62.44%)</b></td><td>213.50 (-0.93%)</td><td>180.98 (-3.39%)</td><td>195.90 (+6.29%)</td><td>134.90 (-15.58%)</td><td>31.24 <b>(+33.61%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>187.34 (n/a)</td><td>184.30 (n/a)</td><td>159.80 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (+17.61%)</td><td>0.09 (+16.80%)</td><td>0.09 (+16.98%)</td><td>0.08 (+5.54%)</td><td>0.01 <b>(+133.84%)</b></td><td>216.00 (-5.26%)</td><td>190.50 (-14.00%)</td><td>191.40 (-14.52%)</td><td>175.40 (-14.94%)</td><td>16.50 <b>(+87.50%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>228.00 (n/a)</td><td>221.50 (n/a)</td><td>223.90 (n/a)</td><td>206.20 (n/a)</td><td>8.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (+7.89%)</td><td>0.07 (-4.40%)</td><td>0.07 (-3.29%)</td><td>0.05 (-15.41%)</td><td>0.02 <b>(+54.19%)</b></td><td>328.30 (+18.22%)</td><td>237.84 (+7.37%)</td><td>225.40 (+3.39%)</td><td>172.10 (-7.32%)</td><td>57.40 <b>(+67.75%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>277.70 (n/a)</td><td>221.52 (n/a)</td><td>218.00 (n/a)</td><td>185.70 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 (+9.72%)</td><td>0.21 (+3.23%)</td><td>0.20 (+2.16%)</td><td>0.16 (-1.05%)</td><td>0.05 <b>(+33.65%)</b></td><td>199.30 (+1.06%)</td><td>163.42 (-1.85%)</td><td>165.80 (-2.13%)</td><td>115.80 (-8.82%)</td><td>31.12 <b>(+23.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>197.20 (n/a)</td><td>166.50 (n/a)</td><td>169.40 (n/a)</td><td>127.00 (n/a)</td><td>25.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (-10.95%)</td><td>0.20 (-5.90%)</td><td>0.19 (-8.41%)</td><td>0.18 (-3.50%)</td><td>0.02 (-16.84%)</td><td>177.70 (+3.68%)</td><td>165.52 (+6.14%)</td><td>171.40 (+9.17%)</td><td>150.90 (+12.28%)</td><td>13.28 (-2.33%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>171.40 (n/a)</td><td>155.94 (n/a)</td><td>157.00 (n/a)</td><td>134.40 (n/a)</td><td>13.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.29 (+9.94%)</td><td>0.23 (-5.31%)</td><td>0.22 (-15.76%)</td><td>0.20 (-6.14%)</td><td>0.04 <b>(+72.74%)</b></td><td>207.90 (+6.56%)</td><td>178.88 (+7.05%)</td><td>188.70 (+18.75%)</td><td>139.40 (-9.01%)</td><td>27.58 <b>(+64.39%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>167.10 (n/a)</td><td>158.90 (n/a)</td><td>153.20 (n/a)</td><td>16.78 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (-6.68%)</td><td>0.20 (-1.38%)</td><td>0.20 (+7.74%)</td><td>0.16 (-13.28%)</td><td>0.02 (+3.46%)</td><td>204.20 (+15.30%)</td><td>166.00 (+1.72%)</td><td>162.00 (-7.16%)</td><td>148.40 (+7.15%)</td><td>22.42 <b>(+28.27%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>177.10 (n/a)</td><td>163.20 (n/a)</td><td>174.50 (n/a)</td><td>138.50 (n/a)</td><td>17.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (-9.67%)</td><td>0.23 (-4.15%)</td><td>0.22 (+2.97%)</td><td>0.18 (+7.78%)</td><td>0.05 <b>(-25.48%)</b></td><td>230.50 (-7.24%)</td><td>186.14 (+1.86%)</td><td>189.10 (-2.88%)</td><td>135.30 (+10.63%)</td><td>36.80 <b>(-22.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>248.50 (n/a)</td><td>182.74 (n/a)</td><td>194.70 (n/a)</td><td>122.30 (n/a)</td><td>47.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 (+7.91%)</td><td>0.18 (-12.95%)</td><td>0.17 <b>(-21.31%)</b></td><td>0.12 (-19.67%)</td><td>0.06 <b>(+34.68%)</b></td><td>262.80 <b>(+24.49%)</b></td><td>189.90 (+18.54%)</td><td>188.80 <b>(+27.05%)</b></td><td>117.80 (-7.39%)</td><td>51.44 <b>(+49.33%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.10 (n/a)</td><td>160.20 (n/a)</td><td>148.60 (n/a)</td><td>127.20 (n/a)</td><td>34.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (-11.64%)</td><td>0.21 (-0.43%)</td><td>0.22 (+0.78%)</td><td>0.17 (+0.10%)</td><td>0.02 <b>(-39.14%)</b></td><td>222.00 (-0.13%)</td><td>180.66 (-1.21%)</td><td>169.10 (-0.76%)</td><td>167.40 (+13.18%)</td><td>23.47 <b>(-32.44%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>222.30 (n/a)</td><td>182.88 (n/a)</td><td>170.40 (n/a)</td><td>147.90 (n/a)</td><td>34.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 <b>(-25.44%)</b></td><td>0.18 (-15.32%)</td><td>0.18 (-0.78%)</td><td>0.16 (-11.16%)</td><td>0.02 <b>(-53.46%)</b></td><td>210.40 (+12.57%)</td><td>186.76 (+15.91%)</td><td>180.30 (+0.78%)</td><td>165.20 <b>(+34.09%)</b></td><td>20.27 <b>(-29.35%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.90 (n/a)</td><td>161.12 (n/a)</td><td>178.90 (n/a)</td><td>123.20 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 <b>(-26.14%)</b></td><td>0.19 (-13.38%)</td><td>0.19 (-10.57%)</td><td>0.17 (+14.96%)</td><td>0.02 <b>(-69.54%)</b></td><td>219.60 (-13.03%)</td><td>195.24 (+10.45%)</td><td>195.20 (+11.80%)</td><td>175.00 <b>(+35.45%)</b></td><td>16.42 <b>(-64.85%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>252.50 (n/a)</td><td>176.76 (n/a)</td><td>174.60 (n/a)</td><td>129.20 (n/a)</td><td>46.72 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (-19.10%)</td><td>0.17 (-19.69%)</td><td>0.16 <b>(-21.99%)</b></td><td>0.13 (-17.35%)</td><td>0.04 <b>(-24.62%)</b></td><td>243.50 <b>(+21.02%)</b></td><td>200.54 <b>(+23.17%)</b></td><td>206.70 <b>(+28.23%)</b></td><td>132.20 <b>(+23.67%)</b></td><td>41.53 (+4.47%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>201.20 (n/a)</td><td>162.82 (n/a)</td><td>161.20 (n/a)</td><td>106.90 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 <b>(-25.26%)</b></td><td>0.16 (-16.21%)</td><td>0.16 (-12.86%)</td><td>0.13 (-14.28%)</td><td>0.02 <b>(-51.52%)</b></td><td>263.90 (+16.67%)</td><td>222.44 (+17.01%)</td><td>223.30 (+14.75%)</td><td>190.90 <b>(+33.78%)</b></td><td>27.04 <b>(-24.87%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>226.20 (n/a)</td><td>190.10 (n/a)</td><td>194.60 (n/a)</td><td>142.70 (n/a)</td><td>36.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (-8.25%)</td><td>0.17 (-0.58%)</td><td>0.16 (-0.10%)</td><td>0.14 (-7.68%)</td><td>0.03 (-4.00%)</td><td>235.80 (+8.31%)</td><td>194.20 (+0.73%)</td><td>207.00 (+0.10%)</td><td>156.90 (+8.96%)</td><td>33.38 (+11.88%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>217.70 (n/a)</td><td>192.80 (n/a)</td><td>206.80 (n/a)</td><td>144.00 (n/a)</td><td>29.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (-0.72%)</td><td>0.18 (+2.16%)</td><td>0.17 (+6.12%)</td><td>0.14 (-3.90%)</td><td>0.03 (-1.20%)</td><td>244.40 (+4.04%)</td><td>201.36 (-2.14%)</td><td>210.00 (-5.79%)</td><td>163.00 (+0.74%)</td><td>33.61 (+0.39%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>234.90 (n/a)</td><td>205.76 (n/a)</td><td>222.90 (n/a)</td><td>161.80 (n/a)</td><td>33.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (-18.01%)</td><td>0.15 (-7.98%)</td><td>0.16 (-3.01%)</td><td>0.14 (-2.84%)</td><td>0.01 <b>(-44.77%)</b></td><td>242.70 (+2.93%)</td><td>213.26 (+7.52%)</td><td>202.20 (+3.11%)</td><td>194.30 <b>(+21.97%)</b></td><td>20.07 <b>(-30.21%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>235.80 (n/a)</td><td>198.34 (n/a)</td><td>196.10 (n/a)</td><td>159.30 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 <b>(+37.03%)</b></td><td>0.12 (+12.36%)</td><td>0.12 (+17.16%)</td><td>0.06 <b>(-36.09%)</b></td><td>0.04 <b>(+289.97%)</b></td><td>350.10 <b>(+56.50%)</b></td><td>195.66 (-0.49%)</td><td>167.80 (-14.65%)</td><td>126.00 <b>(-27.04%)</b></td><td>88.56 <b>(+382.35%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>196.62 (n/a)</td><td>196.60 (n/a)</td><td>172.70 (n/a)</td><td>18.36 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (-2.27%)</td><td>0.14 (+6.60%)</td><td>0.15 <b>(+27.08%)</b></td><td>0.11 (-2.00%)</td><td>0.02 (+2.06%)</td><td>186.40 (+2.03%)</td><td>150.22 (-5.98%)</td><td>136.50 <b>(-21.33%)</b></td><td>124.00 (+2.39%)</td><td>27.84 (+6.92%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>182.70 (n/a)</td><td>159.78 (n/a)</td><td>173.50 (n/a)</td><td>121.10 (n/a)</td><td>26.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (+10.13%)</td><td>0.12 (-1.76%)</td><td>0.12 (-9.17%)</td><td>0.10 (-0.75%)</td><td>0.03 <b>(+39.88%)</b></td><td>213.90 (+0.75%)</td><td>172.16 (+3.59%)</td><td>167.40 (+10.06%)</td><td>130.00 (-9.22%)</td><td>37.71 <b>(+30.66%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>212.30 (n/a)</td><td>166.20 (n/a)</td><td>152.10 (n/a)</td><td>143.20 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (-7.93%)</td><td>0.12 (-5.48%)</td><td>0.11 <b>(-24.05%)</b></td><td>0.09 (+5.51%)</td><td>0.03 <b>(-20.25%)</b></td><td>215.90 (-5.22%)</td><td>175.50 (+3.44%)</td><td>192.90 <b>(+31.67%)</b></td><td>130.60 (+8.65%)</td><td>36.93 <b>(-22.22%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>227.80 (n/a)</td><td>169.66 (n/a)</td><td>146.50 (n/a)</td><td>120.20 (n/a)</td><td>47.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (-1.00%)</td><td>0.13 (+10.06%)</td><td>0.13 <b>(+30.36%)</b></td><td>0.11 (+16.90%)</td><td>0.02 <b>(-32.49%)</b></td><td>194.70 (-14.46%)</td><td>164.88 (-12.15%)</td><td>162.60 <b>(-23.30%)</b></td><td>127.20 (+1.03%)</td><td>25.96 <b>(-43.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>227.60 (n/a)</td><td>187.68 (n/a)</td><td>212.00 (n/a)</td><td>125.90 (n/a)</td><td>45.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 <b>(+31.42%)</b></td><td>0.13 (+13.09%)</td><td>0.12 (-2.06%)</td><td>0.10 (+7.83%)</td><td>0.03 <b>(+112.20%)</b></td><td>196.10 (-7.24%)</td><td>161.42 (-9.07%)</td><td>170.60 (+2.09%)</td><td>119.20 <b>(-23.93%)</b></td><td>35.11 <b>(+51.04%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>177.52 (n/a)</td><td>167.10 (n/a)</td><td>156.70 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (+16.56%)</td><td>0.10 (+1.87%)</td><td>0.10 (-1.17%)</td><td>0.08 (-0.81%)</td><td>0.02 <b>(+50.10%)</b></td><td>252.90 (+0.84%)</td><td>206.70 (-0.54%)</td><td>209.70 (+1.16%)</td><td>150.00 (-14.24%)</td><td>36.74 <b>(+25.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>250.80 (n/a)</td><td>207.82 (n/a)</td><td>207.30 (n/a)</td><td>174.90 (n/a)</td><td>29.36 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 <b>(-21.36%)</b></td><td>0.12 (+0.49%)</td><td>0.11 (+17.90%)</td><td>0.10 (+10.91%)</td><td>0.01 <b>(-68.95%)</b></td><td>199.80 (-9.84%)</td><td>177.86 (-5.04%)</td><td>178.50 (-15.16%)</td><td>157.40 <b>(+27.14%)</b></td><td>15.19 <b>(-65.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>221.60 (n/a)</td><td>187.30 (n/a)</td><td>210.40 (n/a)</td><td>123.80 (n/a)</td><td>43.88 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (+14.08%)</td><td>0.15 (+15.65%)</td><td>0.15 (+8.41%)</td><td>0.12 <b>(+79.54%)</b></td><td>0.02 <b>(-44.10%)</b></td><td>208.70 <b>(-44.32%)</b></td><td>170.42 <b>(-20.27%)</b></td><td>163.00 (-7.75%)</td><td>145.00 (-12.33%)</td><td>24.03 <b>(-73.35%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>374.80 (n/a)</td><td>213.74 (n/a)</td><td>176.70 (n/a)</td><td>165.40 (n/a)</td><td>90.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (+8.73%)</td><td>0.17 <b>(+26.20%)</b></td><td>0.16 (+18.40%)</td><td>0.14 <b>(+38.53%)</b></td><td>0.03 (-18.35%)</td><td>172.40 <b>(-27.81%)</b></td><td>148.54 <b>(-22.55%)</b></td><td>155.10 (-15.52%)</td><td>122.50 (-8.03%)</td><td>22.25 <b>(-46.33%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>238.80 (n/a)</td><td>191.78 (n/a)</td><td>183.60 (n/a)</td><td>133.20 (n/a)</td><td>41.46 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 (+12.10%)</td><td>0.15 (+10.23%)</td><td>0.15 (+17.95%)</td><td>0.12 <b>(+21.02%)</b></td><td>0.02 (-10.01%)</td><td>203.60 (-17.37%)</td><td>167.08 (-10.47%)</td><td>161.90 (-15.24%)</td><td>132.00 (-10.81%)</td><td>26.81 <b>(-32.30%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>246.40 (n/a)</td><td>186.62 (n/a)</td><td>191.00 (n/a)</td><td>148.00 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (+7.88%)</td><td>0.14 (+17.15%)</td><td>0.14 <b>(+25.64%)</b></td><td>0.11 <b>(+28.33%)</b></td><td>0.03 (-11.64%)</td><td>219.00 <b>(-22.06%)</b></td><td>178.50 (-16.21%)</td><td>174.70 <b>(-20.41%)</b></td><td>136.00 (-7.29%)</td><td>31.90 <b>(-34.98%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>281.00 (n/a)</td><td>213.04 (n/a)</td><td>219.50 (n/a)</td><td>146.70 (n/a)</td><td>49.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (+2.77%)</td><td>0.17 (+7.98%)</td><td>0.18 <b>(+24.44%)</b></td><td>0.12 (-11.44%)</td><td>0.04 <b>(+48.62%)</b></td><td>199.20 (+12.93%)</td><td>152.20 (-5.18%)</td><td>133.20 (-19.61%)</td><td>121.10 (-2.65%)</td><td>35.11 <b>(+65.80%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>176.40 (n/a)</td><td>160.52 (n/a)</td><td>165.70 (n/a)</td><td>124.40 (n/a)</td><td>21.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 <b>(+20.46%)</b></td><td>0.16 (+14.57%)</td><td>0.16 <b>(+20.84%)</b></td><td>0.12 (+9.05%)</td><td>0.03 <b>(+47.68%)</b></td><td>197.00 (-8.33%)</td><td>159.72 (-11.65%)</td><td>157.90 (-17.24%)</td><td>127.00 (-16.99%)</td><td>30.84 (+15.29%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>214.90 (n/a)</td><td>180.78 (n/a)</td><td>190.80 (n/a)</td><td>153.00 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (-8.56%)</td><td>0.13 (-8.87%)</td><td>0.12 (-8.82%)</td><td>0.10 (-6.91%)</td><td>0.02 (-16.01%)</td><td>238.80 (+7.42%)</td><td>197.56 (+9.28%)</td><td>198.90 (+9.71%)</td><td>156.50 (+9.36%)</td><td>30.32 (-1.74%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>180.78 (n/a)</td><td>181.30 (n/a)</td><td>143.10 (n/a)</td><td>30.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 (+2.69%)</td><td>0.13 (+5.91%)</td><td>0.12 (+8.16%)</td><td>0.10 (+1.73%)</td><td>0.04 (+3.31%)</td><td>245.30 (-1.72%)</td><td>200.24 (-5.28%)</td><td>208.70 (-7.53%)</td><td>128.20 (-2.58%)</td><td>47.69 (+3.75%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>249.60 (n/a)</td><td>211.40 (n/a)</td><td>225.70 (n/a)</td><td>131.60 (n/a)</td><td>45.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (-12.09%)</td><td>0.10 (-9.11%)</td><td>0.10 (-8.32%)</td><td>0.08 (-10.02%)</td><td>0.01 (-16.78%)</td><td>226.70 (+11.13%)</td><td>192.46 (+9.75%)</td><td>187.90 (+9.05%)</td><td>167.40 (+13.72%)</td><td>25.99 (+3.00%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>175.36 (n/a)</td><td>172.30 (n/a)</td><td>147.20 (n/a)</td><td>25.23 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (-5.90%)</td><td>0.09 <b>(-28.18%)</b></td><td>0.10 (-17.58%)</td><td>0.05 <b>(-54.20%)</b></td><td>0.04 <b>(+161.69%)</b></td><td>394.80 <b>(+118.36%)</b></td><td>257.34 <b>(+64.02%)</b></td><td>193.00 <b>(+21.31%)</b></td><td>143.00 (+6.32%)</td><td>122.13 <b>(+563.30%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>180.80 (n/a)</td><td>156.90 (n/a)</td><td>159.10 (n/a)</td><td>134.50 (n/a)</td><td>18.41 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 <b>(+42.83%)</b></td><td>0.12 <b>(+25.05%)</b></td><td>0.12 <b>(+29.23%)</b></td><td>0.08 (+4.02%)</td><td>0.03 <b>(+116.06%)</b></td><td>230.60 (-3.88%)</td><td>165.10 (-17.50%)</td><td>158.60 <b>(-22.63%)</b></td><td>118.00 <b>(-30.01%)</b></td><td>41.06 <b>(+48.89%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>239.90 (n/a)</td><td>200.12 (n/a)</td><td>205.00 (n/a)</td><td>168.60 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (+5.89%)</td><td>0.12 (-4.46%)</td><td>0.12 (+4.37%)</td><td>0.09 (-12.90%)</td><td>0.02 <b>(+50.46%)</b></td><td>198.60 (+14.80%)</td><td>163.06 (+6.66%)</td><td>154.80 (-4.21%)</td><td>121.20 (-5.53%)</td><td>31.63 <b>(+67.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>173.00 (n/a)</td><td>152.88 (n/a)</td><td>161.60 (n/a)</td><td>128.30 (n/a)</td><td>18.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (+0.62%)</td><td>0.11 (+8.75%)</td><td>0.09 (-0.51%)</td><td>0.08 <b>(+23.50%)</b></td><td>0.03 (+2.54%)</td><td>233.90 (-19.04%)</td><td>184.14 (-8.82%)</td><td>211.50 (+0.48%)</td><td>120.20 (-0.66%)</td><td>52.78 (-15.61%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>288.90 (n/a)</td><td>201.96 (n/a)</td><td>210.50 (n/a)</td><td>121.00 (n/a)</td><td>62.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 <b>(+66.09%)</b></td><td>0.12 <b>(+25.92%)</b></td><td>0.10 (+0.85%)</td><td>0.09 <b>(+24.90%)</b></td><td>0.04 <b>(+168.64%)</b></td><td>203.00 (-19.95%)</td><td>170.14 (-17.03%)</td><td>189.10 (-0.84%)</td><td>102.80 <b>(-39.78%)</b></td><td>41.01 <b>(+25.51%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>253.60 (n/a)</td><td>205.06 (n/a)</td><td>190.70 (n/a)</td><td>170.70 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.12 (+6.76%)</td><td>0.10 (+0.30%)</td><td>0.09 (-11.05%)</td><td>0.08 (+17.90%)</td><td>0.01 (-16.90%)</td><td>226.30 (-15.18%)</td><td>194.96 (-1.60%)</td><td>197.30 (+12.42%)</td><td>157.70 (-6.30%)</td><td>26.71 <b>(-34.80%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>266.80 (n/a)</td><td>198.14 (n/a)</td><td>175.50 (n/a)</td><td>168.30 (n/a)</td><td>40.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (-6.55%)</td><td>0.10 (-2.10%)</td><td>0.10 (-1.69%)</td><td>0.07 (-13.41%)</td><td>0.01 (+8.29%)</td><td>253.90 (+15.46%)</td><td>196.78 (+2.78%)</td><td>189.60 (+1.72%)</td><td>169.20 (+6.95%)</td><td>33.03 <b>(+38.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>191.46 (n/a)</td><td>186.40 (n/a)</td><td>158.20 (n/a)</td><td>23.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.75 (-5.02%)</td><td>0.63 (+0.28%)</td><td>0.63 (+1.45%)</td><td>0.41 (-7.80%)</td><td>0.13 (-1.21%)</td><td>240.80 (+8.42%)</td><td>164.52 (+0.27%)</td><td>156.70 (-1.45%)</td><td>131.30 (+5.21%)</td><td>44.31 (+15.65%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.79 (n/a)</td><td>0.62 (n/a)</td><td>0.62 (n/a)</td><td>0.44 (n/a)</td><td>0.14 (n/a)</td><td>222.10 (n/a)</td><td>164.08 (n/a)</td><td>159.00 (n/a)</td><td>124.80 (n/a)</td><td>38.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.53 (-19.15%)</td><td>0.47 (-10.85%)</td><td>0.51 (-0.43%)</td><td>0.28 <b>(-33.06%)</b></td><td>0.11 (+18.92%)</td><td>346.70 <b>(+49.38%)</b></td><td>222.24 (+16.31%)</td><td>191.80 (+0.42%)</td><td>183.90 <b>(+23.67%)</b></td><td>70.00 <b>(+126.90%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.66 (n/a)</td><td>0.53 (n/a)</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.09 (n/a)</td><td>232.10 (n/a)</td><td>191.08 (n/a)</td><td>191.00 (n/a)</td><td>148.70 (n/a)</td><td>30.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.80 (+0.00%)</td><td>0.63 (+14.56%)</td><td>0.70 <b>(+40.70%)</b></td><td>0.45 (+6.24%)</td><td>0.16 (+2.92%)</td><td>216.20 (-5.88%)</td><td>163.54 (-12.54%)</td><td>140.10 <b>(-28.92%)</b></td><td>123.00 (+0.00%)</td><td>43.28 (-0.06%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 (n/a)</td><td>0.55 (n/a)</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.15 (n/a)</td><td>229.70 (n/a)</td><td>186.98 (n/a)</td><td>197.10 (n/a)</td><td>123.00 (n/a)</td><td>43.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.64 (+5.93%)</td><td>0.54 (+7.14%)</td><td>0.57 <b>(+21.72%)</b></td><td>0.42 (+0.18%)</td><td>0.09 <b>(+20.93%)</b></td><td>232.60 (-0.17%)</td><td>187.28 (-6.06%)</td><td>172.20 (-17.84%)</td><td>153.10 (-5.61%)</td><td>32.31 (+16.47%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.61 (n/a)</td><td>0.50 (n/a)</td><td>0.47 (n/a)</td><td>0.42 (n/a)</td><td>0.07 (n/a)</td><td>233.00 (n/a)</td><td>199.36 (n/a)</td><td>209.60 (n/a)</td><td>162.20 (n/a)</td><td>27.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.53 <b>(+23.27%)</b></td><td>0.39 (-1.44%)</td><td>0.39 (-7.19%)</td><td>0.25 (-16.26%)</td><td>0.10 <b>(+84.59%)</b></td><td>290.00 (+19.39%)</td><td>199.56 (+5.34%)</td><td>187.90 (+7.74%)</td><td>140.00 (-18.89%)</td><td>55.24 <b>(+82.84%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.05 (n/a)</td><td>242.90 (n/a)</td><td>189.44 (n/a)</td><td>174.40 (n/a)</td><td>172.60 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.57 <b>(+22.32%)</b></td><td>0.48 (+11.61%)</td><td>0.49 (+15.93%)</td><td>0.32 <b>(-20.09%)</b></td><td>0.09 <b>(+251.61%)</b></td><td>229.50 <b>(+25.14%)</b></td><td>160.70 (-7.06%)</td><td>150.00 (-13.74%)</td><td>130.20 (-18.22%)</td><td>39.78 <b>(+269.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.46 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.03 (n/a)</td><td>183.40 (n/a)</td><td>172.90 (n/a)</td><td>173.90 (n/a)</td><td>159.20 (n/a)</td><td>10.76 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.58 <b>(+20.43%)</b></td><td>0.43 (+3.42%)</td><td>0.42 (+10.21%)</td><td>0.25 <b>(-31.53%)</b></td><td>0.15 <b>(+196.82%)</b></td><td>300.90 <b>(+46.07%)</b></td><td>194.46 (+7.35%)</td><td>173.60 (-9.25%)</td><td>127.20 (-16.92%)</td><td>75.98 <b>(+246.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.05 (n/a)</td><td>206.00 (n/a)</td><td>181.14 (n/a)</td><td>191.30 (n/a)</td><td>153.10 (n/a)</td><td>21.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.49 (-1.09%)</td><td>0.39 (+3.43%)</td><td>0.39 (-0.93%)</td><td>0.29 (+10.36%)</td><td>0.07 <b>(-22.39%)</b></td><td>251.20 (-9.38%)</td><td>195.54 (-5.67%)</td><td>186.90 (+0.92%)</td><td>151.10 (+1.14%)</td><td>38.38 <b>(-30.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>277.20 (n/a)</td><td>207.30 (n/a)</td><td>185.20 (n/a)</td><td>149.40 (n/a)</td><td>54.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.29 (-2.92%)</td><td>0.23 (-0.62%)</td><td>0.22 (+7.00%)</td><td>0.19 (+1.97%)</td><td>0.04 (-17.18%)</td><td>192.10 (-1.94%)</td><td>165.94 (-0.23%)</td><td>166.50 (-6.57%)</td><td>128.50 (+2.96%)</td><td>23.44 (-17.99%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>195.90 (n/a)</td><td>166.32 (n/a)</td><td>178.20 (n/a)</td><td>124.80 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (+10.27%)</td><td>0.22 (-3.30%)</td><td>0.22 (-4.50%)</td><td>0.10 <b>(-48.35%)</b></td><td>0.08 <b>(+143.25%)</b></td><td>372.70 <b>(+93.61%)</b></td><td>195.12 (+18.66%)</td><td>170.20 (+4.74%)</td><td>123.20 (-9.28%)</td><td>101.92 <b>(+345.34%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>192.50 (n/a)</td><td>164.44 (n/a)</td><td>162.50 (n/a)</td><td>135.80 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (+18.45%)</td><td>0.20 (+5.03%)</td><td>0.18 (-7.01%)</td><td>0.16 (-6.57%)</td><td>0.04 <b>(+125.40%)</b></td><td>226.00 (+7.01%)</td><td>189.18 (-2.28%)</td><td>206.00 (+7.52%)</td><td>140.50 (-15.62%)</td><td>37.01 <b>(+102.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>211.20 (n/a)</td><td>193.60 (n/a)</td><td>191.60 (n/a)</td><td>166.50 (n/a)</td><td>18.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.29 <b>(+25.80%)</b></td><td>0.23 (+17.05%)</td><td>0.24 <b>(+25.16%)</b></td><td>0.12 <b>(-20.29%)</b></td><td>0.07 <b>(+136.69%)</b></td><td>304.40 <b>(+25.42%)</b></td><td>180.04 (-7.28%)</td><td>153.80 <b>(-20.06%)</b></td><td>125.40 <b>(-20.53%)</b></td><td>73.05 <b>(+137.84%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>242.70 (n/a)</td><td>194.18 (n/a)</td><td>192.40 (n/a)</td><td>157.80 (n/a)</td><td>30.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (+16.16%)</td><td>0.22 (-0.34%)</td><td>0.23 (-1.16%)</td><td>0.15 (-1.08%)</td><td>0.06 <b>(+35.48%)</b></td><td>244.50 (+1.07%)</td><td>173.36 (+2.22%)</td><td>157.70 (+1.15%)</td><td>122.70 (-13.89%)</td><td>46.96 (+15.02%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>241.90 (n/a)</td><td>169.60 (n/a)</td><td>155.90 (n/a)</td><td>142.50 (n/a)</td><td>40.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (-1.87%)</td><td>0.24 (+15.77%)</td><td>0.23 (+2.85%)</td><td>0.18 <b>(+78.91%)</b></td><td>0.05 <b>(-39.75%)</b></td><td>205.70 <b>(-44.10%)</b></td><td>157.54 <b>(-23.61%)</b></td><td>163.00 (-2.74%)</td><td>123.40 (+1.90%)</td><td>33.24 <b>(-66.87%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>368.00 (n/a)</td><td>206.22 (n/a)</td><td>167.60 (n/a)</td><td>121.10 (n/a)</td><td>100.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (-15.63%)</td><td>0.19 (-10.18%)</td><td>0.18 (-7.40%)</td><td>0.15 (-11.06%)</td><td>0.03 <b>(-32.07%)</b></td><td>246.60 (+12.45%)</td><td>202.86 (+9.99%)</td><td>202.60 (+8.00%)</td><td>170.00 (+18.55%)</td><td>31.10 (-11.75%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>219.30 (n/a)</td><td>184.44 (n/a)</td><td>187.60 (n/a)</td><td>143.40 (n/a)</td><td>35.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 <b>(-26.12%)</b></td><td>0.18 (-4.76%)</td><td>0.19 (+9.12%)</td><td>0.14 (-5.20%)</td><td>0.03 <b>(-47.52%)</b></td><td>262.50 (+5.51%)</td><td>205.90 (+2.30%)</td><td>190.20 (-8.38%)</td><td>178.10 <b>(+35.33%)</b></td><td>34.37 (-19.99%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>248.80 (n/a)</td><td>201.28 (n/a)</td><td>207.60 (n/a)</td><td>131.60 (n/a)</td><td>42.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.33 (+16.68%)</td><td>0.26 (+7.10%)</td><td>0.26 (+3.23%)</td><td>0.17 (-7.44%)</td><td>0.06 <b>(+52.13%)</b></td><td>244.40 (+8.05%)</td><td>167.12 (-3.81%)</td><td>156.90 (-3.15%)</td><td>122.80 (-14.31%)</td><td>47.77 <b>(+42.37%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>226.20 (n/a)</td><td>173.74 (n/a)</td><td>162.00 (n/a)</td><td>143.30 (n/a)</td><td>33.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.33 (+9.25%)</td><td>0.26 (+1.33%)</td><td>0.23 (-13.17%)</td><td>0.20 (+1.84%)</td><td>0.06 <b>(+25.56%)</b></td><td>209.40 (-1.78%)</td><td>166.68 (-0.16%)</td><td>179.80 (+15.18%)</td><td>124.80 (-8.50%)</td><td>36.95 (+10.88%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>213.20 (n/a)</td><td>166.94 (n/a)</td><td>156.10 (n/a)</td><td>136.40 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (+0.02%)</td><td>0.28 (+7.89%)</td><td>0.30 (+15.72%)</td><td>0.20 (+6.38%)</td><td>0.06 (-4.89%)</td><td>208.60 (-5.99%)</td><td>155.56 (-8.14%)</td><td>136.90 (-13.57%)</td><td>121.10 (+0.00%)</td><td>38.61 (-12.82%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>221.90 (n/a)</td><td>169.34 (n/a)</td><td>158.40 (n/a)</td><td>121.10 (n/a)</td><td>44.29 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.31 <b>(+23.66%)</b></td><td>0.24 (+11.50%)</td><td>0.22 (-3.94%)</td><td>0.18 <b>(+24.68%)</b></td><td>0.05 <b>(+31.27%)</b></td><td>221.50 (-19.80%)</td><td>175.92 (-10.14%)</td><td>184.70 (+4.11%)</td><td>131.30 (-19.10%)</td><td>36.94 (-19.57%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>276.20 (n/a)</td><td>195.78 (n/a)</td><td>177.40 (n/a)</td><td>162.30 (n/a)</td><td>45.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 <b>(-22.53%)</b></td><td>0.22 <b>(-24.48%)</b></td><td>0.22 (-19.16%)</td><td>0.16 <b>(-29.79%)</b></td><td>0.05 <b>(-26.25%)</b></td><td>259.60 <b>(+42.48%)</b></td><td>195.30 <b>(+32.07%)</b></td><td>185.40 <b>(+23.68%)</b></td><td>134.80 <b>(+29.12%)</b></td><td>45.57 <b>(+29.99%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>182.20 (n/a)</td><td>147.88 (n/a)</td><td>149.90 (n/a)</td><td>104.40 (n/a)</td><td>35.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.27 (-14.26%)</td><td>0.24 (-15.12%)</td><td>0.24 (-15.58%)</td><td>0.22 (-5.75%)</td><td>0.02 <b>(-31.82%)</b></td><td>183.40 (+6.13%)</td><td>169.48 (+17.32%)</td><td>167.40 (+18.47%)</td><td>150.40 (+16.68%)</td><td>14.07 (-16.25%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>172.80 (n/a)</td><td>144.46 (n/a)</td><td>141.30 (n/a)</td><td>128.90 (n/a)</td><td>16.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.29 <b>(+36.03%)</b></td><td>0.23 (+11.66%)</td><td>0.20 (+0.45%)</td><td>0.18 (-3.98%)</td><td>0.05 <b>(+562.79%)</b></td><td>222.60 (+4.16%)</td><td>186.78 (-7.79%)</td><td>200.70 (-0.45%)</td><td>143.00 <b>(-26.48%)</b></td><td>34.85 <b>(+402.08%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>202.56 (n/a)</td><td>201.60 (n/a)</td><td>194.50 (n/a)</td><td>6.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 <b>(-25.79%)</b></td><td>0.21 (-18.13%)</td><td>0.20 (-15.64%)</td><td>0.17 (-6.80%)</td><td>0.03 <b>(-48.00%)</b></td><td>235.50 (+7.29%)</td><td>202.96 (+18.83%)</td><td>208.40 (+18.54%)</td><td>161.30 <b>(+34.75%)</b></td><td>29.93 <b>(-24.29%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>219.50 (n/a)</td><td>170.80 (n/a)</td><td>175.80 (n/a)</td><td>119.70 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 <b>(+25.23%)</b></td><td>0.24 (+18.97%)</td><td>0.23 (+11.41%)</td><td>0.19 (+8.64%)</td><td>0.04 <b>(+60.77%)</b></td><td>183.50 (-7.93%)</td><td>147.50 (-14.90%)</td><td>154.10 (-10.25%)</td><td>116.70 <b>(-20.18%)</b></td><td>27.12 (+14.80%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>199.30 (n/a)</td><td>173.32 (n/a)</td><td>171.70 (n/a)</td><td>146.20 (n/a)</td><td>23.63 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.24 (+9.18%)</td><td>0.22 <b>(+25.44%)</b></td><td>0.22 (+9.26%)</td><td>0.19 <b>(+88.73%)</b></td><td>0.02 <b>(-64.71%)</b></td><td>183.20 <b>(-47.02%)</b></td><td>159.48 <b>(-26.45%)</b></td><td>155.30 (-8.49%)</td><td>146.20 (-8.45%)</td><td>13.96 <b>(-82.32%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>345.80 (n/a)</td><td>216.82 (n/a)</td><td>169.70 (n/a)</td><td>159.70 (n/a)</td><td>78.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.27 <b>(+47.08%)</b></td><td>0.21 (+19.50%)</td><td>0.20 (+13.38%)</td><td>0.16 (+0.93%)</td><td>0.04 <b>(+263.23%)</b></td><td>219.70 (-0.95%)</td><td>174.20 (-13.61%)</td><td>175.30 (-11.82%)</td><td>127.50 <b>(-32.00%)</b></td><td>36.05 <b>(+144.71%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>201.64 (n/a)</td><td>198.80 (n/a)</td><td>187.50 (n/a)</td><td>14.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 <b>(+21.17%)</b></td><td>0.20 <b>(+22.68%)</b></td><td>0.21 (+19.07%)</td><td>0.17 <b>(+20.10%)</b></td><td>0.02 (+8.00%)</td><td>209.30 (-16.71%)</td><td>173.64 (-18.76%)</td><td>165.20 (-16.01%)</td><td>153.70 (-17.50%)</td><td>22.97 <b>(-26.28%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>251.30 (n/a)</td><td>213.74 (n/a)</td><td>196.70 (n/a)</td><td>186.30 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 (-1.93%)</td><td>0.23 <b>(+23.46%)</b></td><td>0.25 <b>(+34.74%)</b></td><td>0.18 <b>(+46.18%)</b></td><td>0.05 <b>(-23.30%)</b></td><td>193.40 <b>(-31.59%)</b></td><td>155.22 <b>(-22.21%)</b></td><td>141.40 <b>(-25.77%)</b></td><td>123.90 (+1.98%)</td><td>32.62 <b>(-43.88%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>282.70 (n/a)</td><td>199.54 (n/a)</td><td>190.50 (n/a)</td><td>121.50 (n/a)</td><td>58.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (+9.21%)</td><td>0.22 (-4.99%)</td><td>0.22 (-11.33%)</td><td>0.16 (-10.02%)</td><td>0.06 <b>(+30.14%)</b></td><td>218.50 (+11.14%)</td><td>169.62 (+7.44%)</td><td>159.20 (+12.75%)</td><td>115.90 (-8.45%)</td><td>41.53 <b>(+31.83%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>196.60 (n/a)</td><td>157.88 (n/a)</td><td>141.20 (n/a)</td><td>126.60 (n/a)</td><td>31.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (-19.44%)</td><td>0.17 (-12.08%)</td><td>0.17 (-12.97%)</td><td>0.14 (-8.22%)</td><td>0.03 <b>(-29.44%)</b></td><td>256.50 (+8.96%)</td><td>205.34 (+12.73%)</td><td>200.80 (+14.94%)</td><td>176.50 <b>(+24.12%)</b></td><td>32.44 (-6.35%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>235.40 (n/a)</td><td>182.16 (n/a)</td><td>174.70 (n/a)</td><td>142.20 (n/a)</td><td>34.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (-8.09%)</td><td>0.18 (-1.93%)</td><td>0.18 (+1.99%)</td><td>0.16 (+7.62%)</td><td>0.02 <b>(-41.67%)</b></td><td>212.80 (-7.07%)</td><td>193.88 (+0.79%)</td><td>188.70 (-1.97%)</td><td>175.60 (+8.80%)</td><td>17.37 <b>(-39.52%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>229.00 (n/a)</td><td>192.36 (n/a)</td><td>192.50 (n/a)</td><td>161.40 (n/a)</td><td>28.72 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.97 (-5.14%)</td><td>0.94 (+15.66%)</td><td>0.96 <b>(+23.14%)</b></td><td>0.82 (+17.89%)</td><td>0.07 <b>(-50.70%)</b></td><td>160.70 (-15.20%)</td><td>140.82 (-14.91%)</td><td>136.20 (-18.78%)</td><td>135.00 (+5.47%)</td><td>11.13 <b>(-56.07%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.02 (n/a)</td><td>0.81 (n/a)</td><td>0.78 (n/a)</td><td>0.69 (n/a)</td><td>0.14 (n/a)</td><td>189.50 (n/a)</td><td>165.50 (n/a)</td><td>167.70 (n/a)</td><td>128.00 (n/a)</td><td>25.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.13 <b>(+40.85%)</b></td><td>0.95 <b>(+29.58%)</b></td><td>0.96 <b>(+24.77%)</b></td><td>0.78 <b>(+30.33%)</b></td><td>0.13 <b>(+53.42%)</b></td><td>168.30 <b>(-23.26%)</b></td><td>139.82 <b>(-22.61%)</b></td><td>136.40 (-19.86%)</td><td>116.30 <b>(-29.04%)</b></td><td>18.86 (-16.66%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 (n/a)</td><td>0.73 (n/a)</td><td>0.77 (n/a)</td><td>0.60 (n/a)</td><td>0.08 (n/a)</td><td>219.30 (n/a)</td><td>180.66 (n/a)</td><td>170.20 (n/a)</td><td>163.90 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.02 <b>(+38.46%)</b></td><td>0.80 <b>(+21.84%)</b></td><td>0.81 <b>(+26.23%)</b></td><td>0.58 (-4.98%)</td><td>0.15 <b>(+217.65%)</b></td><td>224.80 (+5.24%)</td><td>169.68 (-15.65%)</td><td>162.20 <b>(-20.76%)</b></td><td>129.00 <b>(-27.81%)</b></td><td>34.80 <b>(+146.59%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.73 (n/a)</td><td>0.65 (n/a)</td><td>0.64 (n/a)</td><td>0.61 (n/a)</td><td>0.05 (n/a)</td><td>213.60 (n/a)</td><td>201.16 (n/a)</td><td>204.70 (n/a)</td><td>178.70 (n/a)</td><td>14.11 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (+2.45%)</td><td>0.02 (-8.27%)</td><td>0.02 (-16.33%)</td><td>0.02 (+0.41%)</td><td>0.01 (+2.86%)</td><td>225.10 (-0.40%)</td><td>178.42 (+9.17%)</td><td>185.80 (+19.56%)</td><td>129.30 (-2.34%)</td><td>38.42 (+0.01%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.00 (n/a)</td><td>163.44 (n/a)</td><td>155.40 (n/a)</td><td>132.40 (n/a)</td><td>38.41 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 <b>(+23.25%)</b></td><td>0.03 <b>(+23.60%)</b></td><td>0.03 <b>(+20.92%)</b></td><td>0.02 <b>(+23.04%)</b></td><td>0.00 <b>(+22.43%)</b></td><td>179.70 (-18.76%)</td><td>148.72 (-19.13%)</td><td>149.60 (-17.30%)</td><td>128.20 (-18.91%)</td><td>21.48 (-19.85%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.20 (n/a)</td><td>183.90 (n/a)</td><td>180.90 (n/a)</td><td>158.10 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (+4.74%)</td><td>0.02 (+8.53%)</td><td>0.02 (+17.36%)</td><td>0.02 (+1.78%)</td><td>0.00 (+1.57%)</td><td>210.50 (-1.77%)</td><td>173.14 (-7.96%)</td><td>176.70 (-14.76%)</td><td>138.20 (-4.49%)</td><td>28.78 (-6.75%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.30 (n/a)</td><td>188.12 (n/a)</td><td>207.30 (n/a)</td><td>144.70 (n/a)</td><td>30.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>16.21 (+7.36%)</td><td>12.83 (+11.59%)</td><td>11.93 (-1.22%)</td><td>8.87 (+13.55%)</td><td>3.25 (+11.86%)</td><td>236.50 (-11.95%)</td><td>172.60 (-10.56%)</td><td>175.90 (+1.21%)</td><td>129.40 (-6.84%)</td><td>45.06 (-14.07%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>15.10 (n/a)</td><td>11.49 (n/a)</td><td>12.07 (n/a)</td><td>7.81 (n/a)</td><td>2.91 (n/a)</td><td>268.60 (n/a)</td><td>192.98 (n/a)</td><td>173.80 (n/a)</td><td>138.90 (n/a)</td><td>52.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.13 (+9.56%)</td><td>0.85 (+3.59%)</td><td>0.76 (-3.28%)</td><td>0.63 (-3.60%)</td><td>0.21 <b>(+46.44%)</b></td><td>209.00 (+3.72%)</td><td>162.78 (-1.17%)</td><td>174.80 (+3.43%)</td><td>116.90 (-8.74%)</td><td>38.23 <b>(+37.18%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.03 (n/a)</td><td>0.82 (n/a)</td><td>0.78 (n/a)</td><td>0.66 (n/a)</td><td>0.14 (n/a)</td><td>201.50 (n/a)</td><td>164.70 (n/a)</td><td>169.00 (n/a)</td><td>128.10 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.07 (-1.37%)</td><td>0.96 <b>(+21.00%)</b></td><td>1.04 <b>(+36.21%)</b></td><td>0.62 (-1.01%)</td><td>0.19 (+7.08%)</td><td>213.20 (+1.04%)</td><td>143.68 (-16.71%)</td><td>127.00 <b>(-26.59%)</b></td><td>123.60 (+1.39%)</td><td>38.97 (+12.65%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.08 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.63 (n/a)</td><td>0.18 (n/a)</td><td>211.00 (n/a)</td><td>172.50 (n/a)</td><td>173.00 (n/a)</td><td>121.90 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.04 <b>(+26.74%)</b></td><td>0.88 (+18.35%)</td><td>0.90 (+14.08%)</td><td>0.68 (+4.00%)</td><td>0.15 <b>(+94.79%)</b></td><td>194.00 (-3.87%)</td><td>153.96 (-14.13%)</td><td>147.10 (-12.28%)</td><td>127.50 <b>(-21.10%)</b></td><td>27.92 <b>(+44.70%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.82 (n/a)</td><td>0.74 (n/a)</td><td>0.79 (n/a)</td><td>0.65 (n/a)</td><td>0.08 (n/a)</td><td>201.80 (n/a)</td><td>179.30 (n/a)</td><td>167.70 (n/a)</td><td>161.60 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.47 <b>(+84.20%)</b></td><td>0.92 (+18.15%)</td><td>0.87 (+9.44%)</td><td>0.62 (-17.44%)</td><td>0.35 <b>(+1640.75%)</b></td><td>213.90 <b>(+21.12%)</b></td><td>158.66 (-6.26%)</td><td>152.70 (-8.62%)</td><td>90.00 <b>(-45.68%)</b></td><td>52.76 <b>(+1089.75%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.79 (n/a)</td><td>0.75 (n/a)</td><td>0.02 (n/a)</td><td>176.60 (n/a)</td><td>169.26 (n/a)</td><td>167.10 (n/a)</td><td>165.70 (n/a)</td><td>4.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.26 <b>(+32.95%)</b></td><td>0.95 <b>(+26.13%)</b></td><td>1.02 <b>(+40.51%)</b></td><td>0.56 (-12.11%)</td><td>0.27 <b>(+136.68%)</b></td><td>234.20 (+13.80%)</td><td>150.32 (-15.49%)</td><td>129.00 <b>(-28.81%)</b></td><td>104.50 <b>(-24.77%)</b></td><td>51.86 <b>(+114.21%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.95 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.64 (n/a)</td><td>0.12 (n/a)</td><td>205.80 (n/a)</td><td>177.88 (n/a)</td><td>181.20 (n/a)</td><td>138.90 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (+8.87%)</td><td>0.03 (+0.64%)</td><td>0.03 (+5.59%)</td><td>0.02 (-14.93%)</td><td>0.01 <b>(+79.42%)</b></td><td>217.30 (+17.52%)</td><td>169.12 (+1.79%)</td><td>161.20 (-5.29%)</td><td>128.40 (-8.09%)</td><td>35.01 <b>(+96.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.90 (n/a)</td><td>166.14 (n/a)</td><td>170.20 (n/a)</td><td>139.70 (n/a)</td><td>17.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (+10.83%)</td><td>0.02 (-1.53%)</td><td>0.02 (+4.11%)</td><td>0.02 (-14.81%)</td><td>0.01 <b>(+71.62%)</b></td><td>237.30 (+17.42%)</td><td>181.76 (+5.95%)</td><td>166.20 (-3.93%)</td><td>119.20 (-9.77%)</td><td>48.54 <b>(+92.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.10 (n/a)</td><td>171.56 (n/a)</td><td>173.00 (n/a)</td><td>132.10 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.00 (-2.22%)</td><td>0.00 (+0.48%)</td><td>0.00 (+0.00%)</td><td>0.00 (+5.26%)</td><td>0.00 <b>(-45.36%)</b></td><td>1033.34 (-3.55%)</td><td>978.66 (-0.67%)</td><td>980.47 (-0.53%)</td><td>928.78 (+0.92%)</td><td>37.49 <b>(-32.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1071.34 (n/a)</td><td>985.24 (n/a)</td><td>985.69 (n/a)</td><td>920.33 (n/a)</td><td>55.21 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.01 (-2.35%)</td><td>0.01 (-2.22%)</td><td>0.01 (+0.00%)</td><td>0.01 (-1.33%)</td><td>0.00 (+0.64%)</td><td>1101.32 (+1.45%)</td><td>1032.44 (+2.06%)</td><td>1007.62 (-0.15%)</td><td>986.33 (+2.75%)</td><td>50.99 (+2.96%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1085.55 (n/a)</td><td>1011.65 (n/a)</td><td>1009.12 (n/a)</td><td>959.90 (n/a)</td><td>49.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.99 (+3.88%)</td><td>0.96 (+1.89%)</td><td>0.95 (+0.85%)</td><td>0.94 (+2.26%)</td><td>0.02 <b>(+65.34%)</b></td><td>2222.24 (-2.22%)</td><td>2187.19 (-1.84%)</td><td>2202.25 (-0.83%)</td><td>2125.20 (-3.73%)</td><td>39.79 <b>(+55.18%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.92 (n/a)</td><td>0.01 (n/a)</td><td>2272.59 (n/a)</td><td>2228.13 (n/a)</td><td>2220.79 (n/a)</td><td>2207.65 (n/a)</td><td>25.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.91 (+1.53%)</td><td>0.88 (+0.58%)</td><td>0.88 (+0.61%)</td><td>0.85 (-0.95%)</td><td>0.02 <b>(+59.85%)</b></td><td>2455.17 (+0.96%)</td><td>2382.46 (-0.55%)</td><td>2386.13 (-0.61%)</td><td>2306.48 (-1.51%)</td><td>52.80 <b>(+59.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.86 (n/a)</td><td>0.01 (n/a)</td><td>2431.77 (n/a)</td><td>2395.65 (n/a)</td><td>2400.67 (n/a)</td><td>2341.90 (n/a)</td><td>33.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.00 (+2.52%)</td><td>0.97 (+2.77%)</td><td>0.98 (+3.79%)</td><td>0.96 (+3.26%)</td><td>0.01 (-10.41%)</td><td>2185.78 (-3.15%)</td><td>2153.41 (-2.70%)</td><td>2147.04 (-3.65%)</td><td>2106.49 (-2.45%)</td><td>32.81 (-15.16%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.02 (n/a)</td><td>2256.91 (n/a)</td><td>2213.15 (n/a)</td><td>2228.31 (n/a)</td><td>2159.48 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.67 (+0.13%)</td><td>0.66 (+3.01%)</td><td>0.66 (+3.12%)</td><td>0.65 (+7.76%)</td><td>0.01 <b>(-71.64%)</b></td><td>1616.90 (-7.20%)</td><td>1587.26 (-3.04%)</td><td>1581.10 (-3.03%)</td><td>1570.90 (-0.13%)</td><td>17.69 <b>(-73.70%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.67 (n/a)</td><td>0.64 (n/a)</td><td>0.64 (n/a)</td><td>0.60 (n/a)</td><td>0.03 (n/a)</td><td>1742.40 (n/a)</td><td>1637.04 (n/a)</td><td>1630.50 (n/a)</td><td>1573.00 (n/a)</td><td>67.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.22 (-0.02%)</td><td>1.16 (-1.06%)</td><td>1.16 (+0.48%)</td><td>1.12 (-1.33%)</td><td>0.04 (-5.17%)</td><td>939.00 (+1.35%)</td><td>905.98 (+1.07%)</td><td>905.80 (-0.47%)</td><td>860.80 (+0.02%)</td><td>29.23 (-3.91%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.22 (n/a)</td><td>1.17 (n/a)</td><td>1.15 (n/a)</td><td>1.13 (n/a)</td><td>0.04 (n/a)</td><td>926.50 (n/a)</td><td>896.42 (n/a)</td><td>910.10 (n/a)</td><td>860.60 (n/a)</td><td>30.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.19 (-1.52%)</td><td>1.15 (-1.15%)</td><td>1.14 (-2.23%)</td><td>1.12 (+2.34%)</td><td>0.03 <b>(-41.81%)</b></td><td>938.10 (-2.29%)</td><td>914.92 (+1.05%)</td><td>917.00 (+2.28%)</td><td>878.00 (+1.55%)</td><td>24.05 <b>(-42.15%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.21 (n/a)</td><td>1.16 (n/a)</td><td>1.17 (n/a)</td><td>1.09 (n/a)</td><td>0.05 (n/a)</td><td>960.10 (n/a)</td><td>905.42 (n/a)</td><td>896.60 (n/a)</td><td>864.60 (n/a)</td><td>41.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.11 (-0.85%)</td><td>1.94 (+2.25%)</td><td>1.91 (+1.38%)</td><td>1.82 (+8.22%)</td><td>0.11 <b>(-38.01%)</b></td><td>574.70 (-7.59%)</td><td>542.00 (-2.62%)</td><td>548.70 (-1.37%)</td><td>496.10 (+0.85%)</td><td>29.26 <b>(-42.66%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.13 (n/a)</td><td>1.90 (n/a)</td><td>1.88 (n/a)</td><td>1.69 (n/a)</td><td>0.18 (n/a)</td><td>621.90 (n/a)</td><td>556.60 (n/a)</td><td>556.30 (n/a)</td><td>491.90 (n/a)</td><td>51.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.70 (+1.92%)</td><td>0.66 (+3.78%)</td><td>0.65 (+0.74%)</td><td>0.64 (+7.89%)</td><td>0.03 <b>(-27.11%)</b></td><td>3294.70 (-7.31%)</td><td>3165.50 (-3.77%)</td><td>3210.60 (-0.73%)</td><td>3014.80 (-1.89%)</td><td>124.46 <b>(-34.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.68 (n/a)</td><td>0.64 (n/a)</td><td>0.65 (n/a)</td><td>0.59 (n/a)</td><td>0.04 (n/a)</td><td>3554.70 (n/a)</td><td>3289.64 (n/a)</td><td>3234.20 (n/a)</td><td>3072.80 (n/a)</td><td>188.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.32 (-0.69%)</td><td>1.28 (+3.10%)</td><td>1.27 (+1.91%)</td><td>1.23 (+6.85%)</td><td>0.04 <b>(-48.72%)</b></td><td>1706.50 (-6.41%)</td><td>1645.30 (-3.18%)</td><td>1650.10 (-1.87%)</td><td>1584.50 (+0.69%)</td><td>45.32 <b>(-51.75%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.33 (n/a)</td><td>1.24 (n/a)</td><td>1.25 (n/a)</td><td>1.15 (n/a)</td><td>0.07 (n/a)</td><td>1823.40 (n/a)</td><td>1699.38 (n/a)</td><td>1681.60 (n/a)</td><td>1573.60 (n/a)</td><td>93.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.33 (+1.48%)</td><td>1.27 (+0.87%)</td><td>1.27 (-0.27%)</td><td>1.21 (+0.46%)</td><td>0.05 (+13.34%)</td><td>1728.00 (-0.46%)</td><td>1647.16 (-0.84%)</td><td>1655.00 (+0.27%)</td><td>1574.50 (-1.46%)</td><td>59.78 (+10.88%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.31 (n/a)</td><td>1.26 (n/a)</td><td>1.27 (n/a)</td><td>1.21 (n/a)</td><td>0.04 (n/a)</td><td>1735.90 (n/a)</td><td>1661.14 (n/a)</td><td>1650.60 (n/a)</td><td>1597.90 (n/a)</td><td>53.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.41 (+2.58%)</td><td>2.16 (-2.30%)</td><td>2.33 (+3.07%)</td><td>1.44 <b>(-25.25%)</b></td><td>0.41 <b>(+145.35%)</b></td><td>1455.00 <b>(+33.77%)</b></td><td>1007.18 (+5.85%)</td><td>899.90 (-2.99%)</td><td>868.50 (-2.51%)</td><td>251.74 <b>(+221.28%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.35 (n/a)</td><td>2.21 (n/a)</td><td>2.26 (n/a)</td><td>1.93 (n/a)</td><td>0.17 (n/a)</td><td>1087.70 (n/a)</td><td>951.56 (n/a)</td><td>927.60 (n/a)</td><td>890.90 (n/a)</td><td>78.36 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.31 (-2.63%)</td><td>2.26 (-2.64%)</td><td>2.25 (-3.67%)</td><td>2.19 (-2.21%)</td><td>0.05 (-10.41%)</td><td>955.70 (+2.27%)</td><td>929.82 (+2.71%)</td><td>931.40 (+3.81%)</td><td>907.80 (+2.70%)</td><td>21.37 (-6.01%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.37 (n/a)</td><td>2.32 (n/a)</td><td>2.34 (n/a)</td><td>2.24 (n/a)</td><td>0.06 (n/a)</td><td>934.50 (n/a)</td><td>905.32 (n/a)</td><td>897.20 (n/a)</td><td>883.90 (n/a)</td><td>22.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.24 (+3.64%)</td><td>3.86 (+2.76%)</td><td>3.67 (-0.67%)</td><td>3.59 (+3.06%)</td><td>0.31 (+11.63%)</td><td>584.70 (-2.97%)</td><td>545.54 (-2.62%)</td><td>571.40 (+0.69%)</td><td>494.60 (-3.51%)</td><td>42.37 (+4.22%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.09 (n/a)</td><td>3.76 (n/a)</td><td>3.70 (n/a)</td><td>3.48 (n/a)</td><td>0.28 (n/a)</td><td>602.60 (n/a)</td><td>560.22 (n/a)</td><td>567.50 (n/a)</td><td>512.60 (n/a)</td><td>40.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.71 (+0.68%)</td><td>0.68 (-0.92%)</td><td>0.67 (-2.17%)</td><td>0.65 (+2.00%)</td><td>0.02 (-9.99%)</td><td>6488.20 (-1.97%)</td><td>6217.76 (+0.90%)</td><td>6217.00 (+2.22%)</td><td>5901.30 (-0.67%)</td><td>227.44 (-13.29%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.71 (n/a)</td><td>0.68 (n/a)</td><td>0.69 (n/a)</td><td>0.63 (n/a)</td><td>0.03 (n/a)</td><td>6618.30 (n/a)</td><td>6162.40 (n/a)</td><td>6082.10 (n/a)</td><td>5941.40 (n/a)</td><td>262.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.37 (-2.05%)</td><td>1.30 (-1.82%)</td><td>1.29 (-1.33%)</td><td>1.17 (-2.91%)</td><td>0.08 (+0.23%)</td><td>3597.00 (+3.00%)</td><td>3245.14 (+1.87%)</td><td>3246.40 (+1.35%)</td><td>3056.50 (+2.09%)</td><td>216.87 (+6.25%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.40 (n/a)</td><td>1.32 (n/a)</td><td>1.31 (n/a)</td><td>1.20 (n/a)</td><td>0.08 (n/a)</td><td>3492.40 (n/a)</td><td>3185.52 (n/a)</td><td>3203.20 (n/a)</td><td>2994.00 (n/a)</td><td>204.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.40 (+0.39%)</td><td>1.35 (+2.10%)</td><td>1.35 (-0.91%)</td><td>1.30 (+12.07%)</td><td>0.04 <b>(-60.61%)</b></td><td>3234.10 (-10.77%)</td><td>3120.18 (-2.47%)</td><td>3115.40 (+0.92%)</td><td>2986.20 (-0.39%)</td><td>90.29 <b>(-65.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.40 (n/a)</td><td>1.32 (n/a)</td><td>1.36 (n/a)</td><td>1.16 (n/a)</td><td>0.10 (n/a)</td><td>3624.60 (n/a)</td><td>3199.30 (n/a)</td><td>3087.10 (n/a)</td><td>2997.90 (n/a)</td><td>259.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.64 (-0.59%)</td><td>2.44 (-2.67%)</td><td>2.54 (+0.67%)</td><td>2.16 (-9.08%)</td><td>0.21 <b>(+107.85%)</b></td><td>1945.80 (+9.99%)</td><td>1729.54 (+3.27%)</td><td>1654.40 (-0.66%)</td><td>1588.30 (+0.59%)</td><td>157.28 <b>(+129.76%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.66 (n/a)</td><td>2.51 (n/a)</td><td>2.52 (n/a)</td><td>2.37 (n/a)</td><td>0.10 (n/a)</td><td>1769.10 (n/a)</td><td>1674.82 (n/a)</td><td>1665.40 (n/a)</td><td>1579.00 (n/a)</td><td>68.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.64 (-0.78%)</td><td>2.29 (-11.12%)</td><td>2.25 (-12.69%)</td><td>1.92 <b>(-23.78%)</b></td><td>0.28 <b>(+393.94%)</b></td><td>2179.60 <b>(+31.20%)</b></td><td>1850.94 (+13.87%)</td><td>1862.80 (+14.54%)</td><td>1586.40 (+0.78%)</td><td>232.44 <b>(+549.32%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.66 (n/a)</td><td>2.58 (n/a)</td><td>2.58 (n/a)</td><td>2.52 (n/a)</td><td>0.06 (n/a)</td><td>1661.30 (n/a)</td><td>1625.54 (n/a)</td><td>1626.40 (n/a)</td><td>1574.10 (n/a)</td><td>35.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.76 (+3.85%)</td><td>4.44 (-1.34%)</td><td>4.64 (+2.52%)</td><td>4.07 (-6.53%)</td><td>0.35 <b>(+273.19%)</b></td><td>1031.70 (+7.00%)</td><td>948.52 (+1.84%)</td><td>904.80 (-2.46%)</td><td>880.30 (-3.71%)</td><td>76.38 <b>(+288.25%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.59 (n/a)</td><td>4.50 (n/a)</td><td>4.52 (n/a)</td><td>4.35 (n/a)</td><td>0.09 (n/a)</td><td>964.20 (n/a)</td><td>931.40 (n/a)</td><td>927.60 (n/a)</td><td>914.20 (n/a)</td><td>19.67 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.84 (+6.41%)</td><td>4.68 (+6.92%)</td><td>4.71 (+5.84%)</td><td>4.50 (+12.81%)</td><td>0.13 <b>(-40.76%)</b></td><td>931.20 (-11.36%)</td><td>896.10 (-6.61%)</td><td>889.70 (-5.52%)</td><td>867.20 (-6.03%)</td><td>25.17 <b>(-51.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.55 (n/a)</td><td>4.38 (n/a)</td><td>4.45 (n/a)</td><td>3.99 (n/a)</td><td>0.22 (n/a)</td><td>1050.50 (n/a)</td><td>959.56 (n/a)</td><td>941.70 (n/a)</td><td>922.80 (n/a)</td><td>51.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>8.05 (+0.56%)</td><td>7.15 (+2.10%)</td><td>7.05 (-0.63%)</td><td>6.43 (+8.37%)</td><td>0.58 <b>(-33.91%)</b></td><td>651.90 (-7.73%)</td><td>590.04 (-2.82%)</td><td>595.40 (+0.64%)</td><td>521.00 (-0.55%)</td><td>46.80 <b>(-40.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>8.01 (n/a)</td><td>7.00 (n/a)</td><td>7.09 (n/a)</td><td>5.94 (n/a)</td><td>0.88 (n/a)</td><td>706.50 (n/a)</td><td>607.16 (n/a)</td><td>591.60 (n/a)</td><td>523.90 (n/a)</td><td>78.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.61 (+4.19%)</td><td>0.58 (+2.95%)</td><td>0.58 (+2.09%)</td><td>0.55 (+2.35%)</td><td>0.02 (+11.80%)</td><td>953.60 (-2.30%)</td><td>900.06 (-2.84%)</td><td>897.30 (-2.05%)</td><td>863.40 (-4.01%)</td><td>34.17 (+5.51%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.58 (n/a)</td><td>0.57 (n/a)</td><td>0.57 (n/a)</td><td>0.54 (n/a)</td><td>0.02 (n/a)</td><td>976.00 (n/a)</td><td>926.38 (n/a)</td><td>916.10 (n/a)</td><td>899.50 (n/a)</td><td>32.39 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.66 (+2.07%)</td><td>0.64 (+2.53%)</td><td>0.64 (+0.71%)</td><td>0.62 (+7.87%)</td><td>0.01 <b>(-51.31%)</b></td><td>1687.20 (-7.30%)</td><td>1646.80 (-2.59%)</td><td>1644.00 (-0.71%)</td><td>1599.40 (-2.03%)</td><td>33.09 <b>(-56.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.64 (n/a)</td><td>0.62 (n/a)</td><td>0.63 (n/a)</td><td>0.58 (n/a)</td><td>0.03 (n/a)</td><td>1820.00 (n/a)</td><td>1690.54 (n/a)</td><td>1655.70 (n/a)</td><td>1632.50 (n/a)</td><td>75.37 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.68 (-0.53%)</td><td>0.64 (+0.04%)</td><td>0.63 (-0.83%)</td><td>0.57 (+3.72%)</td><td>0.04 (-18.67%)</td><td>3659.20 (-3.59%)</td><td>3312.12 (-0.23%)</td><td>3311.90 (+0.83%)</td><td>3065.10 (+0.53%)</td><td>221.65 <b>(-21.89%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.69 (n/a)</td><td>0.64 (n/a)</td><td>0.64 (n/a)</td><td>0.55 (n/a)</td><td>0.05 (n/a)</td><td>3795.30 (n/a)</td><td>3319.92 (n/a)</td><td>3284.50 (n/a)</td><td>3048.90 (n/a)</td><td>283.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.03 (-1.59%)</td><td>1.01 (+3.26%)</td><td>1.02 (+4.89%)</td><td>0.94 (+5.11%)</td><td>0.04 <b>(-41.00%)</b></td><td>557.60 (-4.86%)</td><td>521.08 (-3.37%)</td><td>512.50 (-4.65%)</td><td>510.70 (+1.61%)</td><td>20.43 <b>(-42.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.04 (n/a)</td><td>0.98 (n/a)</td><td>0.98 (n/a)</td><td>0.89 (n/a)</td><td>0.06 (n/a)</td><td>586.10 (n/a)</td><td>539.26 (n/a)</td><td>537.50 (n/a)</td><td>502.60 (n/a)</td><td>35.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 (+6.83%)</td><td>0.16 (+3.73%)</td><td>0.16 (-1.67%)</td><td>0.14 (+3.00%)</td><td>0.02 (+19.02%)</td><td>233.80 (-2.91%)</td><td>202.34 (-3.39%)</td><td>206.30 (+1.73%)</td><td>173.80 (-6.41%)</td><td>22.11 (+7.09%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>240.80 (n/a)</td><td>209.44 (n/a)</td><td>202.80 (n/a)</td><td>185.70 (n/a)</td><td>20.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (+6.07%)</td><td>0.18 (+1.54%)</td><td>0.18 (+4.66%)</td><td>0.15 (-4.41%)</td><td>0.03 <b>(+68.81%)</b></td><td>221.90 (+4.62%)</td><td>188.48 (-0.04%)</td><td>185.50 (-4.43%)</td><td>153.70 (-5.76%)</td><td>31.71 <b>(+70.55%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.10 (n/a)</td><td>188.56 (n/a)</td><td>194.10 (n/a)</td><td>163.10 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (+1.56%)</td><td>0.26 (+0.73%)</td><td>0.26 (-3.23%)</td><td>0.23 (+6.44%)</td><td>0.02 (-10.71%)</td><td>282.70 (-6.05%)</td><td>250.18 (-0.99%)</td><td>254.50 (+3.33%)</td><td>220.40 (-1.52%)</td><td>23.10 (-19.59%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>300.90 (n/a)</td><td>252.68 (n/a)</td><td>246.30 (n/a)</td><td>223.80 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (-4.78%)</td><td>0.32 (+5.55%)</td><td>0.32 (+4.90%)</td><td>0.27 (+8.38%)</td><td>0.03 <b>(-40.79%)</b></td><td>241.20 (-7.73%)</td><td>208.50 (-6.55%)</td><td>202.50 (-4.66%)</td><td>191.30 (+4.99%)</td><td>20.04 <b>(-44.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>261.40 (n/a)</td><td>223.12 (n/a)</td><td>212.40 (n/a)</td><td>182.20 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.37 <b>(-20.19%)</b></td><td>0.35 (-1.48%)</td><td>0.35 (+3.84%)</td><td>0.32 (+15.88%)</td><td>0.02 <b>(-75.81%)</b></td><td>202.30 (-13.69%)</td><td>188.74 (-1.42%)</td><td>187.70 (-3.69%)</td><td>175.60 <b>(+25.34%)</b></td><td>9.57 <b>(-73.60%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.07 (n/a)</td><td>234.40 (n/a)</td><td>191.46 (n/a)</td><td>194.90 (n/a)</td><td>140.10 (n/a)</td><td>36.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.43 (+14.43%)</td><td>0.38 (+14.68%)</td><td>0.41 <b>(+29.37%)</b></td><td>0.29 (-0.25%)</td><td>0.07 <b>(+75.40%)</b></td><td>457.10 (+0.26%)</td><td>358.22 (-11.24%)</td><td>318.10 <b>(-22.70%)</b></td><td>302.40 (-12.60%)</td><td>70.25 <b>(+51.47%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>455.90 (n/a)</td><td>403.58 (n/a)</td><td>411.50 (n/a)</td><td>346.00 (n/a)</td><td>46.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.56 (-7.69%)</td><td>0.50 (+6.21%)</td><td>0.52 (+7.39%)</td><td>0.42 (+18.55%)</td><td>0.05 <b>(-48.56%)</b></td><td>308.90 (-15.65%)</td><td>262.22 (-8.18%)</td><td>253.10 (-6.88%)</td><td>235.60 (+8.32%)</td><td>27.96 <b>(-52.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.60 (n/a)</td><td>0.47 (n/a)</td><td>0.48 (n/a)</td><td>0.36 (n/a)</td><td>0.10 (n/a)</td><td>366.20 (n/a)</td><td>285.58 (n/a)</td><td>271.80 (n/a)</td><td>217.50 (n/a)</td><td>58.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.74 (+10.05%)</td><td>0.64 (+6.05%)</td><td>0.66 (+11.47%)</td><td>0.46 (-17.06%)</td><td>0.11 <b>(+131.17%)</b></td><td>283.60 <b>(+20.58%)</b></td><td>209.66 (-3.44%)</td><td>200.00 (-10.27%)</td><td>176.50 (-9.11%)</td><td>43.06 <b>(+159.90%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.67 (n/a)</td><td>0.61 (n/a)</td><td>0.59 (n/a)</td><td>0.56 (n/a)</td><td>0.05 (n/a)</td><td>235.20 (n/a)</td><td>217.14 (n/a)</td><td>222.90 (n/a)</td><td>194.20 (n/a)</td><td>16.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.89 <b>(+21.81%)</b></td><td>0.70 (+6.69%)</td><td>0.70 (+13.35%)</td><td>0.46 (-18.79%)</td><td>0.15 <b>(+121.23%)</b></td><td>282.80 <b>(+23.12%)</b></td><td>196.98 (-2.78%)</td><td>186.00 (-11.76%)</td><td>146.70 (-17.91%)</td><td>50.88 <b>(+138.15%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.73 (n/a)</td><td>0.65 (n/a)</td><td>0.62 (n/a)</td><td>0.57 (n/a)</td><td>0.07 (n/a)</td><td>229.70 (n/a)</td><td>202.62 (n/a)</td><td>210.80 (n/a)</td><td>178.70 (n/a)</td><td>21.37 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (-3.80%)</td><td>0.09 (+13.95%)</td><td>0.10 (+13.18%)</td><td>0.07 <b>(+50.90%)</b></td><td>0.01 <b>(-44.12%)</b></td><td>229.50 <b>(-33.73%)</b></td><td>181.44 (-18.16%)</td><td>171.40 (-11.65%)</td><td>149.30 (+3.97%)</td><td>30.29 <b>(-61.68%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>346.30 (n/a)</td><td>221.70 (n/a)</td><td>194.00 (n/a)</td><td>143.60 (n/a)</td><td>79.04 (n/a)</td>
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
