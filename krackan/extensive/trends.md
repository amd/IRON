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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (-17.27%)</td><td>0.03 (-10.96%)</td><td>0.03 (-2.70%)</td><td>0.03 (-0.11%)</td><td>0.01 <b>(-45.08%)</b></td><td>228.50 (+0.09%)</td><td>193.72 (+8.09%)</td><td>203.10 (+2.78%)</td><td>150.20 <b>(+20.93%)</b></td><td>31.62 <b>(-32.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>228.30 (n/a)</td><td>179.22 (n/a)</td><td>197.60 (n/a)</td><td>124.20 (n/a)</td><td>47.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (+14.63%)</td><td>0.04 (+17.63%)</td><td>0.04 (+17.92%)</td><td>0.04 <b>(+30.28%)</b></td><td>0.00 (-8.96%)</td><td>175.30 <b>(-23.25%)</b></td><td>155.88 (-15.77%)</td><td>157.20 (-15.21%)</td><td>129.10 (-12.77%)</td><td>18.41 <b>(-39.01%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>185.06 (n/a)</td><td>185.40 (n/a)</td><td>148.00 (n/a)</td><td>30.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (-5.81%)</td><td>0.04 (+4.77%)</td><td>0.04 (+6.68%)</td><td>0.03 (-5.87%)</td><td>0.01 (-6.68%)</td><td>212.70 (+6.24%)</td><td>160.02 (-4.55%)</td><td>154.90 (-6.23%)</td><td>132.00 (+6.19%)</td><td>31.85 (+7.16%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>167.64 (n/a)</td><td>165.20 (n/a)</td><td>124.30 (n/a)</td><td>29.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (+1.40%)</td><td>0.04 (-4.06%)</td><td>0.04 (-9.53%)</td><td>0.03 (+4.21%)</td><td>0.01 <b>(-26.89%)</b></td><td>183.10 (-4.04%)</td><td>158.04 (+2.26%)</td><td>159.20 (+10.56%)</td><td>122.10 (-1.37%)</td><td>22.35 <b>(-33.66%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>154.54 (n/a)</td><td>144.00 (n/a)</td><td>123.80 (n/a)</td><td>33.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (+10.82%)</td><td>0.04 (+2.47%)</td><td>0.04 (-2.11%)</td><td>0.03 (-2.39%)</td><td>0.01 <b>(+80.05%)</b></td><td>201.60 (+2.44%)</td><td>168.74 (-0.58%)</td><td>170.30 (+2.16%)</td><td>133.40 (-9.74%)</td><td>31.13 <b>(+66.63%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>196.80 (n/a)</td><td>169.72 (n/a)</td><td>166.70 (n/a)</td><td>147.80 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (-10.24%)</td><td>0.03 (-5.43%)</td><td>0.03 (-6.00%)</td><td>0.03 (+12.80%)</td><td>0.00 <b>(-59.97%)</b></td><td>198.00 (-11.33%)</td><td>184.22 (+3.91%)</td><td>187.20 (+6.36%)</td><td>167.10 (+11.40%)</td><td>11.82 <b>(-60.17%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>177.28 (n/a)</td><td>176.00 (n/a)</td><td>150.00 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 <b>(+20.54%)</b></td><td>0.03 (+2.32%)</td><td>0.03 (-0.56%)</td><td>0.03 (+3.54%)</td><td>0.01 <b>(+95.74%)</b></td><td>202.90 (-3.43%)</td><td>179.40 (-1.00%)</td><td>180.10 (+0.56%)</td><td>137.50 (-17.07%)</td><td>26.25 <b>(+53.34%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>210.10 (n/a)</td><td>181.22 (n/a)</td><td>179.10 (n/a)</td><td>165.80 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (-3.78%)</td><td>0.04 (+15.28%)</td><td>0.04 <b>(+29.49%)</b></td><td>0.03 <b>(+27.59%)</b></td><td>0.00 <b>(-58.70%)</b></td><td>198.10 <b>(-21.61%)</b></td><td>171.18 (-16.10%)</td><td>165.10 <b>(-22.78%)</b></td><td>160.50 (+3.95%)</td><td>15.27 <b>(-65.20%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.70 (n/a)</td><td>204.02 (n/a)</td><td>213.80 (n/a)</td><td>154.40 (n/a)</td><td>43.89 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (-11.79%)</td><td>0.08 (-2.13%)</td><td>0.08 (-6.03%)</td><td>0.07 <b>(+20.49%)</b></td><td>0.01 <b>(-57.39%)</b></td><td>168.30 (-17.01%)</td><td>151.60 (-0.22%)</td><td>152.60 (+6.42%)</td><td>136.80 (+13.34%)</td><td>11.77 <b>(-61.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>151.94 (n/a)</td><td>143.40 (n/a)</td><td>120.70 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 (+1.11%)</td><td>0.08 (-3.63%)</td><td>0.08 (-18.10%)</td><td>0.06 (+11.34%)</td><td>0.02 (-19.33%)</td><td>209.40 (-10.21%)</td><td>158.04 (+1.13%)</td><td>154.60 <b>(+22.12%)</b></td><td>121.60 (-1.06%)</td><td>35.46 <b>(-26.64%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.20 (n/a)</td><td>156.28 (n/a)</td><td>126.60 (n/a)</td><td>122.90 (n/a)</td><td>48.33 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 (+0.26%)</td><td>0.08 (+10.51%)</td><td>0.08 (+12.45%)</td><td>0.06 (-13.19%)</td><td>0.02 <b>(+24.14%)</b></td><td>216.80 (+15.20%)</td><td>158.18 (-7.93%)</td><td>161.90 (-11.04%)</td><td>124.30 (-0.32%)</td><td>37.67 <b>(+41.07%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>171.80 (n/a)</td><td>182.00 (n/a)</td><td>124.70 (n/a)</td><td>26.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (-0.71%)</td><td>0.08 (+11.02%)</td><td>0.08 (+13.41%)</td><td>0.07 <b>(+30.68%)</b></td><td>0.01 <b>(-23.54%)</b></td><td>181.20 <b>(-23.45%)</b></td><td>154.82 (-11.59%)</td><td>145.20 (-11.84%)</td><td>134.30 (+0.67%)</td><td>22.06 <b>(-42.03%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.70 (n/a)</td><td>175.12 (n/a)</td><td>164.70 (n/a)</td><td>133.40 (n/a)</td><td>38.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (-8.19%)</td><td>0.06 (-0.45%)</td><td>0.06 (-11.45%)</td><td>0.06 <b>(+24.35%)</b></td><td>0.01 <b>(-44.48%)</b></td><td>220.90 (-19.59%)</td><td>192.64 (-3.38%)</td><td>199.20 (+12.93%)</td><td>163.10 (+8.88%)</td><td>25.63 <b>(-52.00%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>274.70 (n/a)</td><td>199.38 (n/a)</td><td>176.40 (n/a)</td><td>149.80 (n/a)</td><td>53.39 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 <b>(+20.04%)</b></td><td>0.07 (+12.25%)</td><td>0.07 (+14.03%)</td><td>0.06 (+11.34%)</td><td>0.01 <b>(+47.63%)</b></td><td>196.00 (-10.17%)</td><td>170.72 (-10.02%)</td><td>168.30 (-12.34%)</td><td>126.60 (-16.66%)</td><td>28.34 (+11.91%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>189.74 (n/a)</td><td>192.00 (n/a)</td><td>151.90 (n/a)</td><td>25.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 <b>(-21.91%)</b></td><td>0.06 (-3.96%)</td><td>0.06 (+1.97%)</td><td>0.05 (+2.59%)</td><td>0.01 <b>(-60.34%)</b></td><td>239.60 (-2.52%)</td><td>210.34 (+0.86%)</td><td>211.20 (-1.95%)</td><td>181.60 <b>(+28.07%)</b></td><td>20.96 <b>(-50.19%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>245.80 (n/a)</td><td>208.54 (n/a)</td><td>215.40 (n/a)</td><td>141.80 (n/a)</td><td>42.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (-3.70%)</td><td>0.06 (+3.03%)</td><td>0.06 (+11.57%)</td><td>0.06 (+3.47%)</td><td>0.01 <b>(-26.67%)</b></td><td>214.00 (-3.34%)</td><td>192.40 (-3.67%)</td><td>192.10 (-10.40%)</td><td>162.50 (+3.90%)</td><td>19.68 <b>(-26.75%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>199.74 (n/a)</td><td>214.40 (n/a)</td><td>156.40 (n/a)</td><td>26.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 <b>(-22.79%)</b></td><td>0.13 (-14.20%)</td><td>0.14 (-19.85%)</td><td>0.12 (+9.65%)</td><td>0.01 <b>(-63.62%)</b></td><td>212.80 (-8.83%)</td><td>185.24 (+10.75%)</td><td>179.20 <b>(+24.70%)</b></td><td>161.30 <b>(+29.56%)</b></td><td>20.72 <b>(-56.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>233.40 (n/a)</td><td>167.26 (n/a)</td><td>143.70 (n/a)</td><td>124.50 (n/a)</td><td>47.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.20 (+19.39%)</td><td>0.17 <b>(+20.43%)</b></td><td>0.17 (+19.50%)</td><td>0.14 (+16.89%)</td><td>0.02 <b>(+28.42%)</b></td><td>174.00 (-14.41%)</td><td>146.00 (-16.79%)</td><td>145.50 (-16.33%)</td><td>125.50 (-16.22%)</td><td>18.02 (-6.95%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.30 (n/a)</td><td>175.46 (n/a)</td><td>173.90 (n/a)</td><td>149.80 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (-10.12%)</td><td>0.13 (-10.77%)</td><td>0.12 (-16.50%)</td><td>0.11 (-13.92%)</td><td>0.01 (-7.60%)</td><td>229.10 (+16.18%)</td><td>195.32 (+12.16%)</td><td>196.80 (+19.78%)</td><td>176.00 (+11.25%)</td><td>21.72 (+18.05%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>174.14 (n/a)</td><td>164.30 (n/a)</td><td>158.20 (n/a)</td><td>18.40 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (-15.04%)</td><td>0.14 (-3.83%)</td><td>0.14 (+3.32%)</td><td>0.12 (+15.52%)</td><td>0.02 <b>(-49.64%)</b></td><td>203.80 (-13.46%)</td><td>178.32 (+1.21%)</td><td>174.30 (-3.22%)</td><td>157.40 (+17.73%)</td><td>19.80 <b>(-48.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>235.50 (n/a)</td><td>176.18 (n/a)</td><td>180.10 (n/a)</td><td>133.70 (n/a)</td><td>38.74 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.18 (+2.08%)</td><td>0.14 (-1.51%)</td><td>0.13 (-10.66%)</td><td>0.13 <b>(+45.58%)</b></td><td>0.02 <b>(-41.33%)</b></td><td>190.20 <b>(-31.31%)</b></td><td>173.22 (-3.01%)</td><td>182.90 (+11.87%)</td><td>139.30 (-2.04%)</td><td>21.59 <b>(-61.47%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>276.90 (n/a)</td><td>178.60 (n/a)</td><td>163.50 (n/a)</td><td>142.20 (n/a)</td><td>56.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.18 <b>(+24.29%)</b></td><td>0.13 (-2.40%)</td><td>0.12 (-15.38%)</td><td>0.07 <b>(-37.44%)</b></td><td>0.05 <b>(+262.53%)</b></td><td>347.50 <b>(+59.84%)</b></td><td>212.54 (+14.08%)</td><td>206.90 (+18.16%)</td><td>138.10 (-19.57%)</td><td>85.36 <b>(+344.84%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>186.30 (n/a)</td><td>175.10 (n/a)</td><td>171.70 (n/a)</td><td>19.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.19 <b>(+27.22%)</b></td><td>0.13 (-8.44%)</td><td>0.12 (-18.09%)</td><td>0.11 (-14.57%)</td><td>0.03 <b>(+294.92%)</b></td><td>222.20 (+17.07%)</td><td>194.26 (+13.62%)</td><td>206.20 <b>(+22.08%)</b></td><td>127.60 <b>(-21.38%)</b></td><td>38.98 <b>(+253.53%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>170.98 (n/a)</td><td>168.90 (n/a)</td><td>162.30 (n/a)</td><td>11.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (+4.86%)</td><td>0.14 (+6.24%)</td><td>0.14 (+10.71%)</td><td>0.12 (+8.26%)</td><td>0.01 (-18.98%)</td><td>200.60 (-7.60%)</td><td>178.34 (-6.43%)</td><td>177.70 (-9.66%)</td><td>152.50 (-4.63%)</td><td>17.89 <b>(-28.95%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.10 (n/a)</td><td>190.60 (n/a)</td><td>196.70 (n/a)</td><td>159.90 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.43 (+12.17%)</td><td>0.30 (-11.21%)</td><td>0.26 (-19.19%)</td><td>0.23 (-13.73%)</td><td>0.08 <b>(+78.29%)</b></td><td>209.90 (+15.90%)</td><td>173.34 (+16.37%)</td><td>187.50 <b>(+23.76%)</b></td><td>114.80 (-10.87%)</td><td>38.40 <b>(+83.51%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>181.10 (n/a)</td><td>148.96 (n/a)</td><td>151.50 (n/a)</td><td>128.80 (n/a)</td><td>20.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.40 (+18.28%)</td><td>0.33 (+13.24%)</td><td>0.32 (+8.12%)</td><td>0.29 <b>(+23.41%)</b></td><td>0.04 (+15.57%)</td><td>168.40 (-19.00%)</td><td>150.88 (-11.84%)</td><td>152.50 (-7.52%)</td><td>122.50 (-15.46%)</td><td>17.64 <b>(-23.56%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>207.90 (n/a)</td><td>171.14 (n/a)</td><td>164.90 (n/a)</td><td>144.90 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.33 (-1.44%)</td><td>0.28 (-7.49%)</td><td>0.27 (-5.80%)</td><td>0.24 (-16.31%)</td><td>0.04 <b>(+40.30%)</b></td><td>208.30 (+19.51%)</td><td>177.84 (+9.16%)</td><td>184.30 (+6.16%)</td><td>147.40 (+1.45%)</td><td>25.50 <b>(+67.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>174.30 (n/a)</td><td>162.92 (n/a)</td><td>173.60 (n/a)</td><td>145.30 (n/a)</td><td>15.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.29 <b>(-31.77%)</b></td><td>0.27 (-7.36%)</td><td>0.27 (-0.35%)</td><td>0.25 (+6.74%)</td><td>0.01 <b>(-81.22%)</b></td><td>197.70 (-6.30%)</td><td>181.54 (+3.17%)</td><td>181.00 (+0.33%)</td><td>170.10 <b>(+46.51%)</b></td><td>10.13 <b>(-73.91%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>211.00 (n/a)</td><td>175.96 (n/a)</td><td>180.40 (n/a)</td><td>116.10 (n/a)</td><td>38.82 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.33 (-4.62%)</td><td>0.29 (+6.50%)</td><td>0.29 (+3.08%)</td><td>0.26 <b>(+40.98%)</b></td><td>0.03 <b>(-58.25%)</b></td><td>186.40 <b>(-29.07%)</b></td><td>167.92 (-9.86%)</td><td>170.00 (-2.97%)</td><td>148.90 (+4.86%)</td><td>14.74 <b>(-69.30%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>262.80 (n/a)</td><td>186.28 (n/a)</td><td>175.20 (n/a)</td><td>142.00 (n/a)</td><td>48.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.36 <b>(+27.33%)</b></td><td>0.29 <b>(+20.03%)</b></td><td>0.28 (+3.90%)</td><td>0.25 <b>(+50.72%)</b></td><td>0.05 (-3.13%)</td><td>199.20 <b>(-33.67%)</b></td><td>173.00 (-18.37%)</td><td>177.80 (-3.79%)</td><td>137.10 <b>(-21.43%)</b></td><td>26.45 <b>(-49.49%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>300.30 (n/a)</td><td>211.94 (n/a)</td><td>184.80 (n/a)</td><td>174.50 (n/a)</td><td>52.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.35 (+17.55%)</td><td>0.28 (+5.51%)</td><td>0.28 (-5.61%)</td><td>0.24 (+15.71%)</td><td>0.04 (+8.03%)</td><td>205.80 (-13.57%)</td><td>177.02 (-5.50%)</td><td>177.50 (+5.97%)</td><td>139.30 (-14.96%)</td><td>25.34 <b>(-20.64%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>238.10 (n/a)</td><td>187.32 (n/a)</td><td>167.50 (n/a)</td><td>163.80 (n/a)</td><td>31.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.37 (+9.80%)</td><td>0.28 (+7.47%)</td><td>0.30 <b>(+25.86%)</b></td><td>0.16 <b>(-22.39%)</b></td><td>0.09 <b>(+54.42%)</b></td><td>311.50 <b>(+28.88%)</b></td><td>189.98 (-1.09%)</td><td>163.70 <b>(-20.53%)</b></td><td>131.80 (-8.91%)</td><td>73.28 <b>(+86.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>241.70 (n/a)</td><td>192.08 (n/a)</td><td>206.00 (n/a)</td><td>144.70 (n/a)</td><td>39.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 (+1.51%)</td><td>0.02 (+3.90%)</td><td>0.02 (-0.79%)</td><td>0.01 (+8.75%)</td><td>0.00 (-11.32%)</td><td>181.40 (-8.06%)</td><td>155.38 (-4.50%)</td><td>158.70 (+0.76%)</td><td>120.40 (-1.47%)</td><td>22.36 <b>(-21.10%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>197.30 (n/a)</td><td>162.70 (n/a)</td><td>157.50 (n/a)</td><td>122.20 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 <b>(+20.89%)</b></td><td>0.02 (+12.84%)</td><td>0.02 <b>(+23.90%)</b></td><td>0.01 (+5.54%)</td><td>0.00 <b>(+62.50%)</b></td><td>196.40 (-5.21%)</td><td>158.88 (-9.91%)</td><td>147.50 (-19.31%)</td><td>122.50 (-17.29%)</td><td>31.40 <b>(+32.41%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>207.20 (n/a)</td><td>176.36 (n/a)</td><td>182.80 (n/a)</td><td>148.10 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 (-1.51%)</td><td>0.02 (+5.00%)</td><td>0.02 (+9.26%)</td><td>0.01 (+5.73%)</td><td>0.00 (-0.59%)</td><td>221.60 (-5.42%)</td><td>171.76 (-4.96%)</td><td>165.10 (-8.48%)</td><td>144.10 (+1.55%)</td><td>32.27 (-7.03%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>234.30 (n/a)</td><td>180.72 (n/a)</td><td>180.40 (n/a)</td><td>141.90 (n/a)</td><td>34.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 <b>(+37.21%)</b></td><td>0.01 (+11.33%)</td><td>0.01 (-0.92%)</td><td>0.01 (+11.31%)</td><td>0.00 <b>(+164.44%)</b></td><td>202.50 (-10.16%)</td><td>182.20 (-8.05%)</td><td>197.40 (+0.92%)</td><td>128.10 <b>(-27.13%)</b></td><td>31.46 <b>(+70.58%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>225.40 (n/a)</td><td>198.16 (n/a)</td><td>195.60 (n/a)</td><td>175.80 (n/a)</td><td>18.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 <b>(-26.50%)</b></td><td>0.02 (-2.40%)</td><td>0.02 (+18.20%)</td><td>0.01 (-1.51%)</td><td>0.00 <b>(-54.70%)</b></td><td>212.10 (+1.53%)</td><td>171.26 (-2.70%)</td><td>165.70 (-15.37%)</td><td>137.20 <b>(+36.11%)</b></td><td>28.73 <b>(-35.67%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>176.02 (n/a)</td><td>195.80 (n/a)</td><td>100.80 (n/a)</td><td>44.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 <b>(+37.81%)</b></td><td>0.02 <b>(+31.67%)</b></td><td>0.02 <b>(+27.83%)</b></td><td>0.01 <b>(+26.05%)</b></td><td>0.00 <b>(+87.64%)</b></td><td>176.10 <b>(-20.64%)</b></td><td>152.82 <b>(-23.70%)</b></td><td>154.40 <b>(-21.74%)</b></td><td>132.00 <b>(-27.43%)</b></td><td>16.05 (+7.75%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>221.90 (n/a)</td><td>200.28 (n/a)</td><td>197.30 (n/a)</td><td>181.90 (n/a)</td><td>14.89 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 (-10.12%)</td><td>0.01 (-3.99%)</td><td>0.01 (+8.49%)</td><td>0.01 (-2.27%)</td><td>0.00 <b>(-38.62%)</b></td><td>225.00 (+2.32%)</td><td>188.78 (+2.24%)</td><td>188.20 (-7.84%)</td><td>155.40 (+11.24%)</td><td>24.87 <b>(-29.98%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>219.90 (n/a)</td><td>184.64 (n/a)</td><td>204.20 (n/a)</td><td>139.70 (n/a)</td><td>35.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.01 (-18.20%)</td><td>0.01 (-12.68%)</td><td>0.01 (+7.61%)</td><td>0.01 <b>(-34.53%)</b></td><td>0.00 <b>(+25.08%)</b></td><td>385.30 <b>(+52.72%)</b></td><td>262.50 (+18.65%)</td><td>221.50 (-7.05%)</td><td>210.00 <b>(+22.24%)</b></td><td>75.29 <b>(+130.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>252.30 (n/a)</td><td>221.24 (n/a)</td><td>238.30 (n/a)</td><td>171.80 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (+16.56%)</td><td>0.03 <b>(+20.15%)</b></td><td>0.03 (+15.84%)</td><td>0.03 (+17.27%)</td><td>0.01 <b>(+42.74%)</b></td><td>187.90 (-14.75%)</td><td>157.64 (-15.82%)</td><td>165.70 (-13.70%)</td><td>121.60 (-14.25%)</td><td>30.80 (+8.37%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.40 (n/a)</td><td>187.26 (n/a)</td><td>192.00 (n/a)</td><td>141.80 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (+16.48%)</td><td>0.03 (+10.45%)</td><td>0.03 (+15.90%)</td><td>0.02 (-13.55%)</td><td>0.01 <b>(+137.60%)</b></td><td>229.00 (+15.72%)</td><td>169.50 (-7.31%)</td><td>161.40 (-13.69%)</td><td>138.50 (-14.14%)</td><td>34.66 <b>(+149.03%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>197.90 (n/a)</td><td>182.86 (n/a)</td><td>187.00 (n/a)</td><td>161.30 (n/a)</td><td>13.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-6.13%)</td><td>0.03 (-3.30%)</td><td>0.03 (-1.19%)</td><td>0.02 (+7.66%)</td><td>0.00 <b>(-26.76%)</b></td><td>210.00 (-7.12%)</td><td>180.12 (+2.38%)</td><td>173.60 (+1.22%)</td><td>154.60 (+6.55%)</td><td>21.47 <b>(-29.13%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.10 (n/a)</td><td>175.94 (n/a)</td><td>171.50 (n/a)</td><td>145.10 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (+13.26%)</td><td>0.03 <b>(+27.87%)</b></td><td>0.03 <b>(+31.19%)</b></td><td>0.03 <b>(+37.63%)</b></td><td>0.00 <b>(-20.27%)</b></td><td>193.70 <b>(-27.34%)</b></td><td>155.42 <b>(-23.40%)</b></td><td>152.40 <b>(-23.80%)</b></td><td>135.70 (-11.71%)</td><td>22.69 <b>(-47.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>266.60 (n/a)</td><td>202.90 (n/a)</td><td>200.00 (n/a)</td><td>153.70 (n/a)</td><td>43.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (-5.63%)</td><td>0.03 (+4.67%)</td><td>0.03 (+1.84%)</td><td>0.02 (+12.55%)</td><td>0.01 <b>(-22.73%)</b></td><td>211.90 (-11.15%)</td><td>165.28 (-6.62%)</td><td>164.90 (-1.79%)</td><td>125.40 (+6.00%)</td><td>32.82 <b>(-26.87%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.50 (n/a)</td><td>177.00 (n/a)</td><td>167.90 (n/a)</td><td>118.30 (n/a)</td><td>44.88 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (+11.61%)</td><td>0.03 (+13.08%)</td><td>0.03 <b>(+26.57%)</b></td><td>0.02 (-2.66%)</td><td>0.01 <b>(+44.69%)</b></td><td>243.20 (+2.70%)</td><td>177.36 (-10.14%)</td><td>158.50 <b>(-20.99%)</b></td><td>147.50 (-10.39%)</td><td>39.14 <b>(+36.47%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.80 (n/a)</td><td>197.38 (n/a)</td><td>200.60 (n/a)</td><td>164.60 (n/a)</td><td>28.68 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+5.10%)</td><td>0.03 (-1.61%)</td><td>0.03 (-7.99%)</td><td>0.03 (-0.06%)</td><td>0.00 (+18.31%)</td><td>206.00 (+0.10%)</td><td>188.12 (+1.90%)</td><td>193.10 (+8.67%)</td><td>150.90 (-4.85%)</td><td>21.53 (+7.79%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.80 (n/a)</td><td>184.62 (n/a)</td><td>177.70 (n/a)</td><td>158.60 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 <b>(-32.79%)</b></td><td>0.02 (-8.88%)</td><td>0.02 (+2.40%)</td><td>0.02 (+16.87%)</td><td>0.00 <b>(-71.85%)</b></td><td>240.30 (-14.42%)</td><td>212.76 (+2.96%)</td><td>213.30 (-2.38%)</td><td>186.60 <b>(+48.80%)</b></td><td>21.24 <b>(-62.80%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>280.80 (n/a)</td><td>206.64 (n/a)</td><td>218.50 (n/a)</td><td>125.40 (n/a)</td><td>57.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (+2.21%)</td><td>0.06 (+1.56%)</td><td>0.06 (+8.74%)</td><td>0.05 (+9.62%)</td><td>0.01 <b>(-23.14%)</b></td><td>198.50 (-8.78%)</td><td>171.28 (-3.22%)</td><td>180.30 (-8.01%)</td><td>132.60 (-2.14%)</td><td>26.13 <b>(-29.75%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>176.98 (n/a)</td><td>196.00 (n/a)</td><td>135.50 (n/a)</td><td>37.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-0.79%)</td><td>0.05 (-0.23%)</td><td>0.05 (-4.91%)</td><td>0.04 (-3.36%)</td><td>0.01 (-0.96%)</td><td>248.30 (+3.50%)</td><td>196.14 (+0.29%)</td><td>191.50 (+5.16%)</td><td>169.50 (+0.77%)</td><td>30.98 (+4.99%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.90 (n/a)</td><td>195.58 (n/a)</td><td>182.10 (n/a)</td><td>168.20 (n/a)</td><td>29.51 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (-10.98%)</td><td>0.06 (+2.49%)</td><td>0.06 (+6.70%)</td><td>0.05 (+11.77%)</td><td>0.01 <b>(-42.86%)</b></td><td>210.90 (-10.52%)</td><td>174.64 (-5.12%)</td><td>171.00 (-6.25%)</td><td>147.60 (+12.33%)</td><td>23.84 <b>(-42.05%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>235.70 (n/a)</td><td>184.06 (n/a)</td><td>182.40 (n/a)</td><td>131.40 (n/a)</td><td>41.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (+12.11%)</td><td>0.07 (+11.78%)</td><td>0.06 (+14.49%)</td><td>0.06 <b>(+23.11%)</b></td><td>0.01 (-0.77%)</td><td>189.30 (-18.76%)</td><td>160.20 (-11.57%)</td><td>168.30 (-12.66%)</td><td>115.80 (-10.79%)</td><td>28.78 <b>(-28.29%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>181.16 (n/a)</td><td>192.70 (n/a)</td><td>129.80 (n/a)</td><td>40.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (-4.75%)</td><td>0.06 (+3.24%)</td><td>0.06 (+9.17%)</td><td>0.05 (+1.27%)</td><td>0.01 (-11.43%)</td><td>218.90 (-1.22%)</td><td>181.58 (-3.50%)</td><td>173.00 (-8.42%)</td><td>156.50 (+5.03%)</td><td>26.66 (-8.84%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>188.16 (n/a)</td><td>188.90 (n/a)</td><td>149.00 (n/a)</td><td>29.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (-0.59%)</td><td>0.05 (+8.27%)</td><td>0.05 (+1.13%)</td><td>0.05 <b>(+44.79%)</b></td><td>0.01 <b>(-33.25%)</b></td><td>226.50 <b>(-30.95%)</b></td><td>196.92 (-11.25%)</td><td>195.10 (-1.12%)</td><td>159.90 (+0.57%)</td><td>29.73 <b>(-54.05%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>328.00 (n/a)</td><td>221.88 (n/a)</td><td>197.30 (n/a)</td><td>159.00 (n/a)</td><td>64.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 <b>(+29.56%)</b></td><td>0.05 (+4.36%)</td><td>0.05 (+2.12%)</td><td>0.04 <b>(-23.52%)</b></td><td>0.01 <b>(+270.86%)</b></td><td>284.20 <b>(+30.73%)</b></td><td>203.44 (+0.14%)</td><td>196.50 (-2.09%)</td><td>145.80 <b>(-22.78%)</b></td><td>51.33 <b>(+276.49%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>217.40 (n/a)</td><td>203.16 (n/a)</td><td>200.70 (n/a)</td><td>188.80 (n/a)</td><td>13.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (+2.88%)</td><td>0.05 (+10.30%)</td><td>0.05 (+7.15%)</td><td>0.05 <b>(+43.97%)</b></td><td>0.01 <b>(-37.00%)</b></td><td>226.80 <b>(-30.54%)</b></td><td>200.80 (-12.23%)</td><td>194.60 (-6.67%)</td><td>171.50 (-2.78%)</td><td>24.90 <b>(-57.66%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>326.50 (n/a)</td><td>228.78 (n/a)</td><td>208.50 (n/a)</td><td>176.40 (n/a)</td><td>58.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (-9.46%)</td><td>0.12 (-2.76%)</td><td>0.13 (+3.90%)</td><td>0.09 (-4.41%)</td><td>0.02 <b>(-20.59%)</b></td><td>229.90 (+4.60%)</td><td>177.64 (+2.10%)</td><td>166.50 (-3.76%)</td><td>152.30 (+10.44%)</td><td>31.24 (-6.01%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>219.80 (n/a)</td><td>173.98 (n/a)</td><td>173.00 (n/a)</td><td>137.90 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 (+1.80%)</td><td>0.14 (+16.39%)</td><td>0.14 (+15.18%)</td><td>0.12 <b>(+28.22%)</b></td><td>0.01 <b>(-49.80%)</b></td><td>168.90 <b>(-21.99%)</b></td><td>148.74 (-16.16%)</td><td>147.70 (-13.17%)</td><td>136.70 (-1.80%)</td><td>12.97 <b>(-62.34%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>177.40 (n/a)</td><td>170.10 (n/a)</td><td>139.20 (n/a)</td><td>34.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (+16.16%)</td><td>0.12 (-9.35%)</td><td>0.12 (-16.67%)</td><td>0.07 <b>(-31.98%)</b></td><td>0.04 <b>(+101.49%)</b></td><td>297.80 <b>(+46.99%)</b></td><td>186.46 (+17.85%)</td><td>175.50 (+19.96%)</td><td>123.30 (-13.96%)</td><td>66.10 <b>(+163.72%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>202.60 (n/a)</td><td>158.22 (n/a)</td><td>146.30 (n/a)</td><td>143.30 (n/a)</td><td>25.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (+12.55%)</td><td>0.14 <b>(+31.02%)</b></td><td>0.13 <b>(+29.85%)</b></td><td>0.12 <b>(+47.82%)</b></td><td>0.02 <b>(-34.73%)</b></td><td>171.20 <b>(-32.33%)</b></td><td>149.74 <b>(-26.13%)</b></td><td>155.70 <b>(-23.00%)</b></td><td>129.80 (-11.16%)</td><td>17.49 <b>(-62.06%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>253.00 (n/a)</td><td>202.72 (n/a)</td><td>202.20 (n/a)</td><td>146.10 (n/a)</td><td>46.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.18 <b>(+33.78%)</b></td><td>0.15 <b>(+42.29%)</b></td><td>0.15 <b>(+54.02%)</b></td><td>0.12 <b>(+36.19%)</b></td><td>0.02 <b>(+34.08%)</b></td><td>174.10 <b>(-26.57%)</b></td><td>144.96 <b>(-29.75%)</b></td><td>144.20 <b>(-35.05%)</b></td><td>118.30 <b>(-25.27%)</b></td><td>24.18 <b>(-26.64%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>237.10 (n/a)</td><td>206.34 (n/a)</td><td>222.00 (n/a)</td><td>158.30 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (+13.16%)</td><td>0.13 <b>(+24.66%)</b></td><td>0.13 <b>(+22.97%)</b></td><td>0.11 <b>(+60.13%)</b></td><td>0.02 <b>(-25.57%)</b></td><td>191.80 <b>(-37.54%)</b></td><td>164.44 <b>(-23.69%)</b></td><td>166.10 (-18.70%)</td><td>129.20 (-11.69%)</td><td>27.98 <b>(-57.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>307.10 (n/a)</td><td>215.50 (n/a)</td><td>204.30 (n/a)</td><td>146.30 (n/a)</td><td>66.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (+19.42%)</td><td>0.13 (+11.50%)</td><td>0.12 (+15.57%)</td><td>0.11 (+9.02%)</td><td>0.02 <b>(+29.34%)</b></td><td>198.40 (-8.28%)</td><td>171.12 (-9.87%)</td><td>174.00 (-13.48%)</td><td>131.80 (-16.26%)</td><td>27.24 (+0.36%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>216.30 (n/a)</td><td>189.86 (n/a)</td><td>201.10 (n/a)</td><td>157.40 (n/a)</td><td>27.14 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 (+11.12%)</td><td>0.09 (-0.15%)</td><td>0.10 (+3.35%)</td><td>0.05 <b>(-47.41%)</b></td><td>0.03 <b>(+281.83%)</b></td><td>455.40 <b>(+90.15%)</b></td><td>250.76 (+12.45%)</td><td>220.40 (-3.25%)</td><td>175.10 (-10.02%)</td><td>116.63 <b>(+589.87%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>223.00 (n/a)</td><td>227.80 (n/a)</td><td>194.60 (n/a)</td><td>16.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>172.48 (n/a)</td><td>180.00 (n/a)</td><td>133.30 (n/a)</td><td>32.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.80 (n/a)</td><td>185.76 (n/a)</td><td>168.30 (n/a)</td><td>140.10 (n/a)</td><td>45.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>181.60 (n/a)</td><td>165.48 (n/a)</td><td>172.70 (n/a)</td><td>124.20 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>196.20 (n/a)</td><td>183.46 (n/a)</td><td>179.50 (n/a)</td><td>175.50 (n/a)</td><td>8.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>273.20 (n/a)</td><td>196.98 (n/a)</td><td>183.10 (n/a)</td><td>160.90 (n/a)</td><td>44.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>191.04 (n/a)</td><td>193.70 (n/a)</td><td>148.20 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>169.42 (n/a)</td><td>164.20 (n/a)</td><td>154.90 (n/a)</td><td>15.77 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>292.00 (n/a)</td><td>217.36 (n/a)</td><td>196.20 (n/a)</td><td>178.20 (n/a)</td><td>44.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>174.90 (n/a)</td><td>153.78 (n/a)</td><td>152.30 (n/a)</td><td>136.60 (n/a)</td><td>13.74 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.70 (n/a)</td><td>175.52 (n/a)</td><td>182.40 (n/a)</td><td>149.50 (n/a)</td><td>18.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>186.80 (n/a)</td><td>170.76 (n/a)</td><td>175.60 (n/a)</td><td>152.10 (n/a)</td><td>16.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>188.12 (n/a)</td><td>195.00 (n/a)</td><td>163.80 (n/a)</td><td>17.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.37 <b>(+23.91%)</b></td><td>0.31 (+13.72%)</td><td>0.29 (+7.60%)</td><td>0.24 (+7.72%)</td><td>0.06 <b>(+83.62%)</b></td><td>207.80 (-7.15%)</td><td>165.86 (-10.29%)</td><td>168.00 (-7.03%)</td><td>131.60 (-19.31%)</td><td>33.80 <b>(+34.60%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>223.80 (n/a)</td><td>184.88 (n/a)</td><td>180.70 (n/a)</td><td>163.10 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>188.30 (n/a)</td><td>159.16 (n/a)</td><td>158.60 (n/a)</td><td>125.90 (n/a)</td><td>23.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>219.60 (n/a)</td><td>178.22 (n/a)</td><td>187.40 (n/a)</td><td>137.30 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>229.60 (n/a)</td><td>182.20 (n/a)</td><td>173.20 (n/a)</td><td>149.50 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>169.02 (n/a)</td><td>162.60 (n/a)</td><td>136.60 (n/a)</td><td>30.40 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.40 (n/a)</td><td>168.94 (n/a)</td><td>162.60 (n/a)</td><td>154.40 (n/a)</td><td>15.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.60 (n/a)</td><td>176.22 (n/a)</td><td>172.40 (n/a)</td><td>166.30 (n/a)</td><td>10.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>292.20 (n/a)</td><td>202.10 (n/a)</td><td>188.60 (n/a)</td><td>153.90 (n/a)</td><td>52.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>216.30 (n/a)</td><td>160.56 (n/a)</td><td>162.20 (n/a)</td><td>125.20 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>177.30 (n/a)</td><td>151.82 (n/a)</td><td>147.30 (n/a)</td><td>139.10 (n/a)</td><td>15.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>311.30 (n/a)</td><td>200.62 (n/a)</td><td>187.80 (n/a)</td><td>131.70 (n/a)</td><td>67.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>251.50 (n/a)</td><td>176.48 (n/a)</td><td>161.60 (n/a)</td><td>137.80 (n/a)</td><td>46.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>226.00 (n/a)</td><td>184.72 (n/a)</td><td>195.90 (n/a)</td><td>136.80 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>175.30 (n/a)</td><td>147.34 (n/a)</td><td>149.80 (n/a)</td><td>126.60 (n/a)</td><td>18.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.90 (n/a)</td><td>168.20 (n/a)</td><td>166.60 (n/a)</td><td>149.60 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>194.84 (n/a)</td><td>192.40 (n/a)</td><td>169.00 (n/a)</td><td>20.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>207.40 (n/a)</td><td>179.62 (n/a)</td><td>166.90 (n/a)</td><td>160.00 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>198.50 (n/a)</td><td>177.56 (n/a)</td><td>177.10 (n/a)</td><td>151.90 (n/a)</td><td>17.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>253.90 (n/a)</td><td>210.02 (n/a)</td><td>208.00 (n/a)</td><td>185.10 (n/a)</td><td>27.40 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>15.29 (-4.26%)</td><td>14.83 (+1.74%)</td><td>15.09 (+3.96%)</td><td>14.12 (+7.01%)</td><td>0.54 <b>(-45.68%)</b></td><td>3944.30 (-6.55%)</td><td>3760.48 (-1.97%)</td><td>3691.10 (-3.81%)</td><td>3643.50 (+4.45%)</td><td>138.82 <b>(-47.20%)</b></td><td>14735.13 (-4.26%)</td><td>14292.06 (+1.74%)</td><td>14544.99 (+3.96%)</td><td>13611.42 (+7.01%)</td><td>519.91 <b>(-45.68%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>15.97 (n/a)</td><td>14.58 (n/a)</td><td>14.52 (n/a)</td><td>13.20 (n/a)</td><td>0.99 (n/a)</td><td>4220.70 (n/a)</td><td>3836.04 (n/a)</td><td>3837.30 (n/a)</td><td>3488.30 (n/a)</td><td>262.95 (n/a)</td><td>15390.58 (n/a)</td><td>14047.81 (n/a)</td><td>13990.69 (n/a)</td><td>12720.09 (n/a)</td><td>957.15 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>16.45 (+1.03%)</td><td>14.46 (-1.32%)</td><td>14.27 (-0.37%)</td><td>12.89 (-2.82%)</td><td>1.28 (+7.06%)</td><td>1016.70 (+2.90%)</td><td>911.94 (+1.42%)</td><td>918.40 (+0.37%)</td><td>796.70 (-1.02%)</td><td>78.54 (+8.53%)</td><td>10781.54 (+1.03%)</td><td>9477.14 (-1.32%)</td><td>9353.27 (-0.37%)</td><td>8449.04 (-2.82%)</td><td>840.28 (+7.06%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>16.28 (n/a)</td><td>14.65 (n/a)</td><td>14.32 (n/a)</td><td>13.27 (n/a)</td><td>1.20 (n/a)</td><td>988.00 (n/a)</td><td>899.16 (n/a)</td><td>915.00 (n/a)</td><td>804.90 (n/a)</td><td>72.36 (n/a)</td><td>10671.63 (n/a)</td><td>9603.68 (n/a)</td><td>9387.68 (n/a)</td><td>8694.53 (n/a)</td><td>784.83 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>15.31 (-0.29%)</td><td>14.35 (+3.25%)</td><td>13.98 (-1.15%)</td><td>13.89 (+8.14%)</td><td>0.61 <b>(-42.73%)</b></td><td>4010.90 (-7.53%)</td><td>3887.66 (-3.46%)</td><td>3984.40 (+1.16%)</td><td>3637.50 (+0.28%)</td><td>160.21 <b>(-47.62%)</b></td><td>14759.16 (-0.29%)</td><td>13828.97 (+3.25%)</td><td>13474.44 (-1.15%)</td><td>13385.18 (+8.14%)</td><td>588.26 <b>(-42.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>15.36 (n/a)</td><td>13.90 (n/a)</td><td>14.14 (n/a)</td><td>12.84 (n/a)</td><td>1.07 (n/a)</td><td>4337.50 (n/a)</td><td>4027.08 (n/a)</td><td>3938.70 (n/a)</td><td>3627.20 (n/a)</td><td>305.88 (n/a)</td><td>14801.36 (n/a)</td><td>13393.81 (n/a)</td><td>13630.68 (n/a)</td><td>12377.36 (n/a)</td><td>1027.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>16.41 (-3.20%)</td><td>14.30 (-8.33%)</td><td>14.82 (-2.53%)</td><td>10.66 <b>(-25.72%)</b></td><td>2.19 <b>(+91.27%)</b></td><td>1675.10 <b>(+34.63%)</b></td><td>1277.34 (+11.07%)</td><td>1205.00 (+2.60%)</td><td>1088.30 (+3.30%)</td><td>230.87 <b>(+177.15%)</b></td><td>12332.54 (-3.20%)</td><td>10744.11 (-8.33%)</td><td>11138.64 (-2.53%)</td><td>8012.72 <b>(-25.72%)</b></td><td>1644.56 <b>(+91.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>16.95 (n/a)</td><td>15.59 (n/a)</td><td>15.21 (n/a)</td><td>14.35 (n/a)</td><td>1.14 (n/a)</td><td>1244.20 (n/a)</td><td>1150.02 (n/a)</td><td>1174.50 (n/a)</td><td>1053.50 (n/a)</td><td>83.30 (n/a)</td><td>12739.75 (n/a)</td><td>11720.46 (n/a)</td><td>11427.50 (n/a)</td><td>10787.06 (n/a)</td><td>859.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>11.20 (-5.05%)</td><td>10.94 (-1.35%)</td><td>11.12 (-0.03%)</td><td>10.61 (-0.26%)</td><td>0.30 <b>(-34.06%)</b></td><td>7724.00 (+0.26%)</td><td>7492.16 (+1.29%)</td><td>7369.10 (+0.03%)</td><td>7314.30 (+5.32%)</td><td>210.28 <b>(-30.27%)</b></td><td>14680.05 (-5.05%)</td><td>14340.51 (-1.35%)</td><td>14570.95 (-0.03%)</td><td>13901.31 (-0.26%)</td><td>398.69 <b>(-34.06%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>11.80 (n/a)</td><td>11.09 (n/a)</td><td>11.12 (n/a)</td><td>10.63 (n/a)</td><td>0.46 (n/a)</td><td>7703.70 (n/a)</td><td>7396.62 (n/a)</td><td>7366.90 (n/a)</td><td>6944.90 (n/a)</td><td>301.55 (n/a)</td><td>15460.94 (n/a)</td><td>14536.37 (n/a)</td><td>14575.14 (n/a)</td><td>13937.95 (n/a)</td><td>604.64 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>16.14 (+2.52%)</td><td>13.38 (-3.85%)</td><td>13.50 (-8.51%)</td><td>10.98 (-1.40%)</td><td>2.21 (+9.29%)</td><td>1957.50 (+1.42%)</td><td>1642.00 (+4.39%)</td><td>1592.70 (+9.31%)</td><td>1332.10 (-2.46%)</td><td>271.42 (+10.66%)</td><td>12897.27 (+2.52%)</td><td>10694.92 (-3.85%)</td><td>10786.96 (-8.51%)</td><td>8776.36 (-1.40%)</td><td>1762.57 (+9.29%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>15.74 (n/a)</td><td>13.92 (n/a)</td><td>14.75 (n/a)</td><td>11.14 (n/a)</td><td>2.02 (n/a)</td><td>1930.10 (n/a)</td><td>1572.94 (n/a)</td><td>1457.10 (n/a)</td><td>1365.70 (n/a)</td><td>245.27 (n/a)</td><td>12579.82 (n/a)</td><td>11122.86 (n/a)</td><td>11790.67 (n/a)</td><td>8901.24 (n/a)</td><td>1612.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>10.91 (+4.85%)</td><td>10.59 (+2.76%)</td><td>10.49 (+1.12%)</td><td>10.44 (+4.41%)</td><td>0.20 (+16.98%)</td><td>7844.40 (-4.22%)</td><td>7739.40 (-2.68%)</td><td>7810.10 (-1.11%)</td><td>7512.00 (-4.62%)</td><td>142.72 (+6.82%)</td><td>14293.71 (+4.85%)</td><td>13877.57 (+2.76%)</td><td>13748.18 (+1.12%)</td><td>13687.99 (+4.41%)</td><td>259.76 (+16.98%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>10.40 (n/a)</td><td>10.30 (n/a)</td><td>10.37 (n/a)</td><td>10.00 (n/a)</td><td>0.17 (n/a)</td><td>8190.30 (n/a)</td><td>7952.88 (n/a)</td><td>7897.60 (n/a)</td><td>7876.00 (n/a)</td><td>133.61 (n/a)</td><td>13633.05 (n/a)</td><td>13504.28 (n/a)</td><td>13595.82 (n/a)</td><td>13109.88 (n/a)</td><td>222.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>3.74 (-19.59%)</td><td>3.08 (-8.69%)</td><td>2.99 (-3.86%)</td><td>2.68 (-7.23%)</td><td>0.40 <b>(-46.22%)</b></td><td>513.80 (+7.81%)</td><td>452.18 (+7.45%)</td><td>460.20 (+4.00%)</td><td>367.90 <b>(+24.37%)</b></td><td>52.91 <b>(-28.65%)</b></td><td>729.62 (-19.59%)</td><td>600.80 (-8.69%)</td><td>583.27 (-3.86%)</td><td>522.45 (-7.23%)</td><td>77.12 <b>(-46.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.65 (n/a)</td><td>3.37 (n/a)</td><td>3.11 (n/a)</td><td>2.89 (n/a)</td><td>0.74 (n/a)</td><td>476.60 (n/a)</td><td>420.82 (n/a)</td><td>442.50 (n/a)</td><td>295.80 (n/a)</td><td>74.16 (n/a)</td><td>907.42 (n/a)</td><td>658.00 (n/a)</td><td>606.70 (n/a)</td><td>563.17 (n/a)</td><td>143.40 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>5.00 <b>(-20.60%)</b></td><td>3.90 (-6.90%)</td><td>3.54 (-5.15%)</td><td>3.48 (-0.73%)</td><td>0.64 <b>(-45.84%)</b></td><td>395.90 (+0.74%)</td><td>359.90 (+4.25%)</td><td>388.90 (+5.42%)</td><td>275.30 <b>(+25.94%)</b></td><td>50.83 <b>(-29.77%)</b></td><td>974.91 <b>(-20.60%)</b></td><td>759.98 (-6.90%)</td><td>690.21 (-5.15%)</td><td>678.05 (-0.73%)</td><td>125.57 <b>(-45.84%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>6.29 (n/a)</td><td>4.19 (n/a)</td><td>3.73 (n/a)</td><td>3.50 (n/a)</td><td>1.19 (n/a)</td><td>393.00 (n/a)</td><td>345.22 (n/a)</td><td>368.90 (n/a)</td><td>218.60 (n/a)</td><td>72.38 (n/a)</td><td>1227.77 (n/a)</td><td>816.28 (n/a)</td><td>727.72 (n/a)</td><td>683.01 (n/a)</td><td>231.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>7.73 <b>(+22.17%)</b></td><td>4.69 (+12.04%)</td><td>3.75 (+5.01%)</td><td>3.50 (+3.31%)</td><td>1.77 <b>(+43.03%)</b></td><td>393.00 (-3.23%)</td><td>319.52 (-7.91%)</td><td>367.00 (-4.77%)</td><td>178.00 (-18.16%)</td><td>88.23 (+12.93%)</td><td>1507.99 <b>(+22.17%)</b></td><td>914.98 (+12.04%)</td><td>731.38 (+5.01%)</td><td>682.96 (+3.31%)</td><td>344.71 <b>(+43.03%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>6.33 (n/a)</td><td>4.19 (n/a)</td><td>3.57 (n/a)</td><td>3.39 (n/a)</td><td>1.24 (n/a)</td><td>406.10 (n/a)</td><td>346.98 (n/a)</td><td>385.40 (n/a)</td><td>217.50 (n/a)</td><td>78.13 (n/a)</td><td>1234.33 (n/a)</td><td>816.64 (n/a)</td><td>696.51 (n/a)</td><td>661.07 (n/a)</td><td>241.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>6.30 <b>(-20.76%)</b></td><td>4.17 (-6.51%)</td><td>3.62 (-2.31%)</td><td>3.47 (+4.86%)</td><td>1.20 <b>(-38.74%)</b></td><td>396.60 (-4.62%)</td><td>347.42 (+1.28%)</td><td>380.70 (+2.37%)</td><td>218.30 <b>(+26.18%)</b></td><td>73.65 <b>(-24.31%)</b></td><td>1229.74 <b>(-20.76%)</b></td><td>812.42 (-6.51%)</td><td>705.14 (-2.31%)</td><td>676.90 (+4.86%)</td><td>234.97 <b>(-38.74%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.96 (n/a)</td><td>4.46 (n/a)</td><td>3.70 (n/a)</td><td>3.31 (n/a)</td><td>1.97 (n/a)</td><td>415.80 (n/a)</td><td>343.02 (n/a)</td><td>371.90 (n/a)</td><td>173.00 (n/a)</td><td>97.31 (n/a)</td><td>1551.84 (n/a)</td><td>868.98 (n/a)</td><td>721.82 (n/a)</td><td>645.54 (n/a)</td><td>383.54 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>4.87 (-5.08%)</td><td>3.96 (+2.61%)</td><td>4.30 <b>(+25.64%)</b></td><td>3.05 (-0.52%)</td><td>0.82 (-5.09%)</td><td>451.70 (+0.53%)</td><td>360.94 (-2.56%)</td><td>320.30 <b>(-20.42%)</b></td><td>282.80 (+5.33%)</td><td>79.07 (+4.57%)</td><td>949.08 (-5.08%)</td><td>771.68 (+2.61%)</td><td>837.97 <b>(+25.64%)</b></td><td>594.33 (-0.52%)</td><td>160.41 (-5.09%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>5.13 (n/a)</td><td>3.86 (n/a)</td><td>3.42 (n/a)</td><td>3.06 (n/a)</td><td>0.87 (n/a)</td><td>449.30 (n/a)</td><td>370.44 (n/a)</td><td>402.50 (n/a)</td><td>268.50 (n/a)</td><td>75.62 (n/a)</td><td>999.83 (n/a)</td><td>752.06 (n/a)</td><td>666.94 (n/a)</td><td>597.45 (n/a)</td><td>169.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>4.52 (-18.21%)</td><td>3.69 (-8.79%)</td><td>3.32 (-6.67%)</td><td>3.00 (+4.09%)</td><td>0.74 <b>(-39.33%)</b></td><td>458.90 (-3.92%)</td><td>385.04 (+5.43%)</td><td>414.40 (+7.14%)</td><td>304.70 <b>(+22.27%)</b></td><td>73.11 <b>(-29.27%)</b></td><td>881.10 (-18.21%)</td><td>719.04 (-8.79%)</td><td>647.74 (-6.67%)</td><td>585.01 (+4.09%)</td><td>144.11 <b>(-39.33%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>5.52 (n/a)</td><td>4.04 (n/a)</td><td>3.56 (n/a)</td><td>2.88 (n/a)</td><td>1.22 (n/a)</td><td>477.60 (n/a)</td><td>365.20 (n/a)</td><td>386.80 (n/a)</td><td>249.20 (n/a)</td><td>103.37 (n/a)</td><td>1077.21 (n/a)</td><td>788.37 (n/a)</td><td>694.02 (n/a)</td><td>562.03 (n/a)</td><td>237.54 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>4.94 (-0.81%)</td><td>3.74 (+10.78%)</td><td>3.11 (+4.07%)</td><td>3.01 (+6.32%)</td><td>0.96 (+6.53%)</td><td>457.70 (-5.94%)</td><td>386.32 (-9.23%)</td><td>442.80 (-3.91%)</td><td>278.70 (+0.83%)</td><td>90.39 (+5.97%)</td><td>963.17 (-0.81%)</td><td>729.93 (+10.78%)</td><td>606.25 (+4.07%)</td><td>586.52 (+6.32%)</td><td>187.46 (+6.53%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.98 (n/a)</td><td>3.38 (n/a)</td><td>2.99 (n/a)</td><td>2.83 (n/a)</td><td>0.90 (n/a)</td><td>486.60 (n/a)</td><td>425.58 (n/a)</td><td>460.80 (n/a)</td><td>276.40 (n/a)</td><td>85.30 (n/a)</td><td>971.02 (n/a)</td><td>658.87 (n/a)</td><td>582.55 (n/a)</td><td>551.67 (n/a)</td><td>175.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>2.03 (-11.91%)</td><td>1.43 (+10.47%)</td><td>1.35 <b>(+31.89%)</b></td><td>1.07 (+18.91%)</td><td>0.40 <b>(-31.23%)</b></td><td>374.80 (-15.91%)</td><td>297.82 (-14.43%)</td><td>296.60 <b>(-24.18%)</b></td><td>198.00 (+13.53%)</td><td>75.58 <b>(-29.12%)</b></td><td>169.46 (-11.91%)</td><td>119.29 (+10.47%)</td><td>113.11 <b>(+31.89%)</b></td><td>89.53 (+18.91%)</td><td>33.23 <b>(-31.23%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.30 (n/a)</td><td>1.29 (n/a)</td><td>1.03 (n/a)</td><td>0.90 (n/a)</td><td>0.58 (n/a)</td><td>445.70 (n/a)</td><td>348.06 (n/a)</td><td>391.20 (n/a)</td><td>174.40 (n/a)</td><td>106.64 (n/a)</td><td>192.36 (n/a)</td><td>107.98 (n/a)</td><td>85.77 (n/a)</td><td>75.29 (n/a)</td><td>48.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>7.98 (+0.78%)</td><td>5.37 (-2.43%)</td><td>4.70 (-3.08%)</td><td>4.61 (-0.16%)</td><td>1.46 (+6.13%)</td><td>418.90 (+0.14%)</td><td>376.26 (+3.01%)</td><td>411.20 (+3.16%)</td><td>242.40 (-0.78%)</td><td>75.33 (+6.15%)</td><td>1660.97 (+0.78%)</td><td>1118.73 (-2.43%)</td><td>979.16 (-3.08%)</td><td>961.11 (-0.16%)</td><td>303.85 (+6.13%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.91 (n/a)</td><td>5.51 (n/a)</td><td>4.85 (n/a)</td><td>4.62 (n/a)</td><td>1.37 (n/a)</td><td>418.30 (n/a)</td><td>365.28 (n/a)</td><td>398.60 (n/a)</td><td>244.30 (n/a)</td><td>70.96 (n/a)</td><td>1648.09 (n/a)</td><td>1146.56 (n/a)</td><td>1010.27 (n/a)</td><td>962.63 (n/a)</td><td>286.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>15.51 (-4.63%)</td><td>12.51 (+1.55%)</td><td>11.09 (-1.01%)</td><td>10.84 (+1.84%)</td><td>2.13 (-7.97%)</td><td>508.00 (-1.80%)</td><td>449.80 (-1.76%)</td><td>496.30 (+1.02%)</td><td>355.00 (+4.84%)</td><td>70.64 (-2.35%)</td><td>6048.98 (-4.63%)</td><td>4878.21 (+1.55%)</td><td>4326.86 (-1.01%)</td><td>4227.35 (+1.84%)</td><td>829.05 (-7.97%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>16.26 (n/a)</td><td>12.31 (n/a)</td><td>11.20 (n/a)</td><td>10.64 (n/a)</td><td>2.31 (n/a)</td><td>517.30 (n/a)</td><td>457.84 (n/a)</td><td>491.30 (n/a)</td><td>338.60 (n/a)</td><td>72.35 (n/a)</td><td>6342.34 (n/a)</td><td>4803.61 (n/a)</td><td>4370.89 (n/a)</td><td>4150.97 (n/a)</td><td>900.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>10.57 (-0.38%)</td><td>8.52 (+9.63%)</td><td>8.31 (+4.59%)</td><td>5.30 <b>(+24.66%)</b></td><td>2.19 (-3.46%)</td><td>1039.60 (-19.78%)</td><td>688.64 (-11.22%)</td><td>662.30 (-4.39%)</td><td>520.90 (+0.39%)</td><td>212.26 <b>(-29.25%)</b></td><td>4122.87 (-0.38%)</td><td>3324.73 (+9.63%)</td><td>3242.36 (+4.59%)</td><td>2065.64 <b>(+24.66%)</b></td><td>855.80 (-3.46%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>10.61 (n/a)</td><td>7.77 (n/a)</td><td>7.95 (n/a)</td><td>4.25 (n/a)</td><td>2.27 (n/a)</td><td>1296.00 (n/a)</td><td>775.64 (n/a)</td><td>692.70 (n/a)</td><td>518.90 (n/a)</td><td>300.01 (n/a)</td><td>4138.63 (n/a)</td><td>3032.77 (n/a)</td><td>3100.17 (n/a)</td><td>1657.05 (n/a)</td><td>886.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>12.20 (+5.73%)</td><td>9.85 (+6.79%)</td><td>9.05 (+5.84%)</td><td>8.12 <b>(+28.98%)</b></td><td>1.67 <b>(-25.67%)</b></td><td>714.50 <b>(-22.47%)</b></td><td>601.80 (-9.06%)</td><td>640.60 (-5.52%)</td><td>475.30 (-5.43%)</td><td>97.02 <b>(-43.72%)</b></td><td>5082.45 (+5.73%)</td><td>4103.83 (+6.79%)</td><td>3771.58 (+5.84%)</td><td>3381.22 <b>(+28.98%)</b></td><td>697.39 <b>(-25.67%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>11.54 (n/a)</td><td>9.23 (n/a)</td><td>8.55 (n/a)</td><td>6.29 (n/a)</td><td>2.25 (n/a)</td><td>921.60 (n/a)</td><td>661.78 (n/a)</td><td>678.00 (n/a)</td><td>502.60 (n/a)</td><td>172.37 (n/a)</td><td>4806.78 (n/a)</td><td>3842.72 (n/a)</td><td>3563.36 (n/a)</td><td>2621.46 (n/a)</td><td>938.27 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>181.20 (n/a)</td><td>135.44 (n/a)</td><td>124.70 (n/a)</td><td>114.30 (n/a)</td><td>27.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>168.70 (n/a)</td><td>151.32 (n/a)</td><td>161.10 (n/a)</td><td>112.00 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>181.90 (n/a)</td><td>149.84 (n/a)</td><td>159.10 (n/a)</td><td>112.30 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.80 (n/a)</td><td>161.34 (n/a)</td><td>154.10 (n/a)</td><td>153.20 (n/a)</td><td>14.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>153.70 (n/a)</td><td>143.44 (n/a)</td><td>150.10 (n/a)</td><td>110.40 (n/a)</td><td>18.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.60 (n/a)</td><td>172.66 (n/a)</td><td>171.30 (n/a)</td><td>148.70 (n/a)</td><td>21.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.60 (n/a)</td><td>180.66 (n/a)</td><td>173.10 (n/a)</td><td>120.60 (n/a)</td><td>44.68 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.30 (n/a)</td><td>206.80 (n/a)</td><td>216.30 (n/a)</td><td>160.70 (n/a)</td><td>27.41 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.30 (n/a)</td><td>151.54 (n/a)</td><td>154.20 (n/a)</td><td>111.10 (n/a)</td><td>28.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.30 (n/a)</td><td>147.00 (n/a)</td><td>156.80 (n/a)</td><td>110.30 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.80 (n/a)</td><td>149.42 (n/a)</td><td>161.40 (n/a)</td><td>110.90 (n/a)</td><td>22.64 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.70 (n/a)</td><td>192.38 (n/a)</td><td>165.60 (n/a)</td><td>156.30 (n/a)</td><td>42.51 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.80 (n/a)</td><td>151.64 (n/a)</td><td>152.30 (n/a)</td><td>127.60 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>171.30 (n/a)</td><td>171.30 (n/a)</td><td>131.30 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>349.50 (n/a)</td><td>195.50 (n/a)</td><td>173.80 (n/a)</td><td>126.80 (n/a)</td><td>90.64 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.70 (n/a)</td><td>232.04 (n/a)</td><td>218.20 (n/a)</td><td>193.50 (n/a)</td><td>40.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>359.30 (n/a)</td><td>195.30 (n/a)</td><td>170.80 (n/a)</td><td>123.50 (n/a)</td><td>94.04 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.50 (n/a)</td><td>165.18 (n/a)</td><td>171.20 (n/a)</td><td>128.60 (n/a)</td><td>25.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.90 (n/a)</td><td>165.82 (n/a)</td><td>172.70 (n/a)</td><td>144.70 (n/a)</td><td>13.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>185.70 (n/a)</td><td>164.18 (n/a)</td><td>176.20 (n/a)</td><td>105.00 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>178.26 (n/a)</td><td>175.30 (n/a)</td><td>161.20 (n/a)</td><td>20.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>218.30 (n/a)</td><td>169.34 (n/a)</td><td>159.70 (n/a)</td><td>148.90 (n/a)</td><td>27.86 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>241.20 (n/a)</td><td>185.14 (n/a)</td><td>185.00 (n/a)</td><td>136.80 (n/a)</td><td>42.35 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>313.50 (n/a)</td><td>247.54 (n/a)</td><td>256.60 (n/a)</td><td>203.50 (n/a)</td><td>45.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>363.10 (n/a)</td><td>209.84 (n/a)</td><td>183.80 (n/a)</td><td>155.00 (n/a)</td><td>87.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>203.00 (n/a)</td><td>169.12 (n/a)</td><td>184.80 (n/a)</td><td>127.50 (n/a)</td><td>38.27 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>197.20 (n/a)</td><td>170.60 (n/a)</td><td>171.10 (n/a)</td><td>145.00 (n/a)</td><td>18.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>220.70 (n/a)</td><td>159.74 (n/a)</td><td>148.20 (n/a)</td><td>130.10 (n/a)</td><td>35.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.60 (n/a)</td><td>160.58 (n/a)</td><td>159.10 (n/a)</td><td>130.20 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>316.50 (n/a)</td><td>207.70 (n/a)</td><td>185.80 (n/a)</td><td>146.70 (n/a)</td><td>64.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>189.80 (n/a)</td><td>163.38 (n/a)</td><td>169.80 (n/a)</td><td>132.60 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>204.00 (n/a)</td><td>208.20 (n/a)</td><td>178.20 (n/a)</td><td>16.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>4.12 (-0.09%)</td><td>4.11 (-0.18%)</td><td>4.11 (-0.03%)</td><td>4.09 (-0.54%)</td><td>0.01 <b>(+226.44%)</b></td><td>19230.40 (+0.55%)</td><td>19145.46 (+0.18%)</td><td>19124.60 (+0.03%)</td><td>19108.40 (+0.09%)</td><td>49.33 <b>(+228.60%)</b></td><td>2809.61 (-0.09%)</td><td>2804.18 (-0.18%)</td><td>2807.23 (-0.03%)</td><td>2791.79 (-0.54%)</td><td>7.20 <b>(+226.43%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.12 (n/a)</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>0.00 (n/a)</td><td>19125.60 (n/a)</td><td>19111.06 (n/a)</td><td>19119.50 (n/a)</td><td>19091.00 (n/a)</td><td>15.01 (n/a)</td><td>2812.16 (n/a)</td><td>2809.22 (n/a)</td><td>2807.98 (n/a)</td><td>2807.08 (n/a)</td><td>2.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>4.96 (-0.04%)</td><td>4.22 (-1.73%)</td><td>4.22 (+2.72%)</td><td>3.44 (-2.89%)</td><td>0.55 (-5.79%)</td><td>2732.90 (+2.97%)</td><td>2260.10 (+1.66%)</td><td>2229.00 (-2.65%)</td><td>1897.50 (+0.04%)</td><td>308.31 (-0.22%)</td><td>1949.59 (-0.04%)</td><td>1660.41 (-1.73%)</td><td>1659.68 (+2.72%)</td><td>1353.66 (-2.89%)</td><td>217.85 (-5.79%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.96 (n/a)</td><td>4.30 (n/a)</td><td>4.11 (n/a)</td><td>3.54 (n/a)</td><td>0.59 (n/a)</td><td>2654.00 (n/a)</td><td>2223.12 (n/a)</td><td>2289.60 (n/a)</td><td>1896.70 (n/a)</td><td>308.99 (n/a)</td><td>1950.41 (n/a)</td><td>1689.64 (n/a)</td><td>1615.75 (n/a)</td><td>1393.89 (n/a)</td><td>231.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.35 (-1.09%)</td><td>1.02 (-9.77%)</td><td>1.07 (-10.48%)</td><td>0.66 <b>(-28.81%)</b></td><td>0.32 <b>(+70.20%)</b></td><td>333.20 <b>(+40.47%)</b></td><td>236.66 (+18.33%)</td><td>206.40 (+11.75%)</td><td>163.60 (+1.11%)</td><td>80.01 <b>(+134.08%)</b></td><td>57.69 (-1.09%)</td><td>43.57 (-9.77%)</td><td>45.73 (-10.48%)</td><td>28.32 <b>(-28.81%)</b></td><td>13.77 <b>(+70.20%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.37 (n/a)</td><td>1.13 (n/a)</td><td>1.20 (n/a)</td><td>0.93 (n/a)</td><td>0.19 (n/a)</td><td>237.20 (n/a)</td><td>200.00 (n/a)</td><td>184.70 (n/a)</td><td>161.80 (n/a)</td><td>34.18 (n/a)</td><td>58.33 (n/a)</td><td>48.28 (n/a)</td><td>51.08 (n/a)</td><td>39.78 (n/a)</td><td>8.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.02 (-16.07%)</td><td>0.86 (-10.56%)</td><td>0.98 (-0.78%)</td><td>0.63 (-8.02%)</td><td>0.19 (-2.23%)</td><td>352.50 (+8.73%)</td><td>269.86 (+12.72%)</td><td>226.50 (+0.80%)</td><td>217.20 (+19.14%)</td><td>65.90 <b>(+23.25%)</b></td><td>43.45 (-16.07%)</td><td>36.57 (-10.56%)</td><td>41.66 (-0.78%)</td><td>26.77 (-8.02%)</td><td>8.17 (-2.23%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.21 (n/a)</td><td>0.96 (n/a)</td><td>0.98 (n/a)</td><td>0.68 (n/a)</td><td>0.20 (n/a)</td><td>324.20 (n/a)</td><td>239.40 (n/a)</td><td>224.70 (n/a)</td><td>182.30 (n/a)</td><td>53.47 (n/a)</td><td>51.77 (n/a)</td><td>40.89 (n/a)</td><td>41.99 (n/a)</td><td>29.11 (n/a)</td><td>8.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.53 (+0.60%)</td><td>0.53 (+0.24%)</td><td>0.53 (+0.16%)</td><td>0.53 (+0.18%)</td><td>0.00 <b>(+194.02%)</b></td><td>47815.50 (-0.18%)</td><td>47740.30 (-0.24%)</td><td>47792.80 (-0.16%)</td><td>47515.00 (-0.59%)</td><td>127.20 <b>(+191.51%)</b></td><td>361.57 (+0.60%)</td><td>359.86 (+0.24%)</td><td>359.47 (+0.16%)</td><td>359.30 (+0.18%)</td><td>0.96 <b>(+194.03%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47899.50 (n/a)</td><td>47854.86 (n/a)</td><td>47867.60 (n/a)</td><td>47799.00 (n/a)</td><td>43.63 (n/a)</td><td>359.42 (n/a)</td><td>359.00 (n/a)</td><td>358.90 (n/a)</td><td>358.67 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.21 (-0.18%)</td><td>0.21 (-0.34%)</td><td>0.21 (+0.09%)</td><td>0.21 (-1.03%)</td><td>0.00 <b>(+90.01%)</b></td><td>120859.50 (+1.04%)</td><td>119114.54 (+0.35%)</td><td>118490.10 (-0.09%)</td><td>118100.90 (+0.18%)</td><td>1232.85 <b>(+92.10%)</b></td><td>145.47 (-0.18%)</td><td>144.24 (-0.34%)</td><td>144.99 (+0.09%)</td><td>142.15 (-1.03%)</td><td>1.49 <b>(+90.01%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119617.60 (n/a)</td><td>118702.54 (n/a)</td><td>118601.60 (n/a)</td><td>117885.90 (n/a)</td><td>641.77 (n/a)</td><td>145.73 (n/a)</td><td>144.73 (n/a)</td><td>144.85 (n/a)</td><td>143.62 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.90 (-0.82%)</td><td>0.90 (-0.38%)</td><td>0.90 (-0.34%)</td><td>0.89 (-0.34%)</td><td>0.00 <b>(-30.79%)</b></td><td>28160.10 (+0.34%)</td><td>28003.66 (+0.38%)</td><td>27977.00 (+0.34%)</td><td>27870.90 (+0.83%)</td><td>118.93 <b>(-29.97%)</b></td><td>616.41 (-0.82%)</td><td>613.50 (-0.38%)</td><td>614.07 (-0.34%)</td><td>610.08 (-0.34%)</td><td>2.60 <b>(-30.79%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.01 (n/a)</td><td>28064.50 (n/a)</td><td>27897.58 (n/a)</td><td>27883.10 (n/a)</td><td>27641.60 (n/a)</td><td>169.82 (n/a)</td><td>621.52 (n/a)</td><td>615.84 (n/a)</td><td>616.14 (n/a)</td><td>612.16 (n/a)</td><td>3.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>3.61 (-2.74%)</td><td>3.56 (+0.62%)</td><td>3.59 (+3.43%)</td><td>3.42 (+0.18%)</td><td>0.08 <b>(-39.20%)</b></td><td>7348.20 (-0.18%)</td><td>7077.28 (-0.68%)</td><td>7014.30 (-3.31%)</td><td>6970.00 (+2.81%)</td><td>157.65 <b>(-37.55%)</b></td><td>2464.81 (-2.74%)</td><td>2428.41 (+0.62%)</td><td>2449.28 (+3.43%)</td><td>2337.95 (+0.18%)</td><td>52.81 <b>(-39.20%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>3.71 (n/a)</td><td>3.54 (n/a)</td><td>3.47 (n/a)</td><td>3.42 (n/a)</td><td>0.13 (n/a)</td><td>7361.70 (n/a)</td><td>7125.80 (n/a)</td><td>7254.70 (n/a)</td><td>6779.30 (n/a)</td><td>252.44 (n/a)</td><td>2534.15 (n/a)</td><td>2413.40 (n/a)</td><td>2368.10 (n/a)</td><td>2333.69 (n/a)</td><td>86.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>3.23 (-0.70%)</td><td>3.06 (-2.79%)</td><td>3.08 (-3.41%)</td><td>2.85 (-3.92%)</td><td>0.18 <b>(+52.01%)</b></td><td>8828.00 (+4.08%)</td><td>8255.84 (+3.04%)</td><td>8176.50 (+3.53%)</td><td>7796.30 (+0.70%)</td><td>480.58 <b>(+58.54%)</b></td><td>2203.59 (-0.70%)</td><td>2086.54 (-2.79%)</td><td>2101.14 (-3.41%)</td><td>1946.06 (-3.92%)</td><td>120.48 <b>(+52.01%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>3.25 (n/a)</td><td>3.14 (n/a)</td><td>3.19 (n/a)</td><td>2.97 (n/a)</td><td>0.12 (n/a)</td><td>8482.30 (n/a)</td><td>8012.64 (n/a)</td><td>7897.80 (n/a)</td><td>7741.80 (n/a)</td><td>303.12 (n/a)</td><td>2219.11 (n/a)</td><td>2146.50 (n/a)</td><td>2175.28 (n/a)</td><td>2025.39 (n/a)</td><td>79.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>3.31 (-1.09%)</td><td>3.19 (-0.78%)</td><td>3.18 (-0.15%)</td><td>3.12 (-1.40%)</td><td>0.07 (-7.25%)</td><td>8060.10 (+1.42%)</td><td>7881.42 (+0.78%)</td><td>7912.30 (+0.15%)</td><td>7604.30 (+1.10%)</td><td>167.33 (-5.25%)</td><td>2259.23 (-1.09%)</td><td>2180.59 (-0.78%)</td><td>2171.27 (-0.15%)</td><td>2131.47 (-1.40%)</td><td>47.14 (-7.25%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>3.35 (n/a)</td><td>3.22 (n/a)</td><td>3.19 (n/a)</td><td>3.17 (n/a)</td><td>0.07 (n/a)</td><td>7947.10 (n/a)</td><td>7820.18 (n/a)</td><td>7900.20 (n/a)</td><td>7521.60 (n/a)</td><td>176.61 (n/a)</td><td>2284.08 (n/a)</td><td>2197.78 (n/a)</td><td>2174.61 (n/a)</td><td>2161.77 (n/a)</td><td>50.83 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.80 (-0.45%)</td><td>0.80 (-0.16%)</td><td>0.80 (-0.08%)</td><td>0.80 (-0.12%)</td><td>0.00 <b>(-68.10%)</b></td><td>94937.50 (+0.12%)</td><td>94853.30 (+0.16%)</td><td>94837.70 (+0.08%)</td><td>94787.70 (+0.45%)</td><td>61.82 <b>(-67.92%)</b></td><td>724.98 (-0.45%)</td><td>724.48 (-0.16%)</td><td>724.60 (-0.08%)</td><td>723.84 (-0.12%)</td><td>0.47 <b>(-68.10%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94826.00 (n/a)</td><td>94701.80 (n/a)</td><td>94763.70 (n/a)</td><td>94360.60 (n/a)</td><td>192.68 (n/a)</td><td>728.26 (n/a)</td><td>725.64 (n/a)</td><td>725.17 (n/a)</td><td>724.69 (n/a)</td><td>1.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.73 (-0.02%)</td><td>0.73 (+0.05%)</td><td>0.73 (-0.04%)</td><td>0.73 (+0.20%)</td><td>0.00 <b>(-76.01%)</b></td><td>103362.20 (-0.20%)</td><td>103317.66 (-0.05%)</td><td>103328.00 (+0.04%)</td><td>103281.70 (+0.02%)</td><td>34.33 <b>(-76.06%)</b></td><td>665.36 (-0.02%)</td><td>665.13 (+0.05%)</td><td>665.06 (-0.04%)</td><td>664.84 (+0.20%)</td><td>0.22 <b>(-76.01%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103568.50 (n/a)</td><td>103372.72 (n/a)</td><td>103281.90 (n/a)</td><td>103256.70 (n/a)</td><td>143.44 (n/a)</td><td>665.52 (n/a)</td><td>664.77 (n/a)</td><td>665.36 (n/a)</td><td>663.52 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.68 (-0.18%)</td><td>0.68 (-0.01%)</td><td>0.68 (+0.05%)</td><td>0.68 (-0.11%)</td><td>0.00 <b>(-21.28%)</b></td><td>110995.90 (+0.11%)</td><td>110626.60 (+0.01%)</td><td>110626.40 (-0.05%)</td><td>110385.50 (+0.18%)</td><td>231.55 <b>(-21.06%)</b></td><td>622.54 (-0.18%)</td><td>621.19 (-0.01%)</td><td>621.19 (+0.05%)</td><td>619.12 (-0.11%)</td><td>1.30 <b>(-21.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110872.90 (n/a)</td><td>110614.24 (n/a)</td><td>110681.80 (n/a)</td><td>110181.70 (n/a)</td><td>293.31 (n/a)</td><td>623.69 (n/a)</td><td>621.26 (n/a)</td><td>620.87 (n/a)</td><td>619.80 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>2.80 (-0.02%)</td><td>2.80 (-0.02%)</td><td>2.80 (+0.04%)</td><td>2.79 (-0.02%)</td><td>0.00 (-3.83%)</td><td>37538.40 (+0.02%)</td><td>37506.22 (+0.02%)</td><td>37498.80 (-0.04%)</td><td>37478.10 (+0.02%)</td><td>26.88 (-3.69%)</td><td>2864.98 (-0.02%)</td><td>2862.84 (-0.02%)</td><td>2863.40 (+0.04%)</td><td>2860.39 (-0.02%)</td><td>2.05 (-3.82%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>0.00 (n/a)</td><td>37530.60 (n/a)</td><td>37500.48 (n/a)</td><td>37514.60 (n/a)</td><td>37469.90 (n/a)</td><td>27.91 (n/a)</td><td>2865.61 (n/a)</td><td>2863.28 (n/a)</td><td>2862.20 (n/a)</td><td>2860.98 (n/a)</td><td>2.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>7.96 (+7.69%)</td><td>6.98 (+2.99%)</td><td>7.68 (+16.62%)</td><td>4.95 <b>(-23.47%)</b></td><td>1.25 <b>(+222.35%)</b></td><td>1799.40 <b>(+30.68%)</b></td><td>1316.74 (-0.08%)</td><td>1160.40 (-14.25%)</td><td>1119.20 (-7.14%)</td><td>283.90 <b>(+294.35%)</b></td><td>479.70 (+7.69%)</td><td>420.59 (+2.99%)</td><td>462.68 (+16.62%)</td><td>298.36 <b>(-23.47%)</b></td><td>75.04 <b>(+222.35%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.39 (n/a)</td><td>6.78 (n/a)</td><td>6.59 (n/a)</td><td>6.47 (n/a)</td><td>0.39 (n/a)</td><td>1377.00 (n/a)</td><td>1317.86 (n/a)</td><td>1353.20 (n/a)</td><td>1205.30 (n/a)</td><td>71.99 (n/a)</td><td>445.43 (n/a)</td><td>408.40 (n/a)</td><td>396.74 (n/a)</td><td>389.88 (n/a)</td><td>23.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>6.96 (-3.05%)</td><td>6.38 (-6.93%)</td><td>6.68 (-3.92%)</td><td>4.77 <b>(-25.87%)</b></td><td>0.91 <b>(+211.56%)</b></td><td>1869.00 <b>(+34.91%)</b></td><td>1426.00 (+9.46%)</td><td>1333.90 (+4.08%)</td><td>1281.40 (+3.14%)</td><td>248.83 <b>(+341.03%)</b></td><td>418.97 (-3.05%)</td><td>384.12 (-6.93%)</td><td>402.49 (-3.92%)</td><td>287.26 <b>(-25.87%)</b></td><td>54.67 <b>(+211.56%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.17 (n/a)</td><td>6.85 (n/a)</td><td>6.95 (n/a)</td><td>6.43 (n/a)</td><td>0.29 (n/a)</td><td>1385.40 (n/a)</td><td>1302.72 (n/a)</td><td>1281.60 (n/a)</td><td>1242.40 (n/a)</td><td>56.42 (n/a)</td><td>432.13 (n/a)</td><td>412.72 (n/a)</td><td>418.89 (n/a)</td><td>387.52 (n/a)</td><td>17.55 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>6.90 (+5.24%)</td><td>6.01 (-2.09%)</td><td>6.22 (-1.94%)</td><td>4.52 (-8.56%)</td><td>0.92 <b>(+35.27%)</b></td><td>1971.60 (+9.36%)</td><td>1515.64 (+3.20%)</td><td>1432.80 (+1.98%)</td><td>1290.80 (-4.98%)</td><td>268.84 <b>(+42.48%)</b></td><td>415.92 (+5.24%)</td><td>362.02 (-2.09%)</td><td>374.69 (-1.94%)</td><td>272.31 (-8.56%)</td><td>55.32 <b>(+35.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>6.56 (n/a)</td><td>6.14 (n/a)</td><td>6.34 (n/a)</td><td>4.94 (n/a)</td><td>0.68 (n/a)</td><td>1802.90 (n/a)</td><td>1468.64 (n/a)</td><td>1405.00 (n/a)</td><td>1358.40 (n/a)</td><td>188.70 (n/a)</td><td>395.22 (n/a)</td><td>369.75 (n/a)</td><td>382.11 (n/a)</td><td>297.78 (n/a)</td><td>40.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>8.10 (-3.42%)</td><td>7.84 (-2.08%)</td><td>7.92 (-0.44%)</td><td>7.28 (-4.37%)</td><td>0.32 (+12.32%)</td><td>4789.50 (+4.57%)</td><td>4453.68 (+2.17%)</td><td>4401.90 (+0.44%)</td><td>4305.50 (+3.54%)</td><td>192.83 <b>(+22.63%)</b></td><td>498.77 (-3.42%)</td><td>482.87 (-2.08%)</td><td>487.85 (-0.44%)</td><td>448.38 (-4.37%)</td><td>19.91 (+12.32%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>8.38 (n/a)</td><td>8.01 (n/a)</td><td>7.96 (n/a)</td><td>7.61 (n/a)</td><td>0.29 (n/a)</td><td>4580.30 (n/a)</td><td>4359.12 (n/a)</td><td>4382.40 (n/a)</td><td>4158.20 (n/a)</td><td>157.25 (n/a)</td><td>516.45 (n/a)</td><td>493.15 (n/a)</td><td>490.02 (n/a)</td><td>468.86 (n/a)</td><td>17.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>7.68 (+0.56%)</td><td>7.50 (+1.08%)</td><td>7.61 (+0.42%)</td><td>7.01 (+2.90%)</td><td>0.27 <b>(-20.20%)</b></td><td>4971.70 (-2.82%)</td><td>4655.20 (-1.13%)</td><td>4583.60 (-0.42%)</td><td>4542.30 (-0.55%)</td><td>178.08 <b>(-22.81%)</b></td><td>472.78 (+0.56%)</td><td>461.82 (+1.08%)</td><td>468.51 (+0.42%)</td><td>431.94 (+2.90%)</td><td>16.83 <b>(-20.20%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.63 (n/a)</td><td>7.42 (n/a)</td><td>7.57 (n/a)</td><td>6.82 (n/a)</td><td>0.34 (n/a)</td><td>5115.80 (n/a)</td><td>4708.62 (n/a)</td><td>4602.90 (n/a)</td><td>4567.60 (n/a)</td><td>230.70 (n/a)</td><td>470.15 (n/a)</td><td>456.90 (n/a)</td><td>466.55 (n/a)</td><td>419.77 (n/a)</td><td>21.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>7.48 (-0.48%)</td><td>7.32 (+3.44%)</td><td>7.43 (+9.18%)</td><td>6.89 (+2.07%)</td><td>0.25 <b>(-37.23%)</b></td><td>5061.70 (-2.03%)</td><td>4767.36 (-3.47%)</td><td>4689.90 (-8.41%)</td><td>4663.30 (+0.48%)</td><td>168.46 <b>(-37.76%)</b></td><td>460.51 (-0.48%)</td><td>450.89 (+3.44%)</td><td>457.90 (+9.18%)</td><td>424.26 (+2.07%)</td><td>15.29 <b>(-37.23%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.51 (n/a)</td><td>7.08 (n/a)</td><td>6.81 (n/a)</td><td>6.75 (n/a)</td><td>0.40 (n/a)</td><td>5166.60 (n/a)</td><td>4938.84 (n/a)</td><td>5120.50 (n/a)</td><td>4641.00 (n/a)</td><td>270.67 (n/a)</td><td>462.72 (n/a)</td><td>435.88 (n/a)</td><td>419.39 (n/a)</td><td>415.65 (n/a)</td><td>24.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.81 (+0.11%)</td><td>0.80 (+0.00%)</td><td>0.80 (+0.02%)</td><td>0.80 (-0.07%)</td><td>0.00 <b>(+43.55%)</b></td><td>94146.30 (+0.07%)</td><td>94001.48 (-0.00%)</td><td>94053.80 (-0.02%)</td><td>93677.30 (-0.11%)</td><td>185.42 <b>(+43.44%)</b></td><td>733.58 (+0.11%)</td><td>731.05 (+0.00%)</td><td>730.64 (+0.02%)</td><td>729.92 (-0.07%)</td><td>1.45 <b>(+43.55%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94080.30 (n/a)</td><td>94005.30 (n/a)</td><td>94074.80 (n/a)</td><td>93779.10 (n/a)</td><td>129.27 (n/a)</td><td>732.78 (n/a)</td><td>731.02 (n/a)</td><td>730.48 (n/a)</td><td>730.43 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.74 (+0.05%)</td><td>0.74 (+0.07%)</td><td>0.74 (+0.07%)</td><td>0.74 (+0.10%)</td><td>0.00 <b>(-30.89%)</b></td><td>102711.40 (-0.10%)</td><td>102602.46 (-0.07%)</td><td>102581.30 (-0.07%)</td><td>102532.40 (-0.05%)</td><td>66.69 <b>(-30.98%)</b></td><td>670.22 (+0.05%)</td><td>669.76 (+0.07%)</td><td>669.90 (+0.07%)</td><td>669.05 (+0.10%)</td><td>0.44 <b>(-30.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102812.60 (n/a)</td><td>102669.42 (n/a)</td><td>102650.20 (n/a)</td><td>102584.50 (n/a)</td><td>96.62 (n/a)</td><td>669.88 (n/a)</td><td>669.33 (n/a)</td><td>669.45 (n/a)</td><td>668.40 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.71 (+0.07%)</td><td>0.71 (+0.04%)</td><td>0.71 (+0.08%)</td><td>0.71 (-0.07%)</td><td>0.00 <b>(+61.58%)</b></td><td>106080.80 (+0.07%)</td><td>105864.78 (-0.04%)</td><td>105838.10 (-0.08%)</td><td>105718.70 (-0.07%)</td><td>138.49 <b>(+61.65%)</b></td><td>650.02 (+0.07%)</td><td>649.13 (+0.04%)</td><td>649.29 (+0.08%)</td><td>647.80 (-0.07%)</td><td>0.85 <b>(+61.57%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106004.10 (n/a)</td><td>105911.72 (n/a)</td><td>105927.70 (n/a)</td><td>105795.60 (n/a)</td><td>85.67 (n/a)</td><td>649.55 (n/a)</td><td>648.84 (n/a)</td><td>648.74 (n/a)</td><td>648.27 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>4.37 (+1.26%)</td><td>3.85 (+0.32%)</td><td>3.63 (-2.90%)</td><td>3.44 (+3.26%)</td><td>0.43 (+0.14%)</td><td>2345.00 (-3.16%)</td><td>2114.28 (-0.35%)</td><td>2219.20 (+2.99%)</td><td>1842.70 (-1.24%)</td><td>230.13 (-3.57%)</td><td>1147.19 (+1.26%)</td><td>1009.72 (+0.32%)</td><td>952.57 (-2.90%)</td><td>901.46 (+3.26%)</td><td>113.61 (+0.14%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.32 (n/a)</td><td>3.84 (n/a)</td><td>3.74 (n/a)</td><td>3.33 (n/a)</td><td>0.43 (n/a)</td><td>2421.40 (n/a)</td><td>2121.78 (n/a)</td><td>2154.80 (n/a)</td><td>1865.80 (n/a)</td><td>238.65 (n/a)</td><td>1132.97 (n/a)</td><td>1006.49 (n/a)</td><td>981.02 (n/a)</td><td>873.03 (n/a)</td><td>113.45 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.55 (+7.63%)</td><td>0.36 (-9.03%)</td><td>0.32 (-1.43%)</td><td>0.27 (-11.30%)</td><td>0.11 (+7.27%)</td><td>4553.10 (+12.74%)</td><td>3671.34 (+10.69%)</td><td>3839.40 (+1.45%)</td><td>2276.30 (-7.09%)</td><td>842.21 (+8.21%)</td><td>29.48 (+7.63%)</td><td>19.33 (-9.03%)</td><td>17.48 (-1.43%)</td><td>14.74 (-11.30%)</td><td>5.81 (+7.27%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>4038.50 (n/a)</td><td>3316.88 (n/a)</td><td>3784.50 (n/a)</td><td>2450.10 (n/a)</td><td>778.30 (n/a)</td><td>27.39 (n/a)</td><td>21.25 (n/a)</td><td>17.73 (n/a)</td><td>16.62 (n/a)</td><td>5.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>6.08 (-4.96%)</td><td>4.79 (+5.66%)</td><td>4.92 (+7.28%)</td><td>3.60 (+9.71%)</td><td>0.92 <b>(-23.93%)</b></td><td>1847.80 (-8.85%)</td><td>1432.26 (-7.52%)</td><td>1352.80 (-6.79%)</td><td>1093.90 (+5.22%)</td><td>282.51 <b>(-26.74%)</b></td><td>1878.82 (-4.96%)</td><td>1479.20 (+5.66%)</td><td>1519.26 (+7.28%)</td><td>1112.24 (+9.71%)</td><td>284.91 <b>(-23.93%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>6.40 (n/a)</td><td>4.53 (n/a)</td><td>4.58 (n/a)</td><td>3.28 (n/a)</td><td>1.21 (n/a)</td><td>2027.30 (n/a)</td><td>1548.76 (n/a)</td><td>1451.30 (n/a)</td><td>1039.60 (n/a)</td><td>385.62 (n/a)</td><td>1976.94 (n/a)</td><td>1399.94 (n/a)</td><td>1416.09 (n/a)</td><td>1013.77 (n/a)</td><td>374.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>13.43 (n/a)</td><td>12.95 (n/a)</td><td>13.31 (n/a)</td><td>12.01 (n/a)</td><td>0.61 (n/a)</td><td>13.42 (n/a)</td><td>12.94 (n/a)</td><td>13.31 (n/a)</td><td>12.00 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>25.19 (-0.68%)</td><td>24.51 (+2.40%)</td><td>24.48 (+2.75%)</td><td>24.04 (+8.71%)</td><td>0.45 <b>(-64.27%)</b></td><td>25.17 (-0.68%)</td><td>24.50 (+2.40%)</td><td>24.47 (+2.75%)</td><td>24.02 (+8.71%)</td><td>0.45 <b>(-64.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>25.36 (n/a)</td><td>23.94 (n/a)</td><td>23.83 (n/a)</td><td>22.11 (n/a)</td><td>1.26 (n/a)</td><td>25.35 (n/a)</td><td>23.92 (n/a)</td><td>23.81 (n/a)</td><td>22.10 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>42.29 (+1.77%)</td><td>40.35 (+1.23%)</td><td>39.91 (+0.77%)</td><td>39.50 (+1.69%)</td><td>1.12 (+5.80%)</td><td>42.27 (+1.77%)</td><td>40.33 (+1.23%)</td><td>39.89 (+0.77%)</td><td>39.47 (+1.69%)</td><td>1.12 (+5.81%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>41.56 (n/a)</td><td>39.86 (n/a)</td><td>39.60 (n/a)</td><td>38.84 (n/a)</td><td>1.06 (n/a)</td><td>41.53 (n/a)</td><td>39.83 (n/a)</td><td>39.58 (n/a)</td><td>38.82 (n/a)</td><td>1.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>44.98 (+1.09%)</td><td>43.36 (+0.85%)</td><td>43.75 (+0.93%)</td><td>41.70 (+2.64%)</td><td>1.25 (-14.44%)</td><td>44.95 (+1.09%)</td><td>43.33 (+0.85%)</td><td>43.72 (+0.93%)</td><td>41.68 (+2.64%)</td><td>1.25 (-14.44%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>44.49 (n/a)</td><td>42.99 (n/a)</td><td>43.34 (n/a)</td><td>40.63 (n/a)</td><td>1.47 (n/a)</td><td>44.46 (n/a)</td><td>42.96 (n/a)</td><td>43.31 (n/a)</td><td>40.61 (n/a)</td><td>1.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>13.48 (n/a)</td><td>12.87 (n/a)</td><td>13.25 (n/a)</td><td>12.17 (n/a)</td><td>0.63 (n/a)</td><td>13.48 (n/a)</td><td>12.86 (n/a)</td><td>13.24 (n/a)</td><td>12.16 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>24.71 (-0.34%)</td><td>24.36 (-1.20%)</td><td>24.39 (-1.26%)</td><td>23.82 (-2.69%)</td><td>0.35 <b>(+177.61%)</b></td><td>24.70 (-0.34%)</td><td>24.34 (-1.20%)</td><td>24.37 (-1.26%)</td><td>23.81 (-2.69%)</td><td>0.35 <b>(+177.61%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>24.80 (n/a)</td><td>24.66 (n/a)</td><td>24.70 (n/a)</td><td>24.48 (n/a)</td><td>0.12 (n/a)</td><td>24.78 (n/a)</td><td>24.64 (n/a)</td><td>24.68 (n/a)</td><td>24.47 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>41.83 (+0.64%)</td><td>39.33 (-2.13%)</td><td>38.91 (-3.44%)</td><td>38.06 (-2.78%)</td><td>1.47 <b>(+40.38%)</b></td><td>41.80 (+0.64%)</td><td>39.31 (-2.13%)</td><td>38.88 (-3.44%)</td><td>38.04 (-2.78%)</td><td>1.47 <b>(+40.38%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>41.56 (n/a)</td><td>40.19 (n/a)</td><td>40.29 (n/a)</td><td>39.15 (n/a)</td><td>1.05 (n/a)</td><td>41.54 (n/a)</td><td>40.16 (n/a)</td><td>40.27 (n/a)</td><td>39.13 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>44.70 (-3.70%)</td><td>44.11 (+0.25%)</td><td>44.62 (+1.94%)</td><td>42.94 (+5.88%)</td><td>0.79 <b>(-64.65%)</b></td><td>44.67 (-3.70%)</td><td>44.08 (+0.25%)</td><td>44.59 (+1.94%)</td><td>42.91 (+5.88%)</td><td>0.79 <b>(-64.65%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>46.41 (n/a)</td><td>44.00 (n/a)</td><td>43.77 (n/a)</td><td>40.56 (n/a)</td><td>2.24 (n/a)</td><td>46.38 (n/a)</td><td>43.97 (n/a)</td><td>43.75 (n/a)</td><td>40.53 (n/a)</td><td>2.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>9.60 (+3.53%)</td><td>8.96 (+7.60%)</td><td>9.02 (+7.31%)</td><td>8.44 (+13.63%)</td><td>0.46 <b>(-35.50%)</b></td><td>9.58 (+3.53%)</td><td>8.94 (+7.60%)</td><td>9.00 (+7.31%)</td><td>8.43 (+13.63%)</td><td>0.46 <b>(-35.50%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>9.27 (n/a)</td><td>8.33 (n/a)</td><td>8.40 (n/a)</td><td>7.43 (n/a)</td><td>0.71 (n/a)</td><td>9.26 (n/a)</td><td>8.31 (n/a)</td><td>8.39 (n/a)</td><td>7.41 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.86 (-17.91%)</td><td>0.81 (-8.08%)</td><td>0.82 (+1.16%)</td><td>0.73 (-4.57%)</td><td>0.05 <b>(-63.81%)</b></td><td>0.84 (-17.91%)</td><td>0.79 (-8.08%)</td><td>0.80 (+1.16%)</td><td>0.72 (-4.57%)</td><td>0.04 <b>(-63.81%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.05 (n/a)</td><td>0.88 (n/a)</td><td>0.81 (n/a)</td><td>0.77 (n/a)</td><td>0.12 (n/a)</td><td>1.03 (n/a)</td><td>0.86 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.23 (+7.68%)</td><td>1.08 (+0.69%)</td><td>1.04 (-3.84%)</td><td>1.01 (+0.16%)</td><td>0.09 <b>(+86.39%)</b></td><td>1.22 (+7.68%)</td><td>1.07 (+0.69%)</td><td>1.03 (-3.84%)</td><td>1.00 (+0.16%)</td><td>0.09 <b>(+86.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.14 (n/a)</td><td>1.07 (n/a)</td><td>1.08 (n/a)</td><td>1.01 (n/a)</td><td>0.05 (n/a)</td><td>1.13 (n/a)</td><td>1.06 (n/a)</td><td>1.07 (n/a)</td><td>1.00 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>17.75 (+1.14%)</td><td>15.78 (-5.22%)</td><td>16.23 (-5.44%)</td><td>12.24 <b>(-21.33%)</b></td><td>2.12 <b>(+125.49%)</b></td><td>17.54 (+1.14%)</td><td>15.60 (-5.22%)</td><td>16.04 (-5.44%)</td><td>12.10 <b>(-21.33%)</b></td><td>2.09 <b>(+125.49%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>17.55 (n/a)</td><td>16.65 (n/a)</td><td>17.17 (n/a)</td><td>15.56 (n/a)</td><td>0.94 (n/a)</td><td>17.35 (n/a)</td><td>16.46 (n/a)</td><td>16.97 (n/a)</td><td>15.38 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>13.09 (-1.41%)</td><td>12.64 (-3.85%)</td><td>12.82 (-2.95%)</td><td>11.86 (-7.69%)</td><td>0.52 <b>(+200.69%)</b></td><td>12.86 (-1.41%)</td><td>12.42 (-3.85%)</td><td>12.59 (-2.95%)</td><td>11.65 (-7.69%)</td><td>0.51 <b>(+200.69%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>13.28 (n/a)</td><td>13.14 (n/a)</td><td>13.21 (n/a)</td><td>12.84 (n/a)</td><td>0.17 (n/a)</td><td>13.04 (n/a)</td><td>12.91 (n/a)</td><td>12.97 (n/a)</td><td>12.62 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>8.11 (+10.12%)</td><td>7.47 (+4.57%)</td><td>7.67 (+5.44%)</td><td>6.91 (+0.84%)</td><td>0.52 <b>(+123.23%)</b></td><td>7.97 (+10.12%)</td><td>7.35 (+4.57%)</td><td>7.54 (+5.44%)</td><td>6.79 (+0.84%)</td><td>0.51 <b>(+123.23%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>7.36 (n/a)</td><td>7.15 (n/a)</td><td>7.27 (n/a)</td><td>6.85 (n/a)</td><td>0.23 (n/a)</td><td>7.23 (n/a)</td><td>7.02 (n/a)</td><td>7.15 (n/a)</td><td>6.73 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>6.62 (+13.02%)</td><td>5.65 (+9.50%)</td><td>5.69 (+14.79%)</td><td>4.82 (+1.58%)</td><td>0.70 <b>(+50.23%)</b></td><td>6.52 (+13.02%)</td><td>5.56 (+9.50%)</td><td>5.60 (+14.79%)</td><td>4.75 (+1.58%)</td><td>0.69 <b>(+50.23%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>5.86 (n/a)</td><td>5.16 (n/a)</td><td>4.96 (n/a)</td><td>4.75 (n/a)</td><td>0.47 (n/a)</td><td>5.77 (n/a)</td><td>5.08 (n/a)</td><td>4.88 (n/a)</td><td>4.67 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>13.22 (n/a)</td><td>11.87 (n/a)</td><td>11.20 (n/a)</td><td>10.69 (n/a)</td><td>1.22 (n/a)</td><td>13.21 (n/a)</td><td>11.87 (n/a)</td><td>11.19 (n/a)</td><td>10.68 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>13.31 (n/a)</td><td>12.71 (n/a)</td><td>13.17 (n/a)</td><td>10.67 (n/a)</td><td>1.14 (n/a)</td><td>13.30 (n/a)</td><td>12.70 (n/a)</td><td>13.16 (n/a)</td><td>10.67 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.90 (n/a)</td><td>190.96 (n/a)</td><td>193.40 (n/a)</td><td>145.80 (n/a)</td><td>31.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.00 (n/a)</td><td>171.34 (n/a)</td><td>161.10 (n/a)</td><td>139.80 (n/a)</td><td>28.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.00 (n/a)</td><td>164.94 (n/a)</td><td>169.40 (n/a)</td><td>127.90 (n/a)</td><td>26.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>179.10 (n/a)</td><td>182.80 (n/a)</td><td>153.50 (n/a)</td><td>16.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.90 (n/a)</td><td>174.44 (n/a)</td><td>178.50 (n/a)</td><td>147.10 (n/a)</td><td>17.39 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.10 (n/a)</td><td>182.52 (n/a)</td><td>172.50 (n/a)</td><td>152.90 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.00 (n/a)</td><td>171.70 (n/a)</td><td>174.50 (n/a)</td><td>151.80 (n/a)</td><td>12.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.90 (n/a)</td><td>219.28 (n/a)</td><td>225.50 (n/a)</td><td>173.70 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>209.10 (n/a)</td><td>165.16 (n/a)</td><td>194.00 (n/a)</td><td>111.40 (n/a)</td><td>48.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>160.00 (n/a)</td><td>167.70 (n/a)</td><td>125.30 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.50 (n/a)</td><td>195.22 (n/a)</td><td>171.80 (n/a)</td><td>142.00 (n/a)</td><td>63.67 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>158.72 (n/a)</td><td>158.30 (n/a)</td><td>118.10 (n/a)</td><td>43.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>191.60 (n/a)</td><td>144.52 (n/a)</td><td>143.50 (n/a)</td><td>99.90 (n/a)</td><td>36.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>180.46 (n/a)</td><td>171.40 (n/a)</td><td>129.80 (n/a)</td><td>40.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>210.84 (n/a)</td><td>226.10 (n/a)</td><td>154.10 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.30 (n/a)</td><td>181.90 (n/a)</td><td>183.00 (n/a)</td><td>137.40 (n/a)</td><td>32.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.20 (n/a)</td><td>158.46 (n/a)</td><td>140.50 (n/a)</td><td>134.30 (n/a)</td><td>29.99 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>172.70 (n/a)</td><td>154.24 (n/a)</td><td>158.40 (n/a)</td><td>129.40 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.10 (n/a)</td><td>169.40 (n/a)</td><td>173.40 (n/a)</td><td>139.50 (n/a)</td><td>26.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.70 (n/a)</td><td>189.54 (n/a)</td><td>199.40 (n/a)</td><td>131.60 (n/a)</td><td>33.22 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>244.60 (n/a)</td><td>195.18 (n/a)</td><td>201.30 (n/a)</td><td>147.80 (n/a)</td><td>37.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>342.30 (n/a)</td><td>219.44 (n/a)</td><td>202.00 (n/a)</td><td>101.90 (n/a)</td><td>100.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.30 (n/a)</td><td>178.58 (n/a)</td><td>195.40 (n/a)</td><td>130.50 (n/a)</td><td>34.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>307.00 (n/a)</td><td>206.06 (n/a)</td><td>177.50 (n/a)</td><td>172.10 (n/a)</td><td>57.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>231.70 (n/a)</td><td>184.34 (n/a)</td><td>181.60 (n/a)</td><td>132.90 (n/a)</td><td>38.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.70 (n/a)</td><td>167.10 (n/a)</td><td>176.40 (n/a)</td><td>127.60 (n/a)</td><td>35.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>210.70 (n/a)</td><td>167.32 (n/a)</td><td>159.10 (n/a)</td><td>122.20 (n/a)</td><td>36.59 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>248.00 (n/a)</td><td>175.82 (n/a)</td><td>171.20 (n/a)</td><td>120.60 (n/a)</td><td>51.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>196.70 (n/a)</td><td>169.10 (n/a)</td><td>166.80 (n/a)</td><td>150.30 (n/a)</td><td>17.54 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>218.10 (n/a)</td><td>179.20 (n/a)</td><td>168.40 (n/a)</td><td>158.00 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.30 (n/a)</td><td>181.50 (n/a)</td><td>182.40 (n/a)</td><td>143.30 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>241.00 (n/a)</td><td>205.44 (n/a)</td><td>232.20 (n/a)</td><td>136.80 (n/a)</td><td>45.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 <b>(-26.58%)</b></td><td>0.02 <b>(-20.33%)</b></td><td>0.02 (-19.31%)</td><td>0.02 (-11.42%)</td><td>0.00 <b>(-42.67%)</b></td><td>224.30 (+12.88%)</td><td>187.04 <b>(+23.33%)</b></td><td>182.70 <b>(+23.86%)</b></td><td>159.00 <b>(+36.25%)</b></td><td>28.56 (-12.72%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>151.66 (n/a)</td><td>147.50 (n/a)</td><td>116.70 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-10.08%)</td><td>0.03 (+1.92%)</td><td>0.03 (+17.93%)</td><td>0.02 <b>(-27.54%)</b></td><td>0.01 (+14.57%)</td><td>241.10 <b>(+38.01%)</b></td><td>157.92 (+0.96%)</td><td>138.20 (-15.21%)</td><td>125.80 (+11.23%)</td><td>47.19 <b>(+89.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>174.70 (n/a)</td><td>156.42 (n/a)</td><td>163.00 (n/a)</td><td>113.10 (n/a)</td><td>24.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+7.84%)</td><td>0.03 (+1.28%)</td><td>0.03 (+0.27%)</td><td>0.02 <b>(-20.98%)</b></td><td>0.01 <b>(+72.04%)</b></td><td>229.40 <b>(+26.53%)</b></td><td>165.26 (+1.75%)</td><td>161.40 (-0.31%)</td><td>122.90 (-7.32%)</td><td>40.00 <b>(+106.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.30 (n/a)</td><td>162.42 (n/a)</td><td>161.90 (n/a)</td><td>132.60 (n/a)</td><td>19.35 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-1.50%)</td><td>0.02 (-0.11%)</td><td>0.02 (+0.40%)</td><td>0.02 (-18.82%)</td><td>0.01 <b>(+48.93%)</b></td><td>236.90 <b>(+23.19%)</b></td><td>172.22 (+2.56%)</td><td>170.60 (-0.41%)</td><td>137.00 (+1.56%)</td><td>39.73 <b>(+91.91%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.30 (n/a)</td><td>167.92 (n/a)</td><td>171.30 (n/a)</td><td>134.90 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (+8.21%)</td><td>0.03 (+9.01%)</td><td>0.03 (+8.73%)</td><td>0.02 (+4.95%)</td><td>0.01 (+7.72%)</td><td>187.90 (-4.72%)</td><td>154.50 (-8.24%)</td><td>159.20 (-8.03%)</td><td>108.70 (-7.57%)</td><td>28.73 (-6.05%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>168.38 (n/a)</td><td>173.10 (n/a)</td><td>117.60 (n/a)</td><td>30.59 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-11.00%)</td><td>0.02 (-9.90%)</td><td>0.02 (-4.18%)</td><td>0.02 (-18.94%)</td><td>0.00 (-0.71%)</td><td>217.10 <b>(+23.35%)</b></td><td>181.38 (+11.32%)</td><td>179.20 (+4.37%)</td><td>157.70 (+12.32%)</td><td>22.27 <b>(+38.19%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.00 (n/a)</td><td>162.94 (n/a)</td><td>171.70 (n/a)</td><td>140.40 (n/a)</td><td>16.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-1.13%)</td><td>0.02 (-6.54%)</td><td>0.02 (+6.10%)</td><td>0.02 (-18.27%)</td><td>0.00 <b>(+40.45%)</b></td><td>246.90 <b>(+22.35%)</b></td><td>195.84 (+8.56%)</td><td>178.70 (-5.80%)</td><td>160.20 (+1.14%)</td><td>35.32 <b>(+79.05%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.80 (n/a)</td><td>180.40 (n/a)</td><td>189.70 (n/a)</td><td>158.40 (n/a)</td><td>19.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 (-13.68%)</td><td>0.02 (-11.08%)</td><td>0.02 (-11.29%)</td><td>0.02 (-7.42%)</td><td>0.00 <b>(-42.95%)</b></td><td>255.00 (+8.01%)</td><td>236.16 (+12.21%)</td><td>232.50 (+12.75%)</td><td>227.80 (+15.81%)</td><td>10.76 <b>(-29.00%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.10 (n/a)</td><td>210.46 (n/a)</td><td>206.20 (n/a)</td><td>196.70 (n/a)</td><td>15.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-10.35%)</td><td>0.05 (-5.13%)</td><td>0.05 (+9.15%)</td><td>0.04 (-8.12%)</td><td>0.01 <b>(-24.08%)</b></td><td>211.30 (+8.86%)</td><td>171.16 (+4.63%)</td><td>159.90 (-8.42%)</td><td>146.10 (+11.53%)</td><td>26.81 (-5.52%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>163.58 (n/a)</td><td>174.60 (n/a)</td><td>131.00 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (+13.30%)</td><td>0.06 (-7.78%)</td><td>0.06 (-6.75%)</td><td>0.04 <b>(-27.69%)</b></td><td>0.02 <b>(+153.29%)</b></td><td>209.10 <b>(+38.29%)</b></td><td>156.74 (+13.88%)</td><td>145.00 (+7.25%)</td><td>105.10 (-11.75%)</td><td>40.67 <b>(+208.75%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>151.20 (n/a)</td><td>137.64 (n/a)</td><td>135.20 (n/a)</td><td>119.10 (n/a)</td><td>13.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (-0.69%)</td><td>0.05 (-7.69%)</td><td>0.05 (-16.56%)</td><td>0.04 (-12.68%)</td><td>0.01 (+17.32%)</td><td>221.60 (+14.52%)</td><td>169.06 (+10.09%)</td><td>172.60 (+19.86%)</td><td>123.50 (+0.73%)</td><td>40.16 <b>(+32.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>153.56 (n/a)</td><td>144.00 (n/a)</td><td>122.60 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-0.89%)</td><td>0.05 (-12.46%)</td><td>0.05 (-17.64%)</td><td>0.04 <b>(-20.90%)</b></td><td>0.01 <b>(+77.69%)</b></td><td>209.10 <b>(+26.42%)</b></td><td>171.10 (+16.28%)</td><td>178.20 <b>(+21.47%)</b></td><td>134.30 (+0.90%)</td><td>29.07 <b>(+125.00%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>165.40 (n/a)</td><td>147.14 (n/a)</td><td>146.70 (n/a)</td><td>133.10 (n/a)</td><td>12.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (+1.28%)</td><td>0.05 (-5.07%)</td><td>0.05 (-16.56%)</td><td>0.03 (-14.43%)</td><td>0.01 <b>(+37.87%)</b></td><td>240.90 (+16.83%)</td><td>177.36 (+7.99%)</td><td>182.00 (+19.82%)</td><td>133.90 (-1.25%)</td><td>44.19 <b>(+51.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>164.24 (n/a)</td><td>151.90 (n/a)</td><td>135.60 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 <b>(-24.14%)</b></td><td>0.04 (-10.61%)</td><td>0.04 (-5.69%)</td><td>0.04 (-8.85%)</td><td>0.01 <b>(-43.41%)</b></td><td>233.70 (+9.72%)</td><td>193.58 (+9.18%)</td><td>195.20 (+6.03%)</td><td>154.50 <b>(+31.83%)</b></td><td>31.77 (-17.47%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>177.30 (n/a)</td><td>184.10 (n/a)</td><td>117.20 (n/a)</td><td>38.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (+5.60%)</td><td>0.05 (-0.63%)</td><td>0.05 (+9.71%)</td><td>0.04 (+1.50%)</td><td>0.01 (-0.55%)</td><td>201.80 (-1.51%)</td><td>172.66 (+0.01%)</td><td>180.70 (-8.83%)</td><td>114.80 (-5.28%)</td><td>33.79 (-13.18%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>172.64 (n/a)</td><td>198.20 (n/a)</td><td>121.20 (n/a)</td><td>38.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 <b>(-24.43%)</b></td><td>0.04 (-18.66%)</td><td>0.04 (-17.39%)</td><td>0.03 <b>(-20.01%)</b></td><td>0.01 <b>(-35.73%)</b></td><td>247.60 <b>(+25.05%)</b></td><td>209.72 <b>(+22.06%)</b></td><td>214.00 <b>(+21.04%)</b></td><td>173.40 <b>(+32.27%)</b></td><td>28.93 (+5.53%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.00 (n/a)</td><td>171.82 (n/a)</td><td>176.80 (n/a)</td><td>131.10 (n/a)</td><td>27.41 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (-16.34%)</td><td>0.04 (-9.31%)</td><td>0.04 (-5.12%)</td><td>0.03 (-12.31%)</td><td>0.01 <b>(-29.87%)</b></td><td>234.20 (+14.02%)</td><td>194.10 (+9.38%)</td><td>191.70 (+5.39%)</td><td>155.30 (+19.46%)</td><td>28.25 (-2.06%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>177.46 (n/a)</td><td>181.90 (n/a)</td><td>130.00 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (+14.36%)</td><td>0.04 (-6.38%)</td><td>0.04 (-7.74%)</td><td>0.03 <b>(-29.82%)</b></td><td>0.01 <b>(+239.26%)</b></td><td>318.30 <b>(+42.48%)</b></td><td>232.80 (+10.75%)</td><td>225.00 (+8.38%)</td><td>171.00 (-12.53%)</td><td>53.29 <b>(+326.71%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>210.20 (n/a)</td><td>207.60 (n/a)</td><td>195.50 (n/a)</td><td>12.49 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.11 <b>(-29.89%)</b></td><td>0.10 (-15.96%)</td><td>0.10 (+1.57%)</td><td>0.07 <b>(-22.94%)</b></td><td>0.01 <b>(-46.34%)</b></td><td>224.70 <b>(+29.73%)</b></td><td>173.68 (+16.85%)</td><td>160.70 (-1.53%)</td><td>148.70 <b>(+42.71%)</b></td><td>30.34 (-0.96%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>173.20 (n/a)</td><td>148.64 (n/a)</td><td>163.20 (n/a)</td><td>104.20 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.11 <b>(-27.69%)</b></td><td>0.09 <b>(-22.75%)</b></td><td>0.10 (+2.32%)</td><td>0.05 <b>(-48.63%)</b></td><td>0.02 (-3.58%)</td><td>345.60 <b>(+94.70%)</b></td><td>205.90 <b>(+36.61%)</b></td><td>163.80 (-2.27%)</td><td>152.30 <b>(+38.33%)</b></td><td>80.97 <b>(+160.41%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>177.50 (n/a)</td><td>150.72 (n/a)</td><td>167.60 (n/a)</td><td>110.10 (n/a)</td><td>31.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.11 (-13.50%)</td><td>0.09 (-19.49%)</td><td>0.09 (-14.32%)</td><td>0.05 <b>(-38.91%)</b></td><td>0.02 <b>(+30.67%)</b></td><td>299.30 <b>(+63.64%)</b></td><td>202.30 <b>(+29.28%)</b></td><td>184.90 (+16.73%)</td><td>144.50 (+15.60%)</td><td>58.73 <b>(+157.46%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>182.90 (n/a)</td><td>156.48 (n/a)</td><td>158.40 (n/a)</td><td>125.00 (n/a)</td><td>22.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (+3.11%)</td><td>0.10 (-4.71%)</td><td>0.10 (-2.19%)</td><td>0.06 <b>(-31.80%)</b></td><td>0.03 <b>(+52.53%)</b></td><td>282.30 <b>(+46.65%)</b></td><td>175.58 (+12.26%)</td><td>159.40 (+2.18%)</td><td>116.10 (-3.01%)</td><td>66.71 <b>(+115.83%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.50 (n/a)</td><td>156.40 (n/a)</td><td>156.00 (n/a)</td><td>119.70 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (+1.28%)</td><td>0.11 (+4.18%)</td><td>0.12 (+18.24%)</td><td>0.08 (-11.38%)</td><td>0.03 <b>(+30.84%)</b></td><td>214.60 (+12.83%)</td><td>162.90 (-1.59%)</td><td>142.30 (-15.40%)</td><td>120.40 (-1.23%)</td><td>41.81 <b>(+50.82%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.20 (n/a)</td><td>165.54 (n/a)</td><td>168.20 (n/a)</td><td>121.90 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.11 <b>(-27.47%)</b></td><td>0.09 <b>(-20.33%)</b></td><td>0.09 <b>(-20.24%)</b></td><td>0.07 (-4.02%)</td><td>0.01 <b>(-59.63%)</b></td><td>225.20 (+4.16%)</td><td>192.06 (+19.38%)</td><td>191.10 <b>(+25.39%)</b></td><td>155.70 <b>(+37.79%)</b></td><td>26.29 <b>(-42.69%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>216.20 (n/a)</td><td>160.88 (n/a)</td><td>152.40 (n/a)</td><td>113.00 (n/a)</td><td>45.88 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 <b>(-39.35%)</b></td><td>0.09 <b>(-25.10%)</b></td><td>0.09 (-16.52%)</td><td>0.08 (-7.35%)</td><td>0.01 <b>(-68.62%)</b></td><td>217.60 (+7.94%)</td><td>192.22 <b>(+27.13%)</b></td><td>180.40 (+19.79%)</td><td>168.80 <b>(+64.84%)</b></td><td>23.07 <b>(-42.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>201.60 (n/a)</td><td>151.20 (n/a)</td><td>150.60 (n/a)</td><td>102.40 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 <b>(-37.43%)</b></td><td>0.07 (-17.40%)</td><td>0.07 (-6.85%)</td><td>0.07 (-10.11%)</td><td>0.01 <b>(-72.55%)</b></td><td>243.40 (+11.24%)</td><td>223.36 (+15.42%)</td><td>229.40 (+7.35%)</td><td>189.10 <b>(+59.85%)</b></td><td>20.82 <b>(-50.95%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>218.80 (n/a)</td><td>193.52 (n/a)</td><td>213.70 (n/a)</td><td>118.30 (n/a)</td><td>42.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.20 <b>(-23.18%)</b></td><td>0.16 (-19.67%)</td><td>0.17 (-6.39%)</td><td>0.10 <b>(-39.97%)</b></td><td>0.04 (+1.47%)</td><td>333.20 <b>(+66.52%)</b></td><td>219.14 <b>(+28.66%)</b></td><td>188.40 (+6.80%)</td><td>166.00 <b>(+30.20%)</b></td><td>66.67 <b>(+131.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>200.10 (n/a)</td><td>170.32 (n/a)</td><td>176.40 (n/a)</td><td>127.50 (n/a)</td><td>28.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 (-8.26%)</td><td>0.17 (-17.10%)</td><td>0.17 <b>(-20.42%)</b></td><td>0.11 <b>(-38.14%)</b></td><td>0.04 <b>(+55.56%)</b></td><td>297.30 <b>(+61.66%)</b></td><td>200.70 <b>(+25.97%)</b></td><td>189.60 <b>(+25.65%)</b></td><td>148.30 (+8.96%)</td><td>58.42 <b>(+174.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.90 (n/a)</td><td>159.32 (n/a)</td><td>150.90 (n/a)</td><td>136.10 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 (-7.39%)</td><td>0.19 (-7.73%)</td><td>0.19 (-13.76%)</td><td>0.17 (+0.78%)</td><td>0.02 <b>(-22.80%)</b></td><td>195.80 (-0.81%)</td><td>174.24 (+7.81%)</td><td>176.00 (+15.94%)</td><td>152.30 (+8.01%)</td><td>18.65 (-18.18%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>197.40 (n/a)</td><td>161.62 (n/a)</td><td>151.80 (n/a)</td><td>141.00 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 (+7.92%)</td><td>0.19 (-0.14%)</td><td>0.18 (+0.13%)</td><td>0.15 (+3.43%)</td><td>0.04 (+7.85%)</td><td>219.40 (-3.31%)</td><td>178.52 (+0.15%)</td><td>183.00 (-0.16%)</td><td>125.00 (-7.34%)</td><td>33.92 (-6.67%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>226.90 (n/a)</td><td>178.26 (n/a)</td><td>183.30 (n/a)</td><td>134.90 (n/a)</td><td>36.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.20 (-10.98%)</td><td>0.16 (-13.78%)</td><td>0.15 (-15.43%)</td><td>0.11 <b>(-26.30%)</b></td><td>0.03 (+7.30%)</td><td>301.80 <b>(+35.64%)</b></td><td>216.72 (+18.10%)</td><td>212.80 (+18.22%)</td><td>160.80 (+12.29%)</td><td>52.73 <b>(+66.37%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>222.50 (n/a)</td><td>183.50 (n/a)</td><td>180.00 (n/a)</td><td>143.20 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (-5.66%)</td><td>0.20 (-1.94%)</td><td>0.18 (-3.07%)</td><td>0.17 (+6.57%)</td><td>0.03 <b>(-33.51%)</b></td><td>194.50 (-6.13%)</td><td>170.50 (-0.28%)</td><td>183.00 (+3.16%)</td><td>139.00 (+5.95%)</td><td>24.91 <b>(-33.32%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>207.20 (n/a)</td><td>170.98 (n/a)</td><td>177.40 (n/a)</td><td>131.20 (n/a)</td><td>37.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 (-9.33%)</td><td>0.13 (-12.72%)</td><td>0.13 (-9.53%)</td><td>0.10 <b>(-31.06%)</b></td><td>0.02 <b>(+69.77%)</b></td><td>343.40 <b>(+45.02%)</b></td><td>258.98 (+16.91%)</td><td>245.10 (+10.55%)</td><td>212.50 (+10.28%)</td><td>49.84 <b>(+183.33%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>236.80 (n/a)</td><td>221.52 (n/a)</td><td>221.70 (n/a)</td><td>192.70 (n/a)</td><td>17.59 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+5.52%)</td><td>0.02 (-4.34%)</td><td>0.03 (+10.38%)</td><td>0.01 <b>(-35.63%)</b></td><td>0.01 <b>(+61.31%)</b></td><td>322.50 <b>(+55.35%)</b></td><td>190.06 (+12.55%)</td><td>160.30 (-9.38%)</td><td>130.10 (-5.24%)</td><td>77.00 <b>(+158.60%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.60 (n/a)</td><td>168.86 (n/a)</td><td>176.90 (n/a)</td><td>137.30 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-0.17%)</td><td>0.02 (+1.00%)</td><td>0.03 (+7.57%)</td><td>0.02 (+1.21%)</td><td>0.01 (+15.82%)</td><td>232.70 (-1.19%)</td><td>179.34 (+0.01%)</td><td>163.60 (-7.05%)</td><td>141.70 (+0.21%)</td><td>41.70 (+13.59%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.50 (n/a)</td><td>179.32 (n/a)</td><td>176.00 (n/a)</td><td>141.40 (n/a)</td><td>36.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 (+9.31%)</td><td>0.02 (+19.91%)</td><td>0.02 <b>(+31.38%)</b></td><td>0.02 (+13.97%)</td><td>0.00 <b>(+21.64%)</b></td><td>238.80 (-12.27%)</td><td>199.90 (-16.38%)</td><td>180.10 <b>(-23.91%)</b></td><td>176.30 (-8.51%)</td><td>29.77 (-2.46%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>272.20 (n/a)</td><td>239.06 (n/a)</td><td>236.70 (n/a)</td><td>192.70 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 (-1.56%)</td><td>0.02 (+8.28%)</td><td>0.02 (+13.24%)</td><td>0.02 (+2.19%)</td><td>0.00 (+1.82%)</td><td>233.00 (-2.14%)</td><td>194.20 (-7.59%)</td><td>185.00 (-11.65%)</td><td>182.30 (+1.56%)</td><td>21.80 (+3.06%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.10 (n/a)</td><td>210.16 (n/a)</td><td>209.40 (n/a)</td><td>179.50 (n/a)</td><td>21.15 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+17.17%)</td><td>0.02 (+11.56%)</td><td>0.02 (+3.16%)</td><td>0.02 <b>(+24.06%)</b></td><td>0.00 <b>(+24.15%)</b></td><td>232.40 (-19.39%)</td><td>190.78 (-10.31%)</td><td>190.30 (-3.06%)</td><td>149.90 (-14.68%)</td><td>36.05 (-17.86%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>288.30 (n/a)</td><td>212.70 (n/a)</td><td>196.30 (n/a)</td><td>175.70 (n/a)</td><td>43.88 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 <b>(+27.04%)</b></td><td>0.03 (+18.71%)</td><td>0.03 (+18.90%)</td><td>0.02 (+10.87%)</td><td>0.00 <b>(+80.00%)</b></td><td>201.20 (-9.78%)</td><td>162.82 (-14.64%)</td><td>160.10 (-15.91%)</td><td>127.50 <b>(-21.30%)</b></td><td>27.99 <b>(+27.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.00 (n/a)</td><td>190.74 (n/a)</td><td>190.40 (n/a)</td><td>162.00 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+5.44%)</td><td>0.02 (-10.18%)</td><td>0.02 (-15.68%)</td><td>0.01 <b>(-30.81%)</b></td><td>0.01 <b>(+76.67%)</b></td><td>301.20 <b>(+44.53%)</b></td><td>211.20 (+16.04%)</td><td>207.70 (+18.62%)</td><td>145.10 (-5.16%)</td><td>56.98 <b>(+140.43%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>182.00 (n/a)</td><td>175.10 (n/a)</td><td>153.00 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+5.22%)</td><td>0.03 (+8.60%)</td><td>0.02 (+10.13%)</td><td>0.02 (+1.16%)</td><td>0.00 (+11.52%)</td><td>198.20 (-1.15%)</td><td>165.60 (-7.72%)</td><td>168.70 (-9.20%)</td><td>140.60 (-4.94%)</td><td>21.94 (+5.58%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.50 (n/a)</td><td>179.46 (n/a)</td><td>185.80 (n/a)</td><td>147.90 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 <b>(+43.41%)</b></td><td>0.03 <b>(+36.69%)</b></td><td>0.03 <b>(+44.38%)</b></td><td>0.02 (+13.91%)</td><td>0.00 <b>(+84.74%)</b></td><td>210.00 (-12.21%)</td><td>157.70 <b>(-25.73%)</b></td><td>150.00 <b>(-30.72%)</b></td><td>124.20 <b>(-30.26%)</b></td><td>31.72 (+15.44%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.20 (n/a)</td><td>212.32 (n/a)</td><td>216.50 (n/a)</td><td>178.10 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-18.84%)</td><td>0.02 (+2.47%)</td><td>0.02 (+4.25%)</td><td>0.02 (+12.70%)</td><td>0.00 <b>(-63.90%)</b></td><td>181.20 (-11.26%)</td><td>166.64 (-4.91%)</td><td>169.60 (-4.07%)</td><td>153.80 <b>(+23.24%)</b></td><td>12.38 <b>(-60.47%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>175.24 (n/a)</td><td>176.80 (n/a)</td><td>124.80 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (+17.50%)</td><td>0.03 (+9.53%)</td><td>0.03 <b>(+21.86%)</b></td><td>0.02 (-10.55%)</td><td>0.01 <b>(+77.91%)</b></td><td>214.10 (+11.80%)</td><td>152.50 (-4.69%)</td><td>133.00 (-17.90%)</td><td>105.40 (-14.86%)</td><td>43.98 <b>(+75.63%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.50 (n/a)</td><td>160.00 (n/a)</td><td>162.00 (n/a)</td><td>123.80 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+6.75%)</td><td>0.03 (+6.57%)</td><td>0.03 (+2.76%)</td><td>0.02 <b>(+26.77%)</b></td><td>0.00 <b>(-27.24%)</b></td><td>182.50 <b>(-21.13%)</b></td><td>164.84 (-7.35%)</td><td>162.70 (-2.69%)</td><td>144.50 (-6.35%)</td><td>16.41 <b>(-46.95%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.40 (n/a)</td><td>177.92 (n/a)</td><td>167.20 (n/a)</td><td>154.30 (n/a)</td><td>30.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-8.15%)</td><td>0.02 (-2.21%)</td><td>0.02 (+9.42%)</td><td>0.02 <b>(-24.42%)</b></td><td>0.00 (+12.42%)</td><td>271.40 <b>(+32.26%)</b></td><td>184.48 (+4.45%)</td><td>171.60 (-8.63%)</td><td>147.50 (+8.86%)</td><td>50.10 <b>(+66.37%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.20 (n/a)</td><td>176.62 (n/a)</td><td>187.80 (n/a)</td><td>135.50 (n/a)</td><td>30.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+6.73%)</td><td>0.02 (+7.14%)</td><td>0.02 (+2.99%)</td><td>0.02 (+2.71%)</td><td>0.00 <b>(+32.95%)</b></td><td>214.10 (-2.64%)</td><td>174.90 (-5.62%)</td><td>179.10 (-2.93%)</td><td>137.10 (-6.29%)</td><td>32.67 <b>(+21.77%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.90 (n/a)</td><td>185.32 (n/a)</td><td>184.50 (n/a)</td><td>146.30 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 <b>(+20.70%)</b></td><td>0.02 (+14.05%)</td><td>0.03 <b>(+22.57%)</b></td><td>0.02 (+0.77%)</td><td>0.00 <b>(+88.61%)</b></td><td>233.40 (-0.77%)</td><td>180.46 (-10.73%)</td><td>161.20 (-18.38%)</td><td>150.60 (-17.16%)</td><td>35.15 <b>(+56.30%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.20 (n/a)</td><td>202.14 (n/a)</td><td>197.50 (n/a)</td><td>181.80 (n/a)</td><td>22.49 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+11.89%)</td><td>0.03 (+18.51%)</td><td>0.03 <b>(+22.93%)</b></td><td>0.02 (+18.01%)</td><td>0.00 (-5.30%)</td><td>217.20 (-15.26%)</td><td>165.88 (-16.53%)</td><td>162.10 (-18.67%)</td><td>132.00 (-10.63%)</td><td>31.33 <b>(-25.84%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.30 (n/a)</td><td>198.72 (n/a)</td><td>199.30 (n/a)</td><td>147.70 (n/a)</td><td>42.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (-13.01%)</td><td>0.04 (-8.16%)</td><td>0.04 (-5.69%)</td><td>0.04 (-2.49%)</td><td>0.00 <b>(-39.21%)</b></td><td>212.70 (+2.56%)</td><td>185.74 (+8.00%)</td><td>183.70 (+6.06%)</td><td>168.60 (+14.93%)</td><td>17.19 <b>(-27.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>171.98 (n/a)</td><td>173.20 (n/a)</td><td>146.70 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 <b>(+23.19%)</b></td><td>0.05 (+16.10%)</td><td>0.05 (+8.43%)</td><td>0.04 (+18.94%)</td><td>0.01 <b>(+33.16%)</b></td><td>192.30 (-15.92%)</td><td>159.04 (-13.64%)</td><td>162.30 (-7.78%)</td><td>132.00 (-18.87%)</td><td>23.67 (-10.88%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>184.16 (n/a)</td><td>176.00 (n/a)</td><td>162.70 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 <b>(+27.74%)</b></td><td>0.04 (+9.12%)</td><td>0.04 (+6.70%)</td><td>0.03 (-5.14%)</td><td>0.01 <b>(+197.13%)</b></td><td>267.40 (+5.40%)</td><td>217.46 (-6.46%)</td><td>221.00 (-6.28%)</td><td>167.40 <b>(-21.74%)</b></td><td>36.83 <b>(+142.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>253.70 (n/a)</td><td>232.48 (n/a)</td><td>235.80 (n/a)</td><td>213.90 (n/a)</td><td>15.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (+7.73%)</td><td>0.04 (+9.88%)</td><td>0.04 (+13.62%)</td><td>0.04 (+6.04%)</td><td>0.00 <b>(+21.94%)</b></td><td>217.90 (-5.71%)</td><td>189.92 (-8.86%)</td><td>183.10 (-11.97%)</td><td>175.10 (-7.16%)</td><td>17.01 (+7.41%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.10 (n/a)</td><td>208.38 (n/a)</td><td>208.00 (n/a)</td><td>188.60 (n/a)</td><td>15.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-10.63%)</td><td>0.05 (+12.44%)</td><td>0.06 <b>(+31.85%)</b></td><td>0.05 <b>(+21.35%)</b></td><td>0.01 <b>(-49.57%)</b></td><td>174.20 (-17.60%)</td><td>152.78 (-13.55%)</td><td>144.60 <b>(-24.17%)</b></td><td>136.80 (+11.86%)</td><td>16.70 <b>(-52.21%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>176.72 (n/a)</td><td>190.70 (n/a)</td><td>122.30 (n/a)</td><td>34.94 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 <b>(+31.48%)</b></td><td>0.05 (+16.52%)</td><td>0.05 (+11.30%)</td><td>0.05 (+4.90%)</td><td>0.01 <b>(+172.62%)</b></td><td>182.00 (-4.66%)</td><td>153.72 (-12.90%)</td><td>160.90 (-10.16%)</td><td>123.20 <b>(-23.90%)</b></td><td>22.55 <b>(+95.97%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.90 (n/a)</td><td>176.48 (n/a)</td><td>179.10 (n/a)</td><td>161.90 (n/a)</td><td>11.51 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 <b>(+35.89%)</b></td><td>0.05 (+3.60%)</td><td>0.04 (-16.38%)</td><td>0.03 (+7.76%)</td><td>0.02 <b>(+82.24%)</b></td><td>239.40 (-7.21%)</td><td>190.42 (+0.55%)</td><td>202.80 (+19.58%)</td><td>113.80 <b>(-26.39%)</b></td><td>52.30 <b>(+23.90%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>258.00 (n/a)</td><td>189.38 (n/a)</td><td>169.60 (n/a)</td><td>154.60 (n/a)</td><td>42.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (-1.65%)</td><td>0.06 (+9.70%)</td><td>0.05 (+6.82%)</td><td>0.05 <b>(+26.42%)</b></td><td>0.01 <b>(-22.83%)</b></td><td>169.70 <b>(-20.89%)</b></td><td>148.56 (-10.66%)</td><td>160.70 (-6.35%)</td><td>118.20 (+1.63%)</td><td>23.02 <b>(-36.24%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>166.28 (n/a)</td><td>171.60 (n/a)</td><td>116.30 (n/a)</td><td>36.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (+12.03%)</td><td>0.05 (-5.32%)</td><td>0.05 <b>(-22.35%)</b></td><td>0.04 <b>(+20.13%)</b></td><td>0.01 (-6.90%)</td><td>182.80 (-16.76%)</td><td>162.56 (+4.06%)</td><td>170.50 <b>(+28.78%)</b></td><td>116.40 (-10.74%)</td><td>26.40 <b>(-31.74%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>156.22 (n/a)</td><td>132.40 (n/a)</td><td>130.40 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-5.99%)</td><td>0.05 (+5.33%)</td><td>0.05 (+8.70%)</td><td>0.04 (+17.28%)</td><td>0.01 <b>(-39.63%)</b></td><td>198.90 (-14.74%)</td><td>163.74 (-8.54%)</td><td>166.00 (-7.98%)</td><td>129.90 (+6.39%)</td><td>24.77 <b>(-45.90%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.30 (n/a)</td><td>179.02 (n/a)</td><td>180.40 (n/a)</td><td>122.10 (n/a)</td><td>45.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-2.84%)</td><td>0.05 (+7.95%)</td><td>0.05 (+17.66%)</td><td>0.04 (+15.29%)</td><td>0.01 <b>(-28.26%)</b></td><td>216.90 (-13.27%)</td><td>173.12 (-9.37%)</td><td>167.40 (-15.03%)</td><td>139.80 (+2.87%)</td><td>28.07 <b>(-34.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.10 (n/a)</td><td>191.02 (n/a)</td><td>197.00 (n/a)</td><td>135.90 (n/a)</td><td>42.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (+17.96%)</td><td>0.05 (+15.47%)</td><td>0.05 (+16.15%)</td><td>0.04 <b>(+23.21%)</b></td><td>0.01 (-6.41%)</td><td>184.80 (-18.80%)</td><td>158.74 (-14.20%)</td><td>159.90 (-13.89%)</td><td>127.70 (-15.21%)</td><td>20.54 <b>(-35.88%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.60 (n/a)</td><td>185.02 (n/a)</td><td>185.70 (n/a)</td><td>150.60 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 <b>(+30.75%)</b></td><td>0.05 (+16.40%)</td><td>0.05 (+11.69%)</td><td>0.04 (+15.74%)</td><td>0.01 <b>(+66.49%)</b></td><td>203.10 (-13.61%)</td><td>170.42 (-13.22%)</td><td>173.50 (-10.43%)</td><td>127.30 <b>(-23.50%)</b></td><td>27.31 (+5.30%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.10 (n/a)</td><td>196.38 (n/a)</td><td>193.70 (n/a)</td><td>166.40 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (-8.92%)</td><td>0.04 (+3.06%)</td><td>0.05 (+13.48%)</td><td>0.03 (-6.73%)</td><td>0.01 (-14.18%)</td><td>248.90 (+7.24%)</td><td>186.96 (-3.21%)</td><td>171.10 (-11.89%)</td><td>155.20 (+9.76%)</td><td>36.66 (+6.11%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>193.16 (n/a)</td><td>194.20 (n/a)</td><td>141.40 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (+19.07%)</td><td>0.05 (+15.32%)</td><td>0.05 <b>(+29.18%)</b></td><td>0.03 (+1.03%)</td><td>0.01 <b>(+60.02%)</b></td><td>241.20 (-1.03%)</td><td>186.40 (-11.16%)</td><td>168.50 <b>(-22.60%)</b></td><td>134.40 (-16.00%)</td><td>43.57 <b>(+40.25%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.70 (n/a)</td><td>209.82 (n/a)</td><td>217.70 (n/a)</td><td>160.00 (n/a)</td><td>31.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 (-13.31%)</td><td>0.04 (-5.29%)</td><td>0.04 (-6.68%)</td><td>0.04 (+5.83%)</td><td>0.01 <b>(-33.52%)</b></td><td>226.70 (-5.50%)</td><td>195.50 (+3.60%)</td><td>205.60 (+7.14%)</td><td>158.90 (+15.40%)</td><td>28.89 <b>(-27.46%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.90 (n/a)</td><td>188.70 (n/a)</td><td>191.90 (n/a)</td><td>137.70 (n/a)</td><td>39.82 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (-0.04%)</td><td>0.11 (+14.18%)</td><td>0.11 <b>(+22.62%)</b></td><td>0.09 (+14.07%)</td><td>0.02 (-6.36%)</td><td>191.80 (-12.34%)</td><td>154.94 (-13.20%)</td><td>151.10 (-18.46%)</td><td>121.10 (+0.08%)</td><td>32.21 (-16.59%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>218.80 (n/a)</td><td>178.50 (n/a)</td><td>185.30 (n/a)</td><td>121.00 (n/a)</td><td>38.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 <b>(+36.26%)</b></td><td>0.12 <b>(+25.40%)</b></td><td>0.11 (+18.98%)</td><td>0.09 <b>(+36.23%)</b></td><td>0.02 <b>(+39.13%)</b></td><td>176.10 <b>(-26.59%)</b></td><td>145.24 <b>(-20.19%)</b></td><td>143.40 (-15.94%)</td><td>112.90 <b>(-26.64%)</b></td><td>25.98 <b>(-25.26%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.90 (n/a)</td><td>181.98 (n/a)</td><td>170.60 (n/a)</td><td>153.90 (n/a)</td><td>34.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (+4.82%)</td><td>0.07 (-3.13%)</td><td>0.07 (-3.47%)</td><td>0.05 <b>(-23.95%)</b></td><td>0.02 <b>(+83.95%)</b></td><td>311.20 <b>(+31.47%)</b></td><td>229.52 (+6.59%)</td><td>235.50 (+3.61%)</td><td>179.10 (-4.63%)</td><td>54.55 <b>(+122.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.70 (n/a)</td><td>215.32 (n/a)</td><td>227.30 (n/a)</td><td>187.80 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (-11.28%)</td><td>0.08 (-17.20%)</td><td>0.07 (-19.85%)</td><td>0.06 <b>(-31.57%)</b></td><td>0.01 <b>(+156.28%)</b></td><td>276.00 <b>(+46.19%)</b></td><td>221.08 <b>(+22.88%)</b></td><td>223.30 <b>(+24.75%)</b></td><td>189.70 (+12.72%)</td><td>35.23 <b>(+313.83%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>188.80 (n/a)</td><td>179.92 (n/a)</td><td>179.00 (n/a)</td><td>168.30 (n/a)</td><td>8.51 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (+0.43%)</td><td>0.10 (-3.64%)</td><td>0.09 (-15.02%)</td><td>0.09 (-5.59%)</td><td>0.02 (+18.94%)</td><td>188.80 (+5.95%)</td><td>162.78 (+5.02%)</td><td>179.90 (+17.66%)</td><td>116.40 (-0.43%)</td><td>31.66 <b>(+26.81%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>178.20 (n/a)</td><td>155.00 (n/a)</td><td>152.90 (n/a)</td><td>116.90 (n/a)</td><td>24.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (+5.74%)</td><td>0.11 (-1.37%)</td><td>0.10 (-12.32%)</td><td>0.09 <b>(+21.99%)</b></td><td>0.02 <b>(-27.55%)</b></td><td>181.70 (-18.04%)</td><td>157.90 (-2.06%)</td><td>163.10 (+14.06%)</td><td>116.10 (-5.38%)</td><td>24.71 <b>(-44.96%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>221.70 (n/a)</td><td>161.22 (n/a)</td><td>143.00 (n/a)</td><td>122.70 (n/a)</td><td>44.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 (-6.38%)</td><td>0.11 (-0.23%)</td><td>0.11 (+3.39%)</td><td>0.10 <b>(+20.95%)</b></td><td>0.01 <b>(-52.89%)</b></td><td>167.10 (-17.32%)</td><td>152.62 (-1.99%)</td><td>151.60 (-3.25%)</td><td>135.80 (+6.85%)</td><td>12.89 <b>(-57.43%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>155.72 (n/a)</td><td>156.70 (n/a)</td><td>127.10 (n/a)</td><td>30.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 (-1.91%)</td><td>0.10 (-10.03%)</td><td>0.10 (-12.30%)</td><td>0.08 (-3.08%)</td><td>0.02 (-9.13%)</td><td>210.90 (+3.18%)</td><td>169.36 (+10.72%)</td><td>167.50 (+14.02%)</td><td>133.60 (+1.91%)</td><td>28.17 (-5.78%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.40 (n/a)</td><td>152.96 (n/a)</td><td>146.90 (n/a)</td><td>131.10 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (-4.38%)</td><td>0.11 (+9.24%)</td><td>0.11 (-1.65%)</td><td>0.10 <b>(+43.45%)</b></td><td>0.01 <b>(-64.33%)</b></td><td>156.40 <b>(-30.30%)</b></td><td>144.26 (-14.22%)</td><td>151.20 (+1.68%)</td><td>126.40 (+4.55%)</td><td>12.89 <b>(-74.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>224.40 (n/a)</td><td>168.18 (n/a)</td><td>148.70 (n/a)</td><td>120.90 (n/a)</td><td>51.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (+5.37%)</td><td>0.09 <b>(-22.70%)</b></td><td>0.10 (-13.42%)</td><td>0.05 <b>(-56.14%)</b></td><td>0.04 <b>(+219.94%)</b></td><td>348.40 <b>(+128.01%)</b></td><td>206.14 <b>(+48.22%)</b></td><td>165.90 (+15.53%)</td><td>118.20 (-5.06%)</td><td>92.19 <b>(+618.20%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>152.80 (n/a)</td><td>139.08 (n/a)</td><td>143.60 (n/a)</td><td>124.50 (n/a)</td><td>12.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (+0.32%)</td><td>0.11 (+7.93%)</td><td>0.11 (+11.13%)</td><td>0.09 <b>(+24.68%)</b></td><td>0.02 <b>(-29.00%)</b></td><td>183.00 (-19.81%)</td><td>156.08 (-9.97%)</td><td>151.90 (-10.01%)</td><td>124.40 (-0.32%)</td><td>24.61 <b>(-42.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>228.20 (n/a)</td><td>173.36 (n/a)</td><td>168.80 (n/a)</td><td>124.80 (n/a)</td><td>42.64 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 <b>(-27.51%)</b></td><td>0.09 <b>(-20.96%)</b></td><td>0.09 (-9.74%)</td><td>0.05 <b>(-38.70%)</b></td><td>0.03 (-19.78%)</td><td>342.20 <b>(+63.11%)</b></td><td>206.90 <b>(+30.52%)</b></td><td>176.10 (+10.82%)</td><td>138.70 <b>(+37.87%)</b></td><td>81.23 <b>(+86.50%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>209.80 (n/a)</td><td>158.52 (n/a)</td><td>158.90 (n/a)</td><td>100.60 (n/a)</td><td>43.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 <b>(-25.78%)</b></td><td>0.09 (-12.53%)</td><td>0.10 (-4.82%)</td><td>0.07 (-4.83%)</td><td>0.01 <b>(-54.64%)</b></td><td>227.50 (+5.08%)</td><td>183.42 (+10.99%)</td><td>172.40 (+5.06%)</td><td>165.60 <b>(+34.74%)</b></td><td>25.27 <b>(-33.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>165.26 (n/a)</td><td>164.10 (n/a)</td><td>122.90 (n/a)</td><td>38.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (+0.33%)</td><td>0.10 (+9.71%)</td><td>0.09 (+6.32%)</td><td>0.08 <b>(+20.64%)</b></td><td>0.02 (-12.08%)</td><td>196.70 (-17.11%)</td><td>163.38 (-10.11%)</td><td>174.10 (-5.94%)</td><td>128.80 (-0.31%)</td><td>28.77 <b>(-27.64%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>237.30 (n/a)</td><td>181.76 (n/a)</td><td>185.10 (n/a)</td><td>129.20 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 (+11.93%)</td><td>0.09 (+7.67%)</td><td>0.09 (-7.88%)</td><td>0.07 <b>(+20.65%)</b></td><td>0.02 (-17.21%)</td><td>223.90 (-17.14%)</td><td>181.98 (-9.34%)</td><td>189.00 (+8.56%)</td><td>139.40 (-10.64%)</td><td>31.03 <b>(-39.42%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>270.20 (n/a)</td><td>200.72 (n/a)</td><td>174.10 (n/a)</td><td>156.00 (n/a)</td><td>51.22 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.11 (-5.42%)</td><td>0.09 (-11.56%)</td><td>0.08 <b>(-23.26%)</b></td><td>0.07 (+1.87%)</td><td>0.02 (-12.71%)</td><td>247.80 (-1.86%)</td><td>197.14 (+11.92%)</td><td>207.80 <b>(+30.28%)</b></td><td>149.50 (+5.73%)</td><td>39.29 (-12.73%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>252.50 (n/a)</td><td>176.14 (n/a)</td><td>159.50 (n/a)</td><td>141.40 (n/a)</td><td>45.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (-10.52%)</td><td>0.19 (-5.07%)</td><td>0.19 (-7.27%)</td><td>0.18 (+3.95%)</td><td>0.02 <b>(-36.86%)</b></td><td>185.90 (-3.78%)</td><td>170.10 (+3.69%)</td><td>173.20 (+7.85%)</td><td>138.40 (+11.70%)</td><td>19.24 <b>(-34.07%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>193.20 (n/a)</td><td>164.04 (n/a)</td><td>160.60 (n/a)</td><td>123.90 (n/a)</td><td>29.18 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 (+2.75%)</td><td>0.21 (+9.76%)</td><td>0.23 <b>(+31.57%)</b></td><td>0.15 (-5.61%)</td><td>0.05 <b>(+38.55%)</b></td><td>222.90 (+5.99%)</td><td>166.24 (-6.34%)</td><td>141.00 <b>(-23.99%)</b></td><td>128.00 (-2.66%)</td><td>45.15 <b>(+44.66%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.30 (n/a)</td><td>177.50 (n/a)</td><td>185.50 (n/a)</td><td>131.50 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 <b>(-20.34%)</b></td><td>0.14 (-4.36%)</td><td>0.14 (+3.76%)</td><td>0.10 (-11.48%)</td><td>0.02 <b>(-29.32%)</b></td><td>323.50 (+12.99%)</td><td>241.46 (+3.78%)</td><td>227.40 (-3.60%)</td><td>210.50 <b>(+25.52%)</b></td><td>46.43 (+6.20%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>286.30 (n/a)</td><td>232.66 (n/a)</td><td>235.90 (n/a)</td><td>167.70 (n/a)</td><td>43.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 <b>(+29.73%)</b></td><td>0.15 (-0.84%)</td><td>0.15 (-0.77%)</td><td>0.11 <b>(-21.40%)</b></td><td>0.04 <b>(+229.83%)</b></td><td>307.80 <b>(+27.24%)</b></td><td>227.96 (+5.97%)</td><td>213.80 (+0.75%)</td><td>151.20 <b>(-22.94%)</b></td><td>57.96 <b>(+219.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>241.90 (n/a)</td><td>215.12 (n/a)</td><td>212.20 (n/a)</td><td>196.20 (n/a)</td><td>18.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (-4.95%)</td><td>0.19 (+1.74%)</td><td>0.18 (+2.29%)</td><td>0.15 (-5.40%)</td><td>0.04 (+8.46%)</td><td>213.60 (+5.69%)</td><td>176.68 (-0.95%)</td><td>182.80 (-2.25%)</td><td>138.20 (+5.26%)</td><td>33.86 <b>(+23.77%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>202.10 (n/a)</td><td>178.38 (n/a)</td><td>187.00 (n/a)</td><td>131.30 (n/a)</td><td>27.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (-5.70%)</td><td>0.20 (-0.75%)</td><td>0.20 (+4.67%)</td><td>0.16 (-11.55%)</td><td>0.03 (+9.84%)</td><td>207.00 (+13.05%)</td><td>164.94 (+1.45%)</td><td>160.60 (-4.46%)</td><td>136.10 (+6.00%)</td><td>27.88 <b>(+36.52%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.10 (n/a)</td><td>162.58 (n/a)</td><td>168.10 (n/a)</td><td>128.40 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 (-10.77%)</td><td>0.19 (+8.41%)</td><td>0.19 (+16.37%)</td><td>0.15 (+6.56%)</td><td>0.03 <b>(-37.75%)</b></td><td>216.60 (-6.15%)</td><td>173.78 (-9.71%)</td><td>168.70 (-14.06%)</td><td>145.90 (+12.06%)</td><td>26.41 <b>(-29.79%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>230.80 (n/a)</td><td>192.46 (n/a)</td><td>196.30 (n/a)</td><td>130.20 (n/a)</td><td>37.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.23 (-9.38%)</td><td>0.20 (+7.03%)</td><td>0.21 (+14.57%)</td><td>0.17 (+16.16%)</td><td>0.02 <b>(-41.73%)</b></td><td>196.50 (-13.93%)</td><td>162.34 (-8.75%)</td><td>158.10 (-12.70%)</td><td>139.50 (+10.28%)</td><td>21.02 <b>(-42.08%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>228.30 (n/a)</td><td>177.90 (n/a)</td><td>181.10 (n/a)</td><td>126.50 (n/a)</td><td>36.29 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.25 (-2.44%)</td><td>0.20 (+11.80%)</td><td>0.19 (+16.54%)</td><td>0.16 (+13.27%)</td><td>0.03 <b>(-20.73%)</b></td><td>200.00 (-11.74%)</td><td>168.36 (-11.87%)</td><td>171.80 (-14.19%)</td><td>133.40 (+2.54%)</td><td>27.44 <b>(-25.35%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>226.60 (n/a)</td><td>191.04 (n/a)</td><td>200.20 (n/a)</td><td>130.10 (n/a)</td><td>36.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.34 <b>(+51.41%)</b></td><td>0.23 <b>(+40.05%)</b></td><td>0.19 (+13.01%)</td><td>0.17 <b>(+90.36%)</b></td><td>0.07 <b>(+51.67%)</b></td><td>195.80 <b>(-47.48%)</b></td><td>155.08 <b>(-30.04%)</b></td><td>169.10 (-11.51%)</td><td>97.70 <b>(-33.94%)</b></td><td>43.39 <b>(-50.25%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>372.80 (n/a)</td><td>221.68 (n/a)</td><td>191.10 (n/a)</td><td>147.90 (n/a)</td><td>87.22 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.20 <b>(-22.11%)</b></td><td>0.17 (-15.80%)</td><td>0.18 (-3.00%)</td><td>0.10 <b>(-39.27%)</b></td><td>0.04 (+10.05%)</td><td>324.40 <b>(+64.67%)</b></td><td>205.72 <b>(+23.35%)</b></td><td>182.80 (+3.10%)</td><td>167.50 <b>(+28.35%)</b></td><td>66.71 <b>(+142.34%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.00 (n/a)</td><td>166.78 (n/a)</td><td>177.30 (n/a)</td><td>130.50 (n/a)</td><td>27.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.21 (-15.31%)</td><td>0.18 (-10.66%)</td><td>0.21 (+6.50%)</td><td>0.09 <b>(-43.53%)</b></td><td>0.05 <b>(+43.26%)</b></td><td>361.10 <b>(+77.10%)</b></td><td>202.48 <b>(+21.27%)</b></td><td>156.80 (-6.11%)</td><td>156.00 (+18.09%)</td><td>89.35 <b>(+203.63%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>203.90 (n/a)</td><td>166.96 (n/a)</td><td>167.00 (n/a)</td><td>132.10 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (+11.46%)</td><td>0.18 (+0.68%)</td><td>0.16 (-16.43%)</td><td>0.15 (+19.41%)</td><td>0.04 (+6.47%)</td><td>222.30 (-16.24%)</td><td>188.06 (-1.20%)</td><td>206.90 (+19.66%)</td><td>136.30 (-10.27%)</td><td>38.07 (-18.76%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>265.40 (n/a)</td><td>190.34 (n/a)</td><td>172.90 (n/a)</td><td>151.90 (n/a)</td><td>46.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (+3.61%)</td><td>0.19 (-3.76%)</td><td>0.18 <b>(-21.74%)</b></td><td>0.16 (+18.61%)</td><td>0.03 <b>(-33.12%)</b></td><td>206.40 (-15.69%)</td><td>179.68 (+0.62%)</td><td>186.50 <b>(+27.74%)</b></td><td>138.20 (-3.49%)</td><td>25.83 <b>(-45.35%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>244.80 (n/a)</td><td>178.58 (n/a)</td><td>146.00 (n/a)</td><td>143.20 (n/a)</td><td>47.27 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 <b>(+38.70%)</b></td><td>0.20 <b>(+35.88%)</b></td><td>0.19 <b>(+23.81%)</b></td><td>0.17 <b>(+60.87%)</b></td><td>0.03 (+11.20%)</td><td>194.40 <b>(-37.85%)</b></td><td>167.80 <b>(-27.68%)</b></td><td>169.50 (-19.25%)</td><td>127.90 <b>(-27.94%)</b></td><td>24.90 <b>(-52.42%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>312.80 (n/a)</td><td>232.02 (n/a)</td><td>209.90 (n/a)</td><td>177.50 (n/a)</td><td>52.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 (+1.18%)</td><td>0.21 (+3.75%)</td><td>0.19 (-1.03%)</td><td>0.17 (+5.70%)</td><td>0.04 (+10.53%)</td><td>188.60 (-5.42%)</td><td>163.34 (-3.26%)</td><td>175.50 (+1.04%)</td><td>128.50 (-1.15%)</td><td>27.36 (+6.19%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.40 (n/a)</td><td>168.84 (n/a)</td><td>173.70 (n/a)</td><td>130.00 (n/a)</td><td>25.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (+0.35%)</td><td>0.16 (+0.10%)</td><td>0.16 (+0.03%)</td><td>0.16 (-0.04%)</td><td>0.00 <b>(+126.88%)</b></td><td>52635.20 (+0.04%)</td><td>52513.10 (-0.10%)</td><td>52556.30 (-0.03%)</td><td>52293.40 (-0.34%)</td><td>130.13 <b>(+126.09%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52614.80 (n/a)</td><td>52567.40 (n/a)</td><td>52572.20 (n/a)</td><td>52474.10 (n/a)</td><td>57.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52751.30 (n/a)</td><td>52585.48 (n/a)</td><td>52537.90 (n/a)</td><td>52527.90 (n/a)</td><td>94.58 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>416040.60 (n/a)</td><td>415716.48 (n/a)</td><td>415743.60 (n/a)</td><td>415443.60 (n/a)</td><td>228.75 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.18 (-9.11%)</td><td>0.16 (-11.55%)</td><td>0.17 (-6.31%)</td><td>0.11 <b>(-25.61%)</b></td><td>0.03 <b>(+46.65%)</b></td><td>214.80 <b>(+34.42%)</b></td><td>154.62 (+15.46%)</td><td>140.40 (+6.69%)</td><td>133.70 (+10.04%)</td><td>33.87 <b>(+121.14%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>159.80 (n/a)</td><td>133.92 (n/a)</td><td>131.60 (n/a)</td><td>121.50 (n/a)</td><td>15.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.39 (-6.90%)</td><td>0.29 (-14.20%)</td><td>0.27 (-15.20%)</td><td>0.25 (-9.11%)</td><td>0.06 (-1.90%)</td><td>195.10 (+10.04%)</td><td>175.60 (+16.86%)</td><td>182.70 (+17.95%)</td><td>126.60 (+7.47%)</td><td>28.09 (+13.32%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>177.30 (n/a)</td><td>150.26 (n/a)</td><td>154.90 (n/a)</td><td>117.80 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>13.17 (-1.76%)</td><td>12.90 (-0.79%)</td><td>13.00 (+0.51%)</td><td>12.49 (-1.18%)</td><td>0.31 (+5.19%)</td><td>839.60 (+1.19%)</td><td>813.10 (+0.81%)</td><td>806.60 (-0.51%)</td><td>796.10 (+1.79%)</td><td>19.40 (+8.31%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>13.41 (n/a)</td><td>13.01 (n/a)</td><td>12.93 (n/a)</td><td>12.64 (n/a)</td><td>0.29 (n/a)</td><td>829.70 (n/a)</td><td>806.60 (n/a)</td><td>810.70 (n/a)</td><td>782.10 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 <b>(-22.85%)</b></td><td>0.22 (-11.52%)</td><td>0.23 (-4.40%)</td><td>0.17 (-12.81%)</td><td>0.04 <b>(-31.93%)</b></td><td>242.60 (+14.70%)</td><td>186.50 (+11.96%)</td><td>178.60 (+4.63%)</td><td>157.00 <b>(+29.64%)</b></td><td>34.26 (+3.77%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>211.50 (n/a)</td><td>166.58 (n/a)</td><td>170.70 (n/a)</td><td>121.10 (n/a)</td><td>33.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-4.93%)</td><td>0.03 (+8.60%)</td><td>0.03 (+0.97%)</td><td>0.03 <b>(+45.96%)</b></td><td>0.00 <b>(-54.33%)</b></td><td>199.60 <b>(-31.48%)</b></td><td>176.22 (-11.76%)</td><td>178.80 (-0.94%)</td><td>155.50 (+5.21%)</td><td>17.04 <b>(-68.68%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>291.30 (n/a)</td><td>199.70 (n/a)</td><td>180.50 (n/a)</td><td>147.80 (n/a)</td><td>54.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 <b>(+46.83%)</b></td><td>0.03 <b>(+22.37%)</b></td><td>0.03 <b>(+25.18%)</b></td><td>0.02 (+4.27%)</td><td>0.01 <b>(+148.16%)</b></td><td>213.50 (-4.09%)</td><td>161.20 (-13.49%)</td><td>147.80 <b>(-20.11%)</b></td><td>101.60 <b>(-31.90%)</b></td><td>47.80 <b>(+69.63%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.60 (n/a)</td><td>186.34 (n/a)</td><td>185.00 (n/a)</td><td>149.20 (n/a)</td><td>28.18 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (-13.00%)</td><td>0.04 (+5.76%)</td><td>0.04 (+2.24%)</td><td>0.03 <b>(+32.56%)</b></td><td>0.00 <b>(-53.06%)</b></td><td>179.30 <b>(-24.57%)</b></td><td>161.32 (-10.07%)</td><td>170.80 (-2.18%)</td><td>139.90 (+14.95%)</td><td>19.34 <b>(-60.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>179.38 (n/a)</td><td>174.60 (n/a)</td><td>121.70 (n/a)</td><td>48.82 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (+2.85%)</td><td>0.03 <b>(+23.73%)</b></td><td>0.03 <b>(+25.90%)</b></td><td>0.02 <b>(+39.15%)</b></td><td>0.01 (-18.51%)</td><td>201.20 <b>(-28.12%)</b></td><td>148.72 <b>(-22.31%)</b></td><td>143.50 <b>(-20.59%)</b></td><td>112.90 (-2.84%)</td><td>34.33 <b>(-41.72%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>279.90 (n/a)</td><td>191.42 (n/a)</td><td>180.70 (n/a)</td><td>116.20 (n/a)</td><td>58.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 <b>(+30.41%)</b></td><td>0.03 (+11.94%)</td><td>0.03 (+5.53%)</td><td>0.02 (+4.24%)</td><td>0.01 <b>(+83.85%)</b></td><td>231.30 (-4.06%)</td><td>178.14 (-8.19%)</td><td>175.40 (-5.24%)</td><td>121.40 <b>(-23.36%)</b></td><td>41.43 <b>(+32.13%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.10 (n/a)</td><td>194.04 (n/a)</td><td>185.10 (n/a)</td><td>158.40 (n/a)</td><td>31.35 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 <b>(-20.37%)</b></td><td>0.02 (-10.02%)</td><td>0.02 (-13.48%)</td><td>0.02 (+18.33%)</td><td>0.01 <b>(-36.35%)</b></td><td>255.00 (-15.48%)</td><td>191.64 (+4.07%)</td><td>203.00 (+15.60%)</td><td>133.10 <b>(+25.57%)</b></td><td>48.54 <b>(-34.45%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>301.70 (n/a)</td><td>184.14 (n/a)</td><td>175.60 (n/a)</td><td>106.00 (n/a)</td><td>74.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (-14.07%)</td><td>0.03 (+10.11%)</td><td>0.03 (+3.47%)</td><td>0.03 <b>(+28.61%)</b></td><td>0.00 <b>(-51.78%)</b></td><td>188.10 <b>(-22.27%)</b></td><td>159.48 (-14.64%)</td><td>163.20 (-3.37%)</td><td>132.40 (+16.34%)</td><td>22.65 <b>(-58.78%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.00 (n/a)</td><td>186.84 (n/a)</td><td>168.90 (n/a)</td><td>113.80 (n/a)</td><td>54.94 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+0.51%)</td><td>0.02 (-1.95%)</td><td>0.02 (-11.13%)</td><td>0.02 (+2.78%)</td><td>0.01 (-3.10%)</td><td>203.90 (-2.67%)</td><td>173.08 (+1.55%)</td><td>189.30 (+12.54%)</td><td>124.10 (-0.56%)</td><td>35.86 (-7.41%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>170.44 (n/a)</td><td>168.20 (n/a)</td><td>124.80 (n/a)</td><td>38.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 <b>(+28.08%)</b></td><td>0.03 (+4.93%)</td><td>0.02 (-5.03%)</td><td>0.02 (-1.48%)</td><td>0.01 <b>(+146.94%)</b></td><td>219.20 (+1.48%)</td><td>182.86 (-2.59%)</td><td>194.10 (+5.26%)</td><td>134.30 <b>(-21.92%)</b></td><td>32.20 <b>(+88.60%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.00 (n/a)</td><td>187.72 (n/a)</td><td>184.40 (n/a)</td><td>172.00 (n/a)</td><td>17.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-14.94%)</td><td>0.02 (-1.14%)</td><td>0.03 (+10.83%)</td><td>0.02 (+5.40%)</td><td>0.00 <b>(-33.95%)</b></td><td>207.20 (-5.13%)</td><td>175.24 (-0.80%)</td><td>163.70 (-9.76%)</td><td>147.80 (+17.49%)</td><td>28.18 <b>(-24.85%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>176.66 (n/a)</td><td>181.40 (n/a)</td><td>125.80 (n/a)</td><td>37.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-5.85%)</td><td>0.03 (+3.83%)</td><td>0.03 (+7.77%)</td><td>0.02 (-11.89%)</td><td>0.01 (+6.06%)</td><td>263.70 (+13.47%)</td><td>177.50 (-2.39%)</td><td>160.70 (-7.22%)</td><td>145.30 (+6.21%)</td><td>48.62 <b>(+33.59%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.40 (n/a)</td><td>181.84 (n/a)</td><td>173.20 (n/a)</td><td>136.80 (n/a)</td><td>36.39 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (+13.17%)</td><td>0.03 (+18.42%)</td><td>0.03 (+10.89%)</td><td>0.02 (+18.50%)</td><td>0.01 (-4.38%)</td><td>196.90 (-15.64%)</td><td>154.10 (-16.77%)</td><td>154.30 (-9.82%)</td><td>115.70 (-11.61%)</td><td>28.93 <b>(-30.62%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.40 (n/a)</td><td>185.14 (n/a)</td><td>171.10 (n/a)</td><td>130.90 (n/a)</td><td>41.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+2.98%)</td><td>0.02 (-3.55%)</td><td>0.02 (+12.47%)</td><td>0.01 <b>(-31.11%)</b></td><td>0.01 <b>(+103.83%)</b></td><td>300.80 <b>(+45.10%)</b></td><td>208.78 (+8.09%)</td><td>183.00 (-11.08%)</td><td>158.40 (-2.88%)</td><td>56.68 <b>(+190.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.30 (n/a)</td><td>193.16 (n/a)</td><td>205.80 (n/a)</td><td>163.10 (n/a)</td><td>19.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 <b>(+35.81%)</b></td><td>0.03 (+14.03%)</td><td>0.02 (+12.86%)</td><td>0.02 (-6.82%)</td><td>0.01 <b>(+87.74%)</b></td><td>240.10 (+7.33%)</td><td>172.36 (-9.10%)</td><td>173.20 (-11.41%)</td><td>116.50 <b>(-26.41%)</b></td><td>45.85 <b>(+52.00%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.70 (n/a)</td><td>189.62 (n/a)</td><td>195.50 (n/a)</td><td>158.30 (n/a)</td><td>30.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+4.64%)</td><td>0.02 (+7.97%)</td><td>0.03 <b>(+27.06%)</b></td><td>0.01 <b>(-28.46%)</b></td><td>0.01 <b>(+87.67%)</b></td><td>303.60 <b>(+39.78%)</b></td><td>187.82 (-2.34%)</td><td>160.30 <b>(-21.31%)</b></td><td>154.30 (-4.46%)</td><td>64.78 <b>(+158.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.20 (n/a)</td><td>192.32 (n/a)</td><td>203.70 (n/a)</td><td>161.50 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.02 (+0.42%)</td><td>0.02 (+1.73%)</td><td>0.02 (-5.03%)</td><td>0.02 (+8.92%)</td><td>0.00 (-15.62%)</td><td>236.90 (-8.18%)</td><td>219.96 (-2.27%)</td><td>230.60 (+5.30%)</td><td>179.20 (-0.39%)</td><td>23.75 <b>(-24.31%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.00 (n/a)</td><td>225.08 (n/a)</td><td>219.00 (n/a)</td><td>179.90 (n/a)</td><td>31.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-10.28%)</td><td>0.05 (-12.56%)</td><td>0.05 (-19.54%)</td><td>0.04 (-1.61%)</td><td>0.01 <b>(-30.40%)</b></td><td>186.40 (+1.64%)</td><td>162.00 (+13.16%)</td><td>162.30 <b>(+24.27%)</b></td><td>133.30 (+11.45%)</td><td>19.54 <b>(-23.15%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>143.16 (n/a)</td><td>130.60 (n/a)</td><td>119.60 (n/a)</td><td>25.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 <b>(+38.99%)</b></td><td>0.08 <b>(+41.54%)</b></td><td>0.08 <b>(+26.83%)</b></td><td>0.07 <b>(+95.58%)</b></td><td>0.01 (-13.96%)</td><td>176.50 <b>(-48.87%)</b></td><td>147.90 <b>(-32.52%)</b></td><td>153.60 <b>(-21.19%)</b></td><td>125.40 <b>(-28.10%)</b></td><td>21.06 <b>(-70.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>345.20 (n/a)</td><td>219.16 (n/a)</td><td>194.90 (n/a)</td><td>174.40 (n/a)</td><td>71.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-10.72%)</td><td>0.05 (-9.54%)</td><td>0.05 <b>(-20.19%)</b></td><td>0.05 (+0.89%)</td><td>0.01 <b>(-31.81%)</b></td><td>181.00 (-0.88%)</td><td>161.26 (+9.20%)</td><td>169.30 <b>(+25.31%)</b></td><td>132.40 (+12.01%)</td><td>19.64 <b>(-25.94%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>147.68 (n/a)</td><td>135.10 (n/a)</td><td>118.20 (n/a)</td><td>26.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (+4.32%)</td><td>0.08 <b>(+29.55%)</b></td><td>0.08 <b>(+29.31%)</b></td><td>0.06 <b>(+110.30%)</b></td><td>0.01 <b>(-51.89%)</b></td><td>170.30 <b>(-52.46%)</b></td><td>138.12 <b>(-31.22%)</b></td><td>132.00 <b>(-22.67%)</b></td><td>118.60 (-4.20%)</td><td>19.60 <b>(-78.78%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>358.20 (n/a)</td><td>200.82 (n/a)</td><td>170.70 (n/a)</td><td>123.80 (n/a)</td><td>92.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 <b>(-23.39%)</b></td><td>0.04 <b>(-20.21%)</b></td><td>0.04 <b>(-21.37%)</b></td><td>0.04 <b>(-22.39%)</b></td><td>0.01 <b>(-24.03%)</b></td><td>216.00 <b>(+28.80%)</b></td><td>186.26 <b>(+25.29%)</b></td><td>186.70 <b>(+27.18%)</b></td><td>159.20 <b>(+30.49%)</b></td><td>22.63 <b>(+28.18%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.70 (n/a)</td><td>148.66 (n/a)</td><td>146.80 (n/a)</td><td>122.00 (n/a)</td><td>17.65 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 (+5.45%)</td><td>0.07 (-0.05%)</td><td>0.06 (-4.00%)</td><td>0.05 (-4.64%)</td><td>0.01 <b>(+26.97%)</b></td><td>190.90 (+4.89%)</td><td>160.84 (+0.87%)</td><td>166.00 (+4.14%)</td><td>121.50 (-5.15%)</td><td>25.36 <b>(+24.31%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>182.00 (n/a)</td><td>159.46 (n/a)</td><td>159.40 (n/a)</td><td>128.10 (n/a)</td><td>20.40 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (+10.43%)</td><td>0.04 (-8.17%)</td><td>0.04 (-4.57%)</td><td>0.02 <b>(-38.70%)</b></td><td>0.01 <b>(+131.58%)</b></td><td>336.80 <b>(+63.10%)</b></td><td>210.54 (+17.82%)</td><td>183.10 (+4.81%)</td><td>136.30 (-9.44%)</td><td>76.86 <b>(+254.34%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>178.70 (n/a)</td><td>174.70 (n/a)</td><td>150.50 (n/a)</td><td>21.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.07 (+0.61%)</td><td>0.06 (+3.30%)</td><td>0.06 (+15.20%)</td><td>0.05 (+5.23%)</td><td>0.01 (-3.31%)</td><td>202.00 (-4.99%)</td><td>164.02 (-3.44%)</td><td>150.50 (-13.21%)</td><td>130.00 (-0.61%)</td><td>33.97 (-4.12%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>169.86 (n/a)</td><td>173.40 (n/a)</td><td>130.80 (n/a)</td><td>35.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (+8.89%)</td><td>0.05 (-9.50%)</td><td>0.05 (-13.99%)</td><td>0.04 <b>(-22.99%)</b></td><td>0.01 <b>(+116.94%)</b></td><td>230.00 <b>(+29.87%)</b></td><td>180.34 (+13.35%)</td><td>182.00 (+16.22%)</td><td>133.10 (-8.14%)</td><td>35.03 <b>(+156.35%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.10 (n/a)</td><td>159.10 (n/a)</td><td>156.60 (n/a)</td><td>144.90 (n/a)</td><td>13.67 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.08 <b>(+23.20%)</b></td><td>0.06 (+17.92%)</td><td>0.05 (+1.20%)</td><td>0.04 <b>(+32.74%)</b></td><td>0.02 <b>(+44.28%)</b></td><td>220.50 <b>(-24.67%)</b></td><td>173.66 (-14.18%)</td><td>190.30 (-1.19%)</td><td>119.00 (-18.83%)</td><td>45.81 (-15.86%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.70 (n/a)</td><td>202.36 (n/a)</td><td>192.60 (n/a)</td><td>146.60 (n/a)</td><td>54.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-17.68%)</td><td>0.05 (-4.26%)</td><td>0.05 (+2.08%)</td><td>0.04 (+5.96%)</td><td>0.01 <b>(-41.48%)</b></td><td>209.60 (-5.63%)</td><td>181.28 (+2.07%)</td><td>175.00 (-2.02%)</td><td>146.40 <b>(+21.49%)</b></td><td>26.27 <b>(-28.45%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.10 (n/a)</td><td>177.60 (n/a)</td><td>178.60 (n/a)</td><td>120.50 (n/a)</td><td>36.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 <b>(+43.51%)</b></td><td>0.05 <b>(+27.06%)</b></td><td>0.05 (+16.88%)</td><td>0.04 <b>(+41.03%)</b></td><td>0.01 <b>(+28.07%)</b></td><td>219.40 <b>(-29.11%)</b></td><td>181.78 <b>(-21.70%)</b></td><td>179.50 (-14.44%)</td><td>143.00 <b>(-30.31%)</b></td><td>27.62 <b>(-37.87%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>309.50 (n/a)</td><td>232.16 (n/a)</td><td>209.80 (n/a)</td><td>205.20 (n/a)</td><td>44.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.06 (-5.07%)</td><td>0.04 (-8.42%)</td><td>0.04 (-11.40%)</td><td>0.04 (-4.06%)</td><td>0.01 (-0.39%)</td><td>219.00 (+4.19%)</td><td>186.36 (+9.31%)</td><td>191.30 (+12.86%)</td><td>145.00 (+5.38%)</td><td>28.12 (+7.02%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>170.48 (n/a)</td><td>169.50 (n/a)</td><td>137.60 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.05 <b>(+26.99%)</b></td><td>0.04 (+11.78%)</td><td>0.04 (+2.07%)</td><td>0.04 (+9.90%)</td><td>0.01 <b>(+150.48%)</b></td><td>224.80 (-8.99%)</td><td>199.74 (-9.49%)</td><td>211.00 (-2.04%)</td><td>166.60 <b>(-21.23%)</b></td><td>26.52 <b>(+78.34%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>247.00 (n/a)</td><td>220.68 (n/a)</td><td>215.40 (n/a)</td><td>211.50 (n/a)</td><td>14.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.04 (+4.48%)</td><td>0.04 (-6.34%)</td><td>0.04 (-8.32%)</td><td>0.03 (-12.32%)</td><td>0.00 <b>(+250.60%)</b></td><td>238.10 (+14.09%)</td><td>219.24 (+7.49%)</td><td>223.40 (+9.08%)</td><td>187.40 (-4.29%)</td><td>20.10 <b>(+280.35%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.70 (n/a)</td><td>203.96 (n/a)</td><td>204.80 (n/a)</td><td>195.80 (n/a)</td><td>5.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 <b>(+44.99%)</b></td><td>0.10 (+13.03%)</td><td>0.10 (+11.35%)</td><td>0.07 (+0.87%)</td><td>0.02 <b>(+221.49%)</b></td><td>218.60 (-0.86%)</td><td>176.72 (-8.61%)</td><td>171.40 (-10.21%)</td><td>123.40 <b>(-31.06%)</b></td><td>36.32 <b>(+116.71%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>193.36 (n/a)</td><td>190.90 (n/a)</td><td>179.00 (n/a)</td><td>16.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.18 (-3.98%)</td><td>0.14 (-4.58%)</td><td>0.13 (-6.15%)</td><td>0.12 (-4.05%)</td><td>0.02 (+7.88%)</td><td>210.50 (+4.26%)</td><td>177.92 (+5.34%)</td><td>185.90 (+6.53%)</td><td>140.10 (+4.16%)</td><td>29.64 (+17.88%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>201.90 (n/a)</td><td>168.90 (n/a)</td><td>174.50 (n/a)</td><td>134.50 (n/a)</td><td>25.14 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (+2.99%)</td><td>0.10 (+8.19%)</td><td>0.10 (+6.52%)</td><td>0.09 (+17.24%)</td><td>0.02 (-17.56%)</td><td>188.20 (-14.69%)</td><td>160.36 (-8.80%)</td><td>160.40 (-6.14%)</td><td>125.50 (-2.94%)</td><td>22.61 <b>(-32.53%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.60 (n/a)</td><td>175.84 (n/a)</td><td>170.90 (n/a)</td><td>129.30 (n/a)</td><td>33.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 (+15.13%)</td><td>0.13 (+14.41%)</td><td>0.14 <b>(+21.06%)</b></td><td>0.11 <b>(+27.90%)</b></td><td>0.02 (-0.18%)</td><td>187.60 <b>(-21.80%)</b></td><td>158.94 (-13.37%)</td><td>149.00 (-17.41%)</td><td>127.50 (-13.15%)</td><td>25.44 <b>(-30.45%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>239.90 (n/a)</td><td>183.48 (n/a)</td><td>180.40 (n/a)</td><td>146.80 (n/a)</td><td>36.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 (+6.60%)</td><td>0.08 (-1.71%)</td><td>0.08 (-4.15%)</td><td>0.06 (-17.20%)</td><td>0.01 <b>(+134.83%)</b></td><td>260.10 <b>(+20.75%)</b></td><td>205.22 (+3.55%)</td><td>202.90 (+4.32%)</td><td>170.20 (-6.17%)</td><td>34.63 <b>(+167.34%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>198.18 (n/a)</td><td>194.50 (n/a)</td><td>181.40 (n/a)</td><td>12.95 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (+7.48%)</td><td>0.13 (+1.16%)</td><td>0.12 (+16.75%)</td><td>0.09 (-11.85%)</td><td>0.03 (+13.66%)</td><td>220.10 (+13.40%)</td><td>169.94 (-0.31%)</td><td>164.30 (-14.34%)</td><td>120.70 (-6.94%)</td><td>36.39 (+15.21%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>194.10 (n/a)</td><td>170.46 (n/a)</td><td>191.80 (n/a)</td><td>129.70 (n/a)</td><td>31.58 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (-6.99%)</td><td>0.11 (+13.91%)</td><td>0.10 (+15.06%)</td><td>0.09 <b>(+21.75%)</b></td><td>0.02 <b>(-34.22%)</b></td><td>175.00 (-17.88%)</td><td>147.42 (-14.95%)</td><td>157.20 (-13.10%)</td><td>117.20 (+7.52%)</td><td>23.71 <b>(-39.54%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>213.10 (n/a)</td><td>173.34 (n/a)</td><td>180.90 (n/a)</td><td>109.00 (n/a)</td><td>39.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 (+10.31%)</td><td>0.11 (+0.42%)</td><td>0.11 (-8.19%)</td><td>0.10 (+13.86%)</td><td>0.02 (+1.20%)</td><td>183.50 (-12.16%)</td><td>166.12 (-0.98%)</td><td>174.60 (+8.92%)</td><td>121.90 (-9.37%)</td><td>25.45 <b>(-20.90%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>208.90 (n/a)</td><td>167.76 (n/a)</td><td>160.30 (n/a)</td><td>134.50 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 <b>(+43.68%)</b></td><td>0.10 <b>(+20.89%)</b></td><td>0.10 (+17.60%)</td><td>0.08 <b>(+28.47%)</b></td><td>0.02 <b>(+69.97%)</b></td><td>199.80 <b>(-22.17%)</b></td><td>166.04 (-16.26%)</td><td>161.00 (-14.95%)</td><td>117.40 <b>(-30.41%)</b></td><td>32.49 (-8.84%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>256.70 (n/a)</td><td>198.28 (n/a)</td><td>189.30 (n/a)</td><td>168.70 (n/a)</td><td>35.64 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 (+7.64%)</td><td>0.09 (-17.86%)</td><td>0.08 <b>(-36.01%)</b></td><td>0.06 <b>(-31.59%)</b></td><td>0.04 <b>(+64.79%)</b></td><td>326.10 <b>(+46.17%)</b></td><td>224.44 <b>(+32.82%)</b></td><td>242.70 <b>(+56.28%)</b></td><td>123.10 (-7.16%)</td><td>81.92 <b>(+118.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>223.10 (n/a)</td><td>168.98 (n/a)</td><td>155.30 (n/a)</td><td>132.60 (n/a)</td><td>37.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (-4.81%)</td><td>0.09 (+8.64%)</td><td>0.09 <b>(+26.84%)</b></td><td>0.06 (-14.16%)</td><td>0.03 (-4.94%)</td><td>291.80 (+16.49%)</td><td>187.02 (-7.17%)</td><td>172.50 <b>(-21.16%)</b></td><td>130.80 (+4.98%)</td><td>62.61 <b>(+21.41%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>250.50 (n/a)</td><td>201.46 (n/a)</td><td>218.80 (n/a)</td><td>124.60 (n/a)</td><td>51.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 (-6.56%)</td><td>0.08 (-10.19%)</td><td>0.09 (-5.00%)</td><td>0.07 (-13.33%)</td><td>0.01 (+9.06%)</td><td>263.80 (+15.35%)</td><td>216.88 (+12.12%)</td><td>203.40 (+5.28%)</td><td>172.80 (+7.00%)</td><td>35.72 <b>(+36.12%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>193.44 (n/a)</td><td>193.20 (n/a)</td><td>161.50 (n/a)</td><td>26.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (+9.90%)</td><td>0.09 (+1.11%)</td><td>0.09 (+2.61%)</td><td>0.08 (-0.16%)</td><td>0.02 <b>(+27.96%)</b></td><td>213.90 (+0.19%)</td><td>181.22 (+0.13%)</td><td>190.90 (-2.55%)</td><td>122.80 (-8.97%)</td><td>35.95 (+15.07%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.50 (n/a)</td><td>180.98 (n/a)</td><td>195.90 (n/a)</td><td>134.90 (n/a)</td><td>31.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 <b>(+30.12%)</b></td><td>0.09 (-1.22%)</td><td>0.09 (+1.66%)</td><td>0.05 <b>(-33.89%)</b></td><td>0.03 <b>(+252.74%)</b></td><td>326.70 <b>(+51.25%)</b></td><td>207.82 (+9.09%)</td><td>188.20 (-1.67%)</td><td>134.80 <b>(-23.15%)</b></td><td>71.24 <b>(+331.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>190.50 (n/a)</td><td>191.40 (n/a)</td><td>175.40 (n/a)</td><td>16.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.09 (-1.58%)</td><td>0.08 (+9.74%)</td><td>0.07 (+1.50%)</td><td>0.07 <b>(+36.57%)</b></td><td>0.01 <b>(-35.99%)</b></td><td>240.40 <b>(-26.77%)</b></td><td>210.30 (-11.58%)</td><td>222.10 (-1.46%)</td><td>174.90 (+1.63%)</td><td>26.65 <b>(-53.57%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>328.30 (n/a)</td><td>237.84 (n/a)</td><td>225.40 (n/a)</td><td>172.10 (n/a)</td><td>57.40 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 (-6.72%)</td><td>0.20 (-2.39%)</td><td>0.20 (+3.39%)</td><td>0.15 (-9.92%)</td><td>0.04 (-5.70%)</td><td>221.30 (+11.04%)</td><td>167.92 (+2.75%)</td><td>160.40 (-3.26%)</td><td>124.10 (+7.17%)</td><td>36.22 (+16.40%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>199.30 (n/a)</td><td>163.42 (n/a)</td><td>165.80 (n/a)</td><td>115.80 (n/a)</td><td>31.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.30 <b>(+36.54%)</b></td><td>0.22 (+9.15%)</td><td>0.20 (+5.27%)</td><td>0.19 (+2.11%)</td><td>0.05 <b>(+174.75%)</b></td><td>174.00 (-2.08%)</td><td>155.08 (-6.31%)</td><td>162.80 (-5.02%)</td><td>110.50 <b>(-26.77%)</b></td><td>25.76 <b>(+94.01%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>177.70 (n/a)</td><td>165.52 (n/a)</td><td>171.40 (n/a)</td><td>150.90 (n/a)</td><td>13.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.23 <b>(-20.91%)</b></td><td>0.21 (-8.20%)</td><td>0.23 (+4.37%)</td><td>0.19 (-3.22%)</td><td>0.02 <b>(-48.49%)</b></td><td>214.80 (+3.32%)</td><td>192.26 (+7.48%)</td><td>180.80 (-4.19%)</td><td>176.20 <b>(+26.40%)</b></td><td>18.75 <b>(-32.02%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>207.90 (n/a)</td><td>178.88 (n/a)</td><td>188.70 (n/a)</td><td>139.40 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 (+1.47%)</td><td>0.19 (-6.89%)</td><td>0.18 (-11.36%)</td><td>0.17 (+3.97%)</td><td>0.02 (-5.22%)</td><td>196.40 (-3.82%)</td><td>177.88 (+7.16%)</td><td>182.70 (+12.78%)</td><td>146.20 (-1.48%)</td><td>19.58 (-12.63%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.20 (n/a)</td><td>166.00 (n/a)</td><td>162.00 (n/a)</td><td>148.40 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.33 (+8.55%)</td><td>0.25 (+10.13%)</td><td>0.26 (+18.90%)</td><td>0.19 (+6.21%)</td><td>0.05 (+12.18%)</td><td>217.00 (-5.86%)</td><td>169.68 (-8.84%)</td><td>159.00 (-15.92%)</td><td>124.70 (-7.83%)</td><td>36.54 (-0.71%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>230.50 (n/a)</td><td>186.14 (n/a)</td><td>189.10 (n/a)</td><td>135.30 (n/a)</td><td>36.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.27 (-2.29%)</td><td>0.23 <b>(+22.18%)</b></td><td>0.23 <b>(+34.23%)</b></td><td>0.19 <b>(+51.85%)</b></td><td>0.04 <b>(-37.56%)</b></td><td>173.00 <b>(-34.17%)</b></td><td>148.44 <b>(-21.83%)</b></td><td>140.70 <b>(-25.48%)</b></td><td>120.60 (+2.38%)</td><td>23.26 <b>(-54.77%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>262.80 (n/a)</td><td>189.90 (n/a)</td><td>188.80 (n/a)</td><td>117.80 (n/a)</td><td>51.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.28 <b>(+28.99%)</b></td><td>0.21 (+2.56%)</td><td>0.22 (+1.46%)</td><td>0.15 (-7.65%)</td><td>0.05 <b>(+122.03%)</b></td><td>240.40 (+8.29%)</td><td>182.54 (+1.04%)</td><td>166.60 (-1.48%)</td><td>129.80 <b>(-22.46%)</b></td><td>44.22 <b>(+88.41%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>222.00 (n/a)</td><td>180.66 (n/a)</td><td>169.10 (n/a)</td><td>167.40 (n/a)</td><td>23.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.27 <b>(+38.47%)</b></td><td>0.22 <b>(+21.98%)</b></td><td>0.22 <b>(+20.53%)</b></td><td>0.14 (-11.07%)</td><td>0.05 <b>(+173.76%)</b></td><td>236.60 (+12.45%)</td><td>160.28 (-14.18%)</td><td>149.60 (-17.03%)</td><td>119.30 <b>(-27.78%)</b></td><td>45.82 <b>(+126.12%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.40 (n/a)</td><td>186.76 (n/a)</td><td>180.30 (n/a)</td><td>165.20 (n/a)</td><td>20.27 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.27 <b>(+29.50%)</b></td><td>0.20 (+6.57%)</td><td>0.19 (-1.17%)</td><td>0.16 (-7.59%)</td><td>0.05 <b>(+203.04%)</b></td><td>237.70 (+8.24%)</td><td>189.86 (-2.76%)</td><td>197.50 (+1.18%)</td><td>135.10 <b>(-22.80%)</b></td><td>41.21 <b>(+150.95%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>219.60 (n/a)</td><td>195.24 (n/a)</td><td>195.20 (n/a)</td><td>175.00 (n/a)</td><td>16.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.29 (+18.79%)</td><td>0.24 <b>(+39.06%)</b></td><td>0.22 <b>(+38.32%)</b></td><td>0.19 <b>(+40.40%)</b></td><td>0.04 (+0.46%)</td><td>173.40 <b>(-28.79%)</b></td><td>141.94 <b>(-29.22%)</b></td><td>149.40 <b>(-27.72%)</b></td><td>111.30 (-15.81%)</td><td>25.85 <b>(-37.75%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>243.50 (n/a)</td><td>200.54 (n/a)</td><td>206.70 (n/a)</td><td>132.20 (n/a)</td><td>41.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.21 (+16.91%)</td><td>0.18 (+15.38%)</td><td>0.17 (+10.40%)</td><td>0.16 (+19.45%)</td><td>0.03 <b>(+51.64%)</b></td><td>220.90 (-16.29%)</td><td>194.18 (-12.70%)</td><td>202.30 (-9.40%)</td><td>163.30 (-14.46%)</td><td>28.86 (+6.72%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>263.90 (n/a)</td><td>222.44 (n/a)</td><td>223.30 (n/a)</td><td>190.90 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.23 (+8.21%)</td><td>0.21 (+19.89%)</td><td>0.21 <b>(+34.81%)</b></td><td>0.18 <b>(+30.32%)</b></td><td>0.02 <b>(-44.51%)</b></td><td>180.90 <b>(-23.28%)</b></td><td>158.98 (-18.14%)</td><td>153.60 <b>(-25.80%)</b></td><td>145.00 (-7.58%)</td><td>13.65 <b>(-59.12%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>235.80 (n/a)</td><td>194.20 (n/a)</td><td>207.00 (n/a)</td><td>156.90 (n/a)</td><td>33.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.21 (+0.43%)</td><td>0.18 (+0.94%)</td><td>0.16 (-3.16%)</td><td>0.15 (+8.38%)</td><td>0.03 (-5.82%)</td><td>225.50 (-7.73%)</td><td>198.74 (-1.30%)</td><td>216.90 (+3.29%)</td><td>162.30 (-0.43%)</td><td>29.64 (-11.80%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>244.40 (n/a)</td><td>201.36 (n/a)</td><td>210.00 (n/a)</td><td>163.00 (n/a)</td><td>33.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.19 (+11.65%)</td><td>0.17 (+9.12%)</td><td>0.17 (+5.45%)</td><td>0.15 (+9.47%)</td><td>0.02 (+8.65%)</td><td>221.70 (-8.65%)</td><td>195.40 (-8.37%)</td><td>191.80 (-5.14%)</td><td>174.00 (-10.45%)</td><td>17.89 (-10.84%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>242.70 (n/a)</td><td>213.26 (n/a)</td><td>202.20 (n/a)</td><td>194.30 (n/a)</td><td>20.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (-17.37%)</td><td>0.11 (-2.60%)</td><td>0.11 (-7.36%)</td><td>0.09 <b>(+58.30%)</b></td><td>0.02 <b>(-59.62%)</b></td><td>221.20 <b>(-36.82%)</b></td><td>181.14 (-7.42%)</td><td>181.20 (+7.99%)</td><td>152.50 <b>(+21.03%)</b></td><td>25.53 <b>(-71.17%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>350.10 (n/a)</td><td>195.66 (n/a)</td><td>167.80 (n/a)</td><td>126.00 (n/a)</td><td>88.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (+1.14%)</td><td>0.14 (-2.84%)</td><td>0.14 (-4.59%)</td><td>0.09 (-18.21%)</td><td>0.03 (+15.61%)</td><td>227.90 <b>(+22.26%)</b></td><td>157.30 (+4.71%)</td><td>143.10 (+4.84%)</td><td>122.60 (-1.13%)</td><td>40.79 <b>(+46.54%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>186.40 (n/a)</td><td>150.22 (n/a)</td><td>136.50 (n/a)</td><td>124.00 (n/a)</td><td>27.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (+5.14%)</td><td>0.14 (+10.30%)</td><td>0.14 (+12.21%)</td><td>0.10 (+7.17%)</td><td>0.02 (-17.63%)</td><td>199.60 (-6.69%)</td><td>153.70 (-10.72%)</td><td>149.20 (-10.87%)</td><td>123.60 (-4.92%)</td><td>27.87 <b>(-26.08%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>213.90 (n/a)</td><td>172.16 (n/a)</td><td>167.40 (n/a)</td><td>130.00 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (-12.27%)</td><td>0.12 (-1.98%)</td><td>0.12 (+12.53%)</td><td>0.09 (-4.12%)</td><td>0.02 <b>(-33.26%)</b></td><td>225.10 (+4.26%)</td><td>175.96 (+0.26%)</td><td>171.40 (-11.15%)</td><td>148.90 (+14.01%)</td><td>30.06 (-18.60%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>215.90 (n/a)</td><td>175.50 (n/a)</td><td>192.90 (n/a)</td><td>130.60 (n/a)</td><td>36.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (+4.34%)</td><td>0.13 (+2.83%)</td><td>0.12 (-1.21%)</td><td>0.11 (+4.27%)</td><td>0.02 (+7.22%)</td><td>186.80 (-4.06%)</td><td>160.54 (-2.63%)</td><td>164.60 (+1.23%)</td><td>121.90 (-4.17%)</td><td>25.54 (-1.62%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>194.70 (n/a)</td><td>164.88 (n/a)</td><td>162.60 (n/a)</td><td>127.20 (n/a)</td><td>25.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (-2.83%)</td><td>0.12 (-6.77%)</td><td>0.12 (-2.12%)</td><td>0.10 (-7.82%)</td><td>0.03 (-4.46%)</td><td>212.70 (+8.47%)</td><td>173.32 (+7.37%)</td><td>174.30 (+2.17%)</td><td>122.70 (+2.94%)</td><td>37.92 (+8.00%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>196.10 (n/a)</td><td>161.42 (n/a)</td><td>170.60 (n/a)</td><td>119.20 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (+2.78%)</td><td>0.11 (+3.07%)</td><td>0.10 (+5.97%)</td><td>0.08 (-5.21%)</td><td>0.02 (+11.69%)</td><td>266.80 (+5.50%)</td><td>202.32 (-2.12%)</td><td>197.90 (-5.63%)</td><td>146.00 (-2.67%)</td><td>43.54 (+18.51%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>252.90 (n/a)</td><td>206.70 (n/a)</td><td>209.70 (n/a)</td><td>150.00 (n/a)</td><td>36.74 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (-0.98%)</td><td>0.12 (+0.60%)</td><td>0.12 (+2.91%)</td><td>0.10 (-7.10%)</td><td>0.01 <b>(+31.92%)</b></td><td>215.00 (+7.61%)</td><td>177.68 (-0.10%)</td><td>173.40 (-2.86%)</td><td>158.90 (+0.95%)</td><td>22.13 <b>(+45.69%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>177.86 (n/a)</td><td>178.50 (n/a)</td><td>157.40 (n/a)</td><td>15.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.20 (+19.07%)</td><td>0.15 (+3.02%)</td><td>0.14 (-8.49%)</td><td>0.12 (+3.38%)</td><td>0.03 <b>(+64.15%)</b></td><td>201.90 (-3.26%)</td><td>168.12 (-1.35%)</td><td>178.10 (+9.26%)</td><td>121.80 (-16.00%)</td><td>30.86 <b>(+28.44%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>208.70 (n/a)</td><td>170.42 (n/a)</td><td>163.00 (n/a)</td><td>145.00 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.19 (-7.64%)</td><td>0.15 (-12.08%)</td><td>0.16 (+3.24%)</td><td>0.10 <b>(-29.86%)</b></td><td>0.04 <b>(+38.99%)</b></td><td>245.80 <b>(+42.58%)</b></td><td>175.18 (+17.93%)</td><td>150.20 (-3.16%)</td><td>132.60 (+8.24%)</td><td>48.30 <b>(+117.06%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>172.40 (n/a)</td><td>148.54 (n/a)</td><td>155.10 (n/a)</td><td>122.50 (n/a)</td><td>22.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.18 (-1.29%)</td><td>0.16 (+7.97%)</td><td>0.17 (+9.51%)</td><td>0.14 (+16.05%)</td><td>0.02 <b>(-32.87%)</b></td><td>175.50 (-13.80%)</td><td>152.82 (-8.53%)</td><td>147.90 (-8.65%)</td><td>133.70 (+1.29%)</td><td>15.84 <b>(-40.92%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.60 (n/a)</td><td>167.08 (n/a)</td><td>161.90 (n/a)</td><td>132.00 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (-4.31%)</td><td>0.16 (+10.61%)</td><td>0.16 (+13.79%)</td><td>0.14 <b>(+22.21%)</b></td><td>0.02 <b>(-40.37%)</b></td><td>179.20 (-18.17%)</td><td>158.46 (-11.23%)</td><td>153.50 (-12.14%)</td><td>142.20 (+4.56%)</td><td>16.30 <b>(-48.90%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>219.00 (n/a)</td><td>178.50 (n/a)</td><td>174.70 (n/a)</td><td>136.00 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (-14.29%)</td><td>0.14 (-15.80%)</td><td>0.15 (-19.07%)</td><td>0.11 (-10.26%)</td><td>0.03 <b>(-21.33%)</b></td><td>222.00 (+11.45%)</td><td>179.56 (+17.98%)</td><td>164.50 <b>(+23.50%)</b></td><td>141.30 (+16.68%)</td><td>36.99 (+5.36%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>199.20 (n/a)</td><td>152.20 (n/a)</td><td>133.20 (n/a)</td><td>121.10 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.20 (+1.59%)</td><td>0.17 (+6.88%)</td><td>0.17 (+11.27%)</td><td>0.13 (+1.65%)</td><td>0.03 (-7.59%)</td><td>193.80 (-1.62%)</td><td>148.70 (-6.90%)</td><td>141.90 (-10.13%)</td><td>125.00 (-1.57%)</td><td>27.85 (-9.69%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.00 (n/a)</td><td>159.72 (n/a)</td><td>157.90 (n/a)</td><td>127.00 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.17 (+9.14%)</td><td>0.13 (+2.37%)</td><td>0.12 (-5.20%)</td><td>0.10 (-4.09%)</td><td>0.03 <b>(+62.06%)</b></td><td>248.90 (+4.23%)</td><td>198.62 (+0.54%)</td><td>209.80 (+5.48%)</td><td>143.40 (-8.37%)</td><td>46.93 <b>(+54.78%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>238.80 (n/a)</td><td>197.56 (n/a)</td><td>198.90 (n/a)</td><td>156.50 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 (+14.38%)</td><td>0.16 <b>(+22.95%)</b></td><td>0.16 <b>(+34.25%)</b></td><td>0.12 (+18.28%)</td><td>0.04 (+1.43%)</td><td>207.40 (-15.45%)</td><td>160.64 (-19.78%)</td><td>155.40 <b>(-25.54%)</b></td><td>112.10 (-12.56%)</td><td>35.42 <b>(-25.74%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>245.30 (n/a)</td><td>200.24 (n/a)</td><td>208.70 (n/a)</td><td>128.20 (n/a)</td><td>47.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.16 <b>(+48.48%)</b></td><td>0.13 <b>(+32.77%)</b></td><td>0.12 <b>(+26.50%)</b></td><td>0.11 <b>(+38.61%)</b></td><td>0.02 <b>(+57.48%)</b></td><td>163.60 <b>(-27.83%)</b></td><td>145.34 <b>(-24.48%)</b></td><td>148.60 <b>(-20.92%)</b></td><td>112.70 <b>(-32.68%)</b></td><td>19.66 <b>(-24.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>226.70 (n/a)</td><td>192.46 (n/a)</td><td>187.90 (n/a)</td><td>167.40 (n/a)</td><td>25.99 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 (+19.52%)</td><td>0.11 <b>(+34.67%)</b></td><td>0.13 <b>(+35.70%)</b></td><td>0.05 (+5.90%)</td><td>0.04 (+11.64%)</td><td>372.80 (-5.57%)</td><td>189.34 <b>(-26.42%)</b></td><td>142.20 <b>(-26.32%)</b></td><td>119.60 (-16.36%)</td><td>104.86 (-14.14%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>394.80 (n/a)</td><td>257.34 (n/a)</td><td>193.00 (n/a)</td><td>143.00 (n/a)</td><td>122.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (-19.13%)</td><td>0.10 (-15.91%)</td><td>0.10 (-10.09%)</td><td>0.05 <b>(-32.13%)</b></td><td>0.03 (-2.54%)</td><td>339.80 <b>(+47.35%)</b></td><td>203.88 <b>(+23.49%)</b></td><td>176.40 (+11.22%)</td><td>145.90 <b>(+23.64%)</b></td><td>77.31 <b>(+88.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>230.60 (n/a)</td><td>165.10 (n/a)</td><td>158.60 (n/a)</td><td>118.00 (n/a)</td><td>41.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.14 (-10.45%)</td><td>0.10 (-11.99%)</td><td>0.10 (-15.62%)</td><td>0.06 <b>(-37.99%)</b></td><td>0.03 <b>(+26.48%)</b></td><td>320.30 <b>(+61.28%)</b></td><td>196.08 <b>(+20.25%)</b></td><td>183.50 (+18.54%)</td><td>135.30 (+11.63%)</td><td>73.22 <b>(+131.49%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>198.60 (n/a)</td><td>163.06 (n/a)</td><td>154.80 (n/a)</td><td>121.20 (n/a)</td><td>31.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.12 <b>(-24.87%)</b></td><td>0.09 (-13.02%)</td><td>0.09 (+4.07%)</td><td>0.08 (+3.71%)</td><td>0.01 <b>(-62.96%)</b></td><td>225.60 (-3.55%)</td><td>198.90 (+8.02%)</td><td>203.30 (-3.88%)</td><td>160.00 <b>(+33.11%)</b></td><td>24.62 <b>(-53.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>233.90 (n/a)</td><td>184.14 (n/a)</td><td>211.50 (n/a)</td><td>120.20 (n/a)</td><td>52.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.15 (-17.12%)</td><td>0.11 (-8.39%)</td><td>0.09 (-7.53%)</td><td>0.08 (-9.17%)</td><td>0.03 <b>(-23.09%)</b></td><td>223.60 (+10.15%)</td><td>183.60 (+7.91%)</td><td>204.50 (+8.14%)</td><td>124.00 <b>(+20.62%)</b></td><td>43.18 (+5.27%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>203.00 (n/a)</td><td>170.14 (n/a)</td><td>189.10 (n/a)</td><td>102.80 (n/a)</td><td>41.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (+8.15%)</td><td>0.09 (-2.77%)</td><td>0.10 (+1.91%)</td><td>0.07 (-15.01%)</td><td>0.02 <b>(+58.97%)</b></td><td>266.30 (+17.68%)</td><td>206.02 (+5.67%)</td><td>193.60 (-1.88%)</td><td>145.80 (-7.55%)</td><td>46.67 <b>(+74.72%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>194.96 (n/a)</td><td>197.30 (n/a)</td><td>157.70 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.13 (+17.55%)</td><td>0.10 (+2.77%)</td><td>0.09 (-4.66%)</td><td>0.08 (+13.04%)</td><td>0.02 <b>(+28.56%)</b></td><td>224.60 (-11.54%)</td><td>192.06 (-2.40%)</td><td>198.90 (+4.91%)</td><td>144.00 (-14.89%)</td><td>29.75 (-9.93%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>253.90 (n/a)</td><td>196.78 (n/a)</td><td>189.60 (n/a)</td><td>169.20 (n/a)</td><td>33.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.56 <b>(-25.76%)</b></td><td>0.54 (-13.45%)</td><td>0.54 (-13.37%)</td><td>0.52 <b>(+26.20%)</b></td><td>0.02 <b>(-87.89%)</b></td><td>190.80 <b>(-20.76%)</b></td><td>181.58 (+10.37%)</td><td>180.90 (+15.44%)</td><td>176.90 <b>(+34.73%)</b></td><td>5.59 <b>(-87.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.75 (n/a)</td><td>0.63 (n/a)</td><td>0.63 (n/a)</td><td>0.41 (n/a)</td><td>0.13 (n/a)</td><td>240.80 (n/a)</td><td>164.52 (n/a)</td><td>156.70 (n/a)</td><td>131.30 (n/a)</td><td>44.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.88 <b>(+64.80%)</b></td><td>0.64 <b>(+37.55%)</b></td><td>0.58 (+12.43%)</td><td>0.50 <b>(+75.43%)</b></td><td>0.16 <b>(+46.99%)</b></td><td>197.60 <b>(-43.01%)</b></td><td>158.98 <b>(-28.46%)</b></td><td>170.60 (-11.05%)</td><td>111.60 <b>(-39.31%)</b></td><td>34.38 <b>(-50.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.53 (n/a)</td><td>0.47 (n/a)</td><td>0.51 (n/a)</td><td>0.28 (n/a)</td><td>0.11 (n/a)</td><td>346.70 (n/a)</td><td>222.24 (n/a)</td><td>191.80 (n/a)</td><td>183.90 (n/a)</td><td>70.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.71 (-10.70%)</td><td>0.57 (-10.50%)</td><td>0.51 <b>(-26.69%)</b></td><td>0.41 (-9.42%)</td><td>0.13 (-14.15%)</td><td>238.70 (+10.41%)</td><td>181.22 (+10.81%)</td><td>191.10 <b>(+36.40%)</b></td><td>137.70 (+11.95%)</td><td>42.68 (-1.40%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.80 (n/a)</td><td>0.63 (n/a)</td><td>0.70 (n/a)</td><td>0.45 (n/a)</td><td>0.16 (n/a)</td><td>216.20 (n/a)</td><td>163.54 (n/a)</td><td>140.10 (n/a)</td><td>123.00 (n/a)</td><td>43.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.56 (-12.48%)</td><td>0.50 (-7.60%)</td><td>0.51 (-11.05%)</td><td>0.42 (-0.30%)</td><td>0.05 <b>(-40.72%)</b></td><td>233.30 (+0.30%)</td><td>200.00 (+6.79%)</td><td>193.60 (+12.43%)</td><td>175.00 (+14.30%)</td><td>21.89 <b>(-32.26%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.09 (n/a)</td><td>232.60 (n/a)</td><td>187.28 (n/a)</td><td>172.20 (n/a)</td><td>153.10 (n/a)</td><td>32.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.66 <b>(+24.81%)</b></td><td>0.51 <b>(+29.90%)</b></td><td>0.51 <b>(+29.83%)</b></td><td>0.41 <b>(+59.47%)</b></td><td>0.10 (+2.53%)</td><td>181.90 <b>(-37.28%)</b></td><td>149.78 <b>(-24.94%)</b></td><td>144.70 <b>(-22.99%)</b></td><td>112.20 (-19.86%)</td><td>27.81 <b>(-49.66%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.53 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>290.00 (n/a)</td><td>199.56 (n/a)</td><td>187.90 (n/a)</td><td>140.00 (n/a)</td><td>55.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.54 (-4.24%)</td><td>0.42 (-11.10%)</td><td>0.44 (-9.60%)</td><td>0.22 <b>(-31.53%)</b></td><td>0.12 <b>(+30.76%)</b></td><td>335.20 <b>(+46.06%)</b></td><td>192.30 (+19.66%)</td><td>165.90 (+10.60%)</td><td>135.90 (+4.38%)</td><td>81.38 <b>(+104.59%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.57 (n/a)</td><td>0.48 (n/a)</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>229.50 (n/a)</td><td>160.70 (n/a)</td><td>150.00 (n/a)</td><td>130.20 (n/a)</td><td>39.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.46 <b>(-20.55%)</b></td><td>0.39 (-8.05%)</td><td>0.41 (-4.58%)</td><td>0.30 <b>(+21.53%)</b></td><td>0.06 <b>(-60.36%)</b></td><td>247.60 (-17.71%)</td><td>192.30 (-1.11%)</td><td>181.90 (+4.78%)</td><td>160.00 <b>(+25.79%)</b></td><td>33.56 <b>(-55.83%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.58 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>300.90 (n/a)</td><td>194.46 (n/a)</td><td>173.60 (n/a)</td><td>127.20 (n/a)</td><td>75.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.40 (-17.84%)</td><td>0.35 (-10.76%)</td><td>0.34 (-13.07%)</td><td>0.29 (-1.32%)</td><td>0.05 <b>(-34.52%)</b></td><td>254.60 (+1.35%)</td><td>216.06 (+10.49%)</td><td>215.00 (+15.03%)</td><td>183.90 <b>(+21.71%)</b></td><td>30.44 <b>(-20.69%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>251.20 (n/a)</td><td>195.54 (n/a)</td><td>186.90 (n/a)</td><td>151.10 (n/a)</td><td>38.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.29 (-0.34%)</td><td>0.26 (+12.98%)</td><td>0.27 <b>(+22.07%)</b></td><td>0.21 (+10.40%)</td><td>0.03 (-3.11%)</td><td>174.00 (-9.42%)</td><td>146.56 (-11.68%)</td><td>136.40 (-18.08%)</td><td>129.00 (+0.39%)</td><td>21.04 (-10.26%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>192.10 (n/a)</td><td>165.94 (n/a)</td><td>166.50 (n/a)</td><td>128.50 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.25 (-17.63%)</td><td>0.20 (-9.74%)</td><td>0.20 (-9.77%)</td><td>0.17 <b>(+66.94%)</b></td><td>0.03 <b>(-56.69%)</b></td><td>223.30 <b>(-40.09%)</b></td><td>189.68 (-2.79%)</td><td>188.60 (+10.81%)</td><td>149.50 <b>(+21.35%)</b></td><td>31.11 <b>(-69.48%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>372.70 (n/a)</td><td>195.12 (n/a)</td><td>170.20 (n/a)</td><td>123.20 (n/a)</td><td>101.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.20 <b>(-23.77%)</b></td><td>0.17 (-14.05%)</td><td>0.17 (-4.21%)</td><td>0.15 (-8.17%)</td><td>0.02 <b>(-55.44%)</b></td><td>246.10 (+8.89%)</td><td>214.90 (+13.60%)</td><td>215.10 (+4.42%)</td><td>184.40 <b>(+31.25%)</b></td><td>23.50 <b>(-36.50%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>226.00 (n/a)</td><td>189.18 (n/a)</td><td>206.00 (n/a)</td><td>140.50 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 <b>(-23.95%)</b></td><td>0.20 (-12.62%)</td><td>0.21 (-12.97%)</td><td>0.17 <b>(+38.14%)</b></td><td>0.02 <b>(-64.18%)</b></td><td>220.40 <b>(-27.60%)</b></td><td>188.70 (+4.81%)</td><td>176.70 (+14.89%)</td><td>164.90 <b>(+31.50%)</b></td><td>24.52 <b>(-66.44%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>304.40 (n/a)</td><td>180.04 (n/a)</td><td>153.80 (n/a)</td><td>125.40 (n/a)</td><td>73.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 (-13.20%)</td><td>0.21 (-4.32%)</td><td>0.22 (-6.56%)</td><td>0.16 (+8.07%)</td><td>0.04 <b>(-33.24%)</b></td><td>226.20 (-7.48%)</td><td>176.08 (+1.57%)</td><td>168.80 (+7.04%)</td><td>141.30 (+15.16%)</td><td>33.12 <b>(-29.47%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>244.50 (n/a)</td><td>173.36 (n/a)</td><td>157.70 (n/a)</td><td>122.70 (n/a)</td><td>46.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 (-12.65%)</td><td>0.19 <b>(-22.75%)</b></td><td>0.17 <b>(-24.75%)</b></td><td>0.13 <b>(-25.51%)</b></td><td>0.05 (+8.18%)</td><td>276.10 <b>(+34.22%)</b></td><td>209.68 <b>(+33.10%)</b></td><td>216.60 <b>(+32.88%)</b></td><td>141.20 (+14.42%)</td><td>56.30 <b>(+69.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>205.70 (n/a)</td><td>157.54 (n/a)</td><td>163.00 (n/a)</td><td>123.40 (n/a)</td><td>33.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.29 <b>(+31.56%)</b></td><td>0.21 (+14.59%)</td><td>0.20 (+10.56%)</td><td>0.16 (+6.39%)</td><td>0.06 <b>(+99.99%)</b></td><td>231.80 (-6.00%)</td><td>183.26 (-9.66%)</td><td>183.20 (-9.58%)</td><td>129.20 <b>(-24.00%)</b></td><td>45.89 <b>(+47.53%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>246.60 (n/a)</td><td>202.86 (n/a)</td><td>202.60 (n/a)</td><td>170.00 (n/a)</td><td>31.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.29 <b>(+40.97%)</b></td><td>0.18 (+0.70%)</td><td>0.18 (-8.48%)</td><td>0.12 (-17.19%)</td><td>0.07 <b>(+147.50%)</b></td><td>316.90 <b>(+20.72%)</b></td><td>219.82 (+6.76%)</td><td>207.80 (+9.25%)</td><td>126.30 <b>(-29.08%)</b></td><td>70.44 <b>(+104.92%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>262.50 (n/a)</td><td>205.90 (n/a)</td><td>190.20 (n/a)</td><td>178.10 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.39 (+18.03%)</td><td>0.27 (+2.85%)</td><td>0.24 (-6.42%)</td><td>0.18 (+7.90%)</td><td>0.08 <b>(+27.17%)</b></td><td>226.50 (-7.32%)</td><td>164.46 (-1.59%)</td><td>167.70 (+6.88%)</td><td>104.00 (-15.31%)</td><td>46.17 (-3.35%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>244.40 (n/a)</td><td>167.12 (n/a)</td><td>156.90 (n/a)</td><td>122.80 (n/a)</td><td>47.77 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.31 (-6.27%)</td><td>0.24 (-4.85%)</td><td>0.23 (+1.53%)</td><td>0.22 (+12.32%)</td><td>0.04 <b>(-39.00%)</b></td><td>186.40 (-10.98%)</td><td>170.56 (+2.33%)</td><td>177.10 (-1.50%)</td><td>133.20 (+6.73%)</td><td>21.69 <b>(-41.29%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>209.40 (n/a)</td><td>166.68 (n/a)</td><td>179.80 (n/a)</td><td>124.80 (n/a)</td><td>36.95 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.23 <b>(-31.13%)</b></td><td>0.20 <b>(-27.73%)</b></td><td>0.20 <b>(-32.28%)</b></td><td>0.16 (-16.18%)</td><td>0.03 <b>(-50.42%)</b></td><td>248.90 (+19.32%)</td><td>209.74 <b>(+34.83%)</b></td><td>202.10 <b>(+47.63%)</b></td><td>175.90 <b>(+45.25%)</b></td><td>33.38 (-13.54%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>208.60 (n/a)</td><td>155.56 (n/a)</td><td>136.90 (n/a)</td><td>121.10 (n/a)</td><td>38.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.27 (-12.20%)</td><td>0.22 (-9.12%)</td><td>0.22 (-1.43%)</td><td>0.17 (-10.30%)</td><td>0.04 <b>(-25.68%)</b></td><td>246.90 (+11.47%)</td><td>191.54 (+8.88%)</td><td>187.30 (+1.41%)</td><td>149.50 (+13.86%)</td><td>35.81 (-3.06%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>221.50 (n/a)</td><td>175.92 (n/a)</td><td>184.70 (n/a)</td><td>131.30 (n/a)</td><td>36.94 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.29 (-4.12%)</td><td>0.24 (+10.87%)</td><td>0.24 (+8.20%)</td><td>0.21 <b>(+33.29%)</b></td><td>0.03 <b>(-44.42%)</b></td><td>194.70 <b>(-25.00%)</b></td><td>170.20 (-12.85%)</td><td>171.30 (-7.61%)</td><td>140.60 (+4.30%)</td><td>19.70 <b>(-56.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>259.60 (n/a)</td><td>195.30 (n/a)</td><td>185.40 (n/a)</td><td>134.80 (n/a)</td><td>45.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (-10.74%)</td><td>0.21 (-14.85%)</td><td>0.22 (-12.06%)</td><td>0.14 <b>(-39.31%)</b></td><td>0.04 <b>(+111.25%)</b></td><td>302.20 <b>(+64.78%)</b></td><td>207.10 <b>(+22.20%)</b></td><td>190.30 (+13.68%)</td><td>168.40 (+11.97%)</td><td>55.12 <b>(+291.62%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>183.40 (n/a)</td><td>169.48 (n/a)</td><td>167.40 (n/a)</td><td>150.40 (n/a)</td><td>14.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.26 (-8.58%)</td><td>0.24 (+5.82%)</td><td>0.24 (+18.95%)</td><td>0.21 (+16.82%)</td><td>0.02 <b>(-56.88%)</b></td><td>190.50 (-14.42%)</td><td>172.18 (-7.82%)</td><td>168.70 (-15.94%)</td><td>156.40 (+9.37%)</td><td>14.21 <b>(-59.24%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>222.60 (n/a)</td><td>186.78 (n/a)</td><td>200.70 (n/a)</td><td>143.00 (n/a)</td><td>34.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (-5.24%)</td><td>0.22 (+8.02%)</td><td>0.22 (+11.71%)</td><td>0.21 (+19.15%)</td><td>0.01 <b>(-56.79%)</b></td><td>197.70 (-16.05%)</td><td>184.98 (-8.86%)</td><td>186.50 (-10.51%)</td><td>170.20 (+5.52%)</td><td>11.50 <b>(-61.58%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>235.50 (n/a)</td><td>202.96 (n/a)</td><td>208.40 (n/a)</td><td>161.30 (n/a)</td><td>29.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.28 (-5.41%)</td><td>0.23 (-7.05%)</td><td>0.22 (-3.26%)</td><td>0.18 (-3.76%)</td><td>0.04 (-13.90%)</td><td>190.60 (+3.87%)</td><td>157.92 (+7.06%)</td><td>159.30 (+3.37%)</td><td>123.40 (+5.74%)</td><td>25.99 (-4.16%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>183.50 (n/a)</td><td>147.50 (n/a)</td><td>154.10 (n/a)</td><td>116.70 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.24 (+1.20%)</td><td>0.22 (-1.38%)</td><td>0.22 (-2.64%)</td><td>0.18 (-4.46%)</td><td>0.02 <b>(+36.40%)</b></td><td>191.80 (+4.69%)</td><td>162.54 (+1.92%)</td><td>159.50 (+2.70%)</td><td>144.50 (-1.16%)</td><td>19.22 <b>(+37.70%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>183.20 (n/a)</td><td>159.48 (n/a)</td><td>155.30 (n/a)</td><td>146.20 (n/a)</td><td>13.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.25 (-8.53%)</td><td>0.23 (+9.91%)</td><td>0.22 (+10.96%)</td><td>0.21 <b>(+29.87%)</b></td><td>0.02 <b>(-57.17%)</b></td><td>169.20 <b>(-22.99%)</b></td><td>153.76 (-11.73%)</td><td>158.00 (-9.87%)</td><td>139.40 (+9.33%)</td><td>12.89 <b>(-64.24%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>219.70 (n/a)</td><td>174.20 (n/a)</td><td>175.30 (n/a)</td><td>127.50 (n/a)</td><td>36.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.27 (+18.82%)</td><td>0.21 (+2.50%)</td><td>0.23 (+7.37%)</td><td>0.10 <b>(-42.05%)</b></td><td>0.07 <b>(+163.12%)</b></td><td>361.10 <b>(+72.53%)</b></td><td>190.90 (+9.94%)</td><td>153.90 (-6.84%)</td><td>129.40 (-15.81%)</td><td>95.82 <b>(+317.16%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>209.30 (n/a)</td><td>173.64 (n/a)</td><td>165.20 (n/a)</td><td>153.70 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.25 (-10.75%)</td><td>0.20 (-15.41%)</td><td>0.20 (-17.80%)</td><td>0.14 (-19.89%)</td><td>0.04 (-15.25%)</td><td>241.40 <b>(+24.82%)</b></td><td>183.36 (+18.13%)</td><td>172.00 <b>(+21.64%)</b></td><td>138.80 (+12.03%)</td><td>38.35 (+17.58%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>193.40 (n/a)</td><td>155.22 (n/a)</td><td>141.40 (n/a)</td><td>123.90 (n/a)</td><td>32.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.25 (-15.54%)</td><td>0.19 (-11.24%)</td><td>0.20 (-6.45%)</td><td>0.10 <b>(-40.29%)</b></td><td>0.07 (+18.21%)</td><td>365.90 <b>(+67.46%)</b></td><td>206.90 <b>(+21.98%)</b></td><td>170.20 (+6.91%)</td><td>137.20 (+18.38%)</td><td>94.96 <b>(+128.65%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>218.50 (n/a)</td><td>169.62 (n/a)</td><td>159.20 (n/a)</td><td>115.90 (n/a)</td><td>41.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.22 (+13.93%)</td><td>0.20 (+15.17%)</td><td>0.20 (+12.53%)</td><td>0.18 <b>(+33.88%)</b></td><td>0.02 <b>(-34.03%)</b></td><td>191.60 <b>(-25.30%)</b></td><td>175.96 (-14.31%)</td><td>178.40 (-11.16%)</td><td>154.90 (-12.24%)</td><td>14.03 <b>(-56.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>256.50 (n/a)</td><td>205.34 (n/a)</td><td>200.80 (n/a)</td><td>176.50 (n/a)</td><td>32.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.20 (-1.23%)</td><td>0.18 (-1.48%)</td><td>0.18 (-0.73%)</td><td>0.16 (-5.18%)</td><td>0.02 (+16.41%)</td><td>224.40 (+5.45%)</td><td>197.32 (+1.77%)</td><td>190.10 (+0.74%)</td><td>177.80 (+1.25%)</td><td>21.19 <b>(+22.02%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>212.80 (n/a)</td><td>193.88 (n/a)</td><td>188.70 (n/a)</td><td>175.60 (n/a)</td><td>17.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.88 (-9.39%)</td><td>0.77 (-17.62%)</td><td>0.85 (-11.35%)</td><td>0.58 <b>(-28.47%)</b></td><td>0.13 <b>(+98.01%)</b></td><td>224.70 <b>(+39.83%)</b></td><td>174.70 <b>(+24.06%)</b></td><td>153.60 (+12.78%)</td><td>148.90 (+10.30%)</td><td>33.36 <b>(+199.81%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.97 (n/a)</td><td>0.94 (n/a)</td><td>0.96 (n/a)</td><td>0.82 (n/a)</td><td>0.07 (n/a)</td><td>160.70 (n/a)</td><td>140.82 (n/a)</td><td>136.20 (n/a)</td><td>135.00 (n/a)</td><td>11.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.84 <b>(-25.47%)</b></td><td>0.66 <b>(-30.92%)</b></td><td>0.64 <b>(-33.28%)</b></td><td>0.55 <b>(-28.99%)</b></td><td>0.11 (-11.89%)</td><td>237.00 <b>(+40.82%)</b></td><td>203.62 <b>(+45.63%)</b></td><td>204.40 <b>(+49.85%)</b></td><td>156.10 <b>(+34.22%)</b></td><td>30.49 <b>(+61.67%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.13 (n/a)</td><td>0.95 (n/a)</td><td>0.96 (n/a)</td><td>0.78 (n/a)</td><td>0.13 (n/a)</td><td>168.30 (n/a)</td><td>139.82 (n/a)</td><td>136.40 (n/a)</td><td>116.30 (n/a)</td><td>18.86 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.82 (-19.55%)</td><td>0.72 (-9.99%)</td><td>0.70 (-13.28%)</td><td>0.63 (+8.84%)</td><td>0.08 <b>(-50.37%)</b></td><td>206.50 (-8.14%)</td><td>184.30 (+8.62%)</td><td>187.00 (+15.29%)</td><td>160.40 <b>(+24.34%)</b></td><td>19.32 <b>(-44.49%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.02 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.58 (n/a)</td><td>0.15 (n/a)</td><td>224.80 (n/a)</td><td>169.68 (n/a)</td><td>162.20 (n/a)</td><td>129.00 (n/a)</td><td>34.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-4.65%)</td><td>0.03 (+19.03%)</td><td>0.03 <b>(+29.05%)</b></td><td>0.03 <b>(+48.06%)</b></td><td>0.00 <b>(-76.45%)</b></td><td>152.00 <b>(-32.47%)</b></td><td>144.28 (-19.13%)</td><td>143.90 <b>(-22.55%)</b></td><td>135.60 (+4.87%)</td><td>6.47 <b>(-83.17%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.10 (n/a)</td><td>178.42 (n/a)</td><td>185.80 (n/a)</td><td>129.30 (n/a)</td><td>38.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+5.24%)</td><td>0.03 (-1.78%)</td><td>0.03 (-3.58%)</td><td>0.02 (+5.77%)</td><td>0.00 (-5.63%)</td><td>169.90 (-5.45%)</td><td>150.96 (+1.51%)</td><td>155.20 (+3.74%)</td><td>121.90 (-4.91%)</td><td>18.28 (-14.92%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.70 (n/a)</td><td>148.72 (n/a)</td><td>149.60 (n/a)</td><td>128.20 (n/a)</td><td>21.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (+5.48%)</td><td>0.02 (+0.10%)</td><td>0.02 (-0.91%)</td><td>0.02 (-1.21%)</td><td>0.00 (+19.41%)</td><td>213.10 (+1.24%)</td><td>174.38 (+0.72%)</td><td>178.30 (+0.91%)</td><td>131.00 (-5.21%)</td><td>33.22 (+15.42%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.50 (n/a)</td><td>173.14 (n/a)</td><td>176.70 (n/a)</td><td>138.20 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>15.19 (-6.31%)</td><td>13.54 (+5.58%)</td><td>14.31 (+20.00%)</td><td>10.69 <b>(+20.49%)</b></td><td>1.75 <b>(-46.18%)</b></td><td>196.30 (-17.00%)</td><td>157.32 (-8.85%)</td><td>146.60 (-16.66%)</td><td>138.10 (+6.72%)</td><td>23.10 <b>(-48.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>16.21 (n/a)</td><td>12.83 (n/a)</td><td>11.93 (n/a)</td><td>8.87 (n/a)</td><td>3.25 (n/a)</td><td>236.50 (n/a)</td><td>172.60 (n/a)</td><td>175.90 (n/a)</td><td>129.40 (n/a)</td><td>45.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.01 (-10.53%)</td><td>0.88 (+3.71%)</td><td>0.98 <b>(+29.63%)</b></td><td>0.70 (+11.00%)</td><td>0.16 <b>(-26.30%)</b></td><td>188.30 (-9.90%)</td><td>153.78 (-5.53%)</td><td>134.80 <b>(-22.88%)</b></td><td>130.70 (+11.80%)</td><td>28.97 <b>(-24.21%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.13 (n/a)</td><td>0.85 (n/a)</td><td>0.76 (n/a)</td><td>0.63 (n/a)</td><td>0.21 (n/a)</td><td>209.00 (n/a)</td><td>162.78 (n/a)</td><td>174.80 (n/a)</td><td>116.90 (n/a)</td><td>38.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.08 (+1.06%)</td><td>0.93 (-3.28%)</td><td>0.91 (-12.37%)</td><td>0.83 <b>(+33.20%)</b></td><td>0.10 <b>(-47.09%)</b></td><td>160.00 <b>(-24.95%)</b></td><td>143.42 (-0.18%)</td><td>144.90 (+14.09%)</td><td>122.30 (-1.05%)</td><td>15.08 <b>(-61.29%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.07 (n/a)</td><td>0.96 (n/a)</td><td>1.04 (n/a)</td><td>0.62 (n/a)</td><td>0.19 (n/a)</td><td>213.20 (n/a)</td><td>143.68 (n/a)</td><td>127.00 (n/a)</td><td>123.60 (n/a)</td><td>38.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.99 (-4.29%)</td><td>0.80 (-9.23%)</td><td>0.79 (-12.18%)</td><td>0.63 (-7.74%)</td><td>0.15 (-3.17%)</td><td>210.30 (+8.40%)</td><td>169.90 (+10.35%)</td><td>167.40 (+13.80%)</td><td>133.20 (+4.47%)</td><td>30.96 (+10.90%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.04 (n/a)</td><td>0.88 (n/a)</td><td>0.90 (n/a)</td><td>0.68 (n/a)</td><td>0.15 (n/a)</td><td>194.00 (n/a)</td><td>153.96 (n/a)</td><td>147.10 (n/a)</td><td>127.50 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.96 <b>(-34.44%)</b></td><td>0.85 (-8.08%)</td><td>0.84 (-2.40%)</td><td>0.74 <b>(+20.16%)</b></td><td>0.10 <b>(-70.10%)</b></td><td>178.10 (-16.74%)</td><td>157.68 (-0.62%)</td><td>156.40 (+2.42%)</td><td>137.20 <b>(+52.44%)</b></td><td>19.44 <b>(-63.14%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.47 (n/a)</td><td>0.92 (n/a)</td><td>0.87 (n/a)</td><td>0.62 (n/a)</td><td>0.35 (n/a)</td><td>213.90 (n/a)</td><td>158.66 (n/a)</td><td>152.70 (n/a)</td><td>90.00 (n/a)</td><td>52.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.97 <b>(-23.05%)</b></td><td>0.86 (-9.38%)</td><td>0.96 (-6.49%)</td><td>0.71 <b>(+25.89%)</b></td><td>0.14 <b>(-49.97%)</b></td><td>186.00 <b>(-20.58%)</b></td><td>156.40 (+4.04%)</td><td>137.90 (+6.90%)</td><td>135.80 <b>(+29.95%)</b></td><td>26.31 <b>(-49.26%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.26 (n/a)</td><td>0.95 (n/a)</td><td>1.02 (n/a)</td><td>0.56 (n/a)</td><td>0.27 (n/a)</td><td>234.20 (n/a)</td><td>150.32 (n/a)</td><td>129.00 (n/a)</td><td>104.50 (n/a)</td><td>51.86 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-4.64%)</td><td>0.03 (+10.46%)</td><td>0.03 (+11.90%)</td><td>0.02 <b>(+22.07%)</b></td><td>0.00 <b>(-45.67%)</b></td><td>178.00 (-18.09%)</td><td>149.34 (-11.70%)</td><td>144.10 (-10.61%)</td><td>134.60 (+4.83%)</td><td>16.65 <b>(-52.44%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.30 (n/a)</td><td>169.12 (n/a)</td><td>161.20 (n/a)</td><td>128.40 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.03 (-9.59%)</td><td>0.03 (+5.13%)</td><td>0.02 (+0.20%)</td><td>0.02 <b>(+24.02%)</b></td><td>0.00 <b>(-44.56%)</b></td><td>191.30 (-19.38%)</td><td>165.38 (-9.01%)</td><td>165.80 (-0.24%)</td><td>131.90 (+10.65%)</td><td>23.29 <b>(-52.02%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>181.76 (n/a)</td><td>166.20 (n/a)</td><td>119.20 (n/a)</td><td>48.54 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.00 (+2.27%)</td><td>0.00 (+2.86%)</td><td>0.00 (+4.76%)</td><td>0.00 (-2.50%)</td><td>0.00 <b>(+76.07%)</b></td><td>1053.89 (+1.99%)</td><td>949.08 (-3.02%)</td><td>936.36 (-4.50%)</td><td>901.82 (-2.90%)</td><td>62.34 <b>(+66.30%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1033.34 (n/a)</td><td>978.66 (n/a)</td><td>980.47 (n/a)</td><td>928.78 (n/a)</td><td>37.49 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.01 (+3.61%)</td><td>0.01 (+4.29%)</td><td>0.01 (+1.23%)</td><td>0.01 (+6.76%)</td><td>0.00 (-17.06%)</td><td>1036.59 (-5.88%)</td><td>992.80 (-3.84%)</td><td>996.25 (-1.13%)</td><td>953.71 (-3.31%)</td><td>38.18 <b>(-25.12%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1101.32 (n/a)</td><td>1032.44 (n/a)</td><td>1007.62 (n/a)</td><td>986.33 (n/a)</td><td>50.99 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.96 (-2.31%)</td><td>0.95 (-0.52%)</td><td>0.95 (+0.03%)</td><td>0.94 (-0.15%)</td><td>0.01 <b>(-51.53%)</b></td><td>2225.48 (+0.15%)</td><td>2198.14 (+0.50%)</td><td>2201.53 (-0.03%)</td><td>2175.41 (+2.36%)</td><td>19.77 <b>(-50.33%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.02 (n/a)</td><td>2222.24 (n/a)</td><td>2187.19 (n/a)</td><td>2202.25 (n/a)</td><td>2125.20 (n/a)</td><td>39.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.88 (-3.00%)</td><td>0.87 (-0.88%)</td><td>0.87 (-0.55%)</td><td>0.86 (+1.16%)</td><td>0.01 <b>(-63.49%)</b></td><td>2426.98 (-1.15%)</td><td>2402.87 (+0.86%)</td><td>2399.21 (+0.55%)</td><td>2378.12 (+3.11%)</td><td>19.59 <b>(-62.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.91 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.85 (n/a)</td><td>0.02 (n/a)</td><td>2455.17 (n/a)</td><td>2382.46 (n/a)</td><td>2386.13 (n/a)</td><td>2306.48 (n/a)</td><td>52.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.67 (-0.23%)</td><td>0.62 (-6.20%)</td><td>0.62 (-7.06%)</td><td>0.58 (-10.47%)</td><td>0.03 <b>(+323.47%)</b></td><td>1806.10 (+11.70%)</td><td>1695.36 (+6.81%)</td><td>1701.20 (+7.60%)</td><td>1574.50 (+0.23%)</td><td>83.44 <b>(+371.65%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.67 (n/a)</td><td>0.66 (n/a)</td><td>0.66 (n/a)</td><td>0.65 (n/a)</td><td>0.01 (n/a)</td><td>1616.90 (n/a)</td><td>1587.26 (n/a)</td><td>1581.10 (n/a)</td><td>1570.90 (n/a)</td><td>17.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.23 (+1.10%)</td><td>1.16 (+0.18%)</td><td>1.15 (-0.60%)</td><td>1.10 (-1.94%)</td><td>0.05 <b>(+30.85%)</b></td><td>957.60 (+1.98%)</td><td>904.96 (-0.11%)</td><td>911.30 (+0.61%)</td><td>851.50 (-1.08%)</td><td>38.64 <b>(+32.19%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.22 (n/a)</td><td>1.16 (n/a)</td><td>1.16 (n/a)</td><td>1.12 (n/a)</td><td>0.04 (n/a)</td><td>939.00 (n/a)</td><td>905.98 (n/a)</td><td>905.80 (n/a)</td><td>860.80 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.23 (+3.29%)</td><td>1.15 (+0.67%)</td><td>1.15 (+0.19%)</td><td>1.11 (-1.04%)</td><td>0.05 <b>(+59.64%)</b></td><td>948.00 (+1.06%)</td><td>909.60 (-0.58%)</td><td>915.30 (-0.19%)</td><td>850.00 (-3.19%)</td><td>37.37 <b>(+55.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.19 (n/a)</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.12 (n/a)</td><td>0.03 (n/a)</td><td>938.10 (n/a)</td><td>914.92 (n/a)</td><td>917.00 (n/a)</td><td>878.00 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>2.05 (-2.94%)</td><td>1.92 (-0.75%)</td><td>1.92 (+0.26%)</td><td>1.85 (+1.31%)</td><td>0.08 <b>(-29.81%)</b></td><td>567.30 (-1.29%)</td><td>545.46 (+0.64%)</td><td>547.30 (-0.26%)</td><td>511.10 (+3.02%)</td><td>20.92 <b>(-28.51%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.11 (n/a)</td><td>1.94 (n/a)</td><td>1.91 (n/a)</td><td>1.82 (n/a)</td><td>0.11 (n/a)</td><td>574.70 (n/a)</td><td>542.00 (n/a)</td><td>548.70 (n/a)</td><td>496.10 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.70 (+0.59%)</td><td>0.65 (-1.40%)</td><td>0.66 (+0.41%)</td><td>0.60 (-5.71%)</td><td>0.04 <b>(+48.77%)</b></td><td>3494.10 (+6.05%)</td><td>3215.92 (+1.59%)</td><td>3197.40 (-0.41%)</td><td>2997.00 (-0.59%)</td><td>195.72 <b>(+57.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.70 (n/a)</td><td>0.66 (n/a)</td><td>0.65 (n/a)</td><td>0.64 (n/a)</td><td>0.03 (n/a)</td><td>3294.70 (n/a)</td><td>3165.50 (n/a)</td><td>3210.60 (n/a)</td><td>3014.80 (n/a)</td><td>124.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.34 (+1.19%)</td><td>1.29 (+1.42%)</td><td>1.30 (+2.40%)</td><td>1.22 (-1.12%)</td><td>0.05 <b>(+34.28%)</b></td><td>1725.90 (+1.14%)</td><td>1623.04 (-1.35%)</td><td>1611.40 (-2.35%)</td><td>1565.80 (-1.18%)</td><td>61.30 <b>(+35.25%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.32 (n/a)</td><td>1.28 (n/a)</td><td>1.27 (n/a)</td><td>1.23 (n/a)</td><td>0.04 (n/a)</td><td>1706.50 (n/a)</td><td>1645.30 (n/a)</td><td>1650.10 (n/a)</td><td>1584.50 (n/a)</td><td>45.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.34 (+0.37%)</td><td>1.28 (+0.28%)</td><td>1.27 (+0.52%)</td><td>1.21 (-0.33%)</td><td>0.05 (+14.51%)</td><td>1733.70 (+0.33%)</td><td>1643.12 (-0.25%)</td><td>1646.40 (-0.52%)</td><td>1568.70 (-0.37%)</td><td>68.28 (+14.21%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.33 (n/a)</td><td>1.27 (n/a)</td><td>1.27 (n/a)</td><td>1.21 (n/a)</td><td>0.05 (n/a)</td><td>1728.00 (n/a)</td><td>1647.16 (n/a)</td><td>1655.00 (n/a)</td><td>1574.50 (n/a)</td><td>59.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>2.37 (-1.77%)</td><td>2.28 (+5.20%)</td><td>2.26 (-3.09%)</td><td>2.23 <b>(+54.46%)</b></td><td>0.06 <b>(-86.10%)</b></td><td>942.00 <b>(-35.26%)</b></td><td>921.68 (-8.49%)</td><td>928.60 (+3.19%)</td><td>884.20 (+1.81%)</td><td>22.53 <b>(-91.05%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.41 (n/a)</td><td>2.16 (n/a)</td><td>2.33 (n/a)</td><td>1.44 (n/a)</td><td>0.41 (n/a)</td><td>1455.00 (n/a)</td><td>1007.18 (n/a)</td><td>899.90 (n/a)</td><td>868.50 (n/a)</td><td>251.74 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>2.51 (+8.54%)</td><td>2.33 (+3.16%)</td><td>2.38 (+5.59%)</td><td>2.01 (-8.63%)</td><td>0.19 <b>(+270.37%)</b></td><td>1045.90 (+9.44%)</td><td>906.28 (-2.53%)</td><td>882.00 (-5.30%)</td><td>836.40 (-7.87%)</td><td>81.48 <b>(+281.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.31 (n/a)</td><td>2.26 (n/a)</td><td>2.25 (n/a)</td><td>2.19 (n/a)</td><td>0.05 (n/a)</td><td>955.70 (n/a)</td><td>929.82 (n/a)</td><td>931.40 (n/a)</td><td>907.80 (n/a)</td><td>21.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>4.07 (-4.04%)</td><td>3.75 (-2.94%)</td><td>3.64 (-0.89%)</td><td>3.55 (-0.90%)</td><td>0.23 <b>(-26.85%)</b></td><td>590.00 (+0.91%)</td><td>560.88 (+2.81%)</td><td>576.50 (+0.89%)</td><td>515.40 (+4.21%)</td><td>32.82 <b>(-22.55%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.24 (n/a)</td><td>3.86 (n/a)</td><td>3.67 (n/a)</td><td>3.59 (n/a)</td><td>0.31 (n/a)</td><td>584.70 (n/a)</td><td>545.54 (n/a)</td><td>571.40 (n/a)</td><td>494.60 (n/a)</td><td>42.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.72 (+1.13%)</td><td>0.70 (+2.99%)</td><td>0.69 (+2.45%)</td><td>0.68 (+5.92%)</td><td>0.01 <b>(-46.36%)</b></td><td>6125.40 (-5.59%)</td><td>6032.28 (-2.98%)</td><td>6068.30 (-2.39%)</td><td>5835.20 (-1.12%)</td><td>113.44 <b>(-50.12%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.71 (n/a)</td><td>0.68 (n/a)</td><td>0.67 (n/a)</td><td>0.65 (n/a)</td><td>0.02 (n/a)</td><td>6488.20 (n/a)</td><td>6217.76 (n/a)</td><td>6217.00 (n/a)</td><td>5901.30 (n/a)</td><td>227.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.39 (+1.38%)</td><td>1.28 (-1.35%)</td><td>1.29 (-0.01%)</td><td>1.09 (-6.95%)</td><td>0.12 <b>(+44.91%)</b></td><td>3865.50 (+7.46%)</td><td>3303.46 (+1.80%)</td><td>3246.60 (+0.01%)</td><td>3014.80 (-1.36%)</td><td>336.33 <b>(+55.09%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.37 (n/a)</td><td>1.30 (n/a)</td><td>1.29 (n/a)</td><td>1.17 (n/a)</td><td>0.08 (n/a)</td><td>3597.00 (n/a)</td><td>3245.14 (n/a)</td><td>3246.40 (n/a)</td><td>3056.50 (n/a)</td><td>216.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.40 (-0.45%)</td><td>1.33 (-0.94%)</td><td>1.30 (-3.08%)</td><td>1.28 (-1.06%)</td><td>0.05 <b>(+28.90%)</b></td><td>3268.60 (+1.07%)</td><td>3151.26 (+1.00%)</td><td>3214.40 (+3.18%)</td><td>2999.80 (+0.46%)</td><td>118.24 <b>(+30.95%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.40 (n/a)</td><td>1.35 (n/a)</td><td>1.35 (n/a)</td><td>1.30 (n/a)</td><td>0.04 (n/a)</td><td>3234.10 (n/a)</td><td>3120.18 (n/a)</td><td>3115.40 (n/a)</td><td>2986.20 (n/a)</td><td>90.29 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>2.66 (+0.62%)</td><td>2.58 (+5.61%)</td><td>2.58 (+1.60%)</td><td>2.49 (+15.66%)</td><td>0.06 <b>(-71.97%)</b></td><td>1682.40 (-13.54%)</td><td>1627.90 (-5.88%)</td><td>1628.40 (-1.57%)</td><td>1578.60 (-0.61%)</td><td>37.99 <b>(-75.84%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.64 (n/a)</td><td>2.44 (n/a)</td><td>2.54 (n/a)</td><td>2.16 (n/a)</td><td>0.21 (n/a)</td><td>1945.80 (n/a)</td><td>1729.54 (n/a)</td><td>1654.40 (n/a)</td><td>1588.30 (n/a)</td><td>157.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>2.65 (+0.32%)</td><td>2.60 (+13.21%)</td><td>2.61 (+16.00%)</td><td>2.47 <b>(+28.43%)</b></td><td>0.07 <b>(-74.27%)</b></td><td>1697.00 <b>(-22.14%)</b></td><td>1615.76 (-12.71%)</td><td>1605.90 (-13.79%)</td><td>1581.30 (-0.32%)</td><td>46.78 <b>(-79.87%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>2.64 (n/a)</td><td>2.29 (n/a)</td><td>2.25 (n/a)</td><td>1.92 (n/a)</td><td>0.28 (n/a)</td><td>2179.60 (n/a)</td><td>1850.94 (n/a)</td><td>1862.80 (n/a)</td><td>1586.40 (n/a)</td><td>232.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>4.82 (+1.14%)</td><td>4.58 (+3.16%)</td><td>4.63 (-0.11%)</td><td>4.36 (+7.26%)</td><td>0.18 <b>(-49.26%)</b></td><td>961.80 (-6.78%)</td><td>915.88 (-3.44%)</td><td>905.80 (+0.11%)</td><td>870.40 (-1.12%)</td><td>35.39 <b>(-53.67%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.76 (n/a)</td><td>4.44 (n/a)</td><td>4.64 (n/a)</td><td>4.07 (n/a)</td><td>0.35 (n/a)</td><td>1031.70 (n/a)</td><td>948.52 (n/a)</td><td>904.80 (n/a)</td><td>880.30 (n/a)</td><td>76.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>4.75 (-1.76%)</td><td>4.52 (-3.59%)</td><td>4.50 (-4.64%)</td><td>4.37 (-3.02%)</td><td>0.14 (+8.82%)</td><td>960.20 (+3.11%)</td><td>929.64 (+3.74%)</td><td>933.00 (+4.87%)</td><td>882.80 (+1.80%)</td><td>28.49 (+13.19%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>4.84 (n/a)</td><td>4.68 (n/a)</td><td>4.71 (n/a)</td><td>4.50 (n/a)</td><td>0.13 (n/a)</td><td>931.20 (n/a)</td><td>896.10 (n/a)</td><td>889.70 (n/a)</td><td>867.20 (n/a)</td><td>25.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>7.57 (-5.95%)</td><td>7.40 (+3.54%)</td><td>7.42 (+5.32%)</td><td>7.23 (+12.36%)</td><td>0.13 <b>(-77.85%)</b></td><td>580.20 (-11.00%)</td><td>567.06 (-3.89%)</td><td>565.30 (-5.06%)</td><td>553.90 (+6.31%)</td><td>9.90 <b>(-78.85%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>8.05 (n/a)</td><td>7.15 (n/a)</td><td>7.05 (n/a)</td><td>6.43 (n/a)</td><td>0.58 (n/a)</td><td>651.90 (n/a)</td><td>590.04 (n/a)</td><td>595.40 (n/a)</td><td>521.00 (n/a)</td><td>46.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.61 (+0.03%)</td><td>0.56 (-4.63%)</td><td>0.56 (-4.90%)</td><td>0.51 (-6.74%)</td><td>0.04 <b>(+77.46%)</b></td><td>1022.50 (+7.23%)</td><td>946.26 (+5.13%)</td><td>943.50 (+5.15%)</td><td>863.10 (-0.03%)</td><td>64.94 <b>(+90.02%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.61 (n/a)</td><td>0.58 (n/a)</td><td>0.58 (n/a)</td><td>0.55 (n/a)</td><td>0.02 (n/a)</td><td>953.60 (n/a)</td><td>900.06 (n/a)</td><td>897.30 (n/a)</td><td>863.40 (n/a)</td><td>34.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.64 (-2.03%)</td><td>0.63 (-1.70%)</td><td>0.63 (-1.79%)</td><td>0.61 (-2.07%)</td><td>0.02 <b>(+23.94%)</b></td><td>1722.90 (+2.12%)</td><td>1675.56 (+1.75%)</td><td>1674.00 (+1.82%)</td><td>1632.50 (+2.07%)</td><td>42.72 <b>(+29.13%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.66 (n/a)</td><td>0.64 (n/a)</td><td>0.64 (n/a)</td><td>0.62 (n/a)</td><td>0.01 (n/a)</td><td>1687.20 (n/a)</td><td>1646.80 (n/a)</td><td>1644.00 (n/a)</td><td>1599.40 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.68 (-0.94%)</td><td>0.64 (+1.44%)</td><td>0.66 (+3.64%)</td><td>0.59 (+2.61%)</td><td>0.04 (-12.95%)</td><td>3566.30 (-2.54%)</td><td>3262.30 (-1.50%)</td><td>3195.60 (-3.51%)</td><td>3094.30 (+0.95%)</td><td>189.24 (-14.62%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.68 (n/a)</td><td>0.64 (n/a)</td><td>0.63 (n/a)</td><td>0.57 (n/a)</td><td>0.04 (n/a)</td><td>3659.20 (n/a)</td><td>3312.12 (n/a)</td><td>3311.90 (n/a)</td><td>3065.10 (n/a)</td><td>221.65 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>1.03 (+0.12%)</td><td>0.95 (-5.47%)</td><td>0.98 (-4.36%)</td><td>0.84 (-10.96%)</td><td>0.07 <b>(+90.93%)</b></td><td>626.30 (+12.32%)</td><td>553.28 (+6.18%)</td><td>535.80 (+4.55%)</td><td>510.10 (-0.12%)</td><td>44.33 <b>(+116.95%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>0.94 (n/a)</td><td>0.04 (n/a)</td><td>557.60 (n/a)</td><td>521.08 (n/a)</td><td>512.50 (n/a)</td><td>510.70 (n/a)</td><td>20.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.19 (-0.68%)</td><td>0.16 (-3.63%)</td><td>0.15 (-4.19%)</td><td>0.14 (+1.47%)</td><td>0.02 (+2.26%)</td><td>230.40 (-1.45%)</td><td>210.02 (+3.80%)</td><td>215.30 (+4.36%)</td><td>175.00 (+0.69%)</td><td>22.40 (+1.27%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>233.80 (n/a)</td><td>202.34 (n/a)</td><td>206.30 (n/a)</td><td>173.80 (n/a)</td><td>22.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.20 (-4.65%)</td><td>0.17 (-3.68%)</td><td>0.17 (-5.76%)</td><td>0.14 (-3.00%)</td><td>0.02 <b>(-23.63%)</b></td><td>228.70 (+3.06%)</td><td>193.98 (+2.92%)</td><td>196.80 (+6.09%)</td><td>161.20 (+4.88%)</td><td>25.63 (-19.17%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.90 (n/a)</td><td>188.48 (n/a)</td><td>185.50 (n/a)</td><td>153.70 (n/a)</td><td>31.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.31 (+3.42%)</td><td>0.26 (-2.60%)</td><td>0.25 (-1.41%)</td><td>0.21 (-7.60%)</td><td>0.04 <b>(+51.97%)</b></td><td>305.90 (+8.21%)</td><td>259.34 (+3.66%)</td><td>258.20 (+1.45%)</td><td>213.10 (-3.31%)</td><td>36.80 <b>(+59.31%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>282.70 (n/a)</td><td>250.18 (n/a)</td><td>254.50 (n/a)</td><td>220.40 (n/a)</td><td>23.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.38 (+10.98%)</td><td>0.31 (-2.33%)</td><td>0.30 (-5.91%)</td><td>0.25 (-8.98%)</td><td>0.05 <b>(+66.96%)</b></td><td>265.00 (+9.87%)</td><td>215.98 (+3.59%)</td><td>215.20 (+6.27%)</td><td>172.40 (-9.88%)</td><td>32.87 <b>(+64.04%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>241.20 (n/a)</td><td>208.50 (n/a)</td><td>202.50 (n/a)</td><td>191.30 (n/a)</td><td>20.04 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.41 (+10.06%)</td><td>0.36 (+2.43%)</td><td>0.35 (+0.27%)</td><td>0.31 (-5.42%)</td><td>0.05 <b>(+191.06%)</b></td><td>213.90 (+5.73%)</td><td>186.98 (-0.93%)</td><td>187.20 (-0.27%)</td><td>159.50 (-9.17%)</td><td>26.83 <b>(+180.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.02 (n/a)</td><td>202.30 (n/a)</td><td>188.74 (n/a)</td><td>187.70 (n/a)</td><td>175.60 (n/a)</td><td>9.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.41 (-5.74%)</td><td>0.37 (-1.68%)</td><td>0.37 (-9.45%)</td><td>0.33 (+16.06%)</td><td>0.03 <b>(-59.62%)</b></td><td>393.80 (-13.85%)</td><td>355.64 (-0.72%)</td><td>351.30 (+10.44%)</td><td>320.80 (+6.08%)</td><td>26.42 <b>(-62.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>457.10 (n/a)</td><td>358.22 (n/a)</td><td>318.10 (n/a)</td><td>302.40 (n/a)</td><td>70.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.59 (+5.56%)</td><td>0.48 (-5.17%)</td><td>0.47 (-10.03%)</td><td>0.30 <b>(-29.64%)</b></td><td>0.12 <b>(+139.01%)</b></td><td>439.00 <b>(+42.12%)</b></td><td>291.22 (+11.06%)</td><td>281.30 (+11.14%)</td><td>223.20 (-5.26%)</td><td>87.98 <b>(+214.65%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.56 (n/a)</td><td>0.50 (n/a)</td><td>0.52 (n/a)</td><td>0.42 (n/a)</td><td>0.05 (n/a)</td><td>308.90 (n/a)</td><td>262.22 (n/a)</td><td>253.10 (n/a)</td><td>235.60 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.68 (-8.38%)</td><td>0.58 (-9.16%)</td><td>0.55 (-16.21%)</td><td>0.51 (+10.72%)</td><td>0.08 <b>(-27.42%)</b></td><td>256.20 (-9.66%)</td><td>227.62 (+8.57%)</td><td>238.70 (+19.35%)</td><td>192.60 (+9.12%)</td><td>30.01 <b>(-30.31%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.74 (n/a)</td><td>0.64 (n/a)</td><td>0.66 (n/a)</td><td>0.46 (n/a)</td><td>0.11 (n/a)</td><td>283.60 (n/a)</td><td>209.66 (n/a)</td><td>200.00 (n/a)</td><td>176.50 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.72 (-19.96%)</td><td>0.60 (-13.99%)</td><td>0.59 (-16.29%)</td><td>0.54 (+16.40%)</td><td>0.07 <b>(-54.47%)</b></td><td>243.00 (-14.07%)</td><td>221.04 (+12.21%)</td><td>222.20 (+19.46%)</td><td>183.30 <b>(+24.95%)</b></td><td>23.54 <b>(-53.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.89 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.46 (n/a)</td><td>0.15 (n/a)</td><td>282.80 (n/a)</td><td>196.98 (n/a)</td><td>186.00 (n/a)</td><td>146.70 (n/a)</td><td>50.88 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:01</td><td>0.10 (-5.32%)</td><td>0.08 (-10.09%)</td><td>0.08 (-12.48%)</td><td>0.07 (-7.05%)</td><td>0.01 (-1.70%)</td><td>246.90 (+7.58%)</td><td>202.10 (+11.39%)</td><td>195.90 (+14.29%)</td><td>157.70 (+5.63%)</td><td>33.02 (+9.03%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.50 (n/a)</td><td>181.44 (n/a)</td><td>171.40 (n/a)</td><td>149.30 (n/a)</td><td>30.29 (n/a)</td>
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
