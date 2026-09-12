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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (+0.55%)</td><td>0.04 (-4.88%)</td><td>0.04 (+7.51%)</td><td>0.03 (-4.56%)</td><td>0.01 (-6.01%)</td><td>219.80 (+4.77%)</td><td>173.60 (+4.94%)</td><td>162.80 (-6.97%)</td><td>126.60 (-0.55%)</td><td>36.20 (+2.26%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>165.42 (n/a)</td><td>175.00 (n/a)</td><td>127.30 (n/a)</td><td>35.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (-9.62%)</td><td>0.04 (-10.87%)</td><td>0.04 (-14.68%)</td><td>0.03 (-11.71%)</td><td>0.01 (-16.51%)</td><td>221.50 (+13.24%)</td><td>172.76 (+11.65%)</td><td>173.60 (+17.22%)</td><td>130.40 (+10.60%)</td><td>32.92 (+3.29%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>154.74 (n/a)</td><td>148.10 (n/a)</td><td>117.90 (n/a)</td><td>31.88 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (+19.02%)</td><td>0.04 (+12.66%)</td><td>0.04 (+12.07%)</td><td>0.03 (+3.86%)</td><td>0.01 <b>(+44.85%)</b></td><td>208.10 (-3.70%)</td><td>171.12 (-10.60%)</td><td>165.70 (-10.77%)</td><td>139.90 (-15.98%)</td><td>25.84 (+15.85%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>216.10 (n/a)</td><td>191.40 (n/a)</td><td>185.70 (n/a)</td><td>166.50 (n/a)</td><td>22.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (-7.31%)</td><td>0.04 (-7.92%)</td><td>0.03 (-15.58%)</td><td>0.03 (+7.16%)</td><td>0.00 <b>(-32.04%)</b></td><td>197.70 (-6.70%)</td><td>174.96 (+7.10%)</td><td>183.20 (+18.50%)</td><td>144.90 (+7.89%)</td><td>20.70 <b>(-32.87%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>211.90 (n/a)</td><td>163.36 (n/a)</td><td>154.60 (n/a)</td><td>134.30 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (+16.25%)</td><td>0.04 (+15.41%)</td><td>0.04 (+16.20%)</td><td>0.03 (+14.35%)</td><td>0.01 (+13.89%)</td><td>189.60 (-12.55%)</td><td>160.48 (-13.39%)</td><td>167.90 (-13.94%)</td><td>130.20 (-13.95%)</td><td>23.35 (-14.23%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>185.28 (n/a)</td><td>195.10 (n/a)</td><td>151.30 (n/a)</td><td>27.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 <b>(-31.57%)</b></td><td>0.03 (-12.45%)</td><td>0.03 (-0.56%)</td><td>0.03 (-3.45%)</td><td>0.00 <b>(-66.89%)</b></td><td>225.60 (+3.58%)</td><td>203.56 (+10.69%)</td><td>197.10 (+0.56%)</td><td>184.00 <b>(+46.15%)</b></td><td>18.76 <b>(-48.25%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>183.90 (n/a)</td><td>196.00 (n/a)</td><td>125.90 (n/a)</td><td>36.25 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (+11.90%)</td><td>0.03 (+18.14%)</td><td>0.03 (+16.83%)</td><td>0.03 <b>(+37.30%)</b></td><td>0.01 (-3.76%)</td><td>214.80 <b>(-27.16%)</b></td><td>181.54 (-16.95%)</td><td>190.50 (-14.42%)</td><td>131.40 (-10.61%)</td><td>34.67 <b>(-36.01%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>294.90 (n/a)</td><td>218.60 (n/a)</td><td>222.60 (n/a)</td><td>147.00 (n/a)</td><td>54.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (+9.94%)</td><td>0.03 (+18.95%)</td><td>0.03 <b>(+21.95%)</b></td><td>0.03 <b>(+34.48%)</b></td><td>0.00 <b>(-30.27%)</b></td><td>211.70 <b>(-25.64%)</b></td><td>191.42 (-17.47%)</td><td>192.60 (-17.97%)</td><td>160.50 (-9.07%)</td><td>19.79 <b>(-52.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>284.70 (n/a)</td><td>231.94 (n/a)</td><td>234.80 (n/a)</td><td>176.50 (n/a)</td><td>42.07 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 <b>(+41.99%)</b></td><td>0.08 (+16.16%)</td><td>0.07 (-6.97%)</td><td>0.06 <b>(+27.31%)</b></td><td>0.02 <b>(+75.75%)</b></td><td>198.00 <b>(-21.46%)</b></td><td>165.54 (-12.11%)</td><td>181.60 (+7.52%)</td><td>112.20 <b>(-29.57%)</b></td><td>38.11 (-1.06%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>252.10 (n/a)</td><td>188.34 (n/a)</td><td>168.90 (n/a)</td><td>159.30 (n/a)</td><td>38.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 <b>(+29.76%)</b></td><td>0.08 <b>(+21.84%)</b></td><td>0.07 (+17.83%)</td><td>0.06 (+13.82%)</td><td>0.01 <b>(+75.12%)</b></td><td>191.00 (-12.14%)</td><td>162.70 (-17.27%)</td><td>164.40 (-15.13%)</td><td>132.00 <b>(-22.90%)</b></td><td>22.09 (+16.27%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>196.66 (n/a)</td><td>193.70 (n/a)</td><td>171.20 (n/a)</td><td>19.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (-0.74%)</td><td>0.08 (+7.80%)</td><td>0.09 (+19.63%)</td><td>0.06 (-1.81%)</td><td>0.02 (+0.02%)</td><td>190.60 (+1.87%)</td><td>149.96 (-7.05%)</td><td>138.90 (-16.43%)</td><td>118.90 (+0.68%)</td><td>28.13 (+8.04%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>187.10 (n/a)</td><td>161.34 (n/a)</td><td>166.20 (n/a)</td><td>118.10 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 <b>(+21.12%)</b></td><td>0.09 <b>(+35.95%)</b></td><td>0.09 <b>(+46.18%)</b></td><td>0.07 <b>(+21.02%)</b></td><td>0.02 <b>(+30.05%)</b></td><td>179.70 (-17.38%)</td><td>136.82 <b>(-26.15%)</b></td><td>130.00 <b>(-31.58%)</b></td><td>116.50 (-17.43%)</td><td>25.80 (-8.37%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>185.26 (n/a)</td><td>190.00 (n/a)</td><td>141.10 (n/a)</td><td>28.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (-4.86%)</td><td>0.08 (+3.44%)</td><td>0.08 (+8.71%)</td><td>0.07 (+4.00%)</td><td>0.01 (-14.43%)</td><td>183.80 (-3.87%)</td><td>151.16 (-3.89%)</td><td>146.60 (-8.03%)</td><td>131.00 (+5.14%)</td><td>22.28 (-14.38%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>157.28 (n/a)</td><td>159.40 (n/a)</td><td>124.60 (n/a)</td><td>26.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (+16.36%)</td><td>0.07 (+5.44%)</td><td>0.07 (+2.16%)</td><td>0.03 <b>(-29.15%)</b></td><td>0.02 <b>(+89.41%)</b></td><td>360.30 <b>(+41.18%)</b></td><td>198.16 (+4.68%)</td><td>169.70 (-2.13%)</td><td>130.80 (-14.06%)</td><td>93.88 <b>(+132.07%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>255.20 (n/a)</td><td>189.30 (n/a)</td><td>173.40 (n/a)</td><td>152.20 (n/a)</td><td>40.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 <b>(+24.63%)</b></td><td>0.07 <b>(+22.95%)</b></td><td>0.07 (+14.73%)</td><td>0.06 <b>(+47.14%)</b></td><td>0.01 (-15.78%)</td><td>197.50 <b>(-32.01%)</b></td><td>172.16 <b>(-20.38%)</b></td><td>173.80 (-12.84%)</td><td>140.70 (-19.78%)</td><td>22.12 <b>(-53.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>290.50 (n/a)</td><td>216.24 (n/a)</td><td>199.40 (n/a)</td><td>175.40 (n/a)</td><td>47.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (-7.36%)</td><td>0.06 (-1.19%)</td><td>0.07 (+6.73%)</td><td>0.04 (+7.01%)</td><td>0.01 <b>(-25.86%)</b></td><td>278.70 (-6.54%)</td><td>202.64 (-1.32%)</td><td>181.90 (-6.29%)</td><td>161.40 (+7.96%)</td><td>46.28 <b>(-22.73%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>298.20 (n/a)</td><td>205.36 (n/a)</td><td>194.10 (n/a)</td><td>149.50 (n/a)</td><td>59.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (-5.50%)</td><td>0.15 (+2.71%)</td><td>0.16 (+10.76%)</td><td>0.11 (-0.27%)</td><td>0.03 (-14.94%)</td><td>220.20 (+0.27%)</td><td>164.36 (-3.31%)</td><td>154.40 (-9.71%)</td><td>131.50 (+5.79%)</td><td>33.53 (-5.93%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>219.60 (n/a)</td><td>169.98 (n/a)</td><td>171.00 (n/a)</td><td>124.30 (n/a)</td><td>35.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (-18.16%)</td><td>0.14 (-13.87%)</td><td>0.14 (-13.68%)</td><td>0.11 (+7.53%)</td><td>0.02 <b>(-47.57%)</b></td><td>218.40 (-6.98%)</td><td>179.48 (+12.33%)</td><td>174.30 (+15.81%)</td><td>152.70 <b>(+22.16%)</b></td><td>25.21 <b>(-42.14%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>234.80 (n/a)</td><td>159.78 (n/a)</td><td>150.50 (n/a)</td><td>125.00 (n/a)</td><td>43.57 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 <b>(+24.69%)</b></td><td>0.16 <b>(+23.14%)</b></td><td>0.16 (+18.72%)</td><td>0.13 <b>(+29.64%)</b></td><td>0.03 (-8.37%)</td><td>188.80 <b>(-22.84%)</b></td><td>155.64 <b>(-20.53%)</b></td><td>154.80 (-15.78%)</td><td>119.80 (-19.76%)</td><td>24.64 <b>(-46.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>244.70 (n/a)</td><td>195.84 (n/a)</td><td>183.80 (n/a)</td><td>149.30 (n/a)</td><td>45.71 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (+16.82%)</td><td>0.15 (+0.16%)</td><td>0.14 (-1.87%)</td><td>0.11 (+1.12%)</td><td>0.03 <b>(+50.97%)</b></td><td>218.40 (-1.13%)</td><td>173.54 (+1.79%)</td><td>171.90 (+1.90%)</td><td>122.70 (-14.38%)</td><td>38.10 <b>(+25.69%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.90 (n/a)</td><td>170.48 (n/a)</td><td>168.70 (n/a)</td><td>143.30 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 <b>(+20.90%)</b></td><td>0.13 (-1.60%)</td><td>0.12 (-7.78%)</td><td>0.11 (+1.25%)</td><td>0.03 <b>(+83.58%)</b></td><td>218.30 (-1.27%)</td><td>194.94 (+3.33%)</td><td>205.30 (+8.45%)</td><td>140.00 (-17.31%)</td><td>31.70 <b>(+48.24%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>188.66 (n/a)</td><td>189.30 (n/a)</td><td>169.30 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (+8.12%)</td><td>0.15 (+7.33%)</td><td>0.14 (+10.29%)</td><td>0.11 (+12.59%)</td><td>0.03 (-1.35%)</td><td>216.70 (-11.19%)</td><td>173.22 (-7.61%)</td><td>171.70 (-9.35%)</td><td>127.10 (-7.56%)</td><td>35.60 (-17.87%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>244.00 (n/a)</td><td>187.48 (n/a)</td><td>189.40 (n/a)</td><td>137.50 (n/a)</td><td>43.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 <b>(+44.79%)</b></td><td>0.14 <b>(+29.75%)</b></td><td>0.14 <b>(+20.62%)</b></td><td>0.11 <b>(+40.15%)</b></td><td>0.02 <b>(+49.06%)</b></td><td>217.70 <b>(-28.65%)</b></td><td>183.58 <b>(-22.74%)</b></td><td>177.60 (-17.09%)</td><td>144.40 <b>(-30.94%)</b></td><td>30.82 <b>(-24.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>305.10 (n/a)</td><td>237.60 (n/a)</td><td>214.20 (n/a)</td><td>209.10 (n/a)</td><td>40.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (+12.01%)</td><td>0.12 (-2.30%)</td><td>0.13 (+1.05%)</td><td>0.07 <b>(-26.90%)</b></td><td>0.04 <b>(+72.92%)</b></td><td>337.10 <b>(+36.81%)</b></td><td>217.52 (+9.05%)</td><td>194.70 (-1.02%)</td><td>134.80 (-10.73%)</td><td>75.20 <b>(+118.91%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>246.40 (n/a)</td><td>199.46 (n/a)</td><td>196.70 (n/a)</td><td>151.00 (n/a)</td><td>34.35 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.47 <b>(+20.84%)</b></td><td>0.33 <b>(+24.70%)</b></td><td>0.30 <b>(+20.22%)</b></td><td>0.27 <b>(+47.86%)</b></td><td>0.08 (+3.74%)</td><td>183.50 <b>(-32.39%)</b></td><td>154.24 <b>(-21.76%)</b></td><td>163.60 (-16.79%)</td><td>104.80 (-17.22%)</td><td>31.63 <b>(-41.98%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>271.40 (n/a)</td><td>197.14 (n/a)</td><td>196.60 (n/a)</td><td>126.60 (n/a)</td><td>54.51 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.33 <b>(+20.81%)</b></td><td>0.25 (-3.58%)</td><td>0.27 (+6.48%)</td><td>0.14 <b>(-43.25%)</b></td><td>0.07 <b>(+594.76%)</b></td><td>353.00 <b>(+76.24%)</b></td><td>216.42 (+12.72%)</td><td>182.40 (-6.08%)</td><td>150.80 (-17.19%)</td><td>79.81 <b>(+971.53%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>200.30 (n/a)</td><td>192.00 (n/a)</td><td>194.20 (n/a)</td><td>182.10 (n/a)</td><td>7.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.31 (-16.32%)</td><td>0.26 (-8.47%)</td><td>0.27 (-6.62%)</td><td>0.22 (+5.32%)</td><td>0.03 <b>(-41.62%)</b></td><td>223.70 (-5.09%)</td><td>189.10 (+7.04%)</td><td>179.60 (+7.10%)</td><td>160.50 (+19.51%)</td><td>24.50 <b>(-34.52%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>235.70 (n/a)</td><td>176.66 (n/a)</td><td>167.70 (n/a)</td><td>134.30 (n/a)</td><td>37.42 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.35 (-12.94%)</td><td>0.29 (-4.11%)</td><td>0.28 (-6.87%)</td><td>0.23 (-0.08%)</td><td>0.05 <b>(-28.37%)</b></td><td>210.20 (+0.05%)</td><td>171.58 (+2.20%)</td><td>176.70 (+7.42%)</td><td>140.30 (+14.81%)</td><td>30.50 <b>(-22.63%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>210.10 (n/a)</td><td>167.88 (n/a)</td><td>164.50 (n/a)</td><td>122.20 (n/a)</td><td>39.42 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.33 (-14.61%)</td><td>0.30 (+11.58%)</td><td>0.30 (+11.67%)</td><td>0.28 <b>(+53.74%)</b></td><td>0.02 <b>(-73.87%)</b></td><td>175.60 <b>(-34.94%)</b></td><td>164.04 (-15.47%)</td><td>164.20 (-10.47%)</td><td>147.60 (+17.14%)</td><td>10.55 <b>(-80.03%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>269.90 (n/a)</td><td>194.06 (n/a)</td><td>183.40 (n/a)</td><td>126.00 (n/a)</td><td>52.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.37 <b>(+28.13%)</b></td><td>0.30 (+16.28%)</td><td>0.28 (+8.50%)</td><td>0.21 (-7.90%)</td><td>0.06 <b>(+162.13%)</b></td><td>235.80 (+8.56%)</td><td>172.38 (-11.17%)</td><td>174.60 (-7.81%)</td><td>133.20 <b>(-21.97%)</b></td><td>40.07 <b>(+121.66%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>217.20 (n/a)</td><td>194.06 (n/a)</td><td>189.40 (n/a)</td><td>170.70 (n/a)</td><td>18.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.31 <b>(-27.43%)</b></td><td>0.27 (-10.96%)</td><td>0.30 (+3.92%)</td><td>0.20 (-10.49%)</td><td>0.05 <b>(-30.98%)</b></td><td>251.70 (+11.72%)</td><td>191.66 (+10.99%)</td><td>163.50 (-3.77%)</td><td>157.70 <b>(+37.85%)</b></td><td>43.52 (+7.31%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>225.30 (n/a)</td><td>172.68 (n/a)</td><td>169.90 (n/a)</td><td>114.40 (n/a)</td><td>40.55 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 (-13.15%)</td><td>0.24 (-10.78%)</td><td>0.25 (-9.99%)</td><td>0.21 (-6.68%)</td><td>0.03 (-13.59%)</td><td>235.70 (+7.14%)</td><td>204.22 (+11.96%)</td><td>194.20 (+11.10%)</td><td>175.10 (+15.12%)</td><td>28.79 (+8.00%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>220.00 (n/a)</td><td>182.40 (n/a)</td><td>174.80 (n/a)</td><td>152.10 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (+7.82%)</td><td>0.01 (-6.88%)</td><td>0.01 (-9.29%)</td><td>0.01 <b>(-23.03%)</b></td><td>0.00 <b>(+89.38%)</b></td><td>266.40 <b>(+29.95%)</b></td><td>192.88 (+11.56%)</td><td>194.10 (+10.22%)</td><td>138.80 (-7.28%)</td><td>49.25 <b>(+128.25%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>172.90 (n/a)</td><td>176.10 (n/a)</td><td>149.70 (n/a)</td><td>21.58 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 <b>(+29.30%)</b></td><td>0.02 (+14.41%)</td><td>0.02 <b>(+23.44%)</b></td><td>0.01 <b>(-22.08%)</b></td><td>0.00 <b>(+228.13%)</b></td><td>228.60 <b>(+28.35%)</b></td><td>153.84 (-7.94%)</td><td>137.10 (-19.02%)</td><td>112.70 <b>(-22.65%)</b></td><td>44.96 <b>(+238.76%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>178.10 (n/a)</td><td>167.10 (n/a)</td><td>169.30 (n/a)</td><td>145.70 (n/a)</td><td>13.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 <b>(+54.76%)</b></td><td>0.02 <b>(+39.51%)</b></td><td>0.02 <b>(+38.38%)</b></td><td>0.02 <b>(+28.59%)</b></td><td>0.00 <b>(+102.15%)</b></td><td>167.40 <b>(-22.25%)</b></td><td>139.24 <b>(-27.33%)</b></td><td>142.80 <b>(-27.73%)</b></td><td>101.90 <b>(-35.38%)</b></td><td>24.49 (-2.07%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>215.30 (n/a)</td><td>191.60 (n/a)</td><td>197.60 (n/a)</td><td>157.70 (n/a)</td><td>25.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (+1.33%)</td><td>0.02 (+16.53%)</td><td>0.02 <b>(+22.02%)</b></td><td>0.01 <b>(+24.01%)</b></td><td>0.00 <b>(-25.70%)</b></td><td>191.00 (-19.34%)</td><td>156.40 (-15.81%)</td><td>152.50 (-18.05%)</td><td>129.20 (-1.30%)</td><td>23.15 <b>(-38.48%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>236.80 (n/a)</td><td>185.78 (n/a)</td><td>186.10 (n/a)</td><td>130.90 (n/a)</td><td>37.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 <b>(+46.63%)</b></td><td>0.02 <b>(+46.78%)</b></td><td>0.02 <b>(+49.33%)</b></td><td>0.02 <b>(+39.48%)</b></td><td>0.00 <b>(+51.82%)</b></td><td>147.10 <b>(-28.31%)</b></td><td>130.08 <b>(-31.77%)</b></td><td>135.80 <b>(-33.07%)</b></td><td>99.70 <b>(-31.85%)</b></td><td>18.47 <b>(-26.74%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.20 (n/a)</td><td>190.64 (n/a)</td><td>202.90 (n/a)</td><td>146.30 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (-1.11%)</td><td>0.01 (+0.48%)</td><td>0.01 (+8.81%)</td><td>0.01 (-1.42%)</td><td>0.00 (+0.86%)</td><td>208.60 (+1.41%)</td><td>181.26 (-0.40%)</td><td>176.50 (-8.07%)</td><td>154.70 (+1.11%)</td><td>23.50 (+5.24%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.70 (n/a)</td><td>181.98 (n/a)</td><td>192.00 (n/a)</td><td>153.00 (n/a)</td><td>22.33 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (+9.24%)</td><td>0.02 (+5.22%)</td><td>0.02 (+6.24%)</td><td>0.01 (-14.21%)</td><td>0.00 <b>(+84.90%)</b></td><td>231.80 (+16.54%)</td><td>169.92 (-2.89%)</td><td>162.00 (-5.92%)</td><td>141.50 (-8.41%)</td><td>35.86 <b>(+103.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>198.90 (n/a)</td><td>174.98 (n/a)</td><td>172.20 (n/a)</td><td>154.50 (n/a)</td><td>17.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (-0.52%)</td><td>0.01 (+19.94%)</td><td>0.01 (+16.79%)</td><td>0.01 <b>(+50.40%)</b></td><td>0.00 <b>(-63.87%)</b></td><td>208.40 <b>(-33.50%)</b></td><td>182.34 <b>(-20.49%)</b></td><td>178.00 (-14.38%)</td><td>172.80 (+0.52%)</td><td>14.77 <b>(-75.55%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>313.40 (n/a)</td><td>229.34 (n/a)</td><td>207.90 (n/a)</td><td>171.90 (n/a)</td><td>60.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 <b>(+24.54%)</b></td><td>0.04 <b>(+35.52%)</b></td><td>0.04 <b>(+39.65%)</b></td><td>0.04 <b>(+42.46%)</b></td><td>0.00 (-17.50%)</td><td>141.60 <b>(-29.80%)</b></td><td>125.40 <b>(-26.80%)</b></td><td>121.90 <b>(-28.38%)</b></td><td>114.40 (-19.72%)</td><td>10.29 <b>(-52.92%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.70 (n/a)</td><td>171.30 (n/a)</td><td>170.20 (n/a)</td><td>142.50 (n/a)</td><td>21.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 <b>(+30.66%)</b></td><td>0.03 <b>(+27.69%)</b></td><td>0.04 <b>(+49.61%)</b></td><td>0.03 (+8.00%)</td><td>0.01 <b>(+80.13%)</b></td><td>202.90 (-7.39%)</td><td>157.32 <b>(-20.42%)</b></td><td>139.00 <b>(-33.17%)</b></td><td>131.40 <b>(-23.47%)</b></td><td>30.90 <b>(+28.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.10 (n/a)</td><td>197.70 (n/a)</td><td>208.00 (n/a)</td><td>171.70 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 <b>(+28.94%)</b></td><td>0.04 <b>(+37.02%)</b></td><td>0.03 <b>(+50.21%)</b></td><td>0.03 <b>(+47.32%)</b></td><td>0.00 (-11.67%)</td><td>169.30 <b>(-32.12%)</b></td><td>149.82 <b>(-28.39%)</b></td><td>151.90 <b>(-33.44%)</b></td><td>126.60 <b>(-22.43%)</b></td><td>19.71 <b>(-51.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.40 (n/a)</td><td>209.22 (n/a)</td><td>228.20 (n/a)</td><td>163.20 (n/a)</td><td>41.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-16.74%)</td><td>0.03 (-12.35%)</td><td>0.03 (-8.13%)</td><td>0.02 (-13.94%)</td><td>0.00 <b>(-22.35%)</b></td><td>213.10 (+16.19%)</td><td>184.50 (+13.73%)</td><td>188.20 (+8.85%)</td><td>155.20 <b>(+20.12%)</b></td><td>24.93 (+7.16%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>162.22 (n/a)</td><td>172.90 (n/a)</td><td>129.20 (n/a)</td><td>23.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 <b>(+20.65%)</b></td><td>0.03 (-1.47%)</td><td>0.03 (-5.73%)</td><td>0.02 (-10.34%)</td><td>0.01 <b>(+125.23%)</b></td><td>222.00 (+11.50%)</td><td>184.30 (+4.50%)</td><td>185.10 (+6.07%)</td><td>125.80 (-17.13%)</td><td>36.24 <b>(+100.16%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>199.10 (n/a)</td><td>176.36 (n/a)</td><td>174.50 (n/a)</td><td>151.80 (n/a)</td><td>18.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 <b>(+31.06%)</b></td><td>0.03 (-2.51%)</td><td>0.02 (-17.92%)</td><td>0.02 <b>(-39.12%)</b></td><td>0.01 <b>(+545.18%)</b></td><td>322.90 <b>(+64.24%)</b></td><td>211.30 (+14.29%)</td><td>227.50 <b>(+21.85%)</b></td><td>129.40 <b>(-23.70%)</b></td><td>77.78 <b>(+680.99%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>196.60 (n/a)</td><td>184.88 (n/a)</td><td>186.70 (n/a)</td><td>169.60 (n/a)</td><td>9.96 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (-19.42%)</td><td>0.03 (-10.47%)</td><td>0.03 (-5.99%)</td><td>0.02 (+4.67%)</td><td>0.01 <b>(-33.82%)</b></td><td>242.50 (-4.45%)</td><td>189.56 (+7.81%)</td><td>177.70 (+6.41%)</td><td>133.40 <b>(+24.09%)</b></td><td>43.57 (-19.67%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.80 (n/a)</td><td>175.82 (n/a)</td><td>167.00 (n/a)</td><td>107.50 (n/a)</td><td>54.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-8.62%)</td><td>0.03 (-3.45%)</td><td>0.03 (-2.69%)</td><td>0.02 (-7.58%)</td><td>0.00 <b>(-21.79%)</b></td><td>241.50 (+8.20%)</td><td>201.20 (+3.06%)</td><td>194.80 (+2.74%)</td><td>171.40 (+9.38%)</td><td>25.62 (-7.74%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.20 (n/a)</td><td>195.22 (n/a)</td><td>189.60 (n/a)</td><td>156.70 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (-14.04%)</td><td>0.07 (+2.82%)</td><td>0.06 (+8.01%)</td><td>0.06 (+13.60%)</td><td>0.01 <b>(-42.31%)</b></td><td>189.00 (-11.97%)</td><td>159.76 (-6.53%)</td><td>163.40 (-7.42%)</td><td>129.50 (+16.35%)</td><td>25.34 <b>(-42.35%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>170.92 (n/a)</td><td>176.50 (n/a)</td><td>111.30 (n/a)</td><td>43.95 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (+16.89%)</td><td>0.06 (+11.49%)</td><td>0.06 (+7.44%)</td><td>0.05 <b>(+44.07%)</b></td><td>0.01 <b>(-20.83%)</b></td><td>191.90 <b>(-30.60%)</b></td><td>169.48 (-13.10%)</td><td>177.50 (-6.92%)</td><td>128.40 (-14.46%)</td><td>24.11 <b>(-53.42%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>276.50 (n/a)</td><td>195.02 (n/a)</td><td>190.70 (n/a)</td><td>150.10 (n/a)</td><td>51.77 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (-17.78%)</td><td>0.06 (+2.16%)</td><td>0.07 (+10.89%)</td><td>0.05 (+15.03%)</td><td>0.01 <b>(-50.88%)</b></td><td>194.10 (-13.08%)</td><td>163.62 (-4.62%)</td><td>154.00 (-9.78%)</td><td>150.50 <b>(+21.57%)</b></td><td>18.53 <b>(-47.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>171.54 (n/a)</td><td>170.70 (n/a)</td><td>123.80 (n/a)</td><td>35.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (-16.46%)</td><td>0.06 (-10.79%)</td><td>0.06 (-15.48%)</td><td>0.05 (-4.53%)</td><td>0.01 <b>(-29.06%)</b></td><td>213.30 (+4.76%)</td><td>180.52 (+10.97%)</td><td>182.70 (+18.25%)</td><td>152.70 (+19.67%)</td><td>25.74 (-13.17%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>162.68 (n/a)</td><td>154.50 (n/a)</td><td>127.60 (n/a)</td><td>29.65 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 <b>(+47.76%)</b></td><td>0.06 (+7.30%)</td><td>0.06 (+1.23%)</td><td>0.05 (-9.68%)</td><td>0.02 <b>(+382.52%)</b></td><td>212.40 (+10.68%)</td><td>171.86 (-2.15%)</td><td>175.50 (-1.24%)</td><td>109.80 <b>(-32.31%)</b></td><td>38.98 <b>(+246.78%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>191.90 (n/a)</td><td>175.64 (n/a)</td><td>177.70 (n/a)</td><td>162.20 (n/a)</td><td>11.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (+12.36%)</td><td>0.05 (-1.47%)</td><td>0.05 (-1.59%)</td><td>0.03 <b>(-30.72%)</b></td><td>0.01 <b>(+133.35%)</b></td><td>307.40 <b>(+44.32%)</b></td><td>207.56 (+6.87%)</td><td>200.10 (+1.63%)</td><td>144.40 (-10.97%)</td><td>60.70 <b>(+216.84%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>194.22 (n/a)</td><td>196.90 (n/a)</td><td>162.20 (n/a)</td><td>19.16 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (+4.23%)</td><td>0.06 (-6.75%)</td><td>0.06 (-3.17%)</td><td>0.05 (-4.09%)</td><td>0.01 (+10.92%)</td><td>224.90 (+4.27%)</td><td>181.72 (+7.83%)</td><td>181.10 (+3.25%)</td><td>127.90 (-4.12%)</td><td>35.25 (+8.53%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>168.52 (n/a)</td><td>175.40 (n/a)</td><td>133.40 (n/a)</td><td>32.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (-6.14%)</td><td>0.05 (-4.84%)</td><td>0.05 (-6.78%)</td><td>0.04 (-2.22%)</td><td>0.01 (+1.83%)</td><td>254.10 (+2.25%)</td><td>212.86 (+5.23%)</td><td>217.50 (+7.25%)</td><td>180.90 (+6.54%)</td><td>31.67 (+6.63%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>248.50 (n/a)</td><td>202.28 (n/a)</td><td>202.80 (n/a)</td><td>169.80 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (-8.53%)</td><td>0.14 (+12.29%)</td><td>0.15 <b>(+22.99%)</b></td><td>0.12 <b>(+27.00%)</b></td><td>0.02 <b>(-34.99%)</b></td><td>177.80 <b>(-21.26%)</b></td><td>151.04 (-13.19%)</td><td>142.90 (-18.71%)</td><td>130.20 (+9.32%)</td><td>22.01 <b>(-41.77%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>225.80 (n/a)</td><td>173.98 (n/a)</td><td>175.80 (n/a)</td><td>119.10 (n/a)</td><td>37.79 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (+2.38%)</td><td>0.10 (-3.39%)</td><td>0.11 (+2.16%)</td><td>0.07 (-19.35%)</td><td>0.02 <b>(+69.76%)</b></td><td>289.70 <b>(+23.96%)</b></td><td>213.40 (+6.92%)</td><td>198.80 (-2.12%)</td><td>166.90 (-2.34%)</td><td>52.95 <b>(+102.92%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>233.70 (n/a)</td><td>199.58 (n/a)</td><td>203.10 (n/a)</td><td>170.90 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (+1.76%)</td><td>0.12 (+13.54%)</td><td>0.12 (+5.63%)</td><td>0.11 <b>(+59.88%)</b></td><td>0.01 <b>(-51.95%)</b></td><td>186.00 <b>(-37.46%)</b></td><td>170.28 (-15.59%)</td><td>177.70 (-5.33%)</td><td>149.00 (-1.72%)</td><td>15.45 <b>(-72.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>297.40 (n/a)</td><td>201.74 (n/a)</td><td>187.70 (n/a)</td><td>151.60 (n/a)</td><td>55.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (+13.70%)</td><td>0.11 (+5.56%)</td><td>0.11 (+9.01%)</td><td>0.10 (+0.51%)</td><td>0.01 <b>(+40.80%)</b></td><td>213.80 (-0.51%)</td><td>189.00 (-4.80%)</td><td>192.10 (-8.26%)</td><td>157.60 (-12.00%)</td><td>21.92 <b>(+23.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>198.52 (n/a)</td><td>209.40 (n/a)</td><td>179.10 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (-1.67%)</td><td>0.10 (-8.28%)</td><td>0.11 (-5.49%)</td><td>0.08 (-19.01%)</td><td>0.02 <b>(+73.64%)</b></td><td>264.40 <b>(+23.44%)</b></td><td>213.52 (+11.34%)</td><td>193.70 (+5.85%)</td><td>174.90 (+1.69%)</td><td>41.31 <b>(+117.53%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>191.78 (n/a)</td><td>183.00 (n/a)</td><td>172.00 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (+9.50%)</td><td>0.10 (-4.00%)</td><td>0.10 (-14.54%)</td><td>0.08 (-4.89%)</td><td>0.02 <b>(+55.07%)</b></td><td>252.20 (+5.17%)</td><td>209.34 (+5.61%)</td><td>220.00 (+17.02%)</td><td>161.10 (-8.67%)</td><td>35.82 <b>(+44.52%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>239.80 (n/a)</td><td>198.22 (n/a)</td><td>188.00 (n/a)</td><td>176.40 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (-14.88%)</td><td>0.11 (-4.88%)</td><td>0.11 (-2.70%)</td><td>0.10 (+16.51%)</td><td>0.01 <b>(-64.14%)</b></td><td>207.50 (-14.19%)</td><td>188.54 (+1.61%)</td><td>193.90 (+2.76%)</td><td>170.10 (+17.47%)</td><td>15.41 <b>(-62.67%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>241.80 (n/a)</td><td>185.56 (n/a)</td><td>188.70 (n/a)</td><td>144.80 (n/a)</td><td>41.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (+3.46%)</td><td>0.10 (+0.01%)</td><td>0.10 (-5.18%)</td><td>0.09 (+4.51%)</td><td>0.01 (-1.16%)</td><td>223.50 (-4.32%)</td><td>214.44 (-0.04%)</td><td>219.30 (+5.43%)</td><td>198.10 (-3.37%)</td><td>11.00 (-8.19%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>214.52 (n/a)</td><td>208.00 (n/a)</td><td>205.00 (n/a)</td><td>11.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>161.30 (n/a)</td><td>173.60 (n/a)</td><td>121.20 (n/a)</td><td>23.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.40 (n/a)</td><td>161.92 (n/a)</td><td>173.90 (n/a)</td><td>133.60 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>161.76 (n/a)</td><td>158.00 (n/a)</td><td>137.10 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.50 (n/a)</td><td>210.08 (n/a)</td><td>233.10 (n/a)</td><td>159.10 (n/a)</td><td>40.59 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>151.44 (n/a)</td><td>143.80 (n/a)</td><td>124.00 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>161.60 (n/a)</td><td>142.34 (n/a)</td><td>135.30 (n/a)</td><td>133.60 (n/a)</td><td>12.20 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>199.30 (n/a)</td><td>160.54 (n/a)</td><td>161.90 (n/a)</td><td>118.70 (n/a)</td><td>37.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>174.38 (n/a)</td><td>172.90 (n/a)</td><td>135.40 (n/a)</td><td>29.97 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>244.10 (n/a)</td><td>170.98 (n/a)</td><td>146.50 (n/a)</td><td>131.60 (n/a)</td><td>49.54 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>168.90 (n/a)</td><td>148.92 (n/a)</td><td>154.70 (n/a)</td><td>124.60 (n/a)</td><td>20.54 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.00 (n/a)</td><td>178.98 (n/a)</td><td>176.10 (n/a)</td><td>126.00 (n/a)</td><td>35.42 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.00 (n/a)</td><td>186.90 (n/a)</td><td>171.50 (n/a)</td><td>163.50 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.38 (+7.11%)</td><td>0.32 (+6.96%)</td><td>0.35 (+18.42%)</td><td>0.24 (-10.78%)</td><td>0.06 <b>(+86.71%)</b></td><td>204.10 (+12.08%)</td><td>156.74 (-4.51%)</td><td>141.10 (-15.56%)</td><td>129.90 (-6.68%)</td><td>31.45 <b>(+98.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>182.10 (n/a)</td><td>164.14 (n/a)</td><td>167.10 (n/a)</td><td>139.20 (n/a)</td><td>15.88 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>186.80 (n/a)</td><td>155.64 (n/a)</td><td>153.30 (n/a)</td><td>114.90 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>205.40 (n/a)</td><td>172.92 (n/a)</td><td>182.90 (n/a)</td><td>133.60 (n/a)</td><td>31.47 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>256.40 (n/a)</td><td>215.40 (n/a)</td><td>220.70 (n/a)</td><td>164.50 (n/a)</td><td>36.54 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>163.66 (n/a)</td><td>161.50 (n/a)</td><td>128.70 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>202.90 (n/a)</td><td>171.32 (n/a)</td><td>168.60 (n/a)</td><td>155.10 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>321.20 (n/a)</td><td>199.14 (n/a)</td><td>163.80 (n/a)</td><td>142.80 (n/a)</td><td>72.75 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>277.90 (n/a)</td><td>210.40 (n/a)</td><td>216.90 (n/a)</td><td>140.60 (n/a)</td><td>56.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>268.30 (n/a)</td><td>164.98 (n/a)</td><td>146.10 (n/a)</td><td>105.00 (n/a)</td><td>61.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>178.66 (n/a)</td><td>163.90 (n/a)</td><td>141.70 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>314.90 (n/a)</td><td>188.92 (n/a)</td><td>162.20 (n/a)</td><td>123.60 (n/a)</td><td>73.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>182.22 (n/a)</td><td>172.10 (n/a)</td><td>163.60 (n/a)</td><td>29.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>181.90 (n/a)</td><td>164.84 (n/a)</td><td>170.50 (n/a)</td><td>144.90 (n/a)</td><td>15.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>207.30 (n/a)</td><td>167.06 (n/a)</td><td>166.80 (n/a)</td><td>138.40 (n/a)</td><td>28.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>253.10 (n/a)</td><td>193.52 (n/a)</td><td>183.10 (n/a)</td><td>158.70 (n/a)</td><td>35.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.40 (n/a)</td><td>178.80 (n/a)</td><td>189.90 (n/a)</td><td>141.70 (n/a)</td><td>33.83 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>186.80 (n/a)</td><td>156.22 (n/a)</td><td>157.00 (n/a)</td><td>126.40 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>213.10 (n/a)</td><td>178.76 (n/a)</td><td>171.10 (n/a)</td><td>143.70 (n/a)</td><td>30.61 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>218.80 (n/a)</td><td>185.54 (n/a)</td><td>185.90 (n/a)</td><td>152.70 (n/a)</td><td>32.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.03 (-9.70%)</td><td>13.63 (-2.48%)</td><td>13.93 (-0.72%)</td><td>12.83 (+5.59%)</td><td>0.51 <b>(-60.69%)</b></td><td>4343.00 (-5.29%)</td><td>4090.38 (+1.94%)</td><td>3998.60 (+0.73%)</td><td>3971.70 (+10.74%)</td><td>156.78 <b>(-58.97%)</b></td><td>13517.38 (-9.70%)</td><td>13140.21 (-2.48%)</td><td>13426.58 (-0.72%)</td><td>12361.80 (+5.59%)</td><td>488.22 <b>(-60.69%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>15.53 (n/a)</td><td>13.98 (n/a)</td><td>14.03 (n/a)</td><td>12.15 (n/a)</td><td>1.29 (n/a)</td><td>4585.70 (n/a)</td><td>4012.56 (n/a)</td><td>3969.70 (n/a)</td><td>3586.40 (n/a)</td><td>382.14 (n/a)</td><td>14969.60 (n/a)</td><td>13474.14 (n/a)</td><td>13524.37 (n/a)</td><td>11707.40 (n/a)</td><td>1241.99 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>22.09 (+9.52%)</td><td>18.13 (+1.83%)</td><td>17.24 (-0.74%)</td><td>16.69 (+4.88%)</td><td>2.26 <b>(+31.10%)</b></td><td>785.50 (-4.65%)</td><td>730.84 (-1.46%)</td><td>760.30 (+0.74%)</td><td>593.20 (-8.70%)</td><td>79.08 (+12.94%)</td><td>14479.96 (+9.52%)</td><td>11881.00 (+1.83%)</td><td>11297.83 (-0.74%)</td><td>10936.13 (+4.88%)</td><td>1477.88 <b>(+31.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>20.17 (n/a)</td><td>17.80 (n/a)</td><td>17.37 (n/a)</td><td>15.91 (n/a)</td><td>1.72 (n/a)</td><td>823.80 (n/a)</td><td>741.64 (n/a)</td><td>754.70 (n/a)</td><td>649.70 (n/a)</td><td>70.02 (n/a)</td><td>13221.24 (n/a)</td><td>11667.47 (n/a)</td><td>11381.81 (n/a)</td><td>10427.74 (n/a)</td><td>1127.33 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.03 (-6.90%)</td><td>12.93 (-6.41%)</td><td>12.77 (-8.35%)</td><td>12.43 (+2.77%)</td><td>0.63 <b>(-41.48%)</b></td><td>4481.10 (-2.70%)</td><td>4316.70 (+6.48%)</td><td>4363.50 (+9.12%)</td><td>3969.50 (+7.41%)</td><td>200.17 <b>(-40.41%)</b></td><td>13525.06 (-6.90%)</td><td>12459.79 (-6.41%)</td><td>12303.69 (-8.35%)</td><td>11980.87 (+2.77%)</td><td>610.52 <b>(-41.48%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>15.07 (n/a)</td><td>13.81 (n/a)</td><td>13.93 (n/a)</td><td>12.10 (n/a)</td><td>1.08 (n/a)</td><td>4605.30 (n/a)</td><td>4053.84 (n/a)</td><td>3998.90 (n/a)</td><td>3695.60 (n/a)</td><td>335.93 (n/a)</td><td>14527.40 (n/a)</td><td>13312.50 (n/a)</td><td>13425.36 (n/a)</td><td>11657.66 (n/a)</td><td>1043.25 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>19.29 (+1.15%)</td><td>16.45 (-3.29%)</td><td>17.53 (+2.15%)</td><td>11.07 (-14.80%)</td><td>3.16 <b>(+29.16%)</b></td><td>1613.90 (+17.37%)</td><td>1127.64 (+5.38%)</td><td>1018.50 (-2.11%)</td><td>925.70 (-1.13%)</td><td>277.06 <b>(+55.12%)</b></td><td>14499.82 (+1.15%)</td><td>12366.82 (-3.29%)</td><td>13177.36 (+2.15%)</td><td>8316.51 (-14.80%)</td><td>2377.95 <b>(+29.16%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>19.07 (n/a)</td><td>17.01 (n/a)</td><td>17.16 (n/a)</td><td>12.99 (n/a)</td><td>2.45 (n/a)</td><td>1375.00 (n/a)</td><td>1070.06 (n/a)</td><td>1040.50 (n/a)</td><td>936.30 (n/a)</td><td>178.61 (n/a)</td><td>14334.57 (n/a)</td><td>12787.54 (n/a)</td><td>12899.96 (n/a)</td><td>9761.02 (n/a)</td><td>1841.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>10.97 (-0.25%)</td><td>10.76 (+1.62%)</td><td>10.79 (+2.37%)</td><td>10.47 (+2.56%)</td><td>0.21 <b>(-31.35%)</b></td><td>7822.30 (-2.50%)</td><td>7614.30 (-1.63%)</td><td>7595.50 (-2.31%)</td><td>7467.00 (+0.25%)</td><td>146.13 <b>(-32.89%)</b></td><td>14379.85 (-0.25%)</td><td>14105.78 (+1.62%)</td><td>14136.62 (+2.37%)</td><td>13726.67 (+2.56%)</td><td>268.90 <b>(-31.35%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>11.00 (n/a)</td><td>10.59 (n/a)</td><td>10.54 (n/a)</td><td>10.21 (n/a)</td><td>0.30 (n/a)</td><td>8022.90 (n/a)</td><td>7740.14 (n/a)</td><td>7775.30 (n/a)</td><td>7448.40 (n/a)</td><td>217.77 (n/a)</td><td>14415.72 (n/a)</td><td>13881.19 (n/a)</td><td>13809.72 (n/a)</td><td>13383.46 (n/a)</td><td>391.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>19.93 (-1.61%)</td><td>17.46 (-0.52%)</td><td>18.16 (-1.51%)</td><td>12.61 (+2.91%)</td><td>2.82 (-8.59%)</td><td>1704.20 (-2.83%)</td><td>1263.62 (-0.03%)</td><td>1183.70 (+1.53%)</td><td>1078.40 (+1.64%)</td><td>250.74 (-10.00%)</td><td>15931.01 (-1.61%)</td><td>13951.67 (-0.52%)</td><td>14513.19 (-1.51%)</td><td>10080.76 (+2.91%)</td><td>2252.83 (-8.58%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>20.26 (n/a)</td><td>17.55 (n/a)</td><td>18.44 (n/a)</td><td>12.26 (n/a)</td><td>3.08 (n/a)</td><td>1753.80 (n/a)</td><td>1263.96 (n/a)</td><td>1165.90 (n/a)</td><td>1061.00 (n/a)</td><td>278.59 (n/a)</td><td>16191.39 (n/a)</td><td>14024.24 (n/a)</td><td>14735.68 (n/a)</td><td>9795.52 (n/a)</td><td>2464.39 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.38 (+6.92%)</td><td>12.35 (+1.35%)</td><td>12.42 (+0.51%)</td><td>11.08 (-1.12%)</td><td>0.82 <b>(+48.70%)</b></td><td>7393.70 (+1.13%)</td><td>6659.14 (-1.15%)</td><td>6595.70 (-0.51%)</td><td>6122.50 (-6.48%)</td><td>458.54 <b>(+41.56%)</b></td><td>17537.63 (+6.92%)</td><td>16183.44 (+1.35%)</td><td>16279.39 (+0.51%)</td><td>14522.42 (-1.12%)</td><td>1075.49 <b>(+48.70%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>12.51 (n/a)</td><td>12.18 (n/a)</td><td>12.36 (n/a)</td><td>11.20 (n/a)</td><td>0.55 (n/a)</td><td>7311.00 (n/a)</td><td>6736.34 (n/a)</td><td>6629.40 (n/a)</td><td>6546.50 (n/a)</td><td>323.93 (n/a)</td><td>16401.82 (n/a)</td><td>15967.33 (n/a)</td><td>16196.72 (n/a)</td><td>14686.61 (n/a)</td><td>723.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.14 (+4.88%)</td><td>4.07 (+4.36%)</td><td>3.93 (-5.35%)</td><td>3.13 (+4.69%)</td><td>0.97 <b>(+20.36%)</b></td><td>440.10 (-4.47%)</td><td>354.00 (-3.18%)</td><td>350.00 (+5.68%)</td><td>267.70 (-4.67%)</td><td>83.48 (+7.33%)</td><td>1002.75 (+4.88%)</td><td>793.78 (+4.36%)</td><td>767.03 (-5.35%)</td><td>609.99 (+4.69%)</td><td>188.99 <b>(+20.36%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.90 (n/a)</td><td>3.90 (n/a)</td><td>4.15 (n/a)</td><td>2.99 (n/a)</td><td>0.81 (n/a)</td><td>460.70 (n/a)</td><td>365.64 (n/a)</td><td>331.20 (n/a)</td><td>280.80 (n/a)</td><td>77.78 (n/a)</td><td>956.06 (n/a)</td><td>760.64 (n/a)</td><td>810.37 (n/a)</td><td>582.65 (n/a)</td><td>157.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>6.27 (-7.06%)</td><td>4.16 (-5.19%)</td><td>3.60 (-7.07%)</td><td>3.48 (-2.16%)</td><td>1.19 (-10.75%)</td><td>395.50 (+2.20%)</td><td>347.56 (+4.83%)</td><td>382.40 (+7.60%)</td><td>219.40 (+7.55%)</td><td>73.83 (-0.51%)</td><td>1223.24 (-7.06%)</td><td>811.66 (-5.19%)</td><td>701.89 (-7.07%)</td><td>678.74 (-2.16%)</td><td>232.70 (-10.75%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>6.75 (n/a)</td><td>4.39 (n/a)</td><td>3.87 (n/a)</td><td>3.56 (n/a)</td><td>1.34 (n/a)</td><td>387.00 (n/a)</td><td>331.54 (n/a)</td><td>355.40 (n/a)</td><td>204.00 (n/a)</td><td>74.21 (n/a)</td><td>1316.13 (n/a)</td><td>856.05 (n/a)</td><td>755.29 (n/a)</td><td>693.69 (n/a)</td><td>260.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.94 (-3.03%)</td><td>4.93 (-3.47%)</td><td>3.92 (-3.32%)</td><td>3.61 (+1.50%)</td><td>1.81 (-5.24%)</td><td>381.00 (-1.50%)</td><td>304.00 (+2.88%)</td><td>351.50 (+3.44%)</td><td>173.20 (+3.10%)</td><td>86.93 (-2.87%)</td><td>1549.41 (-3.03%)</td><td>962.43 (-3.47%)</td><td>763.73 (-3.32%)</td><td>704.47 (+1.50%)</td><td>353.87 (-5.24%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.19 (n/a)</td><td>5.11 (n/a)</td><td>4.05 (n/a)</td><td>3.56 (n/a)</td><td>1.91 (n/a)</td><td>386.80 (n/a)</td><td>295.48 (n/a)</td><td>339.80 (n/a)</td><td>168.00 (n/a)</td><td>89.50 (n/a)</td><td>1597.83 (n/a)</td><td>997.05 (n/a)</td><td>789.99 (n/a)</td><td>694.03 (n/a)</td><td>373.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>9.00 <b>(+31.82%)</b></td><td>5.48 <b>(+21.29%)</b></td><td>5.53 <b>(+33.68%)</b></td><td>3.45 (-5.41%)</td><td>2.25 <b>(+71.41%)</b></td><td>398.90 (+5.72%)</td><td>284.00 (-11.43%)</td><td>249.00 <b>(-25.18%)</b></td><td>152.90 <b>(-24.16%)</b></td><td>104.52 <b>(+50.17%)</b></td><td>1755.50 <b>(+31.82%)</b></td><td>1068.83 <b>(+21.29%)</b></td><td>1078.21 <b>(+33.68%)</b></td><td>672.99 (-5.41%)</td><td>438.26 <b>(+71.41%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>6.83 (n/a)</td><td>4.52 (n/a)</td><td>4.14 (n/a)</td><td>3.65 (n/a)</td><td>1.31 (n/a)</td><td>377.30 (n/a)</td><td>320.64 (n/a)</td><td>332.80 (n/a)</td><td>201.60 (n/a)</td><td>69.60 (n/a)</td><td>1331.70 (n/a)</td><td>881.25 (n/a)</td><td>806.57 (n/a)</td><td>711.51 (n/a)</td><td>255.69 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.63 <b>(+27.93%)</b></td><td>3.77 (+4.21%)</td><td>3.34 (-3.28%)</td><td>3.20 (-1.59%)</td><td>1.05 <b>(+130.82%)</b></td><td>429.70 (+1.63%)</td><td>382.74 (-0.60%)</td><td>411.90 (+3.39%)</td><td>244.50 <b>(-21.81%)</b></td><td>78.02 <b>(+83.79%)</b></td><td>1098.09 <b>(+27.93%)</b></td><td>734.56 (+4.21%)</td><td>651.69 (-3.28%)</td><td>624.77 (-1.59%)</td><td>203.90 <b>(+130.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.40 (n/a)</td><td>3.61 (n/a)</td><td>3.45 (n/a)</td><td>3.25 (n/a)</td><td>0.45 (n/a)</td><td>422.80 (n/a)</td><td>385.06 (n/a)</td><td>398.40 (n/a)</td><td>312.70 (n/a)</td><td>42.45 (n/a)</td><td>858.35 (n/a)</td><td>704.89 (n/a)</td><td>673.80 (n/a)</td><td>634.88 (n/a)</td><td>88.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.22 (-18.77%)</td><td>4.08 (-11.31%)</td><td>4.45 (-0.77%)</td><td>2.98 (-8.69%)</td><td>0.97 <b>(-25.32%)</b></td><td>461.40 (+9.52%)</td><td>354.46 (+11.19%)</td><td>309.30 (+0.78%)</td><td>263.50 <b>(+23.07%)</b></td><td>89.04 (+2.25%)</td><td>1018.65 (-18.77%)</td><td>795.18 (-11.31%)</td><td>867.89 (-0.77%)</td><td>581.77 (-8.69%)</td><td>189.74 <b>(-25.32%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>6.43 (n/a)</td><td>4.60 (n/a)</td><td>4.48 (n/a)</td><td>3.27 (n/a)</td><td>1.30 (n/a)</td><td>421.30 (n/a)</td><td>318.80 (n/a)</td><td>306.90 (n/a)</td><td>214.10 (n/a)</td><td>87.08 (n/a)</td><td>1253.98 (n/a)</td><td>896.59 (n/a)</td><td>874.66 (n/a)</td><td>637.17 (n/a)</td><td>254.06 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>4.45 (-7.51%)</td><td>3.44 (-14.76%)</td><td>3.22 (-17.65%)</td><td>3.12 (-1.40%)</td><td>0.57 (-9.90%)</td><td>440.40 (+1.40%)</td><td>406.82 (+17.05%)</td><td>427.40 <b>(+21.45%)</b></td><td>309.30 (+8.11%)</td><td>55.41 (-2.56%)</td><td>867.75 (-7.51%)</td><td>671.85 (-14.76%)</td><td>628.12 (-17.65%)</td><td>609.47 (-1.40%)</td><td>110.46 (-9.90%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.81 (n/a)</td><td>4.04 (n/a)</td><td>3.91 (n/a)</td><td>3.17 (n/a)</td><td>0.63 (n/a)</td><td>434.30 (n/a)</td><td>347.56 (n/a)</td><td>351.90 (n/a)</td><td>286.10 (n/a)</td><td>56.87 (n/a)</td><td>938.21 (n/a)</td><td>788.20 (n/a)</td><td>762.71 (n/a)</td><td>618.11 (n/a)</td><td>122.60 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>2.03 (-15.34%)</td><td>1.60 (-7.22%)</td><td>1.58 (-1.40%)</td><td>1.22 (-14.27%)</td><td>0.29 <b>(-27.78%)</b></td><td>328.00 (+16.64%)</td><td>257.04 (+6.71%)</td><td>254.80 (+1.39%)</td><td>198.10 (+18.13%)</td><td>46.53 (+0.58%)</td><td>169.38 (-15.34%)</td><td>133.94 (-7.22%)</td><td>131.68 (-1.40%)</td><td>102.31 (-14.27%)</td><td>23.93 <b>(-27.78%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>2.39 (n/a)</td><td>1.73 (n/a)</td><td>1.60 (n/a)</td><td>1.43 (n/a)</td><td>0.40 (n/a)</td><td>281.20 (n/a)</td><td>240.88 (n/a)</td><td>251.30 (n/a)</td><td>167.70 (n/a)</td><td>46.26 (n/a)</td><td>200.06 (n/a)</td><td>144.35 (n/a)</td><td>133.54 (n/a)</td><td>119.33 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.26 (-15.38%)</td><td>6.04 (-3.54%)</td><td>5.52 (+3.52%)</td><td>5.19 (+5.34%)</td><td>1.00 <b>(-37.43%)</b></td><td>372.80 (-5.07%)</td><td>327.10 (+0.96%)</td><td>350.20 (-3.42%)</td><td>266.40 (+18.19%)</td><td>51.48 <b>(-30.38%)</b></td><td>1511.59 (-15.38%)</td><td>1257.17 (-3.54%)</td><td>1149.63 (+3.52%)</td><td>1080.11 (+5.34%)</td><td>208.68 <b>(-37.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.58 (n/a)</td><td>6.26 (n/a)</td><td>5.33 (n/a)</td><td>4.92 (n/a)</td><td>1.60 (n/a)</td><td>392.70 (n/a)</td><td>323.98 (n/a)</td><td>362.60 (n/a)</td><td>225.40 (n/a)</td><td>73.94 (n/a)</td><td>1786.40 (n/a)</td><td>1303.35 (n/a)</td><td>1110.55 (n/a)</td><td>1025.35 (n/a)</td><td>333.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>15.89 (-15.65%)</td><td>13.13 (-12.94%)</td><td>12.67 <b>(-20.71%)</b></td><td>11.38 (+3.00%)</td><td>1.83 <b>(-40.18%)</b></td><td>483.60 (-2.91%)</td><td>425.32 (+12.51%)</td><td>434.70 <b>(+26.11%)</b></td><td>346.40 (+18.55%)</td><td>55.75 <b>(-31.99%)</b></td><td>6199.81 (-15.65%)</td><td>5123.82 (-12.94%)</td><td>4940.64 <b>(-20.71%)</b></td><td>4440.53 (+3.00%)</td><td>714.19 <b>(-40.18%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>18.84 (n/a)</td><td>15.09 (n/a)</td><td>15.97 (n/a)</td><td>11.05 (n/a)</td><td>3.06 (n/a)</td><td>498.10 (n/a)</td><td>378.02 (n/a)</td><td>344.70 (n/a)</td><td>292.20 (n/a)</td><td>81.98 (n/a)</td><td>7350.22 (n/a)</td><td>5885.64 (n/a)</td><td>6230.80 (n/a)</td><td>4311.19 (n/a)</td><td>1193.83 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>10.83 (-3.96%)</td><td>8.89 (+1.50%)</td><td>8.64 (+3.52%)</td><td>7.98 (+6.20%)</td><td>1.15 <b>(-21.02%)</b></td><td>689.70 (-5.84%)</td><td>626.36 (-2.15%)</td><td>637.50 (-3.39%)</td><td>508.20 (+4.12%)</td><td>72.18 <b>(-20.39%)</b></td><td>4225.36 (-3.96%)</td><td>3469.65 (+1.50%)</td><td>3368.85 (+3.52%)</td><td>3113.77 (+6.20%)</td><td>447.10 <b>(-21.02%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>11.28 (n/a)</td><td>8.76 (n/a)</td><td>8.34 (n/a)</td><td>7.52 (n/a)</td><td>1.45 (n/a)</td><td>732.50 (n/a)</td><td>640.14 (n/a)</td><td>659.90 (n/a)</td><td>488.10 (n/a)</td><td>90.67 (n/a)</td><td>4399.51 (n/a)</td><td>3418.50 (n/a)</td><td>3254.37 (n/a)</td><td>2931.86 (n/a)</td><td>566.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.92 (+11.54%)</td><td>10.31 (-3.63%)</td><td>9.52 (+0.35%)</td><td>8.74 (-1.84%)</td><td>2.61 (+18.41%)</td><td>663.50 (+1.87%)</td><td>585.06 (+4.56%)</td><td>609.50 (-0.34%)</td><td>388.60 (-10.36%)</td><td>113.20 (+5.26%)</td><td>6216.52 (+11.54%)</td><td>4296.49 (-3.63%)</td><td>3963.58 (+0.35%)</td><td>3641.05 (-1.84%)</td><td>1085.95 (+18.41%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.38 (n/a)</td><td>10.70 (n/a)</td><td>9.48 (n/a)</td><td>8.90 (n/a)</td><td>2.20 (n/a)</td><td>651.30 (n/a)</td><td>559.56 (n/a)</td><td>611.60 (n/a)</td><td>433.50 (n/a)</td><td>107.54 (n/a)</td><td>5573.12 (n/a)</td><td>4458.42 (n/a)</td><td>3949.94 (n/a)</td><td>3709.27 (n/a)</td><td>917.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.00 (n/a)</td><td>149.64 (n/a)</td><td>150.20 (n/a)</td><td>123.90 (n/a)</td><td>25.97 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.40 (n/a)</td><td>170.64 (n/a)</td><td>166.60 (n/a)</td><td>162.90 (n/a)</td><td>8.71 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>161.80 (n/a)</td><td>148.30 (n/a)</td><td>119.90 (n/a)</td><td>45.20 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>169.58 (n/a)</td><td>183.50 (n/a)</td><td>115.50 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.80 (n/a)</td><td>183.14 (n/a)</td><td>181.30 (n/a)</td><td>135.10 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.80 (n/a)</td><td>186.14 (n/a)</td><td>179.30 (n/a)</td><td>148.10 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.90 (n/a)</td><td>169.66 (n/a)</td><td>166.00 (n/a)</td><td>146.10 (n/a)</td><td>19.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>317.10 (n/a)</td><td>237.36 (n/a)</td><td>220.70 (n/a)</td><td>207.20 (n/a)</td><td>44.97 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>164.54 (n/a)</td><td>166.20 (n/a)</td><td>126.10 (n/a)</td><td>29.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>337.40 (n/a)</td><td>199.38 (n/a)</td><td>176.40 (n/a)</td><td>113.80 (n/a)</td><td>83.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.00 (n/a)</td><td>193.70 (n/a)</td><td>194.40 (n/a)</td><td>125.30 (n/a)</td><td>48.83 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.50 (n/a)</td><td>160.76 (n/a)</td><td>167.10 (n/a)</td><td>133.70 (n/a)</td><td>15.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>166.20 (n/a)</td><td>146.70 (n/a)</td><td>153.90 (n/a)</td><td>118.80 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>282.50 (n/a)</td><td>190.52 (n/a)</td><td>172.00 (n/a)</td><td>159.60 (n/a)</td><td>51.74 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.10 (n/a)</td><td>204.32 (n/a)</td><td>206.30 (n/a)</td><td>159.70 (n/a)</td><td>33.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>313.50 (n/a)</td><td>256.88 (n/a)</td><td>236.80 (n/a)</td><td>210.20 (n/a)</td><td>46.94 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.80 (n/a)</td><td>171.60 (n/a)</td><td>180.70 (n/a)</td><td>146.60 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>170.54 (n/a)</td><td>173.10 (n/a)</td><td>139.40 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.00 (n/a)</td><td>176.22 (n/a)</td><td>151.60 (n/a)</td><td>142.80 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>196.46 (n/a)</td><td>191.70 (n/a)</td><td>166.70 (n/a)</td><td>26.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.90 (n/a)</td><td>187.98 (n/a)</td><td>197.60 (n/a)</td><td>124.70 (n/a)</td><td>42.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.20 (n/a)</td><td>201.76 (n/a)</td><td>207.90 (n/a)</td><td>162.40 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>244.90 (n/a)</td><td>193.74 (n/a)</td><td>194.80 (n/a)</td><td>134.90 (n/a)</td><td>40.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>340.80 (n/a)</td><td>258.52 (n/a)</td><td>216.40 (n/a)</td><td>210.70 (n/a)</td><td>62.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.30 (n/a)</td><td>173.24 (n/a)</td><td>175.30 (n/a)</td><td>135.50 (n/a)</td><td>30.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>204.20 (n/a)</td><td>176.96 (n/a)</td><td>182.20 (n/a)</td><td>138.50 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>182.18 (n/a)</td><td>182.70 (n/a)</td><td>163.30 (n/a)</td><td>18.95 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.90 (n/a)</td><td>174.48 (n/a)</td><td>178.00 (n/a)</td><td>131.30 (n/a)</td><td>29.30 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.20 (n/a)</td><td>163.34 (n/a)</td><td>142.50 (n/a)</td><td>132.30 (n/a)</td><td>36.93 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>231.90 (n/a)</td><td>184.82 (n/a)</td><td>191.40 (n/a)</td><td>131.90 (n/a)</td><td>40.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>210.50 (n/a)</td><td>184.58 (n/a)</td><td>188.90 (n/a)</td><td>142.50 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>211.76 (n/a)</td><td>215.10 (n/a)</td><td>190.60 (n/a)</td><td>12.01 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>4.19 (+1.73%)</td><td>4.11 (+0.06%)</td><td>4.11 (-0.12%)</td><td>4.07 (-0.66%)</td><td>0.05 <b>(+437.75%)</b></td><td>19325.90 (+0.66%)</td><td>19126.68 (-0.05%)</td><td>19154.10 (+0.12%)</td><td>18762.20 (-1.70%)</td><td>219.46 <b>(+430.94%)</b></td><td>2861.45 (+1.73%)</td><td>2807.22 (+0.06%)</td><td>2802.90 (-0.12%)</td><td>2777.99 (-0.66%)</td><td>32.55 <b>(+437.73%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>4.10 (n/a)</td><td>0.01 (n/a)</td><td>19199.20 (n/a)</td><td>19135.78 (n/a)</td><td>19131.60 (n/a)</td><td>19086.00 (n/a)</td><td>41.33 (n/a)</td><td>2812.91 (n/a)</td><td>2805.60 (n/a)</td><td>2806.20 (n/a)</td><td>2796.32 (n/a)</td><td>6.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>4.95 (+3.08%)</td><td>4.32 (+2.81%)</td><td>4.19 (-0.18%)</td><td>4.06 (+13.63%)</td><td>0.36 (-16.84%)</td><td>2317.00 (-11.99%)</td><td>2189.86 (-3.09%)</td><td>2242.40 (+0.19%)</td><td>1898.40 (-2.98%)</td><td>168.37 <b>(-30.47%)</b></td><td>1948.69 (+3.08%)</td><td>1698.13 (+2.81%)</td><td>1649.77 (-0.18%)</td><td>1596.60 (+13.63%)</td><td>143.40 (-16.84%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.81 (n/a)</td><td>4.20 (n/a)</td><td>4.20 (n/a)</td><td>3.57 (n/a)</td><td>0.44 (n/a)</td><td>2632.80 (n/a)</td><td>2259.78 (n/a)</td><td>2238.20 (n/a)</td><td>1956.80 (n/a)</td><td>242.14 (n/a)</td><td>1890.52 (n/a)</td><td>1651.74 (n/a)</td><td>1652.81 (n/a)</td><td>1405.09 (n/a)</td><td>172.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.31 (-16.43%)</td><td>1.06 (-7.25%)</td><td>1.00 (-12.49%)</td><td>0.91 (+4.64%)</td><td>0.17 <b>(-41.97%)</b></td><td>243.70 (-4.43%)</td><td>212.60 (+4.45%)</td><td>220.10 (+14.28%)</td><td>168.40 (+19.60%)</td><td>31.93 <b>(-36.09%)</b></td><td>56.03 (-16.43%)</td><td>45.26 (-7.25%)</td><td>42.87 (-12.49%)</td><td>38.72 (+4.64%)</td><td>7.29 <b>(-41.97%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.57 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>0.87 (n/a)</td><td>0.29 (n/a)</td><td>255.00 (n/a)</td><td>203.54 (n/a)</td><td>192.60 (n/a)</td><td>140.80 (n/a)</td><td>49.96 (n/a)</td><td>67.05 (n/a)</td><td>48.79 (n/a)</td><td>48.99 (n/a)</td><td>37.00 (n/a)</td><td>12.55 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.32 (-18.06%)</td><td>0.98 (-14.87%)</td><td>0.96 (-16.92%)</td><td>0.69 (+1.59%)</td><td>0.22 <b>(-32.45%)</b></td><td>320.80 (-1.56%)</td><td>236.34 (+13.37%)</td><td>230.50 <b>(+20.37%)</b></td><td>167.50 <b>(+22.00%)</b></td><td>54.67 <b>(-22.26%)</b></td><td>56.34 (-18.06%)</td><td>41.65 (-14.87%)</td><td>40.94 (-16.92%)</td><td>29.42 (+1.59%)</td><td>9.58 <b>(-32.45%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.61 (n/a)</td><td>1.15 (n/a)</td><td>1.15 (n/a)</td><td>0.68 (n/a)</td><td>0.33 (n/a)</td><td>325.90 (n/a)</td><td>208.46 (n/a)</td><td>191.50 (n/a)</td><td>137.30 (n/a)</td><td>70.32 (n/a)</td><td>68.75 (n/a)</td><td>48.93 (n/a)</td><td>49.27 (n/a)</td><td>28.96 (n/a)</td><td>14.19 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.53 (-0.78%)</td><td>0.53 (-0.18%)</td><td>0.53 (-0.10%)</td><td>0.53 (+0.14%)</td><td>0.00 <b>(-86.05%)</b></td><td>47837.50 (-0.14%)</td><td>47813.92 (+0.18%)</td><td>47828.80 (+0.10%)</td><td>47776.40 (+0.78%)</td><td>26.57 <b>(-85.95%)</b></td><td>359.59 (-0.78%)</td><td>359.31 (-0.18%)</td><td>359.19 (-0.10%)</td><td>359.13 (+0.14%)</td><td>0.20 <b>(-86.05%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47903.50 (n/a)</td><td>47730.36 (n/a)</td><td>47782.10 (n/a)</td><td>47406.00 (n/a)</td><td>189.04 (n/a)</td><td>362.40 (n/a)</td><td>359.94 (n/a)</td><td>359.55 (n/a)</td><td>358.63 (n/a)</td><td>1.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (-0.30%)</td><td>0.21 (-0.39%)</td><td>0.21 (-0.51%)</td><td>0.21 (-0.00%)</td><td>0.00 (-8.35%)</td><td>119618.90 (+0.00%)</td><td>118904.72 (+0.39%)</td><td>118747.70 (+0.52%)</td><td>118192.10 (+0.30%)</td><td>652.66 (-8.06%)</td><td>145.36 (-0.30%)</td><td>144.49 (-0.39%)</td><td>144.68 (-0.51%)</td><td>143.62 (-0.00%)</td><td>0.79 (-8.34%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119615.70 (n/a)</td><td>118446.96 (n/a)</td><td>118137.00 (n/a)</td><td>117832.80 (n/a)</td><td>709.85 (n/a)</td><td>145.80 (n/a)</td><td>145.05 (n/a)</td><td>145.42 (n/a)</td><td>143.63 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.91 (-0.84%)</td><td>0.90 (-0.13%)</td><td>0.90 (-0.06%)</td><td>0.90 (+0.09%)</td><td>0.00 <b>(-52.64%)</b></td><td>27992.80 (-0.09%)</td><td>27857.14 (+0.13%)</td><td>27852.40 (+0.06%)</td><td>27777.50 (+0.84%)</td><td>82.13 <b>(-52.21%)</b></td><td>618.48 (-0.84%)</td><td>616.72 (-0.13%)</td><td>616.82 (-0.06%)</td><td>613.72 (+0.09%)</td><td>1.81 <b>(-52.64%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.01 (n/a)</td><td>28018.10 (n/a)</td><td>27820.66 (n/a)</td><td>27836.40 (n/a)</td><td>27545.10 (n/a)</td><td>171.85 (n/a)</td><td>623.70 (n/a)</td><td>617.54 (n/a)</td><td>617.17 (n/a)</td><td>613.17 (n/a)</td><td>3.83 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>3.65 (-0.45%)</td><td>3.59 (+2.12%)</td><td>3.62 (+4.54%)</td><td>3.44 (+1.01%)</td><td>0.08 <b>(-22.38%)</b></td><td>7311.10 (-1.00%)</td><td>7008.92 (-2.11%)</td><td>6947.60 (-4.34%)</td><td>6898.30 (+0.45%)</td><td>170.27 <b>(-22.40%)</b></td><td>2490.44 (-0.45%)</td><td>2452.27 (+2.12%)</td><td>2472.79 (+4.54%)</td><td>2349.84 (+1.01%)</td><td>57.77 <b>(-22.38%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.66 (n/a)</td><td>3.52 (n/a)</td><td>3.47 (n/a)</td><td>3.41 (n/a)</td><td>0.11 (n/a)</td><td>7384.80 (n/a)</td><td>7159.96 (n/a)</td><td>7262.80 (n/a)</td><td>6867.40 (n/a)</td><td>219.42 (n/a)</td><td>2501.66 (n/a)</td><td>2401.26 (n/a)</td><td>2365.45 (n/a)</td><td>2326.39 (n/a)</td><td>74.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>2.97 (-8.06%)</td><td>2.91 (-4.06%)</td><td>2.93 (-5.31%)</td><td>2.80 (+1.53%)</td><td>0.07 <b>(-64.67%)</b></td><td>8981.20 (-1.51%)</td><td>8661.22 (+3.96%)</td><td>8596.00 (+5.61%)</td><td>8476.50 (+8.77%)</td><td>198.01 <b>(-62.22%)</b></td><td>2026.77 (-8.06%)</td><td>1984.36 (-4.06%)</td><td>1998.60 (-5.31%)</td><td>1912.88 (+1.53%)</td><td>44.57 <b>(-64.67%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.23 (n/a)</td><td>3.03 (n/a)</td><td>3.09 (n/a)</td><td>2.76 (n/a)</td><td>0.18 (n/a)</td><td>9118.70 (n/a)</td><td>8331.60 (n/a)</td><td>8139.50 (n/a)</td><td>7793.00 (n/a)</td><td>524.07 (n/a)</td><td>2204.52 (n/a)</td><td>2068.35 (n/a)</td><td>2110.67 (n/a)</td><td>1884.04 (n/a)</td><td>126.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>3.41 (+2.76%)</td><td>3.22 (-0.63%)</td><td>3.18 (-1.85%)</td><td>3.14 (-1.43%)</td><td>0.11 <b>(+88.04%)</b></td><td>8017.50 (+1.45%)</td><td>7822.18 (+0.70%)</td><td>7910.40 (+1.88%)</td><td>7387.60 (-2.68%)</td><td>251.66 <b>(+84.11%)</b></td><td>2325.49 (+2.76%)</td><td>2198.19 (-0.63%)</td><td>2171.82 (-1.85%)</td><td>2142.81 (-1.43%)</td><td>73.39 <b>(+88.04%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.32 (n/a)</td><td>3.24 (n/a)</td><td>3.24 (n/a)</td><td>3.18 (n/a)</td><td>0.06 (n/a)</td><td>7903.10 (n/a)</td><td>7768.00 (n/a)</td><td>7764.40 (n/a)</td><td>7591.40 (n/a)</td><td>136.69 (n/a)</td><td>2263.07 (n/a)</td><td>2212.17 (n/a)</td><td>2212.65 (n/a)</td><td>2173.81 (n/a)</td><td>39.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.80 (+0.24%)</td><td>0.80 (+0.06%)</td><td>0.80 (+0.01%)</td><td>0.80 (-0.02%)</td><td>0.00 <b>(+170.32%)</b></td><td>94896.90 (+0.02%)</td><td>94745.20 (-0.06%)</td><td>94778.70 (-0.01%)</td><td>94516.20 (-0.24%)</td><td>140.07 <b>(+169.51%)</b></td><td>727.07 (+0.24%)</td><td>725.31 (+0.06%)</td><td>725.05 (+0.01%)</td><td>724.15 (-0.02%)</td><td>1.07 <b>(+170.31%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94875.30 (n/a)</td><td>94803.16 (n/a)</td><td>94788.40 (n/a)</td><td>94742.10 (n/a)</td><td>51.97 (n/a)</td><td>725.33 (n/a)</td><td>724.87 (n/a)</td><td>724.98 (n/a)</td><td>724.31 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.73 (+0.01%)</td><td>0.73 (+0.04%)</td><td>0.73 (-0.01%)</td><td>0.73 (+0.20%)</td><td>0.00 <b>(-77.21%)</b></td><td>103332.90 (-0.20%)</td><td>103307.96 (-0.04%)</td><td>103309.80 (+0.01%)</td><td>103267.60 (-0.01%)</td><td>25.47 <b>(-77.29%)</b></td><td>665.45 (+0.01%)</td><td>665.19 (+0.04%)</td><td>665.18 (-0.01%)</td><td>665.03 (+0.20%)</td><td>0.16 <b>(-77.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103544.20 (n/a)</td><td>103344.94 (n/a)</td><td>103303.10 (n/a)</td><td>103272.80 (n/a)</td><td>112.14 (n/a)</td><td>665.42 (n/a)</td><td>664.95 (n/a)</td><td>665.22 (n/a)</td><td>663.67 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.69 (-0.10%)</td><td>0.68 (+0.04%)</td><td>0.68 (-0.06%)</td><td>0.68 (+0.25%)</td><td>0.00 <b>(-41.09%)</b></td><td>110611.60 (-0.25%)</td><td>110341.70 (-0.04%)</td><td>110340.70 (+0.06%)</td><td>110148.70 (+0.10%)</td><td>200.35 <b>(-41.21%)</b></td><td>623.88 (-0.10%)</td><td>622.79 (+0.04%)</td><td>622.79 (-0.06%)</td><td>621.27 (+0.25%)</td><td>1.13 <b>(-41.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110890.90 (n/a)</td><td>110384.38 (n/a)</td><td>110272.00 (n/a)</td><td>110040.60 (n/a)</td><td>340.79 (n/a)</td><td>624.49 (n/a)</td><td>622.55 (n/a)</td><td>623.18 (n/a)</td><td>619.70 (n/a)</td><td>1.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>2.80 (-1.03%)</td><td>2.79 (-0.47%)</td><td>2.80 (+0.01%)</td><td>2.79 (-0.33%)</td><td>0.00 <b>(-70.49%)</b></td><td>37633.70 (+0.33%)</td><td>37520.36 (+0.47%)</td><td>37492.90 (-0.01%)</td><td>37485.90 (+1.04%)</td><td>63.58 <b>(-70.08%)</b></td><td>2864.39 (-1.03%)</td><td>2861.76 (-0.47%)</td><td>2863.86 (+0.01%)</td><td>2853.14 (-0.33%)</td><td>4.84 <b>(-70.49%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>2.83 (n/a)</td><td>2.81 (n/a)</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>0.02 (n/a)</td><td>37508.50 (n/a)</td><td>37346.58 (n/a)</td><td>37496.70 (n/a)</td><td>37101.40 (n/a)</td><td>212.50 (n/a)</td><td>2894.07 (n/a)</td><td>2875.15 (n/a)</td><td>2863.57 (n/a)</td><td>2862.66 (n/a)</td><td>16.39 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.64 (+0.69%)</td><td>7.29 (+3.67%)</td><td>7.48 (+7.71%)</td><td>6.72 (+3.60%)</td><td>0.38 <b>(-20.81%)</b></td><td>1325.50 (-3.47%)</td><td>1224.92 (-3.68%)</td><td>1191.80 (-7.16%)</td><td>1166.60 (-0.68%)</td><td>65.30 <b>(-23.56%)</b></td><td>460.19 (+0.69%)</td><td>439.25 (+3.67%)</td><td>450.46 (+7.71%)</td><td>405.02 (+3.60%)</td><td>22.64 <b>(-20.81%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.59 (n/a)</td><td>7.03 (n/a)</td><td>6.94 (n/a)</td><td>6.49 (n/a)</td><td>0.47 (n/a)</td><td>1373.20 (n/a)</td><td>1271.68 (n/a)</td><td>1283.70 (n/a)</td><td>1174.60 (n/a)</td><td>85.43 (n/a)</td><td>457.06 (n/a)</td><td>423.71 (n/a)</td><td>418.22 (n/a)</td><td>390.96 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.15 (+1.56%)</td><td>6.64 (+10.66%)</td><td>6.70 (+7.39%)</td><td>5.86 <b>(+20.45%)</b></td><td>0.47 <b>(-54.30%)</b></td><td>1519.80 (-16.97%)</td><td>1347.76 (-11.49%)</td><td>1330.90 (-6.88%)</td><td>1246.80 (-1.54%)</td><td>102.49 <b>(-62.43%)</b></td><td>430.61 (+1.56%)</td><td>400.08 (+10.66%)</td><td>403.38 (+7.39%)</td><td>353.26 <b>(+20.45%)</b></td><td>28.56 <b>(-54.30%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.04 (n/a)</td><td>6.00 (n/a)</td><td>6.24 (n/a)</td><td>4.87 (n/a)</td><td>1.04 (n/a)</td><td>1830.50 (n/a)</td><td>1522.66 (n/a)</td><td>1429.30 (n/a)</td><td>1266.30 (n/a)</td><td>272.81 (n/a)</td><td>423.98 (n/a)</td><td>361.53 (n/a)</td><td>375.62 (n/a)</td><td>293.30 (n/a)</td><td>62.51 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>6.91 (-2.87%)</td><td>6.12 (-7.77%)</td><td>6.59 (-2.78%)</td><td>4.69 (-18.07%)</td><td>0.91 <b>(+68.51%)</b></td><td>1900.20 <b>(+22.06%)</b></td><td>1485.38 (+10.00%)</td><td>1352.40 (+2.86%)</td><td>1290.30 (+2.95%)</td><td>251.66 <b>(+109.73%)</b></td><td>416.08 (-2.87%)</td><td>368.83 (-7.77%)</td><td>396.96 (-2.78%)</td><td>282.54 (-18.07%)</td><td>54.76 <b>(+68.51%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.11 (n/a)</td><td>6.64 (n/a)</td><td>6.78 (n/a)</td><td>5.73 (n/a)</td><td>0.54 (n/a)</td><td>1556.80 (n/a)</td><td>1350.30 (n/a)</td><td>1314.80 (n/a)</td><td>1253.30 (n/a)</td><td>119.99 (n/a)</td><td>428.36 (n/a)</td><td>399.90 (n/a)</td><td>408.32 (n/a)</td><td>344.87 (n/a)</td><td>32.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.57 (+0.86%)</td><td>8.21 (+1.53%)</td><td>8.07 (+1.08%)</td><td>7.83 (-1.25%)</td><td>0.32 <b>(+37.16%)</b></td><td>4454.40 (+1.26%)</td><td>4252.72 (-1.45%)</td><td>4319.60 (-1.07%)</td><td>4069.70 (-0.85%)</td><td>164.56 <b>(+37.42%)</b></td><td>527.68 (+0.86%)</td><td>505.57 (+1.53%)</td><td>497.15 (+1.08%)</td><td>482.10 (-1.25%)</td><td>19.63 <b>(+37.16%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.49 (n/a)</td><td>8.08 (n/a)</td><td>7.99 (n/a)</td><td>7.93 (n/a)</td><td>0.23 (n/a)</td><td>4398.80 (n/a)</td><td>4315.42 (n/a)</td><td>4366.20 (n/a)</td><td>4104.60 (n/a)</td><td>119.74 (n/a)</td><td>523.19 (n/a)</td><td>497.95 (n/a)</td><td>491.84 (n/a)</td><td>488.20 (n/a)</td><td>14.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.97 (+4.23%)</td><td>7.53 (+3.06%)</td><td>7.58 (+6.27%)</td><td>7.03 (-0.03%)</td><td>0.35 (+19.60%)</td><td>4956.00 (+0.03%)</td><td>4636.78 (-2.92%)</td><td>4599.70 (-5.90%)</td><td>4371.90 (-4.06%)</td><td>219.33 (+15.55%)</td><td>491.20 (+4.23%)</td><td>463.96 (+3.06%)</td><td>466.87 (+6.27%)</td><td>433.31 (-0.03%)</td><td>21.68 (+19.60%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.65 (n/a)</td><td>7.31 (n/a)</td><td>7.13 (n/a)</td><td>7.04 (n/a)</td><td>0.29 (n/a)</td><td>4954.60 (n/a)</td><td>4776.40 (n/a)</td><td>4888.20 (n/a)</td><td>4556.90 (n/a)</td><td>189.82 (n/a)</td><td>471.26 (n/a)</td><td>450.18 (n/a)</td><td>439.32 (n/a)</td><td>433.43 (n/a)</td><td>18.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.88 (+5.10%)</td><td>7.38 (+2.80%)</td><td>7.35 (+1.68%)</td><td>6.86 (+1.43%)</td><td>0.36 (+10.13%)</td><td>5080.10 (-1.41%)</td><td>4734.52 (-2.70%)</td><td>4742.20 (-1.66%)</td><td>4425.00 (-4.85%)</td><td>234.09 (+3.95%)</td><td>485.30 (+5.10%)</td><td>454.46 (+2.80%)</td><td>452.84 (+1.68%)</td><td>422.72 (+1.43%)</td><td>22.31 (+10.13%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>7.50 (n/a)</td><td>7.18 (n/a)</td><td>7.23 (n/a)</td><td>6.77 (n/a)</td><td>0.33 (n/a)</td><td>5152.70 (n/a)</td><td>4865.86 (n/a)</td><td>4822.10 (n/a)</td><td>4650.50 (n/a)</td><td>225.20 (n/a)</td><td>461.77 (n/a)</td><td>442.09 (n/a)</td><td>445.34 (n/a)</td><td>416.77 (n/a)</td><td>20.26 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.80 (-0.41%)</td><td>0.80 (-0.06%)</td><td>0.80 (-0.04%)</td><td>0.80 (+0.16%)</td><td>0.00 <b>(-91.13%)</b></td><td>94079.30 (-0.16%)</td><td>94053.26 (+0.06%)</td><td>94055.50 (+0.04%)</td><td>94034.20 (+0.42%)</td><td>19.26 <b>(-91.11%)</b></td><td>730.79 (-0.41%)</td><td>730.64 (-0.06%)</td><td>730.63 (-0.04%)</td><td>730.44 (+0.16%)</td><td>0.15 <b>(-91.13%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94231.80 (n/a)</td><td>93999.78 (n/a)</td><td>94021.30 (n/a)</td><td>93644.30 (n/a)</td><td>216.62 (n/a)</td><td>733.84 (n/a)</td><td>731.06 (n/a)</td><td>730.89 (n/a)</td><td>729.26 (n/a)</td><td>1.69 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.74 (-0.02%)</td><td>0.74 (-0.00%)</td><td>0.74 (+0.01%)</td><td>0.74 (+0.01%)</td><td>0.00 <b>(-48.41%)</b></td><td>102611.80 (-0.01%)</td><td>102597.08 (+0.00%)</td><td>102589.90 (-0.01%)</td><td>102586.40 (+0.02%)</td><td>13.06 <b>(-48.52%)</b></td><td>669.87 (-0.02%)</td><td>669.80 (-0.00%)</td><td>669.85 (+0.01%)</td><td>669.70 (+0.01%)</td><td>0.09 <b>(-48.40%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102625.40 (n/a)</td><td>102595.94 (n/a)</td><td>102600.60 (n/a)</td><td>102568.10 (n/a)</td><td>25.37 (n/a)</td><td>669.99 (n/a)</td><td>669.81 (n/a)</td><td>669.78 (n/a)</td><td>669.61 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.71 (-0.05%)</td><td>0.71 (-0.05%)</td><td>0.71 (+0.01%)</td><td>0.71 (-0.16%)</td><td>0.00 (+17.61%)</td><td>106114.00 (+0.16%)</td><td>105904.26 (+0.05%)</td><td>105912.40 (-0.01%)</td><td>105672.40 (+0.05%)</td><td>161.52 (+17.86%)</td><td>650.31 (-0.05%)</td><td>648.88 (-0.05%)</td><td>648.83 (+0.01%)</td><td>647.60 (-0.16%)</td><td>0.99 (+17.61%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>105944.90 (n/a)</td><td>105854.18 (n/a)</td><td>105917.90 (n/a)</td><td>105618.90 (n/a)</td><td>137.05 (n/a)</td><td>650.64 (n/a)</td><td>649.19 (n/a)</td><td>648.80 (n/a)</td><td>648.63 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>4.34 (+14.09%)</td><td>3.39 (-5.28%)</td><td>3.16 (-13.61%)</td><td>2.74 (-15.20%)</td><td>0.62 <b>(+165.00%)</b></td><td>2939.00 (+17.93%)</td><td>2436.88 (+7.85%)</td><td>2551.80 (+15.75%)</td><td>1857.60 (-12.35%)</td><td>413.38 <b>(+169.96%)</b></td><td>1138.00 (+14.09%)</td><td>889.30 (-5.28%)</td><td>828.42 (-13.61%)</td><td>719.26 (-15.20%)</td><td>162.39 <b>(+165.00%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.80 (n/a)</td><td>3.58 (n/a)</td><td>3.66 (n/a)</td><td>3.23 (n/a)</td><td>0.23 (n/a)</td><td>2492.20 (n/a)</td><td>2259.54 (n/a)</td><td>2204.60 (n/a)</td><td>2119.30 (n/a)</td><td>153.13 (n/a)</td><td>997.46 (n/a)</td><td>938.87 (n/a)</td><td>958.88 (n/a)</td><td>848.21 (n/a)</td><td>61.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.58 (+13.31%)</td><td>0.42 (+16.92%)</td><td>0.36 (+4.43%)</td><td>0.33 <b>(+22.69%)</b></td><td>0.11 <b>(+20.19%)</b></td><td>3734.00 (-18.49%)</td><td>3074.28 (-14.08%)</td><td>3446.60 (-4.24%)</td><td>2137.20 (-11.74%)</td><td>699.69 (-9.32%)</td><td>31.40 (+13.31%)</td><td>22.89 (+16.92%)</td><td>19.47 (+4.43%)</td><td>17.97 <b>(+22.69%)</b></td><td>5.85 <b>(+20.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.51 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.09 (n/a)</td><td>4581.20 (n/a)</td><td>3578.10 (n/a)</td><td>3599.10 (n/a)</td><td>2421.60 (n/a)</td><td>771.59 (n/a)</td><td>27.71 (n/a)</td><td>19.58 (n/a)</td><td>18.65 (n/a)</td><td>14.65 (n/a)</td><td>4.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>6.03 (+8.48%)</td><td>4.62 (+2.44%)</td><td>4.84 (-0.90%)</td><td>3.65 (+3.44%)</td><td>0.99 (+12.15%)</td><td>1824.60 (-3.33%)</td><td>1492.92 (-2.01%)</td><td>1373.40 (+0.92%)</td><td>1102.30 (-7.82%)</td><td>309.71 (+0.49%)</td><td>1864.42 (+8.48%)</td><td>1426.66 (+2.44%)</td><td>1496.47 (-0.90%)</td><td>1126.37 (+3.44%)</td><td>304.84 (+12.15%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.56 (n/a)</td><td>4.51 (n/a)</td><td>4.89 (n/a)</td><td>3.52 (n/a)</td><td>0.88 (n/a)</td><td>1887.40 (n/a)</td><td>1523.54 (n/a)</td><td>1360.90 (n/a)</td><td>1195.80 (n/a)</td><td>308.21 (n/a)</td><td>1718.64 (n/a)</td><td>1392.73 (n/a)</td><td>1510.14 (n/a)</td><td>1088.93 (n/a)</td><td>271.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.39 (n/a)</td><td>12.18 (n/a)</td><td>12.60 (n/a)</td><td>9.72 (n/a)</td><td>1.45 (n/a)</td><td>13.38 (n/a)</td><td>12.18 (n/a)</td><td>12.59 (n/a)</td><td>9.71 (n/a)</td><td>1.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>24.30 (+0.53%)</td><td>22.20 (-4.78%)</td><td>23.99 (+1.21%)</td><td>15.62 <b>(-29.89%)</b></td><td>3.71 <b>(+348.33%)</b></td><td>24.28 (+0.53%)</td><td>22.19 (-4.78%)</td><td>23.97 (+1.21%)</td><td>15.61 <b>(-29.89%)</b></td><td>3.71 <b>(+348.33%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>24.17 (n/a)</td><td>23.32 (n/a)</td><td>23.70 (n/a)</td><td>22.28 (n/a)</td><td>0.83 (n/a)</td><td>24.15 (n/a)</td><td>23.31 (n/a)</td><td>23.69 (n/a)</td><td>22.27 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>41.17 (+0.55%)</td><td>40.56 (+3.19%)</td><td>40.42 (+3.77%)</td><td>40.01 (+6.39%)</td><td>0.53 <b>(-64.63%)</b></td><td>41.15 (+0.55%)</td><td>40.54 (+3.19%)</td><td>40.39 (+3.77%)</td><td>39.98 (+6.39%)</td><td>0.53 <b>(-64.63%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>40.95 (n/a)</td><td>39.31 (n/a)</td><td>38.95 (n/a)</td><td>37.60 (n/a)</td><td>1.51 (n/a)</td><td>40.92 (n/a)</td><td>39.28 (n/a)</td><td>38.92 (n/a)</td><td>37.58 (n/a)</td><td>1.51 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>45.14 (+1.49%)</td><td>44.06 (+5.82%)</td><td>43.86 (+5.73%)</td><td>43.19 (+8.20%)</td><td>0.84 <b>(-53.71%)</b></td><td>45.11 (+1.49%)</td><td>44.04 (+5.82%)</td><td>43.83 (+5.73%)</td><td>43.17 (+8.20%)</td><td>0.84 <b>(-53.71%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>44.48 (n/a)</td><td>41.64 (n/a)</td><td>41.48 (n/a)</td><td>39.92 (n/a)</td><td>1.81 (n/a)</td><td>44.45 (n/a)</td><td>41.62 (n/a)</td><td>41.46 (n/a)</td><td>39.90 (n/a)</td><td>1.81 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.26 (n/a)</td><td>12.10 (n/a)</td><td>12.21 (n/a)</td><td>10.81 (n/a)</td><td>0.87 (n/a)</td><td>13.25 (n/a)</td><td>12.09 (n/a)</td><td>12.20 (n/a)</td><td>10.80 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>24.68 (-0.58%)</td><td>22.87 (-3.84%)</td><td>24.28 (+0.99%)</td><td>17.13 <b>(-22.25%)</b></td><td>3.23 <b>(+206.96%)</b></td><td>24.66 (-0.58%)</td><td>22.86 (-3.84%)</td><td>24.26 (+0.99%)</td><td>17.12 <b>(-22.25%)</b></td><td>3.23 <b>(+206.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>24.82 (n/a)</td><td>23.78 (n/a)</td><td>24.04 (n/a)</td><td>22.03 (n/a)</td><td>1.05 (n/a)</td><td>24.81 (n/a)</td><td>23.77 (n/a)</td><td>24.03 (n/a)</td><td>22.02 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>44.37 (+5.75%)</td><td>40.17 (+9.19%)</td><td>39.32 (-0.79%)</td><td>35.40 <b>(+49.80%)</b></td><td>3.49 <b>(-53.10%)</b></td><td>44.34 (+5.75%)</td><td>40.14 (+9.19%)</td><td>39.30 (-0.79%)</td><td>35.38 <b>(+49.80%)</b></td><td>3.49 <b>(-53.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>41.96 (n/a)</td><td>36.79 (n/a)</td><td>39.63 (n/a)</td><td>23.63 (n/a)</td><td>7.44 (n/a)</td><td>41.93 (n/a)</td><td>36.76 (n/a)</td><td>39.61 (n/a)</td><td>23.62 (n/a)</td><td>7.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>45.59 (+0.99%)</td><td>44.19 (+10.21%)</td><td>44.35 (+5.07%)</td><td>42.85 <b>(+54.33%)</b></td><td>1.28 <b>(-81.72%)</b></td><td>45.56 (+0.99%)</td><td>44.16 (+10.21%)</td><td>44.32 (+5.07%)</td><td>42.82 <b>(+54.33%)</b></td><td>1.28 <b>(-81.72%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>45.14 (n/a)</td><td>40.10 (n/a)</td><td>42.21 (n/a)</td><td>27.76 (n/a)</td><td>7.00 (n/a)</td><td>45.11 (n/a)</td><td>40.07 (n/a)</td><td>42.18 (n/a)</td><td>27.75 (n/a)</td><td>7.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.76 (-3.35%)</td><td>8.28 (-0.70%)</td><td>8.21 (+1.13%)</td><td>7.76 (-0.41%)</td><td>0.41 <b>(-27.65%)</b></td><td>8.75 (-3.35%)</td><td>8.26 (-0.70%)</td><td>8.19 (+1.13%)</td><td>7.75 (-0.41%)</td><td>0.40 <b>(-27.65%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.07 (n/a)</td><td>8.34 (n/a)</td><td>8.12 (n/a)</td><td>7.79 (n/a)</td><td>0.56 (n/a)</td><td>9.05 (n/a)</td><td>8.32 (n/a)</td><td>8.10 (n/a)</td><td>7.78 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.89 (-16.35%)</td><td>0.84 (-14.08%)</td><td>0.85 (-12.29%)</td><td>0.76 (-13.87%)</td><td>0.06 <b>(-30.36%)</b></td><td>0.87 (-16.35%)</td><td>0.83 (-14.08%)</td><td>0.84 (-12.29%)</td><td>0.74 (-13.87%)</td><td>0.06 <b>(-30.36%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.06 (n/a)</td><td>0.98 (n/a)</td><td>0.97 (n/a)</td><td>0.88 (n/a)</td><td>0.08 (n/a)</td><td>1.05 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.86 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.39 (+5.06%)</td><td>1.16 (-2.97%)</td><td>1.27 (+4.01%)</td><td>0.83 <b>(-20.96%)</b></td><td>0.23 <b>(+78.89%)</b></td><td>1.37 (+5.06%)</td><td>1.14 (-2.97%)</td><td>1.25 (+4.01%)</td><td>0.82 <b>(-20.96%)</b></td><td>0.22 <b>(+78.89%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.32 (n/a)</td><td>1.19 (n/a)</td><td>1.22 (n/a)</td><td>1.06 (n/a)</td><td>0.13 (n/a)</td><td>1.31 (n/a)</td><td>1.18 (n/a)</td><td>1.20 (n/a)</td><td>1.04 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>18.40 (+4.40%)</td><td>16.24 (+0.65%)</td><td>16.26 (+3.03%)</td><td>14.31 (-7.99%)</td><td>1.63 <b>(+92.01%)</b></td><td>18.19 (+4.40%)</td><td>16.06 (+0.65%)</td><td>16.07 (+3.03%)</td><td>14.14 (-7.99%)</td><td>1.61 <b>(+92.01%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>17.62 (n/a)</td><td>16.14 (n/a)</td><td>15.78 (n/a)</td><td>15.55 (n/a)</td><td>0.85 (n/a)</td><td>17.42 (n/a)</td><td>15.95 (n/a)</td><td>15.60 (n/a)</td><td>15.37 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.65 (-2.19%)</td><td>12.96 (-3.87%)</td><td>13.14 (-1.48%)</td><td>11.74 (-9.80%)</td><td>0.73 <b>(+88.19%)</b></td><td>13.41 (-2.19%)</td><td>12.74 (-3.87%)</td><td>12.91 (-1.48%)</td><td>11.53 (-9.80%)</td><td>0.71 <b>(+88.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.96 (n/a)</td><td>13.48 (n/a)</td><td>13.34 (n/a)</td><td>13.01 (n/a)</td><td>0.39 (n/a)</td><td>13.71 (n/a)</td><td>13.25 (n/a)</td><td>13.10 (n/a)</td><td>12.79 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.90 (-14.16%)</td><td>7.46 (-6.87%)</td><td>7.50 (-4.05%)</td><td>6.88 (-5.32%)</td><td>0.42 <b>(-48.44%)</b></td><td>7.77 (-14.16%)</td><td>7.33 (-6.87%)</td><td>7.37 (-4.05%)</td><td>6.76 (-5.32%)</td><td>0.41 <b>(-48.44%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.21 (n/a)</td><td>8.01 (n/a)</td><td>7.82 (n/a)</td><td>7.27 (n/a)</td><td>0.81 (n/a)</td><td>9.05 (n/a)</td><td>7.87 (n/a)</td><td>7.68 (n/a)</td><td>7.14 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.14 (+18.64%)</td><td>5.79 (+7.32%)</td><td>5.41 (-3.29%)</td><td>5.20 <b>(+24.77%)</b></td><td>0.78 (+7.87%)</td><td>7.02 (+18.64%)</td><td>5.70 (+7.32%)</td><td>5.32 (-3.29%)</td><td>5.12 <b>(+24.77%)</b></td><td>0.77 (+7.87%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>6.02 (n/a)</td><td>5.40 (n/a)</td><td>5.59 (n/a)</td><td>4.17 (n/a)</td><td>0.73 (n/a)</td><td>5.92 (n/a)</td><td>5.31 (n/a)</td><td>5.50 (n/a)</td><td>4.10 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.21 (n/a)</td><td>12.11 (n/a)</td><td>12.77 (n/a)</td><td>10.00 (n/a)</td><td>1.30 (n/a)</td><td>13.20 (n/a)</td><td>12.10 (n/a)</td><td>12.76 (n/a)</td><td>9.99 (n/a)</td><td>1.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.54 (n/a)</td><td>13.04 (n/a)</td><td>13.24 (n/a)</td><td>12.41 (n/a)</td><td>0.49 (n/a)</td><td>13.53 (n/a)</td><td>13.03 (n/a)</td><td>13.23 (n/a)</td><td>12.40 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.30 (n/a)</td><td>170.86 (n/a)</td><td>165.70 (n/a)</td><td>156.70 (n/a)</td><td>14.30 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>174.44 (n/a)</td><td>173.80 (n/a)</td><td>153.10 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.00 (n/a)</td><td>159.20 (n/a)</td><td>155.60 (n/a)</td><td>150.60 (n/a)</td><td>9.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.60 (n/a)</td><td>166.78 (n/a)</td><td>173.20 (n/a)</td><td>130.10 (n/a)</td><td>29.82 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.40 (n/a)</td><td>169.12 (n/a)</td><td>174.60 (n/a)</td><td>121.50 (n/a)</td><td>46.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.40 (n/a)</td><td>167.42 (n/a)</td><td>169.30 (n/a)</td><td>129.90 (n/a)</td><td>31.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.00 (n/a)</td><td>179.30 (n/a)</td><td>163.60 (n/a)</td><td>144.90 (n/a)</td><td>33.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.70 (n/a)</td><td>199.86 (n/a)</td><td>196.70 (n/a)</td><td>152.90 (n/a)</td><td>33.81 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>172.50 (n/a)</td><td>161.10 (n/a)</td><td>145.70 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>179.98 (n/a)</td><td>176.50 (n/a)</td><td>126.20 (n/a)</td><td>38.47 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>180.96 (n/a)</td><td>194.40 (n/a)</td><td>126.10 (n/a)</td><td>41.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>207.40 (n/a)</td><td>180.98 (n/a)</td><td>175.50 (n/a)</td><td>168.80 (n/a)</td><td>15.16 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>179.32 (n/a)</td><td>181.30 (n/a)</td><td>144.80 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.50 (n/a)</td><td>182.76 (n/a)</td><td>188.40 (n/a)</td><td>160.10 (n/a)</td><td>19.74 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>183.92 (n/a)</td><td>198.30 (n/a)</td><td>139.10 (n/a)</td><td>27.60 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.90 (n/a)</td><td>212.60 (n/a)</td><td>189.40 (n/a)</td><td>160.40 (n/a)</td><td>47.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.10 (n/a)</td><td>188.66 (n/a)</td><td>184.80 (n/a)</td><td>173.00 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>169.00 (n/a)</td><td>164.90 (n/a)</td><td>137.20 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.10 (n/a)</td><td>189.02 (n/a)</td><td>179.00 (n/a)</td><td>163.00 (n/a)</td><td>32.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>171.84 (n/a)</td><td>179.50 (n/a)</td><td>139.80 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>213.20 (n/a)</td><td>165.16 (n/a)</td><td>165.40 (n/a)</td><td>119.40 (n/a)</td><td>39.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>247.70 (n/a)</td><td>196.28 (n/a)</td><td>181.60 (n/a)</td><td>142.60 (n/a)</td><td>44.06 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>183.22 (n/a)</td><td>177.80 (n/a)</td><td>165.50 (n/a)</td><td>20.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>201.24 (n/a)</td><td>203.50 (n/a)</td><td>174.80 (n/a)</td><td>16.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>190.50 (n/a)</td><td>164.84 (n/a)</td><td>184.50 (n/a)</td><td>104.40 (n/a)</td><td>35.94 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.50 (n/a)</td><td>169.02 (n/a)</td><td>173.40 (n/a)</td><td>135.50 (n/a)</td><td>22.96 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>203.90 (n/a)</td><td>173.96 (n/a)</td><td>169.80 (n/a)</td><td>140.40 (n/a)</td><td>24.42 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>175.70 (n/a)</td><td>160.96 (n/a)</td><td>174.10 (n/a)</td><td>129.80 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.20 (n/a)</td><td>171.14 (n/a)</td><td>172.40 (n/a)</td><td>130.90 (n/a)</td><td>25.20 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>199.10 (n/a)</td><td>180.30 (n/a)</td><td>178.90 (n/a)</td><td>155.10 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>192.60 (n/a)</td><td>169.10 (n/a)</td><td>171.30 (n/a)</td><td>140.10 (n/a)</td><td>20.11 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>193.44 (n/a)</td><td>196.90 (n/a)</td><td>176.80 (n/a)</td><td>14.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+4.64%)</td><td>0.03 (+9.88%)</td><td>0.03 (-2.14%)</td><td>0.02 <b>(+35.97%)</b></td><td>0.00 <b>(-23.04%)</b></td><td>172.60 <b>(-26.46%)</b></td><td>152.40 (-11.20%)</td><td>162.10 (+2.21%)</td><td>119.30 (-4.41%)</td><td>21.45 <b>(-47.22%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>171.62 (n/a)</td><td>158.60 (n/a)</td><td>124.80 (n/a)</td><td>40.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (+5.30%)</td><td>0.03 (-3.30%)</td><td>0.03 (-11.43%)</td><td>0.02 (+11.55%)</td><td>0.01 (-5.59%)</td><td>231.50 (-10.34%)</td><td>162.42 (+1.34%)</td><td>157.80 (+12.88%)</td><td>109.90 (-5.01%)</td><td>46.65 <b>(-20.13%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.20 (n/a)</td><td>160.28 (n/a)</td><td>139.80 (n/a)</td><td>115.70 (n/a)</td><td>58.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+4.86%)</td><td>0.02 (-4.39%)</td><td>0.02 (+0.61%)</td><td>0.02 (-11.37%)</td><td>0.01 <b>(+26.13%)</b></td><td>229.90 (+12.81%)</td><td>174.24 (+6.39%)</td><td>167.70 (-0.59%)</td><td>123.60 (-4.63%)</td><td>39.31 <b>(+36.31%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.80 (n/a)</td><td>163.78 (n/a)</td><td>168.70 (n/a)</td><td>129.60 (n/a)</td><td>28.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-17.93%)</td><td>0.03 (-9.65%)</td><td>0.03 (-11.64%)</td><td>0.02 (+2.19%)</td><td>0.00 <b>(-31.35%)</b></td><td>217.30 (-2.16%)</td><td>164.32 (+8.18%)</td><td>158.30 (+13.15%)</td><td>136.20 <b>(+21.82%)</b></td><td>32.57 <b>(-21.73%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.10 (n/a)</td><td>151.90 (n/a)</td><td>139.90 (n/a)</td><td>111.80 (n/a)</td><td>41.61 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+0.15%)</td><td>0.03 (+7.43%)</td><td>0.02 (-0.21%)</td><td>0.02 <b>(+92.61%)</b></td><td>0.00 <b>(-44.93%)</b></td><td>193.10 <b>(-48.08%)</b></td><td>166.86 (-16.33%)</td><td>168.70 (+0.24%)</td><td>140.30 (-0.14%)</td><td>26.07 <b>(-73.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>371.90 (n/a)</td><td>199.42 (n/a)</td><td>168.30 (n/a)</td><td>140.50 (n/a)</td><td>97.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+0.42%)</td><td>0.02 (+0.27%)</td><td>0.02 (-1.73%)</td><td>0.02 (+12.32%)</td><td>0.00 (-16.94%)</td><td>253.30 (-10.97%)</td><td>195.16 (-1.89%)</td><td>191.00 (+1.76%)</td><td>155.10 (-0.39%)</td><td>36.01 <b>(-27.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>284.50 (n/a)</td><td>198.92 (n/a)</td><td>187.70 (n/a)</td><td>155.70 (n/a)</td><td>49.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-5.27%)</td><td>0.02 (-6.39%)</td><td>0.02 (-14.75%)</td><td>0.02 (+10.13%)</td><td>0.00 <b>(-31.99%)</b></td><td>211.40 (-9.19%)</td><td>190.32 (+5.21%)</td><td>195.50 (+17.35%)</td><td>154.10 (+5.55%)</td><td>21.49 <b>(-37.45%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.80 (n/a)</td><td>180.90 (n/a)</td><td>166.60 (n/a)</td><td>146.00 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-1.36%)</td><td>0.02 (-2.80%)</td><td>0.02 (-6.42%)</td><td>0.01 (+3.47%)</td><td>0.01 (-1.40%)</td><td>291.10 (-3.35%)</td><td>216.60 (+2.54%)</td><td>222.80 (+6.91%)</td><td>142.40 (+1.42%)</td><td>55.14 (-5.63%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>301.20 (n/a)</td><td>211.24 (n/a)</td><td>208.40 (n/a)</td><td>140.40 (n/a)</td><td>58.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (+0.94%)</td><td>0.05 (+4.57%)</td><td>0.05 (+5.31%)</td><td>0.04 (+9.23%)</td><td>0.01 (-14.39%)</td><td>189.10 (-8.47%)</td><td>166.52 (-4.93%)</td><td>156.10 (-5.05%)</td><td>145.50 (-0.89%)</td><td>20.97 <b>(-22.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>175.16 (n/a)</td><td>164.40 (n/a)</td><td>146.80 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (-6.91%)</td><td>0.06 (+4.59%)</td><td>0.06 (+17.12%)</td><td>0.05 (+0.83%)</td><td>0.01 (-18.72%)</td><td>177.20 (-0.84%)</td><td>138.58 (-5.04%)</td><td>128.00 (-14.61%)</td><td>123.60 (+7.48%)</td><td>22.51 (-12.11%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.70 (n/a)</td><td>145.94 (n/a)</td><td>149.90 (n/a)</td><td>115.00 (n/a)</td><td>25.61 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (+19.61%)</td><td>0.06 <b>(+23.36%)</b></td><td>0.06 <b>(+28.04%)</b></td><td>0.05 <b>(+30.09%)</b></td><td>0.01 (+0.25%)</td><td>159.80 <b>(-23.14%)</b></td><td>141.44 (-19.32%)</td><td>140.70 <b>(-21.88%)</b></td><td>123.30 (-16.35%)</td><td>15.26 <b>(-35.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>175.32 (n/a)</td><td>180.10 (n/a)</td><td>147.40 (n/a)</td><td>23.51 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (+9.79%)</td><td>0.05 (-7.76%)</td><td>0.05 (-12.60%)</td><td>0.04 (-9.65%)</td><td>0.01 <b>(+84.92%)</b></td><td>187.20 (+10.70%)</td><td>170.54 (+10.13%)</td><td>181.80 (+14.41%)</td><td>125.70 (-8.91%)</td><td>25.55 <b>(+83.50%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>169.10 (n/a)</td><td>154.86 (n/a)</td><td>158.90 (n/a)</td><td>138.00 (n/a)</td><td>13.93 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (+9.69%)</td><td>0.05 (+3.81%)</td><td>0.05 (+6.98%)</td><td>0.04 (-4.00%)</td><td>0.01 <b>(+49.57%)</b></td><td>191.60 (+4.19%)</td><td>161.70 (-3.08%)</td><td>160.00 (-6.54%)</td><td>137.60 (-8.81%)</td><td>19.30 <b>(+44.46%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>183.90 (n/a)</td><td>166.84 (n/a)</td><td>171.20 (n/a)</td><td>150.90 (n/a)</td><td>13.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (-0.32%)</td><td>0.05 (+0.51%)</td><td>0.05 (-8.16%)</td><td>0.04 <b>(+35.34%)</b></td><td>0.01 <b>(-33.69%)</b></td><td>211.90 <b>(-26.12%)</b></td><td>174.14 (-5.43%)</td><td>176.90 (+8.93%)</td><td>134.30 (+0.30%)</td><td>30.50 <b>(-51.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>286.80 (n/a)</td><td>184.14 (n/a)</td><td>162.40 (n/a)</td><td>133.90 (n/a)</td><td>62.51 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 <b>(+54.47%)</b></td><td>0.06 <b>(+27.14%)</b></td><td>0.06 (+19.37%)</td><td>0.05 (+9.48%)</td><td>0.01 <b>(+288.58%)</b></td><td>177.50 (-8.65%)</td><td>144.96 (-18.92%)</td><td>148.30 (-16.26%)</td><td>105.30 <b>(-35.28%)</b></td><td>28.73 <b>(+128.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>194.30 (n/a)</td><td>178.78 (n/a)</td><td>177.10 (n/a)</td><td>162.70 (n/a)</td><td>12.58 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 <b>(+49.38%)</b></td><td>0.05 (+11.72%)</td><td>0.04 (+0.33%)</td><td>0.03 (+2.47%)</td><td>0.01 <b>(+126.42%)</b></td><td>253.60 (-2.42%)</td><td>185.16 (-6.73%)</td><td>182.30 (-0.33%)</td><td>117.10 <b>(-33.09%)</b></td><td>48.77 <b>(+39.51%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.90 (n/a)</td><td>198.52 (n/a)</td><td>182.90 (n/a)</td><td>175.00 (n/a)</td><td>34.96 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 <b>(+29.37%)</b></td><td>0.05 (+11.87%)</td><td>0.05 (+1.81%)</td><td>0.04 (+17.23%)</td><td>0.01 <b>(+84.64%)</b></td><td>188.00 (-14.70%)</td><td>165.54 (-9.37%)</td><td>177.10 (-1.77%)</td><td>122.50 <b>(-22.71%)</b></td><td>27.34 (+19.11%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.40 (n/a)</td><td>182.66 (n/a)</td><td>180.30 (n/a)</td><td>158.50 (n/a)</td><td>22.96 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 <b>(+24.32%)</b></td><td>0.04 (+0.58%)</td><td>0.04 (-11.14%)</td><td>0.04 (+8.76%)</td><td>0.01 <b>(+56.12%)</b></td><td>231.10 (-8.04%)</td><td>206.70 (+1.16%)</td><td>223.70 (+12.53%)</td><td>136.70 (-19.54%)</td><td>39.45 (+14.00%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.30 (n/a)</td><td>204.32 (n/a)</td><td>198.80 (n/a)</td><td>169.90 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (-9.87%)</td><td>0.10 (-7.87%)</td><td>0.10 (-9.51%)</td><td>0.09 (+18.24%)</td><td>0.01 <b>(-47.24%)</b></td><td>191.30 (-15.39%)</td><td>168.74 (+5.20%)</td><td>164.70 (+10.54%)</td><td>141.40 (+10.90%)</td><td>19.98 <b>(-50.15%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.10 (n/a)</td><td>160.40 (n/a)</td><td>149.00 (n/a)</td><td>127.50 (n/a)</td><td>40.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (+12.58%)</td><td>0.10 (+10.71%)</td><td>0.10 (+10.15%)</td><td>0.10 (+8.67%)</td><td>0.01 <b>(+31.95%)</b></td><td>167.20 (-7.98%)</td><td>158.28 (-9.64%)</td><td>160.50 (-9.22%)</td><td>146.40 (-11.22%)</td><td>7.75 (+7.13%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>181.70 (n/a)</td><td>175.16 (n/a)</td><td>176.80 (n/a)</td><td>164.90 (n/a)</td><td>7.23 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (-2.65%)</td><td>0.10 (-7.74%)</td><td>0.09 (-9.14%)</td><td>0.08 (-11.55%)</td><td>0.02 (+15.81%)</td><td>209.10 (+13.03%)</td><td>176.92 (+9.63%)</td><td>176.00 (+10.07%)</td><td>126.60 (+2.68%)</td><td>33.07 <b>(+35.00%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.00 (n/a)</td><td>161.38 (n/a)</td><td>159.90 (n/a)</td><td>123.30 (n/a)</td><td>24.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 <b>(-28.13%)</b></td><td>0.09 (-6.64%)</td><td>0.09 (+2.19%)</td><td>0.08 (+7.31%)</td><td>0.01 <b>(-70.82%)</b></td><td>195.80 (-6.85%)</td><td>175.56 (+2.33%)</td><td>176.10 (-2.11%)</td><td>155.20 <b>(+39.19%)</b></td><td>15.06 <b>(-61.89%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>210.20 (n/a)</td><td>171.56 (n/a)</td><td>179.90 (n/a)</td><td>111.50 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (+5.78%)</td><td>0.10 (+6.23%)</td><td>0.10 (+7.06%)</td><td>0.08 (+12.36%)</td><td>0.01 (-18.16%)</td><td>192.90 (-10.98%)</td><td>170.68 (-6.78%)</td><td>163.30 (-6.58%)</td><td>142.40 (-5.44%)</td><td>21.59 <b>(-31.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.70 (n/a)</td><td>183.10 (n/a)</td><td>174.80 (n/a)</td><td>150.60 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 <b>(-33.38%)</b></td><td>0.08 (-18.35%)</td><td>0.08 <b>(-23.15%)</b></td><td>0.07 (+6.63%)</td><td>0.01 <b>(-65.71%)</b></td><td>229.60 (-6.21%)</td><td>203.40 (+16.37%)</td><td>206.10 <b>(+30.11%)</b></td><td>174.20 <b>(+50.04%)</b></td><td>23.33 <b>(-51.91%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>244.80 (n/a)</td><td>174.78 (n/a)</td><td>158.40 (n/a)</td><td>116.10 (n/a)</td><td>48.51 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 <b>(-26.81%)</b></td><td>0.09 (-13.37%)</td><td>0.09 (-4.64%)</td><td>0.08 (+8.90%)</td><td>0.01 <b>(-77.25%)</b></td><td>199.20 (-8.16%)</td><td>185.86 (+10.45%)</td><td>184.80 (+4.88%)</td><td>169.50 <b>(+36.69%)</b></td><td>11.82 <b>(-70.52%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>216.90 (n/a)</td><td>168.28 (n/a)</td><td>176.20 (n/a)</td><td>124.00 (n/a)</td><td>40.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (+2.21%)</td><td>0.07 (-1.89%)</td><td>0.07 (+2.19%)</td><td>0.05 <b>(-29.37%)</b></td><td>0.02 <b>(+97.84%)</b></td><td>331.90 <b>(+41.60%)</b></td><td>232.10 (+5.83%)</td><td>225.60 (-2.13%)</td><td>179.30 (-2.13%)</td><td>60.24 <b>(+178.63%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.40 (n/a)</td><td>219.32 (n/a)</td><td>230.50 (n/a)</td><td>183.20 (n/a)</td><td>21.62 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 <b>(-23.43%)</b></td><td>0.17 (-12.28%)</td><td>0.17 (-5.12%)</td><td>0.12 <b>(-23.59%)</b></td><td>0.03 <b>(-25.30%)</b></td><td>265.50 <b>(+30.85%)</b></td><td>198.74 (+13.90%)</td><td>188.30 (+5.37%)</td><td>174.30 <b>(+30.66%)</b></td><td>37.95 <b>(+28.31%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>202.90 (n/a)</td><td>174.48 (n/a)</td><td>178.70 (n/a)</td><td>133.40 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (-14.17%)</td><td>0.18 (+7.98%)</td><td>0.19 (+19.99%)</td><td>0.15 <b>(+34.98%)</b></td><td>0.02 <b>(-55.75%)</b></td><td>214.80 <b>(-25.93%)</b></td><td>180.24 (-12.27%)</td><td>176.80 (-16.68%)</td><td>153.40 (+16.48%)</td><td>22.63 <b>(-60.86%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>290.00 (n/a)</td><td>205.46 (n/a)</td><td>212.20 (n/a)</td><td>131.70 (n/a)</td><td>57.82 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (+7.53%)</td><td>0.19 (+5.93%)</td><td>0.18 (+4.65%)</td><td>0.15 (+8.59%)</td><td>0.03 (-4.90%)</td><td>213.40 (-7.94%)</td><td>178.00 (-6.06%)</td><td>178.30 (-4.45%)</td><td>144.70 (-7.01%)</td><td>25.12 (-18.63%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.80 (n/a)</td><td>189.48 (n/a)</td><td>186.60 (n/a)</td><td>155.60 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.22 (+6.02%)</td><td>0.20 (+3.59%)</td><td>0.20 (+1.94%)</td><td>0.18 (+6.42%)</td><td>0.02 (+8.57%)</td><td>186.90 (-6.03%)</td><td>166.36 (-3.45%)</td><td>166.00 (-1.89%)</td><td>147.40 (-5.63%)</td><td>14.97 (-5.81%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>198.90 (n/a)</td><td>172.30 (n/a)</td><td>169.20 (n/a)</td><td>156.20 (n/a)</td><td>15.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.30 <b>(+32.45%)</b></td><td>0.20 (+14.70%)</td><td>0.21 (+0.26%)</td><td>0.14 (+19.67%)</td><td>0.06 <b>(+32.96%)</b></td><td>238.00 (-16.43%)</td><td>173.40 (-11.99%)</td><td>157.90 (-0.25%)</td><td>110.90 <b>(-24.51%)</b></td><td>53.18 (-12.66%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>284.80 (n/a)</td><td>197.02 (n/a)</td><td>158.30 (n/a)</td><td>146.90 (n/a)</td><td>60.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (-7.29%)</td><td>0.18 (-5.16%)</td><td>0.18 (-13.38%)</td><td>0.14 (+15.67%)</td><td>0.04 <b>(-30.57%)</b></td><td>229.90 (-13.54%)</td><td>188.02 (+1.73%)</td><td>181.90 (+15.49%)</td><td>140.40 (+7.92%)</td><td>35.32 <b>(-36.07%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>265.90 (n/a)</td><td>184.82 (n/a)</td><td>157.50 (n/a)</td><td>130.10 (n/a)</td><td>55.25 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (-7.33%)</td><td>0.15 (+2.79%)</td><td>0.15 (-8.48%)</td><td>0.12 <b>(+20.51%)</b></td><td>0.02 <b>(-47.57%)</b></td><td>278.50 (-17.04%)</td><td>222.26 (-8.27%)</td><td>218.90 (+9.23%)</td><td>182.00 (+7.88%)</td><td>35.54 <b>(-54.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>335.70 (n/a)</td><td>242.30 (n/a)</td><td>200.40 (n/a)</td><td>168.70 (n/a)</td><td>77.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (+7.29%)</td><td>0.02 (-12.05%)</td><td>0.03 (+12.53%)</td><td>0.01 <b>(-47.09%)</b></td><td>0.01 <b>(+68.97%)</b></td><td>373.30 <b>(+89.01%)</b></td><td>211.94 <b>(+31.04%)</b></td><td>153.20 (-11.09%)</td><td>114.70 (-6.82%)</td><td>106.59 <b>(+212.11%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>197.50 (n/a)</td><td>161.74 (n/a)</td><td>172.30 (n/a)</td><td>123.10 (n/a)</td><td>34.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 <b>(+34.81%)</b></td><td>0.03 <b>(+22.76%)</b></td><td>0.03 <b>(+20.29%)</b></td><td>0.02 (+19.49%)</td><td>0.01 <b>(+88.03%)</b></td><td>176.80 (-16.29%)</td><td>144.76 (-17.29%)</td><td>143.80 (-16.88%)</td><td>109.90 <b>(-25.84%)</b></td><td>26.64 (+15.55%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.20 (n/a)</td><td>175.02 (n/a)</td><td>173.00 (n/a)</td><td>148.20 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (-5.17%)</td><td>0.02 (-17.23%)</td><td>0.02 (-14.32%)</td><td>0.01 <b>(-32.49%)</b></td><td>0.00 <b>(+45.83%)</b></td><td>333.70 <b>(+48.11%)</b></td><td>236.66 <b>(+24.62%)</b></td><td>225.40 (+16.73%)</td><td>174.70 (+5.43%)</td><td>59.04 <b>(+139.98%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.30 (n/a)</td><td>189.90 (n/a)</td><td>193.10 (n/a)</td><td>165.70 (n/a)</td><td>24.60 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (-4.70%)</td><td>0.02 (+7.08%)</td><td>0.02 (+10.25%)</td><td>0.02 (+11.20%)</td><td>0.00 <b>(-51.53%)</b></td><td>210.90 (-10.06%)</td><td>193.64 (-7.27%)</td><td>191.30 (-9.29%)</td><td>183.80 (+4.97%)</td><td>10.22 <b>(-52.83%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.50 (n/a)</td><td>208.82 (n/a)</td><td>210.90 (n/a)</td><td>175.10 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 <b>(-21.45%)</b></td><td>0.02 (-4.37%)</td><td>0.03 (+7.81%)</td><td>0.02 (-13.02%)</td><td>0.00 <b>(-32.07%)</b></td><td>230.70 (+15.00%)</td><td>175.44 (+3.35%)</td><td>158.10 (-7.27%)</td><td>150.40 <b>(+27.24%)</b></td><td>33.51 (-0.50%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>169.76 (n/a)</td><td>170.50 (n/a)</td><td>118.20 (n/a)</td><td>33.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+4.49%)</td><td>0.03 (+2.37%)</td><td>0.03 (+4.10%)</td><td>0.02 <b>(-23.17%)</b></td><td>0.01 <b>(+101.83%)</b></td><td>214.20 <b>(+30.13%)</b></td><td>151.66 (+1.44%)</td><td>143.60 (-3.95%)</td><td>119.10 (-4.26%)</td><td>39.32 <b>(+147.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.60 (n/a)</td><td>149.50 (n/a)</td><td>149.50 (n/a)</td><td>124.40 (n/a)</td><td>15.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-4.35%)</td><td>0.02 (-14.17%)</td><td>0.02 <b>(-20.81%)</b></td><td>0.02 (-7.15%)</td><td>0.00 (-8.17%)</td><td>201.00 (+7.72%)</td><td>168.44 (+16.34%)</td><td>175.20 <b>(+26.32%)</b></td><td>124.90 (+4.61%)</td><td>28.90 (+2.93%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>186.60 (n/a)</td><td>144.78 (n/a)</td><td>138.70 (n/a)</td><td>119.40 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 <b>(+32.56%)</b></td><td>0.03 <b>(+20.71%)</b></td><td>0.03 <b>(+30.68%)</b></td><td>0.02 <b>(+31.57%)</b></td><td>0.01 <b>(+32.14%)</b></td><td>175.70 <b>(-23.97%)</b></td><td>144.56 (-17.02%)</td><td>135.40 <b>(-23.46%)</b></td><td>106.70 <b>(-24.54%)</b></td><td>28.65 <b>(-20.99%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.10 (n/a)</td><td>174.22 (n/a)</td><td>176.90 (n/a)</td><td>141.40 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+1.77%)</td><td>0.03 (+8.40%)</td><td>0.02 (-1.02%)</td><td>0.02 <b>(+20.84%)</b></td><td>0.01 (-10.78%)</td><td>198.20 (-17.24%)</td><td>161.06 (-9.76%)</td><td>169.50 (+1.01%)</td><td>120.30 (-1.72%)</td><td>34.77 <b>(-29.40%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>178.48 (n/a)</td><td>167.80 (n/a)</td><td>122.40 (n/a)</td><td>49.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-4.54%)</td><td>0.02 (+0.92%)</td><td>0.02 (-0.23%)</td><td>0.02 (+4.46%)</td><td>0.00 <b>(-27.77%)</b></td><td>185.60 (-4.28%)</td><td>165.40 (-1.69%)</td><td>168.50 (+0.24%)</td><td>139.80 (+4.72%)</td><td>16.68 <b>(-27.99%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.90 (n/a)</td><td>168.24 (n/a)</td><td>168.10 (n/a)</td><td>133.50 (n/a)</td><td>23.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+0.47%)</td><td>0.02 (+15.77%)</td><td>0.02 <b>(+22.28%)</b></td><td>0.02 (+11.24%)</td><td>0.00 (-19.93%)</td><td>209.00 (-10.07%)</td><td>168.82 (-14.93%)</td><td>171.60 (-18.21%)</td><td>132.60 (-0.45%)</td><td>28.53 <b>(-25.29%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.40 (n/a)</td><td>198.46 (n/a)</td><td>209.80 (n/a)</td><td>133.20 (n/a)</td><td>38.20 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 <b>(+25.47%)</b></td><td>0.03 <b>(+26.48%)</b></td><td>0.03 <b>(+28.09%)</b></td><td>0.02 (+13.03%)</td><td>0.00 <b>(+65.26%)</b></td><td>178.60 (-11.54%)</td><td>145.82 <b>(-20.21%)</b></td><td>143.70 <b>(-21.90%)</b></td><td>122.40 <b>(-20.26%)</b></td><td>23.07 (+14.14%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.90 (n/a)</td><td>182.76 (n/a)</td><td>184.00 (n/a)</td><td>153.50 (n/a)</td><td>20.21 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+14.41%)</td><td>0.03 <b>(+33.54%)</b></td><td>0.03 <b>(+28.13%)</b></td><td>0.02 <b>(+58.83%)</b></td><td>0.00 <b>(-36.37%)</b></td><td>194.40 <b>(-37.03%)</b></td><td>161.34 <b>(-27.47%)</b></td><td>155.70 <b>(-21.92%)</b></td><td>147.70 (-12.60%)</td><td>18.80 <b>(-65.08%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>308.70 (n/a)</td><td>222.46 (n/a)</td><td>199.40 (n/a)</td><td>169.00 (n/a)</td><td>53.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 <b>(+26.26%)</b></td><td>0.03 <b>(+29.42%)</b></td><td>0.03 <b>(+24.56%)</b></td><td>0.02 <b>(+43.36%)</b></td><td>0.00 (-15.05%)</td><td>165.40 <b>(-30.24%)</b></td><td>152.80 <b>(-23.55%)</b></td><td>155.90 (-19.72%)</td><td>130.00 <b>(-20.83%)</b></td><td>13.36 <b>(-54.44%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.10 (n/a)</td><td>199.88 (n/a)</td><td>194.20 (n/a)</td><td>164.20 (n/a)</td><td>29.33 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-5.42%)</td><td>0.02 (+3.12%)</td><td>0.03 (+19.74%)</td><td>0.02 (-1.68%)</td><td>0.01 (+8.35%)</td><td>222.60 (+1.69%)</td><td>173.06 (-2.13%)</td><td>156.40 (-16.50%)</td><td>136.90 (+5.71%)</td><td>39.99 (+18.90%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.90 (n/a)</td><td>176.82 (n/a)</td><td>187.30 (n/a)</td><td>129.50 (n/a)</td><td>33.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-0.50%)</td><td>0.02 (-3.51%)</td><td>0.02 (+0.16%)</td><td>0.02 (-5.48%)</td><td>0.00 (+8.55%)</td><td>205.90 (+5.81%)</td><td>180.78 (+4.04%)</td><td>182.70 (-0.16%)</td><td>139.30 (+0.51%)</td><td>26.83 (+15.00%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.60 (n/a)</td><td>173.76 (n/a)</td><td>183.00 (n/a)</td><td>138.60 (n/a)</td><td>23.33 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 <b>(-24.19%)</b></td><td>0.05 (-6.07%)</td><td>0.05 (-1.80%)</td><td>0.05 (+12.75%)</td><td>0.00 <b>(-72.39%)</b></td><td>177.60 (-11.29%)</td><td>165.88 (+2.69%)</td><td>169.60 (+1.80%)</td><td>148.90 <b>(+31.89%)</b></td><td>11.00 <b>(-67.50%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>161.54 (n/a)</td><td>166.60 (n/a)</td><td>112.90 (n/a)</td><td>33.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (+4.36%)</td><td>0.05 (-2.74%)</td><td>0.05 (-18.06%)</td><td>0.04 (-2.95%)</td><td>0.01 (+18.94%)</td><td>212.50 (+3.01%)</td><td>167.04 (+4.04%)</td><td>175.70 <b>(+22.01%)</b></td><td>120.30 (-4.22%)</td><td>39.13 (+14.08%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.30 (n/a)</td><td>160.56 (n/a)</td><td>144.00 (n/a)</td><td>125.60 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (-7.83%)</td><td>0.03 (-4.76%)</td><td>0.04 (-8.30%)</td><td>0.03 (+12.84%)</td><td>0.00 <b>(-37.48%)</b></td><td>301.70 (-11.37%)</td><td>239.34 (+2.23%)</td><td>231.40 (+9.05%)</td><td>207.10 (+8.49%)</td><td>36.58 <b>(-40.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>340.40 (n/a)</td><td>234.12 (n/a)</td><td>212.20 (n/a)</td><td>190.90 (n/a)</td><td>61.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (+13.63%)</td><td>0.04 (+12.19%)</td><td>0.04 (+18.87%)</td><td>0.03 (-1.33%)</td><td>0.01 <b>(+68.61%)</b></td><td>234.20 (+1.34%)</td><td>195.42 (-10.14%)</td><td>191.50 (-15.90%)</td><td>167.50 (-11.98%)</td><td>25.96 <b>(+50.67%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.10 (n/a)</td><td>217.48 (n/a)</td><td>227.70 (n/a)</td><td>190.30 (n/a)</td><td>17.23 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (-9.44%)</td><td>0.05 (-6.66%)</td><td>0.05 (+3.11%)</td><td>0.04 (+3.30%)</td><td>0.01 <b>(-31.73%)</b></td><td>206.70 (-3.19%)</td><td>170.06 (+4.85%)</td><td>165.80 (-3.04%)</td><td>134.40 (+10.44%)</td><td>29.49 <b>(-23.38%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>162.20 (n/a)</td><td>171.00 (n/a)</td><td>121.70 (n/a)</td><td>38.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (+0.17%)</td><td>0.05 (-7.40%)</td><td>0.05 (-17.86%)</td><td>0.04 (-17.30%)</td><td>0.01 <b>(+24.46%)</b></td><td>221.80 <b>(+20.94%)</b></td><td>167.12 (+10.30%)</td><td>167.50 <b>(+21.73%)</b></td><td>121.60 (-0.25%)</td><td>41.65 <b>(+42.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>151.52 (n/a)</td><td>137.60 (n/a)</td><td>121.90 (n/a)</td><td>29.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (+10.32%)</td><td>0.05 (+8.81%)</td><td>0.05 (+7.23%)</td><td>0.04 (-1.76%)</td><td>0.01 <b>(+49.31%)</b></td><td>201.50 (+1.82%)</td><td>163.22 (-6.83%)</td><td>168.10 (-6.77%)</td><td>129.80 (-9.36%)</td><td>29.85 <b>(+35.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>175.18 (n/a)</td><td>180.30 (n/a)</td><td>143.20 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 <b>(+46.57%)</b></td><td>0.06 (+11.52%)</td><td>0.05 (+1.97%)</td><td>0.04 (-0.43%)</td><td>0.02 <b>(+107.96%)</b></td><td>209.90 (+0.43%)</td><td>162.20 (-4.75%)</td><td>166.20 (-1.89%)</td><td>85.30 <b>(-31.76%)</b></td><td>46.98 <b>(+30.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>170.28 (n/a)</td><td>169.40 (n/a)</td><td>125.00 (n/a)</td><td>35.99 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 <b>(+42.00%)</b></td><td>0.05 (+14.43%)</td><td>0.05 (+8.27%)</td><td>0.04 (+14.06%)</td><td>0.01 <b>(+100.18%)</b></td><td>202.60 (-12.33%)</td><td>174.72 (-10.68%)</td><td>181.00 (-7.61%)</td><td>117.60 <b>(-29.62%)</b></td><td>33.22 <b>(+20.68%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>195.62 (n/a)</td><td>195.90 (n/a)</td><td>167.10 (n/a)</td><td>27.53 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (+3.21%)</td><td>0.05 (+5.30%)</td><td>0.06 <b>(+22.57%)</b></td><td>0.04 (-8.56%)</td><td>0.01 <b>(+25.42%)</b></td><td>208.10 (+9.35%)</td><td>164.40 (-4.23%)</td><td>147.80 (-18.39%)</td><td>142.70 (-3.06%)</td><td>28.01 <b>(+32.13%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>171.66 (n/a)</td><td>181.10 (n/a)</td><td>147.20 (n/a)</td><td>21.20 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (-4.10%)</td><td>0.05 (+5.84%)</td><td>0.05 (+2.39%)</td><td>0.05 (+18.22%)</td><td>0.00 <b>(-44.72%)</b></td><td>178.20 (-15.38%)</td><td>167.18 (-6.72%)</td><td>171.70 (-2.33%)</td><td>148.50 (+4.28%)</td><td>12.81 <b>(-50.63%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>179.22 (n/a)</td><td>175.80 (n/a)</td><td>142.40 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 <b>(+60.74%)</b></td><td>0.06 <b>(+36.90%)</b></td><td>0.06 <b>(+41.16%)</b></td><td>0.04 (-9.30%)</td><td>0.02 <b>(+203.76%)</b></td><td>233.30 (+10.26%)</td><td>145.26 <b>(-20.60%)</b></td><td>131.00 <b>(-29.15%)</b></td><td>90.80 <b>(-37.81%)</b></td><td>54.75 <b>(+115.35%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>182.94 (n/a)</td><td>184.90 (n/a)</td><td>146.00 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (-18.34%)</td><td>0.04 (-13.43%)</td><td>0.04 (-10.97%)</td><td>0.03 (-10.41%)</td><td>0.00 <b>(-37.36%)</b></td><td>235.70 (+11.60%)</td><td>203.62 (+14.65%)</td><td>204.70 (+12.35%)</td><td>178.60 <b>(+22.50%)</b></td><td>21.86 (-13.81%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>177.60 (n/a)</td><td>182.20 (n/a)</td><td>145.80 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (-6.39%)</td><td>0.05 (+7.23%)</td><td>0.05 (+14.33%)</td><td>0.04 <b>(+21.09%)</b></td><td>0.01 <b>(-43.23%)</b></td><td>182.30 (-17.44%)</td><td>156.98 (-8.88%)</td><td>151.50 (-12.53%)</td><td>138.30 (+6.80%)</td><td>17.59 <b>(-49.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.80 (n/a)</td><td>172.28 (n/a)</td><td>173.20 (n/a)</td><td>129.50 (n/a)</td><td>34.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (-3.86%)</td><td>0.05 (+0.77%)</td><td>0.05 (+11.78%)</td><td>0.04 (+2.20%)</td><td>0.01 <b>(-24.95%)</b></td><td>202.60 (-2.13%)</td><td>175.56 (-1.58%)</td><td>171.70 (-10.53%)</td><td>148.00 (+4.01%)</td><td>20.72 <b>(-23.00%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>178.38 (n/a)</td><td>191.90 (n/a)</td><td>142.30 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 <b>(+38.46%)</b></td><td>0.05 (+10.25%)</td><td>0.05 (+4.47%)</td><td>0.04 (-8.50%)</td><td>0.01 <b>(+185.39%)</b></td><td>223.20 (+9.25%)</td><td>174.22 (-6.41%)</td><td>174.30 (-4.28%)</td><td>122.40 <b>(-27.79%)</b></td><td>36.12 <b>(+117.45%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.30 (n/a)</td><td>186.16 (n/a)</td><td>182.10 (n/a)</td><td>169.50 (n/a)</td><td>16.61 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (-7.61%)</td><td>0.10 (+13.45%)</td><td>0.10 (+18.54%)</td><td>0.09 <b>(+25.21%)</b></td><td>0.01 <b>(-50.39%)</b></td><td>191.30 <b>(-20.16%)</b></td><td>165.50 (-14.01%)</td><td>160.60 (-15.61%)</td><td>149.40 (+8.26%)</td><td>16.29 <b>(-55.40%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.60 (n/a)</td><td>192.46 (n/a)</td><td>190.30 (n/a)</td><td>138.00 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (+13.66%)</td><td>0.10 (+9.26%)</td><td>0.09 (+3.92%)</td><td>0.09 (+14.48%)</td><td>0.01 (-0.69%)</td><td>187.30 (-12.64%)</td><td>172.50 (-8.74%)</td><td>175.80 (-3.78%)</td><td>144.40 (-12.00%)</td><td>16.91 <b>(-25.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>189.02 (n/a)</td><td>182.70 (n/a)</td><td>164.10 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (-8.95%)</td><td>0.08 (+3.10%)</td><td>0.08 (+7.98%)</td><td>0.07 (+13.96%)</td><td>0.01 <b>(-48.44%)</b></td><td>246.60 (-12.27%)</td><td>217.90 (-4.56%)</td><td>214.30 (-7.43%)</td><td>195.10 (+9.79%)</td><td>18.76 <b>(-49.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>281.10 (n/a)</td><td>228.32 (n/a)</td><td>231.50 (n/a)</td><td>177.70 (n/a)</td><td>37.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (+19.93%)</td><td>0.09 (+17.62%)</td><td>0.09 (+15.18%)</td><td>0.06 <b>(+20.05%)</b></td><td>0.02 <b>(+22.27%)</b></td><td>259.90 (-16.70%)</td><td>189.12 (-14.94%)</td><td>177.30 (-13.17%)</td><td>152.10 (-16.66%)</td><td>43.58 (-16.83%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>312.00 (n/a)</td><td>222.34 (n/a)</td><td>204.20 (n/a)</td><td>182.50 (n/a)</td><td>52.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 <b>(+35.03%)</b></td><td>0.10 (+19.37%)</td><td>0.09 (+9.33%)</td><td>0.08 <b>(+20.80%)</b></td><td>0.02 <b>(+81.81%)</b></td><td>193.50 (-17.24%)</td><td>168.98 (-14.99%)</td><td>185.00 (-8.55%)</td><td>126.40 <b>(-25.95%)</b></td><td>30.03 (+15.31%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.80 (n/a)</td><td>198.78 (n/a)</td><td>202.30 (n/a)</td><td>170.70 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 <b>(+56.06%)</b></td><td>0.10 <b>(+28.48%)</b></td><td>0.10 (+15.95%)</td><td>0.09 <b>(+36.19%)</b></td><td>0.02 <b>(+111.09%)</b></td><td>187.80 <b>(-26.55%)</b></td><td>161.78 <b>(-21.12%)</b></td><td>169.00 (-13.78%)</td><td>116.60 <b>(-35.93%)</b></td><td>27.28 (-6.47%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>255.70 (n/a)</td><td>205.10 (n/a)</td><td>196.00 (n/a)</td><td>182.00 (n/a)</td><td>29.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 <b>(-26.89%)</b></td><td>0.08 (-3.30%)</td><td>0.08 (+9.58%)</td><td>0.06 (+9.59%)</td><td>0.02 <b>(-52.08%)</b></td><td>272.30 (-8.75%)</td><td>201.24 (-2.95%)</td><td>196.20 (-8.74%)</td><td>157.60 <b>(+36.81%)</b></td><td>42.77 <b>(-34.86%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>298.40 (n/a)</td><td>207.36 (n/a)</td><td>215.00 (n/a)</td><td>115.20 (n/a)</td><td>65.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (-7.72%)</td><td>0.10 (-5.68%)</td><td>0.09 (-14.36%)</td><td>0.08 <b>(+29.71%)</b></td><td>0.02 <b>(-33.47%)</b></td><td>199.30 <b>(-22.93%)</b></td><td>171.60 (+1.50%)</td><td>178.60 (+16.73%)</td><td>127.10 (+8.35%)</td><td>27.92 <b>(-48.00%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>258.60 (n/a)</td><td>169.06 (n/a)</td><td>153.00 (n/a)</td><td>117.30 (n/a)</td><td>53.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (-14.63%)</td><td>0.10 (-2.95%)</td><td>0.10 (+8.92%)</td><td>0.09 (+2.57%)</td><td>0.01 <b>(-47.17%)</b></td><td>186.80 (-2.51%)</td><td>162.96 (+0.83%)</td><td>160.60 (-8.18%)</td><td>143.20 (+17.09%)</td><td>18.50 <b>(-39.86%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>191.60 (n/a)</td><td>161.62 (n/a)</td><td>174.90 (n/a)</td><td>122.30 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (+1.51%)</td><td>0.09 (+2.94%)</td><td>0.09 (+5.34%)</td><td>0.08 (+6.85%)</td><td>0.01 (-11.63%)</td><td>201.80 (-6.40%)</td><td>181.18 (-3.13%)</td><td>178.00 (-5.07%)</td><td>159.00 (-1.49%)</td><td>18.30 (-17.14%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>187.04 (n/a)</td><td>187.50 (n/a)</td><td>161.40 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (+9.47%)</td><td>0.10 (+7.80%)</td><td>0.10 (+11.56%)</td><td>0.08 (+2.18%)</td><td>0.01 <b>(+65.55%)</b></td><td>200.30 (-2.15%)</td><td>170.10 (-6.72%)</td><td>157.80 (-10.34%)</td><td>156.70 (-8.68%)</td><td>19.35 <b>(+44.80%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>182.36 (n/a)</td><td>176.00 (n/a)</td><td>171.60 (n/a)</td><td>13.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (+12.70%)</td><td>0.10 (+5.36%)</td><td>0.10 (+3.25%)</td><td>0.09 (+2.53%)</td><td>0.01 <b>(+49.27%)</b></td><td>186.00 (-2.46%)</td><td>163.18 (-4.71%)</td><td>160.10 (-3.15%)</td><td>141.70 (-11.27%)</td><td>16.61 <b>(+29.33%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>171.24 (n/a)</td><td>165.30 (n/a)</td><td>159.70 (n/a)</td><td>12.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (-2.80%)</td><td>0.09 (-4.29%)</td><td>0.08 (-2.97%)</td><td>0.08 (+10.67%)</td><td>0.01 (-17.10%)</td><td>217.10 (-9.65%)</td><td>194.36 (+3.27%)</td><td>199.60 (+3.05%)</td><td>145.90 (+2.89%)</td><td>28.08 <b>(-24.62%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.30 (n/a)</td><td>188.20 (n/a)</td><td>193.70 (n/a)</td><td>141.80 (n/a)</td><td>37.26 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (+10.01%)</td><td>0.08 (-5.65%)</td><td>0.09 (-4.96%)</td><td>0.06 (-6.91%)</td><td>0.02 <b>(+57.39%)</b></td><td>252.10 (+7.41%)</td><td>204.02 (+8.05%)</td><td>191.80 (+5.21%)</td><td>149.30 (-9.13%)</td><td>40.75 <b>(+50.83%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>188.82 (n/a)</td><td>182.30 (n/a)</td><td>164.30 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 <b>(-33.54%)</b></td><td>0.08 (-5.55%)</td><td>0.08 (+8.84%)</td><td>0.07 (+0.16%)</td><td>0.01 <b>(-75.36%)</b></td><td>228.00 (-0.18%)</td><td>199.20 (+0.76%)</td><td>194.30 (-8.13%)</td><td>183.80 <b>(+50.41%)</b></td><td>16.94 <b>(-61.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>228.40 (n/a)</td><td>197.70 (n/a)</td><td>211.50 (n/a)</td><td>122.20 (n/a)</td><td>43.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (-4.66%)</td><td>0.08 (-9.82%)</td><td>0.08 (-11.65%)</td><td>0.07 (-11.15%)</td><td>0.01 (+2.80%)</td><td>231.00 (+12.57%)</td><td>196.82 (+11.25%)</td><td>196.60 (+13.18%)</td><td>157.00 (+4.88%)</td><td>28.39 <b>(+20.03%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>176.92 (n/a)</td><td>173.70 (n/a)</td><td>149.70 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 <b>(+21.73%)</b></td><td>0.24 <b>(+45.88%)</b></td><td>0.26 <b>(+43.50%)</b></td><td>0.16 <b>(+85.22%)</b></td><td>0.05 (-7.17%)</td><td>206.90 <b>(-46.02%)</b></td><td>140.56 <b>(-35.88%)</b></td><td>125.20 <b>(-30.29%)</b></td><td>120.50 (-17.80%)</td><td>37.21 <b>(-60.67%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>383.30 (n/a)</td><td>219.20 (n/a)</td><td>179.60 (n/a)</td><td>146.60 (n/a)</td><td>94.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (+9.25%)</td><td>0.22 (+19.74%)</td><td>0.22 <b>(+23.96%)</b></td><td>0.17 (+9.69%)</td><td>0.04 <b>(+20.91%)</b></td><td>196.30 (-8.82%)</td><td>154.70 (-16.13%)</td><td>147.70 (-19.33%)</td><td>129.10 (-8.50%)</td><td>28.97 (-1.23%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.30 (n/a)</td><td>184.46 (n/a)</td><td>183.10 (n/a)</td><td>141.10 (n/a)</td><td>29.33 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.22 <b>(+22.93%)</b></td><td>0.19 <b>(+23.89%)</b></td><td>0.19 (+15.54%)</td><td>0.16 <b>(+55.91%)</b></td><td>0.02 <b>(-24.99%)</b></td><td>203.60 <b>(-35.85%)</b></td><td>175.80 <b>(-21.46%)</b></td><td>175.90 (-13.44%)</td><td>147.20 (-18.63%)</td><td>20.26 <b>(-62.68%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>317.40 (n/a)</td><td>223.84 (n/a)</td><td>203.20 (n/a)</td><td>180.90 (n/a)</td><td>54.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (-17.88%)</td><td>0.19 (+2.40%)</td><td>0.19 (+9.80%)</td><td>0.18 <b>(+26.06%)</b></td><td>0.00 <b>(-93.25%)</b></td><td>178.00 <b>(-20.68%)</b></td><td>174.48 (-5.86%)</td><td>173.30 (-8.93%)</td><td>171.90 <b>(+21.74%)</b></td><td>2.53 <b>(-93.47%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.40 (n/a)</td><td>185.34 (n/a)</td><td>190.30 (n/a)</td><td>141.20 (n/a)</td><td>38.75 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (+0.36%)</td><td>0.21 (+17.92%)</td><td>0.21 <b>(+31.56%)</b></td><td>0.17 <b>(+32.50%)</b></td><td>0.03 <b>(-34.30%)</b></td><td>196.00 <b>(-24.56%)</b></td><td>156.08 (-18.17%)</td><td>152.60 <b>(-24.00%)</b></td><td>128.70 (-0.31%)</td><td>24.90 <b>(-49.03%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>259.80 (n/a)</td><td>190.74 (n/a)</td><td>200.80 (n/a)</td><td>129.10 (n/a)</td><td>48.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 <b>(+31.26%)</b></td><td>0.23 <b>(+28.55%)</b></td><td>0.24 <b>(+32.39%)</b></td><td>0.18 (+14.55%)</td><td>0.04 <b>(+110.02%)</b></td><td>184.50 (-12.68%)</td><td>145.16 <b>(-20.94%)</b></td><td>135.50 <b>(-24.47%)</b></td><td>122.60 <b>(-23.85%)</b></td><td>26.53 <b>(+37.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>211.30 (n/a)</td><td>183.60 (n/a)</td><td>179.40 (n/a)</td><td>161.00 (n/a)</td><td>19.35 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.31 <b>(+29.44%)</b></td><td>0.23 (+18.69%)</td><td>0.22 <b>(+22.43%)</b></td><td>0.19 (+17.90%)</td><td>0.05 <b>(+43.86%)</b></td><td>170.70 (-15.20%)</td><td>148.20 (-15.21%)</td><td>151.70 (-18.31%)</td><td>106.60 <b>(-22.70%)</b></td><td>24.70 (-9.31%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>201.30 (n/a)</td><td>174.78 (n/a)</td><td>185.70 (n/a)</td><td>137.90 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (-15.27%)</td><td>0.19 (+0.94%)</td><td>0.19 (+0.93%)</td><td>0.17 <b>(+87.91%)</b></td><td>0.02 <b>(-72.93%)</b></td><td>188.20 <b>(-46.78%)</b></td><td>173.46 (-14.74%)</td><td>173.80 (-0.91%)</td><td>145.60 (+17.99%)</td><td>17.20 <b>(-82.17%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>353.60 (n/a)</td><td>203.44 (n/a)</td><td>175.40 (n/a)</td><td>123.40 (n/a)</td><td>96.46 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (-5.83%)</td><td>0.20 (-2.53%)</td><td>0.19 (+0.13%)</td><td>0.14 (-2.50%)</td><td>0.04 <b>(-27.37%)</b></td><td>231.30 (+2.57%)</td><td>172.00 (-0.38%)</td><td>175.60 (-0.17%)</td><td>126.20 (+6.14%)</td><td>39.27 <b>(-20.37%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>225.50 (n/a)</td><td>172.66 (n/a)</td><td>175.90 (n/a)</td><td>118.90 (n/a)</td><td>49.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (-13.80%)</td><td>0.20 (-4.81%)</td><td>0.19 (-0.37%)</td><td>0.17 (-2.85%)</td><td>0.03 <b>(-31.10%)</b></td><td>195.20 (+2.90%)</td><td>167.00 (+3.52%)</td><td>174.10 (+0.40%)</td><td>129.80 (+16.00%)</td><td>25.46 (-16.58%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>189.70 (n/a)</td><td>161.32 (n/a)</td><td>173.40 (n/a)</td><td>111.90 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (+18.54%)</td><td>0.22 (+11.57%)</td><td>0.20 (+4.60%)</td><td>0.18 (+14.83%)</td><td>0.05 <b>(+28.67%)</b></td><td>183.20 (-12.93%)</td><td>152.02 (-9.78%)</td><td>164.40 (-4.36%)</td><td>113.00 (-15.67%)</td><td>30.24 (-3.97%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.40 (n/a)</td><td>168.50 (n/a)</td><td>171.90 (n/a)</td><td>134.00 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 <b>(+42.73%)</b></td><td>0.22 <b>(+25.31%)</b></td><td>0.20 (+10.24%)</td><td>0.19 <b>(+24.12%)</b></td><td>0.04 <b>(+146.46%)</b></td><td>173.80 (-19.43%)</td><td>150.38 (-19.05%)</td><td>163.30 (-9.28%)</td><td>122.50 <b>(-29.92%)</b></td><td>23.08 <b>(+36.03%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>185.78 (n/a)</td><td>180.00 (n/a)</td><td>174.80 (n/a)</td><td>16.97 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (+5.13%)</td><td>0.17 (-1.44%)</td><td>0.18 (+2.42%)</td><td>0.12 (-11.50%)</td><td>0.04 <b>(+66.72%)</b></td><td>271.20 (+13.00%)</td><td>199.68 (+4.84%)</td><td>178.40 (-2.35%)</td><td>154.50 (-4.86%)</td><td>51.84 <b>(+72.81%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>240.00 (n/a)</td><td>190.46 (n/a)</td><td>182.70 (n/a)</td><td>162.40 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.24 (+9.54%)</td><td>0.19 (+5.78%)</td><td>0.18 (+9.89%)</td><td>0.14 (-5.17%)</td><td>0.04 <b>(+39.87%)</b></td><td>238.30 (+5.44%)</td><td>179.72 (-3.60%)</td><td>178.10 (-8.99%)</td><td>135.10 (-8.72%)</td><td>41.86 <b>(+34.69%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>226.00 (n/a)</td><td>186.44 (n/a)</td><td>195.70 (n/a)</td><td>148.00 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.22 (-16.15%)</td><td>0.20 (+4.80%)</td><td>0.20 <b>(+26.37%)</b></td><td>0.17 (+10.85%)</td><td>0.03 <b>(-49.44%)</b></td><td>198.10 (-9.79%)</td><td>168.82 (-8.21%)</td><td>164.00 <b>(-20.89%)</b></td><td>147.10 (+19.30%)</td><td>22.90 <b>(-47.68%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>219.60 (n/a)</td><td>183.92 (n/a)</td><td>207.30 (n/a)</td><td>123.30 (n/a)</td><td>43.76 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (+5.20%)</td><td>0.19 (+10.88%)</td><td>0.20 (+19.51%)</td><td>0.17 (+8.32%)</td><td>0.01 <b>(-25.90%)</b></td><td>189.70 (-7.69%)</td><td>170.92 (-10.09%)</td><td>165.70 (-16.36%)</td><td>163.90 (-4.93%)</td><td>10.72 <b>(-33.77%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>205.50 (n/a)</td><td>190.10 (n/a)</td><td>198.10 (n/a)</td><td>172.40 (n/a)</td><td>16.19 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (+0.05%)</td><td>0.18 (-0.09%)</td><td>0.18 (-0.13%)</td><td>0.18 (-0.19%)</td><td>0.00 <b>(+36.39%)</b></td><td>47748.40 (+0.19%)</td><td>47561.68 (+0.09%)</td><td>47560.80 (+0.13%)</td><td>47418.60 (-0.05%)</td><td>119.53 <b>(+36.61%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47657.80 (n/a)</td><td>47518.84 (n/a)</td><td>47498.90 (n/a)</td><td>47442.40 (n/a)</td><td>87.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (-0.78%)</td><td>0.18 (-0.23%)</td><td>0.18 (-0.16%)</td><td>0.18 (-0.08%)</td><td>0.00 <b>(-74.51%)</b></td><td>47582.70 (+0.08%)</td><td>47530.50 (+0.23%)</td><td>47552.20 (+0.16%)</td><td>47479.20 (+0.79%)</td><td>46.38 <b>(-74.28%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47543.40 (n/a)</td><td>47420.28 (n/a)</td><td>47477.10 (n/a)</td><td>47106.80 (n/a)</td><td>180.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (-0.06%)</td><td>0.11 (-0.02%)</td><td>0.11 (-0.05%)</td><td>0.11 (+0.03%)</td><td>0.00 <b>(-31.02%)</b></td><td>375637.20 (-0.03%)</td><td>375506.92 (+0.02%)</td><td>375617.30 (+0.05%)</td><td>375287.30 (+0.06%)</td><td>170.60 <b>(-31.01%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>375750.70 (n/a)</td><td>375436.24 (n/a)</td><td>375432.80 (n/a)</td><td>375076.90 (n/a)</td><td>247.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (+12.75%)</td><td>0.17 <b>(+22.21%)</b></td><td>0.16 <b>(+20.90%)</b></td><td>0.12 (+14.45%)</td><td>0.03 <b>(+26.17%)</b></td><td>199.50 (-12.61%)</td><td>150.32 (-17.68%)</td><td>150.00 (-17.31%)</td><td>121.50 (-11.25%)</td><td>31.90 (-3.22%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>228.30 (n/a)</td><td>182.60 (n/a)</td><td>181.40 (n/a)</td><td>136.90 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.38 <b>(+28.11%)</b></td><td>0.35 <b>(+32.04%)</b></td><td>0.37 <b>(+40.21%)</b></td><td>0.32 <b>(+42.39%)</b></td><td>0.03 (-4.42%)</td><td>155.60 <b>(-29.75%)</b></td><td>139.40 <b>(-24.70%)</b></td><td>132.30 <b>(-28.68%)</b></td><td>128.60 <b>(-21.92%)</b></td><td>12.31 <b>(-46.98%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>221.50 (n/a)</td><td>185.12 (n/a)</td><td>185.50 (n/a)</td><td>164.70 (n/a)</td><td>23.21 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.66 (+1.45%)</td><td>13.03 (+2.84%)</td><td>12.82 (+2.45%)</td><td>12.63 (+3.14%)</td><td>0.42 (-15.28%)</td><td>830.30 (-3.05%)</td><td>805.24 (-2.80%)</td><td>817.90 (-2.40%)</td><td>767.80 (-1.44%)</td><td>25.35 (-18.99%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.46 (n/a)</td><td>12.67 (n/a)</td><td>12.51 (n/a)</td><td>12.24 (n/a)</td><td>0.49 (n/a)</td><td>856.40 (n/a)</td><td>828.46 (n/a)</td><td>838.00 (n/a)</td><td>779.00 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.30 (-7.39%)</td><td>0.25 (-2.71%)</td><td>0.25 (+0.16%)</td><td>0.23 (-2.84%)</td><td>0.03 <b>(-23.74%)</b></td><td>181.20 (+2.90%)</td><td>164.22 (+2.25%)</td><td>167.10 (-0.18%)</td><td>136.10 (+8.02%)</td><td>16.82 (-15.49%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>176.10 (n/a)</td><td>160.60 (n/a)</td><td>167.40 (n/a)</td><td>126.00 (n/a)</td><td>19.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (-7.21%)</td><td>0.04 (+7.45%)</td><td>0.04 (+16.91%)</td><td>0.03 (+9.37%)</td><td>0.00 <b>(-33.74%)</b></td><td>162.50 (-8.61%)</td><td>131.78 (-8.30%)</td><td>125.20 (-14.48%)</td><td>120.30 (+7.80%)</td><td>17.38 <b>(-32.89%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>177.80 (n/a)</td><td>143.70 (n/a)</td><td>146.40 (n/a)</td><td>111.60 (n/a)</td><td>25.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+11.53%)</td><td>0.03 (+15.13%)</td><td>0.03 (+14.73%)</td><td>0.02 <b>(+29.13%)</b></td><td>0.00 <b>(-30.07%)</b></td><td>170.80 <b>(-22.54%)</b></td><td>156.34 (-14.56%)</td><td>160.60 (-12.81%)</td><td>131.20 (-10.32%)</td><td>15.38 <b>(-51.99%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>182.98 (n/a)</td><td>184.20 (n/a)</td><td>146.30 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (-0.23%)</td><td>0.04 (-6.34%)</td><td>0.04 (-11.67%)</td><td>0.03 (+7.20%)</td><td>0.01 (-9.81%)</td><td>191.70 (-6.72%)</td><td>169.72 (+6.13%)</td><td>175.30 (+13.24%)</td><td>132.10 (+0.23%)</td><td>22.82 (-19.25%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>159.92 (n/a)</td><td>154.80 (n/a)</td><td>131.80 (n/a)</td><td>28.25 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+6.05%)</td><td>0.03 (+4.20%)</td><td>0.02 (+4.85%)</td><td>0.02 (-17.04%)</td><td>0.01 <b>(+87.99%)</b></td><td>218.00 <b>(+20.58%)</b></td><td>165.30 (-1.61%)</td><td>164.80 (-4.63%)</td><td>132.40 (-5.70%)</td><td>34.97 <b>(+109.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.80 (n/a)</td><td>168.00 (n/a)</td><td>172.80 (n/a)</td><td>140.40 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (-5.84%)</td><td>0.03 (-7.79%)</td><td>0.03 (-1.81%)</td><td>0.02 (-12.79%)</td><td>0.01 (-2.51%)</td><td>240.40 (+14.69%)</td><td>183.44 (+9.00%)</td><td>173.40 (+1.88%)</td><td>136.40 (+6.23%)</td><td>38.74 <b>(+20.12%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>168.30 (n/a)</td><td>170.20 (n/a)</td><td>128.40 (n/a)</td><td>32.25 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-3.89%)</td><td>0.03 (+3.57%)</td><td>0.03 (+9.38%)</td><td>0.02 <b>(+27.10%)</b></td><td>0.00 <b>(-35.99%)</b></td><td>195.10 <b>(-21.30%)</b></td><td>162.06 (-6.14%)</td><td>151.00 (-8.60%)</td><td>143.40 (+4.06%)</td><td>22.20 <b>(-49.46%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.90 (n/a)</td><td>172.66 (n/a)</td><td>165.20 (n/a)</td><td>137.80 (n/a)</td><td>43.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-0.42%)</td><td>0.03 (-8.52%)</td><td>0.03 (+5.02%)</td><td>0.02 <b>(-30.38%)</b></td><td>0.01 <b>(+110.92%)</b></td><td>300.10 <b>(+43.66%)</b></td><td>205.44 (+15.74%)</td><td>171.00 (-4.79%)</td><td>152.30 (+0.40%)</td><td>63.66 <b>(+201.12%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.90 (n/a)</td><td>177.50 (n/a)</td><td>179.60 (n/a)</td><td>151.70 (n/a)</td><td>21.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+1.57%)</td><td>0.02 (+0.97%)</td><td>0.02 (-0.50%)</td><td>0.02 (+0.83%)</td><td>0.00 (-2.76%)</td><td>228.70 (-0.78%)</td><td>189.50 (-1.10%)</td><td>179.20 (+0.50%)</td><td>158.40 (-1.55%)</td><td>28.61 (-5.21%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.50 (n/a)</td><td>191.60 (n/a)</td><td>178.30 (n/a)</td><td>160.90 (n/a)</td><td>30.19 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 <b>(-23.23%)</b></td><td>0.03 (-11.97%)</td><td>0.03 (-8.43%)</td><td>0.02 (-16.82%)</td><td>0.01 <b>(-37.85%)</b></td><td>254.30 <b>(+20.18%)</b></td><td>186.10 (+10.83%)</td><td>175.20 (+9.23%)</td><td>139.50 <b>(+30.25%)</b></td><td>42.59 (-3.61%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>167.92 (n/a)</td><td>160.40 (n/a)</td><td>107.10 (n/a)</td><td>44.19 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 <b>(+40.58%)</b></td><td>0.03 (+3.43%)</td><td>0.02 (-6.85%)</td><td>0.02 (-4.71%)</td><td>0.01 <b>(+187.04%)</b></td><td>195.90 (+4.93%)</td><td>166.92 (+1.87%)</td><td>179.80 (+7.41%)</td><td>99.50 <b>(-28.88%)</b></td><td>39.44 <b>(+109.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.70 (n/a)</td><td>163.86 (n/a)</td><td>167.40 (n/a)</td><td>139.90 (n/a)</td><td>18.82 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (-3.48%)</td><td>0.03 (+0.48%)</td><td>0.03 (+3.09%)</td><td>0.02 (-6.50%)</td><td>0.00 (+10.00%)</td><td>217.90 (+6.97%)</td><td>176.10 (+0.01%)</td><td>163.60 (-3.02%)</td><td>149.90 (+3.59%)</td><td>29.36 (+18.90%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.70 (n/a)</td><td>176.08 (n/a)</td><td>168.70 (n/a)</td><td>144.70 (n/a)</td><td>24.69 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 <b>(+44.14%)</b></td><td>0.03 (+18.03%)</td><td>0.03 (+13.58%)</td><td>0.02 (+1.95%)</td><td>0.01 <b>(+118.70%)</b></td><td>219.80 (-1.92%)</td><td>161.10 (-12.63%)</td><td>157.00 (-11.95%)</td><td>112.50 <b>(-30.60%)</b></td><td>38.42 <b>(+49.77%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.10 (n/a)</td><td>184.38 (n/a)</td><td>178.30 (n/a)</td><td>162.10 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+10.91%)</td><td>0.02 (+16.32%)</td><td>0.02 <b>(+21.74%)</b></td><td>0.02 (+16.31%)</td><td>0.00 (-12.25%)</td><td>193.50 (-14.04%)</td><td>176.48 (-14.26%)</td><td>174.30 (-17.86%)</td><td>162.80 (-9.86%)</td><td>12.59 <b>(-31.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.10 (n/a)</td><td>205.84 (n/a)</td><td>212.20 (n/a)</td><td>180.60 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+5.81%)</td><td>0.03 (+6.77%)</td><td>0.03 (+13.32%)</td><td>0.02 (+1.17%)</td><td>0.01 (+11.72%)</td><td>214.60 (-1.15%)</td><td>165.58 (-5.87%)</td><td>155.10 (-11.72%)</td><td>126.40 (-5.46%)</td><td>33.88 (+5.95%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.10 (n/a)</td><td>175.90 (n/a)</td><td>175.70 (n/a)</td><td>133.70 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 <b>(-28.29%)</b></td><td>0.02 (-13.64%)</td><td>0.02 (-6.98%)</td><td>0.02 (-17.53%)</td><td>0.00 <b>(-44.46%)</b></td><td>261.10 <b>(+21.27%)</b></td><td>221.16 (+14.12%)</td><td>221.60 (+7.52%)</td><td>187.80 <b>(+39.42%)</b></td><td>31.69 (-5.06%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>193.80 (n/a)</td><td>206.10 (n/a)</td><td>134.70 (n/a)</td><td>33.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (+12.33%)</td><td>0.02 (+1.83%)</td><td>0.02 (-0.83%)</td><td>0.02 (-7.74%)</td><td>0.00 <b>(+124.93%)</b></td><td>258.80 (+8.42%)</td><td>222.82 (-0.59%)</td><td>223.60 (+0.86%)</td><td>181.30 (-11.00%)</td><td>30.24 <b>(+116.13%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.70 (n/a)</td><td>224.14 (n/a)</td><td>221.70 (n/a)</td><td>203.70 (n/a)</td><td>13.99 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 <b>(+20.35%)</b></td><td>0.06 (+18.63%)</td><td>0.06 <b>(+21.92%)</b></td><td>0.05 <b>(+28.35%)</b></td><td>0.01 (+0.69%)</td><td>172.20 <b>(-22.12%)</b></td><td>150.68 (-16.21%)</td><td>147.80 (-18.03%)</td><td>127.90 (-16.89%)</td><td>18.67 <b>(-32.73%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>179.82 (n/a)</td><td>180.30 (n/a)</td><td>153.90 (n/a)</td><td>27.75 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (-12.55%)</td><td>0.07 (-16.99%)</td><td>0.07 (-1.90%)</td><td>0.04 <b>(-34.54%)</b></td><td>0.02 (+9.90%)</td><td>301.20 <b>(+52.74%)</b></td><td>197.30 <b>(+25.16%)</b></td><td>172.20 (+1.89%)</td><td>141.00 (+14.36%)</td><td>64.12 <b>(+102.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>197.20 (n/a)</td><td>157.64 (n/a)</td><td>169.00 (n/a)</td><td>123.30 (n/a)</td><td>31.59 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 <b>(+32.45%)</b></td><td>0.05 (+5.53%)</td><td>0.05 (-4.19%)</td><td>0.04 (-12.63%)</td><td>0.01 <b>(+282.49%)</b></td><td>213.20 (+14.50%)</td><td>169.90 (-1.60%)</td><td>179.20 (+4.43%)</td><td>120.80 <b>(-24.50%)</b></td><td>36.70 <b>(+226.60%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.20 (n/a)</td><td>172.66 (n/a)</td><td>171.60 (n/a)</td><td>160.00 (n/a)</td><td>11.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 <b>(+30.26%)</b></td><td>0.06 (+5.84%)</td><td>0.06 (+3.72%)</td><td>0.04 (-18.77%)</td><td>0.02 <b>(+215.59%)</b></td><td>256.80 <b>(+23.11%)</b></td><td>183.96 (-0.59%)</td><td>181.50 (-3.61%)</td><td>129.00 <b>(-23.21%)</b></td><td>49.76 <b>(+200.20%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>208.60 (n/a)</td><td>185.06 (n/a)</td><td>188.30 (n/a)</td><td>168.00 (n/a)</td><td>16.58 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (+4.72%)</td><td>0.05 (-0.03%)</td><td>0.05 (-8.06%)</td><td>0.04 (+9.24%)</td><td>0.01 (+3.46%)</td><td>194.20 (-8.48%)</td><td>166.68 (-0.17%)</td><td>174.00 (+8.75%)</td><td>129.60 (-4.50%)</td><td>26.08 (-11.12%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>166.96 (n/a)</td><td>160.00 (n/a)</td><td>135.70 (n/a)</td><td>29.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (-9.00%)</td><td>0.06 (-6.92%)</td><td>0.06 (-1.23%)</td><td>0.05 (-8.45%)</td><td>0.01 (-5.83%)</td><td>207.80 (+9.25%)</td><td>171.50 (+7.69%)</td><td>177.40 (+1.26%)</td><td>131.10 (+9.89%)</td><td>35.66 (+13.26%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>159.26 (n/a)</td><td>175.20 (n/a)</td><td>119.30 (n/a)</td><td>31.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (+18.93%)</td><td>0.05 (+10.21%)</td><td>0.05 (+14.17%)</td><td>0.04 (-15.95%)</td><td>0.01 <b>(+160.56%)</b></td><td>228.80 (+18.98%)</td><td>166.28 (-6.50%)</td><td>157.00 (-12.39%)</td><td>130.80 (-15.94%)</td><td>37.48 <b>(+173.48%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>192.30 (n/a)</td><td>177.84 (n/a)</td><td>179.20 (n/a)</td><td>155.60 (n/a)</td><td>13.71 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 <b>(+28.63%)</b></td><td>0.05 (+0.61%)</td><td>0.05 (-12.94%)</td><td>0.04 (-16.23%)</td><td>0.02 <b>(+279.07%)</b></td><td>218.10 (+19.38%)</td><td>179.52 (+4.99%)</td><td>201.30 (+14.90%)</td><td>121.00 <b>(-22.24%)</b></td><td>45.53 <b>(+260.44%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>182.70 (n/a)</td><td>170.98 (n/a)</td><td>175.20 (n/a)</td><td>155.60 (n/a)</td><td>12.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 <b>(+20.08%)</b></td><td>0.05 (-2.82%)</td><td>0.04 (-15.07%)</td><td>0.03 (-17.09%)</td><td>0.02 <b>(+85.53%)</b></td><td>238.00 <b>(+20.63%)</b></td><td>184.40 (+8.29%)</td><td>198.90 (+17.69%)</td><td>107.00 (-16.73%)</td><td>49.07 <b>(+75.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>170.28 (n/a)</td><td>169.00 (n/a)</td><td>128.50 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (-5.44%)</td><td>0.05 (-19.71%)</td><td>0.05 (-15.79%)</td><td>0.03 <b>(-42.64%)</b></td><td>0.01 <b>(+103.08%)</b></td><td>309.10 <b>(+74.34%)</b></td><td>210.16 <b>(+33.32%)</b></td><td>184.70 (+18.78%)</td><td>139.50 (+5.76%)</td><td>67.89 <b>(+280.47%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.30 (n/a)</td><td>157.64 (n/a)</td><td>155.50 (n/a)</td><td>131.90 (n/a)</td><td>17.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (+1.02%)</td><td>0.04 (-9.38%)</td><td>0.04 (-11.94%)</td><td>0.04 (-8.17%)</td><td>0.01 <b>(+36.88%)</b></td><td>232.50 (+8.90%)</td><td>206.52 (+11.58%)</td><td>213.90 (+13.54%)</td><td>152.10 (-1.04%)</td><td>31.50 <b>(+44.45%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>185.08 (n/a)</td><td>188.40 (n/a)</td><td>153.70 (n/a)</td><td>21.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (-12.33%)</td><td>0.04 (-3.37%)</td><td>0.04 (+2.46%)</td><td>0.04 (-1.32%)</td><td>0.00 <b>(-37.95%)</b></td><td>243.10 (+1.33%)</td><td>210.68 (+2.69%)</td><td>202.30 (-2.41%)</td><td>192.30 (+14.06%)</td><td>19.67 <b>(-26.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.90 (n/a)</td><td>205.16 (n/a)</td><td>207.30 (n/a)</td><td>168.60 (n/a)</td><td>26.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (+3.00%)</td><td>0.04 (-6.61%)</td><td>0.04 (-2.41%)</td><td>0.03 (-1.54%)</td><td>0.01 (+0.14%)</td><td>253.00 (+1.57%)</td><td>196.84 (+7.01%)</td><td>198.20 (+2.48%)</td><td>133.40 (-2.91%)</td><td>44.63 (-0.74%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.10 (n/a)</td><td>183.94 (n/a)</td><td>193.40 (n/a)</td><td>137.40 (n/a)</td><td>44.96 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 <b>(+27.76%)</b></td><td>0.05 (+2.93%)</td><td>0.04 (-1.01%)</td><td>0.03 (-19.17%)</td><td>0.01 <b>(+241.70%)</b></td><td>264.40 <b>(+23.72%)</b></td><td>201.10 (+1.53%)</td><td>204.10 (+1.04%)</td><td>137.00 <b>(-21.76%)</b></td><td>47.64 <b>(+230.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.70 (n/a)</td><td>198.06 (n/a)</td><td>202.00 (n/a)</td><td>175.10 (n/a)</td><td>14.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (-18.41%)</td><td>0.03 (-15.20%)</td><td>0.03 (-6.46%)</td><td>0.03 <b>(-26.86%)</b></td><td>0.01 (+18.69%)</td><td>311.30 <b>(+36.71%)</b></td><td>255.24 (+19.34%)</td><td>238.20 (+6.91%)</td><td>217.10 <b>(+22.52%)</b></td><td>41.99 <b>(+100.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>227.70 (n/a)</td><td>213.88 (n/a)</td><td>222.80 (n/a)</td><td>177.20 (n/a)</td><td>20.95 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (+16.48%)</td><td>0.10 (+2.86%)</td><td>0.09 (-3.11%)</td><td>0.08 (-9.11%)</td><td>0.02 <b>(+87.64%)</b></td><td>216.80 (+10.05%)</td><td>175.42 (-0.27%)</td><td>186.20 (+3.22%)</td><td>122.90 (-14.18%)</td><td>35.11 <b>(+77.47%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>175.90 (n/a)</td><td>180.40 (n/a)</td><td>143.20 (n/a)</td><td>19.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (-2.88%)</td><td>0.13 (+3.21%)</td><td>0.14 (+2.17%)</td><td>0.11 <b>(+39.11%)</b></td><td>0.02 <b>(-37.23%)</b></td><td>229.80 <b>(-28.12%)</b></td><td>186.98 (-7.67%)</td><td>178.90 (-2.13%)</td><td>154.10 (+3.01%)</td><td>29.59 <b>(-56.02%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>319.70 (n/a)</td><td>202.52 (n/a)</td><td>182.80 (n/a)</td><td>149.60 (n/a)</td><td>67.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (-19.07%)</td><td>0.09 (-2.61%)</td><td>0.09 (-13.45%)</td><td>0.07 <b>(+52.32%)</b></td><td>0.01 <b>(-67.43%)</b></td><td>219.40 <b>(-34.37%)</b></td><td>186.64 (-6.19%)</td><td>184.40 (+15.54%)</td><td>168.20 <b>(+23.49%)</b></td><td>20.26 <b>(-74.58%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>334.30 (n/a)</td><td>198.96 (n/a)</td><td>159.60 (n/a)</td><td>136.20 (n/a)</td><td>79.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (-3.96%)</td><td>0.11 (-2.33%)</td><td>0.10 (-7.94%)</td><td>0.09 (+2.50%)</td><td>0.02 (-14.15%)</td><td>219.50 (-2.44%)</td><td>192.22 (+1.60%)</td><td>200.20 (+8.63%)</td><td>144.30 (+4.11%)</td><td>29.18 (-14.90%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>225.00 (n/a)</td><td>189.20 (n/a)</td><td>184.30 (n/a)</td><td>138.60 (n/a)</td><td>34.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (-11.74%)</td><td>0.10 (-9.57%)</td><td>0.10 (-5.31%)</td><td>0.07 <b>(-20.09%)</b></td><td>0.02 (+2.58%)</td><td>226.30 <b>(+25.17%)</b></td><td>177.28 (+11.93%)</td><td>171.20 (+5.61%)</td><td>133.20 (+13.36%)</td><td>36.62 <b>(+51.49%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.80 (n/a)</td><td>158.38 (n/a)</td><td>162.10 (n/a)</td><td>117.50 (n/a)</td><td>24.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (+5.99%)</td><td>0.12 (+11.21%)</td><td>0.12 (+15.25%)</td><td>0.10 (+7.47%)</td><td>0.01 (-7.19%)</td><td>199.40 (-6.95%)</td><td>167.22 (-10.39%)</td><td>168.00 (-13.22%)</td><td>145.70 (-5.63%)</td><td>20.55 (-17.69%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>214.30 (n/a)</td><td>186.60 (n/a)</td><td>193.60 (n/a)</td><td>154.40 (n/a)</td><td>24.97 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 <b>(+35.50%)</b></td><td>0.10 <b>(+22.67%)</b></td><td>0.10 (+16.32%)</td><td>0.08 (+18.61%)</td><td>0.02 <b>(+72.07%)</b></td><td>213.20 (-15.66%)</td><td>163.30 (-17.23%)</td><td>166.90 (-14.01%)</td><td>124.30 <b>(-26.23%)</b></td><td>34.55 (+4.37%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>197.30 (n/a)</td><td>194.10 (n/a)</td><td>168.50 (n/a)</td><td>33.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 <b>(+77.90%)</b></td><td>0.12 <b>(+23.19%)</b></td><td>0.11 (+13.06%)</td><td>0.09 (-1.69%)</td><td>0.04 <b>(+504.57%)</b></td><td>202.50 (+1.71%)</td><td>160.94 (-12.87%)</td><td>166.30 (-11.54%)</td><td>92.90 <b>(-43.80%)</b></td><td>42.19 <b>(+232.95%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>199.10 (n/a)</td><td>184.72 (n/a)</td><td>188.00 (n/a)</td><td>165.30 (n/a)</td><td>12.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 <b>(+34.74%)</b></td><td>0.09 (+9.73%)</td><td>0.08 (-2.61%)</td><td>0.08 (+11.17%)</td><td>0.02 <b>(+118.62%)</b></td><td>212.60 (-10.03%)</td><td>184.24 (-6.30%)</td><td>202.40 (+2.69%)</td><td>122.20 <b>(-25.80%)</b></td><td>36.71 <b>(+41.51%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>196.62 (n/a)</td><td>197.10 (n/a)</td><td>164.70 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.15 <b>(+49.86%)</b></td><td>0.12 <b>(+35.02%)</b></td><td>0.10 <b>(+20.59%)</b></td><td>0.07 (-4.09%)</td><td>0.04 <b>(+195.72%)</b></td><td>263.00 (+4.24%)</td><td>174.88 <b>(-20.49%)</b></td><td>181.60 (-17.08%)</td><td>119.60 <b>(-33.30%)</b></td><td>59.02 <b>(+90.67%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>252.30 (n/a)</td><td>219.94 (n/a)</td><td>219.00 (n/a)</td><td>179.30 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (+3.26%)</td><td>0.11 (+9.23%)</td><td>0.11 <b>(+20.71%)</b></td><td>0.08 (-5.57%)</td><td>0.02 (+10.06%)</td><td>199.30 (+5.90%)</td><td>157.70 (-7.94%)</td><td>147.80 (-17.15%)</td><td>123.70 (-3.13%)</td><td>28.87 (+16.59%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.20 (n/a)</td><td>171.30 (n/a)</td><td>178.40 (n/a)</td><td>127.70 (n/a)</td><td>24.76 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 <b>(+80.77%)</b></td><td>0.10 <b>(+30.87%)</b></td><td>0.09 <b>(+30.15%)</b></td><td>0.07 (+6.17%)</td><td>0.04 <b>(+202.56%)</b></td><td>237.50 (-5.83%)</td><td>181.94 (-18.16%)</td><td>188.30 <b>(-23.14%)</b></td><td>100.70 <b>(-44.70%)</b></td><td>52.53 <b>(+52.00%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>252.20 (n/a)</td><td>222.32 (n/a)</td><td>245.00 (n/a)</td><td>182.10 (n/a)</td><td>34.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (-14.18%)</td><td>0.09 (+1.83%)</td><td>0.11 <b>(+23.08%)</b></td><td>0.06 (-14.10%)</td><td>0.02 (-5.12%)</td><td>283.40 (+16.39%)</td><td>183.42 (-0.57%)</td><td>155.70 (-18.74%)</td><td>150.00 (+16.46%)</td><td>56.83 <b>(+32.79%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>243.50 (n/a)</td><td>184.48 (n/a)</td><td>191.60 (n/a)</td><td>128.80 (n/a)</td><td>42.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (-10.78%)</td><td>0.08 (+0.94%)</td><td>0.08 (+8.24%)</td><td>0.05 (-8.26%)</td><td>0.01 (-9.85%)</td><td>334.60 (+8.99%)</td><td>235.28 (-0.67%)</td><td>217.50 (-7.60%)</td><td>192.10 (+12.08%)</td><td>56.55 (+17.70%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>307.00 (n/a)</td><td>236.86 (n/a)</td><td>235.40 (n/a)</td><td>171.40 (n/a)</td><td>48.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (+19.77%)</td><td>0.07 (-3.09%)</td><td>0.07 (-11.28%)</td><td>0.05 <b>(-25.97%)</b></td><td>0.02 <b>(+233.26%)</b></td><td>343.80 <b>(+35.09%)</b></td><td>247.24 (+10.36%)</td><td>247.00 (+12.68%)</td><td>171.60 (-16.50%)</td><td>74.18 <b>(+263.78%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>254.50 (n/a)</td><td>224.04 (n/a)</td><td>219.20 (n/a)</td><td>205.50 (n/a)</td><td>20.39 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (-17.43%)</td><td>0.20 (+3.76%)</td><td>0.21 (+16.68%)</td><td>0.14 <b>(+29.96%)</b></td><td>0.03 <b>(-47.84%)</b></td><td>227.30 <b>(-23.03%)</b></td><td>170.62 (-9.59%)</td><td>159.50 (-14.29%)</td><td>142.20 <b>(+21.12%)</b></td><td>32.81 <b>(-50.28%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>295.30 (n/a)</td><td>188.72 (n/a)</td><td>186.10 (n/a)</td><td>117.40 (n/a)</td><td>65.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.24 (-1.93%)</td><td>0.19 (-6.89%)</td><td>0.20 (-0.53%)</td><td>0.10 <b>(-34.90%)</b></td><td>0.06 <b>(+52.68%)</b></td><td>316.80 <b>(+53.56%)</b></td><td>187.12 (+14.98%)</td><td>160.00 (+0.50%)</td><td>136.70 (+1.94%)</td><td>74.79 <b>(+148.78%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>206.30 (n/a)</td><td>162.74 (n/a)</td><td>159.20 (n/a)</td><td>134.10 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (+1.93%)</td><td>0.21 (+0.35%)</td><td>0.21 (-5.79%)</td><td>0.17 (+12.62%)</td><td>0.04 (-17.65%)</td><td>248.10 (-11.20%)</td><td>198.30 (-2.25%)</td><td>197.30 (+6.19%)</td><td>153.00 (-1.92%)</td><td>37.64 <b>(-27.55%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>279.40 (n/a)</td><td>202.86 (n/a)</td><td>185.80 (n/a)</td><td>156.00 (n/a)</td><td>51.96 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (+17.79%)</td><td>0.22 <b>(+20.75%)</b></td><td>0.21 (+12.92%)</td><td>0.19 <b>(+24.27%)</b></td><td>0.03 <b>(+31.05%)</b></td><td>171.40 (-19.49%)</td><td>149.32 (-16.99%)</td><td>153.40 (-11.43%)</td><td>126.40 (-15.11%)</td><td>21.51 (-11.80%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>212.90 (n/a)</td><td>179.88 (n/a)</td><td>173.20 (n/a)</td><td>148.90 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (-8.16%)</td><td>0.24 (-5.74%)</td><td>0.23 (-5.32%)</td><td>0.18 (-17.45%)</td><td>0.05 <b>(+20.02%)</b></td><td>226.40 <b>(+21.13%)</b></td><td>179.00 (+7.64%)</td><td>178.80 (+5.61%)</td><td>141.40 (+8.85%)</td><td>35.24 <b>(+59.11%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>186.90 (n/a)</td><td>166.30 (n/a)</td><td>169.30 (n/a)</td><td>129.90 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (+3.92%)</td><td>0.19 (-3.12%)</td><td>0.20 (+3.53%)</td><td>0.11 <b>(-35.35%)</b></td><td>0.06 <b>(+66.08%)</b></td><td>311.20 <b>(+54.67%)</b></td><td>190.10 (+11.29%)</td><td>165.00 (-3.40%)</td><td>122.60 (-3.77%)</td><td>73.60 <b>(+160.87%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.20 (n/a)</td><td>170.82 (n/a)</td><td>170.80 (n/a)</td><td>127.40 (n/a)</td><td>28.21 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (-10.34%)</td><td>0.21 (+6.87%)</td><td>0.21 (+9.04%)</td><td>0.17 (+10.24%)</td><td>0.02 <b>(-42.05%)</b></td><td>217.50 (-9.30%)</td><td>179.10 (-8.60%)</td><td>174.50 (-8.30%)</td><td>157.10 (+11.50%)</td><td>23.44 <b>(-41.12%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>239.80 (n/a)</td><td>195.96 (n/a)</td><td>190.30 (n/a)</td><td>140.90 (n/a)</td><td>39.81 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 (+13.84%)</td><td>0.22 (+15.51%)</td><td>0.23 <b>(+38.38%)</b></td><td>0.16 (+0.79%)</td><td>0.05 <b>(+31.76%)</b></td><td>202.40 (-0.78%)</td><td>155.28 (-12.28%)</td><td>140.00 <b>(-27.72%)</b></td><td>118.40 (-12.17%)</td><td>34.88 (+16.04%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>204.00 (n/a)</td><td>177.02 (n/a)</td><td>193.70 (n/a)</td><td>134.80 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.30 (+7.87%)</td><td>0.22 (+3.96%)</td><td>0.23 (+13.84%)</td><td>0.13 <b>(-23.23%)</b></td><td>0.06 <b>(+40.82%)</b></td><td>278.90 <b>(+30.27%)</b></td><td>179.56 (+0.45%)</td><td>163.70 (-12.13%)</td><td>121.50 (-7.32%)</td><td>59.59 <b>(+78.66%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>214.10 (n/a)</td><td>178.76 (n/a)</td><td>186.30 (n/a)</td><td>131.10 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (+17.44%)</td><td>0.19 (+8.88%)</td><td>0.20 (+13.87%)</td><td>0.15 (+0.81%)</td><td>0.04 <b>(+65.42%)</b></td><td>222.60 (-0.80%)</td><td>178.38 (-6.07%)</td><td>165.60 (-12.15%)</td><td>130.50 (-14.87%)</td><td>38.78 <b>(+44.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>224.40 (n/a)</td><td>189.90 (n/a)</td><td>188.50 (n/a)</td><td>153.30 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (-0.22%)</td><td>0.18 (+7.85%)</td><td>0.18 (+10.42%)</td><td>0.15 <b>(+33.00%)</b></td><td>0.02 <b>(-42.18%)</b></td><td>226.90 <b>(-24.82%)</b></td><td>193.88 (-10.15%)</td><td>193.20 (-9.42%)</td><td>169.20 (+0.18%)</td><td>22.98 <b>(-56.61%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>301.80 (n/a)</td><td>215.78 (n/a)</td><td>213.30 (n/a)</td><td>168.90 (n/a)</td><td>52.97 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (+16.18%)</td><td>0.18 (+11.53%)</td><td>0.16 (-10.22%)</td><td>0.15 <b>(+39.89%)</b></td><td>0.04 (-14.27%)</td><td>215.70 <b>(-28.53%)</b></td><td>184.36 (-13.14%)</td><td>199.00 (+11.36%)</td><td>140.00 (-13.90%)</td><td>32.91 <b>(-46.20%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>301.80 (n/a)</td><td>212.24 (n/a)</td><td>178.70 (n/a)</td><td>162.60 (n/a)</td><td>61.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (-2.40%)</td><td>0.17 (-4.77%)</td><td>0.17 (+0.40%)</td><td>0.15 (-2.29%)</td><td>0.02 (-11.39%)</td><td>232.90 (+2.33%)</td><td>209.96 (+4.81%)</td><td>205.60 (-0.39%)</td><td>177.60 (+2.48%)</td><td>22.72 (-4.82%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>227.60 (n/a)</td><td>200.32 (n/a)</td><td>206.40 (n/a)</td><td>173.30 (n/a)</td><td>23.88 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (-4.08%)</td><td>0.16 (+8.10%)</td><td>0.16 (+12.69%)</td><td>0.14 (+12.71%)</td><td>0.01 <b>(-40.49%)</b></td><td>237.70 (-11.27%)</td><td>207.96 (-8.46%)</td><td>205.10 (-11.29%)</td><td>191.50 (+4.25%)</td><td>17.69 <b>(-43.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>267.90 (n/a)</td><td>227.18 (n/a)</td><td>231.20 (n/a)</td><td>183.70 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (+17.56%)</td><td>0.14 (+13.16%)</td><td>0.13 (+4.24%)</td><td>0.11 (+8.58%)</td><td>0.02 <b>(+34.96%)</b></td><td>183.20 (-7.89%)</td><td>153.72 (-11.06%)</td><td>161.50 (-4.10%)</td><td>119.30 (-14.97%)</td><td>25.93 (+2.30%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>198.90 (n/a)</td><td>172.84 (n/a)</td><td>168.40 (n/a)</td><td>140.30 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (-8.09%)</td><td>0.12 (-13.89%)</td><td>0.12 (-13.48%)</td><td>0.08 <b>(-27.89%)</b></td><td>0.02 <b>(+40.89%)</b></td><td>270.90 <b>(+38.71%)</b></td><td>185.00 (+19.49%)</td><td>168.20 (+15.60%)</td><td>154.60 (+8.80%)</td><td>48.76 <b>(+114.84%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>195.30 (n/a)</td><td>154.82 (n/a)</td><td>145.50 (n/a)</td><td>142.10 (n/a)</td><td>22.69 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (-7.70%)</td><td>0.13 (-0.55%)</td><td>0.14 (+10.06%)</td><td>0.11 (+2.43%)</td><td>0.02 <b>(-23.65%)</b></td><td>189.20 (-2.37%)</td><td>155.38 (-0.52%)</td><td>146.40 (-9.12%)</td><td>131.80 (+8.39%)</td><td>24.13 (-17.98%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>193.80 (n/a)</td><td>156.20 (n/a)</td><td>161.10 (n/a)</td><td>121.60 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (-0.10%)</td><td>0.14 (+8.71%)</td><td>0.13 (-8.44%)</td><td>0.11 <b>(+104.80%)</b></td><td>0.02 <b>(-50.72%)</b></td><td>180.70 <b>(-51.16%)</b></td><td>153.86 (-19.42%)</td><td>159.60 (+9.24%)</td><td>129.10 (+0.08%)</td><td>22.95 <b>(-77.42%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>370.00 (n/a)</td><td>190.94 (n/a)</td><td>146.10 (n/a)</td><td>129.00 (n/a)</td><td>101.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 <b>(+28.30%)</b></td><td>0.13 (+16.36%)</td><td>0.11 (-3.09%)</td><td>0.10 <b>(+74.93%)</b></td><td>0.03 (+6.59%)</td><td>208.90 <b>(-42.83%)</b></td><td>169.10 (-18.33%)</td><td>179.80 (+3.16%)</td><td>119.10 <b>(-22.11%)</b></td><td>40.92 <b>(-54.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>365.40 (n/a)</td><td>207.06 (n/a)</td><td>174.30 (n/a)</td><td>152.90 (n/a)</td><td>89.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (-4.79%)</td><td>0.13 (+1.00%)</td><td>0.11 (-12.48%)</td><td>0.11 (+15.15%)</td><td>0.03 (+0.37%)</td><td>191.40 (-13.16%)</td><td>165.42 (-1.23%)</td><td>189.60 (+14.29%)</td><td>127.40 (+5.03%)</td><td>34.30 (-8.29%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>220.40 (n/a)</td><td>167.48 (n/a)</td><td>165.90 (n/a)</td><td>121.30 (n/a)</td><td>37.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (+4.02%)</td><td>0.10 (-13.43%)</td><td>0.10 (-19.39%)</td><td>0.07 <b>(-32.05%)</b></td><td>0.02 <b>(+103.53%)</b></td><td>294.00 <b>(+47.15%)</b></td><td>210.38 <b>(+20.03%)</b></td><td>209.10 <b>(+24.02%)</b></td><td>153.10 (-3.89%)</td><td>52.89 <b>(+194.29%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>175.28 (n/a)</td><td>168.60 (n/a)</td><td>159.30 (n/a)</td><td>17.97 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (-8.87%)</td><td>0.10 (-10.20%)</td><td>0.10 (-10.23%)</td><td>0.07 (-9.51%)</td><td>0.02 (-17.14%)</td><td>278.90 (+10.50%)</td><td>218.08 (+10.30%)</td><td>212.80 (+11.36%)</td><td>154.80 (+9.79%)</td><td>46.30 (-2.90%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>252.40 (n/a)</td><td>197.72 (n/a)</td><td>191.10 (n/a)</td><td>141.00 (n/a)</td><td>47.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (+2.01%)</td><td>0.15 (+1.07%)</td><td>0.14 (+2.54%)</td><td>0.13 (-3.04%)</td><td>0.03 (+15.96%)</td><td>192.60 (+3.10%)</td><td>163.52 (-0.45%)</td><td>174.30 (-2.52%)</td><td>129.80 (-1.96%)</td><td>28.08 (+15.65%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>186.80 (n/a)</td><td>164.26 (n/a)</td><td>178.80 (n/a)</td><td>132.40 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 <b>(+28.93%)</b></td><td>0.16 (+15.20%)</td><td>0.16 (+13.76%)</td><td>0.12 (+1.66%)</td><td>0.03 <b>(+98.70%)</b></td><td>202.20 (-1.65%)</td><td>156.14 (-11.23%)</td><td>157.00 (-12.09%)</td><td>120.20 <b>(-22.45%)</b></td><td>32.35 <b>(+53.27%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>205.60 (n/a)</td><td>175.90 (n/a)</td><td>178.60 (n/a)</td><td>155.00 (n/a)</td><td>21.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (+0.53%)</td><td>0.15 (+0.30%)</td><td>0.14 (-4.99%)</td><td>0.12 <b>(+27.09%)</b></td><td>0.03 <b>(-28.59%)</b></td><td>204.10 <b>(-21.32%)</b></td><td>172.52 (-3.57%)</td><td>181.80 (+5.27%)</td><td>133.20 (-0.52%)</td><td>28.28 <b>(-44.02%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>259.40 (n/a)</td><td>178.90 (n/a)</td><td>172.70 (n/a)</td><td>133.90 (n/a)</td><td>50.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (-1.01%)</td><td>0.16 (+12.98%)</td><td>0.15 (+6.52%)</td><td>0.14 (+18.94%)</td><td>0.02 (-18.93%)</td><td>177.90 (-15.93%)</td><td>156.12 (-12.70%)</td><td>164.40 (-6.11%)</td><td>129.60 (+1.01%)</td><td>22.90 <b>(-31.36%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.60 (n/a)</td><td>178.84 (n/a)</td><td>175.10 (n/a)</td><td>128.30 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.15 <b>(-31.22%)</b></td><td>0.14 (-14.00%)</td><td>0.15 (+3.31%)</td><td>0.11 (-10.82%)</td><td>0.02 <b>(-56.25%)</b></td><td>215.10 (+12.15%)</td><td>179.00 (+12.78%)</td><td>167.30 (-3.18%)</td><td>159.10 <b>(+45.43%)</b></td><td>24.50 <b>(-29.79%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>191.80 (n/a)</td><td>158.72 (n/a)</td><td>172.80 (n/a)</td><td>109.40 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (-4.93%)</td><td>0.14 (-15.14%)</td><td>0.14 <b>(-22.30%)</b></td><td>0.11 (-10.89%)</td><td>0.03 (-7.65%)</td><td>231.90 (+12.25%)</td><td>185.86 (+17.69%)</td><td>179.80 <b>(+28.70%)</b></td><td>128.60 (+5.15%)</td><td>39.40 (+6.09%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>206.60 (n/a)</td><td>157.92 (n/a)</td><td>139.70 (n/a)</td><td>122.30 (n/a)</td><td>37.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 <b>(+36.66%)</b></td><td>0.15 (+0.60%)</td><td>0.13 (-16.25%)</td><td>0.10 (-15.11%)</td><td>0.05 <b>(+140.50%)</b></td><td>240.30 (+17.79%)</td><td>182.30 (+5.47%)</td><td>192.80 (+19.38%)</td><td>106.30 <b>(-26.79%)</b></td><td>49.82 <b>(+93.27%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>172.84 (n/a)</td><td>161.50 (n/a)</td><td>145.20 (n/a)</td><td>25.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (-0.98%)</td><td>0.14 (-11.41%)</td><td>0.13 <b>(-21.21%)</b></td><td>0.10 (-15.13%)</td><td>0.03 (+8.50%)</td><td>240.80 (+17.87%)</td><td>187.16 (+14.01%)</td><td>194.50 <b>(+26.88%)</b></td><td>126.10 (+0.96%)</td><td>41.50 <b>(+21.08%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>204.30 (n/a)</td><td>164.16 (n/a)</td><td>153.30 (n/a)</td><td>124.90 (n/a)</td><td>34.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (-18.28%)</td><td>0.10 (-15.13%)</td><td>0.10 (-8.47%)</td><td>0.09 (-19.30%)</td><td>0.01 <b>(-32.99%)</b></td><td>211.60 <b>(+23.89%)</b></td><td>180.36 (+17.30%)</td><td>181.90 (+9.25%)</td><td>160.20 <b>(+22.38%)</b></td><td>20.18 (+2.04%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>170.80 (n/a)</td><td>153.76 (n/a)</td><td>166.50 (n/a)</td><td>130.90 (n/a)</td><td>19.77 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (-19.79%)</td><td>0.10 (-8.04%)</td><td>0.10 (-4.97%)</td><td>0.09 (+2.26%)</td><td>0.01 <b>(-55.94%)</b></td><td>206.60 (-2.22%)</td><td>181.38 (+7.20%)</td><td>176.70 (+5.24%)</td><td>172.40 <b>(+24.66%)</b></td><td>14.21 <b>(-46.54%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>211.30 (n/a)</td><td>169.20 (n/a)</td><td>167.90 (n/a)</td><td>138.30 (n/a)</td><td>26.58 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (-11.53%)</td><td>0.11 (-14.52%)</td><td>0.11 (-18.56%)</td><td>0.10 (-2.92%)</td><td>0.01 <b>(-34.99%)</b></td><td>187.40 (+3.02%)</td><td>166.82 (+16.06%)</td><td>167.20 <b>(+22.76%)</b></td><td>145.90 (+13.01%)</td><td>15.83 <b>(-26.52%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>181.90 (n/a)</td><td>143.74 (n/a)</td><td>136.20 (n/a)</td><td>129.10 (n/a)</td><td>21.54 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (-3.42%)</td><td>0.12 (-8.30%)</td><td>0.11 (-11.25%)</td><td>0.09 (-13.49%)</td><td>0.02 (+5.94%)</td><td>197.60 (+15.56%)</td><td>162.14 (+9.54%)</td><td>165.20 (+12.69%)</td><td>133.80 (+3.48%)</td><td>24.34 <b>(+28.20%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>171.00 (n/a)</td><td>148.02 (n/a)</td><td>146.60 (n/a)</td><td>129.30 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 <b>(-26.93%)</b></td><td>0.09 (-19.91%)</td><td>0.09 <b>(-24.02%)</b></td><td>0.09 (+13.54%)</td><td>0.01 <b>(-73.21%)</b></td><td>212.80 (-11.92%)</td><td>199.68 (+19.84%)</td><td>202.30 <b>(+31.62%)</b></td><td>178.10 <b>(+36.89%)</b></td><td>13.40 <b>(-69.37%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>241.60 (n/a)</td><td>166.62 (n/a)</td><td>153.70 (n/a)</td><td>130.10 (n/a)</td><td>43.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (-0.79%)</td><td>0.10 (-10.61%)</td><td>0.09 (-2.93%)</td><td>0.07 (-17.64%)</td><td>0.03 (-6.38%)</td><td>250.00 <b>(+21.42%)</b></td><td>191.44 (+12.03%)</td><td>194.10 (+3.03%)</td><td>129.30 (+0.78%)</td><td>43.42 (+13.03%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>205.90 (n/a)</td><td>170.88 (n/a)</td><td>188.40 (n/a)</td><td>128.30 (n/a)</td><td>38.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 <b>(-20.00%)</b></td><td>0.10 (+4.06%)</td><td>0.10 (+11.97%)</td><td>0.08 <b>(+27.96%)</b></td><td>0.01 <b>(-54.30%)</b></td><td>222.50 <b>(-21.85%)</b></td><td>191.22 (-8.41%)</td><td>180.60 (-10.73%)</td><td>166.00 <b>(+25.00%)</b></td><td>25.55 <b>(-53.67%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>284.70 (n/a)</td><td>208.78 (n/a)</td><td>202.30 (n/a)</td><td>132.80 (n/a)</td><td>55.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 <b>(-39.05%)</b></td><td>0.08 <b>(-27.33%)</b></td><td>0.09 (-17.05%)</td><td>0.06 <b>(-25.08%)</b></td><td>0.01 <b>(-55.03%)</b></td><td>295.50 <b>(+33.47%)</b></td><td>224.88 <b>(+34.50%)</b></td><td>210.90 <b>(+20.58%)</b></td><td>198.00 <b>(+64.04%)</b></td><td>39.85 (+2.97%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>221.40 (n/a)</td><td>167.20 (n/a)</td><td>174.90 (n/a)</td><td>120.70 (n/a)</td><td>38.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.74 (+10.69%)</td><td>0.63 (+7.96%)</td><td>0.66 (+11.13%)</td><td>0.50 (+4.42%)</td><td>0.11 <b>(+53.81%)</b></td><td>198.00 (-4.26%)</td><td>159.96 (-6.20%)</td><td>149.30 (-10.01%)</td><td>132.30 (-9.63%)</td><td>28.93 <b>(+30.16%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.67 (n/a)</td><td>0.58 (n/a)</td><td>0.59 (n/a)</td><td>0.48 (n/a)</td><td>0.07 (n/a)</td><td>206.80 (n/a)</td><td>170.54 (n/a)</td><td>165.90 (n/a)</td><td>146.40 (n/a)</td><td>22.23 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.74 (-4.09%)</td><td>0.59 (-4.19%)</td><td>0.58 (-1.12%)</td><td>0.52 (+9.12%)</td><td>0.09 (-19.09%)</td><td>190.20 (-8.38%)</td><td>170.24 (+3.35%)</td><td>170.30 (+1.13%)</td><td>132.70 (+4.24%)</td><td>23.38 <b>(-22.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.77 (n/a)</td><td>0.61 (n/a)</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.11 (n/a)</td><td>207.60 (n/a)</td><td>164.72 (n/a)</td><td>168.40 (n/a)</td><td>127.30 (n/a)</td><td>30.19 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.71 (-4.56%)</td><td>0.63 (+5.92%)</td><td>0.60 (+1.20%)</td><td>0.56 <b>(+20.41%)</b></td><td>0.07 <b>(-29.28%)</b></td><td>175.50 (-16.94%)</td><td>158.74 (-6.77%)</td><td>165.00 (-1.14%)</td><td>139.40 (+4.81%)</td><td>17.51 <b>(-38.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.74 (n/a)</td><td>0.59 (n/a)</td><td>0.59 (n/a)</td><td>0.47 (n/a)</td><td>0.10 (n/a)</td><td>211.30 (n/a)</td><td>170.26 (n/a)</td><td>166.90 (n/a)</td><td>133.00 (n/a)</td><td>28.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.53 <b>(-43.51%)</b></td><td>0.44 <b>(-36.70%)</b></td><td>0.47 <b>(-29.75%)</b></td><td>0.32 <b>(-37.09%)</b></td><td>0.08 <b>(-48.82%)</b></td><td>302.80 <b>(+58.95%)</b></td><td>229.86 <b>(+56.54%)</b></td><td>210.10 <b>(+42.34%)</b></td><td>187.10 <b>(+77.01%)</b></td><td>46.40 <b>(+47.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.93 (n/a)</td><td>0.70 (n/a)</td><td>0.67 (n/a)</td><td>0.52 (n/a)</td><td>0.16 (n/a)</td><td>190.50 (n/a)</td><td>146.84 (n/a)</td><td>147.60 (n/a)</td><td>105.70 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.64 (+10.15%)</td><td>0.50 (+9.30%)</td><td>0.48 (+1.03%)</td><td>0.42 <b>(+33.69%)</b></td><td>0.08 (-14.40%)</td><td>177.10 <b>(-25.21%)</b></td><td>151.62 (-10.46%)</td><td>154.90 (-1.02%)</td><td>115.90 (-9.17%)</td><td>22.18 <b>(-45.90%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>236.80 (n/a)</td><td>169.34 (n/a)</td><td>156.50 (n/a)</td><td>127.60 (n/a)</td><td>41.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.58 (+3.19%)</td><td>0.45 (-8.88%)</td><td>0.48 (-2.39%)</td><td>0.31 <b>(-27.50%)</b></td><td>0.10 <b>(+98.19%)</b></td><td>240.70 <b>(+37.94%)</b></td><td>172.26 (+14.14%)</td><td>152.70 (+2.48%)</td><td>127.50 (-3.12%)</td><td>44.45 <b>(+169.41%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.56 (n/a)</td><td>0.49 (n/a)</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.05 (n/a)</td><td>174.50 (n/a)</td><td>150.92 (n/a)</td><td>149.00 (n/a)</td><td>131.60 (n/a)</td><td>16.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.39 <b>(-25.73%)</b></td><td>0.35 <b>(-20.80%)</b></td><td>0.36 (-17.31%)</td><td>0.31 (-16.86%)</td><td>0.03 <b>(-47.61%)</b></td><td>241.60 <b>(+20.26%)</b></td><td>210.50 <b>(+25.21%)</b></td><td>206.80 <b>(+20.94%)</b></td><td>187.10 <b>(+34.70%)</b></td><td>20.02 (-14.19%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.06 (n/a)</td><td>200.90 (n/a)</td><td>168.12 (n/a)</td><td>171.00 (n/a)</td><td>138.90 (n/a)</td><td>23.33 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.37 <b>(-35.57%)</b></td><td>0.32 <b>(-25.50%)</b></td><td>0.35 (-12.30%)</td><td>0.22 <b>(-32.89%)</b></td><td>0.06 <b>(-33.65%)</b></td><td>341.70 <b>(+49.02%)</b></td><td>242.06 <b>(+34.49%)</b></td><td>209.90 (+14.01%)</td><td>200.60 <b>(+55.26%)</b></td><td>58.80 <b>(+57.07%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.57 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>229.30 (n/a)</td><td>179.98 (n/a)</td><td>184.10 (n/a)</td><td>129.20 (n/a)</td><td>37.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 (-2.94%)</td><td>0.25 (+4.32%)</td><td>0.24 (+10.43%)</td><td>0.20 (+5.96%)</td><td>0.04 (-16.69%)</td><td>183.20 (-5.66%)</td><td>152.60 (-4.99%)</td><td>151.50 (-9.44%)</td><td>130.00 (+3.01%)</td><td>22.93 (-19.75%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>194.20 (n/a)</td><td>160.62 (n/a)</td><td>167.30 (n/a)</td><td>126.20 (n/a)</td><td>28.57 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (-1.64%)</td><td>0.23 (+1.44%)</td><td>0.22 (-12.37%)</td><td>0.16 <b>(+29.77%)</b></td><td>0.05 <b>(-27.89%)</b></td><td>237.60 <b>(-22.96%)</b></td><td>169.10 (-7.38%)</td><td>168.00 (+14.13%)</td><td>128.80 (+1.66%)</td><td>42.78 <b>(-43.46%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>308.40 (n/a)</td><td>182.58 (n/a)</td><td>147.20 (n/a)</td><td>126.70 (n/a)</td><td>75.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.22 <b>(-28.04%)</b></td><td>0.21 (-17.58%)</td><td>0.21 <b>(-24.43%)</b></td><td>0.20 (+14.46%)</td><td>0.01 <b>(-79.23%)</b></td><td>188.90 (-12.63%)</td><td>176.52 (+15.10%)</td><td>171.70 <b>(+32.28%)</b></td><td>166.20 <b>(+38.96%)</b></td><td>11.08 <b>(-74.08%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>216.20 (n/a)</td><td>153.36 (n/a)</td><td>129.80 (n/a)</td><td>119.60 (n/a)</td><td>42.74 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (-7.16%)</td><td>0.21 (-9.51%)</td><td>0.21 (-8.35%)</td><td>0.18 (+0.20%)</td><td>0.03 <b>(-31.03%)</b></td><td>199.90 (-0.20%)</td><td>173.96 (+9.11%)</td><td>175.40 (+9.08%)</td><td>140.40 (+7.67%)</td><td>21.62 <b>(-25.65%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>200.30 (n/a)</td><td>159.44 (n/a)</td><td>160.80 (n/a)</td><td>130.40 (n/a)</td><td>29.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.30 (+7.24%)</td><td>0.22 (+5.35%)</td><td>0.21 (-2.85%)</td><td>0.17 (+9.08%)</td><td>0.05 (-3.28%)</td><td>210.80 (-8.31%)</td><td>172.58 (-6.00%)</td><td>172.10 (+2.93%)</td><td>124.80 (-6.73%)</td><td>31.34 <b>(-22.38%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>229.90 (n/a)</td><td>183.60 (n/a)</td><td>167.20 (n/a)</td><td>133.80 (n/a)</td><td>40.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 <b>(+34.41%)</b></td><td>0.23 (+18.54%)</td><td>0.22 (+17.36%)</td><td>0.19 (+18.86%)</td><td>0.04 <b>(+81.84%)</b></td><td>191.10 (-15.89%)</td><td>163.08 (-14.52%)</td><td>164.50 (-14.77%)</td><td>125.70 <b>(-25.62%)</b></td><td>28.04 (+17.62%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>227.20 (n/a)</td><td>190.78 (n/a)</td><td>193.00 (n/a)</td><td>169.00 (n/a)</td><td>23.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (-0.99%)</td><td>0.18 (-11.38%)</td><td>0.17 (-18.37%)</td><td>0.15 (-13.56%)</td><td>0.05 (+18.27%)</td><td>253.00 (+15.68%)</td><td>211.72 (+14.39%)</td><td>216.60 <b>(+22.51%)</b></td><td>141.50 (+1.00%)</td><td>42.06 <b>(+28.81%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>218.70 (n/a)</td><td>185.08 (n/a)</td><td>176.80 (n/a)</td><td>140.10 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 <b>(-34.22%)</b></td><td>0.18 (-17.86%)</td><td>0.18 (-8.73%)</td><td>0.16 (-9.00%)</td><td>0.02 <b>(-65.88%)</b></td><td>230.90 (+9.90%)</td><td>209.94 (+18.09%)</td><td>208.10 (+9.53%)</td><td>181.90 <b>(+52.09%)</b></td><td>20.91 <b>(-39.42%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>210.10 (n/a)</td><td>177.78 (n/a)</td><td>190.00 (n/a)</td><td>119.60 (n/a)</td><td>34.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (+5.71%)</td><td>0.24 (+17.86%)</td><td>0.24 (+16.75%)</td><td>0.19 <b>(+67.27%)</b></td><td>0.04 <b>(-27.87%)</b></td><td>215.70 <b>(-40.22%)</b></td><td>175.90 <b>(-20.19%)</b></td><td>168.50 (-14.34%)</td><td>139.50 (-5.42%)</td><td>31.70 <b>(-61.30%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>360.80 (n/a)</td><td>220.40 (n/a)</td><td>196.70 (n/a)</td><td>147.50 (n/a)</td><td>81.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (-16.28%)</td><td>0.24 (-7.78%)</td><td>0.26 (-3.38%)</td><td>0.21 (-1.15%)</td><td>0.03 <b>(-42.99%)</b></td><td>196.50 (+1.18%)</td><td>170.06 (+6.88%)</td><td>159.00 (+3.52%)</td><td>154.30 (+19.43%)</td><td>18.85 <b>(-31.71%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>194.20 (n/a)</td><td>159.12 (n/a)</td><td>153.60 (n/a)</td><td>129.20 (n/a)</td><td>27.60 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (-11.15%)</td><td>0.20 <b>(-27.58%)</b></td><td>0.20 <b>(-34.49%)</b></td><td>0.15 <b>(-34.22%)</b></td><td>0.05 <b>(+26.44%)</b></td><td>270.90 <b>(+52.02%)</b></td><td>210.96 <b>(+42.06%)</b></td><td>206.50 <b>(+52.62%)</b></td><td>142.30 (+12.58%)</td><td>48.00 <b>(+109.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>178.20 (n/a)</td><td>148.50 (n/a)</td><td>135.30 (n/a)</td><td>126.40 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (-17.61%)</td><td>0.23 (-13.42%)</td><td>0.24 (-13.08%)</td><td>0.20 (+1.97%)</td><td>0.02 <b>(-51.14%)</b></td><td>208.30 (-1.93%)</td><td>177.32 (+13.10%)</td><td>172.20 (+15.03%)</td><td>157.70 <b>(+21.40%)</b></td><td>18.83 <b>(-42.32%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>212.40 (n/a)</td><td>156.78 (n/a)</td><td>149.70 (n/a)</td><td>129.90 (n/a)</td><td>32.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 <b>(-34.33%)</b></td><td>0.23 (-13.76%)</td><td>0.23 (-1.61%)</td><td>0.19 (+8.06%)</td><td>0.03 <b>(-65.77%)</b></td><td>212.70 (-7.44%)</td><td>178.32 (+8.34%)</td><td>176.30 (+1.61%)</td><td>152.00 <b>(+52.30%)</b></td><td>24.51 <b>(-50.97%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.41 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>229.80 (n/a)</td><td>164.60 (n/a)</td><td>173.50 (n/a)</td><td>99.80 (n/a)</td><td>49.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.36 (-1.32%)</td><td>0.28 (-5.37%)</td><td>0.28 (-9.22%)</td><td>0.21 (-2.27%)</td><td>0.05 (-2.30%)</td><td>192.60 (+2.34%)</td><td>151.70 (+5.54%)</td><td>148.90 (+10.13%)</td><td>112.80 (+1.35%)</td><td>28.73 (-1.21%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>188.20 (n/a)</td><td>143.74 (n/a)</td><td>135.20 (n/a)</td><td>111.30 (n/a)</td><td>29.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 <b>(-20.16%)</b></td><td>0.22 <b>(-23.75%)</b></td><td>0.21 <b>(-30.41%)</b></td><td>0.18 (-13.63%)</td><td>0.04 <b>(-32.01%)</b></td><td>232.60 (+15.78%)</td><td>191.40 <b>(+29.59%)</b></td><td>192.90 <b>(+43.63%)</b></td><td>148.00 <b>(+25.21%)</b></td><td>30.24 (-5.87%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>200.90 (n/a)</td><td>147.70 (n/a)</td><td>134.30 (n/a)</td><td>118.20 (n/a)</td><td>32.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (-12.14%)</td><td>0.22 (-18.71%)</td><td>0.21 <b>(-24.11%)</b></td><td>0.18 (-13.39%)</td><td>0.03 (-5.91%)</td><td>226.30 (+15.46%)</td><td>193.86 <b>(+23.24%)</b></td><td>197.20 <b>(+31.73%)</b></td><td>151.40 (+13.75%)</td><td>28.38 (+19.28%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>196.00 (n/a)</td><td>157.30 (n/a)</td><td>149.70 (n/a)</td><td>133.10 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (-0.76%)</td><td>0.23 (+5.59%)</td><td>0.21 (+3.33%)</td><td>0.17 (-9.57%)</td><td>0.05 <b>(+26.47%)</b></td><td>199.10 (+10.61%)</td><td>154.94 (-3.67%)</td><td>167.70 (-3.23%)</td><td>119.20 (+0.76%)</td><td>34.93 <b>(+32.93%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>180.00 (n/a)</td><td>160.84 (n/a)</td><td>173.30 (n/a)</td><td>118.30 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.31 (-1.81%)</td><td>0.23 (+6.91%)</td><td>0.20 (-9.35%)</td><td>0.16 <b>(+62.00%)</b></td><td>0.06 <b>(-27.73%)</b></td><td>213.90 <b>(-38.27%)</b></td><td>162.88 (-15.96%)</td><td>170.50 (+10.28%)</td><td>112.60 (+1.81%)</td><td>42.09 <b>(-55.98%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>346.50 (n/a)</td><td>193.82 (n/a)</td><td>154.60 (n/a)</td><td>110.60 (n/a)</td><td>95.60 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (-9.22%)</td><td>0.19 <b>(-21.82%)</b></td><td>0.18 <b>(-29.72%)</b></td><td>0.15 <b>(-23.97%)</b></td><td>0.04 (+8.95%)</td><td>232.70 <b>(+31.47%)</b></td><td>187.46 <b>(+29.71%)</b></td><td>190.30 <b>(+42.23%)</b></td><td>136.30 (+10.19%)</td><td>37.48 <b>(+57.58%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>177.00 (n/a)</td><td>144.52 (n/a)</td><td>133.80 (n/a)</td><td>123.70 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 (+3.78%)</td><td>0.21 (-11.56%)</td><td>0.20 <b>(-20.22%)</b></td><td>0.18 (+4.61%)</td><td>0.04 (+5.50%)</td><td>190.80 (-4.41%)</td><td>169.08 (+13.01%)</td><td>174.30 <b>(+25.40%)</b></td><td>123.20 (-3.67%)</td><td>27.14 (-6.80%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>199.60 (n/a)</td><td>149.62 (n/a)</td><td>139.00 (n/a)</td><td>127.90 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.34 <b>(+27.03%)</b></td><td>0.23 (-1.26%)</td><td>0.23 (-11.57%)</td><td>0.15 (-12.89%)</td><td>0.07 <b>(+63.44%)</b></td><td>230.00 (+14.77%)</td><td>160.24 (+5.19%)</td><td>154.20 (+13.13%)</td><td>101.80 <b>(-21.27%)</b></td><td>45.89 <b>(+48.64%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>200.40 (n/a)</td><td>152.34 (n/a)</td><td>136.30 (n/a)</td><td>129.30 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (+3.72%)</td><td>0.19 (-2.97%)</td><td>0.19 (-1.90%)</td><td>0.14 <b>(-21.57%)</b></td><td>0.03 <b>(+111.71%)</b></td><td>242.70 <b>(+27.54%)</b></td><td>184.56 (+5.45%)</td><td>178.60 (+1.94%)</td><td>149.40 (-3.55%)</td><td>36.27 <b>(+164.12%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>190.30 (n/a)</td><td>175.02 (n/a)</td><td>175.20 (n/a)</td><td>154.90 (n/a)</td><td>13.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 <b>(-32.78%)</b></td><td>0.18 (-19.09%)</td><td>0.19 (-12.52%)</td><td>0.15 (-9.55%)</td><td>0.02 <b>(-68.71%)</b></td><td>229.90 (+10.58%)</td><td>191.60 (+17.95%)</td><td>187.10 (+14.29%)</td><td>174.00 <b>(+48.72%)</b></td><td>22.13 <b>(-47.24%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>207.90 (n/a)</td><td>162.44 (n/a)</td><td>163.70 (n/a)</td><td>117.00 (n/a)</td><td>41.94 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 <b>(-34.57%)</b></td><td>0.16 <b>(-29.02%)</b></td><td>0.15 <b>(-39.33%)</b></td><td>0.14 (-8.72%)</td><td>0.03 <b>(-55.95%)</b></td><td>248.30 (+9.53%)</td><td>218.58 <b>(+34.49%)</b></td><td>235.60 <b>(+64.87%)</b></td><td>164.60 <b>(+52.83%)</b></td><td>34.25 <b>(-28.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>226.70 (n/a)</td><td>162.52 (n/a)</td><td>142.90 (n/a)</td><td>107.70 (n/a)</td><td>47.79 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.91 (+1.97%)</td><td>0.82 (+6.32%)</td><td>0.83 (+8.81%)</td><td>0.73 (+4.77%)</td><td>0.06 (-9.88%)</td><td>179.70 (-4.52%)</td><td>159.80 (-6.07%)</td><td>158.40 (-8.07%)</td><td>144.20 (-1.97%)</td><td>12.79 (-13.18%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.89 (n/a)</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.70 (n/a)</td><td>0.07 (n/a)</td><td>188.20 (n/a)</td><td>170.12 (n/a)</td><td>172.30 (n/a)</td><td>147.10 (n/a)</td><td>14.74 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.99 (-12.99%)</td><td>0.77 (-12.56%)</td><td>0.70 <b>(-22.25%)</b></td><td>0.65 (+6.12%)</td><td>0.14 <b>(-28.19%)</b></td><td>202.50 (-5.77%)</td><td>174.40 (+12.27%)</td><td>186.80 <b>(+28.56%)</b></td><td>132.60 (+14.90%)</td><td>27.44 <b>(-25.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.14 (n/a)</td><td>0.88 (n/a)</td><td>0.90 (n/a)</td><td>0.61 (n/a)</td><td>0.19 (n/a)</td><td>214.90 (n/a)</td><td>155.34 (n/a)</td><td>145.30 (n/a)</td><td>115.40 (n/a)</td><td>36.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.06 (+13.29%)</td><td>0.83 (+6.50%)</td><td>0.85 (+8.77%)</td><td>0.59 (-7.50%)</td><td>0.18 <b>(+53.77%)</b></td><td>220.90 (+8.13%)</td><td>163.46 (-4.05%)</td><td>153.60 (-8.02%)</td><td>124.10 (-11.74%)</td><td>37.36 <b>(+48.45%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.93 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.64 (n/a)</td><td>0.11 (n/a)</td><td>204.30 (n/a)</td><td>170.36 (n/a)</td><td>167.00 (n/a)</td><td>140.60 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+1.44%)</td><td>0.03 (+10.77%)</td><td>0.03 (+9.71%)</td><td>0.02 (+12.46%)</td><td>0.00 (-7.16%)</td><td>182.10 (-11.08%)</td><td>157.84 (-10.15%)</td><td>163.60 (-8.86%)</td><td>133.10 (-1.41%)</td><td>21.65 (-18.26%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.80 (n/a)</td><td>175.68 (n/a)</td><td>179.50 (n/a)</td><td>135.00 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+11.69%)</td><td>0.02 (-4.33%)</td><td>0.02 (-9.36%)</td><td>0.02 (-11.06%)</td><td>0.01 <b>(+53.42%)</b></td><td>239.10 (+12.41%)</td><td>187.22 (+6.86%)</td><td>188.80 (+10.34%)</td><td>135.60 (-10.50%)</td><td>40.17 <b>(+55.94%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.70 (n/a)</td><td>175.20 (n/a)</td><td>171.10 (n/a)</td><td>151.50 (n/a)</td><td>25.76 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+16.25%)</td><td>0.02 (+3.16%)</td><td>0.02 (-0.54%)</td><td>0.02 <b>(+23.04%)</b></td><td>0.01 (+5.05%)</td><td>188.10 (-18.75%)</td><td>169.50 (-3.87%)</td><td>179.70 (+0.56%)</td><td>117.40 (-13.99%)</td><td>29.69 <b>(-25.25%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>176.32 (n/a)</td><td>178.70 (n/a)</td><td>136.50 (n/a)</td><td>39.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>17.46 <b>(+25.39%)</b></td><td>14.67 (+19.96%)</td><td>15.25 (+16.41%)</td><td>11.55 <b>(+37.88%)</b></td><td>2.67 (+19.32%)</td><td>181.60 <b>(-27.48%)</b></td><td>147.02 (-17.21%)</td><td>137.60 (-14.11%)</td><td>120.10 <b>(-20.31%)</b></td><td>27.91 <b>(-32.61%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.93 (n/a)</td><td>12.23 (n/a)</td><td>13.10 (n/a)</td><td>8.38 (n/a)</td><td>2.24 (n/a)</td><td>250.40 (n/a)</td><td>177.58 (n/a)</td><td>160.20 (n/a)</td><td>150.70 (n/a)</td><td>41.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.03 (+6.46%)</td><td>0.89 (+5.93%)</td><td>0.97 (+19.47%)</td><td>0.72 (-7.01%)</td><td>0.15 <b>(+86.30%)</b></td><td>183.50 (+7.50%)</td><td>152.64 (-4.00%)</td><td>136.80 (-16.33%)</td><td>127.80 (-6.03%)</td><td>26.53 <b>(+94.65%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.97 (n/a)</td><td>0.84 (n/a)</td><td>0.81 (n/a)</td><td>0.77 (n/a)</td><td>0.08 (n/a)</td><td>170.70 (n/a)</td><td>159.00 (n/a)</td><td>163.50 (n/a)</td><td>136.00 (n/a)</td><td>13.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.18 (+8.68%)</td><td>0.82 (-9.41%)</td><td>0.76 (-16.57%)</td><td>0.62 (-9.02%)</td><td>0.22 <b>(+42.82%)</b></td><td>212.10 (+9.95%)</td><td>168.90 (+12.93%)</td><td>172.80 (+19.83%)</td><td>112.00 (-7.97%)</td><td>37.51 <b>(+37.62%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.09 (n/a)</td><td>0.90 (n/a)</td><td>0.92 (n/a)</td><td>0.68 (n/a)</td><td>0.15 (n/a)</td><td>192.90 (n/a)</td><td>149.56 (n/a)</td><td>144.20 (n/a)</td><td>121.70 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.90 (-4.85%)</td><td>0.76 (-4.71%)</td><td>0.75 (-4.65%)</td><td>0.67 (+4.39%)</td><td>0.09 <b>(-32.45%)</b></td><td>197.30 (-4.22%)</td><td>175.74 (+3.74%)</td><td>176.60 (+4.87%)</td><td>146.80 (+5.08%)</td><td>18.77 <b>(-32.33%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.95 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.64 (n/a)</td><td>0.13 (n/a)</td><td>206.00 (n/a)</td><td>169.40 (n/a)</td><td>168.40 (n/a)</td><td>139.70 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.14 (+9.66%)</td><td>0.80 (-3.22%)</td><td>0.81 (+4.78%)</td><td>0.53 <b>(-28.26%)</b></td><td>0.24 <b>(+91.56%)</b></td><td>250.00 <b>(+39.35%)</b></td><td>176.98 (+9.50%)</td><td>163.30 (-4.56%)</td><td>116.20 (-8.79%)</td><td>54.03 <b>(+145.07%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.04 (n/a)</td><td>0.83 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.13 (n/a)</td><td>179.40 (n/a)</td><td>161.62 (n/a)</td><td>171.10 (n/a)</td><td>127.40 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.96 (-6.90%)</td><td>0.82 (+0.91%)</td><td>0.88 (+16.00%)</td><td>0.68 (+15.24%)</td><td>0.13 <b>(-27.48%)</b></td><td>195.50 (-13.23%)</td><td>164.68 (-2.79%)</td><td>150.90 (-13.82%)</td><td>137.30 (+7.43%)</td><td>27.04 <b>(-29.53%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.03 (n/a)</td><td>0.81 (n/a)</td><td>0.75 (n/a)</td><td>0.59 (n/a)</td><td>0.18 (n/a)</td><td>225.30 (n/a)</td><td>169.40 (n/a)</td><td>175.10 (n/a)</td><td>127.80 (n/a)</td><td>38.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 <b>(-27.65%)</b></td><td>0.02 <b>(-25.68%)</b></td><td>0.02 <b>(-27.59%)</b></td><td>0.02 <b>(-24.62%)</b></td><td>0.00 <b>(-45.38%)</b></td><td>234.40 <b>(+32.65%)</b></td><td>193.88 <b>(+32.94%)</b></td><td>191.30 <b>(+38.12%)</b></td><td>160.90 <b>(+38.23%)</b></td><td>26.22 (-1.17%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>176.70 (n/a)</td><td>145.84 (n/a)</td><td>138.50 (n/a)</td><td>116.40 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (+15.82%)</td><td>0.03 <b>(+21.88%)</b></td><td>0.03 (+19.55%)</td><td>0.02 <b>(+40.59%)</b></td><td>0.00 (-3.94%)</td><td>166.10 <b>(-28.90%)</b></td><td>147.48 (-18.85%)</td><td>150.80 (-16.36%)</td><td>123.10 (-13.67%)</td><td>19.75 <b>(-40.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.60 (n/a)</td><td>181.74 (n/a)</td><td>180.30 (n/a)</td><td>142.60 (n/a)</td><td>33.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.00 (+0.00%)</td><td>0.00 (-0.94%)</td><td>0.00 (-2.33%)</td><td>0.00 (+0.00%)</td><td>0.00 (+5.89%)</td><td>1012.45 (+0.05%)</td><td>968.79 (+1.13%)</td><td>968.69 (+1.40%)</td><td>916.70 (+1.35%)</td><td>39.43 (+2.84%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1011.98 (n/a)</td><td>957.96 (n/a)</td><td>955.36 (n/a)</td><td>904.46 (n/a)</td><td>38.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.01 (+1.19%)</td><td>0.01 (+1.50%)</td><td>0.01 (+2.47%)</td><td>0.01 (-2.70%)</td><td>0.00 <b>(+43.24%)</b></td><td>1133.19 (+2.10%)</td><td>1013.40 (-1.58%)</td><td>990.30 (-2.64%)</td><td>967.55 (-1.08%)</td><td>67.85 <b>(+39.50%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1109.84 (n/a)</td><td>1029.68 (n/a)</td><td>1017.14 (n/a)</td><td>978.12 (n/a)</td><td>48.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.97 (-3.05%)</td><td>0.95 (-1.45%)</td><td>0.95 (-1.25%)</td><td>0.94 (-0.79%)</td><td>0.01 <b>(-47.83%)</b></td><td>2230.65 (+0.80%)</td><td>2200.07 (+1.46%)</td><td>2203.86 (+1.26%)</td><td>2171.44 (+3.15%)</td><td>22.02 <b>(-45.54%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.00 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2212.87 (n/a)</td><td>2168.52 (n/a)</td><td>2176.37 (n/a)</td><td>2105.11 (n/a)</td><td>40.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.76 (-1.08%)</td><td>5.11 (+7.59%)</td><td>5.34 (+14.48%)</td><td>4.06 (+3.98%)</td><td>0.65 (-6.99%)</td><td>258.40 (-3.83%)</td><td>208.38 (-7.25%)</td><td>196.20 (-12.64%)</td><td>182.10 (+1.11%)</td><td>29.70 (-6.45%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.82 (n/a)</td><td>4.75 (n/a)</td><td>4.67 (n/a)</td><td>3.90 (n/a)</td><td>0.70 (n/a)</td><td>268.70 (n/a)</td><td>224.66 (n/a)</td><td>224.60 (n/a)</td><td>180.10 (n/a)</td><td>31.75 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.79 (+18.20%)</td><td>4.83 (+4.32%)</td><td>5.20 (+11.81%)</td><td>2.97 <b>(-29.94%)</b></td><td>1.14 <b>(+316.03%)</b></td><td>352.60 <b>(+42.75%)</b></td><td>230.28 (+1.44%)</td><td>201.70 (-10.55%)</td><td>181.20 (-15.41%)</td><td>71.02 <b>(+415.74%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>4.90 (n/a)</td><td>4.63 (n/a)</td><td>4.65 (n/a)</td><td>4.24 (n/a)</td><td>0.28 (n/a)</td><td>247.00 (n/a)</td><td>227.02 (n/a)</td><td>225.50 (n/a)</td><td>214.20 (n/a)</td><td>13.77 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.98 (+4.53%)</td><td>5.27 (+1.15%)</td><td>5.02 (-6.36%)</td><td>4.69 (+1.45%)</td><td>0.65 <b>(+50.73%)</b></td><td>223.80 (-1.41%)</td><td>201.48 (-0.52%)</td><td>209.10 (+6.79%)</td><td>175.30 (-4.36%)</td><td>24.11 <b>(+40.55%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.72 (n/a)</td><td>5.21 (n/a)</td><td>5.36 (n/a)</td><td>4.62 (n/a)</td><td>0.43 (n/a)</td><td>227.00 (n/a)</td><td>202.54 (n/a)</td><td>195.80 (n/a)</td><td>183.30 (n/a)</td><td>17.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>6.10 (+4.58%)</td><td>5.12 (+0.29%)</td><td>5.23 (+1.08%)</td><td>3.88 (-11.65%)</td><td>0.83 <b>(+53.81%)</b></td><td>270.10 (+13.20%)</td><td>209.78 (+1.16%)</td><td>200.40 (-1.04%)</td><td>172.00 (-4.34%)</td><td>37.60 <b>(+68.80%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.83 (n/a)</td><td>5.10 (n/a)</td><td>5.18 (n/a)</td><td>4.39 (n/a)</td><td>0.54 (n/a)</td><td>238.60 (n/a)</td><td>207.38 (n/a)</td><td>202.50 (n/a)</td><td>179.80 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.58 (-4.07%)</td><td>7.81 (-5.67%)</td><td>8.15 (-5.60%)</td><td>6.39 (-15.02%)</td><td>0.86 <b>(+28.52%)</b></td><td>328.40 (+17.66%)</td><td>271.50 (+6.59%)</td><td>257.30 (+5.93%)</td><td>244.30 (+4.22%)</td><td>33.39 <b>(+59.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.95 (n/a)</td><td>8.28 (n/a)</td><td>8.63 (n/a)</td><td>7.51 (n/a)</td><td>0.67 (n/a)</td><td>279.10 (n/a)</td><td>254.72 (n/a)</td><td>242.90 (n/a)</td><td>234.40 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.66 (-4.97%)</td><td>8.06 (-4.42%)</td><td>8.49 (+0.82%)</td><td>7.18 (-1.16%)</td><td>0.70 (-6.62%)</td><td>292.00 (+1.18%)</td><td>261.76 (+4.58%)</td><td>246.90 (-0.80%)</td><td>242.00 (+5.22%)</td><td>23.58 (-0.63%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.12 (n/a)</td><td>8.43 (n/a)</td><td>8.42 (n/a)</td><td>7.27 (n/a)</td><td>0.75 (n/a)</td><td>288.60 (n/a)</td><td>250.30 (n/a)</td><td>248.90 (n/a)</td><td>230.00 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>9.56 (+7.13%)</td><td>8.15 (-3.17%)</td><td>7.82 (-9.99%)</td><td>6.93 (-11.72%)</td><td>1.12 <b>(+121.16%)</b></td><td>302.80 (+13.28%)</td><td>261.20 (+4.52%)</td><td>268.00 (+11.11%)</td><td>219.30 (-6.64%)</td><td>35.08 <b>(+129.63%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>8.93 (n/a)</td><td>8.42 (n/a)</td><td>8.69 (n/a)</td><td>7.84 (n/a)</td><td>0.51 (n/a)</td><td>267.30 (n/a)</td><td>249.90 (n/a)</td><td>241.20 (n/a)</td><td>234.90 (n/a)</td><td>15.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>9.96 (+4.32%)</td><td>8.84 (-0.08%)</td><td>9.38 (+6.64%)</td><td>7.13 (-13.59%)</td><td>1.20 <b>(+160.21%)</b></td><td>294.20 (+15.74%)</td><td>241.02 (+1.49%)</td><td>223.50 (-6.21%)</td><td>210.70 (-4.14%)</td><td>35.41 <b>(+189.00%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.54 (n/a)</td><td>8.85 (n/a)</td><td>8.80 (n/a)</td><td>8.25 (n/a)</td><td>0.46 (n/a)</td><td>254.20 (n/a)</td><td>237.48 (n/a)</td><td>238.30 (n/a)</td><td>219.80 (n/a)</td><td>12.25 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>10.87 (+8.43%)</td><td>9.05 (+7.19%)</td><td>9.27 (+10.16%)</td><td>7.28 (+7.14%)</td><td>1.35 (+16.55%)</td><td>287.90 (-6.68%)</td><td>235.88 (-6.46%)</td><td>226.30 (-9.19%)</td><td>193.00 (-7.79%)</td><td>36.04 (-0.22%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>10.02 (n/a)</td><td>8.45 (n/a)</td><td>8.41 (n/a)</td><td>6.80 (n/a)</td><td>1.16 (n/a)</td><td>308.50 (n/a)</td><td>252.18 (n/a)</td><td>249.20 (n/a)</td><td>209.30 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>10.65 (+5.69%)</td><td>9.25 (+17.68%)</td><td>9.64 <b>(+20.34%)</b></td><td>7.91 <b>(+32.93%)</b></td><td>1.21 <b>(-22.81%)</b></td><td>265.20 <b>(-24.77%)</b></td><td>229.98 (-16.53%)</td><td>217.50 (-16.89%)</td><td>196.90 (-5.38%)</td><td>30.82 <b>(-44.15%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>10.08 (n/a)</td><td>7.86 (n/a)</td><td>8.01 (n/a)</td><td>5.95 (n/a)</td><td>1.57 (n/a)</td><td>352.50 (n/a)</td><td>275.52 (n/a)</td><td>261.70 (n/a)</td><td>208.10 (n/a)</td><td>55.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>12.16 (-2.52%)</td><td>11.11 (+3.91%)</td><td>10.73 (+5.85%)</td><td>10.41 (+5.76%)</td><td>0.83 <b>(-22.88%)</b></td><td>402.80 (-5.45%)</td><td>379.10 (-4.06%)</td><td>390.80 (-5.54%)</td><td>344.90 (+2.59%)</td><td>27.61 <b>(-24.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>12.48 (n/a)</td><td>10.69 (n/a)</td><td>10.14 (n/a)</td><td>9.85 (n/a)</td><td>1.08 (n/a)</td><td>426.00 (n/a)</td><td>395.14 (n/a)</td><td>413.70 (n/a)</td><td>336.20 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>12.95 (+0.83%)</td><td>11.83 (+2.37%)</td><td>11.92 (-1.38%)</td><td>10.88 (+11.89%)</td><td>0.76 <b>(-42.33%)</b></td><td>385.60 (-10.64%)</td><td>355.56 (-3.07%)</td><td>351.80 (+1.41%)</td><td>324.00 (-0.83%)</td><td>22.59 <b>(-48.97%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>12.84 (n/a)</td><td>11.56 (n/a)</td><td>12.09 (n/a)</td><td>9.72 (n/a)</td><td>1.32 (n/a)</td><td>431.50 (n/a)</td><td>366.84 (n/a)</td><td>346.90 (n/a)</td><td>326.70 (n/a)</td><td>44.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>11.67 (-10.85%)</td><td>11.22 (-6.55%)</td><td>11.13 (-5.70%)</td><td>11.06 (-2.54%)</td><td>0.25 <b>(-63.86%)</b></td><td>379.20 (+2.63%)</td><td>373.94 (+6.78%)</td><td>377.00 (+6.05%)</td><td>359.40 (+12.17%)</td><td>8.22 <b>(-58.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>13.09 (n/a)</td><td>12.01 (n/a)</td><td>11.80 (n/a)</td><td>11.35 (n/a)</td><td>0.70 (n/a)</td><td>369.50 (n/a)</td><td>350.20 (n/a)</td><td>355.50 (n/a)</td><td>320.40 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.86 (-3.10%)</td><td>13.44 (+0.67%)</td><td>13.67 (+4.77%)</td><td>12.31 (-2.80%)</td><td>0.65 (-7.14%)</td><td>340.80 (+2.87%)</td><td>312.58 (-0.69%)</td><td>306.80 (-4.57%)</td><td>302.60 (+3.17%)</td><td>15.99 (-0.59%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>14.30 (n/a)</td><td>13.35 (n/a)</td><td>13.05 (n/a)</td><td>12.66 (n/a)</td><td>0.70 (n/a)</td><td>331.30 (n/a)</td><td>314.76 (n/a)</td><td>321.50 (n/a)</td><td>293.30 (n/a)</td><td>16.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.45 (-4.15%)</td><td>12.87 (-5.61%)</td><td>13.16 (-8.12%)</td><td>10.83 (-4.15%)</td><td>1.39 (-13.87%)</td><td>387.30 (+4.31%)</td><td>329.18 (+5.70%)</td><td>318.70 (+8.85%)</td><td>290.30 (+4.31%)</td><td>37.58 (-4.98%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>15.07 (n/a)</td><td>13.63 (n/a)</td><td>14.33 (n/a)</td><td>11.30 (n/a)</td><td>1.61 (n/a)</td><td>371.30 (n/a)</td><td>311.42 (n/a)</td><td>292.80 (n/a)</td><td>278.30 (n/a)</td><td>39.55 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.37 (-0.43%)</td><td>13.00 (-0.88%)</td><td>12.78 (-3.29%)</td><td>12.23 (+8.26%)</td><td>0.83 <b>(-30.93%)</b></td><td>342.90 (-7.65%)</td><td>323.52 (+0.49%)</td><td>328.20 (+3.40%)</td><td>291.80 (+0.45%)</td><td>19.47 <b>(-37.25%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>14.44 (n/a)</td><td>13.12 (n/a)</td><td>13.21 (n/a)</td><td>11.30 (n/a)</td><td>1.20 (n/a)</td><td>371.30 (n/a)</td><td>321.94 (n/a)</td><td>317.40 (n/a)</td><td>290.50 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>15.19 (+3.01%)</td><td>13.69 (+0.14%)</td><td>13.43 (-3.02%)</td><td>12.86 (+4.09%)</td><td>0.93 (+7.65%)</td><td>326.20 (-3.95%)</td><td>307.52 (-0.12%)</td><td>312.30 (+3.10%)</td><td>276.10 (-2.92%)</td><td>19.89 (-1.04%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>14.75 (n/a)</td><td>13.67 (n/a)</td><td>13.85 (n/a)</td><td>12.35 (n/a)</td><td>0.87 (n/a)</td><td>339.60 (n/a)</td><td>307.90 (n/a)</td><td>302.90 (n/a)</td><td>284.40 (n/a)</td><td>20.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.09 (-3.96%)</td><td>12.30 (-6.43%)</td><td>12.85 (-0.77%)</td><td>9.80 (-18.99%)</td><td>1.71 <b>(+75.48%)</b></td><td>428.00 <b>(+23.41%)</b></td><td>346.78 (+8.24%)</td><td>326.40 (+0.80%)</td><td>297.60 (+4.13%)</td><td>52.30 <b>(+128.91%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>14.68 (n/a)</td><td>13.15 (n/a)</td><td>12.95 (n/a)</td><td>12.10 (n/a)</td><td>0.97 (n/a)</td><td>346.80 (n/a)</td><td>320.38 (n/a)</td><td>323.80 (n/a)</td><td>285.80 (n/a)</td><td>22.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>3.44 (+11.57%)</td><td>2.91 (+5.46%)</td><td>3.02 (+13.50%)</td><td>2.46 (-3.45%)</td><td>0.40 <b>(+90.45%)</b></td><td>213.50 (+3.59%)</td><td>183.12 (-4.14%)</td><td>173.50 (-11.88%)</td><td>152.30 (-10.41%)</td><td>25.25 <b>(+81.46%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.08 (n/a)</td><td>2.76 (n/a)</td><td>2.66 (n/a)</td><td>2.54 (n/a)</td><td>0.21 (n/a)</td><td>206.10 (n/a)</td><td>191.02 (n/a)</td><td>196.90 (n/a)</td><td>170.00 (n/a)</td><td>13.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.93 (+6.35%)</td><td>4.98 (-3.96%)</td><td>4.75 (-5.94%)</td><td>4.65 (-5.21%)</td><td>0.54 <b>(+87.24%)</b></td><td>225.50 (+5.52%)</td><td>212.44 (+4.75%)</td><td>220.60 (+6.31%)</td><td>176.70 (-6.01%)</td><td>20.39 <b>(+84.51%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>5.58 (n/a)</td><td>5.18 (n/a)</td><td>5.05 (n/a)</td><td>4.91 (n/a)</td><td>0.29 (n/a)</td><td>213.70 (n/a)</td><td>202.80 (n/a)</td><td>207.50 (n/a)</td><td>188.00 (n/a)</td><td>11.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.85 (-2.74%)</td><td>8.23 (+1.94%)</td><td>8.70 (+8.61%)</td><td>7.28 (+1.16%)</td><td>0.74 (+0.41%)</td><td>287.90 (-1.13%)</td><td>256.38 (-1.88%)</td><td>241.10 (-7.91%)</td><td>236.90 (+2.82%)</td><td>23.88 (+1.64%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>9.10 (n/a)</td><td>8.08 (n/a)</td><td>8.01 (n/a)</td><td>7.20 (n/a)</td><td>0.74 (n/a)</td><td>291.20 (n/a)</td><td>261.28 (n/a)</td><td>261.80 (n/a)</td><td>230.40 (n/a)</td><td>23.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>3.70 (+5.10%)</td><td>2.82 (-9.28%)</td><td>2.76 (-14.51%)</td><td>2.08 <b>(-20.53%)</b></td><td>0.58 <b>(+42.70%)</b></td><td>251.80 <b>(+25.84%)</b></td><td>192.48 (+12.40%)</td><td>189.60 (+16.96%)</td><td>141.80 (-4.83%)</td><td>39.76 <b>(+69.92%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>3.52 (n/a)</td><td>3.11 (n/a)</td><td>3.23 (n/a)</td><td>2.62 (n/a)</td><td>0.41 (n/a)</td><td>200.10 (n/a)</td><td>171.24 (n/a)</td><td>162.10 (n/a)</td><td>149.00 (n/a)</td><td>23.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 <b>(+27.20%)</b></td><td>0.21 (+17.49%)</td><td>0.19 (+11.29%)</td><td>0.17 (+19.58%)</td><td>0.04 <b>(+54.90%)</b></td><td>188.70 (-16.36%)</td><td>163.42 (-14.10%)</td><td>170.20 (-10.14%)</td><td>121.90 <b>(-21.35%)</b></td><td>26.93 (+1.50%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>225.60 (n/a)</td><td>190.24 (n/a)</td><td>189.40 (n/a)</td><td>155.00 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (-12.84%)</td><td>0.17 (-5.06%)</td><td>0.18 (-6.95%)</td><td>0.14 (+11.58%)</td><td>0.03 <b>(-32.32%)</b></td><td>233.90 (-10.38%)</td><td>194.42 (+2.46%)</td><td>178.60 (+7.46%)</td><td>160.50 (+14.72%)</td><td>35.91 <b>(-29.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>261.00 (n/a)</td><td>189.76 (n/a)</td><td>166.20 (n/a)</td><td>139.90 (n/a)</td><td>50.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.50 (-1.05%)</td><td>0.40 (+1.44%)</td><td>0.36 (-1.82%)</td><td>0.33 (+1.74%)</td><td>0.08 (+4.43%)</td><td>196.70 (-1.70%)</td><td>167.20 (-1.22%)</td><td>184.00 (+1.88%)</td><td>131.40 (+1.08%)</td><td>31.61 (+1.94%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>200.10 (n/a)</td><td>169.26 (n/a)</td><td>180.60 (n/a)</td><td>130.00 (n/a)</td><td>31.01 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.45 (+14.39%)</td><td>0.39 (+16.33%)</td><td>0.39 (+17.56%)</td><td>0.35 <b>(+37.00%)</b></td><td>0.04 <b>(-32.32%)</b></td><td>187.40 <b>(-27.02%)</b></td><td>167.32 (-15.54%)</td><td>166.60 (-14.96%)</td><td>145.00 (-12.55%)</td><td>16.01 <b>(-56.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>256.80 (n/a)</td><td>198.10 (n/a)</td><td>195.90 (n/a)</td><td>165.80 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.42 <b>(-28.17%)</b></td><td>0.36 (-6.87%)</td><td>0.35 <b>(+21.54%)</b></td><td>0.32 (+18.10%)</td><td>0.04 <b>(-73.36%)</b></td><td>202.30 (-15.32%)</td><td>183.92 (-2.76%)</td><td>187.50 (-17.76%)</td><td>157.30 <b>(+39.20%)</b></td><td>19.48 <b>(-69.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.58 (n/a)</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>238.90 (n/a)</td><td>189.14 (n/a)</td><td>228.00 (n/a)</td><td>113.00 (n/a)</td><td>63.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.03 <b>(-31.26%)</b></td><td>0.88 (-6.93%)</td><td>0.95 (+13.23%)</td><td>0.66 (-4.77%)</td><td>0.16 <b>(-48.60%)</b></td><td>197.70 (+4.99%)</td><td>154.18 (+3.45%)</td><td>138.30 (-11.69%)</td><td>127.80 <b>(+45.39%)</b></td><td>30.96 (-16.60%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.49 (n/a)</td><td>0.94 (n/a)</td><td>0.84 (n/a)</td><td>0.70 (n/a)</td><td>0.31 (n/a)</td><td>188.30 (n/a)</td><td>149.04 (n/a)</td><td>156.60 (n/a)</td><td>87.90 (n/a)</td><td>37.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.77 <b>(-41.83%)</b></td><td>0.73 (-17.54%)</td><td>0.73 (+1.68%)</td><td>0.64 (+9.01%)</td><td>0.05 <b>(-84.69%)</b></td><td>203.80 (-8.24%)</td><td>181.16 (+9.17%)</td><td>178.60 (-1.65%)</td><td>169.30 <b>(+71.88%)</b></td><td>13.70 <b>(-75.88%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.33 (n/a)</td><td>0.88 (n/a)</td><td>0.72 (n/a)</td><td>0.59 (n/a)</td><td>0.34 (n/a)</td><td>222.10 (n/a)</td><td>165.94 (n/a)</td><td>181.60 (n/a)</td><td>98.50 (n/a)</td><td>56.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.02 <b>(-25.79%)</b></td><td>0.77 (-0.68%)</td><td>0.72 (-3.35%)</td><td>0.65 <b>(+57.06%)</b></td><td>0.14 <b>(-60.66%)</b></td><td>200.40 <b>(-36.32%)</b></td><td>173.32 (-11.43%)</td><td>181.80 (+3.47%)</td><td>128.70 <b>(+34.76%)</b></td><td>26.91 <b>(-66.62%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>1.37 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>314.70 (n/a)</td><td>195.68 (n/a)</td><td>175.70 (n/a)</td><td>95.50 (n/a)</td><td>80.61 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.89 <b>(+24.68%)</b></td><td>0.68 (+12.03%)</td><td>0.64 (+2.43%)</td><td>0.44 (-12.83%)</td><td>0.19 <b>(+105.28%)</b></td><td>301.20 (+14.70%)</td><td>204.96 (-6.39%)</td><td>203.50 (-2.35%)</td><td>147.60 (-19.83%)</td><td>61.58 <b>(+84.06%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.71 (n/a)</td><td>0.61 (n/a)</td><td>0.63 (n/a)</td><td>0.50 (n/a)</td><td>0.09 (n/a)</td><td>262.60 (n/a)</td><td>218.96 (n/a)</td><td>208.40 (n/a)</td><td>184.10 (n/a)</td><td>33.46 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (-5.59%)</td><td>0.08 (-19.10%)</td><td>0.09 (-15.84%)</td><td>0.07 <b>(-32.80%)</b></td><td>0.02 <b>(+177.50%)</b></td><td>245.00 <b>(+48.85%)</b></td><td>199.92 <b>(+26.88%)</b></td><td>192.50 (+18.83%)</td><td>153.60 (+5.93%)</td><td>37.27 <b>(+342.45%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 00:46:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>164.60 (n/a)</td><td>157.56 (n/a)</td><td>162.00 (n/a)</td><td>145.00 (n/a)</td><td>8.42 (n/a)</td>
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
