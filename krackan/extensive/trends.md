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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (+10.07%)</td><td>0.04 (+13.81%)</td><td>0.04 (+13.19%)</td><td>0.04 <b>(+28.54%)</b></td><td>0.01 (+0.16%)</td><td>163.00 <b>(-22.20%)</b></td><td>141.18 (-12.80%)</td><td>142.20 (-11.68%)</td><td>113.40 (-9.13%)</td><td>21.91 <b>(-28.55%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>161.90 (n/a)</td><td>161.00 (n/a)</td><td>124.80 (n/a)</td><td>30.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (-0.74%)</td><td>0.03 (-9.26%)</td><td>0.03 (-11.74%)</td><td>0.03 (-10.69%)</td><td>0.01 <b>(+31.07%)</b></td><td>214.00 (+11.98%)</td><td>180.54 (+11.38%)</td><td>179.90 (+13.29%)</td><td>137.40 (+0.73%)</td><td>28.93 <b>(+45.23%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.10 (n/a)</td><td>162.10 (n/a)</td><td>158.80 (n/a)</td><td>136.40 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (-16.72%)</td><td>0.04 (-13.77%)</td><td>0.03 <b>(-23.47%)</b></td><td>0.03 (+8.16%)</td><td>0.01 <b>(-42.90%)</b></td><td>197.10 (-7.55%)</td><td>175.40 (+11.62%)</td><td>187.50 <b>(+30.66%)</b></td><td>131.50 <b>(+20.09%)</b></td><td>26.26 <b>(-39.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>157.14 (n/a)</td><td>143.50 (n/a)</td><td>109.50 (n/a)</td><td>43.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (-13.91%)</td><td>0.04 (+2.36%)</td><td>0.03 (-9.22%)</td><td>0.03 <b>(+82.28%)</b></td><td>0.01 <b>(-45.00%)</b></td><td>196.90 <b>(-45.12%)</b></td><td>168.70 (-12.98%)</td><td>179.40 (+10.13%)</td><td>129.50 (+16.14%)</td><td>31.31 <b>(-67.20%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>358.80 (n/a)</td><td>193.86 (n/a)</td><td>162.90 (n/a)</td><td>111.50 (n/a)</td><td>95.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (+9.97%)</td><td>0.04 (+2.97%)</td><td>0.04 (+5.60%)</td><td>0.03 (+1.22%)</td><td>0.01 (+2.69%)</td><td>225.70 (-1.23%)</td><td>171.86 (-3.84%)</td><td>175.10 (-5.30%)</td><td>105.60 (-9.12%)</td><td>44.18 (-14.57%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>228.50 (n/a)</td><td>178.72 (n/a)</td><td>184.90 (n/a)</td><td>116.20 (n/a)</td><td>51.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (-3.44%)</td><td>0.04 (+7.12%)</td><td>0.04 <b>(+21.29%)</b></td><td>0.03 (+2.16%)</td><td>0.01 (-15.90%)</td><td>218.10 (-2.11%)</td><td>161.86 (-7.81%)</td><td>159.70 (-17.55%)</td><td>127.00 (+3.59%)</td><td>35.47 (-13.02%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>175.58 (n/a)</td><td>193.70 (n/a)</td><td>122.60 (n/a)</td><td>40.78 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (-1.98%)</td><td>0.04 (+4.29%)</td><td>0.04 (+1.96%)</td><td>0.03 (+10.14%)</td><td>0.00 (-19.84%)</td><td>208.40 (-9.23%)</td><td>174.64 (-4.87%)</td><td>169.10 (-1.91%)</td><td>156.60 (+2.02%)</td><td>21.46 <b>(-27.35%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>183.58 (n/a)</td><td>172.40 (n/a)</td><td>153.50 (n/a)</td><td>29.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 <b>(+33.98%)</b></td><td>0.04 (+9.92%)</td><td>0.03 (+7.73%)</td><td>0.03 (-8.26%)</td><td>0.01 <b>(+90.32%)</b></td><td>229.30 (+8.98%)</td><td>172.90 (-5.07%)</td><td>178.80 (-7.17%)</td><td>103.70 <b>(-25.34%)</b></td><td>45.34 <b>(+43.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>182.14 (n/a)</td><td>192.60 (n/a)</td><td>138.90 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (+16.53%)</td><td>0.08 (+0.20%)</td><td>0.08 (-9.06%)</td><td>0.06 (-2.99%)</td><td>0.02 <b>(+43.10%)</b></td><td>193.50 (+3.09%)</td><td>154.04 (+1.21%)</td><td>159.00 (+9.96%)</td><td>111.90 (-14.19%)</td><td>29.90 <b>(+24.82%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>187.70 (n/a)</td><td>152.20 (n/a)</td><td>144.60 (n/a)</td><td>130.40 (n/a)</td><td>23.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (-9.02%)</td><td>0.08 (-3.00%)</td><td>0.08 (-3.10%)</td><td>0.07 (+9.77%)</td><td>0.01 <b>(-47.74%)</b></td><td>165.90 (-8.90%)</td><td>155.58 (+1.94%)</td><td>157.50 (+3.14%)</td><td>137.70 (+9.90%)</td><td>11.09 <b>(-47.93%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>152.62 (n/a)</td><td>152.70 (n/a)</td><td>125.30 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (-17.02%)</td><td>0.07 (-17.28%)</td><td>0.07 <b>(-23.44%)</b></td><td>0.07 (-2.03%)</td><td>0.01 <b>(-45.23%)</b></td><td>188.20 (+2.06%)</td><td>170.12 (+19.00%)</td><td>171.40 <b>(+30.64%)</b></td><td>143.80 <b>(+20.54%)</b></td><td>17.79 <b>(-33.03%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.40 (n/a)</td><td>142.96 (n/a)</td><td>131.20 (n/a)</td><td>119.30 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 <b>(-30.92%)</b></td><td>0.07 (-19.46%)</td><td>0.06 (-19.60%)</td><td>0.06 (-3.98%)</td><td>0.00 <b>(-76.75%)</b></td><td>192.70 (+4.11%)</td><td>185.24 <b>(+22.01%)</b></td><td>189.20 <b>(+24.39%)</b></td><td>173.70 <b>(+44.75%)</b></td><td>8.17 <b>(-64.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>185.10 (n/a)</td><td>151.82 (n/a)</td><td>152.10 (n/a)</td><td>120.00 (n/a)</td><td>23.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (+10.05%)</td><td>0.08 (-2.57%)</td><td>0.07 (-13.78%)</td><td>0.06 (-0.22%)</td><td>0.02 <b>(+36.53%)</b></td><td>216.50 (+0.23%)</td><td>168.64 (+4.33%)</td><td>179.00 (+16.01%)</td><td>117.60 (-9.12%)</td><td>37.95 (+17.51%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>161.64 (n/a)</td><td>154.30 (n/a)</td><td>129.40 (n/a)</td><td>32.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 <b>(-25.95%)</b></td><td>0.07 (-17.20%)</td><td>0.07 (-14.53%)</td><td>0.06 <b>(-20.07%)</b></td><td>0.00 <b>(-47.16%)</b></td><td>203.00 <b>(+25.08%)</b></td><td>182.84 <b>(+20.27%)</b></td><td>183.70 (+17.01%)</td><td>171.40 <b>(+35.07%)</b></td><td>12.89 (-9.55%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>162.30 (n/a)</td><td>152.02 (n/a)</td><td>157.00 (n/a)</td><td>126.90 (n/a)</td><td>14.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 <b>(-31.28%)</b></td><td>0.06 <b>(-25.92%)</b></td><td>0.06 <b>(-24.19%)</b></td><td>0.05 (-5.66%)</td><td>0.01 <b>(-66.43%)</b></td><td>226.40 (+5.99%)</td><td>206.92 <b>(+30.12%)</b></td><td>208.90 <b>(+31.88%)</b></td><td>175.30 <b>(+45.60%)</b></td><td>20.10 <b>(-47.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.60 (n/a)</td><td>159.02 (n/a)</td><td>158.40 (n/a)</td><td>120.40 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (-19.92%)</td><td>0.07 (-17.24%)</td><td>0.07 (-14.55%)</td><td>0.05 <b>(-26.00%)</b></td><td>0.01 <b>(+20.30%)</b></td><td>231.20 <b>(+35.13%)</b></td><td>190.78 <b>(+21.58%)</b></td><td>183.20 (+16.99%)</td><td>174.90 <b>(+24.84%)</b></td><td>23.30 <b>(+107.07%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>171.10 (n/a)</td><td>156.92 (n/a)</td><td>156.60 (n/a)</td><td>140.10 (n/a)</td><td>11.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (-15.29%)</td><td>0.14 (-9.00%)</td><td>0.14 (-12.98%)</td><td>0.12 (-1.74%)</td><td>0.01 <b>(-51.76%)</b></td><td>205.20 (+1.79%)</td><td>174.48 (+7.57%)</td><td>172.70 (+14.90%)</td><td>155.40 (+18.00%)</td><td>18.68 <b>(-41.33%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>201.60 (n/a)</td><td>162.20 (n/a)</td><td>150.30 (n/a)</td><td>131.70 (n/a)</td><td>31.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.17 (-14.82%)</td><td>0.14 (-17.49%)</td><td>0.14 <b>(-21.99%)</b></td><td>0.10 (-19.44%)</td><td>0.02 (-10.59%)</td><td>234.10 <b>(+24.13%)</b></td><td>175.62 <b>(+21.69%)</b></td><td>169.50 <b>(+28.21%)</b></td><td>143.50 (+17.43%)</td><td>34.88 <b>(+31.45%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>188.60 (n/a)</td><td>144.32 (n/a)</td><td>132.20 (n/a)</td><td>122.20 (n/a)</td><td>26.54 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (-8.77%)</td><td>0.15 (+10.82%)</td><td>0.15 (+13.56%)</td><td>0.11 (+7.38%)</td><td>0.04 (-14.56%)</td><td>218.00 (-6.88%)</td><td>166.22 (-11.03%)</td><td>168.30 (-11.98%)</td><td>128.40 (+9.65%)</td><td>38.49 (-13.20%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>234.10 (n/a)</td><td>186.82 (n/a)</td><td>191.20 (n/a)</td><td>117.10 (n/a)</td><td>44.35 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.17 (-7.34%)</td><td>0.15 (+1.84%)</td><td>0.16 (+8.34%)</td><td>0.11 <b>(+71.21%)</b></td><td>0.02 <b>(-50.99%)</b></td><td>215.20 <b>(-41.60%)</b></td><td>170.96 (-12.75%)</td><td>157.40 (-7.68%)</td><td>140.80 (+7.89%)</td><td>29.76 <b>(-69.83%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>368.50 (n/a)</td><td>195.94 (n/a)</td><td>170.50 (n/a)</td><td>130.50 (n/a)</td><td>98.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 (+19.99%)</td><td>0.14 (+10.88%)</td><td>0.14 (+13.70%)</td><td>0.11 (+6.79%)</td><td>0.04 <b>(+36.24%)</b></td><td>228.00 (-6.37%)</td><td>180.08 (-8.51%)</td><td>176.60 (-12.05%)</td><td>117.50 (-16.67%)</td><td>41.47 (+4.12%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>243.50 (n/a)</td><td>196.82 (n/a)</td><td>200.80 (n/a)</td><td>141.00 (n/a)</td><td>39.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (+2.43%)</td><td>0.14 (+8.79%)</td><td>0.13 (+1.58%)</td><td>0.11 (+13.67%)</td><td>0.03 (-0.17%)</td><td>224.70 (-12.02%)</td><td>177.88 (-8.65%)</td><td>191.90 (-1.59%)</td><td>128.90 (-2.35%)</td><td>39.45 (-14.16%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>255.40 (n/a)</td><td>194.72 (n/a)</td><td>195.00 (n/a)</td><td>132.00 (n/a)</td><td>45.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (-15.32%)</td><td>0.13 (+2.33%)</td><td>0.13 (+8.75%)</td><td>0.11 (+2.80%)</td><td>0.01 <b>(-49.68%)</b></td><td>223.70 (-2.70%)</td><td>191.18 (-4.12%)</td><td>189.30 (-8.06%)</td><td>168.40 (+18.01%)</td><td>20.36 <b>(-38.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>229.90 (n/a)</td><td>199.40 (n/a)</td><td>205.90 (n/a)</td><td>142.70 (n/a)</td><td>33.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 <b>(-26.04%)</b></td><td>0.12 <b>(-25.50%)</b></td><td>0.11 <b>(-26.33%)</b></td><td>0.10 <b>(-29.01%)</b></td><td>0.02 (-2.75%)</td><td>246.10 <b>(+40.87%)</b></td><td>213.80 <b>(+35.28%)</b></td><td>217.60 <b>(+35.75%)</b></td><td>179.50 <b>(+35.17%)</b></td><td>31.53 <b>(+84.12%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>174.70 (n/a)</td><td>158.04 (n/a)</td><td>160.30 (n/a)</td><td>132.80 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.35 (-11.60%)</td><td>0.32 (-5.52%)</td><td>0.34 (-2.24%)</td><td>0.26 (+1.72%)</td><td>0.04 <b>(-32.10%)</b></td><td>188.10 (-1.72%)</td><td>155.78 (+4.49%)</td><td>143.70 (+2.28%)</td><td>139.80 (+13.11%)</td><td>21.04 <b>(-24.96%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>191.40 (n/a)</td><td>149.08 (n/a)</td><td>140.50 (n/a)</td><td>123.60 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.45 (+18.86%)</td><td>0.31 (+5.95%)</td><td>0.28 (-0.60%)</td><td>0.25 <b>(+24.04%)</b></td><td>0.08 (+9.93%)</td><td>195.80 (-19.36%)</td><td>163.54 (-6.53%)</td><td>174.30 (+0.58%)</td><td>109.40 (-15.91%)</td><td>33.05 <b>(-27.03%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>242.80 (n/a)</td><td>174.96 (n/a)</td><td>173.30 (n/a)</td><td>130.10 (n/a)</td><td>45.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.36 (-18.87%)</td><td>0.28 (-15.37%)</td><td>0.26 (-14.53%)</td><td>0.23 (-11.92%)</td><td>0.05 <b>(-28.44%)</b></td><td>216.10 (+13.56%)</td><td>179.54 (+16.95%)</td><td>188.90 (+17.04%)</td><td>136.70 <b>(+23.26%)</b></td><td>32.07 (+0.17%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>190.30 (n/a)</td><td>153.52 (n/a)</td><td>161.40 (n/a)</td><td>110.90 (n/a)</td><td>32.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.38 (-6.32%)</td><td>0.34 (+9.72%)</td><td>0.34 (+7.67%)</td><td>0.27 <b>(+31.94%)</b></td><td>0.04 <b>(-44.27%)</b></td><td>181.70 <b>(-24.20%)</b></td><td>148.34 (-12.13%)</td><td>143.20 (-7.13%)</td><td>130.60 (+6.70%)</td><td>19.81 <b>(-55.11%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>239.70 (n/a)</td><td>168.82 (n/a)</td><td>154.20 (n/a)</td><td>122.40 (n/a)</td><td>44.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 <b>(-20.12%)</b></td><td>0.26 (-12.23%)</td><td>0.25 (-18.96%)</td><td>0.22 <b>(+31.45%)</b></td><td>0.03 <b>(-62.85%)</b></td><td>220.50 <b>(-23.94%)</b></td><td>191.72 (+6.27%)</td><td>196.80 <b>(+23.39%)</b></td><td>162.00 <b>(+25.19%)</b></td><td>21.91 <b>(-66.01%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>289.90 (n/a)</td><td>180.40 (n/a)</td><td>159.50 (n/a)</td><td>129.40 (n/a)</td><td>64.47 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 <b>(-25.27%)</b></td><td>0.24 (-16.56%)</td><td>0.25 (-10.73%)</td><td>0.19 <b>(-25.57%)</b></td><td>0.03 <b>(-28.07%)</b></td><td>263.90 <b>(+34.37%)</b></td><td>205.72 (+19.70%)</td><td>197.00 (+12.00%)</td><td>179.80 <b>(+33.78%)</b></td><td>33.81 <b>(+31.13%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>196.40 (n/a)</td><td>171.86 (n/a)</td><td>175.90 (n/a)</td><td>134.40 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (-13.82%)</td><td>0.25 (-2.73%)</td><td>0.26 (+1.37%)</td><td>0.23 <b>(+22.67%)</b></td><td>0.02 <b>(-62.30%)</b></td><td>210.50 (-18.51%)</td><td>195.46 (+0.16%)</td><td>191.40 (-1.34%)</td><td>179.00 (+16.08%)</td><td>14.12 <b>(-64.39%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>258.30 (n/a)</td><td>195.14 (n/a)</td><td>194.00 (n/a)</td><td>154.20 (n/a)</td><td>39.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.36 (+4.00%)</td><td>0.30 (+5.08%)</td><td>0.29 (+18.59%)</td><td>0.24 (-1.42%)</td><td>0.05 (-12.55%)</td><td>205.50 (+1.43%)</td><td>168.58 (-5.49%)</td><td>166.90 (-15.71%)</td><td>134.70 (-3.85%)</td><td>25.38 (-16.34%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>202.60 (n/a)</td><td>178.38 (n/a)</td><td>198.00 (n/a)</td><td>140.10 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (-4.73%)</td><td>0.02 (-7.32%)</td><td>0.02 (-8.53%)</td><td>0.01 <b>(-25.69%)</b></td><td>0.00 <b>(+37.35%)</b></td><td>250.10 <b>(+34.53%)</b></td><td>177.46 (+10.31%)</td><td>164.10 (+9.33%)</td><td>148.90 (+4.93%)</td><td>41.74 <b>(+96.64%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>185.90 (n/a)</td><td>160.88 (n/a)</td><td>150.10 (n/a)</td><td>141.90 (n/a)</td><td>21.22 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (+8.77%)</td><td>0.02 (+2.14%)</td><td>0.02 (-9.44%)</td><td>0.01 (+12.69%)</td><td>0.00 (-13.37%)</td><td>200.80 (-11.27%)</td><td>165.04 (-3.38%)</td><td>168.20 (+10.44%)</td><td>128.90 (-8.06%)</td><td>26.15 <b>(-29.47%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>226.30 (n/a)</td><td>170.82 (n/a)</td><td>152.30 (n/a)</td><td>140.20 (n/a)</td><td>37.07 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (-16.92%)</td><td>0.02 (+4.02%)</td><td>0.02 (+17.69%)</td><td>0.01 <b>(+27.18%)</b></td><td>0.00 <b>(-62.81%)</b></td><td>199.40 <b>(-21.40%)</b></td><td>164.64 (-11.04%)</td><td>163.90 (-15.03%)</td><td>142.40 <b>(+20.37%)</b></td><td>21.59 <b>(-63.68%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>253.70 (n/a)</td><td>185.08 (n/a)</td><td>192.90 (n/a)</td><td>118.30 (n/a)</td><td>59.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (-17.47%)</td><td>0.01 (+1.40%)</td><td>0.01 (+11.19%)</td><td>0.01 (-13.40%)</td><td>0.00 <b>(-20.53%)</b></td><td>258.70 (+15.49%)</td><td>188.40 (-1.94%)</td><td>183.80 (-10.03%)</td><td>143.60 <b>(+21.18%)</b></td><td>47.58 (+13.34%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>224.00 (n/a)</td><td>192.12 (n/a)</td><td>204.30 (n/a)</td><td>118.50 (n/a)</td><td>41.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (+2.83%)</td><td>0.02 (+4.29%)</td><td>0.02 (+9.06%)</td><td>0.01 (-11.96%)</td><td>0.00 (+12.18%)</td><td>230.80 (+13.58%)</td><td>173.98 (-3.04%)</td><td>172.40 (-8.30%)</td><td>123.50 (-2.76%)</td><td>38.32 <b>(+27.27%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>203.20 (n/a)</td><td>179.44 (n/a)</td><td>188.00 (n/a)</td><td>127.00 (n/a)</td><td>30.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (+15.11%)</td><td>0.01 (+11.90%)</td><td>0.01 (+11.51%)</td><td>0.01 (+17.41%)</td><td>0.00 (+6.26%)</td><td>235.70 (-14.85%)</td><td>187.10 (-11.10%)</td><td>184.10 (-10.33%)</td><td>144.50 (-13.11%)</td><td>33.97 <b>(-21.56%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>276.80 (n/a)</td><td>210.46 (n/a)</td><td>205.30 (n/a)</td><td>166.30 (n/a)</td><td>43.31 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (+13.64%)</td><td>0.02 (+8.78%)</td><td>0.02 (+10.11%)</td><td>0.01 (-7.24%)</td><td>0.00 <b>(+81.07%)</b></td><td>214.80 (+7.78%)</td><td>173.06 (-6.48%)</td><td>172.90 (-9.19%)</td><td>136.50 (-12.05%)</td><td>30.95 <b>(+72.28%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>199.30 (n/a)</td><td>185.06 (n/a)</td><td>190.40 (n/a)</td><td>155.20 (n/a)</td><td>17.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (+19.35%)</td><td>0.01 (+17.47%)</td><td>0.01 (+13.17%)</td><td>0.01 <b>(+21.20%)</b></td><td>0.00 (+16.93%)</td><td>248.60 (-17.49%)</td><td>199.90 (-15.00%)</td><td>193.00 (-11.63%)</td><td>159.00 (-16.18%)</td><td>34.82 (-19.90%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>301.30 (n/a)</td><td>235.18 (n/a)</td><td>218.40 (n/a)</td><td>189.70 (n/a)</td><td>43.47 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (-18.35%)</td><td>0.03 (-18.57%)</td><td>0.03 <b>(-22.43%)</b></td><td>0.03 (-1.95%)</td><td>0.01 <b>(-39.41%)</b></td><td>209.90 (+1.99%)</td><td>175.94 (+19.64%)</td><td>178.40 <b>(+28.90%)</b></td><td>134.80 <b>(+22.55%)</b></td><td>27.92 <b>(-26.24%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>147.06 (n/a)</td><td>138.40 (n/a)</td><td>110.00 (n/a)</td><td>37.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 <b>(+38.35%)</b></td><td>0.03 (-5.36%)</td><td>0.03 (-8.43%)</td><td>0.02 <b>(-41.89%)</b></td><td>0.02 <b>(+152.51%)</b></td><td>326.40 <b>(+72.06%)</b></td><td>193.34 <b>(+21.83%)</b></td><td>183.80 (+9.21%)</td><td>92.90 <b>(-27.70%)</b></td><td>86.38 <b>(+217.94%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>158.70 (n/a)</td><td>168.30 (n/a)</td><td>128.50 (n/a)</td><td>27.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (-8.17%)</td><td>0.03 (+1.92%)</td><td>0.03 (+17.56%)</td><td>0.03 (+17.13%)</td><td>0.00 <b>(-44.98%)</b></td><td>194.10 (-14.64%)</td><td>173.54 (-4.49%)</td><td>168.20 (-14.92%)</td><td>145.40 (+8.91%)</td><td>20.24 <b>(-47.23%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>181.70 (n/a)</td><td>197.70 (n/a)</td><td>133.50 (n/a)</td><td>38.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 <b>(+49.64%)</b></td><td>0.03 <b>(+28.59%)</b></td><td>0.03 <b>(+23.32%)</b></td><td>0.02 <b>(+38.74%)</b></td><td>0.01 <b>(+64.16%)</b></td><td>215.10 <b>(-27.94%)</b></td><td>170.14 <b>(-21.52%)</b></td><td>167.50 (-18.89%)</td><td>114.40 <b>(-33.14%)</b></td><td>38.19 <b>(-23.72%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>298.50 (n/a)</td><td>216.80 (n/a)</td><td>206.50 (n/a)</td><td>171.10 (n/a)</td><td>50.07 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (+19.91%)</td><td>0.03 (+0.32%)</td><td>0.03 (-7.73%)</td><td>0.02 (+16.81%)</td><td>0.01 <b>(+24.09%)</b></td><td>212.90 (-14.39%)</td><td>175.32 (-0.14%)</td><td>185.10 (+8.37%)</td><td>116.90 (-16.62%)</td><td>36.55 (-15.88%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.70 (n/a)</td><td>175.56 (n/a)</td><td>170.80 (n/a)</td><td>140.20 (n/a)</td><td>43.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-16.72%)</td><td>0.03 (-14.09%)</td><td>0.02 (-17.82%)</td><td>0.02 (-6.64%)</td><td>0.00 <b>(-25.77%)</b></td><td>222.90 (+7.11%)</td><td>202.56 (+15.93%)</td><td>215.10 <b>(+21.66%)</b></td><td>173.00 <b>(+20.06%)</b></td><td>22.08 (-4.06%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.10 (n/a)</td><td>174.72 (n/a)</td><td>176.80 (n/a)</td><td>144.10 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 <b>(-29.26%)</b></td><td>0.03 (-18.19%)</td><td>0.03 (-12.23%)</td><td>0.02 (-9.14%)</td><td>0.00 <b>(-64.81%)</b></td><td>235.70 (+10.09%)</td><td>203.74 (+18.85%)</td><td>199.40 (+13.94%)</td><td>185.70 <b>(+41.32%)</b></td><td>19.73 <b>(-44.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>171.42 (n/a)</td><td>175.00 (n/a)</td><td>131.40 (n/a)</td><td>35.28 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+7.74%)</td><td>0.02 (+3.78%)</td><td>0.02 (-7.04%)</td><td>0.02 (+8.02%)</td><td>0.00 (+1.91%)</td><td>270.10 (-7.44%)</td><td>217.58 (-3.99%)</td><td>227.40 (+7.57%)</td><td>172.00 (-7.18%)</td><td>40.24 (-12.96%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>291.80 (n/a)</td><td>226.62 (n/a)</td><td>211.40 (n/a)</td><td>185.30 (n/a)</td><td>46.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (-8.23%)</td><td>0.05 (-12.86%)</td><td>0.05 (-13.71%)</td><td>0.03 <b>(-27.86%)</b></td><td>0.01 <b>(+28.94%)</b></td><td>331.20 <b>(+38.64%)</b></td><td>216.20 (+18.86%)</td><td>198.70 (+15.93%)</td><td>166.30 (+8.98%)</td><td>66.34 <b>(+97.10%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>238.90 (n/a)</td><td>181.90 (n/a)</td><td>171.40 (n/a)</td><td>152.60 (n/a)</td><td>33.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (-7.08%)</td><td>0.05 (-1.03%)</td><td>0.05 (-12.15%)</td><td>0.04 (+17.57%)</td><td>0.01 <b>(-34.13%)</b></td><td>235.10 (-14.94%)</td><td>204.32 (-1.63%)</td><td>206.00 (+13.81%)</td><td>173.00 (+7.65%)</td><td>30.18 <b>(-40.50%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>276.40 (n/a)</td><td>207.70 (n/a)</td><td>181.00 (n/a)</td><td>160.70 (n/a)</td><td>50.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (-13.66%)</td><td>0.06 (-0.24%)</td><td>0.06 (+7.98%)</td><td>0.05 <b>(+37.05%)</b></td><td>0.01 <b>(-60.20%)</b></td><td>212.70 <b>(-27.01%)</b></td><td>178.34 (-8.21%)</td><td>181.10 (-7.41%)</td><td>146.90 (+15.85%)</td><td>24.90 <b>(-64.23%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>291.40 (n/a)</td><td>194.30 (n/a)</td><td>195.60 (n/a)</td><td>126.80 (n/a)</td><td>69.63 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (+5.22%)</td><td>0.06 (+7.01%)</td><td>0.06 (+6.36%)</td><td>0.05 (+9.38%)</td><td>0.01 (-5.09%)</td><td>205.40 (-8.59%)</td><td>178.38 (-6.93%)</td><td>165.80 (-5.96%)</td><td>152.30 (-4.93%)</td><td>24.44 (-17.86%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>191.66 (n/a)</td><td>176.30 (n/a)</td><td>160.20 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (+16.09%)</td><td>0.06 (+17.11%)</td><td>0.06 (+14.55%)</td><td>0.05 (+15.43%)</td><td>0.01 (+18.24%)</td><td>195.90 (-13.36%)</td><td>174.46 (-14.59%)</td><td>169.40 (-12.68%)</td><td>161.10 (-13.85%)</td><td>15.37 (-13.26%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>226.10 (n/a)</td><td>204.26 (n/a)</td><td>194.00 (n/a)</td><td>187.00 (n/a)</td><td>17.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 <b>(+21.38%)</b></td><td>0.06 (+8.67%)</td><td>0.06 (+2.18%)</td><td>0.05 (+19.17%)</td><td>0.01 (+12.18%)</td><td>197.90 (-16.07%)</td><td>171.24 (-8.20%)</td><td>173.80 (-2.14%)</td><td>139.60 (-17.59%)</td><td>20.91 <b>(-25.05%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>186.54 (n/a)</td><td>177.60 (n/a)</td><td>169.40 (n/a)</td><td>27.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (+12.42%)</td><td>0.06 (+4.77%)</td><td>0.06 (+6.36%)</td><td>0.05 (+8.10%)</td><td>0.01 (+7.72%)</td><td>217.90 (-7.51%)</td><td>173.84 (-4.58%)</td><td>172.50 (-5.99%)</td><td>127.20 (-11.05%)</td><td>36.83 (-7.36%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>235.60 (n/a)</td><td>182.18 (n/a)</td><td>183.50 (n/a)</td><td>143.00 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 <b>(+45.10%)</b></td><td>0.05 <b>(+24.60%)</b></td><td>0.05 (+9.10%)</td><td>0.05 <b>(+31.00%)</b></td><td>0.01 <b>(+81.25%)</b></td><td>232.40 <b>(-23.68%)</b></td><td>197.18 (-18.93%)</td><td>207.10 (-8.32%)</td><td>147.20 <b>(-31.12%)</b></td><td>33.37 (-7.79%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.50 (n/a)</td><td>243.22 (n/a)</td><td>225.90 (n/a)</td><td>213.70 (n/a)</td><td>36.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (+15.90%)</td><td>0.14 <b>(+22.67%)</b></td><td>0.14 <b>(+32.13%)</b></td><td>0.12 <b>(+26.05%)</b></td><td>0.01 <b>(-30.80%)</b></td><td>171.30 <b>(-20.69%)</b></td><td>154.42 (-19.09%)</td><td>150.70 <b>(-24.35%)</b></td><td>142.50 (-13.74%)</td><td>10.73 <b>(-51.49%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>190.86 (n/a)</td><td>199.20 (n/a)</td><td>165.20 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (+2.46%)</td><td>0.10 (-14.82%)</td><td>0.09 <b>(-24.21%)</b></td><td>0.07 (-4.87%)</td><td>0.03 (+9.96%)</td><td>289.60 (+5.12%)</td><td>227.36 (+18.07%)</td><td>236.20 <b>(+31.96%)</b></td><td>150.60 (-2.40%)</td><td>50.73 (+4.81%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>275.50 (n/a)</td><td>192.56 (n/a)</td><td>179.00 (n/a)</td><td>154.30 (n/a)</td><td>48.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (-2.19%)</td><td>0.12 (+2.12%)</td><td>0.12 (+7.64%)</td><td>0.09 (-12.62%)</td><td>0.02 (+10.01%)</td><td>232.30 (+14.43%)</td><td>173.94 (-1.18%)</td><td>171.30 (-7.10%)</td><td>139.20 (+2.28%)</td><td>35.67 <b>(+32.00%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>203.00 (n/a)</td><td>176.02 (n/a)</td><td>184.40 (n/a)</td><td>136.10 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (-9.26%)</td><td>0.12 (-2.76%)</td><td>0.13 (+5.76%)</td><td>0.10 (-9.11%)</td><td>0.01 (+2.68%)</td><td>218.70 (+10.01%)</td><td>180.78 (+3.14%)</td><td>167.50 (-5.42%)</td><td>162.30 (+10.18%)</td><td>24.38 <b>(+24.15%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>175.28 (n/a)</td><td>177.10 (n/a)</td><td>147.30 (n/a)</td><td>19.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 <b>(+33.21%)</b></td><td>0.15 <b>(+27.44%)</b></td><td>0.16 <b>(+42.70%)</b></td><td>0.11 <b>(+21.93%)</b></td><td>0.04 <b>(+31.59%)</b></td><td>190.90 (-18.00%)</td><td>147.42 <b>(-21.14%)</b></td><td>132.20 <b>(-29.94%)</b></td><td>103.90 <b>(-24.93%)</b></td><td>38.57 (-15.42%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>232.80 (n/a)</td><td>186.94 (n/a)</td><td>188.70 (n/a)</td><td>138.40 (n/a)</td><td>45.60 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 <b>(+22.00%)</b></td><td>0.12 (+7.85%)</td><td>0.12 (+6.92%)</td><td>0.10 (-0.03%)</td><td>0.02 <b>(+101.74%)</b></td><td>207.90 (+0.05%)</td><td>176.58 (-5.92%)</td><td>181.70 (-6.44%)</td><td>138.50 (-18.05%)</td><td>27.37 <b>(+66.55%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>187.70 (n/a)</td><td>194.20 (n/a)</td><td>169.00 (n/a)</td><td>16.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 <b>(+29.37%)</b></td><td>0.13 (+14.45%)</td><td>0.12 (+12.96%)</td><td>0.11 (+8.82%)</td><td>0.02 <b>(+115.21%)</b></td><td>191.80 (-8.10%)</td><td>167.34 (-11.37%)</td><td>170.50 (-11.47%)</td><td>129.50 <b>(-22.69%)</b></td><td>25.60 <b>(+54.32%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>188.80 (n/a)</td><td>192.60 (n/a)</td><td>167.50 (n/a)</td><td>16.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (+1.98%)</td><td>0.10 (+1.80%)</td><td>0.10 (+2.23%)</td><td>0.09 (+8.20%)</td><td>0.01 (-1.49%)</td><td>236.30 (-7.59%)</td><td>211.76 (-1.89%)</td><td>206.40 (-2.18%)</td><td>176.90 (-1.94%)</td><td>24.62 (-9.60%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>255.70 (n/a)</td><td>215.84 (n/a)</td><td>211.00 (n/a)</td><td>180.40 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>156.16 (n/a)</td><td>140.50 (n/a)</td><td>130.20 (n/a)</td><td>27.07 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>168.80 (n/a)</td><td>147.26 (n/a)</td><td>163.50 (n/a)</td><td>106.20 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>168.76 (n/a)</td><td>161.30 (n/a)</td><td>128.10 (n/a)</td><td>37.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.00 (n/a)</td><td>176.38 (n/a)</td><td>167.30 (n/a)</td><td>140.70 (n/a)</td><td>40.22 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>240.80 (n/a)</td><td>175.88 (n/a)</td><td>169.70 (n/a)</td><td>129.00 (n/a)</td><td>41.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.70 (n/a)</td><td>175.84 (n/a)</td><td>166.70 (n/a)</td><td>135.10 (n/a)</td><td>34.81 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>230.90 (n/a)</td><td>171.94 (n/a)</td><td>157.90 (n/a)</td><td>144.80 (n/a)</td><td>34.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>273.60 (n/a)</td><td>236.12 (n/a)</td><td>229.10 (n/a)</td><td>199.60 (n/a)</td><td>28.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>202.40 (n/a)</td><td>159.04 (n/a)</td><td>161.70 (n/a)</td><td>129.70 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>174.24 (n/a)</td><td>175.30 (n/a)</td><td>151.10 (n/a)</td><td>16.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>186.66 (n/a)</td><td>182.30 (n/a)</td><td>161.40 (n/a)</td><td>20.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>202.80 (n/a)</td><td>174.00 (n/a)</td><td>191.60 (n/a)</td><td>134.80 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.39 (+2.97%)</td><td>0.29 (-12.00%)</td><td>0.27 <b>(-24.45%)</b></td><td>0.24 (-4.69%)</td><td>0.06 <b>(+24.25%)</b></td><td>204.30 (+4.88%)</td><td>172.12 (+14.75%)</td><td>185.10 <b>(+32.31%)</b></td><td>125.20 (-2.87%)</td><td>31.30 <b>(+20.64%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>194.80 (n/a)</td><td>150.00 (n/a)</td><td>139.90 (n/a)</td><td>128.90 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.29 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>375.30 (n/a)</td><td>212.82 (n/a)</td><td>169.50 (n/a)</td><td>162.30 (n/a)</td><td>91.49 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>197.30 (n/a)</td><td>164.20 (n/a)</td><td>177.00 (n/a)</td><td>131.90 (n/a)</td><td>28.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>232.90 (n/a)</td><td>199.30 (n/a)</td><td>198.30 (n/a)</td><td>148.80 (n/a)</td><td>33.27 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>215.70 (n/a)</td><td>198.70 (n/a)</td><td>214.70 (n/a)</td><td>167.20 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.40 (n/a)</td><td>184.54 (n/a)</td><td>172.60 (n/a)</td><td>162.70 (n/a)</td><td>30.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.20 (n/a)</td><td>196.46 (n/a)</td><td>188.00 (n/a)</td><td>158.10 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>183.16 (n/a)</td><td>195.70 (n/a)</td><td>144.40 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>159.70 (n/a)</td><td>156.90 (n/a)</td><td>139.40 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>180.58 (n/a)</td><td>182.40 (n/a)</td><td>150.40 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>224.70 (n/a)</td><td>170.40 (n/a)</td><td>161.60 (n/a)</td><td>129.30 (n/a)</td><td>36.53 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.40 (n/a)</td><td>185.00 (n/a)</td><td>175.80 (n/a)</td><td>147.60 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>208.10 (n/a)</td><td>167.22 (n/a)</td><td>150.90 (n/a)</td><td>141.70 (n/a)</td><td>30.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.50 (n/a)</td><td>166.82 (n/a)</td><td>178.00 (n/a)</td><td>119.50 (n/a)</td><td>28.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>161.40 (n/a)</td><td>149.16 (n/a)</td><td>157.00 (n/a)</td><td>131.60 (n/a)</td><td>13.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>315.80 (n/a)</td><td>198.22 (n/a)</td><td>176.70 (n/a)</td><td>144.90 (n/a)</td><td>67.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>229.60 (n/a)</td><td>180.40 (n/a)</td><td>170.20 (n/a)</td><td>135.80 (n/a)</td><td>38.69 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>214.30 (n/a)</td><td>184.80 (n/a)</td><td>178.20 (n/a)</td><td>172.50 (n/a)</td><td>17.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>234.10 (n/a)</td><td>196.04 (n/a)</td><td>192.00 (n/a)</td><td>161.20 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>14.38 (-0.44%)</td><td>13.62 (+0.77%)</td><td>13.21 (+0.15%)</td><td>13.06 (+2.05%)</td><td>0.68 (-4.66%)</td><td>4267.00 (-2.00%)</td><td>4098.74 (-0.78%)</td><td>4217.80 (-0.15%)</td><td>3874.00 (+0.44%)</td><td>202.41 (-6.20%)</td><td>13858.35 (-0.44%)</td><td>13124.49 (+0.77%)</td><td>12728.63 (+0.15%)</td><td>12582.04 (+2.05%)</td><td>659.44 (-4.66%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.44 (n/a)</td><td>13.51 (n/a)</td><td>13.19 (n/a)</td><td>12.79 (n/a)</td><td>0.72 (n/a)</td><td>4354.30 (n/a)</td><td>4131.12 (n/a)</td><td>4224.20 (n/a)</td><td>3857.00 (n/a)</td><td>215.78 (n/a)</td><td>13919.33 (n/a)</td><td>13024.70 (n/a)</td><td>12709.40 (n/a)</td><td>12329.75 (n/a)</td><td>691.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>16.79 (+12.55%)</td><td>13.88 (-3.13%)</td><td>14.28 (-1.09%)</td><td>9.51 <b>(-29.53%)</b></td><td>2.70 <b>(+362.09%)</b></td><td>1378.90 <b>(+41.91%)</b></td><td>980.06 (+6.99%)</td><td>917.90 (+1.10%)</td><td>780.70 (-11.15%)</td><td>232.03 <b>(+510.57%)</b></td><td>11002.71 (+12.55%)</td><td>9095.52 (-3.13%)</td><td>9358.24 (-1.09%)</td><td>6229.62 <b>(-29.53%)</b></td><td>1768.58 <b>(+362.09%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.92 (n/a)</td><td>14.33 (n/a)</td><td>14.44 (n/a)</td><td>13.49 (n/a)</td><td>0.58 (n/a)</td><td>971.70 (n/a)</td><td>916.04 (n/a)</td><td>907.90 (n/a)</td><td>878.70 (n/a)</td><td>38.00 (n/a)</td><td>9775.74 (n/a)</td><td>9389.88 (n/a)</td><td>9461.27 (n/a)</td><td>8840.15 (n/a)</td><td>382.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>14.41 (+2.77%)</td><td>13.36 (-0.68%)</td><td>13.11 (-4.80%)</td><td>12.62 (+4.30%)</td><td>0.80 (+1.85%)</td><td>4415.60 (-4.12%)</td><td>4180.70 (+0.67%)</td><td>4248.20 (+5.04%)</td><td>3866.90 (-2.70%)</td><td>246.30 (-5.36%)</td><td>13883.66 (+2.77%)</td><td>12878.02 (-0.68%)</td><td>12637.62 (-4.80%)</td><td>12158.57 (+4.30%)</td><td>771.95 (+1.85%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.02 (n/a)</td><td>13.45 (n/a)</td><td>13.77 (n/a)</td><td>12.10 (n/a)</td><td>0.79 (n/a)</td><td>4605.50 (n/a)</td><td>4152.70 (n/a)</td><td>4044.20 (n/a)</td><td>3974.20 (n/a)</td><td>260.26 (n/a)</td><td>13509.08 (n/a)</td><td>12966.20 (n/a)</td><td>13274.94 (n/a)</td><td>11657.14 (n/a)</td><td>757.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>16.66 (+0.90%)</td><td>15.17 <b>(+22.22%)</b></td><td>15.13 <b>(+28.67%)</b></td><td>13.80 <b>(+66.91%)</b></td><td>1.02 <b>(-70.69%)</b></td><td>1294.50 <b>(-40.09%)</b></td><td>1181.76 <b>(-23.09%)</b></td><td>1180.20 <b>(-22.28%)</b></td><td>1071.70 (-0.89%)</td><td>78.80 <b>(-82.20%)</b></td><td>12523.43 (+0.90%)</td><td>11397.81 <b>(+22.22%)</b></td><td>11372.49 <b>(+28.67%)</b></td><td>10367.95 <b>(+66.91%)</b></td><td>763.55 <b>(-70.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>16.52 (n/a)</td><td>12.41 (n/a)</td><td>11.76 (n/a)</td><td>8.27 (n/a)</td><td>3.47 (n/a)</td><td>2160.70 (n/a)</td><td>1536.46 (n/a)</td><td>1518.50 (n/a)</td><td>1081.30 (n/a)</td><td>442.80 (n/a)</td><td>12412.12 (n/a)</td><td>9325.31 (n/a)</td><td>8838.69 (n/a)</td><td>6211.87 (n/a)</td><td>2605.27 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>11.08 (-1.19%)</td><td>10.75 (-1.78%)</td><td>10.63 (-4.47%)</td><td>10.49 (+1.07%)</td><td>0.28 <b>(-20.87%)</b></td><td>7809.30 (-1.06%)</td><td>7627.88 (+1.78%)</td><td>7703.90 (+4.68%)</td><td>7395.10 (+1.20%)</td><td>195.85 <b>(-20.74%)</b></td><td>14519.63 (-1.19%)</td><td>14084.05 (-1.78%)</td><td>13937.58 (-4.47%)</td><td>13749.61 (+1.07%)</td><td>364.26 <b>(-20.87%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>11.21 (n/a)</td><td>10.94 (n/a)</td><td>11.13 (n/a)</td><td>10.38 (n/a)</td><td>0.35 (n/a)</td><td>7892.60 (n/a)</td><td>7494.70 (n/a)</td><td>7359.70 (n/a)</td><td>7307.10 (n/a)</td><td>247.10 (n/a)</td><td>14694.47 (n/a)</td><td>14338.84 (n/a)</td><td>14589.53 (n/a)</td><td>13604.44 (n/a)</td><td>460.31 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.09 <b>(+29.73%)</b></td><td>13.00 (+17.33%)</td><td>13.11 (+19.09%)</td><td>11.39 (+6.19%)</td><td>1.45 <b>(+317.06%)</b></td><td>1886.70 (-5.83%)</td><td>1670.34 (-14.00%)</td><td>1639.10 (-16.03%)</td><td>1424.90 <b>(-22.92%)</b></td><td>182.79 <b>(+205.12%)</b></td><td>12056.70 <b>(+29.73%)</b></td><td>10386.46 (+17.33%)</td><td>10481.22 (+19.09%)</td><td>9105.55 (+6.19%)</td><td>1162.32 <b>(+317.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>11.63 (n/a)</td><td>11.08 (n/a)</td><td>11.01 (n/a)</td><td>10.73 (n/a)</td><td>0.35 (n/a)</td><td>2003.50 (n/a)</td><td>1942.28 (n/a)</td><td>1952.00 (n/a)</td><td>1848.50 (n/a)</td><td>59.91 (n/a)</td><td>9294.00 (n/a)</td><td>8852.20 (n/a)</td><td>8801.35 (n/a)</td><td>8574.94 (n/a)</td><td>278.69 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>10.86 (-0.35%)</td><td>10.58 (-2.44%)</td><td>10.41 (-4.24%)</td><td>10.36 (-3.38%)</td><td>0.26 <b>(+252.86%)</b></td><td>7906.80 (+3.50%)</td><td>7745.46 (+2.55%)</td><td>7867.10 (+4.43%)</td><td>7541.10 (+0.36%)</td><td>185.75 <b>(+265.28%)</b></td><td>14238.47 (-0.35%)</td><td>13869.31 (-2.44%)</td><td>13648.54 (-4.24%)</td><td>13579.97 (-3.38%)</td><td>335.37 <b>(+252.85%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>10.90 (n/a)</td><td>10.85 (n/a)</td><td>10.87 (n/a)</td><td>10.72 (n/a)</td><td>0.07 (n/a)</td><td>7639.30 (n/a)</td><td>7553.08 (n/a)</td><td>7533.70 (n/a)</td><td>7514.40 (n/a)</td><td>50.85 (n/a)</td><td>14289.17 (n/a)</td><td>14216.47 (n/a)</td><td>14252.61 (n/a)</td><td>14055.53 (n/a)</td><td>95.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.43 (+14.12%)</td><td>3.50 (+13.77%)</td><td>3.25 (+10.25%)</td><td>2.69 (-1.11%)</td><td>0.78 <b>(+68.10%)</b></td><td>510.70 (+1.13%)</td><td>408.68 (-10.03%)</td><td>423.10 (-9.28%)</td><td>310.40 (-12.37%)</td><td>88.21 <b>(+49.90%)</b></td><td>864.86 (+14.12%)</td><td>682.99 (+13.77%)</td><td>634.46 (+10.25%)</td><td>525.64 (-1.11%)</td><td>152.31 <b>(+68.10%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.89 (n/a)</td><td>3.08 (n/a)</td><td>2.95 (n/a)</td><td>2.73 (n/a)</td><td>0.46 (n/a)</td><td>505.00 (n/a)</td><td>454.24 (n/a)</td><td>466.40 (n/a)</td><td>354.20 (n/a)</td><td>58.85 (n/a)</td><td>757.88 (n/a)</td><td>600.33 (n/a)</td><td>575.49 (n/a)</td><td>531.56 (n/a)</td><td>90.61 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.08 (+0.60%)</td><td>3.81 (+4.79%)</td><td>3.98 (+11.80%)</td><td>3.43 (+0.53%)</td><td>0.29 (+17.63%)</td><td>401.40 (-0.55%)</td><td>362.90 (-4.46%)</td><td>345.60 (-10.56%)</td><td>337.60 (-0.62%)</td><td>28.36 (+17.88%)</td><td>795.01 (+0.60%)</td><td>743.16 (+4.79%)</td><td>776.71 (+11.80%)</td><td>668.70 (+0.53%)</td><td>56.22 (+17.63%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.05 (n/a)</td><td>3.64 (n/a)</td><td>3.56 (n/a)</td><td>3.41 (n/a)</td><td>0.25 (n/a)</td><td>403.60 (n/a)</td><td>379.84 (n/a)</td><td>386.40 (n/a)</td><td>339.70 (n/a)</td><td>24.06 (n/a)</td><td>790.25 (n/a)</td><td>709.15 (n/a)</td><td>694.74 (n/a)</td><td>665.16 (n/a)</td><td>47.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.30 <b>(+30.00%)</b></td><td>5.42 <b>(+32.01%)</b></td><td>5.70 <b>(+49.68%)</b></td><td>3.41 (-3.67%)</td><td>1.80 <b>(+110.31%)</b></td><td>403.20 (+3.81%)</td><td>280.08 (-18.71%)</td><td>241.50 <b>(-33.20%)</b></td><td>188.50 <b>(-23.06%)</b></td><td>100.07 <b>(+73.57%)</b></td><td>1424.23 <b>(+30.00%)</b></td><td>1057.85 <b>(+32.01%)</b></td><td>1111.54 <b>(+49.68%)</b></td><td>665.69 (-3.67%)</td><td>351.58 <b>(+110.31%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.62 (n/a)</td><td>4.11 (n/a)</td><td>3.81 (n/a)</td><td>3.54 (n/a)</td><td>0.86 (n/a)</td><td>388.40 (n/a)</td><td>344.56 (n/a)</td><td>361.50 (n/a)</td><td>245.00 (n/a)</td><td>57.66 (n/a)</td><td>1095.59 (n/a)</td><td>801.34 (n/a)</td><td>742.63 (n/a)</td><td>691.08 (n/a)</td><td>167.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.80 <b>(+20.61%)</b></td><td>4.39 (+8.69%)</td><td>3.86 (+6.55%)</td><td>3.64 (+4.28%)</td><td>1.35 <b>(+48.17%)</b></td><td>377.70 (-4.09%)</td><td>331.66 (-5.86%)</td><td>357.00 (-6.15%)</td><td>202.30 (-17.09%)</td><td>72.91 (+15.61%)</td><td>1327.03 <b>(+20.61%)</b></td><td>855.77 (+8.69%)</td><td>751.99 (+6.55%)</td><td>710.77 (+4.28%)</td><td>264.10 <b>(+48.17%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.64 (n/a)</td><td>4.04 (n/a)</td><td>3.62 (n/a)</td><td>3.49 (n/a)</td><td>0.91 (n/a)</td><td>393.80 (n/a)</td><td>352.32 (n/a)</td><td>380.40 (n/a)</td><td>244.00 (n/a)</td><td>63.07 (n/a)</td><td>1100.22 (n/a)</td><td>787.33 (n/a)</td><td>705.73 (n/a)</td><td>681.59 (n/a)</td><td>178.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>5.49 <b>(+32.52%)</b></td><td>4.02 (+15.22%)</td><td>3.30 (+3.32%)</td><td>2.94 (-6.50%)</td><td>1.18 <b>(+164.92%)</b></td><td>468.00 (+6.95%)</td><td>365.64 (-8.52%)</td><td>416.70 (-3.21%)</td><td>250.50 <b>(-24.55%)</b></td><td>98.19 <b>(+106.37%)</b></td><td>1071.49 <b>(+32.52%)</b></td><td>783.36 (+15.22%)</td><td>644.24 (+3.32%)</td><td>573.63 (-6.50%)</td><td>230.00 <b>(+164.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.15 (n/a)</td><td>3.49 (n/a)</td><td>3.20 (n/a)</td><td>3.15 (n/a)</td><td>0.45 (n/a)</td><td>437.60 (n/a)</td><td>399.70 (n/a)</td><td>430.50 (n/a)</td><td>332.00 (n/a)</td><td>47.58 (n/a)</td><td>808.54 (n/a)</td><td>679.86 (n/a)</td><td>623.53 (n/a)</td><td>613.50 (n/a)</td><td>86.82 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.31 (-5.87%)</td><td>3.10 (-2.28%)</td><td>3.05 (+0.33%)</td><td>2.83 (-1.67%)</td><td>0.19 <b>(-33.06%)</b></td><td>486.40 (+1.69%)</td><td>445.74 (+2.01%)</td><td>450.70 (-0.33%)</td><td>415.90 (+6.23%)</td><td>27.56 <b>(-27.21%)</b></td><td>645.44 (-5.87%)</td><td>604.02 (-2.28%)</td><td>595.54 (+0.33%)</td><td>551.90 (-1.67%)</td><td>36.64 <b>(-33.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.52 (n/a)</td><td>3.17 (n/a)</td><td>3.04 (n/a)</td><td>2.88 (n/a)</td><td>0.28 (n/a)</td><td>478.30 (n/a)</td><td>436.94 (n/a)</td><td>452.20 (n/a)</td><td>391.50 (n/a)</td><td>37.87 (n/a)</td><td>685.67 (n/a)</td><td>618.14 (n/a)</td><td>593.57 (n/a)</td><td>561.28 (n/a)</td><td>54.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.18 (-12.83%)</td><td>3.03 (-3.62%)</td><td>3.06 (+0.29%)</td><td>2.87 (-0.02%)</td><td>0.14 <b>(-55.16%)</b></td><td>478.90 (+0.02%)</td><td>455.58 (+3.22%)</td><td>450.30 (-0.29%)</td><td>432.10 (+14.71%)</td><td>20.55 <b>(-47.33%)</b></td><td>621.21 (-12.83%)</td><td>590.14 (-3.62%)</td><td>596.07 (+0.29%)</td><td>560.48 (-0.02%)</td><td>26.50 <b>(-55.16%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.65 (n/a)</td><td>3.14 (n/a)</td><td>3.05 (n/a)</td><td>2.87 (n/a)</td><td>0.30 (n/a)</td><td>478.80 (n/a)</td><td>441.38 (n/a)</td><td>451.60 (n/a)</td><td>376.70 (n/a)</td><td>39.02 (n/a)</td><td>712.63 (n/a)</td><td>612.32 (n/a)</td><td>594.36 (n/a)</td><td>560.62 (n/a)</td><td>59.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.26 (-17.37%)</td><td>1.13 (-0.96%)</td><td>1.09 (+6.42%)</td><td>1.06 (+6.53%)</td><td>0.09 <b>(-61.55%)</b></td><td>378.20 (-6.13%)</td><td>356.28 (-1.12%)</td><td>369.00 (-6.04%)</td><td>318.20 <b>(+21.03%)</b></td><td>25.74 <b>(-55.73%)</b></td><td>105.46 (-17.37%)</td><td>94.59 (-0.96%)</td><td>90.93 (+6.42%)</td><td>88.73 (+6.53%)</td><td>7.16 <b>(-61.55%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.53 (n/a)</td><td>1.14 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.22 (n/a)</td><td>402.90 (n/a)</td><td>360.32 (n/a)</td><td>392.70 (n/a)</td><td>262.90 (n/a)</td><td>58.13 (n/a)</td><td>127.64 (n/a)</td><td>95.51 (n/a)</td><td>85.44 (n/a)</td><td>83.29 (n/a)</td><td>18.61 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.25 (+10.07%)</td><td>5.27 (+4.02%)</td><td>5.12 (+1.91%)</td><td>4.44 (-2.82%)</td><td>0.83 <b>(+103.09%)</b></td><td>435.80 (+2.90%)</td><td>373.84 (-2.46%)</td><td>377.80 (-1.90%)</td><td>309.30 (-9.14%)</td><td>57.79 <b>(+90.71%)</b></td><td>1301.96 (+10.07%)</td><td>1098.40 (+4.02%)</td><td>1065.65 (+1.91%)</td><td>923.95 (-2.82%)</td><td>172.75 <b>(+103.09%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.68 (n/a)</td><td>5.07 (n/a)</td><td>5.02 (n/a)</td><td>4.57 (n/a)</td><td>0.41 (n/a)</td><td>423.50 (n/a)</td><td>383.28 (n/a)</td><td>385.10 (n/a)</td><td>340.40 (n/a)</td><td>30.30 (n/a)</td><td>1182.89 (n/a)</td><td>1055.90 (n/a)</td><td>1045.69 (n/a)</td><td>950.79 (n/a)</td><td>85.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>19.41 (+19.62%)</td><td>12.99 (+4.92%)</td><td>11.86 (+6.68%)</td><td>10.18 (+2.89%)</td><td>3.69 <b>(+42.66%)</b></td><td>540.50 (-2.81%)</td><td>445.74 (-2.91%)</td><td>464.30 (-6.26%)</td><td>283.70 (-16.39%)</td><td>98.16 (+11.77%)</td><td>7570.41 (+19.62%)</td><td>5068.42 (+4.92%)</td><td>4624.90 (+6.68%)</td><td>3972.96 (+2.89%)</td><td>1439.58 <b>(+42.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>16.22 (n/a)</td><td>12.38 (n/a)</td><td>11.11 (n/a)</td><td>9.90 (n/a)</td><td>2.59 (n/a)</td><td>556.10 (n/a)</td><td>459.08 (n/a)</td><td>495.30 (n/a)</td><td>339.30 (n/a)</td><td>87.83 (n/a)</td><td>6328.52 (n/a)</td><td>4830.85 (n/a)</td><td>4335.45 (n/a)</td><td>3861.51 (n/a)</td><td>1009.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>10.72 <b>(+27.16%)</b></td><td>8.50 <b>(+22.41%)</b></td><td>8.14 (+2.94%)</td><td>7.47 <b>(+65.24%)</b></td><td>1.27 <b>(-25.92%)</b></td><td>737.40 <b>(-39.49%)</b></td><td>657.56 <b>(-21.77%)</b></td><td>676.50 (-2.86%)</td><td>513.40 <b>(-21.37%)</b></td><td>84.78 <b>(-65.32%)</b></td><td>4182.51 <b>(+27.16%)</b></td><td>3316.76 <b>(+22.41%)</b></td><td>3174.20 (+2.94%)</td><td>2912.09 <b>(+65.24%)</b></td><td>497.18 <b>(-25.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>8.43 (n/a)</td><td>6.95 (n/a)</td><td>7.90 (n/a)</td><td>4.52 (n/a)</td><td>1.72 (n/a)</td><td>1218.60 (n/a)</td><td>840.52 (n/a)</td><td>696.40 (n/a)</td><td>652.90 (n/a)</td><td>244.49 (n/a)</td><td>3289.04 (n/a)</td><td>2709.66 (n/a)</td><td>3083.68 (n/a)</td><td>1762.32 (n/a)</td><td>671.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>10.34 (-10.67%)</td><td>8.62 (+1.10%)</td><td>8.94 (+8.13%)</td><td>4.90 (+3.52%)</td><td>2.19 (-15.91%)</td><td>1182.50 (-3.41%)</td><td>724.54 (-2.95%)</td><td>648.40 (-7.53%)</td><td>560.90 (+11.93%)</td><td>259.59 (-8.59%)</td><td>4307.11 (-10.67%)</td><td>3592.50 (+1.10%)</td><td>3725.69 (+8.13%)</td><td>2043.06 (+3.52%)</td><td>910.65 (-15.91%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>11.58 (n/a)</td><td>8.53 (n/a)</td><td>8.27 (n/a)</td><td>4.74 (n/a)</td><td>2.60 (n/a)</td><td>1224.20 (n/a)</td><td>746.56 (n/a)</td><td>701.20 (n/a)</td><td>501.10 (n/a)</td><td>283.98 (n/a)</td><td>4821.50 (n/a)</td><td>3553.58 (n/a)</td><td>3445.59 (n/a)</td><td>1973.54 (n/a)</td><td>1082.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>142.38 (n/a)</td><td>133.10 (n/a)</td><td>107.70 (n/a)</td><td>32.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>170.80 (n/a)</td><td>142.68 (n/a)</td><td>148.40 (n/a)</td><td>112.70 (n/a)</td><td>25.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>156.06 (n/a)</td><td>158.20 (n/a)</td><td>124.40 (n/a)</td><td>32.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>184.30 (n/a)</td><td>154.88 (n/a)</td><td>172.90 (n/a)</td><td>120.10 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>164.94 (n/a)</td><td>159.40 (n/a)</td><td>133.90 (n/a)</td><td>25.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.30 (n/a)</td><td>172.92 (n/a)</td><td>178.30 (n/a)</td><td>157.40 (n/a)</td><td>13.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.80 (n/a)</td><td>158.36 (n/a)</td><td>147.10 (n/a)</td><td>146.50 (n/a)</td><td>15.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>316.00 (n/a)</td><td>246.96 (n/a)</td><td>229.00 (n/a)</td><td>206.50 (n/a)</td><td>42.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>158.88 (n/a)</td><td>163.30 (n/a)</td><td>135.70 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.50 (n/a)</td><td>164.10 (n/a)</td><td>166.70 (n/a)</td><td>141.80 (n/a)</td><td>15.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>170.62 (n/a)</td><td>178.90 (n/a)</td><td>149.70 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>159.00 (n/a)</td><td>165.30 (n/a)</td><td>126.40 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>165.76 (n/a)</td><td>173.20 (n/a)</td><td>136.40 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>179.72 (n/a)</td><td>159.30 (n/a)</td><td>155.90 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>193.32 (n/a)</td><td>189.10 (n/a)</td><td>158.00 (n/a)</td><td>32.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>389.30 (n/a)</td><td>240.42 (n/a)</td><td>207.50 (n/a)</td><td>194.00 (n/a)</td><td>83.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>369.50 (n/a)</td><td>211.92 (n/a)</td><td>167.70 (n/a)</td><td>142.20 (n/a)</td><td>93.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.00 (n/a)</td><td>175.18 (n/a)</td><td>171.60 (n/a)</td><td>140.10 (n/a)</td><td>39.54 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>309.30 (n/a)</td><td>193.00 (n/a)</td><td>165.70 (n/a)</td><td>155.00 (n/a)</td><td>65.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>191.60 (n/a)</td><td>197.80 (n/a)</td><td>148.40 (n/a)</td><td>26.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.10 (n/a)</td><td>175.04 (n/a)</td><td>171.40 (n/a)</td><td>149.10 (n/a)</td><td>19.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>294.60 (n/a)</td><td>221.92 (n/a)</td><td>206.10 (n/a)</td><td>176.40 (n/a)</td><td>45.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.50 (n/a)</td><td>188.84 (n/a)</td><td>198.70 (n/a)</td><td>159.20 (n/a)</td><td>28.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>383.70 (n/a)</td><td>237.48 (n/a)</td><td>209.80 (n/a)</td><td>185.90 (n/a)</td><td>82.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>214.40 (n/a)</td><td>163.76 (n/a)</td><td>170.20 (n/a)</td><td>124.70 (n/a)</td><td>34.70 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>217.00 (n/a)</td><td>145.26 (n/a)</td><td>134.10 (n/a)</td><td>109.50 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>172.40 (n/a)</td><td>155.14 (n/a)</td><td>161.10 (n/a)</td><td>114.40 (n/a)</td><td>23.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>204.70 (n/a)</td><td>161.04 (n/a)</td><td>164.70 (n/a)</td><td>117.10 (n/a)</td><td>31.35 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.60 (n/a)</td><td>164.72 (n/a)</td><td>165.00 (n/a)</td><td>124.70 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>226.50 (n/a)</td><td>174.82 (n/a)</td><td>166.40 (n/a)</td><td>140.10 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>220.20 (n/a)</td><td>174.26 (n/a)</td><td>177.40 (n/a)</td><td>132.40 (n/a)</td><td>34.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>209.70 (n/a)</td><td>209.10 (n/a)</td><td>194.30 (n/a)</td><td>11.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.18 (+1.55%)</td><td>4.12 (+0.21%)</td><td>4.11 (+0.13%)</td><td>4.07 (-0.52%)</td><td>0.04 <b>(+342.30%)</b></td><td>19311.40 (+0.52%)</td><td>19112.10 (-0.21%)</td><td>19119.90 (-0.13%)</td><td>18797.70 (-1.53%)</td><td>192.84 <b>(+337.09%)</b></td><td>2856.04 (+1.55%)</td><td>2809.29 (+0.21%)</td><td>2807.91 (+0.13%)</td><td>2780.07 (-0.52%)</td><td>28.57 <b>(+342.31%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>4.09 (n/a)</td><td>0.01 (n/a)</td><td>19210.80 (n/a)</td><td>19151.42 (n/a)</td><td>19145.30 (n/a)</td><td>19088.90 (n/a)</td><td>44.12 (n/a)</td><td>2812.48 (n/a)</td><td>2803.31 (n/a)</td><td>2804.18 (n/a)</td><td>2794.64 (n/a)</td><td>6.46 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.46 (+6.32%)</td><td>3.97 (-3.91%)</td><td>4.12 (-0.84%)</td><td>3.50 (-13.57%)</td><td>0.42 <b>(+625.19%)</b></td><td>2683.20 (+15.71%)</td><td>2390.26 (+5.03%)</td><td>2282.30 (+0.85%)</td><td>2107.20 (-5.94%)</td><td>260.22 <b>(+703.60%)</b></td><td>1755.62 (+6.32%)</td><td>1562.23 (-3.91%)</td><td>1620.90 (-0.84%)</td><td>1378.72 (-13.57%)</td><td>167.02 <b>(+625.19%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.20 (n/a)</td><td>4.13 (n/a)</td><td>4.16 (n/a)</td><td>4.06 (n/a)</td><td>0.06 (n/a)</td><td>2319.00 (n/a)</td><td>2275.82 (n/a)</td><td>2263.00 (n/a)</td><td>2240.30 (n/a)</td><td>32.38 (n/a)</td><td>1651.30 (n/a)</td><td>1625.77 (n/a)</td><td>1634.70 (n/a)</td><td>1595.24 (n/a)</td><td>23.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.08 (+1.50%)</td><td>0.93 (+18.21%)</td><td>1.03 <b>(+55.44%)</b></td><td>0.63 (+1.81%)</td><td>0.19 (-4.65%)</td><td>350.10 (-1.77%)</td><td>247.74 (-15.85%)</td><td>214.10 <b>(-35.67%)</b></td><td>205.50 (-1.49%)</td><td>60.54 (-7.54%)</td><td>45.92 (+1.50%)</td><td>39.63 (+18.21%)</td><td>44.09 <b>(+55.44%)</b></td><td>26.96 (+1.81%)</td><td>7.89 (-4.65%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.06 (n/a)</td><td>0.79 (n/a)</td><td>0.66 (n/a)</td><td>0.62 (n/a)</td><td>0.19 (n/a)</td><td>356.40 (n/a)</td><td>294.40 (n/a)</td><td>332.80 (n/a)</td><td>208.60 (n/a)</td><td>65.48 (n/a)</td><td>45.24 (n/a)</td><td>33.52 (n/a)</td><td>28.36 (n/a)</td><td>26.48 (n/a)</td><td>8.28 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.04 (-11.07%)</td><td>0.92 (-8.24%)</td><td>0.96 (-11.46%)</td><td>0.64 (-8.53%)</td><td>0.16 (-13.03%)</td><td>347.00 (+9.33%)</td><td>249.36 (+8.75%)</td><td>230.90 (+12.91%)</td><td>213.00 (+12.46%)</td><td>55.31 (+7.32%)</td><td>44.31 (-11.07%)</td><td>39.05 (-8.24%)</td><td>40.86 (-11.46%)</td><td>27.20 (-8.53%)</td><td>6.84 (-13.03%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.17 (n/a)</td><td>1.00 (n/a)</td><td>1.08 (n/a)</td><td>0.70 (n/a)</td><td>0.18 (n/a)</td><td>317.40 (n/a)</td><td>229.30 (n/a)</td><td>204.50 (n/a)</td><td>189.40 (n/a)</td><td>51.53 (n/a)</td><td>49.83 (n/a)</td><td>42.56 (n/a)</td><td>46.15 (n/a)</td><td>29.73 (n/a)</td><td>7.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.53 (+0.01%)</td><td>0.53 (+0.01%)</td><td>0.53 (+0.03%)</td><td>0.53 (-0.02%)</td><td>0.00 (+16.78%)</td><td>47842.50 (+0.02%)</td><td>47806.62 (-0.01%)</td><td>47800.50 (-0.03%)</td><td>47784.10 (-0.01%)</td><td>23.78 (+16.73%)</td><td>359.53 (+0.01%)</td><td>359.36 (+0.01%)</td><td>359.41 (+0.03%)</td><td>359.09 (-0.02%)</td><td>0.18 (+16.80%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47834.90 (n/a)</td><td>47811.60 (n/a)</td><td>47816.60 (n/a)</td><td>47787.80 (n/a)</td><td>20.37 (n/a)</td><td>359.50 (n/a)</td><td>359.32 (n/a)</td><td>359.29 (n/a)</td><td>359.15 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 (-1.23%)</td><td>0.21 (-0.44%)</td><td>0.21 (-0.55%)</td><td>0.21 (-0.20%)</td><td>0.00 <b>(-37.87%)</b></td><td>119741.30 (+0.20%)</td><td>118919.66 (+0.43%)</td><td>119307.60 (+0.55%)</td><td>117988.20 (+1.24%)</td><td>772.86 <b>(-37.05%)</b></td><td>145.61 (-1.23%)</td><td>144.47 (-0.44%)</td><td>144.00 (-0.55%)</td><td>143.47 (-0.20%)</td><td>0.94 <b>(-37.87%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119499.30 (n/a)</td><td>118407.18 (n/a)</td><td>118650.30 (n/a)</td><td>116538.90 (n/a)</td><td>1227.79 (n/a)</td><td>147.42 (n/a)</td><td>145.10 (n/a)</td><td>144.79 (n/a)</td><td>143.77 (n/a)</td><td>1.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.90 (-0.28%)</td><td>0.90 (-0.50%)</td><td>0.90 (-0.22%)</td><td>0.89 (-1.02%)</td><td>0.01 <b>(+143.69%)</b></td><td>28227.50 (+1.03%)</td><td>28012.46 (+0.50%)</td><td>27945.00 (+0.22%)</td><td>27843.30 (+0.28%)</td><td>161.90 <b>(+147.05%)</b></td><td>617.02 (-0.28%)</td><td>613.31 (-0.50%)</td><td>614.77 (-0.22%)</td><td>608.62 (-1.02%)</td><td>3.54 <b>(+143.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>27938.40 (n/a)</td><td>27872.36 (n/a)</td><td>27884.60 (n/a)</td><td>27766.70 (n/a)</td><td>65.53 (n/a)</td><td>618.72 (n/a)</td><td>616.38 (n/a)</td><td>616.11 (n/a)</td><td>614.92 (n/a)</td><td>1.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.70 (+1.63%)</td><td>3.61 (-0.50%)</td><td>3.65 (+0.60%)</td><td>3.49 (-3.31%)</td><td>0.09 <b>(+768.86%)</b></td><td>7200.60 (+3.43%)</td><td>6972.16 (+0.55%)</td><td>6890.60 (-0.60%)</td><td>6797.40 (-1.61%)</td><td>168.89 <b>(+785.78%)</b></td><td>2527.43 (+1.63%)</td><td>2465.22 (-0.50%)</td><td>2493.24 (+0.60%)</td><td>2385.90 (-3.31%)</td><td>59.21 <b>(+768.90%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.64 (n/a)</td><td>3.63 (n/a)</td><td>3.63 (n/a)</td><td>3.61 (n/a)</td><td>0.01 (n/a)</td><td>6961.90 (n/a)</td><td>6934.04 (n/a)</td><td>6932.10 (n/a)</td><td>6908.40 (n/a)</td><td>19.07 (n/a)</td><td>2486.82 (n/a)</td><td>2477.63 (n/a)</td><td>2478.29 (n/a)</td><td>2467.70 (n/a)</td><td>6.81 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.22 (+10.12%)</td><td>3.03 (+5.31%)</td><td>3.04 (+5.49%)</td><td>2.84 (+0.41%)</td><td>0.14 <b>(+288.43%)</b></td><td>8864.20 (-0.41%)</td><td>8313.04 (-4.90%)</td><td>8284.00 (-5.21%)</td><td>7807.80 (-9.19%)</td><td>377.60 <b>(+251.45%)</b></td><td>2200.35 (+10.12%)</td><td>2070.01 (+5.31%)</td><td>2073.86 (+5.49%)</td><td>1938.11 (+0.41%)</td><td>93.60 <b>(+288.44%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>2.93 (n/a)</td><td>2.88 (n/a)</td><td>2.88 (n/a)</td><td>2.83 (n/a)</td><td>0.04 (n/a)</td><td>8900.80 (n/a)</td><td>8740.96 (n/a)</td><td>8739.00 (n/a)</td><td>8598.00 (n/a)</td><td>107.44 (n/a)</td><td>1998.12 (n/a)</td><td>1965.68 (n/a)</td><td>1965.88 (n/a)</td><td>1930.15 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.19 (-3.84%)</td><td>3.15 (-2.21%)</td><td>3.16 (-1.41%)</td><td>3.10 (-1.34%)</td><td>0.03 <b>(-56.58%)</b></td><td>8107.60 (+1.36%)</td><td>7984.10 (+2.23%)</td><td>7965.60 (+1.43%)</td><td>7895.80 (+3.99%)</td><td>77.55 <b>(-54.10%)</b></td><td>2175.81 (-3.84%)</td><td>2151.92 (-2.21%)</td><td>2156.75 (-1.41%)</td><td>2118.99 (-1.34%)</td><td>20.77 <b>(-56.58%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.31 (n/a)</td><td>3.22 (n/a)</td><td>3.20 (n/a)</td><td>3.15 (n/a)</td><td>0.07 (n/a)</td><td>7998.70 (n/a)</td><td>7810.24 (n/a)</td><td>7853.50 (n/a)</td><td>7592.60 (n/a)</td><td>168.96 (n/a)</td><td>2262.72 (n/a)</td><td>2200.49 (n/a)</td><td>2187.54 (n/a)</td><td>2147.84 (n/a)</td><td>47.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.80 (-0.46%)</td><td>0.80 (-0.11%)</td><td>0.80 (-0.04%)</td><td>0.80 (+0.00%)</td><td>0.00 <b>(-79.65%)</b></td><td>94846.30 (-0.00%)</td><td>94802.32 (+0.11%)</td><td>94819.80 (+0.04%)</td><td>94752.00 (+0.46%)</td><td>44.00 <b>(-79.54%)</b></td><td>725.26 (-0.46%)</td><td>724.87 (-0.11%)</td><td>724.74 (-0.04%)</td><td>724.54 (+0.00%)</td><td>0.34 <b>(-79.65%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94849.70 (n/a)</td><td>94694.12 (n/a)</td><td>94777.70 (n/a)</td><td>94315.20 (n/a)</td><td>215.11 (n/a)</td><td>728.62 (n/a)</td><td>725.70 (n/a)</td><td>725.06 (n/a)</td><td>724.51 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.73 (+0.03%)</td><td>0.73 (+0.03%)</td><td>0.73 (+0.03%)</td><td>0.73 (+0.01%)</td><td>0.00 <b>(+31.05%)</b></td><td>103383.70 (-0.01%)</td><td>103312.48 (-0.03%)</td><td>103299.80 (-0.03%)</td><td>103267.60 (-0.03%)</td><td>45.12 <b>(+31.09%)</b></td><td>665.45 (+0.03%)</td><td>665.16 (+0.03%)</td><td>665.24 (+0.03%)</td><td>664.70 (+0.01%)</td><td>0.29 <b>(+31.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103392.10 (n/a)</td><td>103339.90 (n/a)</td><td>103330.80 (n/a)</td><td>103297.90 (n/a)</td><td>34.42 (n/a)</td><td>665.26 (n/a)</td><td>664.98 (n/a)</td><td>665.04 (n/a)</td><td>664.65 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.69 (-0.18%)</td><td>0.69 (-0.33%)</td><td>0.69 (-0.21%)</td><td>0.68 (-0.69%)</td><td>0.00 <b>(+60.06%)</b></td><td>110789.50 (+0.70%)</td><td>110090.12 (+0.33%)</td><td>110087.00 (+0.22%)</td><td>109539.10 (+0.18%)</td><td>471.92 <b>(+61.52%)</b></td><td>627.35 (-0.18%)</td><td>624.22 (-0.33%)</td><td>624.23 (-0.21%)</td><td>620.27 (-0.69%)</td><td>2.67 <b>(+60.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>110023.60 (n/a)</td><td>109727.34 (n/a)</td><td>109850.60 (n/a)</td><td>109342.30 (n/a)</td><td>292.17 (n/a)</td><td>628.48 (n/a)</td><td>626.28 (n/a)</td><td>625.57 (n/a)</td><td>624.59 (n/a)</td><td>1.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>2.80 (-0.89%)</td><td>2.79 (-0.36%)</td><td>2.79 (-0.07%)</td><td>2.78 (-0.39%)</td><td>0.01 <b>(-44.92%)</b></td><td>37675.10 (+0.39%)</td><td>37569.84 (+0.36%)</td><td>37526.90 (+0.07%)</td><td>37493.00 (+0.90%)</td><td>87.08 <b>(-44.19%)</b></td><td>2863.85 (-0.89%)</td><td>2858.00 (-0.36%)</td><td>2861.26 (-0.07%)</td><td>2850.00 (-0.39%)</td><td>6.62 <b>(-44.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>2.82 (n/a)</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>0.01 (n/a)</td><td>37527.50 (n/a)</td><td>37435.12 (n/a)</td><td>37502.00 (n/a)</td><td>37159.40 (n/a)</td><td>156.03 (n/a)</td><td>2889.56 (n/a)</td><td>2868.32 (n/a)</td><td>2863.16 (n/a)</td><td>2861.21 (n/a)</td><td>12.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.43 (+0.25%)</td><td>6.87 (-0.31%)</td><td>7.13 (+4.67%)</td><td>6.23 (+0.14%)</td><td>0.52 (-0.66%)</td><td>1430.80 (-0.14%)</td><td>1304.00 (+0.31%)</td><td>1250.10 (-4.46%)</td><td>1199.70 (-0.25%)</td><td>100.33 (+1.17%)</td><td>447.50 (+0.25%)</td><td>413.63 (-0.31%)</td><td>429.47 (+4.67%)</td><td>375.23 (+0.14%)</td><td>31.16 (-0.66%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>7.41 (n/a)</td><td>6.89 (n/a)</td><td>6.81 (n/a)</td><td>6.22 (n/a)</td><td>0.52 (n/a)</td><td>1432.80 (n/a)</td><td>1299.96 (n/a)</td><td>1308.50 (n/a)</td><td>1202.70 (n/a)</td><td>99.17 (n/a)</td><td>446.40 (n/a)</td><td>414.91 (n/a)</td><td>410.30 (n/a)</td><td>374.70 (n/a)</td><td>31.37 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.85 (-1.75%)</td><td>6.52 (-3.08%)</td><td>6.54 (-5.18%)</td><td>6.03 (-1.31%)</td><td>0.32 (-11.62%)</td><td>1478.00 (+1.32%)</td><td>1369.32 (+3.12%)</td><td>1362.80 (+5.46%)</td><td>1300.50 (+1.78%)</td><td>69.35 (-8.87%)</td><td>412.81 (-1.75%)</td><td>392.85 (-3.08%)</td><td>393.93 (-5.18%)</td><td>363.24 (-1.31%)</td><td>19.32 (-11.62%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>6.98 (n/a)</td><td>6.73 (n/a)</td><td>6.90 (n/a)</td><td>6.11 (n/a)</td><td>0.36 (n/a)</td><td>1458.70 (n/a)</td><td>1327.86 (n/a)</td><td>1292.30 (n/a)</td><td>1277.70 (n/a)</td><td>76.10 (n/a)</td><td>420.18 (n/a)</td><td>405.32 (n/a)</td><td>415.44 (n/a)</td><td>368.05 (n/a)</td><td>21.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.16 (+0.75%)</td><td>6.35 (-6.45%)</td><td>6.98 (+0.81%)</td><td>4.54 <b>(-29.32%)</b></td><td>1.11 <b>(+278.31%)</b></td><td>1963.30 <b>(+41.48%)</b></td><td>1444.66 (+9.94%)</td><td>1277.30 (-0.81%)</td><td>1244.20 (-0.75%)</td><td>304.14 <b>(+430.93%)</b></td><td>431.49 (+0.75%)</td><td>382.79 (-6.45%)</td><td>420.30 (+0.81%)</td><td>273.45 <b>(-29.32%)</b></td><td>66.67 <b>(+278.31%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>7.11 (n/a)</td><td>6.79 (n/a)</td><td>6.92 (n/a)</td><td>6.42 (n/a)</td><td>0.29 (n/a)</td><td>1387.70 (n/a)</td><td>1314.08 (n/a)</td><td>1287.70 (n/a)</td><td>1253.60 (n/a)</td><td>57.28 (n/a)</td><td>428.28 (n/a)</td><td>409.17 (n/a)</td><td>416.93 (n/a)</td><td>386.89 (n/a)</td><td>17.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>8.14 (-0.23%)</td><td>7.86 (-2.68%)</td><td>7.96 (-1.31%)</td><td>7.48 (-6.44%)</td><td>0.30 <b>(+309.84%)</b></td><td>4663.20 (+6.89%)</td><td>4441.20 (+2.87%)</td><td>4378.60 (+1.33%)</td><td>4282.40 (+0.23%)</td><td>170.06 <b>(+338.62%)</b></td><td>501.47 (-0.23%)</td><td>484.10 (-2.68%)</td><td>490.45 (-1.31%)</td><td>460.52 (-6.44%)</td><td>18.31 <b>(+309.84%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>8.16 (n/a)</td><td>8.08 (n/a)</td><td>8.07 (n/a)</td><td>7.99 (n/a)</td><td>0.07 (n/a)</td><td>4362.70 (n/a)</td><td>4317.26 (n/a)</td><td>4321.30 (n/a)</td><td>4272.70 (n/a)</td><td>38.77 (n/a)</td><td>502.60 (n/a)</td><td>497.45 (n/a)</td><td>496.95 (n/a)</td><td>492.24 (n/a)</td><td>4.47 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.66 (+0.97%)</td><td>7.46 (+0.95%)</td><td>7.54 (-0.16%)</td><td>7.03 (-1.01%)</td><td>0.25 (+4.56%)</td><td>4959.60 (+1.02%)</td><td>4675.52 (-0.94%)</td><td>4625.00 (+0.16%)</td><td>4554.30 (-0.96%)</td><td>161.54 (+5.56%)</td><td>471.52 (+0.97%)</td><td>459.72 (+0.95%)</td><td>464.32 (-0.16%)</td><td>432.99 (-1.01%)</td><td>15.24 (+4.55%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>7.58 (n/a)</td><td>7.39 (n/a)</td><td>7.55 (n/a)</td><td>7.10 (n/a)</td><td>0.24 (n/a)</td><td>4909.50 (n/a)</td><td>4719.76 (n/a)</td><td>4617.60 (n/a)</td><td>4598.50 (n/a)</td><td>153.02 (n/a)</td><td>466.99 (n/a)</td><td>455.38 (n/a)</td><td>465.07 (n/a)</td><td>437.42 (n/a)</td><td>14.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.91 (+6.39%)</td><td>7.40 (+2.09%)</td><td>7.35 (-0.39%)</td><td>6.87 (+1.73%)</td><td>0.38 <b>(+32.74%)</b></td><td>5077.40 (-1.70%)</td><td>4721.30 (-1.97%)</td><td>4741.00 (+0.39%)</td><td>4406.50 (-6.01%)</td><td>242.24 <b>(+22.25%)</b></td><td>487.35 (+6.39%)</td><td>455.80 (+2.09%)</td><td>452.96 (-0.39%)</td><td>422.95 (+1.73%)</td><td>23.20 <b>(+32.74%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>7.44 (n/a)</td><td>7.25 (n/a)</td><td>7.38 (n/a)</td><td>6.75 (n/a)</td><td>0.28 (n/a)</td><td>5165.10 (n/a)</td><td>4816.04 (n/a)</td><td>4722.40 (n/a)</td><td>4688.20 (n/a)</td><td>198.15 (n/a)</td><td>458.06 (n/a)</td><td>446.48 (n/a)</td><td>454.75 (n/a)</td><td>415.77 (n/a)</td><td>17.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.80 (+0.02%)</td><td>0.80 (+0.04%)</td><td>0.80 (+0.04%)</td><td>0.80 (+0.08%)</td><td>0.00 <b>(-58.65%)</b></td><td>94079.00 (-0.08%)</td><td>94051.02 (-0.04%)</td><td>94045.20 (-0.04%)</td><td>94039.50 (-0.02%)</td><td>15.89 <b>(-58.71%)</b></td><td>730.75 (+0.02%)</td><td>730.66 (+0.04%)</td><td>730.71 (+0.04%)</td><td>730.44 (+0.08%)</td><td>0.12 <b>(-58.65%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94156.60 (n/a)</td><td>94091.24 (n/a)</td><td>94081.20 (n/a)</td><td>94056.20 (n/a)</td><td>38.48 (n/a)</td><td>730.62 (n/a)</td><td>730.35 (n/a)</td><td>730.43 (n/a)</td><td>729.84 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.74 (+0.02%)</td><td>0.74 (+0.01%)</td><td>0.74 (-0.01%)</td><td>0.73 (+0.04%)</td><td>0.00 (-14.48%)</td><td>102804.40 (-0.04%)</td><td>102627.72 (-0.01%)</td><td>102599.60 (+0.01%)</td><td>102550.10 (-0.02%)</td><td>101.16 (-14.53%)</td><td>670.11 (+0.02%)</td><td>669.60 (+0.01%)</td><td>669.78 (-0.01%)</td><td>668.45 (+0.04%)</td><td>0.66 (-14.48%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102850.60 (n/a)</td><td>102640.02 (n/a)</td><td>102585.60 (n/a)</td><td>102575.40 (n/a)</td><td>118.36 (n/a)</td><td>669.94 (n/a)</td><td>669.52 (n/a)</td><td>669.87 (n/a)</td><td>668.15 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.71 (+0.15%)</td><td>0.71 (+0.12%)</td><td>0.71 (+0.04%)</td><td>0.71 (+0.24%)</td><td>0.00 <b>(-33.36%)</b></td><td>105980.00 (-0.24%)</td><td>105869.14 (-0.12%)</td><td>105882.00 (-0.04%)</td><td>105717.50 (-0.14%)</td><td>95.44 <b>(-33.62%)</b></td><td>650.03 (+0.15%)</td><td>649.10 (+0.12%)</td><td>649.02 (+0.04%)</td><td>648.42 (+0.24%)</td><td>0.59 <b>(-33.36%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106230.40 (n/a)</td><td>105991.34 (n/a)</td><td>105927.90 (n/a)</td><td>105871.00 (n/a)</td><td>143.78 (n/a)</td><td>649.09 (n/a)</td><td>648.35 (n/a)</td><td>648.74 (n/a)</td><td>646.89 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.75 (+1.04%)</td><td>3.23 (-0.42%)</td><td>3.18 (+4.70%)</td><td>2.93 (+0.95%)</td><td>0.32 (-19.81%)</td><td>2755.80 (-0.94%)</td><td>2515.28 (-0.02%)</td><td>2537.80 (-4.49%)</td><td>2148.70 (-1.03%)</td><td>234.68 <b>(-21.75%)</b></td><td>983.81 (+1.04%)</td><td>846.72 (-0.42%)</td><td>832.96 (+4.70%)</td><td>767.08 (+0.95%)</td><td>84.52 (-19.81%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.71 (n/a)</td><td>3.24 (n/a)</td><td>3.03 (n/a)</td><td>2.90 (n/a)</td><td>0.40 (n/a)</td><td>2782.00 (n/a)</td><td>2515.88 (n/a)</td><td>2657.10 (n/a)</td><td>2171.00 (n/a)</td><td>299.91 (n/a)</td><td>973.72 (n/a)</td><td>850.28 (n/a)</td><td>795.57 (n/a)</td><td>759.85 (n/a)</td><td>105.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.55 (+1.97%)</td><td>0.37 (+2.20%)</td><td>0.33 (+0.80%)</td><td>0.32 (+4.88%)</td><td>0.10 (+1.00%)</td><td>3925.80 (-4.65%)</td><td>3498.96 (-2.28%)</td><td>3806.20 (-0.79%)</td><td>2281.10 (-1.93%)</td><td>687.14 (-4.23%)</td><td>29.42 (+1.97%)</td><td>20.01 (+2.20%)</td><td>17.63 (+0.80%)</td><td>17.09 (+4.88%)</td><td>5.28 (+1.00%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.54 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.10 (n/a)</td><td>4117.40 (n/a)</td><td>3580.58 (n/a)</td><td>3836.50 (n/a)</td><td>2326.00 (n/a)</td><td>717.49 (n/a)</td><td>28.85 (n/a)</td><td>19.58 (n/a)</td><td>17.49 (n/a)</td><td>16.30 (n/a)</td><td>5.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.83 (-0.18%)</td><td>3.91 (-8.84%)</td><td>3.40 <b>(-26.26%)</b></td><td>3.25 (-3.44%)</td><td>0.81 <b>(+21.28%)</b></td><td>2046.70 (+3.57%)</td><td>1757.86 (+10.93%)</td><td>1957.30 <b>(+35.61%)</b></td><td>1378.40 (+0.18%)</td><td>338.70 <b>(+26.64%)</b></td><td>1491.04 (-0.18%)</td><td>1207.60 (-8.84%)</td><td>1050.00 <b>(-26.26%)</b></td><td>1004.18 (-3.44%)</td><td>249.51 <b>(+21.28%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.83 (n/a)</td><td>4.29 (n/a)</td><td>4.61 (n/a)</td><td>3.37 (n/a)</td><td>0.67 (n/a)</td><td>1976.20 (n/a)</td><td>1584.60 (n/a)</td><td>1443.30 (n/a)</td><td>1375.90 (n/a)</td><td>267.45 (n/a)</td><td>1493.77 (n/a)</td><td>1324.70 (n/a)</td><td>1424.00 (n/a)</td><td>1039.99 (n/a)</td><td>205.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>13.24 (n/a)</td><td>13.08 (n/a)</td><td>13.21 (n/a)</td><td>12.54 (n/a)</td><td>0.30 (n/a)</td><td>13.24 (n/a)</td><td>13.07 (n/a)</td><td>13.20 (n/a)</td><td>12.54 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>24.02 (-2.97%)</td><td>23.02 (+3.70%)</td><td>23.47 (+0.66%)</td><td>20.53 <b>(+33.11%)</b></td><td>1.42 <b>(-63.41%)</b></td><td>24.01 (-2.97%)</td><td>23.01 (+3.70%)</td><td>23.45 (+0.66%)</td><td>20.52 <b>(+33.11%)</b></td><td>1.42 <b>(-63.41%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>24.76 (n/a)</td><td>22.20 (n/a)</td><td>23.32 (n/a)</td><td>15.42 (n/a)</td><td>3.87 (n/a)</td><td>24.74 (n/a)</td><td>22.19 (n/a)</td><td>23.30 (n/a)</td><td>15.41 (n/a)</td><td>3.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>41.05 (-5.67%)</td><td>39.23 (-3.62%)</td><td>39.08 (-2.99%)</td><td>37.46 (-2.65%)</td><td>1.32 <b>(-35.83%)</b></td><td>41.02 (-5.67%)</td><td>39.21 (-3.62%)</td><td>39.05 (-2.99%)</td><td>37.44 (-2.65%)</td><td>1.32 <b>(-35.83%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>43.51 (n/a)</td><td>40.70 (n/a)</td><td>40.28 (n/a)</td><td>38.48 (n/a)</td><td>2.06 (n/a)</td><td>43.49 (n/a)</td><td>40.68 (n/a)</td><td>40.26 (n/a)</td><td>38.46 (n/a)</td><td>2.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>44.31 (-1.83%)</td><td>43.63 (+3.68%)</td><td>43.68 (+2.62%)</td><td>42.88 (+16.10%)</td><td>0.55 <b>(-82.69%)</b></td><td>44.28 (-1.83%)</td><td>43.60 (+3.68%)</td><td>43.66 (+2.62%)</td><td>42.86 (+16.10%)</td><td>0.55 <b>(-82.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>45.13 (n/a)</td><td>42.08 (n/a)</td><td>42.57 (n/a)</td><td>36.94 (n/a)</td><td>3.19 (n/a)</td><td>45.11 (n/a)</td><td>42.06 (n/a)</td><td>42.54 (n/a)</td><td>36.91 (n/a)</td><td>3.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>12.86 (n/a)</td><td>12.29 (n/a)</td><td>12.51 (n/a)</td><td>11.04 (n/a)</td><td>0.72 (n/a)</td><td>12.86 (n/a)</td><td>12.29 (n/a)</td><td>12.50 (n/a)</td><td>11.03 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>24.47 (-0.76%)</td><td>23.75 (-2.31%)</td><td>23.92 (-1.75%)</td><td>22.05 (-7.86%)</td><td>0.99 <b>(+259.76%)</b></td><td>24.45 (-0.76%)</td><td>23.73 (-2.31%)</td><td>23.90 (-1.75%)</td><td>22.04 (-7.86%)</td><td>0.99 <b>(+259.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>24.66 (n/a)</td><td>24.31 (n/a)</td><td>24.35 (n/a)</td><td>23.94 (n/a)</td><td>0.27 (n/a)</td><td>24.64 (n/a)</td><td>24.30 (n/a)</td><td>24.33 (n/a)</td><td>23.92 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>40.04 (-9.35%)</td><td>38.43 (-5.74%)</td><td>37.88 (-5.77%)</td><td>36.67 (-3.65%)</td><td>1.49 <b>(-34.72%)</b></td><td>40.01 (-9.35%)</td><td>38.41 (-5.74%)</td><td>37.85 (-5.77%)</td><td>36.65 (-3.65%)</td><td>1.49 <b>(-34.72%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>44.17 (n/a)</td><td>40.77 (n/a)</td><td>40.19 (n/a)</td><td>38.06 (n/a)</td><td>2.29 (n/a)</td><td>44.14 (n/a)</td><td>40.75 (n/a)</td><td>40.17 (n/a)</td><td>38.03 (n/a)</td><td>2.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>42.63 (-8.57%)</td><td>42.27 (-2.17%)</td><td>42.46 (-0.70%)</td><td>41.52 (+1.70%)</td><td>0.44 <b>(-80.48%)</b></td><td>42.61 (-8.57%)</td><td>42.24 (-2.17%)</td><td>42.43 (-0.70%)</td><td>41.50 (+1.70%)</td><td>0.44 <b>(-80.48%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>46.63 (n/a)</td><td>43.20 (n/a)</td><td>42.76 (n/a)</td><td>40.83 (n/a)</td><td>2.23 (n/a)</td><td>46.60 (n/a)</td><td>43.18 (n/a)</td><td>42.73 (n/a)</td><td>40.81 (n/a)</td><td>2.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.32 (-4.46%)</td><td>8.49 (-6.48%)</td><td>8.75 (-5.47%)</td><td>7.12 (-15.12%)</td><td>0.82 <b>(+50.93%)</b></td><td>9.30 (-4.46%)</td><td>8.47 (-6.48%)</td><td>8.73 (-5.47%)</td><td>7.11 (-15.12%)</td><td>0.82 <b>(+50.93%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.75 (n/a)</td><td>9.08 (n/a)</td><td>9.25 (n/a)</td><td>8.39 (n/a)</td><td>0.54 (n/a)</td><td>9.74 (n/a)</td><td>9.06 (n/a)</td><td>9.23 (n/a)</td><td>8.37 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.94 (-13.54%)</td><td>0.85 (-8.01%)</td><td>0.83 (-4.75%)</td><td>0.80 (-4.49%)</td><td>0.06 <b>(-47.24%)</b></td><td>0.93 (-13.54%)</td><td>0.83 (-8.01%)</td><td>0.82 (-4.75%)</td><td>0.79 (-4.49%)</td><td>0.05 <b>(-47.24%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.09 (n/a)</td><td>0.92 (n/a)</td><td>0.87 (n/a)</td><td>0.84 (n/a)</td><td>0.11 (n/a)</td><td>1.07 (n/a)</td><td>0.91 (n/a)</td><td>0.86 (n/a)</td><td>0.82 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.36 (+6.08%)</td><td>1.15 (-5.40%)</td><td>1.16 (-8.62%)</td><td>0.93 (-15.53%)</td><td>0.16 <b>(+93.14%)</b></td><td>1.35 (+6.08%)</td><td>1.14 (-5.40%)</td><td>1.14 (-8.62%)</td><td>0.91 (-15.53%)</td><td>0.16 <b>(+93.14%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.28 (n/a)</td><td>1.22 (n/a)</td><td>1.27 (n/a)</td><td>1.10 (n/a)</td><td>0.08 (n/a)</td><td>1.27 (n/a)</td><td>1.20 (n/a)</td><td>1.25 (n/a)</td><td>1.08 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>17.71 (-8.11%)</td><td>15.91 (-12.79%)</td><td>15.90 (-12.77%)</td><td>14.31 (-18.57%)</td><td>1.29 <b>(+88.05%)</b></td><td>17.50 (-8.11%)</td><td>15.72 (-12.79%)</td><td>15.72 (-12.77%)</td><td>14.14 (-18.57%)</td><td>1.28 <b>(+88.05%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>19.27 (n/a)</td><td>18.24 (n/a)</td><td>18.23 (n/a)</td><td>17.57 (n/a)</td><td>0.69 (n/a)</td><td>19.05 (n/a)</td><td>18.03 (n/a)</td><td>18.02 (n/a)</td><td>17.37 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>13.47 (-7.18%)</td><td>13.32 (-5.50%)</td><td>13.37 (-4.63%)</td><td>13.00 (-6.14%)</td><td>0.19 <b>(-24.37%)</b></td><td>13.24 (-7.18%)</td><td>13.09 (-5.50%)</td><td>13.13 (-4.63%)</td><td>12.77 (-6.14%)</td><td>0.18 <b>(-24.37%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.52 (n/a)</td><td>14.10 (n/a)</td><td>14.02 (n/a)</td><td>13.85 (n/a)</td><td>0.25 (n/a)</td><td>14.26 (n/a)</td><td>13.85 (n/a)</td><td>13.77 (n/a)</td><td>13.61 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>8.51 (-19.71%)</td><td>7.91 (-3.09%)</td><td>7.93 (+6.34%)</td><td>7.35 (+2.79%)</td><td>0.43 <b>(-69.66%)</b></td><td>8.36 (-19.71%)</td><td>7.78 (-3.09%)</td><td>7.79 (+6.34%)</td><td>7.22 (+2.79%)</td><td>0.43 <b>(-69.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>10.60 (n/a)</td><td>8.16 (n/a)</td><td>7.46 (n/a)</td><td>7.15 (n/a)</td><td>1.43 (n/a)</td><td>10.41 (n/a)</td><td>8.02 (n/a)</td><td>7.33 (n/a)</td><td>7.03 (n/a)</td><td>1.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>5.79 (-13.14%)</td><td>5.28 (-1.62%)</td><td>5.38 (+4.01%)</td><td>4.62 (+3.67%)</td><td>0.45 <b>(-44.61%)</b></td><td>5.70 (-13.14%)</td><td>5.19 (-1.62%)</td><td>5.30 (+4.01%)</td><td>4.55 (+3.67%)</td><td>0.45 <b>(-44.61%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>6.66 (n/a)</td><td>5.36 (n/a)</td><td>5.18 (n/a)</td><td>4.46 (n/a)</td><td>0.82 (n/a)</td><td>6.56 (n/a)</td><td>5.28 (n/a)</td><td>5.09 (n/a)</td><td>4.38 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>13.35 (n/a)</td><td>12.79 (n/a)</td><td>13.18 (n/a)</td><td>11.94 (n/a)</td><td>0.64 (n/a)</td><td>13.34 (n/a)</td><td>12.78 (n/a)</td><td>13.17 (n/a)</td><td>11.93 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>13.15 (n/a)</td><td>12.40 (n/a)</td><td>12.61 (n/a)</td><td>11.23 (n/a)</td><td>0.77 (n/a)</td><td>13.15 (n/a)</td><td>12.39 (n/a)</td><td>12.60 (n/a)</td><td>11.22 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>265.80 (n/a)</td><td>176.06 (n/a)</td><td>162.20 (n/a)</td><td>119.20 (n/a)</td><td>60.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.40 (n/a)</td><td>176.78 (n/a)</td><td>168.20 (n/a)</td><td>157.70 (n/a)</td><td>21.53 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.50 (n/a)</td><td>162.26 (n/a)</td><td>157.30 (n/a)</td><td>136.80 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.70 (n/a)</td><td>177.94 (n/a)</td><td>182.20 (n/a)</td><td>149.80 (n/a)</td><td>24.31 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>385.70 (n/a)</td><td>208.54 (n/a)</td><td>174.20 (n/a)</td><td>150.50 (n/a)</td><td>99.78 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.30 (n/a)</td><td>179.66 (n/a)</td><td>190.60 (n/a)</td><td>136.90 (n/a)</td><td>25.08 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.40 (n/a)</td><td>195.24 (n/a)</td><td>192.60 (n/a)</td><td>171.10 (n/a)</td><td>17.39 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.50 (n/a)</td><td>221.74 (n/a)</td><td>218.70 (n/a)</td><td>177.10 (n/a)</td><td>33.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.20 (n/a)</td><td>194.30 (n/a)</td><td>193.20 (n/a)</td><td>157.50 (n/a)</td><td>31.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>185.86 (n/a)</td><td>191.90 (n/a)</td><td>139.30 (n/a)</td><td>31.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>172.08 (n/a)</td><td>169.20 (n/a)</td><td>135.20 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>175.64 (n/a)</td><td>186.50 (n/a)</td><td>135.50 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>209.90 (n/a)</td><td>174.40 (n/a)</td><td>187.40 (n/a)</td><td>102.80 (n/a)</td><td>41.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>281.50 (n/a)</td><td>208.12 (n/a)</td><td>222.00 (n/a)</td><td>153.50 (n/a)</td><td>52.78 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>175.20 (n/a)</td><td>178.60 (n/a)</td><td>124.10 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>332.50 (n/a)</td><td>252.02 (n/a)</td><td>232.90 (n/a)</td><td>220.00 (n/a)</td><td>46.08 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.60 (n/a)</td><td>157.92 (n/a)</td><td>161.00 (n/a)</td><td>134.00 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>193.44 (n/a)</td><td>205.60 (n/a)</td><td>158.70 (n/a)</td><td>29.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>211.00 (n/a)</td><td>159.62 (n/a)</td><td>159.80 (n/a)</td><td>112.10 (n/a)</td><td>40.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>207.20 (n/a)</td><td>172.22 (n/a)</td><td>180.70 (n/a)</td><td>114.40 (n/a)</td><td>37.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>182.24 (n/a)</td><td>174.70 (n/a)</td><td>164.10 (n/a)</td><td>16.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>262.70 (n/a)</td><td>170.94 (n/a)</td><td>157.10 (n/a)</td><td>103.00 (n/a)</td><td>58.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>232.40 (n/a)</td><td>186.32 (n/a)</td><td>177.00 (n/a)</td><td>121.90 (n/a)</td><td>46.49 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>235.70 (n/a)</td><td>208.64 (n/a)</td><td>208.80 (n/a)</td><td>183.50 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>178.80 (n/a)</td><td>154.72 (n/a)</td><td>153.30 (n/a)</td><td>126.50 (n/a)</td><td>19.91 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>234.60 (n/a)</td><td>183.48 (n/a)</td><td>161.20 (n/a)</td><td>148.90 (n/a)</td><td>40.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>262.90 (n/a)</td><td>195.62 (n/a)</td><td>180.20 (n/a)</td><td>166.70 (n/a)</td><td>38.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>171.20 (n/a)</td><td>170.80 (n/a)</td><td>155.30 (n/a)</td><td>10.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>382.50 (n/a)</td><td>228.42 (n/a)</td><td>214.00 (n/a)</td><td>159.70 (n/a)</td><td>89.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>171.70 (n/a)</td><td>154.56 (n/a)</td><td>159.20 (n/a)</td><td>124.60 (n/a)</td><td>18.42 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.80 (n/a)</td><td>187.36 (n/a)</td><td>175.50 (n/a)</td><td>153.00 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>286.40 (n/a)</td><td>228.28 (n/a)</td><td>222.50 (n/a)</td><td>172.60 (n/a)</td><td>40.99 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 <b>(+23.98%)</b></td><td>0.03 (+9.03%)</td><td>0.03 (+5.10%)</td><td>0.02 (-8.19%)</td><td>0.01 <b>(+119.09%)</b></td><td>206.50 (+8.91%)</td><td>153.62 (-4.82%)</td><td>151.50 (-4.90%)</td><td>112.70 (-19.33%)</td><td>38.29 <b>(+90.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.60 (n/a)</td><td>161.40 (n/a)</td><td>159.30 (n/a)</td><td>139.70 (n/a)</td><td>20.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 <b>(+32.17%)</b></td><td>0.03 <b>(+30.35%)</b></td><td>0.03 <b>(+49.89%)</b></td><td>0.02 (+14.93%)</td><td>0.01 <b>(+76.31%)</b></td><td>229.80 (-12.99%)</td><td>152.06 (-19.78%)</td><td>128.50 <b>(-33.32%)</b></td><td>106.00 <b>(-24.34%)</b></td><td>53.88 (+13.37%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>264.10 (n/a)</td><td>189.56 (n/a)</td><td>192.70 (n/a)</td><td>140.10 (n/a)</td><td>47.52 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+2.56%)</td><td>0.02 (+2.13%)</td><td>0.02 <b>(+22.70%)</b></td><td>0.01 (-14.20%)</td><td>0.01 (-4.75%)</td><td>308.10 (+16.53%)</td><td>195.58 (-1.44%)</td><td>180.60 (-18.50%)</td><td>131.90 (-2.51%)</td><td>66.37 (+18.95%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>264.40 (n/a)</td><td>198.44 (n/a)</td><td>221.60 (n/a)</td><td>135.30 (n/a)</td><td>55.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+11.50%)</td><td>0.03 (+8.67%)</td><td>0.03 (+12.56%)</td><td>0.02 (-7.37%)</td><td>0.00 <b>(+73.04%)</b></td><td>212.90 (+7.96%)</td><td>167.10 (-6.75%)</td><td>156.60 (-11.17%)</td><td>139.50 (-10.29%)</td><td>27.93 <b>(+71.62%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.20 (n/a)</td><td>179.20 (n/a)</td><td>176.30 (n/a)</td><td>155.50 (n/a)</td><td>16.27 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+7.36%)</td><td>0.03 <b>(+22.09%)</b></td><td>0.03 <b>(+28.92%)</b></td><td>0.02 <b>(+42.29%)</b></td><td>0.00 <b>(-42.89%)</b></td><td>165.80 <b>(-29.72%)</b></td><td>146.02 <b>(-21.10%)</b></td><td>142.90 <b>(-22.42%)</b></td><td>125.80 (-6.81%)</td><td>16.80 <b>(-62.37%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>185.08 (n/a)</td><td>184.20 (n/a)</td><td>135.00 (n/a)</td><td>44.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+16.07%)</td><td>0.02 (+14.45%)</td><td>0.02 (+8.18%)</td><td>0.02 (+3.41%)</td><td>0.00 <b>(+68.66%)</b></td><td>205.30 (-3.30%)</td><td>170.66 (-11.23%)</td><td>185.10 (-7.59%)</td><td>134.30 (-13.86%)</td><td>31.10 <b>(+39.47%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.30 (n/a)</td><td>192.24 (n/a)</td><td>200.30 (n/a)</td><td>155.90 (n/a)</td><td>22.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+1.92%)</td><td>0.02 (-5.55%)</td><td>0.02 (-3.95%)</td><td>0.01 (-15.14%)</td><td>0.00 <b>(+20.94%)</b></td><td>284.10 (+17.83%)</td><td>217.30 (+7.25%)</td><td>218.90 (+4.14%)</td><td>163.40 (-1.92%)</td><td>43.70 <b>(+42.70%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.10 (n/a)</td><td>202.62 (n/a)</td><td>210.20 (n/a)</td><td>166.60 (n/a)</td><td>30.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-1.69%)</td><td>0.02 (+8.21%)</td><td>0.02 (+6.98%)</td><td>0.02 <b>(+50.53%)</b></td><td>0.00 <b>(-50.96%)</b></td><td>215.30 <b>(-33.57%)</b></td><td>195.56 (-15.99%)</td><td>206.60 (-6.52%)</td><td>148.40 (+1.71%)</td><td>27.71 <b>(-67.74%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>324.10 (n/a)</td><td>232.78 (n/a)</td><td>221.00 (n/a)</td><td>145.90 (n/a)</td><td>85.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 <b>(+43.17%)</b></td><td>0.06 <b>(+47.38%)</b></td><td>0.06 <b>(+44.38%)</b></td><td>0.04 <b>(+66.74%)</b></td><td>0.01 <b>(+24.56%)</b></td><td>215.30 <b>(-40.03%)</b></td><td>154.32 <b>(-33.64%)</b></td><td>145.70 <b>(-30.72%)</b></td><td>118.70 <b>(-30.14%)</b></td><td>36.81 <b>(-49.56%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>359.00 (n/a)</td><td>232.56 (n/a)</td><td>210.30 (n/a)</td><td>169.90 (n/a)</td><td>72.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (+16.47%)</td><td>0.05 (+1.79%)</td><td>0.04 (-14.85%)</td><td>0.04 (-9.48%)</td><td>0.01 <b>(+184.90%)</b></td><td>196.40 (+10.52%)</td><td>166.20 (+2.01%)</td><td>188.20 (+17.48%)</td><td>125.20 (-14.19%)</td><td>36.83 <b>(+164.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.70 (n/a)</td><td>162.92 (n/a)</td><td>160.20 (n/a)</td><td>145.90 (n/a)</td><td>13.91 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 <b>(-23.53%)</b></td><td>0.05 (-2.46%)</td><td>0.05 (-2.18%)</td><td>0.04 <b>(+21.40%)</b></td><td>0.01 <b>(-56.02%)</b></td><td>188.70 (-17.63%)</td><td>160.88 (-2.33%)</td><td>164.60 (+2.17%)</td><td>137.60 <b>(+30.80%)</b></td><td>21.14 <b>(-52.34%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>229.10 (n/a)</td><td>164.72 (n/a)</td><td>161.10 (n/a)</td><td>105.20 (n/a)</td><td>44.35 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (+8.59%)</td><td>0.05 (-3.54%)</td><td>0.05 (-2.95%)</td><td>0.03 <b>(-22.17%)</b></td><td>0.01 <b>(+127.27%)</b></td><td>246.20 <b>(+28.50%)</b></td><td>185.02 (+7.44%)</td><td>176.00 (+3.04%)</td><td>136.80 (-7.88%)</td><td>43.28 <b>(+173.30%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.60 (n/a)</td><td>172.20 (n/a)</td><td>170.80 (n/a)</td><td>148.50 (n/a)</td><td>15.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (-0.69%)</td><td>0.05 <b>(+20.36%)</b></td><td>0.05 (-3.39%)</td><td>0.04 <b>(+86.85%)</b></td><td>0.01 <b>(-61.80%)</b></td><td>205.20 <b>(-46.48%)</b></td><td>173.64 <b>(-29.24%)</b></td><td>174.40 (+3.56%)</td><td>150.00 (+0.74%)</td><td>23.26 <b>(-80.43%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>383.40 (n/a)</td><td>245.40 (n/a)</td><td>168.40 (n/a)</td><td>148.90 (n/a)</td><td>118.88 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 <b>(+40.43%)</b></td><td>0.05 <b>(+30.63%)</b></td><td>0.06 <b>(+46.16%)</b></td><td>0.04 (+4.26%)</td><td>0.01 <b>(+163.86%)</b></td><td>219.80 (-4.10%)</td><td>160.04 (-19.57%)</td><td>136.20 <b>(-31.59%)</b></td><td>117.80 <b>(-28.78%)</b></td><td>46.23 <b>(+82.36%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>198.98 (n/a)</td><td>199.10 (n/a)</td><td>165.40 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (-16.44%)</td><td>0.06 (+14.28%)</td><td>0.05 <b>(+20.56%)</b></td><td>0.05 <b>(+36.07%)</b></td><td>0.01 <b>(-60.47%)</b></td><td>174.80 <b>(-26.52%)</b></td><td>149.70 (-18.24%)</td><td>153.10 (-17.02%)</td><td>129.20 (+19.74%)</td><td>18.04 <b>(-65.42%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>237.90 (n/a)</td><td>183.10 (n/a)</td><td>184.50 (n/a)</td><td>107.90 (n/a)</td><td>52.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (+12.88%)</td><td>0.05 (+4.60%)</td><td>0.05 (-1.49%)</td><td>0.04 (-3.06%)</td><td>0.01 <b>(+26.97%)</b></td><td>209.30 (+3.15%)</td><td>165.58 (-3.64%)</td><td>160.20 (+1.52%)</td><td>131.30 (-11.40%)</td><td>30.19 (+15.31%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>171.84 (n/a)</td><td>157.80 (n/a)</td><td>148.20 (n/a)</td><td>26.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 <b>(-21.96%)</b></td><td>0.04 (-3.65%)</td><td>0.05 (+18.65%)</td><td>0.04 (+6.35%)</td><td>0.01 <b>(-55.62%)</b></td><td>219.90 (-5.99%)</td><td>184.66 (+0.04%)</td><td>171.80 (-15.74%)</td><td>165.30 <b>(+28.14%)</b></td><td>23.38 <b>(-46.07%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>184.58 (n/a)</td><td>203.90 (n/a)</td><td>129.00 (n/a)</td><td>43.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 <b>(-21.57%)</b></td><td>0.04 (-4.53%)</td><td>0.04 (+10.83%)</td><td>0.04 (-3.87%)</td><td>0.00 <b>(-49.53%)</b></td><td>229.40 (+4.04%)</td><td>203.10 (+3.17%)</td><td>189.40 (-9.77%)</td><td>187.60 <b>(+27.53%)</b></td><td>20.44 <b>(-33.75%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>196.86 (n/a)</td><td>209.90 (n/a)</td><td>147.10 (n/a)</td><td>30.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (+2.36%)</td><td>0.11 (+11.00%)</td><td>0.11 (+13.44%)</td><td>0.08 <b>(+88.67%)</b></td><td>0.02 <b>(-33.05%)</b></td><td>196.60 <b>(-46.99%)</b></td><td>156.98 (-19.69%)</td><td>143.40 (-11.86%)</td><td>116.30 (-2.35%)</td><td>33.55 <b>(-66.77%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>370.90 (n/a)</td><td>195.46 (n/a)</td><td>162.70 (n/a)</td><td>119.10 (n/a)</td><td>100.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (-8.64%)</td><td>0.10 (-7.35%)</td><td>0.10 (-3.04%)</td><td>0.09 (-3.35%)</td><td>0.01 <b>(-23.19%)</b></td><td>179.40 (+3.46%)</td><td>168.06 (+7.46%)</td><td>171.60 (+3.12%)</td><td>139.50 (+9.50%)</td><td>16.44 (-13.99%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>173.40 (n/a)</td><td>156.40 (n/a)</td><td>166.40 (n/a)</td><td>127.40 (n/a)</td><td>19.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 <b>(-23.25%)</b></td><td>0.09 (-17.05%)</td><td>0.09 (-19.99%)</td><td>0.08 (+5.49%)</td><td>0.01 <b>(-67.91%)</b></td><td>194.20 (-5.18%)</td><td>177.86 (+17.21%)</td><td>181.90 <b>(+25.02%)</b></td><td>163.60 <b>(+30.36%)</b></td><td>12.92 <b>(-60.35%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.80 (n/a)</td><td>151.74 (n/a)</td><td>145.50 (n/a)</td><td>125.50 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (-6.16%)</td><td>0.09 (+4.33%)</td><td>0.10 (+5.39%)</td><td>0.08 <b>(+24.55%)</b></td><td>0.01 <b>(-51.42%)</b></td><td>200.10 (-19.74%)</td><td>173.46 (-6.29%)</td><td>167.70 (-5.15%)</td><td>162.40 (+6.56%)</td><td>15.29 <b>(-59.37%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>249.30 (n/a)</td><td>185.10 (n/a)</td><td>176.80 (n/a)</td><td>152.40 (n/a)</td><td>37.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (-0.46%)</td><td>0.10 (-3.41%)</td><td>0.10 (-10.29%)</td><td>0.07 (-2.33%)</td><td>0.02 (+2.08%)</td><td>223.60 (+2.38%)</td><td>172.08 (+3.73%)</td><td>171.30 (+11.45%)</td><td>133.70 (+0.45%)</td><td>36.59 (+3.60%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>218.40 (n/a)</td><td>165.90 (n/a)</td><td>153.70 (n/a)</td><td>133.10 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (-9.93%)</td><td>0.08 (-10.87%)</td><td>0.08 (-10.12%)</td><td>0.06 <b>(-22.06%)</b></td><td>0.02 (+1.25%)</td><td>291.30 <b>(+28.27%)</b></td><td>206.48 (+14.05%)</td><td>194.50 (+11.27%)</td><td>145.90 (+11.04%)</td><td>55.63 <b>(+44.26%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.10 (n/a)</td><td>181.04 (n/a)</td><td>174.80 (n/a)</td><td>131.40 (n/a)</td><td>38.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (+12.99%)</td><td>0.10 (+2.64%)</td><td>0.09 (+3.89%)</td><td>0.07 (-14.43%)</td><td>0.02 <b>(+115.56%)</b></td><td>219.00 (+16.86%)</td><td>175.68 (-0.17%)</td><td>173.30 (-3.72%)</td><td>132.80 (-11.47%)</td><td>33.79 <b>(+126.90%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>187.40 (n/a)</td><td>175.98 (n/a)</td><td>180.00 (n/a)</td><td>150.00 (n/a)</td><td>14.89 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 <b>(+44.65%)</b></td><td>0.07 (-0.65%)</td><td>0.07 (-10.21%)</td><td>0.05 (-16.85%)</td><td>0.03 <b>(+238.14%)</b></td><td>325.50 <b>(+20.29%)</b></td><td>247.10 (+10.32%)</td><td>240.40 (+11.35%)</td><td>134.00 <b>(-30.86%)</b></td><td>79.09 <b>(+178.70%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>270.60 (n/a)</td><td>223.98 (n/a)</td><td>215.90 (n/a)</td><td>193.80 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 <b>(+23.59%)</b></td><td>0.23 (+11.00%)</td><td>0.24 (+16.91%)</td><td>0.18 (-1.19%)</td><td>0.05 <b>(+133.99%)</b></td><td>178.10 (+1.19%)</td><td>145.80 (-7.38%)</td><td>138.80 (-14.48%)</td><td>110.20 (-19.09%)</td><td>30.49 <b>(+100.44%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>176.00 (n/a)</td><td>157.42 (n/a)</td><td>162.30 (n/a)</td><td>136.20 (n/a)</td><td>15.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (+9.20%)</td><td>0.23 (+9.50%)</td><td>0.24 (+19.68%)</td><td>0.18 (+3.95%)</td><td>0.04 <b>(+25.29%)</b></td><td>180.60 (-3.78%)</td><td>145.68 (-8.11%)</td><td>136.30 (-16.43%)</td><td>120.20 (-8.45%)</td><td>24.25 (+12.21%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>187.70 (n/a)</td><td>158.54 (n/a)</td><td>163.10 (n/a)</td><td>131.30 (n/a)</td><td>21.61 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (+19.81%)</td><td>0.25 (+18.61%)</td><td>0.24 (+12.80%)</td><td>0.19 (+13.26%)</td><td>0.04 <b>(+23.53%)</b></td><td>170.10 (-11.73%)</td><td>135.62 (-15.50%)</td><td>134.40 (-11.35%)</td><td>111.10 (-16.53%)</td><td>22.37 (-9.38%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.70 (n/a)</td><td>160.50 (n/a)</td><td>151.60 (n/a)</td><td>133.10 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (+5.25%)</td><td>0.24 (+7.16%)</td><td>0.24 (+3.64%)</td><td>0.18 (+8.34%)</td><td>0.04 (+15.94%)</td><td>181.60 (-7.68%)</td><td>140.12 (-6.40%)</td><td>136.60 (-3.46%)</td><td>116.20 (-4.99%)</td><td>26.91 (-3.61%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>196.70 (n/a)</td><td>149.70 (n/a)</td><td>141.50 (n/a)</td><td>122.30 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (+16.07%)</td><td>0.20 (+4.96%)</td><td>0.18 (-8.07%)</td><td>0.16 (+6.16%)</td><td>0.04 <b>(+61.14%)</b></td><td>203.80 (-5.82%)</td><td>170.48 (-3.22%)</td><td>178.80 (+8.76%)</td><td>133.60 (-13.86%)</td><td>32.31 <b>(+28.87%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>216.40 (n/a)</td><td>176.16 (n/a)</td><td>164.40 (n/a)</td><td>155.10 (n/a)</td><td>25.07 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 <b>(+22.80%)</b></td><td>0.21 (+15.09%)</td><td>0.20 (+18.93%)</td><td>0.14 (-5.55%)</td><td>0.06 <b>(+56.27%)</b></td><td>227.10 (+5.87%)</td><td>166.28 (-10.52%)</td><td>162.70 (-15.92%)</td><td>107.80 (-18.58%)</td><td>42.90 <b>(+37.36%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>214.50 (n/a)</td><td>185.82 (n/a)</td><td>193.50 (n/a)</td><td>132.40 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (+8.96%)</td><td>0.16 (-2.31%)</td><td>0.16 (-7.88%)</td><td>0.14 (-7.89%)</td><td>0.03 <b>(+58.63%)</b></td><td>238.20 (+8.57%)</td><td>204.00 (+3.61%)</td><td>202.00 (+8.54%)</td><td>161.70 (-8.23%)</td><td>31.82 <b>(+57.30%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.40 (n/a)</td><td>196.90 (n/a)</td><td>186.10 (n/a)</td><td>176.20 (n/a)</td><td>20.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-6.88%)</td><td>0.03 (-9.55%)</td><td>0.03 (-10.75%)</td><td>0.02 <b>(-30.97%)</b></td><td>0.01 <b>(+65.74%)</b></td><td>224.00 <b>(+44.89%)</b></td><td>155.78 (+14.24%)</td><td>150.20 (+12.01%)</td><td>125.30 (+7.37%)</td><td>39.90 <b>(+161.54%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>154.60 (n/a)</td><td>136.36 (n/a)</td><td>134.10 (n/a)</td><td>116.70 (n/a)</td><td>15.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-2.25%)</td><td>0.03 (-17.40%)</td><td>0.03 (-15.05%)</td><td>0.02 <b>(-39.27%)</b></td><td>0.01 <b>(+149.35%)</b></td><td>234.10 <b>(+64.63%)</b></td><td>160.02 <b>(+26.80%)</b></td><td>143.10 (+17.68%)</td><td>121.20 (+2.28%)</td><td>44.35 <b>(+337.11%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>142.20 (n/a)</td><td>126.20 (n/a)</td><td>121.60 (n/a)</td><td>118.50 (n/a)</td><td>10.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.00 (-0.01%)</td><td>0.00 (-0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-82.60%)</b></td><td>4746009.70 (-0.00%)</td><td>4745975.80 (+0.00%)</td><td>4745975.80 (-0.00%)</td><td>4745941.90 (+0.01%)</td><td>47.94 <b>(-82.57%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4746168.60 (n/a)</td><td>4745970.50 (n/a)</td><td>4746086.40 (n/a)</td><td>4745656.50 (n/a)</td><td>275.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+4.47%)</td><td>0.02 (+7.81%)</td><td>0.02 (+17.32%)</td><td>0.02 (-2.68%)</td><td>0.00 <b>(+22.84%)</b></td><td>240.70 (+2.73%)</td><td>179.18 (-6.34%)</td><td>166.40 (-14.75%)</td><td>147.60 (-4.28%)</td><td>36.66 <b>(+24.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.30 (n/a)</td><td>191.30 (n/a)</td><td>195.20 (n/a)</td><td>154.20 (n/a)</td><td>29.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 <b>(-37.27%)</b></td><td>0.02 <b>(-25.89%)</b></td><td>0.02 (-19.10%)</td><td>0.02 <b>(-28.46%)</b></td><td>0.00 <b>(-54.44%)</b></td><td>238.50 <b>(+39.80%)</b></td><td>197.60 <b>(+33.08%)</b></td><td>186.20 <b>(+23.64%)</b></td><td>170.70 <b>(+59.38%)</b></td><td>26.22 (+6.08%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>170.60 (n/a)</td><td>148.48 (n/a)</td><td>150.60 (n/a)</td><td>107.10 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-3.87%)</td><td>0.03 (-8.40%)</td><td>0.02 (-17.20%)</td><td>0.02 (-12.34%)</td><td>0.01 (+11.99%)</td><td>205.00 (+14.08%)</td><td>157.60 (+10.46%)</td><td>166.50 <b>(+20.74%)</b></td><td>120.00 (+4.08%)</td><td>34.38 <b>(+29.94%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>179.70 (n/a)</td><td>142.68 (n/a)</td><td>137.90 (n/a)</td><td>115.30 (n/a)</td><td>26.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-19.13%)</td><td>0.02 <b>(-21.22%)</b></td><td>0.02 (-15.75%)</td><td>0.02 <b>(-38.26%)</b></td><td>0.00 <b>(+30.39%)</b></td><td>259.30 <b>(+61.96%)</b></td><td>189.42 <b>(+30.28%)</b></td><td>179.40 (+18.73%)</td><td>147.50 <b>(+23.64%)</b></td><td>42.95 <b>(+173.12%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>160.10 (n/a)</td><td>145.40 (n/a)</td><td>151.10 (n/a)</td><td>119.30 (n/a)</td><td>15.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 <b>(-21.66%)</b></td><td>0.02 <b>(-32.95%)</b></td><td>0.02 <b>(-21.97%)</b></td><td>0.01 <b>(-51.95%)</b></td><td>0.01 <b>(+31.13%)</b></td><td>356.70 <b>(+108.11%)</b></td><td>229.68 <b>(+59.59%)</b></td><td>190.30 <b>(+28.15%)</b></td><td>154.30 <b>(+27.63%)</b></td><td>81.05 <b>(+267.52%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.40 (n/a)</td><td>143.92 (n/a)</td><td>148.50 (n/a)</td><td>120.90 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (+9.54%)</td><td>0.03 (-12.20%)</td><td>0.02 (-13.92%)</td><td>0.02 (-9.92%)</td><td>0.01 <b>(+54.13%)</b></td><td>206.90 (+11.06%)</td><td>172.36 (+17.46%)</td><td>173.30 (+16.15%)</td><td>109.20 (-8.70%)</td><td>39.65 <b>(+54.37%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.30 (n/a)</td><td>146.74 (n/a)</td><td>149.20 (n/a)</td><td>119.60 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-17.64%)</td><td>0.02 (-19.34%)</td><td>0.02 <b>(-23.32%)</b></td><td>0.02 (-3.60%)</td><td>0.00 <b>(-44.52%)</b></td><td>201.30 (+3.71%)</td><td>180.98 <b>(+22.05%)</b></td><td>176.30 <b>(+30.40%)</b></td><td>153.50 <b>(+21.34%)</b></td><td>20.36 <b>(-28.31%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.10 (n/a)</td><td>148.28 (n/a)</td><td>135.20 (n/a)</td><td>126.50 (n/a)</td><td>28.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (+1.60%)</td><td>0.03 (-3.84%)</td><td>0.03 (+8.08%)</td><td>0.02 <b>(-31.06%)</b></td><td>0.01 <b>(+76.62%)</b></td><td>216.70 <b>(+45.05%)</b></td><td>151.40 (+7.94%)</td><td>136.30 (-7.47%)</td><td>111.90 (-1.58%)</td><td>39.71 <b>(+164.23%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>149.40 (n/a)</td><td>140.26 (n/a)</td><td>147.30 (n/a)</td><td>113.70 (n/a)</td><td>15.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-16.32%)</td><td>0.03 (+4.05%)</td><td>0.03 (+8.86%)</td><td>0.02 <b>(+59.88%)</b></td><td>0.00 <b>(-61.13%)</b></td><td>184.90 <b>(-37.45%)</b></td><td>155.94 (-13.34%)</td><td>159.80 (-8.16%)</td><td>130.20 (+19.56%)</td><td>21.01 <b>(-71.15%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>295.60 (n/a)</td><td>179.94 (n/a)</td><td>174.00 (n/a)</td><td>108.90 (n/a)</td><td>72.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-5.74%)</td><td>0.03 (-2.93%)</td><td>0.03 (+4.40%)</td><td>0.02 <b>(-25.41%)</b></td><td>0.01 <b>(+38.34%)</b></td><td>267.70 <b>(+34.05%)</b></td><td>174.30 (+7.79%)</td><td>150.20 (-4.21%)</td><td>129.20 (+6.08%)</td><td>57.59 <b>(+96.62%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.70 (n/a)</td><td>161.70 (n/a)</td><td>156.80 (n/a)</td><td>121.80 (n/a)</td><td>29.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (-9.91%)</td><td>0.02 (-11.13%)</td><td>0.02 (-11.65%)</td><td>0.02 (-11.08%)</td><td>0.00 (+0.99%)</td><td>232.10 (+12.45%)</td><td>202.20 (+12.71%)</td><td>192.50 (+13.17%)</td><td>185.20 (+11.03%)</td><td>20.85 <b>(+24.93%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.40 (n/a)</td><td>179.40 (n/a)</td><td>170.10 (n/a)</td><td>166.80 (n/a)</td><td>16.69 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 <b>(+29.28%)</b></td><td>0.03 <b>(+20.04%)</b></td><td>0.03 <b>(+23.63%)</b></td><td>0.02 (+15.15%)</td><td>0.01 <b>(+52.55%)</b></td><td>209.40 (-13.18%)</td><td>166.20 (-15.75%)</td><td>159.80 (-19.09%)</td><td>124.20 <b>(-22.67%)</b></td><td>32.75 (+3.14%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.20 (n/a)</td><td>197.26 (n/a)</td><td>197.50 (n/a)</td><td>160.60 (n/a)</td><td>31.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+13.05%)</td><td>0.03 <b>(+26.63%)</b></td><td>0.03 <b>(+38.99%)</b></td><td>0.02 <b>(+31.07%)</b></td><td>0.00 (-19.91%)</td><td>178.70 <b>(-23.70%)</b></td><td>160.76 <b>(-22.07%)</b></td><td>162.20 <b>(-28.04%)</b></td><td>138.80 (-11.54%)</td><td>18.11 <b>(-45.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.20 (n/a)</td><td>206.28 (n/a)</td><td>225.40 (n/a)</td><td>156.90 (n/a)</td><td>33.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (-7.33%)</td><td>0.05 (-1.35%)</td><td>0.05 (-7.54%)</td><td>0.04 (+13.48%)</td><td>0.01 <b>(-25.20%)</b></td><td>186.40 (-11.91%)</td><td>161.68 (-0.97%)</td><td>169.50 (+8.17%)</td><td>118.80 (+7.90%)</td><td>28.35 <b>(-28.53%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>163.26 (n/a)</td><td>156.70 (n/a)</td><td>110.10 (n/a)</td><td>39.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (+12.37%)</td><td>0.06 (+1.16%)</td><td>0.06 (-5.35%)</td><td>0.05 (+0.33%)</td><td>0.01 <b>(+36.57%)</b></td><td>175.90 (-0.34%)</td><td>144.78 (-0.17%)</td><td>144.80 (+5.62%)</td><td>108.50 (-10.99%)</td><td>25.14 (+17.97%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.50 (n/a)</td><td>145.02 (n/a)</td><td>137.10 (n/a)</td><td>121.90 (n/a)</td><td>21.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 <b>(-37.79%)</b></td><td>0.04 (-12.47%)</td><td>0.04 (-5.88%)</td><td>0.03 (+9.21%)</td><td>0.01 <b>(-63.45%)</b></td><td>306.60 (-8.42%)</td><td>228.96 (+4.13%)</td><td>222.80 (+6.25%)</td><td>190.60 <b>(+60.71%)</b></td><td>45.64 <b>(-43.80%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>334.80 (n/a)</td><td>219.88 (n/a)</td><td>209.70 (n/a)</td><td>118.60 (n/a)</td><td>81.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 <b>(+23.08%)</b></td><td>0.04 (+5.84%)</td><td>0.05 (-0.72%)</td><td>0.03 (-2.01%)</td><td>0.01 <b>(+57.72%)</b></td><td>283.00 (+2.06%)</td><td>195.20 (-2.63%)</td><td>179.20 (+0.73%)</td><td>142.10 (-18.75%)</td><td>56.68 <b>(+29.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>277.30 (n/a)</td><td>200.48 (n/a)</td><td>177.90 (n/a)</td><td>174.90 (n/a)</td><td>43.70 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (-8.31%)</td><td>0.05 (-4.79%)</td><td>0.05 (-10.52%)</td><td>0.04 (+4.69%)</td><td>0.00 <b>(-43.92%)</b></td><td>182.90 (-4.44%)</td><td>172.58 (+4.35%)</td><td>178.00 (+11.81%)</td><td>156.70 (+9.05%)</td><td>10.68 <b>(-41.98%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.40 (n/a)</td><td>165.38 (n/a)</td><td>159.20 (n/a)</td><td>143.70 (n/a)</td><td>18.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (+18.14%)</td><td>0.05 (+4.59%)</td><td>0.05 (+4.00%)</td><td>0.04 (-6.82%)</td><td>0.01 <b>(+59.41%)</b></td><td>215.60 (+7.32%)</td><td>160.54 (-1.95%)</td><td>155.30 (-3.84%)</td><td>111.20 (-15.31%)</td><td>37.82 <b>(+43.22%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.90 (n/a)</td><td>163.74 (n/a)</td><td>161.50 (n/a)</td><td>131.30 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (+7.31%)</td><td>0.05 (+6.87%)</td><td>0.05 (+6.49%)</td><td>0.04 (-1.54%)</td><td>0.01 <b>(+24.04%)</b></td><td>205.60 (+1.53%)</td><td>160.90 (-5.66%)</td><td>162.80 (-6.11%)</td><td>127.10 (-6.82%)</td><td>29.87 (+18.27%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>170.56 (n/a)</td><td>173.40 (n/a)</td><td>136.40 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (+19.72%)</td><td>0.06 <b>(+20.26%)</b></td><td>0.06 (+11.13%)</td><td>0.04 <b>(+21.61%)</b></td><td>0.01 (+8.20%)</td><td>187.80 (-17.78%)</td><td>141.88 (-17.59%)</td><td>136.30 (-10.03%)</td><td>108.80 (-16.50%)</td><td>30.32 <b>(-26.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>172.16 (n/a)</td><td>151.50 (n/a)</td><td>130.30 (n/a)</td><td>41.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (+2.61%)</td><td>0.05 (+18.53%)</td><td>0.06 (+17.16%)</td><td>0.04 <b>(+57.38%)</b></td><td>0.01 <b>(-37.29%)</b></td><td>189.30 <b>(-36.46%)</b></td><td>152.34 <b>(-20.12%)</b></td><td>140.50 (-14.64%)</td><td>132.50 (-2.50%)</td><td>23.70 <b>(-62.81%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.90 (n/a)</td><td>190.70 (n/a)</td><td>164.60 (n/a)</td><td>135.90 (n/a)</td><td>63.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 <b>(+47.07%)</b></td><td>0.06 <b>(+36.13%)</b></td><td>0.06 <b>(+30.45%)</b></td><td>0.04 <b>(+23.05%)</b></td><td>0.02 <b>(+59.57%)</b></td><td>192.70 (-18.73%)</td><td>137.30 <b>(-25.22%)</b></td><td>127.20 <b>(-23.33%)</b></td><td>94.00 <b>(-32.03%)</b></td><td>40.46 (-13.36%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.10 (n/a)</td><td>183.60 (n/a)</td><td>165.90 (n/a)</td><td>138.30 (n/a)</td><td>46.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (-0.46%)</td><td>0.05 (+0.94%)</td><td>0.05 (-1.23%)</td><td>0.04 <b>(+21.40%)</b></td><td>0.01 <b>(-32.28%)</b></td><td>190.80 (-17.65%)</td><td>157.78 (-3.49%)</td><td>158.80 (+1.28%)</td><td>129.70 (+0.46%)</td><td>22.43 <b>(-44.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>163.48 (n/a)</td><td>156.80 (n/a)</td><td>129.10 (n/a)</td><td>40.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (-13.24%)</td><td>0.05 (-0.64%)</td><td>0.05 (+8.11%)</td><td>0.04 <b>(+22.56%)</b></td><td>0.01 <b>(-50.93%)</b></td><td>182.30 (-18.43%)</td><td>158.08 (-4.24%)</td><td>155.20 (-7.51%)</td><td>127.50 (+15.28%)</td><td>21.25 <b>(-53.60%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>223.50 (n/a)</td><td>165.08 (n/a)</td><td>167.80 (n/a)</td><td>110.60 (n/a)</td><td>45.80 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 <b>(-23.45%)</b></td><td>0.04 (-13.16%)</td><td>0.04 <b>(-25.09%)</b></td><td>0.04 <b>(+38.85%)</b></td><td>0.01 <b>(-64.28%)</b></td><td>222.10 <b>(-27.98%)</b></td><td>193.42 (+3.65%)</td><td>203.40 <b>(+33.55%)</b></td><td>159.90 <b>(+30.64%)</b></td><td>26.53 <b>(-66.15%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>308.40 (n/a)</td><td>186.60 (n/a)</td><td>152.30 (n/a)</td><td>122.40 (n/a)</td><td>78.38 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 <b>(-26.00%)</b></td><td>0.05 (-13.80%)</td><td>0.05 (-17.81%)</td><td>0.04 (-1.14%)</td><td>0.00 <b>(-67.56%)</b></td><td>206.60 (+1.13%)</td><td>177.08 (+11.29%)</td><td>171.10 <b>(+21.69%)</b></td><td>163.60 <b>(+35.21%)</b></td><td>17.31 <b>(-56.73%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>159.12 (n/a)</td><td>140.60 (n/a)</td><td>121.00 (n/a)</td><td>40.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 <b>(+20.16%)</b></td><td>0.05 (+4.37%)</td><td>0.05 (+4.65%)</td><td>0.04 (-1.62%)</td><td>0.01 <b>(+58.07%)</b></td><td>207.50 (+1.67%)</td><td>175.94 (-2.87%)</td><td>180.50 (-4.40%)</td><td>129.80 (-16.74%)</td><td>29.71 <b>(+32.56%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>181.14 (n/a)</td><td>188.80 (n/a)</td><td>155.90 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 <b>(-29.69%)</b></td><td>0.04 (-10.25%)</td><td>0.05 (-8.22%)</td><td>0.03 (+0.24%)</td><td>0.01 <b>(-54.67%)</b></td><td>238.60 (-0.25%)</td><td>186.20 (+6.85%)</td><td>175.80 (+8.99%)</td><td>163.00 <b>(+42.23%)</b></td><td>30.73 <b>(-34.63%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>174.26 (n/a)</td><td>161.30 (n/a)</td><td>114.60 (n/a)</td><td>47.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 <b>(-21.99%)</b></td><td>0.10 (-5.35%)</td><td>0.10 (+17.47%)</td><td>0.09 (+16.84%)</td><td>0.01 <b>(-69.02%)</b></td><td>191.30 (-14.45%)</td><td>171.76 (-0.50%)</td><td>165.40 (-14.83%)</td><td>151.10 <b>(+28.16%)</b></td><td>16.79 <b>(-64.60%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>223.60 (n/a)</td><td>172.62 (n/a)</td><td>194.20 (n/a)</td><td>117.90 (n/a)</td><td>47.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (+4.42%)</td><td>0.11 (+6.21%)</td><td>0.10 (+0.96%)</td><td>0.09 <b>(+24.44%)</b></td><td>0.02 (-8.13%)</td><td>185.50 (-19.66%)</td><td>154.92 (-7.22%)</td><td>164.00 (-0.97%)</td><td>125.00 (-4.21%)</td><td>27.92 <b>(-30.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.90 (n/a)</td><td>166.98 (n/a)</td><td>165.60 (n/a)</td><td>130.50 (n/a)</td><td>40.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 <b>(+26.90%)</b></td><td>0.08 (+4.86%)</td><td>0.07 (-3.28%)</td><td>0.05 (-13.68%)</td><td>0.03 <b>(+78.84%)</b></td><td>349.70 (+15.87%)</td><td>227.78 (+1.22%)</td><td>232.40 (+3.38%)</td><td>137.20 <b>(-21.19%)</b></td><td>79.08 <b>(+61.81%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>301.80 (n/a)</td><td>225.04 (n/a)</td><td>224.80 (n/a)</td><td>174.10 (n/a)</td><td>48.88 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 <b>(-25.00%)</b></td><td>0.08 <b>(-20.89%)</b></td><td>0.07 (-18.84%)</td><td>0.06 (-17.71%)</td><td>0.01 <b>(-34.50%)</b></td><td>288.00 <b>(+21.52%)</b></td><td>224.30 <b>(+25.03%)</b></td><td>222.70 <b>(+23.24%)</b></td><td>173.60 <b>(+33.33%)</b></td><td>41.92 (+7.19%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>237.00 (n/a)</td><td>179.40 (n/a)</td><td>180.70 (n/a)</td><td>130.20 (n/a)</td><td>39.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (-18.34%)</td><td>0.09 <b>(-22.93%)</b></td><td>0.09 <b>(-30.79%)</b></td><td>0.08 (-16.16%)</td><td>0.01 <b>(-21.84%)</b></td><td>212.30 (+19.27%)</td><td>179.26 <b>(+29.43%)</b></td><td>184.10 <b>(+44.51%)</b></td><td>149.10 <b>(+22.41%)</b></td><td>25.82 (+11.43%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>178.00 (n/a)</td><td>138.50 (n/a)</td><td>127.40 (n/a)</td><td>121.80 (n/a)</td><td>23.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (-3.66%)</td><td>0.10 (-8.47%)</td><td>0.09 (-9.56%)</td><td>0.08 (-11.38%)</td><td>0.02 (+10.56%)</td><td>202.80 (+12.85%)</td><td>176.90 (+10.27%)</td><td>189.10 (+10.58%)</td><td>122.20 (+3.74%)</td><td>31.56 <b>(+28.27%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>179.70 (n/a)</td><td>160.42 (n/a)</td><td>171.00 (n/a)</td><td>117.80 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 <b>(+48.81%)</b></td><td>0.11 (+18.12%)</td><td>0.10 (+8.51%)</td><td>0.08 (+14.05%)</td><td>0.03 <b>(+129.58%)</b></td><td>202.90 (-12.32%)</td><td>163.46 (-12.15%)</td><td>166.90 (-7.84%)</td><td>104.10 <b>(-32.84%)</b></td><td>39.11 <b>(+32.36%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>186.06 (n/a)</td><td>181.10 (n/a)</td><td>155.00 (n/a)</td><td>29.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (+2.17%)</td><td>0.09 (+8.58%)</td><td>0.09 (+0.57%)</td><td>0.07 <b>(+46.18%)</b></td><td>0.02 <b>(-25.17%)</b></td><td>249.40 <b>(-31.60%)</b></td><td>179.36 (-13.79%)</td><td>177.40 (-0.56%)</td><td>141.50 (-2.14%)</td><td>42.46 <b>(-52.44%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>364.60 (n/a)</td><td>208.04 (n/a)</td><td>178.40 (n/a)</td><td>144.60 (n/a)</td><td>89.28 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (+18.74%)</td><td>0.10 (+13.89%)</td><td>0.08 (-5.45%)</td><td>0.07 <b>(+66.06%)</b></td><td>0.03 (+15.15%)</td><td>226.80 <b>(-39.78%)</b></td><td>180.74 (-15.41%)</td><td>206.40 (+5.74%)</td><td>110.90 (-15.79%)</td><td>54.48 <b>(-42.94%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>376.60 (n/a)</td><td>213.66 (n/a)</td><td>195.20 (n/a)</td><td>131.70 (n/a)</td><td>95.47 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (-1.84%)</td><td>0.10 (+0.47%)</td><td>0.09 (-7.87%)</td><td>0.09 (+7.23%)</td><td>0.01 (+6.20%)</td><td>184.70 (-6.76%)</td><td>168.82 (-0.35%)</td><td>183.30 (+8.53%)</td><td>144.10 (+1.91%)</td><td>20.84 (+2.00%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>169.42 (n/a)</td><td>168.90 (n/a)</td><td>141.40 (n/a)</td><td>20.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 <b>(-24.38%)</b></td><td>0.10 (+2.54%)</td><td>0.10 (+4.58%)</td><td>0.09 <b>(+64.70%)</b></td><td>0.01 <b>(-67.56%)</b></td><td>179.70 <b>(-39.29%)</b></td><td>163.72 (-12.68%)</td><td>171.90 (-4.39%)</td><td>134.50 <b>(+32.25%)</b></td><td>19.02 <b>(-73.61%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>296.00 (n/a)</td><td>187.50 (n/a)</td><td>179.80 (n/a)</td><td>101.70 (n/a)</td><td>72.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (-17.29%)</td><td>0.10 (-12.61%)</td><td>0.10 <b>(-20.11%)</b></td><td>0.08 (+2.85%)</td><td>0.01 <b>(-41.39%)</b></td><td>193.50 (-2.76%)</td><td>169.14 (+11.88%)</td><td>169.60 <b>(+25.26%)</b></td><td>140.40 <b>(+20.93%)</b></td><td>23.51 <b>(-31.12%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.00 (n/a)</td><td>151.18 (n/a)</td><td>135.40 (n/a)</td><td>116.10 (n/a)</td><td>34.14 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (-1.51%)</td><td>0.09 (-9.01%)</td><td>0.10 (-8.43%)</td><td>0.06 (-16.90%)</td><td>0.02 (-6.13%)</td><td>296.20 <b>(+20.31%)</b></td><td>192.88 (+10.80%)</td><td>170.40 (+9.23%)</td><td>134.40 (+1.51%)</td><td>61.54 <b>(+24.02%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>246.20 (n/a)</td><td>174.08 (n/a)</td><td>156.00 (n/a)</td><td>132.40 (n/a)</td><td>49.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (-12.60%)</td><td>0.10 (-0.36%)</td><td>0.11 (+1.83%)</td><td>0.09 (+7.00%)</td><td>0.01 <b>(-42.89%)</b></td><td>183.70 (-6.56%)</td><td>158.60 (-0.76%)</td><td>154.60 (-1.78%)</td><td>148.00 (+14.46%)</td><td>14.64 <b>(-38.98%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.60 (n/a)</td><td>159.82 (n/a)</td><td>157.40 (n/a)</td><td>129.30 (n/a)</td><td>23.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (+5.20%)</td><td>0.09 (-11.84%)</td><td>0.10 (-4.81%)</td><td>0.05 <b>(-38.65%)</b></td><td>0.02 <b>(+251.12%)</b></td><td>303.30 <b>(+62.98%)</b></td><td>200.84 <b>(+20.87%)</b></td><td>167.80 (+5.07%)</td><td>151.00 (-4.91%)</td><td>63.55 <b>(+444.05%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.10 (n/a)</td><td>166.16 (n/a)</td><td>159.70 (n/a)</td><td>158.80 (n/a)</td><td>11.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (+18.31%)</td><td>0.10 (+7.22%)</td><td>0.10 (+1.47%)</td><td>0.08 (-4.34%)</td><td>0.02 <b>(+86.82%)</b></td><td>207.00 (+4.55%)</td><td>166.84 (-5.08%)</td><td>172.20 (-1.43%)</td><td>130.40 (-15.49%)</td><td>30.04 <b>(+63.27%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.00 (n/a)</td><td>175.76 (n/a)</td><td>174.70 (n/a)</td><td>154.30 (n/a)</td><td>18.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (-0.13%)</td><td>0.21 (-1.12%)</td><td>0.21 (-6.62%)</td><td>0.16 (+3.58%)</td><td>0.04 (-3.80%)</td><td>202.50 (-3.48%)</td><td>159.20 (+0.77%)</td><td>155.80 (+7.08%)</td><td>127.60 (+0.16%)</td><td>28.96 (-9.01%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>209.80 (n/a)</td><td>157.98 (n/a)</td><td>145.50 (n/a)</td><td>127.40 (n/a)</td><td>31.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (-17.39%)</td><td>0.19 (-7.09%)</td><td>0.19 (-3.65%)</td><td>0.14 (+12.16%)</td><td>0.03 <b>(-43.18%)</b></td><td>228.40 (-10.85%)</td><td>175.80 (+3.35%)</td><td>171.90 (+3.80%)</td><td>148.70 <b>(+21.09%)</b></td><td>31.61 <b>(-39.27%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>256.20 (n/a)</td><td>170.10 (n/a)</td><td>165.60 (n/a)</td><td>122.80 (n/a)</td><td>52.04 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (+1.96%)</td><td>0.15 (-11.63%)</td><td>0.15 (-12.37%)</td><td>0.10 <b>(-32.57%)</b></td><td>0.04 <b>(+109.55%)</b></td><td>344.60 <b>(+48.28%)</b></td><td>230.96 (+18.61%)</td><td>215.00 (+14.12%)</td><td>171.90 (-1.94%)</td><td>67.36 <b>(+207.93%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>232.40 (n/a)</td><td>194.72 (n/a)</td><td>188.40 (n/a)</td><td>175.30 (n/a)</td><td>21.88 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (-2.53%)</td><td>0.18 (-3.22%)</td><td>0.17 (-4.84%)</td><td>0.14 (-6.03%)</td><td>0.03 (+18.29%)</td><td>229.80 (+6.39%)</td><td>184.64 (+4.15%)</td><td>188.80 (+5.06%)</td><td>150.70 (+2.59%)</td><td>32.62 <b>(+25.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>216.00 (n/a)</td><td>177.28 (n/a)</td><td>179.70 (n/a)</td><td>146.90 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (-2.55%)</td><td>0.19 (+2.88%)</td><td>0.19 (+3.91%)</td><td>0.16 (+16.31%)</td><td>0.04 (-17.49%)</td><td>210.80 (-13.99%)</td><td>173.94 (-4.42%)</td><td>173.20 (-3.78%)</td><td>129.50 (+2.61%)</td><td>30.73 <b>(-27.31%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>245.10 (n/a)</td><td>181.98 (n/a)</td><td>180.00 (n/a)</td><td>126.20 (n/a)</td><td>42.28 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (+10.42%)</td><td>0.22 (+11.21%)</td><td>0.23 <b>(+25.29%)</b></td><td>0.16 (-8.23%)</td><td>0.05 <b>(+51.06%)</b></td><td>209.50 (+8.94%)</td><td>154.62 (-8.10%)</td><td>143.70 <b>(-20.17%)</b></td><td>122.10 (-9.42%)</td><td>36.35 <b>(+47.37%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.30 (n/a)</td><td>168.24 (n/a)</td><td>180.00 (n/a)</td><td>134.80 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (+4.11%)</td><td>0.22 (+3.27%)</td><td>0.20 (-3.68%)</td><td>0.19 (+3.59%)</td><td>0.03 <b>(+35.75%)</b></td><td>171.10 (-3.50%)</td><td>150.18 (-2.43%)</td><td>160.00 (+3.76%)</td><td>123.50 (-3.89%)</td><td>22.04 <b>(+26.86%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>177.30 (n/a)</td><td>153.92 (n/a)</td><td>154.20 (n/a)</td><td>128.50 (n/a)</td><td>17.37 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (+3.48%)</td><td>0.22 (-0.27%)</td><td>0.21 (+3.61%)</td><td>0.15 <b>(-22.79%)</b></td><td>0.05 <b>(+57.24%)</b></td><td>221.40 <b>(+29.55%)</b></td><td>157.70 (+3.68%)</td><td>154.70 (-3.49%)</td><td>115.80 (-3.42%)</td><td>41.04 <b>(+99.31%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>170.90 (n/a)</td><td>152.10 (n/a)</td><td>160.30 (n/a)</td><td>119.90 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (+8.71%)</td><td>0.22 (+9.46%)</td><td>0.24 (+15.31%)</td><td>0.15 (-9.25%)</td><td>0.05 <b>(+32.70%)</b></td><td>224.90 (+10.19%)</td><td>156.12 (-6.53%)</td><td>137.90 (-13.27%)</td><td>116.70 (-7.97%)</td><td>43.39 <b>(+33.24%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>204.10 (n/a)</td><td>167.02 (n/a)</td><td>159.00 (n/a)</td><td>126.80 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (+15.62%)</td><td>0.22 <b>(+23.33%)</b></td><td>0.20 (+5.53%)</td><td>0.17 <b>(+107.45%)</b></td><td>0.04 <b>(-26.79%)</b></td><td>194.40 <b>(-51.81%)</b></td><td>154.64 <b>(-27.42%)</b></td><td>163.20 (-5.23%)</td><td>117.70 (-13.46%)</td><td>30.08 <b>(-72.26%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>403.40 (n/a)</td><td>213.06 (n/a)</td><td>172.20 (n/a)</td><td>136.00 (n/a)</td><td>108.42 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (-1.66%)</td><td>0.21 (+9.18%)</td><td>0.21 <b>(+20.62%)</b></td><td>0.17 (+4.11%)</td><td>0.04 (-2.77%)</td><td>193.90 (-3.96%)</td><td>158.80 (-8.69%)</td><td>153.30 (-17.09%)</td><td>130.20 (+1.72%)</td><td>29.83 (-7.69%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.90 (n/a)</td><td>173.92 (n/a)</td><td>184.90 (n/a)</td><td>128.00 (n/a)</td><td>32.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (+7.87%)</td><td>0.23 (+13.94%)</td><td>0.21 <b>(+22.74%)</b></td><td>0.19 (+18.59%)</td><td>0.03 <b>(-20.93%)</b></td><td>169.50 (-15.71%)</td><td>147.24 (-13.62%)</td><td>154.20 (-18.54%)</td><td>121.00 (-7.28%)</td><td>19.73 <b>(-38.50%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.10 (n/a)</td><td>170.46 (n/a)</td><td>189.30 (n/a)</td><td>130.50 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (-2.80%)</td><td>0.20 (+0.81%)</td><td>0.20 (+8.23%)</td><td>0.16 (+1.06%)</td><td>0.03 (-10.10%)</td><td>204.80 (-1.06%)</td><td>169.76 (-1.19%)</td><td>167.20 (-7.62%)</td><td>139.00 (+2.89%)</td><td>26.14 (-7.44%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>207.00 (n/a)</td><td>171.80 (n/a)</td><td>181.00 (n/a)</td><td>135.10 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (+12.24%)</td><td>0.21 (+10.13%)</td><td>0.20 (+0.98%)</td><td>0.15 <b>(+22.82%)</b></td><td>0.04 (+4.69%)</td><td>213.30 (-18.59%)</td><td>164.82 (-10.09%)</td><td>161.50 (-0.98%)</td><td>130.20 (-10.94%)</td><td>34.10 <b>(-26.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>262.00 (n/a)</td><td>183.32 (n/a)</td><td>163.10 (n/a)</td><td>146.20 (n/a)</td><td>46.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 <b>(+21.49%)</b></td><td>0.21 (+11.08%)</td><td>0.21 (+8.36%)</td><td>0.18 (-2.02%)</td><td>0.03 <b>(+189.74%)</b></td><td>186.20 (+2.03%)</td><td>156.72 (-8.96%)</td><td>157.60 (-7.73%)</td><td>131.80 (-17.73%)</td><td>20.33 <b>(+144.00%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>172.14 (n/a)</td><td>170.80 (n/a)</td><td>160.20 (n/a)</td><td>8.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (-17.54%)</td><td>0.18 <b>(-22.70%)</b></td><td>0.16 <b>(-27.61%)</b></td><td>0.15 (-11.92%)</td><td>0.04 (-18.41%)</td><td>219.00 (+13.53%)</td><td>190.28 <b>(+28.95%)</b></td><td>200.40 <b>(+38.21%)</b></td><td>135.10 <b>(+21.27%)</b></td><td>33.48 (+9.53%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>192.90 (n/a)</td><td>147.56 (n/a)</td><td>145.00 (n/a)</td><td>111.40 (n/a)</td><td>30.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (-0.53%)</td><td>0.18 (-0.65%)</td><td>0.18 (-0.67%)</td><td>0.18 (-0.70%)</td><td>0.00 <b>(+61.25%)</b></td><td>47908.80 (+0.71%)</td><td>47838.74 (+0.66%)</td><td>47868.80 (+0.67%)</td><td>47717.90 (+0.53%)</td><td>75.42 <b>(+63.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47571.90 (n/a)</td><td>47525.78 (n/a)</td><td>47550.20 (n/a)</td><td>47467.10 (n/a)</td><td>46.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47906.60 (n/a)</td><td>47867.10 (n/a)</td><td>47866.60 (n/a)</td><td>47840.00 (n/a)</td><td>25.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>378022.00 (n/a)</td><td>377932.60 (n/a)</td><td>377932.60 (n/a)</td><td>377819.20 (n/a)</td><td>83.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (-19.36%)</td><td>0.16 (-13.99%)</td><td>0.16 (-14.46%)</td><td>0.11 <b>(-27.05%)</b></td><td>0.03 (-0.87%)</td><td>216.30 <b>(+37.07%)</b></td><td>158.98 (+17.68%)</td><td>151.50 (+16.90%)</td><td>133.50 <b>(+23.96%)</b></td><td>33.87 <b>(+67.73%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>157.80 (n/a)</td><td>135.10 (n/a)</td><td>129.60 (n/a)</td><td>107.70 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.38 (+16.72%)</td><td>0.30 (+0.22%)</td><td>0.30 (-1.50%)</td><td>0.23 (-2.30%)</td><td>0.06 <b>(+62.87%)</b></td><td>211.10 (+2.38%)</td><td>171.26 (+1.39%)</td><td>165.90 (+1.53%)</td><td>130.50 (-14.31%)</td><td>31.61 <b>(+43.02%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>206.20 (n/a)</td><td>168.92 (n/a)</td><td>163.40 (n/a)</td><td>152.30 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>13.15 (-4.05%)</td><td>13.03 (-0.09%)</td><td>13.08 (+2.60%)</td><td>12.87 (+2.90%)</td><td>0.12 <b>(-78.75%)</b></td><td>815.00 (-2.83%)</td><td>805.04 (-0.06%)</td><td>801.60 (-2.54%)</td><td>797.10 (+4.21%)</td><td>7.55 <b>(-78.34%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.71 (n/a)</td><td>13.04 (n/a)</td><td>12.75 (n/a)</td><td>12.50 (n/a)</td><td>0.57 (n/a)</td><td>838.70 (n/a)</td><td>805.50 (n/a)</td><td>822.50 (n/a)</td><td>764.90 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (-0.05%)</td><td>0.24 (-1.36%)</td><td>0.25 (+1.67%)</td><td>0.21 (-2.47%)</td><td>0.02 (+15.79%)</td><td>196.60 (+2.50%)</td><td>172.80 (+1.58%)</td><td>166.70 (-1.65%)</td><td>152.60 (+0.00%)</td><td>17.22 (+19.06%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>191.80 (n/a)</td><td>170.12 (n/a)</td><td>169.50 (n/a)</td><td>152.60 (n/a)</td><td>14.46 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 <b>(-21.99%)</b></td><td>0.03 (-14.06%)</td><td>0.03 (-14.36%)</td><td>0.02 (-9.79%)</td><td>0.00 <b>(-35.32%)</b></td><td>205.60 (+10.84%)</td><td>167.28 (+15.06%)</td><td>169.30 (+16.76%)</td><td>142.00 <b>(+28.16%)</b></td><td>25.03 (-8.43%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>145.38 (n/a)</td><td>145.00 (n/a)</td><td>110.80 (n/a)</td><td>27.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (+15.14%)</td><td>0.03 (+9.70%)</td><td>0.03 (+18.88%)</td><td>0.02 (-9.98%)</td><td>0.01 <b>(+73.73%)</b></td><td>193.80 (+11.06%)</td><td>150.40 (-7.02%)</td><td>141.70 (-15.86%)</td><td>114.50 (-13.19%)</td><td>29.62 <b>(+71.59%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.50 (n/a)</td><td>161.76 (n/a)</td><td>168.40 (n/a)</td><td>131.90 (n/a)</td><td>17.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (-6.36%)</td><td>0.03 <b>(-25.55%)</b></td><td>0.03 <b>(-30.21%)</b></td><td>0.02 <b>(-44.11%)</b></td><td>0.01 <b>(+87.61%)</b></td><td>324.60 <b>(+78.94%)</b></td><td>217.52 <b>(+45.60%)</b></td><td>214.20 <b>(+43.28%)</b></td><td>137.60 (+6.75%)</td><td>75.43 <b>(+256.08%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>149.40 (n/a)</td><td>149.50 (n/a)</td><td>128.90 (n/a)</td><td>21.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 <b>(+26.95%)</b></td><td>0.03 (+16.10%)</td><td>0.03 (+14.85%)</td><td>0.02 (+14.28%)</td><td>0.01 <b>(+61.89%)</b></td><td>165.80 (-12.51%)</td><td>137.28 (-12.85%)</td><td>140.00 (-12.88%)</td><td>106.70 <b>(-21.20%)</b></td><td>24.24 (+12.36%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.50 (n/a)</td><td>157.52 (n/a)</td><td>160.70 (n/a)</td><td>135.40 (n/a)</td><td>21.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (+2.29%)</td><td>0.03 (-12.97%)</td><td>0.03 <b>(-20.55%)</b></td><td>0.02 <b>(-24.99%)</b></td><td>0.01 <b>(+43.14%)</b></td><td>253.60 <b>(+33.33%)</b></td><td>194.22 (+19.39%)</td><td>197.80 <b>(+25.83%)</b></td><td>118.60 (-2.23%)</td><td>49.90 <b>(+75.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>162.68 (n/a)</td><td>157.20 (n/a)</td><td>121.30 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+3.04%)</td><td>0.03 (+14.32%)</td><td>0.03 <b>(+21.74%)</b></td><td>0.02 (+13.40%)</td><td>0.00 (-1.47%)</td><td>165.60 (-11.82%)</td><td>142.78 (-12.72%)</td><td>136.70 (-17.85%)</td><td>123.30 (-2.91%)</td><td>19.77 (-12.53%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.80 (n/a)</td><td>163.58 (n/a)</td><td>166.40 (n/a)</td><td>127.00 (n/a)</td><td>22.61 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (-3.64%)</td><td>0.03 (-2.61%)</td><td>0.03 (-8.71%)</td><td>0.03 (-0.55%)</td><td>0.01 (-4.77%)</td><td>200.20 (+0.55%)</td><td>166.18 (+2.47%)</td><td>174.00 (+9.57%)</td><td>133.40 (+3.73%)</td><td>29.42 (-3.17%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.10 (n/a)</td><td>162.18 (n/a)</td><td>158.80 (n/a)</td><td>128.60 (n/a)</td><td>30.38 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+4.27%)</td><td>0.02 (-8.66%)</td><td>0.02 (-9.91%)</td><td>0.01 <b>(-21.34%)</b></td><td>0.01 <b>(+31.33%)</b></td><td>344.50 <b>(+27.17%)</b></td><td>214.18 (+18.24%)</td><td>182.90 (+10.98%)</td><td>123.70 (-4.11%)</td><td>94.74 <b>(+62.26%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>270.90 (n/a)</td><td>181.14 (n/a)</td><td>164.80 (n/a)</td><td>129.00 (n/a)</td><td>58.39 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-9.34%)</td><td>0.02 (-12.98%)</td><td>0.02 (-15.39%)</td><td>0.02 (-5.27%)</td><td>0.00 (-19.90%)</td><td>221.60 (+5.57%)</td><td>192.64 (+14.12%)</td><td>207.70 (+18.21%)</td><td>147.10 (+10.27%)</td><td>29.79 (-5.63%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>168.80 (n/a)</td><td>175.70 (n/a)</td><td>133.40 (n/a)</td><td>31.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+12.65%)</td><td>0.03 (+10.56%)</td><td>0.03 (+17.28%)</td><td>0.01 (-19.70%)</td><td>0.01 <b>(+66.73%)</b></td><td>293.00 <b>(+24.52%)</b></td><td>175.02 (-4.05%)</td><td>145.30 (-14.73%)</td><td>132.00 (-11.23%)</td><td>67.88 <b>(+87.59%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.30 (n/a)</td><td>182.40 (n/a)</td><td>170.40 (n/a)</td><td>148.70 (n/a)</td><td>36.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-9.56%)</td><td>0.03 (-16.23%)</td><td>0.03 (-18.80%)</td><td>0.02 (-12.91%)</td><td>0.00 (-19.49%)</td><td>244.20 (+14.81%)</td><td>189.22 (+18.75%)</td><td>184.10 <b>(+23.14%)</b></td><td>146.10 (+10.60%)</td><td>35.18 (+4.75%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>159.34 (n/a)</td><td>149.50 (n/a)</td><td>132.10 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+11.63%)</td><td>0.02 (+1.76%)</td><td>0.02 (-11.39%)</td><td>0.02 (+18.76%)</td><td>0.01 (+12.31%)</td><td>252.50 (-15.78%)</td><td>189.36 (-2.39%)</td><td>194.50 (+12.82%)</td><td>129.80 (-10.42%)</td><td>48.14 <b>(-21.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>299.80 (n/a)</td><td>194.00 (n/a)</td><td>172.40 (n/a)</td><td>144.90 (n/a)</td><td>60.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 <b>(-21.78%)</b></td><td>0.02 (-13.84%)</td><td>0.02 <b>(-21.13%)</b></td><td>0.02 (+5.97%)</td><td>0.00 <b>(-68.68%)</b></td><td>211.70 (-5.66%)</td><td>200.38 (+13.50%)</td><td>205.70 <b>(+26.82%)</b></td><td>182.00 <b>(+27.81%)</b></td><td>12.03 <b>(-62.74%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.40 (n/a)</td><td>176.54 (n/a)</td><td>162.20 (n/a)</td><td>142.40 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 <b>(+42.45%)</b></td><td>0.03 (+10.65%)</td><td>0.02 (+3.30%)</td><td>0.02 (-6.08%)</td><td>0.01 <b>(+212.86%)</b></td><td>218.90 (+6.47%)</td><td>172.70 (-5.22%)</td><td>181.40 (-3.20%)</td><td>112.10 <b>(-29.76%)</b></td><td>41.86 <b>(+131.04%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>182.22 (n/a)</td><td>187.40 (n/a)</td><td>159.60 (n/a)</td><td>18.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+10.12%)</td><td>0.02 (+15.84%)</td><td>0.02 (+15.50%)</td><td>0.02 <b>(+31.16%)</b></td><td>0.00 (-15.51%)</td><td>214.10 <b>(-23.75%)</b></td><td>190.24 (-14.78%)</td><td>191.90 (-13.44%)</td><td>153.60 (-9.17%)</td><td>22.92 <b>(-42.02%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>280.80 (n/a)</td><td>223.24 (n/a)</td><td>221.70 (n/a)</td><td>169.10 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (+3.60%)</td><td>0.02 (+1.90%)</td><td>0.02 (+3.19%)</td><td>0.01 (-7.28%)</td><td>0.00 (+10.56%)</td><td>335.80 (+7.84%)</td><td>226.94 (-0.64%)</td><td>200.70 (-3.09%)</td><td>176.70 (-3.44%)</td><td>64.89 (+18.85%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>311.40 (n/a)</td><td>228.40 (n/a)</td><td>207.10 (n/a)</td><td>183.00 (n/a)</td><td>54.60 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (-2.63%)</td><td>0.05 (+17.09%)</td><td>0.06 <b>(+47.67%)</b></td><td>0.03 (-8.08%)</td><td>0.01 (+1.84%)</td><td>242.10 (+8.81%)</td><td>161.84 (-13.95%)</td><td>142.50 <b>(-32.27%)</b></td><td>129.90 (+2.69%)</td><td>46.64 (+15.15%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>188.08 (n/a)</td><td>210.40 (n/a)</td><td>126.50 (n/a)</td><td>40.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (+13.04%)</td><td>0.07 (-6.17%)</td><td>0.07 (-5.45%)</td><td>0.05 <b>(-26.78%)</b></td><td>0.02 <b>(+268.83%)</b></td><td>244.80 <b>(+36.61%)</b></td><td>186.34 (+10.64%)</td><td>181.30 (+5.78%)</td><td>137.00 (-11.50%)</td><td>41.64 <b>(+348.30%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>179.20 (n/a)</td><td>168.42 (n/a)</td><td>171.40 (n/a)</td><td>154.80 (n/a)</td><td>9.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (-13.11%)</td><td>0.05 (-1.34%)</td><td>0.04 (+4.49%)</td><td>0.04 (+12.97%)</td><td>0.01 <b>(-43.21%)</b></td><td>212.90 (-11.48%)</td><td>180.24 (-1.58%)</td><td>184.00 (-4.32%)</td><td>151.30 (+15.14%)</td><td>24.69 <b>(-41.89%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.50 (n/a)</td><td>183.14 (n/a)</td><td>192.30 (n/a)</td><td>131.40 (n/a)</td><td>42.49 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (-9.44%)</td><td>0.06 (+0.91%)</td><td>0.07 (+10.75%)</td><td>0.05 (+3.08%)</td><td>0.01 <b>(-22.23%)</b></td><td>198.90 (-2.98%)</td><td>165.12 (-2.08%)</td><td>155.20 (-9.71%)</td><td>138.90 (+10.41%)</td><td>28.02 (-17.17%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>168.62 (n/a)</td><td>171.90 (n/a)</td><td>125.80 (n/a)</td><td>33.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (-10.52%)</td><td>0.05 (+8.96%)</td><td>0.05 (+11.43%)</td><td>0.04 (+5.15%)</td><td>0.01 <b>(-30.68%)</b></td><td>212.70 (-4.87%)</td><td>165.84 (-9.93%)</td><td>161.40 (-10.28%)</td><td>141.20 (+11.71%)</td><td>28.56 <b>(-24.72%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>184.12 (n/a)</td><td>179.90 (n/a)</td><td>126.40 (n/a)</td><td>37.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 <b>(+23.72%)</b></td><td>0.07 (+14.06%)</td><td>0.07 (+16.70%)</td><td>0.06 (+17.78%)</td><td>0.01 <b>(+55.98%)</b></td><td>175.80 (-15.07%)</td><td>153.32 (-11.80%)</td><td>143.20 (-14.30%)</td><td>130.30 (-19.17%)</td><td>20.87 (+9.59%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>173.84 (n/a)</td><td>167.10 (n/a)</td><td>161.20 (n/a)</td><td>19.04 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (+2.22%)</td><td>0.05 (-2.42%)</td><td>0.05 (-1.69%)</td><td>0.04 (+1.74%)</td><td>0.01 (+4.52%)</td><td>197.80 (-1.69%)</td><td>167.18 (+2.54%)</td><td>167.90 (+1.70%)</td><td>124.10 (-2.13%)</td><td>27.34 (-1.91%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>163.04 (n/a)</td><td>165.10 (n/a)</td><td>126.80 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 <b>(+28.21%)</b></td><td>0.05 (-17.16%)</td><td>0.04 <b>(-31.28%)</b></td><td>0.03 <b>(-41.34%)</b></td><td>0.02 <b>(+175.32%)</b></td><td>324.80 <b>(+70.50%)</b></td><td>208.14 <b>(+36.20%)</b></td><td>212.10 <b>(+45.47%)</b></td><td>102.60 <b>(-22.04%)</b></td><td>79.54 <b>(+243.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>190.50 (n/a)</td><td>152.82 (n/a)</td><td>145.80 (n/a)</td><td>131.60 (n/a)</td><td>23.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (+8.52%)</td><td>0.05 (+4.40%)</td><td>0.04 (-9.45%)</td><td>0.04 <b>(+26.75%)</b></td><td>0.01 <b>(-24.13%)</b></td><td>194.90 <b>(-21.09%)</b></td><td>171.92 (-7.12%)</td><td>186.00 (+10.39%)</td><td>130.20 (-7.86%)</td><td>27.87 <b>(-43.39%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.00 (n/a)</td><td>185.10 (n/a)</td><td>168.50 (n/a)</td><td>141.30 (n/a)</td><td>49.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 <b>(-20.43%)</b></td><td>0.05 (-8.76%)</td><td>0.04 (-7.45%)</td><td>0.04 (+6.22%)</td><td>0.01 <b>(-52.79%)</b></td><td>226.30 (-5.87%)</td><td>201.48 (+6.55%)</td><td>208.80 (+8.07%)</td><td>172.30 <b>(+25.67%)</b></td><td>22.64 <b>(-43.96%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>189.10 (n/a)</td><td>193.20 (n/a)</td><td>137.10 (n/a)</td><td>40.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 <b>(-26.98%)</b></td><td>0.04 (-14.19%)</td><td>0.04 (-5.22%)</td><td>0.03 <b>(-32.73%)</b></td><td>0.01 <b>(-22.62%)</b></td><td>311.30 <b>(+48.66%)</b></td><td>207.08 (+18.06%)</td><td>197.50 (+5.50%)</td><td>152.80 <b>(+36.92%)</b></td><td>63.12 <b>(+66.25%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>175.40 (n/a)</td><td>187.20 (n/a)</td><td>111.60 (n/a)</td><td>37.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 <b>(-31.10%)</b></td><td>0.04 (-6.80%)</td><td>0.04 (+2.38%)</td><td>0.04 (+16.39%)</td><td>0.00 <b>(-89.01%)</b></td><td>220.50 (-14.07%)</td><td>214.64 (+3.23%)</td><td>216.80 (-2.34%)</td><td>208.20 <b>(+45.09%)</b></td><td>5.99 <b>(-85.90%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.60 (n/a)</td><td>207.92 (n/a)</td><td>222.00 (n/a)</td><td>143.50 (n/a)</td><td>42.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 <b>(-23.24%)</b></td><td>0.05 (-0.87%)</td><td>0.05 (+17.17%)</td><td>0.04 (+13.29%)</td><td>0.00 <b>(-67.52%)</b></td><td>199.50 (-11.73%)</td><td>177.14 (-4.09%)</td><td>176.40 (-14.66%)</td><td>153.60 <b>(+30.28%)</b></td><td>16.66 <b>(-62.68%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.00 (n/a)</td><td>184.70 (n/a)</td><td>206.70 (n/a)</td><td>117.90 (n/a)</td><td>44.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 <b>(-23.17%)</b></td><td>0.04 <b>(-22.92%)</b></td><td>0.04 (-12.35%)</td><td>0.03 <b>(-33.27%)</b></td><td>0.01 (+2.16%)</td><td>330.80 <b>(+49.82%)</b></td><td>245.36 <b>(+32.07%)</b></td><td>213.90 (+14.08%)</td><td>203.70 <b>(+30.16%)</b></td><td>54.91 <b>(+99.64%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.80 (n/a)</td><td>185.78 (n/a)</td><td>187.50 (n/a)</td><td>156.50 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 <b>(+36.01%)</b></td><td>0.04 (+3.10%)</td><td>0.04 (-5.40%)</td><td>0.02 <b>(-29.49%)</b></td><td>0.01 <b>(+526.19%)</b></td><td>332.40 <b>(+41.87%)</b></td><td>227.80 (+3.23%)</td><td>228.40 (+5.69%)</td><td>154.80 <b>(-26.46%)</b></td><td>66.59 <b>(+559.90%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>234.30 (n/a)</td><td>220.68 (n/a)</td><td>216.10 (n/a)</td><td>210.50 (n/a)</td><td>10.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 <b>(+46.17%)</b></td><td>0.10 (+14.16%)</td><td>0.09 (+16.27%)</td><td>0.05 <b>(-34.71%)</b></td><td>0.04 <b>(+235.03%)</b></td><td>330.80 <b>(+53.22%)</b></td><td>189.76 (-1.65%)</td><td>172.90 (-14.02%)</td><td>109.70 <b>(-31.61%)</b></td><td>83.59 <b>(+271.41%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.90 (n/a)</td><td>192.94 (n/a)</td><td>201.10 (n/a)</td><td>160.40 (n/a)</td><td>22.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.17 (-14.57%)</td><td>0.14 (-10.05%)</td><td>0.14 (-3.96%)</td><td>0.12 (-6.98%)</td><td>0.02 <b>(-30.14%)</b></td><td>211.80 (+7.51%)</td><td>178.68 (+10.12%)</td><td>177.10 (+4.12%)</td><td>146.80 (+17.07%)</td><td>25.08 (-11.06%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.00 (n/a)</td><td>162.26 (n/a)</td><td>170.10 (n/a)</td><td>125.40 (n/a)</td><td>28.20 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 <b>(+20.60%)</b></td><td>0.11 (-1.52%)</td><td>0.10 (-9.88%)</td><td>0.09 (-11.03%)</td><td>0.03 <b>(+103.27%)</b></td><td>190.70 (+12.37%)</td><td>155.68 (+5.49%)</td><td>161.00 (+10.96%)</td><td>103.50 (-17.07%)</td><td>36.85 <b>(+90.49%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.70 (n/a)</td><td>147.58 (n/a)</td><td>145.10 (n/a)</td><td>124.80 (n/a)</td><td>19.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (-5.75%)</td><td>0.12 (-17.72%)</td><td>0.11 <b>(-24.31%)</b></td><td>0.09 (-16.23%)</td><td>0.02 (+8.93%)</td><td>221.40 (+19.35%)</td><td>182.52 <b>(+22.81%)</b></td><td>189.60 <b>(+32.13%)</b></td><td>134.80 (+6.14%)</td><td>34.39 <b>(+39.44%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>185.50 (n/a)</td><td>148.62 (n/a)</td><td>143.50 (n/a)</td><td>127.00 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (-0.92%)</td><td>0.11 (+8.46%)</td><td>0.12 (+11.59%)</td><td>0.08 (+18.35%)</td><td>0.03 (-12.94%)</td><td>212.00 (-15.50%)</td><td>157.66 (-10.06%)</td><td>142.20 (-10.40%)</td><td>119.30 (+0.93%)</td><td>39.68 <b>(-26.31%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>250.90 (n/a)</td><td>175.30 (n/a)</td><td>158.70 (n/a)</td><td>118.20 (n/a)</td><td>53.85 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (-1.60%)</td><td>0.11 (-11.00%)</td><td>0.12 (-9.31%)</td><td>0.08 (-7.09%)</td><td>0.03 (+16.26%)</td><td>245.70 (+7.62%)</td><td>191.36 (+14.48%)</td><td>168.50 (+10.27%)</td><td>138.10 (+1.62%)</td><td>49.88 <b>(+33.24%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>228.30 (n/a)</td><td>167.16 (n/a)</td><td>152.80 (n/a)</td><td>135.90 (n/a)</td><td>37.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (-17.50%)</td><td>0.09 (-4.86%)</td><td>0.09 (-7.59%)</td><td>0.07 (+0.58%)</td><td>0.02 <b>(-34.25%)</b></td><td>234.80 (-0.55%)</td><td>184.78 (+2.48%)</td><td>175.10 (+8.15%)</td><td>153.90 <b>(+21.18%)</b></td><td>34.46 <b>(-24.17%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.10 (n/a)</td><td>180.30 (n/a)</td><td>161.90 (n/a)</td><td>127.00 (n/a)</td><td>45.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (-18.74%)</td><td>0.10 (-17.92%)</td><td>0.10 (-8.60%)</td><td>0.07 <b>(-28.27%)</b></td><td>0.02 (+9.08%)</td><td>270.10 <b>(+39.44%)</b></td><td>201.70 <b>(+24.58%)</b></td><td>181.90 (+9.38%)</td><td>156.10 <b>(+23.01%)</b></td><td>48.82 <b>(+88.94%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>193.70 (n/a)</td><td>161.90 (n/a)</td><td>166.30 (n/a)</td><td>126.90 (n/a)</td><td>25.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (+4.50%)</td><td>0.11 (+1.57%)</td><td>0.09 (-12.59%)</td><td>0.08 (+16.63%)</td><td>0.03 (-4.83%)</td><td>214.60 (-14.26%)</td><td>160.86 (-3.77%)</td><td>174.60 (+14.42%)</td><td>104.20 (-4.32%)</td><td>42.90 <b>(-24.01%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>250.30 (n/a)</td><td>167.16 (n/a)</td><td>152.60 (n/a)</td><td>108.90 (n/a)</td><td>56.46 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (+15.57%)</td><td>0.10 (-0.75%)</td><td>0.08 (-9.75%)</td><td>0.07 <b>(-23.79%)</b></td><td>0.03 <b>(+128.77%)</b></td><td>269.40 <b>(+31.22%)</b></td><td>199.12 (+7.18%)</td><td>220.50 (+10.80%)</td><td>135.00 (-13.46%)</td><td>58.67 <b>(+144.45%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>185.78 (n/a)</td><td>199.00 (n/a)</td><td>156.00 (n/a)</td><td>24.00 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 <b>(-25.11%)</b></td><td>0.09 (-16.28%)</td><td>0.09 (-0.38%)</td><td>0.07 (-13.54%)</td><td>0.02 <b>(-32.00%)</b></td><td>231.60 (+15.63%)</td><td>185.14 (+17.55%)</td><td>178.80 (+0.39%)</td><td>141.90 <b>(+33.49%)</b></td><td>43.11 (+6.70%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>200.30 (n/a)</td><td>157.50 (n/a)</td><td>178.10 (n/a)</td><td>106.30 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (+9.43%)</td><td>0.09 (-3.69%)</td><td>0.09 (+7.65%)</td><td>0.05 <b>(-32.92%)</b></td><td>0.02 <b>(+167.19%)</b></td><td>320.20 <b>(+49.07%)</b></td><td>217.86 (+10.85%)</td><td>189.00 (-7.13%)</td><td>155.00 (-8.61%)</td><td>69.24 <b>(+263.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>196.54 (n/a)</td><td>203.50 (n/a)</td><td>169.60 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 <b>(+24.55%)</b></td><td>0.09 (+16.35%)</td><td>0.09 (+9.76%)</td><td>0.06 (+4.26%)</td><td>0.02 <b>(+80.67%)</b></td><td>273.30 (-4.07%)</td><td>191.94 (-11.31%)</td><td>182.50 (-8.93%)</td><td>145.80 (-19.71%)</td><td>52.94 <b>(+31.03%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>284.90 (n/a)</td><td>216.42 (n/a)</td><td>200.40 (n/a)</td><td>181.60 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (+17.04%)</td><td>0.08 (-13.27%)</td><td>0.06 <b>(-42.06%)</b></td><td>0.05 (+1.03%)</td><td>0.04 <b>(+47.33%)</b></td><td>328.30 (-1.03%)</td><td>251.96 <b>(+24.38%)</b></td><td>306.70 <b>(+72.59%)</b></td><td>113.80 (-14.56%)</td><td>97.09 <b>(+25.33%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>331.70 (n/a)</td><td>202.58 (n/a)</td><td>177.70 (n/a)</td><td>133.20 (n/a)</td><td>77.47 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (-8.44%)</td><td>0.08 (+1.09%)</td><td>0.08 (+8.52%)</td><td>0.05 (+9.22%)</td><td>0.02 <b>(-21.77%)</b></td><td>302.80 (-8.44%)</td><td>222.72 (-3.30%)</td><td>213.70 (-7.89%)</td><td>165.50 (+9.24%)</td><td>51.59 <b>(-20.74%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>330.70 (n/a)</td><td>230.32 (n/a)</td><td>232.00 (n/a)</td><td>151.50 (n/a)</td><td>65.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (-17.37%)</td><td>0.19 (-8.15%)</td><td>0.19 (-3.28%)</td><td>0.16 (-4.64%)</td><td>0.02 <b>(-40.03%)</b></td><td>199.10 (+4.84%)</td><td>177.18 (+7.51%)</td><td>173.00 (+3.41%)</td><td>150.60 <b>(+21.06%)</b></td><td>20.61 <b>(-22.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>189.90 (n/a)</td><td>164.80 (n/a)</td><td>167.30 (n/a)</td><td>124.40 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 <b>(-22.03%)</b></td><td>0.21 (-9.17%)</td><td>0.23 (+3.80%)</td><td>0.14 (-18.00%)</td><td>0.05 <b>(-21.57%)</b></td><td>233.20 <b>(+21.97%)</b></td><td>163.82 (+9.96%)</td><td>144.60 (-3.66%)</td><td>123.20 <b>(+28.20%)</b></td><td>46.06 <b>(+23.41%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>191.20 (n/a)</td><td>148.98 (n/a)</td><td>150.10 (n/a)</td><td>96.10 (n/a)</td><td>37.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (-8.54%)</td><td>0.25 (+16.89%)</td><td>0.25 (+14.42%)</td><td>0.22 <b>(+75.07%)</b></td><td>0.02 <b>(-62.94%)</b></td><td>187.30 <b>(-42.90%)</b></td><td>167.78 <b>(-20.48%)</b></td><td>166.30 (-12.61%)</td><td>151.30 (+9.40%)</td><td>15.89 <b>(-77.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>328.00 (n/a)</td><td>210.98 (n/a)</td><td>190.30 (n/a)</td><td>138.30 (n/a)</td><td>71.53 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (-6.95%)</td><td>0.21 (+5.21%)</td><td>0.21 <b>(+21.63%)</b></td><td>0.15 (+2.07%)</td><td>0.03 <b>(-35.69%)</b></td><td>212.70 (-2.03%)</td><td>161.70 (-7.85%)</td><td>159.40 (-17.75%)</td><td>133.00 (+7.52%)</td><td>30.76 <b>(-30.45%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>217.10 (n/a)</td><td>175.48 (n/a)</td><td>193.80 (n/a)</td><td>123.70 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.37 <b>(+26.90%)</b></td><td>0.24 (-0.04%)</td><td>0.24 (+6.91%)</td><td>0.14 <b>(-25.32%)</b></td><td>0.09 <b>(+145.92%)</b></td><td>293.30 <b>(+33.93%)</b></td><td>196.48 (+10.88%)</td><td>168.50 (-6.49%)</td><td>112.20 <b>(-21.21%)</b></td><td>76.07 <b>(+169.20%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>219.00 (n/a)</td><td>177.20 (n/a)</td><td>180.20 (n/a)</td><td>142.40 (n/a)</td><td>28.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (-9.01%)</td><td>0.19 (-7.42%)</td><td>0.19 (+9.41%)</td><td>0.15 (+2.89%)</td><td>0.05 <b>(-29.92%)</b></td><td>212.10 (-2.80%)</td><td>177.64 (+3.68%)</td><td>176.70 (-8.59%)</td><td>118.20 (+9.95%)</td><td>37.21 <b>(-27.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>218.20 (n/a)</td><td>171.34 (n/a)</td><td>193.30 (n/a)</td><td>107.50 (n/a)</td><td>51.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 <b>(-21.58%)</b></td><td>0.20 (-14.38%)</td><td>0.20 (-12.89%)</td><td>0.17 (-11.50%)</td><td>0.02 <b>(-46.32%)</b></td><td>217.50 (+12.99%)</td><td>186.22 (+15.61%)</td><td>180.40 (+14.83%)</td><td>167.50 <b>(+27.47%)</b></td><td>18.80 <b>(-21.43%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>192.50 (n/a)</td><td>161.08 (n/a)</td><td>157.10 (n/a)</td><td>131.40 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (-6.33%)</td><td>0.19 (-0.29%)</td><td>0.18 (+0.35%)</td><td>0.12 <b>(-20.39%)</b></td><td>0.05 (+14.13%)</td><td>272.90 <b>(+25.64%)</b></td><td>186.52 (+2.89%)</td><td>180.60 (-0.39%)</td><td>135.20 (+6.71%)</td><td>55.59 <b>(+48.51%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.20 (n/a)</td><td>181.28 (n/a)</td><td>181.30 (n/a)</td><td>126.70 (n/a)</td><td>37.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (-8.06%)</td><td>0.20 (-13.01%)</td><td>0.20 (-9.02%)</td><td>0.15 <b>(-29.38%)</b></td><td>0.03 <b>(+187.42%)</b></td><td>240.80 <b>(+41.56%)</b></td><td>189.62 (+16.76%)</td><td>181.50 (+9.93%)</td><td>168.80 (+8.76%)</td><td>29.67 <b>(+350.44%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.01 (n/a)</td><td>170.10 (n/a)</td><td>162.40 (n/a)</td><td>165.10 (n/a)</td><td>155.20 (n/a)</td><td>6.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (+13.15%)</td><td>0.18 (-6.20%)</td><td>0.17 (-14.05%)</td><td>0.11 <b>(-22.76%)</b></td><td>0.07 <b>(+54.72%)</b></td><td>288.30 <b>(+29.46%)</b></td><td>202.86 (+12.98%)</td><td>197.90 (+16.34%)</td><td>117.30 (-11.61%)</td><td>66.67 <b>(+69.87%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>222.70 (n/a)</td><td>179.56 (n/a)</td><td>170.10 (n/a)</td><td>132.70 (n/a)</td><td>39.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (+1.76%)</td><td>0.17 (-12.87%)</td><td>0.16 (-18.09%)</td><td>0.15 <b>(-20.31%)</b></td><td>0.03 <b>(+117.18%)</b></td><td>240.10 <b>(+25.51%)</b></td><td>207.08 (+16.86%)</td><td>214.20 <b>(+22.05%)</b></td><td>159.50 (-1.73%)</td><td>32.72 <b>(+165.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>177.20 (n/a)</td><td>175.50 (n/a)</td><td>162.30 (n/a)</td><td>12.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 <b>(+20.39%)</b></td><td>0.16 (-6.43%)</td><td>0.16 (-16.22%)</td><td>0.13 (-3.71%)</td><td>0.05 <b>(+70.20%)</b></td><td>251.40 (+3.84%)</td><td>211.06 (+10.08%)</td><td>211.30 (+19.38%)</td><td>135.00 (-16.92%)</td><td>46.95 <b>(+43.77%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>242.10 (n/a)</td><td>191.74 (n/a)</td><td>177.00 (n/a)</td><td>162.50 (n/a)</td><td>32.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.23 (+10.35%)</td><td>0.18 (+3.63%)</td><td>0.18 (+6.23%)</td><td>0.11 (-18.10%)</td><td>0.04 <b>(+59.03%)</b></td><td>308.20 <b>(+22.11%)</b></td><td>205.32 (+0.18%)</td><td>189.30 (-5.91%)</td><td>149.60 (-9.39%)</td><td>60.82 <b>(+84.02%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>252.40 (n/a)</td><td>204.96 (n/a)</td><td>201.20 (n/a)</td><td>165.10 (n/a)</td><td>33.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 <b>(+46.57%)</b></td><td>0.18 <b>(+41.13%)</b></td><td>0.15 <b>(+41.19%)</b></td><td>0.14 <b>(+42.80%)</b></td><td>0.05 <b>(+45.26%)</b></td><td>234.30 <b>(-29.98%)</b></td><td>193.76 <b>(-29.20%)</b></td><td>215.80 <b>(-29.15%)</b></td><td>123.00 <b>(-31.74%)</b></td><td>46.28 <b>(-31.97%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>334.60 (n/a)</td><td>273.66 (n/a)</td><td>304.60 (n/a)</td><td>180.20 (n/a)</td><td>68.04 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (-14.11%)</td><td>0.13 (-7.44%)</td><td>0.13 (-4.54%)</td><td>0.10 (-4.79%)</td><td>0.02 <b>(-33.45%)</b></td><td>198.90 (+5.02%)</td><td>163.42 (+6.45%)</td><td>161.70 (+4.73%)</td><td>130.70 (+16.38%)</td><td>24.30 (-18.22%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>189.40 (n/a)</td><td>153.52 (n/a)</td><td>154.40 (n/a)</td><td>112.30 (n/a)</td><td>29.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (+16.70%)</td><td>0.13 (+3.71%)</td><td>0.13 (+2.10%)</td><td>0.10 (-12.05%)</td><td>0.02 <b>(+127.02%)</b></td><td>208.10 (+13.72%)</td><td>164.96 (-1.52%)</td><td>163.30 (-2.10%)</td><td>126.90 (-14.31%)</td><td>30.04 <b>(+121.25%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>183.00 (n/a)</td><td>167.50 (n/a)</td><td>166.80 (n/a)</td><td>148.10 (n/a)</td><td>13.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (+10.69%)</td><td>0.14 <b>(+23.59%)</b></td><td>0.15 <b>(+53.16%)</b></td><td>0.10 (+9.53%)</td><td>0.03 (+18.04%)</td><td>202.20 (-8.71%)</td><td>152.20 (-18.46%)</td><td>132.40 <b>(-34.71%)</b></td><td>114.80 (-9.61%)</td><td>38.00 (+1.40%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>221.50 (n/a)</td><td>186.66 (n/a)</td><td>202.80 (n/a)</td><td>127.00 (n/a)</td><td>37.47 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (+12.69%)</td><td>0.13 (+5.58%)</td><td>0.12 (-7.04%)</td><td>0.10 (+0.31%)</td><td>0.03 <b>(+62.09%)</b></td><td>200.50 (-0.30%)</td><td>159.40 (-3.60%)</td><td>167.20 (+7.52%)</td><td>126.50 (-11.29%)</td><td>31.95 <b>(+36.40%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>201.10 (n/a)</td><td>165.36 (n/a)</td><td>155.50 (n/a)</td><td>142.60 (n/a)</td><td>23.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (+8.89%)</td><td>0.14 (+1.75%)</td><td>0.14 (-1.28%)</td><td>0.08 (-4.29%)</td><td>0.04 <b>(+32.11%)</b></td><td>241.00 (+4.51%)</td><td>160.54 (+0.96%)</td><td>150.70 (+1.28%)</td><td>116.50 (-8.20%)</td><td>51.56 <b>(+21.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>230.60 (n/a)</td><td>159.02 (n/a)</td><td>148.80 (n/a)</td><td>126.90 (n/a)</td><td>42.37 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (-19.84%)</td><td>0.12 (-19.65%)</td><td>0.12 <b>(-21.39%)</b></td><td>0.10 (-2.81%)</td><td>0.02 <b>(-42.37%)</b></td><td>205.20 (+2.91%)</td><td>171.28 <b>(+21.79%)</b></td><td>166.80 <b>(+27.23%)</b></td><td>141.90 <b>(+24.69%)</b></td><td>23.73 <b>(-29.46%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>199.40 (n/a)</td><td>140.64 (n/a)</td><td>131.10 (n/a)</td><td>113.80 (n/a)</td><td>33.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 <b>(+28.44%)</b></td><td>0.13 <b>(+23.27%)</b></td><td>0.13 (+16.15%)</td><td>0.10 <b>(+41.85%)</b></td><td>0.03 (+17.93%)</td><td>199.10 <b>(-29.52%)</b></td><td>159.12 (-19.83%)</td><td>161.80 (-13.94%)</td><td>117.00 <b>(-22.10%)</b></td><td>29.98 <b>(-39.54%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>282.50 (n/a)</td><td>198.48 (n/a)</td><td>188.00 (n/a)</td><td>150.20 (n/a)</td><td>49.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (+9.28%)</td><td>0.11 (+0.32%)</td><td>0.11 (+2.73%)</td><td>0.07 <b>(-25.01%)</b></td><td>0.03 <b>(+86.83%)</b></td><td>296.50 <b>(+33.38%)</b></td><td>196.62 (+4.67%)</td><td>184.30 (-2.64%)</td><td>140.70 (-8.46%)</td><td>60.36 <b>(+136.29%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>187.84 (n/a)</td><td>189.30 (n/a)</td><td>153.70 (n/a)</td><td>25.54 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (-10.94%)</td><td>0.15 (-14.98%)</td><td>0.13 <b>(-23.08%)</b></td><td>0.12 (-16.23%)</td><td>0.03 <b>(+35.12%)</b></td><td>207.70 (+19.37%)</td><td>174.12 (+19.77%)</td><td>191.10 <b>(+30.00%)</b></td><td>137.90 (+12.30%)</td><td>33.31 <b>(+74.33%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>174.00 (n/a)</td><td>145.38 (n/a)</td><td>147.00 (n/a)</td><td>122.80 (n/a)</td><td>19.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (+3.17%)</td><td>0.15 (-5.02%)</td><td>0.15 (-8.58%)</td><td>0.12 (-14.48%)</td><td>0.03 <b>(+94.00%)</b></td><td>201.50 (+16.88%)</td><td>167.12 (+8.22%)</td><td>169.10 (+9.38%)</td><td>130.40 (-3.05%)</td><td>34.86 <b>(+118.87%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>172.40 (n/a)</td><td>154.42 (n/a)</td><td>154.60 (n/a)</td><td>134.50 (n/a)</td><td>15.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (+8.52%)</td><td>0.14 (-8.05%)</td><td>0.14 (-15.60%)</td><td>0.11 (+2.56%)</td><td>0.03 (+17.42%)</td><td>215.50 (-2.49%)</td><td>181.52 (+9.55%)</td><td>178.70 (+18.50%)</td><td>126.00 (-7.83%)</td><td>36.65 (+5.83%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>221.00 (n/a)</td><td>165.70 (n/a)</td><td>150.80 (n/a)</td><td>136.70 (n/a)</td><td>34.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (+14.08%)</td><td>0.15 (+4.81%)</td><td>0.15 (+3.00%)</td><td>0.12 (-3.31%)</td><td>0.03 <b>(+80.11%)</b></td><td>197.70 (+3.40%)</td><td>165.12 (-2.79%)</td><td>164.70 (-2.95%)</td><td>126.50 (-12.34%)</td><td>30.31 <b>(+66.04%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>191.20 (n/a)</td><td>169.86 (n/a)</td><td>169.70 (n/a)</td><td>144.30 (n/a)</td><td>18.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (+16.17%)</td><td>0.15 (-1.84%)</td><td>0.16 (+3.39%)</td><td>0.10 <b>(-22.86%)</b></td><td>0.04 <b>(+171.07%)</b></td><td>241.50 <b>(+29.63%)</b></td><td>172.30 (+7.37%)</td><td>152.60 (-3.30%)</td><td>125.70 (-13.90%)</td><td>48.86 <b>(+203.32%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>186.30 (n/a)</td><td>160.48 (n/a)</td><td>157.80 (n/a)</td><td>146.00 (n/a)</td><td>16.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (+5.94%)</td><td>0.14 (+8.54%)</td><td>0.14 <b>(+24.62%)</b></td><td>0.10 (+2.60%)</td><td>0.04 (+4.98%)</td><td>240.60 (-2.55%)</td><td>184.42 (-7.77%)</td><td>172.00 (-19.74%)</td><td>121.40 (-5.60%)</td><td>46.15 (-2.18%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>246.90 (n/a)</td><td>199.96 (n/a)</td><td>214.30 (n/a)</td><td>128.60 (n/a)</td><td>47.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 <b>(+23.57%)</b></td><td>0.17 <b>(+29.91%)</b></td><td>0.15 <b>(+29.77%)</b></td><td>0.15 <b>(+53.03%)</b></td><td>0.02 (-16.59%)</td><td>164.60 <b>(-34.66%)</b></td><td>150.50 <b>(-24.88%)</b></td><td>161.60 <b>(-22.94%)</b></td><td>119.80 (-19.11%)</td><td>19.41 <b>(-54.91%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>251.90 (n/a)</td><td>200.34 (n/a)</td><td>209.70 (n/a)</td><td>148.10 (n/a)</td><td>43.04 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 <b>(+24.17%)</b></td><td>0.15 (+18.12%)</td><td>0.15 (+15.79%)</td><td>0.14 <b>(+30.64%)</b></td><td>0.02 (+2.26%)</td><td>177.20 <b>(-23.46%)</b></td><td>163.70 (-15.82%)</td><td>169.50 (-13.61%)</td><td>133.50 (-19.43%)</td><td>17.92 <b>(-36.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>194.46 (n/a)</td><td>196.20 (n/a)</td><td>165.70 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (-4.10%)</td><td>0.13 (+12.48%)</td><td>0.13 <b>(+24.01%)</b></td><td>0.11 (+9.32%)</td><td>0.01 <b>(-25.16%)</b></td><td>171.50 (-8.53%)</td><td>145.28 (-11.87%)</td><td>138.60 (-19.37%)</td><td>130.40 (+4.32%)</td><td>17.38 <b>(-26.74%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>187.50 (n/a)</td><td>164.84 (n/a)</td><td>171.90 (n/a)</td><td>125.00 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (-4.25%)</td><td>0.13 (-2.85%)</td><td>0.14 (+16.35%)</td><td>0.07 <b>(-31.90%)</b></td><td>0.03 <b>(+40.70%)</b></td><td>246.70 <b>(+46.85%)</b></td><td>155.24 (+7.72%)</td><td>130.10 (-14.01%)</td><td>121.00 (+4.40%)</td><td>52.17 <b>(+124.94%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>168.00 (n/a)</td><td>144.12 (n/a)</td><td>151.30 (n/a)</td><td>115.90 (n/a)</td><td>23.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 <b>(+42.02%)</b></td><td>0.12 (+5.41%)</td><td>0.10 (-15.53%)</td><td>0.07 (-17.56%)</td><td>0.04 <b>(+187.58%)</b></td><td>260.40 <b>(+21.34%)</b></td><td>177.68 (+3.59%)</td><td>192.70 (+18.37%)</td><td>104.70 <b>(-29.59%)</b></td><td>61.49 <b>(+136.08%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>171.52 (n/a)</td><td>162.80 (n/a)</td><td>148.70 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (+3.52%)</td><td>0.10 (-5.25%)</td><td>0.11 (+11.37%)</td><td>0.05 <b>(-24.99%)</b></td><td>0.03 <b>(+21.91%)</b></td><td>350.70 <b>(+33.30%)</b></td><td>204.68 (+11.71%)</td><td>160.60 (-10.18%)</td><td>133.20 (-3.41%)</td><td>87.49 <b>(+69.15%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>263.10 (n/a)</td><td>183.22 (n/a)</td><td>178.80 (n/a)</td><td>137.90 (n/a)</td><td>51.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (+9.43%)</td><td>0.11 (+13.09%)</td><td>0.11 (+18.16%)</td><td>0.10 (+17.17%)</td><td>0.01 (-9.76%)</td><td>182.60 (-14.63%)</td><td>168.30 (-12.21%)</td><td>175.10 (-15.33%)</td><td>134.50 (-8.57%)</td><td>19.25 <b>(-31.20%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>213.90 (n/a)</td><td>191.70 (n/a)</td><td>206.80 (n/a)</td><td>147.10 (n/a)</td><td>27.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 <b>(+24.61%)</b></td><td>0.10 (+4.46%)</td><td>0.09 (-3.75%)</td><td>0.08 (-1.93%)</td><td>0.02 <b>(+93.71%)</b></td><td>237.40 (+1.98%)</td><td>194.72 (-2.24%)</td><td>199.50 (+3.85%)</td><td>137.50 (-19.73%)</td><td>36.04 <b>(+50.34%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>199.18 (n/a)</td><td>192.10 (n/a)</td><td>171.30 (n/a)</td><td>23.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 <b>(-24.40%)</b></td><td>0.11 (+10.62%)</td><td>0.12 <b>(+37.73%)</b></td><td>0.09 <b>(+27.98%)</b></td><td>0.02 <b>(-55.72%)</b></td><td>203.10 <b>(-21.85%)</b></td><td>165.78 (-17.58%)</td><td>160.10 <b>(-27.39%)</b></td><td>133.20 <b>(+32.27%)</b></td><td>30.34 <b>(-52.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>259.90 (n/a)</td><td>201.14 (n/a)</td><td>220.50 (n/a)</td><td>100.70 (n/a)</td><td>64.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (+9.72%)</td><td>0.11 <b>(+21.19%)</b></td><td>0.11 (+12.69%)</td><td>0.09 <b>(+45.82%)</b></td><td>0.01 <b>(-53.52%)</b></td><td>198.10 <b>(-31.43%)</b></td><td>173.12 (-19.83%)</td><td>167.20 (-11.25%)</td><td>165.40 (-8.82%)</td><td>14.01 <b>(-70.18%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>288.90 (n/a)</td><td>215.94 (n/a)</td><td>188.40 (n/a)</td><td>181.40 (n/a)</td><td>46.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.73 (-4.51%)</td><td>0.57 (+0.72%)</td><td>0.58 (+4.81%)</td><td>0.39 (-16.08%)</td><td>0.16 <b>(+35.02%)</b></td><td>255.30 (+19.13%)</td><td>185.56 (+3.18%)</td><td>170.90 (-4.58%)</td><td>134.80 (+4.74%)</td><td>55.61 <b>(+66.34%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.76 (n/a)</td><td>0.56 (n/a)</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.12 (n/a)</td><td>214.30 (n/a)</td><td>179.84 (n/a)</td><td>179.10 (n/a)</td><td>128.70 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.93 (+17.58%)</td><td>0.64 (+6.55%)</td><td>0.58 (-4.18%)</td><td>0.45 (-3.99%)</td><td>0.20 <b>(+60.65%)</b></td><td>219.20 (+4.13%)</td><td>163.64 (-2.48%)</td><td>170.40 (+4.41%)</td><td>105.20 (-14.96%)</td><td>45.70 <b>(+42.50%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.79 (n/a)</td><td>0.60 (n/a)</td><td>0.60 (n/a)</td><td>0.47 (n/a)</td><td>0.12 (n/a)</td><td>210.50 (n/a)</td><td>167.80 (n/a)</td><td>163.20 (n/a)</td><td>123.70 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.81 (+2.75%)</td><td>0.53 (-6.91%)</td><td>0.47 (-14.08%)</td><td>0.31 (+15.16%)</td><td>0.20 (-2.48%)</td><td>318.00 (-13.16%)</td><td>205.78 (+4.08%)</td><td>208.30 (+16.37%)</td><td>120.90 (-2.66%)</td><td>76.66 <b>(-21.61%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.79 (n/a)</td><td>0.57 (n/a)</td><td>0.55 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>366.20 (n/a)</td><td>197.72 (n/a)</td><td>179.00 (n/a)</td><td>124.20 (n/a)</td><td>97.80 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.75 (+1.97%)</td><td>0.56 (-1.82%)</td><td>0.59 (+6.37%)</td><td>0.29 <b>(-32.36%)</b></td><td>0.17 <b>(+31.06%)</b></td><td>334.20 <b>(+47.88%)</b></td><td>194.38 (+8.18%)</td><td>167.50 (-6.00%)</td><td>130.50 (-1.95%)</td><td>79.97 <b>(+105.57%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.74 (n/a)</td><td>0.57 (n/a)</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.13 (n/a)</td><td>226.00 (n/a)</td><td>179.68 (n/a)</td><td>178.20 (n/a)</td><td>133.10 (n/a)</td><td>38.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.58 (-19.18%)</td><td>0.44 (-2.11%)</td><td>0.45 (+2.57%)</td><td>0.32 (-4.99%)</td><td>0.09 <b>(-39.26%)</b></td><td>233.60 (+5.27%)</td><td>172.78 (-1.57%)</td><td>164.80 (-2.54%)</td><td>128.00 <b>(+23.79%)</b></td><td>38.58 (-19.03%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.71 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.15 (n/a)</td><td>221.90 (n/a)</td><td>175.54 (n/a)</td><td>169.10 (n/a)</td><td>103.40 (n/a)</td><td>47.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.70 <b>(+38.47%)</b></td><td>0.48 (+14.37%)</td><td>0.48 <b>(+22.71%)</b></td><td>0.29 (-16.15%)</td><td>0.16 <b>(+140.73%)</b></td><td>254.00 (+19.25%)</td><td>168.04 (-5.95%)</td><td>154.00 (-18.52%)</td><td>105.20 <b>(-27.80%)</b></td><td>58.17 <b>(+112.37%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>213.00 (n/a)</td><td>178.68 (n/a)</td><td>189.00 (n/a)</td><td>145.70 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.48 (-15.18%)</td><td>0.37 (-10.69%)</td><td>0.35 (-13.08%)</td><td>0.31 (+0.65%)</td><td>0.07 <b>(-41.62%)</b></td><td>237.60 (-0.63%)</td><td>201.50 (+8.18%)</td><td>208.00 (+15.04%)</td><td>152.60 (+17.93%)</td><td>30.92 <b>(-35.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.31 (n/a)</td><td>0.11 (n/a)</td><td>239.10 (n/a)</td><td>186.26 (n/a)</td><td>180.80 (n/a)</td><td>129.40 (n/a)</td><td>48.14 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.62 <b>(+47.60%)</b></td><td>0.53 <b>(+37.93%)</b></td><td>0.54 <b>(+36.71%)</b></td><td>0.43 <b>(+49.45%)</b></td><td>0.07 <b>(+32.89%)</b></td><td>169.50 <b>(-33.08%)</b></td><td>141.90 <b>(-27.79%)</b></td><td>136.00 <b>(-26.88%)</b></td><td>118.90 <b>(-32.25%)</b></td><td>19.42 <b>(-40.17%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>253.30 (n/a)</td><td>196.50 (n/a)</td><td>186.00 (n/a)</td><td>175.50 (n/a)</td><td>32.46 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.31 (+19.54%)</td><td>0.25 (+18.35%)</td><td>0.27 (+18.98%)</td><td>0.19 (+5.27%)</td><td>0.05 <b>(+54.37%)</b></td><td>190.80 (-5.03%)</td><td>149.80 (-14.34%)</td><td>138.80 (-15.93%)</td><td>120.40 (-16.33%)</td><td>29.71 (+19.38%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>200.90 (n/a)</td><td>174.88 (n/a)</td><td>165.10 (n/a)</td><td>143.90 (n/a)</td><td>24.89 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 <b>(+25.24%)</b></td><td>0.23 (+9.85%)</td><td>0.21 (+2.42%)</td><td>0.18 (+16.18%)</td><td>0.05 <b>(+47.88%)</b></td><td>199.60 (-13.93%)</td><td>167.06 (-8.01%)</td><td>172.50 (-2.38%)</td><td>121.00 <b>(-20.13%)</b></td><td>31.73 (+0.62%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>231.90 (n/a)</td><td>181.60 (n/a)</td><td>176.70 (n/a)</td><td>151.50 (n/a)</td><td>31.53 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 <b>(+27.69%)</b></td><td>0.22 (+16.35%)</td><td>0.22 (+17.58%)</td><td>0.11 (-3.86%)</td><td>0.07 <b>(+64.73%)</b></td><td>324.10 (+4.01%)</td><td>188.84 (-8.76%)</td><td>165.40 (-14.92%)</td><td>121.50 <b>(-21.71%)</b></td><td>80.61 <b>(+31.98%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>311.60 (n/a)</td><td>206.96 (n/a)</td><td>194.40 (n/a)</td><td>155.20 (n/a)</td><td>61.08 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.23 (-1.83%)</td><td>0.21 (-1.77%)</td><td>0.21 (-7.79%)</td><td>0.20 (+12.59%)</td><td>0.01 <b>(-42.48%)</b></td><td>180.10 (-11.19%)</td><td>172.66 (+1.20%)</td><td>178.50 (+8.44%)</td><td>158.50 (+1.86%)</td><td>9.46 <b>(-48.99%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>202.80 (n/a)</td><td>170.62 (n/a)</td><td>164.60 (n/a)</td><td>155.60 (n/a)</td><td>18.54 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (-5.91%)</td><td>0.23 (-0.73%)</td><td>0.22 (+0.07%)</td><td>0.19 <b>(+25.33%)</b></td><td>0.03 <b>(-45.45%)</b></td><td>191.80 <b>(-20.22%)</b></td><td>164.42 (-2.63%)</td><td>165.10 (-0.06%)</td><td>137.00 (+6.28%)</td><td>19.45 <b>(-55.09%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>240.40 (n/a)</td><td>168.86 (n/a)</td><td>165.20 (n/a)</td><td>128.90 (n/a)</td><td>43.31 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 <b>(+27.87%)</b></td><td>0.23 (+14.13%)</td><td>0.22 (+8.74%)</td><td>0.20 (+3.01%)</td><td>0.03 <b>(+173.03%)</b></td><td>188.20 (-2.89%)</td><td>163.64 (-11.22%)</td><td>170.40 (-8.04%)</td><td>130.80 <b>(-21.77%)</b></td><td>22.17 <b>(+104.54%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>184.32 (n/a)</td><td>185.30 (n/a)</td><td>167.20 (n/a)</td><td>10.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (-7.20%)</td><td>0.23 (+9.81%)</td><td>0.22 (+15.94%)</td><td>0.21 <b>(+26.74%)</b></td><td>0.03 <b>(-46.63%)</b></td><td>177.40 <b>(-21.09%)</b></td><td>161.94 (-11.77%)</td><td>167.70 (-13.73%)</td><td>132.70 (+7.71%)</td><td>17.86 <b>(-53.34%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>224.80 (n/a)</td><td>183.54 (n/a)</td><td>194.40 (n/a)</td><td>123.20 (n/a)</td><td>38.28 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.23 <b>(-20.74%)</b></td><td>0.21 (-9.43%)</td><td>0.23 (+1.46%)</td><td>0.19 (+5.54%)</td><td>0.02 <b>(-50.24%)</b></td><td>196.90 (-5.25%)</td><td>175.24 (+8.29%)</td><td>163.60 (-1.45%)</td><td>160.50 <b>(+26.18%)</b></td><td>18.29 <b>(-40.46%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>207.80 (n/a)</td><td>161.82 (n/a)</td><td>166.00 (n/a)</td><td>127.20 (n/a)</td><td>30.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.34 (+4.72%)</td><td>0.25 (-3.52%)</td><td>0.23 (-11.66%)</td><td>0.22 (+6.12%)</td><td>0.05 (+14.28%)</td><td>188.40 (-5.75%)</td><td>167.04 (+3.97%)</td><td>175.40 (+13.16%)</td><td>121.40 (-4.48%)</td><td>26.16 (-1.34%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>199.90 (n/a)</td><td>160.66 (n/a)</td><td>155.00 (n/a)</td><td>127.10 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.34 (+2.89%)</td><td>0.26 (-7.66%)</td><td>0.25 (-11.53%)</td><td>0.19 (-6.92%)</td><td>0.05 (+14.04%)</td><td>214.00 (+7.43%)</td><td>164.72 (+9.10%)</td><td>164.10 (+13.02%)</td><td>122.00 (-2.87%)</td><td>33.12 (+15.65%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>199.20 (n/a)</td><td>150.98 (n/a)</td><td>145.20 (n/a)</td><td>125.60 (n/a)</td><td>28.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.29 (-8.93%)</td><td>0.24 (-1.50%)</td><td>0.25 (+10.82%)</td><td>0.17 (-18.96%)</td><td>0.04 (-2.96%)</td><td>235.60 <b>(+23.42%)</b></td><td>176.88 (+2.25%)</td><td>164.20 (-9.78%)</td><td>139.00 (+9.79%)</td><td>36.56 <b>(+37.05%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>190.90 (n/a)</td><td>172.98 (n/a)</td><td>182.00 (n/a)</td><td>126.60 (n/a)</td><td>26.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.31 (-6.53%)</td><td>0.24 (+2.49%)</td><td>0.25 (+13.62%)</td><td>0.19 (-3.25%)</td><td>0.05 (-16.32%)</td><td>218.50 (+3.36%)</td><td>175.52 (-3.07%)</td><td>166.00 (-11.98%)</td><td>133.50 (+6.97%)</td><td>32.16 (-3.58%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>211.40 (n/a)</td><td>181.08 (n/a)</td><td>188.60 (n/a)</td><td>124.80 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 <b>(-26.72%)</b></td><td>0.24 (-7.24%)</td><td>0.25 (+7.50%)</td><td>0.16 <b>(-21.39%)</b></td><td>0.05 <b>(-34.19%)</b></td><td>250.30 <b>(+27.25%)</b></td><td>175.48 (+6.90%)</td><td>161.20 (-6.93%)</td><td>144.30 <b>(+36.39%)</b></td><td>43.06 <b>(+23.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>196.70 (n/a)</td><td>164.16 (n/a)</td><td>173.20 (n/a)</td><td>105.80 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.36 <b>(+37.14%)</b></td><td>0.27 <b>(+32.44%)</b></td><td>0.25 <b>(+21.45%)</b></td><td>0.22 <b>(+26.71%)</b></td><td>0.06 <b>(+61.92%)</b></td><td>187.20 <b>(-21.08%)</b></td><td>154.22 <b>(-23.68%)</b></td><td>162.70 (-17.66%)</td><td>114.40 <b>(-27.09%)</b></td><td>30.08 (-8.46%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>237.20 (n/a)</td><td>202.08 (n/a)</td><td>197.60 (n/a)</td><td>156.90 (n/a)</td><td>32.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.29 (-9.47%)</td><td>0.24 (+8.93%)</td><td>0.25 (+18.88%)</td><td>0.19 (+7.19%)</td><td>0.04 <b>(-37.41%)</b></td><td>213.30 (-6.69%)</td><td>172.00 (-10.33%)</td><td>164.50 (-15.86%)</td><td>141.60 (+10.45%)</td><td>26.35 <b>(-32.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>228.60 (n/a)</td><td>191.82 (n/a)</td><td>195.50 (n/a)</td><td>128.20 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (-13.40%)</td><td>0.23 (-3.38%)</td><td>0.24 (-1.68%)</td><td>0.20 (+9.77%)</td><td>0.02 <b>(-46.76%)</b></td><td>207.90 (-8.90%)</td><td>176.70 (+1.66%)</td><td>170.50 (+1.73%)</td><td>160.70 (+15.45%)</td><td>18.25 <b>(-44.54%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>228.20 (n/a)</td><td>173.82 (n/a)</td><td>167.60 (n/a)</td><td>139.20 (n/a)</td><td>32.91 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (+6.83%)</td><td>0.23 (+15.76%)</td><td>0.25 <b>(+30.25%)</b></td><td>0.14 (-12.05%)</td><td>0.05 <b>(+55.78%)</b></td><td>245.30 (+13.67%)</td><td>161.46 (-10.71%)</td><td>139.70 <b>(-23.24%)</b></td><td>131.70 (-6.33%)</td><td>47.66 <b>(+73.41%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>215.80 (n/a)</td><td>180.82 (n/a)</td><td>182.00 (n/a)</td><td>140.60 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 <b>(+27.37%)</b></td><td>0.23 (+18.41%)</td><td>0.19 (+3.67%)</td><td>0.18 (+13.51%)</td><td>0.06 <b>(+99.72%)</b></td><td>192.90 (-11.88%)</td><td>161.70 (-13.00%)</td><td>181.90 (-3.55%)</td><td>116.00 <b>(-21.46%)</b></td><td>36.46 <b>(+43.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>218.90 (n/a)</td><td>185.86 (n/a)</td><td>188.60 (n/a)</td><td>147.70 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 <b>(+20.81%)</b></td><td>0.21 (+5.62%)</td><td>0.20 (-4.11%)</td><td>0.18 (+14.65%)</td><td>0.04 <b>(+28.69%)</b></td><td>196.60 (-12.78%)</td><td>170.10 (-5.01%)</td><td>174.10 (+4.31%)</td><td>128.00 (-17.21%)</td><td>26.44 (-9.23%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.40 (n/a)</td><td>179.08 (n/a)</td><td>166.90 (n/a)</td><td>154.60 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (+7.98%)</td><td>0.22 (+9.67%)</td><td>0.20 (+4.44%)</td><td>0.18 (+14.15%)</td><td>0.05 <b>(+28.23%)</b></td><td>197.00 (-12.41%)</td><td>165.60 (-7.95%)</td><td>172.50 (-4.27%)</td><td>126.80 (-7.38%)</td><td>33.23 (+6.43%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.90 (n/a)</td><td>179.90 (n/a)</td><td>180.20 (n/a)</td><td>136.90 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.23 (-17.06%)</td><td>0.18 <b>(-20.57%)</b></td><td>0.19 (-16.87%)</td><td>0.14 <b>(-30.99%)</b></td><td>0.03 (-1.63%)</td><td>252.50 <b>(+44.87%)</b></td><td>194.40 <b>(+27.21%)</b></td><td>184.20 <b>(+20.31%)</b></td><td>153.40 <b>(+20.50%)</b></td><td>36.64 <b>(+72.53%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>174.30 (n/a)</td><td>152.82 (n/a)</td><td>153.10 (n/a)</td><td>127.30 (n/a)</td><td>21.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (-4.52%)</td><td>0.17 (-19.94%)</td><td>0.16 (-19.70%)</td><td>0.12 <b>(-27.94%)</b></td><td>0.05 (+8.22%)</td><td>293.00 <b>(+38.80%)</b></td><td>214.24 <b>(+28.36%)</b></td><td>223.20 <b>(+24.48%)</b></td><td>133.40 (+4.71%)</td><td>59.15 <b>(+59.99%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>211.10 (n/a)</td><td>166.90 (n/a)</td><td>179.30 (n/a)</td><td>127.40 (n/a)</td><td>36.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (+0.29%)</td><td>0.23 (+17.17%)</td><td>0.22 (+18.48%)</td><td>0.21 (+19.57%)</td><td>0.02 <b>(-39.83%)</b></td><td>168.00 (-16.38%)</td><td>154.64 (-15.62%)</td><td>160.00 (-15.57%)</td><td>141.00 (-0.28%)</td><td>12.15 <b>(-49.33%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>200.90 (n/a)</td><td>183.26 (n/a)</td><td>189.50 (n/a)</td><td>141.40 (n/a)</td><td>23.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (+9.51%)</td><td>0.20 (+1.98%)</td><td>0.21 (+7.81%)</td><td>0.12 <b>(-32.02%)</b></td><td>0.05 <b>(+132.86%)</b></td><td>298.90 <b>(+47.10%)</b></td><td>186.56 (+4.29%)</td><td>165.30 (-7.24%)</td><td>143.50 (-8.66%)</td><td>64.40 <b>(+223.03%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>203.20 (n/a)</td><td>178.88 (n/a)</td><td>178.20 (n/a)</td><td>157.10 (n/a)</td><td>19.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.97 (+10.60%)</td><td>0.72 (-1.29%)</td><td>0.68 (-3.53%)</td><td>0.61 (+11.24%)</td><td>0.14 (+5.01%)</td><td>215.90 (-10.08%)</td><td>186.92 (+0.94%)</td><td>193.10 (+3.65%)</td><td>134.90 (-9.65%)</td><td>30.66 (-16.55%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.88 (n/a)</td><td>0.73 (n/a)</td><td>0.70 (n/a)</td><td>0.55 (n/a)</td><td>0.14 (n/a)</td><td>240.10 (n/a)</td><td>185.18 (n/a)</td><td>186.30 (n/a)</td><td>149.30 (n/a)</td><td>36.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.92 (-8.95%)</td><td>0.73 (-6.18%)</td><td>0.70 (-2.46%)</td><td>0.62 <b>(+24.34%)</b></td><td>0.11 <b>(-46.61%)</b></td><td>210.10 (-19.59%)</td><td>182.86 (+1.69%)</td><td>188.30 (+2.50%)</td><td>143.00 (+9.83%)</td><td>24.82 <b>(-52.95%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.01 (n/a)</td><td>0.78 (n/a)</td><td>0.71 (n/a)</td><td>0.50 (n/a)</td><td>0.21 (n/a)</td><td>261.30 (n/a)</td><td>179.82 (n/a)</td><td>183.70 (n/a)</td><td>130.20 (n/a)</td><td>52.76 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.99 (-0.47%)</td><td>0.74 (+1.15%)</td><td>0.68 (-5.24%)</td><td>0.67 <b>(+48.30%)</b></td><td>0.14 <b>(-32.64%)</b></td><td>197.00 <b>(-32.58%)</b></td><td>182.16 (-6.01%)</td><td>193.70 (+5.50%)</td><td>132.70 (+0.45%)</td><td>27.70 <b>(-55.41%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.99 (n/a)</td><td>0.73 (n/a)</td><td>0.71 (n/a)</td><td>0.45 (n/a)</td><td>0.21 (n/a)</td><td>292.20 (n/a)</td><td>193.80 (n/a)</td><td>183.60 (n/a)</td><td>132.10 (n/a)</td><td>62.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+7.13%)</td><td>0.03 (-2.15%)</td><td>0.02 (-9.70%)</td><td>0.02 (-12.91%)</td><td>0.01 <b>(+88.43%)</b></td><td>188.90 (+14.83%)</td><td>158.64 (+5.18%)</td><td>179.00 (+10.77%)</td><td>119.90 (-6.69%)</td><td>33.60 <b>(+97.71%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.50 (n/a)</td><td>150.82 (n/a)</td><td>161.60 (n/a)</td><td>128.50 (n/a)</td><td>16.99 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+5.49%)</td><td>0.03 (+13.62%)</td><td>0.03 <b>(+37.98%)</b></td><td>0.02 (+3.04%)</td><td>0.01 (+16.15%)</td><td>254.10 (-2.94%)</td><td>168.04 (-10.54%)</td><td>141.90 <b>(-27.53%)</b></td><td>118.70 (-5.19%)</td><td>55.43 (+9.21%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>261.80 (n/a)</td><td>187.84 (n/a)</td><td>195.80 (n/a)</td><td>125.20 (n/a)</td><td>50.76 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (+7.78%)</td><td>0.03 (+4.66%)</td><td>0.03 (+10.44%)</td><td>0.02 (-13.77%)</td><td>0.00 <b>(+77.61%)</b></td><td>205.10 (+16.01%)</td><td>157.10 (-2.89%)</td><td>148.40 (-9.46%)</td><td>129.90 (-7.21%)</td><td>28.32 <b>(+100.60%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.80 (n/a)</td><td>161.78 (n/a)</td><td>163.90 (n/a)</td><td>140.00 (n/a)</td><td>14.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.90 (-6.22%)</td><td>14.00 (+7.30%)</td><td>13.32 (+5.08%)</td><td>12.54 <b>(+58.95%)</b></td><td>1.66 <b>(-52.33%)</b></td><td>167.30 <b>(-37.08%)</b></td><td>151.50 (-12.13%)</td><td>157.60 (-4.83%)</td><td>131.90 (+6.63%)</td><td>17.47 <b>(-68.78%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>16.96 (n/a)</td><td>13.05 (n/a)</td><td>12.67 (n/a)</td><td>7.89 (n/a)</td><td>3.49 (n/a)</td><td>265.90 (n/a)</td><td>172.42 (n/a)</td><td>165.60 (n/a)</td><td>123.70 (n/a)</td><td>55.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.07 (+1.80%)</td><td>0.94 (+2.59%)</td><td>0.95 (+0.32%)</td><td>0.75 (-2.58%)</td><td>0.13 (-1.39%)</td><td>175.90 (+2.69%)</td><td>143.58 (-2.59%)</td><td>139.00 (-0.29%)</td><td>123.50 (-1.83%)</td><td>21.20 (-2.67%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.05 (n/a)</td><td>0.91 (n/a)</td><td>0.95 (n/a)</td><td>0.77 (n/a)</td><td>0.13 (n/a)</td><td>171.30 (n/a)</td><td>147.40 (n/a)</td><td>139.40 (n/a)</td><td>125.80 (n/a)</td><td>21.78 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.11 (+4.66%)</td><td>0.88 (-2.93%)</td><td>0.90 (-6.56%)</td><td>0.73 (+16.88%)</td><td>0.15 (-15.69%)</td><td>180.10 (-14.44%)</td><td>153.12 (+1.46%)</td><td>146.70 (+7.00%)</td><td>118.70 (-4.43%)</td><td>24.75 <b>(-30.59%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.06 (n/a)</td><td>0.91 (n/a)</td><td>0.96 (n/a)</td><td>0.63 (n/a)</td><td>0.18 (n/a)</td><td>210.50 (n/a)</td><td>150.92 (n/a)</td><td>137.10 (n/a)</td><td>124.20 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.90 (-16.83%)</td><td>0.73 (-16.23%)</td><td>0.79 (-9.46%)</td><td>0.35 <b>(-42.90%)</b></td><td>0.22 (+13.95%)</td><td>379.50 <b>(+75.13%)</b></td><td>204.86 <b>(+29.07%)</b></td><td>167.80 (+10.39%)</td><td>146.20 <b>(+20.23%)</b></td><td>98.06 <b>(+157.97%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.09 (n/a)</td><td>0.87 (n/a)</td><td>0.87 (n/a)</td><td>0.61 (n/a)</td><td>0.19 (n/a)</td><td>216.70 (n/a)</td><td>158.72 (n/a)</td><td>152.00 (n/a)</td><td>121.60 (n/a)</td><td>38.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.02 (-4.23%)</td><td>0.89 (-5.52%)</td><td>0.84 (-9.74%)</td><td>0.79 (-3.55%)</td><td>0.11 <b>(+24.84%)</b></td><td>166.80 (+3.67%)</td><td>150.50 (+6.36%)</td><td>158.00 (+10.80%)</td><td>129.90 (+4.42%)</td><td>17.95 <b>(+34.17%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.06 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.82 (n/a)</td><td>0.09 (n/a)</td><td>160.90 (n/a)</td><td>141.50 (n/a)</td><td>142.60 (n/a)</td><td>124.40 (n/a)</td><td>13.38 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.11 (+15.44%)</td><td>0.90 (+8.93%)</td><td>0.95 (+14.97%)</td><td>0.67 (+6.62%)</td><td>0.21 <b>(+59.95%)</b></td><td>197.90 (-6.21%)</td><td>153.82 (-6.02%)</td><td>139.40 (-12.98%)</td><td>118.70 (-13.36%)</td><td>37.23 <b>(+29.49%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.96 (n/a)</td><td>0.82 (n/a)</td><td>0.82 (n/a)</td><td>0.63 (n/a)</td><td>0.13 (n/a)</td><td>211.00 (n/a)</td><td>163.68 (n/a)</td><td>160.20 (n/a)</td><td>137.00 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 <b>(-23.74%)</b></td><td>0.02 <b>(-21.52%)</b></td><td>0.02 <b>(-22.51%)</b></td><td>0.02 (-17.78%)</td><td>0.00 <b>(-40.48%)</b></td><td>202.10 <b>(+21.60%)</b></td><td>181.26 <b>(+26.65%)</b></td><td>171.50 <b>(+29.04%)</b></td><td>165.20 <b>(+31.11%)</b></td><td>18.22 (-4.87%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.20 (n/a)</td><td>143.12 (n/a)</td><td>132.90 (n/a)</td><td>126.00 (n/a)</td><td>19.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (-0.04%)</td><td>0.03 (+8.44%)</td><td>0.03 (+9.60%)</td><td>0.02 (+6.20%)</td><td>0.00 (+8.26%)</td><td>193.30 (-5.85%)</td><td>155.34 (-7.58%)</td><td>151.30 (-8.75%)</td><td>128.90 (+0.00%)</td><td>28.11 (+0.92%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.30 (n/a)</td><td>168.08 (n/a)</td><td>165.80 (n/a)</td><td>128.90 (n/a)</td><td>27.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.00 (-4.44%)</td><td>0.00 (-2.35%)</td><td>0.00 (-2.33%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-34.12%)</b></td><td>1055.26 (+1.32%)</td><td>983.28 (+1.86%)</td><td>969.58 (+2.59%)</td><td>952.66 (+3.50%)</td><td>40.93 (-16.39%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1041.51 (n/a)</td><td>965.28 (n/a)</td><td>945.12 (n/a)</td><td>920.41 (n/a)</td><td>48.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.01 (+1.20%)</td><td>0.01 (-0.50%)</td><td>0.01 (+2.50%)</td><td>0.01 (-8.86%)</td><td>0.00 <b>(+203.07%)</b></td><td>1142.80 (+9.85%)</td><td>1024.32 (+1.19%)</td><td>1003.90 (-1.45%)</td><td>972.29 (-1.42%)</td><td>69.97 <b>(+226.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1040.29 (n/a)</td><td>1012.30 (n/a)</td><td>1018.67 (n/a)</td><td>986.32 (n/a)</td><td>21.42 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.96 (+0.37%)</td><td>0.95 (+0.18%)</td><td>0.95 (+0.20%)</td><td>0.95 (-0.25%)</td><td>0.00 <b>(+110.79%)</b></td><td>2214.00 (+0.25%)</td><td>2198.03 (-0.18%)</td><td>2196.08 (-0.19%)</td><td>2187.86 (-0.37%)</td><td>11.23 <b>(+109.72%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.00 (n/a)</td><td>2208.45 (n/a)</td><td>2201.89 (n/a)</td><td>2200.34 (n/a)</td><td>2195.91 (n/a)</td><td>5.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.15 (+9.58%)</td><td>5.51 <b>(+21.48%)</b></td><td>5.46 (+17.85%)</td><td>4.98 <b>(+52.46%)</b></td><td>0.43 <b>(-48.75%)</b></td><td>210.50 <b>(-34.42%)</b></td><td>191.30 (-19.83%)</td><td>192.10 (-15.15%)</td><td>170.40 (-8.73%)</td><td>14.75 <b>(-70.47%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.62 (n/a)</td><td>4.53 (n/a)</td><td>4.63 (n/a)</td><td>3.27 (n/a)</td><td>0.85 (n/a)</td><td>321.00 (n/a)</td><td>238.62 (n/a)</td><td>226.40 (n/a)</td><td>186.70 (n/a)</td><td>49.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>5.68 (-4.81%)</td><td>4.94 (+8.93%)</td><td>4.98 (+10.59%)</td><td>3.75 <b>(+33.34%)</b></td><td>0.77 <b>(-33.63%)</b></td><td>279.60 <b>(-25.00%)</b></td><td>217.06 (-11.86%)</td><td>210.50 (-9.58%)</td><td>184.60 (+5.07%)</td><td>38.07 <b>(-49.54%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.97 (n/a)</td><td>4.53 (n/a)</td><td>4.50 (n/a)</td><td>2.81 (n/a)</td><td>1.16 (n/a)</td><td>372.80 (n/a)</td><td>246.28 (n/a)</td><td>232.80 (n/a)</td><td>175.70 (n/a)</td><td>75.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.12 (-0.70%)</td><td>5.18 (-3.49%)</td><td>5.24 (-11.85%)</td><td>4.19 (+3.94%)</td><td>0.75 <b>(-22.05%)</b></td><td>250.20 (-3.81%)</td><td>205.78 (+2.45%)</td><td>200.00 (+13.44%)</td><td>171.30 (+0.71%)</td><td>30.64 <b>(-22.90%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>6.16 (n/a)</td><td>5.37 (n/a)</td><td>5.95 (n/a)</td><td>4.03 (n/a)</td><td>0.96 (n/a)</td><td>260.10 (n/a)</td><td>200.86 (n/a)</td><td>176.30 (n/a)</td><td>170.10 (n/a)</td><td>39.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.28 (+3.45%)</td><td>5.06 (-10.31%)</td><td>4.92 (-11.81%)</td><td>4.24 <b>(-20.88%)</b></td><td>0.76 <b>(+186.57%)</b></td><td>247.30 <b>(+26.37%)</b></td><td>210.74 (+13.17%)</td><td>213.10 (+13.41%)</td><td>167.00 (-3.36%)</td><td>29.15 <b>(+246.64%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>6.07 (n/a)</td><td>5.64 (n/a)</td><td>5.58 (n/a)</td><td>5.36 (n/a)</td><td>0.26 (n/a)</td><td>195.70 (n/a)</td><td>186.22 (n/a)</td><td>187.90 (n/a)</td><td>172.80 (n/a)</td><td>8.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.35 (+2.55%)</td><td>8.41 (+2.32%)</td><td>8.48 (-2.48%)</td><td>7.50 <b>(+26.25%)</b></td><td>0.80 <b>(-38.55%)</b></td><td>279.50 <b>(-20.78%)</b></td><td>251.18 (-4.02%)</td><td>247.30 (+2.57%)</td><td>224.20 (-2.52%)</td><td>24.21 <b>(-53.13%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.12 (n/a)</td><td>8.22 (n/a)</td><td>8.70 (n/a)</td><td>5.94 (n/a)</td><td>1.31 (n/a)</td><td>352.80 (n/a)</td><td>261.70 (n/a)</td><td>241.10 (n/a)</td><td>230.00 (n/a)</td><td>51.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.82 (+7.61%)</td><td>8.13 (-0.00%)</td><td>7.89 (+3.33%)</td><td>6.97 (-4.84%)</td><td>1.06 <b>(+23.08%)</b></td><td>300.90 (+5.10%)</td><td>261.10 (+0.41%)</td><td>265.80 (-3.20%)</td><td>213.60 (-7.09%)</td><td>31.93 (+19.95%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.12 (n/a)</td><td>8.14 (n/a)</td><td>7.64 (n/a)</td><td>7.32 (n/a)</td><td>0.86 (n/a)</td><td>286.30 (n/a)</td><td>260.04 (n/a)</td><td>274.60 (n/a)</td><td>229.90 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.20 (-3.46%)</td><td>8.32 (+1.08%)</td><td>8.05 (+2.62%)</td><td>7.85 (+1.65%)</td><td>0.54 <b>(-29.58%)</b></td><td>267.30 (-1.62%)</td><td>252.94 (-1.39%)</td><td>260.60 (-2.58%)</td><td>227.90 (+3.59%)</td><td>15.65 <b>(-28.78%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.53 (n/a)</td><td>8.23 (n/a)</td><td>7.84 (n/a)</td><td>7.72 (n/a)</td><td>0.77 (n/a)</td><td>271.70 (n/a)</td><td>256.50 (n/a)</td><td>267.50 (n/a)</td><td>220.00 (n/a)</td><td>21.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.78 (-0.35%)</td><td>9.02 (+1.81%)</td><td>8.97 (+4.28%)</td><td>7.73 (-3.41%)</td><td>0.82 (-7.31%)</td><td>271.40 (+3.55%)</td><td>234.08 (-1.85%)</td><td>233.70 (-4.10%)</td><td>214.40 (+0.33%)</td><td>22.82 (-2.26%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.82 (n/a)</td><td>8.86 (n/a)</td><td>8.61 (n/a)</td><td>8.00 (n/a)</td><td>0.88 (n/a)</td><td>262.10 (n/a)</td><td>238.48 (n/a)</td><td>243.70 (n/a)</td><td>213.70 (n/a)</td><td>23.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>10.08 (-8.12%)</td><td>9.39 (-2.80%)</td><td>9.58 (-5.60%)</td><td>8.69 (+14.14%)</td><td>0.55 <b>(-59.85%)</b></td><td>241.40 (-12.41%)</td><td>224.02 (+1.34%)</td><td>218.90 (+5.95%)</td><td>208.00 (+8.84%)</td><td>13.27 <b>(-61.70%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>10.97 (n/a)</td><td>9.66 (n/a)</td><td>10.15 (n/a)</td><td>7.61 (n/a)</td><td>1.38 (n/a)</td><td>275.60 (n/a)</td><td>221.06 (n/a)</td><td>206.60 (n/a)</td><td>191.10 (n/a)</td><td>34.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.40 (-3.23%)</td><td>8.25 (-6.96%)</td><td>7.91 (-9.29%)</td><td>7.46 (-7.59%)</td><td>0.81 <b>(+25.28%)</b></td><td>281.20 (+8.24%)</td><td>256.12 (+7.82%)</td><td>265.10 (+10.27%)</td><td>223.10 (+3.33%)</td><td>24.08 <b>(+40.54%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.72 (n/a)</td><td>8.87 (n/a)</td><td>8.72 (n/a)</td><td>8.07 (n/a)</td><td>0.64 (n/a)</td><td>259.80 (n/a)</td><td>237.54 (n/a)</td><td>240.40 (n/a)</td><td>215.90 (n/a)</td><td>17.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>11.62 (-13.17%)</td><td>10.81 (-6.60%)</td><td>10.78 (-3.53%)</td><td>10.07 (+5.92%)</td><td>0.56 <b>(-64.44%)</b></td><td>416.60 (-5.58%)</td><td>388.84 (+5.67%)</td><td>388.90 (+3.65%)</td><td>360.90 (+15.16%)</td><td>20.12 <b>(-60.82%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.38 (n/a)</td><td>11.57 (n/a)</td><td>11.18 (n/a)</td><td>9.51 (n/a)</td><td>1.58 (n/a)</td><td>441.20 (n/a)</td><td>367.96 (n/a)</td><td>375.20 (n/a)</td><td>313.40 (n/a)</td><td>51.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>12.33 (-10.91%)</td><td>11.29 (-1.64%)</td><td>11.14 (-3.41%)</td><td>10.19 (+7.93%)</td><td>0.87 <b>(-44.94%)</b></td><td>411.70 (-7.34%)</td><td>373.32 (+0.64%)</td><td>376.40 (+3.52%)</td><td>340.10 (+12.24%)</td><td>28.91 <b>(-42.84%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.84 (n/a)</td><td>11.48 (n/a)</td><td>11.54 (n/a)</td><td>9.44 (n/a)</td><td>1.58 (n/a)</td><td>444.30 (n/a)</td><td>370.96 (n/a)</td><td>363.60 (n/a)</td><td>303.00 (n/a)</td><td>50.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>12.37 (-5.53%)</td><td>11.53 (-1.80%)</td><td>11.43 (-3.99%)</td><td>11.15 (+11.94%)</td><td>0.49 <b>(-56.95%)</b></td><td>376.10 (-10.69%)</td><td>364.26 (+1.16%)</td><td>367.00 (+4.14%)</td><td>339.00 (+5.84%)</td><td>14.67 <b>(-60.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.10 (n/a)</td><td>11.74 (n/a)</td><td>11.90 (n/a)</td><td>9.96 (n/a)</td><td>1.13 (n/a)</td><td>421.10 (n/a)</td><td>360.08 (n/a)</td><td>352.40 (n/a)</td><td>320.30 (n/a)</td><td>37.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>14.09 (-7.34%)</td><td>12.13 (-8.69%)</td><td>12.69 (+0.08%)</td><td>9.59 <b>(-20.57%)</b></td><td>1.80 <b>(+39.46%)</b></td><td>437.60 <b>(+25.93%)</b></td><td>352.52 (+10.83%)</td><td>330.60 (-0.09%)</td><td>297.70 (+7.94%)</td><td>56.29 <b>(+91.34%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>15.21 (n/a)</td><td>13.28 (n/a)</td><td>12.68 (n/a)</td><td>12.07 (n/a)</td><td>1.29 (n/a)</td><td>347.50 (n/a)</td><td>318.06 (n/a)</td><td>330.90 (n/a)</td><td>275.80 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.24 (+3.62%)</td><td>13.26 (+2.33%)</td><td>13.22 (-1.34%)</td><td>11.79 (+4.37%)</td><td>1.32 (-8.32%)</td><td>355.60 (-4.20%)</td><td>318.84 (-2.51%)</td><td>317.30 (+1.37%)</td><td>275.30 (-3.51%)</td><td>30.68 (-16.71%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.70 (n/a)</td><td>12.95 (n/a)</td><td>13.40 (n/a)</td><td>11.30 (n/a)</td><td>1.44 (n/a)</td><td>371.20 (n/a)</td><td>327.06 (n/a)</td><td>313.00 (n/a)</td><td>285.30 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>14.40 (-8.50%)</td><td>12.47 (-7.00%)</td><td>12.48 (-8.67%)</td><td>11.00 (+10.88%)</td><td>1.30 <b>(-40.08%)</b></td><td>381.40 (-9.81%)</td><td>339.34 (+5.83%)</td><td>336.00 (+9.48%)</td><td>291.30 (+9.31%)</td><td>34.49 <b>(-42.90%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>15.74 (n/a)</td><td>13.40 (n/a)</td><td>13.67 (n/a)</td><td>9.92 (n/a)</td><td>2.18 (n/a)</td><td>422.90 (n/a)</td><td>320.66 (n/a)</td><td>306.90 (n/a)</td><td>266.50 (n/a)</td><td>60.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.30 (+0.96%)</td><td>13.68 (+4.70%)</td><td>12.83 (+0.81%)</td><td>12.42 (+15.12%)</td><td>1.41 (-13.09%)</td><td>337.80 (-13.14%)</td><td>309.16 (-4.93%)</td><td>327.00 (-0.82%)</td><td>274.10 (-0.94%)</td><td>30.91 <b>(-26.42%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>15.16 (n/a)</td><td>13.07 (n/a)</td><td>12.72 (n/a)</td><td>10.79 (n/a)</td><td>1.63 (n/a)</td><td>388.90 (n/a)</td><td>325.18 (n/a)</td><td>329.70 (n/a)</td><td>276.70 (n/a)</td><td>42.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.01 (+13.09%)</td><td>13.66 <b>(+27.00%)</b></td><td>13.49 <b>(+34.85%)</b></td><td>12.67 <b>(+36.32%)</b></td><td>1.04 <b>(-35.34%)</b></td><td>331.00 <b>(-26.66%)</b></td><td>308.36 <b>(-22.19%)</b></td><td>311.00 <b>(-25.85%)</b></td><td>279.50 (-11.55%)</td><td>23.04 <b>(-57.48%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.27 (n/a)</td><td>10.76 (n/a)</td><td>10.00 (n/a)</td><td>9.29 (n/a)</td><td>1.61 (n/a)</td><td>451.30 (n/a)</td><td>396.28 (n/a)</td><td>419.40 (n/a)</td><td>316.00 (n/a)</td><td>54.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.38 (+11.15%)</td><td>3.05 (+14.05%)</td><td>2.97 (+5.79%)</td><td>2.79 <b>(+21.00%)</b></td><td>0.24 <b>(-28.12%)</b></td><td>187.60 (-17.36%)</td><td>172.98 (-13.02%)</td><td>176.50 (-5.46%)</td><td>155.10 (-10.03%)</td><td>13.22 <b>(-47.97%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.04 (n/a)</td><td>2.67 (n/a)</td><td>2.81 (n/a)</td><td>2.31 (n/a)</td><td>0.33 (n/a)</td><td>227.00 (n/a)</td><td>198.88 (n/a)</td><td>186.70 (n/a)</td><td>172.40 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>5.72 (+3.20%)</td><td>5.02 (+2.42%)</td><td>4.98 (-0.58%)</td><td>4.62 <b>(+20.68%)</b></td><td>0.45 <b>(-34.76%)</b></td><td>226.90 (-17.13%)</td><td>210.26 (-3.48%)</td><td>210.70 (+0.57%)</td><td>183.40 (-3.07%)</td><td>17.75 <b>(-47.82%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.54 (n/a)</td><td>4.90 (n/a)</td><td>5.01 (n/a)</td><td>3.83 (n/a)</td><td>0.68 (n/a)</td><td>273.80 (n/a)</td><td>217.84 (n/a)</td><td>209.50 (n/a)</td><td>189.20 (n/a)</td><td>34.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.17 (+11.94%)</td><td>8.11 (+11.08%)</td><td>8.15 (+13.67%)</td><td>7.36 (+11.67%)</td><td>0.70 (-0.94%)</td><td>285.00 (-10.43%)</td><td>260.22 (-10.12%)</td><td>257.30 (-12.03%)</td><td>228.60 (-10.67%)</td><td>21.55 <b>(-21.34%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>8.20 (n/a)</td><td>7.30 (n/a)</td><td>7.17 (n/a)</td><td>6.59 (n/a)</td><td>0.70 (n/a)</td><td>318.20 (n/a)</td><td>289.52 (n/a)</td><td>292.50 (n/a)</td><td>255.90 (n/a)</td><td>27.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.70 (+12.48%)</td><td>2.97 (+2.65%)</td><td>2.90 (-0.30%)</td><td>2.03 (-19.35%)</td><td>0.64 <b>(+124.68%)</b></td><td>258.80 <b>(+24.01%)</b></td><td>184.28 (+0.85%)</td><td>180.90 (+0.28%)</td><td>141.70 (-11.10%)</td><td>45.41 <b>(+151.89%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.29 (n/a)</td><td>2.89 (n/a)</td><td>2.91 (n/a)</td><td>2.51 (n/a)</td><td>0.28 (n/a)</td><td>208.70 (n/a)</td><td>182.72 (n/a)</td><td>180.40 (n/a)</td><td>159.40 (n/a)</td><td>18.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 <b>(+28.04%)</b></td><td>0.19 (+8.66%)</td><td>0.20 (+9.20%)</td><td>0.09 <b>(-35.37%)</b></td><td>0.07 <b>(+205.98%)</b></td><td>358.20 <b>(+54.73%)</b></td><td>199.82 (+4.00%)</td><td>166.80 (-8.40%)</td><td>129.50 <b>(-21.89%)</b></td><td>93.88 <b>(+268.14%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>192.14 (n/a)</td><td>182.10 (n/a)</td><td>165.80 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (+7.57%)</td><td>0.20 (-6.61%)</td><td>0.22 (-1.09%)</td><td>0.15 (-19.94%)</td><td>0.04 <b>(+160.11%)</b></td><td>217.00 <b>(+24.86%)</b></td><td>168.90 (+10.13%)</td><td>150.80 (+1.07%)</td><td>134.10 (-7.07%)</td><td>35.08 <b>(+200.60%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>173.80 (n/a)</td><td>153.36 (n/a)</td><td>149.20 (n/a)</td><td>144.30 (n/a)</td><td>11.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.54 (+16.60%)</td><td>0.43 (+16.93%)</td><td>0.39 (-2.66%)</td><td>0.34 <b>(+95.06%)</b></td><td>0.10 (-13.53%)</td><td>193.10 <b>(-48.73%)</b></td><td>158.40 <b>(-21.49%)</b></td><td>168.90 (+2.74%)</td><td>120.90 (-14.26%)</td><td>33.79 <b>(-65.61%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.40 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>376.60 (n/a)</td><td>201.76 (n/a)</td><td>164.40 (n/a)</td><td>141.00 (n/a)</td><td>98.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.55 <b>(+20.24%)</b></td><td>0.43 (+8.43%)</td><td>0.38 (-1.23%)</td><td>0.33 (-1.27%)</td><td>0.10 <b>(+103.20%)</b></td><td>201.20 (+1.31%)</td><td>159.98 (-4.93%)</td><td>173.40 (+1.29%)</td><td>118.30 (-16.81%)</td><td>35.72 <b>(+67.39%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>198.60 (n/a)</td><td>168.28 (n/a)</td><td>171.20 (n/a)</td><td>142.20 (n/a)</td><td>21.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.53 <b>(+23.73%)</b></td><td>0.42 (+5.58%)</td><td>0.39 (-1.64%)</td><td>0.37 (+4.92%)</td><td>0.07 <b>(+137.18%)</b></td><td>176.30 (-4.65%)</td><td>158.68 (-4.07%)</td><td>166.90 (+1.64%)</td><td>123.20 (-19.16%)</td><td>21.17 <b>(+77.13%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.03 (n/a)</td><td>184.90 (n/a)</td><td>165.42 (n/a)</td><td>164.20 (n/a)</td><td>152.40 (n/a)</td><td>11.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.04 <b>(+29.42%)</b></td><td>0.85 (+14.09%)</td><td>0.89 (+15.34%)</td><td>0.63 (+5.69%)</td><td>0.20 <b>(+133.71%)</b></td><td>209.10 (-5.38%)</td><td>162.08 (-9.26%)</td><td>146.90 (-13.28%)</td><td>126.50 <b>(-22.72%)</b></td><td>39.91 <b>(+67.47%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.80 (n/a)</td><td>0.74 (n/a)</td><td>0.77 (n/a)</td><td>0.59 (n/a)</td><td>0.08 (n/a)</td><td>221.00 (n/a)</td><td>178.62 (n/a)</td><td>169.40 (n/a)</td><td>163.70 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.08 <b>(+49.62%)</b></td><td>0.87 <b>(+33.18%)</b></td><td>0.83 <b>(+27.48%)</b></td><td>0.61 (+9.95%)</td><td>0.18 <b>(+147.58%)</b></td><td>213.70 (-9.03%)</td><td>157.40 <b>(-22.80%)</b></td><td>157.40 <b>(-21.57%)</b></td><td>120.90 <b>(-33.17%)</b></td><td>35.83 <b>(+53.03%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.72 (n/a)</td><td>0.65 (n/a)</td><td>0.65 (n/a)</td><td>0.56 (n/a)</td><td>0.07 (n/a)</td><td>234.90 (n/a)</td><td>203.88 (n/a)</td><td>200.70 (n/a)</td><td>180.90 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.06 (+15.75%)</td><td>0.84 (+8.06%)</td><td>0.91 (+19.01%)</td><td>0.50 <b>(-23.86%)</b></td><td>0.24 <b>(+151.52%)</b></td><td>261.10 <b>(+31.34%)</b></td><td>169.54 (-0.84%)</td><td>143.70 (-15.96%)</td><td>124.10 (-13.64%)</td><td>58.32 <b>(+179.39%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.91 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.66 (n/a)</td><td>0.10 (n/a)</td><td>198.80 (n/a)</td><td>170.98 (n/a)</td><td>171.00 (n/a)</td><td>143.70 (n/a)</td><td>20.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.02 <b>(+39.09%)</b></td><td>0.83 <b>(+24.84%)</b></td><td>0.82 <b>(+23.32%)</b></td><td>0.63 (+11.57%)</td><td>0.17 <b>(+163.33%)</b></td><td>207.80 (-10.39%)</td><td>163.64 (-17.79%)</td><td>159.90 (-18.91%)</td><td>128.80 <b>(-28.12%)</b></td><td>33.96 <b>(+66.11%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.73 (n/a)</td><td>0.66 (n/a)</td><td>0.66 (n/a)</td><td>0.57 (n/a)</td><td>0.06 (n/a)</td><td>231.90 (n/a)</td><td>199.04 (n/a)</td><td>197.20 (n/a)</td><td>179.20 (n/a)</td><td>20.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (+10.53%)</td><td>0.10 (+3.24%)</td><td>0.09 (-1.39%)</td><td>0.08 (+3.58%)</td><td>0.03 (+18.42%)</td><td>193.10 (-3.50%)</td><td>162.82 (-2.44%)</td><td>175.40 (+1.45%)</td><td>111.80 (-9.47%)</td><td>34.04 (+2.24%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.10 (n/a)</td><td>166.90 (n/a)</td><td>172.90 (n/a)</td><td>123.50 (n/a)</td><td>33.30 (n/a)</td>
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
