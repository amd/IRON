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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (-0.41%)</td><td>0.04 (-5.06%)</td><td>0.04 (-9.07%)</td><td>0.03 (+7.04%)</td><td>0.01 <b>(-20.07%)</b></td><td>210.90 (-6.60%)</td><td>159.48 (+3.50%)</td><td>152.30 (+9.96%)</td><td>128.30 (+0.39%)</td><td>30.82 <b>(-24.51%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>154.08 (n/a)</td><td>138.50 (n/a)</td><td>127.80 (n/a)</td><td>40.83 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (+4.76%)</td><td>0.04 (-13.85%)</td><td>0.03 (-16.77%)</td><td>0.03 <b>(-28.48%)</b></td><td>0.01 <b>(+107.79%)</b></td><td>213.70 <b>(+39.76%)</b></td><td>173.68 <b>(+20.28%)</b></td><td>179.00 <b>(+20.13%)</b></td><td>114.80 (-4.49%)</td><td>36.26 <b>(+165.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>152.90 (n/a)</td><td>144.40 (n/a)</td><td>149.00 (n/a)</td><td>120.20 (n/a)</td><td>13.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (-16.34%)</td><td>0.04 (-9.15%)</td><td>0.04 (+7.87%)</td><td>0.03 (-18.89%)</td><td>0.01 (+7.25%)</td><td>207.70 <b>(+23.34%)</b></td><td>159.82 (+11.50%)</td><td>136.90 (-7.31%)</td><td>135.60 (+19.58%)</td><td>33.59 <b>(+54.24%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>168.40 (n/a)</td><td>143.34 (n/a)</td><td>147.70 (n/a)</td><td>113.40 (n/a)</td><td>21.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (-10.20%)</td><td>0.04 (-5.86%)</td><td>0.04 (-9.05%)</td><td>0.03 (-4.86%)</td><td>0.01 (-15.65%)</td><td>204.50 (+5.09%)</td><td>173.50 (+5.77%)</td><td>167.40 (+9.91%)</td><td>147.60 (+11.40%)</td><td>26.38 (-4.54%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.60 (n/a)</td><td>164.04 (n/a)</td><td>152.30 (n/a)</td><td>132.50 (n/a)</td><td>27.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 <b>(-20.60%)</b></td><td>0.03 (-3.80%)</td><td>0.03 (+11.72%)</td><td>0.03 (+3.57%)</td><td>0.00 <b>(-71.77%)</b></td><td>201.10 (-3.46%)</td><td>183.36 (+0.98%)</td><td>182.80 (-10.48%)</td><td>170.00 <b>(+25.93%)</b></td><td>11.55 <b>(-66.34%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>181.58 (n/a)</td><td>204.20 (n/a)</td><td>135.00 (n/a)</td><td>34.31 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 <b>(+47.14%)</b></td><td>0.04 (+9.99%)</td><td>0.04 (+0.97%)</td><td>0.03 <b>(+22.16%)</b></td><td>0.02 <b>(+63.52%)</b></td><td>205.10 (-18.16%)</td><td>158.98 (-5.94%)</td><td>157.70 (-0.94%)</td><td>83.60 <b>(-32.03%)</b></td><td>49.21 (-6.96%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.60 (n/a)</td><td>169.02 (n/a)</td><td>159.20 (n/a)</td><td>123.00 (n/a)</td><td>52.90 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 <b>(-29.04%)</b></td><td>0.03 (-13.35%)</td><td>0.03 (-6.31%)</td><td>0.02 (-10.73%)</td><td>0.00 <b>(-54.58%)</b></td><td>248.60 (+12.03%)</td><td>206.22 (+13.01%)</td><td>203.90 (+6.70%)</td><td>183.00 <b>(+40.99%)</b></td><td>25.58 <b>(-24.69%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>182.48 (n/a)</td><td>191.10 (n/a)</td><td>129.80 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (-17.90%)</td><td>0.03 (-4.26%)</td><td>0.03 (+8.93%)</td><td>0.03 (-1.88%)</td><td>0.00 <b>(-46.43%)</b></td><td>219.30 (+1.95%)</td><td>190.20 (+2.10%)</td><td>190.30 (-8.20%)</td><td>161.60 <b>(+21.78%)</b></td><td>23.72 <b>(-34.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>186.28 (n/a)</td><td>207.30 (n/a)</td><td>132.70 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 <b>(-22.89%)</b></td><td>0.07 (-12.58%)</td><td>0.08 (-2.23%)</td><td>0.06 (-4.80%)</td><td>0.01 <b>(-55.87%)</b></td><td>192.80 (+5.01%)</td><td>168.08 (+11.34%)</td><td>161.40 (+2.28%)</td><td>144.70 <b>(+29.66%)</b></td><td>18.81 <b>(-39.78%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>183.60 (n/a)</td><td>150.96 (n/a)</td><td>157.80 (n/a)</td><td>111.60 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (-4.22%)</td><td>0.08 (-2.21%)</td><td>0.08 (+1.06%)</td><td>0.07 (+0.73%)</td><td>0.01 (-19.48%)</td><td>186.20 (-0.69%)</td><td>157.80 (+1.64%)</td><td>161.40 (-1.04%)</td><td>131.80 (+4.44%)</td><td>20.56 (-15.80%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>155.26 (n/a)</td><td>163.10 (n/a)</td><td>126.20 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (+4.77%)</td><td>0.08 (-4.90%)</td><td>0.08 (-12.41%)</td><td>0.07 (-2.79%)</td><td>0.01 <b>(+25.81%)</b></td><td>186.30 (+2.87%)</td><td>153.60 (+5.92%)</td><td>158.20 (+14.22%)</td><td>120.30 (-4.52%)</td><td>24.98 (+18.43%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>181.10 (n/a)</td><td>145.02 (n/a)</td><td>138.50 (n/a)</td><td>126.00 (n/a)</td><td>21.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 <b>(-31.12%)</b></td><td>0.07 <b>(-21.01%)</b></td><td>0.08 (-17.09%)</td><td>0.05 <b>(-27.47%)</b></td><td>0.01 <b>(-31.06%)</b></td><td>228.30 <b>(+37.86%)</b></td><td>171.08 <b>(+26.54%)</b></td><td>159.30 <b>(+20.68%)</b></td><td>152.70 <b>(+45.15%)</b></td><td>32.24 <b>(+40.16%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>165.60 (n/a)</td><td>135.20 (n/a)</td><td>132.00 (n/a)</td><td>105.20 (n/a)</td><td>23.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (+1.59%)</td><td>0.08 (-3.84%)</td><td>0.07 (-7.56%)</td><td>0.06 (-9.39%)</td><td>0.01 <b>(+57.99%)</b></td><td>203.80 (+10.34%)</td><td>164.36 (+5.93%)</td><td>167.50 (+8.13%)</td><td>132.10 (-1.56%)</td><td>31.71 <b>(+64.78%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>155.16 (n/a)</td><td>154.90 (n/a)</td><td>134.20 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 <b>(-32.46%)</b></td><td>0.07 (-18.63%)</td><td>0.07 (-16.12%)</td><td>0.07 (-5.42%)</td><td>0.01 <b>(-64.29%)</b></td><td>186.90 (+5.71%)</td><td>172.24 (+18.39%)</td><td>176.30 (+19.20%)</td><td>142.50 <b>(+47.98%)</b></td><td>17.94 <b>(-43.79%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>176.80 (n/a)</td><td>145.48 (n/a)</td><td>147.90 (n/a)</td><td>96.30 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 <b>(+43.08%)</b></td><td>0.08 (+4.30%)</td><td>0.08 (-0.43%)</td><td>0.06 (-14.95%)</td><td>0.03 <b>(+260.20%)</b></td><td>203.90 (+17.59%)</td><td>160.58 (+1.90%)</td><td>158.20 (+0.44%)</td><td>96.10 <b>(-30.16%)</b></td><td>41.18 <b>(+184.32%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>173.40 (n/a)</td><td>157.58 (n/a)</td><td>157.50 (n/a)</td><td>137.60 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 <b>(-34.76%)</b></td><td>0.07 (-7.90%)</td><td>0.07 (+7.92%)</td><td>0.06 (+4.38%)</td><td>0.01 <b>(-75.20%)</b></td><td>204.40 (-4.22%)</td><td>178.86 (+2.35%)</td><td>176.60 (-7.35%)</td><td>158.60 <b>(+53.24%)</b></td><td>16.41 <b>(-61.17%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.40 (n/a)</td><td>174.76 (n/a)</td><td>190.60 (n/a)</td><td>103.50 (n/a)</td><td>42.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (+0.52%)</td><td>0.17 (+0.13%)</td><td>0.16 (-4.15%)</td><td>0.14 (+3.65%)</td><td>0.02 (-2.24%)</td><td>174.50 (-3.48%)</td><td>150.70 (-0.26%)</td><td>150.10 (+4.31%)</td><td>125.80 (-0.47%)</td><td>20.99 (-6.46%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>180.80 (n/a)</td><td>151.10 (n/a)</td><td>143.90 (n/a)</td><td>126.40 (n/a)</td><td>22.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 (+8.64%)</td><td>0.15 (-3.60%)</td><td>0.14 (-8.37%)</td><td>0.14 (-6.47%)</td><td>0.03 <b>(+56.43%)</b></td><td>179.90 (+6.89%)</td><td>164.40 (+5.66%)</td><td>176.20 (+9.10%)</td><td>113.60 (-7.94%)</td><td>28.54 <b>(+54.11%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>168.30 (n/a)</td><td>155.60 (n/a)</td><td>161.50 (n/a)</td><td>123.40 (n/a)</td><td>18.52 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (-8.97%)</td><td>0.13 (-15.15%)</td><td>0.13 (-18.82%)</td><td>0.08 <b>(-30.89%)</b></td><td>0.04 (+19.23%)</td><td>308.90 <b>(+44.68%)</b></td><td>196.36 <b>(+22.68%)</b></td><td>182.50 <b>(+23.23%)</b></td><td>139.70 (+9.83%)</td><td>66.05 <b>(+95.32%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.50 (n/a)</td><td>160.06 (n/a)</td><td>148.10 (n/a)</td><td>127.20 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (-0.65%)</td><td>0.13 (-14.68%)</td><td>0.15 (+2.27%)</td><td>0.08 <b>(-45.36%)</b></td><td>0.04 <b>(+83.22%)</b></td><td>322.30 <b>(+83.02%)</b></td><td>199.88 <b>(+26.62%)</b></td><td>165.20 (-2.25%)</td><td>131.80 (+0.61%)</td><td>74.64 <b>(+247.63%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>176.10 (n/a)</td><td>157.86 (n/a)</td><td>169.00 (n/a)</td><td>131.00 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (-17.08%)</td><td>0.11 <b>(-22.10%)</b></td><td>0.11 <b>(-20.40%)</b></td><td>0.07 <b>(-45.80%)</b></td><td>0.03 <b>(+64.80%)</b></td><td>369.40 <b>(+84.52%)</b></td><td>238.70 <b>(+35.01%)</b></td><td>218.30 <b>(+25.60%)</b></td><td>180.70 <b>(+20.63%)</b></td><td>74.80 <b>(+291.22%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>200.20 (n/a)</td><td>176.80 (n/a)</td><td>173.80 (n/a)</td><td>149.80 (n/a)</td><td>19.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 <b>(-42.89%)</b></td><td>0.11 <b>(-30.26%)</b></td><td>0.10 <b>(-37.85%)</b></td><td>0.10 <b>(+64.91%)</b></td><td>0.01 <b>(-82.93%)</b></td><td>243.40 <b>(-39.36%)</b></td><td>227.66 (+18.30%)</td><td>239.00 <b>(+60.83%)</b></td><td>198.10 <b>(+75.15%)</b></td><td>20.14 <b>(-83.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>401.40 (n/a)</td><td>192.44 (n/a)</td><td>148.60 (n/a)</td><td>113.10 (n/a)</td><td>118.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (-13.78%)</td><td>0.13 (-1.62%)</td><td>0.14 (-7.96%)</td><td>0.12 <b>(+35.33%)</b></td><td>0.01 <b>(-66.13%)</b></td><td>209.70 <b>(-26.11%)</b></td><td>184.48 (-5.77%)</td><td>179.40 (+8.66%)</td><td>159.80 (+16.05%)</td><td>19.26 <b>(-70.78%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>283.80 (n/a)</td><td>195.78 (n/a)</td><td>165.10 (n/a)</td><td>137.70 (n/a)</td><td>65.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (+2.89%)</td><td>0.13 (+1.15%)</td><td>0.13 (-1.89%)</td><td>0.11 (+8.37%)</td><td>0.02 <b>(-23.35%)</b></td><td>216.90 (-7.70%)</td><td>190.28 (-2.22%)</td><td>184.30 (+1.94%)</td><td>160.10 (-2.85%)</td><td>23.92 <b>(-29.84%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>235.00 (n/a)</td><td>194.60 (n/a)</td><td>180.80 (n/a)</td><td>164.80 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.37 (-3.04%)</td><td>0.28 (-13.29%)</td><td>0.27 (-15.15%)</td><td>0.18 <b>(-35.23%)</b></td><td>0.07 <b>(+84.64%)</b></td><td>271.70 <b>(+54.37%)</b></td><td>189.42 <b>(+21.36%)</b></td><td>180.00 (+17.80%)</td><td>133.80 (+3.16%)</td><td>55.08 <b>(+189.20%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>176.00 (n/a)</td><td>156.08 (n/a)</td><td>152.80 (n/a)</td><td>129.70 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.40 (+6.44%)</td><td>0.32 (-1.68%)</td><td>0.27 <b>(-20.10%)</b></td><td>0.25 (+13.53%)</td><td>0.07 (+12.97%)</td><td>194.40 (-11.92%)</td><td>161.54 (+1.79%)</td><td>179.10 <b>(+25.16%)</b></td><td>122.60 (-6.05%)</td><td>32.79 (-10.10%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>220.70 (n/a)</td><td>158.70 (n/a)</td><td>143.10 (n/a)</td><td>130.50 (n/a)</td><td>36.48 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.37 (-4.16%)</td><td>0.30 (+5.35%)</td><td>0.28 (+2.78%)</td><td>0.27 <b>(+30.49%)</b></td><td>0.04 <b>(-33.09%)</b></td><td>184.40 <b>(-23.36%)</b></td><td>165.50 (-7.46%)</td><td>173.60 (-2.69%)</td><td>133.00 (+4.40%)</td><td>21.80 <b>(-46.14%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>240.60 (n/a)</td><td>178.84 (n/a)</td><td>178.40 (n/a)</td><td>127.40 (n/a)</td><td>40.47 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.39 (+8.61%)</td><td>0.30 (-3.39%)</td><td>0.31 (-4.49%)</td><td>0.24 (-9.64%)</td><td>0.06 <b>(+55.71%)</b></td><td>206.90 (+10.70%)</td><td>167.90 (+5.39%)</td><td>156.30 (+4.69%)</td><td>127.20 (-7.96%)</td><td>32.39 <b>(+60.41%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>186.90 (n/a)</td><td>159.32 (n/a)</td><td>149.30 (n/a)</td><td>138.20 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.44 (+13.02%)</td><td>0.30 (-8.44%)</td><td>0.27 <b>(-21.93%)</b></td><td>0.22 (-12.64%)</td><td>0.08 <b>(+41.39%)</b></td><td>221.60 (+14.52%)</td><td>174.96 (+11.87%)</td><td>182.70 <b>(+28.03%)</b></td><td>112.70 (-11.54%)</td><td>40.32 <b>(+35.26%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>193.50 (n/a)</td><td>156.40 (n/a)</td><td>142.70 (n/a)</td><td>127.40 (n/a)</td><td>29.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.41 (-2.97%)</td><td>0.29 (-13.42%)</td><td>0.25 <b>(-30.07%)</b></td><td>0.19 (-6.16%)</td><td>0.09 (+5.46%)</td><td>255.40 (+6.59%)</td><td>183.20 (+16.67%)</td><td>197.00 <b>(+43.06%)</b></td><td>119.30 (+3.11%)</td><td>54.43 (+9.92%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.36 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>239.60 (n/a)</td><td>157.02 (n/a)</td><td>137.70 (n/a)</td><td>115.70 (n/a)</td><td>49.51 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.31 <b>(-25.39%)</b></td><td>0.26 (-14.45%)</td><td>0.27 (-13.58%)</td><td>0.22 (+15.37%)</td><td>0.04 <b>(-54.99%)</b></td><td>225.30 (-13.31%)</td><td>190.28 (+11.22%)</td><td>183.20 (+15.73%)</td><td>159.40 <b>(+34.06%)</b></td><td>26.83 <b>(-49.55%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.41 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>259.90 (n/a)</td><td>171.08 (n/a)</td><td>158.30 (n/a)</td><td>118.90 (n/a)</td><td>53.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (-16.66%)</td><td>0.24 <b>(-25.64%)</b></td><td>0.21 <b>(-35.34%)</b></td><td>0.18 <b>(-20.13%)</b></td><td>0.06 (-1.67%)</td><td>266.40 <b>(+25.25%)</b></td><td>215.42 <b>(+36.07%)</b></td><td>230.00 <b>(+54.57%)</b></td><td>153.50 <b>(+20.02%)</b></td><td>46.54 <b>(+42.57%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>212.70 (n/a)</td><td>158.32 (n/a)</td><td>148.80 (n/a)</td><td>127.90 (n/a)</td><td>32.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (+1.16%)</td><td>0.02 (+5.20%)</td><td>0.02 (+6.31%)</td><td>0.01 (+10.29%)</td><td>0.00 (-12.27%)</td><td>189.30 (-9.34%)</td><td>157.04 (-5.99%)</td><td>160.10 (-5.99%)</td><td>118.00 (-1.17%)</td><td>26.51 <b>(-21.69%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.80 (n/a)</td><td>167.04 (n/a)</td><td>170.30 (n/a)</td><td>119.40 (n/a)</td><td>33.85 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (+14.33%)</td><td>0.02 (+1.00%)</td><td>0.02 (+3.05%)</td><td>0.01 (-7.56%)</td><td>0.00 <b>(+82.37%)</b></td><td>190.70 (+8.17%)</td><td>162.30 (+0.93%)</td><td>159.70 (-2.98%)</td><td>121.60 (-12.52%)</td><td>29.41 <b>(+75.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>176.30 (n/a)</td><td>160.80 (n/a)</td><td>164.60 (n/a)</td><td>139.00 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (+11.12%)</td><td>0.02 (+11.74%)</td><td>0.02 (+14.54%)</td><td>0.02 (+16.44%)</td><td>0.00 (+0.92%)</td><td>173.70 (-14.09%)</td><td>137.20 (-11.14%)</td><td>131.00 (-12.72%)</td><td>108.00 (-10.00%)</td><td>26.11 <b>(-21.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>202.20 (n/a)</td><td>154.40 (n/a)</td><td>150.10 (n/a)</td><td>120.00 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (-4.92%)</td><td>0.02 (+2.21%)</td><td>0.02 (+16.40%)</td><td>0.01 (-7.01%)</td><td>0.00 (+10.39%)</td><td>202.10 (+7.56%)</td><td>159.76 (-1.20%)</td><td>147.50 (-14.09%)</td><td>127.70 (+5.19%)</td><td>33.84 <b>(+26.29%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>161.70 (n/a)</td><td>171.70 (n/a)</td><td>121.40 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (+14.16%)</td><td>0.02 (+12.54%)</td><td>0.02 (+17.92%)</td><td>0.01 <b>(-20.03%)</b></td><td>0.00 <b>(+97.32%)</b></td><td>255.30 <b>(+25.02%)</b></td><td>170.22 (-7.20%)</td><td>162.20 (-15.17%)</td><td>131.00 (-12.43%)</td><td>50.37 <b>(+116.50%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>204.20 (n/a)</td><td>183.42 (n/a)</td><td>191.20 (n/a)</td><td>149.60 (n/a)</td><td>23.27 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (-4.87%)</td><td>0.01 (+15.51%)</td><td>0.01 <b>(+41.46%)</b></td><td>0.01 <b>(+35.75%)</b></td><td>0.00 <b>(-42.61%)</b></td><td>225.60 <b>(-26.32%)</b></td><td>185.94 (-19.98%)</td><td>190.10 <b>(-29.30%)</b></td><td>149.80 (+5.12%)</td><td>34.37 <b>(-56.00%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>306.20 (n/a)</td><td>232.38 (n/a)</td><td>268.90 (n/a)</td><td>142.50 (n/a)</td><td>78.13 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (-3.20%)</td><td>0.02 (-5.00%)</td><td>0.02 (-1.94%)</td><td>0.01 (-12.11%)</td><td>0.00 <b>(+20.77%)</b></td><td>234.90 (+13.75%)</td><td>175.74 (+7.12%)</td><td>156.10 (+1.96%)</td><td>134.10 (+3.31%)</td><td>41.85 <b>(+42.27%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>206.50 (n/a)</td><td>164.06 (n/a)</td><td>153.10 (n/a)</td><td>129.80 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.01 (-18.05%)</td><td>0.01 <b>(-20.95%)</b></td><td>0.01 <b>(-25.95%)</b></td><td>0.01 (-10.00%)</td><td>0.00 <b>(-25.91%)</b></td><td>234.30 (+11.10%)</td><td>214.88 <b>(+25.98%)</b></td><td>231.30 <b>(+35.03%)</b></td><td>176.40 <b>(+22.08%)</b></td><td>25.64 (+0.68%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>210.90 (n/a)</td><td>170.56 (n/a)</td><td>171.30 (n/a)</td><td>144.50 (n/a)</td><td>25.47 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (+4.37%)</td><td>0.04 (+5.07%)</td><td>0.04 (+0.28%)</td><td>0.03 (+14.59%)</td><td>0.01 (-17.84%)</td><td>177.90 (-12.71%)</td><td>145.72 (-6.29%)</td><td>142.20 (-0.28%)</td><td>118.90 (-4.11%)</td><td>23.81 <b>(-30.71%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>155.50 (n/a)</td><td>142.60 (n/a)</td><td>124.00 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (-16.88%)</td><td>0.03 (-12.37%)</td><td>0.03 <b>(-22.20%)</b></td><td>0.02 (+13.47%)</td><td>0.00 <b>(-58.25%)</b></td><td>212.40 (-11.87%)</td><td>171.88 (+8.14%)</td><td>165.60 <b>(+28.57%)</b></td><td>149.40 <b>(+20.39%)</b></td><td>23.83 <b>(-53.02%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>241.00 (n/a)</td><td>158.94 (n/a)</td><td>128.80 (n/a)</td><td>124.10 (n/a)</td><td>50.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (-12.31%)</td><td>0.03 (-12.18%)</td><td>0.03 (-7.07%)</td><td>0.02 <b>(-24.79%)</b></td><td>0.01 <b>(+32.68%)</b></td><td>236.70 <b>(+32.98%)</b></td><td>173.20 (+16.19%)</td><td>156.70 (+7.62%)</td><td>144.00 (+14.10%)</td><td>37.72 <b>(+102.30%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>178.00 (n/a)</td><td>149.06 (n/a)</td><td>145.60 (n/a)</td><td>126.20 (n/a)</td><td>18.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (-1.58%)</td><td>0.03 (+9.28%)</td><td>0.03 (+19.94%)</td><td>0.02 (+12.14%)</td><td>0.01 (-7.03%)</td><td>228.10 (-10.83%)</td><td>178.64 (-9.13%)</td><td>161.40 (-16.63%)</td><td>148.70 (+1.57%)</td><td>34.05 (-15.97%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>255.80 (n/a)</td><td>196.58 (n/a)</td><td>193.60 (n/a)</td><td>146.40 (n/a)</td><td>40.52 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 <b>(+27.52%)</b></td><td>0.04 <b>(+23.02%)</b></td><td>0.03 (+13.19%)</td><td>0.03 (+10.06%)</td><td>0.01 <b>(+137.18%)</b></td><td>182.10 (-9.18%)</td><td>152.42 (-16.34%)</td><td>164.10 (-11.68%)</td><td>117.90 <b>(-21.61%)</b></td><td>32.28 <b>(+69.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.50 (n/a)</td><td>182.20 (n/a)</td><td>185.80 (n/a)</td><td>150.40 (n/a)</td><td>19.06 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (-11.29%)</td><td>0.03 (-7.04%)</td><td>0.03 (-13.44%)</td><td>0.02 (+5.47%)</td><td>0.00 <b>(-39.72%)</b></td><td>212.90 (-5.17%)</td><td>183.18 (+4.58%)</td><td>187.70 (+15.51%)</td><td>143.20 (+12.76%)</td><td>25.13 <b>(-39.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>175.16 (n/a)</td><td>162.50 (n/a)</td><td>127.00 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 <b>(-36.21%)</b></td><td>0.03 (-9.70%)</td><td>0.03 (-7.13%)</td><td>0.03 (+7.25%)</td><td>0.00 <b>(-71.96%)</b></td><td>202.80 (-6.76%)</td><td>168.86 (+3.43%)</td><td>159.50 (+7.62%)</td><td>156.00 <b>(+56.78%)</b></td><td>19.48 <b>(-59.28%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>163.26 (n/a)</td><td>148.20 (n/a)</td><td>99.50 (n/a)</td><td>47.84 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+6.17%)</td><td>0.03 (+2.16%)</td><td>0.02 (+4.23%)</td><td>0.02 (-3.45%)</td><td>0.00 <b>(+21.00%)</b></td><td>241.10 (+3.57%)</td><td>204.96 (-1.71%)</td><td>211.60 (-4.08%)</td><td>170.50 (-5.80%)</td><td>27.30 (+18.49%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.80 (n/a)</td><td>208.52 (n/a)</td><td>220.60 (n/a)</td><td>181.00 (n/a)</td><td>23.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 <b>(+30.18%)</b></td><td>0.07 (+14.39%)</td><td>0.07 (+13.92%)</td><td>0.05 (-2.59%)</td><td>0.01 <b>(+110.92%)</b></td><td>219.10 (+2.67%)</td><td>162.06 (-10.27%)</td><td>153.30 (-12.25%)</td><td>122.10 <b>(-23.21%)</b></td><td>36.13 <b>(+68.67%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>180.60 (n/a)</td><td>174.70 (n/a)</td><td>159.00 (n/a)</td><td>21.42 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 <b>(+29.84%)</b></td><td>0.07 <b>(+26.88%)</b></td><td>0.07 <b>(+31.67%)</b></td><td>0.06 <b>(+26.72%)</b></td><td>0.01 <b>(+47.85%)</b></td><td>189.60 <b>(-21.07%)</b></td><td>153.64 <b>(-20.73%)</b></td><td>146.40 <b>(-24.07%)</b></td><td>126.40 <b>(-22.97%)</b></td><td>26.65 (-10.25%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>240.20 (n/a)</td><td>193.82 (n/a)</td><td>192.80 (n/a)</td><td>164.10 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (-17.48%)</td><td>0.07 (-2.46%)</td><td>0.07 (+4.99%)</td><td>0.06 (-0.70%)</td><td>0.01 <b>(-49.23%)</b></td><td>182.60 (+0.72%)</td><td>156.24 (+1.09%)</td><td>152.80 (-4.74%)</td><td>141.50 <b>(+21.15%)</b></td><td>15.48 <b>(-34.17%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>154.56 (n/a)</td><td>160.40 (n/a)</td><td>116.80 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 <b>(+34.57%)</b></td><td>0.08 <b>(+45.88%)</b></td><td>0.07 <b>(+41.26%)</b></td><td>0.07 <b>(+45.14%)</b></td><td>0.01 <b>(+27.55%)</b></td><td>155.80 <b>(-31.12%)</b></td><td>135.78 <b>(-31.71%)</b></td><td>148.30 <b>(-29.21%)</b></td><td>108.10 <b>(-25.65%)</b></td><td>21.59 <b>(-33.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>198.84 (n/a)</td><td>209.50 (n/a)</td><td>145.40 (n/a)</td><td>32.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (-5.81%)</td><td>0.07 (+4.95%)</td><td>0.07 (+14.53%)</td><td>0.05 (-9.13%)</td><td>0.01 (-10.96%)</td><td>221.60 (+10.08%)</td><td>161.62 (-4.75%)</td><td>154.20 (-12.68%)</td><td>125.40 (+6.18%)</td><td>35.77 (+11.84%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>169.68 (n/a)</td><td>176.60 (n/a)</td><td>118.10 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (+7.98%)</td><td>0.07 (+6.69%)</td><td>0.07 (+0.61%)</td><td>0.06 (+19.19%)</td><td>0.01 (-15.81%)</td><td>173.90 (-16.11%)</td><td>156.90 (-7.17%)</td><td>156.80 (-0.63%)</td><td>128.90 (-7.40%)</td><td>17.89 <b>(-35.54%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>169.02 (n/a)</td><td>157.80 (n/a)</td><td>139.20 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (+5.49%)</td><td>0.07 (+6.13%)</td><td>0.07 (+2.08%)</td><td>0.06 <b>(+21.85%)</b></td><td>0.01 (-10.27%)</td><td>175.20 (-17.94%)</td><td>155.02 (-6.66%)</td><td>155.80 (-2.01%)</td><td>123.50 (-5.22%)</td><td>20.97 <b>(-30.95%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>166.08 (n/a)</td><td>159.00 (n/a)</td><td>130.30 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (-14.56%)</td><td>0.06 (+5.62%)</td><td>0.06 (+16.65%)</td><td>0.05 <b>(+35.88%)</b></td><td>0.01 <b>(-58.31%)</b></td><td>207.40 <b>(-26.43%)</b></td><td>184.96 (-9.24%)</td><td>176.70 (-14.26%)</td><td>166.60 (+17.08%)</td><td>18.67 <b>(-63.85%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>281.90 (n/a)</td><td>203.80 (n/a)</td><td>206.10 (n/a)</td><td>142.30 (n/a)</td><td>51.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (-8.16%)</td><td>0.15 (+0.89%)</td><td>0.15 (+7.90%)</td><td>0.12 (+14.22%)</td><td>0.02 <b>(-41.75%)</b></td><td>174.40 (-12.41%)</td><td>145.20 (-3.87%)</td><td>141.00 (-7.30%)</td><td>121.50 (+8.87%)</td><td>20.61 <b>(-43.07%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>199.10 (n/a)</td><td>151.04 (n/a)</td><td>152.10 (n/a)</td><td>111.60 (n/a)</td><td>36.21 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (+16.64%)</td><td>0.13 (+12.58%)</td><td>0.13 (+19.15%)</td><td>0.06 (-3.84%)</td><td>0.05 <b>(+26.39%)</b></td><td>349.20 (+3.99%)</td><td>185.58 (-7.12%)</td><td>160.40 (-16.06%)</td><td>116.90 (-14.30%)</td><td>94.18 (+17.25%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>335.80 (n/a)</td><td>199.80 (n/a)</td><td>191.10 (n/a)</td><td>136.40 (n/a)</td><td>80.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (-1.53%)</td><td>0.15 (+5.84%)</td><td>0.16 (+11.70%)</td><td>0.12 (+7.21%)</td><td>0.03 (-10.30%)</td><td>176.60 (-6.71%)</td><td>145.32 (-6.32%)</td><td>132.60 (-10.47%)</td><td>116.30 (+1.57%)</td><td>27.63 (-15.37%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>189.30 (n/a)</td><td>155.12 (n/a)</td><td>148.10 (n/a)</td><td>114.50 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (-10.55%)</td><td>0.13 (-6.39%)</td><td>0.13 (-0.89%)</td><td>0.10 (-2.08%)</td><td>0.02 <b>(-34.95%)</b></td><td>204.20 (+2.10%)</td><td>167.10 (+4.53%)</td><td>162.50 (+0.93%)</td><td>137.30 (+11.81%)</td><td>27.77 <b>(-24.19%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>200.00 (n/a)</td><td>159.86 (n/a)</td><td>161.00 (n/a)</td><td>122.80 (n/a)</td><td>36.63 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 <b>(+21.55%)</b></td><td>0.12 (-10.10%)</td><td>0.10 <b>(-26.10%)</b></td><td>0.08 <b>(-20.30%)</b></td><td>0.05 <b>(+90.70%)</b></td><td>255.60 <b>(+25.48%)</b></td><td>191.42 (+19.86%)</td><td>200.90 <b>(+35.38%)</b></td><td>102.40 (-17.68%)</td><td>60.60 <b>(+90.24%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>203.70 (n/a)</td><td>159.70 (n/a)</td><td>148.40 (n/a)</td><td>124.40 (n/a)</td><td>31.85 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (-2.40%)</td><td>0.14 (+3.79%)</td><td>0.14 (+2.01%)</td><td>0.12 (+18.91%)</td><td>0.02 <b>(-28.77%)</b></td><td>176.90 (-15.88%)</td><td>151.94 (-5.29%)</td><td>155.40 (-1.96%)</td><td>124.50 (+2.47%)</td><td>19.27 <b>(-39.94%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>210.30 (n/a)</td><td>160.42 (n/a)</td><td>158.50 (n/a)</td><td>121.50 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.16 (+7.62%)</td><td>0.13 (+2.33%)</td><td>0.12 (-13.44%)</td><td>0.10 (+9.51%)</td><td>0.03 (-9.23%)</td><td>215.40 (-8.69%)</td><td>172.92 (-3.69%)</td><td>179.40 (+15.52%)</td><td>127.80 (-7.05%)</td><td>32.30 <b>(-25.85%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>235.90 (n/a)</td><td>179.54 (n/a)</td><td>155.30 (n/a)</td><td>137.50 (n/a)</td><td>43.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 <b>(-33.55%)</b></td><td>0.09 (-16.21%)</td><td>0.10 (-2.53%)</td><td>0.06 <b>(-22.97%)</b></td><td>0.02 <b>(-39.34%)</b></td><td>344.60 <b>(+29.84%)</b></td><td>242.60 (+18.16%)</td><td>218.70 (+2.58%)</td><td>210.30 <b>(+50.43%)</b></td><td>57.28 <b>(+24.95%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>265.40 (n/a)</td><td>205.32 (n/a)</td><td>213.20 (n/a)</td><td>139.80 (n/a)</td><td>45.84 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>171.20 (n/a)</td><td>183.70 (n/a)</td><td>135.70 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>163.16 (n/a)</td><td>173.00 (n/a)</td><td>127.80 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.20 (n/a)</td><td>191.04 (n/a)</td><td>184.60 (n/a)</td><td>165.50 (n/a)</td><td>35.52 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.80 (n/a)</td><td>222.38 (n/a)</td><td>232.70 (n/a)</td><td>150.90 (n/a)</td><td>42.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>175.68 (n/a)</td><td>169.10 (n/a)</td><td>144.40 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>265.80 (n/a)</td><td>188.02 (n/a)</td><td>187.90 (n/a)</td><td>125.10 (n/a)</td><td>51.03 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>192.20 (n/a)</td><td>179.10 (n/a)</td><td>172.20 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>192.28 (n/a)</td><td>187.80 (n/a)</td><td>168.30 (n/a)</td><td>22.31 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>183.80 (n/a)</td><td>158.00 (n/a)</td><td>157.00 (n/a)</td><td>133.00 (n/a)</td><td>24.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>203.90 (n/a)</td><td>177.78 (n/a)</td><td>188.70 (n/a)</td><td>124.30 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>197.20 (n/a)</td><td>173.58 (n/a)</td><td>173.50 (n/a)</td><td>136.70 (n/a)</td><td>23.16 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>230.20 (n/a)</td><td>208.48 (n/a)</td><td>223.30 (n/a)</td><td>163.30 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.35 (-8.27%)</td><td>0.29 (-1.44%)</td><td>0.28 (-5.25%)</td><td>0.22 (-2.43%)</td><td>0.05 (-8.12%)</td><td>220.80 (+2.51%)</td><td>172.38 (+1.33%)</td><td>175.00 (+5.55%)</td><td>140.50 (+9.00%)</td><td>31.77 (+2.46%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>215.40 (n/a)</td><td>170.12 (n/a)</td><td>165.80 (n/a)</td><td>128.90 (n/a)</td><td>31.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>191.00 (n/a)</td><td>162.34 (n/a)</td><td>161.60 (n/a)</td><td>129.20 (n/a)</td><td>24.62 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>208.80 (n/a)</td><td>179.86 (n/a)</td><td>197.80 (n/a)</td><td>129.90 (n/a)</td><td>35.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>242.40 (n/a)</td><td>203.86 (n/a)</td><td>201.20 (n/a)</td><td>176.40 (n/a)</td><td>24.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>167.70 (n/a)</td><td>155.20 (n/a)</td><td>135.20 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>147.12 (n/a)</td><td>148.30 (n/a)</td><td>99.20 (n/a)</td><td>38.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>168.06 (n/a)</td><td>146.40 (n/a)</td><td>105.30 (n/a)</td><td>51.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>192.24 (n/a)</td><td>220.20 (n/a)</td><td>112.00 (n/a)</td><td>50.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>237.80 (n/a)</td><td>180.40 (n/a)</td><td>180.30 (n/a)</td><td>115.10 (n/a)</td><td>43.86 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>252.00 (n/a)</td><td>184.70 (n/a)</td><td>171.90 (n/a)</td><td>144.50 (n/a)</td><td>40.26 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>237.60 (n/a)</td><td>179.02 (n/a)</td><td>207.20 (n/a)</td><td>88.50 (n/a)</td><td>60.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>279.70 (n/a)</td><td>218.28 (n/a)</td><td>231.40 (n/a)</td><td>144.80 (n/a)</td><td>49.58 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.10 (n/a)</td><td>185.16 (n/a)</td><td>193.90 (n/a)</td><td>142.10 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>218.80 (n/a)</td><td>177.60 (n/a)</td><td>172.00 (n/a)</td><td>149.70 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>188.70 (n/a)</td><td>158.70 (n/a)</td><td>161.10 (n/a)</td><td>127.80 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>208.80 (n/a)</td><td>181.96 (n/a)</td><td>198.90 (n/a)</td><td>126.00 (n/a)</td><td>33.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>234.20 (n/a)</td><td>163.78 (n/a)</td><td>162.40 (n/a)</td><td>118.80 (n/a)</td><td>44.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>222.20 (n/a)</td><td>179.16 (n/a)</td><td>170.50 (n/a)</td><td>152.10 (n/a)</td><td>27.16 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>188.40 (n/a)</td><td>165.02 (n/a)</td><td>170.70 (n/a)</td><td>135.80 (n/a)</td><td>19.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>160.06 (n/a)</td><td>149.90 (n/a)</td><td>127.90 (n/a)</td><td>37.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.40 (n/a)</td><td>163.98 (n/a)</td><td>168.60 (n/a)</td><td>123.80 (n/a)</td><td>29.51 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.80 (n/a)</td><td>167.46 (n/a)</td><td>165.80 (n/a)</td><td>149.10 (n/a)</td><td>16.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.20 (n/a)</td><td>170.68 (n/a)</td><td>182.10 (n/a)</td><td>122.30 (n/a)</td><td>42.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.70 (n/a)</td><td>166.98 (n/a)</td><td>171.90 (n/a)</td><td>138.30 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.90 (n/a)</td><td>166.06 (n/a)</td><td>146.50 (n/a)</td><td>139.50 (n/a)</td><td>38.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.20 (n/a)</td><td>180.56 (n/a)</td><td>180.90 (n/a)</td><td>129.60 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>303.80 (n/a)</td><td>232.38 (n/a)</td><td>216.80 (n/a)</td><td>201.50 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>149.42 (n/a)</td><td>129.70 (n/a)</td><td>125.40 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.60 (n/a)</td><td>147.60 (n/a)</td><td>153.50 (n/a)</td><td>113.60 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>159.70 (n/a)</td><td>179.20 (n/a)</td><td>116.30 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>174.62 (n/a)</td><td>176.00 (n/a)</td><td>124.80 (n/a)</td><td>32.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>166.46 (n/a)</td><td>166.90 (n/a)</td><td>130.70 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>191.34 (n/a)</td><td>183.90 (n/a)</td><td>168.50 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>168.66 (n/a)</td><td>159.70 (n/a)</td><td>152.90 (n/a)</td><td>21.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.70 (n/a)</td><td>210.04 (n/a)</td><td>211.50 (n/a)</td><td>200.50 (n/a)</td><td>5.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.30 (n/a)</td><td>156.98 (n/a)</td><td>151.40 (n/a)</td><td>117.70 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>171.22 (n/a)</td><td>173.20 (n/a)</td><td>143.90 (n/a)</td><td>17.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>292.50 (n/a)</td><td>182.96 (n/a)</td><td>165.50 (n/a)</td><td>126.80 (n/a)</td><td>64.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>172.82 (n/a)</td><td>166.50 (n/a)</td><td>157.20 (n/a)</td><td>21.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>273.10 (n/a)</td><td>205.54 (n/a)</td><td>183.10 (n/a)</td><td>178.60 (n/a)</td><td>40.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.00 (n/a)</td><td>185.46 (n/a)</td><td>192.40 (n/a)</td><td>140.40 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.00 (n/a)</td><td>185.02 (n/a)</td><td>193.20 (n/a)</td><td>133.30 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>197.72 (n/a)</td><td>210.00 (n/a)</td><td>169.30 (n/a)</td><td>20.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>248.50 (n/a)</td><td>183.18 (n/a)</td><td>173.40 (n/a)</td><td>131.30 (n/a)</td><td>45.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>231.10 (n/a)</td><td>182.62 (n/a)</td><td>178.00 (n/a)</td><td>159.50 (n/a)</td><td>28.39 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.70 (n/a)</td><td>159.40 (n/a)</td><td>157.10 (n/a)</td><td>130.80 (n/a)</td><td>31.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>172.50 (n/a)</td><td>141.32 (n/a)</td><td>132.80 (n/a)</td><td>130.30 (n/a)</td><td>17.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>229.20 (n/a)</td><td>168.56 (n/a)</td><td>155.70 (n/a)</td><td>143.40 (n/a)</td><td>34.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>161.40 (n/a)</td><td>157.96 (n/a)</td><td>158.00 (n/a)</td><td>154.40 (n/a)</td><td>2.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.10 (n/a)</td><td>176.10 (n/a)</td><td>182.80 (n/a)</td><td>133.80 (n/a)</td><td>34.06 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>301.30 (n/a)</td><td>212.00 (n/a)</td><td>182.80 (n/a)</td><td>174.40 (n/a)</td><td>52.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>4.44 (-8.29%)</td><td>4.09 (-1.78%)</td><td>4.19 (+1.72%)</td><td>3.76 (-0.45%)</td><td>0.28 <b>(-33.89%)</b></td><td>2500.80 (+0.45%)</td><td>2308.92 (+1.41%)</td><td>2241.90 (-1.69%)</td><td>2119.50 (+9.04%)</td><td>158.18 <b>(-26.80%)</b></td><td>1745.41 (-8.29%)</td><td>1608.21 (-1.78%)</td><td>1650.08 (+1.72%)</td><td>1479.26 (-0.44%)</td><td>109.52 <b>(-33.89%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>4.84 (n/a)</td><td>4.16 (n/a)</td><td>4.12 (n/a)</td><td>3.78 (n/a)</td><td>0.42 (n/a)</td><td>2489.70 (n/a)</td><td>2276.84 (n/a)</td><td>2280.40 (n/a)</td><td>1943.70 (n/a)</td><td>216.10 (n/a)</td><td>1903.25 (n/a)</td><td>1637.32 (n/a)</td><td>1622.21 (n/a)</td><td>1485.87 (n/a)</td><td>165.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.92 (-14.87%)</td><td>0.76 (-19.29%)</td><td>0.73 <b>(-23.66%)</b></td><td>0.64 (-7.73%)</td><td>0.11 <b>(-28.78%)</b></td><td>343.90 (+8.38%)</td><td>296.36 <b>(+22.80%)</b></td><td>304.70 <b>(+31.00%)</b></td><td>240.40 (+17.44%)</td><td>41.18 (-10.01%)</td><td>39.25 (-14.87%)</td><td>32.37 (-19.29%)</td><td>30.97 <b>(-23.66%)</b></td><td>27.45 (-7.73%)</td><td>4.72 <b>(-28.78%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.08 (n/a)</td><td>0.94 (n/a)</td><td>0.95 (n/a)</td><td>0.70 (n/a)</td><td>0.16 (n/a)</td><td>317.30 (n/a)</td><td>241.34 (n/a)</td><td>232.60 (n/a)</td><td>204.70 (n/a)</td><td>45.76 (n/a)</td><td>46.11 (n/a)</td><td>40.10 (n/a)</td><td>40.57 (n/a)</td><td>29.74 (n/a)</td><td>6.63 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.49 <b>(+40.34%)</b></td><td>1.04 (+14.09%)</td><td>1.05 (+9.32%)</td><td>0.65 (+4.47%)</td><td>0.30 <b>(+73.64%)</b></td><td>342.50 (-4.28%)</td><td>227.38 (-9.32%)</td><td>211.40 (-8.52%)</td><td>148.60 <b>(-28.76%)</b></td><td>71.07 (+16.78%)</td><td>63.50 <b>(+40.34%)</b></td><td>44.57 (+14.09%)</td><td>44.65 (+9.32%)</td><td>27.55 (+4.47%)</td><td>12.86 <b>(+73.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.06 (n/a)</td><td>0.92 (n/a)</td><td>0.96 (n/a)</td><td>0.62 (n/a)</td><td>0.17 (n/a)</td><td>357.80 (n/a)</td><td>250.76 (n/a)</td><td>231.10 (n/a)</td><td>208.60 (n/a)</td><td>60.86 (n/a)</td><td>45.25 (n/a)</td><td>39.07 (n/a)</td><td>40.84 (n/a)</td><td>26.37 (n/a)</td><td>7.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.53 (+1.42%)</td><td>0.53 (+1.50%)</td><td>0.53 (+1.46%)</td><td>0.53 (+1.74%)</td><td>0.00 <b>(-48.33%)</b></td><td>47895.20 (-1.71%)</td><td>47824.58 (-1.48%)</td><td>47791.50 (-1.44%)</td><td>47779.90 (-1.40%)</td><td>54.66 <b>(-49.95%)</b></td><td>359.56 (+1.42%)</td><td>359.23 (+1.50%)</td><td>359.48 (+1.46%)</td><td>358.70 (+1.74%)</td><td>0.41 <b>(-48.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48728.90 (n/a)</td><td>48542.48 (n/a)</td><td>48489.90 (n/a)</td><td>48458.20 (n/a)</td><td>109.21 (n/a)</td><td>354.53 (n/a)</td><td>353.92 (n/a)</td><td>354.30 (n/a)</td><td>352.56 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 (-0.39%)</td><td>0.21 (+0.28%)</td><td>0.21 (+0.42%)</td><td>0.21 (+1.01%)</td><td>0.00 <b>(-26.17%)</b></td><td>119062.40 (-1.00%)</td><td>118038.30 (-0.29%)</td><td>118672.90 (-0.42%)</td><td>115245.00 (+0.39%)</td><td>1589.81 <b>(-26.56%)</b></td><td>149.07 (-0.39%)</td><td>145.57 (+0.28%)</td><td>144.77 (+0.42%)</td><td>144.29 (+1.01%)</td><td>1.99 <b>(-26.17%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120268.80 (n/a)</td><td>118379.04 (n/a)</td><td>119171.60 (n/a)</td><td>114792.00 (n/a)</td><td>2164.83 (n/a)</td><td>149.66 (n/a)</td><td>145.17 (n/a)</td><td>144.16 (n/a)</td><td>142.85 (n/a)</td><td>2.70 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.91 (+1.38%)</td><td>0.90 (+0.96%)</td><td>0.90 (+0.74%)</td><td>0.89 (+1.41%)</td><td>0.01 (-0.03%)</td><td>28155.80 (-1.39%)</td><td>27932.04 (-0.95%)</td><td>28006.20 (-0.74%)</td><td>27548.30 (-1.36%)</td><td>232.30 (-2.93%)</td><td>623.63 (+1.38%)</td><td>615.09 (+0.96%)</td><td>613.43 (+0.74%)</td><td>610.17 (+1.41%)</td><td>5.15 (-0.03%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28553.60 (n/a)</td><td>28199.94 (n/a)</td><td>28214.50 (n/a)</td><td>27928.50 (n/a)</td><td>239.31 (n/a)</td><td>615.14 (n/a)</td><td>609.25 (n/a)</td><td>608.90 (n/a)</td><td>601.67 (n/a)</td><td>5.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.66 (+3.51%)</td><td>3.63 (+4.14%)</td><td>3.64 (+3.05%)</td><td>3.57 (+7.09%)</td><td>0.04 <b>(-56.59%)</b></td><td>7041.70 (-6.62%)</td><td>6942.06 (-4.01%)</td><td>6916.80 (-2.96%)</td><td>6875.40 (-3.39%)</td><td>71.24 <b>(-60.84%)</b></td><td>2498.75 (+3.51%)</td><td>2474.96 (+4.14%)</td><td>2483.80 (+3.05%)</td><td>2439.73 (+7.09%)</td><td>25.29 <b>(-56.59%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.54 (n/a)</td><td>3.48 (n/a)</td><td>3.53 (n/a)</td><td>3.34 (n/a)</td><td>0.09 (n/a)</td><td>7540.80 (n/a)</td><td>7232.20 (n/a)</td><td>7127.80 (n/a)</td><td>7116.80 (n/a)</td><td>181.93 (n/a)</td><td>2413.99 (n/a)</td><td>2376.64 (n/a)</td><td>2410.28 (n/a)</td><td>2278.24 (n/a)</td><td>58.27 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>2.88 (-5.21%)</td><td>2.86 (-0.41%)</td><td>2.87 (+1.06%)</td><td>2.82 (+0.03%)</td><td>0.02 <b>(-73.67%)</b></td><td>8929.30 (-0.03%)</td><td>8797.16 (+0.34%)</td><td>8775.60 (-1.05%)</td><td>8740.60 (+5.50%)</td><td>75.65 <b>(-72.07%)</b></td><td>1965.53 (-5.21%)</td><td>1953.00 (-0.41%)</td><td>1957.69 (+1.06%)</td><td>1923.99 (+0.03%)</td><td>16.63 <b>(-73.67%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.04 (n/a)</td><td>2.87 (n/a)</td><td>2.84 (n/a)</td><td>2.82 (n/a)</td><td>0.09 (n/a)</td><td>8931.60 (n/a)</td><td>8767.14 (n/a)</td><td>8868.90 (n/a)</td><td>8285.10 (n/a)</td><td>270.89 (n/a)</td><td>2073.59 (n/a)</td><td>1961.13 (n/a)</td><td>1937.10 (n/a)</td><td>1923.49 (n/a)</td><td>63.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.34 (+1.19%)</td><td>3.22 (+0.40%)</td><td>3.19 (-0.23%)</td><td>3.12 (-0.95%)</td><td>0.09 <b>(+44.56%)</b></td><td>8062.50 (+0.96%)</td><td>7825.28 (-0.37%)</td><td>7896.40 (+0.23%)</td><td>7524.00 (-1.18%)</td><td>207.84 <b>(+44.38%)</b></td><td>2283.34 (+1.19%)</td><td>2196.68 (+0.40%)</td><td>2175.65 (-0.23%)</td><td>2130.83 (-0.95%)</td><td>58.99 <b>(+44.56%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.31 (n/a)</td><td>3.21 (n/a)</td><td>3.19 (n/a)</td><td>3.15 (n/a)</td><td>0.06 (n/a)</td><td>7985.80 (n/a)</td><td>7854.12 (n/a)</td><td>7878.60 (n/a)</td><td>7613.70 (n/a)</td><td>143.96 (n/a)</td><td>2256.45 (n/a)</td><td>2187.98 (n/a)</td><td>2180.59 (n/a)</td><td>2151.31 (n/a)</td><td>40.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.80 (+1.40%)</td><td>0.80 (+1.41%)</td><td>0.80 (+1.43%)</td><td>0.80 (+1.43%)</td><td>0.00 <b>(-45.34%)</b></td><td>94803.80 (-1.41%)</td><td>94791.32 (-1.39%)</td><td>94790.70 (-1.41%)</td><td>94770.90 (-1.38%)</td><td>12.84 <b>(-46.79%)</b></td><td>725.11 (+1.40%)</td><td>724.96 (+1.41%)</td><td>724.96 (+1.43%)</td><td>724.86 (+1.43%)</td><td>0.10 <b>(-45.35%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>96155.90 (n/a)</td><td>96131.64 (n/a)</td><td>96143.30 (n/a)</td><td>96097.90 (n/a)</td><td>24.14 (n/a)</td><td>715.10 (n/a)</td><td>714.85 (n/a)</td><td>714.76 (n/a)</td><td>714.67 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.73 (-0.29%)</td><td>0.73 (-0.00%)</td><td>0.73 (+0.01%)</td><td>0.73 (+0.15%)</td><td>0.00 <b>(-77.02%)</b></td><td>103403.40 (-0.15%)</td><td>103317.64 (+0.00%)</td><td>103301.80 (-0.01%)</td><td>103272.90 (+0.29%)</td><td>50.58 <b>(-76.98%)</b></td><td>665.42 (-0.29%)</td><td>665.13 (-0.00%)</td><td>665.23 (+0.01%)</td><td>664.58 (+0.15%)</td><td>0.33 <b>(-77.02%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103559.40 (n/a)</td><td>103314.98 (n/a)</td><td>103307.10 (n/a)</td><td>102971.20 (n/a)</td><td>219.71 (n/a)</td><td>667.37 (n/a)</td><td>665.15 (n/a)</td><td>665.20 (n/a)</td><td>663.58 (n/a)</td><td>1.42 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.69 (-0.88%)</td><td>0.69 (-1.14%)</td><td>0.69 (-1.17%)</td><td>0.68 (-1.48%)</td><td>0.00 <b>(+136.08%)</b></td><td>110624.80 (+1.50%)</td><td>110052.98 (+1.15%)</td><td>110068.60 (+1.19%)</td><td>109462.70 (+0.89%)</td><td>486.97 <b>(+141.72%)</b></td><td>627.79 (-0.88%)</td><td>624.43 (-1.14%)</td><td>624.33 (-1.17%)</td><td>621.19 (-1.48%)</td><td>2.76 <b>(+136.09%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108984.60 (n/a)</td><td>108800.78 (n/a)</td><td>108776.80 (n/a)</td><td>108495.90 (n/a)</td><td>201.46 (n/a)</td><td>633.38 (n/a)</td><td>631.61 (n/a)</td><td>631.75 (n/a)</td><td>630.54 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.01 (+8.91%)</td><td>7.22 (+12.09%)</td><td>7.11 (+6.37%)</td><td>6.72 <b>(+37.83%)</b></td><td>0.48 <b>(-49.49%)</b></td><td>1326.20 <b>(-27.45%)</b></td><td>1238.34 (-12.28%)</td><td>1253.90 (-5.98%)</td><td>1113.00 (-8.18%)</td><td>77.80 <b>(-67.84%)</b></td><td>482.37 (+8.91%)</td><td>434.98 (+12.09%)</td><td>428.17 (+6.37%)</td><td>404.82 <b>(+37.83%)</b></td><td>28.69 <b>(-49.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.35 (n/a)</td><td>6.44 (n/a)</td><td>6.68 (n/a)</td><td>4.88 (n/a)</td><td>0.94 (n/a)</td><td>1827.90 (n/a)</td><td>1411.62 (n/a)</td><td>1333.70 (n/a)</td><td>1212.20 (n/a)</td><td>241.90 (n/a)</td><td>442.90 (n/a)</td><td>388.07 (n/a)</td><td>402.54 (n/a)</td><td>293.72 (n/a)</td><td>56.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.91 (-2.30%)</td><td>6.67 (+2.49%)</td><td>6.76 (+0.18%)</td><td>6.43 (+11.95%)</td><td>0.22 <b>(-60.68%)</b></td><td>1386.20 (-10.68%)</td><td>1336.68 (-2.97%)</td><td>1318.40 (-0.18%)</td><td>1290.70 (+2.36%)</td><td>45.41 <b>(-63.82%)</b></td><td>415.95 (-2.30%)</td><td>402.01 (+2.49%)</td><td>407.23 (+0.18%)</td><td>387.29 (+11.95%)</td><td>13.55 <b>(-60.68%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.07 (n/a)</td><td>6.51 (n/a)</td><td>6.75 (n/a)</td><td>5.74 (n/a)</td><td>0.57 (n/a)</td><td>1551.90 (n/a)</td><td>1377.56 (n/a)</td><td>1320.80 (n/a)</td><td>1261.00 (n/a)</td><td>125.53 (n/a)</td><td>425.76 (n/a)</td><td>392.24 (n/a)</td><td>406.48 (n/a)</td><td>345.95 (n/a)</td><td>34.46 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>7.20 (+4.74%)</td><td>6.27 (+3.48%)</td><td>6.55 (+5.92%)</td><td>4.73 (+3.36%)</td><td>0.93 (+6.11%)</td><td>1884.10 (-3.25%)</td><td>1452.28 (-3.28%)</td><td>1359.80 (-5.60%)</td><td>1237.00 (-4.53%)</td><td>251.98 (-1.96%)</td><td>433.99 (+4.74%)</td><td>377.42 (+3.48%)</td><td>394.80 (+5.92%)</td><td>284.95 (+3.36%)</td><td>56.13 (+6.11%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>6.88 (n/a)</td><td>6.06 (n/a)</td><td>6.19 (n/a)</td><td>4.58 (n/a)</td><td>0.88 (n/a)</td><td>1947.40 (n/a)</td><td>1501.60 (n/a)</td><td>1440.40 (n/a)</td><td>1295.70 (n/a)</td><td>257.01 (n/a)</td><td>414.34 (n/a)</td><td>364.74 (n/a)</td><td>372.73 (n/a)</td><td>275.68 (n/a)</td><td>52.90 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.22 (+2.98%)</td><td>8.13 (+4.48%)</td><td>8.14 (+3.20%)</td><td>8.01 (+10.91%)</td><td>0.09 <b>(-71.69%)</b></td><td>4351.70 (-9.84%)</td><td>4289.94 (-4.41%)</td><td>4284.00 (-3.10%)</td><td>4239.60 (-2.89%)</td><td>47.68 <b>(-75.32%)</b></td><td>506.52 (+2.98%)</td><td>500.63 (+4.48%)</td><td>501.29 (+3.20%)</td><td>493.48 (+10.91%)</td><td>5.55 <b>(-71.69%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.99 (n/a)</td><td>7.78 (n/a)</td><td>7.89 (n/a)</td><td>7.22 (n/a)</td><td>0.32 (n/a)</td><td>4826.50 (n/a)</td><td>4487.98 (n/a)</td><td>4421.20 (n/a)</td><td>4365.80 (n/a)</td><td>193.17 (n/a)</td><td>491.88 (n/a)</td><td>479.17 (n/a)</td><td>485.72 (n/a)</td><td>444.93 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>7.60 (-4.74%)</td><td>7.43 (-2.71%)</td><td>7.59 (+0.19%)</td><td>6.90 (-8.13%)</td><td>0.30 <b>(+57.70%)</b></td><td>5049.40 (+8.85%)</td><td>4696.68 (+2.88%)</td><td>4595.40 (-0.19%)</td><td>4587.20 (+4.97%)</td><td>199.77 <b>(+81.27%)</b></td><td>468.14 (-4.74%)</td><td>457.86 (-2.71%)</td><td>467.31 (+0.19%)</td><td>425.30 (-8.13%)</td><td>18.49 <b>(+57.70%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.98 (n/a)</td><td>7.64 (n/a)</td><td>7.57 (n/a)</td><td>7.52 (n/a)</td><td>0.19 (n/a)</td><td>4638.70 (n/a)</td><td>4565.14 (n/a)</td><td>4604.30 (n/a)</td><td>4369.90 (n/a)</td><td>110.21 (n/a)</td><td>491.43 (n/a)</td><td>470.64 (n/a)</td><td>466.41 (n/a)</td><td>462.95 (n/a)</td><td>11.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>7.80 (+0.34%)</td><td>7.51 (+5.99%)</td><td>7.52 (+10.95%)</td><td>6.94 (+3.36%)</td><td>0.35 <b>(-26.91%)</b></td><td>5021.10 (-3.25%)</td><td>4651.92 (-5.82%)</td><td>4638.40 (-9.87%)</td><td>4468.40 (-0.33%)</td><td>225.20 <b>(-30.05%)</b></td><td>480.60 (+0.34%)</td><td>462.47 (+5.99%)</td><td>462.98 (+10.95%)</td><td>427.69 (+3.36%)</td><td>21.55 <b>(-26.91%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.78 (n/a)</td><td>7.08 (n/a)</td><td>6.77 (n/a)</td><td>6.72 (n/a)</td><td>0.48 (n/a)</td><td>5189.80 (n/a)</td><td>4939.14 (n/a)</td><td>5146.40 (n/a)</td><td>4483.40 (n/a)</td><td>321.95 (n/a)</td><td>478.98 (n/a)</td><td>436.33 (n/a)</td><td>417.28 (n/a)</td><td>413.79 (n/a)</td><td>29.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.80 (+1.43%)</td><td>0.80 (+1.47%)</td><td>0.80 (+1.44%)</td><td>0.80 (+1.49%)</td><td>0.00 <b>(-49.18%)</b></td><td>94132.60 (-1.47%)</td><td>94066.16 (-1.45%)</td><td>94052.30 (-1.42%)</td><td>94043.70 (-1.41%)</td><td>37.52 <b>(-50.63%)</b></td><td>730.72 (+1.43%)</td><td>730.54 (+1.47%)</td><td>730.65 (+1.44%)</td><td>730.03 (+1.49%)</td><td>0.29 <b>(-49.18%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95537.40 (n/a)</td><td>95449.74 (n/a)</td><td>95406.80 (n/a)</td><td>95388.40 (n/a)</td><td>76.00 (n/a)</td><td>720.42 (n/a)</td><td>719.95 (n/a)</td><td>720.28 (n/a)</td><td>719.29 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.74 (-0.35%)</td><td>0.74 (-0.09%)</td><td>0.74 (-0.01%)</td><td>0.73 (-0.09%)</td><td>0.00 <b>(-53.43%)</b></td><td>102771.50 (+0.09%)</td><td>102615.00 (+0.09%)</td><td>102592.60 (+0.01%)</td><td>102552.40 (+0.36%)</td><td>89.95 <b>(-53.20%)</b></td><td>670.09 (-0.35%)</td><td>669.68 (-0.09%)</td><td>669.83 (-0.01%)</td><td>668.66 (-0.09%)</td><td>0.59 <b>(-53.43%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102678.60 (n/a)</td><td>102524.20 (n/a)</td><td>102583.00 (n/a)</td><td>102188.50 (n/a)</td><td>192.20 (n/a)</td><td>672.48 (n/a)</td><td>670.28 (n/a)</td><td>669.89 (n/a)</td><td>669.27 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.71 (+1.33%)</td><td>0.71 (+1.23%)</td><td>0.71 (+1.25%)</td><td>0.71 (+1.15%)</td><td>0.00 <b>(+322.53%)</b></td><td>106155.80 (-1.14%)</td><td>106042.76 (-1.22%)</td><td>106033.50 (-1.23%)</td><td>105920.00 (-1.31%)</td><td>97.96 <b>(+312.26%)</b></td><td>648.79 (+1.33%)</td><td>648.04 (+1.23%)</td><td>648.09 (+1.25%)</td><td>647.35 (+1.15%)</td><td>0.60 <b>(+322.50%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107381.30 (n/a)</td><td>107350.58 (n/a)</td><td>107355.70 (n/a)</td><td>107325.00 (n/a)</td><td>23.76 (n/a)</td><td>640.29 (n/a)</td><td>640.14 (n/a)</td><td>640.11 (n/a)</td><td>639.96 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.80 (-9.54%)</td><td>3.54 (+0.72%)</td><td>3.66 (+1.22%)</td><td>3.23 (+7.21%)</td><td>0.28 <b>(-41.07%)</b></td><td>2496.30 (-6.72%)</td><td>2290.22 (-1.62%)</td><td>2205.00 (-1.21%)</td><td>2120.50 (+10.55%)</td><td>185.13 <b>(-39.38%)</b></td><td>996.88 (-9.54%)</td><td>927.76 (+0.72%)</td><td>958.69 (+1.22%)</td><td>846.83 (+7.21%)</td><td>73.30 <b>(-41.07%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>4.20 (n/a)</td><td>3.51 (n/a)</td><td>3.61 (n/a)</td><td>3.01 (n/a)</td><td>0.47 (n/a)</td><td>2676.20 (n/a)</td><td>2327.84 (n/a)</td><td>2231.90 (n/a)</td><td>1918.20 (n/a)</td><td>305.37 (n/a)</td><td>1102.03 (n/a)</td><td>921.10 (n/a)</td><td>947.16 (n/a)</td><td>789.90 (n/a)</td><td>124.39 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.40 (-16.56%)</td><td>0.35 (+0.14%)</td><td>0.36 (+8.08%)</td><td>0.30 (+8.46%)</td><td>0.04 <b>(-42.75%)</b></td><td>4112.20 (-7.80%)</td><td>3602.30 (-2.14%)</td><td>3491.80 (-7.48%)</td><td>3081.30 (+19.85%)</td><td>465.11 <b>(-32.30%)</b></td><td>21.78 (-16.56%)</td><td>18.88 (+0.14%)</td><td>19.22 (+8.08%)</td><td>16.32 (+8.46%)</td><td>2.42 <b>(-42.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.08 (n/a)</td><td>4460.00 (n/a)</td><td>3681.18 (n/a)</td><td>3774.00 (n/a)</td><td>2570.90 (n/a)</td><td>687.04 (n/a)</td><td>26.10 (n/a)</td><td>18.85 (n/a)</td><td>17.78 (n/a)</td><td>15.05 (n/a)</td><td>4.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.38 (+9.19%)</td><td>4.35 (+7.48%)</td><td>4.50 <b>(+23.80%)</b></td><td>3.39 (-2.66%)</td><td>0.81 <b>(+22.71%)</b></td><td>1963.40 (+2.73%)</td><td>1571.54 (-6.18%)</td><td>1477.30 (-19.23%)</td><td>1236.50 (-8.42%)</td><td>298.93 (+16.86%)</td><td>1662.12 (+9.19%)</td><td>1345.49 (+7.48%)</td><td>1391.20 <b>(+23.80%)</b></td><td>1046.78 (-2.66%)</td><td>249.80 <b>(+22.71%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>4.93 (n/a)</td><td>4.05 (n/a)</td><td>3.64 (n/a)</td><td>3.48 (n/a)</td><td>0.66 (n/a)</td><td>1911.20 (n/a)</td><td>1675.02 (n/a)</td><td>1829.00 (n/a)</td><td>1350.20 (n/a)</td><td>255.81 (n/a)</td><td>1522.16 (n/a)</td><td>1251.81 (n/a)</td><td>1123.70 (n/a)</td><td>1075.36 (n/a)</td><td>203.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.21 (n/a)</td><td>12.42 (n/a)</td><td>12.24 (n/a)</td><td>11.46 (n/a)</td><td>0.76 (n/a)</td><td>13.20 (n/a)</td><td>12.41 (n/a)</td><td>12.23 (n/a)</td><td>11.45 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>24.82 (-1.58%)</td><td>23.08 (-5.83%)</td><td>23.96 (-4.38%)</td><td>19.02 (-15.28%)</td><td>2.32 <b>(+98.29%)</b></td><td>24.80 (-1.58%)</td><td>23.06 (-5.83%)</td><td>23.95 (-4.38%)</td><td>19.01 (-15.28%)</td><td>2.32 <b>(+98.29%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>25.21 (n/a)</td><td>24.51 (n/a)</td><td>25.06 (n/a)</td><td>22.45 (n/a)</td><td>1.17 (n/a)</td><td>25.20 (n/a)</td><td>24.49 (n/a)</td><td>25.05 (n/a)</td><td>22.44 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>41.40 (-2.71%)</td><td>37.23 (-11.02%)</td><td>39.58 (-5.51%)</td><td>26.36 <b>(-35.23%)</b></td><td>6.25 <b>(+710.51%)</b></td><td>41.38 (-2.71%)</td><td>37.20 (-11.02%)</td><td>39.55 (-5.51%)</td><td>26.35 <b>(-35.23%)</b></td><td>6.25 <b>(+710.51%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>42.56 (n/a)</td><td>41.84 (n/a)</td><td>41.89 (n/a)</td><td>40.70 (n/a)</td><td>0.77 (n/a)</td><td>42.53 (n/a)</td><td>41.81 (n/a)</td><td>41.86 (n/a)</td><td>40.68 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>44.54 (-3.46%)</td><td>41.68 (-3.41%)</td><td>42.00 (-7.67%)</td><td>37.64 (+9.33%)</td><td>2.50 <b>(-49.64%)</b></td><td>44.51 (-3.46%)</td><td>41.65 (-3.41%)</td><td>41.98 (-7.67%)</td><td>37.62 (+9.33%)</td><td>2.50 <b>(-49.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>46.13 (n/a)</td><td>43.15 (n/a)</td><td>45.49 (n/a)</td><td>34.43 (n/a)</td><td>4.97 (n/a)</td><td>46.10 (n/a)</td><td>43.12 (n/a)</td><td>45.46 (n/a)</td><td>34.41 (n/a)</td><td>4.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.11 (n/a)</td><td>11.50 (n/a)</td><td>11.34 (n/a)</td><td>10.51 (n/a)</td><td>1.07 (n/a)</td><td>13.10 (n/a)</td><td>11.49 (n/a)</td><td>11.33 (n/a)</td><td>10.51 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>25.05 (-0.68%)</td><td>24.62 (-1.02%)</td><td>24.75 (-0.97%)</td><td>23.99 (-1.89%)</td><td>0.39 <b>(+34.47%)</b></td><td>25.03 (-0.68%)</td><td>24.61 (-1.02%)</td><td>24.73 (-0.97%)</td><td>23.98 (-1.89%)</td><td>0.39 <b>(+34.47%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>25.22 (n/a)</td><td>24.88 (n/a)</td><td>24.99 (n/a)</td><td>24.45 (n/a)</td><td>0.29 (n/a)</td><td>25.20 (n/a)</td><td>24.86 (n/a)</td><td>24.97 (n/a)</td><td>24.44 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>42.14 (-2.34%)</td><td>39.40 (-5.31%)</td><td>39.42 (-5.39%)</td><td>35.64 (-11.10%)</td><td>2.56 <b>(+109.64%)</b></td><td>42.11 (-2.34%)</td><td>39.37 (-5.31%)</td><td>39.40 (-5.39%)</td><td>35.62 (-11.10%)</td><td>2.56 <b>(+109.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>43.15 (n/a)</td><td>41.60 (n/a)</td><td>41.67 (n/a)</td><td>40.09 (n/a)</td><td>1.22 (n/a)</td><td>43.12 (n/a)</td><td>41.58 (n/a)</td><td>41.64 (n/a)</td><td>40.07 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>44.50 (-7.99%)</td><td>41.85 (-8.04%)</td><td>41.27 (-8.77%)</td><td>40.60 (-7.32%)</td><td>1.63 (-11.25%)</td><td>44.47 (-7.99%)</td><td>41.83 (-8.04%)</td><td>41.24 (-8.77%)</td><td>40.57 (-7.32%)</td><td>1.63 (-11.25%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>48.36 (n/a)</td><td>45.51 (n/a)</td><td>45.23 (n/a)</td><td>43.80 (n/a)</td><td>1.84 (n/a)</td><td>48.33 (n/a)</td><td>45.48 (n/a)</td><td>45.20 (n/a)</td><td>43.77 (n/a)</td><td>1.84 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>9.89 (+5.69%)</td><td>9.10 (+2.33%)</td><td>9.39 (+4.16%)</td><td>7.64 (-5.51%)</td><td>0.94 <b>(+78.09%)</b></td><td>9.87 (+5.69%)</td><td>9.09 (+2.33%)</td><td>9.37 (+4.16%)</td><td>7.63 (-5.51%)</td><td>0.94 <b>(+78.09%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.36 (n/a)</td><td>8.90 (n/a)</td><td>9.01 (n/a)</td><td>8.09 (n/a)</td><td>0.53 (n/a)</td><td>9.34 (n/a)</td><td>8.88 (n/a)</td><td>8.99 (n/a)</td><td>8.07 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.01 (-6.90%)</td><td>0.91 (-2.70%)</td><td>0.90 (-4.79%)</td><td>0.81 (+16.41%)</td><td>0.08 <b>(-48.13%)</b></td><td>1.00 (-6.90%)</td><td>0.89 (-2.70%)</td><td>0.89 (-4.79%)</td><td>0.80 (+16.41%)</td><td>0.08 <b>(-48.13%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.09 (n/a)</td><td>0.93 (n/a)</td><td>0.95 (n/a)</td><td>0.70 (n/a)</td><td>0.16 (n/a)</td><td>1.07 (n/a)</td><td>0.92 (n/a)</td><td>0.93 (n/a)</td><td>0.68 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.36 (-11.07%)</td><td>1.16 (-6.62%)</td><td>1.17 (+4.23%)</td><td>1.00 (-4.60%)</td><td>0.13 <b>(-41.00%)</b></td><td>1.35 (-11.07%)</td><td>1.15 (-6.62%)</td><td>1.16 (+4.23%)</td><td>0.99 (-4.60%)</td><td>0.13 <b>(-41.00%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.53 (n/a)</td><td>1.25 (n/a)</td><td>1.13 (n/a)</td><td>1.05 (n/a)</td><td>0.22 (n/a)</td><td>1.51 (n/a)</td><td>1.23 (n/a)</td><td>1.11 (n/a)</td><td>1.03 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>19.00 (+5.46%)</td><td>16.55 (+0.24%)</td><td>17.05 (-1.64%)</td><td>13.69 (+7.12%)</td><td>1.95 (-8.80%)</td><td>18.78 (+5.46%)</td><td>16.35 (+0.24%)</td><td>16.85 (-1.64%)</td><td>13.53 (+7.12%)</td><td>1.93 (-8.80%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>18.02 (n/a)</td><td>16.51 (n/a)</td><td>17.33 (n/a)</td><td>12.78 (n/a)</td><td>2.14 (n/a)</td><td>17.81 (n/a)</td><td>16.32 (n/a)</td><td>17.13 (n/a)</td><td>12.63 (n/a)</td><td>2.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.67 (-1.29%)</td><td>13.12 (+6.88%)</td><td>13.51 (-0.03%)</td><td>12.21 <b>(+62.77%)</b></td><td>0.70 <b>(-74.20%)</b></td><td>13.43 (-1.29%)</td><td>12.89 (+6.88%)</td><td>13.28 (-0.03%)</td><td>11.99 <b>(+62.77%)</b></td><td>0.68 <b>(-74.20%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.85 (n/a)</td><td>12.28 (n/a)</td><td>13.52 (n/a)</td><td>7.50 (n/a)</td><td>2.70 (n/a)</td><td>13.61 (n/a)</td><td>12.06 (n/a)</td><td>13.28 (n/a)</td><td>7.37 (n/a)</td><td>2.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>9.00 (+4.48%)</td><td>7.93 (+1.57%)</td><td>8.00 (+5.29%)</td><td>6.59 (-12.68%)</td><td>0.86 <b>(+89.31%)</b></td><td>8.84 (+4.48%)</td><td>7.79 (+1.57%)</td><td>7.86 (+5.29%)</td><td>6.47 (-12.68%)</td><td>0.85 <b>(+89.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>8.61 (n/a)</td><td>7.80 (n/a)</td><td>7.59 (n/a)</td><td>7.54 (n/a)</td><td>0.46 (n/a)</td><td>8.46 (n/a)</td><td>7.67 (n/a)</td><td>7.46 (n/a)</td><td>7.41 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.94 (+6.67%)</td><td>5.92 (+6.17%)</td><td>5.81 (+8.70%)</td><td>5.04 (+7.86%)</td><td>0.88 (+19.07%)</td><td>6.83 (+6.67%)</td><td>5.83 (+6.17%)</td><td>5.71 (+8.70%)</td><td>4.96 (+7.86%)</td><td>0.86 (+19.07%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>6.51 (n/a)</td><td>5.58 (n/a)</td><td>5.34 (n/a)</td><td>4.67 (n/a)</td><td>0.74 (n/a)</td><td>6.40 (n/a)</td><td>5.49 (n/a)</td><td>5.26 (n/a)</td><td>4.60 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.47 (n/a)</td><td>13.11 (n/a)</td><td>13.24 (n/a)</td><td>12.33 (n/a)</td><td>0.45 (n/a)</td><td>13.46 (n/a)</td><td>13.10 (n/a)</td><td>13.24 (n/a)</td><td>12.32 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.57 (n/a)</td><td>13.20 (n/a)</td><td>13.25 (n/a)</td><td>12.67 (n/a)</td><td>0.33 (n/a)</td><td>13.56 (n/a)</td><td>13.19 (n/a)</td><td>13.24 (n/a)</td><td>12.66 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.80 (n/a)</td><td>153.14 (n/a)</td><td>151.60 (n/a)</td><td>121.50 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>147.36 (n/a)</td><td>137.20 (n/a)</td><td>116.30 (n/a)</td><td>28.95 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>165.00 (n/a)</td><td>178.20 (n/a)</td><td>104.70 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.30 (n/a)</td><td>185.68 (n/a)</td><td>198.30 (n/a)</td><td>139.90 (n/a)</td><td>28.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.80 (n/a)</td><td>175.74 (n/a)</td><td>167.80 (n/a)</td><td>148.10 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>340.20 (n/a)</td><td>214.86 (n/a)</td><td>181.80 (n/a)</td><td>176.70 (n/a)</td><td>70.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.70 (n/a)</td><td>175.74 (n/a)</td><td>184.80 (n/a)</td><td>136.30 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.10 (n/a)</td><td>201.10 (n/a)</td><td>206.70 (n/a)</td><td>182.10 (n/a)</td><td>12.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.30 (n/a)</td><td>173.02 (n/a)</td><td>176.50 (n/a)</td><td>137.80 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>185.56 (n/a)</td><td>196.30 (n/a)</td><td>155.80 (n/a)</td><td>23.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>277.20 (n/a)</td><td>206.36 (n/a)</td><td>190.20 (n/a)</td><td>136.40 (n/a)</td><td>59.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>264.40 (n/a)</td><td>190.12 (n/a)</td><td>179.40 (n/a)</td><td>146.60 (n/a)</td><td>44.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>184.60 (n/a)</td><td>193.10 (n/a)</td><td>162.90 (n/a)</td><td>20.08 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.10 (n/a)</td><td>184.26 (n/a)</td><td>196.00 (n/a)</td><td>143.60 (n/a)</td><td>24.27 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>179.36 (n/a)</td><td>157.70 (n/a)</td><td>137.10 (n/a)</td><td>47.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>281.30 (n/a)</td><td>227.06 (n/a)</td><td>214.80 (n/a)</td><td>162.60 (n/a)</td><td>46.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.30 (n/a)</td><td>167.36 (n/a)</td><td>167.10 (n/a)</td><td>129.50 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.50 (n/a)</td><td>166.26 (n/a)</td><td>158.20 (n/a)</td><td>138.00 (n/a)</td><td>33.05 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.90 (n/a)</td><td>164.58 (n/a)</td><td>172.60 (n/a)</td><td>130.30 (n/a)</td><td>34.06 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>155.60 (n/a)</td><td>132.90 (n/a)</td><td>132.10 (n/a)</td><td>116.50 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.80 (n/a)</td><td>158.88 (n/a)</td><td>151.90 (n/a)</td><td>130.20 (n/a)</td><td>29.39 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>184.58 (n/a)</td><td>187.10 (n/a)</td><td>162.20 (n/a)</td><td>15.94 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.10 (n/a)</td><td>190.78 (n/a)</td><td>181.80 (n/a)</td><td>163.40 (n/a)</td><td>25.07 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>213.38 (n/a)</td><td>211.70 (n/a)</td><td>188.50 (n/a)</td><td>18.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>174.40 (n/a)</td><td>165.22 (n/a)</td><td>172.70 (n/a)</td><td>136.90 (n/a)</td><td>16.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>205.60 (n/a)</td><td>175.02 (n/a)</td><td>176.40 (n/a)</td><td>136.50 (n/a)</td><td>28.26 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.60 (n/a)</td><td>163.26 (n/a)</td><td>177.90 (n/a)</td><td>134.40 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.80 (n/a)</td><td>185.80 (n/a)</td><td>203.90 (n/a)</td><td>136.10 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>237.30 (n/a)</td><td>191.18 (n/a)</td><td>192.30 (n/a)</td><td>146.60 (n/a)</td><td>32.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>194.38 (n/a)</td><td>186.30 (n/a)</td><td>179.60 (n/a)</td><td>17.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>196.00 (n/a)</td><td>161.12 (n/a)</td><td>154.30 (n/a)</td><td>118.60 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>322.00 (n/a)</td><td>262.40 (n/a)</td><td>260.20 (n/a)</td><td>216.80 (n/a)</td><td>43.70 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+7.42%)</td><td>0.03 (+11.19%)</td><td>0.03 (+14.35%)</td><td>0.02 (+6.25%)</td><td>0.00 (+5.83%)</td><td>205.10 (-5.87%)</td><td>159.02 (-10.04%)</td><td>155.70 (-12.53%)</td><td>125.00 (-6.92%)</td><td>29.26 (-4.48%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.90 (n/a)</td><td>176.76 (n/a)</td><td>178.00 (n/a)</td><td>134.30 (n/a)</td><td>30.63 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-3.63%)</td><td>0.03 (+7.49%)</td><td>0.02 (+7.10%)</td><td>0.02 (+16.00%)</td><td>0.00 <b>(-31.12%)</b></td><td>184.90 (-13.80%)</td><td>164.82 (-8.11%)</td><td>172.60 (-6.60%)</td><td>143.00 (+3.77%)</td><td>17.68 <b>(-37.83%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.50 (n/a)</td><td>179.36 (n/a)</td><td>184.80 (n/a)</td><td>137.80 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+1.48%)</td><td>0.02 (-1.60%)</td><td>0.02 (+3.19%)</td><td>0.02 (-17.44%)</td><td>0.00 <b>(+38.38%)</b></td><td>250.30 <b>(+21.15%)</b></td><td>181.20 (+3.97%)</td><td>169.90 (-3.08%)</td><td>135.80 (-1.52%)</td><td>42.67 <b>(+73.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.60 (n/a)</td><td>174.28 (n/a)</td><td>175.30 (n/a)</td><td>137.90 (n/a)</td><td>24.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-16.19%)</td><td>0.02 (-9.37%)</td><td>0.02 (-7.83%)</td><td>0.02 (+10.27%)</td><td>0.00 <b>(-52.60%)</b></td><td>217.00 (-9.32%)</td><td>177.06 (+6.53%)</td><td>169.60 (+8.44%)</td><td>157.60 (+19.30%)</td><td>23.22 <b>(-47.16%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.30 (n/a)</td><td>166.20 (n/a)</td><td>156.40 (n/a)</td><td>132.10 (n/a)</td><td>43.95 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-13.58%)</td><td>0.03 (-3.72%)</td><td>0.03 (+3.18%)</td><td>0.02 (-9.68%)</td><td>0.01 (-19.97%)</td><td>239.80 (+10.71%)</td><td>170.28 (+3.17%)</td><td>159.40 (-3.10%)</td><td>124.30 (+15.63%)</td><td>43.25 (+9.03%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>165.04 (n/a)</td><td>164.50 (n/a)</td><td>107.50 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+12.40%)</td><td>0.02 (+7.76%)</td><td>0.02 (+8.09%)</td><td>0.02 (+2.39%)</td><td>0.00 (+15.92%)</td><td>206.10 (-2.32%)</td><td>167.76 (-6.97%)</td><td>164.90 (-7.52%)</td><td>130.50 (-11.04%)</td><td>27.65 (-1.41%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>180.32 (n/a)</td><td>178.30 (n/a)</td><td>146.70 (n/a)</td><td>28.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+14.65%)</td><td>0.02 (+16.80%)</td><td>0.02 (+10.54%)</td><td>0.02 <b>(+48.92%)</b></td><td>0.01 (-15.00%)</td><td>208.90 <b>(-32.85%)</b></td><td>171.52 (-17.72%)</td><td>184.50 (-9.51%)</td><td>131.60 (-12.73%)</td><td>33.63 <b>(-49.03%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>311.10 (n/a)</td><td>208.46 (n/a)</td><td>203.90 (n/a)</td><td>150.80 (n/a)</td><td>65.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (-3.15%)</td><td>0.02 (+4.44%)</td><td>0.02 (-5.84%)</td><td>0.02 <b>(+30.00%)</b></td><td>0.00 <b>(-22.73%)</b></td><td>255.80 <b>(-23.09%)</b></td><td>206.80 (-7.22%)</td><td>213.40 (+6.17%)</td><td>169.30 (+3.23%)</td><td>37.15 <b>(-43.24%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>332.60 (n/a)</td><td>222.90 (n/a)</td><td>201.00 (n/a)</td><td>164.00 (n/a)</td><td>65.46 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (-0.45%)</td><td>0.05 (-1.89%)</td><td>0.06 (+19.19%)</td><td>0.02 <b>(-45.12%)</b></td><td>0.02 <b>(+80.46%)</b></td><td>349.60 <b>(+82.18%)</b></td><td>182.66 (+16.79%)</td><td>131.40 (-16.09%)</td><td>117.70 (+0.43%)</td><td>98.10 <b>(+227.41%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>156.40 (n/a)</td><td>156.60 (n/a)</td><td>117.20 (n/a)</td><td>29.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (+5.30%)</td><td>0.05 (+2.98%)</td><td>0.06 (+15.29%)</td><td>0.04 (-17.75%)</td><td>0.01 <b>(+137.28%)</b></td><td>214.00 <b>(+21.59%)</b></td><td>160.30 (-0.09%)</td><td>138.00 (-13.26%)</td><td>134.20 (-5.02%)</td><td>34.90 <b>(+171.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>176.00 (n/a)</td><td>160.44 (n/a)</td><td>159.10 (n/a)</td><td>141.30 (n/a)</td><td>12.87 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (+2.80%)</td><td>0.05 (-3.94%)</td><td>0.05 (-11.07%)</td><td>0.04 (-11.98%)</td><td>0.01 <b>(+83.31%)</b></td><td>204.40 (+13.62%)</td><td>168.20 (+6.24%)</td><td>177.60 (+12.48%)</td><td>134.30 (-2.75%)</td><td>30.87 <b>(+96.91%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.90 (n/a)</td><td>158.32 (n/a)</td><td>157.90 (n/a)</td><td>138.10 (n/a)</td><td>15.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (+17.29%)</td><td>0.05 (+11.14%)</td><td>0.05 (+9.76%)</td><td>0.04 (-0.74%)</td><td>0.01 <b>(+91.59%)</b></td><td>211.50 (+0.71%)</td><td>174.14 (-8.84%)</td><td>176.50 (-8.88%)</td><td>143.50 (-14.74%)</td><td>27.33 <b>(+62.70%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.00 (n/a)</td><td>191.02 (n/a)</td><td>193.70 (n/a)</td><td>168.30 (n/a)</td><td>16.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (-12.98%)</td><td>0.05 (+8.61%)</td><td>0.06 <b>(+30.92%)</b></td><td>0.04 (+12.43%)</td><td>0.01 <b>(-27.96%)</b></td><td>200.60 (-11.04%)</td><td>158.30 (-10.25%)</td><td>138.40 <b>(-23.66%)</b></td><td>130.40 (+14.89%)</td><td>32.65 <b>(-25.01%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>176.38 (n/a)</td><td>181.30 (n/a)</td><td>113.50 (n/a)</td><td>43.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (+2.97%)</td><td>0.05 (+17.44%)</td><td>0.05 (+12.98%)</td><td>0.05 <b>(+27.12%)</b></td><td>0.00 <b>(-41.94%)</b></td><td>178.70 <b>(-21.35%)</b></td><td>166.46 (-16.01%)</td><td>173.70 (-11.51%)</td><td>149.10 (-2.87%)</td><td>12.82 <b>(-55.15%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>198.20 (n/a)</td><td>196.30 (n/a)</td><td>153.50 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 <b>(-21.64%)</b></td><td>0.05 (-11.39%)</td><td>0.05 (-1.40%)</td><td>0.04 (-10.28%)</td><td>0.01 <b>(-20.81%)</b></td><td>232.50 (+11.46%)</td><td>187.80 (+12.63%)</td><td>174.30 (+1.46%)</td><td>151.90 <b>(+27.65%)</b></td><td>38.17 (+16.68%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>166.74 (n/a)</td><td>171.80 (n/a)</td><td>119.00 (n/a)</td><td>32.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (-14.61%)</td><td>0.05 (-10.80%)</td><td>0.05 (-5.36%)</td><td>0.03 (-19.02%)</td><td>0.01 (-15.02%)</td><td>238.10 <b>(+23.50%)</b></td><td>184.36 (+12.32%)</td><td>179.20 (+5.66%)</td><td>143.60 (+17.13%)</td><td>33.96 <b>(+28.10%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>164.14 (n/a)</td><td>169.60 (n/a)</td><td>122.60 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (+17.88%)</td><td>0.05 (-8.53%)</td><td>0.05 (-13.48%)</td><td>0.04 (-19.47%)</td><td>0.02 <b>(+101.96%)</b></td><td>223.00 <b>(+24.16%)</b></td><td>169.26 (+15.06%)</td><td>169.50 (+15.62%)</td><td>101.10 (-15.18%)</td><td>44.16 <b>(+100.10%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.60 (n/a)</td><td>147.10 (n/a)</td><td>146.60 (n/a)</td><td>119.20 (n/a)</td><td>22.07 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (+2.56%)</td><td>0.04 (+5.45%)</td><td>0.04 (+2.98%)</td><td>0.04 (+5.93%)</td><td>0.00 (+19.56%)</td><td>226.90 (-5.62%)</td><td>208.26 (-5.01%)</td><td>216.00 (-2.88%)</td><td>187.60 (-2.49%)</td><td>18.99 (+10.00%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>240.40 (n/a)</td><td>219.24 (n/a)</td><td>222.40 (n/a)</td><td>192.40 (n/a)</td><td>17.26 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (-2.84%)</td><td>0.11 (+6.47%)</td><td>0.12 (+17.12%)</td><td>0.09 (+15.55%)</td><td>0.02 <b>(-26.76%)</b></td><td>182.30 (-13.48%)</td><td>149.22 (-7.72%)</td><td>137.20 (-14.62%)</td><td>127.60 (+2.99%)</td><td>22.47 <b>(-34.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.70 (n/a)</td><td>161.70 (n/a)</td><td>160.70 (n/a)</td><td>123.90 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (+8.24%)</td><td>0.10 (+9.04%)</td><td>0.10 (+6.62%)</td><td>0.09 <b>(+54.61%)</b></td><td>0.01 <b>(-36.25%)</b></td><td>179.20 <b>(-35.31%)</b></td><td>162.48 (-12.06%)</td><td>163.60 (-6.19%)</td><td>129.90 (-7.61%)</td><td>19.72 <b>(-63.54%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>277.00 (n/a)</td><td>184.76 (n/a)</td><td>174.40 (n/a)</td><td>140.60 (n/a)</td><td>54.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (+5.25%)</td><td>0.10 (+5.23%)</td><td>0.10 (-9.31%)</td><td>0.09 <b>(+48.62%)</b></td><td>0.01 <b>(-43.56%)</b></td><td>185.60 <b>(-32.70%)</b></td><td>168.36 (-9.67%)</td><td>171.60 (+10.28%)</td><td>134.10 (-4.96%)</td><td>20.25 <b>(-64.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>275.80 (n/a)</td><td>186.38 (n/a)</td><td>155.60 (n/a)</td><td>141.10 (n/a)</td><td>56.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (+7.85%)</td><td>0.10 (+3.36%)</td><td>0.09 (+2.20%)</td><td>0.08 (-7.51%)</td><td>0.03 <b>(+23.64%)</b></td><td>217.40 (+8.11%)</td><td>172.80 (-1.89%)</td><td>181.20 (-2.16%)</td><td>115.40 (-7.31%)</td><td>37.08 <b>(+21.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.10 (n/a)</td><td>176.12 (n/a)</td><td>185.20 (n/a)</td><td>124.50 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (+18.57%)</td><td>0.12 <b>(+21.37%)</b></td><td>0.12 <b>(+21.43%)</b></td><td>0.11 <b>(+30.77%)</b></td><td>0.02 (+5.75%)</td><td>155.70 <b>(-23.53%)</b></td><td>134.84 (-18.09%)</td><td>135.70 (-17.66%)</td><td>108.10 (-15.68%)</td><td>18.34 <b>(-31.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.60 (n/a)</td><td>164.62 (n/a)</td><td>164.80 (n/a)</td><td>128.20 (n/a)</td><td>26.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (+1.02%)</td><td>0.08 (-9.77%)</td><td>0.08 (-8.97%)</td><td>0.04 <b>(-37.10%)</b></td><td>0.02 <b>(+86.56%)</b></td><td>377.00 <b>(+59.00%)</b></td><td>220.64 (+19.86%)</td><td>194.90 (+9.86%)</td><td>159.30 (-0.99%)</td><td>89.83 <b>(+194.40%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>237.10 (n/a)</td><td>184.08 (n/a)</td><td>177.40 (n/a)</td><td>160.90 (n/a)</td><td>30.51 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (+2.45%)</td><td>0.09 (-1.81%)</td><td>0.09 (-0.72%)</td><td>0.07 (-7.50%)</td><td>0.01 <b>(+57.15%)</b></td><td>221.90 (+8.09%)</td><td>185.50 (+2.99%)</td><td>179.80 (+0.73%)</td><td>154.10 (-2.34%)</td><td>28.12 <b>(+65.85%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>180.12 (n/a)</td><td>178.50 (n/a)</td><td>157.80 (n/a)</td><td>16.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (-5.03%)</td><td>0.07 (-6.21%)</td><td>0.07 (-4.52%)</td><td>0.06 (-1.93%)</td><td>0.01 (-10.86%)</td><td>263.50 (+1.97%)</td><td>225.34 (+6.27%)</td><td>227.70 (+4.74%)</td><td>176.30 (+5.32%)</td><td>31.60 (-6.12%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>258.40 (n/a)</td><td>212.04 (n/a)</td><td>217.40 (n/a)</td><td>167.40 (n/a)</td><td>33.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (-5.64%)</td><td>0.22 (+9.34%)</td><td>0.24 <b>(+20.15%)</b></td><td>0.15 (-2.27%)</td><td>0.04 (-7.62%)</td><td>211.90 (+2.32%)</td><td>154.60 (-8.66%)</td><td>138.70 (-16.80%)</td><td>123.40 (+6.01%)</td><td>35.77 (+4.12%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>207.10 (n/a)</td><td>169.26 (n/a)</td><td>166.70 (n/a)</td><td>116.40 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.26 <b>(+20.30%)</b></td><td>0.20 (+11.98%)</td><td>0.22 (+7.36%)</td><td>0.16 <b>(+75.16%)</b></td><td>0.04 <b>(-24.62%)</b></td><td>209.40 <b>(-42.90%)</b></td><td>165.20 (-17.71%)</td><td>152.40 (-6.85%)</td><td>126.80 (-16.85%)</td><td>32.65 <b>(-64.88%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>366.70 (n/a)</td><td>200.76 (n/a)</td><td>163.60 (n/a)</td><td>152.50 (n/a)</td><td>92.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (+8.16%)</td><td>0.19 (-2.47%)</td><td>0.19 (+0.66%)</td><td>0.13 <b>(-21.42%)</b></td><td>0.04 <b>(+59.05%)</b></td><td>242.80 <b>(+27.25%)</b></td><td>176.50 (+5.45%)</td><td>171.10 (-0.64%)</td><td>129.20 (-7.52%)</td><td>42.05 <b>(+90.07%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>190.80 (n/a)</td><td>167.38 (n/a)</td><td>172.20 (n/a)</td><td>139.70 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 <b>(-20.89%)</b></td><td>0.19 (-15.93%)</td><td>0.20 (-18.45%)</td><td>0.16 (-3.22%)</td><td>0.02 <b>(-48.39%)</b></td><td>199.40 (+3.32%)</td><td>171.22 (+16.62%)</td><td>163.50 <b>(+22.66%)</b></td><td>151.00 <b>(+26.47%)</b></td><td>20.27 <b>(-32.79%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>193.00 (n/a)</td><td>146.82 (n/a)</td><td>133.30 (n/a)</td><td>119.40 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 <b>(-22.67%)</b></td><td>0.17 <b>(-21.71%)</b></td><td>0.16 <b>(-25.50%)</b></td><td>0.15 (-3.02%)</td><td>0.03 <b>(-45.26%)</b></td><td>223.00 (+3.15%)</td><td>198.40 <b>(+24.58%)</b></td><td>210.50 <b>(+34.25%)</b></td><td>154.80 <b>(+29.32%)</b></td><td>27.19 <b>(-27.88%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>216.20 (n/a)</td><td>159.26 (n/a)</td><td>156.80 (n/a)</td><td>119.70 (n/a)</td><td>37.70 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (+18.37%)</td><td>0.19 (-11.26%)</td><td>0.15 <b>(-28.39%)</b></td><td>0.12 <b>(-35.70%)</b></td><td>0.08 <b>(+170.54%)</b></td><td>282.80 <b>(+55.47%)</b></td><td>204.10 <b>(+27.85%)</b></td><td>222.00 <b>(+39.62%)</b></td><td>110.70 (-15.56%)</td><td>78.68 <b>(+253.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>181.90 (n/a)</td><td>159.64 (n/a)</td><td>159.00 (n/a)</td><td>131.10 (n/a)</td><td>22.26 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.16 <b>(-20.96%)</b></td><td>0.14 (-16.08%)</td><td>0.14 (-12.68%)</td><td>0.12 (-12.17%)</td><td>0.01 <b>(-42.80%)</b></td><td>262.20 (+13.85%)</td><td>237.12 (+18.25%)</td><td>235.20 (+14.51%)</td><td>210.40 <b>(+26.52%)</b></td><td>22.05 (-16.94%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>230.30 (n/a)</td><td>200.52 (n/a)</td><td>205.40 (n/a)</td><td>166.30 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (+10.63%)</td><td>0.03 (+7.54%)</td><td>0.03 (-0.89%)</td><td>0.02 (+10.26%)</td><td>0.01 (+11.71%)</td><td>173.10 (-9.32%)</td><td>151.44 (-7.05%)</td><td>162.80 (+0.87%)</td><td>105.50 (-9.60%)</td><td>26.98 (-12.07%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>190.90 (n/a)</td><td>162.92 (n/a)</td><td>161.40 (n/a)</td><td>116.70 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-17.26%)</td><td>0.02 (-1.88%)</td><td>0.03 (+9.17%)</td><td>0.02 (+0.98%)</td><td>0.00 <b>(-48.28%)</b></td><td>185.60 (-0.96%)</td><td>167.66 (+0.72%)</td><td>157.70 (-8.42%)</td><td>156.80 <b>(+20.89%)</b></td><td>14.29 <b>(-37.92%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.40 (n/a)</td><td>166.46 (n/a)</td><td>172.20 (n/a)</td><td>129.70 (n/a)</td><td>23.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (-6.71%)</td><td>0.02 (-11.86%)</td><td>0.02 (-6.11%)</td><td>0.01 <b>(-24.68%)</b></td><td>0.00 <b>(+24.34%)</b></td><td>324.40 <b>(+32.79%)</b></td><td>241.10 (+15.90%)</td><td>230.00 (+6.48%)</td><td>177.90 (+7.23%)</td><td>54.59 <b>(+80.97%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.30 (n/a)</td><td>208.02 (n/a)</td><td>216.00 (n/a)</td><td>165.90 (n/a)</td><td>30.17 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+2.91%)</td><td>0.02 (-3.64%)</td><td>0.02 (-6.39%)</td><td>0.02 (+6.08%)</td><td>0.00 (+0.87%)</td><td>223.20 (-5.74%)</td><td>193.70 (+3.62%)</td><td>195.60 (+6.83%)</td><td>154.70 (-2.83%)</td><td>27.09 (-9.69%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.80 (n/a)</td><td>186.94 (n/a)</td><td>183.10 (n/a)</td><td>159.20 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 <b>(+29.07%)</b></td><td>0.03 (+12.87%)</td><td>0.02 (-1.82%)</td><td>0.02 (-5.70%)</td><td>0.01 <b>(+120.65%)</b></td><td>204.60 (+6.07%)</td><td>161.14 (-5.98%)</td><td>181.00 (+1.86%)</td><td>101.80 <b>(-22.47%)</b></td><td>46.99 <b>(+83.51%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.90 (n/a)</td><td>171.38 (n/a)</td><td>177.70 (n/a)</td><td>131.30 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+3.67%)</td><td>0.02 (-3.58%)</td><td>0.02 (-7.66%)</td><td>0.02 (+10.62%)</td><td>0.00 (-17.19%)</td><td>212.30 (-9.62%)</td><td>173.30 (+1.69%)</td><td>175.40 (+8.27%)</td><td>126.10 (-3.59%)</td><td>31.14 <b>(-28.35%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>170.42 (n/a)</td><td>162.00 (n/a)</td><td>130.80 (n/a)</td><td>43.47 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+4.02%)</td><td>0.03 (+2.39%)</td><td>0.02 (+5.50%)</td><td>0.02 (-3.71%)</td><td>0.01 (+12.81%)</td><td>222.10 (+3.88%)</td><td>170.20 (-1.49%)</td><td>166.30 (-5.19%)</td><td>120.60 (-3.90%)</td><td>37.13 (+13.98%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>172.78 (n/a)</td><td>175.40 (n/a)</td><td>125.50 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-2.26%)</td><td>0.02 (+4.18%)</td><td>0.02 (+15.41%)</td><td>0.02 (-0.13%)</td><td>0.00 <b>(-22.46%)</b></td><td>227.40 (+0.13%)</td><td>182.22 (-4.99%)</td><td>178.90 (-13.37%)</td><td>156.10 (+2.29%)</td><td>28.01 (-18.31%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.10 (n/a)</td><td>191.80 (n/a)</td><td>206.50 (n/a)</td><td>152.60 (n/a)</td><td>34.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 <b>(+50.59%)</b></td><td>0.02 (+12.15%)</td><td>0.02 (+11.80%)</td><td>0.01 (+3.88%)</td><td>0.01 <b>(+138.46%)</b></td><td>285.30 (-3.74%)</td><td>211.68 (-5.79%)</td><td>194.30 (-10.58%)</td><td>128.20 <b>(-33.61%)</b></td><td>62.22 <b>(+49.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>296.40 (n/a)</td><td>224.68 (n/a)</td><td>217.30 (n/a)</td><td>193.10 (n/a)</td><td>41.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (+11.24%)</td><td>0.03 (+3.18%)</td><td>0.02 (-7.66%)</td><td>0.02 (+19.99%)</td><td>0.01 (+13.25%)</td><td>185.50 (-16.63%)</td><td>164.62 (-3.22%)</td><td>177.10 (+8.32%)</td><td>116.50 (-10.11%)</td><td>28.30 (-17.48%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.50 (n/a)</td><td>170.10 (n/a)</td><td>163.50 (n/a)</td><td>129.60 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+16.16%)</td><td>0.03 (+16.65%)</td><td>0.02 (+15.16%)</td><td>0.02 <b>(+21.67%)</b></td><td>0.00 (-7.40%)</td><td>167.80 (-17.83%)</td><td>158.14 (-14.53%)</td><td>165.30 (-13.18%)</td><td>142.10 (-13.88%)</td><td>12.17 <b>(-33.26%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.20 (n/a)</td><td>185.02 (n/a)</td><td>190.40 (n/a)</td><td>165.00 (n/a)</td><td>18.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+8.91%)</td><td>0.02 (+2.82%)</td><td>0.02 (+4.68%)</td><td>0.01 <b>(-29.76%)</b></td><td>0.01 <b>(+110.00%)</b></td><td>304.00 <b>(+42.39%)</b></td><td>190.92 (+4.99%)</td><td>175.20 (-4.47%)</td><td>131.00 (-8.20%)</td><td>70.44 <b>(+177.70%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.50 (n/a)</td><td>181.84 (n/a)</td><td>183.40 (n/a)</td><td>142.70 (n/a)</td><td>25.36 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (-5.62%)</td><td>0.02 (+13.18%)</td><td>0.02 (+19.45%)</td><td>0.02 <b>(+40.86%)</b></td><td>0.00 <b>(-55.78%)</b></td><td>213.30 <b>(-29.02%)</b></td><td>193.72 (-14.63%)</td><td>193.20 (-16.29%)</td><td>171.20 (+6.01%)</td><td>17.06 <b>(-66.35%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>300.50 (n/a)</td><td>226.92 (n/a)</td><td>230.80 (n/a)</td><td>161.50 (n/a)</td><td>50.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (-10.56%)</td><td>0.02 (-10.40%)</td><td>0.02 (-15.39%)</td><td>0.02 (-2.63%)</td><td>0.00 <b>(-21.58%)</b></td><td>213.40 (+2.69%)</td><td>202.14 (+11.21%)</td><td>213.10 (+18.19%)</td><td>167.00 (+11.86%)</td><td>20.05 (-9.74%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.80 (n/a)</td><td>181.76 (n/a)</td><td>180.30 (n/a)</td><td>149.30 (n/a)</td><td>22.21 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (-12.30%)</td><td>0.02 (-15.17%)</td><td>0.02 <b>(-20.63%)</b></td><td>0.02 (-11.03%)</td><td>0.00 (-7.55%)</td><td>224.50 (+12.42%)</td><td>197.06 (+17.96%)</td><td>202.60 <b>(+26.00%)</b></td><td>169.60 (+14.06%)</td><td>22.11 (+14.66%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.70 (n/a)</td><td>167.06 (n/a)</td><td>160.80 (n/a)</td><td>148.70 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 <b>(-22.34%)</b></td><td>0.02 (-14.90%)</td><td>0.02 (-14.77%)</td><td>0.02 (-16.09%)</td><td>0.00 <b>(-41.36%)</b></td><td>248.30 (+19.15%)</td><td>212.68 (+16.60%)</td><td>210.40 (+17.35%)</td><td>185.10 <b>(+28.81%)</b></td><td>23.08 (-8.59%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>182.40 (n/a)</td><td>179.30 (n/a)</td><td>143.70 (n/a)</td><td>25.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (-13.76%)</td><td>0.05 (+0.83%)</td><td>0.05 (-0.89%)</td><td>0.04 (+11.54%)</td><td>0.01 <b>(-50.34%)</b></td><td>210.00 (-10.33%)</td><td>176.60 (-4.32%)</td><td>166.70 (+0.91%)</td><td>155.40 (+15.97%)</td><td>22.28 <b>(-50.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>184.58 (n/a)</td><td>165.20 (n/a)</td><td>134.00 (n/a)</td><td>45.24 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 <b>(+20.02%)</b></td><td>0.05 (+6.53%)</td><td>0.06 (+10.84%)</td><td>0.04 (-7.39%)</td><td>0.01 <b>(+138.90%)</b></td><td>208.60 (+7.97%)</td><td>158.90 (-1.85%)</td><td>144.20 (-9.82%)</td><td>119.50 (-16.67%)</td><td>42.46 <b>(+115.73%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>161.90 (n/a)</td><td>159.90 (n/a)</td><td>143.40 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 <b>(+24.58%)</b></td><td>0.05 <b>(+23.55%)</b></td><td>0.05 <b>(+33.52%)</b></td><td>0.04 (+5.17%)</td><td>0.01 <b>(+43.15%)</b></td><td>224.60 (-4.91%)</td><td>171.98 (-17.79%)</td><td>164.20 <b>(-25.13%)</b></td><td>119.00 (-19.76%)</td><td>39.07 (+11.47%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>209.20 (n/a)</td><td>219.30 (n/a)</td><td>148.30 (n/a)</td><td>35.05 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 <b>(+25.02%)</b></td><td>0.05 (+19.48%)</td><td>0.04 (+8.25%)</td><td>0.04 <b>(+32.16%)</b></td><td>0.01 (+0.85%)</td><td>211.50 <b>(-24.33%)</b></td><td>176.16 (-17.55%)</td><td>182.80 (-7.63%)</td><td>134.70 <b>(-20.01%)</b></td><td>29.47 <b>(-39.22%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>279.50 (n/a)</td><td>213.66 (n/a)</td><td>197.90 (n/a)</td><td>168.40 (n/a)</td><td>48.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 <b>(+20.74%)</b></td><td>0.05 <b>(+27.10%)</b></td><td>0.05 <b>(+21.63%)</b></td><td>0.04 <b>(+48.91%)</b></td><td>0.01 (+10.31%)</td><td>202.60 <b>(-32.85%)</b></td><td>158.08 <b>(-22.91%)</b></td><td>164.50 (-17.79%)</td><td>116.80 (-17.16%)</td><td>35.64 <b>(-40.98%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>301.70 (n/a)</td><td>205.06 (n/a)</td><td>200.10 (n/a)</td><td>141.00 (n/a)</td><td>60.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (+1.21%)</td><td>0.05 (+0.82%)</td><td>0.05 (-4.22%)</td><td>0.04 <b>(+21.30%)</b></td><td>0.01 (-3.01%)</td><td>205.70 (-17.56%)</td><td>167.42 (-2.05%)</td><td>170.00 (+4.42%)</td><td>131.70 (-1.20%)</td><td>34.10 <b>(-25.54%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.50 (n/a)</td><td>170.92 (n/a)</td><td>162.80 (n/a)</td><td>133.30 (n/a)</td><td>45.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 <b>(-28.48%)</b></td><td>0.04 (-5.95%)</td><td>0.05 (-6.72%)</td><td>0.04 <b>(+45.15%)</b></td><td>0.01 <b>(-63.99%)</b></td><td>225.20 <b>(-31.11%)</b></td><td>188.52 (-4.33%)</td><td>179.00 (+7.19%)</td><td>159.40 <b>(+39.82%)</b></td><td>27.63 <b>(-66.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>326.90 (n/a)</td><td>197.06 (n/a)</td><td>167.00 (n/a)</td><td>114.00 (n/a)</td><td>81.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 (+8.81%)</td><td>0.05 (-3.53%)</td><td>0.05 (-16.29%)</td><td>0.05 (+6.60%)</td><td>0.01 (+8.41%)</td><td>177.90 (-6.17%)</td><td>159.26 (+3.46%)</td><td>167.00 (+19.46%)</td><td>108.00 (-8.16%)</td><td>29.12 (-12.94%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>153.94 (n/a)</td><td>139.80 (n/a)</td><td>117.60 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 <b>(+24.03%)</b></td><td>0.05 (-0.26%)</td><td>0.04 (-19.22%)</td><td>0.03 (-12.46%)</td><td>0.02 <b>(+119.79%)</b></td><td>239.90 (+14.24%)</td><td>188.40 (+6.63%)</td><td>212.20 <b>(+23.80%)</b></td><td>116.00 (-19.33%)</td><td>54.58 <b>(+103.20%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>176.68 (n/a)</td><td>171.40 (n/a)</td><td>143.80 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (-0.57%)</td><td>0.05 (-5.77%)</td><td>0.05 (-0.78%)</td><td>0.04 (+0.01%)</td><td>0.01 (-14.64%)</td><td>195.40 (+0.00%)</td><td>170.90 (+5.57%)</td><td>171.30 (+0.82%)</td><td>135.90 (+0.52%)</td><td>22.36 (-12.86%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>161.88 (n/a)</td><td>169.90 (n/a)</td><td>135.20 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (-8.72%)</td><td>0.04 (-4.85%)</td><td>0.05 (+5.96%)</td><td>0.04 (-7.13%)</td><td>0.01 (-4.18%)</td><td>221.00 (+7.70%)</td><td>186.42 (+5.39%)</td><td>173.60 (-5.65%)</td><td>149.00 (+9.56%)</td><td>31.15 (+19.48%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>176.88 (n/a)</td><td>184.00 (n/a)</td><td>136.00 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (-13.02%)</td><td>0.05 (+2.31%)</td><td>0.05 (+14.37%)</td><td>0.04 (+7.28%)</td><td>0.00 <b>(-48.37%)</b></td><td>209.90 (-6.79%)</td><td>177.28 (-4.24%)</td><td>170.20 (-12.54%)</td><td>159.20 (+15.03%)</td><td>19.44 <b>(-42.93%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>185.12 (n/a)</td><td>194.60 (n/a)</td><td>138.40 (n/a)</td><td>34.07 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (-6.57%)</td><td>0.05 (+0.73%)</td><td>0.05 (-1.30%)</td><td>0.04 <b>(+25.45%)</b></td><td>0.00 <b>(-55.20%)</b></td><td>194.80 <b>(-20.26%)</b></td><td>177.80 (-3.39%)</td><td>178.20 (+1.31%)</td><td>160.00 (+7.02%)</td><td>15.28 <b>(-61.05%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.30 (n/a)</td><td>184.04 (n/a)</td><td>175.90 (n/a)</td><td>149.50 (n/a)</td><td>39.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (-3.44%)</td><td>0.05 (+6.90%)</td><td>0.05 <b>(+28.04%)</b></td><td>0.04 (+14.49%)</td><td>0.01 <b>(-30.75%)</b></td><td>223.20 (-12.64%)</td><td>176.86 (-9.46%)</td><td>170.60 <b>(-21.89%)</b></td><td>139.40 (+3.57%)</td><td>33.01 <b>(-35.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.50 (n/a)</td><td>195.34 (n/a)</td><td>218.40 (n/a)</td><td>134.60 (n/a)</td><td>51.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (+9.32%)</td><td>0.05 <b>(+21.44%)</b></td><td>0.05 <b>(+30.91%)</b></td><td>0.04 <b>(+25.79%)</b></td><td>0.01 (-19.77%)</td><td>184.30 <b>(-20.49%)</b></td><td>167.16 (-18.92%)</td><td>169.70 <b>(-23.63%)</b></td><td>132.90 (-8.53%)</td><td>20.99 <b>(-40.56%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>206.16 (n/a)</td><td>222.20 (n/a)</td><td>145.30 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 <b>(+22.34%)</b></td><td>0.06 <b>(+20.22%)</b></td><td>0.06 <b>(+32.17%)</b></td><td>0.03 (-15.39%)</td><td>0.01 <b>(+100.27%)</b></td><td>242.20 (+18.20%)</td><td>153.44 (-12.50%)</td><td>135.60 <b>(-24.37%)</b></td><td>113.10 (-18.28%)</td><td>50.87 <b>(+112.57%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>175.36 (n/a)</td><td>179.30 (n/a)</td><td>138.40 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (+2.75%)</td><td>0.11 (+10.89%)</td><td>0.09 (+4.76%)</td><td>0.09 <b>(+54.65%)</b></td><td>0.02 <b>(-35.36%)</b></td><td>180.90 <b>(-35.32%)</b></td><td>156.90 (-16.89%)</td><td>176.00 (-4.56%)</td><td>115.70 (-2.69%)</td><td>31.05 <b>(-56.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>279.70 (n/a)</td><td>188.78 (n/a)</td><td>184.40 (n/a)</td><td>118.90 (n/a)</td><td>70.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 <b>(-23.17%)</b></td><td>0.09 (-11.74%)</td><td>0.09 (-4.43%)</td><td>0.08 (-13.72%)</td><td>0.01 <b>(-44.51%)</b></td><td>216.30 (+15.92%)</td><td>177.22 (+11.47%)</td><td>176.00 (+4.64%)</td><td>155.30 <b>(+30.18%)</b></td><td>24.40 (-17.35%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.60 (n/a)</td><td>158.98 (n/a)</td><td>168.20 (n/a)</td><td>119.30 (n/a)</td><td>29.51 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.08 <b>(-21.72%)</b></td><td>0.07 (-8.01%)</td><td>0.07 (+5.47%)</td><td>0.05 (-14.98%)</td><td>0.01 <b>(-31.97%)</b></td><td>302.20 (+17.59%)</td><td>243.96 (+8.06%)</td><td>225.00 (-5.22%)</td><td>215.60 <b>(+27.73%)</b></td><td>35.74 (+6.55%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>257.00 (n/a)</td><td>225.76 (n/a)</td><td>237.40 (n/a)</td><td>168.80 (n/a)</td><td>33.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (+13.35%)</td><td>0.09 (-2.38%)</td><td>0.08 (-5.47%)</td><td>0.08 (-5.99%)</td><td>0.01 <b>(+183.84%)</b></td><td>211.30 (+6.39%)</td><td>191.86 (+3.41%)</td><td>194.10 (+5.78%)</td><td>157.20 (-11.78%)</td><td>21.24 <b>(+162.07%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>198.60 (n/a)</td><td>185.54 (n/a)</td><td>183.50 (n/a)</td><td>178.20 (n/a)</td><td>8.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (-14.65%)</td><td>0.11 (+10.91%)</td><td>0.11 (+3.86%)</td><td>0.09 <b>(+72.12%)</b></td><td>0.01 <b>(-69.49%)</b></td><td>183.00 <b>(-41.89%)</b></td><td>156.46 <b>(-23.86%)</b></td><td>155.80 (-3.71%)</td><td>136.70 (+17.24%)</td><td>19.26 <b>(-80.50%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>314.90 (n/a)</td><td>205.50 (n/a)</td><td>161.80 (n/a)</td><td>116.60 (n/a)</td><td>98.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (+14.98%)</td><td>0.09 (+0.24%)</td><td>0.08 (-10.04%)</td><td>0.08 (+13.24%)</td><td>0.02 <b>(+26.34%)</b></td><td>203.00 (-11.70%)</td><td>183.24 (+0.07%)</td><td>193.20 (+11.16%)</td><td>138.50 (-13.06%)</td><td>26.45 (-5.78%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>183.12 (n/a)</td><td>173.80 (n/a)</td><td>159.30 (n/a)</td><td>28.07 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (+3.97%)</td><td>0.10 (-5.98%)</td><td>0.09 (-12.88%)</td><td>0.08 (-14.67%)</td><td>0.02 <b>(+50.36%)</b></td><td>208.20 (+17.16%)</td><td>168.08 (+8.68%)</td><td>176.30 (+14.78%)</td><td>126.20 (-3.88%)</td><td>34.83 <b>(+66.40%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.70 (n/a)</td><td>154.66 (n/a)</td><td>153.60 (n/a)</td><td>131.30 (n/a)</td><td>20.93 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 <b>(+21.47%)</b></td><td>0.10 (+12.50%)</td><td>0.09 (-1.91%)</td><td>0.09 (+16.67%)</td><td>0.02 <b>(+30.87%)</b></td><td>191.70 (-14.30%)</td><td>162.82 (-10.76%)</td><td>175.50 (+1.98%)</td><td>129.10 (-17.72%)</td><td>26.96 (-7.41%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>182.46 (n/a)</td><td>172.10 (n/a)</td><td>156.90 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (+8.87%)</td><td>0.10 (+16.22%)</td><td>0.10 (+12.50%)</td><td>0.08 <b>(+36.28%)</b></td><td>0.02 (+11.16%)</td><td>213.70 <b>(-26.61%)</b></td><td>168.88 (-14.86%)</td><td>169.60 (-11.11%)</td><td>127.90 (-8.18%)</td><td>40.02 <b>(-29.03%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>291.20 (n/a)</td><td>198.36 (n/a)</td><td>190.80 (n/a)</td><td>139.30 (n/a)</td><td>56.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (-1.10%)</td><td>0.10 (+12.12%)</td><td>0.11 <b>(+28.66%)</b></td><td>0.07 (+4.03%)</td><td>0.02 (+10.98%)</td><td>219.30 (-3.86%)</td><td>168.24 (-10.15%)</td><td>145.80 <b>(-22.28%)</b></td><td>135.70 (+1.12%)</td><td>38.66 (+10.10%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>228.10 (n/a)</td><td>187.24 (n/a)</td><td>187.60 (n/a)</td><td>134.20 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (-13.12%)</td><td>0.09 (-13.20%)</td><td>0.09 (-7.10%)</td><td>0.07 (-9.09%)</td><td>0.02 <b>(-20.77%)</b></td><td>232.10 (+10.00%)</td><td>182.44 (+14.07%)</td><td>176.30 (+7.63%)</td><td>128.70 (+15.12%)</td><td>38.40 (-0.17%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>211.00 (n/a)</td><td>159.94 (n/a)</td><td>163.80 (n/a)</td><td>111.80 (n/a)</td><td>38.46 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (-0.39%)</td><td>0.11 (+4.63%)</td><td>0.11 <b>(+31.32%)</b></td><td>0.08 (+18.24%)</td><td>0.02 <b>(-31.16%)</b></td><td>195.60 (-15.40%)</td><td>160.66 (-8.73%)</td><td>153.10 <b>(-23.83%)</b></td><td>117.60 (+0.43%)</td><td>33.45 <b>(-36.89%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>231.20 (n/a)</td><td>176.02 (n/a)</td><td>201.00 (n/a)</td><td>117.10 (n/a)</td><td>53.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (-16.99%)</td><td>0.08 (-8.83%)</td><td>0.08 (+3.53%)</td><td>0.07 <b>(+20.70%)</b></td><td>0.01 <b>(-48.40%)</b></td><td>234.70 (-17.15%)</td><td>200.64 (+3.54%)</td><td>197.40 (-3.38%)</td><td>152.90 <b>(+20.49%)</b></td><td>32.62 <b>(-47.15%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>283.30 (n/a)</td><td>193.78 (n/a)</td><td>204.30 (n/a)</td><td>126.90 (n/a)</td><td>61.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (+7.65%)</td><td>0.09 (+0.38%)</td><td>0.10 (+5.14%)</td><td>0.07 (-7.90%)</td><td>0.01 <b>(+122.35%)</b></td><td>222.50 (+8.59%)</td><td>185.98 (+1.13%)</td><td>171.70 (-4.88%)</td><td>157.70 (-7.13%)</td><td>28.98 <b>(+124.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>183.90 (n/a)</td><td>180.50 (n/a)</td><td>169.80 (n/a)</td><td>12.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (+11.29%)</td><td>0.09 (+9.35%)</td><td>0.09 (+8.65%)</td><td>0.08 (+10.84%)</td><td>0.01 (+19.00%)</td><td>196.30 (-9.79%)</td><td>179.94 (-8.45%)</td><td>181.60 (-7.96%)</td><td>151.80 (-10.18%)</td><td>18.01 (-2.81%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>196.54 (n/a)</td><td>197.30 (n/a)</td><td>169.00 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (+11.41%)</td><td>0.10 <b>(+22.11%)</b></td><td>0.11 <b>(+30.75%)</b></td><td>0.08 (+13.45%)</td><td>0.02 <b>(+26.36%)</b></td><td>204.60 (-11.85%)</td><td>165.86 (-17.44%)</td><td>154.80 <b>(-23.52%)</b></td><td>131.70 (-10.29%)</td><td>35.22 (+2.87%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.10 (n/a)</td><td>200.90 (n/a)</td><td>202.40 (n/a)</td><td>146.80 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 <b>(+28.88%)</b></td><td>0.21 (+13.57%)</td><td>0.21 (+10.61%)</td><td>0.17 (-2.11%)</td><td>0.04 <b>(+246.96%)</b></td><td>198.20 (+2.11%)</td><td>161.98 (-9.92%)</td><td>159.70 (-9.57%)</td><td>129.40 <b>(-22.42%)</b></td><td>28.89 <b>(+173.53%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>179.82 (n/a)</td><td>176.60 (n/a)</td><td>166.80 (n/a)</td><td>10.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.26 (-6.19%)</td><td>0.22 (+9.52%)</td><td>0.22 (+18.72%)</td><td>0.14 (+9.44%)</td><td>0.05 (-11.09%)</td><td>228.90 (-8.62%)</td><td>157.26 (-9.80%)</td><td>146.90 (-15.77%)</td><td>125.30 (+6.55%)</td><td>42.18 (-13.12%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>250.50 (n/a)</td><td>174.34 (n/a)</td><td>174.40 (n/a)</td><td>117.60 (n/a)</td><td>48.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 <b>(-39.02%)</b></td><td>0.14 <b>(-23.66%)</b></td><td>0.14 <b>(-22.64%)</b></td><td>0.12 (+17.22%)</td><td>0.01 <b>(-83.52%)</b></td><td>268.80 (-14.69%)</td><td>240.26 (+18.48%)</td><td>237.70 <b>(+29.26%)</b></td><td>218.20 <b>(+64.06%)</b></td><td>18.18 <b>(-76.13%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>315.10 (n/a)</td><td>202.78 (n/a)</td><td>183.90 (n/a)</td><td>133.00 (n/a)</td><td>76.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 <b>(-23.34%)</b></td><td>0.16 (-11.43%)</td><td>0.15 (-2.01%)</td><td>0.15 (-0.98%)</td><td>0.01 <b>(-74.57%)</b></td><td>223.70 (+0.99%)</td><td>210.18 (+10.16%)</td><td>211.70 (+2.07%)</td><td>192.90 <b>(+30.43%)</b></td><td>11.09 <b>(-66.95%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.50 (n/a)</td><td>190.80 (n/a)</td><td>207.40 (n/a)</td><td>147.90 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (+8.77%)</td><td>0.21 (+6.94%)</td><td>0.19 (+1.13%)</td><td>0.17 <b>(+29.01%)</b></td><td>0.06 (+3.76%)</td><td>189.60 <b>(-22.49%)</b></td><td>162.86 (-7.72%)</td><td>171.40 (-1.10%)</td><td>102.20 (-8.01%)</td><td>34.87 <b>(-26.92%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>244.60 (n/a)</td><td>176.48 (n/a)</td><td>173.30 (n/a)</td><td>111.10 (n/a)</td><td>47.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.24 (-14.79%)</td><td>0.19 (-12.73%)</td><td>0.18 <b>(-22.59%)</b></td><td>0.15 (-8.48%)</td><td>0.04 (-2.50%)</td><td>217.30 (+9.31%)</td><td>175.30 (+15.31%)</td><td>180.50 <b>(+29.21%)</b></td><td>135.40 (+17.43%)</td><td>38.71 (+19.92%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>198.80 (n/a)</td><td>152.02 (n/a)</td><td>139.70 (n/a)</td><td>115.30 (n/a)</td><td>32.28 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 <b>(+27.23%)</b></td><td>0.23 <b>(+29.38%)</b></td><td>0.23 <b>(+29.73%)</b></td><td>0.19 (+19.40%)</td><td>0.03 <b>(+44.83%)</b></td><td>176.20 (-16.25%)</td><td>145.66 <b>(-22.46%)</b></td><td>143.30 <b>(-22.96%)</b></td><td>130.00 <b>(-21.40%)</b></td><td>18.89 (-5.72%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.40 (n/a)</td><td>187.86 (n/a)</td><td>186.00 (n/a)</td><td>165.40 (n/a)</td><td>20.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (+2.77%)</td><td>0.18 (-1.28%)</td><td>0.17 (-4.13%)</td><td>0.16 (-2.08%)</td><td>0.02 <b>(+37.83%)</b></td><td>204.70 (+2.15%)</td><td>186.76 (+1.73%)</td><td>197.10 (+4.34%)</td><td>162.90 (-2.69%)</td><td>19.39 <b>(+38.26%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>183.58 (n/a)</td><td>188.90 (n/a)</td><td>167.40 (n/a)</td><td>14.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (-17.96%)</td><td>0.19 (-7.14%)</td><td>0.19 (-1.86%)</td><td>0.15 (-2.09%)</td><td>0.02 <b>(-43.41%)</b></td><td>221.10 (+2.12%)</td><td>179.22 (+5.85%)</td><td>169.80 (+1.86%)</td><td>163.50 <b>(+21.92%)</b></td><td>23.84 <b>(-27.94%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.50 (n/a)</td><td>169.32 (n/a)</td><td>166.70 (n/a)</td><td>134.10 (n/a)</td><td>33.08 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (-13.32%)</td><td>0.20 (+0.28%)</td><td>0.20 (+3.52%)</td><td>0.18 (+5.74%)</td><td>0.01 <b>(-61.71%)</b></td><td>180.80 (-5.39%)</td><td>166.58 (-1.41%)</td><td>165.30 (-3.39%)</td><td>158.10 (+15.40%)</td><td>8.99 <b>(-57.89%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.10 (n/a)</td><td>168.96 (n/a)</td><td>171.10 (n/a)</td><td>137.00 (n/a)</td><td>21.36 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (-4.31%)</td><td>0.16 (-6.22%)</td><td>0.16 (-14.62%)</td><td>0.14 (-7.31%)</td><td>0.02 (-12.61%)</td><td>229.60 (+7.89%)</td><td>200.46 (+6.45%)</td><td>206.30 (+17.15%)</td><td>176.70 (+4.49%)</td><td>21.57 (-3.90%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.80 (n/a)</td><td>188.32 (n/a)</td><td>176.10 (n/a)</td><td>169.10 (n/a)</td><td>22.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (-15.26%)</td><td>0.18 (-12.01%)</td><td>0.18 (-11.08%)</td><td>0.16 (-14.43%)</td><td>0.01 <b>(-21.82%)</b></td><td>202.00 (+16.90%)</td><td>183.82 (+13.60%)</td><td>180.70 (+12.45%)</td><td>173.60 (+18.01%)</td><td>11.00 (+8.95%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>172.80 (n/a)</td><td>161.82 (n/a)</td><td>160.70 (n/a)</td><td>147.10 (n/a)</td><td>10.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 <b>(+38.56%)</b></td><td>0.20 (+17.31%)</td><td>0.18 (+11.29%)</td><td>0.14 (-11.54%)</td><td>0.06 <b>(+167.34%)</b></td><td>237.60 (+13.04%)</td><td>176.94 (-10.42%)</td><td>184.60 (-10.17%)</td><td>115.00 <b>(-27.85%)</b></td><td>46.38 <b>(+116.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.20 (n/a)</td><td>197.52 (n/a)</td><td>205.50 (n/a)</td><td>159.40 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (-14.82%)</td><td>0.17 (-6.89%)</td><td>0.17 (-6.64%)</td><td>0.15 (+7.34%)</td><td>0.02 <b>(-42.47%)</b></td><td>221.10 (-6.87%)</td><td>192.46 (+5.15%)</td><td>193.10 (+7.10%)</td><td>157.00 (+17.43%)</td><td>22.97 <b>(-37.98%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>237.40 (n/a)</td><td>183.04 (n/a)</td><td>180.30 (n/a)</td><td>133.70 (n/a)</td><td>37.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 <b>(+57.88%)</b></td><td>0.18 <b>(+22.69%)</b></td><td>0.16 (+1.57%)</td><td>0.15 <b>(+32.85%)</b></td><td>0.06 <b>(+95.94%)</b></td><td>217.10 <b>(-24.72%)</b></td><td>187.38 (-16.55%)</td><td>202.40 (-1.56%)</td><td>116.30 <b>(-36.62%)</b></td><td>41.43 (-8.59%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>288.40 (n/a)</td><td>224.54 (n/a)</td><td>205.60 (n/a)</td><td>183.50 (n/a)</td><td>45.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (-7.12%)</td><td>0.17 (-2.83%)</td><td>0.18 (+9.29%)</td><td>0.14 (+3.40%)</td><td>0.02 <b>(-33.28%)</b></td><td>236.40 (-3.27%)</td><td>196.52 (+1.25%)</td><td>184.40 (-8.53%)</td><td>166.00 (+7.65%)</td><td>28.10 <b>(-27.11%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>244.40 (n/a)</td><td>194.10 (n/a)</td><td>201.60 (n/a)</td><td>154.20 (n/a)</td><td>38.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (-0.31%)</td><td>0.18 (-0.04%)</td><td>0.18 (+0.16%)</td><td>0.18 (-0.14%)</td><td>0.00 (-14.94%)</td><td>47761.80 (+0.14%)</td><td>47536.14 (+0.04%)</td><td>47475.10 (-0.16%)</td><td>47446.10 (+0.31%)</td><td>132.77 (-14.53%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47695.60 (n/a)</td><td>47515.50 (n/a)</td><td>47549.50 (n/a)</td><td>47299.20 (n/a)</td><td>155.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (+0.18%)</td><td>0.18 (+0.19%)</td><td>0.18 (+0.15%)</td><td>0.18 (+0.24%)</td><td>0.00 (-11.76%)</td><td>47546.90 (-0.24%)</td><td>47501.00 (-0.19%)</td><td>47513.20 (-0.15%)</td><td>47446.90 (-0.18%)</td><td>41.73 (-12.06%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47662.10 (n/a)</td><td>47589.98 (n/a)</td><td>47583.20 (n/a)</td><td>47530.20 (n/a)</td><td>47.46 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (+0.01%)</td><td>0.11 (+0.01%)</td><td>0.11 (-0.00%)</td><td>0.11 (+0.06%)</td><td>0.00 <b>(-46.24%)</b></td><td>375603.20 (-0.06%)</td><td>375485.50 (-0.01%)</td><td>375497.30 (+0.00%)</td><td>375340.30 (-0.01%)</td><td>95.39 <b>(-46.25%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>375832.60 (n/a)</td><td>375530.42 (n/a)</td><td>375479.00 (n/a)</td><td>375393.50 (n/a)</td><td>177.47 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (-9.99%)</td><td>0.14 <b>(-26.79%)</b></td><td>0.14 <b>(-29.41%)</b></td><td>0.11 <b>(-35.22%)</b></td><td>0.03 <b>(+99.60%)</b></td><td>223.40 <b>(+54.39%)</b></td><td>179.64 <b>(+40.41%)</b></td><td>180.20 <b>(+41.67%)</b></td><td>128.80 (+11.13%)</td><td>34.38 <b>(+228.61%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>144.70 (n/a)</td><td>127.94 (n/a)</td><td>127.20 (n/a)</td><td>115.90 (n/a)</td><td>10.46 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 <b>(-33.47%)</b></td><td>0.26 <b>(-30.33%)</b></td><td>0.27 <b>(-28.30%)</b></td><td>0.23 <b>(-30.87%)</b></td><td>0.02 <b>(-40.90%)</b></td><td>213.10 <b>(+44.67%)</b></td><td>187.58 <b>(+43.30%)</b></td><td>178.90 <b>(+39.44%)</b></td><td>175.70 <b>(+50.30%)</b></td><td>15.51 <b>(+28.32%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.03 (n/a)</td><td>147.30 (n/a)</td><td>130.90 (n/a)</td><td>128.30 (n/a)</td><td>116.90 (n/a)</td><td>12.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.36 (-2.24%)</td><td>12.69 (-4.91%)</td><td>12.66 (-4.76%)</td><td>12.02 (-8.20%)</td><td>0.51 <b>(+141.77%)</b></td><td>872.10 (+8.93%)</td><td>827.18 (+5.28%)</td><td>828.10 (+5.00%)</td><td>784.90 (+2.29%)</td><td>33.29 <b>(+170.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.67 (n/a)</td><td>13.35 (n/a)</td><td>13.29 (n/a)</td><td>13.10 (n/a)</td><td>0.21 (n/a)</td><td>800.60 (n/a)</td><td>785.66 (n/a)</td><td>788.70 (n/a)</td><td>767.30 (n/a)</td><td>12.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (-11.53%)</td><td>0.24 <b>(-24.60%)</b></td><td>0.23 <b>(-28.62%)</b></td><td>0.20 <b>(-25.34%)</b></td><td>0.04 <b>(+37.71%)</b></td><td>203.60 <b>(+33.95%)</b></td><td>175.00 <b>(+34.24%)</b></td><td>178.80 <b>(+40.13%)</b></td><td>135.30 (+13.03%)</td><td>25.53 <b>(+100.68%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>152.00 (n/a)</td><td>130.36 (n/a)</td><td>127.60 (n/a)</td><td>119.70 (n/a)</td><td>12.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (-1.37%)</td><td>0.03 (-19.98%)</td><td>0.03 <b>(-28.54%)</b></td><td>0.02 <b>(-36.44%)</b></td><td>0.01 <b>(+84.70%)</b></td><td>237.30 <b>(+57.36%)</b></td><td>174.28 <b>(+30.02%)</b></td><td>177.40 <b>(+39.91%)</b></td><td>119.50 (+1.36%)</td><td>42.82 <b>(+186.02%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>150.80 (n/a)</td><td>134.04 (n/a)</td><td>126.80 (n/a)</td><td>117.90 (n/a)</td><td>14.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-13.78%)</td><td>0.02 <b>(-23.13%)</b></td><td>0.03 <b>(-21.60%)</b></td><td>0.01 <b>(-55.32%)</b></td><td>0.01 <b>(+71.96%)</b></td><td>360.90 <b>(+123.74%)</b></td><td>197.16 <b>(+44.57%)</b></td><td>163.20 <b>(+27.60%)</b></td><td>134.40 (+15.96%)</td><td>92.84 <b>(+373.90%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>161.30 (n/a)</td><td>136.38 (n/a)</td><td>127.90 (n/a)</td><td>115.90 (n/a)</td><td>19.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (-11.93%)</td><td>0.04 (-0.34%)</td><td>0.04 (+6.82%)</td><td>0.03 (-9.38%)</td><td>0.01 (-5.05%)</td><td>226.40 (+10.33%)</td><td>174.00 (+0.60%)</td><td>158.40 (-6.38%)</td><td>157.20 (+13.58%)</td><td>29.73 <b>(+20.94%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>172.96 (n/a)</td><td>169.20 (n/a)</td><td>138.40 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (+0.60%)</td><td>0.03 (-16.87%)</td><td>0.02 <b>(-23.39%)</b></td><td>0.02 <b>(-27.21%)</b></td><td>0.01 <b>(+88.55%)</b></td><td>189.80 <b>(+37.44%)</b></td><td>156.50 <b>(+24.70%)</b></td><td>173.50 <b>(+30.55%)</b></td><td>106.60 (-0.56%)</td><td>34.32 <b>(+156.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>138.10 (n/a)</td><td>125.50 (n/a)</td><td>132.90 (n/a)</td><td>107.20 (n/a)</td><td>13.39 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (+8.93%)</td><td>0.03 (+2.19%)</td><td>0.03 <b>(+22.84%)</b></td><td>0.01 <b>(-36.37%)</b></td><td>0.01 <b>(+68.83%)</b></td><td>362.10 <b>(+57.16%)</b></td><td>209.48 (+7.00%)</td><td>170.10 (-18.61%)</td><td>133.10 (-8.21%)</td><td>91.17 <b>(+153.07%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>195.78 (n/a)</td><td>209.00 (n/a)</td><td>145.00 (n/a)</td><td>36.03 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+2.05%)</td><td>0.02 (-10.64%)</td><td>0.02 <b>(-20.83%)</b></td><td>0.02 (-0.04%)</td><td>0.01 (+2.53%)</td><td>238.30 (+0.04%)</td><td>179.76 (+12.07%)</td><td>193.30 <b>(+26.34%)</b></td><td>117.20 (-2.01%)</td><td>47.65 (-0.48%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.20 (n/a)</td><td>160.40 (n/a)</td><td>153.00 (n/a)</td><td>119.60 (n/a)</td><td>47.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (+2.89%)</td><td>0.03 (-3.51%)</td><td>0.03 (-7.42%)</td><td>0.02 (-12.73%)</td><td>0.01 <b>(+43.00%)</b></td><td>218.40 (+14.59%)</td><td>168.36 (+5.04%)</td><td>166.40 (+7.98%)</td><td>135.30 (-2.80%)</td><td>30.77 <b>(+60.84%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.60 (n/a)</td><td>160.28 (n/a)</td><td>154.10 (n/a)</td><td>139.20 (n/a)</td><td>19.13 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+7.57%)</td><td>0.03 (-0.49%)</td><td>0.03 (+7.99%)</td><td>0.02 (-13.37%)</td><td>0.01 <b>(+118.69%)</b></td><td>209.50 (+15.43%)</td><td>159.14 (+5.27%)</td><td>137.20 (-7.36%)</td><td>121.00 (-7.07%)</td><td>43.93 <b>(+134.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.50 (n/a)</td><td>151.18 (n/a)</td><td>148.10 (n/a)</td><td>130.20 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 <b>(+41.87%)</b></td><td>0.03 <b>(+24.39%)</b></td><td>0.03 (+17.12%)</td><td>0.02 <b>(+30.62%)</b></td><td>0.00 <b>(+68.54%)</b></td><td>191.30 <b>(-23.45%)</b></td><td>167.74 (-19.24%)</td><td>171.00 (-14.63%)</td><td>134.20 <b>(-29.48%)</b></td><td>21.15 (-12.73%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>249.90 (n/a)</td><td>207.70 (n/a)</td><td>200.30 (n/a)</td><td>190.30 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-8.48%)</td><td>0.03 (-6.89%)</td><td>0.03 (-1.70%)</td><td>0.02 (-7.93%)</td><td>0.01 (-12.40%)</td><td>250.10 (+8.60%)</td><td>164.26 (+7.02%)</td><td>152.30 (+1.74%)</td><td>118.20 (+9.34%)</td><td>50.08 (+7.27%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>230.30 (n/a)</td><td>153.48 (n/a)</td><td>149.70 (n/a)</td><td>108.10 (n/a)</td><td>46.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 <b>(+43.32%)</b></td><td>0.03 <b>(+23.52%)</b></td><td>0.03 <b>(+27.36%)</b></td><td>0.02 (+16.32%)</td><td>0.01 <b>(+125.10%)</b></td><td>216.20 (-14.04%)</td><td>178.12 (-17.35%)</td><td>171.20 <b>(-21.47%)</b></td><td>130.20 <b>(-30.23%)</b></td><td>33.59 <b>(+34.99%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.50 (n/a)</td><td>215.50 (n/a)</td><td>218.00 (n/a)</td><td>186.60 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-13.94%)</td><td>0.02 (-14.59%)</td><td>0.02 (-10.41%)</td><td>0.02 <b>(-27.32%)</b></td><td>0.00 <b>(+39.37%)</b></td><td>226.90 <b>(+37.60%)</b></td><td>176.90 (+18.55%)</td><td>170.30 (+11.60%)</td><td>153.50 (+16.20%)</td><td>28.81 <b>(+131.71%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.90 (n/a)</td><td>149.22 (n/a)</td><td>152.60 (n/a)</td><td>132.10 (n/a)</td><td>12.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+10.48%)</td><td>0.02 (+1.70%)</td><td>0.02 (-3.66%)</td><td>0.02 (+5.58%)</td><td>0.00 <b>(+23.14%)</b></td><td>211.00 (-5.30%)</td><td>184.88 (-1.24%)</td><td>193.20 (+3.76%)</td><td>140.40 (-9.48%)</td><td>27.72 (+3.73%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.80 (n/a)</td><td>187.20 (n/a)</td><td>186.20 (n/a)</td><td>155.10 (n/a)</td><td>26.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-7.18%)</td><td>0.02 (-7.97%)</td><td>0.02 (-14.91%)</td><td>0.02 (+6.74%)</td><td>0.00 (-14.19%)</td><td>214.30 (-6.30%)</td><td>178.30 (+7.59%)</td><td>184.40 (+17.53%)</td><td>138.10 (+7.72%)</td><td>31.01 (-17.31%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>165.72 (n/a)</td><td>156.90 (n/a)</td><td>128.20 (n/a)</td><td>37.50 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-11.20%)</td><td>0.02 (-1.03%)</td><td>0.02 (+0.17%)</td><td>0.02 (+15.57%)</td><td>0.00 <b>(-38.74%)</b></td><td>209.30 (-13.48%)</td><td>188.62 (-0.86%)</td><td>195.80 (-0.20%)</td><td>164.20 (+12.62%)</td><td>22.06 <b>(-40.23%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.90 (n/a)</td><td>190.26 (n/a)</td><td>196.20 (n/a)</td><td>145.80 (n/a)</td><td>36.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.02 (-7.25%)</td><td>0.02 (-11.49%)</td><td>0.02 (-15.82%)</td><td>0.01 (+11.14%)</td><td>0.00 <b>(-32.57%)</b></td><td>276.50 (-10.02%)</td><td>228.44 (+9.97%)</td><td>227.70 (+18.78%)</td><td>179.40 (+7.81%)</td><td>34.70 <b>(-38.72%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>307.30 (n/a)</td><td>207.72 (n/a)</td><td>191.70 (n/a)</td><td>166.40 (n/a)</td><td>56.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (-0.13%)</td><td>0.05 <b>(-20.04%)</b></td><td>0.05 <b>(-26.09%)</b></td><td>0.04 <b>(-22.41%)</b></td><td>0.01 <b>(+36.16%)</b></td><td>220.40 <b>(+28.89%)</b></td><td>184.04 <b>(+28.02%)</b></td><td>180.60 <b>(+35.28%)</b></td><td>124.80 (+0.16%)</td><td>38.09 <b>(+74.18%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.00 (n/a)</td><td>143.76 (n/a)</td><td>133.50 (n/a)</td><td>124.60 (n/a)</td><td>21.87 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 <b>(+29.27%)</b></td><td>0.07 (-13.60%)</td><td>0.06 <b>(-29.61%)</b></td><td>0.04 <b>(-43.74%)</b></td><td>0.04 <b>(+128.83%)</b></td><td>323.70 <b>(+77.76%)</b></td><td>197.66 <b>(+33.66%)</b></td><td>189.90 <b>(+42.14%)</b></td><td>95.40 <b>(-22.69%)</b></td><td>87.71 <b>(+209.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>182.10 (n/a)</td><td>147.88 (n/a)</td><td>133.60 (n/a)</td><td>123.40 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (-6.15%)</td><td>0.05 (-4.26%)</td><td>0.05 (-5.75%)</td><td>0.04 (-2.13%)</td><td>0.01 (-5.59%)</td><td>215.40 (+2.18%)</td><td>160.94 (+4.25%)</td><td>152.70 (+6.12%)</td><td>134.50 (+6.49%)</td><td>32.67 (-0.47%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>154.38 (n/a)</td><td>143.90 (n/a)</td><td>126.30 (n/a)</td><td>32.82 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (-6.42%)</td><td>0.06 (-0.51%)</td><td>0.06 (+4.37%)</td><td>0.04 (+17.04%)</td><td>0.01 <b>(-36.33%)</b></td><td>237.90 (-14.55%)</td><td>173.08 (-4.14%)</td><td>164.10 (-4.20%)</td><td>136.90 (+6.87%)</td><td>38.19 <b>(-37.68%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>278.40 (n/a)</td><td>180.56 (n/a)</td><td>171.30 (n/a)</td><td>128.10 (n/a)</td><td>61.28 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (-7.50%)</td><td>0.05 (-15.53%)</td><td>0.05 (-3.49%)</td><td>0.03 <b>(-46.34%)</b></td><td>0.02 <b>(+38.52%)</b></td><td>326.90 <b>(+86.37%)</b></td><td>193.30 <b>(+28.92%)</b></td><td>164.80 (+3.65%)</td><td>116.20 (+8.09%)</td><td>80.53 <b>(+195.44%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.40 (n/a)</td><td>149.94 (n/a)</td><td>159.00 (n/a)</td><td>107.50 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 <b>(+25.20%)</b></td><td>0.06 (-7.60%)</td><td>0.06 (-7.12%)</td><td>0.04 <b>(-24.27%)</b></td><td>0.02 <b>(+229.25%)</b></td><td>251.60 <b>(+32.07%)</b></td><td>192.08 (+15.66%)</td><td>176.90 (+7.67%)</td><td>120.30 <b>(-20.12%)</b></td><td>55.17 <b>(+257.63%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>190.50 (n/a)</td><td>166.08 (n/a)</td><td>164.30 (n/a)</td><td>150.60 (n/a)</td><td>15.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 <b>(+31.36%)</b></td><td>0.06 (+9.80%)</td><td>0.05 (-2.35%)</td><td>0.05 (+10.87%)</td><td>0.01 <b>(+87.79%)</b></td><td>172.20 (-9.80%)</td><td>149.48 (-7.55%)</td><td>155.10 (+2.44%)</td><td>110.20 <b>(-23.90%)</b></td><td>24.98 <b>(+28.24%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.90 (n/a)</td><td>161.68 (n/a)</td><td>151.40 (n/a)</td><td>144.80 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 <b>(-21.50%)</b></td><td>0.05 (+1.28%)</td><td>0.05 (+1.68%)</td><td>0.04 <b>(+42.21%)</b></td><td>0.00 <b>(-72.99%)</b></td><td>206.40 <b>(-29.70%)</b></td><td>177.14 (-9.68%)</td><td>168.90 (-1.63%)</td><td>164.90 <b>(+27.34%)</b></td><td>17.01 <b>(-75.61%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>293.60 (n/a)</td><td>196.12 (n/a)</td><td>171.70 (n/a)</td><td>129.50 (n/a)</td><td>69.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (-10.19%)</td><td>0.05 (-7.70%)</td><td>0.05 (-4.60%)</td><td>0.04 (-11.37%)</td><td>0.01 (-3.33%)</td><td>198.80 (+12.83%)</td><td>172.18 (+8.59%)</td><td>171.50 (+4.83%)</td><td>143.90 (+11.38%)</td><td>23.94 <b>(+21.65%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.20 (n/a)</td><td>158.56 (n/a)</td><td>163.60 (n/a)</td><td>129.20 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.07 (-0.74%)</td><td>0.05 (-5.07%)</td><td>0.05 (-3.48%)</td><td>0.04 (-10.96%)</td><td>0.01 <b>(+22.08%)</b></td><td>210.90 (+12.30%)</td><td>176.06 (+6.56%)</td><td>175.50 (+3.60%)</td><td>129.40 (+0.78%)</td><td>31.08 <b>(+40.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>165.22 (n/a)</td><td>169.40 (n/a)</td><td>128.40 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 <b>(-34.05%)</b></td><td>0.05 (-7.30%)</td><td>0.05 (-3.02%)</td><td>0.04 (+8.62%)</td><td>0.00 <b>(-72.82%)</b></td><td>191.40 (-7.94%)</td><td>166.58 (+1.28%)</td><td>159.30 (+3.11%)</td><td>151.70 <b>(+51.70%)</b></td><td>16.61 <b>(-62.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>207.90 (n/a)</td><td>164.48 (n/a)</td><td>154.50 (n/a)</td><td>100.00 (n/a)</td><td>44.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 <b>(-41.16%)</b></td><td>0.04 (-16.93%)</td><td>0.04 (+4.50%)</td><td>0.03 (-10.71%)</td><td>0.01 <b>(-56.22%)</b></td><td>342.50 (+12.00%)</td><td>226.48 (+11.59%)</td><td>206.90 (-4.35%)</td><td>179.10 <b>(+69.92%)</b></td><td>66.94 (-11.65%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>305.80 (n/a)</td><td>202.96 (n/a)</td><td>216.30 (n/a)</td><td>105.40 (n/a)</td><td>75.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.06 (+7.66%)</td><td>0.05 (+1.74%)</td><td>0.05 (+9.98%)</td><td>0.03 <b>(-27.57%)</b></td><td>0.01 <b>(+103.64%)</b></td><td>286.10 <b>(+38.01%)</b></td><td>183.68 (+3.24%)</td><td>163.70 (-9.06%)</td><td>144.80 (-7.12%)</td><td>58.16 <b>(+176.30%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>177.92 (n/a)</td><td>180.00 (n/a)</td><td>155.90 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 <b>(-41.06%)</b></td><td>0.04 (-16.58%)</td><td>0.04 (-9.46%)</td><td>0.04 (+11.64%)</td><td>0.00 <b>(-87.14%)</b></td><td>211.80 (-10.41%)</td><td>203.60 (+12.14%)</td><td>207.30 (+10.44%)</td><td>187.40 <b>(+69.59%)</b></td><td>9.65 <b>(-79.91%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>236.40 (n/a)</td><td>181.56 (n/a)</td><td>187.70 (n/a)</td><td>110.50 (n/a)</td><td>48.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.05 (+1.19%)</td><td>0.04 (-8.13%)</td><td>0.04 (-9.39%)</td><td>0.03 <b>(-25.13%)</b></td><td>0.01 <b>(+78.17%)</b></td><td>307.20 <b>(+33.57%)</b></td><td>224.14 (+12.37%)</td><td>221.40 (+10.37%)</td><td>165.70 (-1.19%)</td><td>53.15 <b>(+140.51%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>230.00 (n/a)</td><td>199.46 (n/a)</td><td>200.60 (n/a)</td><td>167.70 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 <b>(+30.44%)</b></td><td>0.11 (+19.58%)</td><td>0.10 (+12.45%)</td><td>0.08 (+16.24%)</td><td>0.02 <b>(+59.82%)</b></td><td>199.80 (-13.99%)</td><td>158.08 (-15.56%)</td><td>159.60 (-11.09%)</td><td>122.60 <b>(-23.33%)</b></td><td>28.12 (+2.91%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>187.22 (n/a)</td><td>179.50 (n/a)</td><td>159.90 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (-0.31%)</td><td>0.15 (-7.71%)</td><td>0.14 (-17.98%)</td><td>0.12 (+11.47%)</td><td>0.03 (-12.34%)</td><td>202.50 (-10.28%)</td><td>173.50 (+6.87%)</td><td>178.40 <b>(+21.94%)</b></td><td>125.10 (+0.32%)</td><td>31.74 <b>(-21.85%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>225.70 (n/a)</td><td>162.34 (n/a)</td><td>146.30 (n/a)</td><td>124.70 (n/a)</td><td>40.62 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 (-17.00%)</td><td>0.10 (-12.37%)</td><td>0.11 (-12.95%)</td><td>0.06 <b>(-27.83%)</b></td><td>0.03 (-4.38%)</td><td>294.60 <b>(+38.57%)</b></td><td>178.90 (+17.34%)</td><td>148.80 (+14.90%)</td><td>134.80 <b>(+20.46%)</b></td><td>66.99 <b>(+59.46%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>212.60 (n/a)</td><td>152.46 (n/a)</td><td>129.50 (n/a)</td><td>111.90 (n/a)</td><td>42.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (-15.55%)</td><td>0.12 (+1.12%)</td><td>0.12 (+0.90%)</td><td>0.10 <b>(+23.42%)</b></td><td>0.02 <b>(-48.53%)</b></td><td>203.30 (-18.97%)</td><td>168.72 (-5.87%)</td><td>169.00 (-0.88%)</td><td>134.70 (+18.37%)</td><td>25.10 <b>(-50.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>250.90 (n/a)</td><td>179.24 (n/a)</td><td>170.50 (n/a)</td><td>113.80 (n/a)</td><td>50.51 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 <b>(+21.08%)</b></td><td>0.12 (+16.20%)</td><td>0.13 (+17.94%)</td><td>0.09 (-2.48%)</td><td>0.02 <b>(+128.26%)</b></td><td>180.80 (+2.55%)</td><td>136.14 (-11.88%)</td><td>127.00 (-15.22%)</td><td>113.20 (-17.37%)</td><td>28.22 <b>(+89.67%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>154.50 (n/a)</td><td>149.80 (n/a)</td><td>137.00 (n/a)</td><td>14.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 <b>(-29.44%)</b></td><td>0.11 <b>(-23.45%)</b></td><td>0.10 <b>(-32.51%)</b></td><td>0.09 (-7.73%)</td><td>0.01 <b>(-57.73%)</b></td><td>215.70 (+8.39%)</td><td>191.48 <b>(+25.92%)</b></td><td>200.00 <b>(+48.15%)</b></td><td>158.20 <b>(+41.76%)</b></td><td>24.37 <b>(-37.10%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>199.00 (n/a)</td><td>152.06 (n/a)</td><td>135.00 (n/a)</td><td>111.60 (n/a)</td><td>38.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (+16.37%)</td><td>0.11 (+8.50%)</td><td>0.10 (-3.83%)</td><td>0.09 <b>(+29.99%)</b></td><td>0.02 (+4.73%)</td><td>184.60 <b>(-23.05%)</b></td><td>152.14 (-9.02%)</td><td>159.10 (+3.99%)</td><td>113.10 (-14.12%)</td><td>28.59 <b>(-33.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.90 (n/a)</td><td>167.22 (n/a)</td><td>153.00 (n/a)</td><td>131.70 (n/a)</td><td>42.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.12 <b>(-30.44%)</b></td><td>0.11 (-17.29%)</td><td>0.11 (-13.37%)</td><td>0.09 (-5.69%)</td><td>0.01 <b>(-58.76%)</b></td><td>201.80 (+5.99%)</td><td>177.44 (+16.29%)</td><td>173.60 (+15.43%)</td><td>147.80 <b>(+43.77%)</b></td><td>23.25 <b>(-37.61%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>190.40 (n/a)</td><td>152.58 (n/a)</td><td>150.40 (n/a)</td><td>102.80 (n/a)</td><td>37.26 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (-16.87%)</td><td>0.09 (-15.35%)</td><td>0.10 (-13.49%)</td><td>0.08 (-1.28%)</td><td>0.01 <b>(-40.47%)</b></td><td>199.30 (+1.27%)</td><td>175.44 (+16.42%)</td><td>168.10 (+15.61%)</td><td>151.20 <b>(+20.29%)</b></td><td>21.56 <b>(-25.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>150.70 (n/a)</td><td>145.40 (n/a)</td><td>125.70 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 <b>(+23.57%)</b></td><td>0.11 (-12.74%)</td><td>0.09 <b>(-26.32%)</b></td><td>0.08 (-13.36%)</td><td>0.04 <b>(+93.80%)</b></td><td>220.80 (+15.42%)</td><td>186.08 <b>(+21.02%)</b></td><td>204.40 <b>(+35.72%)</b></td><td>103.50 (-19.14%)</td><td>47.25 <b>(+76.43%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>191.30 (n/a)</td><td>153.76 (n/a)</td><td>150.60 (n/a)</td><td>128.00 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (-9.90%)</td><td>0.09 (-8.94%)</td><td>0.10 (-1.29%)</td><td>0.06 <b>(-28.21%)</b></td><td>0.02 <b>(+31.47%)</b></td><td>282.50 <b>(+39.30%)</b></td><td>191.96 (+13.67%)</td><td>164.00 (+1.30%)</td><td>147.40 (+10.99%)</td><td>55.16 <b>(+106.19%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.80 (n/a)</td><td>168.88 (n/a)</td><td>161.90 (n/a)</td><td>132.80 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (+2.95%)</td><td>0.09 (-14.31%)</td><td>0.08 <b>(-26.89%)</b></td><td>0.06 (-1.56%)</td><td>0.03 (+0.50%)</td><td>307.40 (+1.59%)</td><td>215.78 (+15.79%)</td><td>213.90 <b>(+36.76%)</b></td><td>126.80 (-2.91%)</td><td>64.35 (-7.40%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>302.60 (n/a)</td><td>186.36 (n/a)</td><td>156.40 (n/a)</td><td>130.60 (n/a)</td><td>69.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (+5.21%)</td><td>0.10 (-7.67%)</td><td>0.11 (-6.18%)</td><td>0.06 <b>(-34.28%)</b></td><td>0.03 <b>(+56.89%)</b></td><td>288.60 <b>(+52.13%)</b></td><td>177.84 (+16.24%)</td><td>150.60 (+6.58%)</td><td>113.80 (-4.93%)</td><td>68.36 <b>(+129.01%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.70 (n/a)</td><td>153.00 (n/a)</td><td>141.30 (n/a)</td><td>119.70 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (-5.57%)</td><td>0.07 (-19.58%)</td><td>0.08 (-9.08%)</td><td>0.05 <b>(-41.86%)</b></td><td>0.02 <b>(+90.35%)</b></td><td>369.50 <b>(+72.02%)</b></td><td>253.52 <b>(+33.77%)</b></td><td>206.60 (+9.95%)</td><td>169.10 (+5.89%)</td><td>85.96 <b>(+249.82%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>189.52 (n/a)</td><td>187.90 (n/a)</td><td>159.70 (n/a)</td><td>24.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.09 (-10.22%)</td><td>0.08 (-9.23%)</td><td>0.07 (-13.10%)</td><td>0.07 (-5.06%)</td><td>0.01 <b>(-21.96%)</b></td><td>230.70 (+5.34%)</td><td>208.98 (+9.79%)</td><td>221.40 (+15.07%)</td><td>182.00 (+11.38%)</td><td>21.82 (-8.24%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>190.34 (n/a)</td><td>192.40 (n/a)</td><td>163.40 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 <b>(-24.19%)</b></td><td>0.20 (-5.67%)</td><td>0.20 (-6.32%)</td><td>0.18 <b>(+26.50%)</b></td><td>0.01 <b>(-82.79%)</b></td><td>178.20 <b>(-20.94%)</b></td><td>167.34 (+1.10%)</td><td>165.60 (+6.77%)</td><td>158.60 <b>(+31.95%)</b></td><td>7.46 <b>(-82.17%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>225.40 (n/a)</td><td>165.52 (n/a)</td><td>155.10 (n/a)</td><td>120.20 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.26 (-10.12%)</td><td>0.23 (+8.74%)</td><td>0.22 <b>(+20.71%)</b></td><td>0.21 <b>(+59.32%)</b></td><td>0.02 <b>(-66.29%)</b></td><td>157.60 <b>(-37.24%)</b></td><td>145.62 (-14.71%)</td><td>148.30 (-17.15%)</td><td>123.70 (+11.24%)</td><td>12.95 <b>(-76.44%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>251.10 (n/a)</td><td>170.74 (n/a)</td><td>179.00 (n/a)</td><td>111.20 (n/a)</td><td>54.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (-18.24%)</td><td>0.22 (-15.33%)</td><td>0.21 <b>(-23.96%)</b></td><td>0.18 (-9.53%)</td><td>0.04 <b>(-40.01%)</b></td><td>223.70 (+10.52%)</td><td>186.90 (+15.47%)</td><td>197.90 <b>(+31.50%)</b></td><td>153.10 <b>(+22.28%)</b></td><td>29.12 <b>(-22.42%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>202.40 (n/a)</td><td>161.86 (n/a)</td><td>150.50 (n/a)</td><td>125.20 (n/a)</td><td>37.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (+9.98%)</td><td>0.23 (+11.63%)</td><td>0.24 (+2.01%)</td><td>0.17 <b>(+24.61%)</b></td><td>0.04 <b>(-27.44%)</b></td><td>187.50 (-19.73%)</td><td>144.40 (-13.12%)</td><td>139.00 (-1.97%)</td><td>119.80 (-9.10%)</td><td>25.40 <b>(-43.46%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>233.60 (n/a)</td><td>166.20 (n/a)</td><td>141.80 (n/a)</td><td>131.80 (n/a)</td><td>44.93 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.31 (-1.79%)</td><td>0.24 (-1.71%)</td><td>0.23 (-9.54%)</td><td>0.19 <b>(+60.91%)</b></td><td>0.05 <b>(-38.48%)</b></td><td>217.20 <b>(-37.85%)</b></td><td>179.02 (-7.06%)</td><td>175.40 (+10.59%)</td><td>133.50 (+1.83%)</td><td>31.67 <b>(-64.41%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>349.50 (n/a)</td><td>192.62 (n/a)</td><td>158.60 (n/a)</td><td>131.10 (n/a)</td><td>88.99 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.26 (+10.21%)</td><td>0.21 <b>(+21.33%)</b></td><td>0.21 <b>(+36.62%)</b></td><td>0.15 (+1.50%)</td><td>0.04 (+8.67%)</td><td>216.00 (-1.46%)</td><td>160.60 (-17.45%)</td><td>158.40 <b>(-26.80%)</b></td><td>124.80 (-9.24%)</td><td>34.73 (-2.54%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>219.20 (n/a)</td><td>194.54 (n/a)</td><td>216.40 (n/a)</td><td>137.50 (n/a)</td><td>35.63 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 <b>(-25.79%)</b></td><td>0.19 (-16.09%)</td><td>0.19 (-17.55%)</td><td>0.17 (-8.67%)</td><td>0.02 <b>(-50.93%)</b></td><td>222.40 (+9.50%)</td><td>192.98 (+16.90%)</td><td>192.60 <b>(+21.28%)</b></td><td>164.40 <b>(+34.75%)</b></td><td>22.52 <b>(-27.32%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>203.10 (n/a)</td><td>165.08 (n/a)</td><td>158.80 (n/a)</td><td>122.00 (n/a)</td><td>30.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.23 (-8.72%)</td><td>0.19 (-4.98%)</td><td>0.19 (-9.22%)</td><td>0.15 (-6.94%)</td><td>0.03 (-14.58%)</td><td>219.70 (+7.49%)</td><td>173.52 (+4.72%)</td><td>169.80 (+10.12%)</td><td>144.20 (+9.57%)</td><td>30.99 (-2.87%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>204.40 (n/a)</td><td>165.70 (n/a)</td><td>154.20 (n/a)</td><td>131.60 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 (-7.72%)</td><td>0.21 (-9.64%)</td><td>0.22 (-7.51%)</td><td>0.17 (-11.07%)</td><td>0.04 (+2.66%)</td><td>223.00 (+12.46%)</td><td>177.80 (+11.53%)</td><td>166.90 (+8.10%)</td><td>132.30 (+8.35%)</td><td>35.86 <b>(+27.01%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>198.30 (n/a)</td><td>159.42 (n/a)</td><td>154.40 (n/a)</td><td>122.10 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.22 <b>(-23.39%)</b></td><td>0.19 (-1.80%)</td><td>0.20 (+15.07%)</td><td>0.15 (-6.45%)</td><td>0.03 <b>(-46.18%)</b></td><td>223.40 (+6.89%)</td><td>172.90 (-0.53%)</td><td>163.40 (-13.13%)</td><td>151.70 <b>(+30.55%)</b></td><td>28.73 (-19.46%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>209.00 (n/a)</td><td>173.82 (n/a)</td><td>188.10 (n/a)</td><td>116.20 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 <b>(-28.20%)</b></td><td>0.17 <b>(-20.90%)</b></td><td>0.17 <b>(-21.51%)</b></td><td>0.16 (-13.79%)</td><td>0.02 <b>(-57.40%)</b></td><td>217.20 (+15.96%)</td><td>201.88 <b>(+24.66%)</b></td><td>210.20 <b>(+27.39%)</b></td><td>175.90 <b>(+39.27%)</b></td><td>16.74 <b>(-31.42%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>187.30 (n/a)</td><td>161.94 (n/a)</td><td>165.00 (n/a)</td><td>126.30 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 <b>(-21.58%)</b></td><td>0.17 (-4.58%)</td><td>0.17 (+7.18%)</td><td>0.12 (-2.33%)</td><td>0.03 <b>(-37.03%)</b></td><td>265.10 (+2.39%)</td><td>203.74 (+2.23%)</td><td>192.80 (-6.72%)</td><td>165.10 <b>(+27.49%)</b></td><td>40.84 (-15.52%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>258.90 (n/a)</td><td>199.30 (n/a)</td><td>206.70 (n/a)</td><td>129.50 (n/a)</td><td>48.34 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (-12.99%)</td><td>0.18 (-14.03%)</td><td>0.17 (-16.05%)</td><td>0.17 (-6.44%)</td><td>0.01 <b>(-40.96%)</b></td><td>207.80 (+6.89%)</td><td>198.50 (+15.95%)</td><td>200.70 (+19.11%)</td><td>181.90 (+14.91%)</td><td>10.56 <b>(-27.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>194.40 (n/a)</td><td>171.20 (n/a)</td><td>168.50 (n/a)</td><td>158.30 (n/a)</td><td>14.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 <b>(-24.24%)</b></td><td>0.16 (-6.70%)</td><td>0.16 (-0.98%)</td><td>0.15 (+3.38%)</td><td>0.01 <b>(-66.11%)</b></td><td>217.90 (-3.28%)</td><td>203.50 (+3.94%)</td><td>206.50 (+0.98%)</td><td>176.30 <b>(+31.96%)</b></td><td>16.10 <b>(-56.26%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.30 (n/a)</td><td>195.78 (n/a)</td><td>204.50 (n/a)</td><td>133.60 (n/a)</td><td>36.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (+1.02%)</td><td>0.13 (+2.97%)</td><td>0.13 (+4.42%)</td><td>0.08 (-14.98%)</td><td>0.03 <b>(+34.11%)</b></td><td>254.00 (+17.59%)</td><td>166.18 (+0.44%)</td><td>155.10 (-4.26%)</td><td>123.30 (-0.96%)</td><td>52.23 <b>(+58.20%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>216.00 (n/a)</td><td>165.46 (n/a)</td><td>162.00 (n/a)</td><td>124.50 (n/a)</td><td>33.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.16 (-2.78%)</td><td>0.12 (-7.73%)</td><td>0.12 (-5.56%)</td><td>0.08 <b>(-23.01%)</b></td><td>0.03 <b>(+31.15%)</b></td><td>257.80 <b>(+29.87%)</b></td><td>182.76 (+11.33%)</td><td>177.20 (+5.85%)</td><td>131.00 (+2.83%)</td><td>46.53 <b>(+82.84%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>198.50 (n/a)</td><td>164.16 (n/a)</td><td>167.40 (n/a)</td><td>127.40 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (+10.54%)</td><td>0.15 (+5.73%)</td><td>0.16 (+8.87%)</td><td>0.10 (+5.25%)</td><td>0.03 <b>(+23.32%)</b></td><td>202.80 (-5.01%)</td><td>144.06 (-4.53%)</td><td>124.80 (-8.10%)</td><td>115.50 (-9.55%)</td><td>36.75 (+2.87%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>213.50 (n/a)</td><td>150.90 (n/a)</td><td>135.80 (n/a)</td><td>127.70 (n/a)</td><td>35.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 <b>(+20.64%)</b></td><td>0.15 (+14.32%)</td><td>0.16 <b>(+24.26%)</b></td><td>0.09 (-9.24%)</td><td>0.04 <b>(+42.81%)</b></td><td>234.00 (+10.17%)</td><td>150.78 (-9.56%)</td><td>131.40 (-19.53%)</td><td>106.90 (-17.13%)</td><td>49.60 <b>(+37.62%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>212.40 (n/a)</td><td>166.72 (n/a)</td><td>163.30 (n/a)</td><td>129.00 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.18 (+18.17%)</td><td>0.14 <b>(+30.05%)</b></td><td>0.16 <b>(+51.80%)</b></td><td>0.07 (-10.80%)</td><td>0.04 <b>(+54.33%)</b></td><td>284.00 (+12.12%)</td><td>161.02 (-17.96%)</td><td>126.70 <b>(-34.11%)</b></td><td>110.90 (-15.34%)</td><td>70.91 <b>(+58.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>253.30 (n/a)</td><td>196.26 (n/a)</td><td>192.30 (n/a)</td><td>131.00 (n/a)</td><td>44.70 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 <b>(-27.46%)</b></td><td>0.13 (+4.22%)</td><td>0.13 <b>(+21.73%)</b></td><td>0.12 (+14.56%)</td><td>0.01 <b>(-78.82%)</b></td><td>176.70 (-12.70%)</td><td>159.04 (-8.66%)</td><td>155.80 (-17.83%)</td><td>151.00 <b>(+37.90%)</b></td><td>10.12 <b>(-73.61%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>202.40 (n/a)</td><td>174.12 (n/a)</td><td>189.60 (n/a)</td><td>109.50 (n/a)</td><td>38.34 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (-4.55%)</td><td>0.11 (-9.35%)</td><td>0.11 (-12.14%)</td><td>0.10 (-7.74%)</td><td>0.02 (+10.38%)</td><td>209.10 (+8.40%)</td><td>185.80 (+10.93%)</td><td>188.00 (+13.80%)</td><td>142.70 (+4.77%)</td><td>27.30 <b>(+26.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>192.90 (n/a)</td><td>167.50 (n/a)</td><td>165.20 (n/a)</td><td>136.20 (n/a)</td><td>21.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (-17.39%)</td><td>0.10 <b>(-25.00%)</b></td><td>0.11 <b>(-23.05%)</b></td><td>0.08 <b>(-26.50%)</b></td><td>0.02 (+17.54%)</td><td>242.70 <b>(+36.04%)</b></td><td>201.16 <b>(+34.88%)</b></td><td>186.60 <b>(+29.94%)</b></td><td>163.60 <b>(+21.10%)</b></td><td>32.75 <b>(+92.59%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>178.40 (n/a)</td><td>149.14 (n/a)</td><td>143.60 (n/a)</td><td>135.10 (n/a)</td><td>17.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (+7.46%)</td><td>0.17 (+0.83%)</td><td>0.17 (-5.15%)</td><td>0.14 (+9.76%)</td><td>0.03 (-0.73%)</td><td>172.00 (-8.90%)</td><td>146.34 (-1.15%)</td><td>142.00 (+5.42%)</td><td>118.70 (-6.97%)</td><td>22.62 (-13.50%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>188.80 (n/a)</td><td>148.04 (n/a)</td><td>134.70 (n/a)</td><td>127.60 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (-5.83%)</td><td>0.15 (-12.41%)</td><td>0.14 (-14.48%)</td><td>0.10 <b>(-29.68%)</b></td><td>0.04 <b>(+54.99%)</b></td><td>240.60 <b>(+42.20%)</b></td><td>171.96 (+18.32%)</td><td>171.00 (+16.96%)</td><td>131.70 (+6.21%)</td><td>44.73 <b>(+128.46%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>169.20 (n/a)</td><td>145.34 (n/a)</td><td>146.20 (n/a)</td><td>124.00 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (-5.19%)</td><td>0.17 (+12.67%)</td><td>0.17 <b>(+25.25%)</b></td><td>0.15 <b>(+31.76%)</b></td><td>0.01 <b>(-59.89%)</b></td><td>161.50 <b>(-24.11%)</b></td><td>147.34 (-14.05%)</td><td>143.20 <b>(-20.13%)</b></td><td>132.60 (+5.49%)</td><td>11.60 <b>(-67.46%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>212.80 (n/a)</td><td>171.42 (n/a)</td><td>179.30 (n/a)</td><td>125.70 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (+18.92%)</td><td>0.17 <b>(+24.14%)</b></td><td>0.18 (+14.99%)</td><td>0.15 <b>(+33.07%)</b></td><td>0.02 <b>(-29.50%)</b></td><td>163.50 <b>(-24.83%)</b></td><td>142.82 <b>(-20.80%)</b></td><td>139.30 (-13.05%)</td><td>129.80 (-15.88%)</td><td>14.35 <b>(-56.00%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.50 (n/a)</td><td>180.32 (n/a)</td><td>160.20 (n/a)</td><td>154.30 (n/a)</td><td>32.62 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (+18.26%)</td><td>0.18 <b>(+35.02%)</b></td><td>0.19 <b>(+55.76%)</b></td><td>0.14 <b>(+22.29%)</b></td><td>0.02 (+10.72%)</td><td>179.20 (-18.21%)</td><td>140.92 <b>(-26.19%)</b></td><td>127.80 <b>(-35.78%)</b></td><td>126.90 (-15.46%)</td><td>22.56 <b>(-24.84%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>219.10 (n/a)</td><td>190.92 (n/a)</td><td>199.00 (n/a)</td><td>150.10 (n/a)</td><td>30.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.20 (+0.45%)</td><td>0.16 (-1.94%)</td><td>0.16 (-2.05%)</td><td>0.11 (-5.60%)</td><td>0.03 (-0.91%)</td><td>214.00 (+5.94%)</td><td>159.92 (+2.19%)</td><td>157.20 (+2.08%)</td><td>124.50 (-0.40%)</td><td>35.80 (+7.32%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>202.00 (n/a)</td><td>156.50 (n/a)</td><td>154.00 (n/a)</td><td>125.00 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (-6.92%)</td><td>0.14 (-1.60%)</td><td>0.14 (-5.10%)</td><td>0.13 (+8.15%)</td><td>0.01 <b>(-58.03%)</b></td><td>185.80 (-7.52%)</td><td>171.88 (+0.49%)</td><td>170.20 (+5.39%)</td><td>161.20 (+7.40%)</td><td>9.51 <b>(-58.07%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>200.90 (n/a)</td><td>171.04 (n/a)</td><td>161.50 (n/a)</td><td>150.10 (n/a)</td><td>22.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.19 (+7.67%)</td><td>0.15 (+4.58%)</td><td>0.14 (-13.98%)</td><td>0.11 <b>(+62.66%)</b></td><td>0.03 <b>(-37.08%)</b></td><td>226.30 <b>(-38.52%)</b></td><td>173.20 (-13.61%)</td><td>169.70 (+16.23%)</td><td>131.10 (-7.09%)</td><td>35.53 <b>(-63.46%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>368.10 (n/a)</td><td>200.48 (n/a)</td><td>146.00 (n/a)</td><td>141.10 (n/a)</td><td>97.24 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.15 (-5.65%)</td><td>0.12 (+3.99%)</td><td>0.12 (+14.48%)</td><td>0.10 (+1.05%)</td><td>0.02 <b>(-25.89%)</b></td><td>186.10 (-1.01%)</td><td>154.82 (-5.12%)</td><td>152.80 (-12.69%)</td><td>125.40 (+6.00%)</td><td>23.13 <b>(-23.44%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>188.00 (n/a)</td><td>163.18 (n/a)</td><td>175.00 (n/a)</td><td>118.30 (n/a)</td><td>30.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.17 (+12.74%)</td><td>0.13 (+11.82%)</td><td>0.14 <b>(+26.48%)</b></td><td>0.09 (-5.14%)</td><td>0.03 <b>(+36.66%)</b></td><td>202.40 (+5.47%)</td><td>145.54 (-8.92%)</td><td>130.50 <b>(-20.91%)</b></td><td>111.30 (-11.24%)</td><td>35.15 <b>(+32.38%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>191.90 (n/a)</td><td>159.80 (n/a)</td><td>165.00 (n/a)</td><td>125.40 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.13 (-11.40%)</td><td>0.12 (+5.92%)</td><td>0.13 (+18.84%)</td><td>0.11 <b>(+21.32%)</b></td><td>0.01 <b>(-50.80%)</b></td><td>174.50 (-17.61%)</td><td>153.86 (-8.96%)</td><td>143.20 (-15.86%)</td><td>138.70 (+12.86%)</td><td>18.19 <b>(-54.53%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>211.80 (n/a)</td><td>169.00 (n/a)</td><td>170.20 (n/a)</td><td>122.90 (n/a)</td><td>40.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (+0.04%)</td><td>0.12 (+8.79%)</td><td>0.13 (+7.35%)</td><td>0.10 <b>(+38.90%)</b></td><td>0.01 <b>(-46.66%)</b></td><td>175.80 <b>(-27.98%)</b></td><td>150.12 (-11.54%)</td><td>145.90 (-6.83%)</td><td>130.50 (-0.08%)</td><td>17.22 <b>(-61.92%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>244.10 (n/a)</td><td>169.70 (n/a)</td><td>156.60 (n/a)</td><td>130.60 (n/a)</td><td>45.21 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (+0.05%)</td><td>0.12 (+4.20%)</td><td>0.13 (+18.32%)</td><td>0.10 (+0.29%)</td><td>0.02 (-11.26%)</td><td>193.60 (-0.26%)</td><td>153.82 (-4.40%)</td><td>142.70 (-15.51%)</td><td>132.20 (-0.08%)</td><td>24.15 (-7.37%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>194.10 (n/a)</td><td>160.90 (n/a)</td><td>168.90 (n/a)</td><td>132.30 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.14 (+11.24%)</td><td>0.12 <b>(+22.84%)</b></td><td>0.14 <b>(+40.32%)</b></td><td>0.07 (-15.85%)</td><td>0.03 <b>(+57.60%)</b></td><td>274.10 (+18.81%)</td><td>166.52 (-14.40%)</td><td>134.80 <b>(-28.71%)</b></td><td>127.20 (-10.11%)</td><td>61.64 <b>(+72.14%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>230.70 (n/a)</td><td>194.54 (n/a)</td><td>189.10 (n/a)</td><td>141.50 (n/a)</td><td>35.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (+1.30%)</td><td>0.09 (-6.74%)</td><td>0.09 (-4.47%)</td><td>0.06 <b>(-26.89%)</b></td><td>0.02 <b>(+156.26%)</b></td><td>293.40 <b>(+36.78%)</b></td><td>213.00 (+10.08%)</td><td>197.50 (+4.66%)</td><td>180.40 (-1.26%)</td><td>45.53 <b>(+259.02%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>193.50 (n/a)</td><td>188.70 (n/a)</td><td>182.70 (n/a)</td><td>12.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.10 (-11.40%)</td><td>0.09 (-2.45%)</td><td>0.09 (+8.32%)</td><td>0.06 (+7.59%)</td><td>0.02 <b>(-29.42%)</b></td><td>300.00 (-7.06%)</td><td>214.90 (-0.31%)</td><td>196.50 (-7.66%)</td><td>177.90 (+12.81%)</td><td>49.10 <b>(-24.41%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>322.80 (n/a)</td><td>215.56 (n/a)</td><td>212.80 (n/a)</td><td>157.70 (n/a)</td><td>64.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.74 (-2.99%)</td><td>0.61 (-6.99%)</td><td>0.57 (-14.37%)</td><td>0.53 (-3.56%)</td><td>0.08 (-5.39%)</td><td>184.30 (+3.71%)</td><td>163.12 (+7.43%)</td><td>171.00 (+16.80%)</td><td>132.60 (+3.11%)</td><td>20.18 (-0.92%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.76 (n/a)</td><td>0.66 (n/a)</td><td>0.67 (n/a)</td><td>0.55 (n/a)</td><td>0.09 (n/a)</td><td>177.70 (n/a)</td><td>151.84 (n/a)</td><td>146.40 (n/a)</td><td>128.60 (n/a)</td><td>20.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.75 (+16.32%)</td><td>0.61 (+11.60%)</td><td>0.62 (+0.59%)</td><td>0.47 <b>(+52.71%)</b></td><td>0.13 (-8.95%)</td><td>210.00 <b>(-34.52%)</b></td><td>168.36 (-13.93%)</td><td>159.50 (-0.62%)</td><td>131.90 (-14.02%)</td><td>35.69 <b>(-49.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.61 (n/a)</td><td>0.31 (n/a)</td><td>0.14 (n/a)</td><td>320.70 (n/a)</td><td>195.60 (n/a)</td><td>160.50 (n/a)</td><td>153.40 (n/a)</td><td>70.87 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.82 (+14.19%)</td><td>0.66 (+8.20%)</td><td>0.66 (+11.00%)</td><td>0.51 (-3.31%)</td><td>0.14 <b>(+87.23%)</b></td><td>192.70 (+3.44%)</td><td>154.88 (-5.21%)</td><td>149.90 (-9.92%)</td><td>119.50 (-12.45%)</td><td>33.16 <b>(+72.74%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.72 (n/a)</td><td>0.61 (n/a)</td><td>0.59 (n/a)</td><td>0.53 (n/a)</td><td>0.07 (n/a)</td><td>186.30 (n/a)</td><td>163.40 (n/a)</td><td>166.40 (n/a)</td><td>136.50 (n/a)</td><td>19.20 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.79 <b>(+29.76%)</b></td><td>0.60 <b>(+22.36%)</b></td><td>0.56 (+11.14%)</td><td>0.43 (+17.11%)</td><td>0.15 <b>(+60.31%)</b></td><td>229.70 (-14.61%)</td><td>173.16 (-16.64%)</td><td>175.40 (-10.01%)</td><td>124.50 <b>(-22.96%)</b></td><td>43.42 (+2.78%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.61 (n/a)</td><td>0.49 (n/a)</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.09 (n/a)</td><td>269.00 (n/a)</td><td>207.72 (n/a)</td><td>194.90 (n/a)</td><td>161.60 (n/a)</td><td>42.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.57 (-3.14%)</td><td>0.46 (+7.07%)</td><td>0.43 (+9.95%)</td><td>0.34 (+1.59%)</td><td>0.10 (-2.44%)</td><td>218.60 (-1.53%)</td><td>164.96 (-6.77%)</td><td>169.80 (-9.05%)</td><td>129.80 (+3.26%)</td><td>36.31 (-2.34%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.59 (n/a)</td><td>0.43 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>222.00 (n/a)</td><td>176.94 (n/a)</td><td>186.70 (n/a)</td><td>125.70 (n/a)</td><td>37.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.57 (+10.11%)</td><td>0.43 (-5.53%)</td><td>0.41 (-14.00%)</td><td>0.31 (-17.36%)</td><td>0.10 <b>(+81.75%)</b></td><td>234.20 <b>(+20.97%)</b></td><td>178.14 (+9.29%)</td><td>178.70 (+16.27%)</td><td>128.90 (-9.16%)</td><td>41.75 <b>(+97.05%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.52 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.06 (n/a)</td><td>193.60 (n/a)</td><td>163.00 (n/a)</td><td>153.70 (n/a)</td><td>141.90 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.62 (+12.64%)</td><td>0.46 (+11.24%)</td><td>0.46 (+18.67%)</td><td>0.36 (-0.39%)</td><td>0.10 <b>(+32.70%)</b></td><td>205.60 (+0.39%)</td><td>166.86 (-8.82%)</td><td>158.90 (-15.75%)</td><td>119.00 (-11.26%)</td><td>34.94 <b>(+22.65%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.55 (n/a)</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>204.80 (n/a)</td><td>183.00 (n/a)</td><td>188.60 (n/a)</td><td>134.10 (n/a)</td><td>28.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.48 (-10.90%)</td><td>0.43 (-2.85%)</td><td>0.45 (-4.11%)</td><td>0.34 (+19.85%)</td><td>0.06 <b>(-41.50%)</b></td><td>214.10 (-16.56%)</td><td>173.24 (-0.44%)</td><td>163.70 (+4.27%)</td><td>153.90 (+12.25%)</td><td>25.21 <b>(-47.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.54 (n/a)</td><td>0.44 (n/a)</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.10 (n/a)</td><td>256.60 (n/a)</td><td>174.00 (n/a)</td><td>157.00 (n/a)</td><td>137.10 (n/a)</td><td>48.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (+4.23%)</td><td>0.23 (-1.99%)</td><td>0.28 (+5.14%)</td><td>0.13 <b>(-25.68%)</b></td><td>0.08 <b>(+56.60%)</b></td><td>283.80 <b>(+34.57%)</b></td><td>174.60 (+9.37%)</td><td>134.00 (-4.90%)</td><td>121.30 (-4.11%)</td><td>69.23 <b>(+98.03%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>210.90 (n/a)</td><td>159.64 (n/a)</td><td>140.90 (n/a)</td><td>126.50 (n/a)</td><td>34.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.29 (+3.52%)</td><td>0.24 (+19.13%)</td><td>0.24 <b>(+38.26%)</b></td><td>0.21 <b>(+50.06%)</b></td><td>0.03 <b>(-48.57%)</b></td><td>172.60 <b>(-33.36%)</b></td><td>156.08 <b>(-20.38%)</b></td><td>155.20 <b>(-27.65%)</b></td><td>128.00 (-3.40%)</td><td>18.04 <b>(-66.11%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>259.00 (n/a)</td><td>196.04 (n/a)</td><td>214.50 (n/a)</td><td>132.50 (n/a)</td><td>53.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.29 (+1.44%)</td><td>0.27 (+6.00%)</td><td>0.27 (+1.02%)</td><td>0.23 (+12.16%)</td><td>0.03 <b>(-26.04%)</b></td><td>163.60 (-10.84%)</td><td>140.32 (-6.62%)</td><td>134.80 (-1.03%)</td><td>126.80 (-1.40%)</td><td>15.59 <b>(-35.44%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>183.50 (n/a)</td><td>150.26 (n/a)</td><td>136.20 (n/a)</td><td>128.60 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (+14.48%)</td><td>0.27 (+16.93%)</td><td>0.26 (+5.93%)</td><td>0.25 <b>(+34.11%)</b></td><td>0.02 <b>(-37.64%)</b></td><td>148.30 <b>(-25.44%)</b></td><td>138.66 (-15.61%)</td><td>142.90 (-5.55%)</td><td>123.20 (-12.62%)</td><td>10.19 <b>(-59.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>198.90 (n/a)</td><td>164.30 (n/a)</td><td>151.30 (n/a)</td><td>141.00 (n/a)</td><td>25.24 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.23 (+10.78%)</td><td>0.21 <b>(+24.82%)</b></td><td>0.21 (+15.88%)</td><td>0.20 <b>(+77.86%)</b></td><td>0.01 <b>(-67.32%)</b></td><td>185.00 <b>(-43.77%)</b></td><td>172.36 <b>(-23.88%)</b></td><td>175.30 (-13.69%)</td><td>157.10 (-9.76%)</td><td>10.51 <b>(-83.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>329.00 (n/a)</td><td>226.42 (n/a)</td><td>203.10 (n/a)</td><td>174.10 (n/a)</td><td>63.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.24 (+6.12%)</td><td>0.22 (+15.41%)</td><td>0.23 <b>(+22.72%)</b></td><td>0.19 (+17.71%)</td><td>0.02 <b>(-25.76%)</b></td><td>189.40 (-15.03%)</td><td>165.16 (-13.94%)</td><td>160.50 (-18.49%)</td><td>151.00 (-5.74%)</td><td>14.57 <b>(-39.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>222.90 (n/a)</td><td>191.92 (n/a)</td><td>196.90 (n/a)</td><td>160.20 (n/a)</td><td>23.94 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.33 <b>(+22.45%)</b></td><td>0.22 (-6.52%)</td><td>0.21 (-11.39%)</td><td>0.16 (-16.50%)</td><td>0.07 <b>(+98.32%)</b></td><td>237.70 (+19.75%)</td><td>176.92 (+11.80%)</td><td>175.90 (+12.83%)</td><td>112.40 (-18.31%)</td><td>46.05 <b>(+87.93%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>198.50 (n/a)</td><td>158.24 (n/a)</td><td>155.90 (n/a)</td><td>137.60 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.28 (+6.03%)</td><td>0.21 (-15.70%)</td><td>0.21 (-17.47%)</td><td>0.14 <b>(-38.06%)</b></td><td>0.05 <b>(+211.10%)</b></td><td>262.00 <b>(+61.43%)</b></td><td>187.96 <b>(+25.06%)</b></td><td>176.60 <b>(+21.21%)</b></td><td>129.50 (-5.75%)</td><td>50.65 <b>(+371.98%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>162.30 (n/a)</td><td>150.30 (n/a)</td><td>145.70 (n/a)</td><td>137.40 (n/a)</td><td>10.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.34 (+4.29%)</td><td>0.27 (+3.13%)</td><td>0.26 (+5.72%)</td><td>0.21 (-7.24%)</td><td>0.06 <b>(+45.59%)</b></td><td>195.90 (+7.82%)</td><td>158.84 (-1.10%)</td><td>160.50 (-5.42%)</td><td>121.90 (-4.09%)</td><td>33.50 <b>(+50.34%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>181.70 (n/a)</td><td>160.60 (n/a)</td><td>169.70 (n/a)</td><td>127.10 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.31 (-5.21%)</td><td>0.26 (-6.37%)</td><td>0.27 (-13.24%)</td><td>0.21 (-3.37%)</td><td>0.04 <b>(-25.06%)</b></td><td>191.00 (+3.52%)</td><td>158.70 (+5.56%)</td><td>152.00 (+15.24%)</td><td>130.80 (+5.48%)</td><td>24.09 (-19.03%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>184.50 (n/a)</td><td>150.34 (n/a)</td><td>131.90 (n/a)</td><td>124.00 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.30 (-5.75%)</td><td>0.28 (-4.95%)</td><td>0.29 (+0.16%)</td><td>0.20 <b>(-21.13%)</b></td><td>0.04 <b>(+52.17%)</b></td><td>201.30 <b>(+26.76%)</b></td><td>151.48 (+6.87%)</td><td>139.00 (-0.14%)</td><td>134.60 (+6.15%)</td><td>28.18 <b>(+107.32%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>158.80 (n/a)</td><td>141.74 (n/a)</td><td>139.20 (n/a)</td><td>126.80 (n/a)</td><td>13.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (-1.68%)</td><td>0.29 <b>(+28.11%)</b></td><td>0.31 <b>(+63.24%)</b></td><td>0.17 (+4.94%)</td><td>0.06 (-2.43%)</td><td>235.30 (-4.70%)</td><td>151.60 <b>(-22.09%)</b></td><td>131.00 <b>(-38.73%)</b></td><td>128.60 (+1.74%)</td><td>46.81 (-2.49%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>246.90 (n/a)</td><td>194.58 (n/a)</td><td>213.80 (n/a)</td><td>126.40 (n/a)</td><td>48.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.38 <b>(+57.56%)</b></td><td>0.26 <b>(+20.98%)</b></td><td>0.24 (+5.48%)</td><td>0.17 (+1.40%)</td><td>0.08 <b>(+144.31%)</b></td><td>239.90 (-1.40%)</td><td>168.46 (-13.36%)</td><td>168.70 (-5.17%)</td><td>108.40 <b>(-36.53%)</b></td><td>47.73 <b>(+53.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>243.30 (n/a)</td><td>194.44 (n/a)</td><td>177.90 (n/a)</td><td>170.80 (n/a)</td><td>31.19 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (+4.99%)</td><td>0.20 (-6.15%)</td><td>0.20 (-3.97%)</td><td>0.18 (-6.84%)</td><td>0.03 <b>(+32.82%)</b></td><td>225.10 (+7.34%)</td><td>203.88 (+7.24%)</td><td>207.30 (+4.17%)</td><td>162.00 (-4.76%)</td><td>25.40 <b>(+37.10%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>209.70 (n/a)</td><td>190.12 (n/a)</td><td>199.00 (n/a)</td><td>170.10 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (-13.72%)</td><td>0.26 (-1.12%)</td><td>0.25 (+2.61%)</td><td>0.21 (+10.85%)</td><td>0.04 <b>(-38.64%)</b></td><td>198.50 (-9.77%)</td><td>162.80 (-1.81%)</td><td>161.10 (-2.54%)</td><td>127.30 (+15.94%)</td><td>26.03 <b>(-34.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>220.00 (n/a)</td><td>165.80 (n/a)</td><td>165.30 (n/a)</td><td>109.80 (n/a)</td><td>39.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.32 (+18.67%)</td><td>0.24 (+5.85%)</td><td>0.24 (-6.96%)</td><td>0.18 <b>(+26.54%)</b></td><td>0.05 (+0.00%)</td><td>230.10 <b>(-20.98%)</b></td><td>173.60 (-7.46%)</td><td>171.20 (+7.47%)</td><td>127.70 (-15.71%)</td><td>37.83 <b>(-35.50%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>291.20 (n/a)</td><td>187.60 (n/a)</td><td>159.30 (n/a)</td><td>151.50 (n/a)</td><td>58.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.29 (+8.96%)</td><td>0.23 (+9.67%)</td><td>0.23 (+13.93%)</td><td>0.17 (+5.33%)</td><td>0.05 <b>(+27.12%)</b></td><td>208.80 (-5.05%)</td><td>156.48 (-7.71%)</td><td>148.60 (-12.23%)</td><td>118.20 (-8.23%)</td><td>36.27 (+10.50%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>219.90 (n/a)</td><td>169.56 (n/a)</td><td>169.30 (n/a)</td><td>128.80 (n/a)</td><td>32.82 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (+0.97%)</td><td>0.21 (+1.75%)</td><td>0.19 (-5.15%)</td><td>0.18 (+11.29%)</td><td>0.04 (-2.19%)</td><td>196.60 (-10.11%)</td><td>170.64 (-2.09%)</td><td>183.60 (+5.46%)</td><td>127.40 (-1.01%)</td><td>30.70 (-10.68%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>218.70 (n/a)</td><td>174.28 (n/a)</td><td>174.10 (n/a)</td><td>128.70 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (-6.68%)</td><td>0.23 (+2.02%)</td><td>0.25 (+12.29%)</td><td>0.14 (-17.23%)</td><td>0.05 (+7.66%)</td><td>251.70 <b>(+20.84%)</b></td><td>160.52 (+0.16%)</td><td>141.30 (-10.96%)</td><td>130.80 (+7.21%)</td><td>51.40 <b>(+45.05%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>208.30 (n/a)</td><td>160.26 (n/a)</td><td>158.70 (n/a)</td><td>122.00 (n/a)</td><td>35.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.27 (-1.92%)</td><td>0.25 (+12.00%)</td><td>0.24 (+9.67%)</td><td>0.21 <b>(+24.13%)</b></td><td>0.02 <b>(-40.74%)</b></td><td>165.70 (-19.45%)</td><td>142.80 (-12.30%)</td><td>142.80 (-8.81%)</td><td>130.10 (+1.96%)</td><td>14.17 <b>(-51.56%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>205.70 (n/a)</td><td>162.82 (n/a)</td><td>156.60 (n/a)</td><td>127.60 (n/a)</td><td>29.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (+5.13%)</td><td>0.23 (+12.11%)</td><td>0.23 (+5.94%)</td><td>0.20 <b>(+28.59%)</b></td><td>0.02 <b>(-44.36%)</b></td><td>170.40 <b>(-22.23%)</b></td><td>151.14 (-12.19%)</td><td>150.00 (-5.66%)</td><td>141.30 (-4.85%)</td><td>11.85 <b>(-59.08%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>219.10 (n/a)</td><td>172.12 (n/a)</td><td>159.00 (n/a)</td><td>148.50 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.21 (-12.10%)</td><td>0.18 (-2.34%)</td><td>0.18 (+0.79%)</td><td>0.14 (+6.92%)</td><td>0.03 <b>(-32.27%)</b></td><td>248.80 (-6.47%)</td><td>198.64 (+0.13%)</td><td>189.20 (-0.79%)</td><td>168.10 (+13.81%)</td><td>33.80 <b>(-28.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>266.00 (n/a)</td><td>198.38 (n/a)</td><td>190.70 (n/a)</td><td>147.70 (n/a)</td><td>47.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.25 (+15.86%)</td><td>0.21 (+16.15%)</td><td>0.21 (+15.03%)</td><td>0.17 (+3.87%)</td><td>0.03 <b>(+34.80%)</b></td><td>209.90 (-3.72%)</td><td>168.14 (-13.38%)</td><td>167.60 (-13.03%)</td><td>140.00 (-13.69%)</td><td>26.16 (+12.30%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>218.00 (n/a)</td><td>194.12 (n/a)</td><td>192.70 (n/a)</td><td>162.20 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.37 <b>(+38.54%)</b></td><td>0.24 (+16.66%)</td><td>0.20 (-6.34%)</td><td>0.15 <b>(+31.62%)</b></td><td>0.09 <b>(+45.03%)</b></td><td>235.60 <b>(-24.00%)</b></td><td>162.08 (-13.40%)</td><td>171.20 (+6.80%)</td><td>95.20 <b>(-27.88%)</b></td><td>56.14 <b>(-23.02%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>310.00 (n/a)</td><td>187.16 (n/a)</td><td>160.30 (n/a)</td><td>132.00 (n/a)</td><td>72.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.08 (+10.82%)</td><td>0.90 (+13.32%)</td><td>0.86 (+8.58%)</td><td>0.71 (+7.91%)</td><td>0.17 <b>(+42.87%)</b></td><td>184.90 (-7.36%)</td><td>149.06 (-10.82%)</td><td>152.90 (-7.95%)</td><td>121.20 (-9.82%)</td><td>27.61 (+16.00%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.98 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.66 (n/a)</td><td>0.12 (n/a)</td><td>199.60 (n/a)</td><td>167.14 (n/a)</td><td>166.10 (n/a)</td><td>134.40 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.09 (+16.15%)</td><td>0.87 (+7.94%)</td><td>0.85 (+5.60%)</td><td>0.60 (-14.15%)</td><td>0.21 <b>(+138.93%)</b></td><td>216.70 (+16.51%)</td><td>158.96 (-3.52%)</td><td>154.20 (-5.28%)</td><td>120.40 (-13.88%)</td><td>40.34 <b>(+134.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.94 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.70 (n/a)</td><td>0.09 (n/a)</td><td>186.00 (n/a)</td><td>164.76 (n/a)</td><td>162.80 (n/a)</td><td>139.80 (n/a)</td><td>17.20 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.07 (+2.20%)</td><td>0.82 (-10.36%)</td><td>0.92 (-3.96%)</td><td>0.36 <b>(-48.50%)</b></td><td>0.29 <b>(+118.82%)</b></td><td>366.90 <b>(+94.23%)</b></td><td>187.42 <b>(+28.65%)</b></td><td>142.60 (+4.09%)</td><td>122.60 (-2.15%)</td><td>102.67 <b>(+312.78%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.05 (n/a)</td><td>0.92 (n/a)</td><td>0.96 (n/a)</td><td>0.69 (n/a)</td><td>0.13 (n/a)</td><td>188.90 (n/a)</td><td>145.68 (n/a)</td><td>137.00 (n/a)</td><td>125.30 (n/a)</td><td>24.87 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.04 (+3.13%)</td><td>0.03 (+3.05%)</td><td>0.02 (-5.55%)</td><td>0.02 (-1.88%)</td><td>0.01 <b>(+28.40%)</b></td><td>192.80 (+1.90%)</td><td>160.18 (-1.20%)</td><td>179.30 (+5.91%)</td><td>115.20 (-3.03%)</td><td>36.36 <b>(+28.70%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>162.12 (n/a)</td><td>169.30 (n/a)</td><td>118.80 (n/a)</td><td>28.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 <b>(+23.32%)</b></td><td>0.03 <b>(+20.31%)</b></td><td>0.03 (+19.31%)</td><td>0.02 (+10.97%)</td><td>0.00 <b>(+69.09%)</b></td><td>180.00 (-9.91%)</td><td>157.10 (-16.41%)</td><td>162.40 (-16.16%)</td><td>132.90 (-18.91%)</td><td>18.19 <b>(+22.98%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.80 (n/a)</td><td>187.94 (n/a)</td><td>193.70 (n/a)</td><td>163.90 (n/a)</td><td>14.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 <b>(+22.53%)</b></td><td>0.03 (+13.51%)</td><td>0.02 (+10.74%)</td><td>0.02 (+7.03%)</td><td>0.00 <b>(+84.27%)</b></td><td>188.20 (-6.55%)</td><td>162.38 (-10.53%)</td><td>172.40 (-9.69%)</td><td>128.80 (-18.38%)</td><td>27.63 <b>(+42.13%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.40 (n/a)</td><td>181.50 (n/a)</td><td>190.90 (n/a)</td><td>157.80 (n/a)</td><td>19.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>18.04 (+13.74%)</td><td>14.57 (+11.95%)</td><td>14.06 (+16.04%)</td><td>12.17 (+3.00%)</td><td>2.29 <b>(+35.89%)</b></td><td>172.50 (-2.87%)</td><td>146.76 (-10.06%)</td><td>149.20 (-13.81%)</td><td>116.30 (-12.09%)</td><td>21.72 (+16.04%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>15.86 (n/a)</td><td>13.01 (n/a)</td><td>12.12 (n/a)</td><td>11.81 (n/a)</td><td>1.68 (n/a)</td><td>177.60 (n/a)</td><td>163.18 (n/a)</td><td>173.10 (n/a)</td><td>132.30 (n/a)</td><td>18.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.06 <b>(+31.23%)</b></td><td>0.83 (+14.06%)</td><td>0.78 (+1.42%)</td><td>0.65 (+9.35%)</td><td>0.17 <b>(+100.58%)</b></td><td>201.80 (-8.52%)</td><td>163.66 (-10.58%)</td><td>169.20 (-1.40%)</td><td>124.00 <b>(-23.83%)</b></td><td>31.54 <b>(+37.13%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.81 (n/a)</td><td>0.73 (n/a)</td><td>0.77 (n/a)</td><td>0.60 (n/a)</td><td>0.08 (n/a)</td><td>220.60 (n/a)</td><td>183.02 (n/a)</td><td>171.60 (n/a)</td><td>162.80 (n/a)</td><td>23.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.07 <b>(+38.73%)</b></td><td>0.91 <b>(+22.36%)</b></td><td>0.92 <b>(+22.41%)</b></td><td>0.74 (+3.86%)</td><td>0.15 <b>(+620.41%)</b></td><td>178.80 (-3.72%)</td><td>147.92 (-16.47%)</td><td>143.70 (-18.31%)</td><td>124.00 <b>(-27.91%)</b></td><td>25.01 <b>(+387.54%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.71 (n/a)</td><td>0.02 (n/a)</td><td>185.70 (n/a)</td><td>177.08 (n/a)</td><td>175.90 (n/a)</td><td>172.00 (n/a)</td><td>5.13 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.08 (-6.31%)</td><td>0.72 (-14.24%)</td><td>0.74 (+0.54%)</td><td>0.34 <b>(-46.90%)</b></td><td>0.27 <b>(+30.01%)</b></td><td>384.70 <b>(+88.30%)</b></td><td>210.56 <b>(+28.89%)</b></td><td>178.00 (-0.56%)</td><td>122.20 (+6.72%)</td><td>101.84 <b>(+183.27%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.15 (n/a)</td><td>0.84 (n/a)</td><td>0.74 (n/a)</td><td>0.65 (n/a)</td><td>0.21 (n/a)</td><td>204.30 (n/a)</td><td>163.36 (n/a)</td><td>179.00 (n/a)</td><td>114.50 (n/a)</td><td>35.95 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.08 <b>(+28.95%)</b></td><td>0.83 (+10.53%)</td><td>0.80 (+3.47%)</td><td>0.67 (+16.66%)</td><td>0.16 <b>(+54.78%)</b></td><td>196.40 (-14.27%)</td><td>163.38 (-8.59%)</td><td>166.10 (-3.37%)</td><td>122.20 <b>(-22.41%)</b></td><td>29.55 (+1.11%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.84 (n/a)</td><td>0.75 (n/a)</td><td>0.77 (n/a)</td><td>0.58 (n/a)</td><td>0.11 (n/a)</td><td>229.10 (n/a)</td><td>178.74 (n/a)</td><td>171.90 (n/a)</td><td>157.50 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.09 (+0.40%)</td><td>0.82 (+2.01%)</td><td>0.70 (-4.30%)</td><td>0.56 (-6.97%)</td><td>0.25 (+18.58%)</td><td>237.20 (+7.48%)</td><td>173.94 (+0.08%)</td><td>190.00 (+4.51%)</td><td>120.90 (-0.41%)</td><td>50.95 (+18.89%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.09 (n/a)</td><td>0.80 (n/a)</td><td>0.73 (n/a)</td><td>0.60 (n/a)</td><td>0.21 (n/a)</td><td>220.70 (n/a)</td><td>173.80 (n/a)</td><td>181.80 (n/a)</td><td>121.40 (n/a)</td><td>42.85 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (+11.15%)</td><td>0.02 (-6.39%)</td><td>0.02 (-5.23%)</td><td>0.01 <b>(-24.19%)</b></td><td>0.01 <b>(+55.81%)</b></td><td>281.50 <b>(+31.91%)</b></td><td>190.04 (+11.58%)</td><td>177.00 (+5.55%)</td><td>128.60 (-10.07%)</td><td>57.57 <b>(+93.97%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.40 (n/a)</td><td>170.32 (n/a)</td><td>167.70 (n/a)</td><td>143.00 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.03 (-12.52%)</td><td>0.03 (-2.27%)</td><td>0.03 (+15.57%)</td><td>0.02 (-4.97%)</td><td>0.00 <b>(-37.27%)</b></td><td>208.30 (+5.26%)</td><td>162.04 (+0.17%)</td><td>155.90 (-13.44%)</td><td>140.30 (+14.25%)</td><td>27.86 <b>(-21.74%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>161.76 (n/a)</td><td>180.10 (n/a)</td><td>122.80 (n/a)</td><td>35.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>1005.48 (-0.10%)</td><td>967.69 (-0.34%)</td><td>961.58 (-0.04%)</td><td>945.62 (-1.12%)</td><td>25.07 <b>(+23.54%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1006.46 (n/a)</td><td>971.04 (n/a)</td><td>961.93 (n/a)</td><td>956.32 (n/a)</td><td>20.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.01 (+0.00%)</td><td>0.01 (+0.00%)</td><td>0.01 (+0.00%)</td><td>0.01 (+3.95%)</td><td>0.00 <b>(-34.20%)</b></td><td>1036.40 (-4.39%)</td><td>1012.41 (-0.57%)</td><td>1012.55 (+0.34%)</td><td>970.95 (-0.90%)</td><td>26.42 <b>(-35.25%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1083.96 (n/a)</td><td>1018.22 (n/a)</td><td>1009.16 (n/a)</td><td>979.74 (n/a)</td><td>40.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.02 (+4.65%)</td><td>0.97 (+0.98%)</td><td>0.96 (+0.33%)</td><td>0.96 (-0.33%)</td><td>0.03 <b>(+301.78%)</b></td><td>2193.55 (+0.34%)</td><td>2155.83 (-0.92%)</td><td>2177.52 (-0.33%)</td><td>2057.87 (-4.45%)</td><td>55.70 <b>(+284.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.01 (n/a)</td><td>2186.11 (n/a)</td><td>2175.78 (n/a)</td><td>2184.75 (n/a)</td><td>2153.64 (n/a)</td><td>14.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.02 (+12.61%)</td><td>5.41 (+8.33%)</td><td>5.45 (+10.22%)</td><td>4.79 (+1.94%)</td><td>0.45 <b>(+65.15%)</b></td><td>219.00 (-1.88%)</td><td>194.82 (-7.40%)</td><td>192.30 (-9.29%)</td><td>174.30 (-11.21%)</td><td>16.51 <b>(+44.82%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>5.34 (n/a)</td><td>5.00 (n/a)</td><td>4.95 (n/a)</td><td>4.70 (n/a)</td><td>0.27 (n/a)</td><td>223.20 (n/a)</td><td>210.38 (n/a)</td><td>212.00 (n/a)</td><td>196.30 (n/a)</td><td>11.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.25 (+1.03%)</td><td>4.60 (-4.51%)</td><td>4.66 (-4.12%)</td><td>3.97 (-6.93%)</td><td>0.59 <b>(+73.44%)</b></td><td>263.90 (+7.45%)</td><td>231.28 (+5.69%)</td><td>225.00 (+4.31%)</td><td>199.80 (-1.04%)</td><td>30.15 <b>(+84.74%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>5.19 (n/a)</td><td>4.81 (n/a)</td><td>4.86 (n/a)</td><td>4.27 (n/a)</td><td>0.34 (n/a)</td><td>245.60 (n/a)</td><td>218.82 (n/a)</td><td>215.70 (n/a)</td><td>201.90 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.45 (-10.87%)</td><td>4.92 (-4.86%)</td><td>5.00 (-7.97%)</td><td>3.82 (-7.16%)</td><td>0.65 (-17.75%)</td><td>274.40 (+7.73%)</td><td>216.70 (+4.76%)</td><td>209.70 (+8.65%)</td><td>192.30 (+12.19%)</td><td>33.45 (-0.00%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>6.12 (n/a)</td><td>5.17 (n/a)</td><td>5.43 (n/a)</td><td>4.12 (n/a)</td><td>0.80 (n/a)</td><td>254.70 (n/a)</td><td>206.86 (n/a)</td><td>193.00 (n/a)</td><td>171.40 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>5.14 <b>(-20.81%)</b></td><td>4.47 (-17.63%)</td><td>4.30 <b>(-22.96%)</b></td><td>3.81 (-12.87%)</td><td>0.52 <b>(-42.32%)</b></td><td>275.00 (+14.77%)</td><td>237.10 (+19.99%)</td><td>243.90 <b>(+29.80%)</b></td><td>204.10 <b>(+26.30%)</b></td><td>27.52 (-17.83%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>6.49 (n/a)</td><td>5.43 (n/a)</td><td>5.58 (n/a)</td><td>4.38 (n/a)</td><td>0.90 (n/a)</td><td>239.60 (n/a)</td><td>197.60 (n/a)</td><td>187.90 (n/a)</td><td>161.60 (n/a)</td><td>33.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.62 (-6.60%)</td><td>8.01 (-6.63%)</td><td>7.72 (-10.54%)</td><td>7.44 (-3.31%)</td><td>0.56 (-10.93%)</td><td>282.00 (+3.45%)</td><td>262.86 (+7.04%)</td><td>271.60 (+11.77%)</td><td>243.20 (+7.04%)</td><td>18.01 (-2.29%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.23 (n/a)</td><td>8.58 (n/a)</td><td>8.63 (n/a)</td><td>7.69 (n/a)</td><td>0.63 (n/a)</td><td>272.60 (n/a)</td><td>245.58 (n/a)</td><td>243.00 (n/a)</td><td>227.20 (n/a)</td><td>18.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.56 (-8.25%)</td><td>7.72 (-5.50%)</td><td>7.82 (-1.40%)</td><td>6.72 (-9.94%)</td><td>0.78 (+6.10%)</td><td>311.90 (+11.04%)</td><td>274.10 (+6.06%)</td><td>268.10 (+1.44%)</td><td>245.10 (+8.98%)</td><td>28.32 <b>(+28.92%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.33 (n/a)</td><td>8.16 (n/a)</td><td>7.93 (n/a)</td><td>7.47 (n/a)</td><td>0.73 (n/a)</td><td>280.90 (n/a)</td><td>258.44 (n/a)</td><td>264.30 (n/a)</td><td>224.90 (n/a)</td><td>21.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.90 (-7.12%)</td><td>8.03 (-4.17%)</td><td>7.85 (-2.17%)</td><td>7.21 (-0.28%)</td><td>0.77 <b>(-24.77%)</b></td><td>290.70 (+0.28%)</td><td>263.06 (+3.89%)</td><td>267.00 (+2.22%)</td><td>235.70 (+7.67%)</td><td>25.00 (-18.23%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.58 (n/a)</td><td>8.38 (n/a)</td><td>8.03 (n/a)</td><td>7.23 (n/a)</td><td>1.03 (n/a)</td><td>289.90 (n/a)</td><td>253.22 (n/a)</td><td>261.20 (n/a)</td><td>218.90 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>11.03 (+15.79%)</td><td>8.47 (-0.47%)</td><td>7.95 (-7.30%)</td><td>7.30 (-0.15%)</td><td>1.53 <b>(+71.96%)</b></td><td>287.40 (+0.14%)</td><td>253.20 (+1.85%)</td><td>263.60 (+7.86%)</td><td>190.00 (-13.64%)</td><td>39.59 <b>(+47.62%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.53 (n/a)</td><td>8.51 (n/a)</td><td>8.58 (n/a)</td><td>7.31 (n/a)</td><td>0.89 (n/a)</td><td>287.00 (n/a)</td><td>248.60 (n/a)</td><td>244.40 (n/a)</td><td>220.00 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>11.40 <b>(+20.01%)</b></td><td>9.10 (+10.13%)</td><td>8.50 (+6.87%)</td><td>8.20 (+8.49%)</td><td>1.33 <b>(+61.70%)</b></td><td>255.70 (-7.82%)</td><td>233.94 (-8.55%)</td><td>246.80 (-6.44%)</td><td>183.90 (-16.71%)</td><td>29.46 <b>(+22.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.50 (n/a)</td><td>8.26 (n/a)</td><td>7.95 (n/a)</td><td>7.56 (n/a)</td><td>0.82 (n/a)</td><td>277.40 (n/a)</td><td>255.80 (n/a)</td><td>263.80 (n/a)</td><td>220.80 (n/a)</td><td>24.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>12.39 <b>(+26.43%)</b></td><td>9.40 (+5.40%)</td><td>8.61 (-3.38%)</td><td>7.63 (-5.36%)</td><td>1.99 <b>(+221.74%)</b></td><td>274.90 (+5.69%)</td><td>230.50 (-2.31%)</td><td>243.60 (+3.53%)</td><td>169.30 <b>(-20.89%)</b></td><td>44.33 <b>(+169.42%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.80 (n/a)</td><td>8.92 (n/a)</td><td>8.91 (n/a)</td><td>8.06 (n/a)</td><td>0.62 (n/a)</td><td>260.10 (n/a)</td><td>235.94 (n/a)</td><td>235.30 (n/a)</td><td>214.00 (n/a)</td><td>16.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>11.05 (-10.90%)</td><td>10.63 (-4.71%)</td><td>10.59 (-4.68%)</td><td>10.13 (-3.46%)</td><td>0.37 <b>(-51.24%)</b></td><td>414.10 (+3.58%)</td><td>394.82 (+4.68%)</td><td>396.00 (+4.90%)</td><td>379.50 (+12.24%)</td><td>13.70 <b>(-43.02%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>12.40 (n/a)</td><td>11.16 (n/a)</td><td>11.11 (n/a)</td><td>10.49 (n/a)</td><td>0.75 (n/a)</td><td>399.80 (n/a)</td><td>377.16 (n/a)</td><td>377.50 (n/a)</td><td>338.10 (n/a)</td><td>24.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>12.53 (-0.43%)</td><td>11.43 (-4.63%)</td><td>11.15 (-6.34%)</td><td>10.73 (-7.31%)</td><td>0.69 <b>(+78.86%)</b></td><td>390.80 (+7.90%)</td><td>368.04 (+5.06%)</td><td>376.20 (+6.75%)</td><td>334.70 (+0.45%)</td><td>21.40 <b>(+92.52%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>12.59 (n/a)</td><td>11.98 (n/a)</td><td>11.90 (n/a)</td><td>11.58 (n/a)</td><td>0.39 (n/a)</td><td>362.20 (n/a)</td><td>350.30 (n/a)</td><td>352.40 (n/a)</td><td>333.20 (n/a)</td><td>11.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.97 (+12.30%)</td><td>11.76 (+0.83%)</td><td>11.14 (-5.83%)</td><td>10.55 (-2.10%)</td><td>1.42 <b>(+83.94%)</b></td><td>397.60 (+2.13%)</td><td>360.66 (-0.11%)</td><td>376.60 (+6.20%)</td><td>300.20 (-10.95%)</td><td>40.28 <b>(+66.83%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>12.44 (n/a)</td><td>11.66 (n/a)</td><td>11.83 (n/a)</td><td>10.77 (n/a)</td><td>0.77 (n/a)</td><td>389.30 (n/a)</td><td>361.04 (n/a)</td><td>354.60 (n/a)</td><td>337.10 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.22 (-3.05%)</td><td>12.03 (-7.39%)</td><td>12.62 (-3.88%)</td><td>9.25 <b>(-25.10%)</b></td><td>1.58 <b>(+168.52%)</b></td><td>453.60 <b>(+33.53%)</b></td><td>354.54 (+9.62%)</td><td>332.30 (+4.04%)</td><td>317.30 (+3.15%)</td><td>55.89 <b>(+278.18%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.64 (n/a)</td><td>12.99 (n/a)</td><td>13.13 (n/a)</td><td>12.35 (n/a)</td><td>0.59 (n/a)</td><td>339.70 (n/a)</td><td>323.44 (n/a)</td><td>319.40 (n/a)</td><td>307.60 (n/a)</td><td>14.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.58 (+6.33%)</td><td>12.68 (+4.41%)</td><td>12.49 (+1.19%)</td><td>11.67 (+3.02%)</td><td>0.81 <b>(+43.60%)</b></td><td>359.50 (-2.92%)</td><td>331.76 (-4.08%)</td><td>335.90 (-1.18%)</td><td>308.80 (-5.94%)</td><td>21.16 <b>(+29.42%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>12.77 (n/a)</td><td>12.15 (n/a)</td><td>12.34 (n/a)</td><td>11.33 (n/a)</td><td>0.56 (n/a)</td><td>370.30 (n/a)</td><td>345.86 (n/a)</td><td>339.90 (n/a)</td><td>328.30 (n/a)</td><td>16.35 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>14.55 (+2.46%)</td><td>12.38 (-4.39%)</td><td>12.91 (-1.23%)</td><td>9.74 (-19.51%)</td><td>1.91 <b>(+120.09%)</b></td><td>430.70 <b>(+24.23%)</b></td><td>345.82 (+6.37%)</td><td>324.80 (+1.25%)</td><td>288.30 (-2.44%)</td><td>57.07 <b>(+166.42%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>14.20 (n/a)</td><td>12.95 (n/a)</td><td>13.07 (n/a)</td><td>12.10 (n/a)</td><td>0.87 (n/a)</td><td>346.70 (n/a)</td><td>325.12 (n/a)</td><td>320.80 (n/a)</td><td>295.50 (n/a)</td><td>21.42 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>13.62 (-9.94%)</td><td>12.17 (-8.98%)</td><td>12.64 (-4.19%)</td><td>9.28 <b>(-21.28%)</b></td><td>1.69 <b>(+28.85%)</b></td><td>451.80 <b>(+27.02%)</b></td><td>351.00 (+11.04%)</td><td>331.90 (+4.37%)</td><td>308.00 (+11.03%)</td><td>57.68 <b>(+87.61%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>15.12 (n/a)</td><td>13.37 (n/a)</td><td>13.19 (n/a)</td><td>11.79 (n/a)</td><td>1.31 (n/a)</td><td>355.70 (n/a)</td><td>316.10 (n/a)</td><td>318.00 (n/a)</td><td>277.40 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>14.53 <b>(+21.81%)</b></td><td>12.79 <b>(+23.57%)</b></td><td>12.86 <b>(+32.51%)</b></td><td>9.83 (+3.62%)</td><td>1.89 <b>(+69.24%)</b></td><td>426.70 (-3.51%)</td><td>334.42 (-18.19%)</td><td>326.00 <b>(-24.54%)</b></td><td>288.60 (-17.92%)</td><td>55.67 <b>(+33.07%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>11.93 (n/a)</td><td>10.35 (n/a)</td><td>9.71 (n/a)</td><td>9.49 (n/a)</td><td>1.11 (n/a)</td><td>442.20 (n/a)</td><td>408.80 (n/a)</td><td>432.00 (n/a)</td><td>351.60 (n/a)</td><td>41.83 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.32 (-2.11%)</td><td>3.05 (+11.65%)</td><td>3.11 (+19.01%)</td><td>2.78 (+11.16%)</td><td>0.21 <b>(-43.38%)</b></td><td>188.90 (-10.05%)</td><td>172.46 (-11.23%)</td><td>168.60 (-15.99%)</td><td>157.70 (+2.14%)</td><td>12.08 <b>(-46.72%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.40 (n/a)</td><td>2.73 (n/a)</td><td>2.61 (n/a)</td><td>2.50 (n/a)</td><td>0.37 (n/a)</td><td>210.00 (n/a)</td><td>194.28 (n/a)</td><td>200.70 (n/a)</td><td>154.40 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>6.12 (+17.90%)</td><td>4.94 (+10.03%)</td><td>4.80 (+6.23%)</td><td>4.25 (+8.56%)</td><td>0.72 <b>(+50.08%)</b></td><td>246.50 (-7.88%)</td><td>215.46 (-8.53%)</td><td>218.50 (-5.86%)</td><td>171.50 (-15.18%)</td><td>28.58 (+15.57%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>5.19 (n/a)</td><td>4.49 (n/a)</td><td>4.52 (n/a)</td><td>3.92 (n/a)</td><td>0.48 (n/a)</td><td>267.60 (n/a)</td><td>235.54 (n/a)</td><td>232.10 (n/a)</td><td>202.20 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>8.58 (+15.17%)</td><td>7.99 (+12.23%)</td><td>7.93 (+10.47%)</td><td>7.45 (+15.53%)</td><td>0.42 (+4.57%)</td><td>281.50 (-13.44%)</td><td>262.92 (-10.94%)</td><td>264.60 (-9.48%)</td><td>244.50 (-13.17%)</td><td>13.79 <b>(-21.99%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.45 (n/a)</td><td>7.12 (n/a)</td><td>7.17 (n/a)</td><td>6.45 (n/a)</td><td>0.40 (n/a)</td><td>325.20 (n/a)</td><td>295.22 (n/a)</td><td>292.30 (n/a)</td><td>281.60 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>3.60 (-0.28%)</td><td>3.13 (+9.41%)</td><td>3.15 (+15.71%)</td><td>2.40 (+1.87%)</td><td>0.45 (-2.58%)</td><td>218.40 (-1.84%)</td><td>170.82 (-8.63%)</td><td>166.40 (-13.56%)</td><td>145.50 (+0.28%)</td><td>28.23 (+0.66%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.61 (n/a)</td><td>2.86 (n/a)</td><td>2.72 (n/a)</td><td>2.36 (n/a)</td><td>0.47 (n/a)</td><td>222.50 (n/a)</td><td>186.96 (n/a)</td><td>192.50 (n/a)</td><td>145.10 (n/a)</td><td>28.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.29 (+10.68%)</td><td>0.23 (+15.82%)</td><td>0.26 <b>(+47.00%)</b></td><td>0.15 (-1.88%)</td><td>0.06 <b>(+32.00%)</b></td><td>211.80 (+1.88%)</td><td>150.60 (-11.78%)</td><td>126.80 <b>(-31.97%)</b></td><td>113.00 (-9.60%)</td><td>42.31 <b>(+22.93%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.90 (n/a)</td><td>170.70 (n/a)</td><td>186.40 (n/a)</td><td>125.00 (n/a)</td><td>34.42 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.23 (+10.22%)</td><td>0.19 (+4.58%)</td><td>0.17 (+0.90%)</td><td>0.16 (+6.54%)</td><td>0.03 (+17.32%)</td><td>201.40 (-6.11%)</td><td>174.70 (-4.08%)</td><td>187.60 (-0.90%)</td><td>142.40 (-9.24%)</td><td>25.15 (+2.21%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.50 (n/a)</td><td>182.14 (n/a)</td><td>189.30 (n/a)</td><td>156.90 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.54 (+17.62%)</td><td>0.41 (+10.45%)</td><td>0.38 (+13.45%)</td><td>0.28 (-12.67%)</td><td>0.11 <b>(+71.18%)</b></td><td>233.30 (+14.53%)</td><td>168.24 (-6.25%)</td><td>173.10 (-11.86%)</td><td>120.60 (-14.95%)</td><td>44.79 <b>(+61.95%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>203.70 (n/a)</td><td>179.46 (n/a)</td><td>196.40 (n/a)</td><td>141.80 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.50 (+2.37%)</td><td>0.39 (+4.13%)</td><td>0.39 (+14.02%)</td><td>0.27 (-18.47%)</td><td>0.09 <b>(+45.64%)</b></td><td>240.10 <b>(+22.69%)</b></td><td>176.04 (-1.18%)</td><td>167.90 (-12.28%)</td><td>132.30 (-2.29%)</td><td>44.22 <b>(+73.37%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>195.70 (n/a)</td><td>178.14 (n/a)</td><td>191.40 (n/a)</td><td>135.40 (n/a)</td><td>25.51 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.45 <b>(-29.12%)</b></td><td>0.41 (+4.07%)</td><td>0.40 (+18.70%)</td><td>0.36 (+17.00%)</td><td>0.03 <b>(-75.55%)</b></td><td>183.10 (-14.52%)</td><td>162.24 (-10.14%)</td><td>162.50 (-15.76%)</td><td>144.90 <b>(+41.09%)</b></td><td>13.87 <b>(-68.90%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.64 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.14 (n/a)</td><td>214.20 (n/a)</td><td>180.54 (n/a)</td><td>192.90 (n/a)</td><td>102.70 (n/a)</td><td>44.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.02 (-6.65%)</td><td>0.85 (+10.01%)</td><td>0.84 (+15.53%)</td><td>0.70 <b>(+92.84%)</b></td><td>0.13 <b>(-56.96%)</b></td><td>186.60 <b>(-48.14%)</b></td><td>157.56 <b>(-21.15%)</b></td><td>156.60 (-13.43%)</td><td>128.40 (+7.18%)</td><td>24.51 <b>(-75.02%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.09 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>359.80 (n/a)</td><td>199.82 (n/a)</td><td>180.90 (n/a)</td><td>119.80 (n/a)</td><td>98.11 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.09 (+1.08%)</td><td>0.86 (+10.30%)</td><td>0.84 (+19.02%)</td><td>0.71 (+13.41%)</td><td>0.15 <b>(-20.79%)</b></td><td>184.40 (-11.81%)</td><td>154.94 (-10.94%)</td><td>155.50 (-15.99%)</td><td>119.80 (-1.07%)</td><td>24.62 <b>(-31.18%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.08 (n/a)</td><td>0.78 (n/a)</td><td>0.71 (n/a)</td><td>0.63 (n/a)</td><td>0.19 (n/a)</td><td>209.10 (n/a)</td><td>173.98 (n/a)</td><td>185.10 (n/a)</td><td>121.10 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.97 (-11.25%)</td><td>0.85 (+15.75%)</td><td>0.81 <b>(+25.43%)</b></td><td>0.80 <b>(+40.57%)</b></td><td>0.08 <b>(-64.21%)</b></td><td>164.60 <b>(-28.87%)</b></td><td>154.46 (-17.77%)</td><td>161.50 <b>(-20.29%)</b></td><td>134.90 (+12.60%)</td><td>13.08 <b>(-70.43%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.09 (n/a)</td><td>0.74 (n/a)</td><td>0.65 (n/a)</td><td>0.57 (n/a)</td><td>0.21 (n/a)</td><td>231.40 (n/a)</td><td>187.84 (n/a)</td><td>202.60 (n/a)</td><td>119.80 (n/a)</td><td>44.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>1.00 (+10.35%)</td><td>0.83 <b>(+23.42%)</b></td><td>0.83 <b>(+33.49%)</b></td><td>0.68 (+19.41%)</td><td>0.13 (-5.70%)</td><td>192.40 (-16.24%)</td><td>161.78 (-19.69%)</td><td>158.60 <b>(-25.08%)</b></td><td>131.50 (-9.37%)</td><td>25.30 <b>(-27.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.90 (n/a)</td><td>0.67 (n/a)</td><td>0.62 (n/a)</td><td>0.57 (n/a)</td><td>0.14 (n/a)</td><td>229.70 (n/a)</td><td>201.44 (n/a)</td><td>211.70 (n/a)</td><td>145.10 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:42:32</td><td>0.11 (-15.18%)</td><td>0.09 (-10.77%)</td><td>0.10 (-2.59%)</td><td>0.07 (-18.43%)</td><td>0.02 (+16.95%)</td><td>232.00 <b>(+22.62%)</b></td><td>186.46 (+13.86%)</td><td>169.80 (+2.66%)</td><td>153.80 (+17.85%)</td><td>37.94 <b>(+71.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>163.76 (n/a)</td><td>165.40 (n/a)</td><td>130.50 (n/a)</td><td>22.14 (n/a)</td>
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
