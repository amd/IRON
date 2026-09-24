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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (+10.99%)</td><td>0.04 (+3.74%)</td><td>0.04 (-3.93%)</td><td>0.03 (+7.64%)</td><td>0.01 (+6.11%)</td><td>182.30 (-7.08%)</td><td>152.82 (-3.80%)</td><td>157.90 (+4.09%)</td><td>113.10 (-9.95%)</td><td>29.42 (-10.97%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.20 (n/a)</td><td>158.86 (n/a)</td><td>151.70 (n/a)</td><td>125.60 (n/a)</td><td>33.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (+0.47%)</td><td>0.04 (+0.59%)</td><td>0.04 (-7.81%)</td><td>0.04 (+17.58%)</td><td>0.01 <b>(-22.95%)</b></td><td>163.40 (-14.94%)</td><td>143.20 (-1.97%)</td><td>142.50 (+8.45%)</td><td>121.40 (-0.49%)</td><td>19.47 <b>(-33.81%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.10 (n/a)</td><td>146.08 (n/a)</td><td>131.40 (n/a)</td><td>122.00 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (-2.73%)</td><td>0.05 (+12.67%)</td><td>0.05 <b>(+23.40%)</b></td><td>0.04 (+12.78%)</td><td>0.00 <b>(-39.38%)</b></td><td>158.20 (-11.32%)</td><td>136.72 (-12.28%)</td><td>131.00 (-18.94%)</td><td>128.20 (+2.81%)</td><td>12.47 <b>(-44.46%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>178.40 (n/a)</td><td>155.86 (n/a)</td><td>161.60 (n/a)</td><td>124.70 (n/a)</td><td>22.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (-9.69%)</td><td>0.04 (+10.52%)</td><td>0.04 <b>(+21.40%)</b></td><td>0.03 (+11.66%)</td><td>0.01 <b>(-38.47%)</b></td><td>192.50 (-10.42%)</td><td>152.18 (-12.03%)</td><td>149.80 (-17.65%)</td><td>125.70 (+10.75%)</td><td>24.77 <b>(-35.04%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>173.00 (n/a)</td><td>181.90 (n/a)</td><td>113.50 (n/a)</td><td>38.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (+18.20%)</td><td>0.04 (+5.39%)</td><td>0.04 (-3.52%)</td><td>0.03 (+11.16%)</td><td>0.01 <b>(+34.53%)</b></td><td>185.70 (-10.07%)</td><td>156.54 (-4.54%)</td><td>159.90 (+3.63%)</td><td>118.30 (-15.44%)</td><td>26.38 (+0.16%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>163.98 (n/a)</td><td>154.30 (n/a)</td><td>139.90 (n/a)</td><td>26.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (-7.98%)</td><td>0.04 (+12.01%)</td><td>0.04 (+15.35%)</td><td>0.03 <b>(+51.65%)</b></td><td>0.01 <b>(-47.83%)</b></td><td>177.50 <b>(-34.06%)</b></td><td>147.86 (-16.61%)</td><td>151.10 (-13.36%)</td><td>125.00 (+8.70%)</td><td>21.91 <b>(-63.37%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>269.20 (n/a)</td><td>177.32 (n/a)</td><td>174.40 (n/a)</td><td>115.00 (n/a)</td><td>59.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (-13.73%)</td><td>0.03 (-7.70%)</td><td>0.03 (-2.92%)</td><td>0.03 (-4.94%)</td><td>0.00 <b>(-28.92%)</b></td><td>235.20 (+5.23%)</td><td>193.88 (+7.42%)</td><td>186.50 (+3.04%)</td><td>161.90 (+15.89%)</td><td>27.04 (-11.61%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>180.48 (n/a)</td><td>181.00 (n/a)</td><td>139.70 (n/a)</td><td>30.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (+5.31%)</td><td>0.03 (+5.87%)</td><td>0.03 (+9.99%)</td><td>0.03 (+8.15%)</td><td>0.00 (-5.14%)</td><td>211.90 (-7.55%)</td><td>186.50 (-5.71%)</td><td>177.50 (-9.07%)</td><td>167.80 (-5.04%)</td><td>18.15 (-15.74%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>229.20 (n/a)</td><td>197.80 (n/a)</td><td>195.20 (n/a)</td><td>176.70 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 <b>(+21.60%)</b></td><td>0.07 (-6.46%)</td><td>0.07 (-9.67%)</td><td>0.03 <b>(-43.77%)</b></td><td>0.02 <b>(+206.56%)</b></td><td>354.90 <b>(+77.81%)</b></td><td>207.86 (+17.63%)</td><td>182.60 (+10.67%)</td><td>134.30 (-17.76%)</td><td>85.36 <b>(+385.76%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.60 (n/a)</td><td>176.70 (n/a)</td><td>165.00 (n/a)</td><td>163.30 (n/a)</td><td>17.57 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (+1.84%)</td><td>0.08 (+2.60%)</td><td>0.08 (-10.32%)</td><td>0.07 (+15.88%)</td><td>0.01 <b>(-29.85%)</b></td><td>184.30 (-13.72%)</td><td>160.44 (-4.90%)</td><td>162.70 (+11.51%)</td><td>131.40 (-1.79%)</td><td>23.19 <b>(-41.43%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.60 (n/a)</td><td>168.70 (n/a)</td><td>145.90 (n/a)</td><td>133.80 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (-8.18%)</td><td>0.07 (-0.24%)</td><td>0.07 (-1.69%)</td><td>0.06 (-0.45%)</td><td>0.01 <b>(-31.44%)</b></td><td>194.10 (+0.47%)</td><td>167.98 (-0.66%)</td><td>166.90 (+1.71%)</td><td>146.30 (+8.85%)</td><td>18.22 <b>(-26.37%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>169.10 (n/a)</td><td>164.10 (n/a)</td><td>134.40 (n/a)</td><td>24.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 <b>(+21.92%)</b></td><td>0.08 <b>(+25.08%)</b></td><td>0.08 (+7.90%)</td><td>0.07 <b>(+110.42%)</b></td><td>0.01 <b>(-28.18%)</b></td><td>180.50 <b>(-52.47%)</b></td><td>152.54 <b>(-27.18%)</b></td><td>155.80 (-7.32%)</td><td>119.20 (-17.96%)</td><td>25.31 <b>(-73.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>379.80 (n/a)</td><td>209.48 (n/a)</td><td>168.10 (n/a)</td><td>145.30 (n/a)</td><td>96.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 <b>(+23.12%)</b></td><td>0.09 <b>(+20.09%)</b></td><td>0.09 <b>(+23.78%)</b></td><td>0.06 (-4.58%)</td><td>0.02 <b>(+83.97%)</b></td><td>217.50 (+4.82%)</td><td>149.30 (-13.82%)</td><td>144.30 (-19.20%)</td><td>112.80 (-18.73%)</td><td>41.43 <b>(+59.71%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>173.24 (n/a)</td><td>178.60 (n/a)</td><td>138.80 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (+19.75%)</td><td>0.07 (-4.58%)</td><td>0.06 (-19.42%)</td><td>0.06 (-6.44%)</td><td>0.02 <b>(+145.02%)</b></td><td>218.80 (+6.89%)</td><td>190.26 (+8.23%)</td><td>215.90 <b>(+24.08%)</b></td><td>132.70 (-16.49%)</td><td>38.91 <b>(+121.49%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>175.80 (n/a)</td><td>174.00 (n/a)</td><td>158.90 (n/a)</td><td>17.57 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (+5.51%)</td><td>0.07 (+2.21%)</td><td>0.07 (+8.10%)</td><td>0.05 (-9.44%)</td><td>0.01 (+2.81%)</td><td>257.90 (+10.40%)</td><td>191.12 (-1.81%)</td><td>180.20 (-7.49%)</td><td>147.90 (-5.19%)</td><td>40.91 (+11.01%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>194.64 (n/a)</td><td>194.80 (n/a)</td><td>156.00 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 <b>(-28.35%)</b></td><td>0.07 (-10.14%)</td><td>0.08 (+5.32%)</td><td>0.04 <b>(-29.70%)</b></td><td>0.02 <b>(-20.94%)</b></td><td>289.40 <b>(+42.21%)</b></td><td>191.06 (+12.61%)</td><td>161.10 (-5.01%)</td><td>158.60 <b>(+39.61%)</b></td><td>56.29 <b>(+62.34%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>203.50 (n/a)</td><td>169.66 (n/a)</td><td>169.60 (n/a)</td><td>113.60 (n/a)</td><td>34.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (-9.25%)</td><td>0.16 (-13.32%)</td><td>0.16 (-16.43%)</td><td>0.14 (-4.69%)</td><td>0.02 (-16.91%)</td><td>173.00 (+4.91%)</td><td>154.90 (+15.03%)</td><td>155.70 (+19.68%)</td><td>129.20 (+10.24%)</td><td>16.98 (-6.78%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>164.90 (n/a)</td><td>134.66 (n/a)</td><td>130.10 (n/a)</td><td>117.20 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 (+10.92%)</td><td>0.17 (+4.87%)</td><td>0.16 (+5.48%)</td><td>0.14 (-3.90%)</td><td>0.02 <b>(+37.73%)</b></td><td>178.70 (+4.08%)</td><td>149.90 (-3.97%)</td><td>155.30 (-5.19%)</td><td>123.00 (-9.89%)</td><td>21.30 <b>(+29.13%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>171.70 (n/a)</td><td>156.10 (n/a)</td><td>163.80 (n/a)</td><td>136.50 (n/a)</td><td>16.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (-5.66%)</td><td>0.15 (-10.49%)</td><td>0.14 <b>(-20.08%)</b></td><td>0.11 (-0.90%)</td><td>0.03 (-3.71%)</td><td>213.80 (+0.90%)</td><td>174.20 (+11.62%)</td><td>180.40 <b>(+25.10%)</b></td><td>132.70 (+5.99%)</td><td>35.08 (+1.04%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.90 (n/a)</td><td>156.06 (n/a)</td><td>144.20 (n/a)</td><td>125.20 (n/a)</td><td>34.72 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 (+12.71%)</td><td>0.16 (+2.68%)</td><td>0.17 (+6.74%)</td><td>0.12 (-7.18%)</td><td>0.03 <b>(+79.13%)</b></td><td>198.40 (+7.77%)</td><td>156.86 (-0.63%)</td><td>145.40 (-6.31%)</td><td>120.10 (-11.30%)</td><td>30.46 <b>(+72.39%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>184.10 (n/a)</td><td>157.86 (n/a)</td><td>155.20 (n/a)</td><td>135.40 (n/a)</td><td>17.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 <b>(+29.83%)</b></td><td>0.17 <b>(+24.23%)</b></td><td>0.18 <b>(+41.26%)</b></td><td>0.12 (+4.38%)</td><td>0.04 <b>(+111.56%)</b></td><td>202.90 (-4.16%)</td><td>152.08 (-17.20%)</td><td>136.50 <b>(-29.20%)</b></td><td>122.10 <b>(-22.97%)</b></td><td>35.58 <b>(+57.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>211.70 (n/a)</td><td>183.68 (n/a)</td><td>192.80 (n/a)</td><td>158.50 (n/a)</td><td>22.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (+16.45%)</td><td>0.15 (-2.69%)</td><td>0.13 (-19.29%)</td><td>0.10 <b>(-24.26%)</b></td><td>0.05 <b>(+145.08%)</b></td><td>257.90 <b>(+32.05%)</b></td><td>182.72 (+9.68%)</td><td>194.20 <b>(+23.93%)</b></td><td>126.90 (-14.14%)</td><td>56.03 <b>(+160.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.30 (n/a)</td><td>166.60 (n/a)</td><td>156.70 (n/a)</td><td>147.80 (n/a)</td><td>21.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (+3.18%)</td><td>0.15 (+11.46%)</td><td>0.15 (+19.74%)</td><td>0.12 <b>(+42.73%)</b></td><td>0.03 <b>(-25.81%)</b></td><td>213.60 <b>(-29.94%)</b></td><td>171.98 (-14.10%)</td><td>163.70 (-16.48%)</td><td>133.20 (-3.06%)</td><td>31.52 <b>(-50.62%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>304.90 (n/a)</td><td>200.20 (n/a)</td><td>196.00 (n/a)</td><td>137.40 (n/a)</td><td>63.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (-2.78%)</td><td>0.15 (-5.42%)</td><td>0.15 (-3.51%)</td><td>0.12 (-7.32%)</td><td>0.03 <b>(+25.03%)</b></td><td>207.60 (+7.90%)</td><td>166.16 (+7.56%)</td><td>160.40 (+3.62%)</td><td>128.20 (+2.89%)</td><td>37.06 <b>(+40.25%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.40 (n/a)</td><td>154.48 (n/a)</td><td>154.80 (n/a)</td><td>124.60 (n/a)</td><td>26.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.39 (+9.01%)</td><td>0.30 (+6.84%)</td><td>0.30 (+4.25%)</td><td>0.21 (-6.49%)</td><td>0.08 <b>(+57.99%)</b></td><td>235.80 (+6.94%)</td><td>171.34 (-3.36%)</td><td>165.10 (-4.07%)</td><td>126.40 (-8.27%)</td><td>45.86 <b>(+51.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>220.50 (n/a)</td><td>177.30 (n/a)</td><td>172.10 (n/a)</td><td>137.80 (n/a)</td><td>30.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.38 (-0.29%)</td><td>0.33 (+0.50%)</td><td>0.33 (-2.14%)</td><td>0.27 (+0.13%)</td><td>0.04 (-12.85%)</td><td>180.10 (-0.11%)</td><td>150.72 (-0.96%)</td><td>151.00 (+2.17%)</td><td>128.50 (+0.31%)</td><td>20.66 (-13.39%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>180.30 (n/a)</td><td>152.18 (n/a)</td><td>147.80 (n/a)</td><td>128.10 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.39 (+4.33%)</td><td>0.32 (+4.44%)</td><td>0.29 (-4.80%)</td><td>0.27 (+9.14%)</td><td>0.05 (+16.62%)</td><td>181.80 (-8.37%)</td><td>158.32 (-3.91%)</td><td>171.40 (+5.02%)</td><td>126.70 (-4.09%)</td><td>24.24 (+3.14%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>198.40 (n/a)</td><td>164.76 (n/a)</td><td>163.20 (n/a)</td><td>132.10 (n/a)</td><td>23.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.38 (+2.83%)</td><td>0.31 (+11.48%)</td><td>0.33 <b>(+22.22%)</b></td><td>0.24 (+11.70%)</td><td>0.07 (+12.79%)</td><td>207.80 (-10.47%)</td><td>162.52 (-9.85%)</td><td>148.50 (-18.18%)</td><td>128.20 (-2.73%)</td><td>35.93 (+0.18%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>232.10 (n/a)</td><td>180.28 (n/a)</td><td>181.50 (n/a)</td><td>131.80 (n/a)</td><td>35.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.38 (+2.39%)</td><td>0.33 (+5.99%)</td><td>0.35 (+18.29%)</td><td>0.21 (-12.77%)</td><td>0.07 <b>(+29.30%)</b></td><td>233.70 (+14.67%)</td><td>158.04 (-3.50%)</td><td>142.20 (-15.46%)</td><td>128.50 (-2.28%)</td><td>42.94 <b>(+52.67%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>203.80 (n/a)</td><td>163.78 (n/a)</td><td>168.20 (n/a)</td><td>131.50 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.37 (+5.13%)</td><td>0.32 (+10.75%)</td><td>0.31 (+17.38%)</td><td>0.27 (+15.60%)</td><td>0.04 <b>(-32.33%)</b></td><td>182.70 (-13.49%)</td><td>156.32 (-11.39%)</td><td>157.10 (-14.80%)</td><td>131.40 (-4.92%)</td><td>18.72 <b>(-43.98%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>211.20 (n/a)</td><td>176.42 (n/a)</td><td>184.40 (n/a)</td><td>138.20 (n/a)</td><td>33.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.37 (+11.76%)</td><td>0.28 (+8.82%)</td><td>0.27 (+2.93%)</td><td>0.22 <b>(+47.89%)</b></td><td>0.06 (-17.88%)</td><td>225.70 <b>(-32.38%)</b></td><td>181.86 (-12.38%)</td><td>185.20 (-2.88%)</td><td>134.20 (-10.53%)</td><td>36.24 <b>(-51.30%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>333.80 (n/a)</td><td>207.56 (n/a)</td><td>190.70 (n/a)</td><td>150.00 (n/a)</td><td>74.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 <b>(-25.78%)</b></td><td>0.27 (-13.97%)</td><td>0.26 <b>(-27.89%)</b></td><td>0.26 <b>(+39.80%)</b></td><td>0.02 <b>(-83.06%)</b></td><td>189.30 <b>(-28.46%)</b></td><td>180.74 (+6.04%)</td><td>186.20 <b>(+38.75%)</b></td><td>163.70 <b>(+34.73%)</b></td><td>10.48 <b>(-83.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.37 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>264.60 (n/a)</td><td>170.44 (n/a)</td><td>134.20 (n/a)</td><td>121.50 (n/a)</td><td>62.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+17.22%)</td><td>0.02 <b>(+24.37%)</b></td><td>0.02 <b>(+28.44%)</b></td><td>0.01 <b>(+93.37%)</b></td><td>0.00 (-14.83%)</td><td>212.50 <b>(-48.28%)</b></td><td>158.54 <b>(-28.04%)</b></td><td>161.70 <b>(-22.15%)</b></td><td>104.30 (-14.72%)</td><td>39.88 <b>(-64.66%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>410.90 (n/a)</td><td>220.32 (n/a)</td><td>207.70 (n/a)</td><td>122.30 (n/a)</td><td>112.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-17.14%)</td><td>0.02 (-4.83%)</td><td>0.02 (-2.93%)</td><td>0.01 (-2.23%)</td><td>0.00 <b>(-36.29%)</b></td><td>211.00 (+2.28%)</td><td>165.90 (+2.31%)</td><td>163.00 (+3.03%)</td><td>125.30 <b>(+20.71%)</b></td><td>31.45 (-19.84%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>206.30 (n/a)</td><td>162.16 (n/a)</td><td>158.20 (n/a)</td><td>103.80 (n/a)</td><td>39.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-0.53%)</td><td>0.02 (-6.46%)</td><td>0.02 (-11.70%)</td><td>0.01 (-13.17%)</td><td>0.00 <b>(+37.87%)</b></td><td>195.60 (+15.19%)</td><td>160.86 (+8.56%)</td><td>165.10 (+13.32%)</td><td>122.80 (+0.57%)</td><td>29.14 <b>(+59.10%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>169.80 (n/a)</td><td>148.18 (n/a)</td><td>145.70 (n/a)</td><td>122.10 (n/a)</td><td>18.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-4.02%)</td><td>0.02 (-2.84%)</td><td>0.02 (-3.25%)</td><td>0.01 (+5.21%)</td><td>0.00 (-18.06%)</td><td>223.40 (-4.94%)</td><td>167.68 (+1.40%)</td><td>159.90 (+3.36%)</td><td>131.80 (+4.19%)</td><td>34.60 (-18.65%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>235.00 (n/a)</td><td>165.36 (n/a)</td><td>154.70 (n/a)</td><td>126.50 (n/a)</td><td>42.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (+10.06%)</td><td>0.01 (+3.82%)</td><td>0.02 (+5.16%)</td><td>0.01 (-17.15%)</td><td>0.00 <b>(+51.49%)</b></td><td>299.20 <b>(+20.69%)</b></td><td>191.18 (+0.25%)</td><td>173.40 (-4.93%)</td><td>138.60 (-9.17%)</td><td>62.23 <b>(+74.24%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>247.90 (n/a)</td><td>190.70 (n/a)</td><td>182.40 (n/a)</td><td>152.60 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (+10.24%)</td><td>0.02 (+3.41%)</td><td>0.01 (-7.69%)</td><td>0.01 (-6.35%)</td><td>0.00 <b>(+103.93%)</b></td><td>202.90 (+6.79%)</td><td>168.88 (-0.47%)</td><td>188.40 (+8.34%)</td><td>128.90 (-9.29%)</td><td>35.46 <b>(+95.81%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>190.00 (n/a)</td><td>169.68 (n/a)</td><td>173.90 (n/a)</td><td>142.10 (n/a)</td><td>18.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-2.93%)</td><td>0.02 (+0.47%)</td><td>0.02 (+0.44%)</td><td>0.01 (-16.56%)</td><td>0.00 <b>(+23.18%)</b></td><td>255.40 (+19.85%)</td><td>177.82 (+2.01%)</td><td>165.50 (-0.42%)</td><td>134.90 (+3.06%)</td><td>50.20 <b>(+44.21%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>174.32 (n/a)</td><td>166.20 (n/a)</td><td>130.90 (n/a)</td><td>34.81 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.01 (-2.36%)</td><td>0.01 (-15.82%)</td><td>0.01 (-18.38%)</td><td>0.01 <b>(-33.14%)</b></td><td>0.00 <b>(+60.55%)</b></td><td>354.80 <b>(+49.58%)</b></td><td>237.14 <b>(+23.61%)</b></td><td>220.90 <b>(+22.52%)</b></td><td>178.10 (+2.42%)</td><td>68.25 <b>(+158.57%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>237.20 (n/a)</td><td>191.84 (n/a)</td><td>180.30 (n/a)</td><td>173.90 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 <b>(+26.45%)</b></td><td>0.04 (+16.19%)</td><td>0.04 <b>(+21.66%)</b></td><td>0.03 (-4.02%)</td><td>0.01 <b>(+170.72%)</b></td><td>195.80 (+4.20%)</td><td>154.16 (-11.42%)</td><td>149.10 (-17.81%)</td><td>120.30 <b>(-20.96%)</b></td><td>32.29 <b>(+123.54%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>174.04 (n/a)</td><td>181.40 (n/a)</td><td>152.20 (n/a)</td><td>14.44 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 <b>(-25.64%)</b></td><td>0.03 (-7.88%)</td><td>0.03 (+10.17%)</td><td>0.03 (+14.07%)</td><td>0.00 <b>(-73.69%)</b></td><td>190.20 (-12.35%)</td><td>170.02 (+1.82%)</td><td>173.10 (-9.23%)</td><td>155.30 <b>(+34.46%)</b></td><td>14.87 <b>(-68.16%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>166.98 (n/a)</td><td>190.70 (n/a)</td><td>115.50 (n/a)</td><td>46.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (-10.25%)</td><td>0.03 (-16.43%)</td><td>0.03 (-14.94%)</td><td>0.02 <b>(-21.91%)</b></td><td>0.01 (+15.87%)</td><td>213.20 <b>(+28.05%)</b></td><td>172.62 <b>(+22.83%)</b></td><td>174.40 (+17.60%)</td><td>115.50 (+11.49%)</td><td>41.74 <b>(+73.38%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>166.50 (n/a)</td><td>140.54 (n/a)</td><td>148.30 (n/a)</td><td>103.60 (n/a)</td><td>24.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 <b>(-21.92%)</b></td><td>0.03 (-12.92%)</td><td>0.03 (-1.01%)</td><td>0.02 (-8.16%)</td><td>0.00 <b>(-50.50%)</b></td><td>211.20 (+8.92%)</td><td>179.32 (+12.09%)</td><td>177.30 (+0.97%)</td><td>157.10 <b>(+28.04%)</b></td><td>23.14 <b>(-30.23%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>159.98 (n/a)</td><td>175.60 (n/a)</td><td>122.70 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (-13.18%)</td><td>0.03 (+14.01%)</td><td>0.03 (+19.11%)</td><td>0.03 <b>(+81.05%)</b></td><td>0.00 <b>(-63.99%)</b></td><td>197.10 <b>(-44.76%)</b></td><td>169.54 <b>(-20.35%)</b></td><td>163.70 (-16.05%)</td><td>149.30 (+15.11%)</td><td>18.61 <b>(-78.14%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>356.80 (n/a)</td><td>212.86 (n/a)</td><td>195.00 (n/a)</td><td>129.70 (n/a)</td><td>85.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (+4.67%)</td><td>0.03 (+3.79%)</td><td>0.03 (-9.42%)</td><td>0.03 (+15.23%)</td><td>0.01 (+15.21%)</td><td>189.00 (-13.22%)</td><td>160.62 (-3.37%)</td><td>176.10 (+10.41%)</td><td>122.20 (-4.46%)</td><td>30.81 (-5.81%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>166.22 (n/a)</td><td>159.50 (n/a)</td><td>127.90 (n/a)</td><td>32.71 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (+8.73%)</td><td>0.03 (+5.42%)</td><td>0.03 (-1.89%)</td><td>0.03 (+8.51%)</td><td>0.00 (-6.18%)</td><td>176.20 (-7.85%)</td><td>158.88 (-5.43%)</td><td>160.70 (+1.90%)</td><td>136.80 (-8.00%)</td><td>16.12 <b>(-21.47%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.20 (n/a)</td><td>168.00 (n/a)</td><td>157.70 (n/a)</td><td>148.70 (n/a)</td><td>20.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-8.79%)</td><td>0.03 (-3.82%)</td><td>0.02 (-9.49%)</td><td>0.02 (+3.90%)</td><td>0.00 <b>(-44.73%)</b></td><td>224.30 (-3.73%)</td><td>209.10 (+3.31%)</td><td>214.20 (+10.47%)</td><td>194.60 (+9.63%)</td><td>12.67 <b>(-42.60%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.00 (n/a)</td><td>202.40 (n/a)</td><td>193.90 (n/a)</td><td>177.50 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (+18.76%)</td><td>0.07 <b>(+36.82%)</b></td><td>0.08 <b>(+34.32%)</b></td><td>0.05 <b>(+88.20%)</b></td><td>0.01 <b>(-21.66%)</b></td><td>200.40 <b>(-46.87%)</b></td><td>144.94 <b>(-32.28%)</b></td><td>134.20 <b>(-25.57%)</b></td><td>126.00 (-15.78%)</td><td>31.21 <b>(-66.35%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>377.20 (n/a)</td><td>214.02 (n/a)</td><td>180.30 (n/a)</td><td>149.60 (n/a)</td><td>92.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (+2.13%)</td><td>0.07 (+3.28%)</td><td>0.07 (-10.15%)</td><td>0.06 <b>(+33.50%)</b></td><td>0.01 <b>(-44.75%)</b></td><td>167.00 <b>(-25.08%)</b></td><td>151.84 (-6.62%)</td><td>153.90 (+11.36%)</td><td>125.70 (-2.03%)</td><td>17.13 <b>(-58.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>222.90 (n/a)</td><td>162.60 (n/a)</td><td>138.20 (n/a)</td><td>128.30 (n/a)</td><td>41.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (+0.08%)</td><td>0.07 (+8.61%)</td><td>0.06 (-0.54%)</td><td>0.06 <b>(+78.65%)</b></td><td>0.01 <b>(-64.03%)</b></td><td>172.50 <b>(-44.05%)</b></td><td>161.28 (-14.35%)</td><td>166.40 (+0.54%)</td><td>139.60 (-0.07%)</td><td>12.83 <b>(-81.26%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>308.30 (n/a)</td><td>188.30 (n/a)</td><td>165.50 (n/a)</td><td>139.70 (n/a)</td><td>68.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (-0.13%)</td><td>0.07 (+16.46%)</td><td>0.07 (+15.86%)</td><td>0.06 <b>(+64.77%)</b></td><td>0.01 <b>(-60.82%)</b></td><td>177.50 <b>(-39.30%)</b></td><td>156.76 (-19.49%)</td><td>155.50 (-13.66%)</td><td>136.60 (+0.15%)</td><td>14.59 <b>(-76.41%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>292.40 (n/a)</td><td>194.70 (n/a)</td><td>180.10 (n/a)</td><td>136.40 (n/a)</td><td>61.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (-6.02%)</td><td>0.06 (-0.68%)</td><td>0.06 (-2.36%)</td><td>0.05 (-1.71%)</td><td>0.01 (-7.41%)</td><td>210.90 (+1.74%)</td><td>176.38 (+0.59%)</td><td>182.20 (+2.42%)</td><td>139.70 (+6.40%)</td><td>28.44 (+3.34%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>175.34 (n/a)</td><td>177.90 (n/a)</td><td>131.30 (n/a)</td><td>27.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (+2.29%)</td><td>0.06 (+7.79%)</td><td>0.06 <b>(+21.43%)</b></td><td>0.04 <b>(-22.41%)</b></td><td>0.01 <b>(+54.71%)</b></td><td>294.00 <b>(+28.89%)</b></td><td>201.26 (-3.47%)</td><td>185.90 (-17.63%)</td><td>152.10 (-2.25%)</td><td>59.16 <b>(+90.06%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>208.50 (n/a)</td><td>225.70 (n/a)</td><td>155.60 (n/a)</td><td>31.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (-0.91%)</td><td>0.06 (+12.68%)</td><td>0.07 <b>(+22.16%)</b></td><td>0.05 (+18.42%)</td><td>0.01 <b>(-23.63%)</b></td><td>193.40 (-15.55%)</td><td>167.40 (-12.58%)</td><td>156.50 (-18.15%)</td><td>140.10 (+0.94%)</td><td>24.17 <b>(-32.65%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.00 (n/a)</td><td>191.48 (n/a)</td><td>191.20 (n/a)</td><td>138.80 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (+16.21%)</td><td>0.05 (+9.65%)</td><td>0.05 (+12.88%)</td><td>0.05 (+4.18%)</td><td>0.01 <b>(+47.95%)</b></td><td>230.30 (-4.00%)</td><td>201.02 (-8.04%)</td><td>207.20 (-11.42%)</td><td>162.60 (-13.97%)</td><td>29.66 <b>(+23.40%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.90 (n/a)</td><td>218.60 (n/a)</td><td>233.90 (n/a)</td><td>189.00 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (+1.53%)</td><td>0.12 (+8.87%)</td><td>0.12 (+11.76%)</td><td>0.11 (+17.46%)</td><td>0.01 <b>(-48.10%)</b></td><td>186.10 (-14.87%)</td><td>174.92 (-8.74%)</td><td>173.80 (-10.50%)</td><td>162.80 (-1.51%)</td><td>8.55 <b>(-56.36%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>191.68 (n/a)</td><td>194.20 (n/a)</td><td>165.30 (n/a)</td><td>19.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (+8.76%)</td><td>0.13 (+9.22%)</td><td>0.13 (+10.38%)</td><td>0.11 (+2.26%)</td><td>0.01 <b>(+40.56%)</b></td><td>188.20 (-2.23%)</td><td>168.04 (-8.28%)</td><td>165.30 (-9.37%)</td><td>154.90 (-8.07%)</td><td>12.31 <b>(+27.93%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>183.20 (n/a)</td><td>182.40 (n/a)</td><td>168.50 (n/a)</td><td>9.62 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (-8.72%)</td><td>0.13 (+3.49%)</td><td>0.12 (+0.64%)</td><td>0.11 <b>(+69.89%)</b></td><td>0.03 <b>(-47.06%)</b></td><td>189.50 <b>(-41.13%)</b></td><td>163.08 (-13.60%)</td><td>168.00 (-0.65%)</td><td>118.20 (+9.55%)</td><td>26.83 <b>(-67.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>321.90 (n/a)</td><td>188.74 (n/a)</td><td>169.10 (n/a)</td><td>107.90 (n/a)</td><td>83.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (+7.59%)</td><td>0.12 (+9.51%)</td><td>0.12 (+13.89%)</td><td>0.11 (+11.06%)</td><td>0.01 (+4.27%)</td><td>194.60 (-9.95%)</td><td>174.46 (-8.74%)</td><td>170.40 (-12.16%)</td><td>159.30 (-7.06%)</td><td>15.33 (-12.48%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>191.16 (n/a)</td><td>194.00 (n/a)</td><td>171.40 (n/a)</td><td>17.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (-18.31%)</td><td>0.11 (-19.74%)</td><td>0.11 (-15.94%)</td><td>0.09 (-13.94%)</td><td>0.02 <b>(-31.75%)</b></td><td>226.90 (+16.18%)</td><td>191.66 <b>(+22.65%)</b></td><td>192.90 (+19.00%)</td><td>138.40 <b>(+22.37%)</b></td><td>33.87 (-5.19%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>195.30 (n/a)</td><td>156.26 (n/a)</td><td>162.10 (n/a)</td><td>113.10 (n/a)</td><td>35.72 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (-18.94%)</td><td>0.10 (-7.69%)</td><td>0.10 (-13.70%)</td><td>0.08 (+17.49%)</td><td>0.01 <b>(-54.33%)</b></td><td>260.90 (-14.88%)</td><td>212.16 (+3.24%)</td><td>207.00 (+15.84%)</td><td>181.30 <b>(+23.33%)</b></td><td>29.45 <b>(-52.38%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>306.50 (n/a)</td><td>205.50 (n/a)</td><td>178.70 (n/a)</td><td>147.00 (n/a)</td><td>61.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (+3.79%)</td><td>0.12 (+13.63%)</td><td>0.12 (+8.80%)</td><td>0.10 <b>(+54.68%)</b></td><td>0.01 <b>(-61.89%)</b></td><td>200.00 <b>(-35.36%)</b></td><td>181.12 (-15.21%)</td><td>176.40 (-8.08%)</td><td>168.50 (-3.60%)</td><td>12.42 <b>(-77.22%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>309.40 (n/a)</td><td>213.62 (n/a)</td><td>191.90 (n/a)</td><td>174.80 (n/a)</td><td>54.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (-17.59%)</td><td>0.08 (-19.54%)</td><td>0.08 (-17.63%)</td><td>0.06 <b>(-31.63%)</b></td><td>0.02 <b>(+26.58%)</b></td><td>340.60 <b>(+46.24%)</b></td><td>271.30 <b>(+27.20%)</b></td><td>273.60 <b>(+21.38%)</b></td><td>207.60 <b>(+21.33%)</b></td><td>56.99 <b>(+124.14%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>213.28 (n/a)</td><td>225.40 (n/a)</td><td>171.10 (n/a)</td><td>25.43 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>218.20 (n/a)</td><td>181.72 (n/a)</td><td>176.40 (n/a)</td><td>163.10 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.90 (n/a)</td><td>204.68 (n/a)</td><td>211.50 (n/a)</td><td>151.00 (n/a)</td><td>39.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>272.10 (n/a)</td><td>209.80 (n/a)</td><td>217.10 (n/a)</td><td>168.30 (n/a)</td><td>42.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>250.80 (n/a)</td><td>222.54 (n/a)</td><td>228.50 (n/a)</td><td>176.70 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>168.02 (n/a)</td><td>168.70 (n/a)</td><td>137.90 (n/a)</td><td>22.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>187.22 (n/a)</td><td>182.20 (n/a)</td><td>159.80 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>179.42 (n/a)</td><td>157.40 (n/a)</td><td>149.90 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>207.56 (n/a)</td><td>210.80 (n/a)</td><td>196.90 (n/a)</td><td>10.20 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>177.06 (n/a)</td><td>172.30 (n/a)</td><td>152.80 (n/a)</td><td>17.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>194.60 (n/a)</td><td>179.58 (n/a)</td><td>173.70 (n/a)</td><td>169.60 (n/a)</td><td>11.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>226.10 (n/a)</td><td>196.06 (n/a)</td><td>216.00 (n/a)</td><td>156.60 (n/a)</td><td>36.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>348.50 (n/a)</td><td>239.56 (n/a)</td><td>227.60 (n/a)</td><td>184.70 (n/a)</td><td>65.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 <b>(-26.51%)</b></td><td>0.27 (-16.89%)</td><td>0.26 (-12.66%)</td><td>0.24 (-1.11%)</td><td>0.02 <b>(-66.52%)</b></td><td>207.50 (+1.12%)</td><td>186.54 (+16.40%)</td><td>189.70 (+14.55%)</td><td>162.90 <b>(+36.09%)</b></td><td>16.33 <b>(-53.49%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>205.20 (n/a)</td><td>160.26 (n/a)</td><td>165.60 (n/a)</td><td>119.70 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>208.10 (n/a)</td><td>184.50 (n/a)</td><td>184.30 (n/a)</td><td>157.00 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>194.50 (n/a)</td><td>188.70 (n/a)</td><td>189.50 (n/a)</td><td>179.70 (n/a)</td><td>5.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>271.80 (n/a)</td><td>221.06 (n/a)</td><td>205.50 (n/a)</td><td>199.00 (n/a)</td><td>30.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.60 (n/a)</td><td>161.92 (n/a)</td><td>154.00 (n/a)</td><td>145.20 (n/a)</td><td>18.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>169.60 (n/a)</td><td>178.10 (n/a)</td><td>123.60 (n/a)</td><td>39.46 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.00 (n/a)</td><td>181.26 (n/a)</td><td>189.00 (n/a)</td><td>157.90 (n/a)</td><td>14.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>228.90 (n/a)</td><td>187.72 (n/a)</td><td>176.80 (n/a)</td><td>151.00 (n/a)</td><td>38.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>239.40 (n/a)</td><td>192.02 (n/a)</td><td>206.00 (n/a)</td><td>114.60 (n/a)</td><td>48.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.20 (n/a)</td><td>190.10 (n/a)</td><td>182.10 (n/a)</td><td>159.20 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>183.44 (n/a)</td><td>190.60 (n/a)</td><td>154.30 (n/a)</td><td>23.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>252.20 (n/a)</td><td>177.88 (n/a)</td><td>163.80 (n/a)</td><td>135.50 (n/a)</td><td>46.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>181.82 (n/a)</td><td>167.80 (n/a)</td><td>158.70 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>239.90 (n/a)</td><td>196.94 (n/a)</td><td>201.50 (n/a)</td><td>148.30 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>189.14 (n/a)</td><td>185.40 (n/a)</td><td>167.20 (n/a)</td><td>19.74 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>203.62 (n/a)</td><td>203.40 (n/a)</td><td>187.10 (n/a)</td><td>12.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>231.00 (n/a)</td><td>180.96 (n/a)</td><td>173.70 (n/a)</td><td>158.90 (n/a)</td><td>29.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.43 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>239.10 (n/a)</td><td>182.90 (n/a)</td><td>202.70 (n/a)</td><td>114.30 (n/a)</td><td>50.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>250.10 (n/a)</td><td>189.28 (n/a)</td><td>187.10 (n/a)</td><td>141.50 (n/a)</td><td>41.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>15.52 (+6.40%)</td><td>14.52 (+2.31%)</td><td>14.41 (+0.71%)</td><td>14.01 (+6.32%)</td><td>0.59 (+0.16%)</td><td>3977.00 (-5.95%)</td><td>3841.68 (-2.27%)</td><td>3864.60 (-0.71%)</td><td>3589.20 (-6.01%)</td><td>149.19 (-12.50%)</td><td>14957.80 (+6.40%)</td><td>13992.46 (+2.31%)</td><td>13892.02 (+0.71%)</td><td>13499.48 (+6.32%)</td><td>565.57 (+0.16%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.59 (n/a)</td><td>14.19 (n/a)</td><td>14.31 (n/a)</td><td>13.17 (n/a)</td><td>0.59 (n/a)</td><td>4228.40 (n/a)</td><td>3930.98 (n/a)</td><td>3892.10 (n/a)</td><td>3818.80 (n/a)</td><td>170.51 (n/a)</td><td>14058.67 (n/a)</td><td>13677.09 (n/a)</td><td>13793.98 (n/a)</td><td>12696.88 (n/a)</td><td>564.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>16.18 (+0.01%)</td><td>13.36 (-9.15%)</td><td>13.39 (-8.16%)</td><td>9.63 <b>(-29.77%)</b></td><td>2.46 <b>(+173.00%)</b></td><td>1361.40 <b>(+42.39%)</b></td><td>1011.62 (+13.21%)</td><td>979.10 (+8.89%)</td><td>810.00 (+0.00%)</td><td>212.01 <b>(+302.98%)</b></td><td>10605.47 (+0.01%)</td><td>8758.18 (-9.15%)</td><td>8773.43 (-8.16%)</td><td>6309.43 <b>(-29.77%)</b></td><td>1612.19 <b>(+173.00%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>16.18 (n/a)</td><td>14.71 (n/a)</td><td>14.58 (n/a)</td><td>13.71 (n/a)</td><td>0.90 (n/a)</td><td>956.10 (n/a)</td><td>893.60 (n/a)</td><td>899.20 (n/a)</td><td>810.00 (n/a)</td><td>52.61 (n/a)</td><td>10604.70 (n/a)</td><td>9640.38 (n/a)</td><td>9552.75 (n/a)</td><td>8984.53 (n/a)</td><td>590.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>15.21 (-0.15%)</td><td>13.93 (-0.55%)</td><td>14.13 (+0.43%)</td><td>12.61 (+0.37%)</td><td>1.19 <b>(+25.03%)</b></td><td>4417.80 (-0.37%)</td><td>4023.72 (+0.77%)</td><td>3942.30 (-0.43%)</td><td>3661.80 (+0.15%)</td><td>347.47 <b>(+24.36%)</b></td><td>14661.29 (-0.15%)</td><td>13421.66 (-0.55%)</td><td>13618.15 (+0.43%)</td><td>12152.47 (+0.37%)</td><td>1145.61 <b>(+25.03%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>15.24 (n/a)</td><td>14.00 (n/a)</td><td>14.07 (n/a)</td><td>12.56 (n/a)</td><td>0.95 (n/a)</td><td>4434.30 (n/a)</td><td>3993.04 (n/a)</td><td>3959.20 (n/a)</td><td>3656.40 (n/a)</td><td>279.40 (n/a)</td><td>14683.09 (n/a)</td><td>13496.38 (n/a)</td><td>13559.93 (n/a)</td><td>12107.34 (n/a)</td><td>916.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>16.66 (+2.41%)</td><td>14.46 (+0.53%)</td><td>14.48 (-2.77%)</td><td>11.07 (+3.83%)</td><td>2.12 (-2.05%)</td><td>1613.30 (-3.68%)</td><td>1259.50 (-0.77%)</td><td>1233.60 (+2.85%)</td><td>1072.00 (-2.35%)</td><td>210.29 (-9.01%)</td><td>12520.39 (+2.41%)</td><td>10867.81 (+0.53%)</td><td>10880.26 (-2.77%)</td><td>8319.59 (+3.83%)</td><td>1593.72 (-2.05%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>16.27 (n/a)</td><td>14.38 (n/a)</td><td>14.89 (n/a)</td><td>10.66 (n/a)</td><td>2.16 (n/a)</td><td>1675.00 (n/a)</td><td>1269.24 (n/a)</td><td>1199.40 (n/a)</td><td>1097.80 (n/a)</td><td>231.12 (n/a)</td><td>12226.18 (n/a)</td><td>10810.73 (n/a)</td><td>11190.28 (n/a)</td><td>8012.91 (n/a)</td><td>1627.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>10.96 (-1.81%)</td><td>10.65 (-1.26%)</td><td>10.64 (-0.35%)</td><td>10.39 (-1.08%)</td><td>0.22 (-14.69%)</td><td>7882.20 (+1.10%)</td><td>7697.92 (+1.26%)</td><td>7702.00 (+0.35%)</td><td>7472.70 (+1.85%)</td><td>156.45 (-12.04%)</td><td>14368.82 (-1.81%)</td><td>13953.13 (-1.26%)</td><td>13941.15 (-0.35%)</td><td>13622.43 (-1.08%)</td><td>285.38 (-14.69%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>11.17 (n/a)</td><td>10.78 (n/a)</td><td>10.67 (n/a)</td><td>10.51 (n/a)</td><td>0.26 (n/a)</td><td>7796.80 (n/a)</td><td>7601.98 (n/a)</td><td>7674.80 (n/a)</td><td>7337.10 (n/a)</td><td>177.87 (n/a)</td><td>14634.37 (n/a)</td><td>14130.77 (n/a)</td><td>13990.51 (n/a)</td><td>13771.66 (n/a)</td><td>334.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>16.12 (+9.31%)</td><td>13.26 (+3.13%)</td><td>14.57 (+15.74%)</td><td>9.94 (-7.69%)</td><td>2.68 <b>(+74.35%)</b></td><td>2163.50 (+8.33%)</td><td>1679.94 (-0.71%)</td><td>1475.20 (-13.60%)</td><td>1333.20 (-8.52%)</td><td>363.64 <b>(+75.04%)</b></td><td>12886.48 (+9.31%)</td><td>10595.31 (+3.13%)</td><td>11645.55 (+15.74%)</td><td>7940.70 (-7.69%)</td><td>2139.61 <b>(+74.35%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.75 (n/a)</td><td>12.85 (n/a)</td><td>12.59 (n/a)</td><td>10.76 (n/a)</td><td>1.54 (n/a)</td><td>1997.20 (n/a)</td><td>1692.02 (n/a)</td><td>1707.40 (n/a)</td><td>1457.30 (n/a)</td><td>207.75 (n/a)</td><td>11788.48 (n/a)</td><td>10273.31 (n/a)</td><td>10061.95 (n/a)</td><td>8602.19 (n/a)</td><td>1227.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>11.00 (+0.50%)</td><td>10.71 (-0.45%)</td><td>10.82 (-0.79%)</td><td>10.36 (-0.07%)</td><td>0.28 (+10.08%)</td><td>7908.00 (+0.07%)</td><td>7654.60 (+0.46%)</td><td>7568.30 (+0.79%)</td><td>7447.20 (-0.49%)</td><td>204.86 (+10.14%)</td><td>14418.07 (+0.50%)</td><td>14035.38 (-0.45%)</td><td>14187.29 (-0.79%)</td><td>13577.93 (-0.07%)</td><td>372.81 (+10.08%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>10.95 (n/a)</td><td>10.76 (n/a)</td><td>10.91 (n/a)</td><td>10.37 (n/a)</td><td>0.26 (n/a)</td><td>7902.70 (n/a)</td><td>7619.72 (n/a)</td><td>7508.80 (n/a)</td><td>7484.10 (n/a)</td><td>186.01 (n/a)</td><td>14347.00 (n/a)</td><td>14098.26 (n/a)</td><td>14299.81 (n/a)</td><td>13587.04 (n/a)</td><td>338.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.58 (+0.38%)</td><td>3.35 (-4.59%)</td><td>3.03 (-2.28%)</td><td>2.92 (-0.70%)</td><td>0.70 (+1.75%)</td><td>472.10 (+0.70%)</td><td>423.10 (+4.89%)</td><td>454.90 (+2.34%)</td><td>300.80 (-0.40%)</td><td>72.16 (+0.88%)</td><td>892.40 (+0.38%)</td><td>653.13 (-4.59%)</td><td>590.13 (-2.28%)</td><td>568.60 (-0.70%)</td><td>137.44 (+1.75%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>4.56 (n/a)</td><td>3.51 (n/a)</td><td>3.10 (n/a)</td><td>2.94 (n/a)</td><td>0.69 (n/a)</td><td>468.80 (n/a)</td><td>403.36 (n/a)</td><td>444.50 (n/a)</td><td>302.00 (n/a)</td><td>71.53 (n/a)</td><td>888.99 (n/a)</td><td>684.59 (n/a)</td><td>603.92 (n/a)</td><td>572.59 (n/a)</td><td>135.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.79 (-15.22%)</td><td>3.91 (-9.27%)</td><td>3.69 (-1.41%)</td><td>3.52 (+0.66%)</td><td>0.51 <b>(-46.01%)</b></td><td>391.20 (-0.66%)</td><td>356.20 (+7.67%)</td><td>372.80 (+1.44%)</td><td>287.10 (+17.95%)</td><td>40.56 <b>(-38.35%)</b></td><td>935.03 (-15.22%)</td><td>762.67 (-9.27%)</td><td>720.03 (-1.41%)</td><td>686.21 (+0.66%)</td><td>99.26 <b>(-46.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.65 (n/a)</td><td>4.31 (n/a)</td><td>3.74 (n/a)</td><td>3.49 (n/a)</td><td>0.94 (n/a)</td><td>393.80 (n/a)</td><td>330.82 (n/a)</td><td>367.50 (n/a)</td><td>243.40 (n/a)</td><td>65.80 (n/a)</td><td>1102.89 (n/a)</td><td>840.58 (n/a)</td><td>730.36 (n/a)</td><td>681.69 (n/a)</td><td>183.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.34 <b>(-21.30%)</b></td><td>4.65 (-6.77%)</td><td>4.34 (+5.56%)</td><td>3.75 (+1.55%)</td><td>1.03 <b>(-43.34%)</b></td><td>366.80 (-1.53%)</td><td>305.98 (+2.19%)</td><td>317.20 (-5.29%)</td><td>217.00 <b>(+27.05%)</b></td><td>58.38 <b>(-29.54%)</b></td><td>1237.06 <b>(-21.30%)</b></td><td>907.50 (-6.77%)</td><td>846.20 (+5.56%)</td><td>731.79 (+1.55%)</td><td>200.37 <b>(-43.34%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.06 (n/a)</td><td>4.99 (n/a)</td><td>4.11 (n/a)</td><td>3.69 (n/a)</td><td>1.81 (n/a)</td><td>372.50 (n/a)</td><td>299.42 (n/a)</td><td>334.90 (n/a)</td><td>170.80 (n/a)</td><td>82.85 (n/a)</td><td>1571.77 (n/a)</td><td>973.42 (n/a)</td><td>801.59 (n/a)</td><td>720.60 (n/a)</td><td>353.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>5.28 <b>(-20.39%)</b></td><td>4.24 (-10.56%)</td><td>3.71 (-5.04%)</td><td>3.47 (-3.13%)</td><td>0.94 <b>(-34.68%)</b></td><td>396.90 (+3.22%)</td><td>337.32 (+8.39%)</td><td>371.30 (+5.30%)</td><td>260.50 <b>(+25.60%)</b></td><td>69.91 (-17.67%)</td><td>1030.44 <b>(-20.39%)</b></td><td>826.19 (-10.56%)</td><td>722.91 (-5.04%)</td><td>676.25 (-3.13%)</td><td>183.71 <b>(-34.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.64 (n/a)</td><td>4.74 (n/a)</td><td>3.90 (n/a)</td><td>3.58 (n/a)</td><td>1.44 (n/a)</td><td>384.50 (n/a)</td><td>311.22 (n/a)</td><td>352.60 (n/a)</td><td>207.40 (n/a)</td><td>84.91 (n/a)</td><td>1294.39 (n/a)</td><td>923.73 (n/a)</td><td>761.30 (n/a)</td><td>698.14 (n/a)</td><td>281.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.00 (+8.35%)</td><td>3.44 (+4.91%)</td><td>3.39 (+3.22%)</td><td>3.11 (+5.20%)</td><td>0.33 <b>(+24.58%)</b></td><td>442.60 (-4.94%)</td><td>402.38 (-4.50%)</td><td>405.40 (-3.11%)</td><td>344.40 (-7.69%)</td><td>36.07 (+7.88%)</td><td>779.51 (+8.35%)</td><td>671.78 (+4.91%)</td><td>662.18 (+3.22%)</td><td>606.45 (+5.20%)</td><td>64.77 <b>(+24.58%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.69 (n/a)</td><td>3.28 (n/a)</td><td>3.29 (n/a)</td><td>2.96 (n/a)</td><td>0.27 (n/a)</td><td>465.60 (n/a)</td><td>421.36 (n/a)</td><td>418.40 (n/a)</td><td>373.10 (n/a)</td><td>33.44 (n/a)</td><td>719.43 (n/a)</td><td>640.31 (n/a)</td><td>641.54 (n/a)</td><td>576.49 (n/a)</td><td>51.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.89 (-4.94%)</td><td>3.66 (+1.82%)</td><td>3.20 (-0.51%)</td><td>3.08 (-0.07%)</td><td>0.77 (-12.39%)</td><td>446.50 (+0.07%)</td><td>387.96 (-2.39%)</td><td>429.50 (+0.49%)</td><td>281.40 (+5.24%)</td><td>70.23 (-4.88%)</td><td>954.08 (-4.94%)</td><td>713.43 (+1.82%)</td><td>624.94 (-0.51%)</td><td>601.17 (-0.07%)</td><td>149.33 (-12.39%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.15 (n/a)</td><td>3.59 (n/a)</td><td>3.22 (n/a)</td><td>3.08 (n/a)</td><td>0.87 (n/a)</td><td>446.20 (n/a)</td><td>397.46 (n/a)</td><td>427.40 (n/a)</td><td>267.40 (n/a)</td><td>73.83 (n/a)</td><td>1003.69 (n/a)</td><td>700.65 (n/a)</td><td>628.13 (n/a)</td><td>601.59 (n/a)</td><td>170.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.62 <b>(+31.90%)</b></td><td>3.63 (+14.99%)</td><td>3.27 (+5.26%)</td><td>2.97 (-0.42%)</td><td>0.76 <b>(+279.67%)</b></td><td>463.70 (+0.41%)</td><td>392.22 (-10.35%)</td><td>421.00 (-5.01%)</td><td>298.00 <b>(-24.17%)</b></td><td>76.98 <b>(+195.02%)</b></td><td>900.92 <b>(+31.90%)</b></td><td>707.70 (+14.99%)</td><td>637.55 (+5.26%)</td><td>578.88 (-0.42%)</td><td>148.70 <b>(+279.66%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.50 (n/a)</td><td>3.16 (n/a)</td><td>3.11 (n/a)</td><td>2.98 (n/a)</td><td>0.20 (n/a)</td><td>461.80 (n/a)</td><td>437.50 (n/a)</td><td>443.20 (n/a)</td><td>393.00 (n/a)</td><td>26.09 (n/a)</td><td>683.05 (n/a)</td><td>615.46 (n/a)</td><td>605.70 (n/a)</td><td>581.33 (n/a)</td><td>39.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.92 <b>(+24.65%)</b></td><td>1.44 <b>(+20.70%)</b></td><td>1.19 (+3.10%)</td><td>1.12 (+9.33%)</td><td>0.40 <b>(+100.98%)</b></td><td>357.20 (-8.55%)</td><td>294.00 (-13.97%)</td><td>337.90 (-3.01%)</td><td>209.50 (-19.76%)</td><td>73.42 <b>(+51.88%)</b></td><td>160.18 <b>(+24.65%)</b></td><td>120.74 <b>(+20.70%)</b></td><td>99.30 (+3.10%)</td><td>93.93 (+9.33%)</td><td>33.13 <b>(+100.98%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.54 (n/a)</td><td>1.20 (n/a)</td><td>1.15 (n/a)</td><td>1.03 (n/a)</td><td>0.20 (n/a)</td><td>390.60 (n/a)</td><td>341.76 (n/a)</td><td>348.40 (n/a)</td><td>261.10 (n/a)</td><td>48.34 (n/a)</td><td>128.50 (n/a)</td><td>100.03 (n/a)</td><td>96.31 (n/a)</td><td>85.91 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>9.95 <b>(+42.33%)</b></td><td>5.89 (+14.51%)</td><td>4.89 (+3.85%)</td><td>4.52 (+2.69%)</td><td>2.28 <b>(+116.07%)</b></td><td>428.20 (-2.62%)</td><td>356.96 (-7.63%)</td><td>395.00 (-3.71%)</td><td>194.30 <b>(-29.75%)</b></td><td>93.25 <b>(+44.57%)</b></td><td>2071.79 <b>(+42.33%)</b></td><td>1226.67 (+14.51%)</td><td>1019.47 (+3.85%)</td><td>940.44 (+2.69%)</td><td>475.34 <b>(+116.07%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.99 (n/a)</td><td>5.14 (n/a)</td><td>4.71 (n/a)</td><td>4.40 (n/a)</td><td>1.06 (n/a)</td><td>439.70 (n/a)</td><td>386.46 (n/a)</td><td>410.20 (n/a)</td><td>276.60 (n/a)</td><td>64.50 (n/a)</td><td>1455.63 (n/a)</td><td>1071.21 (n/a)</td><td>981.72 (n/a)</td><td>915.81 (n/a)</td><td>220.00 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>18.69 (+15.87%)</td><td>13.69 (+5.20%)</td><td>11.93 (+0.15%)</td><td>11.19 (+2.54%)</td><td>3.12 <b>(+33.78%)</b></td><td>492.00 (-2.48%)</td><td>416.92 (-3.81%)</td><td>461.40 (-0.15%)</td><td>294.60 (-13.68%)</td><td>81.82 (+12.14%)</td><td>7290.45 (+15.87%)</td><td>5340.56 (+5.20%)</td><td>4654.69 (+0.15%)</td><td>4364.74 (+2.54%)</td><td>1215.89 <b>(+33.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>16.13 (n/a)</td><td>13.01 (n/a)</td><td>11.91 (n/a)</td><td>10.91 (n/a)</td><td>2.33 (n/a)</td><td>504.50 (n/a)</td><td>433.44 (n/a)</td><td>462.10 (n/a)</td><td>341.30 (n/a)</td><td>72.96 (n/a)</td><td>6291.70 (n/a)</td><td>5076.49 (n/a)</td><td>4647.64 (n/a)</td><td>4256.57 (n/a)</td><td>908.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>10.84 <b>(+31.69%)</b></td><td>8.41 (+11.54%)</td><td>8.85 (+11.41%)</td><td>5.69 (-2.23%)</td><td>1.89 <b>(+88.27%)</b></td><td>968.30 (+2.28%)</td><td>685.30 (-7.72%)</td><td>622.10 (-10.24%)</td><td>507.90 <b>(-24.06%)</b></td><td>174.04 <b>(+49.06%)</b></td><td>4228.27 <b>(+31.69%)</b></td><td>3279.98 (+11.54%)</td><td>3451.80 (+11.41%)</td><td>2217.89 (-2.23%)</td><td>736.78 <b>(+88.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.23 (n/a)</td><td>7.54 (n/a)</td><td>7.94 (n/a)</td><td>5.82 (n/a)</td><td>1.00 (n/a)</td><td>946.70 (n/a)</td><td>742.66 (n/a)</td><td>693.10 (n/a)</td><td>668.80 (n/a)</td><td>116.76 (n/a)</td><td>3210.89 (n/a)</td><td>2940.73 (n/a)</td><td>3098.34 (n/a)</td><td>2268.46 (n/a)</td><td>391.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>11.02 (+13.28%)</td><td>9.84 (+7.74%)</td><td>10.42 (+13.01%)</td><td>8.33 (+2.40%)</td><td>1.16 <b>(+85.85%)</b></td><td>696.00 (-2.34%)</td><td>596.50 (-6.47%)</td><td>556.50 (-11.50%)</td><td>526.10 (-11.73%)</td><td>73.29 <b>(+59.87%)</b></td><td>4591.93 (+13.28%)</td><td>4097.36 (+7.74%)</td><td>4341.51 (+13.01%)</td><td>3471.07 (+2.40%)</td><td>481.37 <b>(+85.85%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.73 (n/a)</td><td>9.13 (n/a)</td><td>9.22 (n/a)</td><td>8.14 (n/a)</td><td>0.62 (n/a)</td><td>712.70 (n/a)</td><td>637.76 (n/a)</td><td>628.80 (n/a)</td><td>596.00 (n/a)</td><td>45.84 (n/a)</td><td>4053.46 (n/a)</td><td>3802.91 (n/a)</td><td>3841.82 (n/a)</td><td>3389.73 (n/a)</td><td>259.01 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>137.86 (n/a)</td><td>128.10 (n/a)</td><td>81.00 (n/a)</td><td>44.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.00 (n/a)</td><td>162.26 (n/a)</td><td>149.90 (n/a)</td><td>134.50 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>155.76 (n/a)</td><td>133.00 (n/a)</td><td>118.70 (n/a)</td><td>45.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>271.70 (n/a)</td><td>181.38 (n/a)</td><td>167.70 (n/a)</td><td>131.40 (n/a)</td><td>53.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.10 (n/a)</td><td>174.50 (n/a)</td><td>165.30 (n/a)</td><td>143.60 (n/a)</td><td>37.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.40 (n/a)</td><td>188.90 (n/a)</td><td>201.60 (n/a)</td><td>148.80 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.90 (n/a)</td><td>165.16 (n/a)</td><td>134.20 (n/a)</td><td>124.70 (n/a)</td><td>55.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.60 (n/a)</td><td>207.32 (n/a)</td><td>219.00 (n/a)</td><td>174.80 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.00 (n/a)</td><td>169.06 (n/a)</td><td>152.20 (n/a)</td><td>128.20 (n/a)</td><td>46.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>168.10 (n/a)</td><td>165.10 (n/a)</td><td>140.70 (n/a)</td><td>28.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>177.76 (n/a)</td><td>168.50 (n/a)</td><td>139.20 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>174.58 (n/a)</td><td>175.10 (n/a)</td><td>149.50 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.90 (n/a)</td><td>185.36 (n/a)</td><td>194.20 (n/a)</td><td>145.70 (n/a)</td><td>22.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.50 (n/a)</td><td>190.56 (n/a)</td><td>196.80 (n/a)</td><td>158.40 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>158.74 (n/a)</td><td>138.70 (n/a)</td><td>115.00 (n/a)</td><td>40.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.00 (n/a)</td><td>200.18 (n/a)</td><td>209.80 (n/a)</td><td>142.60 (n/a)</td><td>40.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.20 (n/a)</td><td>156.04 (n/a)</td><td>164.30 (n/a)</td><td>128.30 (n/a)</td><td>17.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.60 (n/a)</td><td>166.96 (n/a)</td><td>167.70 (n/a)</td><td>124.30 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>253.20 (n/a)</td><td>174.54 (n/a)</td><td>165.80 (n/a)</td><td>129.00 (n/a)</td><td>47.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.40 (n/a)</td><td>173.42 (n/a)</td><td>164.80 (n/a)</td><td>137.50 (n/a)</td><td>32.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>313.00 (n/a)</td><td>224.34 (n/a)</td><td>213.00 (n/a)</td><td>180.60 (n/a)</td><td>51.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>284.30 (n/a)</td><td>209.68 (n/a)</td><td>197.30 (n/a)</td><td>158.60 (n/a)</td><td>46.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>246.70 (n/a)</td><td>170.36 (n/a)</td><td>157.90 (n/a)</td><td>113.90 (n/a)</td><td>53.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>195.66 (n/a)</td><td>188.40 (n/a)</td><td>177.60 (n/a)</td><td>15.91 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>225.60 (n/a)</td><td>173.32 (n/a)</td><td>177.30 (n/a)</td><td>122.50 (n/a)</td><td>45.71 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>200.20 (n/a)</td><td>167.18 (n/a)</td><td>160.30 (n/a)</td><td>132.40 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>192.50 (n/a)</td><td>155.70 (n/a)</td><td>140.70 (n/a)</td><td>128.60 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>195.30 (n/a)</td><td>158.12 (n/a)</td><td>142.60 (n/a)</td><td>129.80 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>228.30 (n/a)</td><td>185.04 (n/a)</td><td>195.30 (n/a)</td><td>142.90 (n/a)</td><td>34.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>218.70 (n/a)</td><td>192.80 (n/a)</td><td>198.80 (n/a)</td><td>157.70 (n/a)</td><td>25.96 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.10 (n/a)</td><td>172.10 (n/a)</td><td>156.90 (n/a)</td><td>133.40 (n/a)</td><td>33.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>329.60 (n/a)</td><td>216.16 (n/a)</td><td>173.90 (n/a)</td><td>151.10 (n/a)</td><td>75.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.12 (+0.14%)</td><td>4.11 (+0.13%)</td><td>4.11 (+0.20%)</td><td>4.09 (+0.10%)</td><td>0.01 (+8.04%)</td><td>19229.80 (-0.10%)</td><td>19142.08 (-0.13%)</td><td>19119.90 (-0.19%)</td><td>19094.60 (-0.14%)</td><td>53.74 (+7.70%)</td><td>2811.64 (+0.14%)</td><td>2804.68 (+0.13%)</td><td>2807.92 (+0.20%)</td><td>2791.87 (+0.10%)</td><td>7.86 (+8.05%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>4.11 (n/a)</td><td>4.10 (n/a)</td><td>4.11 (n/a)</td><td>4.09 (n/a)</td><td>0.01 (n/a)</td><td>19249.90 (n/a)</td><td>19166.74 (n/a)</td><td>19157.20 (n/a)</td><td>19120.60 (n/a)</td><td>49.89 (n/a)</td><td>2807.81 (n/a)</td><td>2801.07 (n/a)</td><td>2802.46 (n/a)</td><td>2788.96 (n/a)</td><td>7.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.82 (+14.75%)</td><td>4.25 (+5.67%)</td><td>4.12 (+1.20%)</td><td>4.04 (+10.33%)</td><td>0.32 <b>(+58.00%)</b></td><td>2325.30 (-9.36%)</td><td>2223.24 (-5.17%)</td><td>2280.90 (-1.19%)</td><td>1950.60 (-12.85%)</td><td>155.07 <b>(+22.05%)</b></td><td>1896.56 (+14.75%)</td><td>1671.07 (+5.67%)</td><td>1621.88 (+1.20%)</td><td>1590.89 (+10.33%)</td><td>127.66 <b>(+58.00%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>4.20 (n/a)</td><td>4.02 (n/a)</td><td>4.07 (n/a)</td><td>3.67 (n/a)</td><td>0.21 (n/a)</td><td>2565.50 (n/a)</td><td>2344.54 (n/a)</td><td>2308.40 (n/a)</td><td>2238.20 (n/a)</td><td>127.05 (n/a)</td><td>1652.84 (n/a)</td><td>1581.38 (n/a)</td><td>1602.60 (n/a)</td><td>1441.95 (n/a)</td><td>80.80 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.10 (-8.37%)</td><td>0.94 (-6.50%)</td><td>1.06 (+3.46%)</td><td>0.68 (-6.45%)</td><td>0.20 (+16.14%)</td><td>324.30 (+6.89%)</td><td>245.64 (+8.36%)</td><td>208.10 (-3.34%)</td><td>200.40 (+9.15%)</td><td>57.47 <b>(+27.54%)</b></td><td>47.08 (-8.37%)</td><td>40.00 (-6.50%)</td><td>45.35 (+3.46%)</td><td>29.10 (-6.45%)</td><td>8.49 (+16.14%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.20 (n/a)</td><td>1.00 (n/a)</td><td>1.03 (n/a)</td><td>0.73 (n/a)</td><td>0.17 (n/a)</td><td>303.40 (n/a)</td><td>226.68 (n/a)</td><td>215.30 (n/a)</td><td>183.60 (n/a)</td><td>45.06 (n/a)</td><td>51.39 (n/a)</td><td>42.78 (n/a)</td><td>43.84 (n/a)</td><td>31.11 (n/a)</td><td>7.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.23 (-5.63%)</td><td>1.02 (+3.82%)</td><td>1.11 (+17.42%)</td><td>0.67 (-7.67%)</td><td>0.22 (-5.86%)</td><td>330.70 (+8.28%)</td><td>228.10 (-3.51%)</td><td>199.20 (-14.84%)</td><td>180.50 (+5.99%)</td><td>60.89 (+10.35%)</td><td>52.29 (-5.63%)</td><td>43.36 (+3.82%)</td><td>47.38 (+17.42%)</td><td>28.54 (-7.67%)</td><td>9.41 (-5.86%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.30 (n/a)</td><td>0.98 (n/a)</td><td>0.95 (n/a)</td><td>0.72 (n/a)</td><td>0.23 (n/a)</td><td>305.40 (n/a)</td><td>236.40 (n/a)</td><td>233.90 (n/a)</td><td>170.30 (n/a)</td><td>55.18 (n/a)</td><td>55.41 (n/a)</td><td>41.76 (n/a)</td><td>40.35 (n/a)</td><td>30.91 (n/a)</td><td>9.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.53 (+0.01%)</td><td>0.53 (+0.01%)</td><td>0.53 (-0.01%)</td><td>0.53 (+0.01%)</td><td>0.00 (-2.66%)</td><td>47833.20 (-0.01%)</td><td>47790.70 (-0.01%)</td><td>47790.10 (+0.01%)</td><td>47754.80 (-0.01%)</td><td>32.84 (-2.59%)</td><td>359.75 (+0.01%)</td><td>359.48 (+0.01%)</td><td>359.49 (-0.01%)</td><td>359.16 (+0.01%)</td><td>0.25 (-2.65%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47840.10 (n/a)</td><td>47797.00 (n/a)</td><td>47785.40 (n/a)</td><td>47760.90 (n/a)</td><td>33.71 (n/a)</td><td>359.71 (n/a)</td><td>359.43 (n/a)</td><td>359.52 (n/a)</td><td>359.11 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (-1.33%)</td><td>0.21 (-0.23%)</td><td>0.21 (-0.22%)</td><td>0.21 (+0.59%)</td><td>0.00 <b>(-52.57%)</b></td><td>119506.30 (-0.59%)</td><td>118407.62 (+0.22%)</td><td>118202.00 (+0.22%)</td><td>117359.10 (+1.35%)</td><td>809.25 <b>(-52.20%)</b></td><td>146.39 (-1.33%)</td><td>145.10 (-0.23%)</td><td>145.34 (-0.22%)</td><td>143.76 (+0.59%)</td><td>0.99 <b>(-52.57%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120209.80 (n/a)</td><td>118151.12 (n/a)</td><td>117946.80 (n/a)</td><td>115795.50 (n/a)</td><td>1693.13 (n/a)</td><td>148.36 (n/a)</td><td>145.43 (n/a)</td><td>145.66 (n/a)</td><td>142.92 (n/a)</td><td>2.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.91 (+0.51%)</td><td>0.90 (+0.24%)</td><td>0.91 (+0.42%)</td><td>0.89 (-0.63%)</td><td>0.01 <b>(+89.81%)</b></td><td>28279.00 (+0.63%)</td><td>27858.76 (-0.24%)</td><td>27757.90 (-0.42%)</td><td>27636.00 (-0.50%)</td><td>251.39 <b>(+90.28%)</b></td><td>621.65 (+0.51%)</td><td>616.72 (+0.24%)</td><td>618.92 (+0.42%)</td><td>607.51 (-0.63%)</td><td>5.52 <b>(+89.81%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>28101.00 (n/a)</td><td>27925.30 (n/a)</td><td>27874.50 (n/a)</td><td>27776.00 (n/a)</td><td>132.11 (n/a)</td><td>618.52 (n/a)</td><td>615.22 (n/a)</td><td>616.33 (n/a)</td><td>611.36 (n/a)</td><td>2.91 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>3.62 (-3.19%)</td><td>3.58 (-1.08%)</td><td>3.59 (-1.18%)</td><td>3.51 (+0.64%)</td><td>0.04 <b>(-55.05%)</b></td><td>7176.80 (-0.64%)</td><td>7037.06 (+1.05%)</td><td>7005.10 (+1.19%)</td><td>6957.30 (+3.30%)</td><td>84.44 <b>(-53.82%)</b></td><td>2469.31 (-3.19%)</td><td>2441.62 (-1.08%)</td><td>2452.47 (-1.18%)</td><td>2393.82 (+0.64%)</td><td>28.98 <b>(-55.05%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.74 (n/a)</td><td>3.62 (n/a)</td><td>3.64 (n/a)</td><td>3.48 (n/a)</td><td>0.09 (n/a)</td><td>7222.90 (n/a)</td><td>6964.10 (n/a)</td><td>6922.50 (n/a)</td><td>6735.20 (n/a)</td><td>182.85 (n/a)</td><td>2550.76 (n/a)</td><td>2468.27 (n/a)</td><td>2481.73 (n/a)</td><td>2378.53 (n/a)</td><td>64.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.95 (-9.37%)</td><td>2.91 (-0.54%)</td><td>2.91 (+1.28%)</td><td>2.85 (+2.40%)</td><td>0.04 <b>(-80.63%)</b></td><td>8822.40 (-2.34%)</td><td>8659.28 (+0.23%)</td><td>8651.90 (-1.26%)</td><td>8528.70 (+10.34%)</td><td>111.82 <b>(-78.98%)</b></td><td>2014.37 (-9.37%)</td><td>1984.25 (-0.54%)</td><td>1985.68 (+1.28%)</td><td>1947.30 (+2.40%)</td><td>25.52 <b>(-80.63%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.26 (n/a)</td><td>2.92 (n/a)</td><td>2.87 (n/a)</td><td>2.79 (n/a)</td><td>0.19 (n/a)</td><td>9034.00 (n/a)</td><td>8639.08 (n/a)</td><td>8762.30 (n/a)</td><td>7729.30 (n/a)</td><td>532.07 (n/a)</td><td>2222.68 (n/a)</td><td>1995.11 (n/a)</td><td>1960.66 (n/a)</td><td>1901.69 (n/a)</td><td>131.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>3.31 (-0.11%)</td><td>3.18 (-1.22%)</td><td>3.16 (-1.19%)</td><td>3.11 (-1.92%)</td><td>0.08 <b>(+38.92%)</b></td><td>8085.60 (+1.96%)</td><td>7919.60 (+1.26%)</td><td>7958.30 (+1.20%)</td><td>7597.90 (+0.11%)</td><td>189.46 <b>(+41.66%)</b></td><td>2261.14 (-0.11%)</td><td>2170.31 (-1.22%)</td><td>2158.73 (-1.19%)</td><td>2124.75 (-1.92%)</td><td>53.23 <b>(+38.92%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.32 (n/a)</td><td>3.22 (n/a)</td><td>3.20 (n/a)</td><td>3.17 (n/a)</td><td>0.06 (n/a)</td><td>7930.00 (n/a)</td><td>7821.00 (n/a)</td><td>7863.70 (n/a)</td><td>7589.70 (n/a)</td><td>133.75 (n/a)</td><td>2263.59 (n/a)</td><td>2197.16 (n/a)</td><td>2184.71 (n/a)</td><td>2166.45 (n/a)</td><td>38.32 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.80 (-0.09%)</td><td>0.80 (-0.01%)</td><td>0.80 (+0.02%)</td><td>0.80 (+0.03%)</td><td>0.00 <b>(-21.14%)</b></td><td>94848.90 (-0.03%)</td><td>94730.38 (+0.01%)</td><td>94771.20 (-0.02%)</td><td>94439.70 (+0.09%)</td><td>166.15 <b>(-21.06%)</b></td><td>727.65 (-0.09%)</td><td>725.42 (-0.01%)</td><td>725.11 (+0.02%)</td><td>724.52 (+0.03%)</td><td>1.27 <b>(-21.14%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94880.40 (n/a)</td><td>94723.80 (n/a)</td><td>94791.30 (n/a)</td><td>94353.20 (n/a)</td><td>210.49 (n/a)</td><td>728.32 (n/a)</td><td>725.48 (n/a)</td><td>724.96 (n/a)</td><td>724.27 (n/a)</td><td>1.62 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.73 (-0.32%)</td><td>0.73 (-0.07%)</td><td>0.73 (-0.04%)</td><td>0.73 (+0.09%)</td><td>0.00 <b>(-74.52%)</b></td><td>103410.40 (-0.09%)</td><td>103325.96 (+0.07%)</td><td>103311.60 (+0.04%)</td><td>103271.40 (+0.32%)</td><td>51.47 <b>(-74.45%)</b></td><td>665.43 (-0.32%)</td><td>665.07 (-0.07%)</td><td>665.17 (-0.04%)</td><td>664.53 (+0.09%)</td><td>0.33 <b>(-74.52%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103501.80 (n/a)</td><td>103255.26 (n/a)</td><td>103271.50 (n/a)</td><td>102944.20 (n/a)</td><td>201.45 (n/a)</td><td>667.54 (n/a)</td><td>665.53 (n/a)</td><td>665.43 (n/a)</td><td>663.94 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.69 (+0.50%)</td><td>0.68 (+0.02%)</td><td>0.68 (-0.20%)</td><td>0.68 (+0.09%)</td><td>0.00 <b>(+58.21%)</b></td><td>110807.20 (-0.09%)</td><td>110408.94 (-0.02%)</td><td>110601.70 (+0.20%)</td><td>109419.40 (-0.49%)</td><td>566.29 <b>(+57.16%)</b></td><td>628.04 (+0.50%)</td><td>622.42 (+0.02%)</td><td>621.32 (-0.20%)</td><td>620.17 (+0.09%)</td><td>3.21 <b>(+58.21%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110903.50 (n/a)</td><td>110431.98 (n/a)</td><td>110383.90 (n/a)</td><td>109961.40 (n/a)</td><td>360.33 (n/a)</td><td>624.94 (n/a)</td><td>622.28 (n/a)</td><td>622.55 (n/a)</td><td>619.63 (n/a)</td><td>2.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.83 (+1.14%)</td><td>2.80 (+0.29%)</td><td>2.80 (+0.06%)</td><td>2.79 (+0.20%)</td><td>0.01 <b>(+253.42%)</b></td><td>37542.80 (-0.20%)</td><td>37410.96 (-0.29%)</td><td>37476.30 (-0.06%)</td><td>37065.50 (-1.12%)</td><td>195.35 <b>(+248.32%)</b></td><td>2896.87 (+1.14%)</td><td>2870.19 (+0.29%)</td><td>2865.12 (+0.06%)</td><td>2860.05 (+0.20%)</td><td>15.09 <b>(+253.42%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>0.00 (n/a)</td><td>37618.80 (n/a)</td><td>37518.92 (n/a)</td><td>37498.50 (n/a)</td><td>37486.40 (n/a)</td><td>56.08 (n/a)</td><td>2864.35 (n/a)</td><td>2861.87 (n/a)</td><td>2863.42 (n/a)</td><td>2854.27 (n/a)</td><td>4.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>7.61 (+1.75%)</td><td>7.19 (+4.88%)</td><td>7.01 (+5.15%)</td><td>6.71 (+3.93%)</td><td>0.40 (-2.57%)</td><td>1327.30 (-3.78%)</td><td>1242.96 (-4.68%)</td><td>1270.80 (-4.89%)</td><td>1170.90 (-1.73%)</td><td>68.50 (-8.66%)</td><td>458.50 (+1.75%)</td><td>432.98 (+4.88%)</td><td>422.48 (+5.15%)</td><td>404.47 (+3.93%)</td><td>23.96 (-2.57%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>7.48 (n/a)</td><td>6.85 (n/a)</td><td>6.67 (n/a)</td><td>6.46 (n/a)</td><td>0.41 (n/a)</td><td>1379.50 (n/a)</td><td>1304.00 (n/a)</td><td>1336.20 (n/a)</td><td>1191.50 (n/a)</td><td>74.99 (n/a)</td><td>450.60 (n/a)</td><td>412.85 (n/a)</td><td>401.78 (n/a)</td><td>389.18 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.84 (-0.95%)</td><td>6.22 (-6.65%)</td><td>6.60 (-1.84%)</td><td>4.55 <b>(-28.64%)</b></td><td>0.95 <b>(+303.96%)</b></td><td>1958.20 <b>(+40.14%)</b></td><td>1465.96 (+9.54%)</td><td>1350.20 (+1.87%)</td><td>1303.60 (+0.95%)</td><td>277.30 <b>(+483.04%)</b></td><td>411.83 (-0.95%)</td><td>374.87 (-6.65%)</td><td>397.61 (-1.84%)</td><td>274.17 <b>(-28.64%)</b></td><td>57.19 <b>(+303.96%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.90 (n/a)</td><td>6.67 (n/a)</td><td>6.72 (n/a)</td><td>6.38 (n/a)</td><td>0.24 (n/a)</td><td>1397.30 (n/a)</td><td>1338.26 (n/a)</td><td>1325.40 (n/a)</td><td>1291.30 (n/a)</td><td>47.56 (n/a)</td><td>415.77 (n/a)</td><td>401.57 (n/a)</td><td>405.05 (n/a)</td><td>384.22 (n/a)</td><td>14.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.72 (+0.83%)</td><td>6.22 (-2.25%)</td><td>6.62 (+5.53%)</td><td>4.73 <b>(-24.07%)</b></td><td>0.85 <b>(+368.02%)</b></td><td>1883.10 <b>(+31.69%)</b></td><td>1458.94 (+4.10%)</td><td>1345.50 (-5.24%)</td><td>1325.40 (-0.82%)</td><td>239.59 <b>(+518.37%)</b></td><td>405.07 (+0.83%)</td><td>374.69 (-2.25%)</td><td>399.02 (+5.53%)</td><td>285.11 <b>(-24.07%)</b></td><td>51.04 <b>(+368.02%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.67 (n/a)</td><td>6.36 (n/a)</td><td>6.28 (n/a)</td><td>6.23 (n/a)</td><td>0.18 (n/a)</td><td>1429.90 (n/a)</td><td>1401.48 (n/a)</td><td>1419.90 (n/a)</td><td>1336.40 (n/a)</td><td>38.75 (n/a)</td><td>401.74 (n/a)</td><td>383.32 (n/a)</td><td>378.10 (n/a)</td><td>375.47 (n/a)</td><td>10.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>8.10 (-1.72%)</td><td>7.68 (-1.37%)</td><td>7.95 (-0.53%)</td><td>7.12 (-2.08%)</td><td>0.44 (-0.17%)</td><td>4897.70 (+2.12%)</td><td>4549.60 (+1.40%)</td><td>4388.00 (+0.53%)</td><td>4304.30 (+1.75%)</td><td>266.09 (+3.28%)</td><td>498.92 (-1.72%)</td><td>473.28 (-1.37%)</td><td>489.40 (-0.53%)</td><td>438.47 (-2.08%)</td><td>27.08 (-0.17%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.24 (n/a)</td><td>7.79 (n/a)</td><td>7.99 (n/a)</td><td>7.27 (n/a)</td><td>0.44 (n/a)</td><td>4795.80 (n/a)</td><td>4486.76 (n/a)</td><td>4364.80 (n/a)</td><td>4230.30 (n/a)</td><td>257.66 (n/a)</td><td>507.65 (n/a)</td><td>479.87 (n/a)</td><td>492.00 (n/a)</td><td>447.79 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>7.59 (+0.12%)</td><td>7.27 (-0.57%)</td><td>7.21 (-1.58%)</td><td>6.98 (-0.14%)</td><td>0.26 (+3.22%)</td><td>4992.50 (+0.14%)</td><td>4800.40 (+0.58%)</td><td>4837.50 (+1.61%)</td><td>4596.20 (-0.12%)</td><td>167.97 (+3.26%)</td><td>467.23 (+0.12%)</td><td>447.80 (-0.57%)</td><td>443.92 (-1.58%)</td><td>430.14 (-0.14%)</td><td>15.76 (+3.22%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>7.58 (n/a)</td><td>7.31 (n/a)</td><td>7.32 (n/a)</td><td>6.99 (n/a)</td><td>0.25 (n/a)</td><td>4985.40 (n/a)</td><td>4772.56 (n/a)</td><td>4760.90 (n/a)</td><td>4601.70 (n/a)</td><td>162.67 (n/a)</td><td>466.67 (n/a)</td><td>450.38 (n/a)</td><td>451.07 (n/a)</td><td>430.75 (n/a)</td><td>15.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>7.53 (-0.04%)</td><td>7.35 (+1.31%)</td><td>7.35 (-0.59%)</td><td>7.21 (+7.00%)</td><td>0.12 <b>(-60.97%)</b></td><td>4836.00 (-6.54%)</td><td>4746.10 (-1.42%)</td><td>4740.60 (+0.59%)</td><td>4628.50 (+0.04%)</td><td>78.60 <b>(-63.76%)</b></td><td>463.97 (-0.04%)</td><td>452.57 (+1.31%)</td><td>452.99 (-0.59%)</td><td>444.06 (+7.00%)</td><td>7.55 <b>(-60.97%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>7.54 (n/a)</td><td>7.25 (n/a)</td><td>7.40 (n/a)</td><td>6.74 (n/a)</td><td>0.31 (n/a)</td><td>5174.40 (n/a)</td><td>4814.60 (n/a)</td><td>4712.80 (n/a)</td><td>4626.80 (n/a)</td><td>216.90 (n/a)</td><td>464.14 (n/a)</td><td>446.73 (n/a)</td><td>455.67 (n/a)</td><td>415.02 (n/a)</td><td>19.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.80 (+0.01%)</td><td>0.80 (+0.06%)</td><td>0.80 (+0.02%)</td><td>0.80 (+0.10%)</td><td>0.00 <b>(-33.69%)</b></td><td>94202.40 (-0.10%)</td><td>94083.42 (-0.06%)</td><td>94069.10 (-0.02%)</td><td>94018.20 (-0.01%)</td><td>74.63 <b>(-33.76%)</b></td><td>730.92 (+0.01%)</td><td>730.41 (+0.06%)</td><td>730.52 (+0.02%)</td><td>729.49 (+0.10%)</td><td>0.58 <b>(-33.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94298.90 (n/a)</td><td>94138.08 (n/a)</td><td>94091.10 (n/a)</td><td>94030.50 (n/a)</td><td>112.67 (n/a)</td><td>730.82 (n/a)</td><td>729.99 (n/a)</td><td>730.35 (n/a)</td><td>728.74 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.74 (+0.00%)</td><td>0.74 (+0.07%)</td><td>0.74 (+0.01%)</td><td>0.74 (+0.27%)</td><td>0.00 <b>(-87.56%)</b></td><td>102599.80 (-0.27%)</td><td>102585.36 (-0.07%)</td><td>102591.10 (-0.01%)</td><td>102558.20 (-0.00%)</td><td>16.18 <b>(-87.59%)</b></td><td>670.05 (+0.00%)</td><td>669.88 (+0.07%)</td><td>669.84 (+0.01%)</td><td>669.78 (+0.27%)</td><td>0.11 <b>(-87.56%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102880.30 (n/a)</td><td>102659.38 (n/a)</td><td>102598.10 (n/a)</td><td>102560.10 (n/a)</td><td>130.34 (n/a)</td><td>670.04 (n/a)</td><td>669.39 (n/a)</td><td>669.79 (n/a)</td><td>667.96 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.71 (+0.01%)</td><td>0.71 (+0.20%)</td><td>0.71 (+0.08%)</td><td>0.71 (+0.57%)</td><td>0.00 <b>(-79.73%)</b></td><td>105893.10 (-0.57%)</td><td>105812.30 (-0.20%)</td><td>105777.10 (-0.08%)</td><td>105765.70 (-0.01%)</td><td>59.76 <b>(-79.85%)</b></td><td>649.73 (+0.01%)</td><td>649.45 (+0.20%)</td><td>649.66 (+0.08%)</td><td>648.95 (+0.57%)</td><td>0.37 <b>(-79.73%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106496.60 (n/a)</td><td>106023.04 (n/a)</td><td>105859.90 (n/a)</td><td>105771.50 (n/a)</td><td>296.51 (n/a)</td><td>649.70 (n/a)</td><td>648.16 (n/a)</td><td>649.15 (n/a)</td><td>645.27 (n/a)</td><td>1.81 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>3.52 (-18.05%)</td><td>3.10 (-13.61%)</td><td>3.09 (-15.15%)</td><td>2.85 (-0.59%)</td><td>0.26 <b>(-50.63%)</b></td><td>2833.00 (+0.59%)</td><td>2611.50 (+14.30%)</td><td>2606.50 (+17.85%)</td><td>2287.50 <b>(+22.03%)</b></td><td>207.40 <b>(-40.55%)</b></td><td>924.10 (-18.05%)</td><td>813.79 (-13.61%)</td><td>811.04 (-15.15%)</td><td>746.17 (-0.59%)</td><td>68.25 <b>(-50.63%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>4.30 (n/a)</td><td>3.59 (n/a)</td><td>3.64 (n/a)</td><td>2.86 (n/a)</td><td>0.53 (n/a)</td><td>2816.30 (n/a)</td><td>2284.74 (n/a)</td><td>2211.70 (n/a)</td><td>1874.60 (n/a)</td><td>348.88 (n/a)</td><td>1127.70 (n/a)</td><td>941.96 (n/a)</td><td>955.80 (n/a)</td><td>750.60 (n/a)</td><td>138.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.36 (+10.50%)</td><td>0.33 (+8.47%)</td><td>0.34 (+12.61%)</td><td>0.29 (+3.04%)</td><td>0.03 <b>(+46.91%)</b></td><td>4313.30 (-2.95%)</td><td>3801.46 (-7.46%)</td><td>3630.40 (-11.20%)</td><td>3413.50 (-9.50%)</td><td>385.02 <b>(+29.30%)</b></td><td>19.66 (+10.50%)</td><td>17.79 (+8.47%)</td><td>18.49 (+12.61%)</td><td>15.56 (+3.04%)</td><td>1.75 <b>(+46.91%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.02 (n/a)</td><td>4444.50 (n/a)</td><td>4107.98 (n/a)</td><td>4088.30 (n/a)</td><td>3771.90 (n/a)</td><td>297.78 (n/a)</td><td>17.79 (n/a)</td><td>16.41 (n/a)</td><td>16.41 (n/a)</td><td>15.10 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.15 <b>(+21.88%)</b></td><td>4.85 (+9.33%)</td><td>4.79 (-1.65%)</td><td>3.57 (-1.70%)</td><td>1.25 <b>(+77.12%)</b></td><td>1861.70 (+1.73%)</td><td>1448.00 (-5.45%)</td><td>1389.50 (+1.68%)</td><td>1081.90 (-17.96%)</td><td>377.28 <b>(+46.14%)</b></td><td>1899.61 <b>(+21.88%)</b></td><td>1499.34 (+9.33%)</td><td>1479.14 (-1.65%)</td><td>1103.96 (-1.70%)</td><td>386.45 <b>(+77.12%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.04 (n/a)</td><td>4.44 (n/a)</td><td>4.87 (n/a)</td><td>3.63 (n/a)</td><td>0.71 (n/a)</td><td>1830.00 (n/a)</td><td>1531.50 (n/a)</td><td>1366.50 (n/a)</td><td>1318.70 (n/a)</td><td>258.16 (n/a)</td><td>1558.55 (n/a)</td><td>1371.36 (n/a)</td><td>1503.97 (n/a)</td><td>1123.06 (n/a)</td><td>218.18 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>13.48 (n/a)</td><td>11.98 (n/a)</td><td>11.90 (n/a)</td><td>10.34 (n/a)</td><td>1.36 (n/a)</td><td>13.47 (n/a)</td><td>11.97 (n/a)</td><td>11.89 (n/a)</td><td>10.34 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>24.34 (-2.35%)</td><td>23.69 (+0.53%)</td><td>24.12 (+1.47%)</td><td>21.94 (+5.44%)</td><td>0.99 <b>(-39.37%)</b></td><td>24.33 (-2.35%)</td><td>23.67 (+0.53%)</td><td>24.11 (+1.47%)</td><td>21.93 (+5.44%)</td><td>0.99 <b>(-39.37%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>24.93 (n/a)</td><td>23.56 (n/a)</td><td>23.77 (n/a)</td><td>20.81 (n/a)</td><td>1.63 (n/a)</td><td>24.91 (n/a)</td><td>23.55 (n/a)</td><td>23.76 (n/a)</td><td>20.79 (n/a)</td><td>1.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>41.26 (+0.16%)</td><td>39.78 (+0.02%)</td><td>39.57 (-0.15%)</td><td>38.91 (+1.71%)</td><td>0.88 <b>(-32.89%)</b></td><td>41.24 (+0.16%)</td><td>39.76 (+0.02%)</td><td>39.55 (-0.15%)</td><td>38.88 (+1.71%)</td><td>0.88 <b>(-32.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>41.20 (n/a)</td><td>39.77 (n/a)</td><td>39.63 (n/a)</td><td>38.25 (n/a)</td><td>1.31 (n/a)</td><td>41.17 (n/a)</td><td>39.75 (n/a)</td><td>39.61 (n/a)</td><td>38.23 (n/a)</td><td>1.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>45.38 (+4.92%)</td><td>43.42 (+2.96%)</td><td>43.32 (+2.61%)</td><td>42.20 (+2.12%)</td><td>1.21 <b>(+59.18%)</b></td><td>45.35 (+4.92%)</td><td>43.40 (+2.96%)</td><td>43.29 (+2.61%)</td><td>42.18 (+2.12%)</td><td>1.21 <b>(+59.18%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>43.25 (n/a)</td><td>42.17 (n/a)</td><td>42.22 (n/a)</td><td>41.32 (n/a)</td><td>0.76 (n/a)</td><td>43.22 (n/a)</td><td>42.15 (n/a)</td><td>42.19 (n/a)</td><td>41.30 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>13.27 (n/a)</td><td>12.68 (n/a)</td><td>13.14 (n/a)</td><td>11.02 (n/a)</td><td>0.96 (n/a)</td><td>13.26 (n/a)</td><td>12.68 (n/a)</td><td>13.13 (n/a)</td><td>11.01 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>24.92 (-1.39%)</td><td>24.49 (+1.15%)</td><td>24.70 (+2.62%)</td><td>23.75 (+1.60%)</td><td>0.47 <b>(-32.07%)</b></td><td>24.91 (-1.39%)</td><td>24.48 (+1.15%)</td><td>24.68 (+2.62%)</td><td>23.73 (+1.60%)</td><td>0.47 <b>(-32.07%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>25.27 (n/a)</td><td>24.21 (n/a)</td><td>24.07 (n/a)</td><td>23.37 (n/a)</td><td>0.69 (n/a)</td><td>25.26 (n/a)</td><td>24.20 (n/a)</td><td>24.05 (n/a)</td><td>23.36 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>41.71 (-0.91%)</td><td>40.08 (+1.88%)</td><td>39.88 (+1.59%)</td><td>38.74 (+3.80%)</td><td>1.11 <b>(-36.31%)</b></td><td>41.68 (-0.91%)</td><td>40.06 (+1.88%)</td><td>39.85 (+1.59%)</td><td>38.71 (+3.80%)</td><td>1.11 <b>(-36.31%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>42.09 (n/a)</td><td>39.35 (n/a)</td><td>39.25 (n/a)</td><td>37.32 (n/a)</td><td>1.74 (n/a)</td><td>42.06 (n/a)</td><td>39.32 (n/a)</td><td>39.23 (n/a)</td><td>37.30 (n/a)</td><td>1.74 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>45.16 (+0.52%)</td><td>42.95 (+0.13%)</td><td>43.51 (+2.06%)</td><td>37.84 (-9.00%)</td><td>2.95 <b>(+139.73%)</b></td><td>45.13 (+0.52%)</td><td>42.92 (+0.13%)</td><td>43.48 (+2.06%)</td><td>37.82 (-9.00%)</td><td>2.95 <b>(+139.73%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>44.93 (n/a)</td><td>42.89 (n/a)</td><td>42.63 (n/a)</td><td>41.58 (n/a)</td><td>1.23 (n/a)</td><td>44.90 (n/a)</td><td>42.86 (n/a)</td><td>42.61 (n/a)</td><td>41.56 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>9.33 (-3.72%)</td><td>8.66 (-6.84%)</td><td>8.74 (-5.65%)</td><td>8.05 (-10.90%)</td><td>0.48 <b>(+98.57%)</b></td><td>9.31 (-3.72%)</td><td>8.65 (-6.84%)</td><td>8.72 (-5.65%)</td><td>8.03 (-10.90%)</td><td>0.48 <b>(+98.57%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.69 (n/a)</td><td>9.30 (n/a)</td><td>9.26 (n/a)</td><td>9.03 (n/a)</td><td>0.24 (n/a)</td><td>9.67 (n/a)</td><td>9.28 (n/a)</td><td>9.24 (n/a)</td><td>9.01 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.03 (-0.12%)</td><td>0.90 (-5.20%)</td><td>0.91 (-9.92%)</td><td>0.70 (-2.37%)</td><td>0.14 (+3.68%)</td><td>1.01 (-0.12%)</td><td>0.88 (-5.20%)</td><td>0.90 (-9.92%)</td><td>0.69 (-2.37%)</td><td>0.13 (+3.68%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.03 (n/a)</td><td>0.94 (n/a)</td><td>1.01 (n/a)</td><td>0.72 (n/a)</td><td>0.13 (n/a)</td><td>1.01 (n/a)</td><td>0.93 (n/a)</td><td>1.00 (n/a)</td><td>0.71 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.29 (+3.14%)</td><td>1.17 (+5.28%)</td><td>1.12 (-1.53%)</td><td>1.08 <b>(+21.22%)</b></td><td>0.10 <b>(-22.40%)</b></td><td>1.28 (+3.14%)</td><td>1.15 (+5.28%)</td><td>1.10 (-1.53%)</td><td>1.07 <b>(+21.22%)</b></td><td>0.10 <b>(-22.40%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.25 (n/a)</td><td>1.11 (n/a)</td><td>1.13 (n/a)</td><td>0.89 (n/a)</td><td>0.13 (n/a)</td><td>1.24 (n/a)</td><td>1.10 (n/a)</td><td>1.12 (n/a)</td><td>0.88 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>17.62 (-6.13%)</td><td>17.01 (-3.52%)</td><td>17.04 (-3.64%)</td><td>16.23 (+2.84%)</td><td>0.58 <b>(-52.72%)</b></td><td>17.42 (-6.13%)</td><td>16.81 (-3.52%)</td><td>16.85 (-3.64%)</td><td>16.05 (+2.84%)</td><td>0.57 <b>(-52.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>18.78 (n/a)</td><td>17.63 (n/a)</td><td>17.69 (n/a)</td><td>15.79 (n/a)</td><td>1.22 (n/a)</td><td>18.56 (n/a)</td><td>17.42 (n/a)</td><td>17.48 (n/a)</td><td>15.60 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>13.94 (-4.13%)</td><td>13.01 (-5.32%)</td><td>12.98 (-5.04%)</td><td>12.15 (-8.56%)</td><td>0.73 <b>(+49.12%)</b></td><td>13.69 (-4.13%)</td><td>12.78 (-5.32%)</td><td>12.76 (-5.04%)</td><td>11.93 (-8.56%)</td><td>0.72 <b>(+49.12%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.54 (n/a)</td><td>13.74 (n/a)</td><td>13.67 (n/a)</td><td>13.28 (n/a)</td><td>0.49 (n/a)</td><td>14.28 (n/a)</td><td>13.50 (n/a)</td><td>13.43 (n/a)</td><td>13.05 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>8.91 (+3.62%)</td><td>7.71 (+3.03%)</td><td>7.76 (+0.74%)</td><td>6.71 (+18.73%)</td><td>0.81 <b>(-27.58%)</b></td><td>8.76 (+3.62%)</td><td>7.58 (+3.03%)</td><td>7.62 (+0.74%)</td><td>6.60 (+18.73%)</td><td>0.80 <b>(-27.58%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.60 (n/a)</td><td>7.48 (n/a)</td><td>7.70 (n/a)</td><td>5.66 (n/a)</td><td>1.12 (n/a)</td><td>8.45 (n/a)</td><td>7.35 (n/a)</td><td>7.57 (n/a)</td><td>5.56 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.28 (+2.62%)</td><td>5.48 (-4.84%)</td><td>5.48 (-4.98%)</td><td>4.51 (-15.05%)</td><td>0.65 <b>(+94.03%)</b></td><td>6.18 (+2.62%)</td><td>5.39 (-4.84%)</td><td>5.39 (-4.98%)</td><td>4.44 (-15.05%)</td><td>0.64 <b>(+94.03%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.12 (n/a)</td><td>5.76 (n/a)</td><td>5.77 (n/a)</td><td>5.31 (n/a)</td><td>0.33 (n/a)</td><td>6.02 (n/a)</td><td>5.66 (n/a)</td><td>5.67 (n/a)</td><td>5.23 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>13.17 (n/a)</td><td>12.53 (n/a)</td><td>13.00 (n/a)</td><td>10.79 (n/a)</td><td>0.99 (n/a)</td><td>13.16 (n/a)</td><td>12.52 (n/a)</td><td>12.99 (n/a)</td><td>10.78 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>13.26 (n/a)</td><td>11.93 (n/a)</td><td>11.73 (n/a)</td><td>10.34 (n/a)</td><td>1.10 (n/a)</td><td>13.25 (n/a)</td><td>11.92 (n/a)</td><td>11.72 (n/a)</td><td>10.34 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>168.66 (n/a)</td><td>174.60 (n/a)</td><td>124.70 (n/a)</td><td>32.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>286.30 (n/a)</td><td>185.70 (n/a)</td><td>164.70 (n/a)</td><td>152.50 (n/a)</td><td>56.55 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.00 (n/a)</td><td>156.54 (n/a)</td><td>148.00 (n/a)</td><td>133.90 (n/a)</td><td>23.40 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.00 (n/a)</td><td>178.52 (n/a)</td><td>176.00 (n/a)</td><td>143.70 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.50 (n/a)</td><td>168.86 (n/a)</td><td>161.60 (n/a)</td><td>149.50 (n/a)</td><td>18.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.60 (n/a)</td><td>184.44 (n/a)</td><td>196.90 (n/a)</td><td>110.80 (n/a)</td><td>49.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>297.90 (n/a)</td><td>189.20 (n/a)</td><td>169.50 (n/a)</td><td>134.70 (n/a)</td><td>63.47 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>323.10 (n/a)</td><td>240.98 (n/a)</td><td>229.60 (n/a)</td><td>175.80 (n/a)</td><td>57.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.40 (n/a)</td><td>183.26 (n/a)</td><td>190.60 (n/a)</td><td>134.50 (n/a)</td><td>48.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>232.50 (n/a)</td><td>171.58 (n/a)</td><td>163.00 (n/a)</td><td>99.20 (n/a)</td><td>50.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>276.60 (n/a)</td><td>205.36 (n/a)</td><td>191.90 (n/a)</td><td>143.10 (n/a)</td><td>49.55 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.50 (n/a)</td><td>168.94 (n/a)</td><td>163.10 (n/a)</td><td>142.90 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.90 (n/a)</td><td>176.70 (n/a)</td><td>156.50 (n/a)</td><td>154.90 (n/a)</td><td>38.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>178.30 (n/a)</td><td>180.80 (n/a)</td><td>120.70 (n/a)</td><td>42.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>185.48 (n/a)</td><td>168.60 (n/a)</td><td>156.10 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>244.60 (n/a)</td><td>232.56 (n/a)</td><td>232.70 (n/a)</td><td>222.00 (n/a)</td><td>8.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.20 (n/a)</td><td>160.64 (n/a)</td><td>152.30 (n/a)</td><td>122.40 (n/a)</td><td>33.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>184.80 (n/a)</td><td>144.48 (n/a)</td><td>149.30 (n/a)</td><td>111.70 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.20 (n/a)</td><td>165.54 (n/a)</td><td>162.90 (n/a)</td><td>132.20 (n/a)</td><td>21.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>246.90 (n/a)</td><td>194.54 (n/a)</td><td>183.60 (n/a)</td><td>158.70 (n/a)</td><td>33.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>270.70 (n/a)</td><td>205.90 (n/a)</td><td>195.90 (n/a)</td><td>153.10 (n/a)</td><td>43.43 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>178.44 (n/a)</td><td>179.30 (n/a)</td><td>161.20 (n/a)</td><td>12.44 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>288.00 (n/a)</td><td>204.42 (n/a)</td><td>185.20 (n/a)</td><td>163.70 (n/a)</td><td>52.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>307.20 (n/a)</td><td>242.06 (n/a)</td><td>235.60 (n/a)</td><td>184.60 (n/a)</td><td>52.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>187.70 (n/a)</td><td>158.84 (n/a)</td><td>152.90 (n/a)</td><td>127.20 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.50 (n/a)</td><td>183.82 (n/a)</td><td>181.60 (n/a)</td><td>161.70 (n/a)</td><td>20.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>176.98 (n/a)</td><td>180.60 (n/a)</td><td>165.50 (n/a)</td><td>10.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.90 (n/a)</td><td>169.56 (n/a)</td><td>167.10 (n/a)</td><td>128.90 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>224.00 (n/a)</td><td>175.12 (n/a)</td><td>157.90 (n/a)</td><td>125.30 (n/a)</td><td>45.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>225.90 (n/a)</td><td>196.94 (n/a)</td><td>186.90 (n/a)</td><td>172.70 (n/a)</td><td>25.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>200.50 (n/a)</td><td>175.86 (n/a)</td><td>174.10 (n/a)</td><td>133.80 (n/a)</td><td>26.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>283.60 (n/a)</td><td>229.28 (n/a)</td><td>224.70 (n/a)</td><td>179.30 (n/a)</td><td>37.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+4.40%)</td><td>0.02 (-8.67%)</td><td>0.02 (-19.40%)</td><td>0.02 (-2.86%)</td><td>0.01 <b>(+31.81%)</b></td><td>224.20 (+2.94%)</td><td>188.20 (+11.16%)</td><td>203.70 <b>(+24.06%)</b></td><td>128.50 (-4.18%)</td><td>37.46 <b>(+23.95%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.80 (n/a)</td><td>169.30 (n/a)</td><td>164.20 (n/a)</td><td>134.10 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (+17.93%)</td><td>0.03 (+6.61%)</td><td>0.02 (+0.70%)</td><td>0.02 (+1.12%)</td><td>0.01 <b>(+34.71%)</b></td><td>225.50 (-1.10%)</td><td>164.98 (-3.79%)</td><td>178.30 (-0.72%)</td><td>105.80 (-15.22%)</td><td>48.45 (+14.09%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>171.48 (n/a)</td><td>179.60 (n/a)</td><td>124.80 (n/a)</td><td>42.47 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-16.38%)</td><td>0.02 (-2.45%)</td><td>0.02 (-2.45%)</td><td>0.02 <b>(+48.17%)</b></td><td>0.00 <b>(-72.90%)</b></td><td>187.30 <b>(-32.50%)</b></td><td>165.94 (-4.84%)</td><td>165.30 (+2.48%)</td><td>152.40 (+19.53%)</td><td>13.46 <b>(-78.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>277.50 (n/a)</td><td>174.38 (n/a)</td><td>161.30 (n/a)</td><td>127.50 (n/a)</td><td>61.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+4.56%)</td><td>0.03 (+1.70%)</td><td>0.03 (-1.92%)</td><td>0.02 (+6.08%)</td><td>0.00 (+1.43%)</td><td>180.60 (-5.74%)</td><td>155.74 (-1.82%)</td><td>156.00 (+1.96%)</td><td>124.60 (-4.30%)</td><td>20.58 (-10.89%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.60 (n/a)</td><td>158.62 (n/a)</td><td>153.00 (n/a)</td><td>130.20 (n/a)</td><td>23.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+12.87%)</td><td>0.03 (+7.48%)</td><td>0.02 (-12.92%)</td><td>0.02 <b>(+104.81%)</b></td><td>0.00 <b>(-44.65%)</b></td><td>187.00 <b>(-51.17%)</b></td><td>160.20 (-17.88%)</td><td>171.50 (+14.87%)</td><td>129.00 (-11.40%)</td><td>24.52 <b>(-76.67%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>383.00 (n/a)</td><td>195.08 (n/a)</td><td>149.30 (n/a)</td><td>145.60 (n/a)</td><td>105.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+5.23%)</td><td>0.02 (-2.51%)</td><td>0.02 (+2.89%)</td><td>0.02 (-9.34%)</td><td>0.00 <b>(+35.69%)</b></td><td>237.90 (+10.29%)</td><td>181.84 (+3.88%)</td><td>166.50 (-2.80%)</td><td>148.30 (-5.00%)</td><td>34.85 <b>(+44.29%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.70 (n/a)</td><td>175.04 (n/a)</td><td>171.30 (n/a)</td><td>156.10 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-2.59%)</td><td>0.02 (-8.65%)</td><td>0.02 (-18.37%)</td><td>0.02 (+12.54%)</td><td>0.00 <b>(-23.13%)</b></td><td>192.20 (-11.14%)</td><td>169.52 (+7.30%)</td><td>175.40 <b>(+22.49%)</b></td><td>125.90 (+2.69%)</td><td>26.26 <b>(-31.56%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.30 (n/a)</td><td>157.98 (n/a)</td><td>143.20 (n/a)</td><td>122.60 (n/a)</td><td>38.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+7.56%)</td><td>0.02 (-1.41%)</td><td>0.02 (-16.75%)</td><td>0.02 (+13.85%)</td><td>0.00 (-9.84%)</td><td>226.70 (-12.17%)</td><td>201.02 (+0.27%)</td><td>214.10 <b>(+20.15%)</b></td><td>150.80 (-7.03%)</td><td>31.13 <b>(-27.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.10 (n/a)</td><td>200.48 (n/a)</td><td>178.20 (n/a)</td><td>162.20 (n/a)</td><td>42.65 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-4.51%)</td><td>0.05 (-3.12%)</td><td>0.05 (-5.26%)</td><td>0.04 (-5.45%)</td><td>0.01 (+7.06%)</td><td>191.20 (+5.75%)</td><td>152.04 (+3.61%)</td><td>152.20 (+5.55%)</td><td>129.00 (+4.79%)</td><td>24.52 (+16.25%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.80 (n/a)</td><td>146.74 (n/a)</td><td>144.20 (n/a)</td><td>123.10 (n/a)</td><td>21.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-9.76%)</td><td>0.05 (-12.05%)</td><td>0.05 (-18.15%)</td><td>0.05 (+7.85%)</td><td>0.01 <b>(-41.49%)</b></td><td>174.20 (-7.24%)</td><td>154.02 (+11.67%)</td><td>156.60 <b>(+22.15%)</b></td><td>130.30 (+10.80%)</td><td>16.12 <b>(-42.95%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>137.92 (n/a)</td><td>128.20 (n/a)</td><td>117.60 (n/a)</td><td>28.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (-5.95%)</td><td>0.05 (-1.93%)</td><td>0.06 (+10.57%)</td><td>0.04 (-3.73%)</td><td>0.01 (-15.20%)</td><td>205.40 (+3.89%)</td><td>156.22 (+1.36%)</td><td>146.00 (-9.54%)</td><td>125.80 (+6.34%)</td><td>30.99 (-2.76%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.70 (n/a)</td><td>154.12 (n/a)</td><td>161.40 (n/a)</td><td>118.30 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (+4.46%)</td><td>0.05 (-0.75%)</td><td>0.06 (+1.76%)</td><td>0.05 (-2.60%)</td><td>0.01 <b>(+64.99%)</b></td><td>168.50 (+2.62%)</td><td>150.30 (+1.31%)</td><td>143.90 (-1.71%)</td><td>132.20 (-4.27%)</td><td>15.85 <b>(+62.95%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>164.20 (n/a)</td><td>148.36 (n/a)</td><td>146.40 (n/a)</td><td>138.10 (n/a)</td><td>9.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-4.77%)</td><td>0.06 (-2.52%)</td><td>0.05 (-5.37%)</td><td>0.05 (+15.72%)</td><td>0.00 <b>(-44.91%)</b></td><td>165.50 (-13.58%)</td><td>149.66 (+0.97%)</td><td>154.20 (+5.69%)</td><td>132.60 (+5.07%)</td><td>12.93 <b>(-50.60%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>148.22 (n/a)</td><td>145.90 (n/a)</td><td>126.20 (n/a)</td><td>26.18 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (+9.15%)</td><td>0.06 (+1.67%)</td><td>0.05 (-5.34%)</td><td>0.05 <b>(+26.55%)</b></td><td>0.01 <b>(-24.09%)</b></td><td>169.10 <b>(-20.98%)</b></td><td>149.50 (-3.52%)</td><td>154.20 (+5.62%)</td><td>120.10 (-8.39%)</td><td>18.18 <b>(-47.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>154.96 (n/a)</td><td>146.00 (n/a)</td><td>131.10 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-12.30%)</td><td>0.05 (-14.24%)</td><td>0.04 (-17.39%)</td><td>0.03 <b>(-27.49%)</b></td><td>0.01 (+13.99%)</td><td>241.40 <b>(+37.86%)</b></td><td>182.94 (+18.72%)</td><td>188.00 <b>(+21.06%)</b></td><td>138.00 (+14.05%)</td><td>39.65 <b>(+76.38%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.10 (n/a)</td><td>154.10 (n/a)</td><td>155.30 (n/a)</td><td>121.00 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 <b>(-22.56%)</b></td><td>0.05 (-11.92%)</td><td>0.05 (-12.70%)</td><td>0.04 (-12.72%)</td><td>0.01 <b>(-43.53%)</b></td><td>220.00 (+14.58%)</td><td>180.96 (+11.69%)</td><td>178.90 (+14.61%)</td><td>153.70 <b>(+29.16%)</b></td><td>25.17 (-17.76%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>162.02 (n/a)</td><td>156.10 (n/a)</td><td>119.00 (n/a)</td><td>30.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (+1.04%)</td><td>0.05 (-4.44%)</td><td>0.05 (+4.15%)</td><td>0.03 <b>(-28.55%)</b></td><td>0.01 <b>(+30.47%)</b></td><td>305.40 <b>(+39.96%)</b></td><td>197.12 (+9.45%)</td><td>170.10 (-3.95%)</td><td>130.70 (-1.06%)</td><td>67.06 <b>(+81.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>180.10 (n/a)</td><td>177.10 (n/a)</td><td>132.10 (n/a)</td><td>36.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (-8.05%)</td><td>0.03 (-10.08%)</td><td>0.03 (-9.88%)</td><td>0.03 (+12.38%)</td><td>0.01 (-17.39%)</td><td>327.20 (-11.01%)</td><td>268.38 (+8.96%)</td><td>256.70 (+10.93%)</td><td>188.90 (+8.75%)</td><td>55.74 <b>(-22.97%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>367.70 (n/a)</td><td>246.30 (n/a)</td><td>231.40 (n/a)</td><td>173.70 (n/a)</td><td>72.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (-19.78%)</td><td>0.09 (-16.44%)</td><td>0.08 <b>(-21.13%)</b></td><td>0.08 (-8.66%)</td><td>0.01 <b>(-51.99%)</b></td><td>202.90 (+9.50%)</td><td>192.16 (+18.66%)</td><td>198.30 <b>(+26.79%)</b></td><td>171.10 <b>(+24.62%)</b></td><td>12.87 <b>(-35.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.30 (n/a)</td><td>161.94 (n/a)</td><td>156.40 (n/a)</td><td>137.30 (n/a)</td><td>20.01 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (+8.50%)</td><td>0.10 (+3.71%)</td><td>0.10 (+4.49%)</td><td>0.09 (-4.70%)</td><td>0.02 <b>(+53.73%)</b></td><td>189.50 (+4.93%)</td><td>160.92 (-2.27%)</td><td>162.50 (-4.30%)</td><td>124.70 (-7.83%)</td><td>26.71 <b>(+53.08%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.60 (n/a)</td><td>164.66 (n/a)</td><td>169.80 (n/a)</td><td>135.30 (n/a)</td><td>17.44 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (+1.83%)</td><td>0.10 (-8.08%)</td><td>0.09 (+2.51%)</td><td>0.07 (-18.87%)</td><td>0.03 (+0.22%)</td><td>248.70 <b>(+23.24%)</b></td><td>180.10 (+9.72%)</td><td>180.40 (-2.43%)</td><td>116.90 (-1.76%)</td><td>47.58 <b>(+21.06%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>201.80 (n/a)</td><td>164.14 (n/a)</td><td>184.90 (n/a)</td><td>119.00 (n/a)</td><td>39.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (-2.33%)</td><td>0.08 <b>(-21.61%)</b></td><td>0.08 <b>(-23.49%)</b></td><td>0.06 <b>(-41.70%)</b></td><td>0.02 <b>(+187.61%)</b></td><td>292.20 <b>(+71.48%)</b></td><td>205.36 <b>(+33.28%)</b></td><td>194.50 <b>(+30.71%)</b></td><td>149.00 (+2.41%)</td><td>52.85 <b>(+419.46%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>170.40 (n/a)</td><td>154.08 (n/a)</td><td>148.80 (n/a)</td><td>145.50 (n/a)</td><td>10.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (-1.27%)</td><td>0.10 (-12.08%)</td><td>0.09 (-18.33%)</td><td>0.08 <b>(-24.58%)</b></td><td>0.03 <b>(+68.57%)</b></td><td>215.90 <b>(+32.62%)</b></td><td>174.00 (+17.81%)</td><td>184.30 <b>(+22.38%)</b></td><td>120.30 (+1.26%)</td><td>40.07 <b>(+130.94%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>162.80 (n/a)</td><td>147.70 (n/a)</td><td>150.60 (n/a)</td><td>118.80 (n/a)</td><td>17.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (-2.54%)</td><td>0.10 (-6.94%)</td><td>0.09 (-13.71%)</td><td>0.08 (-9.84%)</td><td>0.02 <b>(+32.74%)</b></td><td>206.80 (+10.94%)</td><td>168.20 (+8.88%)</td><td>178.10 (+15.88%)</td><td>132.00 (+2.64%)</td><td>30.44 <b>(+47.14%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.40 (n/a)</td><td>154.48 (n/a)</td><td>153.70 (n/a)</td><td>128.60 (n/a)</td><td>20.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (-15.99%)</td><td>0.09 (-19.38%)</td><td>0.09 (-12.78%)</td><td>0.06 <b>(-37.34%)</b></td><td>0.02 <b>(+45.69%)</b></td><td>278.40 <b>(+59.54%)</b></td><td>197.56 <b>(+28.19%)</b></td><td>176.00 (+14.66%)</td><td>152.20 (+19.09%)</td><td>49.49 <b>(+188.60%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>174.50 (n/a)</td><td>154.12 (n/a)</td><td>153.50 (n/a)</td><td>127.80 (n/a)</td><td>17.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (+3.22%)</td><td>0.09 (-1.22%)</td><td>0.09 (-4.31%)</td><td>0.07 (+3.01%)</td><td>0.01 (+14.62%)</td><td>229.40 (-2.92%)</td><td>193.20 (+1.55%)</td><td>189.70 (+4.52%)</td><td>163.00 (-3.15%)</td><td>28.60 (+5.44%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>190.26 (n/a)</td><td>181.50 (n/a)</td><td>168.30 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (+5.44%)</td><td>0.21 (+1.31%)</td><td>0.19 (-1.11%)</td><td>0.18 (+7.59%)</td><td>0.03 (+6.54%)</td><td>180.20 (-7.07%)</td><td>161.56 (-1.27%)</td><td>170.30 (+1.13%)</td><td>124.30 (-5.19%)</td><td>23.26 (-5.46%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.90 (n/a)</td><td>163.64 (n/a)</td><td>168.40 (n/a)</td><td>131.10 (n/a)</td><td>24.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 <b>(+37.08%)</b></td><td>0.21 <b>(+23.77%)</b></td><td>0.20 (+11.76%)</td><td>0.18 <b>(+39.25%)</b></td><td>0.03 <b>(+32.20%)</b></td><td>184.20 <b>(-28.19%)</b></td><td>158.60 (-19.39%)</td><td>164.90 (-10.48%)</td><td>124.20 <b>(-27.03%)</b></td><td>23.35 <b>(-32.99%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>256.50 (n/a)</td><td>196.76 (n/a)</td><td>184.20 (n/a)</td><td>170.20 (n/a)</td><td>34.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.32 <b>(+34.12%)</b></td><td>0.22 (+17.00%)</td><td>0.23 <b>(+30.38%)</b></td><td>0.16 <b>(+25.47%)</b></td><td>0.07 <b>(+34.29%)</b></td><td>201.20 <b>(-20.29%)</b></td><td>155.90 (-13.76%)</td><td>142.30 <b>(-23.29%)</b></td><td>100.80 <b>(-25.44%)</b></td><td>42.44 (-12.70%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>252.40 (n/a)</td><td>180.78 (n/a)</td><td>185.50 (n/a)</td><td>135.20 (n/a)</td><td>48.62 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (-4.86%)</td><td>0.20 (-2.91%)</td><td>0.20 (+5.27%)</td><td>0.15 (-10.54%)</td><td>0.03 (+4.26%)</td><td>220.70 (+11.75%)</td><td>171.08 (+3.57%)</td><td>162.90 (-5.01%)</td><td>139.00 (+5.06%)</td><td>31.85 <b>(+25.14%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>197.50 (n/a)</td><td>165.18 (n/a)</td><td>171.50 (n/a)</td><td>132.30 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (+4.13%)</td><td>0.20 (-4.58%)</td><td>0.18 (-7.14%)</td><td>0.15 (-6.32%)</td><td>0.05 (+5.60%)</td><td>219.80 (+6.70%)</td><td>171.96 (+5.39%)</td><td>178.30 (+7.67%)</td><td>121.60 (-4.03%)</td><td>38.85 (+10.39%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>206.00 (n/a)</td><td>163.16 (n/a)</td><td>165.60 (n/a)</td><td>126.70 (n/a)</td><td>35.20 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (-13.57%)</td><td>0.18 (-9.85%)</td><td>0.18 (-4.35%)</td><td>0.14 (-13.13%)</td><td>0.04 (-15.03%)</td><td>242.00 (+15.13%)</td><td>187.34 (+10.72%)</td><td>185.30 (+4.51%)</td><td>150.00 (+15.74%)</td><td>39.51 (+11.73%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.20 (n/a)</td><td>169.20 (n/a)</td><td>177.30 (n/a)</td><td>129.60 (n/a)</td><td>35.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 (+2.84%)</td><td>0.16 (+0.30%)</td><td>0.17 (-6.09%)</td><td>0.11 (+11.15%)</td><td>0.03 (-13.10%)</td><td>297.90 (-10.03%)</td><td>210.12 (-2.26%)</td><td>189.40 (+6.46%)</td><td>166.70 (-2.74%)</td><td>52.66 <b>(-22.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>331.10 (n/a)</td><td>214.98 (n/a)</td><td>177.90 (n/a)</td><td>171.40 (n/a)</td><td>67.80 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 <b>(+33.30%)</b></td><td>0.03 <b>(+30.41%)</b></td><td>0.03 (+5.47%)</td><td>0.03 <b>(+120.23%)</b></td><td>0.00 <b>(-42.61%)</b></td><td>158.00 <b>(-54.60%)</b></td><td>147.56 <b>(-29.07%)</b></td><td>155.00 (-5.14%)</td><td>120.30 <b>(-25.00%)</b></td><td>15.70 <b>(-80.54%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>348.00 (n/a)</td><td>208.04 (n/a)</td><td>163.40 (n/a)</td><td>160.40 (n/a)</td><td>80.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-13.46%)</td><td>0.03 (+1.28%)</td><td>0.03 (+1.21%)</td><td>0.02 (+14.88%)</td><td>0.00 <b>(-47.20%)</b></td><td>171.20 (-12.96%)</td><td>145.20 (-3.80%)</td><td>141.20 (-1.19%)</td><td>128.70 (+15.63%)</td><td>17.10 <b>(-47.23%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>150.94 (n/a)</td><td>142.90 (n/a)</td><td>111.30 (n/a)</td><td>32.40 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 <b>(+2760716.79%)</b></td><td>0.02 <b>(+2209133.52%)</b></td><td>0.02 <b>(+2139579.64%)</b></td><td>0.02 <b>(+1827116.25%)</b></td><td>0.00 <b>(+12535024160.54%)</b></td><td>259.80 <b>(-99.99%)</b></td><td>219.10 <b>(-100.00%)</b></td><td>221.80 <b>(-100.00%)</b></td><td>171.90 <b>(-100.00%)</b></td><td>33.26 <b>(-75.41%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4746284.10 (n/a)</td><td>4746128.87 (n/a)</td><td>4746065.90 (n/a)</td><td>4746036.60 (n/a)</td><td>135.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-13.56%)</td><td>0.02 (+0.98%)</td><td>0.02 (+7.27%)</td><td>0.02 (+4.17%)</td><td>0.00 <b>(-63.39%)</b></td><td>212.50 (-3.98%)</td><td>198.62 (-1.95%)</td><td>194.70 (-6.75%)</td><td>190.80 (+15.71%)</td><td>9.45 <b>(-59.43%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.30 (n/a)</td><td>202.58 (n/a)</td><td>208.80 (n/a)</td><td>164.90 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-2.99%)</td><td>0.03 (+4.89%)</td><td>0.03 (+7.40%)</td><td>0.02 (+18.24%)</td><td>0.00 <b>(-39.09%)</b></td><td>176.80 (-15.45%)</td><td>156.36 (-6.70%)</td><td>159.50 (-6.89%)</td><td>130.60 (+3.08%)</td><td>17.38 <b>(-47.16%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>167.58 (n/a)</td><td>171.30 (n/a)</td><td>126.70 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-10.33%)</td><td>0.03 (-5.10%)</td><td>0.03 (-4.29%)</td><td>0.02 (+8.10%)</td><td>0.00 <b>(-46.81%)</b></td><td>171.70 (-7.49%)</td><td>159.34 (+4.32%)</td><td>155.30 (+4.51%)</td><td>145.50 (+11.49%)</td><td>11.71 <b>(-44.73%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.60 (n/a)</td><td>152.74 (n/a)</td><td>148.60 (n/a)</td><td>130.50 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-17.49%)</td><td>0.02 (-13.15%)</td><td>0.02 (-12.55%)</td><td>0.02 (-6.61%)</td><td>0.00 <b>(-41.77%)</b></td><td>222.90 (+7.06%)</td><td>195.10 (+14.24%)</td><td>192.00 (+14.35%)</td><td>174.70 <b>(+21.24%)</b></td><td>17.55 <b>(-24.96%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.20 (n/a)</td><td>170.78 (n/a)</td><td>167.90 (n/a)</td><td>144.10 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-6.86%)</td><td>0.02 (-4.27%)</td><td>0.02 (-4.48%)</td><td>0.02 (+3.07%)</td><td>0.00 (-18.50%)</td><td>204.50 (-2.99%)</td><td>181.62 (+3.70%)</td><td>192.80 (+4.67%)</td><td>143.70 (+7.32%)</td><td>25.29 (-13.77%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.80 (n/a)</td><td>175.14 (n/a)</td><td>184.20 (n/a)</td><td>133.90 (n/a)</td><td>29.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 <b>(-28.93%)</b></td><td>0.02 (-9.06%)</td><td>0.02 (-5.46%)</td><td>0.02 (+1.55%)</td><td>0.00 <b>(-65.45%)</b></td><td>203.60 (-1.55%)</td><td>189.60 (+6.25%)</td><td>200.30 (+5.76%)</td><td>165.00 <b>(+40.66%)</b></td><td>17.80 <b>(-49.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>178.44 (n/a)</td><td>189.40 (n/a)</td><td>117.30 (n/a)</td><td>35.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 <b>(-31.02%)</b></td><td>0.02 <b>(-24.25%)</b></td><td>0.02 <b>(-20.08%)</b></td><td>0.01 <b>(-28.00%)</b></td><td>0.00 <b>(-35.64%)</b></td><td>299.60 <b>(+38.90%)</b></td><td>211.60 <b>(+31.27%)</b></td><td>201.50 <b>(+25.08%)</b></td><td>161.90 <b>(+44.94%)</b></td><td>52.44 <b>(+36.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>161.20 (n/a)</td><td>161.10 (n/a)</td><td>111.70 (n/a)</td><td>38.56 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-18.88%)</td><td>0.02 (-7.39%)</td><td>0.02 (+4.69%)</td><td>0.02 (-6.18%)</td><td>0.00 <b>(-48.30%)</b></td><td>242.40 (+6.60%)</td><td>202.92 (+5.42%)</td><td>200.70 (-4.47%)</td><td>177.70 <b>(+23.23%)</b></td><td>26.35 <b>(-33.23%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.40 (n/a)</td><td>192.48 (n/a)</td><td>210.10 (n/a)</td><td>144.20 (n/a)</td><td>39.46 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-14.01%)</td><td>0.02 (-5.95%)</td><td>0.02 (-3.14%)</td><td>0.02 (+0.74%)</td><td>0.00 <b>(-37.14%)</b></td><td>221.50 (-0.72%)</td><td>176.50 (+4.67%)</td><td>165.40 (+3.25%)</td><td>162.40 (+16.25%)</td><td>25.31 <b>(-25.96%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.10 (n/a)</td><td>168.62 (n/a)</td><td>160.20 (n/a)</td><td>139.70 (n/a)</td><td>34.18 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-8.67%)</td><td>0.02 (-8.06%)</td><td>0.02 (-6.00%)</td><td>0.02 (-11.97%)</td><td>0.00 (+4.98%)</td><td>247.40 (+13.64%)</td><td>199.38 (+9.20%)</td><td>185.20 (+6.38%)</td><td>176.10 (+9.51%)</td><td>28.56 <b>(+30.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.70 (n/a)</td><td>182.58 (n/a)</td><td>174.10 (n/a)</td><td>160.80 (n/a)</td><td>21.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+4.41%)</td><td>0.02 (+16.53%)</td><td>0.02 (+2.88%)</td><td>0.02 <b>(+64.19%)</b></td><td>0.00 <b>(-51.42%)</b></td><td>219.80 <b>(-39.08%)</b></td><td>182.14 <b>(-20.91%)</b></td><td>182.60 (-2.77%)</td><td>157.70 (-4.19%)</td><td>24.95 <b>(-70.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>360.80 (n/a)</td><td>230.30 (n/a)</td><td>187.80 (n/a)</td><td>164.60 (n/a)</td><td>85.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-3.22%)</td><td>0.02 (-3.37%)</td><td>0.02 (-8.03%)</td><td>0.02 (-4.88%)</td><td>0.00 (-19.85%)</td><td>217.90 (+5.16%)</td><td>185.28 (+3.15%)</td><td>180.60 (+8.73%)</td><td>166.70 (+3.28%)</td><td>19.58 (-11.08%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.20 (n/a)</td><td>179.62 (n/a)</td><td>166.10 (n/a)</td><td>161.40 (n/a)</td><td>22.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-5.50%)</td><td>0.02 (-16.74%)</td><td>0.02 <b>(-28.52%)</b></td><td>0.02 (-6.81%)</td><td>0.00 (-4.67%)</td><td>205.70 (+7.30%)</td><td>187.76 <b>(+20.11%)</b></td><td>198.30 <b>(+39.94%)</b></td><td>136.20 (+5.83%)</td><td>29.08 (+4.51%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.70 (n/a)</td><td>156.32 (n/a)</td><td>141.70 (n/a)</td><td>128.70 (n/a)</td><td>27.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-0.28%)</td><td>0.05 (-2.16%)</td><td>0.05 (-14.89%)</td><td>0.05 <b>(+25.73%)</b></td><td>0.01 <b>(-41.04%)</b></td><td>177.30 <b>(-20.46%)</b></td><td>162.96 (-0.74%)</td><td>170.90 (+17.46%)</td><td>132.50 (+0.23%)</td><td>18.50 <b>(-52.57%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>164.18 (n/a)</td><td>145.50 (n/a)</td><td>132.20 (n/a)</td><td>39.01 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-7.01%)</td><td>0.05 (+2.42%)</td><td>0.05 (+1.64%)</td><td>0.04 <b>(+22.91%)</b></td><td>0.01 <b>(-54.02%)</b></td><td>183.40 (-18.67%)</td><td>167.54 (-6.09%)</td><td>171.80 (-1.60%)</td><td>143.70 (+7.56%)</td><td>17.51 <b>(-59.52%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>178.40 (n/a)</td><td>174.60 (n/a)</td><td>133.60 (n/a)</td><td>43.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (+10.67%)</td><td>0.04 (-0.08%)</td><td>0.04 (-11.89%)</td><td>0.03 (+0.29%)</td><td>0.01 <b>(+32.47%)</b></td><td>301.70 (-0.30%)</td><td>225.86 (+1.59%)</td><td>224.70 (+13.48%)</td><td>172.50 (-9.64%)</td><td>54.01 (+14.94%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.60 (n/a)</td><td>222.32 (n/a)</td><td>198.00 (n/a)</td><td>190.90 (n/a)</td><td>46.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 <b>(+36.53%)</b></td><td>0.04 <b>(+39.84%)</b></td><td>0.05 <b>(+42.96%)</b></td><td>0.03 <b>(+45.23%)</b></td><td>0.01 (+3.54%)</td><td>248.90 <b>(-31.15%)</b></td><td>193.02 <b>(-29.89%)</b></td><td>178.20 <b>(-30.04%)</b></td><td>157.30 <b>(-26.77%)</b></td><td>35.78 <b>(-46.10%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>361.50 (n/a)</td><td>275.30 (n/a)</td><td>254.70 (n/a)</td><td>214.80 (n/a)</td><td>66.39 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (-16.71%)</td><td>0.04 (-14.34%)</td><td>0.04 (-7.99%)</td><td>0.04 (-14.60%)</td><td>0.01 (-17.88%)</td><td>221.50 (+17.07%)</td><td>191.78 (+16.64%)</td><td>191.60 (+8.68%)</td><td>158.80 <b>(+20.03%)</b></td><td>28.85 (+17.45%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>164.42 (n/a)</td><td>176.30 (n/a)</td><td>132.30 (n/a)</td><td>24.56 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (+3.62%)</td><td>0.06 (-1.82%)</td><td>0.05 (-10.31%)</td><td>0.05 (+7.82%)</td><td>0.01 (+8.61%)</td><td>171.90 (-7.23%)</td><td>147.90 (+1.90%)</td><td>156.00 (+11.51%)</td><td>122.00 (-3.48%)</td><td>21.81 (-6.56%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.30 (n/a)</td><td>145.14 (n/a)</td><td>139.90 (n/a)</td><td>126.40 (n/a)</td><td>23.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 <b>(+25.25%)</b></td><td>0.06 <b>(+20.42%)</b></td><td>0.06 (+12.35%)</td><td>0.04 (+10.82%)</td><td>0.01 <b>(+56.83%)</b></td><td>199.90 (-9.79%)</td><td>153.14 (-15.53%)</td><td>143.60 (-10.97%)</td><td>120.80 <b>(-20.16%)</b></td><td>35.71 (+8.93%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>181.30 (n/a)</td><td>161.30 (n/a)</td><td>151.30 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-8.10%)</td><td>0.05 (-14.09%)</td><td>0.04 <b>(-28.69%)</b></td><td>0.04 (-2.05%)</td><td>0.01 (-4.79%)</td><td>225.10 (+2.09%)</td><td>185.82 (+16.24%)</td><td>202.90 <b>(+40.22%)</b></td><td>143.80 (+8.77%)</td><td>35.17 (+0.06%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>159.86 (n/a)</td><td>144.70 (n/a)</td><td>132.20 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (+11.14%)</td><td>0.05 (+3.52%)</td><td>0.05 (-3.09%)</td><td>0.04 <b>(+37.17%)</b></td><td>0.01 <b>(-20.79%)</b></td><td>191.00 <b>(-27.10%)</b></td><td>160.46 (-6.59%)</td><td>160.80 (+3.21%)</td><td>122.30 (-10.01%)</td><td>25.17 <b>(-51.20%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>262.00 (n/a)</td><td>171.78 (n/a)</td><td>155.80 (n/a)</td><td>135.90 (n/a)</td><td>51.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (+4.30%)</td><td>0.05 (+10.70%)</td><td>0.06 (+14.48%)</td><td>0.05 (+8.71%)</td><td>0.00 (-1.07%)</td><td>172.40 (-8.00%)</td><td>151.28 (-9.75%)</td><td>147.30 (-12.69%)</td><td>138.00 (-4.10%)</td><td>13.78 (-11.05%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.40 (n/a)</td><td>167.62 (n/a)</td><td>168.70 (n/a)</td><td>143.90 (n/a)</td><td>15.49 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-15.62%)</td><td>0.05 (-15.26%)</td><td>0.04 (-13.21%)</td><td>0.04 (-8.32%)</td><td>0.01 <b>(-29.54%)</b></td><td>220.30 (+9.06%)</td><td>178.74 (+16.00%)</td><td>182.50 (+15.21%)</td><td>129.80 (+18.54%)</td><td>32.22 (-11.15%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>154.08 (n/a)</td><td>158.40 (n/a)</td><td>109.50 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (+11.33%)</td><td>0.05 (-1.40%)</td><td>0.05 (-4.07%)</td><td>0.04 (-11.95%)</td><td>0.01 <b>(+79.45%)</b></td><td>214.50 (+13.61%)</td><td>169.38 (+4.56%)</td><td>158.30 (+4.21%)</td><td>128.40 (-10.15%)</td><td>39.75 <b>(+87.34%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.80 (n/a)</td><td>162.00 (n/a)</td><td>151.90 (n/a)</td><td>142.90 (n/a)</td><td>21.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (+2.64%)</td><td>0.04 (+4.48%)</td><td>0.04 (-5.17%)</td><td>0.03 <b>(+38.10%)</b></td><td>0.01 <b>(-34.60%)</b></td><td>265.30 <b>(-27.59%)</b></td><td>197.36 (-10.23%)</td><td>184.40 (+5.43%)</td><td>158.50 (-2.58%)</td><td>41.31 <b>(-52.23%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>366.40 (n/a)</td><td>219.84 (n/a)</td><td>174.90 (n/a)</td><td>162.70 (n/a)</td><td>86.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-1.37%)</td><td>0.05 (+4.77%)</td><td>0.05 (+16.74%)</td><td>0.05 (+18.58%)</td><td>0.01 <b>(-45.33%)</b></td><td>178.90 (-15.65%)</td><td>155.74 (-6.95%)</td><td>151.80 (-14.33%)</td><td>133.50 (+1.37%)</td><td>16.92 <b>(-51.02%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>167.38 (n/a)</td><td>177.20 (n/a)</td><td>131.70 (n/a)</td><td>34.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 <b>(-25.83%)</b></td><td>0.05 (-2.64%)</td><td>0.05 (+1.29%)</td><td>0.03 (-0.91%)</td><td>0.01 <b>(-43.57%)</b></td><td>289.70 (+0.94%)</td><td>185.98 (-4.31%)</td><td>165.40 (-1.31%)</td><td>151.30 <b>(+34.85%)</b></td><td>58.48 <b>(-24.46%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>287.00 (n/a)</td><td>194.36 (n/a)</td><td>167.60 (n/a)</td><td>112.20 (n/a)</td><td>77.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-11.59%)</td><td>0.04 (-13.73%)</td><td>0.05 (+1.80%)</td><td>0.02 <b>(-46.33%)</b></td><td>0.02 <b>(+53.11%)</b></td><td>367.90 <b>(+86.37%)</b></td><td>216.84 <b>(+28.58%)</b></td><td>171.60 (-1.77%)</td><td>137.70 (+13.15%)</td><td>95.69 <b>(+236.57%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.40 (n/a)</td><td>168.64 (n/a)</td><td>174.70 (n/a)</td><td>121.70 (n/a)</td><td>28.43 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (-18.16%)</td><td>0.10 (-4.73%)</td><td>0.11 (+0.27%)</td><td>0.08 (-12.81%)</td><td>0.02 (-17.61%)</td><td>210.20 (+14.68%)</td><td>162.16 (+4.82%)</td><td>154.80 (-0.26%)</td><td>129.60 <b>(+22.15%)</b></td><td>34.86 (+16.09%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>183.30 (n/a)</td><td>154.70 (n/a)</td><td>155.20 (n/a)</td><td>106.10 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (+3.97%)</td><td>0.10 (+1.38%)</td><td>0.10 (+2.20%)</td><td>0.09 <b>(+32.10%)</b></td><td>0.02 <b>(-24.28%)</b></td><td>192.40 <b>(-24.28%)</b></td><td>161.10 (-4.73%)</td><td>160.90 (-2.13%)</td><td>120.80 (-3.75%)</td><td>26.41 <b>(-47.74%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>254.10 (n/a)</td><td>169.10 (n/a)</td><td>164.40 (n/a)</td><td>125.50 (n/a)</td><td>50.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (+7.19%)</td><td>0.08 (-3.70%)</td><td>0.07 (-12.32%)</td><td>0.07 (-6.56%)</td><td>0.01 <b>(+109.59%)</b></td><td>226.30 (+7.00%)</td><td>208.16 (+4.70%)</td><td>222.20 (+14.01%)</td><td>175.40 (-6.70%)</td><td>23.28 <b>(+111.30%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>211.50 (n/a)</td><td>198.82 (n/a)</td><td>194.90 (n/a)</td><td>188.00 (n/a)</td><td>11.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (+4.50%)</td><td>0.09 (-4.81%)</td><td>0.09 (-14.56%)</td><td>0.08 (+1.19%)</td><td>0.01 (+13.66%)</td><td>198.90 (-1.14%)</td><td>180.04 (+5.27%)</td><td>188.70 (+17.06%)</td><td>148.60 (-4.31%)</td><td>19.84 (+5.82%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>171.02 (n/a)</td><td>161.20 (n/a)</td><td>155.30 (n/a)</td><td>18.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (-17.51%)</td><td>0.10 (-2.74%)</td><td>0.10 (+5.35%)</td><td>0.08 (-5.49%)</td><td>0.02 <b>(-21.92%)</b></td><td>204.90 (+5.84%)</td><td>167.10 (+2.04%)</td><td>166.50 (-5.07%)</td><td>131.30 <b>(+21.24%)</b></td><td>34.22 (+4.02%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>193.60 (n/a)</td><td>163.76 (n/a)</td><td>175.40 (n/a)</td><td>108.30 (n/a)</td><td>32.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 <b>(+32.45%)</b></td><td>0.11 (+10.32%)</td><td>0.10 (+5.84%)</td><td>0.07 <b>(-24.31%)</b></td><td>0.03 <b>(+293.02%)</b></td><td>251.00 <b>(+32.11%)</b></td><td>166.36 (-3.11%)</td><td>158.50 (-5.49%)</td><td>119.50 <b>(-24.51%)</b></td><td>53.04 <b>(+287.53%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>171.70 (n/a)</td><td>167.70 (n/a)</td><td>158.30 (n/a)</td><td>13.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (+9.72%)</td><td>0.11 (+0.10%)</td><td>0.09 (-3.13%)</td><td>0.08 (-1.05%)</td><td>0.02 (+18.07%)</td><td>195.20 (+1.04%)</td><td>159.56 (+0.83%)</td><td>175.20 (+3.24%)</td><td>115.10 (-8.87%)</td><td>33.43 (+12.27%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.20 (n/a)</td><td>158.24 (n/a)</td><td>169.70 (n/a)</td><td>126.30 (n/a)</td><td>29.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (-1.66%)</td><td>0.10 (-4.51%)</td><td>0.11 (-7.83%)</td><td>0.08 (-2.23%)</td><td>0.02 (-19.76%)</td><td>203.60 (+2.26%)</td><td>163.82 (+3.45%)</td><td>153.10 (+8.50%)</td><td>130.40 (+1.72%)</td><td>29.37 (-16.30%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.10 (n/a)</td><td>158.36 (n/a)</td><td>141.10 (n/a)</td><td>128.20 (n/a)</td><td>35.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (-4.67%)</td><td>0.10 (-5.02%)</td><td>0.09 <b>(-21.53%)</b></td><td>0.09 (+11.75%)</td><td>0.02 <b>(-23.55%)</b></td><td>187.70 (-10.53%)</td><td>164.80 (+3.31%)</td><td>179.50 <b>(+27.40%)</b></td><td>134.20 (+4.84%)</td><td>27.44 <b>(-27.61%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.80 (n/a)</td><td>159.52 (n/a)</td><td>140.90 (n/a)</td><td>128.00 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (+11.25%)</td><td>0.10 (+4.45%)</td><td>0.09 (-0.32%)</td><td>0.08 (-3.53%)</td><td>0.01 <b>(+62.14%)</b></td><td>205.10 (+3.64%)</td><td>173.22 (-3.38%)</td><td>176.70 (+0.34%)</td><td>140.50 (-10.11%)</td><td>23.87 <b>(+49.81%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>179.28 (n/a)</td><td>176.10 (n/a)</td><td>156.30 (n/a)</td><td>15.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (+0.48%)</td><td>0.09 (+2.70%)</td><td>0.09 (+1.07%)</td><td>0.08 (+8.63%)</td><td>0.01 (-12.68%)</td><td>216.10 (-7.93%)</td><td>183.32 (-3.20%)</td><td>184.10 (-1.07%)</td><td>159.20 (-0.50%)</td><td>23.66 <b>(-20.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>189.38 (n/a)</td><td>186.10 (n/a)</td><td>160.00 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (-5.23%)</td><td>0.09 (-2.74%)</td><td>0.09 (+0.90%)</td><td>0.07 (-10.62%)</td><td>0.02 (-2.88%)</td><td>229.90 (+11.87%)</td><td>182.60 (+3.18%)</td><td>179.90 (-0.88%)</td><td>133.70 (+5.52%)</td><td>36.03 (+15.84%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.50 (n/a)</td><td>176.98 (n/a)</td><td>181.50 (n/a)</td><td>126.70 (n/a)</td><td>31.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (+15.16%)</td><td>0.10 (+7.52%)</td><td>0.10 (+10.25%)</td><td>0.07 (-12.35%)</td><td>0.02 <b>(+110.82%)</b></td><td>219.50 (+14.09%)</td><td>164.58 (-4.88%)</td><td>158.80 (-9.31%)</td><td>132.40 (-13.18%)</td><td>33.32 <b>(+114.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>173.02 (n/a)</td><td>175.10 (n/a)</td><td>152.50 (n/a)</td><td>15.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (-11.60%)</td><td>0.09 (-6.79%)</td><td>0.09 (+2.56%)</td><td>0.07 (-5.26%)</td><td>0.01 <b>(-40.06%)</b></td><td>237.00 (+5.52%)</td><td>186.16 (+4.96%)</td><td>179.50 (-2.50%)</td><td>155.20 (+13.12%)</td><td>30.36 <b>(-22.70%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.60 (n/a)</td><td>177.36 (n/a)</td><td>184.10 (n/a)</td><td>137.20 (n/a)</td><td>39.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (-1.92%)</td><td>0.10 (-0.98%)</td><td>0.09 (+1.91%)</td><td>0.08 (+4.05%)</td><td>0.02 (-15.16%)</td><td>202.10 (-3.90%)</td><td>170.26 (-0.09%)</td><td>178.20 (-1.87%)</td><td>126.80 (+2.01%)</td><td>28.41 (-18.08%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>170.42 (n/a)</td><td>181.60 (n/a)</td><td>124.30 (n/a)</td><td>34.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (-9.32%)</td><td>0.09 (-3.96%)</td><td>0.09 (+2.99%)</td><td>0.07 (+8.43%)</td><td>0.01 <b>(-32.31%)</b></td><td>232.80 (-7.77%)</td><td>195.36 (+2.28%)</td><td>186.30 (-2.92%)</td><td>169.30 (+10.29%)</td><td>28.88 <b>(-29.50%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>252.40 (n/a)</td><td>191.00 (n/a)</td><td>191.90 (n/a)</td><td>153.50 (n/a)</td><td>40.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (+13.43%)</td><td>0.25 <b>(+26.46%)</b></td><td>0.26 <b>(+38.13%)</b></td><td>0.17 (+2.85%)</td><td>0.04 <b>(+52.63%)</b></td><td>188.70 (-2.78%)</td><td>136.80 (-19.72%)</td><td>124.30 <b>(-27.61%)</b></td><td>120.30 (-11.80%)</td><td>29.21 <b>(+36.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.10 (n/a)</td><td>170.40 (n/a)</td><td>171.70 (n/a)</td><td>136.40 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (-1.83%)</td><td>0.22 (+4.71%)</td><td>0.22 (+13.77%)</td><td>0.17 (-3.97%)</td><td>0.04 (+10.32%)</td><td>191.10 (+4.14%)</td><td>154.08 (-4.01%)</td><td>148.40 (-12.14%)</td><td>127.90 (+1.83%)</td><td>27.82 (+14.65%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.50 (n/a)</td><td>160.52 (n/a)</td><td>168.90 (n/a)</td><td>125.60 (n/a)</td><td>24.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (-5.30%)</td><td>0.17 (+14.87%)</td><td>0.17 <b>(+26.91%)</b></td><td>0.14 (+19.00%)</td><td>0.02 <b>(-46.22%)</b></td><td>236.00 (-15.98%)</td><td>199.64 (-14.77%)</td><td>189.70 <b>(-21.19%)</b></td><td>187.00 (+5.59%)</td><td>20.59 <b>(-51.92%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>280.90 (n/a)</td><td>234.24 (n/a)</td><td>240.70 (n/a)</td><td>177.10 (n/a)</td><td>42.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (-18.05%)</td><td>0.17 (-9.90%)</td><td>0.17 <b>(-20.09%)</b></td><td>0.15 (+8.31%)</td><td>0.01 <b>(-67.73%)</b></td><td>214.30 (-7.67%)</td><td>189.84 (+7.51%)</td><td>188.10 <b>(+25.15%)</b></td><td>178.20 <b>(+22.05%)</b></td><td>14.61 <b>(-62.76%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>232.10 (n/a)</td><td>176.58 (n/a)</td><td>150.30 (n/a)</td><td>146.00 (n/a)</td><td>39.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.29 <b>(+35.24%)</b></td><td>0.22 (+12.47%)</td><td>0.25 <b>(+27.89%)</b></td><td>0.14 <b>(-26.25%)</b></td><td>0.06 <b>(+634.78%)</b></td><td>231.70 <b>(+35.58%)</b></td><td>157.24 (-4.93%)</td><td>129.90 <b>(-21.79%)</b></td><td>114.50 <b>(-26.03%)</b></td><td>48.83 <b>(+641.95%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>170.90 (n/a)</td><td>165.40 (n/a)</td><td>166.10 (n/a)</td><td>154.80 (n/a)</td><td>6.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (+0.64%)</td><td>0.24 (+13.49%)</td><td>0.25 <b>(+28.83%)</b></td><td>0.19 (+7.66%)</td><td>0.03 (-11.14%)</td><td>168.30 (-7.12%)</td><td>141.50 (-12.35%)</td><td>132.60 <b>(-22.37%)</b></td><td>122.60 (-0.65%)</td><td>19.74 (-17.37%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>181.20 (n/a)</td><td>161.44 (n/a)</td><td>170.80 (n/a)</td><td>123.40 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.23 (+1.84%)</td><td>0.19 (+1.57%)</td><td>0.20 (+12.03%)</td><td>0.10 <b>(-36.31%)</b></td><td>0.05 <b>(+95.13%)</b></td><td>313.20 <b>(+56.99%)</b></td><td>187.60 (+5.50%)</td><td>166.30 (-10.74%)</td><td>141.80 (-1.80%)</td><td>71.33 <b>(+213.11%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.50 (n/a)</td><td>177.82 (n/a)</td><td>186.30 (n/a)</td><td>144.40 (n/a)</td><td>22.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (-6.53%)</td><td>0.21 (+4.88%)</td><td>0.21 (+14.88%)</td><td>0.17 (+17.19%)</td><td>0.03 <b>(-36.76%)</b></td><td>197.30 (-14.66%)</td><td>159.10 (-7.15%)</td><td>154.10 (-12.94%)</td><td>134.10 (+7.02%)</td><td>23.84 <b>(-41.00%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>231.20 (n/a)</td><td>171.36 (n/a)</td><td>177.00 (n/a)</td><td>125.30 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 <b>(+20.80%)</b></td><td>0.19 (-3.11%)</td><td>0.18 (-2.42%)</td><td>0.11 <b>(-35.33%)</b></td><td>0.06 <b>(+388.46%)</b></td><td>288.70 <b>(+54.63%)</b></td><td>194.44 (+13.10%)</td><td>178.10 (+2.47%)</td><td>132.40 (-17.20%)</td><td>68.22 <b>(+507.06%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>186.70 (n/a)</td><td>171.92 (n/a)</td><td>173.80 (n/a)</td><td>159.90 (n/a)</td><td>11.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 <b>(+27.80%)</b></td><td>0.22 (+11.14%)</td><td>0.21 (+6.07%)</td><td>0.20 (+7.45%)</td><td>0.03 <b>(+194.17%)</b></td><td>167.60 (-6.94%)</td><td>151.44 (-9.30%)</td><td>155.20 (-5.71%)</td><td>126.30 <b>(-21.80%)</b></td><td>16.09 <b>(+111.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>166.96 (n/a)</td><td>164.60 (n/a)</td><td>161.50 (n/a)</td><td>7.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (-17.90%)</td><td>0.21 (-10.79%)</td><td>0.23 (-1.61%)</td><td>0.09 <b>(-46.78%)</b></td><td>0.07 (+17.39%)</td><td>363.00 <b>(+87.89%)</b></td><td>185.50 <b>(+23.86%)</b></td><td>140.40 (+1.67%)</td><td>130.00 <b>(+21.84%)</b></td><td>99.98 <b>(+169.14%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>193.20 (n/a)</td><td>149.76 (n/a)</td><td>138.10 (n/a)</td><td>106.70 (n/a)</td><td>37.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (+17.78%)</td><td>0.23 <b>(+31.00%)</b></td><td>0.24 <b>(+39.58%)</b></td><td>0.19 <b>(+45.89%)</b></td><td>0.03 <b>(-27.46%)</b></td><td>175.60 <b>(-31.46%)</b></td><td>142.42 <b>(-25.65%)</b></td><td>138.20 <b>(-28.32%)</b></td><td>126.40 (-15.11%)</td><td>19.31 <b>(-55.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>256.20 (n/a)</td><td>191.56 (n/a)</td><td>192.80 (n/a)</td><td>148.90 (n/a)</td><td>43.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (+8.46%)</td><td>0.20 (+7.28%)</td><td>0.18 (-2.54%)</td><td>0.17 <b>(+28.08%)</b></td><td>0.04 (+1.13%)</td><td>194.20 <b>(-21.91%)</b></td><td>166.10 (-7.75%)</td><td>186.40 (+2.59%)</td><td>130.30 (-7.85%)</td><td>32.31 <b>(-26.31%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>248.70 (n/a)</td><td>180.06 (n/a)</td><td>181.70 (n/a)</td><td>141.40 (n/a)</td><td>43.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (+16.85%)</td><td>0.23 <b>(+25.83%)</b></td><td>0.22 <b>(+22.74%)</b></td><td>0.20 <b>(+45.12%)</b></td><td>0.03 (-19.79%)</td><td>162.50 <b>(-31.11%)</b></td><td>144.00 <b>(-21.78%)</b></td><td>146.70 (-18.50%)</td><td>125.30 (-14.41%)</td><td>15.75 <b>(-53.50%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>235.90 (n/a)</td><td>184.10 (n/a)</td><td>180.00 (n/a)</td><td>146.40 (n/a)</td><td>33.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (-1.90%)</td><td>0.21 <b>(+20.01%)</b></td><td>0.23 <b>(+40.04%)</b></td><td>0.17 (+18.63%)</td><td>0.04 (-16.04%)</td><td>197.20 (-15.73%)</td><td>160.24 (-17.81%)</td><td>142.50 <b>(-28.61%)</b></td><td>135.30 (+1.96%)</td><td>28.82 <b>(-24.83%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>234.00 (n/a)</td><td>194.96 (n/a)</td><td>199.60 (n/a)</td><td>132.70 (n/a)</td><td>38.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.31 (+19.25%)</td><td>0.22 (+11.88%)</td><td>0.22 (+12.84%)</td><td>0.15 (+12.75%)</td><td>0.06 <b>(+22.15%)</b></td><td>214.10 (-11.35%)</td><td>156.78 (-10.10%)</td><td>147.90 (-11.38%)</td><td>104.10 (-16.12%)</td><td>42.61 (-8.90%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>241.50 (n/a)</td><td>174.40 (n/a)</td><td>166.90 (n/a)</td><td>124.10 (n/a)</td><td>46.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (-0.31%)</td><td>0.16 (-0.29%)</td><td>0.16 (-0.32%)</td><td>0.16 (-0.24%)</td><td>0.00 <b>(-29.02%)</b></td><td>52607.20 (+0.24%)</td><td>52561.36 (+0.29%)</td><td>52549.10 (+0.33%)</td><td>52517.30 (+0.31%)</td><td>40.25 <b>(-28.65%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52481.00 (n/a)</td><td>52408.44 (n/a)</td><td>52378.40 (n/a)</td><td>52354.10 (n/a)</td><td>56.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52656.90 (n/a)</td><td>52562.72 (n/a)</td><td>52557.30 (n/a)</td><td>52493.90 (n/a)</td><td>60.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>415886.30 (n/a)</td><td>415727.64 (n/a)</td><td>415723.80 (n/a)</td><td>415547.10 (n/a)</td><td>151.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (-8.27%)</td><td>0.16 (-18.94%)</td><td>0.15 <b>(-23.29%)</b></td><td>0.13 <b>(-23.08%)</b></td><td>0.03 <b>(+33.61%)</b></td><td>183.70 <b>(+30.01%)</b></td><td>157.56 <b>(+25.21%)</b></td><td>163.00 <b>(+30.40%)</b></td><td>118.20 (+9.04%)</td><td>26.11 <b>(+86.09%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>141.30 (n/a)</td><td>125.84 (n/a)</td><td>125.00 (n/a)</td><td>108.40 (n/a)</td><td>14.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.39 (-12.26%)</td><td>0.29 (-17.94%)</td><td>0.29 (-19.83%)</td><td>0.22 <b>(+37.04%)</b></td><td>0.07 <b>(-40.38%)</b></td><td>221.30 <b>(-27.01%)</b></td><td>180.38 (+10.87%)</td><td>169.80 <b>(+24.76%)</b></td><td>124.80 (+13.97%)</td><td>40.85 <b>(-49.45%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.45 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>303.20 (n/a)</td><td>162.70 (n/a)</td><td>136.10 (n/a)</td><td>109.50 (n/a)</td><td>80.81 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>13.88 (+1.19%)</td><td>12.96 (-1.44%)</td><td>13.00 (-1.50%)</td><td>11.19 (-10.25%)</td><td>1.08 <b>(+132.78%)</b></td><td>936.90 (+11.43%)</td><td>814.16 (+1.96%)</td><td>806.60 (+1.51%)</td><td>755.40 (-1.18%)</td><td>73.08 <b>(+157.26%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>13.72 (n/a)</td><td>13.15 (n/a)</td><td>13.20 (n/a)</td><td>12.47 (n/a)</td><td>0.46 (n/a)</td><td>840.80 (n/a)</td><td>798.48 (n/a)</td><td>794.60 (n/a)</td><td>764.40 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.33 (-14.28%)</td><td>0.26 (-7.35%)</td><td>0.26 (-3.31%)</td><td>0.20 (-12.38%)</td><td>0.06 (+3.35%)</td><td>207.70 (+14.12%)</td><td>164.20 (+9.60%)</td><td>157.90 (+3.41%)</td><td>124.20 (+16.62%)</td><td>39.51 <b>(+45.23%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>182.00 (n/a)</td><td>149.82 (n/a)</td><td>152.70 (n/a)</td><td>106.50 (n/a)</td><td>27.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (+3.13%)</td><td>0.03 (-1.00%)</td><td>0.03 (-15.91%)</td><td>0.03 (+12.92%)</td><td>0.01 (+11.10%)</td><td>177.50 (-11.47%)</td><td>157.66 (+1.13%)</td><td>173.40 (+18.93%)</td><td>126.40 (-2.99%)</td><td>25.01 (-6.31%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>155.90 (n/a)</td><td>145.80 (n/a)</td><td>130.30 (n/a)</td><td>26.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-0.53%)</td><td>0.03 (-4.42%)</td><td>0.02 (-17.41%)</td><td>0.02 (+8.49%)</td><td>0.01 (+8.75%)</td><td>185.50 (-7.85%)</td><td>161.28 (+4.97%)</td><td>181.30 <b>(+21.11%)</b></td><td>125.30 (+0.56%)</td><td>30.96 (+1.46%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.30 (n/a)</td><td>153.64 (n/a)</td><td>149.70 (n/a)</td><td>124.60 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (-11.90%)</td><td>0.04 (-13.81%)</td><td>0.04 (-13.80%)</td><td>0.03 (-14.99%)</td><td>0.01 (+3.52%)</td><td>210.50 (+17.66%)</td><td>165.68 (+17.62%)</td><td>158.60 (+16.02%)</td><td>127.90 (+13.49%)</td><td>39.35 <b>(+39.17%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>140.86 (n/a)</td><td>136.70 (n/a)</td><td>112.70 (n/a)</td><td>28.28 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-3.02%)</td><td>0.03 (-0.55%)</td><td>0.03 (+2.35%)</td><td>0.02 (-0.64%)</td><td>0.00 (-3.17%)</td><td>205.00 (+0.64%)</td><td>162.28 (+0.50%)</td><td>155.70 (-2.32%)</td><td>143.00 (+3.10%)</td><td>25.16 (-0.39%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.70 (n/a)</td><td>161.48 (n/a)</td><td>159.40 (n/a)</td><td>138.70 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-11.73%)</td><td>0.03 (-4.44%)</td><td>0.03 (-1.75%)</td><td>0.03 (-0.41%)</td><td>0.00 <b>(-47.55%)</b></td><td>180.00 (+0.39%)</td><td>162.52 (+3.63%)</td><td>160.30 (+1.78%)</td><td>146.90 (+13.35%)</td><td>12.22 <b>(-40.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>179.30 (n/a)</td><td>156.82 (n/a)</td><td>157.50 (n/a)</td><td>129.60 (n/a)</td><td>20.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+9.87%)</td><td>0.03 (-0.55%)</td><td>0.02 (-5.80%)</td><td>0.02 (+4.68%)</td><td>0.00 <b>(+27.71%)</b></td><td>200.50 (-4.48%)</td><td>167.10 (+1.20%)</td><td>164.50 (+6.13%)</td><td>132.60 (-8.99%)</td><td>28.12 (+9.17%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.90 (n/a)</td><td>165.12 (n/a)</td><td>155.00 (n/a)</td><td>145.70 (n/a)</td><td>25.76 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 <b>(+26.22%)</b></td><td>0.04 (+3.91%)</td><td>0.03 (-3.01%)</td><td>0.03 (-11.07%)</td><td>0.01 <b>(+152.40%)</b></td><td>197.30 (+12.42%)</td><td>153.34 (+0.68%)</td><td>154.00 (+3.08%)</td><td>105.70 <b>(-20.76%)</b></td><td>38.89 <b>(+127.00%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>175.50 (n/a)</td><td>152.30 (n/a)</td><td>149.40 (n/a)</td><td>133.40 (n/a)</td><td>17.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+7.66%)</td><td>0.03 (+7.77%)</td><td>0.03 (+17.27%)</td><td>0.02 (+7.01%)</td><td>0.00 <b>(+29.82%)</b></td><td>187.60 (-6.57%)</td><td>157.20 (-6.46%)</td><td>144.40 (-14.71%)</td><td>131.90 (-7.11%)</td><td>27.72 (+16.34%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.80 (n/a)</td><td>168.06 (n/a)</td><td>169.30 (n/a)</td><td>142.00 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 <b>(+21.67%)</b></td><td>0.03 (-0.20%)</td><td>0.03 (-8.39%)</td><td>0.02 (-17.63%)</td><td>0.01 <b>(+273.25%)</b></td><td>205.70 <b>(+21.43%)</b></td><td>161.98 (+3.89%)</td><td>169.60 (+9.14%)</td><td>118.80 (-17.84%)</td><td>34.90 <b>(+267.08%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>169.40 (n/a)</td><td>155.92 (n/a)</td><td>155.40 (n/a)</td><td>144.60 (n/a)</td><td>9.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+16.72%)</td><td>0.02 (-8.36%)</td><td>0.02 (-1.86%)</td><td>0.01 <b>(-34.55%)</b></td><td>0.01 <b>(+210.41%)</b></td><td>284.90 <b>(+52.76%)</b></td><td>196.78 (+18.27%)</td><td>165.60 (+1.91%)</td><td>125.50 (-14.33%)</td><td>65.78 <b>(+315.57%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.50 (n/a)</td><td>166.38 (n/a)</td><td>162.50 (n/a)</td><td>146.50 (n/a)</td><td>15.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (-3.60%)</td><td>0.03 (+13.33%)</td><td>0.03 (+17.88%)</td><td>0.03 <b>(+31.08%)</b></td><td>0.00 <b>(-47.01%)</b></td><td>179.30 <b>(-23.70%)</b></td><td>147.86 (-15.08%)</td><td>143.70 (-15.17%)</td><td>128.40 (+3.80%)</td><td>18.85 <b>(-56.96%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.00 (n/a)</td><td>174.12 (n/a)</td><td>169.40 (n/a)</td><td>123.70 (n/a)</td><td>43.81 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+14.43%)</td><td>0.02 (+6.42%)</td><td>0.02 (-12.03%)</td><td>0.02 <b>(+49.04%)</b></td><td>0.00 <b>(-22.20%)</b></td><td>211.40 <b>(-32.89%)</b></td><td>174.54 (-10.33%)</td><td>181.40 (+13.66%)</td><td>134.70 (-12.65%)</td><td>30.23 <b>(-55.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>315.00 (n/a)</td><td>194.64 (n/a)</td><td>159.60 (n/a)</td><td>154.20 (n/a)</td><td>68.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 <b>(-25.13%)</b></td><td>0.02 (-8.26%)</td><td>0.02 (-1.06%)</td><td>0.02 (-4.96%)</td><td>0.00 <b>(-39.83%)</b></td><td>226.40 (+5.25%)</td><td>191.24 (+6.85%)</td><td>183.20 (+1.05%)</td><td>158.40 <b>(+33.56%)</b></td><td>33.23 (-11.38%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>178.98 (n/a)</td><td>181.30 (n/a)</td><td>118.60 (n/a)</td><td>37.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 <b>(-20.45%)</b></td><td>0.02 (-16.55%)</td><td>0.02 <b>(-20.30%)</b></td><td>0.02 (-4.05%)</td><td>0.00 <b>(-31.04%)</b></td><td>232.10 (+4.22%)</td><td>196.60 (+18.32%)</td><td>197.90 <b>(+25.49%)</b></td><td>156.00 <b>(+25.71%)</b></td><td>32.05 (-10.42%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>166.16 (n/a)</td><td>157.70 (n/a)</td><td>124.10 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 <b>(+39.37%)</b></td><td>0.02 (+7.97%)</td><td>0.02 (-9.38%)</td><td>0.02 (-1.63%)</td><td>0.01 <b>(+183.62%)</b></td><td>227.20 (+1.66%)</td><td>189.42 (-3.60%)</td><td>207.20 (+10.33%)</td><td>127.90 <b>(-28.23%)</b></td><td>42.92 <b>(+110.42%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.50 (n/a)</td><td>196.50 (n/a)</td><td>187.80 (n/a)</td><td>178.20 (n/a)</td><td>20.40 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (-0.50%)</td><td>0.02 (+8.87%)</td><td>0.02 (+1.86%)</td><td>0.02 <b>(+52.99%)</b></td><td>0.00 <b>(-67.66%)</b></td><td>217.50 <b>(-34.63%)</b></td><td>202.66 (-11.59%)</td><td>200.80 (-1.81%)</td><td>189.20 (+0.53%)</td><td>11.94 <b>(-79.66%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>332.70 (n/a)</td><td>229.22 (n/a)</td><td>204.50 (n/a)</td><td>188.20 (n/a)</td><td>58.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 <b>(+44.96%)</b></td><td>0.06 <b>(+23.27%)</b></td><td>0.06 (+19.24%)</td><td>0.04 (+3.75%)</td><td>0.02 <b>(+109.63%)</b></td><td>190.00 (-3.65%)</td><td>138.88 (-16.00%)</td><td>142.50 (-16.13%)</td><td>93.00 <b>(-31.06%)</b></td><td>35.54 <b>(+38.92%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>165.34 (n/a)</td><td>169.90 (n/a)</td><td>134.90 (n/a)</td><td>25.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (+0.39%)</td><td>0.07 (-5.57%)</td><td>0.07 (-9.95%)</td><td>0.07 (+4.44%)</td><td>0.01 <b>(-25.71%)</b></td><td>182.30 (-4.25%)</td><td>166.58 (+5.43%)</td><td>166.50 (+11.07%)</td><td>147.40 (-0.41%)</td><td>12.60 <b>(-30.66%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>158.00 (n/a)</td><td>149.90 (n/a)</td><td>148.00 (n/a)</td><td>18.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (+2.09%)</td><td>0.05 (-4.35%)</td><td>0.05 (+0.25%)</td><td>0.03 <b>(-29.37%)</b></td><td>0.01 <b>(+56.90%)</b></td><td>254.70 <b>(+41.58%)</b></td><td>170.46 (+8.46%)</td><td>154.30 (-0.26%)</td><td>129.00 (-2.05%)</td><td>48.64 <b>(+126.99%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.90 (n/a)</td><td>157.16 (n/a)</td><td>154.70 (n/a)</td><td>131.70 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (+0.76%)</td><td>0.06 (-8.22%)</td><td>0.06 (-13.25%)</td><td>0.05 (-10.30%)</td><td>0.01 <b>(+26.31%)</b></td><td>197.90 (+11.49%)</td><td>164.70 (+10.34%)</td><td>157.60 (+15.29%)</td><td>131.20 (-0.76%)</td><td>30.97 <b>(+45.39%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>149.26 (n/a)</td><td>136.70 (n/a)</td><td>132.20 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (-4.94%)</td><td>0.05 (-4.06%)</td><td>0.05 (-1.08%)</td><td>0.05 (+10.58%)</td><td>0.01 <b>(-33.38%)</b></td><td>171.70 (-9.58%)</td><td>154.72 (+2.22%)</td><td>159.40 (+1.14%)</td><td>122.00 (+5.26%)</td><td>19.43 <b>(-36.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>151.36 (n/a)</td><td>157.60 (n/a)</td><td>115.90 (n/a)</td><td>30.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 <b>(+23.93%)</b></td><td>0.07 (+2.65%)</td><td>0.06 (-3.18%)</td><td>0.05 (-12.38%)</td><td>0.02 <b>(+164.93%)</b></td><td>206.90 (+14.18%)</td><td>162.98 (+1.72%)</td><td>157.90 (+3.27%)</td><td>118.30 (-19.30%)</td><td>40.77 <b>(+152.36%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>181.20 (n/a)</td><td>160.22 (n/a)</td><td>152.90 (n/a)</td><td>146.60 (n/a)</td><td>16.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-14.00%)</td><td>0.05 (-10.42%)</td><td>0.05 (-12.24%)</td><td>0.04 (-12.79%)</td><td>0.01 (-7.56%)</td><td>189.70 (+14.69%)</td><td>166.06 (+11.93%)</td><td>176.00 (+13.99%)</td><td>135.20 (+16.25%)</td><td>24.44 <b>(+25.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.40 (n/a)</td><td>148.36 (n/a)</td><td>154.40 (n/a)</td><td>116.30 (n/a)</td><td>19.44 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 <b>(-27.21%)</b></td><td>0.04 (-16.68%)</td><td>0.04 (-18.71%)</td><td>0.04 (+3.75%)</td><td>0.00 <b>(-63.23%)</b></td><td>229.70 (-3.61%)</td><td>210.56 (+16.69%)</td><td>210.10 <b>(+23.01%)</b></td><td>186.30 <b>(+37.39%)</b></td><td>18.63 <b>(-51.29%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>180.44 (n/a)</td><td>170.80 (n/a)</td><td>135.60 (n/a)</td><td>38.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (-6.50%)</td><td>0.05 (-14.55%)</td><td>0.05 (-12.80%)</td><td>0.04 (-12.24%)</td><td>0.01 (-14.90%)</td><td>207.30 (+13.96%)</td><td>174.46 (+16.52%)</td><td>172.20 (+14.72%)</td><td>125.80 (+6.97%)</td><td>32.15 (+3.38%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.90 (n/a)</td><td>149.72 (n/a)</td><td>150.10 (n/a)</td><td>117.60 (n/a)</td><td>31.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (+12.40%)</td><td>0.06 (+4.76%)</td><td>0.05 (+2.96%)</td><td>0.04 (-10.20%)</td><td>0.01 <b>(+85.87%)</b></td><td>224.30 (+11.37%)</td><td>170.22 (-2.16%)</td><td>171.10 (-2.89%)</td><td>130.50 (-10.98%)</td><td>36.21 <b>(+84.82%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>173.98 (n/a)</td><td>176.20 (n/a)</td><td>146.60 (n/a)</td><td>19.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-8.52%)</td><td>0.05 (-2.22%)</td><td>0.05 (+0.91%)</td><td>0.03 <b>(-22.04%)</b></td><td>0.01 (+13.66%)</td><td>272.70 <b>(+28.27%)</b></td><td>178.26 (+5.18%)</td><td>159.80 (-0.87%)</td><td>135.90 (+9.33%)</td><td>55.61 <b>(+61.91%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>169.48 (n/a)</td><td>161.20 (n/a)</td><td>124.30 (n/a)</td><td>34.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (-15.53%)</td><td>0.04 (-19.71%)</td><td>0.04 (-9.90%)</td><td>0.03 <b>(-34.24%)</b></td><td>0.01 <b>(+23.13%)</b></td><td>304.20 <b>(+52.02%)</b></td><td>223.20 <b>(+28.45%)</b></td><td>202.20 (+10.98%)</td><td>161.80 (+18.36%)</td><td>56.50 <b>(+127.67%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>173.76 (n/a)</td><td>182.20 (n/a)</td><td>136.70 (n/a)</td><td>24.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (-3.70%)</td><td>0.04 (-11.84%)</td><td>0.05 (+3.64%)</td><td>0.02 <b>(-33.61%)</b></td><td>0.01 <b>(+41.58%)</b></td><td>343.20 <b>(+50.66%)</b></td><td>219.12 <b>(+21.50%)</b></td><td>177.60 (-3.48%)</td><td>142.30 (+3.79%)</td><td>82.67 <b>(+127.92%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>180.34 (n/a)</td><td>184.00 (n/a)</td><td>137.10 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (+3.40%)</td><td>0.04 (-15.32%)</td><td>0.04 (-9.81%)</td><td>0.03 <b>(-36.63%)</b></td><td>0.01 <b>(+272.44%)</b></td><td>300.60 <b>(+57.80%)</b></td><td>220.12 <b>(+23.89%)</b></td><td>193.90 (+10.86%)</td><td>160.50 (-3.31%)</td><td>56.76 <b>(+477.22%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>190.50 (n/a)</td><td>177.68 (n/a)</td><td>174.90 (n/a)</td><td>166.00 (n/a)</td><td>9.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 <b>(+51.32%)</b></td><td>0.04 (+3.01%)</td><td>0.04 (-1.08%)</td><td>0.03 <b>(-20.80%)</b></td><td>0.01 <b>(+623.28%)</b></td><td>264.60 <b>(+26.24%)</b></td><td>206.70 (+4.85%)</td><td>199.10 (+1.07%)</td><td>123.30 <b>(-33.92%)</b></td><td>59.69 <b>(+522.85%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.60 (n/a)</td><td>197.14 (n/a)</td><td>197.00 (n/a)</td><td>186.60 (n/a)</td><td>9.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (-8.84%)</td><td>0.10 (-3.96%)</td><td>0.09 (-18.58%)</td><td>0.08 <b>(+54.67%)</b></td><td>0.01 <b>(-55.37%)</b></td><td>202.40 <b>(-35.34%)</b></td><td>173.84 (-5.30%)</td><td>175.50 <b>(+22.81%)</b></td><td>143.10 (+9.66%)</td><td>25.32 <b>(-67.48%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>313.00 (n/a)</td><td>183.56 (n/a)</td><td>142.90 (n/a)</td><td>130.50 (n/a)</td><td>77.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (+1.63%)</td><td>0.15 (-7.00%)</td><td>0.16 (-11.44%)</td><td>0.12 (-7.98%)</td><td>0.03 <b>(+36.96%)</b></td><td>203.10 (+8.73%)</td><td>165.50 (+8.94%)</td><td>158.40 (+12.98%)</td><td>136.30 (-1.59%)</td><td>30.05 <b>(+45.85%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>186.80 (n/a)</td><td>151.92 (n/a)</td><td>140.20 (n/a)</td><td>138.50 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (-4.53%)</td><td>0.09 (-16.60%)</td><td>0.09 (-18.94%)</td><td>0.08 <b>(-22.49%)</b></td><td>0.01 <b>(+148.15%)</b></td><td>197.50 <b>(+29.08%)</b></td><td>178.18 <b>(+21.33%)</b></td><td>186.00 <b>(+23.34%)</b></td><td>145.20 (+4.76%)</td><td>21.97 <b>(+236.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>153.00 (n/a)</td><td>146.86 (n/a)</td><td>150.80 (n/a)</td><td>138.60 (n/a)</td><td>6.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (+3.53%)</td><td>0.13 (+13.27%)</td><td>0.13 <b>(+21.95%)</b></td><td>0.09 (+16.47%)</td><td>0.02 (-8.57%)</td><td>223.30 (-14.15%)</td><td>164.12 (-12.84%)</td><td>157.10 (-18.01%)</td><td>134.20 (-3.38%)</td><td>35.34 <b>(-23.32%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>260.10 (n/a)</td><td>188.30 (n/a)</td><td>191.60 (n/a)</td><td>138.90 (n/a)</td><td>46.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (+1.31%)</td><td>0.10 (-0.84%)</td><td>0.09 (-19.85%)</td><td>0.08 <b>(+66.56%)</b></td><td>0.02 <b>(-36.07%)</b></td><td>195.80 <b>(-39.98%)</b></td><td>165.32 (-8.00%)</td><td>182.60 <b>(+24.81%)</b></td><td>125.00 (-1.26%)</td><td>31.34 <b>(-62.71%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>326.20 (n/a)</td><td>179.70 (n/a)</td><td>146.30 (n/a)</td><td>126.60 (n/a)</td><td>84.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 <b>(-23.80%)</b></td><td>0.12 <b>(-21.47%)</b></td><td>0.12 (-19.48%)</td><td>0.09 <b>(-23.73%)</b></td><td>0.03 <b>(-21.53%)</b></td><td>225.50 <b>(+31.10%)</b></td><td>173.72 <b>(+27.66%)</b></td><td>168.10 <b>(+24.15%)</b></td><td>129.10 <b>(+31.20%)</b></td><td>38.86 <b>(+36.04%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>172.00 (n/a)</td><td>136.08 (n/a)</td><td>135.40 (n/a)</td><td>98.40 (n/a)</td><td>28.57 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (+5.95%)</td><td>0.09 (-6.00%)</td><td>0.09 (-5.58%)</td><td>0.07 (-13.28%)</td><td>0.02 <b>(+27.17%)</b></td><td>224.40 (+15.31%)</td><td>179.90 (+8.02%)</td><td>182.90 (+5.91%)</td><td>125.00 (-5.59%)</td><td>36.57 <b>(+33.44%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.60 (n/a)</td><td>166.54 (n/a)</td><td>172.70 (n/a)</td><td>132.40 (n/a)</td><td>27.40 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 <b>(-30.25%)</b></td><td>0.12 (-15.24%)</td><td>0.12 (-1.29%)</td><td>0.09 (+3.61%)</td><td>0.02 <b>(-49.61%)</b></td><td>198.70 (-3.50%)</td><td>164.10 (+13.30%)</td><td>151.20 (+1.34%)</td><td>138.10 <b>(+43.26%)</b></td><td>29.05 <b>(-29.48%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>205.90 (n/a)</td><td>144.84 (n/a)</td><td>149.20 (n/a)</td><td>96.40 (n/a)</td><td>41.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (-2.23%)</td><td>0.09 (-17.69%)</td><td>0.09 (-13.97%)</td><td>0.05 <b>(-54.25%)</b></td><td>0.03 <b>(+177.99%)</b></td><td>341.20 <b>(+118.58%)</b></td><td>197.24 <b>(+36.14%)</b></td><td>178.80 (+16.25%)</td><td>130.50 (+2.27%)</td><td>86.09 <b>(+509.32%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>156.10 (n/a)</td><td>144.88 (n/a)</td><td>153.80 (n/a)</td><td>127.60 (n/a)</td><td>14.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (-14.32%)</td><td>0.11 (-8.04%)</td><td>0.11 (-9.00%)</td><td>0.09 (+4.91%)</td><td>0.01 <b>(-41.36%)</b></td><td>197.20 (-4.69%)</td><td>167.86 (+6.86%)</td><td>165.60 (+9.89%)</td><td>146.50 (+16.73%)</td><td>19.85 <b>(-36.00%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>157.08 (n/a)</td><td>150.70 (n/a)</td><td>125.50 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 <b>(-27.61%)</b></td><td>0.08 (-14.47%)</td><td>0.08 (-19.99%)</td><td>0.08 (+8.96%)</td><td>0.01 <b>(-74.13%)</b></td><td>216.80 (-8.21%)</td><td>202.52 (+12.91%)</td><td>208.20 <b>(+24.97%)</b></td><td>187.40 <b>(+38.20%)</b></td><td>12.82 <b>(-67.85%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.20 (n/a)</td><td>179.36 (n/a)</td><td>166.60 (n/a)</td><td>135.60 (n/a)</td><td>39.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (+1.93%)</td><td>0.09 (-0.24%)</td><td>0.10 (+5.24%)</td><td>0.08 (-11.95%)</td><td>0.01 <b>(+48.80%)</b></td><td>230.30 (+13.56%)</td><td>186.54 (+1.15%)</td><td>177.00 (-4.94%)</td><td>161.20 (-1.89%)</td><td>26.76 <b>(+68.76%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>184.42 (n/a)</td><td>186.20 (n/a)</td><td>164.30 (n/a)</td><td>15.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 <b>(-40.46%)</b></td><td>0.09 (-17.30%)</td><td>0.09 (-12.80%)</td><td>0.09 (+18.10%)</td><td>0.00 <b>(-87.99%)</b></td><td>187.50 (-15.35%)</td><td>179.52 (+12.58%)</td><td>180.30 (+14.69%)</td><td>166.90 <b>(+68.08%)</b></td><td>7.92 <b>(-82.84%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>221.50 (n/a)</td><td>159.46 (n/a)</td><td>157.20 (n/a)</td><td>99.30 (n/a)</td><td>46.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (+9.50%)</td><td>0.08 (-11.43%)</td><td>0.08 (-18.89%)</td><td>0.05 <b>(-30.55%)</b></td><td>0.03 <b>(+203.73%)</b></td><td>323.60 <b>(+44.01%)</b></td><td>232.92 <b>(+21.29%)</b></td><td>231.50 <b>(+23.27%)</b></td><td>162.10 (-8.68%)</td><td>72.03 <b>(+276.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>192.04 (n/a)</td><td>187.80 (n/a)</td><td>177.50 (n/a)</td><td>19.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 <b>(-23.05%)</b></td><td>0.07 (-11.57%)</td><td>0.07 (-6.86%)</td><td>0.06 (-12.52%)</td><td>0.01 <b>(-47.81%)</b></td><td>256.90 (+14.28%)</td><td>220.62 (+11.55%)</td><td>221.90 (+7.35%)</td><td>193.70 <b>(+29.91%)</b></td><td>24.29 <b>(-22.42%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.80 (n/a)</td><td>197.78 (n/a)</td><td>206.70 (n/a)</td><td>149.10 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (-15.74%)</td><td>0.21 (+0.76%)</td><td>0.21 (+7.60%)</td><td>0.14 (-15.12%)</td><td>0.04 (-14.70%)</td><td>234.90 (+17.86%)</td><td>164.62 (-0.56%)</td><td>153.30 (-7.03%)</td><td>132.60 (+18.71%)</td><td>41.88 <b>(+22.22%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>199.30 (n/a)</td><td>165.54 (n/a)</td><td>164.90 (n/a)</td><td>111.70 (n/a)</td><td>34.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (-7.10%)</td><td>0.19 (-16.86%)</td><td>0.17 (-17.90%)</td><td>0.13 <b>(-32.95%)</b></td><td>0.06 <b>(+35.19%)</b></td><td>261.00 <b>(+49.14%)</b></td><td>186.04 <b>(+26.92%)</b></td><td>190.10 <b>(+21.78%)</b></td><td>117.20 (+7.62%)</td><td>58.14 <b>(+115.71%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>175.00 (n/a)</td><td>146.58 (n/a)</td><td>156.10 (n/a)</td><td>108.90 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (+2.23%)</td><td>0.23 (+3.44%)</td><td>0.23 (-0.19%)</td><td>0.19 <b>(+21.12%)</b></td><td>0.04 (-10.38%)</td><td>215.50 (-17.43%)</td><td>185.10 (-4.34%)</td><td>181.60 (+0.22%)</td><td>152.50 (-2.18%)</td><td>29.49 <b>(-27.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>261.00 (n/a)</td><td>193.50 (n/a)</td><td>181.20 (n/a)</td><td>155.90 (n/a)</td><td>40.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (-4.61%)</td><td>0.22 (+4.37%)</td><td>0.22 (-3.50%)</td><td>0.17 (+11.64%)</td><td>0.04 <b>(-23.32%)</b></td><td>192.80 (-10.45%)</td><td>154.96 (-6.71%)</td><td>147.80 (+3.65%)</td><td>123.50 (+4.84%)</td><td>30.45 <b>(-31.85%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>215.30 (n/a)</td><td>166.10 (n/a)</td><td>142.60 (n/a)</td><td>117.80 (n/a)</td><td>44.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.31 (+13.53%)</td><td>0.21 (-4.91%)</td><td>0.19 (-14.45%)</td><td>0.14 <b>(-26.93%)</b></td><td>0.07 <b>(+84.22%)</b></td><td>303.10 <b>(+36.90%)</b></td><td>207.60 (+11.47%)</td><td>217.50 (+16.87%)</td><td>130.30 (-11.96%)</td><td>64.74 <b>(+119.61%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>221.40 (n/a)</td><td>186.24 (n/a)</td><td>186.10 (n/a)</td><td>148.00 (n/a)</td><td>29.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (-11.60%)</td><td>0.24 (-5.22%)</td><td>0.25 (-1.04%)</td><td>0.18 (-6.20%)</td><td>0.04 (-15.94%)</td><td>181.80 (+6.63%)</td><td>138.86 (+5.15%)</td><td>131.60 (+1.08%)</td><td>118.40 (+13.09%)</td><td>25.22 (+2.51%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>170.50 (n/a)</td><td>132.06 (n/a)</td><td>130.20 (n/a)</td><td>104.70 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (-0.66%)</td><td>0.21 (-2.52%)</td><td>0.19 (-17.47%)</td><td>0.16 (+18.51%)</td><td>0.04 (-10.03%)</td><td>225.70 (-15.63%)</td><td>181.76 (+0.78%)</td><td>192.00 <b>(+21.14%)</b></td><td>141.80 (+0.64%)</td><td>36.20 <b>(-28.70%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>267.50 (n/a)</td><td>180.36 (n/a)</td><td>158.50 (n/a)</td><td>140.90 (n/a)</td><td>50.76 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (+12.75%)</td><td>0.22 (+5.47%)</td><td>0.23 (+4.71%)</td><td>0.16 (+5.33%)</td><td>0.05 <b>(+29.83%)</b></td><td>199.50 (-5.05%)</td><td>155.04 (-3.98%)</td><td>139.50 (-4.52%)</td><td>119.80 (-11.32%)</td><td>35.88 (+12.34%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.10 (n/a)</td><td>161.46 (n/a)</td><td>146.10 (n/a)</td><td>135.10 (n/a)</td><td>31.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.23 (-14.76%)</td><td>0.20 (-11.86%)</td><td>0.20 (-4.37%)</td><td>0.16 (-14.80%)</td><td>0.03 (-13.15%)</td><td>233.20 (+17.42%)</td><td>187.40 (+13.59%)</td><td>180.90 (+4.57%)</td><td>157.40 (+17.38%)</td><td>30.89 <b>(+20.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>198.60 (n/a)</td><td>164.98 (n/a)</td><td>173.00 (n/a)</td><td>134.10 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (+3.41%)</td><td>0.22 (+16.44%)</td><td>0.23 <b>(+21.63%)</b></td><td>0.16 (+2.59%)</td><td>0.04 (+7.22%)</td><td>210.60 (-2.55%)</td><td>154.54 (-13.91%)</td><td>141.50 (-17.78%)</td><td>130.00 (-3.27%)</td><td>33.16 (+0.91%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.10 (n/a)</td><td>179.50 (n/a)</td><td>172.10 (n/a)</td><td>134.40 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (-11.07%)</td><td>0.17 (-8.71%)</td><td>0.17 (-6.46%)</td><td>0.11 <b>(-26.68%)</b></td><td>0.04 <b>(+22.69%)</b></td><td>305.50 <b>(+36.38%)</b></td><td>212.88 (+13.03%)</td><td>201.70 (+6.95%)</td><td>158.60 (+12.48%)</td><td>59.27 <b>(+90.60%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>224.00 (n/a)</td><td>188.34 (n/a)</td><td>188.60 (n/a)</td><td>141.00 (n/a)</td><td>31.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 <b>(-26.14%)</b></td><td>0.19 (+2.29%)</td><td>0.19 (+16.76%)</td><td>0.17 (+12.14%)</td><td>0.02 <b>(-69.36%)</b></td><td>195.10 (-10.83%)</td><td>169.90 (-6.98%)</td><td>169.30 (-14.37%)</td><td>151.40 <b>(+35.30%)</b></td><td>16.28 <b>(-60.52%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>218.80 (n/a)</td><td>182.64 (n/a)</td><td>197.70 (n/a)</td><td>111.90 (n/a)</td><td>41.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (+0.20%)</td><td>0.19 (+4.31%)</td><td>0.19 (-0.53%)</td><td>0.17 <b>(+37.08%)</b></td><td>0.02 <b>(-47.60%)</b></td><td>209.00 <b>(-27.05%)</b></td><td>186.00 (-7.06%)</td><td>185.40 (+0.54%)</td><td>162.10 (-0.18%)</td><td>17.76 <b>(-63.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>286.50 (n/a)</td><td>200.12 (n/a)</td><td>184.40 (n/a)</td><td>162.40 (n/a)</td><td>49.20 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 <b>(-24.18%)</b></td><td>0.15 (-15.75%)</td><td>0.15 <b>(-28.40%)</b></td><td>0.13 <b>(+58.03%)</b></td><td>0.02 <b>(-70.98%)</b></td><td>243.70 <b>(-36.72%)</b></td><td>214.36 (+3.87%)</td><td>218.70 <b>(+39.66%)</b></td><td>177.80 <b>(+31.90%)</b></td><td>23.79 <b>(-77.04%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>385.10 (n/a)</td><td>206.38 (n/a)</td><td>156.60 (n/a)</td><td>134.80 (n/a)</td><td>103.62 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (-7.78%)</td><td>0.14 (-0.76%)</td><td>0.12 (-14.66%)</td><td>0.12 (+15.69%)</td><td>0.02 <b>(-22.44%)</b></td><td>174.10 (-13.56%)</td><td>154.38 (-0.63%)</td><td>168.10 (+17.14%)</td><td>129.00 (+8.40%)</td><td>22.33 <b>(-28.81%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>201.40 (n/a)</td><td>155.36 (n/a)</td><td>143.50 (n/a)</td><td>119.00 (n/a)</td><td>31.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (-0.90%)</td><td>0.12 (-8.84%)</td><td>0.11 (-6.61%)</td><td>0.09 (+1.43%)</td><td>0.03 (-9.99%)</td><td>238.80 (-1.44%)</td><td>183.80 (+8.62%)</td><td>179.80 (+7.09%)</td><td>128.50 (+0.86%)</td><td>41.77 (-9.60%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>242.30 (n/a)</td><td>169.22 (n/a)</td><td>167.90 (n/a)</td><td>127.40 (n/a)</td><td>46.20 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (-2.62%)</td><td>0.12 (+3.00%)</td><td>0.13 (+14.58%)</td><td>0.09 (-11.77%)</td><td>0.02 (+19.46%)</td><td>224.10 (+13.30%)</td><td>172.12 (-1.56%)</td><td>156.20 (-12.74%)</td><td>136.40 (+2.71%)</td><td>37.21 <b>(+39.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>197.80 (n/a)</td><td>174.84 (n/a)</td><td>179.00 (n/a)</td><td>132.80 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (-17.72%)</td><td>0.13 (+12.71%)</td><td>0.13 <b>(+29.68%)</b></td><td>0.09 (-0.40%)</td><td>0.03 <b>(-30.81%)</b></td><td>237.10 (+0.38%)</td><td>163.68 (-14.09%)</td><td>160.60 <b>(-22.86%)</b></td><td>127.50 <b>(+21.54%)</b></td><td>44.74 (-12.00%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>236.20 (n/a)</td><td>190.52 (n/a)</td><td>208.20 (n/a)</td><td>104.90 (n/a)</td><td>50.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.17 (+5.99%)</td><td>0.12 (-8.20%)</td><td>0.11 (-12.10%)</td><td>0.09 (-5.94%)</td><td>0.03 <b>(+33.60%)</b></td><td>217.40 (+6.36%)</td><td>180.76 (+10.95%)</td><td>185.30 (+13.75%)</td><td>118.50 (-5.65%)</td><td>37.43 <b>(+28.23%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.40 (n/a)</td><td>162.92 (n/a)</td><td>162.90 (n/a)</td><td>125.60 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (-12.30%)</td><td>0.11 (-3.98%)</td><td>0.11 (-3.38%)</td><td>0.10 (+10.98%)</td><td>0.02 <b>(-43.65%)</b></td><td>205.70 (-9.90%)</td><td>181.28 (+1.13%)</td><td>180.80 (+3.49%)</td><td>148.10 (+14.10%)</td><td>23.93 <b>(-42.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>228.30 (n/a)</td><td>179.26 (n/a)</td><td>174.70 (n/a)</td><td>129.80 (n/a)</td><td>41.46 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (+13.59%)</td><td>0.12 (+10.45%)</td><td>0.12 (+3.90%)</td><td>0.10 (+7.93%)</td><td>0.02 <b>(+28.20%)</b></td><td>197.40 (-7.32%)</td><td>169.54 (-9.12%)</td><td>170.50 (-3.73%)</td><td>140.30 (-11.98%)</td><td>23.03 (+2.97%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>186.56 (n/a)</td><td>177.10 (n/a)</td><td>159.40 (n/a)</td><td>22.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 <b>(-28.50%)</b></td><td>0.10 (-16.62%)</td><td>0.10 (-13.89%)</td><td>0.09 (-6.93%)</td><td>0.01 <b>(-71.57%)</b></td><td>230.10 (+7.42%)</td><td>211.26 (+17.44%)</td><td>208.40 (+16.16%)</td><td>195.20 <b>(+39.93%)</b></td><td>12.90 <b>(-57.50%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>214.20 (n/a)</td><td>179.88 (n/a)</td><td>179.40 (n/a)</td><td>139.50 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (-9.37%)</td><td>0.15 (-2.92%)</td><td>0.14 (-4.61%)</td><td>0.13 <b>(+24.57%)</b></td><td>0.02 <b>(-42.86%)</b></td><td>186.30 (-19.73%)</td><td>171.02 (+0.21%)</td><td>179.60 (+4.78%)</td><td>140.00 (+10.32%)</td><td>19.38 <b>(-50.19%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>232.10 (n/a)</td><td>170.66 (n/a)</td><td>171.40 (n/a)</td><td>126.90 (n/a)</td><td>38.92 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (-16.25%)</td><td>0.12 (-11.70%)</td><td>0.13 (+7.89%)</td><td>0.06 <b>(-42.91%)</b></td><td>0.03 <b>(+44.22%)</b></td><td>386.30 <b>(+75.19%)</b></td><td>233.90 <b>(+21.46%)</b></td><td>186.10 (-7.32%)</td><td>172.80 (+19.42%)</td><td>90.08 <b>(+210.22%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.50 (n/a)</td><td>192.58 (n/a)</td><td>200.80 (n/a)</td><td>144.70 (n/a)</td><td>29.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (+18.08%)</td><td>0.16 (+16.74%)</td><td>0.15 (+18.70%)</td><td>0.14 (+18.43%)</td><td>0.02 (+12.90%)</td><td>175.40 (-15.55%)</td><td>157.42 (-14.43%)</td><td>161.40 (-15.76%)</td><td>131.70 (-15.31%)</td><td>16.92 (-19.53%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.70 (n/a)</td><td>183.96 (n/a)</td><td>191.60 (n/a)</td><td>155.50 (n/a)</td><td>21.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (-17.41%)</td><td>0.16 (+1.07%)</td><td>0.16 (+15.89%)</td><td>0.13 (+16.44%)</td><td>0.03 <b>(-52.29%)</b></td><td>187.60 (-14.10%)</td><td>153.04 (-7.01%)</td><td>155.70 (-13.74%)</td><td>128.60 <b>(+21.09%)</b></td><td>24.41 <b>(-50.71%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>218.40 (n/a)</td><td>164.58 (n/a)</td><td>180.50 (n/a)</td><td>106.20 (n/a)</td><td>49.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 <b>(+43.87%)</b></td><td>0.15 (+16.75%)</td><td>0.13 (+9.14%)</td><td>0.10 (-5.92%)</td><td>0.05 <b>(+171.12%)</b></td><td>241.20 (+6.30%)</td><td>181.32 (-9.52%)</td><td>188.90 (-8.39%)</td><td>112.70 <b>(-30.48%)</b></td><td>48.95 <b>(+98.63%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>226.90 (n/a)</td><td>200.40 (n/a)</td><td>206.20 (n/a)</td><td>162.10 (n/a)</td><td>24.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (+7.75%)</td><td>0.15 (-4.27%)</td><td>0.14 (-2.75%)</td><td>0.12 (-11.19%)</td><td>0.03 <b>(+53.55%)</b></td><td>209.80 (+12.61%)</td><td>171.04 (+6.41%)</td><td>172.90 (+2.79%)</td><td>128.70 (-7.14%)</td><td>32.83 <b>(+63.82%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>186.30 (n/a)</td><td>160.74 (n/a)</td><td>168.20 (n/a)</td><td>138.60 (n/a)</td><td>20.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (-4.03%)</td><td>0.12 (-12.67%)</td><td>0.12 <b>(-22.89%)</b></td><td>0.10 (-13.24%)</td><td>0.02 (-10.77%)</td><td>254.30 (+15.28%)</td><td>211.28 (+14.30%)</td><td>213.40 <b>(+29.73%)</b></td><td>163.70 (+4.27%)</td><td>32.42 (+2.83%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.60 (n/a)</td><td>184.84 (n/a)</td><td>164.50 (n/a)</td><td>157.00 (n/a)</td><td>31.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (-11.50%)</td><td>0.11 (-7.45%)</td><td>0.12 (+1.49%)</td><td>0.08 <b>(-20.73%)</b></td><td>0.02 (+0.63%)</td><td>290.70 <b>(+26.12%)</b></td><td>222.02 (+9.03%)</td><td>211.00 (-1.49%)</td><td>176.50 (+13.00%)</td><td>43.10 <b>(+50.04%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>230.50 (n/a)</td><td>203.64 (n/a)</td><td>214.20 (n/a)</td><td>156.20 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (+12.38%)</td><td>0.11 (+2.68%)</td><td>0.10 (-0.04%)</td><td>0.10 (+12.11%)</td><td>0.02 (+4.53%)</td><td>187.80 (-10.78%)</td><td>169.48 (-2.81%)</td><td>179.70 (+0.06%)</td><td>131.60 (-11.02%)</td><td>22.36 (-16.09%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>210.50 (n/a)</td><td>174.38 (n/a)</td><td>179.60 (n/a)</td><td>147.90 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (-2.20%)</td><td>0.10 (-13.95%)</td><td>0.10 (-11.20%)</td><td>0.06 <b>(-43.66%)</b></td><td>0.03 <b>(+72.49%)</b></td><td>326.30 <b>(+77.43%)</b></td><td>201.44 <b>(+24.36%)</b></td><td>183.90 (+12.61%)</td><td>134.20 (+2.29%)</td><td>72.87 <b>(+230.21%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>183.90 (n/a)</td><td>161.98 (n/a)</td><td>163.30 (n/a)</td><td>131.20 (n/a)</td><td>22.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (-2.55%)</td><td>0.11 (-5.32%)</td><td>0.10 (-11.96%)</td><td>0.10 (+1.25%)</td><td>0.01 (+5.55%)</td><td>187.60 (-1.21%)</td><td>171.86 (+5.77%)</td><td>182.50 (+13.64%)</td><td>146.00 (+2.60%)</td><td>18.39 (+6.38%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>162.48 (n/a)</td><td>160.60 (n/a)</td><td>142.30 (n/a)</td><td>17.28 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (-12.33%)</td><td>0.10 (+6.39%)</td><td>0.10 <b>(+20.96%)</b></td><td>0.09 <b>(+20.67%)</b></td><td>0.01 <b>(-50.59%)</b></td><td>196.40 (-17.13%)</td><td>178.24 (-10.08%)</td><td>183.10 (-17.34%)</td><td>142.40 (+14.01%)</td><td>21.85 <b>(-53.74%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>237.00 (n/a)</td><td>198.22 (n/a)</td><td>221.50 (n/a)</td><td>124.90 (n/a)</td><td>47.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (-5.75%)</td><td>0.10 (-9.02%)</td><td>0.10 (-11.36%)</td><td>0.09 (-11.12%)</td><td>0.01 (+7.77%)</td><td>197.80 (+12.51%)</td><td>179.02 (+10.10%)</td><td>180.60 (+12.80%)</td><td>157.30 (+6.14%)</td><td>15.82 <b>(+26.46%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>162.60 (n/a)</td><td>160.10 (n/a)</td><td>148.20 (n/a)</td><td>12.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 <b>(-23.92%)</b></td><td>0.10 (-11.18%)</td><td>0.10 (+0.87%)</td><td>0.08 (-3.33%)</td><td>0.01 <b>(-54.89%)</b></td><td>223.90 (+3.47%)</td><td>186.18 (+8.99%)</td><td>184.40 (-0.86%)</td><td>157.20 <b>(+31.44%)</b></td><td>24.42 <b>(-37.16%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>216.40 (n/a)</td><td>170.82 (n/a)</td><td>186.00 (n/a)</td><td>119.60 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (+15.22%)</td><td>0.10 (+0.31%)</td><td>0.09 (-12.03%)</td><td>0.08 (-7.89%)</td><td>0.02 <b>(+78.36%)</b></td><td>220.60 (+8.56%)</td><td>184.04 (+2.12%)</td><td>201.00 (+13.69%)</td><td>130.20 (-13.26%)</td><td>36.82 <b>(+63.79%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>180.22 (n/a)</td><td>176.80 (n/a)</td><td>150.10 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 <b>(+33.20%)</b></td><td>0.11 (+14.47%)</td><td>0.10 (+10.72%)</td><td>0.07 <b>(-20.00%)</b></td><td>0.03 <b>(+205.04%)</b></td><td>270.50 <b>(+25.00%)</b></td><td>186.36 (-7.24%)</td><td>187.60 (-9.68%)</td><td>126.00 <b>(-24.91%)</b></td><td>55.55 <b>(+191.47%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>200.90 (n/a)</td><td>207.70 (n/a)</td><td>167.80 (n/a)</td><td>19.06 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.76 (+5.14%)</td><td>0.60 (+5.74%)</td><td>0.61 (+15.79%)</td><td>0.38 (-16.21%)</td><td>0.16 <b>(+30.92%)</b></td><td>259.90 (+19.33%)</td><td>174.22 (-2.50%)</td><td>159.90 (-13.66%)</td><td>129.60 (-4.92%)</td><td>53.78 <b>(+46.51%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.72 (n/a)</td><td>0.57 (n/a)</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.12 (n/a)</td><td>217.80 (n/a)</td><td>178.68 (n/a)</td><td>185.20 (n/a)</td><td>136.30 (n/a)</td><td>36.71 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.78 (+5.27%)</td><td>0.65 (+1.42%)</td><td>0.67 (-1.00%)</td><td>0.40 <b>(-24.00%)</b></td><td>0.15 <b>(+50.51%)</b></td><td>244.80 <b>(+31.61%)</b></td><td>159.94 (+2.41%)</td><td>147.00 (+1.03%)</td><td>125.60 (-4.99%)</td><td>49.13 <b>(+89.29%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.74 (n/a)</td><td>0.64 (n/a)</td><td>0.68 (n/a)</td><td>0.53 (n/a)</td><td>0.10 (n/a)</td><td>186.00 (n/a)</td><td>156.18 (n/a)</td><td>145.50 (n/a)</td><td>132.20 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.79 (-1.37%)</td><td>0.56 (-2.87%)</td><td>0.52 (-1.12%)</td><td>0.43 (+0.57%)</td><td>0.14 (+2.21%)</td><td>228.30 (-0.57%)</td><td>185.42 (+3.30%)</td><td>188.80 (+1.12%)</td><td>124.10 (+1.39%)</td><td>40.83 (+5.17%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.80 (n/a)</td><td>0.57 (n/a)</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.14 (n/a)</td><td>229.60 (n/a)</td><td>179.50 (n/a)</td><td>186.70 (n/a)</td><td>122.40 (n/a)</td><td>38.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.70 (+8.79%)</td><td>0.54 (+6.05%)</td><td>0.48 (-1.14%)</td><td>0.45 (+1.73%)</td><td>0.11 <b>(+48.83%)</b></td><td>218.40 (-1.71%)</td><td>187.36 (-4.12%)</td><td>204.00 (+1.14%)</td><td>141.10 (-8.14%)</td><td>35.72 <b>(+41.38%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.64 (n/a)</td><td>0.51 (n/a)</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.08 (n/a)</td><td>222.20 (n/a)</td><td>195.42 (n/a)</td><td>201.70 (n/a)</td><td>153.60 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.58 (-7.69%)</td><td>0.51 (+3.89%)</td><td>0.50 (+4.86%)</td><td>0.46 (+19.13%)</td><td>0.04 <b>(-57.95%)</b></td><td>160.20 (-16.08%)</td><td>145.70 (-6.46%)</td><td>148.00 (-4.64%)</td><td>127.80 (+8.40%)</td><td>11.78 <b>(-62.77%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.63 (n/a)</td><td>0.49 (n/a)</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.10 (n/a)</td><td>190.90 (n/a)</td><td>155.76 (n/a)</td><td>155.20 (n/a)</td><td>117.90 (n/a)</td><td>31.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.58 (-15.91%)</td><td>0.45 (-2.10%)</td><td>0.40 (+6.24%)</td><td>0.34 (-3.40%)</td><td>0.10 <b>(-28.08%)</b></td><td>215.40 (+3.51%)</td><td>170.60 (-0.11%)</td><td>182.80 (-5.87%)</td><td>126.70 (+18.86%)</td><td>36.65 (-12.70%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.69 (n/a)</td><td>0.46 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.14 (n/a)</td><td>208.10 (n/a)</td><td>170.78 (n/a)</td><td>194.20 (n/a)</td><td>106.60 (n/a)</td><td>41.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.58 (+14.29%)</td><td>0.44 (+0.86%)</td><td>0.38 (-17.94%)</td><td>0.30 (+16.21%)</td><td>0.13 <b>(+32.94%)</b></td><td>246.70 (-13.92%)</td><td>182.24 (+0.31%)</td><td>193.30 <b>(+21.88%)</b></td><td>127.60 (-12.48%)</td><td>53.28 (-9.85%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.46 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>286.60 (n/a)</td><td>181.68 (n/a)</td><td>158.60 (n/a)</td><td>145.80 (n/a)</td><td>59.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.46 (-7.54%)</td><td>0.38 (-6.21%)</td><td>0.38 (+1.00%)</td><td>0.29 (-14.67%)</td><td>0.06 (-7.59%)</td><td>251.30 (+17.21%)</td><td>200.78 (+6.76%)</td><td>193.70 (-1.02%)</td><td>160.20 (+8.17%)</td><td>33.37 (+16.72%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>214.40 (n/a)</td><td>188.06 (n/a)</td><td>195.70 (n/a)</td><td>148.10 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (+3.78%)</td><td>0.23 (+3.32%)</td><td>0.23 (+5.10%)</td><td>0.19 <b>(+28.93%)</b></td><td>0.03 <b>(-23.17%)</b></td><td>194.40 <b>(-22.46%)</b></td><td>166.58 (-5.37%)</td><td>160.00 (-4.88%)</td><td>134.60 (-3.65%)</td><td>24.21 <b>(-44.28%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>250.70 (n/a)</td><td>176.04 (n/a)</td><td>168.20 (n/a)</td><td>139.70 (n/a)</td><td>43.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 <b>(+21.00%)</b></td><td>0.25 <b>(+22.44%)</b></td><td>0.26 <b>(+23.30%)</b></td><td>0.21 (+17.72%)</td><td>0.02 (+10.12%)</td><td>176.40 (-15.03%)</td><td>148.92 (-18.43%)</td><td>143.40 (-18.89%)</td><td>133.50 (-17.34%)</td><td>16.30 <b>(-21.24%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>207.60 (n/a)</td><td>182.56 (n/a)</td><td>176.80 (n/a)</td><td>161.50 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (-9.96%)</td><td>0.22 (-11.99%)</td><td>0.21 (-19.15%)</td><td>0.19 (-4.18%)</td><td>0.04 <b>(-21.66%)</b></td><td>195.40 (+4.32%)</td><td>170.12 (+12.51%)</td><td>178.60 <b>(+23.68%)</b></td><td>130.60 (+11.05%)</td><td>28.50 (-9.20%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>187.30 (n/a)</td><td>151.20 (n/a)</td><td>144.40 (n/a)</td><td>117.60 (n/a)</td><td>31.39 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (-0.84%)</td><td>0.19 (-5.41%)</td><td>0.18 (-6.33%)</td><td>0.16 (-11.58%)</td><td>0.02 <b>(+53.84%)</b></td><td>231.90 (+13.07%)</td><td>200.72 (+6.54%)</td><td>204.40 (+6.79%)</td><td>169.00 (+0.90%)</td><td>24.54 <b>(+75.55%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>205.10 (n/a)</td><td>188.40 (n/a)</td><td>191.40 (n/a)</td><td>167.50 (n/a)</td><td>13.98 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (-8.50%)</td><td>0.19 (-10.55%)</td><td>0.18 (-18.11%)</td><td>0.15 (+2.29%)</td><td>0.03 <b>(-20.44%)</b></td><td>242.10 (-2.26%)</td><td>199.16 (+10.41%)</td><td>206.40 <b>(+22.13%)</b></td><td>153.10 (+9.28%)</td><td>32.44 (-19.59%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>247.70 (n/a)</td><td>180.38 (n/a)</td><td>169.00 (n/a)</td><td>140.10 (n/a)</td><td>40.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (-7.58%)</td><td>0.23 (+5.23%)</td><td>0.22 (+8.96%)</td><td>0.17 <b>(+38.91%)</b></td><td>0.04 <b>(-38.78%)</b></td><td>213.60 <b>(-28.01%)</b></td><td>166.48 (-10.56%)</td><td>165.90 (-8.24%)</td><td>135.80 (+8.21%)</td><td>30.91 <b>(-53.69%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>296.70 (n/a)</td><td>186.14 (n/a)</td><td>180.80 (n/a)</td><td>125.50 (n/a)</td><td>66.76 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (+6.23%)</td><td>0.20 (+6.76%)</td><td>0.19 (-4.50%)</td><td>0.17 <b>(+38.51%)</b></td><td>0.03 <b>(-22.31%)</b></td><td>218.30 <b>(-27.81%)</b></td><td>185.78 (-9.10%)</td><td>190.20 (+4.74%)</td><td>149.20 (-5.87%)</td><td>28.82 <b>(-49.50%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>302.40 (n/a)</td><td>204.38 (n/a)</td><td>181.60 (n/a)</td><td>158.50 (n/a)</td><td>57.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 <b>(-25.93%)</b></td><td>0.19 (-8.99%)</td><td>0.20 (+7.66%)</td><td>0.17 (-2.52%)</td><td>0.02 <b>(-61.11%)</b></td><td>222.00 (+2.54%)</td><td>192.62 (+6.30%)</td><td>187.70 (-7.13%)</td><td>169.70 <b>(+35.00%)</b></td><td>20.67 <b>(-46.14%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>216.50 (n/a)</td><td>181.20 (n/a)</td><td>202.10 (n/a)</td><td>125.70 (n/a)</td><td>38.38 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.31 (+7.37%)</td><td>0.26 (-2.06%)</td><td>0.25 (-7.03%)</td><td>0.20 (-18.70%)</td><td>0.04 <b>(+131.37%)</b></td><td>206.90 <b>(+23.01%)</b></td><td>163.58 (+4.19%)</td><td>167.20 (+7.59%)</td><td>131.00 (-6.89%)</td><td>28.95 <b>(+165.50%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>168.20 (n/a)</td><td>157.00 (n/a)</td><td>155.40 (n/a)</td><td>140.70 (n/a)</td><td>10.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 (+13.68%)</td><td>0.25 (+11.97%)</td><td>0.25 (+12.57%)</td><td>0.22 (+9.32%)</td><td>0.03 <b>(+25.51%)</b></td><td>188.20 (-8.55%)</td><td>162.90 (-10.49%)</td><td>160.90 (-11.15%)</td><td>136.90 (-12.07%)</td><td>18.79 (+1.15%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>205.80 (n/a)</td><td>182.00 (n/a)</td><td>181.10 (n/a)</td><td>155.70 (n/a)</td><td>18.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (-14.42%)</td><td>0.23 (-8.10%)</td><td>0.24 (+5.37%)</td><td>0.20 (-0.28%)</td><td>0.03 <b>(-43.30%)</b></td><td>205.60 (+0.24%)</td><td>177.00 (+6.63%)</td><td>169.90 (-5.08%)</td><td>147.80 (+16.84%)</td><td>22.46 <b>(-31.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>205.10 (n/a)</td><td>166.00 (n/a)</td><td>179.00 (n/a)</td><td>126.50 (n/a)</td><td>32.98 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 <b>(-28.90%)</b></td><td>0.19 <b>(-27.76%)</b></td><td>0.21 <b>(-25.73%)</b></td><td>0.12 <b>(-35.64%)</b></td><td>0.05 <b>(-21.92%)</b></td><td>335.10 <b>(+55.35%)</b></td><td>226.28 <b>(+40.42%)</b></td><td>199.80 <b>(+34.64%)</b></td><td>167.90 <b>(+40.62%)</b></td><td>65.00 <b>(+75.28%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>215.70 (n/a)</td><td>161.14 (n/a)</td><td>148.40 (n/a)</td><td>119.40 (n/a)</td><td>37.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (-10.37%)</td><td>0.23 (-9.27%)</td><td>0.25 (-7.03%)</td><td>0.17 (-14.19%)</td><td>0.04 (+15.59%)</td><td>238.90 (+16.54%)</td><td>180.86 (+11.52%)</td><td>166.80 (+7.54%)</td><td>151.70 (+11.54%)</td><td>36.87 <b>(+43.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>205.00 (n/a)</td><td>162.18 (n/a)</td><td>155.10 (n/a)</td><td>136.00 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (-13.17%)</td><td>0.23 (-1.47%)</td><td>0.24 (+6.03%)</td><td>0.19 (+14.45%)</td><td>0.03 <b>(-46.58%)</b></td><td>218.30 (-12.65%)</td><td>178.22 (-2.12%)</td><td>169.80 (-5.67%)</td><td>151.40 (+15.22%)</td><td>25.81 <b>(-45.13%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>249.90 (n/a)</td><td>182.08 (n/a)</td><td>180.00 (n/a)</td><td>131.40 (n/a)</td><td>47.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 <b>(-28.30%)</b></td><td>0.21 (-10.10%)</td><td>0.24 (+15.34%)</td><td>0.15 <b>(-24.60%)</b></td><td>0.04 <b>(-37.31%)</b></td><td>278.60 <b>(+32.60%)</b></td><td>198.34 (+9.85%)</td><td>174.10 (-13.30%)</td><td>158.40 <b>(+39.44%)</b></td><td>48.18 <b>(+21.05%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>210.10 (n/a)</td><td>180.56 (n/a)</td><td>200.80 (n/a)</td><td>113.60 (n/a)</td><td>39.80 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 <b>(+36.12%)</b></td><td>0.24 (+16.33%)</td><td>0.21 (+2.62%)</td><td>0.19 (+4.73%)</td><td>0.05 <b>(+229.64%)</b></td><td>214.80 (-4.49%)</td><td>179.40 (-11.28%)</td><td>196.20 (-2.53%)</td><td>135.50 <b>(-26.52%)</b></td><td>36.54 <b>(+129.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>224.90 (n/a)</td><td>202.20 (n/a)</td><td>201.30 (n/a)</td><td>184.40 (n/a)</td><td>15.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (-13.82%)</td><td>0.21 (+2.21%)</td><td>0.20 (+3.39%)</td><td>0.18 <b>(+23.28%)</b></td><td>0.03 <b>(-52.55%)</b></td><td>190.70 (-18.85%)</td><td>168.84 (-5.79%)</td><td>170.10 (-3.24%)</td><td>139.50 (+16.06%)</td><td>18.89 <b>(-55.06%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>235.00 (n/a)</td><td>179.22 (n/a)</td><td>175.80 (n/a)</td><td>120.20 (n/a)</td><td>42.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (+0.37%)</td><td>0.21 (+5.14%)</td><td>0.20 (-2.02%)</td><td>0.19 <b>(+30.16%)</b></td><td>0.03 <b>(-38.92%)</b></td><td>182.50 <b>(-23.16%)</b></td><td>168.82 (-7.32%)</td><td>175.30 (+2.04%)</td><td>137.70 (-0.36%)</td><td>17.78 <b>(-54.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>237.50 (n/a)</td><td>182.16 (n/a)</td><td>171.80 (n/a)</td><td>138.20 (n/a)</td><td>39.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (+9.25%)</td><td>0.22 (+4.62%)</td><td>0.20 (-7.52%)</td><td>0.20 <b>(+32.99%)</b></td><td>0.03 (-18.80%)</td><td>177.60 <b>(-24.81%)</b></td><td>159.64 (-6.35%)</td><td>170.60 (+8.11%)</td><td>124.70 (-8.51%)</td><td>21.34 <b>(-46.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>236.20 (n/a)</td><td>170.46 (n/a)</td><td>157.80 (n/a)</td><td>136.30 (n/a)</td><td>39.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (-0.79%)</td><td>0.21 (-4.46%)</td><td>0.20 (-6.88%)</td><td>0.19 (+3.77%)</td><td>0.03 <b>(-21.88%)</b></td><td>186.60 (-3.67%)</td><td>166.56 (+3.47%)</td><td>170.30 (+7.38%)</td><td>130.20 (+0.77%)</td><td>21.52 <b>(-26.82%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>193.70 (n/a)</td><td>160.98 (n/a)</td><td>158.60 (n/a)</td><td>129.20 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 <b>(-24.83%)</b></td><td>0.19 (-17.83%)</td><td>0.19 (-13.91%)</td><td>0.17 (-17.40%)</td><td>0.02 <b>(-48.85%)</b></td><td>208.80 <b>(+21.04%)</b></td><td>186.58 <b>(+20.83%)</b></td><td>184.10 (+16.15%)</td><td>167.00 <b>(+33.07%)</b></td><td>15.33 (-16.49%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>172.50 (n/a)</td><td>154.42 (n/a)</td><td>158.50 (n/a)</td><td>125.50 (n/a)</td><td>18.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (+13.68%)</td><td>0.16 (-11.98%)</td><td>0.15 (-17.23%)</td><td>0.10 <b>(-38.88%)</b></td><td>0.05 <b>(+152.54%)</b></td><td>351.50 <b>(+63.56%)</b></td><td>232.06 <b>(+22.07%)</b></td><td>226.20 <b>(+20.77%)</b></td><td>145.50 (-12.03%)</td><td>75.99 <b>(+263.76%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>214.90 (n/a)</td><td>190.10 (n/a)</td><td>187.30 (n/a)</td><td>165.40 (n/a)</td><td>20.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (-7.83%)</td><td>0.18 (-4.98%)</td><td>0.16 (-5.70%)</td><td>0.14 (-11.10%)</td><td>0.03 (-8.14%)</td><td>256.10 (+12.47%)</td><td>201.42 (+5.19%)</td><td>212.30 (+6.04%)</td><td>162.30 (+8.49%)</td><td>39.46 (+7.68%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>227.70 (n/a)</td><td>191.48 (n/a)</td><td>200.20 (n/a)</td><td>149.60 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (+2.06%)</td><td>0.17 (-1.52%)</td><td>0.16 (-2.67%)</td><td>0.15 (+12.30%)</td><td>0.03 (-11.18%)</td><td>237.50 (-10.95%)</td><td>211.32 (+0.74%)</td><td>218.60 (+2.73%)</td><td>164.60 (-2.02%)</td><td>27.44 <b>(-25.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>266.70 (n/a)</td><td>209.76 (n/a)</td><td>212.80 (n/a)</td><td>168.00 (n/a)</td><td>36.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.03 (+14.33%)</td><td>0.83 (+2.39%)</td><td>0.84 (+5.96%)</td><td>0.57 <b>(-20.89%)</b></td><td>0.17 <b>(+101.94%)</b></td><td>231.70 <b>(+26.40%)</b></td><td>163.48 (+0.84%)</td><td>155.60 (-5.58%)</td><td>126.80 (-12.55%)</td><td>40.19 <b>(+138.20%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.90 (n/a)</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.09 (n/a)</td><td>183.30 (n/a)</td><td>162.12 (n/a)</td><td>164.80 (n/a)</td><td>145.00 (n/a)</td><td>16.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.00 <b>(+31.32%)</b></td><td>0.88 <b>(+24.49%)</b></td><td>0.95 <b>(+30.65%)</b></td><td>0.70 (+13.57%)</td><td>0.13 <b>(+137.09%)</b></td><td>186.40 (-11.95%)</td><td>151.90 (-18.52%)</td><td>138.00 <b>(-23.46%)</b></td><td>131.20 <b>(-23.85%)</b></td><td>24.50 <b>(+56.63%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.76 (n/a)</td><td>0.71 (n/a)</td><td>0.73 (n/a)</td><td>0.62 (n/a)</td><td>0.06 (n/a)</td><td>211.70 (n/a)</td><td>186.42 (n/a)</td><td>180.30 (n/a)</td><td>172.30 (n/a)</td><td>15.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.03 (-12.84%)</td><td>0.87 (+4.67%)</td><td>0.99 <b>(+28.32%)</b></td><td>0.50 (-18.69%)</td><td>0.22 (+3.41%)</td><td>261.30 <b>(+22.96%)</b></td><td>161.80 (-1.93%)</td><td>132.70 <b>(-22.08%)</b></td><td>127.90 (+14.71%)</td><td>56.94 <b>(+51.13%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.18 (n/a)</td><td>0.83 (n/a)</td><td>0.77 (n/a)</td><td>0.62 (n/a)</td><td>0.21 (n/a)</td><td>212.50 (n/a)</td><td>164.98 (n/a)</td><td>170.30 (n/a)</td><td>111.50 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-0.09%)</td><td>0.03 (+15.33%)</td><td>0.03 <b>(+27.98%)</b></td><td>0.02 (+7.95%)</td><td>0.01 (+0.03%)</td><td>194.90 (-7.37%)</td><td>152.10 (-13.47%)</td><td>144.00 <b>(-21.87%)</b></td><td>122.90 (+0.16%)</td><td>31.62 (-6.66%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>175.78 (n/a)</td><td>184.30 (n/a)</td><td>122.70 (n/a)</td><td>33.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+11.34%)</td><td>0.03 <b>(+30.73%)</b></td><td>0.03 <b>(+36.96%)</b></td><td>0.02 <b>(+32.96%)</b></td><td>0.00 <b>(-30.43%)</b></td><td>167.90 <b>(-24.78%)</b></td><td>141.98 <b>(-24.87%)</b></td><td>137.90 <b>(-26.96%)</b></td><td>128.90 (-10.17%)</td><td>15.65 <b>(-53.52%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.20 (n/a)</td><td>188.98 (n/a)</td><td>188.80 (n/a)</td><td>143.50 (n/a)</td><td>33.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-15.64%)</td><td>0.02 (-19.81%)</td><td>0.02 <b>(-26.63%)</b></td><td>0.02 (-16.37%)</td><td>0.00 (+11.04%)</td><td>206.70 (+19.55%)</td><td>182.44 <b>(+25.99%)</b></td><td>200.90 <b>(+36.30%)</b></td><td>145.30 (+18.52%)</td><td>30.25 <b>(+58.97%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.90 (n/a)</td><td>144.80 (n/a)</td><td>147.40 (n/a)</td><td>122.60 (n/a)</td><td>19.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>17.32 (-4.44%)</td><td>15.34 (+12.79%)</td><td>15.51 <b>(+22.30%)</b></td><td>12.59 <b>(+22.03%)</b></td><td>1.89 <b>(-40.13%)</b></td><td>166.60 (-18.05%)</td><td>138.56 (-13.77%)</td><td>135.30 (-18.20%)</td><td>121.20 (+4.66%)</td><td>18.14 <b>(-48.32%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>18.12 (n/a)</td><td>13.60 (n/a)</td><td>12.68 (n/a)</td><td>10.32 (n/a)</td><td>3.15 (n/a)</td><td>203.30 (n/a)</td><td>160.68 (n/a)</td><td>165.40 (n/a)</td><td>115.80 (n/a)</td><td>35.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.03 (+17.46%)</td><td>0.84 (+8.75%)</td><td>0.87 <b>(+20.17%)</b></td><td>0.59 (-17.78%)</td><td>0.19 <b>(+162.25%)</b></td><td>225.10 <b>(+21.61%)</b></td><td>164.88 (-4.44%)</td><td>151.90 (-16.77%)</td><td>128.70 (-14.82%)</td><td>40.71 <b>(+164.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.87 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.71 (n/a)</td><td>0.07 (n/a)</td><td>185.10 (n/a)</td><td>172.54 (n/a)</td><td>182.50 (n/a)</td><td>151.10 (n/a)</td><td>15.38 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.14 (+4.36%)</td><td>0.87 (-7.01%)</td><td>0.78 (-11.32%)</td><td>0.73 (-5.38%)</td><td>0.16 (+18.14%)</td><td>179.80 (+5.70%)</td><td>156.12 (+8.34%)</td><td>168.30 (+12.73%)</td><td>116.40 (-4.12%)</td><td>25.74 <b>(+21.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.09 (n/a)</td><td>0.93 (n/a)</td><td>0.88 (n/a)</td><td>0.78 (n/a)</td><td>0.14 (n/a)</td><td>170.10 (n/a)</td><td>144.10 (n/a)</td><td>149.30 (n/a)</td><td>121.40 (n/a)</td><td>21.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.17 <b>(+32.73%)</b></td><td>0.84 (+6.32%)</td><td>0.78 (-0.34%)</td><td>0.50 <b>(-21.77%)</b></td><td>0.26 <b>(+179.94%)</b></td><td>263.50 <b>(+27.79%)</b></td><td>171.72 (+0.96%)</td><td>169.00 (+0.36%)</td><td>113.20 <b>(-24.68%)</b></td><td>57.99 <b>(+166.99%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.88 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.64 (n/a)</td><td>0.09 (n/a)</td><td>206.20 (n/a)</td><td>170.08 (n/a)</td><td>168.40 (n/a)</td><td>150.30 (n/a)</td><td>21.72 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.33 <b>(+49.07%)</b></td><td>0.94 (+16.86%)</td><td>0.90 (+14.48%)</td><td>0.67 (-10.24%)</td><td>0.24 <b>(+329.94%)</b></td><td>197.90 (+11.43%)</td><td>148.14 (-10.55%)</td><td>146.60 (-12.63%)</td><td>99.40 <b>(-32.97%)</b></td><td>34.89 <b>(+216.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.89 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.74 (n/a)</td><td>0.06 (n/a)</td><td>177.60 (n/a)</td><td>165.62 (n/a)</td><td>167.80 (n/a)</td><td>148.30 (n/a)</td><td>11.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.05 (+0.65%)</td><td>0.86 (+5.25%)</td><td>0.83 (+7.41%)</td><td>0.65 (-5.96%)</td><td>0.17 <b>(+27.36%)</b></td><td>204.10 (+6.30%)</td><td>159.02 (-3.68%)</td><td>159.70 (-6.93%)</td><td>125.90 (-0.63%)</td><td>32.66 <b>(+34.73%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.04 (n/a)</td><td>0.82 (n/a)</td><td>0.77 (n/a)</td><td>0.69 (n/a)</td><td>0.14 (n/a)</td><td>192.00 (n/a)</td><td>165.10 (n/a)</td><td>171.60 (n/a)</td><td>126.70 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (-3.72%)</td><td>0.03 (+0.21%)</td><td>0.02 (-1.99%)</td><td>0.02 (+4.24%)</td><td>0.00 (-14.33%)</td><td>202.90 (-4.07%)</td><td>163.36 (-1.07%)</td><td>168.30 (+2.06%)</td><td>127.40 (+3.83%)</td><td>28.14 (-14.63%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>165.12 (n/a)</td><td>164.90 (n/a)</td><td>122.70 (n/a)</td><td>32.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (+4.02%)</td><td>0.03 (-1.75%)</td><td>0.02 (-9.52%)</td><td>0.02 (+5.18%)</td><td>0.00 (+7.93%)</td><td>176.30 (-4.91%)</td><td>158.48 (+1.93%)</td><td>172.10 (+10.53%)</td><td>122.80 (-3.84%)</td><td>22.98 (-0.45%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.40 (n/a)</td><td>155.48 (n/a)</td><td>155.70 (n/a)</td><td>127.70 (n/a)</td><td>23.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.00 (+2.33%)</td><td>0.00 (+1.91%)</td><td>0.00 (+0.00%)</td><td>0.00 (+7.69%)</td><td>0.00 <b>(-45.57%)</b></td><td>980.33 (-6.77%)</td><td>964.90 (-1.46%)</td><td>967.87 (-0.08%)</td><td>935.82 (-0.86%)</td><td>18.18 <b>(-56.43%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1051.48 (n/a)</td><td>979.21 (n/a)</td><td>968.60 (n/a)</td><td>943.91 (n/a)</td><td>41.72 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.01 (+6.10%)</td><td>0.01 (+2.99%)</td><td>0.01 (+2.47%)</td><td>0.01 (+0.00%)</td><td>0.00 <b>(+180.87%)</b></td><td>1036.90 (-0.58%)</td><td>990.89 (-2.72%)</td><td>984.67 (-2.58%)</td><td>944.11 (-5.32%)</td><td>42.48 <b>(+110.84%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1042.95 (n/a)</td><td>1018.56 (n/a)</td><td>1010.70 (n/a)</td><td>997.17 (n/a)</td><td>20.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.97 (-2.65%)</td><td>0.96 (-0.94%)</td><td>0.96 (-0.53%)</td><td>0.95 (+0.52%)</td><td>0.01 <b>(-62.92%)</b></td><td>2210.09 (-0.52%)</td><td>2190.48 (+0.92%)</td><td>2187.88 (+0.53%)</td><td>2166.87 (+2.71%)</td><td>16.66 <b>(-62.07%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.99 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.02 (n/a)</td><td>2221.66 (n/a)</td><td>2170.51 (n/a)</td><td>2176.41 (n/a)</td><td>2109.60 (n/a)</td><td>43.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.89 (-0.52%)</td><td>0.88 (+0.17%)</td><td>0.88 (+0.25%)</td><td>0.87 (+0.22%)</td><td>0.01 (-8.77%)</td><td>2415.15 (-0.22%)</td><td>2373.31 (-0.17%)</td><td>2376.74 (-0.24%)</td><td>2345.31 (+0.53%)</td><td>28.83 (-8.76%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>2420.45 (n/a)</td><td>2377.26 (n/a)</td><td>2382.57 (n/a)</td><td>2332.96 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.68 <b>(-88.61%)</b></td><td>0.66 <b>(-87.26%)</b></td><td>0.67 <b>(-87.62%)</b></td><td>0.64 <b>(-85.53%)</b></td><td>0.02 <b>(-97.76%)</b></td><td>1636.20 <b>(+591.25%)</b></td><td>1579.36 <b>(+673.51%)</b></td><td>1572.80 <b>(+707.81%)</b></td><td>1537.80 <b>(+777.74%)</b></td><td>37.68 <b>(+34.64%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.99 (n/a)</td><td>5.21 (n/a)</td><td>5.39 (n/a)</td><td>4.43 (n/a)</td><td>0.70 (n/a)</td><td>236.70 (n/a)</td><td>204.18 (n/a)</td><td>194.70 (n/a)</td><td>175.20 (n/a)</td><td>27.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.19 <b>(-78.24%)</b></td><td>1.12 <b>(-77.42%)</b></td><td>1.13 <b>(-77.77%)</b></td><td>0.99 <b>(-75.66%)</b></td><td>0.08 <b>(-85.30%)</b></td><td>1057.80 <b>(+310.96%)</b></td><td>936.66 <b>(+340.08%)</b></td><td>928.10 <b>(+349.88%)</b></td><td>883.90 <b>(+359.65%)</b></td><td>71.32 <b>(+174.18%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.45 (n/a)</td><td>4.98 (n/a)</td><td>5.08 (n/a)</td><td>4.07 (n/a)</td><td>0.54 (n/a)</td><td>257.40 (n/a)</td><td>212.84 (n/a)</td><td>206.30 (n/a)</td><td>192.30 (n/a)</td><td>26.01 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.21 <b>(-79.06%)</b></td><td>1.15 <b>(-75.44%)</b></td><td>1.15 <b>(-75.45%)</b></td><td>1.10 <b>(-69.79%)</b></td><td>0.04 <b>(-95.45%)</b></td><td>957.50 <b>(+230.97%)</b></td><td>915.64 <b>(+292.98%)</b></td><td>913.00 <b>(+307.23%)</b></td><td>864.70 <b>(+377.47%)</b></td><td>35.31 <b>(-29.00%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.79 (n/a)</td><td>4.67 (n/a)</td><td>4.68 (n/a)</td><td>3.62 (n/a)</td><td>0.98 (n/a)</td><td>289.30 (n/a)</td><td>233.00 (n/a)</td><td>224.20 (n/a)</td><td>181.10 (n/a)</td><td>49.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.01 <b>(-60.53%)</b></td><td>1.84 <b>(-60.32%)</b></td><td>1.82 <b>(-62.24%)</b></td><td>1.76 <b>(-52.19%)</b></td><td>0.10 <b>(-82.62%)</b></td><td>595.30 <b>(+109.17%)</b></td><td>570.30 <b>(+149.17%)</b></td><td>576.80 <b>(+164.83%)</b></td><td>521.60 <b>(+153.33%)</b></td><td>28.31 (-11.11%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>5.09 (n/a)</td><td>4.64 (n/a)</td><td>4.82 (n/a)</td><td>3.68 (n/a)</td><td>0.56 (n/a)</td><td>284.60 (n/a)</td><td>228.88 (n/a)</td><td>217.80 (n/a)</td><td>205.90 (n/a)</td><td>31.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.67 <b>(-92.73%)</b></td><td>0.66 <b>(-91.84%)</b></td><td>0.65 <b>(-91.50%)</b></td><td>0.64 <b>(-91.12%)</b></td><td>0.01 <b>(-98.40%)</b></td><td>3270.60 <b>(+1026.24%)</b></td><td>3188.80 <b>(+1116.26%)</b></td><td>3202.80 <b>(+1077.07%)</b></td><td>3111.40 <b>(+1275.51%)</b></td><td>62.73 <b>(+149.71%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.27 (n/a)</td><td>8.06 (n/a)</td><td>7.71 (n/a)</td><td>7.22 (n/a)</td><td>0.81 (n/a)</td><td>290.40 (n/a)</td><td>262.18 (n/a)</td><td>272.10 (n/a)</td><td>226.20 (n/a)</td><td>25.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.32 <b>(-84.18%)</b></td><td>1.25 <b>(-83.13%)</b></td><td>1.26 <b>(-83.45%)</b></td><td>1.18 <b>(-82.05%)</b></td><td>0.05 <b>(-92.21%)</b></td><td>1784.70 <b>(+457.02%)</b></td><td>1675.92 <b>(+489.70%)</b></td><td>1670.70 <b>(+504.23%)</b></td><td>1584.30 <b>(+531.95%)</b></td><td>71.76 <b>(+174.50%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>8.37 (n/a)</td><td>7.43 (n/a)</td><td>7.58 (n/a)</td><td>6.55 (n/a)</td><td>0.68 (n/a)</td><td>320.40 (n/a)</td><td>284.20 (n/a)</td><td>276.50 (n/a)</td><td>250.70 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.35 <b>(-85.04%)</b></td><td>1.22 <b>(-84.54%)</b></td><td>1.28 <b>(-83.72%)</b></td><td>0.94 <b>(-86.14%)</b></td><td>0.16 <b>(-81.14%)</b></td><td>2233.10 <b>(+621.29%)</b></td><td>1750.00 <b>(+551.53%)</b></td><td>1639.00 <b>(+514.32%)</b></td><td>1558.90 <b>(+568.77%)</b></td><td>277.37 <b>(+826.05%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.00 (n/a)</td><td>7.89 (n/a)</td><td>7.86 (n/a)</td><td>6.77 (n/a)</td><td>0.87 (n/a)</td><td>309.60 (n/a)</td><td>268.60 (n/a)</td><td>266.80 (n/a)</td><td>233.10 (n/a)</td><td>29.95 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.41 <b>(-74.98%)</b></td><td>2.32 <b>(-73.20%)</b></td><td>2.33 <b>(-72.72%)</b></td><td>2.23 <b>(-68.71%)</b></td><td>0.08 <b>(-92.50%)</b></td><td>939.70 <b>(+219.63%)</b></td><td>906.20 <b>(+269.12%)</b></td><td>901.40 <b>(+266.57%)</b></td><td>871.50 <b>(+299.59%)</b></td><td>29.91 (-3.04%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.62 (n/a)</td><td>8.64 (n/a)</td><td>8.53 (n/a)</td><td>7.13 (n/a)</td><td>1.02 (n/a)</td><td>294.00 (n/a)</td><td>245.50 (n/a)</td><td>245.90 (n/a)</td><td>218.10 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.28 <b>(-76.64%)</b></td><td>2.13 <b>(-75.81%)</b></td><td>2.23 <b>(-73.68%)</b></td><td>1.81 <b>(-78.19%)</b></td><td>0.20 <b>(-67.33%)</b></td><td>1160.00 <b>(+358.50%)</b></td><td>990.08 <b>(+315.02%)</b></td><td>939.30 <b>(+279.98%)</b></td><td>921.40 <b>(+328.16%)</b></td><td>101.38 <b>(+540.60%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.75 (n/a)</td><td>8.82 (n/a)</td><td>8.48 (n/a)</td><td>8.29 (n/a)</td><td>0.61 (n/a)</td><td>253.00 (n/a)</td><td>238.56 (n/a)</td><td>247.20 (n/a)</td><td>215.20 (n/a)</td><td>15.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>3.78 <b>(-58.30%)</b></td><td>3.51 <b>(-58.47%)</b></td><td>3.55 <b>(-58.01%)</b></td><td>3.32 <b>(-57.97%)</b></td><td>0.19 <b>(-58.41%)</b></td><td>631.70 <b>(+137.93%)</b></td><td>598.20 <b>(+140.80%)</b></td><td>591.30 <b>(+138.14%)</b></td><td>555.30 <b>(+139.87%)</b></td><td>32.04 <b>(+138.97%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.06 (n/a)</td><td>8.46 (n/a)</td><td>8.45 (n/a)</td><td>7.90 (n/a)</td><td>0.46 (n/a)</td><td>265.50 (n/a)</td><td>248.42 (n/a)</td><td>248.30 (n/a)</td><td>231.50 (n/a)</td><td>13.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.71 <b>(-93.90%)</b></td><td>0.68 <b>(-93.97%)</b></td><td>0.68 <b>(-94.03%)</b></td><td>0.65 <b>(-93.95%)</b></td><td>0.02 <b>(-94.27%)</b></td><td>6491.30 <b>(+1552.57%)</b></td><td>6185.76 <b>(+1558.11%)</b></td><td>6134.90 <b>(+1576.20%)</b></td><td>5884.90 <b>(+1540.62%)</b></td><td>225.39 <b>(+1452.44%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>11.69 (n/a)</td><td>11.26 (n/a)</td><td>11.46 (n/a)</td><td>10.68 (n/a)</td><td>0.43 (n/a)</td><td>392.80 (n/a)</td><td>373.06 (n/a)</td><td>366.00 (n/a)</td><td>358.70 (n/a)</td><td>14.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.37 <b>(-90.17%)</b></td><td>1.25 <b>(-89.64%)</b></td><td>1.28 <b>(-89.61%)</b></td><td>1.11 <b>(-89.10%)</b></td><td>0.13 <b>(-90.73%)</b></td><td>3762.40 <b>(+817.66%)</b></td><td>3387.36 <b>(+862.87%)</b></td><td>3289.40 <b>(+862.38%)</b></td><td>3052.20 <b>(+917.74%)</b></td><td>350.17 <b>(+770.44%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>13.99 (n/a)</td><td>12.05 (n/a)</td><td>12.27 (n/a)</td><td>10.23 (n/a)</td><td>1.37 (n/a)</td><td>410.00 (n/a)</td><td>351.80 (n/a)</td><td>341.80 (n/a)</td><td>299.90 (n/a)</td><td>40.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.38 <b>(-89.04%)</b></td><td>1.28 <b>(-89.48%)</b></td><td>1.27 <b>(-89.71%)</b></td><td>1.14 <b>(-90.01%)</b></td><td>0.09 <b>(-83.82%)</b></td><td>3682.90 <b>(+901.33%)</b></td><td>3298.70 <b>(+852.56%)</b></td><td>3291.10 <b>(+871.40%)</b></td><td>3032.10 <b>(+812.73%)</b></td><td>239.65 <b>(+1399.03%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>12.63 (n/a)</td><td>12.13 (n/a)</td><td>12.38 (n/a)</td><td>11.40 (n/a)</td><td>0.55 (n/a)</td><td>367.80 (n/a)</td><td>346.30 (n/a)</td><td>338.80 (n/a)</td><td>332.20 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.57 <b>(-82.84%)</b></td><td>2.48 <b>(-81.54%)</b></td><td>2.45 <b>(-81.17%)</b></td><td>2.36 <b>(-80.75%)</b></td><td>0.09 <b>(-91.82%)</b></td><td>1774.50 <b>(+419.47%)</b></td><td>1695.98 <b>(+439.67%)</b></td><td>1710.60 <b>(+430.91%)</b></td><td>1634.10 <b>(+482.77%)</b></td><td>58.82 <b>(+147.31%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.96 (n/a)</td><td>13.41 (n/a)</td><td>13.02 (n/a)</td><td>12.28 (n/a)</td><td>1.05 (n/a)</td><td>341.60 (n/a)</td><td>314.26 (n/a)</td><td>322.20 (n/a)</td><td>280.40 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.63 <b>(-83.55%)</b></td><td>2.47 <b>(-81.43%)</b></td><td>2.44 <b>(-80.05%)</b></td><td>2.36 <b>(-79.91%)</b></td><td>0.11 <b>(-93.80%)</b></td><td>1773.70 <b>(+397.81%)</b></td><td>1698.30 <b>(+431.75%)</b></td><td>1716.30 <b>(+401.26%)</b></td><td>1591.90 <b>(+507.83%)</b></td><td>76.06 <b>(+87.10%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>16.01 (n/a)</td><td>13.32 (n/a)</td><td>12.25 (n/a)</td><td>11.77 (n/a)</td><td>1.82 (n/a)</td><td>356.30 (n/a)</td><td>319.38 (n/a)</td><td>342.40 (n/a)</td><td>261.90 (n/a)</td><td>40.65 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.83 <b>(-66.16%)</b></td><td>4.61 <b>(-65.57%)</b></td><td>4.57 <b>(-67.46%)</b></td><td>4.49 <b>(-61.07%)</b></td><td>0.14 <b>(-88.46%)</b></td><td>933.50 <b>(+156.88%)</b></td><td>909.50 <b>(+188.69%)</b></td><td>917.10 <b>(+207.34%)</b></td><td>868.80 <b>(+195.51%)</b></td><td>26.30 (-11.91%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.27 (n/a)</td><td>13.40 (n/a)</td><td>14.06 (n/a)</td><td>11.54 (n/a)</td><td>1.18 (n/a)</td><td>363.40 (n/a)</td><td>315.04 (n/a)</td><td>298.40 (n/a)</td><td>294.00 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.54 <b>(-68.52%)</b></td><td>4.25 <b>(-67.78%)</b></td><td>4.36 <b>(-68.39%)</b></td><td>3.88 <b>(-64.48%)</b></td><td>0.31 <b>(-77.12%)</b></td><td>1081.70 <b>(+181.55%)</b></td><td>992.00 <b>(+208.71%)</b></td><td>960.90 <b>(+216.40%)</b></td><td>924.10 <b>(+217.56%)</b></td><td>75.04 <b>(+101.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.42 (n/a)</td><td>13.18 (n/a)</td><td>13.81 (n/a)</td><td>10.92 (n/a)</td><td>1.37 (n/a)</td><td>384.20 (n/a)</td><td>321.34 (n/a)</td><td>303.70 (n/a)</td><td>291.00 (n/a)</td><td>37.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>7.21 <b>(-51.01%)</b></td><td>6.80 <b>(-45.90%)</b></td><td>6.93 <b>(-44.61%)</b></td><td>5.93 <b>(-32.20%)</b></td><td>0.52 <b>(-78.37%)</b></td><td>707.50 <b>(+47.49%)</b></td><td>619.92 <b>(+79.29%)</b></td><td>605.20 <b>(+80.50%)</b></td><td>581.50 <b>(+104.11%)</b></td><td>51.63 <b>(-34.92%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>14.72 (n/a)</td><td>12.57 (n/a)</td><td>12.51 (n/a)</td><td>8.74 (n/a)</td><td>2.42 (n/a)</td><td>479.70 (n/a)</td><td>345.76 (n/a)</td><td>335.30 (n/a)</td><td>284.90 (n/a)</td><td>79.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.62 <b>(-79.76%)</b></td><td>0.58 <b>(-77.30%)</b></td><td>0.58 <b>(-77.34%)</b></td><td>0.55 <b>(-70.89%)</b></td><td>0.03 <b>(-93.80%)</b></td><td>953.00 <b>(+243.55%)</b></td><td>901.62 <b>(+329.75%)</b></td><td>899.70 <b>(+341.25%)</b></td><td>845.40 <b>(+394.10%)</b></td><td>41.66 (+2.41%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.06 (n/a)</td><td>2.57 (n/a)</td><td>2.57 (n/a)</td><td>1.89 (n/a)</td><td>0.44 (n/a)</td><td>277.40 (n/a)</td><td>209.80 (n/a)</td><td>203.90 (n/a)</td><td>171.10 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.68 <b>(-89.12%)</b></td><td>0.63 <b>(-87.40%)</b></td><td>0.64 <b>(-86.33%)</b></td><td>0.59 <b>(-85.90%)</b></td><td>0.03 <b>(-96.24%)</b></td><td>1769.20 <b>(+609.10%)</b></td><td>1662.94 <b>(+677.87%)</b></td><td>1649.00 <b>(+631.59%)</b></td><td>1552.60 <b>(+818.70%)</b></td><td>84.44 <b>(+146.07%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>6.21 (n/a)</td><td>5.01 (n/a)</td><td>4.65 (n/a)</td><td>4.20 (n/a)</td><td>0.86 (n/a)</td><td>249.50 (n/a)</td><td>213.78 (n/a)</td><td>225.40 (n/a)</td><td>169.00 (n/a)</td><td>34.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.68 <b>(-92.54%)</b></td><td>0.64 <b>(-91.72%)</b></td><td>0.66 <b>(-91.41%)</b></td><td>0.57 <b>(-91.48%)</b></td><td>0.04 <b>(-95.80%)</b></td><td>3692.80 <b>(+1074.18%)</b></td><td>3281.00 <b>(+1095.00%)</b></td><td>3164.00 <b>(+1064.09%)</b></td><td>3102.20 <b>(+1240.04%)</b></td><td>246.09 <b>(+553.13%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>9.06 (n/a)</td><td>7.75 (n/a)</td><td>7.71 (n/a)</td><td>6.67 (n/a)</td><td>1.07 (n/a)</td><td>314.50 (n/a)</td><td>274.56 (n/a)</td><td>271.80 (n/a)</td><td>231.50 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.06 <b>(-68.97%)</b></td><td>1.03 <b>(-66.09%)</b></td><td>1.05 <b>(-66.07%)</b></td><td>0.98 <b>(-62.99%)</b></td><td>0.03 <b>(-89.00%)</b></td><td>533.50 <b>(+170.13%)</b></td><td>508.80 <b>(+192.92%)</b></td><td>500.40 <b>(+194.70%)</b></td><td>494.40 <b>(+222.29%)</b></td><td>16.07 (-4.76%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>3.42 (n/a)</td><td>3.04 (n/a)</td><td>3.09 (n/a)</td><td>2.65 (n/a)</td><td>0.29 (n/a)</td><td>197.50 (n/a)</td><td>173.70 (n/a)</td><td>169.80 (n/a)</td><td>153.40 (n/a)</td><td>16.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 <b>(-30.66%)</b></td><td>0.16 (-16.73%)</td><td>0.16 (-14.52%)</td><td>0.14 (-0.72%)</td><td>0.01 <b>(-69.04%)</b></td><td>227.30 (+0.71%)</td><td>201.36 (+16.20%)</td><td>199.90 (+16.97%)</td><td>180.00 <b>(+44.23%)</b></td><td>17.02 <b>(-54.47%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.70 (n/a)</td><td>173.28 (n/a)</td><td>170.90 (n/a)</td><td>124.80 (n/a)</td><td>37.39 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 <b>(-28.89%)</b></td><td>0.17 (-19.49%)</td><td>0.17 (-12.94%)</td><td>0.13 <b>(-28.44%)</b></td><td>0.02 <b>(-32.64%)</b></td><td>243.20 <b>(+39.77%)</b></td><td>200.60 <b>(+24.03%)</b></td><td>198.50 (+14.87%)</td><td>178.20 <b>(+40.65%)</b></td><td>26.63 <b>(+32.18%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>174.00 (n/a)</td><td>161.74 (n/a)</td><td>172.80 (n/a)</td><td>126.70 (n/a)</td><td>20.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 <b>(-39.38%)</b></td><td>0.25 <b>(-35.83%)</b></td><td>0.25 <b>(-34.42%)</b></td><td>0.19 <b>(-38.65%)</b></td><td>0.05 <b>(-32.03%)</b></td><td>353.40 <b>(+63.01%)</b></td><td>266.50 <b>(+56.71%)</b></td><td>260.60 <b>(+52.49%)</b></td><td>218.00 <b>(+65.03%)</b></td><td>55.42 <b>(+78.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>216.80 (n/a)</td><td>170.06 (n/a)</td><td>170.90 (n/a)</td><td>132.10 (n/a)</td><td>31.00 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.39 <b>(-25.34%)</b></td><td>0.31 <b>(-22.75%)</b></td><td>0.30 (-16.24%)</td><td>0.27 (-16.37%)</td><td>0.05 <b>(-44.51%)</b></td><td>244.40 (+19.57%)</td><td>215.42 <b>(+27.42%)</b></td><td>219.90 (+19.38%)</td><td>169.80 <b>(+34.02%)</b></td><td>27.78 (-12.95%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>204.40 (n/a)</td><td>169.06 (n/a)</td><td>184.20 (n/a)</td><td>126.70 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.41 <b>(-20.67%)</b></td><td>0.33 (-11.59%)</td><td>0.34 (-8.12%)</td><td>0.27 (+7.32%)</td><td>0.06 <b>(-38.86%)</b></td><td>239.00 (-6.82%)</td><td>202.12 (+10.08%)</td><td>190.50 (+8.86%)</td><td>159.00 <b>(+26.09%)</b></td><td>34.86 <b>(-26.00%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.52 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.09 (n/a)</td><td>256.50 (n/a)</td><td>183.62 (n/a)</td><td>175.00 (n/a)</td><td>126.10 (n/a)</td><td>47.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.40 <b>(-58.71%)</b></td><td>0.35 <b>(-56.03%)</b></td><td>0.35 <b>(-55.83%)</b></td><td>0.30 <b>(-56.09%)</b></td><td>0.04 <b>(-62.17%)</b></td><td>436.20 <b>(+127.78%)</b></td><td>376.64 <b>(+126.89%)</b></td><td>378.70 <b>(+126.36%)</b></td><td>328.50 <b>(+142.26%)</b></td><td>42.25 <b>(+112.35%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.97 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.68 (n/a)</td><td>0.10 (n/a)</td><td>191.50 (n/a)</td><td>166.00 (n/a)</td><td>167.30 (n/a)</td><td>135.60 (n/a)</td><td>19.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.61 <b>(-42.06%)</b></td><td>0.54 <b>(-35.40%)</b></td><td>0.56 <b>(-36.37%)</b></td><td>0.43 <b>(-36.27%)</b></td><td>0.07 <b>(-55.74%)</b></td><td>306.80 <b>(+56.93%)</b></td><td>246.22 <b>(+52.74%)</b></td><td>234.40 <b>(+57.21%)</b></td><td>216.40 <b>(+72.57%)</b></td><td>35.86 (+18.20%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>1.05 (n/a)</td><td>0.84 (n/a)</td><td>0.88 (n/a)</td><td>0.67 (n/a)</td><td>0.16 (n/a)</td><td>195.50 (n/a)</td><td>161.20 (n/a)</td><td>149.10 (n/a)</td><td>125.40 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.69 <b>(-24.11%)</b></td><td>0.60 <b>(-23.71%)</b></td><td>0.63 (-18.77%)</td><td>0.51 <b>(-26.64%)</b></td><td>0.07 (-15.67%)</td><td>255.50 <b>(+36.27%)</b></td><td>219.20 <b>(+31.40%)</b></td><td>206.60 <b>(+23.12%)</b></td><td>190.40 <b>(+31.76%)</b></td><td>26.47 <b>(+52.62%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.91 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.70 (n/a)</td><td>0.08 (n/a)</td><td>187.50 (n/a)</td><td>166.82 (n/a)</td><td>167.80 (n/a)</td><td>144.50 (n/a)</td><td>17.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.82 (-8.08%)</td><td>0.62 (-13.08%)</td><td>0.57 <b>(-20.81%)</b></td><td>0.42 <b>(-28.89%)</b></td><td>0.16 <b>(+26.26%)</b></td><td>312.50 <b>(+40.64%)</b></td><td>223.74 (+18.67%)</td><td>231.00 <b>(+26.30%)</b></td><td>160.70 (+8.80%)</td><td>60.03 <b>(+83.69%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.89 (n/a)</td><td>0.71 (n/a)</td><td>0.72 (n/a)</td><td>0.59 (n/a)</td><td>0.13 (n/a)</td><td>222.20 (n/a)</td><td>188.54 (n/a)</td><td>182.90 (n/a)</td><td>147.70 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 <b>(-21.22%)</b></td><td>0.10 (-7.90%)</td><td>0.09 (-16.59%)</td><td>0.09 <b>(+57.77%)</b></td><td>0.01 <b>(-67.88%)</b></td><td>188.50 <b>(-36.62%)</b></td><td>173.10 (-0.55%)</td><td>180.50 (+19.85%)</td><td>150.70 <b>(+26.96%)</b></td><td>16.78 <b>(-76.16%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:18:09</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>297.40 (n/a)</td><td>174.06 (n/a)</td><td>150.60 (n/a)</td><td>118.70 (n/a)</td><td>70.41 (n/a)</td>
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
