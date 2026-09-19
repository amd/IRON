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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (+18.47%)</td><td>0.04 (+10.02%)</td><td>0.04 (+10.56%)</td><td>0.03 (-5.18%)</td><td>0.01 <b>(+158.08%)</b></td><td>196.20 (+5.43%)</td><td>158.86 (-6.49%)</td><td>151.70 (-9.54%)</td><td>125.60 (-15.59%)</td><td>33.05 <b>(+133.06%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.10 (n/a)</td><td>169.88 (n/a)</td><td>167.70 (n/a)</td><td>148.80 (n/a)</td><td>14.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (+8.38%)</td><td>0.04 (+19.20%)</td><td>0.05 <b>(+29.68%)</b></td><td>0.03 <b>(+28.58%)</b></td><td>0.01 (-1.59%)</td><td>192.10 <b>(-22.23%)</b></td><td>146.08 (-17.20%)</td><td>131.40 <b>(-22.89%)</b></td><td>122.00 (-7.72%)</td><td>29.42 <b>(-31.68%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.00 (n/a)</td><td>176.42 (n/a)</td><td>170.40 (n/a)</td><td>132.20 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (+15.57%)</td><td>0.04 (+15.63%)</td><td>0.04 <b>(+20.78%)</b></td><td>0.03 <b>(+24.35%)</b></td><td>0.01 (-8.17%)</td><td>178.40 (-19.57%)</td><td>155.86 (-14.48%)</td><td>161.60 (-17.21%)</td><td>124.70 (-13.46%)</td><td>22.45 <b>(-33.96%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>182.26 (n/a)</td><td>195.20 (n/a)</td><td>144.10 (n/a)</td><td>33.99 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (+11.60%)</td><td>0.04 (-2.95%)</td><td>0.03 (-11.33%)</td><td>0.03 (-12.36%)</td><td>0.01 <b>(+54.04%)</b></td><td>214.90 (+14.13%)</td><td>173.00 (+5.80%)</td><td>181.90 (+12.77%)</td><td>113.50 (-10.42%)</td><td>38.12 <b>(+49.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.30 (n/a)</td><td>163.52 (n/a)</td><td>161.30 (n/a)</td><td>126.70 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 <b>(+27.26%)</b></td><td>0.04 <b>(+32.72%)</b></td><td>0.04 <b>(+31.19%)</b></td><td>0.03 <b>(+45.64%)</b></td><td>0.01 (+3.61%)</td><td>206.50 <b>(-31.33%)</b></td><td>163.98 <b>(-25.66%)</b></td><td>154.30 <b>(-23.76%)</b></td><td>139.90 <b>(-21.40%)</b></td><td>26.34 <b>(-45.02%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>300.70 (n/a)</td><td>220.58 (n/a)</td><td>202.40 (n/a)</td><td>178.00 (n/a)</td><td>47.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 <b>(+23.60%)</b></td><td>0.04 (+3.71%)</td><td>0.04 (-0.22%)</td><td>0.02 <b>(-27.00%)</b></td><td>0.01 <b>(+153.30%)</b></td><td>269.20 <b>(+37.00%)</b></td><td>177.32 (+3.70%)</td><td>174.40 (+0.23%)</td><td>115.00 (-19.13%)</td><td>59.82 <b>(+181.70%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>196.50 (n/a)</td><td>171.00 (n/a)</td><td>174.00 (n/a)</td><td>142.20 (n/a)</td><td>21.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (+1.68%)</td><td>0.03 (-1.86%)</td><td>0.03 (-3.48%)</td><td>0.03 (-2.40%)</td><td>0.01 (-10.12%)</td><td>223.50 (+2.43%)</td><td>180.48 (+1.29%)</td><td>181.00 (+3.61%)</td><td>139.70 (-1.69%)</td><td>30.59 (-10.06%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>178.18 (n/a)</td><td>174.70 (n/a)</td><td>142.10 (n/a)</td><td>34.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 <b>(-26.17%)</b></td><td>0.03 (-16.70%)</td><td>0.03 (-16.20%)</td><td>0.03 (-13.51%)</td><td>0.00 <b>(-45.43%)</b></td><td>229.20 (+15.64%)</td><td>197.80 (+18.86%)</td><td>195.20 (+19.32%)</td><td>176.70 <b>(+35.51%)</b></td><td>21.55 (-14.14%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>166.42 (n/a)</td><td>163.60 (n/a)</td><td>130.40 (n/a)</td><td>25.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 <b>(-21.83%)</b></td><td>0.07 (-10.52%)</td><td>0.07 (+5.34%)</td><td>0.06 (-6.61%)</td><td>0.01 <b>(-50.41%)</b></td><td>199.60 (+7.08%)</td><td>176.70 (+10.11%)</td><td>165.00 (-5.06%)</td><td>163.30 <b>(+27.88%)</b></td><td>17.57 <b>(-32.28%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.40 (n/a)</td><td>160.48 (n/a)</td><td>173.80 (n/a)</td><td>127.70 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.09 (-12.90%)</td><td>0.08 (-9.71%)</td><td>0.08 (+6.04%)</td><td>0.06 (-11.56%)</td><td>0.02 (-2.59%)</td><td>213.60 (+13.08%)</td><td>168.70 (+11.80%)</td><td>145.90 (-5.69%)</td><td>133.80 (+14.75%)</td><td>39.60 <b>(+31.82%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>188.90 (n/a)</td><td>150.90 (n/a)</td><td>154.70 (n/a)</td><td>116.60 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.09 (-7.26%)</td><td>0.07 (+3.68%)</td><td>0.07 (+8.06%)</td><td>0.06 <b>(+22.76%)</b></td><td>0.01 <b>(-39.20%)</b></td><td>193.20 (-18.55%)</td><td>169.10 (-6.93%)</td><td>164.10 (-7.50%)</td><td>134.40 (+7.87%)</td><td>24.75 <b>(-45.97%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>237.20 (n/a)</td><td>181.70 (n/a)</td><td>177.40 (n/a)</td><td>124.60 (n/a)</td><td>45.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (+0.03%)</td><td>0.07 (-5.48%)</td><td>0.07 (+6.97%)</td><td>0.03 <b>(-44.68%)</b></td><td>0.02 <b>(+113.71%)</b></td><td>379.80 <b>(+80.77%)</b></td><td>209.48 (+17.28%)</td><td>168.10 (-6.51%)</td><td>145.30 (+0.00%)</td><td>96.58 <b>(+319.11%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>178.62 (n/a)</td><td>179.80 (n/a)</td><td>145.30 (n/a)</td><td>23.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.09 (-8.64%)</td><td>0.07 (-11.88%)</td><td>0.07 (-13.46%)</td><td>0.06 (-8.27%)</td><td>0.01 <b>(-21.86%)</b></td><td>207.50 (+9.04%)</td><td>173.24 (+12.77%)</td><td>178.60 (+15.60%)</td><td>138.80 (+9.38%)</td><td>25.94 (-4.49%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>153.62 (n/a)</td><td>154.50 (n/a)</td><td>126.90 (n/a)</td><td>27.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (-11.49%)</td><td>0.07 (+0.25%)</td><td>0.07 (-3.31%)</td><td>0.06 <b>(+22.13%)</b></td><td>0.01 <b>(-58.61%)</b></td><td>204.70 (-18.12%)</td><td>175.80 (-3.90%)</td><td>174.00 (+3.45%)</td><td>158.90 (+13.02%)</td><td>17.57 <b>(-61.09%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>250.00 (n/a)</td><td>182.94 (n/a)</td><td>168.20 (n/a)</td><td>140.60 (n/a)</td><td>45.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 <b>(-28.34%)</b></td><td>0.07 (-15.54%)</td><td>0.06 (-9.41%)</td><td>0.05 (-11.46%)</td><td>0.01 <b>(-35.84%)</b></td><td>233.60 (+12.96%)</td><td>194.64 (+16.84%)</td><td>194.80 (+10.37%)</td><td>156.00 <b>(+39.53%)</b></td><td>36.85 (+5.53%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>206.80 (n/a)</td><td>166.58 (n/a)</td><td>176.50 (n/a)</td><td>111.80 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 <b>(+41.77%)</b></td><td>0.08 (+18.66%)</td><td>0.07 (-1.89%)</td><td>0.06 <b>(+39.43%)</b></td><td>0.02 (+18.09%)</td><td>203.50 <b>(-28.27%)</b></td><td>169.66 (-17.19%)</td><td>169.60 (+1.92%)</td><td>113.60 <b>(-29.48%)</b></td><td>34.68 <b>(-40.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>283.70 (n/a)</td><td>204.88 (n/a)</td><td>166.40 (n/a)</td><td>161.10 (n/a)</td><td>58.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (+5.47%)</td><td>0.18 (+7.26%)</td><td>0.19 (+6.56%)</td><td>0.15 (+2.38%)</td><td>0.02 (+11.18%)</td><td>164.90 (-2.31%)</td><td>134.66 (-6.59%)</td><td>130.10 (-6.20%)</td><td>117.20 (-5.18%)</td><td>18.21 (+4.56%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>168.80 (n/a)</td><td>144.16 (n/a)</td><td>138.70 (n/a)</td><td>123.60 (n/a)</td><td>17.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (-4.35%)</td><td>0.16 (+7.38%)</td><td>0.15 (+9.01%)</td><td>0.14 <b>(+36.63%)</b></td><td>0.02 <b>(-51.18%)</b></td><td>171.70 <b>(-26.81%)</b></td><td>156.10 (-10.39%)</td><td>163.80 (-8.29%)</td><td>136.50 (+4.60%)</td><td>16.50 <b>(-61.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>234.60 (n/a)</td><td>174.20 (n/a)</td><td>178.60 (n/a)</td><td>130.50 (n/a)</td><td>42.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 (+13.27%)</td><td>0.16 (+13.71%)</td><td>0.17 <b>(+24.61%)</b></td><td>0.12 (+2.26%)</td><td>0.03 <b>(+34.97%)</b></td><td>211.90 (-2.22%)</td><td>156.06 (-10.90%)</td><td>144.20 (-19.76%)</td><td>125.20 (-11.71%)</td><td>34.72 (+18.73%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.70 (n/a)</td><td>175.16 (n/a)</td><td>179.70 (n/a)</td><td>141.80 (n/a)</td><td>29.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (-5.76%)</td><td>0.16 (-2.43%)</td><td>0.16 (-2.46%)</td><td>0.13 (+2.56%)</td><td>0.02 <b>(-21.65%)</b></td><td>184.10 (-2.49%)</td><td>157.86 (+1.92%)</td><td>155.20 (+2.51%)</td><td>135.40 (+6.11%)</td><td>17.67 (-19.35%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>188.80 (n/a)</td><td>154.88 (n/a)</td><td>151.40 (n/a)</td><td>127.60 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 <b>(-22.68%)</b></td><td>0.14 (-15.81%)</td><td>0.13 (-19.22%)</td><td>0.12 (-9.47%)</td><td>0.02 <b>(-38.39%)</b></td><td>211.70 (+10.43%)</td><td>183.68 (+17.50%)</td><td>192.80 <b>(+23.75%)</b></td><td>158.50 <b>(+29.39%)</b></td><td>22.66 (-13.65%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.70 (n/a)</td><td>156.32 (n/a)</td><td>155.80 (n/a)</td><td>122.50 (n/a)</td><td>26.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.17 (-9.21%)</td><td>0.15 (-3.35%)</td><td>0.16 (+2.92%)</td><td>0.13 (-9.40%)</td><td>0.02 (+7.39%)</td><td>195.30 (+10.40%)</td><td>166.60 (+3.87%)</td><td>156.70 (-2.85%)</td><td>147.80 (+10.22%)</td><td>21.52 <b>(+31.71%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>176.90 (n/a)</td><td>160.40 (n/a)</td><td>161.30 (n/a)</td><td>134.10 (n/a)</td><td>16.34 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (-5.37%)</td><td>0.13 (+0.05%)</td><td>0.13 (-2.37%)</td><td>0.08 (-5.37%)</td><td>0.04 (-8.54%)</td><td>304.90 (+5.68%)</td><td>200.20 (-0.36%)</td><td>196.00 (+2.46%)</td><td>137.40 (+5.69%)</td><td>63.84 (+4.76%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>288.50 (n/a)</td><td>200.92 (n/a)</td><td>191.30 (n/a)</td><td>130.00 (n/a)</td><td>60.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 (+18.23%)</td><td>0.16 <b>(+22.86%)</b></td><td>0.16 (+19.41%)</td><td>0.13 <b>(+50.64%)</b></td><td>0.03 (-16.74%)</td><td>192.40 <b>(-33.61%)</b></td><td>154.48 <b>(-21.38%)</b></td><td>154.80 (-16.23%)</td><td>124.60 (-15.41%)</td><td>26.42 <b>(-53.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>289.80 (n/a)</td><td>196.50 (n/a)</td><td>184.80 (n/a)</td><td>147.30 (n/a)</td><td>57.05 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.36 (-1.57%)</td><td>0.28 (-9.41%)</td><td>0.29 (-2.97%)</td><td>0.22 (-17.20%)</td><td>0.05 (+9.56%)</td><td>220.50 <b>(+20.82%)</b></td><td>177.30 (+11.26%)</td><td>172.10 (+3.05%)</td><td>137.80 (+1.62%)</td><td>30.22 <b>(+37.23%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>182.50 (n/a)</td><td>159.36 (n/a)</td><td>167.00 (n/a)</td><td>135.60 (n/a)</td><td>22.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.38 (-12.41%)</td><td>0.33 (-3.10%)</td><td>0.33 (+6.02%)</td><td>0.27 (+14.58%)</td><td>0.05 <b>(-39.52%)</b></td><td>180.30 (-12.73%)</td><td>152.18 (+0.05%)</td><td>147.80 (-5.68%)</td><td>128.10 (+14.17%)</td><td>23.85 <b>(-37.89%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.08 (n/a)</td><td>206.60 (n/a)</td><td>152.10 (n/a)</td><td>156.70 (n/a)</td><td>112.20 (n/a)</td><td>38.41 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.37 (+9.29%)</td><td>0.30 (-4.34%)</td><td>0.30 (-7.57%)</td><td>0.25 (-9.25%)</td><td>0.04 <b>(+62.30%)</b></td><td>198.40 (+10.16%)</td><td>164.76 (+5.60%)</td><td>163.20 (+8.22%)</td><td>132.10 (-8.52%)</td><td>23.50 <b>(+61.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>180.10 (n/a)</td><td>156.02 (n/a)</td><td>150.80 (n/a)</td><td>144.40 (n/a)</td><td>14.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.37 <b>(+20.49%)</b></td><td>0.28 (+1.89%)</td><td>0.27 (+0.70%)</td><td>0.21 (-10.60%)</td><td>0.06 <b>(+93.58%)</b></td><td>232.10 (+11.86%)</td><td>180.28 (+0.43%)</td><td>181.50 (-0.71%)</td><td>131.80 (-17.00%)</td><td>35.87 <b>(+80.06%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>207.50 (n/a)</td><td>179.50 (n/a)</td><td>182.80 (n/a)</td><td>158.80 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.37 (+18.62%)</td><td>0.31 <b>(+22.49%)</b></td><td>0.29 (+7.46%)</td><td>0.24 <b>(+38.69%)</b></td><td>0.05 (-15.89%)</td><td>203.80 <b>(-27.91%)</b></td><td>163.78 <b>(-20.84%)</b></td><td>168.20 (-6.92%)</td><td>131.50 (-15.71%)</td><td>28.12 <b>(-49.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>282.70 (n/a)</td><td>206.90 (n/a)</td><td>180.70 (n/a)</td><td>156.00 (n/a)</td><td>55.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.36 <b>(+34.10%)</b></td><td>0.29 <b>(+44.37%)</b></td><td>0.27 <b>(+35.96%)</b></td><td>0.23 <b>(+79.89%)</b></td><td>0.06 (+16.47%)</td><td>211.20 <b>(-44.42%)</b></td><td>176.42 <b>(-32.36%)</b></td><td>184.40 <b>(-26.45%)</b></td><td>138.20 <b>(-25.42%)</b></td><td>33.42 <b>(-53.79%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>380.00 (n/a)</td><td>260.82 (n/a)</td><td>250.70 (n/a)</td><td>185.30 (n/a)</td><td>72.32 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.33 (-7.04%)</td><td>0.26 (-1.76%)</td><td>0.26 (-1.42%)</td><td>0.15 (-4.92%)</td><td>0.07 (-10.53%)</td><td>333.80 (+5.17%)</td><td>207.56 (+1.18%)</td><td>190.70 (+1.49%)</td><td>150.00 (+7.60%)</td><td>74.42 (+3.47%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>317.40 (n/a)</td><td>205.14 (n/a)</td><td>187.90 (n/a)</td><td>139.40 (n/a)</td><td>71.92 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.40 (+15.53%)</td><td>0.32 (+8.91%)</td><td>0.37 <b>(+28.72%)</b></td><td>0.19 <b>(-28.19%)</b></td><td>0.10 <b>(+165.47%)</b></td><td>264.60 <b>(+39.26%)</b></td><td>170.44 (-0.26%)</td><td>134.20 <b>(-22.34%)</b></td><td>121.50 (-13.40%)</td><td>62.86 <b>(+211.79%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>190.00 (n/a)</td><td>170.88 (n/a)</td><td>172.80 (n/a)</td><td>140.30 (n/a)</td><td>20.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (+16.36%)</td><td>0.01 (-9.80%)</td><td>0.01 (-14.68%)</td><td>0.01 <b>(-54.05%)</b></td><td>0.01 <b>(+195.05%)</b></td><td>410.90 <b>(+117.64%)</b></td><td>220.32 <b>(+29.45%)</b></td><td>207.70 (+17.21%)</td><td>122.30 (-14.05%)</td><td>112.85 <b>(+471.48%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>188.80 (n/a)</td><td>170.20 (n/a)</td><td>177.20 (n/a)</td><td>142.30 (n/a)</td><td>19.75 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+14.80%)</td><td>0.02 (+4.80%)</td><td>0.02 (-0.27%)</td><td>0.01 <b>(+55.97%)</b></td><td>0.00 (-6.64%)</td><td>206.30 <b>(-35.89%)</b></td><td>162.16 (-10.39%)</td><td>158.20 (+0.25%)</td><td>103.80 (-12.92%)</td><td>39.24 <b>(-51.75%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>321.80 (n/a)</td><td>180.96 (n/a)</td><td>157.80 (n/a)</td><td>119.20 (n/a)</td><td>81.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (-2.90%)</td><td>0.02 (-4.34%)</td><td>0.02 (-7.40%)</td><td>0.02 (+10.85%)</td><td>0.00 <b>(-35.97%)</b></td><td>169.80 (-9.78%)</td><td>148.18 (+2.46%)</td><td>145.70 (+7.93%)</td><td>122.10 (+2.95%)</td><td>18.31 <b>(-39.27%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>188.20 (n/a)</td><td>144.62 (n/a)</td><td>135.00 (n/a)</td><td>118.60 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (-14.00%)</td><td>0.02 (+1.50%)</td><td>0.02 <b>(+26.96%)</b></td><td>0.01 (-2.70%)</td><td>0.00 <b>(-31.23%)</b></td><td>235.00 (+2.75%)</td><td>165.36 (-4.57%)</td><td>154.70 <b>(-21.23%)</b></td><td>126.50 (+16.27%)</td><td>42.53 (-15.09%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>173.28 (n/a)</td><td>196.40 (n/a)</td><td>108.80 (n/a)</td><td>50.08 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (-15.04%)</td><td>0.01 (-8.01%)</td><td>0.01 (+1.67%)</td><td>0.01 (-18.89%)</td><td>0.00 (-15.63%)</td><td>247.90 <b>(+23.27%)</b></td><td>190.70 (+8.90%)</td><td>182.40 (-1.62%)</td><td>152.60 (+17.75%)</td><td>35.71 <b>(+28.08%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>201.10 (n/a)</td><td>175.12 (n/a)</td><td>185.40 (n/a)</td><td>129.60 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (-8.46%)</td><td>0.02 (-2.28%)</td><td>0.02 (-0.62%)</td><td>0.01 (+0.13%)</td><td>0.00 <b>(-28.83%)</b></td><td>190.00 (-0.16%)</td><td>169.68 (+1.56%)</td><td>173.90 (+0.64%)</td><td>142.10 (+9.31%)</td><td>18.11 <b>(-21.98%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>190.30 (n/a)</td><td>167.08 (n/a)</td><td>172.80 (n/a)</td><td>130.00 (n/a)</td><td>23.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (-7.80%)</td><td>0.02 (+19.02%)</td><td>0.02 <b>(+47.03%)</b></td><td>0.01 <b>(+35.01%)</b></td><td>0.00 <b>(-37.97%)</b></td><td>213.10 <b>(-25.93%)</b></td><td>174.32 <b>(-21.13%)</b></td><td>166.20 <b>(-32.00%)</b></td><td>130.90 (+8.45%)</td><td>34.81 <b>(-47.28%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>287.70 (n/a)</td><td>221.02 (n/a)</td><td>244.40 (n/a)</td><td>120.70 (n/a)</td><td>66.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (+9.13%)</td><td>0.01 (+11.40%)</td><td>0.01 (+17.83%)</td><td>0.01 (-1.28%)</td><td>0.00 <b>(+73.88%)</b></td><td>237.20 (+1.28%)</td><td>191.84 (-9.45%)</td><td>180.30 (-15.11%)</td><td>173.90 (-8.38%)</td><td>26.39 <b>(+62.89%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>234.20 (n/a)</td><td>211.86 (n/a)</td><td>212.40 (n/a)</td><td>189.80 (n/a)</td><td>16.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-13.77%)</td><td>0.03 (-19.31%)</td><td>0.03 <b>(-21.04%)</b></td><td>0.03 <b>(-20.41%)</b></td><td>0.00 <b>(+23.79%)</b></td><td>187.90 <b>(+25.60%)</b></td><td>174.04 <b>(+24.31%)</b></td><td>181.40 <b>(+26.59%)</b></td><td>152.20 (+16.01%)</td><td>14.44 <b>(+80.89%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>149.60 (n/a)</td><td>140.00 (n/a)</td><td>143.30 (n/a)</td><td>131.20 (n/a)</td><td>7.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (+10.74%)</td><td>0.03 (-8.28%)</td><td>0.03 <b>(-22.35%)</b></td><td>0.02 <b>(-24.75%)</b></td><td>0.01 <b>(+176.82%)</b></td><td>217.00 <b>(+32.88%)</b></td><td>166.98 (+15.99%)</td><td>190.70 <b>(+28.76%)</b></td><td>115.50 (-9.70%)</td><td>46.70 <b>(+221.47%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>163.30 (n/a)</td><td>143.96 (n/a)</td><td>148.10 (n/a)</td><td>127.90 (n/a)</td><td>14.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 <b>(+25.41%)</b></td><td>0.04 (+12.25%)</td><td>0.04 (-0.60%)</td><td>0.03 (+12.93%)</td><td>0.01 <b>(+50.89%)</b></td><td>166.50 (-11.44%)</td><td>140.54 (-10.06%)</td><td>148.30 (+0.61%)</td><td>103.60 <b>(-20.31%)</b></td><td>24.07 (+3.21%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>188.00 (n/a)</td><td>156.26 (n/a)</td><td>147.40 (n/a)</td><td>130.00 (n/a)</td><td>23.32 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (-3.33%)</td><td>0.03 (-2.32%)</td><td>0.03 (-9.27%)</td><td>0.03 (-10.92%)</td><td>0.01 <b>(+37.98%)</b></td><td>193.90 (+12.21%)</td><td>159.98 (+4.47%)</td><td>175.60 (+10.23%)</td><td>122.70 (+3.46%)</td><td>33.16 <b>(+60.71%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>172.80 (n/a)</td><td>153.14 (n/a)</td><td>159.30 (n/a)</td><td>118.60 (n/a)</td><td>20.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (-19.62%)</td><td>0.03 <b>(-27.79%)</b></td><td>0.03 <b>(-23.14%)</b></td><td>0.01 <b>(-52.98%)</b></td><td>0.01 (+18.29%)</td><td>356.80 <b>(+112.63%)</b></td><td>212.86 <b>(+49.46%)</b></td><td>195.00 <b>(+30.09%)</b></td><td>129.70 <b>(+24.47%)</b></td><td>85.11 <b>(+232.60%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>167.80 (n/a)</td><td>142.42 (n/a)</td><td>149.90 (n/a)</td><td>104.20 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (+6.57%)</td><td>0.03 (+5.19%)</td><td>0.03 (+15.51%)</td><td>0.02 (-2.35%)</td><td>0.01 (+2.04%)</td><td>217.80 (+2.45%)</td><td>166.22 (-4.88%)</td><td>159.50 (-13.46%)</td><td>127.90 (-6.16%)</td><td>32.71 (+1.40%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>174.74 (n/a)</td><td>184.30 (n/a)</td><td>136.30 (n/a)</td><td>32.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (-14.28%)</td><td>0.03 (-8.90%)</td><td>0.03 (-2.77%)</td><td>0.03 (-0.23%)</td><td>0.00 <b>(-27.78%)</b></td><td>191.20 (+0.21%)</td><td>168.00 (+8.99%)</td><td>157.70 (+2.87%)</td><td>148.70 (+16.63%)</td><td>20.53 (-14.75%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>154.14 (n/a)</td><td>153.30 (n/a)</td><td>127.50 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-3.48%)</td><td>0.03 (+3.32%)</td><td>0.03 (+5.51%)</td><td>0.02 (+3.06%)</td><td>0.00 (-18.66%)</td><td>233.00 (-3.00%)</td><td>202.40 (-3.65%)</td><td>193.90 (-5.23%)</td><td>177.50 (+3.62%)</td><td>22.08 (-17.61%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.20 (n/a)</td><td>210.06 (n/a)</td><td>204.60 (n/a)</td><td>171.30 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (-15.80%)</td><td>0.05 (-20.00%)</td><td>0.06 (-6.47%)</td><td>0.03 <b>(-49.56%)</b></td><td>0.02 (+16.91%)</td><td>377.20 <b>(+98.21%)</b></td><td>214.02 <b>(+34.60%)</b></td><td>180.30 (+6.94%)</td><td>149.60 (+18.73%)</td><td>92.77 <b>(+202.79%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>159.00 (n/a)</td><td>168.60 (n/a)</td><td>126.00 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (-14.47%)</td><td>0.07 (-0.54%)</td><td>0.08 (+18.95%)</td><td>0.05 (+1.41%)</td><td>0.02 (-15.64%)</td><td>222.90 (-1.42%)</td><td>162.60 (-0.36%)</td><td>138.20 (-15.94%)</td><td>128.30 (+16.85%)</td><td>41.63 (-2.99%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>226.10 (n/a)</td><td>163.18 (n/a)</td><td>164.40 (n/a)</td><td>109.80 (n/a)</td><td>42.92 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (-12.06%)</td><td>0.06 (-2.07%)</td><td>0.06 (+14.41%)</td><td>0.03 <b>(-32.57%)</b></td><td>0.02 (+13.67%)</td><td>308.30 <b>(+48.29%)</b></td><td>188.30 (+6.72%)</td><td>165.50 (-12.62%)</td><td>139.70 (+13.67%)</td><td>68.48 <b>(+110.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>176.44 (n/a)</td><td>189.40 (n/a)</td><td>122.90 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (-4.96%)</td><td>0.06 (-11.76%)</td><td>0.06 (-6.27%)</td><td>0.04 <b>(-28.54%)</b></td><td>0.02 (+18.73%)</td><td>292.40 <b>(+39.97%)</b></td><td>194.70 (+17.60%)</td><td>180.10 (+6.69%)</td><td>136.40 (+5.17%)</td><td>61.82 <b>(+81.38%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>165.56 (n/a)</td><td>168.80 (n/a)</td><td>129.70 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (+2.37%)</td><td>0.06 (-5.00%)</td><td>0.06 (-12.22%)</td><td>0.05 (-3.57%)</td><td>0.01 (-0.06%)</td><td>207.30 (+3.70%)</td><td>175.34 (+5.11%)</td><td>177.90 (+13.89%)</td><td>131.30 (-2.31%)</td><td>27.53 (-5.36%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>166.82 (n/a)</td><td>156.20 (n/a)</td><td>134.40 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 <b>(-26.14%)</b></td><td>0.05 (-17.71%)</td><td>0.05 <b>(-20.48%)</b></td><td>0.05 <b>(+24.52%)</b></td><td>0.01 <b>(-53.10%)</b></td><td>228.10 (-19.68%)</td><td>208.50 (+14.05%)</td><td>225.70 <b>(+25.74%)</b></td><td>155.60 <b>(+35.42%)</b></td><td>31.12 <b>(-50.20%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>284.00 (n/a)</td><td>182.82 (n/a)</td><td>179.50 (n/a)</td><td>114.90 (n/a)</td><td>62.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (+2.80%)</td><td>0.06 (-9.82%)</td><td>0.05 (-16.66%)</td><td>0.05 (+4.58%)</td><td>0.01 (-1.60%)</td><td>229.00 (-4.38%)</td><td>191.48 (+10.48%)</td><td>191.20 <b>(+20.03%)</b></td><td>138.80 (-2.73%)</td><td>35.88 (-9.39%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>173.32 (n/a)</td><td>159.30 (n/a)</td><td>142.70 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (-10.77%)</td><td>0.05 (-12.10%)</td><td>0.04 (-19.80%)</td><td>0.04 (+4.74%)</td><td>0.01 <b>(-31.19%)</b></td><td>239.90 (-4.54%)</td><td>218.60 (+12.62%)</td><td>233.90 <b>(+24.68%)</b></td><td>189.00 (+12.10%)</td><td>24.03 <b>(-27.84%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>251.30 (n/a)</td><td>194.10 (n/a)</td><td>187.60 (n/a)</td><td>168.60 (n/a)</td><td>33.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (-10.76%)</td><td>0.11 (-8.22%)</td><td>0.11 (-6.05%)</td><td>0.10 (-6.24%)</td><td>0.01 <b>(-30.27%)</b></td><td>218.60 (+6.63%)</td><td>191.68 (+8.31%)</td><td>194.20 (+6.41%)</td><td>165.30 (+12.07%)</td><td>19.60 (-16.45%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>205.00 (n/a)</td><td>176.98 (n/a)</td><td>182.50 (n/a)</td><td>147.50 (n/a)</td><td>23.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (-18.75%)</td><td>0.11 (-4.50%)</td><td>0.12 (-1.15%)</td><td>0.11 (+10.08%)</td><td>0.01 <b>(-69.16%)</b></td><td>192.50 (-9.16%)</td><td>183.20 (+2.82%)</td><td>182.40 (+1.11%)</td><td>168.50 <b>(+23.08%)</b></td><td>9.62 <b>(-64.52%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.90 (n/a)</td><td>178.18 (n/a)</td><td>180.40 (n/a)</td><td>136.90 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 <b>(+46.91%)</b></td><td>0.13 (+8.36%)</td><td>0.12 (+1.55%)</td><td>0.07 <b>(-27.77%)</b></td><td>0.05 <b>(+195.60%)</b></td><td>321.90 <b>(+38.45%)</b></td><td>188.74 (+3.99%)</td><td>169.10 (-1.51%)</td><td>107.90 <b>(-31.92%)</b></td><td>83.31 <b>(+178.64%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>232.50 (n/a)</td><td>181.50 (n/a)</td><td>171.70 (n/a)</td><td>158.50 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (-9.27%)</td><td>0.11 (-1.95%)</td><td>0.11 (-0.87%)</td><td>0.10 (-2.50%)</td><td>0.01 <b>(-24.55%)</b></td><td>216.10 (+2.56%)</td><td>191.16 (+1.65%)</td><td>194.00 (+0.88%)</td><td>171.40 (+10.23%)</td><td>17.52 (-12.93%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>188.06 (n/a)</td><td>192.30 (n/a)</td><td>155.50 (n/a)</td><td>20.12 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 <b>(+20.63%)</b></td><td>0.14 <b>(+23.74%)</b></td><td>0.13 <b>(+20.56%)</b></td><td>0.11 <b>(+39.88%)</b></td><td>0.03 (-1.33%)</td><td>195.30 <b>(-28.49%)</b></td><td>156.26 <b>(-21.57%)</b></td><td>162.10 (-17.08%)</td><td>113.10 (-17.08%)</td><td>35.72 <b>(-40.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>273.10 (n/a)</td><td>199.24 (n/a)</td><td>195.50 (n/a)</td><td>136.40 (n/a)</td><td>60.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (+6.06%)</td><td>0.11 (-6.58%)</td><td>0.12 (-4.31%)</td><td>0.07 <b>(-27.18%)</b></td><td>0.03 <b>(+41.01%)</b></td><td>306.50 <b>(+37.32%)</b></td><td>205.50 (+11.15%)</td><td>178.70 (+4.50%)</td><td>147.00 (-5.71%)</td><td>61.85 <b>(+88.00%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>223.20 (n/a)</td><td>184.88 (n/a)</td><td>171.00 (n/a)</td><td>155.90 (n/a)</td><td>32.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 <b>(-37.34%)</b></td><td>0.10 <b>(-21.54%)</b></td><td>0.11 (-9.79%)</td><td>0.07 <b>(-35.63%)</b></td><td>0.02 <b>(-42.06%)</b></td><td>309.40 <b>(+55.32%)</b></td><td>213.62 <b>(+26.94%)</b></td><td>191.90 (+10.80%)</td><td>174.80 <b>(+59.63%)</b></td><td>54.53 <b>(+56.56%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>199.20 (n/a)</td><td>168.28 (n/a)</td><td>173.20 (n/a)</td><td>109.50 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (+2.00%)</td><td>0.10 (-1.06%)</td><td>0.09 (-6.72%)</td><td>0.09 (+0.81%)</td><td>0.01 (+14.29%)</td><td>232.90 (-0.81%)</td><td>213.28 (+1.37%)</td><td>225.40 (+7.23%)</td><td>171.10 (-1.95%)</td><td>25.43 (+12.10%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>234.80 (n/a)</td><td>210.40 (n/a)</td><td>210.20 (n/a)</td><td>174.50 (n/a)</td><td>22.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.10 (n/a)</td><td>170.96 (n/a)</td><td>157.90 (n/a)</td><td>128.10 (n/a)</td><td>39.85 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.20 (n/a)</td><td>187.62 (n/a)</td><td>195.50 (n/a)</td><td>162.90 (n/a)</td><td>15.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>365.50 (n/a)</td><td>225.12 (n/a)</td><td>193.90 (n/a)</td><td>155.70 (n/a)</td><td>81.74 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.40 (n/a)</td><td>202.80 (n/a)</td><td>217.60 (n/a)</td><td>134.60 (n/a)</td><td>48.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>255.70 (n/a)</td><td>180.54 (n/a)</td><td>173.90 (n/a)</td><td>122.20 (n/a)</td><td>51.35 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>225.30 (n/a)</td><td>176.18 (n/a)</td><td>203.90 (n/a)</td><td>113.90 (n/a)</td><td>49.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>167.36 (n/a)</td><td>159.20 (n/a)</td><td>148.40 (n/a)</td><td>18.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>258.00 (n/a)</td><td>195.40 (n/a)</td><td>190.10 (n/a)</td><td>111.50 (n/a)</td><td>60.83 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.80 (n/a)</td><td>165.80 (n/a)</td><td>174.20 (n/a)</td><td>121.00 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.80 (n/a)</td><td>171.10 (n/a)</td><td>184.10 (n/a)</td><td>116.60 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>239.20 (n/a)</td><td>158.84 (n/a)</td><td>156.10 (n/a)</td><td>106.50 (n/a)</td><td>49.54 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>242.40 (n/a)</td><td>175.92 (n/a)</td><td>164.60 (n/a)</td><td>113.80 (n/a)</td><td>53.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.41 (+11.35%)</td><td>0.32 (+5.00%)</td><td>0.30 (+0.20%)</td><td>0.24 (+1.42%)</td><td>0.07 (+13.52%)</td><td>205.20 (-1.39%)</td><td>160.26 (-4.30%)</td><td>165.60 (-0.24%)</td><td>119.70 (-10.20%)</td><td>35.11 (+1.24%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>208.10 (n/a)</td><td>167.46 (n/a)</td><td>166.00 (n/a)</td><td>133.30 (n/a)</td><td>34.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>355.60 (n/a)</td><td>200.28 (n/a)</td><td>166.40 (n/a)</td><td>132.20 (n/a)</td><td>91.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>199.90 (n/a)</td><td>180.52 (n/a)</td><td>189.80 (n/a)</td><td>127.10 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>261.00 (n/a)</td><td>187.22 (n/a)</td><td>190.70 (n/a)</td><td>129.70 (n/a)</td><td>48.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>175.70 (n/a)</td><td>131.98 (n/a)</td><td>134.50 (n/a)</td><td>105.70 (n/a)</td><td>28.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>135.72 (n/a)</td><td>117.90 (n/a)</td><td>98.40 (n/a)</td><td>37.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>157.16 (n/a)</td><td>153.30 (n/a)</td><td>130.90 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>197.20 (n/a)</td><td>167.90 (n/a)</td><td>161.20 (n/a)</td><td>141.10 (n/a)</td><td>22.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>261.70 (n/a)</td><td>163.50 (n/a)</td><td>152.10 (n/a)</td><td>125.30 (n/a)</td><td>56.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>279.40 (n/a)</td><td>160.90 (n/a)</td><td>131.70 (n/a)</td><td>113.60 (n/a)</td><td>67.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>224.20 (n/a)</td><td>155.04 (n/a)</td><td>134.20 (n/a)</td><td>130.40 (n/a)</td><td>39.83 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>173.30 (n/a)</td><td>160.20 (n/a)</td><td>148.70 (n/a)</td><td>27.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>182.10 (n/a)</td><td>143.38 (n/a)</td><td>130.10 (n/a)</td><td>113.60 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.60 (n/a)</td><td>148.12 (n/a)</td><td>138.30 (n/a)</td><td>117.90 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>236.90 (n/a)</td><td>191.74 (n/a)</td><td>186.20 (n/a)</td><td>154.90 (n/a)</td><td>30.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>223.40 (n/a)</td><td>167.08 (n/a)</td><td>168.50 (n/a)</td><td>115.60 (n/a)</td><td>41.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>216.00 (n/a)</td><td>178.22 (n/a)</td><td>188.70 (n/a)</td><td>112.30 (n/a)</td><td>38.99 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>207.30 (n/a)</td><td>180.62 (n/a)</td><td>190.50 (n/a)</td><td>153.00 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>204.00 (n/a)</td><td>180.06 (n/a)</td><td>192.70 (n/a)</td><td>147.00 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.59 (-5.04%)</td><td>14.19 (-0.80%)</td><td>14.31 (-0.56%)</td><td>13.17 (+1.00%)</td><td>0.59 <b>(-29.00%)</b></td><td>4228.40 (-0.99%)</td><td>3930.98 (+0.67%)</td><td>3892.10 (+0.56%)</td><td>3818.80 (+5.31%)</td><td>170.51 <b>(-26.33%)</b></td><td>14058.67 (-5.04%)</td><td>13677.09 (-0.80%)</td><td>13793.98 (-0.56%)</td><td>12696.88 (+1.00%)</td><td>564.68 <b>(-29.00%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>15.36 (n/a)</td><td>14.31 (n/a)</td><td>14.39 (n/a)</td><td>13.04 (n/a)</td><td>0.83 (n/a)</td><td>4270.80 (n/a)</td><td>3904.76 (n/a)</td><td>3870.40 (n/a)</td><td>3626.30 (n/a)</td><td>231.43 (n/a)</td><td>14804.78 (n/a)</td><td>13786.70 (n/a)</td><td>13871.06 (n/a)</td><td>12570.64 (n/a)</td><td>795.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>16.18 (+10.35%)</td><td>14.71 (+13.79%)</td><td>14.58 (+10.34%)</td><td>13.71 <b>(+40.05%)</b></td><td>0.90 <b>(-51.55%)</b></td><td>956.10 <b>(-28.60%)</b></td><td>893.60 (-13.59%)</td><td>899.20 (-9.37%)</td><td>810.00 (-9.39%)</td><td>52.61 <b>(-70.04%)</b></td><td>10604.70 (+10.35%)</td><td>9640.38 (+13.79%)</td><td>9552.75 (+10.34%)</td><td>8984.53 <b>(+40.05%)</b></td><td>590.54 <b>(-51.56%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.66 (n/a)</td><td>12.93 (n/a)</td><td>13.21 (n/a)</td><td>9.79 (n/a)</td><td>1.86 (n/a)</td><td>1339.00 (n/a)</td><td>1034.08 (n/a)</td><td>992.20 (n/a)</td><td>893.90 (n/a)</td><td>175.60 (n/a)</td><td>9609.80 (n/a)</td><td>8471.71 (n/a)</td><td>8657.82 (n/a)</td><td>6415.14 (n/a)</td><td>1218.99 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>15.24 (+7.02%)</td><td>14.00 (+0.87%)</td><td>14.07 (+0.68%)</td><td>12.56 (-7.10%)</td><td>0.95 <b>(+226.63%)</b></td><td>4434.30 (+7.64%)</td><td>3993.04 (-0.52%)</td><td>3959.20 (-0.68%)</td><td>3656.40 (-6.56%)</td><td>279.40 <b>(+231.14%)</b></td><td>14683.09 (+7.02%)</td><td>13496.38 (+0.87%)</td><td>13559.93 (+0.68%)</td><td>12107.34 (-7.10%)</td><td>916.25 <b>(+226.63%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.24 (n/a)</td><td>13.88 (n/a)</td><td>13.97 (n/a)</td><td>13.52 (n/a)</td><td>0.29 (n/a)</td><td>4119.40 (n/a)</td><td>4014.00 (n/a)</td><td>3986.30 (n/a)</td><td>3913.00 (n/a)</td><td>84.37 (n/a)</td><td>13720.26 (n/a)</td><td>13379.72 (n/a)</td><td>13467.90 (n/a)</td><td>13032.89 (n/a)</td><td>280.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>16.27 (+4.51%)</td><td>14.38 (+8.50%)</td><td>14.89 (+10.73%)</td><td>10.66 (-5.67%)</td><td>2.16 (+12.18%)</td><td>1675.00 (+6.01%)</td><td>1269.24 (-7.38%)</td><td>1199.40 (-9.69%)</td><td>1097.80 (-4.31%)</td><td>231.12 (+14.98%)</td><td>12226.18 (+4.51%)</td><td>10810.73 (+8.50%)</td><td>11190.28 (+10.73%)</td><td>8012.91 (-5.67%)</td><td>1627.05 (+12.18%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>15.57 (n/a)</td><td>13.26 (n/a)</td><td>13.45 (n/a)</td><td>11.30 (n/a)</td><td>1.93 (n/a)</td><td>1580.00 (n/a)</td><td>1370.42 (n/a)</td><td>1328.10 (n/a)</td><td>1147.30 (n/a)</td><td>201.00 (n/a)</td><td>11698.42 (n/a)</td><td>9963.57 (n/a)</td><td>10106.01 (n/a)</td><td>8494.75 (n/a)</td><td>1450.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>11.17 (-0.83%)</td><td>10.78 (-0.58%)</td><td>10.67 (-0.53%)</td><td>10.51 (+0.03%)</td><td>0.26 <b>(-22.50%)</b></td><td>7796.80 (-0.03%)</td><td>7601.98 (+0.56%)</td><td>7674.80 (+0.53%)</td><td>7337.10 (+0.83%)</td><td>177.87 <b>(-21.92%)</b></td><td>14634.37 (-0.83%)</td><td>14130.77 (-0.58%)</td><td>13990.51 (-0.53%)</td><td>13771.66 (+0.03%)</td><td>334.52 <b>(-22.50%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>11.26 (n/a)</td><td>10.84 (n/a)</td><td>10.73 (n/a)</td><td>10.50 (n/a)</td><td>0.33 (n/a)</td><td>7798.80 (n/a)</td><td>7559.92 (n/a)</td><td>7634.40 (n/a)</td><td>7276.50 (n/a)</td><td>227.80 (n/a)</td><td>14756.25 (n/a)</td><td>14213.48 (n/a)</td><td>14064.46 (n/a)</td><td>13768.02 (n/a)</td><td>431.62 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.75 (-3.31%)</td><td>12.85 (+1.47%)</td><td>12.59 (+13.16%)</td><td>10.76 (-1.99%)</td><td>1.54 <b>(-31.01%)</b></td><td>1997.20 (+2.03%)</td><td>1692.02 (-2.60%)</td><td>1707.40 (-11.63%)</td><td>1457.30 (+3.42%)</td><td>207.75 <b>(-27.53%)</b></td><td>11788.48 (-3.31%)</td><td>10273.31 (+1.47%)</td><td>10061.95 (+13.16%)</td><td>8602.19 (-1.99%)</td><td>1227.17 <b>(-31.01%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>15.25 (n/a)</td><td>12.67 (n/a)</td><td>11.13 (n/a)</td><td>10.98 (n/a)</td><td>2.23 (n/a)</td><td>1957.40 (n/a)</td><td>1737.18 (n/a)</td><td>1932.10 (n/a)</td><td>1409.10 (n/a)</td><td>286.68 (n/a)</td><td>12191.97 (n/a)</td><td>10124.35 (n/a)</td><td>8891.63 (n/a)</td><td>8776.76 (n/a)</td><td>1778.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>10.95 (+0.42%)</td><td>10.76 (+2.05%)</td><td>10.91 (+4.56%)</td><td>10.37 (-0.21%)</td><td>0.26 (+19.04%)</td><td>7902.70 (+0.21%)</td><td>7619.72 (-2.00%)</td><td>7508.80 (-4.36%)</td><td>7484.10 (-0.42%)</td><td>186.01 (+18.42%)</td><td>14347.00 (+0.42%)</td><td>14098.26 (+2.05%)</td><td>14299.81 (+4.56%)</td><td>13587.04 (-0.21%)</td><td>338.68 (+19.04%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>10.90 (n/a)</td><td>10.54 (n/a)</td><td>10.43 (n/a)</td><td>10.39 (n/a)</td><td>0.22 (n/a)</td><td>7886.10 (n/a)</td><td>7775.24 (n/a)</td><td>7850.80 (n/a)</td><td>7515.70 (n/a)</td><td>157.08 (n/a)</td><td>14286.69 (n/a)</td><td>13814.38 (n/a)</td><td>13676.78 (n/a)</td><td>13615.70 (n/a)</td><td>284.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>4.56 <b>(+26.95%)</b></td><td>3.51 (+12.39%)</td><td>3.10 (+1.45%)</td><td>2.94 (+7.10%)</td><td>0.69 <b>(+121.78%)</b></td><td>468.80 (-6.63%)</td><td>403.36 (-9.19%)</td><td>444.50 (-1.42%)</td><td>302.00 <b>(-21.21%)</b></td><td>71.53 <b>(+64.85%)</b></td><td>888.99 <b>(+26.95%)</b></td><td>684.59 (+12.39%)</td><td>603.92 (+1.45%)</td><td>572.59 (+7.10%)</td><td>135.07 <b>(+121.78%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.59 (n/a)</td><td>3.12 (n/a)</td><td>3.05 (n/a)</td><td>2.74 (n/a)</td><td>0.31 (n/a)</td><td>502.10 (n/a)</td><td>444.16 (n/a)</td><td>450.90 (n/a)</td><td>383.30 (n/a)</td><td>43.39 (n/a)</td><td>700.27 (n/a)</td><td>609.11 (n/a)</td><td>595.32 (n/a)</td><td>534.65 (n/a)</td><td>60.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.65 <b>(+45.72%)</b></td><td>4.31 (+15.21%)</td><td>3.74 (-1.37%)</td><td>3.49 (-0.59%)</td><td>0.94 <b>(+496.12%)</b></td><td>393.80 (+0.61%)</td><td>330.82 (-10.21%)</td><td>367.50 (+1.38%)</td><td>243.40 <b>(-31.38%)</b></td><td>65.80 <b>(+314.58%)</b></td><td>1102.89 <b>(+45.72%)</b></td><td>840.58 (+15.21%)</td><td>730.36 (-1.37%)</td><td>681.69 (-0.59%)</td><td>183.85 <b>(+496.12%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.88 (n/a)</td><td>3.74 (n/a)</td><td>3.80 (n/a)</td><td>3.52 (n/a)</td><td>0.16 (n/a)</td><td>391.40 (n/a)</td><td>368.44 (n/a)</td><td>362.50 (n/a)</td><td>354.70 (n/a)</td><td>15.87 (n/a)</td><td>756.85 (n/a)</td><td>729.63 (n/a)</td><td>740.53 (n/a)</td><td>685.76 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.06 <b>(+28.54%)</b></td><td>4.99 <b>(+21.53%)</b></td><td>4.11 (+14.01%)</td><td>3.69 (+6.78%)</td><td>1.81 <b>(+49.31%)</b></td><td>372.50 (-6.36%)</td><td>299.42 (-15.18%)</td><td>334.90 (-12.28%)</td><td>170.80 <b>(-22.19%)</b></td><td>82.85 (+9.53%)</td><td>1571.77 <b>(+28.54%)</b></td><td>973.42 <b>(+21.53%)</b></td><td>801.59 (+14.01%)</td><td>720.60 (+6.78%)</td><td>353.66 <b>(+49.31%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.27 (n/a)</td><td>4.11 (n/a)</td><td>3.60 (n/a)</td><td>3.46 (n/a)</td><td>1.21 (n/a)</td><td>397.80 (n/a)</td><td>353.00 (n/a)</td><td>381.80 (n/a)</td><td>219.50 (n/a)</td><td>75.64 (n/a)</td><td>1222.79 (n/a)</td><td>800.98 (n/a)</td><td>703.12 (n/a)</td><td>674.87 (n/a)</td><td>236.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.64 (+12.28%)</td><td>4.74 (+7.83%)</td><td>3.90 (+4.05%)</td><td>3.58 (-1.30%)</td><td>1.44 <b>(+39.99%)</b></td><td>384.50 (+1.32%)</td><td>311.22 (-4.56%)</td><td>352.60 (-3.90%)</td><td>207.40 (-10.95%)</td><td>84.91 <b>(+24.94%)</b></td><td>1294.39 (+12.28%)</td><td>923.73 (+7.83%)</td><td>761.30 (+4.05%)</td><td>698.14 (-1.30%)</td><td>281.25 <b>(+39.99%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.91 (n/a)</td><td>4.39 (n/a)</td><td>3.75 (n/a)</td><td>3.63 (n/a)</td><td>1.03 (n/a)</td><td>379.50 (n/a)</td><td>326.08 (n/a)</td><td>366.90 (n/a)</td><td>232.90 (n/a)</td><td>67.96 (n/a)</td><td>1152.81 (n/a)</td><td>856.63 (n/a)</td><td>731.67 (n/a)</td><td>707.35 (n/a)</td><td>200.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.69 <b>(-29.85%)</b></td><td>3.28 (-13.34%)</td><td>3.29 (-2.48%)</td><td>2.96 (-5.72%)</td><td>0.27 <b>(-69.55%)</b></td><td>465.60 (+6.06%)</td><td>421.36 (+11.90%)</td><td>418.40 (+2.52%)</td><td>373.10 <b>(+42.57%)</b></td><td>33.44 <b>(-53.75%)</b></td><td>719.43 <b>(-29.85%)</b></td><td>640.31 (-13.34%)</td><td>641.54 (-2.48%)</td><td>576.49 (-5.72%)</td><td>51.99 <b>(-69.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.26 (n/a)</td><td>3.79 (n/a)</td><td>3.37 (n/a)</td><td>3.13 (n/a)</td><td>0.88 (n/a)</td><td>439.00 (n/a)</td><td>376.56 (n/a)</td><td>408.10 (n/a)</td><td>261.70 (n/a)</td><td>72.30 (n/a)</td><td>1025.58 (n/a)</td><td>738.86 (n/a)</td><td>657.82 (n/a)</td><td>611.46 (n/a)</td><td>170.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.15 <b>(+54.00%)</b></td><td>3.59 (+14.26%)</td><td>3.22 (+5.54%)</td><td>3.08 (+2.41%)</td><td>0.87 <b>(+462.77%)</b></td><td>446.20 (-2.36%)</td><td>397.46 (-9.38%)</td><td>427.40 (-5.23%)</td><td>267.40 <b>(-35.08%)</b></td><td>73.83 <b>(+247.19%)</b></td><td>1003.69 <b>(+54.00%)</b></td><td>700.65 (+14.26%)</td><td>628.13 (+5.54%)</td><td>601.59 (+2.41%)</td><td>170.45 <b>(+462.77%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.34 (n/a)</td><td>3.14 (n/a)</td><td>3.05 (n/a)</td><td>3.01 (n/a)</td><td>0.16 (n/a)</td><td>457.00 (n/a)</td><td>438.60 (n/a)</td><td>451.00 (n/a)</td><td>411.90 (n/a)</td><td>21.26 (n/a)</td><td>651.73 (n/a)</td><td>613.20 (n/a)</td><td>595.16 (n/a)</td><td>587.44 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.50 (+12.73%)</td><td>3.16 (+3.77%)</td><td>3.11 (+1.60%)</td><td>2.98 (+0.42%)</td><td>0.20 <b>(+231.45%)</b></td><td>461.80 (-0.41%)</td><td>437.50 (-3.37%)</td><td>443.20 (-1.58%)</td><td>393.00 (-11.29%)</td><td>26.09 <b>(+188.68%)</b></td><td>683.05 (+12.73%)</td><td>615.46 (+3.77%)</td><td>605.70 (+1.60%)</td><td>581.33 (+0.42%)</td><td>39.17 <b>(+231.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.11 (n/a)</td><td>3.04 (n/a)</td><td>3.06 (n/a)</td><td>2.97 (n/a)</td><td>0.06 (n/a)</td><td>463.70 (n/a)</td><td>452.74 (n/a)</td><td>450.30 (n/a)</td><td>443.00 (n/a)</td><td>9.04 (n/a)</td><td>605.93 (n/a)</td><td>593.10 (n/a)</td><td>596.14 (n/a)</td><td>578.88 (n/a)</td><td>11.82 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.54 (-9.67%)</td><td>1.20 (-9.01%)</td><td>1.15 (-8.33%)</td><td>1.03 (+3.74%)</td><td>0.20 <b>(-30.45%)</b></td><td>390.60 (-3.60%)</td><td>341.76 (+7.93%)</td><td>348.40 (+9.08%)</td><td>261.10 (+10.68%)</td><td>48.34 <b>(-27.90%)</b></td><td>128.50 (-9.67%)</td><td>100.03 (-9.01%)</td><td>96.31 (-8.33%)</td><td>85.91 (+3.74%)</td><td>16.48 <b>(-30.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.70 (n/a)</td><td>1.32 (n/a)</td><td>1.26 (n/a)</td><td>0.99 (n/a)</td><td>0.28 (n/a)</td><td>405.20 (n/a)</td><td>316.64 (n/a)</td><td>319.40 (n/a)</td><td>235.90 (n/a)</td><td>67.04 (n/a)</td><td>142.25 (n/a)</td><td>109.94 (n/a)</td><td>105.06 (n/a)</td><td>82.81 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.99 (+9.97%)</td><td>5.14 (+1.36%)</td><td>4.71 (-1.72%)</td><td>4.40 (-0.52%)</td><td>1.06 <b>(+40.42%)</b></td><td>439.70 (+0.53%)</td><td>386.46 (-0.13%)</td><td>410.20 (+1.76%)</td><td>276.60 (-9.07%)</td><td>64.50 <b>(+28.07%)</b></td><td>1455.63 (+9.97%)</td><td>1071.21 (+1.36%)</td><td>981.72 (-1.72%)</td><td>915.81 (-0.52%)</td><td>220.00 <b>(+40.42%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.36 (n/a)</td><td>5.07 (n/a)</td><td>4.80 (n/a)</td><td>4.42 (n/a)</td><td>0.75 (n/a)</td><td>437.40 (n/a)</td><td>386.96 (n/a)</td><td>403.10 (n/a)</td><td>304.20 (n/a)</td><td>50.37 (n/a)</td><td>1323.69 (n/a)</td><td>1056.83 (n/a)</td><td>998.95 (n/a)</td><td>920.62 (n/a)</td><td>156.67 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>16.13 (-17.31%)</td><td>13.01 (+1.33%)</td><td>11.91 (+6.07%)</td><td>10.91 (+14.03%)</td><td>2.33 <b>(-40.24%)</b></td><td>504.50 (-12.31%)</td><td>433.44 (-4.68%)</td><td>462.10 (-5.71%)</td><td>341.30 <b>(+20.94%)</b></td><td>72.96 <b>(-33.39%)</b></td><td>6291.70 (-17.31%)</td><td>5076.49 (+1.33%)</td><td>4647.64 (+6.07%)</td><td>4256.57 (+14.03%)</td><td>908.89 <b>(-40.24%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>19.50 (n/a)</td><td>12.84 (n/a)</td><td>11.23 (n/a)</td><td>9.57 (n/a)</td><td>3.90 (n/a)</td><td>575.30 (n/a)</td><td>454.72 (n/a)</td><td>490.10 (n/a)</td><td>282.20 (n/a)</td><td>109.53 (n/a)</td><td>7608.80 (n/a)</td><td>5010.09 (n/a)</td><td>4381.60 (n/a)</td><td>3732.77 (n/a)</td><td>1520.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.23 (-0.54%)</td><td>7.54 (+6.21%)</td><td>7.94 (+2.59%)</td><td>5.82 <b>(+46.33%)</b></td><td>1.00 <b>(-43.10%)</b></td><td>946.70 <b>(-31.66%)</b></td><td>742.66 (-11.22%)</td><td>693.10 (-2.53%)</td><td>668.80 (+0.54%)</td><td>116.76 <b>(-62.03%)</b></td><td>3210.89 (-0.54%)</td><td>2940.73 (+6.21%)</td><td>3098.34 (+2.59%)</td><td>2268.46 <b>(+46.33%)</b></td><td>391.35 <b>(-43.10%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>8.28 (n/a)</td><td>7.10 (n/a)</td><td>7.74 (n/a)</td><td>3.97 (n/a)</td><td>1.76 (n/a)</td><td>1385.30 (n/a)</td><td>836.56 (n/a)</td><td>711.10 (n/a)</td><td>665.20 (n/a)</td><td>307.48 (n/a)</td><td>3228.25 (n/a)</td><td>2768.85 (n/a)</td><td>3020.14 (n/a)</td><td>1550.23 (n/a)</td><td>687.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.73 (-6.72%)</td><td>9.13 (+9.36%)</td><td>9.22 (+5.13%)</td><td>8.14 <b>(+68.92%)</b></td><td>0.62 <b>(-70.41%)</b></td><td>712.70 <b>(-40.80%)</b></td><td>637.76 (-14.55%)</td><td>628.80 (-4.89%)</td><td>596.00 (+7.19%)</td><td>45.84 <b>(-82.36%)</b></td><td>4053.46 (-6.72%)</td><td>3802.91 (+9.36%)</td><td>3841.82 (+5.13%)</td><td>3389.73 <b>(+68.92%)</b></td><td>259.01 <b>(-70.41%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>10.43 (n/a)</td><td>8.35 (n/a)</td><td>8.77 (n/a)</td><td>4.82 (n/a)</td><td>2.10 (n/a)</td><td>1203.90 (n/a)</td><td>746.36 (n/a)</td><td>661.10 (n/a)</td><td>556.00 (n/a)</td><td>259.93 (n/a)</td><td>4345.26 (n/a)</td><td>3477.27 (n/a)</td><td>3654.35 (n/a)</td><td>2006.74 (n/a)</td><td>875.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.50 (n/a)</td><td>169.10 (n/a)</td><td>168.70 (n/a)</td><td>164.40 (n/a)</td><td>4.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.50 (n/a)</td><td>152.58 (n/a)</td><td>157.30 (n/a)</td><td>120.30 (n/a)</td><td>22.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.00 (n/a)</td><td>176.22 (n/a)</td><td>160.40 (n/a)</td><td>141.00 (n/a)</td><td>40.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.10 (n/a)</td><td>192.70 (n/a)</td><td>189.00 (n/a)</td><td>150.20 (n/a)</td><td>43.14 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.40 (n/a)</td><td>149.28 (n/a)</td><td>140.90 (n/a)</td><td>130.10 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>167.14 (n/a)</td><td>174.10 (n/a)</td><td>124.20 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.20 (n/a)</td><td>172.08 (n/a)</td><td>177.70 (n/a)</td><td>131.80 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.30 (n/a)</td><td>209.92 (n/a)</td><td>206.70 (n/a)</td><td>180.10 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>167.06 (n/a)</td><td>172.80 (n/a)</td><td>127.50 (n/a)</td><td>29.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>169.46 (n/a)</td><td>174.00 (n/a)</td><td>124.20 (n/a)</td><td>44.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>162.52 (n/a)</td><td>152.60 (n/a)</td><td>120.50 (n/a)</td><td>42.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>153.22 (n/a)</td><td>138.60 (n/a)</td><td>123.50 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.80 (n/a)</td><td>174.26 (n/a)</td><td>172.50 (n/a)</td><td>138.80 (n/a)</td><td>34.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.30 (n/a)</td><td>197.02 (n/a)</td><td>197.60 (n/a)</td><td>184.50 (n/a)</td><td>11.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.20 (n/a)</td><td>169.16 (n/a)</td><td>172.80 (n/a)</td><td>155.80 (n/a)</td><td>12.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.90 (n/a)</td><td>222.08 (n/a)</td><td>221.70 (n/a)</td><td>209.90 (n/a)</td><td>10.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.80 (n/a)</td><td>164.60 (n/a)</td><td>154.40 (n/a)</td><td>140.00 (n/a)</td><td>27.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>181.40 (n/a)</td><td>192.10 (n/a)</td><td>141.00 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>283.30 (n/a)</td><td>186.36 (n/a)</td><td>171.70 (n/a)</td><td>131.90 (n/a)</td><td>57.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.30 (n/a)</td><td>160.36 (n/a)</td><td>173.00 (n/a)</td><td>118.20 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.40 (n/a)</td><td>156.44 (n/a)</td><td>154.70 (n/a)</td><td>114.10 (n/a)</td><td>28.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.60 (n/a)</td><td>170.42 (n/a)</td><td>176.40 (n/a)</td><td>144.70 (n/a)</td><td>20.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>181.86 (n/a)</td><td>185.80 (n/a)</td><td>153.70 (n/a)</td><td>26.32 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>189.60 (n/a)</td><td>189.40 (n/a)</td><td>162.10 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>183.30 (n/a)</td><td>165.20 (n/a)</td><td>176.50 (n/a)</td><td>118.40 (n/a)</td><td>26.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>195.90 (n/a)</td><td>166.96 (n/a)</td><td>175.70 (n/a)</td><td>124.70 (n/a)</td><td>26.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>244.90 (n/a)</td><td>193.82 (n/a)</td><td>197.20 (n/a)</td><td>143.40 (n/a)</td><td>36.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>226.70 (n/a)</td><td>177.72 (n/a)</td><td>177.70 (n/a)</td><td>132.30 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>180.20 (n/a)</td><td>177.30 (n/a)</td><td>166.90 (n/a)</td><td>14.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>208.00 (n/a)</td><td>190.90 (n/a)</td><td>198.20 (n/a)</td><td>169.30 (n/a)</td><td>16.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>256.30 (n/a)</td><td>190.16 (n/a)</td><td>166.50 (n/a)</td><td>155.20 (n/a)</td><td>43.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>278.70 (n/a)</td><td>224.66 (n/a)</td><td>212.50 (n/a)</td><td>202.90 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>4.11 (-0.06%)</td><td>4.10 (-0.04%)</td><td>4.11 (-0.18%)</td><td>4.09 (+0.41%)</td><td>0.01 <b>(-47.54%)</b></td><td>19249.90 (-0.41%)</td><td>19166.74 (+0.04%)</td><td>19157.20 (+0.18%)</td><td>19120.60 (+0.06%)</td><td>49.89 <b>(-47.72%)</b></td><td>2807.81 (-0.06%)</td><td>2801.07 (-0.04%)</td><td>2802.46 (-0.18%)</td><td>2788.96 (+0.41%)</td><td>7.27 <b>(-47.54%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>4.12 (n/a)</td><td>4.10 (n/a)</td><td>4.11 (n/a)</td><td>4.07 (n/a)</td><td>0.02 (n/a)</td><td>19329.50 (n/a)</td><td>19159.20 (n/a)</td><td>19122.80 (n/a)</td><td>19109.80 (n/a)</td><td>95.43 (n/a)</td><td>2809.40 (n/a)</td><td>2802.21 (n/a)</td><td>2807.50 (n/a)</td><td>2777.47 (n/a)</td><td>13.86 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>4.20 (-12.29%)</td><td>4.02 (-3.72%)</td><td>4.07 (-2.50%)</td><td>3.67 (-0.88%)</td><td>0.21 <b>(-49.55%)</b></td><td>2565.50 (+0.89%)</td><td>2344.54 (+3.33%)</td><td>2308.40 (+2.56%)</td><td>2238.20 (+14.02%)</td><td>127.05 <b>(-40.90%)</b></td><td>1652.84 (-12.29%)</td><td>1581.38 (-3.72%)</td><td>1602.60 (-2.50%)</td><td>1441.95 (-0.88%)</td><td>80.80 <b>(-49.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>4.79 (n/a)</td><td>4.18 (n/a)</td><td>4.18 (n/a)</td><td>3.70 (n/a)</td><td>0.41 (n/a)</td><td>2542.90 (n/a)</td><td>2268.90 (n/a)</td><td>2250.80 (n/a)</td><td>1963.00 (n/a)</td><td>214.97 (n/a)</td><td>1884.53 (n/a)</td><td>1642.56 (n/a)</td><td>1643.62 (n/a)</td><td>1454.77 (n/a)</td><td>160.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.20 (-16.59%)</td><td>1.00 (-9.67%)</td><td>1.03 (-0.21%)</td><td>0.73 (-17.70%)</td><td>0.17 <b>(-23.02%)</b></td><td>303.40 <b>(+21.51%)</b></td><td>226.68 (+10.40%)</td><td>215.30 (+0.23%)</td><td>183.60 (+19.84%)</td><td>45.06 (+18.31%)</td><td>51.39 (-16.59%)</td><td>42.78 (-9.67%)</td><td>43.84 (-0.21%)</td><td>31.11 (-17.70%)</td><td>7.31 <b>(-23.02%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.44 (n/a)</td><td>1.11 (n/a)</td><td>1.03 (n/a)</td><td>0.89 (n/a)</td><td>0.22 (n/a)</td><td>249.70 (n/a)</td><td>205.32 (n/a)</td><td>214.80 (n/a)</td><td>153.20 (n/a)</td><td>38.09 (n/a)</td><td>61.61 (n/a)</td><td>47.36 (n/a)</td><td>43.93 (n/a)</td><td>37.80 (n/a)</td><td>9.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.30 (-0.42%)</td><td>0.98 (-5.60%)</td><td>0.95 (-14.80%)</td><td>0.72 (+14.59%)</td><td>0.23 (-8.43%)</td><td>305.40 (-12.72%)</td><td>236.40 (+4.05%)</td><td>233.90 (+17.42%)</td><td>170.30 (+0.41%)</td><td>55.18 <b>(-23.04%)</b></td><td>55.41 (-0.42%)</td><td>41.76 (-5.60%)</td><td>40.35 (-14.80%)</td><td>30.91 (+14.59%)</td><td>9.99 (-8.43%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.30 (n/a)</td><td>1.04 (n/a)</td><td>1.11 (n/a)</td><td>0.63 (n/a)</td><td>0.26 (n/a)</td><td>349.90 (n/a)</td><td>227.20 (n/a)</td><td>199.20 (n/a)</td><td>169.60 (n/a)</td><td>71.70 (n/a)</td><td>55.65 (n/a)</td><td>44.24 (n/a)</td><td>47.37 (n/a)</td><td>26.97 (n/a)</td><td>10.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.53 (+0.04%)</td><td>0.53 (+0.11%)</td><td>0.53 (+0.08%)</td><td>0.53 (+0.23%)</td><td>0.00 <b>(-52.39%)</b></td><td>47840.10 (-0.23%)</td><td>47797.00 (-0.11%)</td><td>47785.40 (-0.08%)</td><td>47760.90 (-0.04%)</td><td>33.71 <b>(-52.53%)</b></td><td>359.71 (+0.04%)</td><td>359.43 (+0.11%)</td><td>359.52 (+0.08%)</td><td>359.11 (+0.23%)</td><td>0.25 <b>(-52.39%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>47948.30 (n/a)</td><td>47849.84 (n/a)</td><td>47824.30 (n/a)</td><td>47779.80 (n/a)</td><td>71.02 (n/a)</td><td>359.56 (n/a)</td><td>359.04 (n/a)</td><td>359.23 (n/a)</td><td>358.30 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (+1.13%)</td><td>0.21 (+0.08%)</td><td>0.21 (+0.44%)</td><td>0.21 (-0.80%)</td><td>0.00 <b>(+97.66%)</b></td><td>120209.80 (+0.81%)</td><td>118151.12 (-0.07%)</td><td>117946.80 (-0.44%)</td><td>115795.50 (-1.11%)</td><td>1693.13 <b>(+97.14%)</b></td><td>148.36 (+1.13%)</td><td>145.43 (+0.08%)</td><td>145.66 (+0.44%)</td><td>142.92 (-0.80%)</td><td>2.09 <b>(+97.65%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119249.70 (n/a)</td><td>118235.84 (n/a)</td><td>118464.20 (n/a)</td><td>117098.80 (n/a)</td><td>858.86 (n/a)</td><td>146.71 (n/a)</td><td>145.31 (n/a)</td><td>145.02 (n/a)</td><td>144.07 (n/a)</td><td>1.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.91 (-1.12%)</td><td>0.90 (-0.29%)</td><td>0.90 (+0.08%)</td><td>0.90 (+0.48%)</td><td>0.00 <b>(-54.29%)</b></td><td>28101.00 (-0.48%)</td><td>27925.30 (+0.28%)</td><td>27874.50 (-0.08%)</td><td>27776.00 (+1.13%)</td><td>132.11 <b>(-53.98%)</b></td><td>618.52 (-1.12%)</td><td>615.22 (-0.29%)</td><td>616.33 (+0.08%)</td><td>611.36 (+0.48%)</td><td>2.91 <b>(-54.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.92 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28237.20 (n/a)</td><td>27846.82 (n/a)</td><td>27896.80 (n/a)</td><td>27464.30 (n/a)</td><td>287.10 (n/a)</td><td>625.53 (n/a)</td><td>616.99 (n/a)</td><td>615.84 (n/a)</td><td>608.41 (n/a)</td><td>6.36 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.74 (+2.90%)</td><td>3.62 (+1.02%)</td><td>3.64 (+0.65%)</td><td>3.48 (+0.26%)</td><td>0.09 <b>(+46.04%)</b></td><td>7222.90 (-0.26%)</td><td>6964.10 (-0.99%)</td><td>6922.50 (-0.65%)</td><td>6735.20 (-2.82%)</td><td>182.85 <b>(+41.72%)</b></td><td>2550.76 (+2.90%)</td><td>2468.27 (+1.02%)</td><td>2481.73 (+0.65%)</td><td>2378.53 (+0.26%)</td><td>64.48 <b>(+46.04%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.63 (n/a)</td><td>3.58 (n/a)</td><td>3.61 (n/a)</td><td>3.48 (n/a)</td><td>0.06 (n/a)</td><td>7241.90 (n/a)</td><td>7033.40 (n/a)</td><td>6967.80 (n/a)</td><td>6930.40 (n/a)</td><td>129.02 (n/a)</td><td>2478.93 (n/a)</td><td>2443.27 (n/a)</td><td>2465.62 (n/a)</td><td>2372.29 (n/a)</td><td>44.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.26 (+12.12%)</td><td>2.92 (+2.63%)</td><td>2.87 (-0.14%)</td><td>2.79 (+3.21%)</td><td>0.19 <b>(+130.38%)</b></td><td>9034.00 (-3.11%)</td><td>8639.08 (-2.32%)</td><td>8762.30 (+0.14%)</td><td>7729.30 (-10.81%)</td><td>532.07 <b>(+96.79%)</b></td><td>2222.68 (+12.12%)</td><td>1995.11 (+2.63%)</td><td>1960.66 (-0.14%)</td><td>1901.69 (+3.21%)</td><td>131.75 <b>(+130.38%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>2.90 (n/a)</td><td>2.85 (n/a)</td><td>2.88 (n/a)</td><td>2.70 (n/a)</td><td>0.08 (n/a)</td><td>9323.70 (n/a)</td><td>8844.08 (n/a)</td><td>8750.10 (n/a)</td><td>8666.00 (n/a)</td><td>270.37 (n/a)</td><td>1982.44 (n/a)</td><td>1943.93 (n/a)</td><td>1963.39 (n/a)</td><td>1842.61 (n/a)</td><td>57.19 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.32 (-0.41%)</td><td>3.22 (-0.72%)</td><td>3.20 (-1.06%)</td><td>3.17 (+0.29%)</td><td>0.06 (-13.10%)</td><td>7930.00 (-0.29%)</td><td>7821.00 (+0.72%)</td><td>7863.70 (+1.07%)</td><td>7589.70 (+0.42%)</td><td>133.75 (-13.27%)</td><td>2263.59 (-0.41%)</td><td>2197.16 (-0.72%)</td><td>2184.71 (-1.06%)</td><td>2166.45 (+0.29%)</td><td>38.32 (-13.10%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.33 (n/a)</td><td>3.24 (n/a)</td><td>3.23 (n/a)</td><td>3.16 (n/a)</td><td>0.06 (n/a)</td><td>7952.90 (n/a)</td><td>7765.06 (n/a)</td><td>7780.30 (n/a)</td><td>7558.20 (n/a)</td><td>154.20 (n/a)</td><td>2273.00 (n/a)</td><td>2213.15 (n/a)</td><td>2208.11 (n/a)</td><td>2160.19 (n/a)</td><td>44.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.80 (-0.02%)</td><td>0.80 (-0.01%)</td><td>0.80 (-0.00%)</td><td>0.80 (-0.02%)</td><td>0.00 (-1.22%)</td><td>94880.40 (+0.02%)</td><td>94723.80 (+0.01%)</td><td>94791.30 (+0.00%)</td><td>94353.20 (+0.02%)</td><td>210.49 (-1.18%)</td><td>728.32 (-0.02%)</td><td>725.48 (-0.01%)</td><td>724.96 (-0.00%)</td><td>724.27 (-0.02%)</td><td>1.62 (-1.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94864.50 (n/a)</td><td>94715.22 (n/a)</td><td>94791.10 (n/a)</td><td>94338.70 (n/a)</td><td>213.00 (n/a)</td><td>728.43 (n/a)</td><td>725.54 (n/a)</td><td>724.96 (n/a)</td><td>724.40 (n/a)</td><td>1.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.73 (+0.31%)</td><td>0.73 (+0.09%)</td><td>0.73 (+0.05%)</td><td>0.73 (+0.01%)</td><td>0.00 <b>(+107.88%)</b></td><td>103501.80 (-0.01%)</td><td>103255.26 (-0.09%)</td><td>103271.50 (-0.05%)</td><td>102944.20 (-0.31%)</td><td>201.45 <b>(+107.12%)</b></td><td>667.54 (+0.31%)</td><td>665.53 (+0.09%)</td><td>665.43 (+0.05%)</td><td>663.94 (+0.01%)</td><td>1.30 <b>(+107.87%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103514.50 (n/a)</td><td>103346.48 (n/a)</td><td>103325.40 (n/a)</td><td>103267.40 (n/a)</td><td>97.26 (n/a)</td><td>665.45 (n/a)</td><td>664.94 (n/a)</td><td>665.08 (n/a)</td><td>663.86 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.69 (-0.60%)</td><td>0.68 (-0.62%)</td><td>0.68 (-0.42%)</td><td>0.68 (-0.81%)</td><td>0.00 (+19.00%)</td><td>110903.50 (+0.82%)</td><td>110431.98 (+0.62%)</td><td>110383.90 (+0.42%)</td><td>109961.40 (+0.61%)</td><td>360.33 <b>(+20.70%)</b></td><td>624.94 (-0.60%)</td><td>622.28 (-0.62%)</td><td>622.55 (-0.42%)</td><td>619.63 (-0.81%)</td><td>2.03 (+19.00%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>110003.60 (n/a)</td><td>109750.64 (n/a)</td><td>109922.60 (n/a)</td><td>109298.80 (n/a)</td><td>298.54 (n/a)</td><td>628.73 (n/a)</td><td>626.15 (n/a)</td><td>625.16 (n/a)</td><td>624.70 (n/a)</td><td>1.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>2.80 (-0.12%)</td><td>2.79 (-0.03%)</td><td>2.80 (+0.03%)</td><td>2.79 (-0.20%)</td><td>0.00 <b>(+44.15%)</b></td><td>37618.80 (+0.20%)</td><td>37518.92 (+0.03%)</td><td>37498.50 (-0.04%)</td><td>37486.40 (+0.12%)</td><td>56.08 <b>(+44.68%)</b></td><td>2864.35 (-0.12%)</td><td>2861.87 (-0.03%)</td><td>2863.42 (+0.03%)</td><td>2854.27 (-0.20%)</td><td>4.27 <b>(+44.15%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>0.00 (n/a)</td><td>37542.80 (n/a)</td><td>37506.10 (n/a)</td><td>37511.70 (n/a)</td><td>37441.00 (n/a)</td><td>38.76 (n/a)</td><td>2867.82 (n/a)</td><td>2862.85 (n/a)</td><td>2862.42 (n/a)</td><td>2860.05 (n/a)</td><td>2.96 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>7.48 (-2.18%)</td><td>6.85 (+14.13%)</td><td>6.67 (+3.75%)</td><td>6.46 <b>(+42.01%)</b></td><td>0.41 <b>(-68.57%)</b></td><td>1379.50 <b>(-29.58%)</b></td><td>1304.00 (-15.49%)</td><td>1336.20 (-3.61%)</td><td>1191.50 (+2.24%)</td><td>74.99 <b>(-78.15%)</b></td><td>450.60 (-2.18%)</td><td>412.85 (+14.13%)</td><td>401.78 (+3.75%)</td><td>389.18 <b>(+42.01%)</b></td><td>24.59 <b>(-68.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.65 (n/a)</td><td>6.01 (n/a)</td><td>6.43 (n/a)</td><td>4.55 (n/a)</td><td>1.30 (n/a)</td><td>1959.00 (n/a)</td><td>1543.06 (n/a)</td><td>1386.30 (n/a)</td><td>1165.40 (n/a)</td><td>343.16 (n/a)</td><td>460.66 (n/a)</td><td>361.73 (n/a)</td><td>387.27 (n/a)</td><td>274.05 (n/a)</td><td>78.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.90 (-3.36%)</td><td>6.67 (-2.09%)</td><td>6.72 (-1.18%)</td><td>6.38 (+0.26%)</td><td>0.24 <b>(-27.16%)</b></td><td>1397.30 (-0.26%)</td><td>1338.26 (+2.05%)</td><td>1325.40 (+1.19%)</td><td>1291.30 (+3.48%)</td><td>47.56 <b>(-24.52%)</b></td><td>415.77 (-3.36%)</td><td>401.57 (-2.09%)</td><td>405.05 (-1.18%)</td><td>384.22 (+0.26%)</td><td>14.16 <b>(-27.16%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.14 (n/a)</td><td>6.81 (n/a)</td><td>6.80 (n/a)</td><td>6.36 (n/a)</td><td>0.32 (n/a)</td><td>1401.00 (n/a)</td><td>1311.34 (n/a)</td><td>1309.80 (n/a)</td><td>1247.90 (n/a)</td><td>63.01 (n/a)</td><td>430.22 (n/a)</td><td>410.16 (n/a)</td><td>409.90 (n/a)</td><td>383.20 (n/a)</td><td>19.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.67 (-6.89%)</td><td>6.36 (+3.98%)</td><td>6.28 (-0.06%)</td><td>6.23 <b>(+33.46%)</b></td><td>0.18 <b>(-80.49%)</b></td><td>1429.90 <b>(-25.07%)</b></td><td>1401.48 (-5.74%)</td><td>1419.90 (+0.06%)</td><td>1336.40 (+7.41%)</td><td>38.75 <b>(-84.74%)</b></td><td>401.74 (-6.89%)</td><td>383.32 (+3.98%)</td><td>378.10 (-0.06%)</td><td>375.47 <b>(+33.46%)</b></td><td>10.90 <b>(-80.49%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.16 (n/a)</td><td>6.12 (n/a)</td><td>6.28 (n/a)</td><td>4.67 (n/a)</td><td>0.93 (n/a)</td><td>1908.30 (n/a)</td><td>1486.78 (n/a)</td><td>1419.00 (n/a)</td><td>1244.20 (n/a)</td><td>253.86 (n/a)</td><td>431.48 (n/a)</td><td>368.66 (n/a)</td><td>378.34 (n/a)</td><td>281.34 (n/a)</td><td>55.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.24 (-4.05%)</td><td>7.79 (-3.13%)</td><td>7.99 (-1.69%)</td><td>7.27 (-1.58%)</td><td>0.44 (+0.92%)</td><td>4795.80 (+1.60%)</td><td>4486.76 (+3.25%)</td><td>4364.80 (+1.72%)</td><td>4230.30 (+4.22%)</td><td>257.66 (+6.72%)</td><td>507.65 (-4.05%)</td><td>479.87 (-3.13%)</td><td>492.00 (-1.69%)</td><td>447.79 (-1.58%)</td><td>27.12 (+0.92%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>8.59 (n/a)</td><td>8.04 (n/a)</td><td>8.13 (n/a)</td><td>7.39 (n/a)</td><td>0.44 (n/a)</td><td>4720.20 (n/a)</td><td>4345.32 (n/a)</td><td>4290.90 (n/a)</td><td>4059.00 (n/a)</td><td>241.43 (n/a)</td><td>529.06 (n/a)</td><td>495.40 (n/a)</td><td>500.48 (n/a)</td><td>454.96 (n/a)</td><td>26.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>7.58 (-3.10%)</td><td>7.31 (-2.75%)</td><td>7.32 (-3.91%)</td><td>6.99 (+2.19%)</td><td>0.25 <b>(-35.95%)</b></td><td>4985.40 (-2.15%)</td><td>4772.56 (+2.69%)</td><td>4760.90 (+4.07%)</td><td>4601.70 (+3.20%)</td><td>162.67 <b>(-36.17%)</b></td><td>466.67 (-3.10%)</td><td>450.38 (-2.75%)</td><td>451.07 (-3.91%)</td><td>430.75 (+2.19%)</td><td>15.26 <b>(-35.95%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.82 (n/a)</td><td>7.52 (n/a)</td><td>7.62 (n/a)</td><td>6.84 (n/a)</td><td>0.39 (n/a)</td><td>5094.70 (n/a)</td><td>4647.76 (n/a)</td><td>4574.60 (n/a)</td><td>4459.20 (n/a)</td><td>254.83 (n/a)</td><td>481.58 (n/a)</td><td>463.09 (n/a)</td><td>469.44 (n/a)</td><td>421.52 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>7.54 (+0.22%)</td><td>7.25 (+0.02%)</td><td>7.40 (-0.58%)</td><td>6.74 (-2.56%)</td><td>0.31 (+5.39%)</td><td>5174.40 (+2.63%)</td><td>4814.60 (+0.00%)</td><td>4712.80 (+0.58%)</td><td>4626.80 (-0.22%)</td><td>216.90 (+8.10%)</td><td>464.14 (+0.22%)</td><td>446.73 (+0.02%)</td><td>455.67 (-0.58%)</td><td>415.02 (-2.56%)</td><td>19.34 (+5.39%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.52 (n/a)</td><td>7.25 (n/a)</td><td>7.44 (n/a)</td><td>6.92 (n/a)</td><td>0.30 (n/a)</td><td>5041.80 (n/a)</td><td>4814.44 (n/a)</td><td>4685.70 (n/a)</td><td>4636.90 (n/a)</td><td>200.65 (n/a)</td><td>463.13 (n/a)</td><td>446.66 (n/a)</td><td>458.31 (n/a)</td><td>425.94 (n/a)</td><td>18.35 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.80 (-0.01%)</td><td>0.80 (-0.09%)</td><td>0.80 (-0.04%)</td><td>0.80 (-0.22%)</td><td>0.00 <b>(+286.51%)</b></td><td>94298.90 (+0.22%)</td><td>94138.08 (+0.09%)</td><td>94091.10 (+0.04%)</td><td>94030.50 (+0.01%)</td><td>112.67 <b>(+287.36%)</b></td><td>730.82 (-0.01%)</td><td>729.99 (-0.09%)</td><td>730.35 (-0.04%)</td><td>728.74 (-0.22%)</td><td>0.87 <b>(+286.43%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94095.60 (n/a)</td><td>94056.70 (n/a)</td><td>94056.40 (n/a)</td><td>94018.10 (n/a)</td><td>29.09 (n/a)</td><td>730.92 (n/a)</td><td>730.62 (n/a)</td><td>730.62 (n/a)</td><td>730.32 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.74 (+0.02%)</td><td>0.74 (+0.02%)</td><td>0.74 (+0.08%)</td><td>0.73 (-0.10%)</td><td>0.00 <b>(+82.78%)</b></td><td>102880.30 (+0.10%)</td><td>102659.38 (-0.02%)</td><td>102598.10 (-0.08%)</td><td>102560.10 (-0.02%)</td><td>130.34 <b>(+82.99%)</b></td><td>670.04 (+0.02%)</td><td>669.39 (+0.02%)</td><td>669.79 (+0.08%)</td><td>667.96 (-0.10%)</td><td>0.85 <b>(+82.77%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102775.70 (n/a)</td><td>102679.78 (n/a)</td><td>102676.50 (n/a)</td><td>102576.70 (n/a)</td><td>71.23 (n/a)</td><td>669.93 (n/a)</td><td>669.26 (n/a)</td><td>669.28 (n/a)</td><td>668.64 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.71 (+0.02%)</td><td>0.71 (+0.02%)</td><td>0.71 (+0.20%)</td><td>0.71 (-0.30%)</td><td>0.00 <b>(+96.51%)</b></td><td>106496.60 (+0.30%)</td><td>106023.04 (-0.02%)</td><td>105859.90 (-0.20%)</td><td>105771.50 (-0.02%)</td><td>296.51 <b>(+97.12%)</b></td><td>649.70 (+0.02%)</td><td>648.16 (+0.02%)</td><td>649.15 (+0.20%)</td><td>645.27 (-0.30%)</td><td>1.81 <b>(+96.51%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106182.40 (n/a)</td><td>106046.26 (n/a)</td><td>106070.70 (n/a)</td><td>105790.20 (n/a)</td><td>150.42 (n/a)</td><td>649.58 (n/a)</td><td>648.02 (n/a)</td><td>647.86 (n/a)</td><td>647.18 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>4.30 (-0.91%)</td><td>3.59 (-3.38%)</td><td>3.64 (-5.51%)</td><td>2.86 (-5.88%)</td><td>0.53 (-5.94%)</td><td>2816.30 (+6.24%)</td><td>2284.74 (+3.40%)</td><td>2211.70 (+5.83%)</td><td>1874.60 (+0.93%)</td><td>348.88 (+1.15%)</td><td>1127.70 (-0.91%)</td><td>941.96 (-3.38%)</td><td>955.80 (-5.51%)</td><td>750.60 (-5.88%)</td><td>138.23 (-5.94%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>4.34 (n/a)</td><td>3.72 (n/a)</td><td>3.86 (n/a)</td><td>3.04 (n/a)</td><td>0.56 (n/a)</td><td>2650.80 (n/a)</td><td>2209.68 (n/a)</td><td>2089.90 (n/a)</td><td>1857.40 (n/a)</td><td>344.90 (n/a)</td><td>1138.10 (n/a)</td><td>974.96 (n/a)</td><td>1011.48 (n/a)</td><td>797.47 (n/a)</td><td>146.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.33 (-6.46%)</td><td>0.30 (-7.42%)</td><td>0.30 (-4.17%)</td><td>0.28 (-9.47%)</td><td>0.02 (+3.05%)</td><td>4444.50 (+10.46%)</td><td>4107.98 (+8.11%)</td><td>4088.30 (+4.35%)</td><td>3771.90 (+6.90%)</td><td>297.78 <b>(+22.81%)</b></td><td>17.79 (-6.46%)</td><td>16.41 (-7.42%)</td><td>16.41 (-4.17%)</td><td>15.10 (-9.47%)</td><td>1.19 (+3.05%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.02 (n/a)</td><td>4023.60 (n/a)</td><td>3799.98 (n/a)</td><td>3917.80 (n/a)</td><td>3528.30 (n/a)</td><td>242.48 (n/a)</td><td>19.02 (n/a)</td><td>17.72 (n/a)</td><td>17.13 (n/a)</td><td>16.68 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.04 (-18.86%)</td><td>4.44 (-8.51%)</td><td>4.87 (+1.50%)</td><td>3.63 (+4.43%)</td><td>0.71 <b>(-29.50%)</b></td><td>1830.00 (-4.24%)</td><td>1531.50 (+7.72%)</td><td>1366.50 (-1.48%)</td><td>1318.70 <b>(+23.25%)</b></td><td>258.16 (-17.38%)</td><td>1558.55 (-18.86%)</td><td>1371.36 (-8.51%)</td><td>1503.97 (+1.50%)</td><td>1123.06 (+4.43%)</td><td>218.18 <b>(-29.50%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.22 (n/a)</td><td>4.85 (n/a)</td><td>4.80 (n/a)</td><td>3.48 (n/a)</td><td>1.00 (n/a)</td><td>1911.10 (n/a)</td><td>1421.76 (n/a)</td><td>1387.00 (n/a)</td><td>1069.90 (n/a)</td><td>312.45 (n/a)</td><td>1920.92 (n/a)</td><td>1498.84 (n/a)</td><td>1481.81 (n/a)</td><td>1075.41 (n/a)</td><td>309.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>13.39 (n/a)</td><td>12.47 (n/a)</td><td>13.17 (n/a)</td><td>10.39 (n/a)</td><td>1.25 (n/a)</td><td>13.38 (n/a)</td><td>12.47 (n/a)</td><td>13.16 (n/a)</td><td>10.38 (n/a)</td><td>1.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>24.93 (-0.99%)</td><td>23.56 (-4.93%)</td><td>23.77 (-4.77%)</td><td>20.81 (-14.05%)</td><td>1.63 <b>(+291.99%)</b></td><td>24.91 (-0.99%)</td><td>23.55 (-4.93%)</td><td>23.76 (-4.77%)</td><td>20.79 (-14.05%)</td><td>1.63 <b>(+291.99%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>25.18 (n/a)</td><td>24.78 (n/a)</td><td>24.96 (n/a)</td><td>24.21 (n/a)</td><td>0.42 (n/a)</td><td>25.16 (n/a)</td><td>24.77 (n/a)</td><td>24.95 (n/a)</td><td>24.19 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>41.20 (-5.71%)</td><td>39.77 (-3.95%)</td><td>39.63 (-3.09%)</td><td>38.25 (-5.17%)</td><td>1.31 (-1.46%)</td><td>41.17 (-5.71%)</td><td>39.75 (-3.95%)</td><td>39.61 (-3.09%)</td><td>38.23 (-5.17%)</td><td>1.31 (-1.46%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>43.69 (n/a)</td><td>41.41 (n/a)</td><td>40.90 (n/a)</td><td>40.34 (n/a)</td><td>1.33 (n/a)</td><td>43.67 (n/a)</td><td>41.39 (n/a)</td><td>40.87 (n/a)</td><td>40.32 (n/a)</td><td>1.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>43.25 (-5.45%)</td><td>42.17 (-4.74%)</td><td>42.22 (-4.43%)</td><td>41.32 (-3.54%)</td><td>0.76 <b>(-36.40%)</b></td><td>43.22 (-5.45%)</td><td>42.15 (-4.74%)</td><td>42.19 (-4.43%)</td><td>41.30 (-3.54%)</td><td>0.76 <b>(-36.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>45.74 (n/a)</td><td>44.28 (n/a)</td><td>44.18 (n/a)</td><td>42.84 (n/a)</td><td>1.20 (n/a)</td><td>45.71 (n/a)</td><td>44.25 (n/a)</td><td>44.15 (n/a)</td><td>42.82 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>13.22 (n/a)</td><td>12.40 (n/a)</td><td>12.95 (n/a)</td><td>10.97 (n/a)</td><td>1.01 (n/a)</td><td>13.21 (n/a)</td><td>12.39 (n/a)</td><td>12.94 (n/a)</td><td>10.96 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>25.27 (+1.26%)</td><td>24.21 (-1.54%)</td><td>24.07 (-2.48%)</td><td>23.37 (-3.18%)</td><td>0.69 <b>(+124.07%)</b></td><td>25.26 (+1.26%)</td><td>24.20 (-1.54%)</td><td>24.05 (-2.48%)</td><td>23.36 (-3.18%)</td><td>0.69 <b>(+124.07%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>24.96 (n/a)</td><td>24.59 (n/a)</td><td>24.68 (n/a)</td><td>24.14 (n/a)</td><td>0.31 (n/a)</td><td>24.94 (n/a)</td><td>24.58 (n/a)</td><td>24.66 (n/a)</td><td>24.12 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>42.09 (-0.77%)</td><td>39.35 (-4.40%)</td><td>39.25 (-4.01%)</td><td>37.32 (-5.62%)</td><td>1.74 <b>(+42.58%)</b></td><td>42.06 (-0.77%)</td><td>39.32 (-4.40%)</td><td>39.23 (-4.01%)</td><td>37.30 (-5.62%)</td><td>1.74 <b>(+42.58%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>42.42 (n/a)</td><td>41.16 (n/a)</td><td>40.89 (n/a)</td><td>39.54 (n/a)</td><td>1.22 (n/a)</td><td>42.39 (n/a)</td><td>41.13 (n/a)</td><td>40.87 (n/a)</td><td>39.52 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>44.93 (+0.92%)</td><td>42.89 (-2.44%)</td><td>42.63 (-2.59%)</td><td>41.58 (-4.12%)</td><td>1.23 <b>(+158.40%)</b></td><td>44.90 (+0.92%)</td><td>42.86 (-2.44%)</td><td>42.61 (-2.59%)</td><td>41.56 (-4.12%)</td><td>1.23 <b>(+158.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>44.52 (n/a)</td><td>43.96 (n/a)</td><td>43.77 (n/a)</td><td>43.37 (n/a)</td><td>0.48 (n/a)</td><td>44.49 (n/a)</td><td>43.93 (n/a)</td><td>43.74 (n/a)</td><td>43.34 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.69 (-2.91%)</td><td>9.30 (-0.00%)</td><td>9.26 (-0.50%)</td><td>9.03 (+5.90%)</td><td>0.24 <b>(-55.69%)</b></td><td>9.67 (-2.91%)</td><td>9.28 (-0.00%)</td><td>9.24 (-0.50%)</td><td>9.01 (+5.90%)</td><td>0.24 <b>(-55.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.98 (n/a)</td><td>9.30 (n/a)</td><td>9.31 (n/a)</td><td>8.53 (n/a)</td><td>0.55 (n/a)</td><td>9.96 (n/a)</td><td>9.28 (n/a)</td><td>9.29 (n/a)</td><td>8.51 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.03 (+0.20%)</td><td>0.94 (+5.63%)</td><td>1.01 (+8.98%)</td><td>0.72 (-4.00%)</td><td>0.13 <b>(+20.53%)</b></td><td>1.01 (+0.20%)</td><td>0.93 (+5.63%)</td><td>1.00 (+8.98%)</td><td>0.71 (-4.00%)</td><td>0.13 <b>(+20.53%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.03 (n/a)</td><td>0.89 (n/a)</td><td>0.93 (n/a)</td><td>0.75 (n/a)</td><td>0.11 (n/a)</td><td>1.01 (n/a)</td><td>0.88 (n/a)</td><td>0.92 (n/a)</td><td>0.74 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.25 (-17.24%)</td><td>1.11 (-15.67%)</td><td>1.13 (-12.67%)</td><td>0.89 (-18.96%)</td><td>0.13 (-14.15%)</td><td>1.24 (-17.24%)</td><td>1.10 (-15.67%)</td><td>1.12 (-12.67%)</td><td>0.88 (-18.96%)</td><td>0.13 (-14.15%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.51 (n/a)</td><td>1.32 (n/a)</td><td>1.30 (n/a)</td><td>1.10 (n/a)</td><td>0.16 (n/a)</td><td>1.50 (n/a)</td><td>1.30 (n/a)</td><td>1.28 (n/a)</td><td>1.09 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>18.78 (+5.19%)</td><td>17.63 (+6.26%)</td><td>17.69 (+5.70%)</td><td>15.79 (+12.80%)</td><td>1.22 <b>(-22.26%)</b></td><td>18.56 (+5.19%)</td><td>17.42 (+6.26%)</td><td>17.48 (+5.70%)</td><td>15.60 (+12.80%)</td><td>1.21 <b>(-22.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>17.85 (n/a)</td><td>16.59 (n/a)</td><td>16.73 (n/a)</td><td>13.99 (n/a)</td><td>1.57 (n/a)</td><td>17.64 (n/a)</td><td>16.40 (n/a)</td><td>16.54 (n/a)</td><td>13.83 (n/a)</td><td>1.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.54 (+3.16%)</td><td>13.74 (+1.17%)</td><td>13.67 (+0.53%)</td><td>13.28 (+4.91%)</td><td>0.49 (-15.09%)</td><td>14.28 (+3.16%)</td><td>13.50 (+1.17%)</td><td>13.43 (+0.53%)</td><td>13.05 (+4.91%)</td><td>0.48 (-15.09%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.09 (n/a)</td><td>13.58 (n/a)</td><td>13.60 (n/a)</td><td>12.66 (n/a)</td><td>0.58 (n/a)</td><td>13.84 (n/a)</td><td>13.35 (n/a)</td><td>13.36 (n/a)</td><td>12.44 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.60 (-12.65%)</td><td>7.48 (-10.68%)</td><td>7.70 (-2.79%)</td><td>5.66 <b>(-25.67%)</b></td><td>1.12 <b>(+20.55%)</b></td><td>8.45 (-12.65%)</td><td>7.35 (-10.68%)</td><td>7.57 (-2.79%)</td><td>5.56 <b>(-25.67%)</b></td><td>1.10 <b>(+20.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.85 (n/a)</td><td>8.38 (n/a)</td><td>7.92 (n/a)</td><td>7.61 (n/a)</td><td>0.93 (n/a)</td><td>9.68 (n/a)</td><td>8.23 (n/a)</td><td>7.78 (n/a)</td><td>7.48 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.12 (-0.37%)</td><td>5.76 (+8.56%)</td><td>5.77 (+15.85%)</td><td>5.31 (+17.19%)</td><td>0.33 <b>(-57.11%)</b></td><td>6.02 (-0.37%)</td><td>5.66 (+8.56%)</td><td>5.67 (+15.85%)</td><td>5.23 (+17.19%)</td><td>0.33 <b>(-57.11%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.14 (n/a)</td><td>5.30 (n/a)</td><td>4.98 (n/a)</td><td>4.53 (n/a)</td><td>0.78 (n/a)</td><td>6.04 (n/a)</td><td>5.22 (n/a)</td><td>4.90 (n/a)</td><td>4.46 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>13.47 (n/a)</td><td>12.82 (n/a)</td><td>13.30 (n/a)</td><td>10.64 (n/a)</td><td>1.22 (n/a)</td><td>13.46 (n/a)</td><td>12.81 (n/a)</td><td>13.30 (n/a)</td><td>10.64 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>13.25 (n/a)</td><td>11.94 (n/a)</td><td>12.07 (n/a)</td><td>10.43 (n/a)</td><td>1.01 (n/a)</td><td>13.24 (n/a)</td><td>11.94 (n/a)</td><td>12.06 (n/a)</td><td>10.42 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.40 (n/a)</td><td>161.60 (n/a)</td><td>177.30 (n/a)</td><td>126.90 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>150.00 (n/a)</td><td>164.90 (n/a)</td><td>110.10 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>149.92 (n/a)</td><td>152.10 (n/a)</td><td>116.30 (n/a)</td><td>34.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.60 (n/a)</td><td>164.78 (n/a)</td><td>160.60 (n/a)</td><td>105.80 (n/a)</td><td>51.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>272.60 (n/a)</td><td>167.88 (n/a)</td><td>135.90 (n/a)</td><td>132.30 (n/a)</td><td>59.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.30 (n/a)</td><td>165.12 (n/a)</td><td>169.40 (n/a)</td><td>142.90 (n/a)</td><td>20.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.80 (n/a)</td><td>182.12 (n/a)</td><td>194.00 (n/a)</td><td>112.70 (n/a)</td><td>42.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>254.70 (n/a)</td><td>217.98 (n/a)</td><td>213.90 (n/a)</td><td>189.10 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>184.80 (n/a)</td><td>168.80 (n/a)</td><td>155.90 (n/a)</td><td>33.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>176.62 (n/a)</td><td>171.30 (n/a)</td><td>129.80 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>183.00 (n/a)</td><td>175.80 (n/a)</td><td>177.20 (n/a)</td><td>168.20 (n/a)</td><td>5.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.20 (n/a)</td><td>169.20 (n/a)</td><td>163.10 (n/a)</td><td>131.90 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.70 (n/a)</td><td>171.98 (n/a)</td><td>173.40 (n/a)</td><td>113.70 (n/a)</td><td>39.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.30 (n/a)</td><td>175.48 (n/a)</td><td>148.00 (n/a)</td><td>134.10 (n/a)</td><td>51.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.90 (n/a)</td><td>199.34 (n/a)</td><td>209.50 (n/a)</td><td>156.40 (n/a)</td><td>38.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.60 (n/a)</td><td>220.24 (n/a)</td><td>217.60 (n/a)</td><td>209.90 (n/a)</td><td>8.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>254.90 (n/a)</td><td>185.36 (n/a)</td><td>174.80 (n/a)</td><td>155.00 (n/a)</td><td>40.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>183.86 (n/a)</td><td>165.80 (n/a)</td><td>162.70 (n/a)</td><td>31.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.20 (n/a)</td><td>187.70 (n/a)</td><td>165.20 (n/a)</td><td>161.30 (n/a)</td><td>37.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.20 (n/a)</td><td>183.62 (n/a)</td><td>181.80 (n/a)</td><td>136.00 (n/a)</td><td>32.83 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>176.30 (n/a)</td><td>172.10 (n/a)</td><td>148.20 (n/a)</td><td>24.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.30 (n/a)</td><td>186.48 (n/a)</td><td>190.20 (n/a)</td><td>142.20 (n/a)</td><td>29.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>249.20 (n/a)</td><td>202.60 (n/a)</td><td>206.60 (n/a)</td><td>146.60 (n/a)</td><td>41.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>264.20 (n/a)</td><td>212.54 (n/a)</td><td>216.70 (n/a)</td><td>147.20 (n/a)</td><td>43.12 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.20 (n/a)</td><td>187.00 (n/a)</td><td>189.20 (n/a)</td><td>152.10 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>218.40 (n/a)</td><td>195.44 (n/a)</td><td>199.20 (n/a)</td><td>171.90 (n/a)</td><td>18.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.43 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>213.00 (n/a)</td><td>166.52 (n/a)</td><td>180.60 (n/a)</td><td>76.30 (n/a)</td><td>52.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.90 (n/a)</td><td>176.84 (n/a)</td><td>193.80 (n/a)</td><td>127.30 (n/a)</td><td>32.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>232.10 (n/a)</td><td>181.18 (n/a)</td><td>189.50 (n/a)</td><td>124.40 (n/a)</td><td>42.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>255.80 (n/a)</td><td>205.20 (n/a)</td><td>196.40 (n/a)</td><td>158.20 (n/a)</td><td>43.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>260.60 (n/a)</td><td>193.72 (n/a)</td><td>179.40 (n/a)</td><td>147.30 (n/a)</td><td>42.34 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>271.90 (n/a)</td><td>195.38 (n/a)</td><td>188.30 (n/a)</td><td>128.50 (n/a)</td><td>52.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+12.32%)</td><td>0.02 (-0.25%)</td><td>0.02 (+3.10%)</td><td>0.02 (-19.28%)</td><td>0.00 <b>(+147.80%)</b></td><td>217.80 <b>(+23.89%)</b></td><td>169.30 (+2.31%)</td><td>164.20 (-3.01%)</td><td>134.10 (-10.96%)</td><td>30.23 <b>(+178.13%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.80 (n/a)</td><td>165.48 (n/a)</td><td>169.30 (n/a)</td><td>150.60 (n/a)</td><td>10.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-7.94%)</td><td>0.03 (-3.87%)</td><td>0.02 (-5.23%)</td><td>0.02 (-11.33%)</td><td>0.01 (+3.41%)</td><td>228.00 (+12.76%)</td><td>171.48 (+5.19%)</td><td>179.60 (+5.52%)</td><td>124.80 (+8.62%)</td><td>42.47 <b>(+24.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>163.02 (n/a)</td><td>170.20 (n/a)</td><td>114.90 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+1.85%)</td><td>0.03 (+5.32%)</td><td>0.03 (+8.19%)</td><td>0.01 <b>(-26.31%)</b></td><td>0.01 <b>(+52.09%)</b></td><td>277.50 <b>(+35.70%)</b></td><td>174.38 (+0.06%)</td><td>161.30 (-7.56%)</td><td>127.50 (-1.77%)</td><td>61.22 <b>(+101.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>174.28 (n/a)</td><td>174.50 (n/a)</td><td>129.80 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+10.04%)</td><td>0.03 (+5.96%)</td><td>0.03 (+3.11%)</td><td>0.02 <b>(+20.00%)</b></td><td>0.00 (-12.49%)</td><td>191.60 (-16.66%)</td><td>158.62 (-6.77%)</td><td>153.00 (-2.98%)</td><td>130.20 (-9.14%)</td><td>23.10 <b>(-34.41%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.90 (n/a)</td><td>170.14 (n/a)</td><td>157.70 (n/a)</td><td>143.30 (n/a)</td><td>35.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-5.13%)</td><td>0.02 (-2.90%)</td><td>0.03 (+6.75%)</td><td>0.01 <b>(-47.44%)</b></td><td>0.01 <b>(+120.45%)</b></td><td>383.00 <b>(+90.26%)</b></td><td>195.08 (+17.19%)</td><td>149.30 (-6.34%)</td><td>145.60 (+5.35%)</td><td>105.07 <b>(+345.90%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.30 (n/a)</td><td>166.46 (n/a)</td><td>159.40 (n/a)</td><td>138.20 (n/a)</td><td>23.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-1.11%)</td><td>0.02 (+6.39%)</td><td>0.02 (+7.24%)</td><td>0.02 (+1.54%)</td><td>0.00 (-7.10%)</td><td>215.70 (-1.51%)</td><td>175.04 (-6.21%)</td><td>171.30 (-6.75%)</td><td>156.10 (+1.10%)</td><td>24.15 (-7.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.00 (n/a)</td><td>186.62 (n/a)</td><td>183.70 (n/a)</td><td>154.40 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 <b>(+40.99%)</b></td><td>0.03 <b>(+25.62%)</b></td><td>0.03 <b>(+32.20%)</b></td><td>0.02 (-2.25%)</td><td>0.01 <b>(+258.10%)</b></td><td>216.30 (+2.32%)</td><td>157.98 (-17.31%)</td><td>143.20 <b>(-24.35%)</b></td><td>122.60 <b>(-29.09%)</b></td><td>38.37 <b>(+160.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.40 (n/a)</td><td>191.04 (n/a)</td><td>189.30 (n/a)</td><td>172.90 (n/a)</td><td>14.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-16.38%)</td><td>0.02 (+7.55%)</td><td>0.02 (+7.09%)</td><td>0.02 <b>(+27.49%)</b></td><td>0.00 <b>(-44.04%)</b></td><td>258.10 <b>(-21.57%)</b></td><td>200.48 (-14.51%)</td><td>178.20 (-6.60%)</td><td>162.20 (+19.62%)</td><td>42.65 <b>(-51.92%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>329.10 (n/a)</td><td>234.50 (n/a)</td><td>190.80 (n/a)</td><td>135.60 (n/a)</td><td>88.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (-3.98%)</td><td>0.06 (+6.67%)</td><td>0.06 (+11.62%)</td><td>0.05 (-1.06%)</td><td>0.01 (-18.65%)</td><td>180.80 (+1.06%)</td><td>146.74 (-6.80%)</td><td>144.20 (-10.43%)</td><td>123.10 (+4.15%)</td><td>21.09 (-10.06%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>157.44 (n/a)</td><td>161.00 (n/a)</td><td>118.20 (n/a)</td><td>23.45 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (+1.44%)</td><td>0.06 (+18.57%)</td><td>0.06 <b>(+36.20%)</b></td><td>0.04 (+1.11%)</td><td>0.01 (-3.68%)</td><td>187.80 (-1.11%)</td><td>137.92 (-15.77%)</td><td>128.20 <b>(-26.58%)</b></td><td>117.60 (-1.42%)</td><td>28.26 (-1.16%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>163.74 (n/a)</td><td>174.60 (n/a)</td><td>119.30 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 <b>(+29.31%)</b></td><td>0.06 (+10.52%)</td><td>0.05 (+2.79%)</td><td>0.04 (-12.96%)</td><td>0.01 <b>(+369.98%)</b></td><td>197.70 (+14.88%)</td><td>154.12 (-6.50%)</td><td>161.40 (-2.71%)</td><td>118.30 <b>(-22.68%)</b></td><td>31.87 <b>(+309.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.10 (n/a)</td><td>164.84 (n/a)</td><td>165.90 (n/a)</td><td>153.00 (n/a)</td><td>7.79 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (+12.30%)</td><td>0.06 (+18.70%)</td><td>0.06 (+16.39%)</td><td>0.05 <b>(+24.05%)</b></td><td>0.00 <b>(-30.55%)</b></td><td>164.20 (-19.35%)</td><td>148.36 (-16.25%)</td><td>146.40 (-14.08%)</td><td>138.10 (-10.90%)</td><td>9.73 <b>(-49.93%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>177.14 (n/a)</td><td>170.40 (n/a)</td><td>155.00 (n/a)</td><td>19.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (-9.54%)</td><td>0.06 (+15.82%)</td><td>0.06 <b>(+43.32%)</b></td><td>0.04 <b>(+81.97%)</b></td><td>0.01 <b>(-59.57%)</b></td><td>191.50 <b>(-45.03%)</b></td><td>148.22 <b>(-26.08%)</b></td><td>145.90 <b>(-30.22%)</b></td><td>126.20 (+10.51%)</td><td>26.18 <b>(-72.82%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>348.40 (n/a)</td><td>200.52 (n/a)</td><td>209.10 (n/a)</td><td>114.20 (n/a)</td><td>96.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (+12.46%)</td><td>0.05 (+15.56%)</td><td>0.06 (+14.50%)</td><td>0.04 (+4.23%)</td><td>0.01 <b>(+39.70%)</b></td><td>214.00 (-4.08%)</td><td>154.96 (-12.34%)</td><td>146.00 (-12.63%)</td><td>131.10 (-11.06%)</td><td>34.30 (+18.12%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.10 (n/a)</td><td>176.78 (n/a)</td><td>167.10 (n/a)</td><td>147.40 (n/a)</td><td>29.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 <b>(+30.65%)</b></td><td>0.05 <b>(+26.09%)</b></td><td>0.05 <b>(+29.08%)</b></td><td>0.05 <b>(+30.09%)</b></td><td>0.01 <b>(+37.02%)</b></td><td>175.10 <b>(-23.10%)</b></td><td>154.10 <b>(-20.52%)</b></td><td>155.30 <b>(-22.54%)</b></td><td>121.00 <b>(-23.47%)</b></td><td>22.48 (-17.75%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>193.88 (n/a)</td><td>200.50 (n/a)</td><td>158.10 (n/a)</td><td>27.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (-1.96%)</td><td>0.05 (+15.79%)</td><td>0.05 <b>(+36.02%)</b></td><td>0.04 (+15.82%)</td><td>0.01 <b>(-24.30%)</b></td><td>192.00 (-13.67%)</td><td>162.02 (-15.93%)</td><td>156.10 <b>(-26.51%)</b></td><td>119.00 (+1.97%)</td><td>30.61 <b>(-29.24%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.40 (n/a)</td><td>192.72 (n/a)</td><td>212.40 (n/a)</td><td>116.70 (n/a)</td><td>43.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 <b>(+22.70%)</b></td><td>0.05 (+1.04%)</td><td>0.05 (-3.90%)</td><td>0.04 (-10.72%)</td><td>0.01 <b>(+200.00%)</b></td><td>218.20 (+12.01%)</td><td>180.10 (+2.12%)</td><td>177.10 (+4.05%)</td><td>132.10 (-18.51%)</td><td>36.89 <b>(+180.02%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>194.80 (n/a)</td><td>176.36 (n/a)</td><td>170.20 (n/a)</td><td>162.10 (n/a)</td><td>13.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (+11.58%)</td><td>0.04 (-2.09%)</td><td>0.04 (-5.17%)</td><td>0.02 (-10.10%)</td><td>0.01 <b>(+33.31%)</b></td><td>367.70 (+11.22%)</td><td>246.30 (+4.66%)</td><td>231.40 (+5.47%)</td><td>173.70 (-10.37%)</td><td>72.36 <b>(+32.91%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.60 (n/a)</td><td>235.34 (n/a)</td><td>219.40 (n/a)</td><td>193.80 (n/a)</td><td>54.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (-16.03%)</td><td>0.10 (-5.44%)</td><td>0.10 (+1.08%)</td><td>0.09 (-2.96%)</td><td>0.01 <b>(-35.28%)</b></td><td>185.30 (+3.06%)</td><td>161.94 (+4.68%)</td><td>156.40 (-1.08%)</td><td>137.30 (+19.08%)</td><td>20.01 (-16.02%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>179.80 (n/a)</td><td>154.70 (n/a)</td><td>158.10 (n/a)</td><td>115.30 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (-1.44%)</td><td>0.10 (-7.44%)</td><td>0.10 (-6.70%)</td><td>0.09 (-7.66%)</td><td>0.01 (+10.55%)</td><td>180.60 (+8.34%)</td><td>164.66 (+8.31%)</td><td>169.80 (+7.13%)</td><td>135.30 (+1.50%)</td><td>17.44 (+19.16%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>166.70 (n/a)</td><td>152.02 (n/a)</td><td>158.50 (n/a)</td><td>133.30 (n/a)</td><td>14.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (-12.90%)</td><td>0.11 (-4.01%)</td><td>0.09 (-10.93%)</td><td>0.08 (-7.84%)</td><td>0.03 (-5.06%)</td><td>201.80 (+8.49%)</td><td>164.14 (+4.75%)</td><td>184.90 (+12.26%)</td><td>119.00 (+14.86%)</td><td>39.30 (+16.99%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>186.00 (n/a)</td><td>156.70 (n/a)</td><td>164.70 (n/a)</td><td>103.60 (n/a)</td><td>33.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 <b>(-24.14%)</b></td><td>0.11 (+7.56%)</td><td>0.11 (+17.79%)</td><td>0.10 <b>(+35.45%)</b></td><td>0.01 <b>(-77.45%)</b></td><td>170.40 <b>(-26.14%)</b></td><td>154.08 (-12.24%)</td><td>148.80 (-15.12%)</td><td>145.50 <b>(+31.79%)</b></td><td>10.17 <b>(-77.15%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>230.70 (n/a)</td><td>175.56 (n/a)</td><td>175.30 (n/a)</td><td>110.40 (n/a)</td><td>44.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (-6.74%)</td><td>0.11 (+2.42%)</td><td>0.11 (-8.22%)</td><td>0.10 <b>(+35.74%)</b></td><td>0.01 <b>(-48.21%)</b></td><td>162.80 <b>(-26.37%)</b></td><td>147.70 (-6.81%)</td><td>150.60 (+8.97%)</td><td>118.80 (+7.22%)</td><td>17.35 <b>(-60.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>221.10 (n/a)</td><td>158.50 (n/a)</td><td>138.20 (n/a)</td><td>110.80 (n/a)</td><td>44.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (-1.37%)</td><td>0.11 (+14.37%)</td><td>0.11 (+14.79%)</td><td>0.09 <b>(+21.74%)</b></td><td>0.01 <b>(-37.51%)</b></td><td>186.40 (-17.89%)</td><td>154.48 (-14.96%)</td><td>153.70 (-12.87%)</td><td>128.60 (+1.34%)</td><td>20.69 <b>(-47.61%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.00 (n/a)</td><td>181.66 (n/a)</td><td>176.40 (n/a)</td><td>126.90 (n/a)</td><td>39.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (+9.84%)</td><td>0.11 (+14.69%)</td><td>0.11 <b>(+26.58%)</b></td><td>0.09 <b>(+25.00%)</b></td><td>0.01 <b>(-32.66%)</b></td><td>174.50 (-19.99%)</td><td>154.12 (-14.62%)</td><td>153.50 <b>(-21.00%)</b></td><td>127.80 (-8.97%)</td><td>17.15 <b>(-50.66%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>218.10 (n/a)</td><td>180.52 (n/a)</td><td>194.30 (n/a)</td><td>140.40 (n/a)</td><td>34.76 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (+0.83%)</td><td>0.09 <b>(+24.54%)</b></td><td>0.09 <b>(+31.71%)</b></td><td>0.07 <b>(+44.66%)</b></td><td>0.01 <b>(-37.77%)</b></td><td>236.30 <b>(-30.87%)</b></td><td>190.26 <b>(-22.59%)</b></td><td>181.50 <b>(-24.09%)</b></td><td>168.30 (-0.82%)</td><td>27.13 <b>(-56.73%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>341.80 (n/a)</td><td>245.78 (n/a)</td><td>239.10 (n/a)</td><td>169.70 (n/a)</td><td>62.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (-11.36%)</td><td>0.20 (+8.93%)</td><td>0.19 (-0.76%)</td><td>0.17 <b>(+73.61%)</b></td><td>0.03 <b>(-52.16%)</b></td><td>193.90 <b>(-42.39%)</b></td><td>163.64 (-17.04%)</td><td>168.40 (+0.78%)</td><td>131.10 (+12.82%)</td><td>24.60 <b>(-70.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>336.60 (n/a)</td><td>197.26 (n/a)</td><td>167.10 (n/a)</td><td>116.20 (n/a)</td><td>83.59 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 <b>(-31.37%)</b></td><td>0.17 (-17.61%)</td><td>0.18 (-8.82%)</td><td>0.13 (-16.85%)</td><td>0.03 <b>(-51.85%)</b></td><td>256.50 <b>(+20.25%)</b></td><td>196.76 (+17.82%)</td><td>184.20 (+9.64%)</td><td>170.20 <b>(+45.72%)</b></td><td>34.85 (-14.66%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>213.30 (n/a)</td><td>167.00 (n/a)</td><td>168.00 (n/a)</td><td>116.80 (n/a)</td><td>40.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 <b>(+22.03%)</b></td><td>0.19 (+1.99%)</td><td>0.18 (-5.33%)</td><td>0.13 <b>(-27.44%)</b></td><td>0.05 <b>(+594.62%)</b></td><td>252.40 <b>(+37.85%)</b></td><td>180.78 (+3.55%)</td><td>185.50 (+5.64%)</td><td>135.20 (-18.06%)</td><td>48.62 <b>(+648.43%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>174.58 (n/a)</td><td>175.60 (n/a)</td><td>165.00 (n/a)</td><td>6.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (+18.84%)</td><td>0.20 (+12.66%)</td><td>0.19 (+4.40%)</td><td>0.17 <b>(+21.50%)</b></td><td>0.03 <b>(+20.67%)</b></td><td>197.50 (-17.67%)</td><td>165.18 (-11.27%)</td><td>171.50 (-4.19%)</td><td>132.30 (-15.84%)</td><td>25.45 (-19.78%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>239.90 (n/a)</td><td>186.16 (n/a)</td><td>179.00 (n/a)</td><td>157.20 (n/a)</td><td>31.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (+16.87%)</td><td>0.21 <b>(+26.52%)</b></td><td>0.20 (+19.86%)</td><td>0.16 <b>(+37.61%)</b></td><td>0.05 (+17.29%)</td><td>206.00 <b>(-27.31%)</b></td><td>163.16 <b>(-21.50%)</b></td><td>165.60 (-16.53%)</td><td>126.70 (-14.39%)</td><td>35.20 <b>(-29.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>283.40 (n/a)</td><td>207.84 (n/a)</td><td>198.40 (n/a)</td><td>148.00 (n/a)</td><td>50.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 <b>(+27.04%)</b></td><td>0.20 (+12.41%)</td><td>0.18 (+0.34%)</td><td>0.16 (-0.60%)</td><td>0.04 <b>(+137.48%)</b></td><td>210.20 (+0.57%)</td><td>169.20 (-8.52%)</td><td>177.30 (-0.34%)</td><td>129.60 <b>(-21.31%)</b></td><td>35.36 <b>(+82.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>209.00 (n/a)</td><td>184.96 (n/a)</td><td>177.90 (n/a)</td><td>164.70 (n/a)</td><td>19.40 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (-6.51%)</td><td>0.16 (+1.99%)</td><td>0.18 <b>(+22.37%)</b></td><td>0.10 <b>(-28.59%)</b></td><td>0.04 <b>(+50.59%)</b></td><td>331.10 <b>(+40.06%)</b></td><td>214.98 (+2.45%)</td><td>177.90 (-18.28%)</td><td>171.40 (+6.92%)</td><td>67.80 <b>(+134.01%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.40 (n/a)</td><td>209.84 (n/a)</td><td>217.70 (n/a)</td><td>160.30 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-19.48%)</td><td>0.02 <b>(-21.39%)</b></td><td>0.03 (-8.70%)</td><td>0.01 <b>(-49.77%)</b></td><td>0.01 <b>(+87.85%)</b></td><td>348.00 <b>(+99.08%)</b></td><td>208.04 <b>(+37.50%)</b></td><td>163.40 (+9.52%)</td><td>160.40 <b>(+24.24%)</b></td><td>80.68 <b>(+360.74%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.80 (n/a)</td><td>151.30 (n/a)</td><td>149.20 (n/a)</td><td>129.10 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (+4.32%)</td><td>0.03 (+7.48%)</td><td>0.03 (+17.72%)</td><td>0.02 (-2.83%)</td><td>0.01 (+9.29%)</td><td>196.70 (+2.93%)</td><td>150.94 (-6.42%)</td><td>142.90 (-15.04%)</td><td>111.30 (-4.22%)</td><td>32.40 (+10.26%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>161.30 (n/a)</td><td>168.20 (n/a)</td><td>116.20 (n/a)</td><td>29.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4746284.10 (n/a)</td><td>4746128.87 (n/a)</td><td>4746065.90 (n/a)</td><td>4746036.60 (n/a)</td><td>135.23 (n/a)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (+2.03%)</td><td>0.02 (+0.14%)</td><td>0.02 (-3.28%)</td><td>0.02 (+2.91%)</td><td>0.00 (+8.37%)</td><td>221.30 (-2.85%)</td><td>202.58 (-0.01%)</td><td>208.80 (+3.37%)</td><td>164.90 (-2.02%)</td><td>23.30 (+4.48%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.80 (n/a)</td><td>202.60 (n/a)</td><td>202.00 (n/a)</td><td>168.30 (n/a)</td><td>22.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+9.74%)</td><td>0.03 (+4.18%)</td><td>0.02 (+4.15%)</td><td>0.02 (-11.86%)</td><td>0.01 <b>(+72.85%)</b></td><td>209.10 (+13.46%)</td><td>167.58 (-1.92%)</td><td>171.30 (-3.98%)</td><td>126.70 (-8.85%)</td><td>32.89 <b>(+80.87%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.30 (n/a)</td><td>170.86 (n/a)</td><td>178.40 (n/a)</td><td>139.00 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-12.40%)</td><td>0.03 (-2.83%)</td><td>0.03 (+2.05%)</td><td>0.02 (+4.94%)</td><td>0.00 <b>(-47.15%)</b></td><td>185.60 (-4.72%)</td><td>152.74 (-0.33%)</td><td>148.60 (-2.04%)</td><td>130.50 (+14.17%)</td><td>21.19 <b>(-41.81%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>153.24 (n/a)</td><td>151.70 (n/a)</td><td>114.30 (n/a)</td><td>36.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-6.26%)</td><td>0.02 (-12.59%)</td><td>0.02 (-12.10%)</td><td>0.02 (-19.76%)</td><td>0.00 <b>(+39.93%)</b></td><td>208.20 <b>(+24.67%)</b></td><td>170.78 (+15.42%)</td><td>167.90 (+13.75%)</td><td>144.10 (+6.66%)</td><td>23.38 <b>(+89.19%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>167.00 (n/a)</td><td>147.96 (n/a)</td><td>147.60 (n/a)</td><td>135.10 (n/a)</td><td>12.36 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-11.62%)</td><td>0.02 (-9.85%)</td><td>0.02 (-16.40%)</td><td>0.02 (-3.17%)</td><td>0.00 <b>(-22.81%)</b></td><td>210.80 (+3.28%)</td><td>175.14 (+9.75%)</td><td>184.20 (+19.69%)</td><td>133.90 (+13.19%)</td><td>29.33 (-11.47%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>159.58 (n/a)</td><td>153.90 (n/a)</td><td>118.30 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 <b>(+26.83%)</b></td><td>0.02 (+7.49%)</td><td>0.02 (-5.40%)</td><td>0.02 <b>(+25.41%)</b></td><td>0.01 (+19.54%)</td><td>206.80 <b>(-20.25%)</b></td><td>178.44 (-7.47%)</td><td>189.40 (+5.75%)</td><td>117.30 <b>(-21.17%)</b></td><td>35.12 <b>(-26.79%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>259.30 (n/a)</td><td>192.84 (n/a)</td><td>179.10 (n/a)</td><td>148.80 (n/a)</td><td>47.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 <b>(+43.46%)</b></td><td>0.03 (+18.82%)</td><td>0.03 (+12.57%)</td><td>0.02 (-0.73%)</td><td>0.01 <b>(+147.94%)</b></td><td>215.70 (+0.75%)</td><td>161.20 (-12.76%)</td><td>161.10 (-11.14%)</td><td>111.70 <b>(-30.32%)</b></td><td>38.56 <b>(+72.58%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.10 (n/a)</td><td>184.78 (n/a)</td><td>181.30 (n/a)</td><td>160.30 (n/a)</td><td>22.34 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-0.55%)</td><td>0.02 (-3.20%)</td><td>0.02 (-19.40%)</td><td>0.02 (+17.06%)</td><td>0.00 (-10.94%)</td><td>227.40 (-14.58%)</td><td>192.48 (+1.68%)</td><td>210.10 <b>(+24.03%)</b></td><td>144.20 (+0.56%)</td><td>39.46 <b>(-22.67%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>266.20 (n/a)</td><td>189.30 (n/a)</td><td>169.40 (n/a)</td><td>143.40 (n/a)</td><td>51.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+10.49%)</td><td>0.03 (+14.13%)</td><td>0.03 <b>(+24.72%)</b></td><td>0.02 (+2.84%)</td><td>0.00 <b>(+25.87%)</b></td><td>223.10 (-2.75%)</td><td>168.62 (-11.65%)</td><td>160.20 (-19.82%)</td><td>139.70 (-9.52%)</td><td>34.18 (+11.74%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.40 (n/a)</td><td>190.86 (n/a)</td><td>199.80 (n/a)</td><td>154.40 (n/a)</td><td>30.59 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+8.55%)</td><td>0.02 (+10.03%)</td><td>0.02 (+16.33%)</td><td>0.02 (+7.66%)</td><td>0.00 (+7.57%)</td><td>217.70 (-7.12%)</td><td>182.58 (-9.12%)</td><td>174.10 (-14.07%)</td><td>160.80 (-7.90%)</td><td>21.83 (-6.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.40 (n/a)</td><td>200.90 (n/a)</td><td>202.60 (n/a)</td><td>174.60 (n/a)</td><td>23.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 <b>(-24.13%)</b></td><td>0.02 <b>(-21.06%)</b></td><td>0.02 (+3.64%)</td><td>0.01 <b>(-41.58%)</b></td><td>0.01 (-5.76%)</td><td>360.80 <b>(+71.16%)</b></td><td>230.30 <b>(+32.43%)</b></td><td>187.80 (-3.54%)</td><td>164.60 <b>(+31.79%)</b></td><td>85.63 <b>(+105.01%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>173.90 (n/a)</td><td>194.70 (n/a)</td><td>124.90 (n/a)</td><td>41.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-3.92%)</td><td>0.02 (+5.53%)</td><td>0.02 <b>(+21.84%)</b></td><td>0.02 (+7.23%)</td><td>0.00 (-17.39%)</td><td>207.20 (-6.75%)</td><td>179.62 (-5.77%)</td><td>166.10 (-17.93%)</td><td>161.40 (+4.13%)</td><td>22.02 (-19.19%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.20 (n/a)</td><td>190.62 (n/a)</td><td>202.40 (n/a)</td><td>155.00 (n/a)</td><td>27.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+19.68%)</td><td>0.03 (+10.37%)</td><td>0.03 (+15.15%)</td><td>0.02 (+0.49%)</td><td>0.00 <b>(+86.21%)</b></td><td>191.70 (-0.52%)</td><td>156.32 (-7.94%)</td><td>141.70 (-13.17%)</td><td>128.70 (-16.43%)</td><td>27.82 <b>(+57.95%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.70 (n/a)</td><td>169.80 (n/a)</td><td>163.20 (n/a)</td><td>154.00 (n/a)</td><td>17.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (+2.62%)</td><td>0.05 (+7.65%)</td><td>0.06 (+16.58%)</td><td>0.04 (-4.23%)</td><td>0.01 (+15.33%)</td><td>222.90 (+4.40%)</td><td>164.18 (-6.24%)</td><td>145.50 (-14.21%)</td><td>132.20 (-2.51%)</td><td>39.01 (+13.26%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>175.10 (n/a)</td><td>169.60 (n/a)</td><td>135.60 (n/a)</td><td>34.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 <b>(+20.80%)</b></td><td>0.05 (+5.35%)</td><td>0.05 (+7.00%)</td><td>0.04 (-12.83%)</td><td>0.01 <b>(+172.83%)</b></td><td>225.50 (+14.76%)</td><td>178.40 (-1.10%)</td><td>174.60 (-6.58%)</td><td>133.60 (-17.22%)</td><td>43.25 <b>(+162.35%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>196.50 (n/a)</td><td>180.38 (n/a)</td><td>186.90 (n/a)</td><td>161.40 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 <b>(-26.42%)</b></td><td>0.04 (-11.00%)</td><td>0.04 (+5.78%)</td><td>0.03 <b>(-22.86%)</b></td><td>0.01 <b>(-28.96%)</b></td><td>302.60 <b>(+29.65%)</b></td><td>222.32 (+12.07%)</td><td>198.00 (-5.49%)</td><td>190.90 <b>(+35.97%)</b></td><td>46.99 <b>(+28.54%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.40 (n/a)</td><td>198.38 (n/a)</td><td>209.50 (n/a)</td><td>140.40 (n/a)</td><td>36.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 <b>(-39.12%)</b></td><td>0.03 <b>(-27.95%)</b></td><td>0.03 (-13.90%)</td><td>0.02 <b>(-32.99%)</b></td><td>0.01 <b>(-40.12%)</b></td><td>361.50 <b>(+49.26%)</b></td><td>275.30 <b>(+37.94%)</b></td><td>254.70 (+16.14%)</td><td>214.80 <b>(+64.22%)</b></td><td>66.39 <b>(+45.68%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.20 (n/a)</td><td>199.58 (n/a)</td><td>219.30 (n/a)</td><td>130.80 (n/a)</td><td>45.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (+15.52%)</td><td>0.05 (+9.22%)</td><td>0.05 (-7.92%)</td><td>0.04 <b>(+27.38%)</b></td><td>0.01 (+2.49%)</td><td>189.20 <b>(-21.49%)</b></td><td>164.42 (-9.16%)</td><td>176.30 (+8.63%)</td><td>132.30 (-13.42%)</td><td>24.56 <b>(-31.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.00 (n/a)</td><td>181.00 (n/a)</td><td>162.30 (n/a)</td><td>152.80 (n/a)</td><td>35.92 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 <b>(+24.02%)</b></td><td>0.06 <b>(+27.59%)</b></td><td>0.06 <b>(+29.23%)</b></td><td>0.04 <b>(+26.22%)</b></td><td>0.01 (+17.42%)</td><td>185.30 <b>(-20.78%)</b></td><td>145.14 <b>(-21.78%)</b></td><td>139.90 <b>(-22.62%)</b></td><td>126.40 (-19.39%)</td><td>23.34 <b>(-23.39%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>185.56 (n/a)</td><td>180.80 (n/a)</td><td>156.80 (n/a)</td><td>30.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (-17.85%)</td><td>0.05 (-8.98%)</td><td>0.05 (+9.70%)</td><td>0.04 (+10.75%)</td><td>0.01 <b>(-42.54%)</b></td><td>221.60 (-9.70%)</td><td>181.30 (+5.80%)</td><td>161.30 (-8.82%)</td><td>151.30 <b>(+21.72%)</b></td><td>32.78 <b>(-33.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.40 (n/a)</td><td>171.36 (n/a)</td><td>176.90 (n/a)</td><td>124.30 (n/a)</td><td>49.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (-10.59%)</td><td>0.05 (+11.40%)</td><td>0.06 <b>(+28.97%)</b></td><td>0.04 (+16.10%)</td><td>0.01 <b>(-30.27%)</b></td><td>220.50 (-13.87%)</td><td>159.86 (-12.84%)</td><td>144.70 <b>(-22.45%)</b></td><td>132.20 (+11.84%)</td><td>35.15 <b>(-28.93%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.00 (n/a)</td><td>183.42 (n/a)</td><td>186.60 (n/a)</td><td>118.20 (n/a)</td><td>49.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (+5.25%)</td><td>0.05 (+10.45%)</td><td>0.05 <b>(+20.48%)</b></td><td>0.03 (-0.31%)</td><td>0.01 (+7.61%)</td><td>262.00 (+0.31%)</td><td>171.78 (-8.73%)</td><td>155.80 (-17.00%)</td><td>135.90 (-5.03%)</td><td>51.58 (+8.62%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.20 (n/a)</td><td>188.22 (n/a)</td><td>187.70 (n/a)</td><td>143.10 (n/a)</td><td>47.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (+0.47%)</td><td>0.05 (+14.27%)</td><td>0.05 (+3.78%)</td><td>0.04 <b>(+89.26%)</b></td><td>0.00 <b>(-62.46%)</b></td><td>187.40 <b>(-47.15%)</b></td><td>167.62 (-19.99%)</td><td>168.70 (-3.60%)</td><td>143.90 (-0.48%)</td><td>15.49 <b>(-81.59%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>354.60 (n/a)</td><td>209.50 (n/a)</td><td>175.00 (n/a)</td><td>144.60 (n/a)</td><td>84.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (+4.86%)</td><td>0.06 (+13.43%)</td><td>0.05 (+16.26%)</td><td>0.04 (-0.87%)</td><td>0.01 (+6.62%)</td><td>202.00 (+0.90%)</td><td>154.08 (-11.49%)</td><td>158.40 (-13.96%)</td><td>109.50 (-4.62%)</td><td>36.26 (+3.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>174.08 (n/a)</td><td>184.10 (n/a)</td><td>114.80 (n/a)</td><td>35.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 <b>(+26.24%)</b></td><td>0.05 <b>(+27.73%)</b></td><td>0.05 <b>(+43.27%)</b></td><td>0.04 <b>(+21.01%)</b></td><td>0.01 <b>(+35.20%)</b></td><td>188.80 (-17.37%)</td><td>162.00 <b>(-21.53%)</b></td><td>151.90 <b>(-30.19%)</b></td><td>142.90 <b>(-20.79%)</b></td><td>21.22 (-10.25%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>228.50 (n/a)</td><td>206.44 (n/a)</td><td>217.60 (n/a)</td><td>180.40 (n/a)</td><td>23.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (-14.63%)</td><td>0.04 (-15.92%)</td><td>0.05 (-9.01%)</td><td>0.02 <b>(-41.73%)</b></td><td>0.01 <b>(+48.33%)</b></td><td>366.40 <b>(+71.62%)</b></td><td>219.84 <b>(+27.78%)</b></td><td>174.90 (+9.93%)</td><td>162.70 (+17.13%)</td><td>86.48 <b>(+192.20%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>172.04 (n/a)</td><td>159.10 (n/a)</td><td>138.90 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 <b>(+21.68%)</b></td><td>0.05 (+13.73%)</td><td>0.05 (+8.02%)</td><td>0.04 (-4.51%)</td><td>0.01 <b>(+139.36%)</b></td><td>212.10 (+4.69%)</td><td>167.38 (-9.63%)</td><td>177.20 (-7.42%)</td><td>131.70 (-17.79%)</td><td>34.54 <b>(+96.65%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.60 (n/a)</td><td>185.22 (n/a)</td><td>191.40 (n/a)</td><td>160.20 (n/a)</td><td>17.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 <b>(+40.46%)</b></td><td>0.05 (+6.17%)</td><td>0.05 (+5.98%)</td><td>0.03 <b>(-24.54%)</b></td><td>0.02 <b>(+187.29%)</b></td><td>287.00 <b>(+32.50%)</b></td><td>194.36 (+5.36%)</td><td>167.60 (-5.63%)</td><td>112.20 <b>(-28.81%)</b></td><td>77.41 <b>(+183.88%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>184.48 (n/a)</td><td>177.60 (n/a)</td><td>157.60 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (+1.21%)</td><td>0.05 (-11.29%)</td><td>0.05 (-12.32%)</td><td>0.04 (-11.35%)</td><td>0.01 (+12.70%)</td><td>197.40 (+12.80%)</td><td>168.64 (+13.58%)</td><td>174.70 (+14.11%)</td><td>121.70 (-1.22%)</td><td>28.43 <b>(+23.21%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.00 (n/a)</td><td>148.48 (n/a)</td><td>153.10 (n/a)</td><td>123.20 (n/a)</td><td>23.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 <b>(+29.89%)</b></td><td>0.11 (+5.89%)</td><td>0.11 (+0.88%)</td><td>0.09 (-1.62%)</td><td>0.03 <b>(+146.49%)</b></td><td>183.30 (+1.61%)</td><td>154.70 (-2.81%)</td><td>155.20 (-0.89%)</td><td>106.10 <b>(-23.00%)</b></td><td>30.02 <b>(+87.48%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>159.18 (n/a)</td><td>156.60 (n/a)</td><td>137.80 (n/a)</td><td>16.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (-2.40%)</td><td>0.10 (-1.55%)</td><td>0.10 (-9.70%)</td><td>0.06 (-10.20%)</td><td>0.03 (-7.92%)</td><td>254.10 (+11.35%)</td><td>169.10 (+1.43%)</td><td>164.40 (+10.71%)</td><td>125.50 (+2.45%)</td><td>50.54 (+7.62%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>228.20 (n/a)</td><td>166.72 (n/a)</td><td>148.50 (n/a)</td><td>122.50 (n/a)</td><td>46.96 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.09 (-13.75%)</td><td>0.08 (+0.87%)</td><td>0.08 (+6.77%)</td><td>0.08 (+18.91%)</td><td>0.00 <b>(-66.03%)</b></td><td>211.50 (-15.90%)</td><td>198.82 (-2.70%)</td><td>194.90 (-6.34%)</td><td>188.00 (+15.98%)</td><td>11.02 <b>(-66.68%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>251.50 (n/a)</td><td>204.34 (n/a)</td><td>208.10 (n/a)</td><td>162.10 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (+0.55%)</td><td>0.10 (+6.86%)</td><td>0.10 (+8.96%)</td><td>0.08 (+9.14%)</td><td>0.01 (-14.50%)</td><td>201.20 (-8.38%)</td><td>171.02 (-6.85%)</td><td>161.20 (-8.25%)</td><td>155.30 (-0.58%)</td><td>18.75 <b>(-22.42%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>183.60 (n/a)</td><td>175.70 (n/a)</td><td>156.20 (n/a)</td><td>24.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (+11.29%)</td><td>0.10 (+1.46%)</td><td>0.09 (-7.59%)</td><td>0.08 (+9.30%)</td><td>0.03 <b>(+25.88%)</b></td><td>193.60 (-8.55%)</td><td>163.76 (-0.58%)</td><td>175.40 (+8.20%)</td><td>108.30 (-10.20%)</td><td>32.90 (+0.07%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.70 (n/a)</td><td>164.72 (n/a)</td><td>162.10 (n/a)</td><td>120.60 (n/a)</td><td>32.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (-0.58%)</td><td>0.10 (+12.32%)</td><td>0.10 (+16.46%)</td><td>0.09 (+14.69%)</td><td>0.01 <b>(-34.85%)</b></td><td>190.00 (-12.80%)</td><td>171.70 (-11.69%)</td><td>167.70 (-14.13%)</td><td>158.30 (+0.64%)</td><td>13.69 <b>(-42.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>194.42 (n/a)</td><td>195.30 (n/a)</td><td>157.30 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (+1.90%)</td><td>0.11 (+4.68%)</td><td>0.10 (+4.27%)</td><td>0.08 (+8.90%)</td><td>0.02 (-5.31%)</td><td>193.20 (-8.13%)</td><td>158.24 (-5.13%)</td><td>169.70 (-4.12%)</td><td>126.30 (-1.86%)</td><td>29.77 (-14.94%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>166.80 (n/a)</td><td>177.00 (n/a)</td><td>128.70 (n/a)</td><td>35.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (-10.03%)</td><td>0.11 (-2.75%)</td><td>0.12 (+6.44%)</td><td>0.08 (+14.06%)</td><td>0.02 <b>(-27.05%)</b></td><td>199.10 (-12.33%)</td><td>158.36 (-0.19%)</td><td>141.10 (-6.06%)</td><td>128.20 (+11.09%)</td><td>35.09 <b>(-25.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>227.10 (n/a)</td><td>158.66 (n/a)</td><td>150.20 (n/a)</td><td>115.40 (n/a)</td><td>47.22 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (-1.58%)</td><td>0.11 (+2.45%)</td><td>0.12 (+13.20%)</td><td>0.08 (-14.10%)</td><td>0.02 <b>(+49.37%)</b></td><td>209.80 (+16.43%)</td><td>159.52 (+0.18%)</td><td>140.90 (-11.66%)</td><td>128.00 (+1.67%)</td><td>37.90 <b>(+74.00%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.20 (n/a)</td><td>159.24 (n/a)</td><td>159.50 (n/a)</td><td>125.90 (n/a)</td><td>21.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 <b>(-24.17%)</b></td><td>0.09 (-14.51%)</td><td>0.09 (-13.59%)</td><td>0.08 (+0.27%)</td><td>0.01 <b>(-63.18%)</b></td><td>197.90 (-0.25%)</td><td>179.28 (+13.54%)</td><td>176.10 (+15.70%)</td><td>156.30 <b>(+31.79%)</b></td><td>15.93 <b>(-52.24%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.40 (n/a)</td><td>157.90 (n/a)</td><td>152.20 (n/a)</td><td>118.60 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 <b>(-22.75%)</b></td><td>0.09 <b>(-22.91%)</b></td><td>0.09 <b>(-26.67%)</b></td><td>0.07 <b>(-24.73%)</b></td><td>0.01 <b>(-26.73%)</b></td><td>234.70 <b>(+32.82%)</b></td><td>189.38 <b>(+29.46%)</b></td><td>186.10 <b>(+36.34%)</b></td><td>160.00 <b>(+29.45%)</b></td><td>29.90 <b>(+24.95%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>176.70 (n/a)</td><td>146.28 (n/a)</td><td>136.50 (n/a)</td><td>123.60 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (+1.81%)</td><td>0.10 (-1.38%)</td><td>0.09 (-1.36%)</td><td>0.08 <b>(+21.73%)</b></td><td>0.02 <b>(-26.73%)</b></td><td>205.50 (-17.83%)</td><td>176.98 (-2.19%)</td><td>181.50 (+1.40%)</td><td>126.70 (-1.78%)</td><td>31.10 <b>(-39.92%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>250.10 (n/a)</td><td>180.94 (n/a)</td><td>179.00 (n/a)</td><td>129.00 (n/a)</td><td>51.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (-11.46%)</td><td>0.10 (-1.62%)</td><td>0.09 (-8.30%)</td><td>0.09 <b>(+54.25%)</b></td><td>0.01 <b>(-64.84%)</b></td><td>192.40 <b>(-35.18%)</b></td><td>173.02 (-5.03%)</td><td>175.10 (+9.03%)</td><td>152.50 (+12.96%)</td><td>15.51 <b>(-76.15%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>296.80 (n/a)</td><td>182.18 (n/a)</td><td>160.60 (n/a)</td><td>135.00 (n/a)</td><td>65.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (+10.21%)</td><td>0.10 (+12.25%)</td><td>0.09 (+12.84%)</td><td>0.07 (+10.87%)</td><td>0.02 (+5.27%)</td><td>224.60 (-9.80%)</td><td>177.36 (-11.35%)</td><td>184.10 (-11.36%)</td><td>137.20 (-9.26%)</td><td>39.27 (-15.57%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>249.00 (n/a)</td><td>200.06 (n/a)</td><td>207.70 (n/a)</td><td>151.20 (n/a)</td><td>46.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 <b>(+29.16%)</b></td><td>0.10 (+14.42%)</td><td>0.09 (-8.57%)</td><td>0.08 <b>(+54.75%)</b></td><td>0.02 (+0.21%)</td><td>210.30 <b>(-35.37%)</b></td><td>170.42 (-15.68%)</td><td>181.60 (+9.33%)</td><td>124.30 <b>(-22.60%)</b></td><td>34.68 <b>(-50.80%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>325.40 (n/a)</td><td>202.12 (n/a)</td><td>166.10 (n/a)</td><td>160.60 (n/a)</td><td>70.48 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 <b>(-20.06%)</b></td><td>0.09 (-10.23%)</td><td>0.09 (-16.78%)</td><td>0.06 (-14.54%)</td><td>0.02 <b>(-23.85%)</b></td><td>252.40 (+17.01%)</td><td>191.00 (+10.40%)</td><td>191.90 <b>(+20.16%)</b></td><td>153.50 <b>(+25.10%)</b></td><td>40.97 (+3.88%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.70 (n/a)</td><td>173.00 (n/a)</td><td>159.70 (n/a)</td><td>122.70 (n/a)</td><td>39.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 (+4.52%)</td><td>0.20 (+1.49%)</td><td>0.19 (+4.84%)</td><td>0.17 (+3.93%)</td><td>0.03 (-6.02%)</td><td>194.10 (-3.77%)</td><td>170.40 (-1.82%)</td><td>171.70 (-4.61%)</td><td>136.40 (-4.35%)</td><td>21.43 (-14.83%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>201.70 (n/a)</td><td>173.56 (n/a)</td><td>180.00 (n/a)</td><td>142.60 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (+1.44%)</td><td>0.21 (-3.12%)</td><td>0.19 (-1.66%)</td><td>0.18 (+0.20%)</td><td>0.03 (-11.08%)</td><td>183.50 (-0.22%)</td><td>160.52 (+2.70%)</td><td>168.90 (+1.69%)</td><td>125.60 (-1.41%)</td><td>24.27 (-9.81%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>183.90 (n/a)</td><td>156.30 (n/a)</td><td>166.10 (n/a)</td><td>127.40 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (-1.47%)</td><td>0.14 (-13.20%)</td><td>0.14 (-15.81%)</td><td>0.12 <b>(-22.25%)</b></td><td>0.03 <b>(+93.29%)</b></td><td>280.90 <b>(+28.62%)</b></td><td>234.24 (+17.86%)</td><td>240.70 (+18.81%)</td><td>177.10 (+1.49%)</td><td>42.82 <b>(+154.72%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>198.74 (n/a)</td><td>202.60 (n/a)</td><td>174.50 (n/a)</td><td>16.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (+4.86%)</td><td>0.19 (+8.05%)</td><td>0.22 <b>(+29.99%)</b></td><td>0.14 (-11.91%)</td><td>0.04 <b>(+74.45%)</b></td><td>232.10 (+13.55%)</td><td>176.58 (-5.11%)</td><td>150.30 <b>(-23.08%)</b></td><td>146.00 (-4.64%)</td><td>39.25 <b>(+85.71%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.40 (n/a)</td><td>186.08 (n/a)</td><td>195.40 (n/a)</td><td>153.10 (n/a)</td><td>21.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 <b>(-24.99%)</b></td><td>0.20 (-4.08%)</td><td>0.20 (-4.91%)</td><td>0.19 <b>(+26.93%)</b></td><td>0.01 <b>(-83.61%)</b></td><td>170.90 <b>(-21.21%)</b></td><td>165.40 (-0.14%)</td><td>166.10 (+5.13%)</td><td>154.80 <b>(+33.33%)</b></td><td>6.58 <b>(-82.75%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>216.90 (n/a)</td><td>165.64 (n/a)</td><td>158.00 (n/a)</td><td>116.10 (n/a)</td><td>38.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.27 (+15.36%)</td><td>0.21 (-2.80%)</td><td>0.19 (-13.90%)</td><td>0.18 (-2.82%)</td><td>0.04 <b>(+84.92%)</b></td><td>181.20 (+2.90%)</td><td>161.44 (+4.29%)</td><td>170.80 (+16.19%)</td><td>123.40 (-13.28%)</td><td>23.89 <b>(+64.42%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>176.10 (n/a)</td><td>154.80 (n/a)</td><td>147.00 (n/a)</td><td>142.30 (n/a)</td><td>14.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 <b>(-20.98%)</b></td><td>0.19 <b>(-25.12%)</b></td><td>0.18 <b>(-28.57%)</b></td><td>0.16 <b>(-23.78%)</b></td><td>0.03 (-1.30%)</td><td>199.50 <b>(+31.25%)</b></td><td>177.82 <b>(+34.28%)</b></td><td>186.30 <b>(+39.97%)</b></td><td>144.40 <b>(+26.56%)</b></td><td>22.78 <b>(+64.16%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>152.00 (n/a)</td><td>132.42 (n/a)</td><td>133.10 (n/a)</td><td>114.10 (n/a)</td><td>13.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (-8.91%)</td><td>0.20 (-14.71%)</td><td>0.19 <b>(-22.22%)</b></td><td>0.14 (-18.77%)</td><td>0.05 (+9.31%)</td><td>231.20 <b>(+23.11%)</b></td><td>171.36 (+19.10%)</td><td>177.00 <b>(+28.54%)</b></td><td>125.30 (+9.82%)</td><td>40.41 <b>(+44.61%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>187.80 (n/a)</td><td>143.88 (n/a)</td><td>137.70 (n/a)</td><td>114.10 (n/a)</td><td>27.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 <b>(-21.47%)</b></td><td>0.19 (-11.38%)</td><td>0.19 (-12.71%)</td><td>0.18 (-2.09%)</td><td>0.01 <b>(-62.59%)</b></td><td>186.70 (+2.13%)</td><td>171.92 (+11.10%)</td><td>173.80 (+14.57%)</td><td>159.90 <b>(+27.31%)</b></td><td>11.24 <b>(-52.28%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>182.80 (n/a)</td><td>154.74 (n/a)</td><td>151.70 (n/a)</td><td>125.60 (n/a)</td><td>23.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 <b>(-21.52%)</b></td><td>0.20 (-9.54%)</td><td>0.20 (-1.80%)</td><td>0.18 (+7.08%)</td><td>0.01 <b>(-78.40%)</b></td><td>180.10 (-6.59%)</td><td>166.96 (+7.81%)</td><td>164.60 (+1.86%)</td><td>161.50 <b>(+27.47%)</b></td><td>7.61 <b>(-73.04%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>192.80 (n/a)</td><td>154.86 (n/a)</td><td>161.60 (n/a)</td><td>126.70 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.31 <b>(+28.84%)</b></td><td>0.23 (+8.15%)</td><td>0.24 (+8.07%)</td><td>0.17 (-2.01%)</td><td>0.06 <b>(+114.49%)</b></td><td>193.20 (+2.06%)</td><td>149.76 (-4.14%)</td><td>138.10 (-7.50%)</td><td>106.70 <b>(-22.40%)</b></td><td>37.15 <b>(+75.64%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>189.30 (n/a)</td><td>156.22 (n/a)</td><td>149.30 (n/a)</td><td>137.50 (n/a)</td><td>21.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 <b>(-20.50%)</b></td><td>0.18 (-8.80%)</td><td>0.17 (-15.19%)</td><td>0.13 <b>(+37.85%)</b></td><td>0.04 <b>(-51.27%)</b></td><td>256.20 <b>(-27.46%)</b></td><td>191.56 (-3.33%)</td><td>192.80 (+17.85%)</td><td>148.90 <b>(+25.76%)</b></td><td>43.58 <b>(-55.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>353.20 (n/a)</td><td>198.16 (n/a)</td><td>163.60 (n/a)</td><td>118.40 (n/a)</td><td>97.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (-1.18%)</td><td>0.19 (-5.29%)</td><td>0.18 (-14.17%)</td><td>0.13 (-13.60%)</td><td>0.04 <b>(+36.74%)</b></td><td>248.70 (+15.73%)</td><td>180.06 (+7.95%)</td><td>181.70 (+16.55%)</td><td>141.40 (+1.22%)</td><td>43.85 <b>(+51.42%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>214.90 (n/a)</td><td>166.80 (n/a)</td><td>155.90 (n/a)</td><td>139.70 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (+4.91%)</td><td>0.18 (-0.67%)</td><td>0.18 (-4.28%)</td><td>0.14 (-1.16%)</td><td>0.03 (+8.48%)</td><td>235.90 (+1.20%)</td><td>184.10 (+0.99%)</td><td>180.00 (+4.47%)</td><td>146.40 (-4.69%)</td><td>33.88 (+5.33%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>233.10 (n/a)</td><td>182.30 (n/a)</td><td>172.30 (n/a)</td><td>153.60 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (-3.11%)</td><td>0.17 <b>(-20.21%)</b></td><td>0.16 <b>(-28.44%)</b></td><td>0.14 (-9.03%)</td><td>0.04 (+10.55%)</td><td>234.00 (+9.91%)</td><td>194.96 <b>(+26.30%)</b></td><td>199.60 <b>(+39.78%)</b></td><td>132.70 (+3.19%)</td><td>38.34 (+14.94%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.90 (n/a)</td><td>154.36 (n/a)</td><td>142.80 (n/a)</td><td>128.60 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 <b>(+22.18%)</b></td><td>0.20 (+4.46%)</td><td>0.20 (+3.72%)</td><td>0.14 (-15.50%)</td><td>0.05 <b>(+121.47%)</b></td><td>241.50 (+18.38%)</td><td>174.40 (+0.00%)</td><td>166.90 (-3.58%)</td><td>124.10 (-18.19%)</td><td>46.77 <b>(+116.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>174.40 (n/a)</td><td>173.10 (n/a)</td><td>151.70 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (-0.19%)</td><td>0.16 (-0.18%)</td><td>0.16 (-0.09%)</td><td>0.16 (-0.24%)</td><td>0.00 <b>(+36.04%)</b></td><td>52481.00 (+0.24%)</td><td>52408.44 (+0.18%)</td><td>52378.40 (+0.09%)</td><td>52354.10 (+0.19%)</td><td>56.41 <b>(+36.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52355.70 (n/a)</td><td>52312.58 (n/a)</td><td>52332.90 (n/a)</td><td>52254.70 (n/a)</td><td>41.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52508.60 (n/a)</td><td>52389.18 (n/a)</td><td>52374.50 (n/a)</td><td>52309.00 (n/a)</td><td>86.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>414225.90 (n/a)</td><td>414108.12 (n/a)</td><td>414134.70 (n/a)</td><td>413926.60 (n/a)</td><td>114.86 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (+6.83%)</td><td>0.20 (+6.09%)</td><td>0.20 (+0.57%)</td><td>0.17 <b>(+20.08%)</b></td><td>0.02 (-16.31%)</td><td>141.30 (-16.74%)</td><td>125.84 (-6.52%)</td><td>125.00 (-0.56%)</td><td>108.40 (-6.39%)</td><td>14.03 <b>(-34.97%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>169.70 (n/a)</td><td>134.62 (n/a)</td><td>125.70 (n/a)</td><td>115.80 (n/a)</td><td>21.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.45 (+14.71%)</td><td>0.35 (+5.18%)</td><td>0.36 (+7.56%)</td><td>0.16 <b>(-37.18%)</b></td><td>0.12 <b>(+92.08%)</b></td><td>303.20 <b>(+59.16%)</b></td><td>162.70 (+6.21%)</td><td>136.10 (-7.04%)</td><td>109.50 (-12.82%)</td><td>80.81 <b>(+174.60%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>190.50 (n/a)</td><td>153.18 (n/a)</td><td>146.40 (n/a)</td><td>125.60 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>13.72 (+2.06%)</td><td>13.15 (+0.49%)</td><td>13.20 (-1.71%)</td><td>12.47 (+0.01%)</td><td>0.46 (-4.91%)</td><td>840.80 (-0.01%)</td><td>798.48 (-0.50%)</td><td>794.60 (+1.74%)</td><td>764.40 (-2.03%)</td><td>28.41 (-6.13%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.44 (n/a)</td><td>13.08 (n/a)</td><td>13.43 (n/a)</td><td>12.47 (n/a)</td><td>0.49 (n/a)</td><td>840.90 (n/a)</td><td>802.48 (n/a)</td><td>781.00 (n/a)</td><td>780.20 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.38 (+17.48%)</td><td>0.28 (-8.55%)</td><td>0.27 (-15.77%)</td><td>0.23 <b>(-21.03%)</b></td><td>0.06 <b>(+184.49%)</b></td><td>182.00 <b>(+26.56%)</b></td><td>149.82 (+12.36%)</td><td>152.70 (+18.74%)</td><td>106.50 (-14.87%)</td><td>27.21 <b>(+190.48%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.02 (n/a)</td><td>143.80 (n/a)</td><td>133.34 (n/a)</td><td>128.60 (n/a)</td><td>125.10 (n/a)</td><td>9.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (-7.12%)</td><td>0.03 (-7.71%)</td><td>0.04 (+0.10%)</td><td>0.03 (-18.99%)</td><td>0.01 (+19.11%)</td><td>200.50 <b>(+23.46%)</b></td><td>155.90 (+9.45%)</td><td>145.80 (-0.14%)</td><td>130.30 (+7.69%)</td><td>26.69 <b>(+64.19%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>162.40 (n/a)</td><td>142.44 (n/a)</td><td>146.00 (n/a)</td><td>121.00 (n/a)</td><td>16.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-9.42%)</td><td>0.03 (-1.52%)</td><td>0.03 (+3.64%)</td><td>0.02 (-17.23%)</td><td>0.00 (+4.55%)</td><td>201.30 <b>(+20.83%)</b></td><td>153.64 (+2.49%)</td><td>149.70 (-3.54%)</td><td>124.60 (+10.36%)</td><td>30.52 <b>(+43.54%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.60 (n/a)</td><td>149.90 (n/a)</td><td>155.20 (n/a)</td><td>112.90 (n/a)</td><td>21.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (+4.36%)</td><td>0.05 <b>(+20.38%)</b></td><td>0.04 <b>(+26.91%)</b></td><td>0.03 <b>(+25.97%)</b></td><td>0.01 (-5.17%)</td><td>178.90 <b>(-20.63%)</b></td><td>140.86 (-17.99%)</td><td>136.70 <b>(-21.21%)</b></td><td>112.70 (-4.17%)</td><td>28.28 <b>(-27.09%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>225.40 (n/a)</td><td>171.76 (n/a)</td><td>173.50 (n/a)</td><td>117.60 (n/a)</td><td>38.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-19.65%)</td><td>0.03 (-0.80%)</td><td>0.03 (+8.03%)</td><td>0.02 (-9.47%)</td><td>0.00 <b>(-40.76%)</b></td><td>203.70 (+10.47%)</td><td>161.48 (-0.86%)</td><td>159.40 (-7.43%)</td><td>138.70 <b>(+24.51%)</b></td><td>25.26 (-14.14%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>184.40 (n/a)</td><td>162.88 (n/a)</td><td>172.20 (n/a)</td><td>111.40 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (-17.57%)</td><td>0.03 (-9.34%)</td><td>0.03 (-7.00%)</td><td>0.03 (+1.15%)</td><td>0.00 <b>(-37.42%)</b></td><td>179.30 (-1.10%)</td><td>156.82 (+8.68%)</td><td>157.50 (+7.51%)</td><td>129.60 <b>(+21.23%)</b></td><td>20.63 <b>(-22.88%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>144.30 (n/a)</td><td>146.50 (n/a)</td><td>106.90 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-9.68%)</td><td>0.03 (-2.09%)</td><td>0.03 (+0.79%)</td><td>0.02 (+1.78%)</td><td>0.00 <b>(-32.40%)</b></td><td>209.90 (-1.78%)</td><td>165.12 (+0.57%)</td><td>155.00 (-0.77%)</td><td>145.70 (+10.71%)</td><td>25.76 <b>(-23.98%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.70 (n/a)</td><td>164.18 (n/a)</td><td>156.20 (n/a)</td><td>131.60 (n/a)</td><td>33.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (+15.26%)</td><td>0.03 (+17.79%)</td><td>0.03 <b>(+21.49%)</b></td><td>0.03 <b>(+24.23%)</b></td><td>0.00 (+0.85%)</td><td>175.50 (-19.50%)</td><td>152.30 (-15.45%)</td><td>149.40 (-17.69%)</td><td>133.40 (-13.26%)</td><td>17.13 <b>(-29.90%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.00 (n/a)</td><td>180.14 (n/a)</td><td>181.50 (n/a)</td><td>153.80 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+2.36%)</td><td>0.02 (+2.33%)</td><td>0.02 (+1.85%)</td><td>0.02 (+4.35%)</td><td>0.00 (-8.68%)</td><td>200.80 (-4.15%)</td><td>168.06 (-2.68%)</td><td>169.30 (-1.80%)</td><td>142.00 (-2.27%)</td><td>23.83 (-13.42%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.50 (n/a)</td><td>172.68 (n/a)</td><td>172.40 (n/a)</td><td>145.30 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-15.77%)</td><td>0.03 (+3.18%)</td><td>0.03 (+10.87%)</td><td>0.03 <b>(+23.62%)</b></td><td>0.00 <b>(-70.69%)</b></td><td>169.40 (-19.10%)</td><td>155.92 (-6.04%)</td><td>155.40 (-9.76%)</td><td>144.60 (+18.72%)</td><td>9.51 <b>(-71.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>165.94 (n/a)</td><td>172.20 (n/a)</td><td>121.80 (n/a)</td><td>33.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-5.45%)</td><td>0.02 (-1.04%)</td><td>0.03 (+3.87%)</td><td>0.02 (+9.42%)</td><td>0.00 <b>(-34.91%)</b></td><td>186.50 (-8.58%)</td><td>166.38 (+0.04%)</td><td>162.50 (-3.73%)</td><td>146.50 (+5.78%)</td><td>15.83 <b>(-36.72%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.00 (n/a)</td><td>166.32 (n/a)</td><td>168.80 (n/a)</td><td>138.50 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 <b>(+21.78%)</b></td><td>0.03 (+8.77%)</td><td>0.03 (+7.08%)</td><td>0.02 (-2.27%)</td><td>0.01 <b>(+74.55%)</b></td><td>235.00 (+2.35%)</td><td>174.12 (-5.25%)</td><td>169.40 (-6.62%)</td><td>123.70 (-17.92%)</td><td>43.81 <b>(+45.81%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.60 (n/a)</td><td>183.76 (n/a)</td><td>181.40 (n/a)</td><td>150.70 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+3.52%)</td><td>0.02 (-2.59%)</td><td>0.03 (+7.67%)</td><td>0.01 <b>(-28.84%)</b></td><td>0.01 <b>(+90.56%)</b></td><td>315.00 <b>(+40.50%)</b></td><td>194.64 (+8.68%)</td><td>159.60 (-7.16%)</td><td>154.20 (-3.38%)</td><td>68.36 <b>(+160.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.20 (n/a)</td><td>179.10 (n/a)</td><td>171.90 (n/a)</td><td>159.60 (n/a)</td><td>26.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 <b>(+27.36%)</b></td><td>0.03 (+12.76%)</td><td>0.02 (+14.26%)</td><td>0.02 (+0.16%)</td><td>0.01 <b>(+83.35%)</b></td><td>215.10 (-0.19%)</td><td>178.98 (-8.93%)</td><td>181.30 (-12.46%)</td><td>118.60 <b>(-21.46%)</b></td><td>37.50 <b>(+41.59%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.50 (n/a)</td><td>196.52 (n/a)</td><td>207.10 (n/a)</td><td>151.00 (n/a)</td><td>26.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+6.35%)</td><td>0.03 (+3.73%)</td><td>0.03 (+9.88%)</td><td>0.02 (-6.11%)</td><td>0.01 <b>(+24.02%)</b></td><td>222.70 (+6.50%)</td><td>166.16 (-2.40%)</td><td>157.70 (-9.00%)</td><td>124.10 (-5.98%)</td><td>35.77 <b>(+27.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.10 (n/a)</td><td>170.24 (n/a)</td><td>173.30 (n/a)</td><td>132.00 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (-15.46%)</td><td>0.02 (+8.21%)</td><td>0.02 <b>(+21.99%)</b></td><td>0.02 <b>(+39.55%)</b></td><td>0.00 <b>(-67.93%)</b></td><td>223.50 <b>(-28.34%)</b></td><td>196.50 (-14.97%)</td><td>187.80 (-18.03%)</td><td>178.20 (+18.25%)</td><td>20.40 <b>(-73.06%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>311.90 (n/a)</td><td>231.10 (n/a)</td><td>229.10 (n/a)</td><td>150.70 (n/a)</td><td>75.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (+0.02%)</td><td>0.02 (+9.05%)</td><td>0.02 (+4.14%)</td><td>0.01 (+5.54%)</td><td>0.00 <b>(-22.41%)</b></td><td>332.70 (-5.24%)</td><td>229.22 (-10.86%)</td><td>204.50 (-3.99%)</td><td>188.20 (-0.05%)</td><td>58.73 <b>(-24.78%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>351.10 (n/a)</td><td>257.16 (n/a)</td><td>213.00 (n/a)</td><td>188.30 (n/a)</td><td>78.08 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (+13.94%)</td><td>0.05 (+2.90%)</td><td>0.05 (+0.22%)</td><td>0.04 (-7.85%)</td><td>0.01 <b>(+113.07%)</b></td><td>197.20 (+8.53%)</td><td>165.34 (-1.36%)</td><td>169.90 (-0.23%)</td><td>134.90 (-12.23%)</td><td>25.58 <b>(+102.79%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>181.70 (n/a)</td><td>167.62 (n/a)</td><td>170.30 (n/a)</td><td>153.70 (n/a)</td><td>12.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (-18.27%)</td><td>0.08 (-2.59%)</td><td>0.08 (+7.62%)</td><td>0.06 (-6.42%)</td><td>0.01 <b>(-37.54%)</b></td><td>190.40 (+6.85%)</td><td>158.00 (+1.82%)</td><td>149.90 (-7.07%)</td><td>148.00 <b>(+22.31%)</b></td><td>18.17 (-15.28%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>178.20 (n/a)</td><td>155.18 (n/a)</td><td>161.30 (n/a)</td><td>121.00 (n/a)</td><td>21.45 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (+17.30%)</td><td>0.05 (+15.32%)</td><td>0.05 (+16.36%)</td><td>0.05 (+10.83%)</td><td>0.01 <b>(+62.38%)</b></td><td>179.90 (-9.78%)</td><td>157.16 (-12.59%)</td><td>154.70 (-14.06%)</td><td>131.70 (-14.70%)</td><td>21.43 <b>(+28.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.40 (n/a)</td><td>179.80 (n/a)</td><td>180.00 (n/a)</td><td>154.40 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (+5.00%)</td><td>0.07 (+14.59%)</td><td>0.07 <b>(+29.17%)</b></td><td>0.06 (+12.77%)</td><td>0.01 (-9.02%)</td><td>177.50 (-11.34%)</td><td>149.26 (-13.34%)</td><td>136.70 <b>(-22.55%)</b></td><td>132.20 (-4.76%)</td><td>21.30 <b>(-24.73%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>172.24 (n/a)</td><td>176.50 (n/a)</td><td>138.80 (n/a)</td><td>28.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 <b>(+28.29%)</b></td><td>0.06 (+19.13%)</td><td>0.05 (+14.67%)</td><td>0.04 (+5.04%)</td><td>0.01 <b>(+90.80%)</b></td><td>189.90 (-4.81%)</td><td>151.36 (-14.27%)</td><td>157.60 (-12.83%)</td><td>115.90 <b>(-22.06%)</b></td><td>30.79 <b>(+38.05%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>176.56 (n/a)</td><td>180.80 (n/a)</td><td>148.70 (n/a)</td><td>22.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (-2.20%)</td><td>0.06 (+9.34%)</td><td>0.07 <b>(+21.78%)</b></td><td>0.06 (+8.95%)</td><td>0.01 <b>(-21.66%)</b></td><td>181.20 (-8.25%)</td><td>160.22 (-9.07%)</td><td>152.90 (-17.88%)</td><td>146.60 (+2.23%)</td><td>16.15 <b>(-26.85%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.50 (n/a)</td><td>176.20 (n/a)</td><td>186.20 (n/a)</td><td>143.40 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 <b>(+39.27%)</b></td><td>0.06 <b>(+21.27%)</b></td><td>0.05 (+7.41%)</td><td>0.05 <b>(+26.29%)</b></td><td>0.01 <b>(+67.05%)</b></td><td>165.40 <b>(-20.82%)</b></td><td>148.36 (-17.07%)</td><td>154.40 (-6.93%)</td><td>116.30 <b>(-28.17%)</b></td><td>19.44 (-6.16%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>178.90 (n/a)</td><td>165.90 (n/a)</td><td>161.90 (n/a)</td><td>20.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (+5.92%)</td><td>0.05 (+8.44%)</td><td>0.05 (+12.40%)</td><td>0.04 (+4.02%)</td><td>0.01 (+10.59%)</td><td>238.30 (-3.83%)</td><td>180.44 (-7.37%)</td><td>170.80 (-11.00%)</td><td>135.60 (-5.57%)</td><td>38.25 (+3.08%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>247.80 (n/a)</td><td>194.80 (n/a)</td><td>191.90 (n/a)</td><td>143.60 (n/a)</td><td>37.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 <b>(+34.69%)</b></td><td>0.06 <b>(+25.62%)</b></td><td>0.05 (+18.27%)</td><td>0.05 (+13.20%)</td><td>0.01 <b>(+154.54%)</b></td><td>181.90 (-11.66%)</td><td>149.72 (-18.22%)</td><td>150.10 (-15.44%)</td><td>117.60 <b>(-25.76%)</b></td><td>31.09 <b>(+65.17%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.90 (n/a)</td><td>183.08 (n/a)</td><td>177.50 (n/a)</td><td>158.40 (n/a)</td><td>18.83 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (-13.71%)</td><td>0.05 (+1.58%)</td><td>0.05 (-4.00%)</td><td>0.05 <b>(+51.08%)</b></td><td>0.01 <b>(-59.57%)</b></td><td>201.40 <b>(-33.82%)</b></td><td>173.98 (-8.36%)</td><td>176.20 (+4.14%)</td><td>146.60 (+15.89%)</td><td>19.59 <b>(-70.92%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>304.30 (n/a)</td><td>189.86 (n/a)</td><td>169.20 (n/a)</td><td>126.50 (n/a)</td><td>67.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (+19.02%)</td><td>0.05 <b>(+22.45%)</b></td><td>0.05 <b>(+29.35%)</b></td><td>0.04 <b>(+45.76%)</b></td><td>0.01 (+0.65%)</td><td>212.60 <b>(-31.38%)</b></td><td>169.48 <b>(-20.26%)</b></td><td>161.20 <b>(-22.69%)</b></td><td>124.30 (-16.01%)</td><td>34.34 <b>(-43.03%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>309.80 (n/a)</td><td>212.54 (n/a)</td><td>208.50 (n/a)</td><td>148.00 (n/a)</td><td>60.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (+6.69%)</td><td>0.05 (+3.41%)</td><td>0.05 (-1.02%)</td><td>0.04 (+4.88%)</td><td>0.01 (+7.07%)</td><td>200.10 (-4.62%)</td><td>173.76 (-3.26%)</td><td>182.20 (+1.05%)</td><td>136.70 (-6.24%)</td><td>24.82 (-5.89%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>179.62 (n/a)</td><td>180.30 (n/a)</td><td>145.80 (n/a)</td><td>26.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (-7.13%)</td><td>0.05 (+5.18%)</td><td>0.04 (+12.34%)</td><td>0.04 (+4.54%)</td><td>0.01 <b>(-22.39%)</b></td><td>227.80 (-4.37%)</td><td>180.34 (-6.84%)</td><td>184.00 (-10.98%)</td><td>137.10 (+7.70%)</td><td>36.27 <b>(-21.08%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.20 (n/a)</td><td>193.58 (n/a)</td><td>206.70 (n/a)</td><td>127.30 (n/a)</td><td>45.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 <b>(-21.68%)</b></td><td>0.05 (-0.71%)</td><td>0.05 (+10.45%)</td><td>0.05 (+16.72%)</td><td>0.00 <b>(-76.24%)</b></td><td>190.50 (-14.34%)</td><td>177.68 (-2.81%)</td><td>174.90 (-9.47%)</td><td>166.00 <b>(+27.69%)</b></td><td>9.83 <b>(-73.85%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.40 (n/a)</td><td>182.82 (n/a)</td><td>193.20 (n/a)</td><td>130.00 (n/a)</td><td>37.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (-5.87%)</td><td>0.04 (+6.97%)</td><td>0.04 (+12.89%)</td><td>0.04 (+15.91%)</td><td>0.00 <b>(-59.99%)</b></td><td>209.60 (-13.71%)</td><td>197.14 (-7.50%)</td><td>197.00 (-11.42%)</td><td>186.60 (+6.20%)</td><td>9.58 <b>(-62.92%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.90 (n/a)</td><td>213.12 (n/a)</td><td>222.40 (n/a)</td><td>175.70 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (+12.84%)</td><td>0.10 (+9.80%)</td><td>0.11 <b>(+27.74%)</b></td><td>0.05 <b>(-34.49%)</b></td><td>0.03 <b>(+159.30%)</b></td><td>313.00 <b>(+52.61%)</b></td><td>183.56 (+0.54%)</td><td>142.90 <b>(-21.70%)</b></td><td>130.50 (-11.35%)</td><td>77.85 <b>(+245.99%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>182.58 (n/a)</td><td>182.50 (n/a)</td><td>147.20 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (-15.54%)</td><td>0.16 (-1.66%)</td><td>0.18 (+10.87%)</td><td>0.13 (-4.78%)</td><td>0.02 <b>(-26.59%)</b></td><td>186.80 (+5.00%)</td><td>151.92 (+1.08%)</td><td>140.20 (-9.84%)</td><td>138.50 (+18.38%)</td><td>20.61 (-6.69%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>177.90 (n/a)</td><td>150.30 (n/a)</td><td>155.50 (n/a)</td><td>117.00 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (-7.20%)</td><td>0.11 (+4.69%)</td><td>0.11 (+11.01%)</td><td>0.11 (+16.86%)</td><td>0.01 <b>(-67.48%)</b></td><td>153.00 (-14.43%)</td><td>146.86 (-5.86%)</td><td>150.80 (-9.92%)</td><td>138.60 (+7.78%)</td><td>6.52 <b>(-69.77%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>178.80 (n/a)</td><td>156.00 (n/a)</td><td>167.40 (n/a)</td><td>128.60 (n/a)</td><td>21.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 <b>(-28.35%)</b></td><td>0.11 (-19.30%)</td><td>0.11 (-18.52%)</td><td>0.08 <b>(-29.69%)</b></td><td>0.03 <b>(-31.38%)</b></td><td>260.10 <b>(+42.21%)</b></td><td>188.30 <b>(+23.69%)</b></td><td>191.60 <b>(+22.74%)</b></td><td>138.90 <b>(+39.60%)</b></td><td>46.09 <b>(+40.81%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>182.90 (n/a)</td><td>152.24 (n/a)</td><td>156.10 (n/a)</td><td>99.50 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (+13.99%)</td><td>0.10 (+6.45%)</td><td>0.11 <b>(+23.77%)</b></td><td>0.05 <b>(-43.27%)</b></td><td>0.03 <b>(+204.52%)</b></td><td>326.20 <b>(+76.32%)</b></td><td>179.70 (+5.31%)</td><td>146.30 (-19.22%)</td><td>126.60 (-12.27%)</td><td>84.05 <b>(+374.12%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>170.64 (n/a)</td><td>181.10 (n/a)</td><td>144.30 (n/a)</td><td>17.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 <b>(+25.33%)</b></td><td>0.16 (+10.40%)</td><td>0.15 (+2.55%)</td><td>0.12 (+7.25%)</td><td>0.03 <b>(+53.07%)</b></td><td>172.00 (-6.78%)</td><td>136.08 (-8.00%)</td><td>135.40 (-2.45%)</td><td>98.40 <b>(-20.19%)</b></td><td>28.57 (+13.01%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>184.50 (n/a)</td><td>147.92 (n/a)</td><td>138.80 (n/a)</td><td>123.30 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (+12.69%)</td><td>0.10 (+16.63%)</td><td>0.09 (+6.66%)</td><td>0.08 <b>(+39.83%)</b></td><td>0.02 (-11.89%)</td><td>194.60 <b>(-28.48%)</b></td><td>166.54 (-16.19%)</td><td>172.70 (-6.24%)</td><td>132.40 (-11.26%)</td><td>27.40 <b>(-44.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>272.10 (n/a)</td><td>198.72 (n/a)</td><td>184.20 (n/a)</td><td>149.20 (n/a)</td><td>49.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (+12.35%)</td><td>0.14 (+7.64%)</td><td>0.12 (+12.12%)</td><td>0.09 (-5.56%)</td><td>0.04 (+13.31%)</td><td>205.90 (+5.92%)</td><td>144.84 (-6.18%)</td><td>149.20 (-10.82%)</td><td>96.40 (-10.99%)</td><td>41.19 (+7.07%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>194.40 (n/a)</td><td>154.38 (n/a)</td><td>167.30 (n/a)</td><td>108.30 (n/a)</td><td>38.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (+10.74%)</td><td>0.11 <b>(+20.16%)</b></td><td>0.11 (+10.63%)</td><td>0.10 <b>(+51.69%)</b></td><td>0.01 <b>(-34.28%)</b></td><td>156.10 <b>(-34.05%)</b></td><td>144.88 (-18.63%)</td><td>153.80 (-9.58%)</td><td>127.60 (-9.70%)</td><td>14.13 <b>(-61.37%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.70 (n/a)</td><td>178.04 (n/a)</td><td>170.10 (n/a)</td><td>141.30 (n/a)</td><td>36.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (-10.51%)</td><td>0.12 (-8.20%)</td><td>0.12 (-7.47%)</td><td>0.09 (-0.91%)</td><td>0.02 <b>(-28.27%)</b></td><td>206.90 (+0.93%)</td><td>157.08 (+6.93%)</td><td>150.70 (+8.11%)</td><td>125.50 (+11.75%)</td><td>31.02 (-17.03%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>205.00 (n/a)</td><td>146.90 (n/a)</td><td>139.40 (n/a)</td><td>112.30 (n/a)</td><td>37.38 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (-4.11%)</td><td>0.09 (-6.79%)</td><td>0.10 (-1.79%)</td><td>0.07 (-12.11%)</td><td>0.02 (+16.94%)</td><td>236.20 (+13.78%)</td><td>179.36 (+8.85%)</td><td>166.60 (+1.83%)</td><td>135.60 (+4.23%)</td><td>39.87 <b>(+39.78%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.60 (n/a)</td><td>164.78 (n/a)</td><td>163.60 (n/a)</td><td>130.10 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 <b>(-32.56%)</b></td><td>0.09 (-4.63%)</td><td>0.09 (-3.36%)</td><td>0.09 <b>(+71.92%)</b></td><td>0.01 <b>(-78.81%)</b></td><td>202.80 <b>(-41.84%)</b></td><td>184.42 (-8.18%)</td><td>186.20 (+3.44%)</td><td>164.30 <b>(+48.29%)</b></td><td>15.86 <b>(-82.32%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>348.70 (n/a)</td><td>200.86 (n/a)</td><td>180.00 (n/a)</td><td>110.80 (n/a)</td><td>89.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 <b>(+50.44%)</b></td><td>0.11 <b>(+22.59%)</b></td><td>0.10 <b>(+24.39%)</b></td><td>0.07 (+5.14%)</td><td>0.03 <b>(+104.68%)</b></td><td>221.50 (-4.89%)</td><td>159.46 (-14.71%)</td><td>157.20 (-19.59%)</td><td>99.30 <b>(-33.53%)</b></td><td>46.15 <b>(+31.60%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>186.96 (n/a)</td><td>195.50 (n/a)</td><td>149.40 (n/a)</td><td>35.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (-7.34%)</td><td>0.09 (-4.18%)</td><td>0.09 (-4.89%)</td><td>0.08 (-9.97%)</td><td>0.01 (+6.77%)</td><td>224.70 (+11.07%)</td><td>192.04 (+4.57%)</td><td>187.80 (+5.15%)</td><td>177.50 (+7.90%)</td><td>19.12 <b>(+28.66%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>183.64 (n/a)</td><td>178.60 (n/a)</td><td>164.50 (n/a)</td><td>14.86 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (+13.46%)</td><td>0.08 (+8.90%)</td><td>0.08 (+5.40%)</td><td>0.07 <b>(+54.44%)</b></td><td>0.02 <b>(-23.81%)</b></td><td>224.80 <b>(-35.23%)</b></td><td>197.78 (-12.11%)</td><td>206.70 (-5.10%)</td><td>149.10 (-11.83%)</td><td>31.30 <b>(-56.70%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>347.10 (n/a)</td><td>225.02 (n/a)</td><td>217.80 (n/a)</td><td>169.10 (n/a)</td><td>72.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 <b>(+29.81%)</b></td><td>0.21 (+7.45%)</td><td>0.20 (+7.71%)</td><td>0.16 (-6.25%)</td><td>0.05 <b>(+155.38%)</b></td><td>199.30 (+6.63%)</td><td>165.54 (-3.79%)</td><td>164.90 (-7.20%)</td><td>111.70 <b>(-23.02%)</b></td><td>34.27 <b>(+108.63%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>172.06 (n/a)</td><td>177.70 (n/a)</td><td>145.10 (n/a)</td><td>16.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.30 (+15.80%)</td><td>0.23 (+15.87%)</td><td>0.21 (+11.17%)</td><td>0.19 <b>(+25.87%)</b></td><td>0.05 (+14.92%)</td><td>175.00 <b>(-20.56%)</b></td><td>146.58 (-13.93%)</td><td>156.10 (-10.03%)</td><td>108.90 (-13.64%)</td><td>26.96 <b>(-21.17%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>220.30 (n/a)</td><td>170.30 (n/a)</td><td>173.50 (n/a)</td><td>126.10 (n/a)</td><td>34.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (-13.15%)</td><td>0.22 (-15.41%)</td><td>0.23 (-19.64%)</td><td>0.16 (-19.93%)</td><td>0.04 (-13.19%)</td><td>261.00 <b>(+24.88%)</b></td><td>193.50 (+18.55%)</td><td>181.20 <b>(+24.45%)</b></td><td>155.90 (+15.14%)</td><td>40.88 <b>(+28.22%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>209.00 (n/a)</td><td>163.22 (n/a)</td><td>145.60 (n/a)</td><td>135.40 (n/a)</td><td>31.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.28 (-11.72%)</td><td>0.21 (-2.26%)</td><td>0.23 <b>(+22.68%)</b></td><td>0.15 (-14.44%)</td><td>0.05 (-5.60%)</td><td>215.30 (+16.88%)</td><td>166.10 (+3.55%)</td><td>142.60 (-18.51%)</td><td>117.80 (+13.27%)</td><td>44.67 <b>(+35.90%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>184.20 (n/a)</td><td>160.40 (n/a)</td><td>175.00 (n/a)</td><td>104.00 (n/a)</td><td>32.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.28 (-12.12%)</td><td>0.22 (-8.21%)</td><td>0.22 (+4.56%)</td><td>0.18 (-7.94%)</td><td>0.04 <b>(-30.30%)</b></td><td>221.40 (+8.64%)</td><td>186.24 (+7.44%)</td><td>186.10 (-4.37%)</td><td>148.00 (+13.85%)</td><td>29.48 (-14.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>203.80 (n/a)</td><td>173.34 (n/a)</td><td>194.60 (n/a)</td><td>130.00 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.31 (+18.77%)</td><td>0.25 <b>(+42.14%)</b></td><td>0.25 <b>(+64.98%)</b></td><td>0.19 <b>(+71.58%)</b></td><td>0.04 <b>(-27.98%)</b></td><td>170.50 <b>(-41.71%)</b></td><td>132.06 <b>(-34.25%)</b></td><td>130.20 <b>(-39.39%)</b></td><td>104.70 (-15.77%)</td><td>24.61 <b>(-63.24%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>292.50 (n/a)</td><td>200.84 (n/a)</td><td>214.80 (n/a)</td><td>124.30 (n/a)</td><td>66.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (-1.69%)</td><td>0.22 (-3.73%)</td><td>0.23 (+8.05%)</td><td>0.14 <b>(-32.90%)</b></td><td>0.05 <b>(+89.76%)</b></td><td>267.50 <b>(+49.03%)</b></td><td>180.36 (+8.29%)</td><td>158.50 (-7.42%)</td><td>140.90 (+1.73%)</td><td>50.76 <b>(+200.59%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>179.50 (n/a)</td><td>166.56 (n/a)</td><td>171.20 (n/a)</td><td>138.50 (n/a)</td><td>16.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 (+6.91%)</td><td>0.21 (+5.17%)</td><td>0.22 (+6.65%)</td><td>0.16 (-0.46%)</td><td>0.04 <b>(+21.50%)</b></td><td>210.10 (+0.48%)</td><td>161.46 (-4.17%)</td><td>146.10 (-6.23%)</td><td>135.10 (-6.51%)</td><td>31.94 (+14.31%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>209.10 (n/a)</td><td>168.48 (n/a)</td><td>155.80 (n/a)</td><td>144.50 (n/a)</td><td>27.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.27 (-3.86%)</td><td>0.23 (-5.65%)</td><td>0.21 (-12.07%)</td><td>0.19 (-11.91%)</td><td>0.04 (+19.03%)</td><td>198.60 (+13.49%)</td><td>164.98 (+6.78%)</td><td>173.00 (+13.74%)</td><td>134.10 (+3.95%)</td><td>25.60 <b>(+37.70%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>175.00 (n/a)</td><td>154.50 (n/a)</td><td>152.10 (n/a)</td><td>129.00 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 (-8.71%)</td><td>0.19 (-0.08%)</td><td>0.19 (+13.47%)</td><td>0.15 (+10.52%)</td><td>0.04 <b>(-28.65%)</b></td><td>216.10 (-9.51%)</td><td>179.50 (-2.42%)</td><td>172.10 (-11.83%)</td><td>134.40 (+9.54%)</td><td>32.86 <b>(-27.22%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>238.80 (n/a)</td><td>183.96 (n/a)</td><td>195.20 (n/a)</td><td>122.70 (n/a)</td><td>45.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 <b>(+25.98%)</b></td><td>0.19 (+17.42%)</td><td>0.18 (+6.94%)</td><td>0.16 <b>(+60.26%)</b></td><td>0.04 (-9.64%)</td><td>224.00 <b>(-37.60%)</b></td><td>188.34 (-18.06%)</td><td>188.60 (-6.49%)</td><td>141.00 <b>(-20.65%)</b></td><td>31.10 <b>(-57.99%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>359.00 (n/a)</td><td>229.84 (n/a)</td><td>201.70 (n/a)</td><td>177.70 (n/a)</td><td>74.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 <b>(+24.98%)</b></td><td>0.19 (-3.66%)</td><td>0.17 (-15.23%)</td><td>0.15 (-3.10%)</td><td>0.06 <b>(+103.24%)</b></td><td>218.80 (+3.21%)</td><td>182.64 (+7.88%)</td><td>197.70 (+17.96%)</td><td>111.90 (-19.96%)</td><td>41.23 <b>(+55.53%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>212.00 (n/a)</td><td>169.30 (n/a)</td><td>167.60 (n/a)</td><td>139.80 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (+1.41%)</td><td>0.18 (-0.86%)</td><td>0.19 (+3.89%)</td><td>0.12 <b>(-21.25%)</b></td><td>0.03 <b>(+26.05%)</b></td><td>286.50 <b>(+26.99%)</b></td><td>200.12 (+2.89%)</td><td>184.40 (-3.71%)</td><td>162.40 (-1.40%)</td><td>49.20 <b>(+65.88%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.60 (n/a)</td><td>194.50 (n/a)</td><td>191.50 (n/a)</td><td>164.70 (n/a)</td><td>29.66 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 <b>(+30.85%)</b></td><td>0.18 (+8.06%)</td><td>0.21 <b>(+20.22%)</b></td><td>0.09 <b>(-38.48%)</b></td><td>0.06 <b>(+245.26%)</b></td><td>385.10 <b>(+62.56%)</b></td><td>206.38 (+5.75%)</td><td>156.60 (-16.79%)</td><td>134.80 <b>(-23.58%)</b></td><td>103.62 <b>(+332.64%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>236.90 (n/a)</td><td>195.16 (n/a)</td><td>188.20 (n/a)</td><td>176.40 (n/a)</td><td>23.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.17 (+8.75%)</td><td>0.14 (+5.53%)</td><td>0.14 (+12.61%)</td><td>0.10 (+5.33%)</td><td>0.03 (+8.44%)</td><td>201.40 (-5.09%)</td><td>155.36 (-5.13%)</td><td>143.50 (-11.20%)</td><td>119.00 (-8.04%)</td><td>31.37 (-3.94%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>212.20 (n/a)</td><td>163.76 (n/a)</td><td>161.60 (n/a)</td><td>129.40 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (+3.91%)</td><td>0.13 (+1.13%)</td><td>0.12 (-6.53%)</td><td>0.08 (-0.17%)</td><td>0.03 <b>(+21.55%)</b></td><td>242.30 (+0.21%)</td><td>169.22 (+0.17%)</td><td>167.90 (+6.94%)</td><td>127.40 (-3.70%)</td><td>46.20 (+9.38%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>241.80 (n/a)</td><td>168.94 (n/a)</td><td>157.00 (n/a)</td><td>132.30 (n/a)</td><td>42.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (+16.49%)</td><td>0.12 (+8.17%)</td><td>0.11 (+8.88%)</td><td>0.10 (+19.34%)</td><td>0.02 (+13.54%)</td><td>197.80 (-16.19%)</td><td>174.84 (-7.67%)</td><td>179.00 (-8.16%)</td><td>132.80 (-14.16%)</td><td>26.64 (-17.33%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>236.00 (n/a)</td><td>189.36 (n/a)</td><td>194.90 (n/a)</td><td>154.70 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 <b>(+30.83%)</b></td><td>0.12 (-9.77%)</td><td>0.10 <b>(-32.29%)</b></td><td>0.09 (-1.06%)</td><td>0.04 <b>(+66.10%)</b></td><td>236.20 (+1.07%)</td><td>190.52 (+15.51%)</td><td>208.20 <b>(+47.66%)</b></td><td>104.90 <b>(-23.60%)</b></td><td>50.84 <b>(+22.80%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>233.70 (n/a)</td><td>164.94 (n/a)</td><td>141.00 (n/a)</td><td>137.30 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (+3.42%)</td><td>0.13 (-3.38%)</td><td>0.13 (-5.15%)</td><td>0.10 (-10.34%)</td><td>0.02 (+16.03%)</td><td>204.40 (+11.51%)</td><td>162.92 (+4.29%)</td><td>162.90 (+5.44%)</td><td>125.60 (-3.31%)</td><td>29.19 <b>(+24.07%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>183.30 (n/a)</td><td>156.22 (n/a)</td><td>154.50 (n/a)</td><td>129.90 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (-3.03%)</td><td>0.12 (-16.67%)</td><td>0.12 (-18.15%)</td><td>0.09 (-19.96%)</td><td>0.03 <b>(+35.04%)</b></td><td>228.30 <b>(+24.96%)</b></td><td>179.26 <b>(+23.10%)</b></td><td>174.70 <b>(+22.17%)</b></td><td>129.80 (+3.10%)</td><td>41.46 <b>(+78.21%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>182.70 (n/a)</td><td>145.62 (n/a)</td><td>143.00 (n/a)</td><td>125.90 (n/a)</td><td>23.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (-17.20%)</td><td>0.11 (-6.55%)</td><td>0.12 (+6.93%)</td><td>0.10 (-4.24%)</td><td>0.01 <b>(-39.76%)</b></td><td>213.00 (+4.41%)</td><td>186.56 (+5.66%)</td><td>177.10 (-6.49%)</td><td>159.40 <b>(+20.76%)</b></td><td>22.37 <b>(-21.59%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>176.56 (n/a)</td><td>189.40 (n/a)</td><td>132.00 (n/a)</td><td>28.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (-6.20%)</td><td>0.12 (-4.09%)</td><td>0.11 (-9.57%)</td><td>0.10 (+14.91%)</td><td>0.02 <b>(-24.22%)</b></td><td>214.20 (-12.96%)</td><td>179.88 (+2.12%)</td><td>179.40 (+10.54%)</td><td>139.50 (+6.57%)</td><td>30.34 <b>(-30.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>246.10 (n/a)</td><td>176.14 (n/a)</td><td>162.30 (n/a)</td><td>130.90 (n/a)</td><td>43.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 <b>(+28.01%)</b></td><td>0.15 (+4.55%)</td><td>0.14 (+0.80%)</td><td>0.11 <b>(-23.14%)</b></td><td>0.03 <b>(+545.40%)</b></td><td>232.10 <b>(+30.10%)</b></td><td>170.66 (-0.64%)</td><td>171.40 (-0.75%)</td><td>126.90 <b>(-21.86%)</b></td><td>38.92 <b>(+571.85%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.00 (n/a)</td><td>178.40 (n/a)</td><td>171.76 (n/a)</td><td>172.70 (n/a)</td><td>162.40 (n/a)</td><td>5.79 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.17 (-1.53%)</td><td>0.13 (-18.38%)</td><td>0.12 <b>(-26.30%)</b></td><td>0.11 <b>(-22.86%)</b></td><td>0.02 <b>(+75.78%)</b></td><td>220.50 <b>(+29.63%)</b></td><td>192.58 <b>(+24.49%)</b></td><td>200.80 <b>(+35.68%)</b></td><td>144.70 (+1.54%)</td><td>29.04 <b>(+123.22%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>170.10 (n/a)</td><td>154.70 (n/a)</td><td>148.00 (n/a)</td><td>142.50 (n/a)</td><td>13.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (-19.35%)</td><td>0.14 (-2.46%)</td><td>0.13 (-13.24%)</td><td>0.12 <b>(+31.13%)</b></td><td>0.02 <b>(-60.46%)</b></td><td>207.70 <b>(-23.72%)</b></td><td>183.96 (-3.50%)</td><td>191.60 (+15.28%)</td><td>155.50 <b>(+24.00%)</b></td><td>21.03 <b>(-63.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>272.30 (n/a)</td><td>190.64 (n/a)</td><td>166.20 (n/a)</td><td>125.40 (n/a)</td><td>57.54 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 <b>(+21.41%)</b></td><td>0.16 (-3.14%)</td><td>0.14 (-19.10%)</td><td>0.11 (-14.44%)</td><td>0.05 <b>(+138.19%)</b></td><td>218.40 (+16.85%)</td><td>164.58 (+10.25%)</td><td>180.50 <b>(+23.63%)</b></td><td>106.20 (-17.61%)</td><td>49.51 <b>(+120.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>149.28 (n/a)</td><td>146.00 (n/a)</td><td>128.90 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 <b>(-26.16%)</b></td><td>0.12 <b>(-21.60%)</b></td><td>0.12 <b>(-28.66%)</b></td><td>0.11 (-8.18%)</td><td>0.02 <b>(-53.78%)</b></td><td>226.90 (+8.88%)</td><td>200.40 <b>(+23.78%)</b></td><td>206.20 <b>(+40.18%)</b></td><td>162.10 <b>(+35.42%)</b></td><td>24.64 <b>(-34.80%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>208.40 (n/a)</td><td>161.90 (n/a)</td><td>147.10 (n/a)</td><td>119.70 (n/a)</td><td>37.79 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (-19.98%)</td><td>0.15 (-10.42%)</td><td>0.15 <b>(-21.52%)</b></td><td>0.13 (+2.15%)</td><td>0.02 <b>(-49.23%)</b></td><td>186.30 (-2.10%)</td><td>160.74 (+8.49%)</td><td>168.20 <b>(+27.42%)</b></td><td>138.60 <b>(+24.98%)</b></td><td>20.04 <b>(-40.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>190.30 (n/a)</td><td>148.16 (n/a)</td><td>132.00 (n/a)</td><td>110.90 (n/a)</td><td>33.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 <b>(-31.62%)</b></td><td>0.14 (-18.02%)</td><td>0.15 (-5.86%)</td><td>0.11 (+3.96%)</td><td>0.02 <b>(-50.64%)</b></td><td>220.60 (-3.79%)</td><td>184.84 (+17.31%)</td><td>164.50 (+6.20%)</td><td>157.00 <b>(+46.18%)</b></td><td>31.53 <b>(-30.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>229.30 (n/a)</td><td>157.56 (n/a)</td><td>154.90 (n/a)</td><td>107.40 (n/a)</td><td>45.23 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (-15.84%)</td><td>0.12 (+0.03%)</td><td>0.11 (+0.19%)</td><td>0.11 (+15.09%)</td><td>0.02 <b>(-47.49%)</b></td><td>230.50 (-13.08%)</td><td>203.64 (-4.47%)</td><td>214.20 (-0.19%)</td><td>156.20 (+18.78%)</td><td>28.73 <b>(-46.89%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>265.20 (n/a)</td><td>213.16 (n/a)</td><td>214.60 (n/a)</td><td>131.50 (n/a)</td><td>54.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (-13.15%)</td><td>0.11 (-14.00%)</td><td>0.10 <b>(-26.05%)</b></td><td>0.09 (-1.19%)</td><td>0.02 <b>(-31.98%)</b></td><td>210.50 (+1.20%)</td><td>174.38 (+14.42%)</td><td>179.60 <b>(+35.24%)</b></td><td>147.90 (+15.19%)</td><td>26.64 <b>(-22.18%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>208.00 (n/a)</td><td>152.40 (n/a)</td><td>132.80 (n/a)</td><td>128.40 (n/a)</td><td>34.23 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (-5.22%)</td><td>0.12 (-9.96%)</td><td>0.11 (-16.44%)</td><td>0.10 (+1.66%)</td><td>0.02 (-12.85%)</td><td>183.90 (-1.61%)</td><td>161.98 (+10.60%)</td><td>163.30 (+19.72%)</td><td>131.20 (+5.55%)</td><td>22.07 (-10.25%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>146.46 (n/a)</td><td>136.40 (n/a)</td><td>124.30 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (-9.92%)</td><td>0.11 (+2.92%)</td><td>0.11 (-1.13%)</td><td>0.10 (+14.88%)</td><td>0.01 <b>(-50.13%)</b></td><td>189.90 (-12.97%)</td><td>162.48 (-5.40%)</td><td>160.60 (+1.13%)</td><td>142.30 (+11.00%)</td><td>17.28 <b>(-51.85%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>218.20 (n/a)</td><td>171.76 (n/a)</td><td>158.80 (n/a)</td><td>128.20 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (+10.29%)</td><td>0.10 (+0.50%)</td><td>0.08 (-18.39%)</td><td>0.08 <b>(+49.13%)</b></td><td>0.03 (-0.52%)</td><td>237.00 <b>(-32.96%)</b></td><td>198.22 (-4.50%)</td><td>221.50 <b>(+22.51%)</b></td><td>124.90 (-9.30%)</td><td>47.24 <b>(-43.87%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>353.50 (n/a)</td><td>207.56 (n/a)</td><td>180.80 (n/a)</td><td>137.70 (n/a)</td><td>84.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (-13.29%)</td><td>0.11 (-1.55%)</td><td>0.12 (+3.54%)</td><td>0.10 <b>(+30.19%)</b></td><td>0.01 <b>(-64.28%)</b></td><td>175.80 <b>(-23.20%)</b></td><td>162.60 (-1.95%)</td><td>160.10 (-3.44%)</td><td>148.20 (+15.33%)</td><td>12.51 <b>(-68.13%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>228.90 (n/a)</td><td>165.84 (n/a)</td><td>165.80 (n/a)</td><td>128.50 (n/a)</td><td>39.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (+11.97%)</td><td>0.11 (-7.63%)</td><td>0.10 (-19.07%)</td><td>0.09 (-19.19%)</td><td>0.03 <b>(+97.45%)</b></td><td>216.40 <b>(+23.73%)</b></td><td>170.82 (+12.10%)</td><td>186.00 <b>(+23.59%)</b></td><td>119.60 (-10.68%)</td><td>38.86 <b>(+116.65%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>174.90 (n/a)</td><td>152.38 (n/a)</td><td>150.50 (n/a)</td><td>133.90 (n/a)</td><td>17.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (+8.10%)</td><td>0.10 (+6.22%)</td><td>0.10 (+6.49%)</td><td>0.09 (+4.56%)</td><td>0.01 <b>(+29.88%)</b></td><td>203.20 (-4.38%)</td><td>180.22 (-5.44%)</td><td>176.80 (-6.11%)</td><td>150.10 (-7.46%)</td><td>22.48 (+17.70%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>190.58 (n/a)</td><td>188.30 (n/a)</td><td>162.20 (n/a)</td><td>19.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (-3.85%)</td><td>0.09 (-10.22%)</td><td>0.09 (-14.91%)</td><td>0.09 (+0.31%)</td><td>0.01 (-11.37%)</td><td>216.40 (-0.28%)</td><td>200.90 (+11.17%)</td><td>207.70 (+17.54%)</td><td>167.80 (+4.03%)</td><td>19.06 (-11.71%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>180.72 (n/a)</td><td>176.70 (n/a)</td><td>161.30 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.72 (+19.46%)</td><td>0.57 (+3.71%)</td><td>0.53 (-4.21%)</td><td>0.45 (-5.08%)</td><td>0.12 <b>(+137.13%)</b></td><td>217.80 (+5.37%)</td><td>178.68 (-0.79%)</td><td>185.20 (+4.40%)</td><td>136.30 (-16.28%)</td><td>36.71 <b>(+108.50%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.60 (n/a)</td><td>0.55 (n/a)</td><td>0.55 (n/a)</td><td>0.48 (n/a)</td><td>0.05 (n/a)</td><td>206.70 (n/a)</td><td>180.10 (n/a)</td><td>177.40 (n/a)</td><td>162.80 (n/a)</td><td>17.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.74 (+7.44%)</td><td>0.64 (+16.12%)</td><td>0.68 <b>(+25.51%)</b></td><td>0.53 (+14.75%)</td><td>0.10 (+8.56%)</td><td>186.00 (-12.88%)</td><td>156.18 (-13.96%)</td><td>145.50 <b>(-20.36%)</b></td><td>132.20 (-6.90%)</td><td>25.95 (-11.58%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.69 (n/a)</td><td>0.55 (n/a)</td><td>0.54 (n/a)</td><td>0.46 (n/a)</td><td>0.09 (n/a)</td><td>213.50 (n/a)</td><td>181.52 (n/a)</td><td>182.70 (n/a)</td><td>142.00 (n/a)</td><td>29.35 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.80 (+5.03%)</td><td>0.57 (-5.24%)</td><td>0.53 <b>(-21.92%)</b></td><td>0.43 (-0.89%)</td><td>0.14 (-8.99%)</td><td>229.60 (+0.88%)</td><td>179.50 (+3.89%)</td><td>186.70 <b>(+28.05%)</b></td><td>122.40 (-4.75%)</td><td>38.83 (-18.85%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.76 (n/a)</td><td>0.60 (n/a)</td><td>0.67 (n/a)</td><td>0.43 (n/a)</td><td>0.15 (n/a)</td><td>227.60 (n/a)</td><td>172.78 (n/a)</td><td>145.80 (n/a)</td><td>128.50 (n/a)</td><td>47.85 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.64 (+6.00%)</td><td>0.51 (+11.85%)</td><td>0.49 (-0.14%)</td><td>0.44 <b>(+45.10%)</b></td><td>0.08 <b>(-41.36%)</b></td><td>222.20 <b>(-31.08%)</b></td><td>195.42 (-15.32%)</td><td>201.70 (+0.15%)</td><td>153.60 (-5.65%)</td><td>25.27 <b>(-63.78%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.60 (n/a)</td><td>0.46 (n/a)</td><td>0.49 (n/a)</td><td>0.30 (n/a)</td><td>0.13 (n/a)</td><td>322.40 (n/a)</td><td>230.78 (n/a)</td><td>201.40 (n/a)</td><td>162.80 (n/a)</td><td>69.75 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.63 (+5.34%)</td><td>0.49 (+2.84%)</td><td>0.48 (+4.06%)</td><td>0.39 (+7.50%)</td><td>0.10 (+9.28%)</td><td>190.90 (-6.97%)</td><td>155.76 (-2.50%)</td><td>155.20 (-3.90%)</td><td>117.90 (-5.07%)</td><td>31.64 (-1.20%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.59 (n/a)</td><td>0.48 (n/a)</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.09 (n/a)</td><td>205.20 (n/a)</td><td>159.76 (n/a)</td><td>161.50 (n/a)</td><td>124.20 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.69 <b>(+25.91%)</b></td><td>0.46 (+6.40%)</td><td>0.38 (-10.91%)</td><td>0.35 (+9.30%)</td><td>0.14 <b>(+70.82%)</b></td><td>208.10 (-8.53%)</td><td>170.78 (-3.00%)</td><td>194.20 (+12.25%)</td><td>106.60 <b>(-20.57%)</b></td><td>41.99 <b>(+22.70%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>227.50 (n/a)</td><td>176.06 (n/a)</td><td>173.00 (n/a)</td><td>134.20 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.51 (-14.12%)</td><td>0.43 (-3.99%)</td><td>0.46 (+0.82%)</td><td>0.26 (-8.13%)</td><td>0.10 (-18.54%)</td><td>286.60 (+8.85%)</td><td>181.68 (+3.38%)</td><td>158.60 (-0.81%)</td><td>145.80 (+16.45%)</td><td>59.10 (+6.89%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.59 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>263.30 (n/a)</td><td>175.74 (n/a)</td><td>159.90 (n/a)</td><td>125.20 (n/a)</td><td>55.28 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.50 (+8.70%)</td><td>0.40 (+11.40%)</td><td>0.38 (+8.62%)</td><td>0.34 <b>(+50.72%)</b></td><td>0.07 <b>(-27.21%)</b></td><td>214.40 <b>(-33.66%)</b></td><td>188.06 (-13.70%)</td><td>195.70 (-7.91%)</td><td>148.10 (-8.01%)</td><td>28.59 <b>(-55.42%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>323.20 (n/a)</td><td>217.92 (n/a)</td><td>212.50 (n/a)</td><td>161.00 (n/a)</td><td>64.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (-7.14%)</td><td>0.22 (-7.92%)</td><td>0.22 (-4.52%)</td><td>0.15 <b>(-25.40%)</b></td><td>0.04 <b>(+34.54%)</b></td><td>250.70 <b>(+34.06%)</b></td><td>176.04 (+11.38%)</td><td>168.20 (+4.73%)</td><td>139.70 (+7.71%)</td><td>43.45 <b>(+103.97%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>187.00 (n/a)</td><td>158.06 (n/a)</td><td>160.60 (n/a)</td><td>129.70 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (-5.99%)</td><td>0.20 (-0.50%)</td><td>0.21 (-1.92%)</td><td>0.18 (+7.07%)</td><td>0.02 <b>(-35.75%)</b></td><td>207.60 (-6.61%)</td><td>182.56 (-0.98%)</td><td>176.80 (+1.90%)</td><td>161.50 (+6.32%)</td><td>20.70 <b>(-36.79%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>222.30 (n/a)</td><td>184.36 (n/a)</td><td>173.50 (n/a)</td><td>151.90 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.31 <b>(+44.91%)</b></td><td>0.25 <b>(+23.61%)</b></td><td>0.26 (+19.38%)</td><td>0.20 (+9.96%)</td><td>0.05 <b>(+212.01%)</b></td><td>187.30 (-9.03%)</td><td>151.20 (-16.72%)</td><td>144.40 (-16.19%)</td><td>117.60 <b>(-30.99%)</b></td><td>31.39 <b>(+100.92%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>205.90 (n/a)</td><td>181.56 (n/a)</td><td>172.30 (n/a)</td><td>170.40 (n/a)</td><td>15.62 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 <b>(-21.20%)</b></td><td>0.20 (-13.38%)</td><td>0.19 (-11.97%)</td><td>0.18 (-7.01%)</td><td>0.02 <b>(-52.67%)</b></td><td>205.10 (+7.55%)</td><td>188.40 (+14.32%)</td><td>191.40 (+13.59%)</td><td>167.50 <b>(+26.89%)</b></td><td>13.98 <b>(-34.39%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>190.70 (n/a)</td><td>164.80 (n/a)</td><td>168.50 (n/a)</td><td>132.00 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (-19.83%)</td><td>0.21 (-13.34%)</td><td>0.22 (-6.91%)</td><td>0.15 <b>(-27.43%)</b></td><td>0.04 (-16.62%)</td><td>247.70 <b>(+37.84%)</b></td><td>180.38 (+16.19%)</td><td>169.00 (+7.37%)</td><td>140.10 <b>(+24.76%)</b></td><td>40.35 <b>(+51.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>179.70 (n/a)</td><td>155.24 (n/a)</td><td>157.40 (n/a)</td><td>112.30 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 <b>(+20.78%)</b></td><td>0.22 (+3.69%)</td><td>0.20 (+4.29%)</td><td>0.12 <b>(-29.95%)</b></td><td>0.06 <b>(+137.63%)</b></td><td>296.70 <b>(+42.71%)</b></td><td>186.14 (+3.75%)</td><td>180.80 (-4.08%)</td><td>125.50 (-17.22%)</td><td>66.76 <b>(+190.68%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>207.90 (n/a)</td><td>179.42 (n/a)</td><td>188.50 (n/a)</td><td>151.60 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (-6.79%)</td><td>0.19 (-8.48%)</td><td>0.20 (-9.46%)</td><td>0.12 <b>(-22.91%)</b></td><td>0.04 (+11.87%)</td><td>302.40 <b>(+29.73%)</b></td><td>204.38 (+11.68%)</td><td>181.60 (+10.46%)</td><td>158.50 (+7.31%)</td><td>57.07 <b>(+60.87%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>233.10 (n/a)</td><td>183.00 (n/a)</td><td>164.40 (n/a)</td><td>147.70 (n/a)</td><td>35.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 (+13.27%)</td><td>0.21 (-0.50%)</td><td>0.18 <b>(-21.28%)</b></td><td>0.17 (+17.90%)</td><td>0.05 (+17.95%)</td><td>216.50 (-15.16%)</td><td>181.20 (+0.59%)</td><td>202.10 <b>(+27.03%)</b></td><td>125.70 (-11.73%)</td><td>38.38 (-14.12%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>255.20 (n/a)</td><td>180.14 (n/a)</td><td>159.10 (n/a)</td><td>142.40 (n/a)</td><td>44.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 (+5.14%)</td><td>0.26 (+9.53%)</td><td>0.26 (+9.72%)</td><td>0.24 (+18.78%)</td><td>0.02 <b>(-30.78%)</b></td><td>168.20 (-15.82%)</td><td>157.00 (-9.29%)</td><td>155.40 (-8.86%)</td><td>140.70 (-4.87%)</td><td>10.90 <b>(-44.70%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>199.80 (n/a)</td><td>173.08 (n/a)</td><td>170.50 (n/a)</td><td>147.90 (n/a)</td><td>19.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (-3.84%)</td><td>0.23 (-0.16%)</td><td>0.23 (+5.06%)</td><td>0.20 (+5.52%)</td><td>0.02 <b>(-41.43%)</b></td><td>205.80 (-5.20%)</td><td>182.00 (-1.48%)</td><td>181.10 (-4.83%)</td><td>155.70 (+4.01%)</td><td>18.58 <b>(-42.22%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>217.10 (n/a)</td><td>184.74 (n/a)</td><td>190.30 (n/a)</td><td>149.70 (n/a)</td><td>32.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.32 (+12.90%)</td><td>0.26 (+10.03%)</td><td>0.23 (+2.05%)</td><td>0.20 (+0.01%)</td><td>0.05 <b>(+56.37%)</b></td><td>205.10 (+0.00%)</td><td>166.00 (-7.50%)</td><td>179.00 (-2.03%)</td><td>126.50 (-11.41%)</td><td>32.98 <b>(+37.39%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>205.10 (n/a)</td><td>179.46 (n/a)</td><td>182.70 (n/a)</td><td>142.80 (n/a)</td><td>24.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.34 (+10.85%)</td><td>0.26 (+0.92%)</td><td>0.28 (+13.86%)</td><td>0.19 (-16.57%)</td><td>0.06 <b>(+42.62%)</b></td><td>215.70 (+19.83%)</td><td>161.14 (+1.31%)</td><td>148.40 (-12.14%)</td><td>119.40 (-9.75%)</td><td>37.08 <b>(+56.68%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>180.00 (n/a)</td><td>159.06 (n/a)</td><td>168.90 (n/a)</td><td>132.30 (n/a)</td><td>23.67 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.30 (-3.42%)</td><td>0.26 (-2.04%)</td><td>0.26 (+3.11%)</td><td>0.20 (-5.47%)</td><td>0.04 (-8.89%)</td><td>205.00 (+5.78%)</td><td>162.18 (+1.97%)</td><td>155.10 (-3.00%)</td><td>136.00 (+3.50%)</td><td>25.66 (+3.62%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>193.80 (n/a)</td><td>159.04 (n/a)</td><td>159.90 (n/a)</td><td>131.40 (n/a)</td><td>24.76 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.31 (+3.35%)</td><td>0.24 (-5.02%)</td><td>0.23 (-4.17%)</td><td>0.16 <b>(-27.14%)</b></td><td>0.06 <b>(+84.65%)</b></td><td>249.90 <b>(+37.23%)</b></td><td>182.08 (+9.57%)</td><td>180.00 (+4.35%)</td><td>131.40 (-3.31%)</td><td>47.03 <b>(+142.30%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>182.10 (n/a)</td><td>166.18 (n/a)</td><td>172.50 (n/a)</td><td>135.90 (n/a)</td><td>19.41 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.36 (+2.82%)</td><td>0.24 (-6.19%)</td><td>0.20 (-18.68%)</td><td>0.19 (+0.92%)</td><td>0.07 (+17.14%)</td><td>210.10 (-0.90%)</td><td>180.56 (+8.02%)</td><td>200.80 <b>(+22.96%)</b></td><td>113.60 (-2.74%)</td><td>39.80 (+13.07%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>212.00 (n/a)</td><td>167.16 (n/a)</td><td>163.30 (n/a)</td><td>116.80 (n/a)</td><td>35.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 <b>(-28.12%)</b></td><td>0.20 <b>(-21.04%)</b></td><td>0.20 <b>(-22.92%)</b></td><td>0.18 (-0.51%)</td><td>0.02 <b>(-67.26%)</b></td><td>224.90 (+0.49%)</td><td>202.20 <b>(+23.17%)</b></td><td>201.30 <b>(+29.70%)</b></td><td>184.40 <b>(+39.17%)</b></td><td>15.89 <b>(-55.46%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>223.80 (n/a)</td><td>164.16 (n/a)</td><td>155.20 (n/a)</td><td>132.50 (n/a)</td><td>35.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 (+4.00%)</td><td>0.20 (-1.35%)</td><td>0.20 (-10.27%)</td><td>0.15 (-1.48%)</td><td>0.05 (+1.59%)</td><td>235.00 (+1.47%)</td><td>179.22 (+1.06%)</td><td>175.80 (+11.41%)</td><td>120.20 (-3.84%)</td><td>42.04 (-6.36%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>231.60 (n/a)</td><td>177.34 (n/a)</td><td>157.80 (n/a)</td><td>125.00 (n/a)</td><td>44.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (+2.11%)</td><td>0.20 (+4.37%)</td><td>0.20 (-1.09%)</td><td>0.15 <b>(+61.02%)</b></td><td>0.04 <b>(-31.20%)</b></td><td>237.50 <b>(-37.91%)</b></td><td>182.16 (-12.37%)</td><td>171.80 (+1.12%)</td><td>138.20 (-2.06%)</td><td>39.26 <b>(-60.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>382.50 (n/a)</td><td>207.88 (n/a)</td><td>169.90 (n/a)</td><td>141.10 (n/a)</td><td>99.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (+2.65%)</td><td>0.21 (-4.27%)</td><td>0.22 (+3.67%)</td><td>0.15 <b>(-26.21%)</b></td><td>0.04 <b>(+75.17%)</b></td><td>236.20 <b>(+35.51%)</b></td><td>170.46 (+7.40%)</td><td>157.80 (-3.55%)</td><td>136.30 (-2.57%)</td><td>39.52 <b>(+136.72%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>174.30 (n/a)</td><td>158.72 (n/a)</td><td>163.60 (n/a)</td><td>139.90 (n/a)</td><td>16.70 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.27 (+2.45%)</td><td>0.22 (+2.46%)</td><td>0.22 (+1.28%)</td><td>0.18 (-5.53%)</td><td>0.04 <b>(+42.54%)</b></td><td>193.70 (+5.85%)</td><td>160.98 (-1.01%)</td><td>158.60 (-1.25%)</td><td>129.20 (-2.42%)</td><td>29.41 <b>(+49.28%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>183.00 (n/a)</td><td>162.62 (n/a)</td><td>160.60 (n/a)</td><td>132.40 (n/a)</td><td>19.70 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.28 (+2.31%)</td><td>0.23 (-4.30%)</td><td>0.22 (-11.00%)</td><td>0.20 (-0.99%)</td><td>0.03 (-3.81%)</td><td>172.50 (+1.00%)</td><td>154.42 (+4.34%)</td><td>158.50 (+12.41%)</td><td>125.50 (-2.26%)</td><td>18.35 (-7.24%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>170.80 (n/a)</td><td>148.00 (n/a)</td><td>141.00 (n/a)</td><td>128.40 (n/a)</td><td>19.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 <b>(-22.09%)</b></td><td>0.18 (-11.24%)</td><td>0.19 (-2.98%)</td><td>0.16 (-1.15%)</td><td>0.02 <b>(-54.92%)</b></td><td>214.90 (+1.18%)</td><td>190.10 (+9.80%)</td><td>187.30 (+3.08%)</td><td>165.40 <b>(+28.32%)</b></td><td>20.89 <b>(-40.66%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>212.40 (n/a)</td><td>173.14 (n/a)</td><td>181.70 (n/a)</td><td>128.90 (n/a)</td><td>35.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 <b>(-34.56%)</b></td><td>0.19 (-18.73%)</td><td>0.17 (-19.38%)</td><td>0.15 (-15.42%)</td><td>0.04 <b>(-47.84%)</b></td><td>227.70 (+18.22%)</td><td>191.48 (+19.50%)</td><td>200.20 <b>(+24.04%)</b></td><td>149.60 <b>(+52.81%)</b></td><td>36.64 (-3.80%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.36 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>192.60 (n/a)</td><td>160.24 (n/a)</td><td>161.40 (n/a)</td><td>97.90 (n/a)</td><td>38.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 <b>(-21.47%)</b></td><td>0.17 (-19.81%)</td><td>0.16 <b>(-25.10%)</b></td><td>0.13 (-19.52%)</td><td>0.03 <b>(-41.11%)</b></td><td>266.70 <b>(+24.22%)</b></td><td>209.76 <b>(+22.21%)</b></td><td>212.80 <b>(+33.58%)</b></td><td>168.00 <b>(+27.37%)</b></td><td>36.97 (-8.88%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>214.70 (n/a)</td><td>171.64 (n/a)</td><td>159.30 (n/a)</td><td>131.90 (n/a)</td><td>40.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.90 (+9.06%)</td><td>0.82 <b>(+20.65%)</b></td><td>0.80 (+14.90%)</td><td>0.72 <b>(+43.89%)</b></td><td>0.09 <b>(-30.29%)</b></td><td>183.30 <b>(-30.49%)</b></td><td>162.12 (-18.77%)</td><td>164.80 (-12.99%)</td><td>145.00 (-8.29%)</td><td>16.87 <b>(-57.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.83 (n/a)</td><td>0.68 (n/a)</td><td>0.69 (n/a)</td><td>0.50 (n/a)</td><td>0.12 (n/a)</td><td>263.70 (n/a)</td><td>199.58 (n/a)</td><td>189.40 (n/a)</td><td>158.10 (n/a)</td><td>39.74 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.76 (-17.81%)</td><td>0.71 (-4.88%)</td><td>0.73 (+0.73%)</td><td>0.62 (+2.57%)</td><td>0.06 <b>(-53.14%)</b></td><td>211.70 (-2.49%)</td><td>186.42 (+3.64%)</td><td>180.30 (-0.72%)</td><td>172.30 <b>(+21.68%)</b></td><td>15.64 <b>(-43.34%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.93 (n/a)</td><td>0.74 (n/a)</td><td>0.72 (n/a)</td><td>0.60 (n/a)</td><td>0.12 (n/a)</td><td>217.10 (n/a)</td><td>179.88 (n/a)</td><td>181.60 (n/a)</td><td>141.60 (n/a)</td><td>27.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.18 <b>(+24.34%)</b></td><td>0.83 <b>(+26.36%)</b></td><td>0.77 <b>(+26.52%)</b></td><td>0.62 <b>(+60.25%)</b></td><td>0.21 (-18.67%)</td><td>212.50 <b>(-37.59%)</b></td><td>164.98 <b>(-27.45%)</b></td><td>170.30 <b>(-20.94%)</b></td><td>111.50 (-19.55%)</td><td>37.68 <b>(-58.67%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.95 (n/a)</td><td>0.66 (n/a)</td><td>0.61 (n/a)</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>340.50 (n/a)</td><td>227.40 (n/a)</td><td>215.40 (n/a)</td><td>138.60 (n/a)</td><td>91.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (-2.15%)</td><td>0.02 (-3.12%)</td><td>0.02 (+3.09%)</td><td>0.02 (-2.13%)</td><td>0.01 (-10.74%)</td><td>210.40 (+2.19%)</td><td>175.78 (+2.32%)</td><td>184.30 (-3.00%)</td><td>122.70 (+2.16%)</td><td>33.88 (-10.18%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>171.80 (n/a)</td><td>190.00 (n/a)</td><td>120.10 (n/a)</td><td>37.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+13.14%)</td><td>0.02 (-7.01%)</td><td>0.02 (-12.68%)</td><td>0.02 (-17.69%)</td><td>0.00 <b>(+190.81%)</b></td><td>223.20 <b>(+21.50%)</b></td><td>188.98 (+10.15%)</td><td>188.80 (+14.49%)</td><td>143.50 (-11.64%)</td><td>33.67 <b>(+216.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.70 (n/a)</td><td>171.56 (n/a)</td><td>164.90 (n/a)</td><td>162.40 (n/a)</td><td>10.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 <b>(+20.71%)</b></td><td>0.03 <b>(+24.56%)</b></td><td>0.03 <b>(+23.79%)</b></td><td>0.02 (+17.45%)</td><td>0.00 <b>(+29.14%)</b></td><td>172.90 (-14.87%)</td><td>144.80 (-19.56%)</td><td>147.40 (-19.23%)</td><td>122.60 (-17.16%)</td><td>19.03 (-7.13%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.10 (n/a)</td><td>180.00 (n/a)</td><td>182.50 (n/a)</td><td>148.00 (n/a)</td><td>20.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>18.12 (+18.14%)</td><td>13.60 (+9.91%)</td><td>12.68 (+5.81%)</td><td>10.32 (+2.63%)</td><td>3.15 <b>(+64.34%)</b></td><td>203.30 (-2.59%)</td><td>160.68 (-6.96%)</td><td>165.40 (-5.49%)</td><td>115.80 (-15.35%)</td><td>35.10 <b>(+36.04%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>15.34 (n/a)</td><td>12.37 (n/a)</td><td>11.99 (n/a)</td><td>10.05 (n/a)</td><td>1.92 (n/a)</td><td>208.70 (n/a)</td><td>172.70 (n/a)</td><td>175.00 (n/a)</td><td>136.80 (n/a)</td><td>25.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.87 (-12.68%)</td><td>0.77 (-9.17%)</td><td>0.72 (-9.06%)</td><td>0.71 (-0.41%)</td><td>0.07 <b>(-38.47%)</b></td><td>185.10 (+0.43%)</td><td>172.54 (+9.20%)</td><td>182.50 (+9.94%)</td><td>151.10 (+14.47%)</td><td>15.38 <b>(-27.63%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.00 (n/a)</td><td>0.85 (n/a)</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.12 (n/a)</td><td>184.30 (n/a)</td><td>158.00 (n/a)</td><td>166.00 (n/a)</td><td>132.00 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.09 (+18.31%)</td><td>0.93 (+18.38%)</td><td>0.88 (+9.09%)</td><td>0.78 <b>(+23.84%)</b></td><td>0.14 <b>(+23.67%)</b></td><td>170.10 (-19.27%)</td><td>144.10 (-15.50%)</td><td>149.30 (-8.29%)</td><td>121.40 (-15.52%)</td><td>21.15 (-18.73%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.92 (n/a)</td><td>0.79 (n/a)</td><td>0.81 (n/a)</td><td>0.63 (n/a)</td><td>0.11 (n/a)</td><td>210.70 (n/a)</td><td>170.54 (n/a)</td><td>162.80 (n/a)</td><td>143.70 (n/a)</td><td>26.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.88 (-11.86%)</td><td>0.79 (+0.01%)</td><td>0.78 (+7.22%)</td><td>0.64 (-4.38%)</td><td>0.09 <b>(-30.16%)</b></td><td>206.20 (+4.62%)</td><td>170.08 (-0.78%)</td><td>168.40 (-6.76%)</td><td>150.30 (+13.52%)</td><td>21.72 (-14.69%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.00 (n/a)</td><td>0.79 (n/a)</td><td>0.73 (n/a)</td><td>0.67 (n/a)</td><td>0.13 (n/a)</td><td>197.10 (n/a)</td><td>171.42 (n/a)</td><td>180.60 (n/a)</td><td>132.40 (n/a)</td><td>25.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.89 (+9.47%)</td><td>0.80 (+6.62%)</td><td>0.79 (+1.95%)</td><td>0.74 <b>(+20.90%)</b></td><td>0.06 <b>(-29.38%)</b></td><td>177.60 (-17.28%)</td><td>165.62 (-6.81%)</td><td>167.80 (-1.93%)</td><td>148.30 (-8.63%)</td><td>11.03 <b>(-48.13%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.81 (n/a)</td><td>0.75 (n/a)</td><td>0.77 (n/a)</td><td>0.62 (n/a)</td><td>0.08 (n/a)</td><td>214.70 (n/a)</td><td>177.72 (n/a)</td><td>171.10 (n/a)</td><td>162.30 (n/a)</td><td>21.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.04 (+15.56%)</td><td>0.82 <b>(+21.96%)</b></td><td>0.77 <b>(+21.24%)</b></td><td>0.69 <b>(+40.71%)</b></td><td>0.14 (-18.15%)</td><td>192.00 <b>(-28.92%)</b></td><td>165.10 <b>(-20.26%)</b></td><td>171.60 (-17.50%)</td><td>126.70 (-13.46%)</td><td>24.24 <b>(-50.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.90 (n/a)</td><td>0.67 (n/a)</td><td>0.64 (n/a)</td><td>0.49 (n/a)</td><td>0.17 (n/a)</td><td>270.10 (n/a)</td><td>207.06 (n/a)</td><td>208.00 (n/a)</td><td>146.40 (n/a)</td><td>49.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+7.03%)</td><td>0.03 (+2.19%)</td><td>0.02 (+5.16%)</td><td>0.02 (-3.98%)</td><td>0.01 (+13.62%)</td><td>211.50 (+4.14%)</td><td>165.12 (-1.51%)</td><td>164.90 (-4.90%)</td><td>122.70 (-6.55%)</td><td>32.97 (+10.90%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.10 (n/a)</td><td>167.66 (n/a)</td><td>173.40 (n/a)</td><td>131.30 (n/a)</td><td>29.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (+16.94%)</td><td>0.03 (+18.49%)</td><td>0.03 (+13.78%)</td><td>0.02 <b>(+30.61%)</b></td><td>0.00 (+6.47%)</td><td>185.40 <b>(-23.45%)</b></td><td>155.48 (-16.18%)</td><td>155.70 (-12.13%)</td><td>127.70 (-14.47%)</td><td>23.09 <b>(-32.67%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.20 (n/a)</td><td>185.50 (n/a)</td><td>177.20 (n/a)</td><td>149.30 (n/a)</td><td>34.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.00 (-2.27%)</td><td>0.00 (-1.42%)</td><td>0.00 (-2.33%)</td><td>0.00 (+0.00%)</td><td>0.00 (-15.71%)</td><td>1051.48 (+0.72%)</td><td>979.21 (+1.31%)</td><td>968.60 (+2.17%)</td><td>943.91 (+1.08%)</td><td>41.72 (-6.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1043.92 (n/a)</td><td>966.58 (n/a)</td><td>948.07 (n/a)</td><td>933.79 (n/a)</td><td>44.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.01 (-1.20%)</td><td>0.01 (-0.25%)</td><td>0.01 (-1.22%)</td><td>0.01 (+6.76%)</td><td>0.00 <b>(-64.52%)</b></td><td>1042.95 (-5.60%)</td><td>1018.56 (+0.08%)</td><td>1010.70 (+1.21%)</td><td>997.17 (+1.47%)</td><td>20.15 <b>(-59.43%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1104.77 (n/a)</td><td>1017.79 (n/a)</td><td>998.63 (n/a)</td><td>982.71 (n/a)</td><td>49.66 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.99 (-1.40%)</td><td>0.97 (-0.44%)</td><td>0.96 (-0.69%)</td><td>0.94 (-0.16%)</td><td>0.02 (-16.28%)</td><td>2221.66 (+0.16%)</td><td>2170.51 (+0.44%)</td><td>2176.41 (+0.70%)</td><td>2109.60 (+1.42%)</td><td>43.93 (-14.73%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.01 (n/a)</td><td>0.97 (n/a)</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2218.07 (n/a)</td><td>2161.11 (n/a)</td><td>2161.24 (n/a)</td><td>2080.06 (n/a)</td><td>51.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.90 (-0.53%)</td><td>0.88 (+0.65%)</td><td>0.88 (-0.22%)</td><td>0.87 (+3.71%)</td><td>0.01 <b>(-54.32%)</b></td><td>2420.45 (-3.58%)</td><td>2377.26 (-0.70%)</td><td>2382.57 (+0.22%)</td><td>2332.96 (+0.53%)</td><td>31.60 <b>(-55.94%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.84 (n/a)</td><td>0.03 (n/a)</td><td>2510.42 (n/a)</td><td>2394.12 (n/a)</td><td>2377.33 (n/a)</td><td>2320.72 (n/a)</td><td>71.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.99 (-10.57%)</td><td>5.21 (+8.67%)</td><td>5.39 <b>(+22.98%)</b></td><td>4.43 (+12.61%)</td><td>0.70 <b>(-35.93%)</b></td><td>236.70 (-11.22%)</td><td>204.18 (-9.69%)</td><td>194.70 (-18.67%)</td><td>175.20 (+11.88%)</td><td>27.99 <b>(-32.50%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.69 (n/a)</td><td>4.80 (n/a)</td><td>4.38 (n/a)</td><td>3.93 (n/a)</td><td>1.09 (n/a)</td><td>266.60 (n/a)</td><td>226.10 (n/a)</td><td>239.40 (n/a)</td><td>156.60 (n/a)</td><td>41.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.45 (-7.30%)</td><td>4.98 (-1.44%)</td><td>5.08 (-2.40%)</td><td>4.07 (+1.14%)</td><td>0.54 <b>(-28.13%)</b></td><td>257.40 (-1.15%)</td><td>212.84 (+0.61%)</td><td>206.30 (+2.43%)</td><td>192.30 (+7.85%)</td><td>26.01 <b>(-22.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.88 (n/a)</td><td>5.05 (n/a)</td><td>5.21 (n/a)</td><td>4.03 (n/a)</td><td>0.75 (n/a)</td><td>260.40 (n/a)</td><td>211.56 (n/a)</td><td>201.40 (n/a)</td><td>178.30 (n/a)</td><td>33.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.79 (-12.75%)</td><td>4.67 (+2.49%)</td><td>4.68 (+11.95%)</td><td>3.62 (+0.42%)</td><td>0.98 (-17.39%)</td><td>289.30 (-0.41%)</td><td>233.00 (-3.09%)</td><td>224.20 (-10.68%)</td><td>181.10 (+14.62%)</td><td>49.73 (+0.86%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.64 (n/a)</td><td>4.55 (n/a)</td><td>4.18 (n/a)</td><td>3.61 (n/a)</td><td>1.19 (n/a)</td><td>290.50 (n/a)</td><td>240.44 (n/a)</td><td>251.00 (n/a)</td><td>158.00 (n/a)</td><td>49.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.09 (-11.78%)</td><td>4.64 (-4.19%)</td><td>4.82 (+1.65%)</td><td>3.68 (-4.84%)</td><td>0.56 <b>(-24.51%)</b></td><td>284.60 (+5.06%)</td><td>228.88 (+3.77%)</td><td>217.80 (-1.63%)</td><td>205.90 (+13.38%)</td><td>31.84 (-7.87%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.77 (n/a)</td><td>4.85 (n/a)</td><td>4.74 (n/a)</td><td>3.87 (n/a)</td><td>0.74 (n/a)</td><td>270.90 (n/a)</td><td>220.56 (n/a)</td><td>221.40 (n/a)</td><td>181.60 (n/a)</td><td>34.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.27 (-5.07%)</td><td>8.06 (+5.04%)</td><td>7.71 (+4.39%)</td><td>7.22 <b>(+20.86%)</b></td><td>0.81 <b>(-41.47%)</b></td><td>290.40 (-17.26%)</td><td>262.18 (-6.46%)</td><td>272.10 (-4.22%)</td><td>226.20 (+5.36%)</td><td>25.12 <b>(-49.00%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.77 (n/a)</td><td>7.67 (n/a)</td><td>7.38 (n/a)</td><td>5.97 (n/a)</td><td>1.38 (n/a)</td><td>351.00 (n/a)</td><td>280.28 (n/a)</td><td>284.10 (n/a)</td><td>214.70 (n/a)</td><td>49.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.37 (-14.06%)</td><td>7.43 (-2.56%)</td><td>7.58 (+4.14%)</td><td>6.55 (-3.53%)</td><td>0.68 <b>(-44.12%)</b></td><td>320.40 (+3.69%)</td><td>284.20 (+1.52%)</td><td>276.50 (-3.99%)</td><td>250.70 (+16.39%)</td><td>26.14 <b>(-31.52%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.73 (n/a)</td><td>7.62 (n/a)</td><td>7.28 (n/a)</td><td>6.79 (n/a)</td><td>1.22 (n/a)</td><td>309.00 (n/a)</td><td>279.94 (n/a)</td><td>288.00 (n/a)</td><td>215.40 (n/a)</td><td>38.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.00 (-1.99%)</td><td>7.89 (+7.92%)</td><td>7.86 (+9.75%)</td><td>6.77 (+12.16%)</td><td>0.87 <b>(-27.68%)</b></td><td>309.60 (-10.86%)</td><td>268.60 (-8.30%)</td><td>266.80 (-8.88%)</td><td>233.10 (+2.01%)</td><td>29.95 <b>(-33.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.18 (n/a)</td><td>7.31 (n/a)</td><td>7.16 (n/a)</td><td>6.04 (n/a)</td><td>1.20 (n/a)</td><td>347.30 (n/a)</td><td>292.92 (n/a)</td><td>292.80 (n/a)</td><td>228.50 (n/a)</td><td>45.12 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.62 (+2.81%)</td><td>8.64 (+10.80%)</td><td>8.53 (+3.26%)</td><td>7.13 <b>(+32.58%)</b></td><td>1.02 <b>(-31.44%)</b></td><td>294.00 <b>(-24.60%)</b></td><td>245.50 (-11.87%)</td><td>245.90 (-3.15%)</td><td>218.10 (-2.72%)</td><td>30.84 <b>(-52.34%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.35 (n/a)</td><td>7.80 (n/a)</td><td>8.26 (n/a)</td><td>5.38 (n/a)</td><td>1.48 (n/a)</td><td>389.90 (n/a)</td><td>278.58 (n/a)</td><td>253.90 (n/a)</td><td>224.20 (n/a)</td><td>64.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.75 (-6.25%)</td><td>8.82 (+4.57%)</td><td>8.48 (+4.71%)</td><td>8.29 (+11.98%)</td><td>0.61 <b>(-50.60%)</b></td><td>253.00 (-10.70%)</td><td>238.56 (-5.51%)</td><td>247.20 (-4.48%)</td><td>215.20 (+6.69%)</td><td>15.83 <b>(-53.23%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>10.40 (n/a)</td><td>8.44 (n/a)</td><td>8.10 (n/a)</td><td>7.40 (n/a)</td><td>1.23 (n/a)</td><td>283.30 (n/a)</td><td>252.46 (n/a)</td><td>258.80 (n/a)</td><td>201.70 (n/a)</td><td>33.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.06 (-9.56%)</td><td>8.46 (+3.85%)</td><td>8.45 (-0.00%)</td><td>7.90 <b>(+32.02%)</b></td><td>0.46 <b>(-69.59%)</b></td><td>265.50 <b>(-24.25%)</b></td><td>248.42 (-6.33%)</td><td>248.30 (+0.00%)</td><td>231.50 (+10.55%)</td><td>13.41 <b>(-75.02%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>10.02 (n/a)</td><td>8.15 (n/a)</td><td>8.45 (n/a)</td><td>5.98 (n/a)</td><td>1.50 (n/a)</td><td>350.50 (n/a)</td><td>265.20 (n/a)</td><td>248.30 (n/a)</td><td>209.40 (n/a)</td><td>53.67 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>11.69 (-6.34%)</td><td>11.26 (-2.98%)</td><td>11.46 (-1.60%)</td><td>10.68 (+2.91%)</td><td>0.43 <b>(-48.83%)</b></td><td>392.80 (-2.82%)</td><td>373.06 (+2.75%)</td><td>366.00 (+1.64%)</td><td>358.70 (+6.76%)</td><td>14.52 <b>(-46.73%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>12.48 (n/a)</td><td>11.60 (n/a)</td><td>11.65 (n/a)</td><td>10.38 (n/a)</td><td>0.84 (n/a)</td><td>404.20 (n/a)</td><td>363.08 (n/a)</td><td>360.10 (n/a)</td><td>336.00 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>13.99 (+12.72%)</td><td>12.05 (+0.63%)</td><td>12.27 (+2.76%)</td><td>10.23 (-10.40%)</td><td>1.37 <b>(+251.07%)</b></td><td>410.00 (+11.63%)</td><td>351.80 (+0.33%)</td><td>341.80 (-2.68%)</td><td>299.90 (-11.30%)</td><td>40.23 <b>(+249.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>12.41 (n/a)</td><td>11.97 (n/a)</td><td>11.94 (n/a)</td><td>11.42 (n/a)</td><td>0.39 (n/a)</td><td>367.30 (n/a)</td><td>350.64 (n/a)</td><td>351.20 (n/a)</td><td>338.10 (n/a)</td><td>11.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>12.63 (-1.18%)</td><td>12.13 (-0.62%)</td><td>12.38 (+0.24%)</td><td>11.40 (+3.61%)</td><td>0.55 <b>(-23.75%)</b></td><td>367.80 (-3.49%)</td><td>346.30 (+0.49%)</td><td>338.80 (-0.24%)</td><td>332.20 (+1.19%)</td><td>15.99 <b>(-25.99%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>12.78 (n/a)</td><td>12.21 (n/a)</td><td>12.35 (n/a)</td><td>11.01 (n/a)</td><td>0.72 (n/a)</td><td>381.10 (n/a)</td><td>344.60 (n/a)</td><td>339.60 (n/a)</td><td>328.30 (n/a)</td><td>21.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.96 (+3.71%)</td><td>13.41 (-1.61%)</td><td>13.02 (-6.97%)</td><td>12.28 (-3.25%)</td><td>1.05 <b>(+39.48%)</b></td><td>341.60 (+3.36%)</td><td>314.26 (+1.87%)</td><td>322.20 (+7.51%)</td><td>280.40 (-3.58%)</td><td>23.79 <b>(+37.79%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.42 (n/a)</td><td>13.63 (n/a)</td><td>13.99 (n/a)</td><td>12.69 (n/a)</td><td>0.75 (n/a)</td><td>330.50 (n/a)</td><td>308.48 (n/a)</td><td>299.70 (n/a)</td><td>290.80 (n/a)</td><td>17.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>16.01 (+7.19%)</td><td>13.32 (+2.50%)</td><td>12.25 (-1.93%)</td><td>11.77 (+3.37%)</td><td>1.82 (+18.74%)</td><td>356.30 (-3.26%)</td><td>319.38 (-2.14%)</td><td>342.40 (+1.97%)</td><td>261.90 (-6.73%)</td><td>40.65 (+8.25%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.94 (n/a)</td><td>12.99 (n/a)</td><td>12.49 (n/a)</td><td>11.39 (n/a)</td><td>1.53 (n/a)</td><td>368.30 (n/a)</td><td>326.36 (n/a)</td><td>335.80 (n/a)</td><td>280.80 (n/a)</td><td>37.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.27 (+9.28%)</td><td>13.40 (+6.32%)</td><td>14.06 (+10.18%)</td><td>11.54 (-1.59%)</td><td>1.18 <b>(+119.91%)</b></td><td>363.40 (+1.59%)</td><td>315.04 (-5.46%)</td><td>298.40 (-9.25%)</td><td>294.00 (-8.50%)</td><td>29.86 <b>(+102.47%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.06 (n/a)</td><td>12.61 (n/a)</td><td>12.76 (n/a)</td><td>11.73 (n/a)</td><td>0.54 (n/a)</td><td>357.70 (n/a)</td><td>333.22 (n/a)</td><td>328.80 (n/a)</td><td>321.30 (n/a)</td><td>14.75 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.42 (+4.50%)</td><td>13.18 (-0.75%)</td><td>13.81 (+2.64%)</td><td>10.92 (-13.65%)</td><td>1.37 <b>(+199.79%)</b></td><td>384.20 (+15.83%)</td><td>321.34 (+1.64%)</td><td>303.70 (-2.57%)</td><td>291.00 (-4.31%)</td><td>37.19 <b>(+236.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.79 (n/a)</td><td>13.28 (n/a)</td><td>13.45 (n/a)</td><td>12.64 (n/a)</td><td>0.46 (n/a)</td><td>331.70 (n/a)</td><td>316.16 (n/a)</td><td>311.70 (n/a)</td><td>304.10 (n/a)</td><td>11.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.72 (+6.30%)</td><td>12.57 (-1.12%)</td><td>12.51 (+0.15%)</td><td>8.74 <b>(-28.34%)</b></td><td>2.42 <b>(+269.58%)</b></td><td>479.70 <b>(+39.53%)</b></td><td>345.76 (+4.59%)</td><td>335.30 (-0.12%)</td><td>284.90 (-5.91%)</td><td>79.34 <b>(+392.56%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.85 (n/a)</td><td>12.71 (n/a)</td><td>12.49 (n/a)</td><td>12.20 (n/a)</td><td>0.66 (n/a)</td><td>343.80 (n/a)</td><td>330.58 (n/a)</td><td>335.70 (n/a)</td><td>302.80 (n/a)</td><td>16.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.06 <b>(-20.65%)</b></td><td>2.57 (-13.09%)</td><td>2.57 (-5.48%)</td><td>1.89 <b>(-24.11%)</b></td><td>0.44 <b>(-21.78%)</b></td><td>277.40 <b>(+31.78%)</b></td><td>209.80 (+15.20%)</td><td>203.90 (+5.81%)</td><td>171.10 <b>(+25.99%)</b></td><td>40.67 <b>(+34.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.86 (n/a)</td><td>2.95 (n/a)</td><td>2.72 (n/a)</td><td>2.49 (n/a)</td><td>0.56 (n/a)</td><td>210.50 (n/a)</td><td>182.12 (n/a)</td><td>192.70 (n/a)</td><td>135.80 (n/a)</td><td>30.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.21 (+3.61%)</td><td>5.01 (+1.34%)</td><td>4.65 (-4.02%)</td><td>4.20 (-2.52%)</td><td>0.86 <b>(+30.12%)</b></td><td>249.50 (+2.59%)</td><td>213.78 (-0.43%)</td><td>225.40 (+4.16%)</td><td>169.00 (-3.43%)</td><td>34.31 <b>(+29.36%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.99 (n/a)</td><td>4.95 (n/a)</td><td>4.85 (n/a)</td><td>4.31 (n/a)</td><td>0.66 (n/a)</td><td>243.20 (n/a)</td><td>214.70 (n/a)</td><td>216.40 (n/a)</td><td>175.00 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.06 (+5.08%)</td><td>7.75 (-0.07%)</td><td>7.71 (-4.19%)</td><td>6.67 (-4.06%)</td><td>1.07 <b>(+41.41%)</b></td><td>314.50 (+4.21%)</td><td>274.56 (+0.80%)</td><td>271.80 (+4.34%)</td><td>231.50 (-4.85%)</td><td>37.68 <b>(+39.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>8.62 (n/a)</td><td>7.76 (n/a)</td><td>8.05 (n/a)</td><td>6.95 (n/a)</td><td>0.76 (n/a)</td><td>301.80 (n/a)</td><td>272.38 (n/a)</td><td>260.50 (n/a)</td><td>243.30 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.42 (+3.57%)</td><td>3.04 (+12.87%)</td><td>3.09 (+16.39%)</td><td>2.65 <b>(+23.18%)</b></td><td>0.29 <b>(-38.69%)</b></td><td>197.50 (-18.79%)</td><td>173.70 (-12.92%)</td><td>169.80 (-14.07%)</td><td>153.40 (-3.46%)</td><td>16.87 <b>(-51.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.30 (n/a)</td><td>2.69 (n/a)</td><td>2.65 (n/a)</td><td>2.16 (n/a)</td><td>0.47 (n/a)</td><td>243.20 (n/a)</td><td>199.48 (n/a)</td><td>197.60 (n/a)</td><td>158.90 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (+14.13%)</td><td>0.20 (+1.98%)</td><td>0.19 (-1.98%)</td><td>0.15 (-12.87%)</td><td>0.04 <b>(+67.25%)</b></td><td>225.70 (+14.80%)</td><td>173.28 (+0.45%)</td><td>170.90 (+2.03%)</td><td>124.80 (-12.42%)</td><td>37.39 <b>(+63.95%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.60 (n/a)</td><td>172.50 (n/a)</td><td>167.50 (n/a)</td><td>142.50 (n/a)</td><td>22.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (+16.69%)</td><td>0.21 (+1.93%)</td><td>0.19 (-4.84%)</td><td>0.19 (+5.92%)</td><td>0.03 <b>(+60.04%)</b></td><td>174.00 (-5.59%)</td><td>161.74 (-1.15%)</td><td>172.80 (+5.11%)</td><td>126.70 (-14.33%)</td><td>20.14 <b>(+30.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>184.30 (n/a)</td><td>163.62 (n/a)</td><td>164.40 (n/a)</td><td>147.90 (n/a)</td><td>15.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.50 (-5.56%)</td><td>0.40 (+1.14%)</td><td>0.38 (-0.29%)</td><td>0.30 (+8.56%)</td><td>0.07 <b>(-27.75%)</b></td><td>216.80 (-7.90%)</td><td>170.06 (-3.51%)</td><td>170.90 (+0.29%)</td><td>132.10 (+5.85%)</td><td>31.00 <b>(-29.42%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.53 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>235.40 (n/a)</td><td>176.24 (n/a)</td><td>170.40 (n/a)</td><td>124.80 (n/a)</td><td>43.92 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.52 (+2.90%)</td><td>0.40 (+8.60%)</td><td>0.36 (+3.08%)</td><td>0.32 (+5.49%)</td><td>0.08 (+5.56%)</td><td>204.40 (-5.24%)</td><td>169.06 (-7.75%)</td><td>184.20 (-3.00%)</td><td>126.70 (-2.84%)</td><td>31.91 (+0.88%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>215.70 (n/a)</td><td>183.26 (n/a)</td><td>189.90 (n/a)</td><td>130.40 (n/a)</td><td>31.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.52 <b>(+27.29%)</b></td><td>0.38 (+5.07%)</td><td>0.37 (+7.21%)</td><td>0.26 (-14.91%)</td><td>0.09 <b>(+120.54%)</b></td><td>256.50 (+17.50%)</td><td>183.62 (-0.98%)</td><td>175.00 (-6.72%)</td><td>126.10 <b>(-21.43%)</b></td><td>47.11 <b>(+105.84%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.04 (n/a)</td><td>218.30 (n/a)</td><td>185.44 (n/a)</td><td>187.60 (n/a)</td><td>160.50 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.97 <b>(+25.54%)</b></td><td>0.80 (+13.85%)</td><td>0.78 (+9.07%)</td><td>0.68 (+14.35%)</td><td>0.10 <b>(+47.67%)</b></td><td>191.50 (-12.56%)</td><td>166.00 (-11.82%)</td><td>167.30 (-8.28%)</td><td>135.60 <b>(-20.38%)</b></td><td>19.90 (+0.64%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.77 (n/a)</td><td>0.70 (n/a)</td><td>0.72 (n/a)</td><td>0.60 (n/a)</td><td>0.07 (n/a)</td><td>219.00 (n/a)</td><td>188.26 (n/a)</td><td>182.40 (n/a)</td><td>170.30 (n/a)</td><td>19.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.05 (+3.62%)</td><td>0.84 (+9.32%)</td><td>0.88 <b>(+24.72%)</b></td><td>0.67 (+6.04%)</td><td>0.16 (+7.29%)</td><td>195.50 (-5.69%)</td><td>161.20 (-8.25%)</td><td>149.10 (-19.84%)</td><td>125.40 (-3.46%)</td><td>30.34 (+3.71%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.01 (n/a)</td><td>0.77 (n/a)</td><td>0.70 (n/a)</td><td>0.63 (n/a)</td><td>0.15 (n/a)</td><td>207.30 (n/a)</td><td>175.70 (n/a)</td><td>186.00 (n/a)</td><td>129.90 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.91 (+2.94%)</td><td>0.79 (+5.87%)</td><td>0.78 (+5.23%)</td><td>0.70 (+6.21%)</td><td>0.08 (-1.30%)</td><td>187.50 (-5.83%)</td><td>166.82 (-5.63%)</td><td>167.80 (-4.98%)</td><td>144.50 (-2.82%)</td><td>17.34 (-9.03%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.88 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.66 (n/a)</td><td>0.09 (n/a)</td><td>199.10 (n/a)</td><td>176.78 (n/a)</td><td>176.60 (n/a)</td><td>148.70 (n/a)</td><td>19.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.89 (+8.00%)</td><td>0.71 (-1.11%)</td><td>0.72 (+1.55%)</td><td>0.59 (-7.66%)</td><td>0.13 <b>(+88.60%)</b></td><td>222.20 (+8.28%)</td><td>188.54 (+2.95%)</td><td>182.90 (-1.56%)</td><td>147.70 (-7.40%)</td><td>32.68 <b>(+96.61%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.82 (n/a)</td><td>0.72 (n/a)</td><td>0.71 (n/a)</td><td>0.64 (n/a)</td><td>0.07 (n/a)</td><td>205.20 (n/a)</td><td>183.14 (n/a)</td><td>185.80 (n/a)</td><td>159.50 (n/a)</td><td>16.62 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (+11.96%)</td><td>0.10 (+9.44%)</td><td>0.11 (+9.53%)</td><td>0.06 (+10.06%)</td><td>0.03 (+7.15%)</td><td>297.40 (-9.16%)</td><td>174.06 (-8.97%)</td><td>150.60 (-8.67%)</td><td>118.70 (-10.68%)</td><td>70.41 (-10.31%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>327.40 (n/a)</td><td>191.22 (n/a)</td><td>164.90 (n/a)</td><td>132.90 (n/a)</td><td>78.50 (n/a)</td>
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
