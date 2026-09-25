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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-13.60%)</td><td>0.04 (-2.14%)</td><td>0.04 (+0.52%)</td><td>0.03 (-1.46%)</td><td>0.01 <b>(-35.80%)</b></td><td>185.00 (+1.48%)</td><td>153.56 (+0.48%)</td><td>157.10 (-0.51%)</td><td>131.00 (+15.83%)</td><td>21.64 <b>(-26.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>152.82 (n/a)</td><td>157.90 (n/a)</td><td>113.10 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (+3.05%)</td><td>0.05 (+5.26%)</td><td>0.04 (+4.17%)</td><td>0.04 (+5.85%)</td><td>0.00 <b>(-23.78%)</b></td><td>154.30 (-5.57%)</td><td>135.06 (-5.68%)</td><td>136.80 (-4.00%)</td><td>117.80 (-2.97%)</td><td>13.44 <b>(-30.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>163.40 (n/a)</td><td>143.20 (n/a)</td><td>142.50 (n/a)</td><td>121.40 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (+0.22%)</td><td>0.04 (-18.88%)</td><td>0.03 <b>(-29.32%)</b></td><td>0.03 <b>(-25.13%)</b></td><td>0.01 <b>(+109.41%)</b></td><td>211.20 <b>(+33.50%)</b></td><td>173.30 <b>(+26.76%)</b></td><td>185.30 <b>(+41.45%)</b></td><td>128.00 (-0.16%)</td><td>34.18 <b>(+174.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>158.20 (n/a)</td><td>136.72 (n/a)</td><td>131.00 (n/a)</td><td>128.20 (n/a)</td><td>12.47 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (+1.88%)</td><td>0.04 (+0.80%)</td><td>0.04 (-1.23%)</td><td>0.04 (+16.46%)</td><td>0.01 (-15.69%)</td><td>165.30 (-14.13%)</td><td>149.80 (-1.56%)</td><td>151.70 (+1.27%)</td><td>123.30 (-1.91%)</td><td>17.30 <b>(-30.13%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>152.18 (n/a)</td><td>149.80 (n/a)</td><td>125.70 (n/a)</td><td>24.77 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-9.66%)</td><td>0.04 (-8.17%)</td><td>0.03 (-11.11%)</td><td>0.03 (-11.87%)</td><td>0.01 (-4.27%)</td><td>210.80 (+13.52%)</td><td>171.12 (+9.31%)</td><td>179.90 (+12.51%)</td><td>131.00 (+10.74%)</td><td>31.59 (+19.73%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.70 (n/a)</td><td>156.54 (n/a)</td><td>159.90 (n/a)</td><td>118.30 (n/a)</td><td>26.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-4.76%)</td><td>0.04 (-15.01%)</td><td>0.03 <b>(-27.58%)</b></td><td>0.03 (-17.92%)</td><td>0.01 <b>(+52.69%)</b></td><td>216.20 <b>(+21.80%)</b></td><td>180.12 <b>(+21.82%)</b></td><td>208.70 <b>(+38.12%)</b></td><td>131.20 (+4.96%)</td><td>43.39 <b>(+98.01%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>147.86 (n/a)</td><td>151.10 (n/a)</td><td>125.00 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 <b>(+21.26%)</b></td><td>0.04 (+13.03%)</td><td>0.04 (+8.00%)</td><td>0.03 (-0.47%)</td><td>0.01 <b>(+90.44%)</b></td><td>236.30 (+0.47%)</td><td>176.40 (-9.02%)</td><td>172.60 (-7.45%)</td><td>133.60 (-17.48%)</td><td>41.63 <b>(+53.97%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.20 (n/a)</td><td>193.88 (n/a)</td><td>186.50 (n/a)</td><td>161.90 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (+0.84%)</td><td>0.03 (+2.20%)</td><td>0.04 (+1.76%)</td><td>0.03 (-4.54%)</td><td>0.00 (+19.50%)</td><td>222.00 (+4.77%)</td><td>183.16 (-1.79%)</td><td>174.40 (-1.75%)</td><td>166.40 (-0.83%)</td><td>22.70 <b>(+25.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>211.90 (n/a)</td><td>186.50 (n/a)</td><td>177.50 (n/a)</td><td>167.80 (n/a)</td><td>18.15 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (+4.82%)</td><td>0.07 (+9.53%)</td><td>0.07 (+8.05%)</td><td>0.05 <b>(+55.72%)</b></td><td>0.02 (-17.18%)</td><td>227.90 <b>(-35.78%)</b></td><td>178.80 (-13.98%)</td><td>169.00 (-7.45%)</td><td>128.10 (-4.62%)</td><td>41.20 <b>(-51.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>354.90 (n/a)</td><td>207.86 (n/a)</td><td>182.60 (n/a)</td><td>134.30 (n/a)</td><td>85.36 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (-1.24%)</td><td>0.08 (+4.78%)</td><td>0.08 (+12.04%)</td><td>0.07 (+0.29%)</td><td>0.01 (-12.72%)</td><td>183.80 (-0.27%)</td><td>152.52 (-4.94%)</td><td>145.20 (-10.76%)</td><td>133.10 (+1.29%)</td><td>20.34 (-12.30%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.30 (n/a)</td><td>160.44 (n/a)</td><td>162.70 (n/a)</td><td>131.40 (n/a)</td><td>23.19 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (-7.30%)</td><td>0.06 (-13.43%)</td><td>0.07 (-9.81%)</td><td>0.05 (-17.98%)</td><td>0.01 <b>(+43.22%)</b></td><td>236.70 <b>(+21.95%)</b></td><td>197.24 (+17.42%)</td><td>185.10 (+10.90%)</td><td>157.90 (+7.93%)</td><td>35.32 <b>(+93.80%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>167.98 (n/a)</td><td>166.90 (n/a)</td><td>146.30 (n/a)</td><td>18.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (-5.63%)</td><td>0.08 (-7.17%)</td><td>0.07 (-7.10%)</td><td>0.06 (-16.00%)</td><td>0.02 (+13.86%)</td><td>214.90 (+19.06%)</td><td>166.62 (+9.23%)</td><td>167.70 (+7.64%)</td><td>126.30 (+5.96%)</td><td>35.85 <b>(+41.67%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>152.54 (n/a)</td><td>155.80 (n/a)</td><td>119.20 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (-19.13%)</td><td>0.07 (-19.72%)</td><td>0.06 <b>(-26.75%)</b></td><td>0.05 (-7.01%)</td><td>0.02 <b>(-20.44%)</b></td><td>233.80 (+7.49%)</td><td>184.12 <b>(+23.32%)</b></td><td>197.00 <b>(+36.52%)</b></td><td>139.40 <b>(+23.58%)</b></td><td>41.55 (+0.28%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>217.50 (n/a)</td><td>149.30 (n/a)</td><td>144.30 (n/a)</td><td>112.80 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (+3.40%)</td><td>0.07 (+6.95%)</td><td>0.07 (+17.97%)</td><td>0.06 (+1.13%)</td><td>0.02 (-4.14%)</td><td>216.30 (-1.14%)</td><td>176.76 (-7.10%)</td><td>183.00 (-15.24%)</td><td>128.30 (-3.32%)</td><td>34.30 (-11.84%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>218.80 (n/a)</td><td>190.26 (n/a)</td><td>215.90 (n/a)</td><td>132.70 (n/a)</td><td>38.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (+8.65%)</td><td>0.07 (+9.67%)</td><td>0.07 (+9.72%)</td><td>0.04 (-6.98%)</td><td>0.02 <b>(+39.64%)</b></td><td>277.30 (+7.52%)</td><td>179.60 (-6.03%)</td><td>164.30 (-8.82%)</td><td>136.10 (-7.98%)</td><td>56.83 <b>(+38.90%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>257.90 (n/a)</td><td>191.12 (n/a)</td><td>180.20 (n/a)</td><td>147.90 (n/a)</td><td>40.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (+0.82%)</td><td>0.06 (-9.92%)</td><td>0.06 <b>(-22.09%)</b></td><td>0.04 (+3.72%)</td><td>0.01 (-8.02%)</td><td>279.00 (-3.59%)</td><td>209.82 (+9.82%)</td><td>206.70 <b>(+28.31%)</b></td><td>157.30 (-0.82%)</td><td>48.95 (-13.04%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>289.40 (n/a)</td><td>191.06 (n/a)</td><td>161.10 (n/a)</td><td>158.60 (n/a)</td><td>56.29 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (-0.72%)</td><td>0.15 (-3.70%)</td><td>0.15 (-3.15%)</td><td>0.12 (-17.47%)</td><td>0.03 <b>(+61.90%)</b></td><td>209.60 <b>(+21.16%)</b></td><td>164.42 (+6.15%)</td><td>160.80 (+3.28%)</td><td>130.10 (+0.70%)</td><td>33.35 <b>(+96.44%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>173.00 (n/a)</td><td>154.90 (n/a)</td><td>155.70 (n/a)</td><td>129.20 (n/a)</td><td>16.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (-0.17%)</td><td>0.15 (-11.71%)</td><td>0.15 (-7.69%)</td><td>0.09 <b>(-33.72%)</b></td><td>0.04 <b>(+68.83%)</b></td><td>269.50 <b>(+50.81%)</b></td><td>178.92 (+19.36%)</td><td>168.20 (+8.31%)</td><td>123.20 (+0.16%)</td><td>56.02 <b>(+162.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>178.70 (n/a)</td><td>149.90 (n/a)</td><td>155.30 (n/a)</td><td>123.00 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (+1.90%)</td><td>0.16 (+6.96%)</td><td>0.15 (+8.67%)</td><td>0.11 (-0.37%)</td><td>0.03 (+2.63%)</td><td>214.60 (+0.37%)</td><td>162.90 (-6.49%)</td><td>166.00 (-7.98%)</td><td>130.20 (-1.88%)</td><td>34.64 (-1.26%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>213.80 (n/a)</td><td>174.20 (n/a)</td><td>180.40 (n/a)</td><td>132.70 (n/a)</td><td>35.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (-15.73%)</td><td>0.15 (-7.26%)</td><td>0.15 (-14.14%)</td><td>0.13 (+7.97%)</td><td>0.02 <b>(-49.34%)</b></td><td>183.70 (-7.41%)</td><td>165.54 (+5.53%)</td><td>169.40 (+16.51%)</td><td>142.50 (+18.65%)</td><td>16.77 <b>(-44.95%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>198.40 (n/a)</td><td>156.86 (n/a)</td><td>145.40 (n/a)</td><td>120.10 (n/a)</td><td>30.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (-16.41%)</td><td>0.14 (-14.72%)</td><td>0.14 <b>(-21.01%)</b></td><td>0.11 (-6.58%)</td><td>0.02 <b>(-37.34%)</b></td><td>217.10 (+7.00%)</td><td>174.82 (+14.95%)</td><td>172.80 <b>(+26.59%)</b></td><td>146.00 (+19.57%)</td><td>28.75 (-19.19%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>202.90 (n/a)</td><td>152.08 (n/a)</td><td>136.50 (n/a)</td><td>122.10 (n/a)</td><td>35.58 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (-18.95%)</td><td>0.13 (-9.81%)</td><td>0.13 (+1.36%)</td><td>0.11 (+12.34%)</td><td>0.02 <b>(-59.01%)</b></td><td>229.50 (-11.01%)</td><td>190.40 (+4.20%)</td><td>191.50 (-1.39%)</td><td>156.50 <b>(+23.33%)</b></td><td>27.09 <b>(-51.66%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>257.90 (n/a)</td><td>182.72 (n/a)</td><td>194.20 (n/a)</td><td>126.90 (n/a)</td><td>56.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 (+0.06%)</td><td>0.15 (+2.06%)</td><td>0.14 (-9.39%)</td><td>0.13 (+9.49%)</td><td>0.02 (-8.28%)</td><td>195.10 (-8.66%)</td><td>167.42 (-2.65%)</td><td>180.60 (+10.32%)</td><td>133.10 (-0.08%)</td><td>26.01 (-17.47%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.60 (n/a)</td><td>171.98 (n/a)</td><td>163.70 (n/a)</td><td>133.20 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 <b>(-21.50%)</b></td><td>0.14 (-10.28%)</td><td>0.14 (-6.04%)</td><td>0.11 (-10.94%)</td><td>0.02 <b>(-45.65%)</b></td><td>233.10 (+12.28%)</td><td>181.06 (+8.97%)</td><td>170.70 (+6.42%)</td><td>163.30 <b>(+27.38%)</b></td><td>29.26 <b>(-21.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>207.60 (n/a)</td><td>166.16 (n/a)</td><td>160.40 (n/a)</td><td>128.20 (n/a)</td><td>37.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.34 (-13.08%)</td><td>0.27 (-9.92%)</td><td>0.28 (-4.88%)</td><td>0.20 (-3.72%)</td><td>0.05 <b>(-33.06%)</b></td><td>244.90 (+3.86%)</td><td>185.66 (+8.36%)</td><td>173.60 (+5.15%)</td><td>145.40 (+15.03%)</td><td>38.18 (-16.75%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>235.80 (n/a)</td><td>171.34 (n/a)</td><td>165.10 (n/a)</td><td>126.40 (n/a)</td><td>45.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.38 (-1.42%)</td><td>0.31 (-5.12%)</td><td>0.32 (-2.67%)</td><td>0.25 (-6.85%)</td><td>0.05 <b>(+24.09%)</b></td><td>193.30 (+7.33%)</td><td>160.48 (+6.48%)</td><td>155.20 (+2.78%)</td><td>130.30 (+1.40%)</td><td>28.42 <b>(+37.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>180.10 (n/a)</td><td>150.72 (n/a)</td><td>151.00 (n/a)</td><td>128.50 (n/a)</td><td>20.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.37 (-3.97%)</td><td>0.31 (-0.59%)</td><td>0.30 (+3.70%)</td><td>0.26 (-2.24%)</td><td>0.05 (-12.11%)</td><td>186.00 (+2.31%)</td><td>158.68 (+0.23%)</td><td>165.30 (-3.56%)</td><td>131.90 (+4.10%)</td><td>22.44 (-7.44%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>181.80 (n/a)</td><td>158.32 (n/a)</td><td>171.40 (n/a)</td><td>126.70 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.37 (-3.80%)</td><td>0.31 (-2.30%)</td><td>0.29 (-12.77%)</td><td>0.23 (-1.92%)</td><td>0.06 (-14.84%)</td><td>211.90 (+1.97%)</td><td>164.78 (+1.39%)</td><td>170.30 (+14.68%)</td><td>133.20 (+3.90%)</td><td>31.61 (-12.01%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>207.80 (n/a)</td><td>162.52 (n/a)</td><td>148.50 (n/a)</td><td>128.20 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.32 (-16.28%)</td><td>0.28 (-13.85%)</td><td>0.28 (-17.83%)</td><td>0.23 (+11.30%)</td><td>0.03 <b>(-54.02%)</b></td><td>210.00 (-10.14%)</td><td>177.06 (+12.03%)</td><td>173.00 <b>(+21.66%)</b></td><td>153.50 (+19.46%)</td><td>20.59 <b>(-52.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>233.70 (n/a)</td><td>158.04 (n/a)</td><td>142.20 (n/a)</td><td>128.50 (n/a)</td><td>42.94 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.38 (+0.52%)</td><td>0.30 (-6.13%)</td><td>0.28 (-9.45%)</td><td>0.25 (-8.82%)</td><td>0.05 <b>(+31.37%)</b></td><td>200.40 (+9.69%)</td><td>168.20 (+7.60%)</td><td>173.50 (+10.44%)</td><td>130.80 (-0.46%)</td><td>26.55 <b>(+41.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>182.70 (n/a)</td><td>156.32 (n/a)</td><td>157.10 (n/a)</td><td>131.40 (n/a)</td><td>18.72 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.40 (+8.23%)</td><td>0.29 (+5.16%)</td><td>0.30 (+13.04%)</td><td>0.18 (-16.77%)</td><td>0.08 <b>(+31.59%)</b></td><td>271.20 <b>(+20.16%)</b></td><td>178.56 (-1.81%)</td><td>163.90 (-11.50%)</td><td>124.00 (-7.60%)</td><td>55.55 <b>(+53.28%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>225.70 (n/a)</td><td>181.86 (n/a)</td><td>185.20 (n/a)</td><td>134.20 (n/a)</td><td>36.24 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.30 (-0.16%)</td><td>0.25 (-9.43%)</td><td>0.26 (-1.00%)</td><td>0.18 <b>(-30.15%)</b></td><td>0.05 <b>(+182.55%)</b></td><td>271.00 <b>(+43.16%)</b></td><td>205.46 (+13.68%)</td><td>188.00 (+0.97%)</td><td>163.90 (+0.12%)</td><td>43.06 <b>(+310.82%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.02 (n/a)</td><td>189.30 (n/a)</td><td>180.74 (n/a)</td><td>186.20 (n/a)</td><td>163.70 (n/a)</td><td>10.48 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 <b>(-34.25%)</b></td><td>0.01 <b>(-21.45%)</b></td><td>0.01 (-13.83%)</td><td>0.01 (-14.45%)</td><td>0.00 <b>(-53.60%)</b></td><td>248.40 (+16.89%)</td><td>195.34 <b>(+23.21%)</b></td><td>187.70 (+16.08%)</td><td>158.60 <b>(+52.06%)</b></td><td>34.13 (-14.42%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>212.50 (n/a)</td><td>158.54 (n/a)</td><td>161.70 (n/a)</td><td>104.30 (n/a)</td><td>39.88 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 <b>(+20.12%)</b></td><td>0.02 (-7.56%)</td><td>0.01 (-14.43%)</td><td>0.01 <b>(-24.05%)</b></td><td>0.01 <b>(+90.03%)</b></td><td>277.90 <b>(+31.71%)</b></td><td>192.86 (+16.25%)</td><td>190.40 (+16.81%)</td><td>104.30 (-16.76%)</td><td>61.97 <b>(+97.04%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>165.90 (n/a)</td><td>163.00 (n/a)</td><td>125.30 (n/a)</td><td>31.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (+0.85%)</td><td>0.01 (-13.37%)</td><td>0.01 (-14.35%)</td><td>0.01 (-14.08%)</td><td>0.00 <b>(+25.85%)</b></td><td>227.60 (+16.36%)</td><td>189.50 (+17.80%)</td><td>192.70 (+16.72%)</td><td>121.70 (-0.90%)</td><td>40.76 <b>(+39.89%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>195.60 (n/a)</td><td>160.86 (n/a)</td><td>165.10 (n/a)</td><td>122.80 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (-15.80%)</td><td>0.01 (-19.64%)</td><td>0.01 (-18.42%)</td><td>0.01 <b>(-42.21%)</b></td><td>0.00 <b>(+27.56%)</b></td><td>386.50 <b>(+73.01%)</b></td><td>223.88 <b>(+33.52%)</b></td><td>196.00 <b>(+22.58%)</b></td><td>156.50 (+18.74%)</td><td>93.33 <b>(+169.76%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>167.68 (n/a)</td><td>159.90 (n/a)</td><td>131.80 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (-16.24%)</td><td>0.01 (-5.16%)</td><td>0.01 (-2.09%)</td><td>0.01 (+15.11%)</td><td>0.00 <b>(-36.51%)</b></td><td>259.90 (-13.14%)</td><td>193.92 (+1.43%)</td><td>177.10 (+2.13%)</td><td>165.50 (+19.41%)</td><td>38.78 <b>(-37.68%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>299.20 (n/a)</td><td>191.18 (n/a)</td><td>173.40 (n/a)</td><td>138.60 (n/a)</td><td>62.23 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.01 <b>(-29.99%)</b></td><td>0.01 (-19.20%)</td><td>0.01 (-1.66%)</td><td>0.01 (-13.78%)</td><td>0.00 <b>(-62.82%)</b></td><td>235.30 (+15.97%)</td><td>202.90 <b>(+20.14%)</b></td><td>191.60 (+1.70%)</td><td>184.10 <b>(+42.82%)</b></td><td>22.22 <b>(-37.34%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>202.90 (n/a)</td><td>168.88 (n/a)</td><td>188.40 (n/a)</td><td>128.90 (n/a)</td><td>35.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (+2.95%)</td><td>0.01 (-4.30%)</td><td>0.01 (-12.23%)</td><td>0.01 <b>(+26.28%)</b></td><td>0.00 <b>(-26.61%)</b></td><td>202.30 <b>(-20.79%)</b></td><td>179.80 (+1.11%)</td><td>188.60 (+13.96%)</td><td>131.00 (-2.89%)</td><td>28.19 <b>(-43.85%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>255.40 (n/a)</td><td>177.82 (n/a)</td><td>165.50 (n/a)</td><td>134.90 (n/a)</td><td>50.20 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (+6.16%)</td><td>0.01 (+1.20%)</td><td>0.01 (-0.16%)</td><td>0.01 <b>(+27.20%)</b></td><td>0.00 (-10.21%)</td><td>278.90 <b>(-21.39%)</b></td><td>229.00 (-3.43%)</td><td>221.20 (+0.14%)</td><td>167.80 (-5.78%)</td><td>42.42 <b>(-37.85%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>354.80 (n/a)</td><td>237.14 (n/a)</td><td>220.90 (n/a)</td><td>178.10 (n/a)</td><td>68.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 <b>(-33.52%)</b></td><td>0.03 <b>(-25.11%)</b></td><td>0.03 <b>(-22.70%)</b></td><td>0.02 (-14.52%)</td><td>0.00 <b>(-67.96%)</b></td><td>229.10 (+17.01%)</td><td>200.14 <b>(+29.83%)</b></td><td>192.90 <b>(+29.38%)</b></td><td>181.00 <b>(+50.46%)</b></td><td>18.48 <b>(-42.77%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>154.16 (n/a)</td><td>149.10 (n/a)</td><td>120.30 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+3.04%)</td><td>0.03 (-1.67%)</td><td>0.03 (+3.75%)</td><td>0.02 (-10.38%)</td><td>0.00 <b>(+69.59%)</b></td><td>212.30 (+11.62%)</td><td>175.12 (+3.00%)</td><td>166.80 (-3.64%)</td><td>150.70 (-2.96%)</td><td>27.42 <b>(+84.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.20 (n/a)</td><td>170.02 (n/a)</td><td>173.10 (n/a)</td><td>155.30 (n/a)</td><td>14.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (-5.51%)</td><td>0.03 (+6.85%)</td><td>0.03 (+16.14%)</td><td>0.03 (+9.06%)</td><td>0.01 <b>(-25.59%)</b></td><td>195.50 (-8.30%)</td><td>157.64 (-8.68%)</td><td>150.10 (-13.93%)</td><td>122.20 (+5.80%)</td><td>29.76 <b>(-28.69%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>172.62 (n/a)</td><td>174.40 (n/a)</td><td>115.50 (n/a)</td><td>41.74 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (+14.70%)</td><td>0.03 (-7.86%)</td><td>0.02 (-16.19%)</td><td>0.02 <b>(-24.79%)</b></td><td>0.01 <b>(+100.49%)</b></td><td>280.80 <b>(+32.95%)</b></td><td>203.60 (+13.54%)</td><td>211.60 (+19.35%)</td><td>137.00 (-12.79%)</td><td>54.06 <b>(+133.62%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.20 (n/a)</td><td>179.32 (n/a)</td><td>177.30 (n/a)</td><td>157.10 (n/a)</td><td>23.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (+0.45%)</td><td>0.03 (-3.39%)</td><td>0.03 (+6.85%)</td><td>0.02 (-15.48%)</td><td>0.01 <b>(+86.14%)</b></td><td>233.20 (+18.32%)</td><td>180.38 (+6.39%)</td><td>153.20 (-6.41%)</td><td>148.70 (-0.40%)</td><td>39.96 <b>(+114.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>197.10 (n/a)</td><td>169.54 (n/a)</td><td>163.70 (n/a)</td><td>149.30 (n/a)</td><td>18.61 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (-11.92%)</td><td>0.03 (-4.75%)</td><td>0.03 (+9.51%)</td><td>0.03 (-9.71%)</td><td>0.01 <b>(-25.79%)</b></td><td>209.30 (+10.74%)</td><td>166.96 (+3.95%)</td><td>160.80 (-8.69%)</td><td>138.70 (+13.50%)</td><td>28.61 (-7.14%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>160.62 (n/a)</td><td>176.10 (n/a)</td><td>122.20 (n/a)</td><td>30.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-12.70%)</td><td>0.03 (-11.53%)</td><td>0.03 (-6.20%)</td><td>0.02 <b>(-22.52%)</b></td><td>0.00 <b>(+29.07%)</b></td><td>227.40 <b>(+29.06%)</b></td><td>181.76 (+14.40%)</td><td>171.40 (+6.66%)</td><td>156.70 (+14.55%)</td><td>30.21 <b>(+87.42%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>176.20 (n/a)</td><td>158.88 (n/a)</td><td>160.70 (n/a)</td><td>136.80 (n/a)</td><td>16.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+15.37%)</td><td>0.03 (+4.85%)</td><td>0.03 (+5.43%)</td><td>0.02 (-8.15%)</td><td>0.00 <b>(+188.52%)</b></td><td>244.20 (+8.87%)</td><td>203.42 (-2.72%)</td><td>203.20 (-5.14%)</td><td>168.70 (-13.31%)</td><td>34.18 <b>(+169.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.30 (n/a)</td><td>209.10 (n/a)</td><td>214.20 (n/a)</td><td>194.60 (n/a)</td><td>12.67 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 <b>(+25.92%)</b></td><td>0.07 (-4.97%)</td><td>0.07 (-14.67%)</td><td>0.06 (+5.89%)</td><td>0.02 <b>(+58.15%)</b></td><td>189.30 (-5.54%)</td><td>155.90 (+7.56%)</td><td>157.30 (+17.21%)</td><td>100.00 <b>(-20.63%)</b></td><td>35.24 (+12.90%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>144.94 (n/a)</td><td>134.20 (n/a)</td><td>126.00 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (+8.14%)</td><td>0.07 (-4.38%)</td><td>0.07 (+3.70%)</td><td>0.04 <b>(-28.78%)</b></td><td>0.02 <b>(+115.36%)</b></td><td>234.40 <b>(+40.36%)</b></td><td>167.50 (+10.31%)</td><td>148.40 (-3.57%)</td><td>116.20 (-7.56%)</td><td>48.53 <b>(+183.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>167.00 (n/a)</td><td>151.84 (n/a)</td><td>153.90 (n/a)</td><td>125.70 (n/a)</td><td>17.13 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 <b>(+25.47%)</b></td><td>0.08 (+18.58%)</td><td>0.09 <b>(+42.18%)</b></td><td>0.05 (-18.08%)</td><td>0.02 <b>(+246.61%)</b></td><td>210.60 <b>(+22.09%)</b></td><td>143.92 (-10.76%)</td><td>117.00 <b>(-29.69%)</b></td><td>111.30 <b>(-20.27%)</b></td><td>43.09 <b>(+235.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>172.50 (n/a)</td><td>161.28 (n/a)</td><td>166.40 (n/a)</td><td>139.60 (n/a)</td><td>12.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 <b>(+26.75%)</b></td><td>0.07 (+7.11%)</td><td>0.07 (-0.87%)</td><td>0.05 <b>(-20.24%)</b></td><td>0.02 <b>(+219.70%)</b></td><td>222.50 <b>(+25.35%)</b></td><td>155.26 (-0.96%)</td><td>156.80 (+0.84%)</td><td>107.80 <b>(-21.08%)</b></td><td>45.40 <b>(+211.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>156.76 (n/a)</td><td>155.50 (n/a)</td><td>136.60 (n/a)</td><td>14.59 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (+19.07%)</td><td>0.06 (+5.03%)</td><td>0.06 (-0.78%)</td><td>0.05 (-5.18%)</td><td>0.02 <b>(+87.45%)</b></td><td>222.40 (+5.45%)</td><td>175.94 (-0.25%)</td><td>183.70 (+0.82%)</td><td>117.40 (-15.96%)</td><td>48.85 <b>(+71.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>176.38 (n/a)</td><td>182.20 (n/a)</td><td>139.70 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (-3.20%)</td><td>0.06 (-0.71%)</td><td>0.05 (-8.58%)</td><td>0.05 <b>(+39.07%)</b></td><td>0.01 <b>(-49.25%)</b></td><td>211.40 <b>(-28.10%)</b></td><td>193.06 (-4.07%)</td><td>203.30 (+9.36%)</td><td>157.10 (+3.29%)</td><td>23.01 <b>(-61.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>294.00 (n/a)</td><td>201.26 (n/a)</td><td>185.90 (n/a)</td><td>152.10 (n/a)</td><td>59.16 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (-6.31%)</td><td>0.06 (-11.60%)</td><td>0.06 (-11.76%)</td><td>0.03 <b>(-41.66%)</b></td><td>0.02 <b>(+68.06%)</b></td><td>331.50 <b>(+71.41%)</b></td><td>202.04 <b>(+20.69%)</b></td><td>177.30 (+13.29%)</td><td>149.50 (+6.71%)</td><td>74.54 <b>(+208.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>167.40 (n/a)</td><td>156.50 (n/a)</td><td>140.10 (n/a)</td><td>24.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (+0.34%)</td><td>0.05 (-6.48%)</td><td>0.05 (+1.54%)</td><td>0.03 <b>(-39.39%)</b></td><td>0.01 <b>(+70.12%)</b></td><td>379.90 <b>(+64.96%)</b></td><td>230.08 (+14.46%)</td><td>204.10 (-1.50%)</td><td>162.10 (-0.31%)</td><td>86.73 <b>(+192.44%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>230.30 (n/a)</td><td>201.02 (n/a)</td><td>207.20 (n/a)</td><td>162.60 (n/a)</td><td>29.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (+5.33%)</td><td>0.13 (+8.05%)</td><td>0.13 (+9.83%)</td><td>0.12 (+8.40%)</td><td>0.01 (+2.60%)</td><td>171.70 (-7.74%)</td><td>161.86 (-7.47%)</td><td>158.20 (-8.98%)</td><td>154.60 (-5.04%)</td><td>7.71 (-9.83%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>186.10 (n/a)</td><td>174.92 (n/a)</td><td>173.80 (n/a)</td><td>162.80 (n/a)</td><td>8.55 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 <b>(+36.97%)</b></td><td>0.15 <b>(+22.67%)</b></td><td>0.16 <b>(+26.64%)</b></td><td>0.10 (-11.41%)</td><td>0.03 <b>(+279.62%)</b></td><td>212.40 (+12.86%)</td><td>143.20 (-14.78%)</td><td>130.50 <b>(-21.05%)</b></td><td>113.10 <b>(-26.99%)</b></td><td>39.75 <b>(+222.85%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>168.04 (n/a)</td><td>165.30 (n/a)</td><td>154.90 (n/a)</td><td>12.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (-9.26%)</td><td>0.12 (-10.11%)</td><td>0.11 (-13.36%)</td><td>0.10 (-13.49%)</td><td>0.03 (+4.04%)</td><td>219.00 (+15.57%)</td><td>183.48 (+12.51%)</td><td>193.90 (+15.42%)</td><td>130.20 (+10.15%)</td><td>37.32 <b>(+39.12%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>189.50 (n/a)</td><td>163.08 (n/a)</td><td>168.00 (n/a)</td><td>118.20 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 <b>(+34.94%)</b></td><td>0.13 (+9.48%)</td><td>0.12 (-2.89%)</td><td>0.11 (+0.29%)</td><td>0.03 <b>(+181.94%)</b></td><td>194.00 (-0.31%)</td><td>164.02 (-5.98%)</td><td>175.40 (+2.93%)</td><td>118.00 <b>(-25.93%)</b></td><td>32.27 <b>(+110.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>194.60 (n/a)</td><td>174.46 (n/a)</td><td>170.40 (n/a)</td><td>159.30 (n/a)</td><td>15.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 <b>(+32.41%)</b></td><td>0.14 <b>(+28.52%)</b></td><td>0.14 <b>(+25.37%)</b></td><td>0.12 <b>(+26.01%)</b></td><td>0.03 <b>(+39.82%)</b></td><td>180.10 <b>(-20.63%)</b></td><td>149.74 <b>(-21.87%)</b></td><td>153.80 <b>(-20.27%)</b></td><td>104.50 <b>(-24.49%)</b></td><td>27.71 (-18.18%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>226.90 (n/a)</td><td>191.66 (n/a)</td><td>192.90 (n/a)</td><td>138.40 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 <b>(+27.48%)</b></td><td>0.11 (+4.85%)</td><td>0.11 (+3.67%)</td><td>0.07 (-7.45%)</td><td>0.03 <b>(+114.63%)</b></td><td>281.90 (+8.05%)</td><td>209.96 (-1.04%)</td><td>199.70 (-3.53%)</td><td>142.20 <b>(-21.57%)</b></td><td>51.78 <b>(+75.81%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>260.90 (n/a)</td><td>212.16 (n/a)</td><td>207.00 (n/a)</td><td>181.30 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (+7.56%)</td><td>0.10 (-15.00%)</td><td>0.10 (-17.22%)</td><td>0.07 <b>(-28.78%)</b></td><td>0.02 <b>(+188.76%)</b></td><td>280.90 <b>(+40.45%)</b></td><td>220.42 <b>(+21.70%)</b></td><td>213.10 <b>(+20.80%)</b></td><td>156.60 (-7.06%)</td><td>46.02 <b>(+270.45%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>181.12 (n/a)</td><td>176.40 (n/a)</td><td>168.50 (n/a)</td><td>12.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (+17.91%)</td><td>0.10 (+18.96%)</td><td>0.10 <b>(+25.51%)</b></td><td>0.06 (+0.09%)</td><td>0.02 <b>(+38.40%)</b></td><td>340.30 (-0.09%)</td><td>232.96 (-14.13%)</td><td>218.00 <b>(-20.32%)</b></td><td>176.00 (-15.22%)</td><td>66.89 (+17.36%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>340.60 (n/a)</td><td>271.30 (n/a)</td><td>273.60 (n/a)</td><td>207.60 (n/a)</td><td>56.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>230.20 (n/a)</td><td>188.26 (n/a)</td><td>189.20 (n/a)</td><td>164.40 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>184.70 (n/a)</td><td>174.90 (n/a)</td><td>178.40 (n/a)</td><td>160.90 (n/a)</td><td>10.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>175.60 (n/a)</td><td>149.70 (n/a)</td><td>150.90 (n/a)</td><td>127.90 (n/a)</td><td>17.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>177.30 (n/a)</td><td>153.70 (n/a)</td><td>157.50 (n/a)</td><td>132.20 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>156.60 (n/a)</td><td>138.46 (n/a)</td><td>136.20 (n/a)</td><td>115.80 (n/a)</td><td>17.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>287.30 (n/a)</td><td>162.02 (n/a)</td><td>131.80 (n/a)</td><td>111.90 (n/a)</td><td>71.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>156.30 (n/a)</td><td>146.92 (n/a)</td><td>154.10 (n/a)</td><td>132.50 (n/a)</td><td>11.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>264.40 (n/a)</td><td>170.46 (n/a)</td><td>163.30 (n/a)</td><td>112.80 (n/a)</td><td>57.47 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>165.00 (n/a)</td><td>141.04 (n/a)</td><td>133.10 (n/a)</td><td>130.30 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>249.50 (n/a)</td><td>165.88 (n/a)</td><td>132.60 (n/a)</td><td>117.20 (n/a)</td><td>57.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>229.40 (n/a)</td><td>176.02 (n/a)</td><td>164.00 (n/a)</td><td>127.70 (n/a)</td><td>40.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>249.40 (n/a)</td><td>172.06 (n/a)</td><td>159.00 (n/a)</td><td>133.90 (n/a)</td><td>44.62 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.38 <b>(+26.17%)</b></td><td>0.33 <b>(+25.01%)</b></td><td>0.37 <b>(+43.17%)</b></td><td>0.23 (-4.43%)</td><td>0.07 <b>(+182.33%)</b></td><td>217.20 (+4.67%)</td><td>154.42 (-17.22%)</td><td>132.50 <b>(-30.15%)</b></td><td>129.10 <b>(-20.75%)</b></td><td>37.94 <b>(+132.35%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>207.50 (n/a)</td><td>186.54 (n/a)</td><td>189.70 (n/a)</td><td>162.90 (n/a)</td><td>16.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>172.90 (n/a)</td><td>144.04 (n/a)</td><td>132.10 (n/a)</td><td>128.10 (n/a)</td><td>19.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>244.10 (n/a)</td><td>160.00 (n/a)</td><td>140.30 (n/a)</td><td>125.40 (n/a)</td><td>48.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>173.10 (n/a)</td><td>160.84 (n/a)</td><td>161.90 (n/a)</td><td>136.00 (n/a)</td><td>14.84 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.30 (n/a)</td><td>190.18 (n/a)</td><td>170.90 (n/a)</td><td>155.60 (n/a)</td><td>37.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>170.62 (n/a)</td><td>168.40 (n/a)</td><td>142.00 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.10 (n/a)</td><td>165.98 (n/a)</td><td>163.50 (n/a)</td><td>147.50 (n/a)</td><td>18.13 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.70 (n/a)</td><td>209.60 (n/a)</td><td>204.80 (n/a)</td><td>177.90 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>173.30 (n/a)</td><td>163.36 (n/a)</td><td>164.80 (n/a)</td><td>146.60 (n/a)</td><td>10.00 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>155.92 (n/a)</td><td>145.00 (n/a)</td><td>141.60 (n/a)</td><td>22.77 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.10 (n/a)</td><td>163.04 (n/a)</td><td>166.90 (n/a)</td><td>147.00 (n/a)</td><td>14.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>181.46 (n/a)</td><td>179.20 (n/a)</td><td>158.80 (n/a)</td><td>16.84 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>169.40 (n/a)</td><td>153.64 (n/a)</td><td>165.40 (n/a)</td><td>130.20 (n/a)</td><td>19.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>252.90 (n/a)</td><td>179.16 (n/a)</td><td>176.30 (n/a)</td><td>119.90 (n/a)</td><td>48.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>256.30 (n/a)</td><td>185.66 (n/a)</td><td>188.90 (n/a)</td><td>114.30 (n/a)</td><td>55.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>229.40 (n/a)</td><td>183.30 (n/a)</td><td>177.10 (n/a)</td><td>135.70 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>193.50 (n/a)</td><td>172.72 (n/a)</td><td>173.80 (n/a)</td><td>145.60 (n/a)</td><td>17.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>169.20 (n/a)</td><td>148.94 (n/a)</td><td>153.90 (n/a)</td><td>116.90 (n/a)</td><td>20.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>295.00 (n/a)</td><td>210.60 (n/a)</td><td>199.00 (n/a)</td><td>171.10 (n/a)</td><td>48.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>15.69 (+1.11%)</td><td>14.56 (+0.26%)</td><td>14.34 (-0.50%)</td><td>14.11 (+0.72%)</td><td>0.66 (+11.80%)</td><td>3948.40 (-0.72%)</td><td>3832.66 (-0.23%)</td><td>3883.80 (+0.50%)</td><td>3549.90 (-1.09%)</td><td>164.41 (+10.20%)</td><td>15123.75 (+1.11%)</td><td>14029.48 (+0.26%)</td><td>13823.24 (-0.50%)</td><td>13597.35 (+0.72%)</td><td>632.29 (+11.80%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>15.52 (n/a)</td><td>14.52 (n/a)</td><td>14.41 (n/a)</td><td>14.01 (n/a)</td><td>0.59 (n/a)</td><td>3977.00 (n/a)</td><td>3841.68 (n/a)</td><td>3864.60 (n/a)</td><td>3589.20 (n/a)</td><td>149.19 (n/a)</td><td>14957.80 (n/a)</td><td>13992.46 (n/a)</td><td>13892.02 (n/a)</td><td>13499.48 (n/a)</td><td>565.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>17.01 (+5.09%)</td><td>15.17 (+13.54%)</td><td>14.82 (+10.68%)</td><td>13.24 <b>(+37.49%)</b></td><td>1.55 <b>(-37.19%)</b></td><td>990.20 <b>(-27.27%)</b></td><td>871.06 (-13.89%)</td><td>884.60 (-9.65%)</td><td>770.80 (-4.84%)</td><td>89.11 <b>(-57.97%)</b></td><td>11144.79 (+5.09%)</td><td>9944.09 (+13.54%)</td><td>9710.24 (+10.68%)</td><td>8674.62 <b>(+37.49%)</b></td><td>1012.66 <b>(-37.19%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>16.18 (n/a)</td><td>13.36 (n/a)</td><td>13.39 (n/a)</td><td>9.63 (n/a)</td><td>2.46 (n/a)</td><td>1361.40 (n/a)</td><td>1011.62 (n/a)</td><td>979.10 (n/a)</td><td>810.00 (n/a)</td><td>212.01 (n/a)</td><td>10605.47 (n/a)</td><td>8758.18 (n/a)</td><td>8773.43 (n/a)</td><td>6309.43 (n/a)</td><td>1612.19 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>13.89 (-8.68%)</td><td>13.56 (-2.66%)</td><td>13.74 (-2.77%)</td><td>12.80 (+1.52%)</td><td>0.46 <b>(-61.54%)</b></td><td>4351.40 (-1.50%)</td><td>4113.10 (+2.22%)</td><td>4054.70 (+2.85%)</td><td>4010.00 (+9.51%)</td><td>143.20 <b>(-58.79%)</b></td><td>13388.41 (-8.68%)</td><td>13064.97 (-2.66%)</td><td>13240.69 (-2.77%)</td><td>12337.75 (+1.52%)</td><td>440.65 <b>(-61.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>15.21 (n/a)</td><td>13.93 (n/a)</td><td>14.13 (n/a)</td><td>12.61 (n/a)</td><td>1.19 (n/a)</td><td>4417.80 (n/a)</td><td>4023.72 (n/a)</td><td>3942.30 (n/a)</td><td>3661.80 (n/a)</td><td>347.47 (n/a)</td><td>14661.29 (n/a)</td><td>13421.66 (n/a)</td><td>13618.15 (n/a)</td><td>12152.47 (n/a)</td><td>1145.61 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>17.14 (+2.86%)</td><td>13.73 (-5.07%)</td><td>14.95 (+3.24%)</td><td>10.59 (-4.31%)</td><td>2.90 <b>(+36.70%)</b></td><td>1685.90 (+4.50%)</td><td>1351.00 (+7.26%)</td><td>1194.90 (-3.14%)</td><td>1042.20 (-2.78%)</td><td>297.57 <b>(+41.51%)</b></td><td>12878.48 (+2.86%)</td><td>10316.73 (-5.07%)</td><td>11232.49 (+3.24%)</td><td>7961.28 (-4.31%)</td><td>2178.57 <b>(+36.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>16.66 (n/a)</td><td>14.46 (n/a)</td><td>14.48 (n/a)</td><td>11.07 (n/a)</td><td>2.12 (n/a)</td><td>1613.30 (n/a)</td><td>1259.50 (n/a)</td><td>1233.60 (n/a)</td><td>1072.00 (n/a)</td><td>210.29 (n/a)</td><td>12520.39 (n/a)</td><td>10867.81 (n/a)</td><td>10880.26 (n/a)</td><td>8319.59 (n/a)</td><td>1593.72 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>11.24 (+2.52%)</td><td>10.87 (+2.11%)</td><td>10.75 (+1.12%)</td><td>10.54 (+1.39%)</td><td>0.34 <b>(+54.64%)</b></td><td>7774.00 (-1.37%)</td><td>7542.14 (-2.02%)</td><td>7617.00 (-1.10%)</td><td>7289.10 (-2.46%)</td><td>232.06 <b>(+48.32%)</b></td><td>14730.86 (+2.52%)</td><td>14247.47 (+2.11%)</td><td>14096.67 (+1.12%)</td><td>13812.04 (+1.39%)</td><td>441.32 <b>(+54.64%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>10.96 (n/a)</td><td>10.65 (n/a)</td><td>10.64 (n/a)</td><td>10.39 (n/a)</td><td>0.22 (n/a)</td><td>7882.20 (n/a)</td><td>7697.92 (n/a)</td><td>7702.00 (n/a)</td><td>7472.70 (n/a)</td><td>156.45 (n/a)</td><td>14368.82 (n/a)</td><td>13953.13 (n/a)</td><td>13941.15 (n/a)</td><td>13622.43 (n/a)</td><td>285.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>16.20 (+0.48%)</td><td>13.99 (+5.55%)</td><td>14.89 (+2.20%)</td><td>10.87 (+9.42%)</td><td>2.42 (-9.71%)</td><td>1977.30 (-8.61%)</td><td>1576.44 (-6.16%)</td><td>1443.40 (-2.16%)</td><td>1326.70 (-0.49%)</td><td>291.75 (-19.77%)</td><td>12948.95 (+0.48%)</td><td>11183.02 (+5.55%)</td><td>11902.20 (+2.20%)</td><td>8688.66 (+9.42%)</td><td>1931.92 (-9.71%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>16.12 (n/a)</td><td>13.26 (n/a)</td><td>14.57 (n/a)</td><td>9.94 (n/a)</td><td>2.68 (n/a)</td><td>2163.50 (n/a)</td><td>1679.94 (n/a)</td><td>1475.20 (n/a)</td><td>1333.20 (n/a)</td><td>363.64 (n/a)</td><td>12886.48 (n/a)</td><td>10595.31 (n/a)</td><td>11645.55 (n/a)</td><td>7940.70 (n/a)</td><td>2139.61 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>10.96 (-0.34%)</td><td>10.73 (+0.24%)</td><td>10.90 (+0.68%)</td><td>10.43 (+0.66%)</td><td>0.27 (-5.65%)</td><td>7856.40 (-0.65%)</td><td>7635.42 (-0.25%)</td><td>7517.00 (-0.68%)</td><td>7472.80 (+0.34%)</td><td>192.57 (-6.00%)</td><td>14368.68 (-0.34%)</td><td>14069.73 (+0.24%)</td><td>14284.11 (+0.68%)</td><td>13667.07 (+0.66%)</td><td>351.75 (-5.65%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>11.00 (n/a)</td><td>10.71 (n/a)</td><td>10.82 (n/a)</td><td>10.36 (n/a)</td><td>0.28 (n/a)</td><td>7908.00 (n/a)</td><td>7654.60 (n/a)</td><td>7568.30 (n/a)</td><td>7447.20 (n/a)</td><td>204.86 (n/a)</td><td>14418.07 (n/a)</td><td>14035.38 (n/a)</td><td>14187.29 (n/a)</td><td>13577.93 (n/a)</td><td>372.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.52 (-1.14%)</td><td>3.86 (+15.22%)</td><td>3.89 <b>(+28.54%)</b></td><td>2.98 (+2.12%)</td><td>0.59 (-15.64%)</td><td>462.30 (-2.08%)</td><td>364.20 (-13.92%)</td><td>353.90 <b>(-22.20%)</b></td><td>304.30 (+1.16%)</td><td>61.43 (-14.86%)</td><td>882.20 (-1.14%)</td><td>752.56 (+15.22%)</td><td>758.54 <b>(+28.54%)</b></td><td>580.64 (+2.12%)</td><td>115.94 (-15.64%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.58 (n/a)</td><td>3.35 (n/a)</td><td>3.03 (n/a)</td><td>2.92 (n/a)</td><td>0.70 (n/a)</td><td>472.10 (n/a)</td><td>423.10 (n/a)</td><td>454.90 (n/a)</td><td>300.80 (n/a)</td><td>72.16 (n/a)</td><td>892.40 (n/a)</td><td>653.13 (n/a)</td><td>590.13 (n/a)</td><td>568.60 (n/a)</td><td>137.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>5.83 <b>(+21.57%)</b></td><td>4.57 (+16.92%)</td><td>4.13 (+11.99%)</td><td>3.65 (+3.63%)</td><td>1.00 <b>(+97.40%)</b></td><td>377.50 (-3.50%)</td><td>312.36 (-12.31%)</td><td>332.90 (-10.70%)</td><td>236.10 (-17.76%)</td><td>64.69 <b>(+59.49%)</b></td><td>1136.76 <b>(+21.57%)</b></td><td>891.69 (+16.92%)</td><td>806.39 (+11.99%)</td><td>711.15 (+3.63%)</td><td>195.95 <b>(+97.40%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.79 (n/a)</td><td>3.91 (n/a)</td><td>3.69 (n/a)</td><td>3.52 (n/a)</td><td>0.51 (n/a)</td><td>391.20 (n/a)</td><td>356.20 (n/a)</td><td>372.80 (n/a)</td><td>287.10 (n/a)</td><td>40.56 (n/a)</td><td>935.03 (n/a)</td><td>762.67 (n/a)</td><td>720.03 (n/a)</td><td>686.21 (n/a)</td><td>99.26 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>5.54 (-12.60%)</td><td>4.27 (-8.29%)</td><td>3.93 (-9.32%)</td><td>3.39 (-9.64%)</td><td>0.85 (-17.21%)</td><td>405.90 (+10.66%)</td><td>332.22 (+8.58%)</td><td>349.80 (+10.28%)</td><td>248.30 (+14.42%)</td><td>61.47 (+5.29%)</td><td>1081.25 (-12.60%)</td><td>832.29 (-8.29%)</td><td>767.36 (-9.32%)</td><td>661.28 (-9.64%)</td><td>165.90 (-17.21%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.34 (n/a)</td><td>4.65 (n/a)</td><td>4.34 (n/a)</td><td>3.75 (n/a)</td><td>1.03 (n/a)</td><td>366.80 (n/a)</td><td>305.98 (n/a)</td><td>317.20 (n/a)</td><td>217.00 (n/a)</td><td>58.38 (n/a)</td><td>1237.06 (n/a)</td><td>907.50 (n/a)</td><td>846.20 (n/a)</td><td>731.79 (n/a)</td><td>200.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.32 <b>(+38.57%)</b></td><td>5.00 (+18.03%)</td><td>4.04 (+9.06%)</td><td>3.67 (+5.77%)</td><td>1.57 <b>(+66.75%)</b></td><td>375.30 (-5.44%)</td><td>295.34 (-12.45%)</td><td>340.50 (-8.30%)</td><td>188.00 <b>(-27.83%)</b></td><td>80.65 (+15.37%)</td><td>1427.86 <b>(+38.57%)</b></td><td>975.18 (+18.03%)</td><td>788.43 (+9.06%)</td><td>715.27 (+5.77%)</td><td>306.35 <b>(+66.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>5.28 (n/a)</td><td>4.24 (n/a)</td><td>3.71 (n/a)</td><td>3.47 (n/a)</td><td>0.94 (n/a)</td><td>396.90 (n/a)</td><td>337.32 (n/a)</td><td>371.30 (n/a)</td><td>260.50 (n/a)</td><td>69.91 (n/a)</td><td>1030.44 (n/a)</td><td>826.19 (n/a)</td><td>722.91 (n/a)</td><td>676.25 (n/a)</td><td>183.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>5.26 <b>(+31.68%)</b></td><td>4.03 (+16.89%)</td><td>3.26 (-4.09%)</td><td>3.20 (+2.77%)</td><td>1.11 <b>(+232.90%)</b></td><td>430.70 (-2.69%)</td><td>361.70 (-10.11%)</td><td>422.70 (+4.27%)</td><td>261.50 <b>(-24.07%)</b></td><td>90.29 <b>(+150.31%)</b></td><td>1026.45 <b>(+31.68%)</b></td><td>785.23 (+16.89%)</td><td>635.10 (-4.09%)</td><td>623.27 (+2.77%)</td><td>215.61 <b>(+232.90%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.00 (n/a)</td><td>3.44 (n/a)</td><td>3.39 (n/a)</td><td>3.11 (n/a)</td><td>0.33 (n/a)</td><td>442.60 (n/a)</td><td>402.38 (n/a)</td><td>405.40 (n/a)</td><td>344.40 (n/a)</td><td>36.07 (n/a)</td><td>779.51 (n/a)</td><td>671.78 (n/a)</td><td>662.18 (n/a)</td><td>606.45 (n/a)</td><td>64.77 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.73 (-3.37%)</td><td>3.75 (+2.44%)</td><td>3.39 (+5.79%)</td><td>2.93 (-4.86%)</td><td>0.90 (+17.70%)</td><td>469.40 (+5.13%)</td><td>384.10 (-0.99%)</td><td>406.00 (-5.47%)</td><td>291.20 (+3.48%)</td><td>87.63 <b>(+24.78%)</b></td><td>921.94 (-3.37%)</td><td>730.85 (+2.44%)</td><td>661.12 (+5.79%)</td><td>571.93 (-4.86%)</td><td>175.77 (+17.70%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.89 (n/a)</td><td>3.66 (n/a)</td><td>3.20 (n/a)</td><td>3.08 (n/a)</td><td>0.77 (n/a)</td><td>446.50 (n/a)</td><td>387.96 (n/a)</td><td>429.50 (n/a)</td><td>281.40 (n/a)</td><td>70.23 (n/a)</td><td>954.08 (n/a)</td><td>713.43 (n/a)</td><td>624.94 (n/a)</td><td>601.17 (n/a)</td><td>149.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>5.04 (+9.07%)</td><td>3.77 (+3.84%)</td><td>3.66 (+11.86%)</td><td>3.03 (+2.13%)</td><td>0.77 (+0.36%)</td><td>454.10 (-2.07%)</td><td>376.04 (-4.13%)</td><td>376.40 (-10.59%)</td><td>273.20 (-8.32%)</td><td>67.04 (-12.92%)</td><td>982.60 (+9.07%)</td><td>734.90 (+3.84%)</td><td>713.15 (+11.86%)</td><td>591.18 (+2.13%)</td><td>149.23 (+0.36%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.62 (n/a)</td><td>3.63 (n/a)</td><td>3.27 (n/a)</td><td>2.97 (n/a)</td><td>0.76 (n/a)</td><td>463.70 (n/a)</td><td>392.22 (n/a)</td><td>421.00 (n/a)</td><td>298.00 (n/a)</td><td>76.98 (n/a)</td><td>900.92 (n/a)</td><td>707.70 (n/a)</td><td>637.55 (n/a)</td><td>578.88 (n/a)</td><td>148.70 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.85 (-3.54%)</td><td>1.30 (-10.18%)</td><td>1.08 (-8.84%)</td><td>1.06 (-5.96%)</td><td>0.35 (-12.72%)</td><td>379.90 (+6.35%)</td><td>324.84 (+10.49%)</td><td>370.70 (+9.71%)</td><td>217.20 (+3.68%)</td><td>73.03 (-0.53%)</td><td>154.50 (-3.54%)</td><td>108.45 (-10.18%)</td><td>90.52 (-8.84%)</td><td>88.33 (-5.96%)</td><td>28.91 (-12.72%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.92 (n/a)</td><td>1.44 (n/a)</td><td>1.19 (n/a)</td><td>1.12 (n/a)</td><td>0.40 (n/a)</td><td>357.20 (n/a)</td><td>294.00 (n/a)</td><td>337.90 (n/a)</td><td>209.50 (n/a)</td><td>73.42 (n/a)</td><td>160.18 (n/a)</td><td>120.74 (n/a)</td><td>99.30 (n/a)</td><td>93.93 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>8.12 (-18.39%)</td><td>6.67 (+13.20%)</td><td>6.48 <b>(+32.31%)</b></td><td>5.71 <b>(+26.39%)</b></td><td>0.91 <b>(-60.30%)</b></td><td>338.80 <b>(-20.88%)</b></td><td>293.98 (-17.64%)</td><td>298.50 <b>(-24.43%)</b></td><td>238.10 <b>(+22.54%)</b></td><td>37.20 <b>(-60.11%)</b></td><td>1690.80 (-18.39%)</td><td>1388.55 (+13.20%)</td><td>1348.84 <b>(+32.31%)</b></td><td>1188.59 <b>(+26.39%)</b></td><td>188.70 <b>(-60.30%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>9.95 (n/a)</td><td>5.89 (n/a)</td><td>4.89 (n/a)</td><td>4.52 (n/a)</td><td>2.28 (n/a)</td><td>428.20 (n/a)</td><td>356.96 (n/a)</td><td>395.00 (n/a)</td><td>194.30 (n/a)</td><td>93.25 (n/a)</td><td>2071.79 (n/a)</td><td>1226.67 (n/a)</td><td>1019.47 (n/a)</td><td>940.44 (n/a)</td><td>475.34 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>16.17 (-13.49%)</td><td>12.38 (-9.59%)</td><td>11.45 (-4.07%)</td><td>10.92 (-2.44%)</td><td>2.16 <b>(-30.61%)</b></td><td>504.30 (+2.50%)</td><td>453.94 (+8.88%)</td><td>480.90 (+4.23%)</td><td>340.50 (+15.58%)</td><td>65.91 (-19.45%)</td><td>6307.06 (-13.49%)</td><td>4828.36 (-9.59%)</td><td>4465.40 (-4.07%)</td><td>4258.09 (-2.44%)</td><td>843.71 <b>(-30.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>18.69 (n/a)</td><td>13.69 (n/a)</td><td>11.93 (n/a)</td><td>11.19 (n/a)</td><td>3.12 (n/a)</td><td>492.00 (n/a)</td><td>416.92 (n/a)</td><td>461.40 (n/a)</td><td>294.60 (n/a)</td><td>81.82 (n/a)</td><td>7290.45 (n/a)</td><td>5340.56 (n/a)</td><td>4654.69 (n/a)</td><td>4364.74 (n/a)</td><td>1215.89 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>10.03 (-7.48%)</td><td>8.28 (-1.49%)</td><td>8.01 (-9.51%)</td><td>7.42 <b>(+30.51%)</b></td><td>1.03 <b>(-45.23%)</b></td><td>741.90 <b>(-23.38%)</b></td><td>672.18 (-1.91%)</td><td>687.50 (+10.51%)</td><td>548.90 (+8.07%)</td><td>75.40 <b>(-56.68%)</b></td><td>3912.01 (-7.48%)</td><td>3230.95 (-1.49%)</td><td>3123.71 (-9.51%)</td><td>2894.64 <b>(+30.51%)</b></td><td>403.57 <b>(-45.23%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>10.84 (n/a)</td><td>8.41 (n/a)</td><td>8.85 (n/a)</td><td>5.69 (n/a)</td><td>1.89 (n/a)</td><td>968.30 (n/a)</td><td>685.30 (n/a)</td><td>622.10 (n/a)</td><td>507.90 (n/a)</td><td>174.04 (n/a)</td><td>4228.27 (n/a)</td><td>3279.98 (n/a)</td><td>3451.80 (n/a)</td><td>2217.89 (n/a)</td><td>736.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>12.31 (+11.66%)</td><td>9.21 (-6.35%)</td><td>8.88 (-14.82%)</td><td>5.22 <b>(-37.37%)</b></td><td>2.79 <b>(+141.35%)</b></td><td>1111.40 <b>(+59.68%)</b></td><td>689.18 (+15.54%)</td><td>653.30 (+17.39%)</td><td>471.20 (-10.44%)</td><td>254.51 <b>(+247.27%)</b></td><td>5127.52 (+11.66%)</td><td>3837.10 (-6.35%)</td><td>3698.00 (-14.82%)</td><td>2173.85 <b>(-37.37%)</b></td><td>1161.77 <b>(+141.35%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>11.02 (n/a)</td><td>9.84 (n/a)</td><td>10.42 (n/a)</td><td>8.33 (n/a)</td><td>1.16 (n/a)</td><td>696.00 (n/a)</td><td>596.50 (n/a)</td><td>556.50 (n/a)</td><td>526.10 (n/a)</td><td>73.29 (n/a)</td><td>4591.93 (n/a)</td><td>4097.36 (n/a)</td><td>4341.51 (n/a)</td><td>3471.07 (n/a)</td><td>481.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>169.40 (n/a)</td><td>141.66 (n/a)</td><td>137.40 (n/a)</td><td>117.70 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>155.20 (n/a)</td><td>132.26 (n/a)</td><td>136.10 (n/a)</td><td>108.60 (n/a)</td><td>18.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.20 (n/a)</td><td>143.92 (n/a)</td><td>144.20 (n/a)</td><td>124.10 (n/a)</td><td>19.64 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.70 (n/a)</td><td>172.04 (n/a)</td><td>172.40 (n/a)</td><td>137.50 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>263.70 (n/a)</td><td>176.38 (n/a)</td><td>162.70 (n/a)</td><td>115.30 (n/a)</td><td>58.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.20 (n/a)</td><td>165.58 (n/a)</td><td>166.40 (n/a)</td><td>140.40 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>290.80 (n/a)</td><td>176.18 (n/a)</td><td>158.00 (n/a)</td><td>125.50 (n/a)</td><td>66.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.70 (n/a)</td><td>218.08 (n/a)</td><td>216.80 (n/a)</td><td>208.90 (n/a)</td><td>6.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>361.60 (n/a)</td><td>212.56 (n/a)</td><td>191.40 (n/a)</td><td>140.40 (n/a)</td><td>86.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.70 (n/a)</td><td>172.52 (n/a)</td><td>183.10 (n/a)</td><td>143.10 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>175.30 (n/a)</td><td>180.50 (n/a)</td><td>136.30 (n/a)</td><td>25.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.90 (n/a)</td><td>153.98 (n/a)</td><td>158.40 (n/a)</td><td>116.30 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>155.78 (n/a)</td><td>153.00 (n/a)</td><td>139.90 (n/a)</td><td>16.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.80 (n/a)</td><td>150.18 (n/a)</td><td>148.50 (n/a)</td><td>129.50 (n/a)</td><td>13.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>286.00 (n/a)</td><td>199.66 (n/a)</td><td>211.80 (n/a)</td><td>123.90 (n/a)</td><td>65.96 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>337.00 (n/a)</td><td>239.92 (n/a)</td><td>241.80 (n/a)</td><td>160.00 (n/a)</td><td>79.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>228.90 (n/a)</td><td>170.38 (n/a)</td><td>142.20 (n/a)</td><td>123.70 (n/a)</td><td>52.48 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.00 (n/a)</td><td>182.30 (n/a)</td><td>183.50 (n/a)</td><td>141.40 (n/a)</td><td>28.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>161.22 (n/a)</td><td>142.40 (n/a)</td><td>131.40 (n/a)</td><td>34.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>233.20 (n/a)</td><td>151.08 (n/a)</td><td>135.40 (n/a)</td><td>102.00 (n/a)</td><td>51.01 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.60 (n/a)</td><td>183.12 (n/a)</td><td>178.20 (n/a)</td><td>147.70 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>232.40 (n/a)</td><td>151.36 (n/a)</td><td>135.40 (n/a)</td><td>110.30 (n/a)</td><td>47.26 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>320.80 (n/a)</td><td>193.00 (n/a)</td><td>160.90 (n/a)</td><td>144.60 (n/a)</td><td>74.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>264.40 (n/a)</td><td>198.50 (n/a)</td><td>195.20 (n/a)</td><td>150.10 (n/a)</td><td>41.75 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>187.40 (n/a)</td><td>164.06 (n/a)</td><td>159.90 (n/a)</td><td>141.70 (n/a)</td><td>17.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>189.50 (n/a)</td><td>171.06 (n/a)</td><td>180.60 (n/a)</td><td>132.20 (n/a)</td><td>23.84 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>321.30 (n/a)</td><td>209.10 (n/a)</td><td>199.60 (n/a)</td><td>143.40 (n/a)</td><td>67.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.20 (n/a)</td><td>164.96 (n/a)</td><td>167.40 (n/a)</td><td>141.60 (n/a)</td><td>24.01 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>208.60 (n/a)</td><td>178.94 (n/a)</td><td>183.70 (n/a)</td><td>139.80 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>228.50 (n/a)</td><td>183.18 (n/a)</td><td>186.10 (n/a)</td><td>137.30 (n/a)</td><td>35.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.60 (n/a)</td><td>168.04 (n/a)</td><td>175.40 (n/a)</td><td>126.70 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>374.40 (n/a)</td><td>268.76 (n/a)</td><td>255.10 (n/a)</td><td>190.60 (n/a)</td><td>76.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.12 (+0.08%)</td><td>4.11 (+0.13%)</td><td>4.11 (-0.00%)</td><td>4.11 (+0.44%)</td><td>0.01 <b>(-55.13%)</b></td><td>19144.70 (-0.44%)</td><td>19117.32 (-0.13%)</td><td>19120.60 (+0.00%)</td><td>19078.90 (-0.08%)</td><td>23.96 <b>(-55.42%)</b></td><td>2813.96 (+0.08%)</td><td>2808.30 (+0.13%)</td><td>2807.82 (-0.00%)</td><td>2804.28 (+0.44%)</td><td>3.53 <b>(-55.14%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>4.09 (n/a)</td><td>0.01 (n/a)</td><td>19229.80 (n/a)</td><td>19142.08 (n/a)</td><td>19119.90 (n/a)</td><td>19094.60 (n/a)</td><td>53.74 (n/a)</td><td>2811.64 (n/a)</td><td>2804.68 (n/a)</td><td>2807.92 (n/a)</td><td>2791.87 (n/a)</td><td>7.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.88 (+1.16%)</td><td>4.31 (+1.41%)</td><td>4.20 (+1.81%)</td><td>4.09 (+1.04%)</td><td>0.32 (-0.93%)</td><td>2301.50 (-1.02%)</td><td>2191.86 (-1.41%)</td><td>2240.50 (-1.77%)</td><td>1928.30 (-1.14%)</td><td>149.60 (-3.53%)</td><td>1918.46 (+1.15%)</td><td>1694.68 (+1.41%)</td><td>1651.16 (+1.81%)</td><td>1607.40 (+1.04%)</td><td>126.47 (-0.93%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.82 (n/a)</td><td>4.25 (n/a)</td><td>4.12 (n/a)</td><td>4.04 (n/a)</td><td>0.32 (n/a)</td><td>2325.30 (n/a)</td><td>2223.24 (n/a)</td><td>2280.90 (n/a)</td><td>1950.60 (n/a)</td><td>155.07 (n/a)</td><td>1896.56 (n/a)</td><td>1671.07 (n/a)</td><td>1621.88 (n/a)</td><td>1590.89 (n/a)</td><td>127.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.03 (-6.39%)</td><td>0.95 (+1.38%)</td><td>0.97 (-8.89%)</td><td>0.82 <b>(+20.07%)</b></td><td>0.08 <b>(-59.86%)</b></td><td>270.10 (-16.71%)</td><td>234.14 (-4.68%)</td><td>228.40 (+9.75%)</td><td>214.10 (+6.84%)</td><td>21.29 <b>(-62.97%)</b></td><td>44.07 (-6.39%)</td><td>40.56 (+1.38%)</td><td>41.32 (-8.89%)</td><td>34.94 <b>(+20.07%)</b></td><td>3.41 <b>(-59.86%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.10 (n/a)</td><td>0.94 (n/a)</td><td>1.06 (n/a)</td><td>0.68 (n/a)</td><td>0.20 (n/a)</td><td>324.30 (n/a)</td><td>245.64 (n/a)</td><td>208.10 (n/a)</td><td>200.40 (n/a)</td><td>57.47 (n/a)</td><td>47.08 (n/a)</td><td>40.00 (n/a)</td><td>45.35 (n/a)</td><td>29.10 (n/a)</td><td>8.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.38 (+12.25%)</td><td>1.09 (+6.81%)</td><td>1.02 (-8.24%)</td><td>0.99 <b>(+48.69%)</b></td><td>0.16 <b>(-26.13%)</b></td><td>222.40 <b>(-32.75%)</b></td><td>206.86 (-9.31%)</td><td>217.00 (+8.94%)</td><td>160.80 (-10.91%)</td><td>25.92 <b>(-57.43%)</b></td><td>58.70 (+12.25%)</td><td>46.31 (+6.81%)</td><td>43.48 (-8.24%)</td><td>42.43 <b>(+48.69%)</b></td><td>6.95 <b>(-26.13%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.23 (n/a)</td><td>1.02 (n/a)</td><td>1.11 (n/a)</td><td>0.67 (n/a)</td><td>0.22 (n/a)</td><td>330.70 (n/a)</td><td>228.10 (n/a)</td><td>199.20 (n/a)</td><td>180.50 (n/a)</td><td>60.89 (n/a)</td><td>52.29 (n/a)</td><td>43.36 (n/a)</td><td>47.38 (n/a)</td><td>28.54 (n/a)</td><td>9.41 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.53 (+0.04%)</td><td>0.53 (-0.03%)</td><td>0.53 (-0.01%)</td><td>0.53 (-0.12%)</td><td>0.00 <b>(+77.36%)</b></td><td>47889.00 (+0.12%)</td><td>47803.18 (+0.03%)</td><td>47794.80 (+0.01%)</td><td>47737.90 (-0.04%)</td><td>58.27 <b>(+77.44%)</b></td><td>359.88 (+0.04%)</td><td>359.39 (-0.03%)</td><td>359.45 (-0.01%)</td><td>358.74 (-0.12%)</td><td>0.44 <b>(+77.34%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47833.20 (n/a)</td><td>47790.70 (n/a)</td><td>47790.10 (n/a)</td><td>47754.80 (n/a)</td><td>32.84 (n/a)</td><td>359.75 (n/a)</td><td>359.48 (n/a)</td><td>359.49 (n/a)</td><td>359.16 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (-0.35%)</td><td>0.21 (-0.33%)</td><td>0.21 (-0.62%)</td><td>0.21 (-0.31%)</td><td>0.00 (-3.36%)</td><td>119879.90 (+0.31%)</td><td>118794.58 (+0.33%)</td><td>118943.30 (+0.63%)</td><td>117766.70 (+0.35%)</td><td>786.91 (-2.76%)</td><td>145.88 (-0.35%)</td><td>144.62 (-0.33%)</td><td>144.44 (-0.62%)</td><td>143.31 (-0.31%)</td><td>0.96 (-3.36%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119506.30 (n/a)</td><td>118407.62 (n/a)</td><td>118202.00 (n/a)</td><td>117359.10 (n/a)</td><td>809.25 (n/a)</td><td>146.39 (n/a)</td><td>145.10 (n/a)</td><td>145.34 (n/a)</td><td>143.76 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.92 (+1.44%)</td><td>0.91 (+0.49%)</td><td>0.90 (-0.58%)</td><td>0.90 (+1.04%)</td><td>0.01 <b>(+35.83%)</b></td><td>27987.30 (-1.03%)</td><td>27725.10 (-0.48%)</td><td>27918.80 (+0.58%)</td><td>27242.80 (-1.42%)</td><td>333.07 <b>(+32.49%)</b></td><td>630.62 (+1.44%)</td><td>619.72 (+0.49%)</td><td>615.35 (-0.58%)</td><td>613.85 (+1.04%)</td><td>7.50 <b>(+35.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28279.00 (n/a)</td><td>27858.76 (n/a)</td><td>27757.90 (n/a)</td><td>27636.00 (n/a)</td><td>251.39 (n/a)</td><td>621.65 (n/a)</td><td>616.72 (n/a)</td><td>618.92 (n/a)</td><td>607.51 (n/a)</td><td>5.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>3.65 (+1.00%)</td><td>3.58 (-0.01%)</td><td>3.56 (-0.96%)</td><td>3.49 (-0.58%)</td><td>0.07 <b>(+61.75%)</b></td><td>7218.80 (+0.59%)</td><td>7038.80 (+0.02%)</td><td>7073.00 (+0.97%)</td><td>6888.80 (-0.98%)</td><td>135.37 <b>(+60.32%)</b></td><td>2493.89 (+1.00%)</td><td>2441.46 (-0.01%)</td><td>2428.94 (-0.96%)</td><td>2379.88 (-0.58%)</td><td>46.88 <b>(+61.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>3.62 (n/a)</td><td>3.58 (n/a)</td><td>3.59 (n/a)</td><td>3.51 (n/a)</td><td>0.04 (n/a)</td><td>7176.80 (n/a)</td><td>7037.06 (n/a)</td><td>7005.10 (n/a)</td><td>6957.30 (n/a)</td><td>84.44 (n/a)</td><td>2469.31 (n/a)</td><td>2441.62 (n/a)</td><td>2452.47 (n/a)</td><td>2393.82 (n/a)</td><td>28.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>3.23 (+9.43%)</td><td>2.97 (+2.03%)</td><td>2.88 (-1.15%)</td><td>2.72 (-4.63%)</td><td>0.22 <b>(+498.45%)</b></td><td>9250.60 (+4.85%)</td><td>8523.76 (-1.57%)</td><td>8752.30 (+1.16%)</td><td>7793.60 (-8.62%)</td><td>634.23 <b>(+467.19%)</b></td><td>2204.36 (+9.43%)</td><td>2024.61 (+2.03%)</td><td>1962.89 (-1.15%)</td><td>1857.16 (-4.63%)</td><td>152.71 <b>(+498.45%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.95 (n/a)</td><td>2.91 (n/a)</td><td>2.91 (n/a)</td><td>2.85 (n/a)</td><td>0.04 (n/a)</td><td>8822.40 (n/a)</td><td>8659.28 (n/a)</td><td>8651.90 (n/a)</td><td>8528.70 (n/a)</td><td>111.82 (n/a)</td><td>2014.37 (n/a)</td><td>1984.25 (n/a)</td><td>1985.68 (n/a)</td><td>1947.30 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>3.35 (+1.00%)</td><td>3.22 (+1.43%)</td><td>3.19 (+0.89%)</td><td>3.15 (+1.33%)</td><td>0.08 (+2.46%)</td><td>7979.50 (-1.31%)</td><td>7808.40 (-1.40%)</td><td>7888.50 (-0.88%)</td><td>7522.80 (-0.99%)</td><td>190.61 (+0.60%)</td><td>2283.71 (+1.00%)</td><td>2201.25 (+1.43%)</td><td>2177.84 (+0.89%)</td><td>2153.00 (+1.33%)</td><td>54.54 (+2.46%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>3.31 (n/a)</td><td>3.18 (n/a)</td><td>3.16 (n/a)</td><td>3.11 (n/a)</td><td>0.08 (n/a)</td><td>8085.60 (n/a)</td><td>7919.60 (n/a)</td><td>7958.30 (n/a)</td><td>7597.90 (n/a)</td><td>189.46 (n/a)</td><td>2261.14 (n/a)</td><td>2170.31 (n/a)</td><td>2158.73 (n/a)</td><td>2124.75 (n/a)</td><td>53.23 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 (-0.33%)</td><td>0.80 (-0.06%)</td><td>0.80 (+0.00%)</td><td>0.80 (+0.02%)</td><td>0.00 <b>(-79.16%)</b></td><td>94827.90 (-0.02%)</td><td>94789.48 (+0.06%)</td><td>94770.20 (-0.00%)</td><td>94756.80 (+0.34%)</td><td>34.73 <b>(-79.10%)</b></td><td>725.22 (-0.33%)</td><td>724.97 (-0.06%)</td><td>725.12 (+0.00%)</td><td>724.68 (+0.02%)</td><td>0.27 <b>(-79.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94848.90 (n/a)</td><td>94730.38 (n/a)</td><td>94771.20 (n/a)</td><td>94439.70 (n/a)</td><td>166.15 (n/a)</td><td>727.65 (n/a)</td><td>725.42 (n/a)</td><td>725.11 (n/a)</td><td>724.52 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.73 (+0.38%)</td><td>0.73 (+0.12%)</td><td>0.73 (+0.04%)</td><td>0.73 (+0.11%)</td><td>0.00 <b>(+248.68%)</b></td><td>103301.80 (-0.11%)</td><td>103201.70 (-0.12%)</td><td>103272.60 (-0.04%)</td><td>102883.20 (-0.38%)</td><td>178.55 <b>(+246.92%)</b></td><td>667.94 (+0.38%)</td><td>665.88 (+0.12%)</td><td>665.42 (+0.04%)</td><td>665.23 (+0.11%)</td><td>1.15 <b>(+248.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103410.40 (n/a)</td><td>103325.96 (n/a)</td><td>103311.60 (n/a)</td><td>103271.40 (n/a)</td><td>51.47 (n/a)</td><td>665.43 (n/a)</td><td>665.07 (n/a)</td><td>665.17 (n/a)</td><td>664.53 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.68 (-0.84%)</td><td>0.68 (-0.09%)</td><td>0.68 (+0.17%)</td><td>0.68 (+0.06%)</td><td>0.00 <b>(-71.31%)</b></td><td>110738.80 (-0.06%)</td><td>110505.02 (+0.09%)</td><td>110417.10 (-0.17%)</td><td>110342.80 (+0.84%)</td><td>163.90 <b>(-71.06%)</b></td><td>622.78 (-0.84%)</td><td>621.87 (-0.09%)</td><td>622.36 (+0.17%)</td><td>620.55 (+0.06%)</td><td>0.92 <b>(-71.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110807.20 (n/a)</td><td>110408.94 (n/a)</td><td>110601.70 (n/a)</td><td>109419.40 (n/a)</td><td>566.29 (n/a)</td><td>628.04 (n/a)</td><td>622.42 (n/a)</td><td>621.32 (n/a)</td><td>620.17 (n/a)</td><td>3.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.80 (-1.13%)</td><td>2.79 (-0.41%)</td><td>2.79 (-0.15%)</td><td>2.78 (-0.29%)</td><td>0.01 <b>(-61.26%)</b></td><td>37652.70 (+0.29%)</td><td>37563.62 (+0.41%)</td><td>37531.40 (+0.15%)</td><td>37490.00 (+1.15%)</td><td>76.84 <b>(-60.66%)</b></td><td>2864.08 (-1.13%)</td><td>2858.47 (-0.41%)</td><td>2860.91 (-0.15%)</td><td>2851.70 (-0.29%)</td><td>5.84 <b>(-61.26%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.83 (n/a)</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>0.01 (n/a)</td><td>37542.80 (n/a)</td><td>37410.96 (n/a)</td><td>37476.30 (n/a)</td><td>37065.50 (n/a)</td><td>195.35 (n/a)</td><td>2896.87 (n/a)</td><td>2870.19 (n/a)</td><td>2865.12 (n/a)</td><td>2860.05 (n/a)</td><td>15.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.67 (+0.81%)</td><td>7.33 (+2.00%)</td><td>7.36 (+4.97%)</td><td>6.89 (+2.68%)</td><td>0.28 <b>(-29.47%)</b></td><td>1292.70 (-2.61%)</td><td>1217.10 (-2.08%)</td><td>1210.50 (-4.75%)</td><td>1161.60 (-0.79%)</td><td>47.58 <b>(-30.54%)</b></td><td>462.19 (+0.81%)</td><td>441.63 (+2.00%)</td><td>443.50 (+4.97%)</td><td>415.32 (+2.68%)</td><td>16.90 <b>(-29.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>7.61 (n/a)</td><td>7.19 (n/a)</td><td>7.01 (n/a)</td><td>6.71 (n/a)</td><td>0.40 (n/a)</td><td>1327.30 (n/a)</td><td>1242.96 (n/a)</td><td>1270.80 (n/a)</td><td>1170.90 (n/a)</td><td>68.50 (n/a)</td><td>458.50 (n/a)</td><td>432.98 (n/a)</td><td>422.48 (n/a)</td><td>404.47 (n/a)</td><td>23.96 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>6.79 (-0.71%)</td><td>6.52 (+4.84%)</td><td>6.54 (-0.96%)</td><td>6.23 <b>(+36.87%)</b></td><td>0.25 <b>(-74.09%)</b></td><td>1430.70 <b>(-26.94%)</b></td><td>1367.54 (-6.71%)</td><td>1363.30 (+0.97%)</td><td>1312.90 (+0.71%)</td><td>51.76 <b>(-81.33%)</b></td><td>408.91 (-0.71%)</td><td>393.02 (+4.84%)</td><td>393.79 (-0.96%)</td><td>375.25 <b>(+36.87%)</b></td><td>14.82 <b>(-74.09%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.84 (n/a)</td><td>6.22 (n/a)</td><td>6.60 (n/a)</td><td>4.55 (n/a)</td><td>0.95 (n/a)</td><td>1958.20 (n/a)</td><td>1465.96 (n/a)</td><td>1350.20 (n/a)</td><td>1303.60 (n/a)</td><td>277.30 (n/a)</td><td>411.83 (n/a)</td><td>374.87 (n/a)</td><td>397.61 (n/a)</td><td>274.17 (n/a)</td><td>57.19 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.15 (+6.28%)</td><td>6.34 (+1.97%)</td><td>6.53 (-1.44%)</td><td>4.77 (+0.77%)</td><td>0.92 (+8.55%)</td><td>1868.60 (-0.77%)</td><td>1433.90 (-1.72%)</td><td>1365.10 (+1.46%)</td><td>1247.10 (-5.91%)</td><td>248.50 (+3.72%)</td><td>430.50 (+6.28%)</td><td>382.06 (+1.97%)</td><td>393.29 (-1.44%)</td><td>287.31 (+0.77%)</td><td>55.40 (+8.55%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.72 (n/a)</td><td>6.22 (n/a)</td><td>6.62 (n/a)</td><td>4.73 (n/a)</td><td>0.85 (n/a)</td><td>1883.10 (n/a)</td><td>1458.94 (n/a)</td><td>1345.50 (n/a)</td><td>1325.40 (n/a)</td><td>239.59 (n/a)</td><td>405.07 (n/a)</td><td>374.69 (n/a)</td><td>399.02 (n/a)</td><td>285.11 (n/a)</td><td>51.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>8.11 (+0.07%)</td><td>7.99 (+4.01%)</td><td>7.99 (+0.51%)</td><td>7.92 (+11.31%)</td><td>0.07 <b>(-83.34%)</b></td><td>4399.90 (-10.16%)</td><td>4362.74 (-4.11%)</td><td>4365.90 (-0.50%)</td><td>4301.10 (-0.07%)</td><td>39.76 <b>(-85.06%)</b></td><td>499.28 (+0.07%)</td><td>492.26 (+4.01%)</td><td>491.88 (+0.51%)</td><td>488.08 (+11.31%)</td><td>4.51 <b>(-83.34%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>8.10 (n/a)</td><td>7.68 (n/a)</td><td>7.95 (n/a)</td><td>7.12 (n/a)</td><td>0.44 (n/a)</td><td>4897.70 (n/a)</td><td>4549.60 (n/a)</td><td>4388.00 (n/a)</td><td>4304.30 (n/a)</td><td>266.09 (n/a)</td><td>498.92 (n/a)</td><td>473.28 (n/a)</td><td>489.40 (n/a)</td><td>438.47 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.79 (+2.68%)</td><td>7.58 (+4.30%)</td><td>7.74 (+7.34%)</td><td>7.04 (+0.85%)</td><td>0.31 <b>(+22.81%)</b></td><td>4950.20 (-0.85%)</td><td>4604.64 (-4.08%)</td><td>4506.90 (-6.83%)</td><td>4476.10 (-2.61%)</td><td>200.04 (+19.10%)</td><td>479.77 (+2.68%)</td><td>467.05 (+4.30%)</td><td>476.49 (+7.34%)</td><td>433.81 (+0.85%)</td><td>19.35 <b>(+22.81%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>7.59 (n/a)</td><td>7.27 (n/a)</td><td>7.21 (n/a)</td><td>6.98 (n/a)</td><td>0.26 (n/a)</td><td>4992.50 (n/a)</td><td>4800.40 (n/a)</td><td>4837.50 (n/a)</td><td>4596.20 (n/a)</td><td>167.97 (n/a)</td><td>467.23 (n/a)</td><td>447.80 (n/a)</td><td>443.92 (n/a)</td><td>430.14 (n/a)</td><td>15.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.51 (-0.34%)</td><td>7.23 (-1.60%)</td><td>7.31 (-0.56%)</td><td>6.81 (-5.53%)</td><td>0.27 <b>(+122.33%)</b></td><td>5118.80 (+5.85%)</td><td>4827.90 (+1.72%)</td><td>4767.20 (+0.56%)</td><td>4644.40 (+0.34%)</td><td>186.37 <b>(+137.11%)</b></td><td>462.39 (-0.34%)</td><td>445.33 (-1.60%)</td><td>450.47 (-0.56%)</td><td>419.53 (-5.53%)</td><td>16.79 <b>(+122.33%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>7.53 (n/a)</td><td>7.35 (n/a)</td><td>7.35 (n/a)</td><td>7.21 (n/a)</td><td>0.12 (n/a)</td><td>4836.00 (n/a)</td><td>4746.10 (n/a)</td><td>4740.60 (n/a)</td><td>4628.50 (n/a)</td><td>78.60 (n/a)</td><td>463.97 (n/a)</td><td>452.57 (n/a)</td><td>452.99 (n/a)</td><td>444.06 (n/a)</td><td>7.55 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 (-0.02%)</td><td>0.80 (-0.02%)</td><td>0.80 (-0.00%)</td><td>0.80 (-0.07%)</td><td>0.00 <b>(+27.30%)</b></td><td>94272.40 (+0.07%)</td><td>94105.52 (+0.02%)</td><td>94069.10 (+0.00%)</td><td>94038.90 (+0.02%)</td><td>95.10 <b>(+27.42%)</b></td><td>730.76 (-0.02%)</td><td>730.24 (-0.02%)</td><td>730.52 (-0.00%)</td><td>728.95 (-0.07%)</td><td>0.74 <b>(+27.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94202.40 (n/a)</td><td>94083.42 (n/a)</td><td>94069.10 (n/a)</td><td>94018.20 (n/a)</td><td>74.63 (n/a)</td><td>730.92 (n/a)</td><td>730.41 (n/a)</td><td>730.52 (n/a)</td><td>729.49 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.74 (+0.01%)</td><td>0.74 (-0.00%)</td><td>0.74 (+0.00%)</td><td>0.74 (-0.04%)</td><td>0.00 <b>(+132.27%)</b></td><td>102636.90 (+0.04%)</td><td>102587.46 (+0.00%)</td><td>102587.70 (-0.00%)</td><td>102549.70 (-0.01%)</td><td>37.53 <b>(+132.02%)</b></td><td>670.11 (+0.01%)</td><td>669.86 (-0.00%)</td><td>669.86 (+0.00%)</td><td>669.54 (-0.04%)</td><td>0.25 <b>(+132.24%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102599.80 (n/a)</td><td>102585.36 (n/a)</td><td>102591.10 (n/a)</td><td>102558.20 (n/a)</td><td>16.18 (n/a)</td><td>670.05 (n/a)</td><td>669.88 (n/a)</td><td>669.84 (n/a)</td><td>669.78 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.71 (-0.10%)</td><td>0.71 (-0.13%)</td><td>0.71 (-0.18%)</td><td>0.71 (-0.13%)</td><td>0.00 (+19.17%)</td><td>106028.50 (+0.13%)</td><td>105947.80 (+0.13%)</td><td>105963.00 (+0.18%)</td><td>105870.10 (+0.10%)</td><td>71.35 (+19.41%)</td><td>649.09 (-0.10%)</td><td>648.62 (-0.13%)</td><td>648.52 (-0.18%)</td><td>648.12 (-0.13%)</td><td>0.44 (+19.17%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>105893.10 (n/a)</td><td>105812.30 (n/a)</td><td>105777.10 (n/a)</td><td>105765.70 (n/a)</td><td>59.76 (n/a)</td><td>649.73 (n/a)</td><td>649.45 (n/a)</td><td>649.66 (n/a)</td><td>648.95 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.29 <b>(+21.86%)</b></td><td>3.59 (+15.59%)</td><td>3.65 (+18.10%)</td><td>3.03 (+6.39%)</td><td>0.52 <b>(+101.11%)</b></td><td>2663.00 (-6.00%)</td><td>2285.68 (-12.48%)</td><td>2207.00 (-15.33%)</td><td>1877.20 (-17.94%)</td><td>330.47 <b>(+59.34%)</b></td><td>1126.11 <b>(+21.86%)</b></td><td>940.66 (+15.59%)</td><td>957.85 (+18.10%)</td><td>793.82 (+6.39%)</td><td>137.25 <b>(+101.12%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>3.52 (n/a)</td><td>3.10 (n/a)</td><td>3.09 (n/a)</td><td>2.85 (n/a)</td><td>0.26 (n/a)</td><td>2833.00 (n/a)</td><td>2611.50 (n/a)</td><td>2606.50 (n/a)</td><td>2287.50 (n/a)</td><td>207.40 (n/a)</td><td>924.10 (n/a)</td><td>813.79 (n/a)</td><td>811.04 (n/a)</td><td>746.17 (n/a)</td><td>68.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.41 (+13.60%)</td><td>0.35 (+4.75%)</td><td>0.34 (-1.52%)</td><td>0.31 (+6.09%)</td><td>0.04 <b>(+27.96%)</b></td><td>4065.60 (-5.74%)</td><td>3638.26 (-4.29%)</td><td>3686.50 (+1.55%)</td><td>3004.70 (-11.98%)</td><td>399.69 (+3.81%)</td><td>22.33 (+13.60%)</td><td>18.64 (+4.75%)</td><td>18.20 (-1.52%)</td><td>16.51 (+6.09%)</td><td>2.23 <b>(+27.96%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.03 (n/a)</td><td>4313.30 (n/a)</td><td>3801.46 (n/a)</td><td>3630.40 (n/a)</td><td>3413.50 (n/a)</td><td>385.02 (n/a)</td><td>19.66 (n/a)</td><td>17.79 (n/a)</td><td>18.49 (n/a)</td><td>15.56 (n/a)</td><td>1.75 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>6.87 (+11.81%)</td><td>4.92 (+1.45%)</td><td>4.83 (+0.84%)</td><td>3.24 (-9.24%)</td><td>1.29 (+3.14%)</td><td>2051.10 (+10.17%)</td><td>1429.70 (-1.26%)</td><td>1377.90 (-0.83%)</td><td>967.70 (-10.56%)</td><td>389.97 (+3.36%)</td><td>2123.91 (+11.81%)</td><td>1521.03 (+1.45%)</td><td>1491.60 (+0.84%)</td><td>1001.99 (-9.24%)</td><td>398.59 (+3.14%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.15 (n/a)</td><td>4.85 (n/a)</td><td>4.79 (n/a)</td><td>3.57 (n/a)</td><td>1.25 (n/a)</td><td>1861.70 (n/a)</td><td>1448.00 (n/a)</td><td>1389.50 (n/a)</td><td>1081.90 (n/a)</td><td>377.28 (n/a)</td><td>1899.61 (n/a)</td><td>1499.34 (n/a)</td><td>1479.14 (n/a)</td><td>1103.96 (n/a)</td><td>386.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>13.20 (n/a)</td><td>12.55 (n/a)</td><td>12.26 (n/a)</td><td>11.89 (n/a)</td><td>0.60 (n/a)</td><td>13.19 (n/a)</td><td>12.54 (n/a)</td><td>12.26 (n/a)</td><td>11.89 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>25.13 (+3.21%)</td><td>24.43 (+3.13%)</td><td>24.64 (+2.14%)</td><td>23.30 (+6.21%)</td><td>0.71 <b>(-28.77%)</b></td><td>25.11 (+3.21%)</td><td>24.41 (+3.13%)</td><td>24.62 (+2.14%)</td><td>23.29 (+6.21%)</td><td>0.71 <b>(-28.77%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>24.34 (n/a)</td><td>23.69 (n/a)</td><td>24.12 (n/a)</td><td>21.94 (n/a)</td><td>0.99 (n/a)</td><td>24.33 (n/a)</td><td>23.67 (n/a)</td><td>24.11 (n/a)</td><td>21.93 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>42.40 (+2.74%)</td><td>39.91 (+0.31%)</td><td>39.26 (-0.78%)</td><td>37.77 (-2.94%)</td><td>1.81 <b>(+106.45%)</b></td><td>42.37 (+2.74%)</td><td>39.88 (+0.31%)</td><td>39.24 (-0.78%)</td><td>37.74 (-2.94%)</td><td>1.81 <b>(+106.45%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>41.26 (n/a)</td><td>39.78 (n/a)</td><td>39.57 (n/a)</td><td>38.91 (n/a)</td><td>0.88 (n/a)</td><td>41.24 (n/a)</td><td>39.76 (n/a)</td><td>39.55 (n/a)</td><td>38.88 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>45.03 (-0.77%)</td><td>43.10 (-0.75%)</td><td>42.89 (-1.00%)</td><td>40.60 (-3.79%)</td><td>1.90 <b>(+56.52%)</b></td><td>45.00 (-0.77%)</td><td>43.07 (-0.75%)</td><td>42.86 (-1.00%)</td><td>40.58 (-3.79%)</td><td>1.89 <b>(+56.52%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>45.38 (n/a)</td><td>43.42 (n/a)</td><td>43.32 (n/a)</td><td>42.20 (n/a)</td><td>1.21 (n/a)</td><td>45.35 (n/a)</td><td>43.40 (n/a)</td><td>43.29 (n/a)</td><td>42.18 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>13.18 (n/a)</td><td>12.67 (n/a)</td><td>13.07 (n/a)</td><td>11.77 (n/a)</td><td>0.65 (n/a)</td><td>13.18 (n/a)</td><td>12.67 (n/a)</td><td>13.07 (n/a)</td><td>11.76 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>24.26 (-2.65%)</td><td>23.84 (-2.68%)</td><td>23.75 (-3.84%)</td><td>23.43 (-1.33%)</td><td>0.40 (-13.98%)</td><td>24.25 (-2.65%)</td><td>23.82 (-2.68%)</td><td>23.73 (-3.84%)</td><td>23.42 (-1.33%)</td><td>0.40 (-13.98%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>24.92 (n/a)</td><td>24.49 (n/a)</td><td>24.70 (n/a)</td><td>23.75 (n/a)</td><td>0.47 (n/a)</td><td>24.91 (n/a)</td><td>24.48 (n/a)</td><td>24.68 (n/a)</td><td>23.73 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>39.76 (-4.66%)</td><td>38.59 (-3.72%)</td><td>38.65 (-3.08%)</td><td>37.46 (-3.30%)</td><td>0.91 (-17.91%)</td><td>39.74 (-4.66%)</td><td>38.57 (-3.72%)</td><td>38.63 (-3.08%)</td><td>37.44 (-3.30%)</td><td>0.91 (-17.91%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>41.71 (n/a)</td><td>40.08 (n/a)</td><td>39.88 (n/a)</td><td>38.74 (n/a)</td><td>1.11 (n/a)</td><td>41.68 (n/a)</td><td>40.06 (n/a)</td><td>39.85 (n/a)</td><td>38.71 (n/a)</td><td>1.11 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>44.76 (-0.88%)</td><td>41.71 (-2.89%)</td><td>40.46 (-7.01%)</td><td>39.96 (+5.61%)</td><td>2.10 <b>(-28.78%)</b></td><td>44.74 (-0.88%)</td><td>41.68 (-2.89%)</td><td>40.44 (-7.01%)</td><td>39.94 (+5.61%)</td><td>2.10 <b>(-28.77%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>45.16 (n/a)</td><td>42.95 (n/a)</td><td>43.51 (n/a)</td><td>37.84 (n/a)</td><td>2.95 (n/a)</td><td>45.13 (n/a)</td><td>42.92 (n/a)</td><td>43.48 (n/a)</td><td>37.82 (n/a)</td><td>2.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>8.71 (-6.64%)</td><td>8.39 (-3.14%)</td><td>8.57 (-1.89%)</td><td>7.65 (-4.96%)</td><td>0.43 (-11.42%)</td><td>8.69 (-6.64%)</td><td>8.37 (-3.14%)</td><td>8.55 (-1.89%)</td><td>7.63 (-4.96%)</td><td>0.43 (-11.42%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>9.33 (n/a)</td><td>8.66 (n/a)</td><td>8.74 (n/a)</td><td>8.05 (n/a)</td><td>0.48 (n/a)</td><td>9.31 (n/a)</td><td>8.65 (n/a)</td><td>8.72 (n/a)</td><td>8.03 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.06 (+3.30%)</td><td>0.91 (+1.75%)</td><td>0.89 (-2.47%)</td><td>0.81 (+15.63%)</td><td>0.10 <b>(-26.14%)</b></td><td>1.05 (+3.30%)</td><td>0.90 (+1.75%)</td><td>0.88 (-2.47%)</td><td>0.80 (+15.63%)</td><td>0.10 <b>(-26.14%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.03 (n/a)</td><td>0.90 (n/a)</td><td>0.91 (n/a)</td><td>0.70 (n/a)</td><td>0.14 (n/a)</td><td>1.01 (n/a)</td><td>0.88 (n/a)</td><td>0.90 (n/a)</td><td>0.69 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.31 (+1.00%)</td><td>1.10 (-5.68%)</td><td>1.10 (-1.56%)</td><td>0.89 (-17.17%)</td><td>0.15 <b>(+44.70%)</b></td><td>1.29 (+1.00%)</td><td>1.09 (-5.68%)</td><td>1.09 (-1.56%)</td><td>0.88 (-17.17%)</td><td>0.15 <b>(+44.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.29 (n/a)</td><td>1.17 (n/a)</td><td>1.12 (n/a)</td><td>1.08 (n/a)</td><td>0.10 (n/a)</td><td>1.28 (n/a)</td><td>1.15 (n/a)</td><td>1.10 (n/a)</td><td>1.07 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>18.46 (+4.74%)</td><td>15.82 (-7.01%)</td><td>15.96 (-6.38%)</td><td>13.36 (-17.68%)</td><td>2.09 <b>(+262.05%)</b></td><td>18.25 (+4.74%)</td><td>15.63 (-7.01%)</td><td>15.77 (-6.38%)</td><td>13.21 (-17.68%)</td><td>2.07 <b>(+262.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>17.62 (n/a)</td><td>17.01 (n/a)</td><td>17.04 (n/a)</td><td>16.23 (n/a)</td><td>0.58 (n/a)</td><td>17.42 (n/a)</td><td>16.81 (n/a)</td><td>16.85 (n/a)</td><td>16.05 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>12.99 (-6.83%)</td><td>12.52 (-3.80%)</td><td>12.73 (-1.99%)</td><td>11.47 (-5.56%)</td><td>0.60 (-17.95%)</td><td>12.76 (-6.83%)</td><td>12.30 (-3.80%)</td><td>12.50 (-1.99%)</td><td>11.27 (-5.56%)</td><td>0.59 (-17.95%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>13.94 (n/a)</td><td>13.01 (n/a)</td><td>12.98 (n/a)</td><td>12.15 (n/a)</td><td>0.73 (n/a)</td><td>13.69 (n/a)</td><td>12.78 (n/a)</td><td>12.76 (n/a)</td><td>11.93 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>7.69 (-13.73%)</td><td>6.61 (-14.30%)</td><td>6.79 (-12.42%)</td><td>5.16 <b>(-23.20%)</b></td><td>1.00 <b>(+23.49%)</b></td><td>7.56 (-13.73%)</td><td>6.49 (-14.30%)</td><td>6.68 (-12.42%)</td><td>5.07 <b>(-23.20%)</b></td><td>0.99 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>8.91 (n/a)</td><td>7.71 (n/a)</td><td>7.76 (n/a)</td><td>6.71 (n/a)</td><td>0.81 (n/a)</td><td>8.76 (n/a)</td><td>7.58 (n/a)</td><td>7.62 (n/a)</td><td>6.60 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>6.57 (+4.72%)</td><td>5.58 (+1.79%)</td><td>5.67 (+3.57%)</td><td>3.81 (-15.48%)</td><td>1.12 <b>(+72.07%)</b></td><td>6.47 (+4.72%)</td><td>5.49 (+1.79%)</td><td>5.58 (+3.57%)</td><td>3.75 (-15.48%)</td><td>1.10 <b>(+72.07%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>6.28 (n/a)</td><td>5.48 (n/a)</td><td>5.48 (n/a)</td><td>4.51 (n/a)</td><td>0.65 (n/a)</td><td>6.18 (n/a)</td><td>5.39 (n/a)</td><td>5.39 (n/a)</td><td>4.44 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>13.50 (n/a)</td><td>12.85 (n/a)</td><td>13.30 (n/a)</td><td>10.84 (n/a)</td><td>1.13 (n/a)</td><td>13.49 (n/a)</td><td>12.84 (n/a)</td><td>13.29 (n/a)</td><td>10.84 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>13.24 (n/a)</td><td>12.45 (n/a)</td><td>13.02 (n/a)</td><td>10.34 (n/a)</td><td>1.22 (n/a)</td><td>13.23 (n/a)</td><td>12.44 (n/a)</td><td>13.01 (n/a)</td><td>10.33 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.50 (n/a)</td><td>156.86 (n/a)</td><td>168.90 (n/a)</td><td>129.60 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.20 (n/a)</td><td>159.54 (n/a)</td><td>157.80 (n/a)</td><td>126.90 (n/a)</td><td>28.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.00 (n/a)</td><td>180.74 (n/a)</td><td>181.80 (n/a)</td><td>163.70 (n/a)</td><td>14.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.90 (n/a)</td><td>187.50 (n/a)</td><td>190.50 (n/a)</td><td>154.30 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>352.00 (n/a)</td><td>224.24 (n/a)</td><td>212.30 (n/a)</td><td>127.80 (n/a)</td><td>82.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>185.54 (n/a)</td><td>189.40 (n/a)</td><td>145.40 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>174.94 (n/a)</td><td>192.60 (n/a)</td><td>111.40 (n/a)</td><td>37.40 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>336.80 (n/a)</td><td>220.56 (n/a)</td><td>183.60 (n/a)</td><td>165.40 (n/a)</td><td>70.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>163.40 (n/a)</td><td>154.50 (n/a)</td><td>127.90 (n/a)</td><td>35.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.20 (n/a)</td><td>186.36 (n/a)</td><td>188.10 (n/a)</td><td>136.50 (n/a)</td><td>39.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.50 (n/a)</td><td>193.60 (n/a)</td><td>215.20 (n/a)</td><td>125.00 (n/a)</td><td>55.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>157.68 (n/a)</td><td>144.50 (n/a)</td><td>133.60 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>160.38 (n/a)</td><td>164.80 (n/a)</td><td>135.40 (n/a)</td><td>19.35 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>169.50 (n/a)</td><td>169.50 (n/a)</td><td>129.10 (n/a)</td><td>35.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.40 (n/a)</td><td>189.18 (n/a)</td><td>190.30 (n/a)</td><td>129.90 (n/a)</td><td>36.62 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.70 (n/a)</td><td>200.40 (n/a)</td><td>202.90 (n/a)</td><td>174.50 (n/a)</td><td>17.28 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.20 (n/a)</td><td>168.70 (n/a)</td><td>169.40 (n/a)</td><td>138.00 (n/a)</td><td>30.47 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>192.90 (n/a)</td><td>153.40 (n/a)</td><td>140.70 (n/a)</td><td>116.50 (n/a)</td><td>34.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.40 (n/a)</td><td>166.24 (n/a)</td><td>151.30 (n/a)</td><td>133.80 (n/a)</td><td>31.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>211.90 (n/a)</td><td>155.36 (n/a)</td><td>139.10 (n/a)</td><td>109.10 (n/a)</td><td>44.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.20 (n/a)</td><td>157.58 (n/a)</td><td>148.80 (n/a)</td><td>123.50 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>179.26 (n/a)</td><td>179.00 (n/a)</td><td>156.30 (n/a)</td><td>22.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.50 (n/a)</td><td>186.40 (n/a)</td><td>173.00 (n/a)</td><td>154.40 (n/a)</td><td>30.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>256.50 (n/a)</td><td>213.46 (n/a)</td><td>203.30 (n/a)</td><td>186.50 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>179.80 (n/a)</td><td>179.50 (n/a)</td><td>170.00 (n/a)</td><td>9.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.70 (n/a)</td><td>164.58 (n/a)</td><td>156.20 (n/a)</td><td>135.30 (n/a)</td><td>24.96 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>205.20 (n/a)</td><td>160.14 (n/a)</td><td>150.40 (n/a)</td><td>132.00 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.20 (n/a)</td><td>166.56 (n/a)</td><td>162.00 (n/a)</td><td>127.30 (n/a)</td><td>34.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>195.10 (n/a)</td><td>169.46 (n/a)</td><td>170.80 (n/a)</td><td>123.70 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.30 (n/a)</td><td>173.20 (n/a)</td><td>168.60 (n/a)</td><td>130.60 (n/a)</td><td>29.53 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>200.46 (n/a)</td><td>203.10 (n/a)</td><td>182.00 (n/a)</td><td>10.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>222.10 (n/a)</td><td>201.60 (n/a)</td><td>207.10 (n/a)</td><td>163.20 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-6.60%)</td><td>0.03 (+10.50%)</td><td>0.03 <b>(+27.10%)</b></td><td>0.02 (+1.18%)</td><td>0.00 <b>(-23.38%)</b></td><td>221.60 (-1.16%)</td><td>168.10 (-10.68%)</td><td>160.30 <b>(-21.31%)</b></td><td>137.60 (+7.08%)</td><td>32.12 (-14.26%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>188.20 (n/a)</td><td>203.70 (n/a)</td><td>128.50 (n/a)</td><td>37.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 <b>(-25.60%)</b></td><td>0.03 (-4.35%)</td><td>0.03 (+12.10%)</td><td>0.02 (+15.33%)</td><td>0.00 <b>(-63.64%)</b></td><td>195.50 (-13.30%)</td><td>161.90 (-1.87%)</td><td>159.10 (-10.77%)</td><td>142.20 <b>(+34.40%)</b></td><td>21.05 <b>(-56.55%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>164.98 (n/a)</td><td>178.30 (n/a)</td><td>105.80 (n/a)</td><td>48.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+3.79%)</td><td>0.02 (-6.29%)</td><td>0.02 (-13.06%)</td><td>0.02 (-10.46%)</td><td>0.00 <b>(+102.05%)</b></td><td>209.20 (+11.69%)</td><td>180.06 (+8.51%)</td><td>190.20 (+15.06%)</td><td>146.90 (-3.61%)</td><td>28.77 <b>(+113.65%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.30 (n/a)</td><td>165.94 (n/a)</td><td>165.30 (n/a)</td><td>152.40 (n/a)</td><td>13.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+5.77%)</td><td>0.02 (-12.55%)</td><td>0.02 (-19.66%)</td><td>0.02 <b>(-24.95%)</b></td><td>0.01 <b>(+77.90%)</b></td><td>240.70 <b>(+33.28%)</b></td><td>185.64 (+19.20%)</td><td>194.10 <b>(+24.42%)</b></td><td>117.80 (-5.46%)</td><td>44.97 <b>(+118.51%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.60 (n/a)</td><td>155.74 (n/a)</td><td>156.00 (n/a)</td><td>124.60 (n/a)</td><td>20.58 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-1.54%)</td><td>0.02 (-7.60%)</td><td>0.02 (+0.78%)</td><td>0.02 (-17.05%)</td><td>0.00 (+13.58%)</td><td>225.50 <b>(+20.59%)</b></td><td>175.32 (+9.44%)</td><td>170.20 (-0.76%)</td><td>131.00 (+1.55%)</td><td>34.39 <b>(+40.28%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.00 (n/a)</td><td>160.20 (n/a)</td><td>171.50 (n/a)</td><td>129.00 (n/a)</td><td>24.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+17.33%)</td><td>0.02 (+5.99%)</td><td>0.02 (-6.98%)</td><td>0.02 <b>(+25.16%)</b></td><td>0.00 (+12.30%)</td><td>190.10 <b>(-20.09%)</b></td><td>170.76 (-6.09%)</td><td>179.00 (+7.51%)</td><td>126.40 (-14.77%)</td><td>25.26 <b>(-27.51%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.90 (n/a)</td><td>181.84 (n/a)</td><td>166.50 (n/a)</td><td>148.30 (n/a)</td><td>34.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-1.22%)</td><td>0.02 (-7.31%)</td><td>0.02 (-15.22%)</td><td>0.02 (-15.24%)</td><td>0.01 <b>(+33.64%)</b></td><td>226.80 (+18.00%)</td><td>187.88 (+10.83%)</td><td>206.90 (+17.96%)</td><td>127.50 (+1.27%)</td><td>43.44 <b>(+65.40%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.20 (n/a)</td><td>169.52 (n/a)</td><td>175.40 (n/a)</td><td>125.90 (n/a)</td><td>26.26 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (-14.48%)</td><td>0.02 (-1.29%)</td><td>0.02 (+12.74%)</td><td>0.02 (-3.07%)</td><td>0.00 <b>(-31.67%)</b></td><td>233.90 (+3.18%)</td><td>201.72 (+0.35%)</td><td>189.90 (-11.30%)</td><td>176.40 (+16.98%)</td><td>26.07 (-16.26%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.70 (n/a)</td><td>201.02 (n/a)</td><td>214.10 (n/a)</td><td>150.80 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (+11.84%)</td><td>0.05 (-9.76%)</td><td>0.05 (-15.97%)</td><td>0.04 (-4.89%)</td><td>0.01 <b>(+53.12%)</b></td><td>201.10 (+5.18%)</td><td>172.18 (+13.25%)</td><td>181.20 (+19.05%)</td><td>115.30 (-10.62%)</td><td>34.55 <b>(+40.88%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>152.04 (n/a)</td><td>152.20 (n/a)</td><td>129.00 (n/a)</td><td>24.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-13.76%)</td><td>0.05 (-10.00%)</td><td>0.05 (-4.97%)</td><td>0.04 (-14.20%)</td><td>0.01 (+6.71%)</td><td>203.00 (+16.53%)</td><td>171.98 (+11.66%)</td><td>164.80 (+5.24%)</td><td>151.10 (+15.96%)</td><td>23.24 <b>(+44.17%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.20 (n/a)</td><td>154.02 (n/a)</td><td>156.60 (n/a)</td><td>130.30 (n/a)</td><td>16.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (+8.68%)</td><td>0.05 (-15.14%)</td><td>0.04 <b>(-28.64%)</b></td><td>0.03 (-19.38%)</td><td>0.01 <b>(+53.81%)</b></td><td>254.80 <b>(+24.05%)</b></td><td>191.74 <b>(+22.74%)</b></td><td>204.50 <b>(+40.07%)</b></td><td>115.80 (-7.95%)</td><td>50.97 <b>(+64.48%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>156.22 (n/a)</td><td>146.00 (n/a)</td><td>125.80 (n/a)</td><td>30.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 <b>(+29.13%)</b></td><td>0.05 (-2.28%)</td><td>0.04 <b>(-23.00%)</b></td><td>0.04 <b>(-25.61%)</b></td><td>0.02 <b>(+254.91%)</b></td><td>226.60 <b>(+34.48%)</b></td><td>169.76 (+12.95%)</td><td>186.80 <b>(+29.81%)</b></td><td>102.30 <b>(-22.62%)</b></td><td>57.76 <b>(+264.36%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.50 (n/a)</td><td>150.30 (n/a)</td><td>143.90 (n/a)</td><td>132.20 (n/a)</td><td>15.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (+14.43%)</td><td>0.05 (-11.45%)</td><td>0.04 (-18.78%)</td><td>0.04 <b>(-24.59%)</b></td><td>0.01 <b>(+184.61%)</b></td><td>219.40 <b>(+32.57%)</b></td><td>177.56 (+18.64%)</td><td>189.80 <b>(+23.09%)</b></td><td>115.80 (-12.67%)</td><td>43.05 <b>(+232.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>165.50 (n/a)</td><td>149.66 (n/a)</td><td>154.20 (n/a)</td><td>132.60 (n/a)</td><td>12.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (+1.69%)</td><td>0.05 (-7.17%)</td><td>0.05 (-4.46%)</td><td>0.04 <b>(-20.09%)</b></td><td>0.01 <b>(+48.04%)</b></td><td>211.60 <b>(+25.13%)</b></td><td>164.56 (+10.07%)</td><td>161.40 (+4.67%)</td><td>118.10 (-1.67%)</td><td>33.33 <b>(+83.38%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.10 (n/a)</td><td>149.50 (n/a)</td><td>154.20 (n/a)</td><td>120.10 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (+11.12%)</td><td>0.05 (+1.93%)</td><td>0.04 (-0.16%)</td><td>0.04 (+18.00%)</td><td>0.01 (+9.00%)</td><td>204.60 (-15.24%)</td><td>178.84 (-2.24%)</td><td>188.30 (+0.16%)</td><td>124.20 (-10.00%)</td><td>32.29 (-18.54%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.40 (n/a)</td><td>182.94 (n/a)</td><td>188.00 (n/a)</td><td>138.00 (n/a)</td><td>39.65 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-8.63%)</td><td>0.04 (-11.40%)</td><td>0.04 (-12.69%)</td><td>0.03 (-6.45%)</td><td>0.01 (+0.34%)</td><td>235.20 (+6.91%)</td><td>204.80 (+13.17%)</td><td>204.80 (+14.48%)</td><td>168.20 (+9.43%)</td><td>29.85 (+18.56%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>180.96 (n/a)</td><td>178.90 (n/a)</td><td>153.70 (n/a)</td><td>25.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-16.62%)</td><td>0.04 (-8.21%)</td><td>0.04 (-16.19%)</td><td>0.03 <b>(+26.51%)</b></td><td>0.01 <b>(-43.84%)</b></td><td>241.40 <b>(-20.96%)</b></td><td>203.12 (+3.04%)</td><td>202.90 (+19.28%)</td><td>156.80 (+19.97%)</td><td>34.89 <b>(-47.97%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>305.40 (n/a)</td><td>197.12 (n/a)</td><td>170.10 (n/a)</td><td>130.70 (n/a)</td><td>67.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 <b>(+64.29%)</b></td><td>0.05 <b>(+42.97%)</b></td><td>0.04 (+16.53%)</td><td>0.04 <b>(+45.55%)</b></td><td>0.01 <b>(+103.57%)</b></td><td>224.80 <b>(-31.30%)</b></td><td>192.86 <b>(-28.14%)</b></td><td>220.30 (-14.18%)</td><td>115.00 <b>(-39.12%)</b></td><td>46.94 (-15.78%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>327.20 (n/a)</td><td>268.38 (n/a)</td><td>256.70 (n/a)</td><td>188.90 (n/a)</td><td>55.74 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 <b>(+35.65%)</b></td><td>0.10 (+15.09%)</td><td>0.10 (+16.27%)</td><td>0.07 (-13.61%)</td><td>0.02 <b>(+282.80%)</b></td><td>234.80 (+15.72%)</td><td>174.18 (-9.36%)</td><td>170.50 (-14.02%)</td><td>126.20 <b>(-26.24%)</b></td><td>42.15 <b>(+227.52%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>192.16 (n/a)</td><td>198.30 (n/a)</td><td>171.10 (n/a)</td><td>12.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (+0.83%)</td><td>0.11 (+2.02%)</td><td>0.10 (+3.15%)</td><td>0.09 (+4.83%)</td><td>0.02 (-12.30%)</td><td>180.70 (-4.64%)</td><td>156.68 (-2.63%)</td><td>157.60 (-3.02%)</td><td>123.70 (-0.80%)</td><td>21.65 (-18.94%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.50 (n/a)</td><td>160.92 (n/a)</td><td>162.50 (n/a)</td><td>124.70 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 <b>(-21.22%)</b></td><td>0.10 (+8.41%)</td><td>0.11 (+17.36%)</td><td>0.10 <b>(+49.81%)</b></td><td>0.01 <b>(-80.99%)</b></td><td>166.00 <b>(-33.25%)</b></td><td>156.82 (-12.93%)</td><td>153.70 (-14.80%)</td><td>148.30 <b>(+26.86%)</b></td><td>7.87 <b>(-83.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>248.70 (n/a)</td><td>180.10 (n/a)</td><td>180.40 (n/a)</td><td>116.90 (n/a)</td><td>47.58 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 <b>(+27.54%)</b></td><td>0.10 (+14.60%)</td><td>0.09 (+10.93%)</td><td>0.07 <b>(+24.05%)</b></td><td>0.03 <b>(+39.21%)</b></td><td>235.50 (-19.40%)</td><td>180.42 (-12.14%)</td><td>175.40 (-9.82%)</td><td>116.80 <b>(-21.61%)</b></td><td>43.44 (-17.82%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>292.20 (n/a)</td><td>205.36 (n/a)</td><td>194.50 (n/a)</td><td>149.00 (n/a)</td><td>52.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 <b>(-24.12%)</b></td><td>0.10 (-3.44%)</td><td>0.10 (+11.84%)</td><td>0.09 (+12.08%)</td><td>0.01 <b>(-64.48%)</b></td><td>192.70 (-10.75%)</td><td>173.08 (-0.53%)</td><td>164.80 (-10.58%)</td><td>158.50 <b>(+31.75%)</b></td><td>16.79 <b>(-58.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>215.90 (n/a)</td><td>174.00 (n/a)</td><td>184.30 (n/a)</td><td>120.30 (n/a)</td><td>40.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (-4.22%)</td><td>0.09 (-8.24%)</td><td>0.08 (-9.75%)</td><td>0.07 (-11.17%)</td><td>0.02 (+7.10%)</td><td>232.80 (+12.57%)</td><td>184.98 (+9.98%)</td><td>197.30 (+10.78%)</td><td>137.80 (+4.39%)</td><td>38.38 <b>(+26.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.80 (n/a)</td><td>168.20 (n/a)</td><td>178.10 (n/a)</td><td>132.00 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 <b>(+32.16%)</b></td><td>0.10 (+12.33%)</td><td>0.09 (-7.69%)</td><td>0.08 <b>(+33.46%)</b></td><td>0.03 <b>(+40.90%)</b></td><td>208.60 <b>(-25.07%)</b></td><td>176.46 (-10.68%)</td><td>190.70 (+8.35%)</td><td>115.10 <b>(-24.38%)</b></td><td>37.75 <b>(-23.71%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>278.40 (n/a)</td><td>197.56 (n/a)</td><td>176.00 (n/a)</td><td>152.20 (n/a)</td><td>49.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (-5.38%)</td><td>0.08 (-9.46%)</td><td>0.07 <b>(-20.09%)</b></td><td>0.07 (-4.53%)</td><td>0.01 (+5.30%)</td><td>240.30 (+4.75%)</td><td>214.36 (+10.95%)</td><td>237.40 <b>(+25.14%)</b></td><td>172.30 (+5.71%)</td><td>34.03 (+18.97%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>193.20 (n/a)</td><td>189.70 (n/a)</td><td>163.00 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (-15.28%)</td><td>0.20 (-5.08%)</td><td>0.20 (+3.09%)</td><td>0.17 (-6.54%)</td><td>0.02 <b>(-39.55%)</b></td><td>192.80 (+6.99%)</td><td>168.46 (+4.27%)</td><td>165.20 (-2.99%)</td><td>146.70 (+18.02%)</td><td>17.84 <b>(-23.30%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>180.20 (n/a)</td><td>161.56 (n/a)</td><td>170.30 (n/a)</td><td>124.30 (n/a)</td><td>23.26 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (-15.37%)</td><td>0.20 (-4.28%)</td><td>0.20 (-0.79%)</td><td>0.18 (+2.98%)</td><td>0.01 <b>(-55.94%)</b></td><td>178.80 (-2.93%)</td><td>163.26 (+2.94%)</td><td>166.20 (+0.79%)</td><td>146.80 (+18.20%)</td><td>11.86 <b>(-49.21%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.20 (n/a)</td><td>158.60 (n/a)</td><td>164.90 (n/a)</td><td>124.20 (n/a)</td><td>23.35 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 <b>(-32.13%)</b></td><td>0.17 <b>(-23.88%)</b></td><td>0.19 (-18.18%)</td><td>0.11 <b>(-32.29%)</b></td><td>0.04 <b>(-34.60%)</b></td><td>297.10 <b>(+47.66%)</b></td><td>203.76 <b>(+30.70%)</b></td><td>173.90 <b>(+22.21%)</b></td><td>148.60 <b>(+47.42%)</b></td><td>59.27 <b>(+39.66%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>201.20 (n/a)</td><td>155.90 (n/a)</td><td>142.30 (n/a)</td><td>100.80 (n/a)</td><td>42.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (+8.46%)</td><td>0.20 (-0.47%)</td><td>0.19 (-3.68%)</td><td>0.14 (-5.71%)</td><td>0.04 <b>(+23.79%)</b></td><td>234.10 (+6.07%)</td><td>173.98 (+1.70%)</td><td>169.10 (+3.81%)</td><td>128.20 (-7.77%)</td><td>38.57 <b>(+21.09%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>220.70 (n/a)</td><td>171.08 (n/a)</td><td>162.90 (n/a)</td><td>139.00 (n/a)</td><td>31.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (-3.44%)</td><td>0.17 (-13.21%)</td><td>0.14 <b>(-23.04%)</b></td><td>0.13 (-9.75%)</td><td>0.05 (+11.38%)</td><td>243.60 (+10.83%)</td><td>202.12 (+17.54%)</td><td>231.70 <b>(+29.95%)</b></td><td>126.00 (+3.62%)</td><td>50.88 <b>(+30.95%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>219.80 (n/a)</td><td>171.96 (n/a)</td><td>178.30 (n/a)</td><td>121.60 (n/a)</td><td>38.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (+4.07%)</td><td>0.18 (+0.05%)</td><td>0.18 (+2.30%)</td><td>0.14 (+4.79%)</td><td>0.04 (-0.89%)</td><td>231.00 (-4.55%)</td><td>186.94 (-0.21%)</td><td>181.20 (-2.21%)</td><td>144.10 (-3.93%)</td><td>37.81 (-4.31%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>242.00 (n/a)</td><td>187.34 (n/a)</td><td>185.30 (n/a)</td><td>150.00 (n/a)</td><td>39.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (+2.18%)</td><td>0.14 (-11.65%)</td><td>0.14 (-18.55%)</td><td>0.09 (-16.09%)</td><td>0.04 (+13.35%)</td><td>355.00 (+19.17%)</td><td>242.28 (+15.31%)</td><td>232.60 <b>(+22.81%)</b></td><td>163.10 (-2.16%)</td><td>69.66 <b>(+32.28%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>297.90 (n/a)</td><td>210.12 (n/a)</td><td>189.40 (n/a)</td><td>166.70 (n/a)</td><td>52.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+0.73%)</td><td>0.03 (-1.84%)</td><td>0.03 (-0.09%)</td><td>0.02 (-15.36%)</td><td>0.00 <b>(+42.39%)</b></td><td>186.70 (+18.16%)</td><td>152.44 (+3.31%)</td><td>155.10 (+0.06%)</td><td>119.40 (-0.75%)</td><td>26.33 <b>(+67.71%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>158.00 (n/a)</td><td>147.56 (n/a)</td><td>155.00 (n/a)</td><td>120.30 (n/a)</td><td>15.70 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+3.54%)</td><td>0.03 (-6.94%)</td><td>0.03 (-13.24%)</td><td>0.02 (+1.83%)</td><td>0.00 (+13.99%)</td><td>168.10 (-1.81%)</td><td>156.36 (+7.69%)</td><td>162.70 (+15.23%)</td><td>124.30 (-3.42%)</td><td>18.20 (+6.43%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.20 (n/a)</td><td>145.20 (n/a)</td><td>141.20 (n/a)</td><td>128.70 (n/a)</td><td>17.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+15.05%)</td><td>0.02 <b>(+25.44%)</b></td><td>0.02 <b>(+34.29%)</b></td><td>0.02 <b>(+21.21%)</b></td><td>0.00 <b>(+20.95%)</b></td><td>214.30 (-17.51%)</td><td>174.82 <b>(-20.21%)</b></td><td>165.20 <b>(-25.52%)</b></td><td>149.40 (-13.09%)</td><td>28.73 (-13.61%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>259.80 (n/a)</td><td>219.10 (n/a)</td><td>221.80 (n/a)</td><td>171.90 (n/a)</td><td>33.26 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 <b>(+37.97%)</b></td><td>0.02 (+12.75%)</td><td>0.02 (+10.52%)</td><td>0.02 (-9.62%)</td><td>0.00 <b>(+407.42%)</b></td><td>235.10 (+10.64%)</td><td>182.26 (-8.24%)</td><td>176.20 (-9.50%)</td><td>138.30 <b>(-27.52%)</b></td><td>38.73 <b>(+309.82%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.50 (n/a)</td><td>198.62 (n/a)</td><td>194.70 (n/a)</td><td>190.80 (n/a)</td><td>9.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (+13.13%)</td><td>0.03 (+3.19%)</td><td>0.03 (+1.05%)</td><td>0.02 (+1.02%)</td><td>0.00 <b>(+58.71%)</b></td><td>175.00 (-1.02%)</td><td>153.44 (-1.87%)</td><td>157.80 (-1.07%)</td><td>115.40 (-11.64%)</td><td>24.42 <b>(+40.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.80 (n/a)</td><td>156.36 (n/a)</td><td>159.50 (n/a)</td><td>130.60 (n/a)</td><td>17.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+14.96%)</td><td>0.02 (-5.11%)</td><td>0.02 (-12.63%)</td><td>0.02 (-11.62%)</td><td>0.00 <b>(+137.11%)</b></td><td>194.30 (+13.16%)</td><td>170.96 (+7.29%)</td><td>177.70 (+14.42%)</td><td>126.60 (-12.99%)</td><td>25.85 <b>(+120.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.70 (n/a)</td><td>159.34 (n/a)</td><td>155.30 (n/a)</td><td>145.50 (n/a)</td><td>11.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+15.96%)</td><td>0.02 (+11.84%)</td><td>0.02 (+14.88%)</td><td>0.02 (+5.43%)</td><td>0.00 <b>(+95.91%)</b></td><td>211.40 (-5.16%)</td><td>176.68 (-9.44%)</td><td>167.10 (-12.97%)</td><td>150.60 (-13.80%)</td><td>27.78 <b>(+58.32%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.90 (n/a)</td><td>195.10 (n/a)</td><td>192.00 (n/a)</td><td>174.70 (n/a)</td><td>17.55 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+17.35%)</td><td>0.03 (+11.92%)</td><td>0.03 <b>(+28.05%)</b></td><td>0.02 (-7.22%)</td><td>0.01 <b>(+63.50%)</b></td><td>220.40 (+7.78%)</td><td>166.36 (-8.40%)</td><td>150.60 <b>(-21.89%)</b></td><td>122.50 (-14.75%)</td><td>38.50 <b>(+52.20%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>181.62 (n/a)</td><td>192.80 (n/a)</td><td>143.70 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 <b>(+21.73%)</b></td><td>0.02 (+7.93%)</td><td>0.02 (+1.61%)</td><td>0.02 (-1.86%)</td><td>0.00 <b>(+118.52%)</b></td><td>207.50 (+1.92%)</td><td>179.58 (-5.28%)</td><td>197.10 (-1.60%)</td><td>135.60 (-17.82%)</td><td>32.62 <b>(+83.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>189.60 (n/a)</td><td>200.30 (n/a)</td><td>165.00 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 <b>(+42.21%)</b></td><td>0.03 <b>(+27.87%)</b></td><td>0.02 (+11.81%)</td><td>0.02 <b>(+53.07%)</b></td><td>0.01 <b>(+44.22%)</b></td><td>195.70 <b>(-34.68%)</b></td><td>164.90 <b>(-22.07%)</b></td><td>180.20 (-10.57%)</td><td>113.90 <b>(-29.65%)</b></td><td>32.93 <b>(-37.21%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>299.60 (n/a)</td><td>211.60 (n/a)</td><td>201.50 (n/a)</td><td>161.90 (n/a)</td><td>52.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 <b>(+46.39%)</b></td><td>0.03 <b>(+33.92%)</b></td><td>0.03 <b>(+25.33%)</b></td><td>0.02 <b>(+31.19%)</b></td><td>0.01 <b>(+102.74%)</b></td><td>184.80 <b>(-23.76%)</b></td><td>153.72 <b>(-24.25%)</b></td><td>160.10 <b>(-20.23%)</b></td><td>121.40 <b>(-31.68%)</b></td><td>27.71 (+5.17%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.40 (n/a)</td><td>202.92 (n/a)</td><td>200.70 (n/a)</td><td>177.70 (n/a)</td><td>26.35 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 <b>(+48.89%)</b></td><td>0.03 (+10.10%)</td><td>0.02 (-3.31%)</td><td>0.01 <b>(-33.22%)</b></td><td>0.01 <b>(+244.12%)</b></td><td>331.60 <b>(+49.71%)</b></td><td>183.26 (+3.83%)</td><td>171.00 (+3.39%)</td><td>109.10 <b>(-32.82%)</b></td><td>88.26 <b>(+248.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.50 (n/a)</td><td>176.50 (n/a)</td><td>165.40 (n/a)</td><td>162.40 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 <b>(+34.61%)</b></td><td>0.02 (-4.17%)</td><td>0.02 (-11.07%)</td><td>0.01 <b>(-32.47%)</b></td><td>0.01 <b>(+174.63%)</b></td><td>366.30 <b>(+48.06%)</b></td><td>228.16 (+14.43%)</td><td>208.30 (+12.47%)</td><td>130.80 <b>(-25.72%)</b></td><td>85.76 <b>(+200.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.40 (n/a)</td><td>199.38 (n/a)</td><td>185.20 (n/a)</td><td>176.10 (n/a)</td><td>28.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 <b>(+28.37%)</b></td><td>0.03 <b>(+25.74%)</b></td><td>0.03 <b>(+44.56%)</b></td><td>0.02 (+6.03%)</td><td>0.01 <b>(+100.38%)</b></td><td>207.30 (-5.69%)</td><td>148.80 (-18.30%)</td><td>126.30 <b>(-30.83%)</b></td><td>122.80 <b>(-22.13%)</b></td><td>36.43 <b>(+46.02%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.80 (n/a)</td><td>182.14 (n/a)</td><td>182.60 (n/a)</td><td>157.70 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 <b>(+28.26%)</b></td><td>0.03 <b>(+26.78%)</b></td><td>0.03 <b>(+28.37%)</b></td><td>0.02 <b>(+25.22%)</b></td><td>0.00 <b>(+47.29%)</b></td><td>174.00 <b>(-20.15%)</b></td><td>146.54 <b>(-20.91%)</b></td><td>140.70 <b>(-22.09%)</b></td><td>130.00 <b>(-22.02%)</b></td><td>17.69 (-9.66%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.90 (n/a)</td><td>185.28 (n/a)</td><td>180.60 (n/a)</td><td>166.70 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+6.36%)</td><td>0.03 <b>(+31.80%)</b></td><td>0.03 <b>(+45.33%)</b></td><td>0.03 <b>(+32.85%)</b></td><td>0.00 <b>(-46.24%)</b></td><td>154.90 <b>(-24.70%)</b></td><td>139.74 <b>(-25.58%)</b></td><td>136.40 <b>(-31.22%)</b></td><td>128.00 (-6.02%)</td><td>11.33 <b>(-61.04%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.70 (n/a)</td><td>187.76 (n/a)</td><td>198.30 (n/a)</td><td>136.20 (n/a)</td><td>29.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (+6.71%)</td><td>0.05 (+7.16%)</td><td>0.05 (+13.79%)</td><td>0.04 <b>(-23.83%)</b></td><td>0.01 <b>(+94.89%)</b></td><td>232.80 <b>(+31.30%)</b></td><td>158.44 (-2.77%)</td><td>150.20 (-12.11%)</td><td>124.20 (-6.26%)</td><td>44.43 <b>(+140.15%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.30 (n/a)</td><td>162.96 (n/a)</td><td>170.90 (n/a)</td><td>132.50 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 <b>(+52.28%)</b></td><td>0.06 <b>(+22.33%)</b></td><td>0.06 (+19.65%)</td><td>0.04 (-9.62%)</td><td>0.02 <b>(+220.25%)</b></td><td>203.00 (+10.69%)</td><td>144.52 (-13.74%)</td><td>143.60 (-16.41%)</td><td>94.30 <b>(-34.38%)</b></td><td>39.96 <b>(+128.27%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>167.54 (n/a)</td><td>171.80 (n/a)</td><td>143.70 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 <b>(-21.47%)</b></td><td>0.03 (-13.17%)</td><td>0.04 (-0.44%)</td><td>0.03 (-5.47%)</td><td>0.01 <b>(-39.20%)</b></td><td>319.10 (+5.77%)</td><td>254.56 (+12.71%)</td><td>225.80 (+0.49%)</td><td>219.60 <b>(+27.30%)</b></td><td>44.92 (-16.85%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>301.70 (n/a)</td><td>225.86 (n/a)</td><td>224.70 (n/a)</td><td>172.50 (n/a)</td><td>54.01 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-3.13%)</td><td>0.04 (-3.34%)</td><td>0.04 (-9.69%)</td><td>0.04 (+7.86%)</td><td>0.01 <b>(-27.05%)</b></td><td>230.80 (-7.27%)</td><td>197.20 (+2.17%)</td><td>197.30 (+10.72%)</td><td>162.40 (+3.24%)</td><td>24.33 <b>(-32.00%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.90 (n/a)</td><td>193.02 (n/a)</td><td>178.20 (n/a)</td><td>157.30 (n/a)</td><td>35.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 <b>(+26.58%)</b></td><td>0.06 <b>(+32.47%)</b></td><td>0.06 <b>(+32.03%)</b></td><td>0.05 <b>(+34.36%)</b></td><td>0.01 (-6.51%)</td><td>164.90 <b>(-25.55%)</b></td><td>143.48 <b>(-25.19%)</b></td><td>145.10 <b>(-24.27%)</b></td><td>125.50 <b>(-20.97%)</b></td><td>15.56 <b>(-46.06%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>191.78 (n/a)</td><td>191.60 (n/a)</td><td>158.80 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (+4.12%)</td><td>0.05 (-5.86%)</td><td>0.04 (-15.45%)</td><td>0.04 (-7.99%)</td><td>0.01 <b>(+45.44%)</b></td><td>186.80 (+8.67%)</td><td>160.78 (+8.71%)</td><td>184.50 (+18.27%)</td><td>117.20 (-3.93%)</td><td>34.54 <b>(+58.34%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.90 (n/a)</td><td>147.90 (n/a)</td><td>156.00 (n/a)</td><td>122.00 (n/a)</td><td>21.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (-5.31%)</td><td>0.05 (-3.25%)</td><td>0.06 (-0.19%)</td><td>0.04 (+4.70%)</td><td>0.01 <b>(-27.64%)</b></td><td>191.00 (-4.45%)</td><td>155.36 (+1.45%)</td><td>143.80 (+0.14%)</td><td>127.60 (+5.63%)</td><td>27.01 <b>(-24.35%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>153.14 (n/a)</td><td>143.60 (n/a)</td><td>120.80 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (+1.25%)</td><td>0.05 (+2.64%)</td><td>0.05 (+13.59%)</td><td>0.03 (-6.59%)</td><td>0.01 (-0.55%)</td><td>241.00 (+7.06%)</td><td>181.42 (-2.37%)</td><td>178.70 (-11.93%)</td><td>142.10 (-1.18%)</td><td>38.01 (+8.07%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.10 (n/a)</td><td>185.82 (n/a)</td><td>202.90 (n/a)</td><td>143.80 (n/a)</td><td>35.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-18.99%)</td><td>0.05 (-12.88%)</td><td>0.05 (-6.86%)</td><td>0.04 (-16.36%)</td><td>0.01 <b>(-22.22%)</b></td><td>228.30 (+19.53%)</td><td>183.88 (+14.60%)</td><td>172.60 (+7.34%)</td><td>151.00 <b>(+23.47%)</b></td><td>29.92 (+18.89%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>160.46 (n/a)</td><td>160.80 (n/a)</td><td>122.30 (n/a)</td><td>25.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (-5.69%)</td><td>0.05 (-9.92%)</td><td>0.05 (-10.84%)</td><td>0.04 (-11.71%)</td><td>0.01 (+17.21%)</td><td>195.20 (+13.23%)</td><td>168.62 (+11.46%)</td><td>165.20 (+12.15%)</td><td>146.30 (+6.01%)</td><td>19.36 <b>(+40.51%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.40 (n/a)</td><td>151.28 (n/a)</td><td>147.30 (n/a)</td><td>138.00 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (-11.32%)</td><td>0.05 (-2.31%)</td><td>0.05 (+3.45%)</td><td>0.04 (+1.61%)</td><td>0.01 <b>(-30.22%)</b></td><td>216.80 (-1.59%)</td><td>180.66 (+1.07%)</td><td>176.40 (-3.34%)</td><td>146.30 (+12.71%)</td><td>25.82 (-19.87%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.30 (n/a)</td><td>178.74 (n/a)</td><td>182.50 (n/a)</td><td>129.80 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (-0.14%)</td><td>0.05 (+0.48%)</td><td>0.05 (-7.77%)</td><td>0.04 (-0.51%)</td><td>0.01 (-9.94%)</td><td>215.60 (+0.51%)</td><td>167.02 (-1.39%)</td><td>171.70 (+8.46%)</td><td>128.60 (+0.16%)</td><td>34.64 (-12.84%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>169.38 (n/a)</td><td>158.30 (n/a)</td><td>128.40 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 <b>(+24.46%)</b></td><td>0.05 (+12.47%)</td><td>0.04 (-4.90%)</td><td>0.04 (+13.83%)</td><td>0.01 <b>(+59.06%)</b></td><td>233.10 (-12.14%)</td><td>179.24 (-9.18%)</td><td>193.90 (+5.15%)</td><td>127.40 (-19.62%)</td><td>44.06 (+6.66%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>265.30 (n/a)</td><td>197.36 (n/a)</td><td>184.40 (n/a)</td><td>158.50 (n/a)</td><td>41.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-18.36%)</td><td>0.05 (-14.86%)</td><td>0.04 (-18.36%)</td><td>0.04 (-7.34%)</td><td>0.00 <b>(-45.52%)</b></td><td>193.10 (+7.94%)</td><td>181.86 (+16.77%)</td><td>185.90 <b>(+22.46%)</b></td><td>163.50 <b>(+22.47%)</b></td><td>12.19 <b>(-27.97%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>155.74 (n/a)</td><td>151.80 (n/a)</td><td>133.50 (n/a)</td><td>16.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-14.02%)</td><td>0.04 (-7.45%)</td><td>0.04 (-13.64%)</td><td>0.04 <b>(+39.79%)</b></td><td>0.00 <b>(-73.85%)</b></td><td>207.20 <b>(-28.48%)</b></td><td>190.20 (+2.27%)</td><td>191.60 (+15.84%)</td><td>176.00 (+16.33%)</td><td>12.27 <b>(-79.02%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.70 (n/a)</td><td>185.98 (n/a)</td><td>165.40 (n/a)</td><td>151.30 (n/a)</td><td>58.48 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-18.87%)</td><td>0.04 (+2.56%)</td><td>0.04 (-6.25%)</td><td>0.04 <b>(+67.86%)</b></td><td>0.00 <b>(-73.36%)</b></td><td>219.10 <b>(-40.45%)</b></td><td>186.88 (-13.82%)</td><td>183.00 (+6.64%)</td><td>169.70 <b>(+23.24%)</b></td><td>19.01 <b>(-80.13%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>367.90 (n/a)</td><td>216.84 (n/a)</td><td>171.60 (n/a)</td><td>137.70 (n/a)</td><td>95.69 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (+17.53%)</td><td>0.10 (-1.43%)</td><td>0.09 (-13.13%)</td><td>0.09 (+9.33%)</td><td>0.03 <b>(+20.32%)</b></td><td>192.30 (-8.52%)</td><td>165.10 (+1.81%)</td><td>178.20 (+15.12%)</td><td>110.30 (-14.89%)</td><td>31.97 (-8.28%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.20 (n/a)</td><td>162.16 (n/a)</td><td>154.80 (n/a)</td><td>129.60 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (-9.11%)</td><td>0.10 (-7.03%)</td><td>0.09 (-15.26%)</td><td>0.08 (-2.26%)</td><td>0.02 (-9.23%)</td><td>196.80 (+2.29%)</td><td>173.14 (+7.47%)</td><td>189.90 (+18.02%)</td><td>132.90 (+10.02%)</td><td>27.96 (+5.84%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.40 (n/a)</td><td>161.10 (n/a)</td><td>160.90 (n/a)</td><td>120.80 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 (-16.43%)</td><td>0.07 (-6.75%)</td><td>0.07 (+1.40%)</td><td>0.07 (-7.12%)</td><td>0.00 <b>(-55.98%)</b></td><td>243.70 (+7.69%)</td><td>221.44 (+6.38%)</td><td>219.20 (-1.35%)</td><td>209.80 (+19.61%)</td><td>13.17 <b>(-43.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>208.16 (n/a)</td><td>222.20 (n/a)</td><td>175.40 (n/a)</td><td>23.28 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 <b>(-21.74%)</b></td><td>0.07 (-19.89%)</td><td>0.07 (-16.87%)</td><td>0.06 <b>(-27.88%)</b></td><td>0.01 (-0.98%)</td><td>275.70 <b>(+38.61%)</b></td><td>226.46 <b>(+25.78%)</b></td><td>227.00 <b>(+20.30%)</b></td><td>189.90 <b>(+27.79%)</b></td><td>34.75 <b>(+75.13%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>180.04 (n/a)</td><td>188.70 (n/a)</td><td>148.60 (n/a)</td><td>19.84 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (-5.58%)</td><td>0.10 (-1.83%)</td><td>0.10 (+0.71%)</td><td>0.08 (+1.29%)</td><td>0.01 <b>(-32.11%)</b></td><td>202.30 (-1.27%)</td><td>167.26 (+0.10%)</td><td>165.30 (-0.72%)</td><td>139.10 (+5.94%)</td><td>24.47 <b>(-28.48%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.90 (n/a)</td><td>167.10 (n/a)</td><td>166.50 (n/a)</td><td>131.30 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (-2.53%)</td><td>0.11 (+5.44%)</td><td>0.11 (+5.64%)</td><td>0.10 <b>(+52.71%)</b></td><td>0.01 <b>(-55.58%)</b></td><td>164.30 <b>(-34.54%)</b></td><td>148.30 (-10.86%)</td><td>150.00 (-5.36%)</td><td>122.60 (+2.59%)</td><td>15.67 <b>(-70.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>251.00 (n/a)</td><td>166.36 (n/a)</td><td>158.50 (n/a)</td><td>119.50 (n/a)</td><td>53.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (-1.14%)</td><td>0.11 (+3.02%)</td><td>0.11 (+13.87%)</td><td>0.08 (+1.12%)</td><td>0.02 (-7.44%)</td><td>193.00 (-1.13%)</td><td>154.04 (-3.46%)</td><td>153.90 (-12.16%)</td><td>116.40 (+1.13%)</td><td>31.15 (-6.81%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.20 (n/a)</td><td>159.56 (n/a)</td><td>175.20 (n/a)</td><td>115.10 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (+10.51%)</td><td>0.10 (+1.17%)</td><td>0.10 (-8.66%)</td><td>0.08 (+4.21%)</td><td>0.02 <b>(+20.19%)</b></td><td>195.40 (-4.03%)</td><td>162.80 (-0.62%)</td><td>167.60 (+9.47%)</td><td>118.00 (-9.51%)</td><td>29.70 (+1.14%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.60 (n/a)</td><td>163.82 (n/a)</td><td>153.10 (n/a)</td><td>130.40 (n/a)</td><td>29.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (+13.64%)</td><td>0.11 (+8.05%)</td><td>0.11 (+16.40%)</td><td>0.08 (-5.51%)</td><td>0.03 <b>(+44.72%)</b></td><td>198.70 (+5.86%)</td><td>155.84 (-5.44%)</td><td>154.20 (-14.09%)</td><td>118.10 (-12.00%)</td><td>36.68 <b>(+33.68%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.70 (n/a)</td><td>164.80 (n/a)</td><td>179.50 (n/a)</td><td>134.20 (n/a)</td><td>27.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (+19.47%)</td><td>0.10 (+7.33%)</td><td>0.10 (+8.43%)</td><td>0.08 (-4.94%)</td><td>0.03 <b>(+99.14%)</b></td><td>215.80 (+5.22%)</td><td>167.94 (-3.05%)</td><td>162.90 (-7.81%)</td><td>117.60 (-16.30%)</td><td>43.38 <b>(+81.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>173.22 (n/a)</td><td>176.70 (n/a)</td><td>140.50 (n/a)</td><td>23.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 <b>(+21.02%)</b></td><td>0.10 (+8.80%)</td><td>0.11 (+18.83%)</td><td>0.06 (-14.99%)</td><td>0.02 <b>(+99.18%)</b></td><td>254.20 (+17.63%)</td><td>175.08 (-4.49%)</td><td>155.00 (-15.81%)</td><td>131.60 (-17.34%)</td><td>48.01 <b>(+102.90%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>183.32 (n/a)</td><td>184.10 (n/a)</td><td>159.20 (n/a)</td><td>23.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (-7.02%)</td><td>0.10 (+6.19%)</td><td>0.10 (+14.06%)</td><td>0.08 (+12.14%)</td><td>0.01 <b>(-26.32%)</b></td><td>205.00 (-10.83%)</td><td>169.34 (-7.26%)</td><td>157.70 (-12.34%)</td><td>143.80 (+7.55%)</td><td>25.85 <b>(-28.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>229.90 (n/a)</td><td>182.60 (n/a)</td><td>179.90 (n/a)</td><td>133.70 (n/a)</td><td>36.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (-11.93%)</td><td>0.08 (-17.64%)</td><td>0.09 (-16.65%)</td><td>0.06 <b>(-21.95%)</b></td><td>0.02 (+4.71%)</td><td>281.30 <b>(+28.15%)</b></td><td>203.12 <b>(+23.42%)</b></td><td>190.60 <b>(+20.03%)</b></td><td>150.40 (+13.60%)</td><td>50.30 <b>(+50.97%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.50 (n/a)</td><td>164.58 (n/a)</td><td>158.80 (n/a)</td><td>132.40 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (-2.12%)</td><td>0.09 (-1.26%)</td><td>0.09 (+2.02%)</td><td>0.07 (-2.78%)</td><td>0.01 (+5.46%)</td><td>243.80 (+2.87%)</td><td>189.10 (+1.58%)</td><td>175.90 (-2.01%)</td><td>158.60 (+2.19%)</td><td>33.28 (+9.62%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>237.00 (n/a)</td><td>186.16 (n/a)</td><td>179.50 (n/a)</td><td>155.20 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (-6.25%)</td><td>0.09 (-11.61%)</td><td>0.08 (-11.44%)</td><td>0.07 (-9.19%)</td><td>0.02 (+3.89%)</td><td>222.60 (+10.14%)</td><td>193.86 (+13.86%)</td><td>201.20 (+12.91%)</td><td>135.20 (+6.62%)</td><td>34.36 <b>(+20.95%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>170.26 (n/a)</td><td>178.20 (n/a)</td><td>126.80 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (+7.37%)</td><td>0.10 (+14.81%)</td><td>0.10 (+13.24%)</td><td>0.09 <b>(+27.70%)</b></td><td>0.01 <b>(-56.61%)</b></td><td>182.30 <b>(-21.69%)</b></td><td>167.68 (-14.17%)</td><td>164.50 (-11.70%)</td><td>157.60 (-6.91%)</td><td>9.33 <b>(-67.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>195.36 (n/a)</td><td>186.30 (n/a)</td><td>169.30 (n/a)</td><td>28.88 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (+2.00%)</td><td>0.20 (-18.86%)</td><td>0.19 <b>(-28.59%)</b></td><td>0.15 (-12.00%)</td><td>0.05 (+18.54%)</td><td>214.40 (+13.62%)</td><td>171.00 <b>(+25.00%)</b></td><td>174.10 <b>(+40.06%)</b></td><td>117.90 (-2.00%)</td><td>37.42 <b>(+28.07%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.70 (n/a)</td><td>136.80 (n/a)</td><td>124.30 (n/a)</td><td>120.30 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (+9.64%)</td><td>0.22 (+2.31%)</td><td>0.21 (-2.78%)</td><td>0.18 (+3.44%)</td><td>0.04 (+15.12%)</td><td>184.70 (-3.35%)</td><td>151.34 (-1.78%)</td><td>152.70 (+2.90%)</td><td>116.70 (-8.76%)</td><td>28.76 (+3.39%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>191.10 (n/a)</td><td>154.08 (n/a)</td><td>148.40 (n/a)</td><td>127.90 (n/a)</td><td>27.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 <b>(+34.04%)</b></td><td>0.18 (+11.54%)</td><td>0.18 (+6.31%)</td><td>0.14 (+0.17%)</td><td>0.04 <b>(+148.94%)</b></td><td>235.60 (-0.17%)</td><td>183.74 (-7.96%)</td><td>178.40 (-5.96%)</td><td>139.50 <b>(-25.40%)</b></td><td>37.90 <b>(+84.08%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>236.00 (n/a)</td><td>199.64 (n/a)</td><td>189.70 (n/a)</td><td>187.00 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (+9.42%)</td><td>0.17 (-0.89%)</td><td>0.16 (-5.46%)</td><td>0.14 (-7.98%)</td><td>0.02 <b>(+95.22%)</b></td><td>232.90 (+8.68%)</td><td>193.86 (+2.12%)</td><td>198.90 (+5.74%)</td><td>162.90 (-8.59%)</td><td>27.87 <b>(+90.67%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>189.84 (n/a)</td><td>188.10 (n/a)</td><td>178.20 (n/a)</td><td>14.61 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (-1.40%)</td><td>0.21 (-6.15%)</td><td>0.18 <b>(-29.20%)</b></td><td>0.17 <b>(+23.64%)</b></td><td>0.05 (-19.28%)</td><td>187.40 (-19.12%)</td><td>162.60 (+3.41%)</td><td>183.50 <b>(+41.26%)</b></td><td>116.10 (+1.40%)</td><td>33.11 <b>(-32.19%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>231.70 (n/a)</td><td>157.24 (n/a)</td><td>129.90 (n/a)</td><td>114.50 (n/a)</td><td>48.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (-18.44%)</td><td>0.17 <b>(-28.07%)</b></td><td>0.19 <b>(-24.70%)</b></td><td>0.09 <b>(-53.39%)</b></td><td>0.05 <b>(+70.74%)</b></td><td>361.10 <b>(+114.56%)</b></td><td>215.40 <b>(+52.23%)</b></td><td>176.00 <b>(+32.73%)</b></td><td>150.30 <b>(+22.59%)</b></td><td>87.93 <b>(+345.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>168.30 (n/a)</td><td>141.50 (n/a)</td><td>132.60 (n/a)</td><td>122.60 (n/a)</td><td>19.74 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (-6.86%)</td><td>0.18 (-3.99%)</td><td>0.18 (-9.74%)</td><td>0.15 <b>(+45.06%)</b></td><td>0.02 <b>(-54.45%)</b></td><td>215.90 <b>(-31.07%)</b></td><td>182.08 (-2.94%)</td><td>184.20 (+10.76%)</td><td>152.20 (+7.33%)</td><td>23.12 <b>(-67.59%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>313.20 (n/a)</td><td>187.60 (n/a)</td><td>166.30 (n/a)</td><td>141.80 (n/a)</td><td>71.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (+15.39%)</td><td>0.18 (-13.33%)</td><td>0.17 (-19.23%)</td><td>0.09 <b>(-46.77%)</b></td><td>0.07 <b>(+149.44%)</b></td><td>370.60 <b>(+87.84%)</b></td><td>209.60 <b>(+31.74%)</b></td><td>190.80 <b>(+23.82%)</b></td><td>116.20 (-13.35%)</td><td>97.90 <b>(+310.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>197.30 (n/a)</td><td>159.10 (n/a)</td><td>154.10 (n/a)</td><td>134.10 (n/a)</td><td>23.84 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (+11.60%)</td><td>0.17 (-6.62%)</td><td>0.16 (-14.49%)</td><td>0.09 (-19.95%)</td><td>0.07 (+12.89%)</td><td>360.70 <b>(+24.94%)</b></td><td>216.12 (+11.15%)</td><td>208.30 (+16.96%)</td><td>118.60 (-10.42%)</td><td>90.66 <b>(+32.89%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>288.70 (n/a)</td><td>194.44 (n/a)</td><td>178.10 (n/a)</td><td>132.40 (n/a)</td><td>68.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (-18.32%)</td><td>0.19 (-15.25%)</td><td>0.18 (-12.48%)</td><td>0.15 <b>(-22.00%)</b></td><td>0.03 (+1.88%)</td><td>214.90 <b>(+28.22%)</b></td><td>179.80 (+18.73%)</td><td>177.30 (+14.24%)</td><td>154.70 <b>(+22.49%)</b></td><td>25.57 <b>(+58.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>167.60 (n/a)</td><td>151.44 (n/a)</td><td>155.20 (n/a)</td><td>126.30 (n/a)</td><td>16.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (+10.75%)</td><td>0.21 (+0.57%)</td><td>0.19 <b>(-20.21%)</b></td><td>0.17 <b>(+93.59%)</b></td><td>0.04 <b>(-34.71%)</b></td><td>187.50 <b>(-48.35%)</b></td><td>163.76 (-11.72%)</td><td>175.90 <b>(+25.28%)</b></td><td>117.40 (-9.69%)</td><td>29.38 <b>(-70.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>363.00 (n/a)</td><td>185.50 (n/a)</td><td>140.40 (n/a)</td><td>130.00 (n/a)</td><td>99.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.27 (+5.07%)</td><td>0.19 (-18.82%)</td><td>0.17 <b>(-29.18%)</b></td><td>0.14 <b>(-24.29%)</b></td><td>0.05 <b>(+90.28%)</b></td><td>232.00 <b>(+32.12%)</b></td><td>183.02 <b>(+28.51%)</b></td><td>195.10 <b>(+41.17%)</b></td><td>120.30 (-4.83%)</td><td>44.59 <b>(+130.91%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>175.60 (n/a)</td><td>142.42 (n/a)</td><td>138.20 (n/a)</td><td>126.40 (n/a)</td><td>19.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (+3.70%)</td><td>0.17 (-16.56%)</td><td>0.16 (-9.78%)</td><td>0.12 <b>(-26.27%)</b></td><td>0.06 <b>(+31.74%)</b></td><td>263.40 <b>(+35.63%)</b></td><td>207.52 <b>(+24.94%)</b></td><td>206.60 (+10.84%)</td><td>125.70 (-3.53%)</td><td>58.02 <b>(+79.58%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.20 (n/a)</td><td>166.10 (n/a)</td><td>186.40 (n/a)</td><td>130.30 (n/a)</td><td>32.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (-9.97%)</td><td>0.20 (-14.13%)</td><td>0.21 (-7.23%)</td><td>0.16 <b>(-22.37%)</b></td><td>0.03 <b>(+36.00%)</b></td><td>209.40 <b>(+28.86%)</b></td><td>170.46 (+18.38%)</td><td>158.10 (+7.77%)</td><td>139.10 (+11.01%)</td><td>31.30 <b>(+98.68%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>162.50 (n/a)</td><td>144.00 (n/a)</td><td>146.70 (n/a)</td><td>125.30 (n/a)</td><td>15.75 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (-1.37%)</td><td>0.20 (-4.06%)</td><td>0.20 (-11.75%)</td><td>0.15 (-6.83%)</td><td>0.03 (-9.93%)</td><td>211.70 (+7.35%)</td><td>166.58 (+3.96%)</td><td>161.50 (+13.33%)</td><td>137.20 (+1.40%)</td><td>28.56 (-0.91%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.20 (n/a)</td><td>160.24 (n/a)</td><td>142.50 (n/a)</td><td>135.30 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 <b>(-34.45%)</b></td><td>0.17 <b>(-24.21%)</b></td><td>0.16 <b>(-27.65%)</b></td><td>0.15 (+0.03%)</td><td>0.02 <b>(-65.37%)</b></td><td>214.10 (+0.00%)</td><td>196.82 <b>(+25.54%)</b></td><td>204.50 <b>(+38.27%)</b></td><td>158.80 <b>(+52.55%)</b></td><td>21.93 <b>(-48.52%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>214.10 (n/a)</td><td>156.78 (n/a)</td><td>147.90 (n/a)</td><td>104.10 (n/a)</td><td>42.61 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (-0.03%)</td><td>0.16 (-0.02%)</td><td>0.16 (-0.05%)</td><td>0.16 (-0.01%)</td><td>0.00 <b>(-28.68%)</b></td><td>52611.10 (+0.01%)</td><td>52570.46 (+0.02%)</td><td>52573.00 (+0.05%)</td><td>52531.10 (+0.03%)</td><td>28.70 <b>(-28.68%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52607.20 (n/a)</td><td>52561.36 (n/a)</td><td>52549.10 (n/a)</td><td>52517.30 (n/a)</td><td>40.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52594.40 (n/a)</td><td>52537.26 (n/a)</td><td>52541.50 (n/a)</td><td>52461.60 (n/a)</td><td>48.75 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>415722.20 (n/a)</td><td>415628.82 (n/a)</td><td>415641.20 (n/a)</td><td>415541.30 (n/a)</td><td>75.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (-5.28%)</td><td>0.17 (+6.90%)</td><td>0.17 (+15.67%)</td><td>0.14 (+3.92%)</td><td>0.02 (-16.64%)</td><td>176.80 (-3.76%)</td><td>146.32 (-7.13%)</td><td>140.90 (-13.56%)</td><td>124.70 (+5.50%)</td><td>22.15 (-15.16%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>183.70 (n/a)</td><td>157.56 (n/a)</td><td>163.00 (n/a)</td><td>118.20 (n/a)</td><td>26.11 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.40 (+2.65%)</td><td>0.35 <b>(+22.05%)</b></td><td>0.38 <b>(+31.37%)</b></td><td>0.26 (+17.59%)</td><td>0.06 (-7.63%)</td><td>188.20 (-14.96%)</td><td>145.74 (-19.20%)</td><td>129.30 <b>(-23.85%)</b></td><td>121.60 (-2.56%)</td><td>29.78 <b>(-27.09%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>221.30 (n/a)</td><td>180.38 (n/a)</td><td>169.80 (n/a)</td><td>124.80 (n/a)</td><td>40.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>13.63 (-1.81%)</td><td>13.11 (+1.18%)</td><td>13.22 (+1.71%)</td><td>12.53 (+11.98%)</td><td>0.45 <b>(-58.23%)</b></td><td>836.60 (-10.71%)</td><td>800.64 (-1.66%)</td><td>793.00 (-1.69%)</td><td>769.30 (+1.84%)</td><td>27.64 <b>(-62.17%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>13.88 (n/a)</td><td>12.96 (n/a)</td><td>13.00 (n/a)</td><td>11.19 (n/a)</td><td>1.08 (n/a)</td><td>936.90 (n/a)</td><td>814.16 (n/a)</td><td>806.60 (n/a)</td><td>755.40 (n/a)</td><td>73.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.32 (-1.77%)</td><td>0.27 (+4.57%)</td><td>0.30 (+17.35%)</td><td>0.20 (+3.21%)</td><td>0.06 (-2.99%)</td><td>201.30 (-3.08%)</td><td>156.52 (-4.68%)</td><td>134.60 (-14.76%)</td><td>126.50 (+1.85%)</td><td>37.43 (-5.27%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>207.70 (n/a)</td><td>164.20 (n/a)</td><td>157.90 (n/a)</td><td>124.20 (n/a)</td><td>39.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (+10.42%)</td><td>0.04 (+13.12%)</td><td>0.04 <b>(+35.00%)</b></td><td>0.03 (-1.67%)</td><td>0.01 (+10.91%)</td><td>180.50 (+1.69%)</td><td>139.76 (-11.35%)</td><td>128.50 <b>(-25.89%)</b></td><td>114.40 (-9.49%)</td><td>25.68 (+2.69%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>157.66 (n/a)</td><td>173.40 (n/a)</td><td>126.40 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-4.38%)</td><td>0.02 (-11.12%)</td><td>0.02 (+5.56%)</td><td>0.02 (-19.03%)</td><td>0.01 (+1.82%)</td><td>229.10 <b>(+23.50%)</b></td><td>183.52 (+13.79%)</td><td>171.70 (-5.30%)</td><td>131.00 (+4.55%)</td><td>42.02 <b>(+35.71%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>161.28 (n/a)</td><td>181.30 (n/a)</td><td>125.30 (n/a)</td><td>30.96 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (+17.53%)</td><td>0.04 (+12.11%)</td><td>0.05 (+19.16%)</td><td>0.03 (-2.81%)</td><td>0.01 <b>(+32.00%)</b></td><td>216.60 (+2.90%)</td><td>151.20 (-8.74%)</td><td>133.10 (-16.08%)</td><td>108.80 (-14.93%)</td><td>45.81 (+16.40%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>165.68 (n/a)</td><td>158.60 (n/a)</td><td>127.90 (n/a)</td><td>39.35 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-7.46%)</td><td>0.02 (-13.07%)</td><td>0.02 (-17.06%)</td><td>0.02 (-2.71%)</td><td>0.00 (-17.58%)</td><td>210.70 (+2.78%)</td><td>185.88 (+14.54%)</td><td>187.70 <b>(+20.55%)</b></td><td>154.50 (+8.04%)</td><td>22.84 (-9.22%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>162.28 (n/a)</td><td>155.70 (n/a)</td><td>143.00 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (+5.86%)</td><td>0.03 (-7.93%)</td><td>0.03 (-16.02%)</td><td>0.02 <b>(-20.91%)</b></td><td>0.01 <b>(+184.49%)</b></td><td>227.60 <b>(+26.44%)</b></td><td>183.18 (+12.71%)</td><td>190.90 (+19.09%)</td><td>138.70 (-5.58%)</td><td>40.61 <b>(+232.45%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>180.00 (n/a)</td><td>162.52 (n/a)</td><td>160.30 (n/a)</td><td>146.90 (n/a)</td><td>12.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 <b>(+24.22%)</b></td><td>0.03 (+9.55%)</td><td>0.03 (+10.02%)</td><td>0.02 (-9.49%)</td><td>0.01 <b>(+66.04%)</b></td><td>221.60 (+10.52%)</td><td>157.34 (-5.84%)</td><td>149.60 (-9.06%)</td><td>106.80 (-19.46%)</td><td>41.34 <b>(+46.97%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.50 (n/a)</td><td>167.10 (n/a)</td><td>164.50 (n/a)</td><td>132.60 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (-10.53%)</td><td>0.03 (-6.53%)</td><td>0.03 (-4.85%)</td><td>0.03 (+2.43%)</td><td>0.01 <b>(-29.15%)</b></td><td>192.70 (-2.33%)</td><td>160.02 (+4.36%)</td><td>161.80 (+5.06%)</td><td>118.10 (+11.73%)</td><td>29.74 <b>(-23.53%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>153.34 (n/a)</td><td>154.00 (n/a)</td><td>105.70 (n/a)</td><td>38.89 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.04 (+14.97%)</td><td>0.03 (-2.77%)</td><td>0.02 (-12.15%)</td><td>0.02 (-16.65%)</td><td>0.01 <b>(+45.47%)</b></td><td>225.10 (+19.99%)</td><td>165.88 (+5.52%)</td><td>164.30 (+13.78%)</td><td>114.70 (-13.04%)</td><td>41.00 <b>(+47.91%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.60 (n/a)</td><td>157.20 (n/a)</td><td>144.40 (n/a)</td><td>131.90 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-11.31%)</td><td>0.03 (-7.95%)</td><td>0.03 (-6.47%)</td><td>0.02 (+0.15%)</td><td>0.00 <b>(-29.31%)</b></td><td>205.40 (-0.15%)</td><td>173.04 (+6.83%)</td><td>181.30 (+6.90%)</td><td>134.00 (+12.79%)</td><td>27.81 <b>(-20.30%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>161.98 (n/a)</td><td>169.60 (n/a)</td><td>118.80 (n/a)</td><td>34.90 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+6.86%)</td><td>0.03 (+15.60%)</td><td>0.03 (+4.92%)</td><td>0.02 <b>(+48.54%)</b></td><td>0.01 <b>(-27.59%)</b></td><td>191.80 <b>(-32.68%)</b></td><td>160.56 (-18.41%)</td><td>157.90 (-4.65%)</td><td>117.50 (-6.37%)</td><td>28.85 <b>(-56.15%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>284.90 (n/a)</td><td>196.78 (n/a)</td><td>165.60 (n/a)</td><td>125.50 (n/a)</td><td>65.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-4.86%)</td><td>0.03 (-7.81%)</td><td>0.03 (-8.38%)</td><td>0.02 (-5.81%)</td><td>0.00 (+9.04%)</td><td>190.30 (+6.13%)</td><td>160.90 (+8.82%)</td><td>156.80 (+9.12%)</td><td>134.90 (+5.06%)</td><td>22.45 (+19.09%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>179.30 (n/a)</td><td>147.86 (n/a)</td><td>143.70 (n/a)</td><td>128.40 (n/a)</td><td>18.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+10.24%)</td><td>0.03 (+9.09%)</td><td>0.03 (+15.27%)</td><td>0.02 (+4.15%)</td><td>0.00 (+10.84%)</td><td>202.90 (-4.02%)</td><td>160.28 (-8.17%)</td><td>157.40 (-13.23%)</td><td>122.20 (-9.28%)</td><td>29.37 (-2.84%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.40 (n/a)</td><td>174.54 (n/a)</td><td>181.40 (n/a)</td><td>134.70 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-2.35%)</td><td>0.02 (-8.46%)</td><td>0.02 (-13.91%)</td><td>0.01 <b>(-24.22%)</b></td><td>0.00 (+17.89%)</td><td>298.70 <b>(+31.93%)</b></td><td>213.06 (+11.41%)</td><td>212.80 (+16.16%)</td><td>162.20 (+2.40%)</td><td>52.80 <b>(+58.86%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.40 (n/a)</td><td>191.24 (n/a)</td><td>183.20 (n/a)</td><td>158.40 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+3.53%)</td><td>0.02 (+13.54%)</td><td>0.02 (+14.76%)</td><td>0.02 <b>(+20.19%)</b></td><td>0.00 <b>(-35.44%)</b></td><td>193.10 (-16.80%)</td><td>170.62 (-13.21%)</td><td>172.40 (-12.89%)</td><td>150.70 (-3.40%)</td><td>16.45 <b>(-48.68%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.10 (n/a)</td><td>196.60 (n/a)</td><td>197.90 (n/a)</td><td>156.00 (n/a)</td><td>32.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-17.45%)</td><td>0.02 (-9.07%)</td><td>0.02 (-5.39%)</td><td>0.02 (-6.95%)</td><td>0.00 <b>(-32.41%)</b></td><td>244.20 (+7.48%)</td><td>204.24 (+7.82%)</td><td>219.00 (+5.69%)</td><td>154.90 <b>(+21.11%)</b></td><td>37.01 (-13.78%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>189.42 (n/a)</td><td>207.20 (n/a)</td><td>127.90 (n/a)</td><td>42.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.02 (+5.17%)</td><td>0.02 (+3.53%)</td><td>0.02 (+5.82%)</td><td>0.02 (-1.29%)</td><td>0.00 <b>(+61.46%)</b></td><td>220.30 (+1.29%)</td><td>196.56 (-3.01%)</td><td>189.80 (-5.48%)</td><td>179.90 (-4.92%)</td><td>18.45 <b>(+54.45%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.50 (n/a)</td><td>202.66 (n/a)</td><td>200.80 (n/a)</td><td>189.20 (n/a)</td><td>11.94 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 <b>(-26.92%)</b></td><td>0.06 (-8.07%)</td><td>0.06 (+1.30%)</td><td>0.05 (+7.71%)</td><td>0.01 <b>(-58.55%)</b></td><td>176.40 (-7.16%)</td><td>144.90 (+4.33%)</td><td>140.70 (-1.26%)</td><td>127.30 <b>(+36.88%)</b></td><td>19.22 <b>(-45.91%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>190.00 (n/a)</td><td>138.88 (n/a)</td><td>142.50 (n/a)</td><td>93.00 (n/a)</td><td>35.54 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 <b>(+30.71%)</b></td><td>0.08 (+11.40%)</td><td>0.08 (+8.04%)</td><td>0.06 (-12.23%)</td><td>0.02 <b>(+254.23%)</b></td><td>207.80 (+13.99%)</td><td>156.58 (-6.00%)</td><td>154.10 (-7.45%)</td><td>112.80 <b>(-23.47%)</b></td><td>39.17 <b>(+210.82%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>166.58 (n/a)</td><td>166.50 (n/a)</td><td>147.40 (n/a)</td><td>12.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (+5.65%)</td><td>0.04 (-13.05%)</td><td>0.04 <b>(-23.31%)</b></td><td>0.03 (+2.65%)</td><td>0.01 (+18.24%)</td><td>248.10 (-2.59%)</td><td>197.68 (+15.97%)</td><td>201.20 <b>(+30.40%)</b></td><td>122.10 (-5.35%)</td><td>47.92 (-1.47%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.70 (n/a)</td><td>170.46 (n/a)</td><td>154.30 (n/a)</td><td>129.00 (n/a)</td><td>48.64 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (-9.13%)</td><td>0.06 (-4.43%)</td><td>0.06 (-9.33%)</td><td>0.05 (+3.22%)</td><td>0.01 <b>(-39.18%)</b></td><td>191.70 (-3.13%)</td><td>169.36 (+2.83%)</td><td>173.80 (+10.28%)</td><td>144.40 (+10.06%)</td><td>19.43 <b>(-37.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>164.70 (n/a)</td><td>157.60 (n/a)</td><td>131.20 (n/a)</td><td>30.97 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (-5.26%)</td><td>0.05 (+1.49%)</td><td>0.05 (+5.75%)</td><td>0.05 (+1.07%)</td><td>0.01 <b>(-20.13%)</b></td><td>169.90 (-1.05%)</td><td>151.74 (-1.93%)</td><td>150.70 (-5.46%)</td><td>128.70 (+5.49%)</td><td>16.71 (-14.01%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.70 (n/a)</td><td>154.72 (n/a)</td><td>159.40 (n/a)</td><td>122.00 (n/a)</td><td>19.43 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (+3.98%)</td><td>0.06 (-4.34%)</td><td>0.06 (-3.44%)</td><td>0.04 (-13.12%)</td><td>0.02 (+10.93%)</td><td>238.10 (+15.08%)</td><td>173.10 (+6.21%)</td><td>163.50 (+3.55%)</td><td>113.80 (-3.80%)</td><td>49.23 <b>(+20.77%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>162.98 (n/a)</td><td>157.90 (n/a)</td><td>118.30 (n/a)</td><td>40.77 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (+7.76%)</td><td>0.05 (-7.68%)</td><td>0.05 (+8.03%)</td><td>0.03 <b>(-31.26%)</b></td><td>0.01 <b>(+77.98%)</b></td><td>276.00 <b>(+45.49%)</b></td><td>190.54 (+14.74%)</td><td>162.90 (-7.44%)</td><td>125.40 (-7.25%)</td><td>59.92 <b>(+145.13%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>166.06 (n/a)</td><td>176.00 (n/a)</td><td>135.20 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 <b>(+44.87%)</b></td><td>0.05 (+17.46%)</td><td>0.05 (+8.12%)</td><td>0.04 (+3.29%)</td><td>0.01 <b>(+194.00%)</b></td><td>222.30 (-3.22%)</td><td>184.28 (-12.48%)</td><td>194.30 (-7.52%)</td><td>128.60 <b>(-30.97%)</b></td><td>34.64 <b>(+85.95%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>229.70 (n/a)</td><td>210.56 (n/a)</td><td>210.10 (n/a)</td><td>186.30 (n/a)</td><td>18.63 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (-11.57%)</td><td>0.05 (-4.61%)</td><td>0.04 (-9.16%)</td><td>0.04 (-4.64%)</td><td>0.01 (-19.85%)</td><td>217.40 (+4.87%)</td><td>181.58 (+4.08%)</td><td>189.50 (+10.05%)</td><td>142.30 (+13.12%)</td><td>30.49 (-5.15%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>174.46 (n/a)</td><td>172.20 (n/a)</td><td>125.80 (n/a)</td><td>32.15 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.07 (-2.87%)</td><td>0.05 (-9.33%)</td><td>0.05 (-11.92%)</td><td>0.04 (+5.97%)</td><td>0.01 (-10.83%)</td><td>211.60 (-5.66%)</td><td>186.18 (+9.38%)</td><td>194.30 (+13.56%)</td><td>134.30 (+2.91%)</td><td>30.56 (-15.61%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>170.22 (n/a)</td><td>171.10 (n/a)</td><td>130.50 (n/a)</td><td>36.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (-1.01%)</td><td>0.04 (-12.23%)</td><td>0.04 <b>(-25.41%)</b></td><td>0.03 (-1.95%)</td><td>0.01 (-2.67%)</td><td>278.10 (+1.98%)</td><td>202.34 (+13.51%)</td><td>214.20 <b>(+34.04%)</b></td><td>137.30 (+1.03%)</td><td>53.88 (-3.11%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.70 (n/a)</td><td>178.26 (n/a)</td><td>159.80 (n/a)</td><td>135.90 (n/a)</td><td>55.61 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (+15.07%)</td><td>0.04 (+7.58%)</td><td>0.04 (-0.62%)</td><td>0.02 (-13.26%)</td><td>0.01 <b>(+36.77%)</b></td><td>350.80 (+15.32%)</td><td>216.24 (-3.12%)</td><td>203.50 (+0.64%)</td><td>140.60 (-13.10%)</td><td>80.03 <b>(+41.64%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.20 (n/a)</td><td>223.20 (n/a)</td><td>202.20 (n/a)</td><td>161.80 (n/a)</td><td>56.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (+1.57%)</td><td>0.05 <b>(+22.20%)</b></td><td>0.05 (+6.57%)</td><td>0.04 <b>(+82.83%)</b></td><td>0.01 <b>(-58.57%)</b></td><td>187.70 <b>(-45.31%)</b></td><td>163.54 <b>(-25.37%)</b></td><td>166.60 (-6.19%)</td><td>140.10 (-1.55%)</td><td>18.02 <b>(-78.20%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>343.20 (n/a)</td><td>219.12 (n/a)</td><td>177.60 (n/a)</td><td>142.30 (n/a)</td><td>82.67 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.05 (-0.02%)</td><td>0.04 (-0.15%)</td><td>0.04 (-7.02%)</td><td>0.03 (-5.30%)</td><td>0.01 (-5.27%)</td><td>317.40 (+5.59%)</td><td>220.04 (-0.04%)</td><td>208.60 (+7.58%)</td><td>160.60 (+0.06%)</td><td>58.20 (+2.55%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>300.60 (n/a)</td><td>220.12 (n/a)</td><td>193.90 (n/a)</td><td>160.50 (n/a)</td><td>56.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.06 (-6.59%)</td><td>0.05 (+7.17%)</td><td>0.04 (+7.71%)</td><td>0.03 (+11.02%)</td><td>0.01 (-18.76%)</td><td>238.30 (-9.94%)</td><td>187.64 (-9.22%)</td><td>184.90 (-7.13%)</td><td>132.00 (+7.06%)</td><td>46.38 <b>(-22.30%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>264.60 (n/a)</td><td>206.70 (n/a)</td><td>199.10 (n/a)</td><td>123.30 (n/a)</td><td>59.69 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (-0.01%)</td><td>0.10 (+0.65%)</td><td>0.10 (+6.05%)</td><td>0.07 (-9.51%)</td><td>0.02 (+13.70%)</td><td>223.60 (+10.47%)</td><td>174.00 (+0.09%)</td><td>165.50 (-5.70%)</td><td>143.20 (+0.07%)</td><td>31.89 <b>(+25.98%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>173.84 (n/a)</td><td>175.50 (n/a)</td><td>143.10 (n/a)</td><td>25.32 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 <b>(+23.20%)</b></td><td>0.16 (+5.30%)</td><td>0.14 (-7.96%)</td><td>0.12 (-1.68%)</td><td>0.04 <b>(+57.25%)</b></td><td>206.50 (+1.67%)</td><td>161.18 (-2.61%)</td><td>172.00 (+8.59%)</td><td>110.60 (-18.86%)</td><td>38.81 <b>(+29.13%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>203.10 (n/a)</td><td>165.50 (n/a)</td><td>158.40 (n/a)</td><td>136.30 (n/a)</td><td>30.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (+9.90%)</td><td>0.10 (+3.97%)</td><td>0.09 (-2.81%)</td><td>0.08 (-5.12%)</td><td>0.02 <b>(+63.05%)</b></td><td>208.10 (+5.37%)</td><td>174.84 (-1.87%)</td><td>191.40 (+2.90%)</td><td>132.10 (-9.02%)</td><td>34.12 <b>(+55.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.50 (n/a)</td><td>178.18 (n/a)</td><td>186.00 (n/a)</td><td>145.20 (n/a)</td><td>21.97 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (+0.78%)</td><td>0.13 (-2.85%)</td><td>0.12 (-5.58%)</td><td>0.10 (+10.47%)</td><td>0.02 (-8.02%)</td><td>202.10 (-9.49%)</td><td>167.60 (+2.12%)</td><td>166.40 (+5.92%)</td><td>133.10 (-0.82%)</td><td>28.79 (-18.54%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>223.30 (n/a)</td><td>164.12 (n/a)</td><td>157.10 (n/a)</td><td>134.20 (n/a)</td><td>35.34 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 <b>(+46.76%)</b></td><td>0.11 (+8.59%)</td><td>0.10 (+9.43%)</td><td>0.07 (-14.90%)</td><td>0.05 <b>(+123.38%)</b></td><td>230.10 (+17.52%)</td><td>164.26 (-0.64%)</td><td>166.80 (-8.65%)</td><td>85.20 <b>(-31.84%)</b></td><td>51.92 <b>(+65.65%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.80 (n/a)</td><td>165.32 (n/a)</td><td>182.60 (n/a)</td><td>125.00 (n/a)</td><td>31.34 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (+8.45%)</td><td>0.14 (+16.54%)</td><td>0.14 (+11.81%)</td><td>0.12 <b>(+33.41%)</b></td><td>0.02 (-15.76%)</td><td>169.00 <b>(-25.06%)</b></td><td>146.12 (-15.89%)</td><td>150.40 (-10.53%)</td><td>119.00 (-7.82%)</td><td>22.66 <b>(-41.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>225.50 (n/a)</td><td>173.72 (n/a)</td><td>168.10 (n/a)</td><td>129.10 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 <b>(-28.91%)</b></td><td>0.08 (-14.46%)</td><td>0.08 (-11.64%)</td><td>0.07 (+2.35%)</td><td>0.01 <b>(-67.20%)</b></td><td>219.20 (-2.32%)</td><td>203.68 (+13.22%)</td><td>207.00 (+13.18%)</td><td>175.90 <b>(+40.72%)</b></td><td>16.76 <b>(-54.18%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.40 (n/a)</td><td>179.90 (n/a)</td><td>182.90 (n/a)</td><td>125.00 (n/a)</td><td>36.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (+11.39%)</td><td>0.11 (-6.94%)</td><td>0.11 (-13.08%)</td><td>0.07 <b>(-24.75%)</b></td><td>0.03 <b>(+44.10%)</b></td><td>264.10 <b>(+32.91%)</b></td><td>182.30 (+11.09%)</td><td>173.90 (+15.01%)</td><td>124.00 (-10.21%)</td><td>50.71 <b>(+74.57%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>198.70 (n/a)</td><td>164.10 (n/a)</td><td>151.20 (n/a)</td><td>138.10 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (+2.35%)</td><td>0.10 (+6.17%)</td><td>0.09 (+1.29%)</td><td>0.07 <b>(+47.11%)</b></td><td>0.03 (-18.09%)</td><td>231.90 <b>(-32.03%)</b></td><td>174.00 (-11.78%)</td><td>176.50 (-1.29%)</td><td>127.50 (-2.30%)</td><td>45.60 <b>(-47.03%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>341.20 (n/a)</td><td>197.24 (n/a)</td><td>178.80 (n/a)</td><td>130.50 (n/a)</td><td>86.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (+6.95%)</td><td>0.11 (+2.95%)</td><td>0.11 (+3.07%)</td><td>0.09 (-3.39%)</td><td>0.02 <b>(+28.53%)</b></td><td>204.10 (+3.50%)</td><td>164.12 (-2.23%)</td><td>160.70 (-2.96%)</td><td>137.00 (-6.48%)</td><td>25.07 <b>(+26.32%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>167.86 (n/a)</td><td>165.60 (n/a)</td><td>146.50 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 <b>(+42.90%)</b></td><td>0.09 (+15.97%)</td><td>0.09 (+10.27%)</td><td>0.08 (+5.48%)</td><td>0.02 <b>(+257.53%)</b></td><td>205.60 (-5.17%)</td><td>178.88 (-11.67%)</td><td>188.80 (-9.32%)</td><td>131.10 <b>(-30.04%)</b></td><td>30.57 <b>(+138.55%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>202.52 (n/a)</td><td>208.20 (n/a)</td><td>187.40 (n/a)</td><td>12.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (+1.93%)</td><td>0.08 (-11.30%)</td><td>0.08 (-16.02%)</td><td>0.07 (-9.21%)</td><td>0.02 <b>(+34.98%)</b></td><td>253.70 (+10.16%)</td><td>213.24 (+14.31%)</td><td>210.70 (+19.04%)</td><td>158.20 (-1.86%)</td><td>38.61 <b>(+44.27%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>230.30 (n/a)</td><td>186.54 (n/a)</td><td>177.00 (n/a)</td><td>161.20 (n/a)</td><td>26.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.10 (+4.45%)</td><td>0.09 (-3.12%)</td><td>0.09 (-2.22%)</td><td>0.08 (-12.98%)</td><td>0.01 <b>(+164.56%)</b></td><td>215.50 (+14.93%)</td><td>187.34 (+4.36%)</td><td>184.30 (+2.22%)</td><td>159.80 (-4.25%)</td><td>23.38 <b>(+195.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>187.50 (n/a)</td><td>179.52 (n/a)</td><td>180.30 (n/a)</td><td>166.90 (n/a)</td><td>7.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.08 <b>(-21.39%)</b></td><td>0.08 (-2.68%)</td><td>0.08 (+3.42%)</td><td>0.08 <b>(+41.94%)</b></td><td>0.00 <b>(-86.98%)</b></td><td>228.00 <b>(-29.54%)</b></td><td>221.50 (-4.90%)</td><td>223.90 (-3.28%)</td><td>206.20 <b>(+27.21%)</b></td><td>8.80 <b>(-87.78%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>323.60 (n/a)</td><td>232.92 (n/a)</td><td>231.50 (n/a)</td><td>162.10 (n/a)</td><td>72.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.09 (+4.33%)</td><td>0.08 (+0.41%)</td><td>0.08 (+1.78%)</td><td>0.06 (-7.47%)</td><td>0.01 <b>(+32.82%)</b></td><td>277.70 (+8.10%)</td><td>221.52 (+0.41%)</td><td>218.00 (-1.76%)</td><td>185.70 (-4.13%)</td><td>34.22 <b>(+40.90%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>256.90 (n/a)</td><td>220.62 (n/a)</td><td>221.90 (n/a)</td><td>193.70 (n/a)</td><td>24.29 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (+4.40%)</td><td>0.20 (-3.37%)</td><td>0.19 (-9.52%)</td><td>0.17 (+19.07%)</td><td>0.03 <b>(-22.30%)</b></td><td>197.20 (-16.05%)</td><td>166.50 (+1.14%)</td><td>169.40 (+10.50%)</td><td>127.00 (-4.22%)</td><td>25.19 <b>(-39.85%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>234.90 (n/a)</td><td>164.62 (n/a)</td><td>153.30 (n/a)</td><td>132.60 (n/a)</td><td>41.88 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (-12.77%)</td><td>0.21 (+10.43%)</td><td>0.21 <b>(+21.09%)</b></td><td>0.19 <b>(+52.24%)</b></td><td>0.02 <b>(-68.75%)</b></td><td>171.40 <b>(-34.33%)</b></td><td>155.94 (-16.18%)</td><td>157.00 (-17.41%)</td><td>134.40 (+14.68%)</td><td>13.59 <b>(-76.62%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>261.00 (n/a)</td><td>186.04 (n/a)</td><td>190.10 (n/a)</td><td>117.20 (n/a)</td><td>58.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.27 (-0.46%)</td><td>0.25 (+9.33%)</td><td>0.26 (+14.25%)</td><td>0.21 (+10.44%)</td><td>0.02 <b>(-36.78%)</b></td><td>195.10 (-9.47%)</td><td>167.10 (-9.72%)</td><td>158.90 (-12.50%)</td><td>153.20 (+0.46%)</td><td>16.78 <b>(-43.12%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>215.50 (n/a)</td><td>185.10 (n/a)</td><td>181.60 (n/a)</td><td>152.50 (n/a)</td><td>29.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (-10.82%)</td><td>0.20 (-6.99%)</td><td>0.19 (-15.31%)</td><td>0.19 (+8.89%)</td><td>0.02 <b>(-44.62%)</b></td><td>177.10 (-8.14%)</td><td>163.20 (+5.32%)</td><td>174.50 (+18.06%)</td><td>138.50 (+12.15%)</td><td>17.48 <b>(-42.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>192.80 (n/a)</td><td>154.96 (n/a)</td><td>147.80 (n/a)</td><td>123.50 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.34 (+6.60%)</td><td>0.24 (+11.21%)</td><td>0.21 (+11.74%)</td><td>0.16 <b>(+21.97%)</b></td><td>0.07 (-3.51%)</td><td>248.50 (-18.01%)</td><td>182.74 (-11.97%)</td><td>194.70 (-10.48%)</td><td>122.30 (-6.14%)</td><td>47.75 <b>(-26.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>303.10 (n/a)</td><td>207.60 (n/a)</td><td>217.50 (n/a)</td><td>130.30 (n/a)</td><td>64.74 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (-6.86%)</td><td>0.21 (-12.30%)</td><td>0.22 (-11.45%)</td><td>0.16 (-13.89%)</td><td>0.04 (+12.01%)</td><td>211.10 (+16.12%)</td><td>160.20 (+15.37%)</td><td>148.60 (+12.92%)</td><td>127.20 (+7.43%)</td><td>34.45 <b>(+36.56%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>181.80 (n/a)</td><td>138.86 (n/a)</td><td>131.60 (n/a)</td><td>118.40 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.25 (-4.13%)</td><td>0.21 (-1.09%)</td><td>0.22 (+12.67%)</td><td>0.17 (+1.54%)</td><td>0.04 (-11.53%)</td><td>222.30 (-1.51%)</td><td>182.88 (+0.62%)</td><td>170.40 (-11.25%)</td><td>147.90 (+4.30%)</td><td>34.74 (-4.04%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>225.70 (n/a)</td><td>181.76 (n/a)</td><td>192.00 (n/a)</td><td>141.80 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.27 (-2.73%)</td><td>0.21 (-5.05%)</td><td>0.18 <b>(-22.04%)</b></td><td>0.18 (+6.72%)</td><td>0.04 (-15.98%)</td><td>186.90 (-6.32%)</td><td>161.12 (+3.92%)</td><td>178.90 <b>(+28.24%)</b></td><td>123.20 (+2.84%)</td><td>28.69 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>199.50 (n/a)</td><td>155.04 (n/a)</td><td>139.50 (n/a)</td><td>119.80 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.29 <b>(+21.75%)</b></td><td>0.22 (+9.14%)</td><td>0.21 (+3.63%)</td><td>0.15 (-7.66%)</td><td>0.05 <b>(+65.56%)</b></td><td>252.50 (+8.28%)</td><td>176.76 (-5.68%)</td><td>174.60 (-3.48%)</td><td>129.20 (-17.92%)</td><td>46.72 <b>(+51.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>233.20 (n/a)</td><td>187.40 (n/a)</td><td>180.90 (n/a)</td><td>157.40 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.31 <b>(+21.61%)</b></td><td>0.21 (-2.82%)</td><td>0.20 (-12.26%)</td><td>0.16 (+4.67%)</td><td>0.06 <b>(+50.42%)</b></td><td>201.20 (-4.46%)</td><td>162.82 (+5.36%)</td><td>161.20 (+13.92%)</td><td>106.90 (-17.77%)</td><td>39.75 (+19.88%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.60 (n/a)</td><td>154.54 (n/a)</td><td>141.50 (n/a)</td><td>130.00 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (+11.14%)</td><td>0.19 (+9.24%)</td><td>0.18 (+3.64%)</td><td>0.15 <b>(+35.08%)</b></td><td>0.04 (-11.00%)</td><td>226.20 <b>(-25.96%)</b></td><td>190.10 (-10.70%)</td><td>194.60 (-3.52%)</td><td>142.70 (-10.03%)</td><td>36.00 <b>(-39.27%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>305.50 (n/a)</td><td>212.88 (n/a)</td><td>201.70 (n/a)</td><td>158.60 (n/a)</td><td>59.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (+5.18%)</td><td>0.17 (-10.48%)</td><td>0.16 (-18.15%)</td><td>0.15 (-10.39%)</td><td>0.03 <b>(+76.91%)</b></td><td>217.70 (+11.58%)</td><td>192.80 (+13.48%)</td><td>206.80 <b>(+22.15%)</b></td><td>144.00 (-4.89%)</td><td>29.84 <b>(+83.29%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>169.90 (n/a)</td><td>169.30 (n/a)</td><td>151.40 (n/a)</td><td>16.28 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (+0.17%)</td><td>0.17 (-8.19%)</td><td>0.16 (-16.83%)</td><td>0.15 (-11.01%)</td><td>0.03 <b>(+65.82%)</b></td><td>234.90 (+12.39%)</td><td>205.76 (+10.62%)</td><td>222.90 <b>(+20.23%)</b></td><td>161.80 (-0.19%)</td><td>33.48 <b>(+88.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>209.00 (n/a)</td><td>186.00 (n/a)</td><td>185.40 (n/a)</td><td>162.10 (n/a)</td><td>17.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (+11.62%)</td><td>0.17 (+8.82%)</td><td>0.17 (+11.51%)</td><td>0.14 (+3.33%)</td><td>0.03 <b>(+37.41%)</b></td><td>235.80 (-3.24%)</td><td>198.34 (-7.47%)</td><td>196.10 (-10.33%)</td><td>159.30 (-10.40%)</td><td>28.75 <b>(+20.84%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>243.70 (n/a)</td><td>214.36 (n/a)</td><td>218.70 (n/a)</td><td>177.80 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 <b>(-25.31%)</b></td><td>0.10 <b>(-22.33%)</b></td><td>0.10 (-14.50%)</td><td>0.09 <b>(-22.18%)</b></td><td>0.01 <b>(-52.80%)</b></td><td>223.70 <b>(+28.49%)</b></td><td>196.62 <b>(+27.36%)</b></td><td>196.60 (+16.95%)</td><td>172.70 <b>(+33.88%)</b></td><td>18.36 (-17.79%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>174.10 (n/a)</td><td>154.38 (n/a)</td><td>168.10 (n/a)</td><td>129.00 (n/a)</td><td>22.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (+6.09%)</td><td>0.13 (+12.77%)</td><td>0.12 (+3.65%)</td><td>0.11 <b>(+30.73%)</b></td><td>0.02 (-14.51%)</td><td>182.70 <b>(-23.49%)</b></td><td>159.78 (-13.07%)</td><td>173.50 (-3.50%)</td><td>121.10 (-5.76%)</td><td>26.03 <b>(-37.67%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>238.80 (n/a)</td><td>183.80 (n/a)</td><td>179.80 (n/a)</td><td>128.50 (n/a)</td><td>41.77 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (-4.72%)</td><td>0.13 (+2.18%)</td><td>0.13 (+2.73%)</td><td>0.10 (+5.59%)</td><td>0.02 <b>(-21.52%)</b></td><td>212.30 (-5.27%)</td><td>166.20 (-3.44%)</td><td>152.10 (-2.62%)</td><td>143.20 (+4.99%)</td><td>28.86 <b>(-22.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>224.10 (n/a)</td><td>172.12 (n/a)</td><td>156.20 (n/a)</td><td>136.40 (n/a)</td><td>37.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (+6.06%)</td><td>0.13 (-2.59%)</td><td>0.14 (+9.62%)</td><td>0.09 (+4.12%)</td><td>0.03 (+11.03%)</td><td>227.80 (-3.92%)</td><td>169.66 (+3.65%)</td><td>146.50 (-8.78%)</td><td>120.20 (-5.73%)</td><td>47.48 (+6.12%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>237.10 (n/a)</td><td>163.68 (n/a)</td><td>160.60 (n/a)</td><td>127.50 (n/a)</td><td>44.74 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (-5.88%)</td><td>0.12 (-2.63%)</td><td>0.10 (-12.58%)</td><td>0.09 (-4.52%)</td><td>0.03 (+2.61%)</td><td>227.60 (+4.69%)</td><td>187.68 (+3.83%)</td><td>212.00 (+14.41%)</td><td>125.90 (+6.24%)</td><td>45.65 <b>(+21.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>217.40 (n/a)</td><td>180.76 (n/a)</td><td>185.30 (n/a)</td><td>118.50 (n/a)</td><td>37.43 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (-5.53%)</td><td>0.12 (+1.92%)</td><td>0.12 (+8.21%)</td><td>0.10 (-2.73%)</td><td>0.01 (-9.42%)</td><td>211.40 (+2.77%)</td><td>177.52 (-2.07%)</td><td>167.10 (-7.58%)</td><td>156.70 (+5.81%)</td><td>23.25 (-2.87%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>205.70 (n/a)</td><td>181.28 (n/a)</td><td>180.80 (n/a)</td><td>148.10 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 (-19.74%)</td><td>0.10 (-18.40%)</td><td>0.10 (-17.78%)</td><td>0.08 <b>(-21.32%)</b></td><td>0.01 (-19.33%)</td><td>250.80 <b>(+27.05%)</b></td><td>207.82 <b>(+22.58%)</b></td><td>207.30 <b>(+21.58%)</b></td><td>174.90 <b>(+24.66%)</b></td><td>29.36 <b>(+27.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>197.40 (n/a)</td><td>169.54 (n/a)</td><td>170.50 (n/a)</td><td>140.30 (n/a)</td><td>23.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 <b>(+57.70%)</b></td><td>0.12 (+18.56%)</td><td>0.10 (-0.97%)</td><td>0.09 (+3.87%)</td><td>0.03 <b>(+443.10%)</b></td><td>221.60 (-3.69%)</td><td>187.30 (-11.34%)</td><td>210.40 (+0.96%)</td><td>123.80 <b>(-36.58%)</b></td><td>43.88 <b>(+240.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>211.26 (n/a)</td><td>208.40 (n/a)</td><td>195.20 (n/a)</td><td>12.90 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 (-15.38%)</td><td>0.13 (-12.94%)</td><td>0.14 (+1.65%)</td><td>0.07 <b>(-50.28%)</b></td><td>0.03 <b>(+87.78%)</b></td><td>374.80 <b>(+101.18%)</b></td><td>213.74 <b>(+24.98%)</b></td><td>176.70 (-1.61%)</td><td>165.40 (+18.14%)</td><td>90.17 <b>(+365.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>186.30 (n/a)</td><td>171.02 (n/a)</td><td>179.60 (n/a)</td><td>140.00 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 <b>(+29.73%)</b></td><td>0.13 (+16.05%)</td><td>0.13 (+1.35%)</td><td>0.10 <b>(+61.76%)</b></td><td>0.03 (-3.49%)</td><td>238.80 <b>(-38.18%)</b></td><td>191.78 (-18.01%)</td><td>183.60 (-1.34%)</td><td>133.20 <b>(-22.92%)</b></td><td>41.46 <b>(-53.97%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>386.30 (n/a)</td><td>233.90 (n/a)</td><td>186.10 (n/a)</td><td>172.80 (n/a)</td><td>90.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (-11.01%)</td><td>0.14 (-13.58%)</td><td>0.13 (-15.49%)</td><td>0.10 <b>(-28.83%)</b></td><td>0.03 <b>(+49.83%)</b></td><td>246.40 <b>(+40.48%)</b></td><td>186.62 (+18.55%)</td><td>191.00 (+18.34%)</td><td>148.00 (+12.38%)</td><td>39.60 <b>(+133.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>175.40 (n/a)</td><td>157.42 (n/a)</td><td>161.40 (n/a)</td><td>131.70 (n/a)</td><td>16.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (-12.38%)</td><td>0.12 <b>(-26.31%)</b></td><td>0.11 <b>(-29.04%)</b></td><td>0.09 <b>(-33.24%)</b></td><td>0.03 (+16.99%)</td><td>281.00 <b>(+49.79%)</b></td><td>213.04 <b>(+39.21%)</b></td><td>219.50 <b>(+40.98%)</b></td><td>146.70 (+14.07%)</td><td>49.05 <b>(+100.98%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>187.60 (n/a)</td><td>153.04 (n/a)</td><td>155.70 (n/a)</td><td>128.60 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (-9.44%)</td><td>0.16 (+7.27%)</td><td>0.15 (+14.01%)</td><td>0.14 <b>(+36.75%)</b></td><td>0.02 <b>(-47.03%)</b></td><td>176.40 <b>(-26.87%)</b></td><td>160.52 (-11.47%)</td><td>165.70 (-12.28%)</td><td>124.40 (+10.38%)</td><td>21.18 <b>(-56.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>241.20 (n/a)</td><td>181.32 (n/a)</td><td>188.90 (n/a)</td><td>112.70 (n/a)</td><td>48.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.16 (-15.90%)</td><td>0.14 (-6.64%)</td><td>0.13 (-9.40%)</td><td>0.11 (-2.36%)</td><td>0.02 <b>(-30.82%)</b></td><td>214.90 (+2.43%)</td><td>180.78 (+5.69%)</td><td>190.80 (+10.35%)</td><td>153.00 (+18.88%)</td><td>26.75 (-18.53%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>209.80 (n/a)</td><td>171.04 (n/a)</td><td>172.90 (n/a)</td><td>128.70 (n/a)</td><td>32.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.17 (+14.35%)</td><td>0.14 (+17.26%)</td><td>0.14 (+17.69%)</td><td>0.11 (+14.40%)</td><td>0.02 <b>(+22.30%)</b></td><td>222.30 (-12.58%)</td><td>180.78 (-14.44%)</td><td>181.30 (-15.04%)</td><td>143.10 (-12.58%)</td><td>30.86 (-4.82%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>254.30 (n/a)</td><td>211.28 (n/a)</td><td>213.40 (n/a)</td><td>163.70 (n/a)</td><td>32.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 <b>(+34.11%)</b></td><td>0.12 (+7.67%)</td><td>0.11 (-6.50%)</td><td>0.10 (+16.50%)</td><td>0.04 <b>(+79.08%)</b></td><td>249.60 (-14.14%)</td><td>211.40 (-4.78%)</td><td>225.70 (+6.97%)</td><td>131.60 <b>(-25.44%)</b></td><td>45.97 (+6.66%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>290.70 (n/a)</td><td>222.02 (n/a)</td><td>211.00 (n/a)</td><td>176.50 (n/a)</td><td>43.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.13 (-10.61%)</td><td>0.11 (-3.34%)</td><td>0.11 (+4.28%)</td><td>0.09 (-7.97%)</td><td>0.02 (-9.94%)</td><td>204.00 (+8.63%)</td><td>175.36 (+3.47%)</td><td>172.30 (-4.12%)</td><td>147.20 (+11.85%)</td><td>25.23 (+12.85%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>187.80 (n/a)</td><td>169.48 (n/a)</td><td>179.70 (n/a)</td><td>131.60 (n/a)</td><td>22.36 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (-0.27%)</td><td>0.12 (+19.40%)</td><td>0.12 (+15.58%)</td><td>0.10 <b>(+80.47%)</b></td><td>0.01 <b>(-51.18%)</b></td><td>180.80 <b>(-44.59%)</b></td><td>156.90 <b>(-22.11%)</b></td><td>159.10 (-13.49%)</td><td>134.50 (+0.22%)</td><td>18.41 <b>(-74.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>326.30 (n/a)</td><td>201.44 (n/a)</td><td>183.90 (n/a)</td><td>134.20 (n/a)</td><td>72.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (-13.37%)</td><td>0.09 (-13.68%)</td><td>0.09 (-10.97%)</td><td>0.08 <b>(-21.81%)</b></td><td>0.01 (+2.86%)</td><td>239.90 <b>(+27.88%)</b></td><td>200.12 (+16.44%)</td><td>205.00 (+12.33%)</td><td>168.60 (+15.48%)</td><td>27.58 <b>(+49.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>171.86 (n/a)</td><td>182.50 (n/a)</td><td>146.00 (n/a)</td><td>18.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.14 (+10.97%)</td><td>0.12 (+16.52%)</td><td>0.11 (+13.36%)</td><td>0.11 (+13.53%)</td><td>0.02 (+8.86%)</td><td>173.00 (-11.91%)</td><td>152.88 (-14.23%)</td><td>161.60 (-11.74%)</td><td>128.30 (-9.90%)</td><td>18.94 (-13.34%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>178.24 (n/a)</td><td>183.10 (n/a)</td><td>142.40 (n/a)</td><td>21.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.15 <b>(+30.03%)</b></td><td>0.10 (-4.16%)</td><td>0.09 (-14.17%)</td><td>0.06 <b>(-31.54%)</b></td><td>0.03 <b>(+259.25%)</b></td><td>288.90 <b>(+46.06%)</b></td><td>201.96 (+12.81%)</td><td>210.50 (+16.56%)</td><td>121.00 <b>(-23.08%)</b></td><td>62.54 <b>(+295.35%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>197.80 (n/a)</td><td>179.02 (n/a)</td><td>180.60 (n/a)</td><td>157.30 (n/a)</td><td>15.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (-7.94%)</td><td>0.09 (-8.67%)</td><td>0.10 (-3.31%)</td><td>0.07 (-11.72%)</td><td>0.01 (+8.61%)</td><td>253.60 (+13.26%)</td><td>205.06 (+10.14%)</td><td>190.70 (+3.42%)</td><td>170.70 (+8.59%)</td><td>32.68 <b>(+33.81%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>223.90 (n/a)</td><td>186.18 (n/a)</td><td>184.40 (n/a)</td><td>157.20 (n/a)</td><td>24.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 <b>(-22.62%)</b></td><td>0.10 (-7.86%)</td><td>0.11 (+14.49%)</td><td>0.07 (-17.32%)</td><td>0.02 <b>(-29.77%)</b></td><td>266.80 <b>(+20.94%)</b></td><td>198.14 (+7.66%)</td><td>175.50 (-12.69%)</td><td>168.30 <b>(+29.26%)</b></td><td>40.97 (+11.27%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>220.60 (n/a)</td><td>184.04 (n/a)</td><td>201.00 (n/a)</td><td>130.20 (n/a)</td><td>36.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.12 <b>(-20.36%)</b></td><td>0.10 (-7.90%)</td><td>0.10 (+0.61%)</td><td>0.08 <b>(+23.01%)</b></td><td>0.01 <b>(-58.11%)</b></td><td>219.90 (-18.71%)</td><td>191.46 (+2.74%)</td><td>186.40 (-0.64%)</td><td>158.20 <b>(+25.56%)</b></td><td>23.84 <b>(-57.09%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>270.50 (n/a)</td><td>186.36 (n/a)</td><td>187.60 (n/a)</td><td>126.00 (n/a)</td><td>55.55 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.79 (+3.89%)</td><td>0.62 (+3.52%)</td><td>0.62 (+0.57%)</td><td>0.44 (+17.06%)</td><td>0.14 (-15.06%)</td><td>222.10 (-14.54%)</td><td>164.08 (-5.82%)</td><td>159.00 (-0.56%)</td><td>124.80 (-3.70%)</td><td>38.32 <b>(-28.76%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.76 (n/a)</td><td>0.60 (n/a)</td><td>0.61 (n/a)</td><td>0.38 (n/a)</td><td>0.16 (n/a)</td><td>259.90 (n/a)</td><td>174.22 (n/a)</td><td>159.90 (n/a)</td><td>129.60 (n/a)</td><td>53.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.66 (-15.55%)</td><td>0.53 (-19.36%)</td><td>0.51 <b>(-23.02%)</b></td><td>0.42 (+5.46%)</td><td>0.09 <b>(-42.53%)</b></td><td>232.10 (-5.19%)</td><td>191.08 (+19.47%)</td><td>191.00 <b>(+29.93%)</b></td><td>148.70 (+18.39%)</td><td>30.85 <b>(-37.20%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.78 (n/a)</td><td>0.65 (n/a)</td><td>0.67 (n/a)</td><td>0.40 (n/a)</td><td>0.15 (n/a)</td><td>244.80 (n/a)</td><td>159.94 (n/a)</td><td>147.00 (n/a)</td><td>125.60 (n/a)</td><td>49.13 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 (+0.90%)</td><td>0.55 (-0.30%)</td><td>0.50 (-4.20%)</td><td>0.43 (-0.60%)</td><td>0.15 (+5.30%)</td><td>229.70 (+0.61%)</td><td>186.98 (+0.84%)</td><td>197.10 (+4.40%)</td><td>123.00 (-0.89%)</td><td>43.31 (+6.06%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.79 (n/a)</td><td>0.56 (n/a)</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.14 (n/a)</td><td>228.30 (n/a)</td><td>185.42 (n/a)</td><td>188.80 (n/a)</td><td>124.10 (n/a)</td><td>40.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.61 (-12.99%)</td><td>0.50 (-7.48%)</td><td>0.47 (-2.66%)</td><td>0.42 (-6.24%)</td><td>0.07 <b>(-35.09%)</b></td><td>233.00 (+6.68%)</td><td>199.36 (+6.40%)</td><td>209.60 (+2.75%)</td><td>162.20 (+14.95%)</td><td>27.74 <b>(-22.34%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.70 (n/a)</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.45 (n/a)</td><td>0.11 (n/a)</td><td>218.40 (n/a)</td><td>187.36 (n/a)</td><td>204.00 (n/a)</td><td>141.10 (n/a)</td><td>35.72 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.43 <b>(-25.98%)</b></td><td>0.40 <b>(-22.20%)</b></td><td>0.42 (-15.14%)</td><td>0.30 <b>(-34.03%)</b></td><td>0.05 <b>(+22.43%)</b></td><td>242.90 <b>(+51.62%)</b></td><td>189.44 <b>(+30.02%)</b></td><td>174.40 (+17.84%)</td><td>172.60 <b>(+35.05%)</b></td><td>30.21 <b>(+156.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.58 (n/a)</td><td>0.51 (n/a)</td><td>0.50 (n/a)</td><td>0.46 (n/a)</td><td>0.04 (n/a)</td><td>160.20 (n/a)</td><td>145.70 (n/a)</td><td>148.00 (n/a)</td><td>127.80 (n/a)</td><td>11.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.46 <b>(-20.41%)</b></td><td>0.43 (-4.81%)</td><td>0.42 (+5.16%)</td><td>0.40 (+17.49%)</td><td>0.03 <b>(-73.34%)</b></td><td>183.40 (-14.86%)</td><td>172.90 (+1.35%)</td><td>173.90 (-4.87%)</td><td>159.20 <b>(+25.65%)</b></td><td>10.76 <b>(-70.64%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>215.40 (n/a)</td><td>170.60 (n/a)</td><td>182.80 (n/a)</td><td>126.70 (n/a)</td><td>36.65 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.48 (-16.70%)</td><td>0.41 (-5.37%)</td><td>0.39 (+1.04%)</td><td>0.36 (+19.74%)</td><td>0.05 <b>(-61.09%)</b></td><td>206.00 (-16.50%)</td><td>181.14 (-0.60%)</td><td>191.30 (-1.03%)</td><td>153.10 (+19.98%)</td><td>21.95 <b>(-58.80%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.58 (n/a)</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.13 (n/a)</td><td>246.70 (n/a)</td><td>182.24 (n/a)</td><td>193.30 (n/a)</td><td>127.60 (n/a)</td><td>53.28 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.49 (+7.21%)</td><td>0.38 (+0.13%)</td><td>0.40 (+4.60%)</td><td>0.27 (-9.36%)</td><td>0.10 <b>(+57.31%)</b></td><td>277.20 (+10.31%)</td><td>207.30 (+3.25%)</td><td>185.20 (-4.39%)</td><td>149.40 (-6.74%)</td><td>54.92 <b>(+64.57%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.46 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.06 (n/a)</td><td>251.30 (n/a)</td><td>200.78 (n/a)</td><td>193.70 (n/a)</td><td>160.20 (n/a)</td><td>33.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.30 (+7.85%)</td><td>0.23 (+1.05%)</td><td>0.21 (-10.20%)</td><td>0.19 (-0.77%)</td><td>0.04 <b>(+29.14%)</b></td><td>195.90 (+0.77%)</td><td>166.32 (-0.16%)</td><td>178.20 (+11.37%)</td><td>124.80 (-7.28%)</td><td>28.58 (+18.06%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>194.40 (n/a)</td><td>166.58 (n/a)</td><td>160.00 (n/a)</td><td>134.60 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.27 (-1.70%)</td><td>0.23 (-8.80%)</td><td>0.23 (-11.74%)</td><td>0.19 (-8.39%)</td><td>0.03 <b>(+28.79%)</b></td><td>192.50 (+9.13%)</td><td>164.44 (+10.42%)</td><td>162.50 (+13.32%)</td><td>135.80 (+1.72%)</td><td>22.89 <b>(+40.36%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>176.40 (n/a)</td><td>148.92 (n/a)</td><td>143.40 (n/a)</td><td>133.50 (n/a)</td><td>16.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 <b>(-21.53%)</b></td><td>0.19 (-13.61%)</td><td>0.19 (-6.78%)</td><td>0.17 (-7.44%)</td><td>0.02 <b>(-52.88%)</b></td><td>211.20 (+8.09%)</td><td>193.60 (+13.80%)</td><td>191.60 (+7.28%)</td><td>166.50 <b>(+27.49%)</b></td><td>18.31 <b>(-35.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>195.40 (n/a)</td><td>170.12 (n/a)</td><td>178.60 (n/a)</td><td>130.60 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.23 (+7.09%)</td><td>0.19 (+4.06%)</td><td>0.19 (+6.21%)</td><td>0.15 (-4.43%)</td><td>0.03 <b>(+25.32%)</b></td><td>242.70 (+4.66%)</td><td>194.18 (-3.26%)</td><td>192.40 (-5.87%)</td><td>157.80 (-6.63%)</td><td>30.71 <b>(+25.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>231.90 (n/a)</td><td>200.72 (n/a)</td><td>204.40 (n/a)</td><td>169.00 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (+7.45%)</td><td>0.23 (+19.08%)</td><td>0.24 <b>(+32.39%)</b></td><td>0.15 (+0.11%)</td><td>0.04 <b>(+27.65%)</b></td><td>241.90 (-0.08%)</td><td>169.60 (-14.84%)</td><td>155.90 <b>(-24.47%)</b></td><td>142.50 (-6.92%)</td><td>40.83 <b>(+25.84%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>242.10 (n/a)</td><td>199.16 (n/a)</td><td>206.40 (n/a)</td><td>153.10 (n/a)</td><td>32.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.30 (+12.18%)</td><td>0.21 (-7.92%)</td><td>0.22 (-1.03%)</td><td>0.10 <b>(-41.95%)</b></td><td>0.08 <b>(+107.49%)</b></td><td>368.00 <b>(+72.28%)</b></td><td>206.22 <b>(+23.87%)</b></td><td>167.60 (+1.02%)</td><td>121.10 (-10.82%)</td><td>100.33 <b>(+224.55%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>213.60 (n/a)</td><td>166.48 (n/a)</td><td>165.90 (n/a)</td><td>135.80 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.26 (+4.02%)</td><td>0.21 (+1.78%)</td><td>0.20 (+1.37%)</td><td>0.17 (-0.46%)</td><td>0.04 <b>(+24.60%)</b></td><td>219.30 (+0.46%)</td><td>184.44 (-0.72%)</td><td>187.60 (-1.37%)</td><td>143.40 (-3.89%)</td><td>35.24 <b>(+22.28%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>218.30 (n/a)</td><td>185.78 (n/a)</td><td>190.20 (n/a)</td><td>149.20 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 <b>(+28.95%)</b></td><td>0.19 (-0.71%)</td><td>0.18 (-9.58%)</td><td>0.15 (-10.76%)</td><td>0.05 <b>(+153.56%)</b></td><td>248.80 (+12.07%)</td><td>201.28 (+4.50%)</td><td>207.60 (+10.60%)</td><td>131.60 <b>(-22.45%)</b></td><td>42.96 <b>(+107.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>222.00 (n/a)</td><td>192.62 (n/a)</td><td>187.70 (n/a)</td><td>169.70 (n/a)</td><td>20.67 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.29 (-8.57%)</td><td>0.24 (-5.56%)</td><td>0.25 (+3.22%)</td><td>0.18 (-8.53%)</td><td>0.04 (-3.45%)</td><td>226.20 (+9.33%)</td><td>173.74 (+6.21%)</td><td>162.00 (-3.11%)</td><td>143.30 (+9.39%)</td><td>33.55 (+15.90%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>206.90 (n/a)</td><td>163.58 (n/a)</td><td>167.20 (n/a)</td><td>131.00 (n/a)</td><td>28.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.30 (+0.40%)</td><td>0.25 (-0.51%)</td><td>0.26 (+3.06%)</td><td>0.19 (-11.74%)</td><td>0.05 <b>(+58.38%)</b></td><td>213.20 (+13.28%)</td><td>166.94 (+2.48%)</td><td>156.10 (-2.98%)</td><td>136.40 (-0.37%)</td><td>33.32 <b>(+77.36%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>188.20 (n/a)</td><td>162.90 (n/a)</td><td>160.90 (n/a)</td><td>136.90 (n/a)</td><td>18.79 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.34 <b>(+22.04%)</b></td><td>0.26 (+8.99%)</td><td>0.26 (+7.25%)</td><td>0.18 (-7.34%)</td><td>0.07 <b>(+119.02%)</b></td><td>221.90 (+7.93%)</td><td>169.34 (-4.33%)</td><td>158.40 (-6.77%)</td><td>121.10 (-18.06%)</td><td>44.29 <b>(+97.19%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>205.60 (n/a)</td><td>177.00 (n/a)</td><td>169.90 (n/a)</td><td>147.80 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.25 (+3.45%)</td><td>0.22 (+13.32%)</td><td>0.23 (+12.62%)</td><td>0.15 <b>(+21.35%)</b></td><td>0.04 (-11.43%)</td><td>276.20 (-17.58%)</td><td>195.78 (-13.48%)</td><td>177.40 (-11.21%)</td><td>162.30 (-3.34%)</td><td>45.93 <b>(-29.34%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>335.10 (n/a)</td><td>226.28 (n/a)</td><td>199.80 (n/a)</td><td>167.90 (n/a)</td><td>65.00 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.39 <b>(+45.31%)</b></td><td>0.29 <b>(+24.60%)</b></td><td>0.27 (+11.31%)</td><td>0.22 <b>(+31.10%)</b></td><td>0.07 <b>(+73.16%)</b></td><td>182.20 <b>(-23.73%)</b></td><td>147.88 (-18.24%)</td><td>149.90 (-10.13%)</td><td>104.40 <b>(-31.18%)</b></td><td>35.06 (-4.92%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>238.90 (n/a)</td><td>180.86 (n/a)</td><td>166.80 (n/a)</td><td>151.70 (n/a)</td><td>36.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.32 (+17.43%)</td><td>0.29 <b>(+22.66%)</b></td><td>0.29 <b>(+20.17%)</b></td><td>0.24 <b>(+26.34%)</b></td><td>0.03 (-4.27%)</td><td>172.80 <b>(-20.84%)</b></td><td>144.46 (-18.94%)</td><td>141.30 (-16.78%)</td><td>128.90 (-14.86%)</td><td>16.81 <b>(-34.88%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>218.30 (n/a)</td><td>178.22 (n/a)</td><td>169.80 (n/a)</td><td>151.40 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.21 (-18.57%)</td><td>0.20 (-5.82%)</td><td>0.20 (-13.65%)</td><td>0.19 <b>(+30.38%)</b></td><td>0.01 <b>(-84.44%)</b></td><td>213.70 <b>(-23.30%)</b></td><td>202.56 (+2.13%)</td><td>201.60 (+15.80%)</td><td>194.50 <b>(+22.79%)</b></td><td>6.94 <b>(-85.59%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>278.60 (n/a)</td><td>198.34 (n/a)</td><td>174.10 (n/a)</td><td>158.40 (n/a)</td><td>48.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.34 (+13.16%)</td><td>0.25 (+6.07%)</td><td>0.23 (+11.59%)</td><td>0.19 (-2.15%)</td><td>0.06 <b>(+20.00%)</b></td><td>219.50 (+2.19%)</td><td>170.80 (-4.79%)</td><td>175.80 (-10.40%)</td><td>119.70 (-11.66%)</td><td>39.53 (+8.20%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>214.80 (n/a)</td><td>179.40 (n/a)</td><td>196.20 (n/a)</td><td>135.50 (n/a)</td><td>36.54 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (-4.58%)</td><td>0.20 (-2.17%)</td><td>0.20 (-0.93%)</td><td>0.17 (-4.35%)</td><td>0.03 (+11.05%)</td><td>199.30 (+4.51%)</td><td>173.32 (+2.65%)</td><td>171.70 (+0.94%)</td><td>146.20 (+4.80%)</td><td>23.63 <b>(+25.04%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>190.70 (n/a)</td><td>168.84 (n/a)</td><td>170.10 (n/a)</td><td>139.50 (n/a)</td><td>18.89 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (-13.77%)</td><td>0.17 (-16.00%)</td><td>0.21 (+3.31%)</td><td>0.10 <b>(-47.23%)</b></td><td>0.05 <b>(+99.78%)</b></td><td>345.80 <b>(+89.48%)</b></td><td>216.82 <b>(+28.43%)</b></td><td>169.70 (-3.19%)</td><td>159.70 (+15.98%)</td><td>78.96 <b>(+344.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>182.50 (n/a)</td><td>168.82 (n/a)</td><td>175.30 (n/a)</td><td>137.70 (n/a)</td><td>17.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 <b>(-33.48%)</b></td><td>0.17 <b>(-21.79%)</b></td><td>0.18 (-14.18%)</td><td>0.16 (-19.91%)</td><td>0.01 <b>(-63.49%)</b></td><td>221.80 <b>(+24.89%)</b></td><td>201.64 <b>(+26.31%)</b></td><td>198.80 (+16.53%)</td><td>187.50 <b>(+50.36%)</b></td><td>14.73 <b>(-30.96%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>177.60 (n/a)</td><td>159.64 (n/a)</td><td>170.60 (n/a)</td><td>124.70 (n/a)</td><td>21.34 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.19 <b>(-30.09%)</b></td><td>0.17 <b>(-22.01%)</b></td><td>0.18 (-13.41%)</td><td>0.14 <b>(-25.74%)</b></td><td>0.02 <b>(-27.47%)</b></td><td>251.30 <b>(+34.67%)</b></td><td>213.74 <b>(+28.33%)</b></td><td>196.70 (+15.50%)</td><td>186.30 <b>(+43.09%)</b></td><td>31.15 <b>(+44.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>186.60 (n/a)</td><td>166.56 (n/a)</td><td>170.30 (n/a)</td><td>130.20 (n/a)</td><td>21.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.29 <b>(+37.42%)</b></td><td>0.19 (+0.20%)</td><td>0.18 (-3.39%)</td><td>0.12 <b>(-26.13%)</b></td><td>0.06 <b>(+296.41%)</b></td><td>282.70 <b>(+35.39%)</b></td><td>199.54 (+6.95%)</td><td>190.50 (+3.48%)</td><td>121.50 <b>(-27.25%)</b></td><td>58.12 <b>(+279.22%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>208.80 (n/a)</td><td>186.58 (n/a)</td><td>184.10 (n/a)</td><td>167.00 (n/a)</td><td>15.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.28 (+14.99%)</td><td>0.23 <b>(+39.70%)</b></td><td>0.25 <b>(+60.28%)</b></td><td>0.18 <b>(+78.84%)</b></td><td>0.04 (-15.86%)</td><td>196.60 <b>(-44.07%)</b></td><td>157.88 <b>(-31.97%)</b></td><td>141.20 <b>(-37.58%)</b></td><td>126.60 (-12.99%)</td><td>31.50 <b>(-58.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>351.50 (n/a)</td><td>232.06 (n/a)</td><td>226.20 (n/a)</td><td>145.50 (n/a)</td><td>75.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.24 (+14.13%)</td><td>0.20 (+10.22%)</td><td>0.20 <b>(+21.49%)</b></td><td>0.15 (+8.81%)</td><td>0.04 (+3.14%)</td><td>235.40 (-8.08%)</td><td>182.16 (-9.56%)</td><td>174.70 (-17.71%)</td><td>142.20 (-12.38%)</td><td>34.64 (-12.22%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>256.10 (n/a)</td><td>201.42 (n/a)</td><td>212.30 (n/a)</td><td>162.30 (n/a)</td><td>39.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.22 (+1.98%)</td><td>0.18 (+10.10%)</td><td>0.18 (+13.57%)</td><td>0.15 (+3.72%)</td><td>0.03 (+8.12%)</td><td>229.00 (-3.58%)</td><td>192.36 (-8.97%)</td><td>192.50 (-11.94%)</td><td>161.40 (-1.94%)</td><td>28.72 (+4.68%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>237.50 (n/a)</td><td>211.32 (n/a)</td><td>218.60 (n/a)</td><td>164.60 (n/a)</td><td>27.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.02 (-0.95%)</td><td>0.81 (-3.17%)</td><td>0.78 (-7.25%)</td><td>0.69 <b>(+22.28%)</b></td><td>0.14 <b>(-20.91%)</b></td><td>189.50 (-18.21%)</td><td>165.50 (+1.24%)</td><td>167.70 (+7.78%)</td><td>128.00 (+0.95%)</td><td>25.33 <b>(-36.98%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.03 (n/a)</td><td>0.83 (n/a)</td><td>0.84 (n/a)</td><td>0.57 (n/a)</td><td>0.17 (n/a)</td><td>231.70 (n/a)</td><td>163.48 (n/a)</td><td>155.60 (n/a)</td><td>126.80 (n/a)</td><td>40.19 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 (-19.93%)</td><td>0.73 (-16.61%)</td><td>0.77 (-18.92%)</td><td>0.60 (-15.01%)</td><td>0.08 <b>(-38.27%)</b></td><td>219.30 (+17.65%)</td><td>180.66 (+18.93%)</td><td>170.20 <b>(+23.33%)</b></td><td>163.90 <b>(+24.92%)</b></td><td>22.63 (-7.63%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.00 (n/a)</td><td>0.88 (n/a)</td><td>0.95 (n/a)</td><td>0.70 (n/a)</td><td>0.13 (n/a)</td><td>186.40 (n/a)</td><td>151.90 (n/a)</td><td>138.00 (n/a)</td><td>131.20 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.73 <b>(-28.43%)</b></td><td>0.65 <b>(-24.93%)</b></td><td>0.64 <b>(-35.17%)</b></td><td>0.61 <b>(+22.33%)</b></td><td>0.05 <b>(-78.01%)</b></td><td>213.60 (-18.25%)</td><td>201.16 <b>(+24.33%)</b></td><td>204.70 <b>(+54.26%)</b></td><td>178.70 <b>(+39.72%)</b></td><td>14.11 <b>(-75.22%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.03 (n/a)</td><td>0.87 (n/a)</td><td>0.99 (n/a)</td><td>0.50 (n/a)</td><td>0.22 (n/a)</td><td>261.30 (n/a)</td><td>161.80 (n/a)</td><td>132.70 (n/a)</td><td>127.90 (n/a)</td><td>56.94 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-7.24%)</td><td>0.03 (-6.45%)</td><td>0.03 (-7.32%)</td><td>0.02 (-13.77%)</td><td>0.01 (-3.63%)</td><td>226.00 (+15.96%)</td><td>163.44 (+7.46%)</td><td>155.40 (+7.92%)</td><td>132.40 (+7.73%)</td><td>38.41 <b>(+21.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>152.10 (n/a)</td><td>144.00 (n/a)</td><td>122.90 (n/a)</td><td>31.62 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-18.44%)</td><td>0.02 <b>(-22.21%)</b></td><td>0.02 <b>(-23.77%)</b></td><td>0.02 <b>(-24.08%)</b></td><td>0.00 (+8.64%)</td><td>221.20 <b>(+31.75%)</b></td><td>183.90 <b>(+29.53%)</b></td><td>180.90 <b>(+31.18%)</b></td><td>158.10 <b>(+22.65%)</b></td><td>26.81 <b>(+71.27%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>167.90 (n/a)</td><td>141.98 (n/a)</td><td>137.90 (n/a)</td><td>128.90 (n/a)</td><td>15.65 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (+0.43%)</td><td>0.02 (-3.01%)</td><td>0.02 (-3.12%)</td><td>0.02 (-3.51%)</td><td>0.00 (-1.26%)</td><td>214.30 (+3.68%)</td><td>188.12 (+3.11%)</td><td>207.30 (+3.19%)</td><td>144.70 (-0.41%)</td><td>30.86 (+2.02%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>182.44 (n/a)</td><td>200.90 (n/a)</td><td>145.30 (n/a)</td><td>30.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>15.10 (-12.79%)</td><td>11.49 <b>(-25.08%)</b></td><td>12.07 <b>(-22.16%)</b></td><td>7.81 <b>(-37.96%)</b></td><td>2.91 <b>(+54.23%)</b></td><td>268.60 <b>(+61.22%)</b></td><td>192.98 <b>(+39.28%)</b></td><td>173.80 <b>(+28.46%)</b></td><td>138.90 (+14.60%)</td><td>52.44 <b>(+189.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>17.32 (n/a)</td><td>15.34 (n/a)</td><td>15.51 (n/a)</td><td>12.59 (n/a)</td><td>1.89 (n/a)</td><td>166.60 (n/a)</td><td>138.56 (n/a)</td><td>135.30 (n/a)</td><td>121.20 (n/a)</td><td>18.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.03 (+0.47%)</td><td>0.82 (-2.00%)</td><td>0.78 (-10.15%)</td><td>0.66 (+11.72%)</td><td>0.14 <b>(-23.61%)</b></td><td>201.50 (-10.48%)</td><td>164.70 (-0.11%)</td><td>169.00 (+11.26%)</td><td>128.10 (-0.47%)</td><td>27.87 <b>(-31.55%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.03 (n/a)</td><td>0.84 (n/a)</td><td>0.87 (n/a)</td><td>0.59 (n/a)</td><td>0.19 (n/a)</td><td>225.10 (n/a)</td><td>164.88 (n/a)</td><td>151.90 (n/a)</td><td>128.70 (n/a)</td><td>40.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.08 (-4.57%)</td><td>0.79 (-8.47%)</td><td>0.76 (-2.70%)</td><td>0.63 (-14.79%)</td><td>0.18 (+9.44%)</td><td>211.00 (+17.35%)</td><td>172.50 (+10.49%)</td><td>173.00 (+2.79%)</td><td>121.90 (+4.73%)</td><td>34.60 <b>(+34.39%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.14 (n/a)</td><td>0.87 (n/a)</td><td>0.78 (n/a)</td><td>0.73 (n/a)</td><td>0.16 (n/a)</td><td>179.80 (n/a)</td><td>156.12 (n/a)</td><td>168.30 (n/a)</td><td>116.40 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.82 <b>(-29.95%)</b></td><td>0.74 (-11.05%)</td><td>0.79 (+0.76%)</td><td>0.65 <b>(+30.59%)</b></td><td>0.08 <b>(-69.69%)</b></td><td>201.80 <b>(-23.42%)</b></td><td>179.30 (+4.41%)</td><td>167.70 (-0.77%)</td><td>161.60 <b>(+42.76%)</b></td><td>19.30 <b>(-66.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.17 (n/a)</td><td>0.84 (n/a)</td><td>0.78 (n/a)</td><td>0.50 (n/a)</td><td>0.26 (n/a)</td><td>263.50 (n/a)</td><td>171.72 (n/a)</td><td>169.00 (n/a)</td><td>113.20 (n/a)</td><td>57.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.80 <b>(-39.98%)</b></td><td>0.78 (-16.53%)</td><td>0.79 (-12.25%)</td><td>0.75 (+12.01%)</td><td>0.02 <b>(-91.67%)</b></td><td>176.60 (-10.76%)</td><td>169.26 (+14.26%)</td><td>167.10 (+13.98%)</td><td>165.70 <b>(+66.70%)</b></td><td>4.43 <b>(-87.29%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.33 (n/a)</td><td>0.94 (n/a)</td><td>0.90 (n/a)</td><td>0.67 (n/a)</td><td>0.24 (n/a)</td><td>197.90 (n/a)</td><td>148.14 (n/a)</td><td>146.60 (n/a)</td><td>99.40 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.95 (-9.39%)</td><td>0.76 (-12.07%)</td><td>0.73 (-11.86%)</td><td>0.64 (-0.80%)</td><td>0.12 <b>(-32.96%)</b></td><td>205.80 (+0.83%)</td><td>177.88 (+11.86%)</td><td>181.20 (+13.46%)</td><td>138.90 (+10.33%)</td><td>24.21 <b>(-25.88%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.05 (n/a)</td><td>0.86 (n/a)</td><td>0.83 (n/a)</td><td>0.65 (n/a)</td><td>0.17 (n/a)</td><td>204.10 (n/a)</td><td>159.02 (n/a)</td><td>159.70 (n/a)</td><td>125.90 (n/a)</td><td>32.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-8.83%)</td><td>0.02 (-3.07%)</td><td>0.02 (-1.16%)</td><td>0.02 (+9.76%)</td><td>0.00 <b>(-36.59%)</b></td><td>184.90 (-8.87%)</td><td>166.14 (+1.70%)</td><td>170.20 (+1.13%)</td><td>139.70 (+9.65%)</td><td>17.86 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.90 (n/a)</td><td>163.36 (n/a)</td><td>168.30 (n/a)</td><td>127.40 (n/a)</td><td>28.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.03 (-7.08%)</td><td>0.02 (-7.62%)</td><td>0.02 (-0.50%)</td><td>0.02 (-12.77%)</td><td>0.00 (-7.71%)</td><td>202.10 (+14.63%)</td><td>171.56 (+8.25%)</td><td>173.00 (+0.52%)</td><td>132.10 (+7.57%)</td><td>25.21 (+9.68%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.30 (n/a)</td><td>158.48 (n/a)</td><td>172.10 (n/a)</td><td>122.80 (n/a)</td><td>22.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.00 (+2.27%)</td><td>0.00 (-1.88%)</td><td>0.00 (+0.00%)</td><td>0.00 (-9.52%)</td><td>0.00 <b>(+189.40%)</b></td><td>1071.34 (+9.28%)</td><td>985.24 (+2.11%)</td><td>985.69 (+1.84%)</td><td>920.33 (-1.66%)</td><td>55.21 <b>(+203.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>980.33 (n/a)</td><td>964.90 (n/a)</td><td>967.87 (n/a)</td><td>935.82 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.01 (-2.30%)</td><td>0.01 (-2.17%)</td><td>0.01 (-2.41%)</td><td>0.01 (-5.06%)</td><td>0.00 (+4.48%)</td><td>1085.55 (+4.69%)</td><td>1011.65 (+2.10%)</td><td>1009.12 (+2.48%)</td><td>959.90 (+1.67%)</td><td>49.53 (+16.58%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1036.90 (n/a)</td><td>990.89 (n/a)</td><td>984.67 (n/a)</td><td>944.11 (n/a)</td><td>42.48 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.95 (-1.85%)</td><td>0.94 (-1.68%)</td><td>0.94 (-1.48%)</td><td>0.92 (-2.75%)</td><td>0.01 <b>(+46.60%)</b></td><td>2272.59 (+2.83%)</td><td>2228.13 (+1.72%)</td><td>2220.79 (+1.50%)</td><td>2207.65 (+1.88%)</td><td>25.64 <b>(+53.89%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2210.09 (n/a)</td><td>2190.48 (n/a)</td><td>2187.88 (n/a)</td><td>2166.87 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.90 (+0.15%)</td><td>0.88 (-0.93%)</td><td>0.87 (-1.00%)</td><td>0.86 (-0.68%)</td><td>0.01 (+14.21%)</td><td>2431.77 (+0.69%)</td><td>2395.65 (+0.94%)</td><td>2400.67 (+1.01%)</td><td>2341.90 (-0.15%)</td><td>33.11 (+14.87%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>2415.15 (n/a)</td><td>2373.31 (n/a)</td><td>2376.74 (n/a)</td><td>2345.31 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.67 (-2.24%)</td><td>0.64 (-3.44%)</td><td>0.64 (-3.54%)</td><td>0.60 (-6.09%)</td><td>0.03 <b>(+64.08%)</b></td><td>1742.40 (+6.49%)</td><td>1637.04 (+3.65%)</td><td>1630.50 (+3.67%)</td><td>1573.00 (+2.29%)</td><td>67.27 <b>(+78.52%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.68 (n/a)</td><td>0.66 (n/a)</td><td>0.67 (n/a)</td><td>0.64 (n/a)</td><td>0.02 (n/a)</td><td>1636.20 (n/a)</td><td>1579.36 (n/a)</td><td>1572.80 (n/a)</td><td>1537.80 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.22 (+2.70%)</td><td>1.17 (+4.13%)</td><td>1.15 (+1.97%)</td><td>1.13 (+14.17%)</td><td>0.04 <b>(-49.66%)</b></td><td>926.50 (-12.41%)</td><td>896.42 (-4.30%)</td><td>910.10 (-1.94%)</td><td>860.60 (-2.64%)</td><td>30.42 <b>(-57.35%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.19 (n/a)</td><td>1.12 (n/a)</td><td>1.13 (n/a)</td><td>0.99 (n/a)</td><td>0.08 (n/a)</td><td>1057.80 (n/a)</td><td>936.66 (n/a)</td><td>928.10 (n/a)</td><td>883.90 (n/a)</td><td>71.32 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.21 (+0.01%)</td><td>1.16 (+1.18%)</td><td>1.17 (+1.83%)</td><td>1.09 (-0.27%)</td><td>0.05 (+17.57%)</td><td>960.10 (+0.27%)</td><td>905.42 (-1.12%)</td><td>896.60 (-1.80%)</td><td>864.60 (-0.01%)</td><td>41.57 (+17.72%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.21 (n/a)</td><td>1.15 (n/a)</td><td>1.15 (n/a)</td><td>1.10 (n/a)</td><td>0.04 (n/a)</td><td>957.50 (n/a)</td><td>915.64 (n/a)</td><td>913.00 (n/a)</td><td>864.70 (n/a)</td><td>35.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.13 (+6.04%)</td><td>1.90 (+2.94%)</td><td>1.88 (+3.68%)</td><td>1.69 (-4.27%)</td><td>0.18 <b>(+80.82%)</b></td><td>621.90 (+4.47%)</td><td>556.60 (-2.40%)</td><td>556.30 (-3.55%)</td><td>491.90 (-5.69%)</td><td>51.03 <b>(+80.28%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.01 (n/a)</td><td>1.84 (n/a)</td><td>1.82 (n/a)</td><td>1.76 (n/a)</td><td>0.10 (n/a)</td><td>595.30 (n/a)</td><td>570.30 (n/a)</td><td>576.80 (n/a)</td><td>521.60 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.68 (+1.25%)</td><td>0.64 (-2.84%)</td><td>0.65 (-0.97%)</td><td>0.59 (-7.99%)</td><td>0.04 <b>(+179.15%)</b></td><td>3554.70 (+8.69%)</td><td>3289.64 (+3.16%)</td><td>3234.20 (+0.98%)</td><td>3072.80 (-1.24%)</td><td>188.85 <b>(+201.04%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.67 (n/a)</td><td>0.66 (n/a)</td><td>0.65 (n/a)</td><td>0.64 (n/a)</td><td>0.01 (n/a)</td><td>3270.60 (n/a)</td><td>3188.80 (n/a)</td><td>3202.80 (n/a)</td><td>3111.40 (n/a)</td><td>62.73 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.33 (+0.68%)</td><td>1.24 (-1.28%)</td><td>1.25 (-0.65%)</td><td>1.15 (-2.12%)</td><td>0.07 <b>(+29.36%)</b></td><td>1823.40 (+2.17%)</td><td>1699.38 (+1.40%)</td><td>1681.60 (+0.65%)</td><td>1573.60 (-0.68%)</td><td>93.94 <b>(+30.90%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.32 (n/a)</td><td>1.25 (n/a)</td><td>1.26 (n/a)</td><td>1.18 (n/a)</td><td>0.05 (n/a)</td><td>1784.70 (n/a)</td><td>1675.92 (n/a)</td><td>1670.70 (n/a)</td><td>1584.30 (n/a)</td><td>71.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.31 (-2.44%)</td><td>1.26 (+3.64%)</td><td>1.27 (-0.71%)</td><td>1.21 <b>(+28.64%)</b></td><td>0.04 <b>(-75.18%)</b></td><td>1735.90 <b>(-22.27%)</b></td><td>1661.14 (-5.08%)</td><td>1650.60 (+0.71%)</td><td>1597.90 (+2.50%)</td><td>53.92 <b>(-80.56%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.35 (n/a)</td><td>1.22 (n/a)</td><td>1.28 (n/a)</td><td>0.94 (n/a)</td><td>0.16 (n/a)</td><td>2233.10 (n/a)</td><td>1750.00 (n/a)</td><td>1639.00 (n/a)</td><td>1558.90 (n/a)</td><td>277.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.35 (-2.18%)</td><td>2.21 (-4.37%)</td><td>2.26 (-2.83%)</td><td>1.93 (-13.60%)</td><td>0.17 <b>(+118.81%)</b></td><td>1087.70 (+15.75%)</td><td>951.56 (+5.01%)</td><td>927.60 (+2.91%)</td><td>890.90 (+2.23%)</td><td>78.36 <b>(+162.00%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.41 (n/a)</td><td>2.32 (n/a)</td><td>2.33 (n/a)</td><td>2.23 (n/a)</td><td>0.08 (n/a)</td><td>939.70 (n/a)</td><td>906.20 (n/a)</td><td>901.40 (n/a)</td><td>871.50 (n/a)</td><td>29.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.37 (+4.24%)</td><td>2.32 (+8.58%)</td><td>2.34 (+4.69%)</td><td>2.24 <b>(+24.13%)</b></td><td>0.06 <b>(-70.99%)</b></td><td>934.50 (-19.44%)</td><td>905.32 (-8.56%)</td><td>897.20 (-4.48%)</td><td>883.90 (-4.07%)</td><td>22.74 <b>(-77.57%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.28 (n/a)</td><td>2.13 (n/a)</td><td>2.23 (n/a)</td><td>1.81 (n/a)</td><td>0.20 (n/a)</td><td>1160.00 (n/a)</td><td>990.08 (n/a)</td><td>939.30 (n/a)</td><td>921.40 (n/a)</td><td>101.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.09 (+8.32%)</td><td>3.76 (+6.99%)</td><td>3.70 (+4.19%)</td><td>3.48 (+4.83%)</td><td>0.28 <b>(+45.40%)</b></td><td>602.60 (-4.61%)</td><td>560.22 (-6.35%)</td><td>567.50 (-4.03%)</td><td>512.60 (-7.69%)</td><td>40.65 <b>(+26.88%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>3.78 (n/a)</td><td>3.51 (n/a)</td><td>3.55 (n/a)</td><td>3.32 (n/a)</td><td>0.19 (n/a)</td><td>631.70 (n/a)</td><td>598.20 (n/a)</td><td>591.30 (n/a)</td><td>555.30 (n/a)</td><td>32.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.71 (-0.95%)</td><td>0.68 (+0.41%)</td><td>0.69 (+0.87%)</td><td>0.63 (-1.92%)</td><td>0.03 (+11.97%)</td><td>6618.30 (+1.96%)</td><td>6162.40 (-0.38%)</td><td>6082.10 (-0.86%)</td><td>5941.40 (+0.96%)</td><td>262.31 (+16.38%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.71 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.65 (n/a)</td><td>0.02 (n/a)</td><td>6491.30 (n/a)</td><td>6185.76 (n/a)</td><td>6134.90 (n/a)</td><td>5884.90 (n/a)</td><td>225.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.40 (+1.94%)</td><td>1.32 (+5.78%)</td><td>1.31 (+2.69%)</td><td>1.20 (+7.73%)</td><td>0.08 <b>(-34.97%)</b></td><td>3492.40 (-7.18%)</td><td>3185.52 (-5.96%)</td><td>3203.20 (-2.62%)</td><td>2994.00 (-1.91%)</td><td>204.12 <b>(-41.71%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.37 (n/a)</td><td>1.25 (n/a)</td><td>1.28 (n/a)</td><td>1.11 (n/a)</td><td>0.13 (n/a)</td><td>3762.40 (n/a)</td><td>3387.36 (n/a)</td><td>3289.40 (n/a)</td><td>3052.20 (n/a)</td><td>350.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.40 (+1.14%)</td><td>1.32 (+3.20%)</td><td>1.36 (+6.61%)</td><td>1.16 (+1.61%)</td><td>0.10 (+12.08%)</td><td>3624.60 (-1.58%)</td><td>3199.30 (-3.01%)</td><td>3087.10 (-6.20%)</td><td>2997.90 (-1.13%)</td><td>259.05 (+8.09%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.38 (n/a)</td><td>1.28 (n/a)</td><td>1.27 (n/a)</td><td>1.14 (n/a)</td><td>0.09 (n/a)</td><td>3682.90 (n/a)</td><td>3298.70 (n/a)</td><td>3291.10 (n/a)</td><td>3032.10 (n/a)</td><td>239.65 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.66 (+3.49%)</td><td>2.51 (+1.30%)</td><td>2.52 (+2.71%)</td><td>2.37 (+0.30%)</td><td>0.10 <b>(+20.22%)</b></td><td>1769.10 (-0.30%)</td><td>1674.82 (-1.25%)</td><td>1665.40 (-2.64%)</td><td>1579.00 (-3.37%)</td><td>68.45 (+16.37%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.57 (n/a)</td><td>2.48 (n/a)</td><td>2.45 (n/a)</td><td>2.36 (n/a)</td><td>0.09 (n/a)</td><td>1774.50 (n/a)</td><td>1695.98 (n/a)</td><td>1710.60 (n/a)</td><td>1634.10 (n/a)</td><td>58.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>2.66 (+1.13%)</td><td>2.58 (+4.35%)</td><td>2.58 (+5.52%)</td><td>2.52 (+6.77%)</td><td>0.06 <b>(-49.18%)</b></td><td>1661.30 (-6.34%)</td><td>1625.54 (-4.28%)</td><td>1626.40 (-5.24%)</td><td>1574.10 (-1.12%)</td><td>35.80 <b>(-52.93%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>2.63 (n/a)</td><td>2.47 (n/a)</td><td>2.44 (n/a)</td><td>2.36 (n/a)</td><td>0.11 (n/a)</td><td>1773.70 (n/a)</td><td>1698.30 (n/a)</td><td>1716.30 (n/a)</td><td>1591.90 (n/a)</td><td>76.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.59 (-4.97%)</td><td>4.50 (-2.38%)</td><td>4.52 (-1.12%)</td><td>4.35 (-3.19%)</td><td>0.09 <b>(-31.38%)</b></td><td>964.20 (+3.29%)</td><td>931.40 (+2.41%)</td><td>927.60 (+1.14%)</td><td>914.20 (+5.23%)</td><td>19.67 <b>(-25.20%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.83 (n/a)</td><td>4.61 (n/a)</td><td>4.57 (n/a)</td><td>4.49 (n/a)</td><td>0.14 (n/a)</td><td>933.50 (n/a)</td><td>909.50 (n/a)</td><td>917.10 (n/a)</td><td>868.80 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>4.55 (+0.14%)</td><td>4.38 (+3.14%)</td><td>4.45 (+2.05%)</td><td>3.99 (+2.96%)</td><td>0.22 <b>(-29.91%)</b></td><td>1050.50 (-2.88%)</td><td>959.56 (-3.27%)</td><td>941.70 (-2.00%)</td><td>922.80 (-0.14%)</td><td>51.48 <b>(-31.40%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>4.54 (n/a)</td><td>4.25 (n/a)</td><td>4.36 (n/a)</td><td>3.88 (n/a)</td><td>0.31 (n/a)</td><td>1081.70 (n/a)</td><td>992.00 (n/a)</td><td>960.90 (n/a)</td><td>924.10 (n/a)</td><td>75.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>8.01 (+10.99%)</td><td>7.00 (+2.91%)</td><td>7.09 (+2.30%)</td><td>5.94 (+0.15%)</td><td>0.88 <b>(+68.42%)</b></td><td>706.50 (-0.14%)</td><td>607.16 (-2.06%)</td><td>591.60 (-2.25%)</td><td>523.90 (-9.91%)</td><td>78.01 <b>(+51.08%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>7.21 (n/a)</td><td>6.80 (n/a)</td><td>6.93 (n/a)</td><td>5.93 (n/a)</td><td>0.52 (n/a)</td><td>707.50 (n/a)</td><td>619.92 (n/a)</td><td>605.20 (n/a)</td><td>581.50 (n/a)</td><td>51.63 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.58 (-6.01%)</td><td>0.57 (-2.75%)</td><td>0.57 (-1.79%)</td><td>0.54 (-2.36%)</td><td>0.02 <b>(-28.46%)</b></td><td>976.00 (+2.41%)</td><td>926.38 (+2.75%)</td><td>916.10 (+1.82%)</td><td>899.50 (+6.40%)</td><td>32.39 <b>(-22.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.62 (n/a)</td><td>0.58 (n/a)</td><td>0.58 (n/a)</td><td>0.55 (n/a)</td><td>0.03 (n/a)</td><td>953.00 (n/a)</td><td>901.62 (n/a)</td><td>899.70 (n/a)</td><td>845.40 (n/a)</td><td>41.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.64 (-4.90%)</td><td>0.62 (-1.69%)</td><td>0.63 (-0.40%)</td><td>0.58 (-2.79%)</td><td>0.03 (-17.87%)</td><td>1820.00 (+2.87%)</td><td>1690.54 (+1.66%)</td><td>1655.70 (+0.41%)</td><td>1632.50 (+5.15%)</td><td>75.37 (-10.74%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.68 (n/a)</td><td>0.63 (n/a)</td><td>0.64 (n/a)</td><td>0.59 (n/a)</td><td>0.03 (n/a)</td><td>1769.20 (n/a)</td><td>1662.94 (n/a)</td><td>1649.00 (n/a)</td><td>1552.60 (n/a)</td><td>84.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.69 (+1.75%)</td><td>0.64 (-1.05%)</td><td>0.64 (-3.67%)</td><td>0.55 (-2.70%)</td><td>0.05 (+12.59%)</td><td>3795.30 (+2.78%)</td><td>3319.92 (+1.19%)</td><td>3284.50 (+3.81%)</td><td>3048.90 (-1.72%)</td><td>283.77 (+15.31%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.68 (n/a)</td><td>0.64 (n/a)</td><td>0.66 (n/a)</td><td>0.57 (n/a)</td><td>0.04 (n/a)</td><td>3692.80 (n/a)</td><td>3281.00 (n/a)</td><td>3164.00 (n/a)</td><td>3102.20 (n/a)</td><td>246.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>1.04 (-1.63%)</td><td>0.98 (-5.40%)</td><td>0.98 (-6.91%)</td><td>0.89 (-8.97%)</td><td>0.06 <b>(+99.49%)</b></td><td>586.10 (+9.86%)</td><td>539.26 (+5.99%)</td><td>537.50 (+7.41%)</td><td>502.60 (+1.66%)</td><td>35.57 <b>(+121.40%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>1.06 (n/a)</td><td>1.03 (n/a)</td><td>1.05 (n/a)</td><td>0.98 (n/a)</td><td>0.03 (n/a)</td><td>533.50 (n/a)</td><td>508.80 (n/a)</td><td>500.40 (n/a)</td><td>494.40 (n/a)</td><td>16.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.18 (-3.08%)</td><td>0.16 (-3.68%)</td><td>0.16 (-1.43%)</td><td>0.14 (-5.61%)</td><td>0.01 (+10.65%)</td><td>240.80 (+5.94%)</td><td>209.44 (+4.01%)</td><td>202.80 (+1.45%)</td><td>185.70 (+3.17%)</td><td>20.65 <b>(+21.30%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>201.36 (n/a)</td><td>199.90 (n/a)</td><td>180.00 (n/a)</td><td>17.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.20 (+9.28%)</td><td>0.18 (+5.85%)</td><td>0.17 (+2.25%)</td><td>0.15 (+14.69%)</td><td>0.02 (-12.62%)</td><td>212.10 (-12.79%)</td><td>188.56 (-6.00%)</td><td>194.10 (-2.22%)</td><td>163.10 (-8.47%)</td><td>18.59 <b>(-30.18%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>243.20 (n/a)</td><td>200.60 (n/a)</td><td>198.50 (n/a)</td><td>178.20 (n/a)</td><td>26.63 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.29 (-2.61%)</td><td>0.26 (+3.16%)</td><td>0.27 (+5.78%)</td><td>0.22 (+17.45%)</td><td>0.03 <b>(-43.17%)</b></td><td>300.90 (-14.86%)</td><td>252.68 (-5.19%)</td><td>246.30 (-5.49%)</td><td>223.80 (+2.66%)</td><td>28.73 <b>(-48.17%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>353.40 (n/a)</td><td>266.50 (n/a)</td><td>260.60 (n/a)</td><td>218.00 (n/a)</td><td>55.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.36 (-6.81%)</td><td>0.30 (-2.92%)</td><td>0.31 (+3.54%)</td><td>0.25 (-6.49%)</td><td>0.05 (+5.58%)</td><td>261.40 (+6.96%)</td><td>223.12 (+3.57%)</td><td>212.40 (-3.41%)</td><td>182.20 (+7.30%)</td><td>35.86 <b>(+29.09%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>244.40 (n/a)</td><td>215.42 (n/a)</td><td>219.90 (n/a)</td><td>169.80 (n/a)</td><td>27.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.47 (+13.46%)</td><td>0.35 (+6.33%)</td><td>0.34 (-2.26%)</td><td>0.28 (+1.96%)</td><td>0.07 <b>(+26.04%)</b></td><td>234.40 (-1.92%)</td><td>191.46 (-5.27%)</td><td>194.90 (+2.31%)</td><td>140.10 (-11.89%)</td><td>36.24 (+3.97%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>239.00 (n/a)</td><td>202.12 (n/a)</td><td>190.50 (n/a)</td><td>159.00 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.38 (-5.07%)</td><td>0.33 (-6.59%)</td><td>0.32 (-7.96%)</td><td>0.29 (-4.32%)</td><td>0.04 (-0.48%)</td><td>455.90 (+4.52%)</td><td>403.58 (+7.15%)</td><td>411.50 (+8.66%)</td><td>346.00 (+5.33%)</td><td>46.38 (+9.77%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.04 (n/a)</td><td>436.20 (n/a)</td><td>376.64 (n/a)</td><td>378.70 (n/a)</td><td>328.50 (n/a)</td><td>42.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.60 (-0.53%)</td><td>0.47 (-12.19%)</td><td>0.48 (-13.76%)</td><td>0.36 (-16.22%)</td><td>0.10 <b>(+38.02%)</b></td><td>366.20 (+19.36%)</td><td>285.58 (+15.99%)</td><td>271.80 (+15.96%)</td><td>217.50 (+0.51%)</td><td>58.80 <b>(+63.96%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.61 (n/a)</td><td>0.54 (n/a)</td><td>0.56 (n/a)</td><td>0.43 (n/a)</td><td>0.07 (n/a)</td><td>306.80 (n/a)</td><td>246.22 (n/a)</td><td>234.40 (n/a)</td><td>216.40 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.67 (-2.00%)</td><td>0.61 (+0.28%)</td><td>0.59 (-7.33%)</td><td>0.56 (+8.62%)</td><td>0.05 <b>(-32.67%)</b></td><td>235.20 (-7.95%)</td><td>217.14 (-0.94%)</td><td>222.90 (+7.89%)</td><td>194.20 (+2.00%)</td><td>16.57 <b>(-37.40%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.69 (n/a)</td><td>0.60 (n/a)</td><td>0.63 (n/a)</td><td>0.51 (n/a)</td><td>0.07 (n/a)</td><td>255.50 (n/a)</td><td>219.20 (n/a)</td><td>206.60 (n/a)</td><td>190.40 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.73 (-10.10%)</td><td>0.65 (+5.37%)</td><td>0.62 (+9.57%)</td><td>0.57 <b>(+36.05%)</b></td><td>0.07 <b>(-56.58%)</b></td><td>229.70 <b>(-26.50%)</b></td><td>202.62 (-9.44%)</td><td>210.80 (-8.74%)</td><td>178.70 (+11.20%)</td><td>21.37 <b>(-64.41%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.82 (n/a)</td><td>0.62 (n/a)</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.16 (n/a)</td><td>312.50 (n/a)</td><td>223.74 (n/a)</td><td>231.00 (n/a)</td><td>160.70 (n/a)</td><td>60.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 01:09:33</td><td>0.11 (+4.95%)</td><td>0.08 (-15.20%)</td><td>0.08 (-6.96%)</td><td>0.05 <b>(-45.55%)</b></td><td>0.03 <b>(+163.51%)</b></td><td>346.30 <b>(+83.71%)</b></td><td>221.70 <b>(+28.08%)</b></td><td>194.00 (+7.48%)</td><td>143.60 (-4.71%)</td><td>79.04 <b>(+370.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:20:51</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.50 (n/a)</td><td>173.10 (n/a)</td><td>180.50 (n/a)</td><td>150.70 (n/a)</td><td>16.78 (n/a)</td>
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
