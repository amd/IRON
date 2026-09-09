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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-12.76%)</td><td>0.04 (-5.54%)</td><td>0.04 (-16.13%)</td><td>0.03 (+3.67%)</td><td>0.01 <b>(-25.66%)</b></td><td>194.90 (-3.56%)</td><td>158.12 (+2.86%)</td><td>169.30 (+19.31%)</td><td>112.00 (+14.64%)</td><td>35.10 <b>(-21.35%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>153.72 (n/a)</td><td>141.90 (n/a)</td><td>97.70 (n/a)</td><td>44.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (+1.04%)</td><td>0.04 (+4.36%)</td><td>0.05 <b>(+20.91%)</b></td><td>0.03 (+2.97%)</td><td>0.01 (+13.83%)</td><td>186.90 (-2.91%)</td><td>152.64 (-3.61%)</td><td>136.20 (-17.30%)</td><td>128.40 (-1.08%)</td><td>28.97 (+12.28%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>158.36 (n/a)</td><td>164.70 (n/a)</td><td>129.80 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-2.78%)</td><td>0.04 (+3.16%)</td><td>0.04 <b>(+26.22%)</b></td><td>0.03 (-6.22%)</td><td>0.01 (-16.38%)</td><td>214.90 (+6.65%)</td><td>159.64 (-4.00%)</td><td>144.70 <b>(-20.80%)</b></td><td>127.90 (+2.90%)</td><td>35.55 (-6.05%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>166.30 (n/a)</td><td>182.70 (n/a)</td><td>124.30 (n/a)</td><td>37.84 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (+3.03%)</td><td>0.04 (+18.42%)</td><td>0.04 <b>(+25.54%)</b></td><td>0.03 (-1.26%)</td><td>0.01 (+9.09%)</td><td>210.90 (+1.30%)</td><td>158.04 (-15.15%)</td><td>154.80 <b>(-20.37%)</b></td><td>126.60 (-2.91%)</td><td>34.48 (+7.21%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>186.26 (n/a)</td><td>194.40 (n/a)</td><td>130.40 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 <b>(+21.63%)</b></td><td>0.04 (+13.69%)</td><td>0.04 (+8.70%)</td><td>0.03 (+10.24%)</td><td>0.01 <b>(+70.96%)</b></td><td>189.10 (-9.30%)</td><td>159.22 (-10.39%)</td><td>168.00 (-8.05%)</td><td>117.70 (-17.75%)</td><td>31.28 <b>(+31.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.50 (n/a)</td><td>177.68 (n/a)</td><td>182.70 (n/a)</td><td>143.10 (n/a)</td><td>23.87 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (+15.01%)</td><td>0.04 (+10.21%)</td><td>0.04 (+7.75%)</td><td>0.03 (+9.08%)</td><td>0.01 <b>(+21.70%)</b></td><td>215.70 (-8.33%)</td><td>173.64 (-9.00%)</td><td>168.40 (-7.22%)</td><td>145.80 (-13.06%)</td><td>27.65 (-1.99%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.30 (n/a)</td><td>190.82 (n/a)</td><td>181.50 (n/a)</td><td>167.70 (n/a)</td><td>28.22 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 <b>(+31.86%)</b></td><td>0.03 <b>(+23.14%)</b></td><td>0.03 (+8.51%)</td><td>0.02 (+11.93%)</td><td>0.01 <b>(+59.32%)</b></td><td>273.40 (-10.65%)</td><td>197.20 (-15.86%)</td><td>216.50 (-7.83%)</td><td>116.60 <b>(-24.14%)</b></td><td>59.80 (+9.29%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>306.00 (n/a)</td><td>234.38 (n/a)</td><td>234.90 (n/a)</td><td>153.70 (n/a)</td><td>54.72 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (+19.09%)</td><td>0.03 (+8.42%)</td><td>0.03 (+0.02%)</td><td>0.02 (-8.28%)</td><td>0.01 <b>(+70.02%)</b></td><td>321.50 (+9.02%)</td><td>212.96 (-3.50%)</td><td>211.50 (-0.05%)</td><td>144.90 (-16.05%)</td><td>68.91 <b>(+51.22%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>294.90 (n/a)</td><td>220.68 (n/a)</td><td>211.60 (n/a)</td><td>172.60 (n/a)</td><td>45.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 <b>(+31.14%)</b></td><td>0.08 <b>(+20.49%)</b></td><td>0.08 (+16.00%)</td><td>0.07 (+8.94%)</td><td>0.01 <b>(+182.56%)</b></td><td>179.20 (-8.20%)</td><td>152.14 (-16.19%)</td><td>153.10 (-13.75%)</td><td>130.70 <b>(-23.75%)</b></td><td>18.59 <b>(+97.06%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>195.20 (n/a)</td><td>181.54 (n/a)</td><td>177.50 (n/a)</td><td>171.40 (n/a)</td><td>9.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (+1.07%)</td><td>0.07 (+0.04%)</td><td>0.07 (+6.87%)</td><td>0.05 (-11.26%)</td><td>0.01 (+13.77%)</td><td>251.60 (+12.67%)</td><td>184.14 (+1.21%)</td><td>174.40 (-6.44%)</td><td>137.50 (-1.01%)</td><td>42.58 <b>(+30.47%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>181.94 (n/a)</td><td>186.40 (n/a)</td><td>138.90 (n/a)</td><td>32.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (-6.94%)</td><td>0.08 (-3.51%)</td><td>0.07 (-7.89%)</td><td>0.06 (+3.70%)</td><td>0.01 <b>(-26.02%)</b></td><td>200.30 (-3.61%)</td><td>165.20 (+2.18%)</td><td>163.90 (+8.54%)</td><td>131.30 (+7.45%)</td><td>24.54 <b>(-24.64%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>207.80 (n/a)</td><td>161.68 (n/a)</td><td>151.00 (n/a)</td><td>122.20 (n/a)</td><td>32.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (-0.29%)</td><td>0.08 (-1.84%)</td><td>0.08 (+4.47%)</td><td>0.06 (+7.92%)</td><td>0.01 (-16.04%)</td><td>204.00 (-7.31%)</td><td>162.82 (+0.68%)</td><td>155.00 (-4.26%)</td><td>129.80 (+0.31%)</td><td>29.08 <b>(-20.38%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>220.10 (n/a)</td><td>161.72 (n/a)</td><td>161.90 (n/a)</td><td>129.40 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (-1.16%)</td><td>0.08 (+1.37%)</td><td>0.07 (-1.83%)</td><td>0.07 <b>(+22.82%)</b></td><td>0.01 <b>(-36.30%)</b></td><td>184.00 (-18.58%)</td><td>160.20 (-3.88%)</td><td>165.10 (+1.85%)</td><td>131.60 (+1.15%)</td><td>20.19 <b>(-47.56%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>226.00 (n/a)</td><td>166.66 (n/a)</td><td>162.10 (n/a)</td><td>130.10 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (+0.96%)</td><td>0.08 (+11.58%)</td><td>0.08 (+14.24%)</td><td>0.05 (-3.94%)</td><td>0.02 (+15.73%)</td><td>236.60 (+4.09%)</td><td>160.12 (-9.10%)</td><td>151.50 (-12.43%)</td><td>127.50 (-0.93%)</td><td>44.87 <b>(+20.20%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>227.30 (n/a)</td><td>176.14 (n/a)</td><td>173.00 (n/a)</td><td>128.70 (n/a)</td><td>37.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (+2.51%)</td><td>0.07 (-6.24%)</td><td>0.06 <b>(-26.21%)</b></td><td>0.05 (-1.90%)</td><td>0.02 (-0.70%)</td><td>235.00 (+1.95%)</td><td>186.78 (+6.45%)</td><td>202.80 <b>(+35.56%)</b></td><td>135.10 (-2.45%)</td><td>43.06 (-3.09%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>230.50 (n/a)</td><td>175.46 (n/a)</td><td>149.60 (n/a)</td><td>138.50 (n/a)</td><td>44.44 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (-6.73%)</td><td>0.07 (-4.07%)</td><td>0.07 (-4.30%)</td><td>0.04 <b>(-20.50%)</b></td><td>0.02 (-3.58%)</td><td>295.20 <b>(+25.78%)</b></td><td>189.12 (+5.58%)</td><td>165.20 (+4.49%)</td><td>141.80 (+7.26%)</td><td>61.79 <b>(+30.65%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>234.70 (n/a)</td><td>179.12 (n/a)</td><td>158.10 (n/a)</td><td>132.20 (n/a)</td><td>47.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (+1.12%)</td><td>0.17 (+6.56%)</td><td>0.19 (+12.81%)</td><td>0.14 <b>(+20.39%)</b></td><td>0.02 <b>(-24.46%)</b></td><td>180.80 (-16.95%)</td><td>145.08 (-8.03%)</td><td>131.10 (-11.36%)</td><td>126.70 (-1.17%)</td><td>23.06 <b>(-37.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>217.70 (n/a)</td><td>157.74 (n/a)</td><td>147.90 (n/a)</td><td>128.20 (n/a)</td><td>36.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (+6.49%)</td><td>0.17 (+0.59%)</td><td>0.18 (+5.80%)</td><td>0.11 (-18.25%)</td><td>0.04 <b>(+54.75%)</b></td><td>220.50 <b>(+22.30%)</b></td><td>155.62 (+2.22%)</td><td>137.50 (-5.50%)</td><td>123.90 (-6.07%)</td><td>39.72 <b>(+80.26%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>180.30 (n/a)</td><td>152.24 (n/a)</td><td>145.50 (n/a)</td><td>131.90 (n/a)</td><td>22.04 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (+4.01%)</td><td>0.18 (+3.32%)</td><td>0.19 (+8.33%)</td><td>0.15 (+4.91%)</td><td>0.02 (+18.48%)</td><td>161.70 (-4.71%)</td><td>137.52 (-2.98%)</td><td>128.20 (-7.70%)</td><td>123.20 (-3.83%)</td><td>17.67 (+6.25%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>169.70 (n/a)</td><td>141.74 (n/a)</td><td>138.90 (n/a)</td><td>128.10 (n/a)</td><td>16.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (+10.94%)</td><td>0.17 (+13.70%)</td><td>0.18 <b>(+20.60%)</b></td><td>0.13 (+17.16%)</td><td>0.03 (-12.86%)</td><td>190.40 (-14.66%)</td><td>144.70 (-13.46%)</td><td>133.20 (-17.11%)</td><td>117.80 (-9.80%)</td><td>28.09 <b>(-29.17%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>223.10 (n/a)</td><td>167.20 (n/a)</td><td>160.70 (n/a)</td><td>130.60 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 <b>(+20.02%)</b></td><td>0.18 <b>(+39.36%)</b></td><td>0.19 <b>(+43.12%)</b></td><td>0.14 <b>(+66.21%)</b></td><td>0.02 <b>(-21.60%)</b></td><td>171.70 <b>(-39.82%)</b></td><td>136.48 <b>(-30.58%)</b></td><td>127.80 <b>(-30.13%)</b></td><td>121.10 (-16.71%)</td><td>20.22 <b>(-61.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>285.30 (n/a)</td><td>196.60 (n/a)</td><td>182.90 (n/a)</td><td>145.40 (n/a)</td><td>52.50 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (+6.00%)</td><td>0.16 <b>(+27.36%)</b></td><td>0.16 <b>(+32.64%)</b></td><td>0.13 <b>(+38.05%)</b></td><td>0.03 <b>(-31.03%)</b></td><td>194.30 <b>(-27.58%)</b></td><td>156.84 <b>(-25.14%)</b></td><td>156.40 <b>(-24.59%)</b></td><td>120.30 (-5.65%)</td><td>26.46 <b>(-53.68%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>268.30 (n/a)</td><td>209.52 (n/a)</td><td>207.40 (n/a)</td><td>127.50 (n/a)</td><td>57.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (+16.25%)</td><td>0.13 (+18.00%)</td><td>0.14 (+19.85%)</td><td>0.12 <b>(+32.99%)</b></td><td>0.02 (-3.00%)</td><td>212.40 <b>(-24.81%)</b></td><td>184.68 (-15.87%)</td><td>173.30 (-16.56%)</td><td>165.20 (-13.96%)</td><td>21.70 <b>(-39.47%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>282.50 (n/a)</td><td>219.52 (n/a)</td><td>207.70 (n/a)</td><td>192.00 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (+17.79%)</td><td>0.16 <b>(+21.43%)</b></td><td>0.14 (+9.37%)</td><td>0.13 <b>(+31.31%)</b></td><td>0.03 (+6.86%)</td><td>182.60 <b>(-23.85%)</b></td><td>159.46 (-18.26%)</td><td>171.50 (-8.58%)</td><td>132.50 (-15.12%)</td><td>24.34 <b>(-32.68%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>239.80 (n/a)</td><td>195.08 (n/a)</td><td>187.60 (n/a)</td><td>156.10 (n/a)</td><td>36.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.41 <b>(+21.27%)</b></td><td>0.34 <b>(+22.89%)</b></td><td>0.38 <b>(+39.06%)</b></td><td>0.26 (+13.08%)</td><td>0.07 <b>(+73.39%)</b></td><td>188.70 (-11.57%)</td><td>149.12 (-16.95%)</td><td>130.40 <b>(-28.08%)</b></td><td>120.80 (-17.54%)</td><td>33.04 <b>(+28.13%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>213.40 (n/a)</td><td>179.56 (n/a)</td><td>181.30 (n/a)</td><td>146.50 (n/a)</td><td>25.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.38 <b>(+31.56%)</b></td><td>0.34 <b>(+38.90%)</b></td><td>0.34 <b>(+32.35%)</b></td><td>0.28 <b>(+84.32%)</b></td><td>0.04 <b>(-25.52%)</b></td><td>173.80 <b>(-45.74%)</b></td><td>146.56 <b>(-30.89%)</b></td><td>145.80 <b>(-24.46%)</b></td><td>128.50 <b>(-23.96%)</b></td><td>18.24 <b>(-70.55%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>320.30 (n/a)</td><td>212.06 (n/a)</td><td>193.00 (n/a)</td><td>169.00 (n/a)</td><td>61.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.40 (-3.26%)</td><td>0.33 (+5.58%)</td><td>0.30 (+5.21%)</td><td>0.29 (+12.08%)</td><td>0.05 (-12.52%)</td><td>170.70 (-10.77%)</td><td>150.56 (-6.02%)</td><td>162.20 (-4.92%)</td><td>123.90 (+3.34%)</td><td>22.94 (-18.56%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>191.30 (n/a)</td><td>160.20 (n/a)</td><td>170.60 (n/a)</td><td>119.90 (n/a)</td><td>28.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.33 (-16.82%)</td><td>0.31 (+7.73%)</td><td>0.33 (+18.19%)</td><td>0.28 <b>(+35.63%)</b></td><td>0.03 <b>(-62.85%)</b></td><td>175.60 <b>(-26.25%)</b></td><td>159.80 (-10.64%)</td><td>150.90 (-15.37%)</td><td>148.20 <b>(+20.19%)</b></td><td>13.78 <b>(-66.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>238.10 (n/a)</td><td>178.82 (n/a)</td><td>178.30 (n/a)</td><td>123.30 (n/a)</td><td>40.80 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.41 (-12.40%)</td><td>0.34 (+1.29%)</td><td>0.33 (+1.95%)</td><td>0.25 (+12.33%)</td><td>0.06 <b>(-27.66%)</b></td><td>194.20 (-11.00%)</td><td>149.88 (-3.60%)</td><td>148.70 (-1.91%)</td><td>120.40 (+14.23%)</td><td>29.37 <b>(-27.28%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>218.20 (n/a)</td><td>155.48 (n/a)</td><td>151.60 (n/a)</td><td>105.40 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.47 <b>(+20.96%)</b></td><td>0.36 <b>(+30.22%)</b></td><td>0.37 <b>(+38.71%)</b></td><td>0.22 <b>(+23.62%)</b></td><td>0.09 (+18.61%)</td><td>220.50 (-19.11%)</td><td>146.74 <b>(-23.20%)</b></td><td>133.40 <b>(-27.89%)</b></td><td>103.50 (-17.33%)</td><td>44.00 (-16.65%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>272.60 (n/a)</td><td>191.06 (n/a)</td><td>185.00 (n/a)</td><td>125.20 (n/a)</td><td>52.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.37 (+19.63%)</td><td>0.32 <b>(+22.86%)</b></td><td>0.35 <b>(+30.57%)</b></td><td>0.21 (+1.50%)</td><td>0.06 <b>(+74.49%)</b></td><td>236.30 (-1.46%)</td><td>161.66 (-16.44%)</td><td>140.40 <b>(-23.40%)</b></td><td>134.50 (-16.41%)</td><td>42.72 <b>(+44.41%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>239.80 (n/a)</td><td>193.46 (n/a)</td><td>183.30 (n/a)</td><td>160.90 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.37 <b>(+25.22%)</b></td><td>0.30 <b>(+27.87%)</b></td><td>0.28 (+18.92%)</td><td>0.23 <b>(+26.55%)</b></td><td>0.06 <b>(+39.34%)</b></td><td>216.70 <b>(-20.97%)</b></td><td>169.10 <b>(-21.36%)</b></td><td>175.60 (-15.90%)</td><td>131.80 <b>(-20.12%)</b></td><td>34.96 (-14.87%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>274.20 (n/a)</td><td>215.04 (n/a)</td><td>208.80 (n/a)</td><td>165.00 (n/a)</td><td>41.07 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (+9.65%)</td><td>0.02 (+13.23%)</td><td>0.02 (+17.64%)</td><td>0.01 <b>(+20.57%)</b></td><td>0.00 (+19.88%)</td><td>191.90 (-17.07%)</td><td>149.88 (-11.46%)</td><td>137.40 (-14.98%)</td><td>118.00 (-8.81%)</td><td>33.18 (-11.82%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>231.40 (n/a)</td><td>169.28 (n/a)</td><td>161.60 (n/a)</td><td>129.40 (n/a)</td><td>37.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (-1.60%)</td><td>0.02 (+3.70%)</td><td>0.02 (+16.03%)</td><td>0.01 <b>(-29.95%)</b></td><td>0.01 (+15.41%)</td><td>284.20 <b>(+42.81%)</b></td><td>168.74 (+1.38%)</td><td>150.40 (-13.81%)</td><td>108.60 (+1.59%)</td><td>67.07 <b>(+87.82%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>199.00 (n/a)</td><td>166.44 (n/a)</td><td>174.50 (n/a)</td><td>106.90 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (+15.73%)</td><td>0.01 (-1.07%)</td><td>0.01 (-12.71%)</td><td>0.01 (-13.44%)</td><td>0.00 <b>(+91.43%)</b></td><td>267.90 (+15.52%)</td><td>190.26 (+6.30%)</td><td>193.20 (+14.59%)</td><td>132.70 (-13.61%)</td><td>56.80 <b>(+80.10%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>231.90 (n/a)</td><td>178.98 (n/a)</td><td>168.60 (n/a)</td><td>153.60 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 <b>(+29.16%)</b></td><td>0.02 <b>(+20.18%)</b></td><td>0.02 <b>(+22.41%)</b></td><td>0.01 (-3.26%)</td><td>0.00 <b>(+60.04%)</b></td><td>223.50 (+3.33%)</td><td>150.00 (-14.27%)</td><td>133.00 (-18.30%)</td><td>108.90 <b>(-22.60%)</b></td><td>44.42 <b>(+30.81%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>216.30 (n/a)</td><td>174.96 (n/a)</td><td>162.80 (n/a)</td><td>140.70 (n/a)</td><td>33.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (+13.83%)</td><td>0.02 (+18.57%)</td><td>0.02 (+10.10%)</td><td>0.02 <b>(+29.41%)</b></td><td>0.00 (+13.69%)</td><td>174.10 <b>(-22.73%)</b></td><td>154.76 (-15.82%)</td><td>167.60 (-9.16%)</td><td>126.20 (-12.12%)</td><td>22.93 <b>(-21.51%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>225.30 (n/a)</td><td>183.84 (n/a)</td><td>184.50 (n/a)</td><td>143.60 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (+12.25%)</td><td>0.02 <b>(+22.74%)</b></td><td>0.02 <b>(+25.16%)</b></td><td>0.01 <b>(+46.99%)</b></td><td>0.00 <b>(-20.10%)</b></td><td>196.30 <b>(-31.98%)</b></td><td>164.20 <b>(-20.90%)</b></td><td>153.20 <b>(-20.13%)</b></td><td>139.80 (-10.90%)</td><td>26.14 <b>(-51.29%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>288.60 (n/a)</td><td>207.58 (n/a)</td><td>191.80 (n/a)</td><td>156.90 (n/a)</td><td>53.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (+1.07%)</td><td>0.02 (+17.73%)</td><td>0.02 <b>(+39.41%)</b></td><td>0.01 (+1.66%)</td><td>0.00 (+6.84%)</td><td>232.90 (-1.65%)</td><td>174.36 (-14.61%)</td><td>162.10 <b>(-28.27%)</b></td><td>131.60 (-1.13%)</td><td>44.65 (+5.04%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>236.80 (n/a)</td><td>204.20 (n/a)</td><td>226.00 (n/a)</td><td>133.10 (n/a)</td><td>42.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 <b>(+26.42%)</b></td><td>0.01 <b>(+27.96%)</b></td><td>0.01 (+19.57%)</td><td>0.01 <b>(+62.10%)</b></td><td>0.00 <b>(-26.74%)</b></td><td>209.50 <b>(-38.33%)</b></td><td>188.62 <b>(-23.55%)</b></td><td>193.40 (-16.39%)</td><td>167.20 <b>(-20.87%)</b></td><td>18.08 <b>(-65.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>339.70 (n/a)</td><td>246.72 (n/a)</td><td>231.30 (n/a)</td><td>211.30 (n/a)</td><td>52.74 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 <b>(+46.99%)</b></td><td>0.03 (+11.47%)</td><td>0.03 (+18.43%)</td><td>0.02 <b>(-34.12%)</b></td><td>0.01 <b>(+209.95%)</b></td><td>347.50 <b>(+51.81%)</b></td><td>204.04 (+1.05%)</td><td>173.70 (-15.56%)</td><td>113.00 <b>(-31.97%)</b></td><td>88.45 <b>(+225.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>228.90 (n/a)</td><td>201.92 (n/a)</td><td>205.70 (n/a)</td><td>166.10 (n/a)</td><td>27.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 <b>(+36.14%)</b></td><td>0.04 <b>(+27.50%)</b></td><td>0.04 <b>(+33.00%)</b></td><td>0.03 <b>(+21.09%)</b></td><td>0.01 <b>(+121.15%)</b></td><td>190.80 (-17.40%)</td><td>151.44 (-19.67%)</td><td>138.10 <b>(-24.82%)</b></td><td>121.90 <b>(-26.52%)</b></td><td>33.01 <b>(+31.39%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.00 (n/a)</td><td>188.52 (n/a)</td><td>183.70 (n/a)</td><td>165.90 (n/a)</td><td>25.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 <b>(+29.11%)</b></td><td>0.03 <b>(+22.84%)</b></td><td>0.03 (+14.69%)</td><td>0.03 (+15.39%)</td><td>0.01 <b>(+63.33%)</b></td><td>198.70 (-13.34%)</td><td>164.58 (-17.58%)</td><td>176.30 (-12.81%)</td><td>127.70 <b>(-22.51%)</b></td><td>30.36 (+6.97%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.30 (n/a)</td><td>199.68 (n/a)</td><td>202.20 (n/a)</td><td>164.80 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 <b>(+44.35%)</b></td><td>0.04 <b>(+40.45%)</b></td><td>0.04 <b>(+44.86%)</b></td><td>0.03 <b>(+46.84%)</b></td><td>0.01 <b>(+67.46%)</b></td><td>168.30 <b>(-31.92%)</b></td><td>143.92 <b>(-28.45%)</b></td><td>138.40 <b>(-31.01%)</b></td><td>120.30 <b>(-30.70%)</b></td><td>22.64 <b>(-20.39%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.20 (n/a)</td><td>201.16 (n/a)</td><td>200.60 (n/a)</td><td>173.60 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 <b>(+48.53%)</b></td><td>0.03 (+18.25%)</td><td>0.03 (+12.98%)</td><td>0.02 (+12.04%)</td><td>0.01 <b>(+138.84%)</b></td><td>224.20 (-10.75%)</td><td>178.58 (-12.52%)</td><td>179.30 (-11.50%)</td><td>116.80 <b>(-32.68%)</b></td><td>40.50 <b>(+37.26%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.20 (n/a)</td><td>204.14 (n/a)</td><td>202.60 (n/a)</td><td>173.50 (n/a)</td><td>29.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 <b>(+26.81%)</b></td><td>0.03 <b>(+20.89%)</b></td><td>0.03 <b>(+26.34%)</b></td><td>0.02 (-3.14%)</td><td>0.01 <b>(+103.57%)</b></td><td>212.10 (+3.26%)</td><td>158.14 (-15.47%)</td><td>155.10 <b>(-20.83%)</b></td><td>124.80 <b>(-21.16%)</b></td><td>32.75 <b>(+71.44%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.40 (n/a)</td><td>187.08 (n/a)</td><td>195.90 (n/a)</td><td>158.30 (n/a)</td><td>19.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (-18.80%)</td><td>0.03 (+13.32%)</td><td>0.03 (+16.41%)</td><td>0.02 <b>(+56.78%)</b></td><td>0.01 <b>(-51.35%)</b></td><td>221.90 <b>(-36.22%)</b></td><td>165.02 <b>(-20.43%)</b></td><td>160.30 (-14.09%)</td><td>138.30 <b>(+23.15%)</b></td><td>33.42 <b>(-61.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>347.90 (n/a)</td><td>207.40 (n/a)</td><td>186.60 (n/a)</td><td>112.30 (n/a)</td><td>87.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+17.22%)</td><td>0.03 <b>(+20.02%)</b></td><td>0.03 <b>(+29.03%)</b></td><td>0.02 <b>(+24.91%)</b></td><td>0.00 (+3.82%)</td><td>258.80 (-19.95%)</td><td>208.52 (-17.14%)</td><td>192.90 <b>(-22.50%)</b></td><td>182.60 (-14.67%)</td><td>31.13 <b>(-28.83%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>323.30 (n/a)</td><td>251.64 (n/a)</td><td>248.90 (n/a)</td><td>214.00 (n/a)</td><td>43.74 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (+9.45%)</td><td>0.06 <b>(+23.14%)</b></td><td>0.06 <b>(+22.50%)</b></td><td>0.05 <b>(+71.21%)</b></td><td>0.01 <b>(-35.03%)</b></td><td>198.30 <b>(-41.59%)</b></td><td>168.16 <b>(-24.00%)</b></td><td>172.30 (-18.38%)</td><td>131.20 (-8.64%)</td><td>25.95 <b>(-65.85%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>339.50 (n/a)</td><td>221.26 (n/a)</td><td>211.10 (n/a)</td><td>143.60 (n/a)</td><td>75.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 <b>(+33.43%)</b></td><td>0.07 <b>(+28.57%)</b></td><td>0.07 <b>(+37.41%)</b></td><td>0.05 <b>(+39.27%)</b></td><td>0.01 (+18.04%)</td><td>191.10 <b>(-28.21%)</b></td><td>163.36 <b>(-22.74%)</b></td><td>160.50 <b>(-27.21%)</b></td><td>124.90 <b>(-25.07%)</b></td><td>27.13 <b>(-33.93%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>266.20 (n/a)</td><td>211.44 (n/a)</td><td>220.50 (n/a)</td><td>166.70 (n/a)</td><td>41.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 <b>(+36.52%)</b></td><td>0.07 <b>(+25.38%)</b></td><td>0.06 (+11.62%)</td><td>0.05 <b>(+35.56%)</b></td><td>0.01 <b>(+46.66%)</b></td><td>205.40 <b>(-26.22%)</b></td><td>164.20 (-19.86%)</td><td>164.90 (-10.38%)</td><td>125.50 <b>(-26.74%)</b></td><td>34.61 <b>(-21.79%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>278.40 (n/a)</td><td>204.90 (n/a)</td><td>184.00 (n/a)</td><td>171.30 (n/a)</td><td>44.25 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 <b>(+39.60%)</b></td><td>0.07 <b>(+42.57%)</b></td><td>0.06 <b>(+27.07%)</b></td><td>0.06 <b>(+91.09%)</b></td><td>0.01 (-9.60%)</td><td>180.50 <b>(-47.68%)</b></td><td>159.64 <b>(-32.30%)</b></td><td>170.60 <b>(-21.31%)</b></td><td>130.20 <b>(-28.38%)</b></td><td>21.70 <b>(-66.77%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>345.00 (n/a)</td><td>235.80 (n/a)</td><td>216.80 (n/a)</td><td>181.80 (n/a)</td><td>65.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (-8.47%)</td><td>0.07 (-2.44%)</td><td>0.06 (+1.78%)</td><td>0.05 (+0.56%)</td><td>0.01 <b>(-30.41%)</b></td><td>197.40 (-0.55%)</td><td>163.02 (+1.13%)</td><td>163.40 (-1.74%)</td><td>135.90 (+9.24%)</td><td>23.04 <b>(-23.32%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>161.20 (n/a)</td><td>166.30 (n/a)</td><td>124.40 (n/a)</td><td>30.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 <b>(+39.11%)</b></td><td>0.07 <b>(+32.72%)</b></td><td>0.07 <b>(+36.57%)</b></td><td>0.05 <b>(+31.85%)</b></td><td>0.02 <b>(+52.43%)</b></td><td>204.80 <b>(-24.18%)</b></td><td>156.46 <b>(-23.96%)</b></td><td>155.00 <b>(-26.78%)</b></td><td>109.30 <b>(-28.14%)</b></td><td>36.51 (-17.11%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>270.10 (n/a)</td><td>205.76 (n/a)</td><td>211.70 (n/a)</td><td>152.10 (n/a)</td><td>44.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (+17.92%)</td><td>0.06 (+12.82%)</td><td>0.06 (-0.76%)</td><td>0.05 <b>(+30.07%)</b></td><td>0.01 (+19.05%)</td><td>207.30 <b>(-23.11%)</b></td><td>170.14 (-11.67%)</td><td>172.30 (+0.76%)</td><td>130.30 (-15.22%)</td><td>35.16 <b>(-23.89%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>269.60 (n/a)</td><td>192.62 (n/a)</td><td>171.00 (n/a)</td><td>153.70 (n/a)</td><td>46.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (-3.59%)</td><td>0.05 (+6.13%)</td><td>0.05 (+7.93%)</td><td>0.05 <b>(+38.64%)</b></td><td>0.00 <b>(-64.48%)</b></td><td>225.80 <b>(-27.88%)</b></td><td>206.56 (-9.82%)</td><td>206.30 (-7.32%)</td><td>182.70 (+3.75%)</td><td>15.91 <b>(-72.59%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>313.10 (n/a)</td><td>229.06 (n/a)</td><td>222.60 (n/a)</td><td>176.10 (n/a)</td><td>58.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (+8.04%)</td><td>0.14 (+9.34%)</td><td>0.15 <b>(+26.98%)</b></td><td>0.12 (+7.01%)</td><td>0.02 (+10.19%)</td><td>182.40 (-6.56%)</td><td>152.20 (-8.35%)</td><td>136.80 <b>(-21.24%)</b></td><td>128.60 (-7.42%)</td><td>25.26 (-0.32%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>195.20 (n/a)</td><td>166.06 (n/a)</td><td>173.70 (n/a)</td><td>138.90 (n/a)</td><td>25.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 <b>(+23.93%)</b></td><td>0.13 (+15.13%)</td><td>0.12 (+3.37%)</td><td>0.11 <b>(+29.85%)</b></td><td>0.02 (+2.51%)</td><td>184.30 <b>(-22.98%)</b></td><td>162.06 (-13.68%)</td><td>168.50 (-3.27%)</td><td>135.40 (-19.31%)</td><td>18.92 <b>(-37.19%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>239.30 (n/a)</td><td>187.74 (n/a)</td><td>174.20 (n/a)</td><td>167.80 (n/a)</td><td>30.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (+0.24%)</td><td>0.13 (-5.10%)</td><td>0.12 (-12.65%)</td><td>0.10 (-13.21%)</td><td>0.03 <b>(+22.04%)</b></td><td>215.50 (+15.24%)</td><td>165.42 (+7.37%)</td><td>175.60 (+14.47%)</td><td>122.50 (-0.24%)</td><td>39.73 <b>(+35.26%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>187.00 (n/a)</td><td>154.06 (n/a)</td><td>153.40 (n/a)</td><td>122.80 (n/a)</td><td>29.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (+14.97%)</td><td>0.14 (+13.84%)</td><td>0.13 (+12.07%)</td><td>0.10 (+10.19%)</td><td>0.03 <b>(+29.42%)</b></td><td>201.70 (-9.27%)</td><td>156.68 (-11.45%)</td><td>157.10 (-10.79%)</td><td>120.80 (-13.03%)</td><td>32.60 (+1.08%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>176.94 (n/a)</td><td>176.10 (n/a)</td><td>138.90 (n/a)</td><td>32.25 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (-4.35%)</td><td>0.12 (-2.38%)</td><td>0.12 (+2.03%)</td><td>0.07 <b>(-24.69%)</b></td><td>0.03 <b>(+45.49%)</b></td><td>281.20 <b>(+32.77%)</b></td><td>185.38 (+6.36%)</td><td>172.30 (-1.99%)</td><td>144.00 (+4.50%)</td><td>55.51 <b>(+110.54%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.80 (n/a)</td><td>174.30 (n/a)</td><td>175.80 (n/a)</td><td>137.80 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (-10.19%)</td><td>0.13 (-1.03%)</td><td>0.11 (-2.25%)</td><td>0.09 (-2.20%)</td><td>0.03 (-5.96%)</td><td>222.50 (+2.25%)</td><td>172.62 (+1.02%)</td><td>184.90 (+2.32%)</td><td>130.30 (+11.37%)</td><td>39.79 (+4.72%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>217.60 (n/a)</td><td>170.88 (n/a)</td><td>180.70 (n/a)</td><td>117.00 (n/a)</td><td>37.99 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (+4.08%)</td><td>0.12 (+8.97%)</td><td>0.12 (+3.00%)</td><td>0.10 <b>(+28.95%)</b></td><td>0.02 (-14.56%)</td><td>211.40 <b>(-22.45%)</b></td><td>175.14 (-10.12%)</td><td>173.10 (-2.86%)</td><td>136.30 (-3.88%)</td><td>30.76 <b>(-37.32%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>272.60 (n/a)</td><td>194.86 (n/a)</td><td>178.20 (n/a)</td><td>141.80 (n/a)</td><td>49.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 <b>(+30.87%)</b></td><td>0.10 (+13.59%)</td><td>0.10 (+5.74%)</td><td>0.09 (+5.91%)</td><td>0.01 <b>(+123.16%)</b></td><td>237.60 (-5.56%)</td><td>206.58 (-11.16%)</td><td>210.50 (-5.44%)</td><td>167.20 <b>(-23.62%)</b></td><td>25.23 <b>(+57.16%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>251.60 (n/a)</td><td>232.52 (n/a)</td><td>222.60 (n/a)</td><td>218.90 (n/a)</td><td>16.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>172.50 (n/a)</td><td>145.12 (n/a)</td><td>138.30 (n/a)</td><td>119.50 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>165.10 (n/a)</td><td>167.10 (n/a)</td><td>111.80 (n/a)</td><td>49.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.10 (n/a)</td><td>174.56 (n/a)</td><td>172.50 (n/a)</td><td>151.90 (n/a)</td><td>21.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.90 (n/a)</td><td>201.42 (n/a)</td><td>206.00 (n/a)</td><td>144.40 (n/a)</td><td>43.65 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>193.50 (n/a)</td><td>160.74 (n/a)</td><td>166.10 (n/a)</td><td>116.30 (n/a)</td><td>30.01 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.20 (n/a)</td><td>175.88 (n/a)</td><td>184.80 (n/a)</td><td>138.10 (n/a)</td><td>22.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.20 (n/a)</td><td>191.06 (n/a)</td><td>187.80 (n/a)</td><td>150.70 (n/a)</td><td>30.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>208.18 (n/a)</td><td>200.40 (n/a)</td><td>183.20 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.70 (n/a)</td><td>167.96 (n/a)</td><td>164.50 (n/a)</td><td>126.80 (n/a)</td><td>31.25 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>170.00 (n/a)</td><td>154.30 (n/a)</td><td>154.30 (n/a)</td><td>132.30 (n/a)</td><td>14.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>168.90 (n/a)</td><td>137.62 (n/a)</td><td>132.90 (n/a)</td><td>120.30 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.60 (n/a)</td><td>169.62 (n/a)</td><td>159.20 (n/a)</td><td>140.40 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.40 (+9.48%)</td><td>0.32 (+11.26%)</td><td>0.30 (+4.70%)</td><td>0.28 <b>(+25.32%)</b></td><td>0.05 (-6.25%)</td><td>176.10 <b>(-20.17%)</b></td><td>156.52 (-10.92%)</td><td>161.40 (-4.50%)</td><td>122.90 (-8.62%)</td><td>21.29 <b>(-32.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>220.60 (n/a)</td><td>175.70 (n/a)</td><td>169.00 (n/a)</td><td>134.50 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>346.20 (n/a)</td><td>196.62 (n/a)</td><td>176.20 (n/a)</td><td>128.20 (n/a)</td><td>86.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>220.50 (n/a)</td><td>175.42 (n/a)</td><td>191.50 (n/a)</td><td>118.30 (n/a)</td><td>40.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.44 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>181.70 (n/a)</td><td>166.02 (n/a)</td><td>177.10 (n/a)</td><td>112.80 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>176.50 (n/a)</td><td>152.78 (n/a)</td><td>167.00 (n/a)</td><td>115.30 (n/a)</td><td>27.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>301.40 (n/a)</td><td>213.60 (n/a)</td><td>199.20 (n/a)</td><td>162.60 (n/a)</td><td>52.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.60 (n/a)</td><td>197.16 (n/a)</td><td>188.60 (n/a)</td><td>174.90 (n/a)</td><td>24.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>265.50 (n/a)</td><td>193.48 (n/a)</td><td>200.70 (n/a)</td><td>143.90 (n/a)</td><td>48.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>279.30 (n/a)</td><td>202.50 (n/a)</td><td>190.70 (n/a)</td><td>146.60 (n/a)</td><td>49.44 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>222.60 (n/a)</td><td>174.82 (n/a)</td><td>163.70 (n/a)</td><td>120.30 (n/a)</td><td>46.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>224.90 (n/a)</td><td>159.52 (n/a)</td><td>131.90 (n/a)</td><td>107.60 (n/a)</td><td>50.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>277.40 (n/a)</td><td>203.00 (n/a)</td><td>199.10 (n/a)</td><td>127.80 (n/a)</td><td>56.75 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>210.30 (n/a)</td><td>165.86 (n/a)</td><td>172.30 (n/a)</td><td>123.20 (n/a)</td><td>33.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>208.40 (n/a)</td><td>174.26 (n/a)</td><td>170.20 (n/a)</td><td>133.90 (n/a)</td><td>33.41 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>209.30 (n/a)</td><td>171.30 (n/a)</td><td>186.40 (n/a)</td><td>126.80 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.00 (n/a)</td><td>169.42 (n/a)</td><td>172.00 (n/a)</td><td>124.60 (n/a)</td><td>34.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>219.30 (n/a)</td><td>191.98 (n/a)</td><td>194.70 (n/a)</td><td>151.10 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>174.20 (n/a)</td><td>174.50 (n/a)</td><td>158.70 (n/a)</td><td>14.23 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.46 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>242.50 (n/a)</td><td>179.10 (n/a)</td><td>185.50 (n/a)</td><td>105.90 (n/a)</td><td>51.35 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.40 (n/a)</td><td>168.46 (n/a)</td><td>177.00 (n/a)</td><td>121.40 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>333.70 (n/a)</td><td>191.62 (n/a)</td><td>164.90 (n/a)</td><td>140.20 (n/a)</td><td>80.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.00 (n/a)</td><td>156.04 (n/a)</td><td>166.90 (n/a)</td><td>112.00 (n/a)</td><td>34.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.40 (n/a)</td><td>149.82 (n/a)</td><td>154.00 (n/a)</td><td>122.90 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>336.60 (n/a)</td><td>201.92 (n/a)</td><td>191.90 (n/a)</td><td>125.10 (n/a)</td><td>81.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.60 (n/a)</td><td>205.48 (n/a)</td><td>207.40 (n/a)</td><td>174.10 (n/a)</td><td>19.26 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.90 (n/a)</td><td>162.70 (n/a)</td><td>169.50 (n/a)</td><td>124.80 (n/a)</td><td>37.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.80 (n/a)</td><td>187.62 (n/a)</td><td>188.60 (n/a)</td><td>148.60 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>158.62 (n/a)</td><td>158.80 (n/a)</td><td>121.60 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.80 (n/a)</td><td>147.46 (n/a)</td><td>144.40 (n/a)</td><td>129.40 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>161.80 (n/a)</td><td>169.50 (n/a)</td><td>123.40 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>243.80 (n/a)</td><td>175.32 (n/a)</td><td>166.90 (n/a)</td><td>109.40 (n/a)</td><td>49.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.30 (n/a)</td><td>163.06 (n/a)</td><td>158.20 (n/a)</td><td>138.20 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.50 (n/a)</td><td>209.44 (n/a)</td><td>194.10 (n/a)</td><td>170.90 (n/a)</td><td>45.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>193.36 (n/a)</td><td>192.80 (n/a)</td><td>148.70 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>209.42 (n/a)</td><td>214.70 (n/a)</td><td>160.20 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.30 (n/a)</td><td>166.78 (n/a)</td><td>168.50 (n/a)</td><td>125.70 (n/a)</td><td>24.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>224.50 (n/a)</td><td>164.98 (n/a)</td><td>174.90 (n/a)</td><td>108.70 (n/a)</td><td>48.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>169.90 (n/a)</td><td>141.56 (n/a)</td><td>143.80 (n/a)</td><td>114.70 (n/a)</td><td>20.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>227.00 (n/a)</td><td>189.26 (n/a)</td><td>219.10 (n/a)</td><td>132.10 (n/a)</td><td>46.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.50 (n/a)</td><td>169.36 (n/a)</td><td>155.80 (n/a)</td><td>135.80 (n/a)</td><td>37.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>219.40 (n/a)</td><td>163.20 (n/a)</td><td>154.60 (n/a)</td><td>94.80 (n/a)</td><td>47.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>219.20 (n/a)</td><td>180.04 (n/a)</td><td>193.40 (n/a)</td><td>95.80 (n/a)</td><td>48.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>295.70 (n/a)</td><td>235.42 (n/a)</td><td>238.60 (n/a)</td><td>176.30 (n/a)</td><td>49.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>226.90 (n/a)</td><td>157.80 (n/a)</td><td>131.90 (n/a)</td><td>129.50 (n/a)</td><td>42.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>222.10 (n/a)</td><td>154.38 (n/a)</td><td>127.60 (n/a)</td><td>123.70 (n/a)</td><td>42.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>227.90 (n/a)</td><td>159.24 (n/a)</td><td>157.60 (n/a)</td><td>125.40 (n/a)</td><td>41.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>201.60 (n/a)</td><td>161.06 (n/a)</td><td>176.70 (n/a)</td><td>122.50 (n/a)</td><td>35.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>293.80 (n/a)</td><td>169.10 (n/a)</td><td>131.30 (n/a)</td><td>123.00 (n/a)</td><td>72.32 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>249.00 (n/a)</td><td>177.72 (n/a)</td><td>165.30 (n/a)</td><td>130.20 (n/a)</td><td>46.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.60 (n/a)</td><td>159.96 (n/a)</td><td>155.10 (n/a)</td><td>122.60 (n/a)</td><td>28.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>217.80 (n/a)</td><td>192.30 (n/a)</td><td>206.50 (n/a)</td><td>145.40 (n/a)</td><td>30.49 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>4.21 (-2.88%)</td><td>4.12 (+0.52%)</td><td>4.12 (-1.47%)</td><td>4.05 (+14.53%)</td><td>0.06 <b>(-82.25%)</b></td><td>2319.40 (-12.69%)</td><td>2282.88 (-1.04%)</td><td>2282.40 (+1.49%)</td><td>2236.20 (+2.96%)</td><td>31.58 <b>(-84.21%)</b></td><td>1654.31 (-2.88%)</td><td>1620.74 (+0.52%)</td><td>1620.84 (-1.47%)</td><td>1594.99 (+14.53%)</td><td>22.54 <b>(-82.25%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>4.33 (n/a)</td><td>4.10 (n/a)</td><td>4.18 (n/a)</td><td>3.54 (n/a)</td><td>0.32 (n/a)</td><td>2656.50 (n/a)</td><td>2306.88 (n/a)</td><td>2248.80 (n/a)</td><td>2171.90 (n/a)</td><td>200.02 (n/a)</td><td>1703.33 (n/a)</td><td>1612.43 (n/a)</td><td>1645.03 (n/a)</td><td>1392.58 (n/a)</td><td>126.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.20 (-17.70%)</td><td>0.88 (-11.64%)</td><td>0.93 (-13.88%)</td><td>0.62 (-6.58%)</td><td>0.25 <b>(-22.99%)</b></td><td>356.60 (+7.02%)</td><td>267.72 (+11.02%)</td><td>238.20 (+16.08%)</td><td>184.80 <b>(+21.50%)</b></td><td>78.65 (-0.40%)</td><td>51.06 (-17.70%)</td><td>37.74 (-11.64%)</td><td>39.61 (-13.88%)</td><td>26.46 (-6.58%)</td><td>10.73 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.45 (n/a)</td><td>1.00 (n/a)</td><td>1.08 (n/a)</td><td>0.66 (n/a)</td><td>0.33 (n/a)</td><td>333.20 (n/a)</td><td>241.14 (n/a)</td><td>205.20 (n/a)</td><td>152.10 (n/a)</td><td>78.96 (n/a)</td><td>62.04 (n/a)</td><td>42.71 (n/a)</td><td>46.00 (n/a)</td><td>28.32 (n/a)</td><td>13.93 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.30 (+10.92%)</td><td>0.99 (+2.76%)</td><td>0.88 (-11.19%)</td><td>0.71 (+0.56%)</td><td>0.26 <b>(+35.38%)</b></td><td>312.60 (-0.54%)</td><td>235.76 (-0.76%)</td><td>251.90 (+12.56%)</td><td>170.20 (-9.85%)</td><td>60.20 (+17.15%)</td><td>55.43 (+10.92%)</td><td>42.27 (+2.76%)</td><td>37.46 (-11.19%)</td><td>30.19 (+0.56%)</td><td>11.11 <b>(+35.38%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.17 (n/a)</td><td>0.96 (n/a)</td><td>0.99 (n/a)</td><td>0.70 (n/a)</td><td>0.19 (n/a)</td><td>314.30 (n/a)</td><td>237.56 (n/a)</td><td>223.80 (n/a)</td><td>188.80 (n/a)</td><td>51.38 (n/a)</td><td>49.98 (n/a)</td><td>41.13 (n/a)</td><td>42.18 (n/a)</td><td>30.02 (n/a)</td><td>8.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.52 (-0.06%)</td><td>0.52 (-0.04%)</td><td>0.52 (+0.05%)</td><td>0.52 (-0.04%)</td><td>0.00 (+17.15%)</td><td>48557.30 (+0.04%)</td><td>48486.46 (+0.04%)</td><td>48450.40 (-0.05%)</td><td>48433.80 (+0.06%)</td><td>60.80 (+17.25%)</td><td>354.71 (-0.06%)</td><td>354.32 (-0.04%)</td><td>354.59 (+0.05%)</td><td>353.81 (-0.04%)</td><td>0.44 (+17.14%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48536.60 (n/a)</td><td>48469.22 (n/a)</td><td>48476.60 (n/a)</td><td>48403.90 (n/a)</td><td>51.85 (n/a)</td><td>354.93 (n/a)</td><td>354.45 (n/a)</td><td>354.40 (n/a)</td><td>353.96 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (+0.03%)</td><td>0.21 (-0.17%)</td><td>0.21 (-0.22%)</td><td>0.21 (-0.00%)</td><td>0.00 (+13.66%)</td><td>119505.70 (+0.00%)</td><td>118843.18 (+0.18%)</td><td>118740.00 (+0.22%)</td><td>118101.40 (-0.03%)</td><td>585.29 (+13.58%)</td><td>145.47 (+0.03%)</td><td>144.56 (-0.17%)</td><td>144.68 (-0.22%)</td><td>143.76 (-0.00%)</td><td>0.71 (+13.67%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119502.50 (n/a)</td><td>118635.40 (n/a)</td><td>118479.90 (n/a)</td><td>118136.70 (n/a)</td><td>515.30 (n/a)</td><td>145.42 (n/a)</td><td>144.81 (n/a)</td><td>145.00 (n/a)</td><td>143.76 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.90 (+0.29%)</td><td>0.89 (-0.23%)</td><td>0.89 (-0.21%)</td><td>0.87 (-0.74%)</td><td>0.01 <b>(+48.76%)</b></td><td>28765.60 (+0.74%)</td><td>28321.40 (+0.23%)</td><td>28314.30 (+0.21%)</td><td>27894.80 (-0.29%)</td><td>307.99 <b>(+49.44%)</b></td><td>615.88 (+0.29%)</td><td>606.66 (-0.23%)</td><td>606.76 (-0.21%)</td><td>597.24 (-0.74%)</td><td>6.59 <b>(+48.76%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28554.10 (n/a)</td><td>28255.80 (n/a)</td><td>28255.40 (n/a)</td><td>27975.50 (n/a)</td><td>206.10 (n/a)</td><td>614.10 (n/a)</td><td>608.04 (n/a)</td><td>608.02 (n/a)</td><td>601.66 (n/a)</td><td>4.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.50 (-1.33%)</td><td>3.38 (-2.28%)</td><td>3.37 (-3.46%)</td><td>3.30 (-1.00%)</td><td>0.07 <b>(-25.47%)</b></td><td>7623.10 (+1.01%)</td><td>7446.60 (+2.30%)</td><td>7468.50 (+3.58%)</td><td>7192.50 (+1.35%)</td><td>156.75 <b>(-23.87%)</b></td><td>2388.59 (-1.33%)</td><td>2307.91 (-2.28%)</td><td>2300.30 (-3.46%)</td><td>2253.65 (-1.00%)</td><td>49.35 <b>(-25.47%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>3.55 (n/a)</td><td>3.46 (n/a)</td><td>3.49 (n/a)</td><td>3.33 (n/a)</td><td>0.10 (n/a)</td><td>7547.10 (n/a)</td><td>7278.98 (n/a)</td><td>7210.10 (n/a)</td><td>7097.00 (n/a)</td><td>205.90 (n/a)</td><td>2420.72 (n/a)</td><td>2361.70 (n/a)</td><td>2382.74 (n/a)</td><td>2276.36 (n/a)</td><td>66.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>2.94 (-7.58%)</td><td>2.82 (-5.01%)</td><td>2.81 (-6.57%)</td><td>2.74 (-1.69%)</td><td>0.08 <b>(-51.24%)</b></td><td>9183.50 (+1.72%)</td><td>8920.94 (+5.11%)</td><td>8940.20 (+7.03%)</td><td>8557.40 (+8.20%)</td><td>235.52 <b>(-46.66%)</b></td><td>2007.60 (-7.58%)</td><td>1926.88 (-5.01%)</td><td>1921.63 (-6.57%)</td><td>1870.73 (-1.69%)</td><td>51.63 <b>(-51.24%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>3.18 (n/a)</td><td>2.97 (n/a)</td><td>3.01 (n/a)</td><td>2.79 (n/a)</td><td>0.16 (n/a)</td><td>9027.90 (n/a)</td><td>8487.46 (n/a)</td><td>8353.20 (n/a)</td><td>7908.60 (n/a)</td><td>441.54 (n/a)</td><td>2172.29 (n/a)</td><td>2028.55 (n/a)</td><td>2056.69 (n/a)</td><td>1902.97 (n/a)</td><td>105.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.28 (-0.67%)</td><td>3.12 (-2.85%)</td><td>3.15 (-0.88%)</td><td>2.89 (-7.48%)</td><td>0.14 <b>(+68.95%)</b></td><td>8696.90 (+8.09%)</td><td>8075.92 (+3.06%)</td><td>8000.90 (+0.89%)</td><td>7669.00 (+0.67%)</td><td>377.09 <b>(+86.61%)</b></td><td>2240.18 (-0.67%)</td><td>2130.89 (-2.85%)</td><td>2147.24 (-0.88%)</td><td>1975.41 (-7.48%)</td><td>96.17 <b>(+68.95%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>3.30 (n/a)</td><td>3.21 (n/a)</td><td>3.17 (n/a)</td><td>3.13 (n/a)</td><td>0.08 (n/a)</td><td>8046.30 (n/a)</td><td>7836.36 (n/a)</td><td>7930.30 (n/a)</td><td>7617.70 (n/a)</td><td>202.08 (n/a)</td><td>2255.25 (n/a)</td><td>2193.50 (n/a)</td><td>2166.36 (n/a)</td><td>2135.14 (n/a)</td><td>56.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.79 (-0.02%)</td><td>0.79 (+0.01%)</td><td>0.79 (+0.09%)</td><td>0.78 (-0.02%)</td><td>0.00 (+18.95%)</td><td>96313.40 (+0.02%)</td><td>96170.74 (-0.01%)</td><td>96112.20 (-0.09%)</td><td>96099.70 (+0.02%)</td><td>93.88 (+18.97%)</td><td>715.09 (-0.02%)</td><td>714.56 (+0.01%)</td><td>714.99 (+0.09%)</td><td>713.50 (-0.02%)</td><td>0.70 (+18.94%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96292.40 (n/a)</td><td>96182.56 (n/a)</td><td>96195.70 (n/a)</td><td>96079.90 (n/a)</td><td>78.91 (n/a)</td><td>715.23 (n/a)</td><td>714.47 (n/a)</td><td>714.37 (n/a)</td><td>713.65 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.73 (+0.30%)</td><td>0.73 (+0.05%)</td><td>0.73 (+0.00%)</td><td>0.73 (-0.06%)</td><td>0.00 <b>(+278.61%)</b></td><td>103456.20 (+0.06%)</td><td>103256.14 (-0.05%)</td><td>103293.20 (-0.00%)</td><td>102967.70 (-0.30%)</td><td>177.72 <b>(+277.60%)</b></td><td>667.39 (+0.30%)</td><td>665.53 (+0.05%)</td><td>665.29 (+0.00%)</td><td>664.24 (-0.06%)</td><td>1.15 <b>(+278.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103393.50 (n/a)</td><td>103311.40 (n/a)</td><td>103296.70 (n/a)</td><td>103273.00 (n/a)</td><td>47.07 (n/a)</td><td>665.42 (n/a)</td><td>665.17 (n/a)</td><td>665.26 (n/a)</td><td>664.64 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.70 (+0.44%)</td><td>0.70 (+0.25%)</td><td>0.70 (+0.12%)</td><td>0.69 (+0.20%)</td><td>0.00 <b>(+98.75%)</b></td><td>108732.40 (-0.20%)</td><td>108446.74 (-0.25%)</td><td>108556.50 (-0.12%)</td><td>108128.70 (-0.44%)</td><td>274.56 <b>(+97.44%)</b></td><td>635.53 (+0.44%)</td><td>633.67 (+0.25%)</td><td>633.03 (+0.12%)</td><td>632.01 (+0.20%)</td><td>1.61 <b>(+98.75%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108945.40 (n/a)</td><td>108713.24 (n/a)</td><td>108681.80 (n/a)</td><td>108601.40 (n/a)</td><td>139.06 (n/a)</td><td>632.77 (n/a)</td><td>632.12 (n/a)</td><td>632.30 (n/a)</td><td>630.77 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>6.80 (-4.60%)</td><td>6.22 (-9.46%)</td><td>6.46 (-6.20%)</td><td>4.87 <b>(-25.12%)</b></td><td>0.77 <b>(+190.97%)</b></td><td>1829.30 <b>(+33.54%)</b></td><td>1454.70 (+11.93%)</td><td>1379.80 (+6.61%)</td><td>1311.40 (+4.81%)</td><td>212.48 <b>(+318.68%)</b></td><td>409.38 (-4.60%)</td><td>374.48 (-9.46%)</td><td>389.10 (-6.20%)</td><td>293.48 <b>(-25.12%)</b></td><td>46.48 <b>(+190.97%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.12 (n/a)</td><td>6.87 (n/a)</td><td>6.89 (n/a)</td><td>6.51 (n/a)</td><td>0.27 (n/a)</td><td>1369.90 (n/a)</td><td>1299.66 (n/a)</td><td>1294.20 (n/a)</td><td>1251.20 (n/a)</td><td>50.75 (n/a)</td><td>429.10 (n/a)</td><td>413.59 (n/a)</td><td>414.82 (n/a)</td><td>391.91 (n/a)</td><td>15.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>7.04 (+0.92%)</td><td>5.95 (-5.59%)</td><td>6.34 (-3.26%)</td><td>4.28 (-9.79%)</td><td>1.18 <b>(+32.24%)</b></td><td>2080.60 (+10.86%)</td><td>1551.90 (+7.64%)</td><td>1405.00 (+3.37%)</td><td>1266.40 (-0.92%)</td><td>345.05 <b>(+39.98%)</b></td><td>423.94 (+0.92%)</td><td>358.49 (-5.59%)</td><td>382.10 (-3.26%)</td><td>258.04 (-9.79%)</td><td>71.10 <b>(+32.24%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.97 (n/a)</td><td>6.30 (n/a)</td><td>6.56 (n/a)</td><td>4.75 (n/a)</td><td>0.89 (n/a)</td><td>1876.80 (n/a)</td><td>1441.70 (n/a)</td><td>1359.20 (n/a)</td><td>1278.10 (n/a)</td><td>246.50 (n/a)</td><td>420.06 (n/a)</td><td>379.73 (n/a)</td><td>394.98 (n/a)</td><td>286.05 (n/a)</td><td>53.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>6.75 (+2.71%)</td><td>6.42 (+0.96%)</td><td>6.50 (+2.12%)</td><td>5.92 (-3.78%)</td><td>0.32 <b>(+94.21%)</b></td><td>1505.70 (+3.93%)</td><td>1391.80 (-0.80%)</td><td>1371.80 (-2.07%)</td><td>1321.30 (-2.65%)</td><td>71.38 <b>(+97.68%)</b></td><td>406.32 (+2.71%)</td><td>386.53 (+0.96%)</td><td>391.37 (+2.12%)</td><td>356.57 (-3.78%)</td><td>19.15 <b>(+94.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.57 (n/a)</td><td>6.36 (n/a)</td><td>6.36 (n/a)</td><td>6.15 (n/a)</td><td>0.16 (n/a)</td><td>1448.70 (n/a)</td><td>1403.06 (n/a)</td><td>1400.80 (n/a)</td><td>1357.20 (n/a)</td><td>36.11 (n/a)</td><td>395.59 (n/a)</td><td>382.84 (n/a)</td><td>383.25 (n/a)</td><td>370.59 (n/a)</td><td>9.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>7.97 (-0.56%)</td><td>7.75 (+0.89%)</td><td>7.92 (+0.30%)</td><td>7.03 (-3.17%)</td><td>0.41 (+11.03%)</td><td>4962.50 (+3.28%)</td><td>4509.74 (-0.83%)</td><td>4400.50 (-0.29%)</td><td>4371.90 (+0.56%)</td><td>253.68 (+15.41%)</td><td>491.20 (-0.56%)</td><td>477.31 (+0.89%)</td><td>488.01 (+0.30%)</td><td>432.75 (-3.17%)</td><td>24.99 (+11.03%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>8.02 (n/a)</td><td>7.68 (n/a)</td><td>7.90 (n/a)</td><td>7.26 (n/a)</td><td>0.37 (n/a)</td><td>4805.10 (n/a)</td><td>4547.50 (n/a)</td><td>4413.50 (n/a)</td><td>4347.60 (n/a)</td><td>219.80 (n/a)</td><td>493.95 (n/a)</td><td>473.11 (n/a)</td><td>486.57 (n/a)</td><td>446.92 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>7.69 (-3.60%)</td><td>7.51 (-2.12%)</td><td>7.61 (+0.10%)</td><td>7.05 (-6.83%)</td><td>0.26 <b>(+53.03%)</b></td><td>4942.50 (+7.33%)</td><td>4644.46 (+2.23%)</td><td>4579.50 (-0.10%)</td><td>4533.80 (+3.73%)</td><td>167.97 <b>(+71.84%)</b></td><td>473.67 (-3.60%)</td><td>462.84 (-2.12%)</td><td>468.93 (+0.10%)</td><td>434.49 (-6.83%)</td><td>16.00 <b>(+53.03%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.98 (n/a)</td><td>7.68 (n/a)</td><td>7.61 (n/a)</td><td>7.57 (n/a)</td><td>0.17 (n/a)</td><td>4604.80 (n/a)</td><td>4542.98 (n/a)</td><td>4584.10 (n/a)</td><td>4370.70 (n/a)</td><td>97.75 (n/a)</td><td>491.33 (n/a)</td><td>472.88 (n/a)</td><td>468.47 (n/a)</td><td>466.36 (n/a)</td><td>10.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>7.74 (+3.83%)</td><td>7.33 (-0.92%)</td><td>7.33 (-1.26%)</td><td>6.84 (-5.98%)</td><td>0.33 <b>(+344.00%)</b></td><td>5097.90 (+6.35%)</td><td>4763.82 (+1.08%)</td><td>4753.40 (+1.28%)</td><td>4504.60 (-3.69%)</td><td>216.42 <b>(+356.56%)</b></td><td>476.73 (+3.83%)</td><td>451.52 (-0.92%)</td><td>451.78 (-1.26%)</td><td>421.25 (-5.98%)</td><td>20.14 <b>(+344.00%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.45 (n/a)</td><td>7.40 (n/a)</td><td>7.43 (n/a)</td><td>7.27 (n/a)</td><td>0.07 (n/a)</td><td>4793.30 (n/a)</td><td>4712.88 (n/a)</td><td>4693.40 (n/a)</td><td>4677.10 (n/a)</td><td>47.40 (n/a)</td><td>459.15 (n/a)</td><td>455.70 (n/a)</td><td>457.56 (n/a)</td><td>448.02 (n/a)</td><td>4.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.79 (-0.01%)</td><td>0.79 (+0.00%)</td><td>0.79 (+0.02%)</td><td>0.79 (+0.04%)</td><td>0.00 <b>(-25.43%)</b></td><td>95449.60 (-0.04%)</td><td>95412.38 (-0.00%)</td><td>95392.30 (-0.02%)</td><td>95384.90 (+0.01%)</td><td>33.87 <b>(-25.44%)</b></td><td>720.44 (-0.01%)</td><td>720.24 (+0.00%)</td><td>720.39 (+0.02%)</td><td>719.96 (+0.04%)</td><td>0.26 <b>(-25.42%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95489.30 (n/a)</td><td>95415.82 (n/a)</td><td>95408.40 (n/a)</td><td>95377.60 (n/a)</td><td>45.42 (n/a)</td><td>720.50 (n/a)</td><td>720.21 (n/a)</td><td>720.27 (n/a)</td><td>719.66 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.74 (+0.01%)</td><td>0.74 (+0.01%)</td><td>0.74 (+0.02%)</td><td>0.74 (-0.02%)</td><td>0.00 <b>(+56.34%)</b></td><td>102665.80 (+0.02%)</td><td>102598.92 (-0.01%)</td><td>102584.60 (-0.02%)</td><td>102569.40 (-0.01%)</td><td>38.58 <b>(+56.17%)</b></td><td>669.98 (+0.01%)</td><td>669.79 (+0.01%)</td><td>669.88 (+0.02%)</td><td>669.35 (-0.02%)</td><td>0.25 <b>(+56.32%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102646.00 (n/a)</td><td>102610.64 (n/a)</td><td>102610.20 (n/a)</td><td>102576.90 (n/a)</td><td>24.70 (n/a)</td><td>669.93 (n/a)</td><td>669.71 (n/a)</td><td>669.71 (n/a)</td><td>669.48 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.70 (+0.07%)</td><td>0.70 (+0.07%)</td><td>0.70 (+0.04%)</td><td>0.70 (+0.08%)</td><td>0.00 (-6.72%)</td><td>107485.30 (-0.08%)</td><td>107380.30 (-0.07%)</td><td>107364.30 (-0.04%)</td><td>107308.70 (-0.07%)</td><td>73.59 (-6.86%)</td><td>640.39 (+0.07%)</td><td>639.96 (+0.07%)</td><td>640.06 (+0.04%)</td><td>639.34 (+0.08%)</td><td>0.44 (-6.72%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107576.30 (n/a)</td><td>107450.88 (n/a)</td><td>107406.40 (n/a)</td><td>107388.70 (n/a)</td><td>79.00 (n/a)</td><td>639.91 (n/a)</td><td>639.54 (n/a)</td><td>639.81 (n/a)</td><td>638.80 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.66 (-13.57%)</td><td>3.34 (-2.43%)</td><td>3.16 (-4.29%)</td><td>3.12 (+4.07%)</td><td>0.27 <b>(-46.57%)</b></td><td>2586.50 (-3.92%)</td><td>2428.62 (+1.35%)</td><td>2551.10 (+4.48%)</td><td>2201.50 (+15.70%)</td><td>193.07 <b>(-40.95%)</b></td><td>960.21 (-13.57%)</td><td>874.98 (-2.43%)</td><td>828.63 (-4.29%)</td><td>817.28 (+4.07%)</td><td>71.64 <b>(-46.57%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>4.24 (n/a)</td><td>3.42 (n/a)</td><td>3.30 (n/a)</td><td>2.99 (n/a)</td><td>0.51 (n/a)</td><td>2691.90 (n/a)</td><td>2396.32 (n/a)</td><td>2441.60 (n/a)</td><td>1902.70 (n/a)</td><td>326.98 (n/a)</td><td>1111.03 (n/a)</td><td>896.72 (n/a)</td><td>865.79 (n/a)</td><td>785.29 (n/a)</td><td>134.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.39 <b>(-26.02%)</b></td><td>0.35 (-11.86%)</td><td>0.35 (+0.86%)</td><td>0.29 (+8.14%)</td><td>0.03 <b>(-69.26%)</b></td><td>4224.00 (-7.53%)</td><td>3630.26 (+7.70%)</td><td>3552.00 (-0.85%)</td><td>3216.10 <b>(+35.17%)</b></td><td>366.59 <b>(-59.49%)</b></td><td>20.87 <b>(-26.02%)</b></td><td>18.63 (-11.86%)</td><td>18.89 (+0.86%)</td><td>15.89 (+8.14%)</td><td>1.78 <b>(-69.26%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.52 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>4567.80 (n/a)</td><td>3370.58 (n/a)</td><td>3582.60 (n/a)</td><td>2379.30 (n/a)</td><td>904.98 (n/a)</td><td>28.21 (n/a)</td><td>21.14 (n/a)</td><td>18.73 (n/a)</td><td>14.69 (n/a)</td><td>5.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>4.96 (-0.14%)</td><td>4.30 (+4.30%)</td><td>4.65 (+17.59%)</td><td>3.15 (-7.09%)</td><td>0.78 (+18.20%)</td><td>2114.10 (+7.63%)</td><td>1595.32 (-3.16%)</td><td>1430.30 (-14.96%)</td><td>1340.20 (+0.15%)</td><td>328.16 <b>(+27.34%)</b></td><td>1533.56 (-0.14%)</td><td>1327.53 (+4.30%)</td><td>1436.87 (+17.59%)</td><td>972.14 (-7.09%)</td><td>240.05 (+18.20%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>4.97 (n/a)</td><td>4.12 (n/a)</td><td>3.95 (n/a)</td><td>3.39 (n/a)</td><td>0.66 (n/a)</td><td>1964.20 (n/a)</td><td>1647.44 (n/a)</td><td>1681.90 (n/a)</td><td>1338.20 (n/a)</td><td>257.70 (n/a)</td><td>1535.75 (n/a)</td><td>1272.81 (n/a)</td><td>1221.95 (n/a)</td><td>1046.35 (n/a)</td><td>203.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>13.43 (n/a)</td><td>12.28 (n/a)</td><td>12.74 (n/a)</td><td>10.45 (n/a)</td><td>1.24 (n/a)</td><td>13.42 (n/a)</td><td>12.27 (n/a)</td><td>12.74 (n/a)</td><td>10.45 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>24.52 (-2.13%)</td><td>23.75 (-1.62%)</td><td>24.26 (+0.66%)</td><td>22.04 (-6.37%)</td><td>1.01 <b>(+77.32%)</b></td><td>24.50 (-2.13%)</td><td>23.74 (-1.62%)</td><td>24.24 (+0.66%)</td><td>22.03 (-6.37%)</td><td>1.01 <b>(+77.32%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>25.05 (n/a)</td><td>24.14 (n/a)</td><td>24.10 (n/a)</td><td>23.54 (n/a)</td><td>0.57 (n/a)</td><td>25.04 (n/a)</td><td>24.13 (n/a)</td><td>24.08 (n/a)</td><td>23.53 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>40.86 (-2.14%)</td><td>40.01 (+0.66%)</td><td>39.86 (+1.33%)</td><td>39.39 (+1.89%)</td><td>0.64 <b>(-46.22%)</b></td><td>40.84 (-2.14%)</td><td>39.98 (+0.66%)</td><td>39.84 (+1.33%)</td><td>39.36 (+1.89%)</td><td>0.63 <b>(-46.22%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>41.76 (n/a)</td><td>39.75 (n/a)</td><td>39.33 (n/a)</td><td>38.66 (n/a)</td><td>1.18 (n/a)</td><td>41.73 (n/a)</td><td>39.72 (n/a)</td><td>39.31 (n/a)</td><td>38.64 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>43.12 (-6.71%)</td><td>42.34 (-1.70%)</td><td>42.30 (-0.65%)</td><td>41.92 (+1.46%)</td><td>0.48 <b>(-74.21%)</b></td><td>43.09 (-6.71%)</td><td>42.31 (-1.70%)</td><td>42.28 (-0.65%)</td><td>41.89 (+1.46%)</td><td>0.48 <b>(-74.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>46.22 (n/a)</td><td>43.07 (n/a)</td><td>42.58 (n/a)</td><td>41.32 (n/a)</td><td>1.85 (n/a)</td><td>46.19 (n/a)</td><td>43.04 (n/a)</td><td>42.55 (n/a)</td><td>41.29 (n/a)</td><td>1.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>13.39 (n/a)</td><td>12.13 (n/a)</td><td>11.84 (n/a)</td><td>10.77 (n/a)</td><td>1.08 (n/a)</td><td>13.38 (n/a)</td><td>12.12 (n/a)</td><td>11.83 (n/a)</td><td>10.76 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>24.21 (-1.39%)</td><td>23.93 (+0.58%)</td><td>23.89 (-0.39%)</td><td>23.61 (+4.95%)</td><td>0.26 <b>(-66.16%)</b></td><td>24.19 (-1.39%)</td><td>23.92 (+0.58%)</td><td>23.88 (-0.39%)</td><td>23.60 (+4.95%)</td><td>0.26 <b>(-66.16%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>24.55 (n/a)</td><td>23.79 (n/a)</td><td>23.99 (n/a)</td><td>22.50 (n/a)</td><td>0.77 (n/a)</td><td>24.53 (n/a)</td><td>23.78 (n/a)</td><td>23.97 (n/a)</td><td>22.48 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>40.28 (-1.48%)</td><td>36.34 (-8.10%)</td><td>39.50 (+0.46%)</td><td>23.07 <b>(-39.61%)</b></td><td>7.44 <b>(+524.85%)</b></td><td>40.26 (-1.48%)</td><td>36.32 (-8.10%)</td><td>39.48 (+0.46%)</td><td>23.05 <b>(-39.61%)</b></td><td>7.44 <b>(+524.85%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>40.89 (n/a)</td><td>39.55 (n/a)</td><td>39.32 (n/a)</td><td>38.20 (n/a)</td><td>1.19 (n/a)</td><td>40.86 (n/a)</td><td>39.52 (n/a)</td><td>39.29 (n/a)</td><td>38.17 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>44.08 (-3.81%)</td><td>38.62 (-8.18%)</td><td>41.91 (-0.28%)</td><td>23.62 <b>(-41.02%)</b></td><td>8.45 <b>(+257.59%)</b></td><td>44.05 (-3.81%)</td><td>38.60 (-8.18%)</td><td>41.89 (-0.28%)</td><td>23.61 <b>(-41.02%)</b></td><td>8.44 <b>(+257.59%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>45.82 (n/a)</td><td>42.06 (n/a)</td><td>42.03 (n/a)</td><td>40.05 (n/a)</td><td>2.36 (n/a)</td><td>45.79 (n/a)</td><td>42.04 (n/a)</td><td>42.01 (n/a)</td><td>40.02 (n/a)</td><td>2.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>9.77 (+5.09%)</td><td>8.98 (+8.05%)</td><td>9.19 (+7.69%)</td><td>8.00 (+15.75%)</td><td>0.66 <b>(-25.69%)</b></td><td>9.75 (+5.09%)</td><td>8.97 (+8.05%)</td><td>9.17 (+7.69%)</td><td>7.98 (+15.75%)</td><td>0.66 <b>(-25.69%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.29 (n/a)</td><td>8.31 (n/a)</td><td>8.53 (n/a)</td><td>6.91 (n/a)</td><td>0.89 (n/a)</td><td>9.27 (n/a)</td><td>8.30 (n/a)</td><td>8.51 (n/a)</td><td>6.90 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.04 (+4.74%)</td><td>0.92 (+8.24%)</td><td>0.88 (+11.36%)</td><td>0.85 (+12.77%)</td><td>0.08 <b>(-20.74%)</b></td><td>1.02 (+4.74%)</td><td>0.90 (+8.24%)</td><td>0.87 (+11.36%)</td><td>0.84 (+12.77%)</td><td>0.08 <b>(-20.74%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.99 (n/a)</td><td>0.85 (n/a)</td><td>0.79 (n/a)</td><td>0.75 (n/a)</td><td>0.10 (n/a)</td><td>0.98 (n/a)</td><td>0.83 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.33 (+17.12%)</td><td>1.22 (+19.00%)</td><td>1.23 (+18.74%)</td><td>1.08 <b>(+21.33%)</b></td><td>0.09 (+2.47%)</td><td>1.31 (+17.12%)</td><td>1.21 (+19.00%)</td><td>1.21 (+18.74%)</td><td>1.07 <b>(+21.33%)</b></td><td>0.09 (+2.47%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.13 (n/a)</td><td>1.02 (n/a)</td><td>1.03 (n/a)</td><td>0.89 (n/a)</td><td>0.09 (n/a)</td><td>1.12 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>0.88 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>18.34 (-5.36%)</td><td>16.61 (+0.91%)</td><td>16.18 (+0.40%)</td><td>15.98 (+8.13%)</td><td>0.98 <b>(-44.08%)</b></td><td>18.13 (-5.36%)</td><td>16.42 (+0.91%)</td><td>16.00 (+0.40%)</td><td>15.80 (+8.13%)</td><td>0.97 <b>(-44.08%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>19.38 (n/a)</td><td>16.46 (n/a)</td><td>16.12 (n/a)</td><td>14.78 (n/a)</td><td>1.76 (n/a)</td><td>19.15 (n/a)</td><td>16.27 (n/a)</td><td>15.93 (n/a)</td><td>14.61 (n/a)</td><td>1.74 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>14.34 (+6.57%)</td><td>13.63 (+4.55%)</td><td>13.37 (+3.21%)</td><td>13.07 (+3.02%)</td><td>0.57 <b>(+89.97%)</b></td><td>14.09 (+6.57%)</td><td>13.39 (+4.55%)</td><td>13.14 (+3.21%)</td><td>12.84 (+3.02%)</td><td>0.56 <b>(+89.97%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.45 (n/a)</td><td>13.04 (n/a)</td><td>12.96 (n/a)</td><td>12.69 (n/a)</td><td>0.30 (n/a)</td><td>13.22 (n/a)</td><td>12.81 (n/a)</td><td>12.73 (n/a)</td><td>12.47 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>9.67 <b>(+23.87%)</b></td><td>8.10 (+16.58%)</td><td>8.08 (+12.26%)</td><td>6.71 (+11.67%)</td><td>1.22 <b>(+73.38%)</b></td><td>9.50 <b>(+23.87%)</b></td><td>7.96 (+16.58%)</td><td>7.94 (+12.26%)</td><td>6.60 (+11.67%)</td><td>1.20 <b>(+73.38%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.80 (n/a)</td><td>6.95 (n/a)</td><td>7.20 (n/a)</td><td>6.01 (n/a)</td><td>0.71 (n/a)</td><td>7.67 (n/a)</td><td>6.83 (n/a)</td><td>7.08 (n/a)</td><td>5.91 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>6.46 (+6.69%)</td><td>5.60 (+4.96%)</td><td>5.47 (-0.03%)</td><td>4.80 (+3.90%)</td><td>0.65 (+16.81%)</td><td>6.36 (+6.69%)</td><td>5.51 (+4.96%)</td><td>5.38 (-0.03%)</td><td>4.72 (+3.90%)</td><td>0.64 (+16.81%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.06 (n/a)</td><td>5.34 (n/a)</td><td>5.47 (n/a)</td><td>4.62 (n/a)</td><td>0.55 (n/a)</td><td>5.96 (n/a)</td><td>5.25 (n/a)</td><td>5.38 (n/a)</td><td>4.54 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>13.33 (n/a)</td><td>12.91 (n/a)</td><td>13.31 (n/a)</td><td>12.06 (n/a)</td><td>0.58 (n/a)</td><td>13.32 (n/a)</td><td>12.90 (n/a)</td><td>13.30 (n/a)</td><td>12.05 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>13.39 (n/a)</td><td>12.41 (n/a)</td><td>13.15 (n/a)</td><td>10.55 (n/a)</td><td>1.24 (n/a)</td><td>13.38 (n/a)</td><td>12.40 (n/a)</td><td>13.14 (n/a)</td><td>10.55 (n/a)</td><td>1.24 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.50 (n/a)</td><td>158.72 (n/a)</td><td>149.80 (n/a)</td><td>146.80 (n/a)</td><td>16.99 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.10 (n/a)</td><td>155.74 (n/a)</td><td>152.20 (n/a)</td><td>137.80 (n/a)</td><td>16.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>259.20 (n/a)</td><td>179.64 (n/a)</td><td>175.60 (n/a)</td><td>137.10 (n/a)</td><td>47.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>183.20 (n/a)</td><td>206.40 (n/a)</td><td>109.80 (n/a)</td><td>49.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>167.72 (n/a)</td><td>162.30 (n/a)</td><td>117.10 (n/a)</td><td>42.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.60 (n/a)</td><td>184.08 (n/a)</td><td>180.70 (n/a)</td><td>162.40 (n/a)</td><td>22.14 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.90 (n/a)</td><td>178.48 (n/a)</td><td>162.80 (n/a)</td><td>146.00 (n/a)</td><td>33.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>329.90 (n/a)</td><td>236.98 (n/a)</td><td>226.90 (n/a)</td><td>180.30 (n/a)</td><td>63.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.90 (n/a)</td><td>153.14 (n/a)</td><td>151.40 (n/a)</td><td>128.20 (n/a)</td><td>16.31 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>177.10 (n/a)</td><td>182.20 (n/a)</td><td>150.50 (n/a)</td><td>15.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>174.56 (n/a)</td><td>184.50 (n/a)</td><td>117.70 (n/a)</td><td>38.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.40 (n/a)</td><td>181.86 (n/a)</td><td>187.00 (n/a)</td><td>122.70 (n/a)</td><td>52.32 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>162.46 (n/a)</td><td>152.90 (n/a)</td><td>125.20 (n/a)</td><td>39.73 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>196.10 (n/a)</td><td>208.10 (n/a)</td><td>153.50 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>175.60 (n/a)</td><td>175.90 (n/a)</td><td>134.80 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.50 (n/a)</td><td>199.60 (n/a)</td><td>198.30 (n/a)</td><td>168.80 (n/a)</td><td>25.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>169.20 (n/a)</td><td>171.90 (n/a)</td><td>144.90 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>304.90 (n/a)</td><td>185.94 (n/a)</td><td>176.90 (n/a)</td><td>129.20 (n/a)</td><td>71.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>181.50 (n/a)</td><td>157.86 (n/a)</td><td>174.10 (n/a)</td><td>123.80 (n/a)</td><td>27.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>230.20 (n/a)</td><td>176.56 (n/a)</td><td>167.50 (n/a)</td><td>131.70 (n/a)</td><td>46.65 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>173.60 (n/a)</td><td>175.80 (n/a)</td><td>149.40 (n/a)</td><td>16.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>179.32 (n/a)</td><td>178.90 (n/a)</td><td>144.60 (n/a)</td><td>25.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>177.88 (n/a)</td><td>180.20 (n/a)</td><td>157.70 (n/a)</td><td>20.26 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>256.00 (n/a)</td><td>203.22 (n/a)</td><td>177.00 (n/a)</td><td>172.20 (n/a)</td><td>39.61 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>202.00 (n/a)</td><td>162.68 (n/a)</td><td>152.60 (n/a)</td><td>131.10 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>283.40 (n/a)</td><td>213.14 (n/a)</td><td>212.60 (n/a)</td><td>126.90 (n/a)</td><td>59.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.50 (n/a)</td><td>179.46 (n/a)</td><td>175.80 (n/a)</td><td>154.20 (n/a)</td><td>24.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>219.40 (n/a)</td><td>174.34 (n/a)</td><td>187.30 (n/a)</td><td>116.80 (n/a)</td><td>48.07 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>242.90 (n/a)</td><td>187.92 (n/a)</td><td>162.10 (n/a)</td><td>150.10 (n/a)</td><td>45.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>233.60 (n/a)</td><td>209.96 (n/a)</td><td>219.20 (n/a)</td><td>168.50 (n/a)</td><td>26.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>222.80 (n/a)</td><td>185.92 (n/a)</td><td>194.60 (n/a)</td><td>149.30 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>235.30 (n/a)</td><td>203.24 (n/a)</td><td>209.40 (n/a)</td><td>131.20 (n/a)</td><td>42.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(+31.97%)</b></td><td>0.03 <b>(+28.48%)</b></td><td>0.03 <b>(+42.14%)</b></td><td>0.02 (+15.83%)</td><td>0.00 <b>(+100.52%)</b></td><td>174.30 (-13.63%)</td><td>144.94 <b>(-21.29%)</b></td><td>131.20 <b>(-29.65%)</b></td><td>126.20 <b>(-24.25%)</b></td><td>22.31 <b>(+32.17%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.80 (n/a)</td><td>184.14 (n/a)</td><td>186.50 (n/a)</td><td>166.60 (n/a)</td><td>16.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+19.78%)</td><td>0.03 (+16.59%)</td><td>0.03 (+18.20%)</td><td>0.02 (+8.91%)</td><td>0.00 <b>(+53.10%)</b></td><td>199.60 (-8.19%)</td><td>161.48 (-13.61%)</td><td>157.90 (-15.43%)</td><td>135.40 (-16.52%)</td><td>23.73 (+18.77%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.40 (n/a)</td><td>186.92 (n/a)</td><td>186.70 (n/a)</td><td>162.20 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 <b>(+42.69%)</b></td><td>0.03 (+6.15%)</td><td>0.02 (-1.46%)</td><td>0.01 <b>(-41.11%)</b></td><td>0.01 <b>(+538.38%)</b></td><td>326.60 <b>(+69.75%)</b></td><td>185.90 (+7.69%)</td><td>171.40 (+1.48%)</td><td>114.40 <b>(-29.94%)</b></td><td>84.99 <b>(+647.00%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.40 (n/a)</td><td>172.62 (n/a)</td><td>168.90 (n/a)</td><td>163.30 (n/a)</td><td>11.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-8.71%)</td><td>0.03 (+9.95%)</td><td>0.03 (+17.83%)</td><td>0.02 (+4.45%)</td><td>0.00 (-18.12%)</td><td>199.00 (-4.28%)</td><td>158.88 (-10.05%)</td><td>155.00 (-15.12%)</td><td>129.00 (+9.51%)</td><td>30.53 (-12.10%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>176.64 (n/a)</td><td>182.60 (n/a)</td><td>117.80 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-2.22%)</td><td>0.03 (+12.63%)</td><td>0.03 (+15.20%)</td><td>0.02 (+8.19%)</td><td>0.00 (-16.39%)</td><td>206.60 (-7.56%)</td><td>154.62 (-12.27%)</td><td>149.30 (-13.15%)</td><td>126.60 (+2.34%)</td><td>31.04 (-18.16%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>176.24 (n/a)</td><td>171.90 (n/a)</td><td>123.70 (n/a)</td><td>37.93 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(+27.86%)</b></td><td>0.02 (+10.30%)</td><td>0.02 (+8.18%)</td><td>0.01 (-17.58%)</td><td>0.01 <b>(+113.35%)</b></td><td>298.20 <b>(+21.32%)</b></td><td>196.00 (-4.02%)</td><td>179.30 (-7.58%)</td><td>130.00 <b>(-21.83%)</b></td><td>63.69 <b>(+106.43%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>245.80 (n/a)</td><td>204.20 (n/a)</td><td>194.00 (n/a)</td><td>166.30 (n/a)</td><td>30.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(+39.61%)</b></td><td>0.03 <b>(+23.48%)</b></td><td>0.03 <b>(+23.69%)</b></td><td>0.02 (+13.85%)</td><td>0.00 <b>(+143.95%)</b></td><td>193.10 (-12.15%)</td><td>160.80 (-17.92%)</td><td>154.00 (-19.12%)</td><td>130.70 <b>(-28.38%)</b></td><td>24.32 <b>(+55.22%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.80 (n/a)</td><td>195.90 (n/a)</td><td>190.40 (n/a)</td><td>182.50 (n/a)</td><td>15.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (+14.64%)</td><td>0.02 (+6.01%)</td><td>0.02 (+15.62%)</td><td>0.01 (-19.99%)</td><td>0.01 <b>(+103.35%)</b></td><td>338.10 <b>(+24.99%)</b></td><td>220.86 (-0.74%)</td><td>188.40 (-13.50%)</td><td>165.90 (-12.78%)</td><td>70.36 <b>(+124.51%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.50 (n/a)</td><td>222.50 (n/a)</td><td>217.80 (n/a)</td><td>190.20 (n/a)</td><td>31.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 <b>(+20.24%)</b></td><td>0.06 <b>(+20.61%)</b></td><td>0.05 (+15.29%)</td><td>0.04 <b>(+89.01%)</b></td><td>0.01 (-16.91%)</td><td>192.80 <b>(-47.11%)</b></td><td>152.80 <b>(-24.59%)</b></td><td>162.90 (-13.26%)</td><td>105.30 (-16.82%)</td><td>34.33 <b>(-64.20%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>364.50 (n/a)</td><td>202.62 (n/a)</td><td>187.80 (n/a)</td><td>126.60 (n/a)</td><td>95.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (-6.39%)</td><td>0.05 (+11.79%)</td><td>0.05 <b>(+29.50%)</b></td><td>0.04 (+5.46%)</td><td>0.01 <b>(-22.78%)</b></td><td>201.40 (-5.18%)</td><td>155.56 (-12.52%)</td><td>154.60 <b>(-22.78%)</b></td><td>118.80 (+6.83%)</td><td>32.86 <b>(-21.60%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>177.82 (n/a)</td><td>200.20 (n/a)</td><td>111.20 (n/a)</td><td>41.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (+9.47%)</td><td>0.05 (-5.15%)</td><td>0.04 (-11.52%)</td><td>0.04 <b>(-22.23%)</b></td><td>0.01 <b>(+288.97%)</b></td><td>231.40 <b>(+28.63%)</b></td><td>183.80 (+8.81%)</td><td>190.60 (+12.98%)</td><td>143.50 (-8.66%)</td><td>37.26 <b>(+345.76%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>179.90 (n/a)</td><td>168.92 (n/a)</td><td>168.70 (n/a)</td><td>157.10 (n/a)</td><td>8.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (+2.02%)</td><td>0.05 (+7.01%)</td><td>0.05 (+18.99%)</td><td>0.04 (+0.98%)</td><td>0.01 (-3.49%)</td><td>192.00 (-0.98%)</td><td>160.16 (-7.02%)</td><td>158.70 (-15.94%)</td><td>106.50 (-2.02%)</td><td>33.72 (-6.08%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>172.26 (n/a)</td><td>188.80 (n/a)</td><td>108.70 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 <b>(+34.94%)</b></td><td>0.05 (+13.13%)</td><td>0.06 (+17.68%)</td><td>0.04 (-0.25%)</td><td>0.01 <b>(+223.04%)</b></td><td>189.30 (+0.26%)</td><td>155.46 (-9.19%)</td><td>144.50 (-15.00%)</td><td>118.40 <b>(-25.86%)</b></td><td>30.14 <b>(+149.22%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>188.80 (n/a)</td><td>171.20 (n/a)</td><td>170.00 (n/a)</td><td>159.70 (n/a)</td><td>12.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (-0.24%)</td><td>0.05 (+9.89%)</td><td>0.05 (+17.90%)</td><td>0.04 (-8.09%)</td><td>0.01 (+7.88%)</td><td>208.50 (+8.82%)</td><td>156.32 (-8.26%)</td><td>149.90 (-15.21%)</td><td>121.10 (+0.25%)</td><td>34.59 <b>(+21.33%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>170.40 (n/a)</td><td>176.80 (n/a)</td><td>120.80 (n/a)</td><td>28.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (+6.71%)</td><td>0.05 (+16.38%)</td><td>0.05 (+13.59%)</td><td>0.04 (+13.15%)</td><td>0.01 (-8.02%)</td><td>183.30 (-11.62%)</td><td>153.14 (-14.67%)</td><td>155.90 (-11.97%)</td><td>133.80 (-6.30%)</td><td>20.43 <b>(-27.32%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>179.46 (n/a)</td><td>177.10 (n/a)</td><td>142.80 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 <b>(-31.76%)</b></td><td>0.05 (-0.29%)</td><td>0.05 (+10.69%)</td><td>0.04 <b>(+20.79%)</b></td><td>0.01 <b>(-70.63%)</b></td><td>210.60 (-17.22%)</td><td>179.06 (-6.83%)</td><td>180.60 (-9.70%)</td><td>158.50 <b>(+46.49%)</b></td><td>20.40 <b>(-62.06%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>254.40 (n/a)</td><td>192.18 (n/a)</td><td>200.00 (n/a)</td><td>108.20 (n/a)</td><td>53.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-6.71%)</td><td>0.05 (+6.13%)</td><td>0.05 (+11.55%)</td><td>0.04 (+16.81%)</td><td>0.01 <b>(-37.51%)</b></td><td>220.70 (-14.39%)</td><td>183.06 (-8.33%)</td><td>178.60 (-10.34%)</td><td>152.10 (+7.19%)</td><td>26.32 <b>(-42.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.80 (n/a)</td><td>199.70 (n/a)</td><td>199.20 (n/a)</td><td>141.90 (n/a)</td><td>45.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-1.08%)</td><td>0.04 (+6.29%)</td><td>0.04 (+11.70%)</td><td>0.04 <b>(+22.53%)</b></td><td>0.00 <b>(-40.41%)</b></td><td>227.70 (-18.42%)</td><td>207.76 (-7.41%)</td><td>205.50 (-10.50%)</td><td>179.40 (+1.13%)</td><td>18.57 <b>(-51.10%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>279.10 (n/a)</td><td>224.38 (n/a)</td><td>229.60 (n/a)</td><td>177.40 (n/a)</td><td>37.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (+11.11%)</td><td>0.10 (+10.55%)</td><td>0.10 (+5.40%)</td><td>0.09 <b>(+23.42%)</b></td><td>0.01 (-7.57%)</td><td>180.40 (-18.99%)</td><td>158.78 (-10.21%)</td><td>162.80 (-5.13%)</td><td>131.50 (-9.99%)</td><td>18.09 <b>(-35.39%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>176.84 (n/a)</td><td>171.60 (n/a)</td><td>146.10 (n/a)</td><td>28.00 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (-0.29%)</td><td>0.10 (+6.08%)</td><td>0.11 <b>(+24.87%)</b></td><td>0.05 (-10.51%)</td><td>0.03 (+18.14%)</td><td>300.50 (+11.75%)</td><td>179.20 (-2.46%)</td><td>143.00 (-19.93%)</td><td>128.00 (+0.31%)</td><td>70.64 <b>(+33.92%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>268.90 (n/a)</td><td>183.72 (n/a)</td><td>178.60 (n/a)</td><td>127.60 (n/a)</td><td>52.75 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 <b>(+42.57%)</b></td><td>0.10 <b>(+20.28%)</b></td><td>0.11 (+19.47%)</td><td>0.09 (+11.83%)</td><td>0.02 <b>(+232.42%)</b></td><td>186.10 (-10.57%)</td><td>159.64 (-15.46%)</td><td>152.40 (-16.31%)</td><td>127.10 <b>(-29.86%)</b></td><td>24.33 <b>(+112.32%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>208.10 (n/a)</td><td>188.84 (n/a)</td><td>182.10 (n/a)</td><td>181.20 (n/a)</td><td>11.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (+7.97%)</td><td>0.10 (+17.30%)</td><td>0.10 <b>(+24.69%)</b></td><td>0.08 <b>(+68.19%)</b></td><td>0.02 <b>(-36.85%)</b></td><td>201.10 <b>(-40.56%)</b></td><td>161.26 <b>(-21.12%)</b></td><td>160.40 (-19.80%)</td><td>129.60 (-7.43%)</td><td>28.29 <b>(-64.83%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>338.30 (n/a)</td><td>204.44 (n/a)</td><td>200.00 (n/a)</td><td>140.00 (n/a)</td><td>80.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 <b>(+69.45%)</b></td><td>0.11 <b>(+35.84%)</b></td><td>0.11 <b>(+30.85%)</b></td><td>0.08 (+9.04%)</td><td>0.02 <b>(+466.45%)</b></td><td>193.60 (-8.29%)</td><td>149.68 <b>(-23.78%)</b></td><td>150.10 <b>(-23.57%)</b></td><td>108.30 <b>(-40.98%)</b></td><td>31.54 <b>(+203.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>211.10 (n/a)</td><td>196.38 (n/a)</td><td>196.40 (n/a)</td><td>183.50 (n/a)</td><td>10.41 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (-3.05%)</td><td>0.09 (-3.92%)</td><td>0.09 (-1.63%)</td><td>0.08 (-5.32%)</td><td>0.02 (+0.96%)</td><td>215.30 (+5.64%)</td><td>181.42 (+4.31%)</td><td>181.60 (+1.68%)</td><td>138.10 (+3.14%)</td><td>28.22 (+10.31%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>173.92 (n/a)</td><td>178.60 (n/a)</td><td>133.90 (n/a)</td><td>25.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (+17.92%)</td><td>0.11 <b>(+20.35%)</b></td><td>0.11 <b>(+21.07%)</b></td><td>0.09 <b>(+25.27%)</b></td><td>0.01 (-5.91%)</td><td>179.50 <b>(-20.19%)</b></td><td>156.44 (-17.28%)</td><td>155.30 (-17.39%)</td><td>139.80 (-15.17%)</td><td>14.95 <b>(-36.04%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>189.12 (n/a)</td><td>188.00 (n/a)</td><td>164.80 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (-0.17%)</td><td>0.08 (+7.01%)</td><td>0.08 (+8.17%)</td><td>0.07 <b>(+21.43%)</b></td><td>0.00 <b>(-52.12%)</b></td><td>224.60 (-17.67%)</td><td>211.64 (-7.36%)</td><td>206.30 (-7.57%)</td><td>200.60 (+0.15%)</td><td>10.65 <b>(-60.98%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>272.80 (n/a)</td><td>228.46 (n/a)</td><td>223.20 (n/a)</td><td>200.30 (n/a)</td><td>27.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.30 <b>(+30.74%)</b></td><td>0.23 <b>(+26.82%)</b></td><td>0.23 <b>(+29.05%)</b></td><td>0.17 (+13.52%)</td><td>0.05 <b>(+49.16%)</b></td><td>189.90 (-11.92%)</td><td>147.22 <b>(-20.32%)</b></td><td>144.30 <b>(-22.54%)</b></td><td>110.50 <b>(-23.48%)</b></td><td>30.09 (-1.13%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.60 (n/a)</td><td>184.76 (n/a)</td><td>186.30 (n/a)</td><td>144.40 (n/a)</td><td>30.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (-13.66%)</td><td>0.17 (-9.38%)</td><td>0.17 (-5.88%)</td><td>0.12 <b>(-21.57%)</b></td><td>0.03 (-5.22%)</td><td>281.90 <b>(+27.50%)</b></td><td>200.82 (+11.44%)</td><td>195.40 (+6.25%)</td><td>162.80 (+15.87%)</td><td>47.75 <b>(+43.78%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>221.10 (n/a)</td><td>180.20 (n/a)</td><td>183.90 (n/a)</td><td>140.50 (n/a)</td><td>33.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (-16.00%)</td><td>0.20 (-7.50%)</td><td>0.19 (-8.18%)</td><td>0.16 (-7.29%)</td><td>0.04 <b>(-21.97%)</b></td><td>205.70 (+7.87%)</td><td>169.90 (+7.17%)</td><td>174.50 (+8.93%)</td><td>127.50 (+19.05%)</td><td>34.42 (+1.03%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>190.70 (n/a)</td><td>158.54 (n/a)</td><td>160.20 (n/a)</td><td>107.10 (n/a)</td><td>34.07 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 (+11.25%)</td><td>0.21 (+5.98%)</td><td>0.19 (-5.62%)</td><td>0.17 <b>(+32.09%)</b></td><td>0.04 (-11.08%)</td><td>193.40 <b>(-24.31%)</b></td><td>162.50 (-7.75%)</td><td>168.20 (+5.99%)</td><td>122.70 (-10.11%)</td><td>27.02 <b>(-42.52%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>255.50 (n/a)</td><td>176.16 (n/a)</td><td>158.70 (n/a)</td><td>136.50 (n/a)</td><td>47.00 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 <b>(-43.27%)</b></td><td>0.17 <b>(-28.16%)</b></td><td>0.17 <b>(-22.01%)</b></td><td>0.16 (-11.14%)</td><td>0.01 <b>(-80.51%)</b></td><td>203.90 (+12.53%)</td><td>189.36 <b>(+33.80%)</b></td><td>190.60 <b>(+28.26%)</b></td><td>175.90 <b>(+76.25%)</b></td><td>12.30 <b>(-61.00%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>181.20 (n/a)</td><td>141.52 (n/a)</td><td>148.60 (n/a)</td><td>99.80 (n/a)</td><td>31.53 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (+0.73%)</td><td>0.21 (+17.29%)</td><td>0.21 <b>(+29.10%)</b></td><td>0.16 (+14.76%)</td><td>0.04 (-8.11%)</td><td>203.60 (-12.84%)</td><td>162.24 (-15.45%)</td><td>155.40 <b>(-22.53%)</b></td><td>130.40 (-0.76%)</td><td>31.18 (-16.68%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>233.60 (n/a)</td><td>191.88 (n/a)</td><td>200.60 (n/a)</td><td>131.40 (n/a)</td><td>37.42 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 <b>(+20.74%)</b></td><td>0.15 (+6.94%)</td><td>0.16 (+10.56%)</td><td>0.10 (-4.71%)</td><td>0.04 <b>(+73.56%)</b></td><td>342.90 (+4.93%)</td><td>235.94 (-2.86%)</td><td>206.80 (-9.54%)</td><td>168.90 (-17.21%)</td><td>70.44 <b>(+46.31%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>326.80 (n/a)</td><td>242.88 (n/a)</td><td>228.60 (n/a)</td><td>204.00 (n/a)</td><td>48.14 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+4.51%)</td><td>0.03 (+5.80%)</td><td>0.03 (+1.48%)</td><td>0.02 (+7.98%)</td><td>0.00 (-10.33%)</td><td>178.80 (-7.41%)</td><td>153.28 (-6.17%)</td><td>162.50 (-1.46%)</td><td>125.90 (-4.33%)</td><td>21.86 <b>(-21.82%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.10 (n/a)</td><td>163.36 (n/a)</td><td>164.90 (n/a)</td><td>131.60 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-16.59%)</td><td>0.03 (-12.06%)</td><td>0.03 (-14.31%)</td><td>0.02 (+0.56%)</td><td>0.00 <b>(-56.55%)</b></td><td>170.10 (-0.58%)</td><td>152.34 (+12.30%)</td><td>148.40 (+16.67%)</td><td>144.10 (+19.88%)</td><td>10.52 <b>(-48.91%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.10 (n/a)</td><td>135.66 (n/a)</td><td>127.20 (n/a)</td><td>120.20 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(+21.41%)</b></td><td>0.02 <b>(+28.68%)</b></td><td>0.02 (+14.01%)</td><td>0.02 <b>(+45.43%)</b></td><td>0.00 <b>(-23.44%)</b></td><td>220.30 <b>(-31.24%)</b></td><td>189.38 <b>(-24.66%)</b></td><td>195.30 (-12.26%)</td><td>159.70 (-17.64%)</td><td>25.44 <b>(-58.56%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>320.40 (n/a)</td><td>251.36 (n/a)</td><td>222.60 (n/a)</td><td>193.90 (n/a)</td><td>61.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(+50.83%)</b></td><td>0.02 <b>(+26.09%)</b></td><td>0.02 <b>(+26.46%)</b></td><td>0.02 (+7.50%)</td><td>0.01 <b>(+291.20%)</b></td><td>251.70 (-6.98%)</td><td>199.62 (-17.42%)</td><td>187.70 <b>(-20.94%)</b></td><td>147.40 <b>(-33.69%)</b></td><td>47.37 <b>(+148.87%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.60 (n/a)</td><td>241.72 (n/a)</td><td>237.40 (n/a)</td><td>222.30 (n/a)</td><td>19.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-3.82%)</td><td>0.02 (-3.84%)</td><td>0.02 (-2.60%)</td><td>0.02 (-4.04%)</td><td>0.00 (-8.86%)</td><td>188.10 (+4.21%)</td><td>167.18 (+3.79%)</td><td>171.60 (+2.63%)</td><td>132.40 (+4.01%)</td><td>20.77 (-4.15%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.50 (n/a)</td><td>161.08 (n/a)</td><td>167.20 (n/a)</td><td>127.30 (n/a)</td><td>21.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-11.35%)</td><td>0.03 (+0.96%)</td><td>0.03 (-7.57%)</td><td>0.02 <b>(+42.39%)</b></td><td>0.00 <b>(-52.23%)</b></td><td>166.20 <b>(-29.75%)</b></td><td>151.36 (-6.23%)</td><td>163.00 (+8.23%)</td><td>126.40 (+12.86%)</td><td>18.67 <b>(-61.90%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.60 (n/a)</td><td>161.42 (n/a)</td><td>150.60 (n/a)</td><td>112.00 (n/a)</td><td>49.01 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-8.12%)</td><td>0.02 (-2.24%)</td><td>0.02 (-5.20%)</td><td>0.02 (+0.72%)</td><td>0.00 <b>(-24.44%)</b></td><td>190.60 (-0.73%)</td><td>173.94 (+1.62%)</td><td>181.30 (+5.47%)</td><td>145.00 (+8.78%)</td><td>19.59 (-17.03%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.00 (n/a)</td><td>171.16 (n/a)</td><td>171.90 (n/a)</td><td>133.30 (n/a)</td><td>23.61 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+3.73%)</td><td>0.03 <b>(+23.49%)</b></td><td>0.03 <b>(+23.37%)</b></td><td>0.02 <b>(+36.46%)</b></td><td>0.01 <b>(-26.03%)</b></td><td>197.00 <b>(-26.71%)</b></td><td>148.22 <b>(-22.92%)</b></td><td>147.50 (-18.96%)</td><td>121.80 (-3.56%)</td><td>30.74 <b>(-49.18%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.80 (n/a)</td><td>192.30 (n/a)</td><td>182.00 (n/a)</td><td>126.30 (n/a)</td><td>60.50 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+9.91%)</td><td>0.03 (+5.31%)</td><td>0.03 (-2.75%)</td><td>0.02 <b>(+32.71%)</b></td><td>0.01 (-12.44%)</td><td>205.40 <b>(-24.62%)</b></td><td>161.70 (-7.91%)</td><td>148.50 (+2.84%)</td><td>123.70 (-9.04%)</td><td>35.35 <b>(-38.53%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>272.50 (n/a)</td><td>175.58 (n/a)</td><td>144.40 (n/a)</td><td>136.00 (n/a)</td><td>57.50 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-12.76%)</td><td>0.02 (+2.48%)</td><td>0.02 (+7.05%)</td><td>0.02 (+17.15%)</td><td>0.00 <b>(-46.28%)</b></td><td>198.90 (-14.64%)</td><td>167.00 (-5.86%)</td><td>165.90 (-6.59%)</td><td>144.20 (+14.63%)</td><td>22.78 <b>(-47.94%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>177.40 (n/a)</td><td>177.60 (n/a)</td><td>125.80 (n/a)</td><td>43.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+4.52%)</td><td>0.02 (+7.45%)</td><td>0.03 (+12.93%)</td><td>0.02 (+19.94%)</td><td>0.00 (-19.03%)</td><td>195.30 (-16.65%)</td><td>167.10 (-8.20%)</td><td>154.00 (-11.44%)</td><td>141.80 (-4.32%)</td><td>24.63 <b>(-32.60%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.30 (n/a)</td><td>182.02 (n/a)</td><td>173.90 (n/a)</td><td>148.20 (n/a)</td><td>36.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-11.19%)</td><td>0.02 (-0.76%)</td><td>0.02 (+4.20%)</td><td>0.02 (+3.24%)</td><td>0.00 <b>(-39.02%)</b></td><td>195.20 (-3.17%)</td><td>170.76 (-0.59%)</td><td>171.30 (-4.03%)</td><td>143.80 (+12.52%)</td><td>18.50 <b>(-31.54%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.60 (n/a)</td><td>171.78 (n/a)</td><td>178.50 (n/a)</td><td>127.80 (n/a)</td><td>27.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(+42.49%)</b></td><td>0.02 (+9.65%)</td><td>0.02 (+0.72%)</td><td>0.02 (-6.05%)</td><td>0.01 <b>(+172.68%)</b></td><td>246.90 (+6.42%)</td><td>193.40 (-5.36%)</td><td>197.40 (-0.70%)</td><td>128.50 <b>(-29.82%)</b></td><td>42.77 <b>(+95.56%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.00 (n/a)</td><td>204.36 (n/a)</td><td>198.80 (n/a)</td><td>183.10 (n/a)</td><td>21.87 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+13.78%)</td><td>0.02 (+10.25%)</td><td>0.02 (+9.35%)</td><td>0.02 (-7.13%)</td><td>0.00 <b>(+59.60%)</b></td><td>223.40 (+7.66%)</td><td>170.38 (-7.98%)</td><td>168.40 (-8.53%)</td><td>142.80 (-12.12%)</td><td>31.96 <b>(+51.89%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.50 (n/a)</td><td>185.16 (n/a)</td><td>184.10 (n/a)</td><td>162.50 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-10.75%)</td><td>0.02 (+2.54%)</td><td>0.02 (+0.97%)</td><td>0.02 (+1.88%)</td><td>0.00 (-16.47%)</td><td>256.90 (-1.83%)</td><td>209.50 (-3.32%)</td><td>224.10 (-0.97%)</td><td>162.90 (+12.11%)</td><td>41.03 (-6.87%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>261.70 (n/a)</td><td>216.70 (n/a)</td><td>226.30 (n/a)</td><td>145.30 (n/a)</td><td>44.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(+45.68%)</b></td><td>0.02 <b>(+26.83%)</b></td><td>0.02 <b>(+21.19%)</b></td><td>0.02 (+14.16%)</td><td>0.00 <b>(+386.82%)</b></td><td>193.70 (-12.39%)</td><td>171.62 (-19.91%)</td><td>180.90 (-17.47%)</td><td>138.70 <b>(-31.37%)</b></td><td>23.98 <b>(+195.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.10 (n/a)</td><td>214.28 (n/a)</td><td>219.20 (n/a)</td><td>202.10 (n/a)</td><td>8.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 <b>(+26.99%)</b></td><td>0.05 (+19.75%)</td><td>0.05 (+17.96%)</td><td>0.04 (+7.25%)</td><td>0.01 <b>(+65.75%)</b></td><td>201.20 (-6.77%)</td><td>156.76 (-15.28%)</td><td>160.20 (-15.24%)</td><td>125.80 <b>(-21.28%)</b></td><td>30.33 <b>(+22.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>185.04 (n/a)</td><td>189.00 (n/a)</td><td>159.80 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 <b>(+27.71%)</b></td><td>0.05 (+8.52%)</td><td>0.05 (+8.30%)</td><td>0.04 (-17.16%)</td><td>0.01 <b>(+209.24%)</b></td><td>228.90 <b>(+20.73%)</b></td><td>166.68 (-4.77%)</td><td>160.10 (-7.67%)</td><td>126.20 <b>(-21.66%)</b></td><td>37.85 <b>(+200.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.60 (n/a)</td><td>175.02 (n/a)</td><td>173.40 (n/a)</td><td>161.10 (n/a)</td><td>12.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-0.05%)</td><td>0.04 (+14.10%)</td><td>0.04 (+5.59%)</td><td>0.04 <b>(+46.98%)</b></td><td>0.01 <b>(-36.24%)</b></td><td>223.70 <b>(-31.94%)</b></td><td>197.68 (-15.20%)</td><td>209.50 (-5.33%)</td><td>171.40 (+0.06%)</td><td>24.20 <b>(-58.82%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>328.70 (n/a)</td><td>233.12 (n/a)</td><td>221.30 (n/a)</td><td>171.30 (n/a)</td><td>58.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 <b>(+34.63%)</b></td><td>0.04 (+15.89%)</td><td>0.04 (+8.99%)</td><td>0.04 (-0.34%)</td><td>0.01 <b>(+212.72%)</b></td><td>228.70 (+0.35%)</td><td>187.52 (-12.00%)</td><td>192.70 (-8.24%)</td><td>148.40 <b>(-25.73%)</b></td><td>31.36 <b>(+130.26%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>227.90 (n/a)</td><td>213.08 (n/a)</td><td>210.00 (n/a)</td><td>199.80 (n/a)</td><td>13.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 <b>(+42.62%)</b></td><td>0.05 <b>(+22.98%)</b></td><td>0.05 (+7.88%)</td><td>0.04 <b>(+22.29%)</b></td><td>0.01 <b>(+89.21%)</b></td><td>204.50 (-18.23%)</td><td>166.12 (-16.95%)</td><td>172.80 (-7.30%)</td><td>116.40 <b>(-29.84%)</b></td><td>35.97 (+7.28%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.10 (n/a)</td><td>200.02 (n/a)</td><td>186.40 (n/a)</td><td>165.90 (n/a)</td><td>33.53 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (-8.70%)</td><td>0.05 (+1.90%)</td><td>0.04 (-2.99%)</td><td>0.04 (+14.69%)</td><td>0.01 <b>(-39.35%)</b></td><td>204.20 (-12.81%)</td><td>178.66 (-4.44%)</td><td>184.90 (+3.07%)</td><td>145.30 (+9.58%)</td><td>23.22 <b>(-43.28%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>186.96 (n/a)</td><td>179.40 (n/a)</td><td>132.60 (n/a)</td><td>40.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 <b>(-21.47%)</b></td><td>0.04 (-14.10%)</td><td>0.04 (-13.97%)</td><td>0.04 (-12.58%)</td><td>0.01 <b>(-36.07%)</b></td><td>230.10 (+14.36%)</td><td>196.18 (+15.41%)</td><td>203.30 (+16.24%)</td><td>163.90 <b>(+27.35%)</b></td><td>25.44 (-5.06%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>169.98 (n/a)</td><td>174.90 (n/a)</td><td>128.70 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (+3.59%)</td><td>0.05 (+8.56%)</td><td>0.05 (+2.39%)</td><td>0.04 <b>(+65.09%)</b></td><td>0.01 <b>(-25.50%)</b></td><td>227.50 <b>(-39.43%)</b></td><td>178.60 (-14.95%)</td><td>172.50 (-2.32%)</td><td>130.30 (-3.41%)</td><td>37.88 <b>(-60.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>375.60 (n/a)</td><td>210.00 (n/a)</td><td>176.60 (n/a)</td><td>134.90 (n/a)</td><td>94.73 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 <b>(+24.69%)</b></td><td>0.05 (+16.43%)</td><td>0.05 (+13.52%)</td><td>0.04 <b>(+27.19%)</b></td><td>0.01 (+13.11%)</td><td>184.50 <b>(-21.36%)</b></td><td>166.70 (-14.43%)</td><td>171.20 (-11.89%)</td><td>129.90 (-19.81%)</td><td>21.34 <b>(-29.85%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.60 (n/a)</td><td>194.82 (n/a)</td><td>194.30 (n/a)</td><td>162.00 (n/a)</td><td>30.42 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (-12.82%)</td><td>0.05 (+4.62%)</td><td>0.05 (+3.62%)</td><td>0.04 (+19.00%)</td><td>0.00 <b>(-52.28%)</b></td><td>182.80 (-15.95%)</td><td>165.24 (-6.56%)</td><td>171.60 (-3.54%)</td><td>148.20 (+14.71%)</td><td>14.97 <b>(-53.48%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>176.84 (n/a)</td><td>177.90 (n/a)</td><td>129.20 (n/a)</td><td>32.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 <b>(-31.53%)</b></td><td>0.04 (-17.79%)</td><td>0.04 (-2.01%)</td><td>0.03 (+1.82%)</td><td>0.01 <b>(-63.19%)</b></td><td>237.30 (-1.78%)</td><td>201.22 (+13.49%)</td><td>185.80 (+2.09%)</td><td>168.40 <b>(+46.05%)</b></td><td>31.11 <b>(-44.98%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>241.60 (n/a)</td><td>177.30 (n/a)</td><td>182.00 (n/a)</td><td>115.30 (n/a)</td><td>56.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (-10.15%)</td><td>0.05 (-1.54%)</td><td>0.05 (+3.89%)</td><td>0.04 (-0.15%)</td><td>0.01 <b>(-28.21%)</b></td><td>232.70 (+0.17%)</td><td>174.10 (-1.23%)</td><td>173.00 (-3.73%)</td><td>130.50 (+11.25%)</td><td>39.05 <b>(-20.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>176.26 (n/a)</td><td>179.70 (n/a)</td><td>117.30 (n/a)</td><td>48.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (-7.77%)</td><td>0.05 (+10.58%)</td><td>0.05 (+14.41%)</td><td>0.04 <b>(+20.30%)</b></td><td>0.01 <b>(-31.04%)</b></td><td>199.10 (-16.87%)</td><td>170.08 (-11.41%)</td><td>174.60 (-12.61%)</td><td>145.40 (+8.43%)</td><td>24.10 <b>(-37.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>191.98 (n/a)</td><td>199.80 (n/a)</td><td>134.10 (n/a)</td><td>38.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (+5.83%)</td><td>0.05 (+8.56%)</td><td>0.05 (+8.35%)</td><td>0.04 (+8.71%)</td><td>0.01 (-9.06%)</td><td>197.50 (-8.01%)</td><td>163.32 (-8.48%)</td><td>160.60 (-7.75%)</td><td>137.60 (-5.49%)</td><td>23.56 <b>(-21.33%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>178.46 (n/a)</td><td>174.10 (n/a)</td><td>145.60 (n/a)</td><td>29.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 <b>(-24.98%)</b></td><td>0.05 (-3.68%)</td><td>0.05 (+11.06%)</td><td>0.03 (-16.22%)</td><td>0.01 <b>(-40.61%)</b></td><td>239.50 (+19.33%)</td><td>184.30 (+2.47%)</td><td>171.60 (-9.97%)</td><td>165.90 <b>(+33.36%)</b></td><td>31.09 (-1.64%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.70 (n/a)</td><td>179.86 (n/a)</td><td>190.60 (n/a)</td><td>124.40 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-12.22%)</td><td>0.05 (+10.23%)</td><td>0.05 (+12.39%)</td><td>0.05 <b>(+33.65%)</b></td><td>0.00 <b>(-67.04%)</b></td><td>179.00 <b>(-25.17%)</b></td><td>166.38 (-12.34%)</td><td>168.50 (-11.03%)</td><td>150.90 (+13.97%)</td><td>11.28 <b>(-71.13%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>189.80 (n/a)</td><td>189.40 (n/a)</td><td>132.40 (n/a)</td><td>39.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (+2.26%)</td><td>0.08 (-13.59%)</td><td>0.09 (+0.82%)</td><td>0.04 <b>(-45.23%)</b></td><td>0.03 <b>(+113.85%)</b></td><td>386.70 <b>(+82.58%)</b></td><td>221.96 <b>(+28.27%)</b></td><td>173.00 (-0.80%)</td><td>147.80 (-2.18%)</td><td>97.53 <b>(+297.46%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.80 (n/a)</td><td>173.04 (n/a)</td><td>174.40 (n/a)</td><td>151.10 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (-11.49%)</td><td>0.10 (+4.19%)</td><td>0.10 (+5.16%)</td><td>0.08 (+0.15%)</td><td>0.02 (-18.49%)</td><td>202.60 (-0.20%)</td><td>163.54 (-4.90%)</td><td>168.70 (-4.90%)</td><td>130.00 (+13.04%)</td><td>31.40 (-6.60%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.00 (n/a)</td><td>171.96 (n/a)</td><td>177.40 (n/a)</td><td>115.00 (n/a)</td><td>33.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (+14.77%)</td><td>0.09 (+16.44%)</td><td>0.09 (+19.88%)</td><td>0.07 (+9.14%)</td><td>0.01 <b>(+24.84%)</b></td><td>224.70 (-8.36%)</td><td>186.04 (-13.75%)</td><td>178.20 (-16.57%)</td><td>148.70 (-12.84%)</td><td>29.40 (+1.15%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>245.20 (n/a)</td><td>215.70 (n/a)</td><td>213.60 (n/a)</td><td>170.60 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (-8.40%)</td><td>0.09 <b>(+20.77%)</b></td><td>0.09 <b>(+24.72%)</b></td><td>0.08 <b>(+59.49%)</b></td><td>0.01 <b>(-69.53%)</b></td><td>203.40 <b>(-37.32%)</b></td><td>179.32 <b>(-21.86%)</b></td><td>174.10 (-19.84%)</td><td>171.60 (+9.16%)</td><td>13.54 <b>(-79.14%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>324.50 (n/a)</td><td>229.50 (n/a)</td><td>217.20 (n/a)</td><td>157.20 (n/a)</td><td>64.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (+13.09%)</td><td>0.11 (+9.93%)</td><td>0.11 (+17.07%)</td><td>0.07 (-14.28%)</td><td>0.02 <b>(+68.52%)</b></td><td>224.80 (+16.66%)</td><td>158.90 (-6.10%)</td><td>145.20 (-14.59%)</td><td>119.00 (-11.52%)</td><td>41.49 <b>(+76.42%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.70 (n/a)</td><td>169.22 (n/a)</td><td>170.00 (n/a)</td><td>134.50 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (-7.70%)</td><td>0.11 (-4.47%)</td><td>0.11 (+2.62%)</td><td>0.09 (+9.53%)</td><td>0.02 <b>(-24.36%)</b></td><td>190.90 (-8.70%)</td><td>158.86 (+2.81%)</td><td>155.30 (-2.57%)</td><td>122.50 (+8.31%)</td><td>27.84 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>209.10 (n/a)</td><td>154.52 (n/a)</td><td>159.40 (n/a)</td><td>113.10 (n/a)</td><td>36.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 <b>(+42.21%)</b></td><td>0.12 (+13.04%)</td><td>0.12 (+19.50%)</td><td>0.09 (-7.31%)</td><td>0.03 <b>(+228.36%)</b></td><td>181.20 (+7.92%)</td><td>144.04 (-7.93%)</td><td>135.60 (-16.30%)</td><td>98.90 <b>(-29.66%)</b></td><td>32.64 <b>(+150.23%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>167.90 (n/a)</td><td>156.44 (n/a)</td><td>162.00 (n/a)</td><td>140.60 (n/a)</td><td>13.04 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 <b>(+26.03%)</b></td><td>0.12 (+18.41%)</td><td>0.13 <b>(+24.74%)</b></td><td>0.09 (-10.36%)</td><td>0.02 <b>(+364.48%)</b></td><td>185.80 (+11.52%)</td><td>138.40 (-13.54%)</td><td>127.80 (-19.87%)</td><td>120.00 <b>(-20.63%)</b></td><td>26.93 <b>(+320.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>166.60 (n/a)</td><td>160.08 (n/a)</td><td>159.50 (n/a)</td><td>151.20 (n/a)</td><td>6.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (+13.58%)</td><td>0.13 (+18.50%)</td><td>0.12 (+12.51%)</td><td>0.11 (+18.98%)</td><td>0.01 (+1.07%)</td><td>148.50 (-15.96%)</td><td>129.12 (-15.86%)</td><td>131.80 (-11.13%)</td><td>115.60 (-11.96%)</td><td>13.47 <b>(-26.94%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.70 (n/a)</td><td>153.46 (n/a)</td><td>148.30 (n/a)</td><td>131.30 (n/a)</td><td>18.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (-8.67%)</td><td>0.11 <b>(+21.16%)</b></td><td>0.12 <b>(+54.20%)</b></td><td>0.09 (+19.79%)</td><td>0.02 <b>(-39.49%)</b></td><td>192.40 (-16.49%)</td><td>149.80 <b>(-20.52%)</b></td><td>137.10 <b>(-35.18%)</b></td><td>129.70 (+9.45%)</td><td>25.67 <b>(-43.15%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>230.40 (n/a)</td><td>188.48 (n/a)</td><td>211.50 (n/a)</td><td>118.50 (n/a)</td><td>45.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 <b>(+20.27%)</b></td><td>0.10 (+12.26%)</td><td>0.10 (+2.22%)</td><td>0.09 (+13.70%)</td><td>0.02 <b>(+52.04%)</b></td><td>181.40 (-12.07%)</td><td>161.00 (-10.18%)</td><td>171.60 (-2.17%)</td><td>124.50 (-16.89%)</td><td>24.42 (+12.04%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.30 (n/a)</td><td>179.24 (n/a)</td><td>175.40 (n/a)</td><td>149.80 (n/a)</td><td>21.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (+16.74%)</td><td>0.09 (-11.37%)</td><td>0.09 (-17.39%)</td><td>0.07 <b>(-26.47%)</b></td><td>0.03 <b>(+136.11%)</b></td><td>239.10 <b>(+36.01%)</b></td><td>184.22 (+17.86%)</td><td>184.50 <b>(+21.06%)</b></td><td>119.90 (-14.36%)</td><td>43.74 <b>(+165.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>156.30 (n/a)</td><td>152.40 (n/a)</td><td>140.00 (n/a)</td><td>16.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (-7.79%)</td><td>0.09 (+4.44%)</td><td>0.09 (+19.13%)</td><td>0.07 (-6.48%)</td><td>0.02 (-15.92%)</td><td>233.00 (+6.93%)</td><td>179.74 (-5.04%)</td><td>177.60 (-16.07%)</td><td>135.20 (+8.42%)</td><td>38.56 (-2.81%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.90 (n/a)</td><td>189.28 (n/a)</td><td>211.60 (n/a)</td><td>124.70 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (+5.58%)</td><td>0.08 (-11.02%)</td><td>0.09 (-8.64%)</td><td>0.04 <b>(-43.23%)</b></td><td>0.03 <b>(+110.62%)</b></td><td>381.50 <b>(+76.13%)</b></td><td>217.98 <b>(+24.46%)</b></td><td>181.20 (+9.49%)</td><td>145.90 (-5.26%)</td><td>96.31 <b>(+263.44%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>175.14 (n/a)</td><td>165.50 (n/a)</td><td>154.00 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 <b>(+23.00%)</b></td><td>0.11 <b>(+20.89%)</b></td><td>0.11 (+16.90%)</td><td>0.09 <b>(+26.89%)</b></td><td>0.02 (+6.48%)</td><td>180.90 <b>(-21.18%)</b></td><td>148.90 (-17.93%)</td><td>153.60 (-14.43%)</td><td>116.20 (-18.74%)</td><td>23.60 <b>(-32.18%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>229.50 (n/a)</td><td>181.44 (n/a)</td><td>179.50 (n/a)</td><td>143.00 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 <b>(+33.27%)</b></td><td>0.11 <b>(+35.14%)</b></td><td>0.12 <b>(+32.76%)</b></td><td>0.09 <b>(+41.92%)</b></td><td>0.02 (+15.27%)</td><td>174.50 <b>(-29.52%)</b></td><td>145.48 <b>(-26.53%)</b></td><td>138.70 <b>(-24.70%)</b></td><td>120.20 <b>(-24.97%)</b></td><td>21.30 <b>(-39.20%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>247.60 (n/a)</td><td>198.02 (n/a)</td><td>184.20 (n/a)</td><td>160.20 (n/a)</td><td>35.04 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (+11.20%)</td><td>0.23 (+8.90%)</td><td>0.25 (+16.44%)</td><td>0.17 (-0.08%)</td><td>0.04 <b>(+40.39%)</b></td><td>191.40 (+0.10%)</td><td>146.06 (-7.12%)</td><td>131.70 (-14.15%)</td><td>124.20 (-10.13%)</td><td>28.07 <b>(+27.91%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.20 (n/a)</td><td>157.26 (n/a)</td><td>153.40 (n/a)</td><td>138.20 (n/a)</td><td>21.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 <b>(+28.96%)</b></td><td>0.23 <b>(+30.27%)</b></td><td>0.25 <b>(+44.11%)</b></td><td>0.14 (+13.70%)</td><td>0.06 <b>(+63.37%)</b></td><td>228.50 (-12.05%)</td><td>153.10 <b>(-21.20%)</b></td><td>131.80 <b>(-30.63%)</b></td><td>119.60 <b>(-22.44%)</b></td><td>45.96 (+10.06%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>259.80 (n/a)</td><td>194.30 (n/a)</td><td>190.00 (n/a)</td><td>154.20 (n/a)</td><td>41.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (-18.13%)</td><td>0.15 (-9.13%)</td><td>0.15 (+1.05%)</td><td>0.13 (-9.90%)</td><td>0.02 <b>(-40.22%)</b></td><td>245.20 (+11.00%)</td><td>218.88 (+9.05%)</td><td>217.90 (-1.00%)</td><td>195.40 <b>(+22.13%)</b></td><td>22.29 <b>(-21.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>220.90 (n/a)</td><td>200.72 (n/a)</td><td>220.10 (n/a)</td><td>160.00 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 <b>(+25.78%)</b></td><td>0.18 (+5.87%)</td><td>0.17 (-1.07%)</td><td>0.15 (+2.28%)</td><td>0.04 <b>(+116.24%)</b></td><td>216.60 (-2.21%)</td><td>190.22 (-3.74%)</td><td>198.20 (+1.07%)</td><td>137.80 <b>(-20.48%)</b></td><td>31.21 <b>(+63.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.50 (n/a)</td><td>197.62 (n/a)</td><td>196.10 (n/a)</td><td>173.30 (n/a)</td><td>19.07 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (-10.44%)</td><td>0.18 (-6.93%)</td><td>0.19 (+3.00%)</td><td>0.10 <b>(-39.16%)</b></td><td>0.05 <b>(+32.09%)</b></td><td>326.00 <b>(+64.40%)</b></td><td>197.72 (+13.75%)</td><td>176.80 (-2.91%)</td><td>142.50 (+11.59%)</td><td>73.16 <b>(+171.22%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>198.30 (n/a)</td><td>173.82 (n/a)</td><td>182.10 (n/a)</td><td>127.70 (n/a)</td><td>26.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.28 (+17.73%)</td><td>0.25 (+17.49%)</td><td>0.26 (+12.56%)</td><td>0.21 <b>(+28.27%)</b></td><td>0.03 (-12.47%)</td><td>157.10 <b>(-22.03%)</b></td><td>130.72 (-15.69%)</td><td>126.90 (-11.13%)</td><td>118.00 (-15.05%)</td><td>15.38 <b>(-41.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>201.50 (n/a)</td><td>155.04 (n/a)</td><td>142.80 (n/a)</td><td>138.90 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (+14.96%)</td><td>0.20 (+8.54%)</td><td>0.19 (+5.15%)</td><td>0.13 (-12.04%)</td><td>0.05 <b>(+81.99%)</b></td><td>242.70 (+13.68%)</td><td>173.30 (-4.38%)</td><td>174.40 (-4.91%)</td><td>130.20 (-13.03%)</td><td>46.72 <b>(+72.50%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.50 (n/a)</td><td>181.24 (n/a)</td><td>183.40 (n/a)</td><td>149.70 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 <b>(+43.06%)</b></td><td>0.23 <b>(+32.59%)</b></td><td>0.22 <b>(+22.69%)</b></td><td>0.18 <b>(+29.72%)</b></td><td>0.03 <b>(+92.17%)</b></td><td>180.70 <b>(-22.88%)</b></td><td>147.48 <b>(-23.89%)</b></td><td>150.50 (-18.52%)</td><td>123.10 <b>(-30.10%)</b></td><td>23.13 (-0.24%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>234.30 (n/a)</td><td>193.78 (n/a)</td><td>184.70 (n/a)</td><td>176.10 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (-1.20%)</td><td>0.20 (-3.34%)</td><td>0.20 (-7.65%)</td><td>0.15 (+9.54%)</td><td>0.04 <b>(-20.38%)</b></td><td>212.20 (-8.73%)</td><td>169.20 (+1.60%)</td><td>162.00 (+8.29%)</td><td>131.40 (+1.23%)</td><td>30.44 <b>(-26.85%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>232.50 (n/a)</td><td>166.54 (n/a)</td><td>149.60 (n/a)</td><td>129.80 (n/a)</td><td>41.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 <b>(+31.83%)</b></td><td>0.19 (+8.25%)</td><td>0.17 (-3.87%)</td><td>0.16 (+0.85%)</td><td>0.05 <b>(+144.89%)</b></td><td>209.70 (-0.85%)</td><td>175.92 (-4.83%)</td><td>190.60 (+4.04%)</td><td>124.20 <b>(-24.18%)</b></td><td>36.03 <b>(+85.79%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>211.50 (n/a)</td><td>184.84 (n/a)</td><td>183.20 (n/a)</td><td>163.80 (n/a)</td><td>19.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.22 <b>(-25.88%)</b></td><td>0.17 <b>(-22.92%)</b></td><td>0.16 (-19.58%)</td><td>0.10 <b>(-36.61%)</b></td><td>0.04 <b>(-21.85%)</b></td><td>319.20 <b>(+57.79%)</b></td><td>210.82 <b>(+31.70%)</b></td><td>203.80 <b>(+24.34%)</b></td><td>147.90 <b>(+34.95%)</b></td><td>66.05 <b>(+68.55%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>202.30 (n/a)</td><td>160.08 (n/a)</td><td>163.90 (n/a)</td><td>109.60 (n/a)</td><td>39.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 <b>(-20.30%)</b></td><td>0.20 (+2.60%)</td><td>0.20 (+13.71%)</td><td>0.18 <b>(+25.11%)</b></td><td>0.02 <b>(-61.59%)</b></td><td>185.40 <b>(-20.09%)</b></td><td>164.74 (-7.23%)</td><td>162.50 (-12.07%)</td><td>139.20 <b>(+25.41%)</b></td><td>17.66 <b>(-59.45%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>232.00 (n/a)</td><td>177.58 (n/a)</td><td>184.80 (n/a)</td><td>111.00 (n/a)</td><td>43.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (-0.27%)</td><td>0.16 (-5.04%)</td><td>0.15 (-13.81%)</td><td>0.11 (-19.78%)</td><td>0.04 <b>(+46.21%)</b></td><td>299.30 <b>(+24.66%)</b></td><td>215.92 (+8.89%)</td><td>222.50 (+16.01%)</td><td>155.50 (+0.26%)</td><td>57.20 <b>(+79.54%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>240.10 (n/a)</td><td>198.30 (n/a)</td><td>191.80 (n/a)</td><td>155.10 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (-3.30%)</td><td>0.18 (+7.54%)</td><td>0.18 (+16.12%)</td><td>0.15 (+5.51%)</td><td>0.02 <b>(-22.14%)</b></td><td>225.00 (-5.22%)</td><td>183.86 (-7.97%)</td><td>177.20 (-13.90%)</td><td>157.30 (+3.35%)</td><td>26.61 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>237.40 (n/a)</td><td>199.78 (n/a)</td><td>205.80 (n/a)</td><td>152.20 (n/a)</td><td>34.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (-9.08%)</td><td>0.19 (-0.88%)</td><td>0.18 (-10.73%)</td><td>0.18 (+19.77%)</td><td>0.01 <b>(-68.52%)</b></td><td>182.80 (-16.53%)</td><td>174.76 (-1.91%)</td><td>177.90 (+12.03%)</td><td>157.90 (+9.96%)</td><td>9.88 <b>(-72.26%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>219.00 (n/a)</td><td>178.16 (n/a)</td><td>158.80 (n/a)</td><td>143.60 (n/a)</td><td>35.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (-11.29%)</td><td>0.17 (-4.80%)</td><td>0.18 (+3.61%)</td><td>0.15 (+3.42%)</td><td>0.02 <b>(-44.81%)</b></td><td>221.80 (-3.27%)</td><td>194.10 (+3.34%)</td><td>186.30 (-3.47%)</td><td>173.20 (+12.76%)</td><td>20.71 <b>(-37.56%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>229.30 (n/a)</td><td>187.82 (n/a)</td><td>193.00 (n/a)</td><td>153.60 (n/a)</td><td>33.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.18 (-0.68%)</td><td>0.18 (-0.10%)</td><td>0.18 (-0.01%)</td><td>0.18 (+0.26%)</td><td>0.00 <b>(-77.89%)</b></td><td>47469.50 (-0.26%)</td><td>47414.92 (+0.09%)</td><td>47403.90 (+0.01%)</td><td>47358.40 (+0.68%)</td><td>45.76 <b>(-77.78%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47594.30 (n/a)</td><td>47369.96 (n/a)</td><td>47396.80 (n/a)</td><td>47037.90 (n/a)</td><td>205.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.18 (+0.09%)</td><td>0.18 (+0.13%)</td><td>0.18 (+0.22%)</td><td>0.18 (+0.05%)</td><td>0.00 (+5.16%)</td><td>47574.00 (-0.05%)</td><td>47325.96 (-0.13%)</td><td>47304.70 (-0.22%)</td><td>47068.60 (-0.09%)</td><td>183.52 (+5.08%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47596.10 (n/a)</td><td>47388.28 (n/a)</td><td>47410.00 (n/a)</td><td>47112.70 (n/a)</td><td>174.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (-0.18%)</td><td>0.11 (-0.03%)</td><td>0.11 (+0.01%)</td><td>0.11 (-0.00%)</td><td>0.00 <b>(-76.08%)</b></td><td>374533.90 (+0.00%)</td><td>374401.68 (+0.03%)</td><td>374372.50 (-0.01%)</td><td>374335.20 (+0.18%)</td><td>82.63 <b>(-76.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374519.40 (n/a)</td><td>374279.60 (n/a)</td><td>374423.10 (n/a)</td><td>373679.70 (n/a)</td><td>344.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (-9.80%)</td><td>0.13 (-11.25%)</td><td>0.13 (-3.16%)</td><td>0.11 (-18.79%)</td><td>0.02 <b>(+21.62%)</b></td><td>232.90 <b>(+23.16%)</b></td><td>195.74 (+13.99%)</td><td>187.70 (+3.25%)</td><td>161.40 (+10.85%)</td><td>33.33 <b>(+67.56%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>189.10 (n/a)</td><td>171.72 (n/a)</td><td>181.80 (n/a)</td><td>145.60 (n/a)</td><td>19.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.34 (+12.28%)</td><td>0.29 (+4.34%)</td><td>0.28 (+0.45%)</td><td>0.23 (-3.36%)</td><td>0.04 <b>(+73.49%)</b></td><td>212.50 (+3.51%)</td><td>174.80 (-3.21%)</td><td>177.00 (-0.45%)</td><td>146.70 (-10.93%)</td><td>24.65 <b>(+59.43%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>205.30 (n/a)</td><td>180.60 (n/a)</td><td>177.80 (n/a)</td><td>164.70 (n/a)</td><td>15.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>12.69 (-1.25%)</td><td>11.93 (-5.26%)</td><td>12.40 (-2.58%)</td><td>9.63 <b>(-20.22%)</b></td><td>1.29 <b>(+309.47%)</b></td><td>1088.90 <b>(+25.35%)</b></td><td>888.60 (+6.67%)</td><td>845.30 (+2.65%)</td><td>826.20 (+1.26%)</td><td>112.36 <b>(+424.89%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>12.85 (n/a)</td><td>12.59 (n/a)</td><td>12.73 (n/a)</td><td>12.07 (n/a)</td><td>0.32 (n/a)</td><td>868.70 (n/a)</td><td>833.04 (n/a)</td><td>823.50 (n/a)</td><td>815.90 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 (-9.93%)</td><td>0.22 (-0.28%)</td><td>0.23 (+5.92%)</td><td>0.19 (+1.44%)</td><td>0.02 <b>(-29.05%)</b></td><td>211.80 (-1.40%)</td><td>186.48 (-0.22%)</td><td>177.20 (-5.59%)</td><td>170.80 (+10.98%)</td><td>17.21 <b>(-20.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>214.80 (n/a)</td><td>186.90 (n/a)</td><td>187.70 (n/a)</td><td>153.90 (n/a)</td><td>21.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-13.18%)</td><td>0.03 (-4.28%)</td><td>0.03 (-1.79%)</td><td>0.03 (+15.03%)</td><td>0.00 <b>(-66.15%)</b></td><td>195.10 (-13.10%)</td><td>175.02 (+1.96%)</td><td>171.70 (+1.84%)</td><td>164.70 (+15.17%)</td><td>11.67 <b>(-65.07%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>171.66 (n/a)</td><td>168.60 (n/a)</td><td>143.00 (n/a)</td><td>33.41 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (+11.24%)</td><td>0.03 (+13.92%)</td><td>0.03 (+13.04%)</td><td>0.02 <b>(+36.99%)</b></td><td>0.01 <b>(-25.11%)</b></td><td>175.80 <b>(-26.99%)</b></td><td>153.10 (-16.06%)</td><td>158.10 (-11.53%)</td><td>112.20 (-10.10%)</td><td>25.61 <b>(-51.92%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.80 (n/a)</td><td>182.40 (n/a)</td><td>178.70 (n/a)</td><td>124.80 (n/a)</td><td>53.26 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 <b>(+39.51%)</b></td><td>0.04 (+19.43%)</td><td>0.05 <b>(+30.07%)</b></td><td>0.04 (-1.66%)</td><td>0.01 <b>(+400.66%)</b></td><td>175.00 (+1.69%)</td><td>141.96 (-14.03%)</td><td>130.00 <b>(-23.12%)</b></td><td>111.60 <b>(-28.32%)</b></td><td>26.71 <b>(+274.55%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>172.10 (n/a)</td><td>165.12 (n/a)</td><td>169.10 (n/a)</td><td>155.70 (n/a)</td><td>7.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-9.04%)</td><td>0.02 (-14.59%)</td><td>0.02 (-15.61%)</td><td>0.02 (-19.95%)</td><td>0.00 (+9.84%)</td><td>232.20 <b>(+24.91%)</b></td><td>190.66 (+18.48%)</td><td>196.50 (+18.52%)</td><td>149.50 (+9.93%)</td><td>36.33 <b>(+51.86%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.90 (n/a)</td><td>160.92 (n/a)</td><td>165.80 (n/a)</td><td>136.00 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (+14.34%)</td><td>0.03 (+7.58%)</td><td>0.03 (+13.16%)</td><td>0.02 (-15.82%)</td><td>0.01 <b>(+142.20%)</b></td><td>238.10 (+18.81%)</td><td>169.10 (-4.04%)</td><td>153.50 (-11.63%)</td><td>136.80 (-12.59%)</td><td>40.59 <b>(+157.25%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.40 (n/a)</td><td>176.22 (n/a)</td><td>173.70 (n/a)</td><td>156.50 (n/a)</td><td>15.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(-20.34%)</b></td><td>0.02 (-6.66%)</td><td>0.02 (-5.62%)</td><td>0.02 (-0.74%)</td><td>0.00 <b>(-48.63%)</b></td><td>214.00 (+0.75%)</td><td>178.66 (+5.27%)</td><td>174.70 (+5.94%)</td><td>161.60 <b>(+25.47%)</b></td><td>20.52 <b>(-33.15%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.40 (n/a)</td><td>169.72 (n/a)</td><td>164.90 (n/a)</td><td>128.80 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-12.38%)</td><td>0.03 (-3.23%)</td><td>0.03 (-9.27%)</td><td>0.03 <b>(+33.30%)</b></td><td>0.00 <b>(-66.89%)</b></td><td>189.60 <b>(-25.00%)</b></td><td>173.28 (-0.63%)</td><td>174.10 (+10.19%)</td><td>159.10 (+14.13%)</td><td>12.22 <b>(-72.99%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>174.38 (n/a)</td><td>158.00 (n/a)</td><td>139.40 (n/a)</td><td>45.24 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+3.90%)</td><td>0.02 (+7.56%)</td><td>0.02 (+9.94%)</td><td>0.02 (+7.24%)</td><td>0.00 (+9.69%)</td><td>200.40 (-6.75%)</td><td>175.66 (-6.99%)</td><td>170.20 (-9.03%)</td><td>160.80 (-3.77%)</td><td>16.71 (-2.55%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.90 (n/a)</td><td>188.86 (n/a)</td><td>187.10 (n/a)</td><td>167.10 (n/a)</td><td>17.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-9.61%)</td><td>0.03 (-4.52%)</td><td>0.03 (+1.44%)</td><td>0.02 (+9.86%)</td><td>0.01 <b>(-20.62%)</b></td><td>223.60 (-8.96%)</td><td>177.72 (+2.98%)</td><td>158.50 (-1.43%)</td><td>145.20 (+10.59%)</td><td>35.59 <b>(-20.81%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>245.60 (n/a)</td><td>172.58 (n/a)</td><td>160.80 (n/a)</td><td>131.30 (n/a)</td><td>44.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (+10.21%)</td><td>0.02 (+1.62%)</td><td>0.02 (-3.60%)</td><td>0.02 (-6.02%)</td><td>0.00 <b>(+64.62%)</b></td><td>244.60 (+6.39%)</td><td>197.62 (-0.41%)</td><td>197.00 (+3.68%)</td><td>164.30 (-9.28%)</td><td>31.66 <b>(+57.94%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.90 (n/a)</td><td>198.44 (n/a)</td><td>190.00 (n/a)</td><td>181.10 (n/a)</td><td>20.04 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+4.59%)</td><td>0.03 (-1.17%)</td><td>0.03 (-4.56%)</td><td>0.02 (-13.70%)</td><td>0.00 <b>(+46.49%)</b></td><td>235.50 (+15.90%)</td><td>182.62 (+2.81%)</td><td>181.00 (+4.81%)</td><td>141.80 (-4.38%)</td><td>34.62 <b>(+63.65%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.20 (n/a)</td><td>177.62 (n/a)</td><td>172.70 (n/a)</td><td>148.30 (n/a)</td><td>21.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (-12.21%)</td><td>0.02 (-5.89%)</td><td>0.02 (+8.51%)</td><td>0.02 (-18.06%)</td><td>0.00 (+1.29%)</td><td>245.30 <b>(+22.04%)</b></td><td>191.56 (+6.93%)</td><td>177.20 (-7.85%)</td><td>165.00 (+13.87%)</td><td>33.97 <b>(+38.53%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.00 (n/a)</td><td>179.14 (n/a)</td><td>192.30 (n/a)</td><td>144.90 (n/a)</td><td>24.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-15.19%)</td><td>0.02 (-14.48%)</td><td>0.02 <b>(-20.14%)</b></td><td>0.01 (+6.22%)</td><td>0.00 <b>(-28.98%)</b></td><td>300.40 (-5.86%)</td><td>226.06 (+13.06%)</td><td>217.80 <b>(+25.24%)</b></td><td>168.00 (+17.89%)</td><td>51.03 <b>(-25.86%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>319.10 (n/a)</td><td>199.94 (n/a)</td><td>173.90 (n/a)</td><td>142.50 (n/a)</td><td>68.84 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (-0.87%)</td><td>0.02 (+12.51%)</td><td>0.02 (+18.38%)</td><td>0.02 <b>(+36.90%)</b></td><td>0.00 <b>(-54.65%)</b></td><td>196.90 <b>(-26.97%)</b></td><td>176.74 (-14.46%)</td><td>178.60 (-15.52%)</td><td>151.70 (+0.86%)</td><td>16.16 <b>(-66.67%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>269.60 (n/a)</td><td>206.62 (n/a)</td><td>211.40 (n/a)</td><td>150.40 (n/a)</td><td>48.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(+23.87%)</b></td><td>0.03 (+13.53%)</td><td>0.03 (+10.30%)</td><td>0.02 (+12.13%)</td><td>0.00 <b>(+61.32%)</b></td><td>193.70 (-10.82%)</td><td>167.12 (-11.30%)</td><td>168.20 (-9.38%)</td><td>131.90 (-19.28%)</td><td>22.32 (+12.44%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.20 (n/a)</td><td>188.42 (n/a)</td><td>185.60 (n/a)</td><td>163.40 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (-13.94%)</td><td>0.02 (-3.16%)</td><td>0.02 (-6.07%)</td><td>0.01 <b>(+20.41%)</b></td><td>0.00 <b>(-57.53%)</b></td><td>273.10 (-16.94%)</td><td>240.76 (-0.40%)</td><td>238.20 (+6.48%)</td><td>208.10 (+16.19%)</td><td>23.52 <b>(-59.68%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>328.80 (n/a)</td><td>241.72 (n/a)</td><td>223.70 (n/a)</td><td>179.10 (n/a)</td><td>58.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 <b>(-27.17%)</b></td><td>0.04 (-5.77%)</td><td>0.04 (+1.50%)</td><td>0.04 (-0.69%)</td><td>0.00 <b>(-60.90%)</b></td><td>213.70 (+0.71%)</td><td>187.88 (+3.06%)</td><td>192.40 (-1.48%)</td><td>168.40 <b>(+37.36%)</b></td><td>19.21 <b>(-44.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>182.30 (n/a)</td><td>195.30 (n/a)</td><td>122.60 (n/a)</td><td>34.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 <b>(-21.01%)</b></td><td>0.07 (-9.03%)</td><td>0.07 (-5.64%)</td><td>0.06 (-9.82%)</td><td>0.01 <b>(-46.23%)</b></td><td>203.00 (+10.87%)</td><td>173.22 (+8.49%)</td><td>172.70 (+6.02%)</td><td>149.50 <b>(+26.59%)</b></td><td>19.51 <b>(-21.20%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>159.66 (n/a)</td><td>162.90 (n/a)</td><td>118.10 (n/a)</td><td>24.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-5.09%)</td><td>0.04 (-3.51%)</td><td>0.05 (+0.07%)</td><td>0.03 <b>(-25.88%)</b></td><td>0.01 <b>(+66.68%)</b></td><td>279.90 <b>(+34.89%)</b></td><td>195.84 (+6.52%)</td><td>177.50 (-0.11%)</td><td>166.50 (+5.38%)</td><td>47.46 <b>(+142.54%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>207.50 (n/a)</td><td>183.86 (n/a)</td><td>177.70 (n/a)</td><td>158.00 (n/a)</td><td>19.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (+16.85%)</td><td>0.06 (+4.79%)</td><td>0.06 (-4.38%)</td><td>0.06 (+9.15%)</td><td>0.01 <b>(+61.49%)</b></td><td>180.50 (-8.38%)</td><td>163.60 (-3.69%)</td><td>174.20 (+4.56%)</td><td>125.00 (-14.38%)</td><td>22.89 <b>(+24.70%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>169.86 (n/a)</td><td>166.60 (n/a)</td><td>146.00 (n/a)</td><td>18.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (-2.96%)</td><td>0.05 (+3.44%)</td><td>0.05 <b>(+25.30%)</b></td><td>0.03 (-16.44%)</td><td>0.01 (+7.53%)</td><td>234.20 (+19.67%)</td><td>172.20 (-2.15%)</td><td>155.90 <b>(-20.17%)</b></td><td>129.80 (+3.02%)</td><td>40.72 <b>(+33.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>175.98 (n/a)</td><td>195.30 (n/a)</td><td>126.00 (n/a)</td><td>30.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 <b>(-23.60%)</b></td><td>0.05 <b>(-22.95%)</b></td><td>0.06 (-18.37%)</td><td>0.03 <b>(-37.78%)</b></td><td>0.01 <b>(+27.02%)</b></td><td>292.90 <b>(+60.67%)</b></td><td>199.66 <b>(+33.66%)</b></td><td>176.20 <b>(+22.53%)</b></td><td>170.60 <b>(+30.83%)</b></td><td>52.37 <b>(+166.46%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>149.38 (n/a)</td><td>143.80 (n/a)</td><td>130.40 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (+7.70%)</td><td>0.05 (+10.33%)</td><td>0.05 <b>(+24.98%)</b></td><td>0.04 (+9.67%)</td><td>0.01 (-4.41%)</td><td>211.20 (-8.81%)</td><td>171.68 (-10.49%)</td><td>168.40 <b>(-20.00%)</b></td><td>119.70 (-7.14%)</td><td>34.22 <b>(-21.94%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.60 (n/a)</td><td>191.80 (n/a)</td><td>210.50 (n/a)</td><td>128.90 (n/a)</td><td>43.84 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (+8.98%)</td><td>0.06 (+9.22%)</td><td>0.06 (+10.21%)</td><td>0.04 (-5.91%)</td><td>0.01 <b>(+23.15%)</b></td><td>227.80 (+6.30%)</td><td>160.62 (-7.15%)</td><td>151.40 (-9.23%)</td><td>122.50 (-8.24%)</td><td>39.54 <b>(+25.59%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>172.98 (n/a)</td><td>166.80 (n/a)</td><td>133.50 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (-4.46%)</td><td>0.05 (-8.86%)</td><td>0.04 (-19.57%)</td><td>0.03 (-9.69%)</td><td>0.01 (-5.52%)</td><td>235.90 (+10.75%)</td><td>183.98 (+9.71%)</td><td>185.70 <b>(+24.30%)</b></td><td>135.60 (+4.63%)</td><td>37.93 (+6.28%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>167.70 (n/a)</td><td>149.40 (n/a)</td><td>129.60 (n/a)</td><td>35.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 <b>(+30.15%)</b></td><td>0.05 (+3.69%)</td><td>0.05 (-2.82%)</td><td>0.04 (-11.36%)</td><td>0.01 <b>(+169.06%)</b></td><td>254.60 (+12.80%)</td><td>193.40 (+1.43%)</td><td>191.40 (+2.90%)</td><td>131.80 <b>(-23.15%)</b></td><td>51.60 <b>(+135.24%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.70 (n/a)</td><td>190.68 (n/a)</td><td>186.00 (n/a)</td><td>171.50 (n/a)</td><td>21.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 <b>(+22.39%)</b></td><td>0.05 (+6.18%)</td><td>0.04 (-13.63%)</td><td>0.04 (+17.22%)</td><td>0.01 <b>(+41.42%)</b></td><td>225.00 (-14.68%)</td><td>180.58 (-4.65%)</td><td>199.10 (+15.82%)</td><td>128.80 (-18.27%)</td><td>41.82 (-4.03%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.70 (n/a)</td><td>189.38 (n/a)</td><td>171.90 (n/a)</td><td>157.60 (n/a)</td><td>43.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (+17.04%)</td><td>0.05 (+16.83%)</td><td>0.05 (+17.15%)</td><td>0.04 (+16.14%)</td><td>0.01 <b>(+34.27%)</b></td><td>204.30 (-13.91%)</td><td>180.40 (-14.12%)</td><td>177.10 (-14.65%)</td><td>151.10 (-14.54%)</td><td>22.73 (+1.66%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>237.30 (n/a)</td><td>210.06 (n/a)</td><td>207.50 (n/a)</td><td>176.80 (n/a)</td><td>22.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-2.80%)</td><td>0.05 (+4.68%)</td><td>0.04 (-0.20%)</td><td>0.04 <b>(+24.86%)</b></td><td>0.01 <b>(-39.96%)</b></td><td>199.10 (-19.91%)</td><td>178.10 (-6.93%)</td><td>183.60 (+0.22%)</td><td>151.10 (+2.86%)</td><td>20.83 <b>(-50.36%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.60 (n/a)</td><td>191.36 (n/a)</td><td>183.20 (n/a)</td><td>146.90 (n/a)</td><td>41.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-7.46%)</td><td>0.05 (+2.71%)</td><td>0.05 (+1.88%)</td><td>0.04 (+19.26%)</td><td>0.00 <b>(-40.56%)</b></td><td>205.80 (-16.14%)</td><td>184.56 (-4.21%)</td><td>186.40 (-1.84%)</td><td>162.20 (+8.06%)</td><td>18.20 <b>(-46.66%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>245.40 (n/a)</td><td>192.68 (n/a)</td><td>189.90 (n/a)</td><td>150.10 (n/a)</td><td>34.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (-1.68%)</td><td>0.04 (-7.44%)</td><td>0.04 (+6.45%)</td><td>0.03 (-19.54%)</td><td>0.01 <b>(+49.90%)</b></td><td>321.90 <b>(+24.29%)</b></td><td>238.24 (+11.87%)</td><td>206.40 (-6.05%)</td><td>178.20 (+1.71%)</td><td>63.44 <b>(+93.97%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.00 (n/a)</td><td>212.96 (n/a)</td><td>219.70 (n/a)</td><td>175.20 (n/a)</td><td>32.70 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (-5.38%)</td><td>0.11 (+2.67%)</td><td>0.10 <b>(+22.16%)</b></td><td>0.08 (+6.07%)</td><td>0.02 <b>(-25.67%)</b></td><td>200.70 (-5.73%)</td><td>158.64 (-5.44%)</td><td>158.40 (-18.10%)</td><td>121.40 (+5.66%)</td><td>34.38 <b>(-25.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>212.90 (n/a)</td><td>167.76 (n/a)</td><td>193.40 (n/a)</td><td>114.90 (n/a)</td><td>45.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.18 (+13.73%)</td><td>0.15 (+3.63%)</td><td>0.13 (-6.77%)</td><td>0.13 (+7.14%)</td><td>0.02 <b>(+42.86%)</b></td><td>195.20 (-6.69%)</td><td>171.38 (-2.81%)</td><td>183.20 (+7.26%)</td><td>134.00 (-12.07%)</td><td>24.48 (+14.68%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>209.20 (n/a)</td><td>176.34 (n/a)</td><td>170.80 (n/a)</td><td>152.40 (n/a)</td><td>21.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (-7.36%)</td><td>0.10 (+3.20%)</td><td>0.10 (+9.17%)</td><td>0.08 (+5.51%)</td><td>0.02 <b>(-27.58%)</b></td><td>208.70 (-5.22%)</td><td>169.66 (-5.04%)</td><td>168.80 (-8.41%)</td><td>127.60 (+7.95%)</td><td>28.85 <b>(-24.70%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>220.20 (n/a)</td><td>178.66 (n/a)</td><td>184.30 (n/a)</td><td>118.20 (n/a)</td><td>38.31 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 <b>(+31.08%)</b></td><td>0.13 (+16.83%)</td><td>0.12 (+14.12%)</td><td>0.10 (+9.78%)</td><td>0.03 <b>(+96.64%)</b></td><td>199.50 (-8.90%)</td><td>167.14 (-12.62%)</td><td>173.00 (-12.36%)</td><td>119.90 <b>(-23.73%)</b></td><td>31.91 <b>(+37.81%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>191.28 (n/a)</td><td>197.40 (n/a)</td><td>157.20 (n/a)</td><td>23.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (-12.46%)</td><td>0.11 (-3.79%)</td><td>0.10 (-7.83%)</td><td>0.09 (+2.86%)</td><td>0.02 <b>(-21.51%)</b></td><td>182.60 (-2.77%)</td><td>153.82 (+2.31%)</td><td>164.80 (+8.49%)</td><td>121.10 (+14.25%)</td><td>29.73 (-16.01%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>187.80 (n/a)</td><td>150.34 (n/a)</td><td>151.90 (n/a)</td><td>106.00 (n/a)</td><td>35.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 <b>(+22.90%)</b></td><td>0.13 (+8.68%)</td><td>0.12 (+5.92%)</td><td>0.10 (-11.18%)</td><td>0.02 <b>(+445.09%)</b></td><td>207.70 (+12.57%)</td><td>165.20 (-6.37%)</td><td>164.90 (-5.61%)</td><td>140.20 (-18.63%)</td><td>26.06 <b>(+406.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>184.50 (n/a)</td><td>176.44 (n/a)</td><td>174.70 (n/a)</td><td>172.30 (n/a)</td><td>5.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (-13.79%)</td><td>0.10 (-9.30%)</td><td>0.11 <b>(+24.05%)</b></td><td>0.07 <b>(-24.32%)</b></td><td>0.03 (-9.70%)</td><td>251.50 <b>(+32.16%)</b></td><td>175.52 (+11.71%)</td><td>148.70 (-19.40%)</td><td>127.30 (+15.94%)</td><td>55.20 <b>(+37.05%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>190.30 (n/a)</td><td>157.12 (n/a)</td><td>184.50 (n/a)</td><td>109.80 (n/a)</td><td>40.28 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (-0.79%)</td><td>0.11 (-4.67%)</td><td>0.11 (-13.04%)</td><td>0.08 (-14.59%)</td><td>0.03 <b>(+32.53%)</b></td><td>242.20 (+17.12%)</td><td>173.08 (+7.46%)</td><td>169.00 (+15.04%)</td><td>132.20 (+0.76%)</td><td>44.91 <b>(+50.63%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>206.80 (n/a)</td><td>161.06 (n/a)</td><td>146.90 (n/a)</td><td>131.20 (n/a)</td><td>29.81 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (-10.97%)</td><td>0.09 <b>(-20.80%)</b></td><td>0.09 <b>(-30.13%)</b></td><td>0.08 (-14.78%)</td><td>0.02 <b>(-23.64%)</b></td><td>201.20 (+17.32%)</td><td>178.90 <b>(+25.35%)</b></td><td>185.70 <b>(+43.07%)</b></td><td>135.20 (+12.39%)</td><td>25.33 (-4.42%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>171.50 (n/a)</td><td>142.72 (n/a)</td><td>129.80 (n/a)</td><td>120.30 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (+17.11%)</td><td>0.11 <b>(+27.44%)</b></td><td>0.11 <b>(+28.61%)</b></td><td>0.09 <b>(+76.22%)</b></td><td>0.02 <b>(-27.92%)</b></td><td>214.60 <b>(-43.24%)</b></td><td>167.84 <b>(-26.94%)</b></td><td>168.00 <b>(-22.26%)</b></td><td>130.50 (-14.59%)</td><td>30.38 <b>(-65.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>378.10 (n/a)</td><td>229.74 (n/a)</td><td>216.10 (n/a)</td><td>152.80 (n/a)</td><td>88.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (-2.65%)</td><td>0.10 <b>(+21.00%)</b></td><td>0.10 <b>(+27.41%)</b></td><td>0.08 <b>(+36.39%)</b></td><td>0.02 <b>(-22.88%)</b></td><td>210.20 <b>(-26.66%)</b></td><td>163.48 <b>(-20.90%)</b></td><td>167.80 <b>(-21.52%)</b></td><td>118.40 (+2.78%)</td><td>37.57 <b>(-38.47%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>286.60 (n/a)</td><td>206.68 (n/a)</td><td>213.80 (n/a)</td><td>115.20 (n/a)</td><td>61.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 <b>(+58.02%)</b></td><td>0.11 <b>(+29.76%)</b></td><td>0.10 (+9.48%)</td><td>0.08 <b>(+45.78%)</b></td><td>0.03 <b>(+71.73%)</b></td><td>219.70 <b>(-31.39%)</b></td><td>168.78 <b>(-21.98%)</b></td><td>181.70 (-8.69%)</td><td>106.20 <b>(-36.67%)</b></td><td>44.53 <b>(-27.87%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>320.20 (n/a)</td><td>216.34 (n/a)</td><td>199.00 (n/a)</td><td>167.70 (n/a)</td><td>61.74 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (+12.31%)</td><td>0.09 (+3.03%)</td><td>0.09 (+7.55%)</td><td>0.07 (-7.55%)</td><td>0.02 <b>(+51.28%)</b></td><td>242.90 (+8.20%)</td><td>191.54 (-1.40%)</td><td>186.60 (-7.03%)</td><td>143.90 (-10.95%)</td><td>36.07 <b>(+46.14%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>194.26 (n/a)</td><td>200.70 (n/a)</td><td>161.60 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (-2.54%)</td><td>0.07 (-19.03%)</td><td>0.06 <b>(-28.83%)</b></td><td>0.05 <b>(-38.34%)</b></td><td>0.02 <b>(+139.88%)</b></td><td>370.90 <b>(+62.18%)</b></td><td>264.38 <b>(+32.89%)</b></td><td>285.00 <b>(+40.53%)</b></td><td>177.30 (+2.60%)</td><td>82.54 <b>(+278.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>198.94 (n/a)</td><td>202.80 (n/a)</td><td>172.80 (n/a)</td><td>21.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (+12.12%)</td><td>0.08 (-2.70%)</td><td>0.08 (+8.29%)</td><td>0.05 <b>(-36.26%)</b></td><td>0.02 <b>(+337.11%)</b></td><td>345.80 <b>(+56.90%)</b></td><td>231.06 (+8.57%)</td><td>199.60 (-7.68%)</td><td>173.10 (-10.82%)</td><td>68.17 <b>(+542.59%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>220.40 (n/a)</td><td>212.82 (n/a)</td><td>216.20 (n/a)</td><td>194.10 (n/a)</td><td>10.61 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (+10.89%)</td><td>0.20 (+10.67%)</td><td>0.20 (+13.51%)</td><td>0.16 (+7.63%)</td><td>0.02 (+8.79%)</td><td>203.40 (-7.08%)</td><td>169.14 (-9.63%)</td><td>165.60 (-11.91%)</td><td>144.60 (-9.79%)</td><td>22.06 (-7.14%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>218.90 (n/a)</td><td>187.16 (n/a)</td><td>188.00 (n/a)</td><td>160.30 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.22 (+7.81%)</td><td>0.18 (-0.17%)</td><td>0.17 (-6.03%)</td><td>0.15 (+2.31%)</td><td>0.03 <b>(+27.84%)</b></td><td>211.50 (-2.26%)</td><td>188.56 (+0.62%)</td><td>193.90 (+6.42%)</td><td>148.90 (-7.23%)</td><td>23.74 (+12.20%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>216.40 (n/a)</td><td>187.40 (n/a)</td><td>182.20 (n/a)</td><td>160.50 (n/a)</td><td>21.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (-8.17%)</td><td>0.22 (-0.62%)</td><td>0.21 (-2.45%)</td><td>0.20 (+4.56%)</td><td>0.01 <b>(-47.62%)</b></td><td>201.50 (-4.37%)</td><td>189.60 (+0.03%)</td><td>192.40 (+2.50%)</td><td>175.60 (+8.87%)</td><td>10.23 <b>(-44.98%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>210.70 (n/a)</td><td>189.54 (n/a)</td><td>187.70 (n/a)</td><td>161.30 (n/a)</td><td>18.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (-2.02%)</td><td>0.19 (+13.55%)</td><td>0.19 <b>(+25.19%)</b></td><td>0.16 (+19.98%)</td><td>0.02 <b>(-42.50%)</b></td><td>209.20 (-16.65%)</td><td>175.84 (-13.65%)</td><td>169.80 <b>(-20.09%)</b></td><td>161.50 (+2.09%)</td><td>19.05 <b>(-49.34%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>251.00 (n/a)</td><td>203.64 (n/a)</td><td>212.50 (n/a)</td><td>158.20 (n/a)</td><td>37.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (-7.80%)</td><td>0.21 (-12.07%)</td><td>0.19 (-15.99%)</td><td>0.16 (+4.51%)</td><td>0.06 <b>(-22.82%)</b></td><td>258.90 (-4.32%)</td><td>207.50 (+10.71%)</td><td>217.60 (+19.04%)</td><td>140.30 (+8.51%)</td><td>50.20 (-15.87%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>270.60 (n/a)</td><td>187.42 (n/a)</td><td>182.80 (n/a)</td><td>129.30 (n/a)</td><td>59.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.22 (+6.71%)</td><td>0.20 (+10.57%)</td><td>0.19 (+9.85%)</td><td>0.17 (+10.77%)</td><td>0.02 (+12.33%)</td><td>193.50 (-9.75%)</td><td>169.80 (-9.52%)</td><td>172.50 (-8.97%)</td><td>148.30 (-6.32%)</td><td>20.94 (-6.59%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.40 (n/a)</td><td>187.66 (n/a)</td><td>189.50 (n/a)</td><td>158.30 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.33 (+11.79%)</td><td>0.23 (+4.51%)</td><td>0.21 (+7.89%)</td><td>0.19 (+11.12%)</td><td>0.06 (+9.89%)</td><td>197.10 (-10.00%)</td><td>169.08 (-4.56%)</td><td>176.30 (-7.31%)</td><td>110.40 (-10.53%)</td><td>34.65 (-14.31%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>219.00 (n/a)</td><td>177.16 (n/a)</td><td>190.20 (n/a)</td><td>123.40 (n/a)</td><td>40.44 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (-7.79%)</td><td>0.18 (+12.98%)</td><td>0.18 <b>(+20.60%)</b></td><td>0.17 <b>(+48.61%)</b></td><td>0.03 <b>(-53.02%)</b></td><td>194.60 <b>(-32.69%)</b></td><td>179.58 (-16.77%)</td><td>186.20 (-17.10%)</td><td>143.30 (+8.48%)</td><td>20.98 <b>(-65.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>289.10 (n/a)</td><td>215.76 (n/a)</td><td>224.60 (n/a)</td><td>132.10 (n/a)</td><td>60.99 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (-8.42%)</td><td>0.22 (-1.54%)</td><td>0.23 (+1.51%)</td><td>0.20 (+8.67%)</td><td>0.02 <b>(-44.70%)</b></td><td>183.90 (-8.00%)</td><td>166.24 (+0.16%)</td><td>162.60 (-1.45%)</td><td>148.40 (+9.20%)</td><td>14.88 <b>(-43.76%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>199.90 (n/a)</td><td>165.98 (n/a)</td><td>165.00 (n/a)</td><td>135.90 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (+4.54%)</td><td>0.18 (+3.90%)</td><td>0.18 (+2.82%)</td><td>0.17 (+7.52%)</td><td>0.01 (-16.16%)</td><td>195.00 (-6.97%)</td><td>182.56 (-3.89%)</td><td>182.80 (-2.71%)</td><td>167.40 (-4.34%)</td><td>9.97 <b>(-25.92%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>189.94 (n/a)</td><td>187.90 (n/a)</td><td>175.00 (n/a)</td><td>13.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (+3.24%)</td><td>0.17 (+0.84%)</td><td>0.17 (-0.87%)</td><td>0.15 (+3.76%)</td><td>0.02 (+0.97%)</td><td>230.00 (-3.60%)</td><td>206.08 (-0.91%)</td><td>206.90 (+0.88%)</td><td>166.30 (-3.15%)</td><td>25.28 (-7.14%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>238.60 (n/a)</td><td>207.98 (n/a)</td><td>205.10 (n/a)</td><td>171.70 (n/a)</td><td>27.22 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (+13.65%)</td><td>0.19 (+13.53%)</td><td>0.19 (+18.34%)</td><td>0.16 (+7.38%)</td><td>0.02 <b>(+37.97%)</b></td><td>205.70 (-6.88%)</td><td>175.82 (-11.54%)</td><td>172.30 (-15.50%)</td><td>154.10 (-12.04%)</td><td>22.44 (+12.53%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>220.90 (n/a)</td><td>198.76 (n/a)</td><td>203.90 (n/a)</td><td>175.20 (n/a)</td><td>19.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 <b>(+23.40%)</b></td><td>0.20 (+15.71%)</td><td>0.22 <b>(+28.76%)</b></td><td>0.15 (+7.06%)</td><td>0.04 <b>(+40.23%)</b></td><td>228.80 (-6.61%)</td><td>176.28 (-12.46%)</td><td>160.30 <b>(-22.34%)</b></td><td>133.60 (-18.93%)</td><td>38.28 (+10.66%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>245.00 (n/a)</td><td>201.36 (n/a)</td><td>206.40 (n/a)</td><td>164.80 (n/a)</td><td>34.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (+2.12%)</td><td>0.17 (+5.98%)</td><td>0.17 (+2.35%)</td><td>0.14 (+6.72%)</td><td>0.02 (-17.80%)</td><td>241.80 (-6.28%)</td><td>199.98 (-6.24%)</td><td>194.10 (-2.27%)</td><td>175.60 (-2.06%)</td><td>24.83 <b>(-23.29%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>258.00 (n/a)</td><td>213.28 (n/a)</td><td>198.60 (n/a)</td><td>179.30 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (+5.51%)</td><td>0.11 (+2.23%)</td><td>0.11 (-3.63%)</td><td>0.10 (+10.23%)</td><td>0.01 (-15.26%)</td><td>198.50 (-9.28%)</td><td>184.48 (-2.51%)</td><td>185.90 (+3.74%)</td><td>162.10 (-5.20%)</td><td>14.55 <b>(-27.33%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>218.80 (n/a)</td><td>189.22 (n/a)</td><td>179.20 (n/a)</td><td>171.00 (n/a)</td><td>20.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (-12.12%)</td><td>0.11 (-8.12%)</td><td>0.11 (-5.02%)</td><td>0.10 (-1.28%)</td><td>0.01 <b>(-30.23%)</b></td><td>202.40 (+1.30%)</td><td>183.92 (+7.85%)</td><td>191.40 (+5.28%)</td><td>149.40 (+13.79%)</td><td>21.76 (-18.70%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>199.80 (n/a)</td><td>170.54 (n/a)</td><td>181.80 (n/a)</td><td>131.30 (n/a)</td><td>26.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (+11.17%)</td><td>0.14 (-0.08%)</td><td>0.14 (-0.37%)</td><td>0.08 (-13.73%)</td><td>0.04 <b>(+48.37%)</b></td><td>246.40 (+15.90%)</td><td>159.68 (+3.96%)</td><td>146.10 (+0.34%)</td><td>117.40 (-10.04%)</td><td>51.97 <b>(+53.41%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>212.60 (n/a)</td><td>153.60 (n/a)</td><td>145.60 (n/a)</td><td>130.50 (n/a)</td><td>33.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (-0.69%)</td><td>0.13 (+3.59%)</td><td>0.13 (+19.35%)</td><td>0.09 (-4.11%)</td><td>0.03 (-5.47%)</td><td>220.20 (+4.26%)</td><td>166.96 (-3.76%)</td><td>159.60 (-16.22%)</td><td>119.10 (+0.68%)</td><td>38.00 (-0.18%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>211.20 (n/a)</td><td>173.48 (n/a)</td><td>190.50 (n/a)</td><td>118.30 (n/a)</td><td>38.07 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (+17.84%)</td><td>0.12 (+13.86%)</td><td>0.11 (-6.53%)</td><td>0.10 <b>(+32.62%)</b></td><td>0.03 (-5.41%)</td><td>206.90 <b>(-24.60%)</b></td><td>170.78 (-14.40%)</td><td>189.00 (+6.96%)</td><td>126.80 (-15.18%)</td><td>34.59 <b>(-39.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>274.40 (n/a)</td><td>199.50 (n/a)</td><td>176.70 (n/a)</td><td>149.50 (n/a)</td><td>56.81 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 <b>(+31.78%)</b></td><td>0.14 (+17.92%)</td><td>0.14 (+19.08%)</td><td>0.09 <b>(-21.68%)</b></td><td>0.03 <b>(+396.23%)</b></td><td>240.80 <b>(+27.68%)</b></td><td>159.44 (-10.56%)</td><td>151.30 (-15.99%)</td><td>126.30 <b>(-24.10%)</b></td><td>47.18 <b>(+386.76%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>178.26 (n/a)</td><td>180.10 (n/a)</td><td>166.40 (n/a)</td><td>9.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 <b>(-25.02%)</b></td><td>0.11 (-9.98%)</td><td>0.10 (-12.56%)</td><td>0.09 (+8.05%)</td><td>0.02 <b>(-44.64%)</b></td><td>227.80 (-7.47%)</td><td>193.94 (+6.47%)</td><td>209.30 (+14.37%)</td><td>154.50 <b>(+33.42%)</b></td><td>34.61 <b>(-32.38%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>246.20 (n/a)</td><td>182.16 (n/a)</td><td>183.00 (n/a)</td><td>115.80 (n/a)</td><td>51.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (-13.37%)</td><td>0.11 (-6.62%)</td><td>0.12 (+0.16%)</td><td>0.10 (-3.40%)</td><td>0.02 <b>(-25.28%)</b></td><td>212.70 (+3.50%)</td><td>184.48 (+6.32%)</td><td>172.80 (-0.12%)</td><td>161.30 (+15.46%)</td><td>25.99 (-10.32%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>205.50 (n/a)</td><td>173.52 (n/a)</td><td>173.00 (n/a)</td><td>139.70 (n/a)</td><td>28.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (-11.73%)</td><td>0.15 (-5.48%)</td><td>0.14 (-14.33%)</td><td>0.12 (-9.93%)</td><td>0.03 (-1.48%)</td><td>204.90 (+11.00%)</td><td>167.30 (+6.38%)</td><td>180.80 (+16.72%)</td><td>130.90 (+13.33%)</td><td>32.65 <b>(+21.73%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>184.60 (n/a)</td><td>157.26 (n/a)</td><td>154.90 (n/a)</td><td>115.50 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (+2.25%)</td><td>0.13 (-3.38%)</td><td>0.12 (-11.81%)</td><td>0.12 (-5.43%)</td><td>0.02 <b>(+46.02%)</b></td><td>207.80 (+5.75%)</td><td>185.18 (+4.30%)</td><td>197.90 (+13.34%)</td><td>152.90 (-2.18%)</td><td>23.92 <b>(+50.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>177.54 (n/a)</td><td>174.60 (n/a)</td><td>156.30 (n/a)</td><td>15.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 <b>(+32.87%)</b></td><td>0.18 <b>(+39.94%)</b></td><td>0.18 <b>(+59.04%)</b></td><td>0.15 <b>(+45.91%)</b></td><td>0.03 (-6.93%)</td><td>166.40 <b>(-31.47%)</b></td><td>136.98 <b>(-30.14%)</b></td><td>135.60 <b>(-37.13%)</b></td><td>109.00 <b>(-24.72%)</b></td><td>20.88 <b>(-51.34%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>242.80 (n/a)</td><td>196.08 (n/a)</td><td>215.70 (n/a)</td><td>144.80 (n/a)</td><td>42.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.18 (-8.57%)</td><td>0.16 (+8.17%)</td><td>0.17 (+19.90%)</td><td>0.13 (+3.84%)</td><td>0.03 (-18.21%)</td><td>192.60 (-3.70%)</td><td>155.34 (-8.31%)</td><td>144.60 (-16.56%)</td><td>132.90 (+9.38%)</td><td>26.31 (-12.88%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>200.00 (n/a)</td><td>169.42 (n/a)</td><td>173.30 (n/a)</td><td>121.50 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 <b>(+41.27%)</b></td><td>0.15 (+19.83%)</td><td>0.12 (-5.90%)</td><td>0.12 (+17.51%)</td><td>0.05 <b>(+148.72%)</b></td><td>206.50 (-14.92%)</td><td>170.08 (-12.53%)</td><td>197.30 (+6.25%)</td><td>120.00 <b>(-29.25%)</b></td><td>45.40 <b>(+49.53%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>242.70 (n/a)</td><td>194.44 (n/a)</td><td>185.70 (n/a)</td><td>169.60 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 <b>(+63.39%)</b></td><td>0.17 <b>(+34.83%)</b></td><td>0.15 (+14.47%)</td><td>0.12 (+14.59%)</td><td>0.05 <b>(+176.89%)</b></td><td>199.60 (-12.72%)</td><td>152.20 <b>(-22.23%)</b></td><td>167.80 (-12.65%)</td><td>101.30 <b>(-38.83%)</b></td><td>40.74 <b>(+45.05%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>228.70 (n/a)</td><td>195.70 (n/a)</td><td>192.10 (n/a)</td><td>165.60 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (-12.92%)</td><td>0.12 <b>(-20.34%)</b></td><td>0.11 <b>(-28.39%)</b></td><td>0.10 (-9.49%)</td><td>0.02 (-19.50%)</td><td>242.00 (+10.45%)</td><td>210.36 <b>(+24.92%)</b></td><td>214.90 <b>(+39.64%)</b></td><td>163.70 (+14.80%)</td><td>30.01 (-1.55%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>219.10 (n/a)</td><td>168.40 (n/a)</td><td>153.90 (n/a)</td><td>142.60 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (-19.74%)</td><td>0.12 (-16.74%)</td><td>0.12 <b>(-21.22%)</b></td><td>0.10 (-11.75%)</td><td>0.02 <b>(-42.43%)</b></td><td>253.00 (+13.30%)</td><td>212.86 (+17.94%)</td><td>210.30 <b>(+26.92%)</b></td><td>176.70 <b>(+24.61%)</b></td><td>29.58 <b>(-21.12%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>223.30 (n/a)</td><td>180.48 (n/a)</td><td>165.70 (n/a)</td><td>141.80 (n/a)</td><td>37.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (+2.70%)</td><td>0.09 (-17.76%)</td><td>0.09 <b>(-21.40%)</b></td><td>0.06 <b>(-35.04%)</b></td><td>0.03 <b>(+57.78%)</b></td><td>330.50 <b>(+53.94%)</b></td><td>213.26 <b>(+28.49%)</b></td><td>200.80 <b>(+27.17%)</b></td><td>140.10 (-2.64%)</td><td>70.72 <b>(+144.23%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>165.98 (n/a)</td><td>157.90 (n/a)</td><td>143.90 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (-3.04%)</td><td>0.10 (+0.99%)</td><td>0.10 (-5.64%)</td><td>0.09 <b>(+61.69%)</b></td><td>0.01 <b>(-60.97%)</b></td><td>199.30 <b>(-38.16%)</b></td><td>183.86 (-7.69%)</td><td>184.00 (+5.99%)</td><td>155.90 (+3.18%)</td><td>17.51 <b>(-75.46%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>322.30 (n/a)</td><td>199.18 (n/a)</td><td>173.60 (n/a)</td><td>151.10 (n/a)</td><td>71.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (-14.14%)</td><td>0.11 (-12.63%)</td><td>0.11 <b>(-21.50%)</b></td><td>0.10 (+0.01%)</td><td>0.02 <b>(-40.24%)</b></td><td>189.20 (+0.00%)</td><td>164.50 (+12.24%)</td><td>168.10 <b>(+27.45%)</b></td><td>132.80 (+16.49%)</td><td>20.39 <b>(-33.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>189.20 (n/a)</td><td>146.56 (n/a)</td><td>131.90 (n/a)</td><td>114.00 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (-2.47%)</td><td>0.13 (+3.98%)</td><td>0.13 (-6.57%)</td><td>0.11 <b>(+21.45%)</b></td><td>0.01 <b>(-52.03%)</b></td><td>164.40 (-17.68%)</td><td>144.74 (-6.93%)</td><td>141.00 (+7.06%)</td><td>128.60 (+2.55%)</td><td>14.65 <b>(-59.64%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>199.70 (n/a)</td><td>155.52 (n/a)</td><td>131.70 (n/a)</td><td>125.40 (n/a)</td><td>36.31 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (-1.07%)</td><td>0.11 <b>(-20.87%)</b></td><td>0.11 <b>(-20.37%)</b></td><td>0.06 <b>(-39.39%)</b></td><td>0.04 <b>(+67.50%)</b></td><td>285.70 <b>(+64.95%)</b></td><td>185.22 <b>(+35.34%)</b></td><td>168.20 <b>(+25.52%)</b></td><td>115.80 (+1.14%)</td><td>64.05 <b>(+181.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>173.20 (n/a)</td><td>136.86 (n/a)</td><td>134.00 (n/a)</td><td>114.50 (n/a)</td><td>22.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 <b>(-20.74%)</b></td><td>0.08 <b>(-32.69%)</b></td><td>0.08 <b>(-39.42%)</b></td><td>0.05 <b>(-48.43%)</b></td><td>0.03 <b>(+70.77%)</b></td><td>353.40 <b>(+93.86%)</b></td><td>243.26 <b>(+61.61%)</b></td><td>240.10 <b>(+65.02%)</b></td><td>157.30 <b>(+26.24%)</b></td><td>84.53 <b>(+298.80%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>182.30 (n/a)</td><td>150.52 (n/a)</td><td>145.50 (n/a)</td><td>124.60 (n/a)</td><td>21.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (-7.43%)</td><td>0.10 (+12.26%)</td><td>0.11 <b>(+22.71%)</b></td><td>0.09 <b>(+27.30%)</b></td><td>0.01 <b>(-29.99%)</b></td><td>216.30 <b>(-21.46%)</b></td><td>180.34 (-12.91%)</td><td>164.30 (-18.50%)</td><td>159.10 (+8.01%)</td><td>26.97 <b>(-40.95%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>275.40 (n/a)</td><td>207.08 (n/a)</td><td>201.60 (n/a)</td><td>147.30 (n/a)</td><td>45.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (-8.39%)</td><td>0.10 (-12.57%)</td><td>0.10 (-14.90%)</td><td>0.07 (-19.42%)</td><td>0.02 (+1.79%)</td><td>263.50 <b>(+24.12%)</b></td><td>200.08 (+15.41%)</td><td>182.80 (+17.48%)</td><td>159.20 (+9.19%)</td><td>41.24 <b>(+38.94%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>212.30 (n/a)</td><td>173.36 (n/a)</td><td>155.60 (n/a)</td><td>145.80 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.76 (-18.60%)</td><td>0.65 (-0.41%)</td><td>0.64 (+1.75%)</td><td>0.56 (+3.38%)</td><td>0.07 <b>(-54.95%)</b></td><td>175.50 (-3.25%)</td><td>151.96 (-2.49%)</td><td>154.30 (-1.72%)</td><td>129.50 <b>(+22.87%)</b></td><td>16.70 <b>(-45.92%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.93 (n/a)</td><td>0.66 (n/a)</td><td>0.63 (n/a)</td><td>0.54 (n/a)</td><td>0.16 (n/a)</td><td>181.40 (n/a)</td><td>155.84 (n/a)</td><td>157.00 (n/a)</td><td>105.40 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.75 (-7.38%)</td><td>0.63 (+12.14%)</td><td>0.64 (+13.35%)</td><td>0.50 <b>(+23.48%)</b></td><td>0.11 <b>(-27.10%)</b></td><td>197.70 (-19.04%)</td><td>159.20 (-13.33%)</td><td>154.60 (-11.76%)</td><td>131.20 (+7.98%)</td><td>29.09 <b>(-36.69%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.81 (n/a)</td><td>0.57 (n/a)</td><td>0.56 (n/a)</td><td>0.40 (n/a)</td><td>0.15 (n/a)</td><td>244.20 (n/a)</td><td>183.68 (n/a)</td><td>175.20 (n/a)</td><td>121.50 (n/a)</td><td>45.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.71 <b>(+23.65%)</b></td><td>0.56 (+12.48%)</td><td>0.53 (+11.68%)</td><td>0.45 (+9.58%)</td><td>0.10 <b>(+38.13%)</b></td><td>218.90 (-8.75%)</td><td>178.38 (-10.45%)</td><td>185.40 (-10.43%)</td><td>137.80 (-19.08%)</td><td>30.29 (+3.78%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.58 (n/a)</td><td>0.50 (n/a)</td><td>0.47 (n/a)</td><td>0.41 (n/a)</td><td>0.07 (n/a)</td><td>239.90 (n/a)</td><td>199.20 (n/a)</td><td>207.00 (n/a)</td><td>170.30 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.63 (-2.65%)</td><td>0.53 (-6.09%)</td><td>0.56 (-8.32%)</td><td>0.41 (-6.69%)</td><td>0.09 (-4.80%)</td><td>242.40 (+7.16%)</td><td>190.52 (+6.51%)</td><td>174.80 (+9.05%)</td><td>156.70 (+2.69%)</td><td>33.96 (+6.93%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.64 (n/a)</td><td>0.56 (n/a)</td><td>0.61 (n/a)</td><td>0.43 (n/a)</td><td>0.09 (n/a)</td><td>226.20 (n/a)</td><td>178.88 (n/a)</td><td>160.30 (n/a)</td><td>152.60 (n/a)</td><td>31.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.42 (-18.49%)</td><td>0.37 (-12.05%)</td><td>0.39 (-5.66%)</td><td>0.30 (-19.95%)</td><td>0.05 (-10.39%)</td><td>243.10 <b>(+24.92%)</b></td><td>201.04 (+14.03%)</td><td>191.50 (+6.04%)</td><td>174.50 <b>(+22.71%)</b></td><td>28.96 <b>(+37.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.52 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.06 (n/a)</td><td>194.60 (n/a)</td><td>176.30 (n/a)</td><td>180.60 (n/a)</td><td>142.20 (n/a)</td><td>21.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.69 <b>(+40.16%)</b></td><td>0.51 (+16.65%)</td><td>0.46 (+4.23%)</td><td>0.42 (+13.35%)</td><td>0.11 <b>(+134.13%)</b></td><td>177.50 (-11.78%)</td><td>148.52 (-12.26%)</td><td>160.10 (-4.07%)</td><td>106.60 <b>(-28.65%)</b></td><td>28.21 <b>(+43.42%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.05 (n/a)</td><td>201.20 (n/a)</td><td>169.28 (n/a)</td><td>166.90 (n/a)</td><td>149.40 (n/a)</td><td>19.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.43 (-12.55%)</td><td>0.39 (-0.69%)</td><td>0.43 (+6.25%)</td><td>0.32 (+3.11%)</td><td>0.05 <b>(-39.19%)</b></td><td>230.70 (-3.03%)</td><td>189.36 (-1.34%)</td><td>173.30 (-5.92%)</td><td>170.70 (+14.33%)</td><td>26.08 <b>(-34.24%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>237.90 (n/a)</td><td>191.94 (n/a)</td><td>184.20 (n/a)</td><td>149.30 (n/a)</td><td>39.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.48 (-2.72%)</td><td>0.41 (-6.27%)</td><td>0.45 (+5.32%)</td><td>0.30 (-16.76%)</td><td>0.07 <b>(+37.85%)</b></td><td>245.20 <b>(+20.14%)</b></td><td>184.44 (+8.55%)</td><td>162.80 (-5.07%)</td><td>154.30 (+2.80%)</td><td>37.97 <b>(+72.46%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.05 (n/a)</td><td>204.10 (n/a)</td><td>169.92 (n/a)</td><td>171.50 (n/a)</td><td>150.10 (n/a)</td><td>22.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (-9.07%)</td><td>0.24 (+2.31%)</td><td>0.22 (+3.74%)</td><td>0.20 (+1.23%)</td><td>0.04 (-14.22%)</td><td>180.30 (-1.26%)</td><td>156.00 (-2.78%)</td><td>165.00 (-3.57%)</td><td>128.10 (+9.96%)</td><td>25.11 (-7.03%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>182.60 (n/a)</td><td>160.46 (n/a)</td><td>171.10 (n/a)</td><td>116.50 (n/a)</td><td>27.01 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (+2.82%)</td><td>0.26 (+3.94%)</td><td>0.28 (+8.17%)</td><td>0.21 (+4.27%)</td><td>0.04 (+11.72%)</td><td>176.10 (-4.08%)</td><td>147.40 (-3.50%)</td><td>130.40 (-7.58%)</td><td>126.60 (-2.76%)</td><td>25.29 (+4.78%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>183.60 (n/a)</td><td>152.74 (n/a)</td><td>141.10 (n/a)</td><td>130.20 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.28 (-5.63%)</td><td>0.23 (-7.93%)</td><td>0.23 (-17.81%)</td><td>0.15 (-2.08%)</td><td>0.05 (-10.77%)</td><td>243.60 (+2.14%)</td><td>168.16 (+7.67%)</td><td>160.60 <b>(+21.67%)</b></td><td>132.30 (+6.01%)</td><td>45.14 (-5.01%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.28 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>238.50 (n/a)</td><td>156.18 (n/a)</td><td>132.00 (n/a)</td><td>124.80 (n/a)</td><td>47.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (-4.00%)</td><td>0.24 (-5.91%)</td><td>0.26 (+1.13%)</td><td>0.16 <b>(-24.47%)</b></td><td>0.05 <b>(+49.86%)</b></td><td>229.70 <b>(+32.47%)</b></td><td>161.04 (+9.67%)</td><td>142.90 (-1.18%)</td><td>127.20 (+4.18%)</td><td>42.17 <b>(+107.43%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>173.40 (n/a)</td><td>146.84 (n/a)</td><td>144.60 (n/a)</td><td>122.10 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (-9.49%)</td><td>0.23 (-10.51%)</td><td>0.23 (-8.39%)</td><td>0.18 (-16.86%)</td><td>0.04 (+7.76%)</td><td>203.10 <b>(+20.25%)</b></td><td>165.18 (+12.77%)</td><td>159.50 (+9.17%)</td><td>128.00 (+10.44%)</td><td>29.29 <b>(+46.14%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>168.90 (n/a)</td><td>146.48 (n/a)</td><td>146.10 (n/a)</td><td>115.90 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (-6.42%)</td><td>0.24 (-11.10%)</td><td>0.22 (-14.36%)</td><td>0.19 (-18.56%)</td><td>0.05 <b>(+58.93%)</b></td><td>198.70 <b>(+22.81%)</b></td><td>161.62 (+14.88%)</td><td>166.70 (+16.74%)</td><td>128.40 (+6.91%)</td><td>31.11 <b>(+103.47%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>161.80 (n/a)</td><td>140.68 (n/a)</td><td>142.80 (n/a)</td><td>120.10 (n/a)</td><td>15.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 <b>(-22.22%)</b></td><td>0.19 (-13.46%)</td><td>0.21 (+2.61%)</td><td>0.12 <b>(-35.48%)</b></td><td>0.05 (-6.73%)</td><td>310.40 <b>(+54.97%)</b></td><td>203.08 (+18.80%)</td><td>178.20 (-2.57%)</td><td>151.90 <b>(+28.62%)</b></td><td>63.92 <b>(+93.55%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>200.30 (n/a)</td><td>170.94 (n/a)</td><td>182.90 (n/a)</td><td>118.10 (n/a)</td><td>33.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.34 <b>(+20.50%)</b></td><td>0.21 (-1.16%)</td><td>0.18 (-15.56%)</td><td>0.17 (+5.41%)</td><td>0.07 <b>(+58.47%)</b></td><td>220.60 (-5.16%)</td><td>187.92 (+4.49%)</td><td>210.50 (+18.39%)</td><td>109.90 (-17.06%)</td><td>45.72 <b>(+22.10%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>232.60 (n/a)</td><td>179.84 (n/a)</td><td>177.80 (n/a)</td><td>132.50 (n/a)</td><td>37.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.34 (-1.53%)</td><td>0.26 (-6.71%)</td><td>0.24 (-6.17%)</td><td>0.23 (+4.63%)</td><td>0.05 (-19.37%)</td><td>178.90 (-4.43%)</td><td>159.36 (+5.99%)</td><td>168.80 (+6.57%)</td><td>120.10 (+1.52%)</td><td>23.52 <b>(-20.53%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>187.20 (n/a)</td><td>150.36 (n/a)</td><td>158.40 (n/a)</td><td>118.30 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.31 (-6.84%)</td><td>0.25 (-8.85%)</td><td>0.24 (-12.09%)</td><td>0.22 (+0.86%)</td><td>0.04 (-18.21%)</td><td>187.10 (-0.90%)</td><td>164.50 (+9.00%)</td><td>168.00 (+13.74%)</td><td>132.80 (+7.36%)</td><td>23.84 (-10.76%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>188.80 (n/a)</td><td>150.92 (n/a)</td><td>147.70 (n/a)</td><td>123.70 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.42 <b>(+22.78%)</b></td><td>0.30 (-1.44%)</td><td>0.30 (-2.69%)</td><td>0.23 (-14.35%)</td><td>0.07 <b>(+146.63%)</b></td><td>176.90 (+16.77%)</td><td>141.40 (+5.29%)</td><td>135.50 (+2.73%)</td><td>97.70 (-18.58%)</td><td>32.02 <b>(+137.87%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>151.50 (n/a)</td><td>134.30 (n/a)</td><td>131.90 (n/a)</td><td>120.00 (n/a)</td><td>13.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.30 (-8.04%)</td><td>0.25 (-4.65%)</td><td>0.24 (-3.65%)</td><td>0.19 (-3.71%)</td><td>0.05 (-1.87%)</td><td>212.00 (+3.82%)</td><td>169.00 (+5.05%)</td><td>170.90 (+3.76%)</td><td>136.20 (+8.79%)</td><td>32.21 (+7.79%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>204.20 (n/a)</td><td>160.88 (n/a)</td><td>164.70 (n/a)</td><td>125.20 (n/a)</td><td>29.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.33 (-15.58%)</td><td>0.24 (-16.89%)</td><td>0.23 (-18.59%)</td><td>0.15 <b>(-27.95%)</b></td><td>0.07 (-10.99%)</td><td>265.20 <b>(+38.78%)</b></td><td>184.32 <b>(+21.74%)</b></td><td>176.30 <b>(+22.77%)</b></td><td>124.20 (+18.40%)</td><td>53.24 <b>(+41.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>191.10 (n/a)</td><td>151.40 (n/a)</td><td>143.60 (n/a)</td><td>104.90 (n/a)</td><td>37.65 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (-13.92%)</td><td>0.25 (-9.05%)</td><td>0.26 (+2.97%)</td><td>0.20 (+8.64%)</td><td>0.04 <b>(-36.57%)</b></td><td>206.50 (-7.94%)</td><td>168.44 (+6.93%)</td><td>154.90 (-2.88%)</td><td>139.30 (+16.18%)</td><td>29.58 <b>(-29.85%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>224.30 (n/a)</td><td>157.52 (n/a)</td><td>159.50 (n/a)</td><td>119.90 (n/a)</td><td>42.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 <b>(-31.62%)</b></td><td>0.20 <b>(-21.17%)</b></td><td>0.21 (-14.25%)</td><td>0.15 <b>(-24.28%)</b></td><td>0.03 <b>(-45.70%)</b></td><td>269.50 <b>(+32.04%)</b></td><td>206.32 <b>(+25.00%)</b></td><td>197.30 (+16.61%)</td><td>177.50 <b>(+46.21%)</b></td><td>36.60 (+7.93%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>204.10 (n/a)</td><td>165.06 (n/a)</td><td>169.20 (n/a)</td><td>121.40 (n/a)</td><td>33.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 <b>(-33.74%)</b></td><td>0.20 <b>(-21.89%)</b></td><td>0.20 <b>(-23.45%)</b></td><td>0.18 (-11.82%)</td><td>0.01 <b>(-79.40%)</b></td><td>222.70 (+13.45%)</td><td>208.78 <b>(+25.57%)</b></td><td>208.00 <b>(+30.65%)</b></td><td>197.50 <b>(+50.88%)</b></td><td>9.23 <b>(-65.00%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>196.30 (n/a)</td><td>166.26 (n/a)</td><td>159.20 (n/a)</td><td>130.90 (n/a)</td><td>26.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.28 <b>(-27.60%)</b></td><td>0.22 (-14.07%)</td><td>0.21 (-13.81%)</td><td>0.18 (+15.52%)</td><td>0.04 <b>(-57.01%)</b></td><td>190.40 (-13.45%)</td><td>162.26 (+7.77%)</td><td>164.20 (+16.04%)</td><td>122.20 <b>(+38.08%)</b></td><td>25.91 <b>(-49.82%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>220.00 (n/a)</td><td>150.56 (n/a)</td><td>141.50 (n/a)</td><td>88.50 (n/a)</td><td>51.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (-8.40%)</td><td>0.20 (-4.32%)</td><td>0.20 (+9.27%)</td><td>0.16 (-10.66%)</td><td>0.04 (-14.86%)</td><td>213.90 (+11.93%)</td><td>177.30 (+4.13%)</td><td>171.80 (-8.47%)</td><td>135.20 (+9.12%)</td><td>29.62 (+2.59%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>191.10 (n/a)</td><td>170.26 (n/a)</td><td>187.70 (n/a)</td><td>123.90 (n/a)</td><td>28.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 (-7.76%)</td><td>0.23 (-5.09%)</td><td>0.26 (-3.98%)</td><td>0.16 (-9.13%)</td><td>0.04 (-16.11%)</td><td>212.70 (+10.04%)</td><td>155.56 (+4.68%)</td><td>135.10 (+4.16%)</td><td>130.00 (+8.42%)</td><td>34.90 (+0.50%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>193.30 (n/a)</td><td>148.60 (n/a)</td><td>129.70 (n/a)</td><td>119.90 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (-8.71%)</td><td>0.23 (+4.86%)</td><td>0.23 (+8.97%)</td><td>0.17 <b>(+39.59%)</b></td><td>0.04 <b>(-42.64%)</b></td><td>205.90 <b>(-28.36%)</b></td><td>156.18 (-10.65%)</td><td>150.20 (-8.25%)</td><td>132.70 (+9.49%)</td><td>29.20 <b>(-55.73%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>287.40 (n/a)</td><td>174.80 (n/a)</td><td>163.70 (n/a)</td><td>121.20 (n/a)</td><td>65.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (+2.87%)</td><td>0.24 <b>(+23.16%)</b></td><td>0.23 <b>(+31.26%)</b></td><td>0.20 <b>(+37.41%)</b></td><td>0.04 <b>(-32.90%)</b></td><td>172.80 <b>(-27.21%)</b></td><td>150.46 <b>(-21.68%)</b></td><td>149.60 <b>(-23.83%)</b></td><td>119.40 (-2.77%)</td><td>22.12 <b>(-51.07%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>237.40 (n/a)</td><td>192.10 (n/a)</td><td>196.40 (n/a)</td><td>122.80 (n/a)</td><td>45.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (-12.24%)</td><td>0.20 (-18.19%)</td><td>0.20 (-18.43%)</td><td>0.16 (-14.33%)</td><td>0.04 (-5.25%)</td><td>221.20 (+16.73%)</td><td>181.08 <b>(+23.02%)</b></td><td>172.20 <b>(+22.65%)</b></td><td>140.20 (+13.98%)</td><td>36.29 <b>(+31.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>189.50 (n/a)</td><td>147.20 (n/a)</td><td>140.40 (n/a)</td><td>123.00 (n/a)</td><td>27.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 <b>(-25.48%)</b></td><td>0.18 (-11.43%)</td><td>0.19 (+5.47%)</td><td>0.14 (-4.91%)</td><td>0.02 <b>(-61.59%)</b></td><td>244.10 (+5.17%)</td><td>196.18 (+7.19%)</td><td>187.20 (-5.22%)</td><td>170.60 <b>(+34.12%)</b></td><td>28.32 <b>(-43.54%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>232.10 (n/a)</td><td>183.02 (n/a)</td><td>197.50 (n/a)</td><td>127.20 (n/a)</td><td>50.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (-1.07%)</td><td>0.19 (-9.33%)</td><td>0.17 (-13.11%)</td><td>0.17 (-1.69%)</td><td>0.04 (-6.33%)</td><td>209.50 (+1.70%)</td><td>190.02 (+9.88%)</td><td>205.10 (+15.10%)</td><td>135.50 (+1.04%)</td><td>30.95 (-6.22%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>206.00 (n/a)</td><td>172.94 (n/a)</td><td>178.20 (n/a)</td><td>134.10 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.06 <b>(+24.95%)</b></td><td>0.79 <b>(+24.34%)</b></td><td>0.73 (+18.00%)</td><td>0.61 <b>(+20.79%)</b></td><td>0.17 <b>(+28.55%)</b></td><td>213.90 (-17.19%)</td><td>171.50 (-19.36%)</td><td>178.40 (-15.25%)</td><td>124.10 (-19.94%)</td><td>33.63 (-15.80%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.85 (n/a)</td><td>0.64 (n/a)</td><td>0.62 (n/a)</td><td>0.51 (n/a)</td><td>0.13 (n/a)</td><td>258.30 (n/a)</td><td>212.68 (n/a)</td><td>210.50 (n/a)</td><td>155.00 (n/a)</td><td>39.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.30 <b>(+49.91%)</b></td><td>0.78 (+12.68%)</td><td>0.67 (-2.84%)</td><td>0.43 (-15.64%)</td><td>0.34 <b>(+162.79%)</b></td><td>306.90 (+18.54%)</td><td>193.84 (-0.87%)</td><td>196.40 (+2.94%)</td><td>100.70 <b>(-33.27%)</b></td><td>77.98 <b>(+98.96%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.87 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.51 (n/a)</td><td>0.13 (n/a)</td><td>258.90 (n/a)</td><td>195.54 (n/a)</td><td>190.80 (n/a)</td><td>150.90 (n/a)</td><td>39.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.91 <b>(+37.40%)</b></td><td>0.76 <b>(+29.98%)</b></td><td>0.73 (+17.12%)</td><td>0.62 <b>(+30.40%)</b></td><td>0.12 <b>(+56.20%)</b></td><td>212.50 <b>(-23.31%)</b></td><td>175.94 <b>(-22.64%)</b></td><td>180.40 (-14.58%)</td><td>144.50 <b>(-27.20%)</b></td><td>28.48 (-14.31%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.66 (n/a)</td><td>0.59 (n/a)</td><td>0.62 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>277.10 (n/a)</td><td>227.44 (n/a)</td><td>211.20 (n/a)</td><td>198.50 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+10.63%)</td><td>0.03 (+11.57%)</td><td>0.03 (+6.90%)</td><td>0.02 <b>(+24.30%)</b></td><td>0.00 (-18.40%)</td><td>168.30 (-19.55%)</td><td>146.26 (-11.34%)</td><td>149.80 (-6.43%)</td><td>124.20 (-9.61%)</td><td>16.20 <b>(-41.73%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.20 (n/a)</td><td>164.96 (n/a)</td><td>160.10 (n/a)</td><td>137.40 (n/a)</td><td>27.80 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+13.67%)</td><td>0.03 <b>(+21.26%)</b></td><td>0.03 <b>(+23.36%)</b></td><td>0.02 <b>(+25.24%)</b></td><td>0.00 (+7.02%)</td><td>175.40 <b>(-20.13%)</b></td><td>151.10 (-17.79%)</td><td>151.70 (-18.96%)</td><td>125.20 (-12.02%)</td><td>21.53 <b>(-22.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.60 (n/a)</td><td>183.80 (n/a)</td><td>187.20 (n/a)</td><td>142.30 (n/a)</td><td>27.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+9.03%)</td><td>0.03 (+18.39%)</td><td>0.03 <b>(+25.60%)</b></td><td>0.02 <b>(+22.90%)</b></td><td>0.00 (-12.97%)</td><td>180.70 (-18.64%)</td><td>149.30 (-16.89%)</td><td>145.80 <b>(-20.37%)</b></td><td>123.40 (-8.32%)</td><td>24.46 <b>(-35.37%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.10 (n/a)</td><td>179.64 (n/a)</td><td>183.10 (n/a)</td><td>134.60 (n/a)</td><td>37.84 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>15.76 (+12.23%)</td><td>13.32 (+6.09%)</td><td>12.55 (-3.25%)</td><td>11.29 (+5.56%)</td><td>1.85 (+19.52%)</td><td>185.80 (-5.25%)</td><td>159.90 (-5.52%)</td><td>167.20 (+3.34%)</td><td>133.10 (-10.91%)</td><td>21.57 (+0.25%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>14.04 (n/a)</td><td>12.56 (n/a)</td><td>12.97 (n/a)</td><td>10.70 (n/a)</td><td>1.55 (n/a)</td><td>196.10 (n/a)</td><td>169.24 (n/a)</td><td>161.80 (n/a)</td><td>149.40 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.99 (+12.97%)</td><td>0.83 (+19.46%)</td><td>0.83 (+15.87%)</td><td>0.57 <b>(+32.66%)</b></td><td>0.16 (+0.88%)</td><td>231.20 <b>(-24.64%)</b></td><td>164.60 (-17.93%)</td><td>158.40 (-13.68%)</td><td>133.60 (-11.52%)</td><td>39.17 <b>(-35.70%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.88 (n/a)</td><td>0.70 (n/a)</td><td>0.72 (n/a)</td><td>0.43 (n/a)</td><td>0.16 (n/a)</td><td>306.80 (n/a)</td><td>200.56 (n/a)</td><td>183.50 (n/a)</td><td>151.00 (n/a)</td><td>60.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.05 (+12.91%)</td><td>0.86 (+15.13%)</td><td>0.83 (+15.76%)</td><td>0.64 (+14.01%)</td><td>0.18 (+2.92%)</td><td>205.90 (-12.31%)</td><td>159.78 (-13.83%)</td><td>159.90 (-13.61%)</td><td>126.10 (-11.38%)</td><td>33.95 <b>(-20.80%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.93 (n/a)</td><td>0.74 (n/a)</td><td>0.71 (n/a)</td><td>0.56 (n/a)</td><td>0.17 (n/a)</td><td>234.80 (n/a)</td><td>185.42 (n/a)</td><td>185.10 (n/a)</td><td>142.30 (n/a)</td><td>42.87 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.01 (-6.05%)</td><td>0.80 (-5.84%)</td><td>0.77 (-1.38%)</td><td>0.69 (-2.29%)</td><td>0.13 <b>(-22.20%)</b></td><td>192.20 (+2.34%)</td><td>168.14 (+5.15%)</td><td>171.40 (+1.36%)</td><td>130.90 (+6.42%)</td><td>24.02 (-16.72%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.07 (n/a)</td><td>0.85 (n/a)</td><td>0.78 (n/a)</td><td>0.70 (n/a)</td><td>0.16 (n/a)</td><td>187.80 (n/a)</td><td>159.90 (n/a)</td><td>169.10 (n/a)</td><td>123.00 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.12 (+14.78%)</td><td>0.87 <b>(+23.13%)</b></td><td>0.81 (+11.99%)</td><td>0.76 <b>(+56.47%)</b></td><td>0.15 (-17.61%)</td><td>174.30 <b>(-36.08%)</b></td><td>154.16 <b>(-21.27%)</b></td><td>162.80 (-10.70%)</td><td>118.30 (-12.89%)</td><td>22.52 <b>(-54.97%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.97 (n/a)</td><td>0.71 (n/a)</td><td>0.72 (n/a)</td><td>0.48 (n/a)</td><td>0.18 (n/a)</td><td>272.70 (n/a)</td><td>195.80 (n/a)</td><td>182.30 (n/a)</td><td>135.80 (n/a)</td><td>50.01 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.06 (+12.84%)</td><td>0.90 (+8.56%)</td><td>0.85 (+9.26%)</td><td>0.77 (+2.71%)</td><td>0.13 <b>(+32.86%)</b></td><td>172.30 (-2.60%)</td><td>149.02 (-7.37%)</td><td>155.50 (-8.48%)</td><td>124.40 (-11.40%)</td><td>21.00 (+14.21%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.94 (n/a)</td><td>0.83 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.10 (n/a)</td><td>176.90 (n/a)</td><td>160.88 (n/a)</td><td>169.90 (n/a)</td><td>140.40 (n/a)</td><td>18.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (+16.50%)</td><td>0.03 <b>(+31.15%)</b></td><td>0.03 <b>(+57.12%)</b></td><td>0.02 <b>(+29.91%)</b></td><td>0.01 (+18.19%)</td><td>190.60 <b>(-23.02%)</b></td><td>154.26 <b>(-23.86%)</b></td><td>135.70 <b>(-36.32%)</b></td><td>127.00 (-14.19%)</td><td>31.84 (-19.91%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.60 (n/a)</td><td>202.60 (n/a)</td><td>213.10 (n/a)</td><td>148.00 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 <b>(+31.47%)</b></td><td>0.03 <b>(+22.70%)</b></td><td>0.03 <b>(+51.19%)</b></td><td>0.02 <b>(-27.31%)</b></td><td>0.01 <b>(+318.58%)</b></td><td>272.30 <b>(+37.59%)</b></td><td>165.70 (-11.11%)</td><td>128.50 <b>(-33.83%)</b></td><td>123.70 <b>(-23.97%)</b></td><td>63.70 <b>(+329.70%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.90 (n/a)</td><td>186.42 (n/a)</td><td>194.20 (n/a)</td><td>162.70 (n/a)</td><td>14.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]

_No metrics available._


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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.00 (-6.67%)</td><td>0.00 (-6.85%)</td><td>0.00 (-6.82%)</td><td>0.00 (-9.52%)</td><td>0.00 <b>(+26.03%)</b></td><td>1080.02 (+11.84%)</td><td>1001.57 (+7.07%)</td><td>994.86 (+6.40%)</td><td>967.89 (+6.76%)</td><td>45.90 <b>(+71.86%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>965.66 (n/a)</td><td>935.46 (n/a)</td><td>934.99 (n/a)</td><td>906.61 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.01 (-4.65%)</td><td>0.01 (+0.77%)</td><td>0.01 (-1.27%)</td><td>0.01 (+10.00%)</td><td>0.00 <b>(-66.36%)</b></td><td>1067.97 (-8.94%)</td><td>1041.75 (-1.02%)</td><td>1045.39 (+0.39%)</td><td>1003.13 (+5.31%)</td><td>23.97 <b>(-69.58%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1172.87 (n/a)</td><td>1052.48 (n/a)</td><td>1041.34 (n/a)</td><td>952.51 (n/a)</td><td>78.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.96 (+0.36%)</td><td>0.95 (+0.32%)</td><td>0.95 (+0.38%)</td><td>0.93 (+0.88%)</td><td>0.01 (-5.22%)</td><td>2249.01 (-0.86%)</td><td>2218.57 (-0.32%)</td><td>2214.60 (-0.38%)</td><td>2190.76 (-0.36%)</td><td>25.29 (-6.26%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.92 (n/a)</td><td>0.01 (n/a)</td><td>2268.56 (n/a)</td><td>2225.69 (n/a)</td><td>2222.94 (n/a)</td><td>2198.58 (n/a)</td><td>26.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>5.58 (-7.03%)</td><td>4.72 (-2.30%)</td><td>4.70 (-2.92%)</td><td>3.70 (+4.79%)</td><td>0.70 <b>(-40.72%)</b></td><td>283.30 (-4.58%)</td><td>226.60 (-0.80%)</td><td>223.00 (+3.00%)</td><td>187.90 (+7.56%)</td><td>35.98 <b>(-37.25%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.00 (n/a)</td><td>4.83 (n/a)</td><td>4.84 (n/a)</td><td>3.53 (n/a)</td><td>1.18 (n/a)</td><td>296.90 (n/a)</td><td>228.42 (n/a)</td><td>216.50 (n/a)</td><td>174.70 (n/a)</td><td>57.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>5.95 (-15.27%)</td><td>5.07 (-4.92%)</td><td>5.13 (-7.54%)</td><td>3.54 (-2.87%)</td><td>0.97 <b>(-21.75%)</b></td><td>296.00 (+2.96%)</td><td>214.10 (+3.96%)</td><td>204.40 (+8.15%)</td><td>176.10 (+18.03%)</td><td>48.59 (-6.01%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.03 (n/a)</td><td>5.33 (n/a)</td><td>5.55 (n/a)</td><td>3.65 (n/a)</td><td>1.24 (n/a)</td><td>287.50 (n/a)</td><td>205.94 (n/a)</td><td>189.00 (n/a)</td><td>149.20 (n/a)</td><td>51.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>5.77 (+11.73%)</td><td>5.00 (+10.05%)</td><td>5.13 (+10.07%)</td><td>4.26 (+11.69%)</td><td>0.71 (+19.20%)</td><td>245.90 (-10.48%)</td><td>213.32 (-8.93%)</td><td>204.40 (-9.16%)</td><td>181.70 (-10.49%)</td><td>30.81 (-2.37%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>5.17 (n/a)</td><td>4.54 (n/a)</td><td>4.66 (n/a)</td><td>3.82 (n/a)</td><td>0.59 (n/a)</td><td>274.70 (n/a)</td><td>234.24 (n/a)</td><td>225.00 (n/a)</td><td>203.00 (n/a)</td><td>31.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>6.29 (+2.90%)</td><td>5.41 (+2.95%)</td><td>5.37 (-1.10%)</td><td>4.30 (-2.92%)</td><td>0.83 (+15.69%)</td><td>243.80 (+3.00%)</td><td>197.58 (-2.43%)</td><td>195.10 (+1.09%)</td><td>166.80 (-2.80%)</td><td>31.74 (+12.35%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.11 (n/a)</td><td>5.26 (n/a)</td><td>5.43 (n/a)</td><td>4.43 (n/a)</td><td>0.72 (n/a)</td><td>236.70 (n/a)</td><td>202.50 (n/a)</td><td>193.00 (n/a)</td><td>171.60 (n/a)</td><td>28.25 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>8.51 (-6.69%)</td><td>7.80 (-6.37%)</td><td>7.73 (-6.72%)</td><td>7.13 (-7.50%)</td><td>0.53 (-10.59%)</td><td>294.10 (+8.13%)</td><td>269.98 (+6.77%)</td><td>271.20 (+7.19%)</td><td>246.50 (+7.17%)</td><td>18.43 (+2.85%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.12 (n/a)</td><td>8.33 (n/a)</td><td>8.29 (n/a)</td><td>7.71 (n/a)</td><td>0.60 (n/a)</td><td>272.00 (n/a)</td><td>252.86 (n/a)</td><td>253.00 (n/a)</td><td>230.00 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>9.71 (+6.40%)</td><td>8.01 (+0.68%)</td><td>7.79 (+1.87%)</td><td>7.17 (+1.61%)</td><td>0.99 (+11.40%)</td><td>292.40 (-1.58%)</td><td>264.82 (-0.56%)</td><td>269.30 (-1.82%)</td><td>216.00 (-6.05%)</td><td>29.14 (+1.00%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.12 (n/a)</td><td>7.95 (n/a)</td><td>7.65 (n/a)</td><td>7.06 (n/a)</td><td>0.89 (n/a)</td><td>297.10 (n/a)</td><td>266.32 (n/a)</td><td>274.30 (n/a)</td><td>229.90 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>8.36 (+1.71%)</td><td>7.62 (+0.94%)</td><td>7.25 (-4.64%)</td><td>7.07 (+11.15%)</td><td>0.61 (-19.45%)</td><td>296.70 (-10.04%)</td><td>276.46 (-1.29%)</td><td>289.40 (+4.86%)</td><td>250.80 (-1.69%)</td><td>21.42 <b>(-29.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>8.22 (n/a)</td><td>7.55 (n/a)</td><td>7.60 (n/a)</td><td>6.36 (n/a)</td><td>0.75 (n/a)</td><td>329.80 (n/a)</td><td>280.08 (n/a)</td><td>276.00 (n/a)</td><td>255.10 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>9.21 (-5.67%)</td><td>8.50 (+0.04%)</td><td>8.24 (+0.69%)</td><td>7.97 (+8.91%)</td><td>0.60 <b>(-43.23%)</b></td><td>263.10 (-8.20%)</td><td>247.66 (-0.88%)</td><td>254.40 (-0.70%)</td><td>227.70 (+6.01%)</td><td>17.14 <b>(-44.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.76 (n/a)</td><td>8.50 (n/a)</td><td>8.19 (n/a)</td><td>7.32 (n/a)</td><td>1.06 (n/a)</td><td>286.60 (n/a)</td><td>249.86 (n/a)</td><td>256.20 (n/a)</td><td>214.80 (n/a)</td><td>30.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>10.12 (+11.65%)</td><td>8.41 (+2.30%)</td><td>8.10 (-3.78%)</td><td>6.40 (-10.46%)</td><td>1.56 <b>(+107.50%)</b></td><td>327.90 (+11.68%)</td><td>256.68 (-0.10%)</td><td>259.00 (+3.93%)</td><td>207.30 (-10.41%)</td><td>49.45 <b>(+101.54%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.06 (n/a)</td><td>8.22 (n/a)</td><td>8.42 (n/a)</td><td>7.14 (n/a)</td><td>0.75 (n/a)</td><td>293.60 (n/a)</td><td>256.94 (n/a)</td><td>249.20 (n/a)</td><td>231.40 (n/a)</td><td>24.53 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>10.34 (+3.49%)</td><td>8.75 (+5.22%)</td><td>9.11 (+14.80%)</td><td>7.31 (+3.09%)</td><td>1.28 (+4.40%)</td><td>287.10 (-2.97%)</td><td>244.06 (-4.89%)</td><td>230.30 (-12.86%)</td><td>202.70 (-3.38%)</td><td>36.31 (-0.01%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>10.00 (n/a)</td><td>8.31 (n/a)</td><td>7.93 (n/a)</td><td>7.09 (n/a)</td><td>1.23 (n/a)</td><td>295.90 (n/a)</td><td>256.60 (n/a)</td><td>264.30 (n/a)</td><td>209.80 (n/a)</td><td>36.31 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>11.89 (-11.20%)</td><td>11.53 (-5.12%)</td><td>11.46 (-5.62%)</td><td>11.27 (+0.94%)</td><td>0.28 <b>(-64.79%)</b></td><td>372.00 (-0.93%)</td><td>363.84 (+5.09%)</td><td>366.10 (+5.93%)</td><td>352.90 (+12.64%)</td><td>8.76 <b>(-60.48%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.39 (n/a)</td><td>12.16 (n/a)</td><td>12.14 (n/a)</td><td>11.17 (n/a)</td><td>0.80 (n/a)</td><td>375.50 (n/a)</td><td>346.22 (n/a)</td><td>345.60 (n/a)</td><td>313.30 (n/a)</td><td>22.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>13.23 (+1.77%)</td><td>11.73 (-2.89%)</td><td>11.57 (-4.46%)</td><td>9.93 (-13.06%)</td><td>1.36 <b>(+119.61%)</b></td><td>422.40 (+15.03%)</td><td>361.54 (+3.90%)</td><td>362.50 (+4.65%)</td><td>316.90 (-1.77%)</td><td>42.94 <b>(+145.77%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.00 (n/a)</td><td>12.08 (n/a)</td><td>12.11 (n/a)</td><td>11.42 (n/a)</td><td>0.62 (n/a)</td><td>367.20 (n/a)</td><td>347.98 (n/a)</td><td>346.40 (n/a)</td><td>322.60 (n/a)</td><td>17.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>13.00 (+2.52%)</td><td>11.45 (-2.13%)</td><td>11.55 (+3.15%)</td><td>10.16 (-7.30%)</td><td>1.12 <b>(+39.95%)</b></td><td>412.70 (+7.87%)</td><td>369.26 (+2.57%)</td><td>363.30 (-3.04%)</td><td>322.60 (-2.48%)</td><td>35.79 <b>(+48.51%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>12.68 (n/a)</td><td>11.69 (n/a)</td><td>11.19 (n/a)</td><td>10.96 (n/a)</td><td>0.80 (n/a)</td><td>382.60 (n/a)</td><td>360.00 (n/a)</td><td>374.70 (n/a)</td><td>330.80 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>14.06 (-8.42%)</td><td>12.79 (+2.50%)</td><td>12.80 (+7.16%)</td><td>10.53 (+6.61%)</td><td>1.39 <b>(-32.71%)</b></td><td>398.20 (-6.20%)</td><td>331.40 (-3.54%)</td><td>327.70 (-6.66%)</td><td>298.30 (+9.19%)</td><td>39.70 <b>(-30.00%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>15.35 (n/a)</td><td>12.48 (n/a)</td><td>11.95 (n/a)</td><td>9.88 (n/a)</td><td>2.06 (n/a)</td><td>424.50 (n/a)</td><td>343.56 (n/a)</td><td>351.10 (n/a)</td><td>273.20 (n/a)</td><td>56.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>16.55 (+11.15%)</td><td>12.66 (-1.58%)</td><td>11.97 (-8.96%)</td><td>10.83 (-0.97%)</td><td>2.35 <b>(+60.14%)</b></td><td>387.20 (+0.99%)</td><td>339.34 (+3.01%)</td><td>350.40 (+9.84%)</td><td>253.50 (-10.01%)</td><td>54.92 <b>(+44.79%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>14.89 (n/a)</td><td>12.87 (n/a)</td><td>13.15 (n/a)</td><td>10.94 (n/a)</td><td>1.47 (n/a)</td><td>383.40 (n/a)</td><td>329.44 (n/a)</td><td>319.00 (n/a)</td><td>281.70 (n/a)</td><td>37.93 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>15.58 (+3.47%)</td><td>11.92 (-7.63%)</td><td>11.42 (-9.24%)</td><td>9.98 (-12.64%)</td><td>2.21 <b>(+62.18%)</b></td><td>420.10 (+14.47%)</td><td>360.44 (+9.98%)</td><td>367.30 (+10.20%)</td><td>269.20 (-3.34%)</td><td>58.79 <b>(+78.93%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>15.06 (n/a)</td><td>12.91 (n/a)</td><td>12.58 (n/a)</td><td>11.43 (n/a)</td><td>1.37 (n/a)</td><td>367.00 (n/a)</td><td>327.72 (n/a)</td><td>333.30 (n/a)</td><td>278.50 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>15.04 (-1.15%)</td><td>13.00 (-9.56%)</td><td>13.40 (-7.21%)</td><td>9.58 <b>(-29.29%)</b></td><td>2.15 <b>(+222.10%)</b></td><td>437.60 <b>(+41.44%)</b></td><td>330.84 (+13.22%)</td><td>313.00 (+7.78%)</td><td>278.80 (+1.16%)</td><td>63.49 <b>(+368.79%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>15.22 (n/a)</td><td>14.38 (n/a)</td><td>14.44 (n/a)</td><td>13.55 (n/a)</td><td>0.67 (n/a)</td><td>309.40 (n/a)</td><td>292.20 (n/a)</td><td>290.40 (n/a)</td><td>275.60 (n/a)</td><td>13.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>15.09 (+17.32%)</td><td>13.03 (+4.30%)</td><td>13.26 (+3.92%)</td><td>9.38 <b>(-20.10%)</b></td><td>2.28 <b>(+373.28%)</b></td><td>447.10 <b>(+25.17%)</b></td><td>331.38 (-1.41%)</td><td>316.40 (-3.77%)</td><td>278.00 (-14.75%)</td><td>68.37 <b>(+413.04%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>12.86 (n/a)</td><td>12.49 (n/a)</td><td>12.76 (n/a)</td><td>11.74 (n/a)</td><td>0.48 (n/a)</td><td>357.20 (n/a)</td><td>336.12 (n/a)</td><td>328.80 (n/a)</td><td>326.10 (n/a)</td><td>13.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.02 (+6.10%)</td><td>2.59 (+6.70%)</td><td>2.55 (+6.11%)</td><td>2.25 (+4.65%)</td><td>0.28 (-3.68%)</td><td>233.50 (-4.42%)</td><td>204.22 (-6.48%)</td><td>205.80 (-5.77%)</td><td>173.90 (-5.75%)</td><td>21.76 (-14.97%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>2.84 (n/a)</td><td>2.43 (n/a)</td><td>2.40 (n/a)</td><td>2.15 (n/a)</td><td>0.29 (n/a)</td><td>244.30 (n/a)</td><td>218.36 (n/a)</td><td>218.40 (n/a)</td><td>184.50 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>5.85 (+12.27%)</td><td>4.67 (+1.57%)</td><td>4.59 (-1.54%)</td><td>3.82 (+11.01%)</td><td>0.78 (+9.37%)</td><td>274.60 (-9.91%)</td><td>229.14 (-1.69%)</td><td>228.60 (+1.55%)</td><td>179.10 (-10.94%)</td><td>36.14 (-14.05%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>5.21 (n/a)</td><td>4.60 (n/a)</td><td>4.66 (n/a)</td><td>3.44 (n/a)</td><td>0.71 (n/a)</td><td>304.80 (n/a)</td><td>233.08 (n/a)</td><td>225.10 (n/a)</td><td>201.10 (n/a)</td><td>42.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>8.96 (+12.24%)</td><td>7.93 (+0.71%)</td><td>8.32 (+5.67%)</td><td>6.74 (-13.18%)</td><td>1.04 <b>(+1018.99%)</b></td><td>311.10 (+15.18%)</td><td>268.32 (+0.72%)</td><td>252.00 (-5.37%)</td><td>234.00 (-10.89%)</td><td>36.39 <b>(+1055.29%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.99 (n/a)</td><td>7.87 (n/a)</td><td>7.88 (n/a)</td><td>7.76 (n/a)</td><td>0.09 (n/a)</td><td>270.10 (n/a)</td><td>266.40 (n/a)</td><td>266.30 (n/a)</td><td>262.60 (n/a)</td><td>3.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.06 (-5.67%)</td><td>2.63 (-7.62%)</td><td>2.57 (-6.83%)</td><td>2.30 (-13.85%)</td><td>0.33 <b>(+42.69%)</b></td><td>227.90 (+16.10%)</td><td>202.18 (+9.06%)</td><td>203.80 (+7.32%)</td><td>171.40 (+6.00%)</td><td>24.83 <b>(+79.39%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>3.24 (n/a)</td><td>2.84 (n/a)</td><td>2.76 (n/a)</td><td>2.67 (n/a)</td><td>0.23 (n/a)</td><td>196.30 (n/a)</td><td>185.38 (n/a)</td><td>189.90 (n/a)</td><td>161.70 (n/a)</td><td>13.84 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (+14.81%)</td><td>0.19 (-6.73%)</td><td>0.20 (+0.14%)</td><td>0.12 <b>(-37.70%)</b></td><td>0.06 <b>(+166.74%)</b></td><td>280.60 <b>(+60.43%)</b></td><td>184.78 (+16.37%)</td><td>162.60 (-0.12%)</td><td>114.70 (-12.91%)</td><td>63.92 <b>(+285.93%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>174.90 (n/a)</td><td>158.78 (n/a)</td><td>162.80 (n/a)</td><td>131.70 (n/a)</td><td>16.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (+3.80%)</td><td>0.18 (-14.72%)</td><td>0.16 <b>(-20.82%)</b></td><td>0.14 (-8.26%)</td><td>0.05 <b>(+29.28%)</b></td><td>231.80 (+9.03%)</td><td>191.62 (+19.24%)</td><td>199.90 <b>(+26.28%)</b></td><td>126.20 (-3.66%)</td><td>39.52 <b>(+25.99%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.60 (n/a)</td><td>160.70 (n/a)</td><td>158.30 (n/a)</td><td>131.00 (n/a)</td><td>31.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.43 (-3.10%)</td><td>0.33 (-13.97%)</td><td>0.30 <b>(-23.93%)</b></td><td>0.27 (+10.07%)</td><td>0.07 (-16.72%)</td><td>239.60 (-9.14%)</td><td>205.68 (+14.33%)</td><td>217.10 <b>(+31.50%)</b></td><td>150.70 (+3.22%)</td><td>36.05 <b>(-24.95%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.45 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>263.70 (n/a)</td><td>179.90 (n/a)</td><td>165.10 (n/a)</td><td>146.00 (n/a)</td><td>48.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.41 (-18.69%)</td><td>0.34 (-14.92%)</td><td>0.33 <b>(-24.34%)</b></td><td>0.29 (+6.47%)</td><td>0.05 <b>(-56.40%)</b></td><td>228.30 (-6.09%)</td><td>195.84 (+11.51%)</td><td>196.50 <b>(+32.15%)</b></td><td>159.10 <b>(+23.05%)</b></td><td>26.23 <b>(-50.30%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.51 (n/a)</td><td>0.40 (n/a)</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>243.10 (n/a)</td><td>175.62 (n/a)</td><td>148.70 (n/a)</td><td>129.30 (n/a)</td><td>52.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.48 (-13.96%)</td><td>0.36 <b>(-22.74%)</b></td><td>0.33 <b>(-28.56%)</b></td><td>0.32 (-15.21%)</td><td>0.07 (-0.05%)</td><td>206.00 (+17.92%)</td><td>187.10 <b>(+30.27%)</b></td><td>200.10 <b>(+40.03%)</b></td><td>135.30 (+16.24%)</td><td>29.45 <b>(+34.33%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.46 (n/a)</td><td>0.38 (n/a)</td><td>0.07 (n/a)</td><td>174.70 (n/a)</td><td>143.62 (n/a)</td><td>142.90 (n/a)</td><td>116.40 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.88 (-12.91%)</td><td>0.74 (-12.03%)</td><td>0.76 (-9.89%)</td><td>0.62 (-15.54%)</td><td>0.11 (-2.21%)</td><td>210.80 (+18.36%)</td><td>179.20 (+14.14%)</td><td>172.00 (+10.97%)</td><td>148.50 (+14.85%)</td><td>26.73 <b>(+33.55%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.01 (n/a)</td><td>0.85 (n/a)</td><td>0.85 (n/a)</td><td>0.74 (n/a)</td><td>0.11 (n/a)</td><td>178.10 (n/a)</td><td>157.00 (n/a)</td><td>155.00 (n/a)</td><td>129.30 (n/a)</td><td>20.01 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.80 <b>(-27.11%)</b></td><td>0.72 (-16.10%)</td><td>0.71 <b>(-27.52%)</b></td><td>0.62 (+15.16%)</td><td>0.07 <b>(-68.80%)</b></td><td>211.10 (-13.16%)</td><td>184.08 (+11.96%)</td><td>184.50 <b>(+38.00%)</b></td><td>163.90 <b>(+37.15%)</b></td><td>19.16 <b>(-63.23%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.10 (n/a)</td><td>0.86 (n/a)</td><td>0.98 (n/a)</td><td>0.54 (n/a)</td><td>0.23 (n/a)</td><td>243.10 (n/a)</td><td>164.42 (n/a)</td><td>133.70 (n/a)</td><td>119.50 (n/a)</td><td>52.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.42 <b>(+42.71%)</b></td><td>0.75 (-10.70%)</td><td>0.59 <b>(-27.34%)</b></td><td>0.54 (-19.09%)</td><td>0.38 <b>(+154.80%)</b></td><td>241.50 <b>(+23.59%)</b></td><td>197.46 <b>(+24.27%)</b></td><td>221.50 <b>(+37.66%)</b></td><td>92.10 <b>(-29.96%)</b></td><td>60.56 <b>(+117.43%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.00 (n/a)</td><td>0.85 (n/a)</td><td>0.81 (n/a)</td><td>0.67 (n/a)</td><td>0.15 (n/a)</td><td>195.40 (n/a)</td><td>158.90 (n/a)</td><td>160.90 (n/a)</td><td>131.50 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.65 <b>(-39.28%)</b></td><td>0.62 (-18.66%)</td><td>0.64 <b>(-21.95%)</b></td><td>0.59 (+8.65%)</td><td>0.03 <b>(-87.38%)</b></td><td>221.40 (-7.98%)</td><td>210.44 (+15.52%)</td><td>204.80 <b>(+28.16%)</b></td><td>202.00 <b>(+64.76%)</b></td><td>9.31 <b>(-81.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.07 (n/a)</td><td>0.77 (n/a)</td><td>0.82 (n/a)</td><td>0.54 (n/a)</td><td>0.22 (n/a)</td><td>240.60 (n/a)</td><td>182.16 (n/a)</td><td>159.80 (n/a)</td><td>122.60 (n/a)</td><td>50.93 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (+1.29%)</td><td>0.11 (+0.98%)</td><td>0.11 (+2.93%)</td><td>0.10 (-0.85%)</td><td>0.01 (+1.99%)</td><td>171.40 (+0.88%)</td><td>152.22 (-0.95%)</td><td>152.40 (-2.87%)</td><td>137.10 (-1.30%)</td><td>12.71 (+2.84%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.90 (n/a)</td><td>153.68 (n/a)</td><td>156.90 (n/a)</td><td>138.90 (n/a)</td><td>12.36 (n/a)</td>
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
