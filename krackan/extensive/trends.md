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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (+5.93%)</td><td>0.04 (-3.84%)</td><td>0.04 (+2.12%)</td><td>0.02 <b>(-24.78%)</b></td><td>0.01 <b>(+55.09%)</b></td><td>292.30 <b>(+32.98%)</b></td><td>193.80 (+11.64%)</td><td>159.40 (-2.09%)</td><td>119.50 (-5.61%)</td><td>72.31 <b>(+99.75%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>173.60 (n/a)</td><td>162.80 (n/a)</td><td>126.60 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (+0.35%)</td><td>0.04 (-4.22%)</td><td>0.03 (-6.67%)</td><td>0.03 (+2.87%)</td><td>0.01 (+7.50%)</td><td>215.30 (-2.80%)</td><td>181.04 (+4.79%)</td><td>186.00 (+7.14%)</td><td>130.00 (-0.31%)</td><td>34.17 (+3.77%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>172.76 (n/a)</td><td>173.60 (n/a)</td><td>130.40 (n/a)</td><td>32.92 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-2.10%)</td><td>0.03 (-7.99%)</td><td>0.03 (-13.61%)</td><td>0.03 (-13.49%)</td><td>0.01 (+19.20%)</td><td>240.50 (+15.57%)</td><td>188.10 (+9.92%)</td><td>191.80 (+15.75%)</td><td>142.90 (+2.14%)</td><td>36.05 <b>(+39.47%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>171.12 (n/a)</td><td>165.70 (n/a)</td><td>139.90 (n/a)</td><td>25.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-10.94%)</td><td>0.03 (-9.33%)</td><td>0.03 (-6.12%)</td><td>0.03 (-14.21%)</td><td>0.00 (+5.73%)</td><td>230.50 (+16.59%)</td><td>194.02 (+10.89%)</td><td>195.10 (+6.50%)</td><td>162.70 (+12.28%)</td><td>28.61 <b>(+38.22%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>197.70 (n/a)</td><td>174.96 (n/a)</td><td>183.20 (n/a)</td><td>144.90 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (+0.78%)</td><td>0.04 (-0.91%)</td><td>0.04 (+1.37%)</td><td>0.03 (+5.12%)</td><td>0.01 (-9.04%)</td><td>180.30 (-4.91%)</td><td>161.32 (+0.52%)</td><td>165.70 (-1.31%)</td><td>129.20 (-0.77%)</td><td>19.90 (-14.76%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>160.48 (n/a)</td><td>167.90 (n/a)</td><td>130.20 (n/a)</td><td>23.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (+10.80%)</td><td>0.03 (-9.98%)</td><td>0.03 (-19.76%)</td><td>0.02 <b>(-31.17%)</b></td><td>0.01 <b>(+161.11%)</b></td><td>327.80 <b>(+45.30%)</b></td><td>237.54 (+16.69%)</td><td>245.70 <b>(+24.66%)</b></td><td>166.00 (-9.78%)</td><td>62.89 <b>(+235.20%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>225.60 (n/a)</td><td>203.56 (n/a)</td><td>197.10 (n/a)</td><td>184.00 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-9.86%)</td><td>0.03 (-8.49%)</td><td>0.03 (-5.53%)</td><td>0.02 (-13.55%)</td><td>0.01 (-15.06%)</td><td>248.50 (+15.69%)</td><td>197.72 (+8.91%)</td><td>201.70 (+5.88%)</td><td>145.70 (+10.88%)</td><td>36.93 (+6.50%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>181.54 (n/a)</td><td>190.50 (n/a)</td><td>131.40 (n/a)</td><td>34.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 <b>(+25.78%)</b></td><td>0.03 (-1.57%)</td><td>0.03 (-14.68%)</td><td>0.02 (-13.93%)</td><td>0.01 <b>(+164.25%)</b></td><td>246.00 (+16.20%)</td><td>203.96 (+6.55%)</td><td>225.70 (+17.19%)</td><td>127.60 <b>(-20.50%)</b></td><td>47.78 <b>(+141.43%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>211.70 (n/a)</td><td>191.42 (n/a)</td><td>192.60 (n/a)</td><td>160.50 (n/a)</td><td>19.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 <b>(-32.34%)</b></td><td>0.07 (-15.59%)</td><td>0.06 (-4.42%)</td><td>0.06 (-3.37%)</td><td>0.01 <b>(-74.70%)</b></td><td>205.00 (+3.54%)</td><td>187.56 (+13.30%)</td><td>190.00 (+4.63%)</td><td>165.90 <b>(+47.86%)</b></td><td>14.26 <b>(-62.58%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>198.00 (n/a)</td><td>165.54 (n/a)</td><td>181.60 (n/a)</td><td>112.20 (n/a)</td><td>38.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (-0.76%)</td><td>0.07 (-4.48%)</td><td>0.08 (+0.80%)</td><td>0.05 (-19.74%)</td><td>0.02 <b>(+41.14%)</b></td><td>238.00 <b>(+24.61%)</b></td><td>174.36 (+7.17%)</td><td>163.10 (-0.79%)</td><td>133.00 (+0.76%)</td><td>40.30 <b>(+82.40%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>162.70 (n/a)</td><td>164.40 (n/a)</td><td>132.00 (n/a)</td><td>22.09 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (+18.00%)</td><td>0.08 (-1.06%)</td><td>0.08 (-11.62%)</td><td>0.07 (+3.11%)</td><td>0.02 <b>(+48.08%)</b></td><td>184.80 (-3.04%)</td><td>154.44 (+2.99%)</td><td>157.20 (+13.17%)</td><td>100.80 (-15.22%)</td><td>32.60 (+15.87%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>190.60 (n/a)</td><td>149.96 (n/a)</td><td>138.90 (n/a)</td><td>118.90 (n/a)</td><td>28.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 <b>(-20.14%)</b></td><td>0.07 <b>(-26.87%)</b></td><td>0.07 <b>(-28.53%)</b></td><td>0.06 (-18.35%)</td><td>0.01 <b>(-28.21%)</b></td><td>220.10 <b>(+22.48%)</b></td><td>186.08 <b>(+36.00%)</b></td><td>181.90 <b>(+39.92%)</b></td><td>145.90 <b>(+25.24%)</b></td><td>28.10 (+8.92%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>179.70 (n/a)</td><td>136.82 (n/a)</td><td>130.00 (n/a)</td><td>116.50 (n/a)</td><td>25.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (-17.28%)</td><td>0.06 <b>(-24.59%)</b></td><td>0.06 <b>(-28.64%)</b></td><td>0.04 <b>(-39.32%)</b></td><td>0.02 <b>(+31.17%)</b></td><td>302.90 <b>(+64.80%)</b></td><td>208.22 <b>(+37.75%)</b></td><td>205.40 <b>(+40.11%)</b></td><td>158.30 <b>(+20.84%)</b></td><td>58.37 <b>(+161.96%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.80 (n/a)</td><td>151.16 (n/a)</td><td>146.60 (n/a)</td><td>131.00 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (+13.35%)</td><td>0.07 (+2.12%)</td><td>0.07 (-5.06%)</td><td>0.05 <b>(+38.29%)</b></td><td>0.02 (+0.68%)</td><td>260.50 <b>(-27.70%)</b></td><td>185.42 (-6.43%)</td><td>178.70 (+5.30%)</td><td>115.40 (-11.77%)</td><td>58.86 <b>(-37.30%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>360.30 (n/a)</td><td>198.16 (n/a)</td><td>169.70 (n/a)</td><td>130.80 (n/a)</td><td>93.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (-11.57%)</td><td>0.06 (-11.01%)</td><td>0.06 (-8.89%)</td><td>0.05 <b>(-21.46%)</b></td><td>0.01 (+8.33%)</td><td>251.40 <b>(+27.29%)</b></td><td>195.38 (+13.49%)</td><td>190.80 (+9.78%)</td><td>159.20 (+13.15%)</td><td>35.13 <b>(+58.81%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.50 (n/a)</td><td>172.16 (n/a)</td><td>173.80 (n/a)</td><td>140.70 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (+15.19%)</td><td>0.06 (+2.04%)</td><td>0.06 (-13.52%)</td><td>0.05 (+18.29%)</td><td>0.01 (+17.29%)</td><td>235.60 (-15.46%)</td><td>198.42 (-2.08%)</td><td>210.30 (+15.61%)</td><td>140.10 (-13.20%)</td><td>38.56 (-16.67%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>278.70 (n/a)</td><td>202.64 (n/a)</td><td>181.90 (n/a)</td><td>161.40 (n/a)</td><td>46.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (+17.78%)</td><td>0.16 (+4.03%)</td><td>0.15 (-8.14%)</td><td>0.13 (+14.21%)</td><td>0.04 <b>(+36.43%)</b></td><td>192.80 (-12.44%)</td><td>159.50 (-2.96%)</td><td>168.10 (+8.87%)</td><td>111.70 (-15.06%)</td><td>32.62 (-2.69%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>220.20 (n/a)</td><td>164.36 (n/a)</td><td>154.40 (n/a)</td><td>131.50 (n/a)</td><td>33.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (+9.62%)</td><td>0.14 (+2.92%)</td><td>0.14 (+1.42%)</td><td>0.12 (+4.49%)</td><td>0.02 (+16.39%)</td><td>209.00 (-4.30%)</td><td>174.78 (-2.62%)</td><td>171.90 (-1.38%)</td><td>139.30 (-8.78%)</td><td>25.05 (-0.64%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>218.40 (n/a)</td><td>179.48 (n/a)</td><td>174.30 (n/a)</td><td>152.70 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 <b>(-24.68%)</b></td><td>0.14 (-15.83%)</td><td>0.13 (-15.85%)</td><td>0.12 (-11.14%)</td><td>0.01 <b>(-47.12%)</b></td><td>212.40 (+12.50%)</td><td>182.66 (+17.36%)</td><td>184.00 (+18.86%)</td><td>159.00 <b>(+32.72%)</b></td><td>19.92 (-19.14%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>188.80 (n/a)</td><td>155.64 (n/a)</td><td>154.80 (n/a)</td><td>119.80 (n/a)</td><td>24.64 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (+9.46%)</td><td>0.15 (+0.96%)</td><td>0.13 (-10.15%)</td><td>0.11 (+0.13%)</td><td>0.04 <b>(+22.23%)</b></td><td>218.10 (-0.14%)</td><td>174.16 (+0.36%)</td><td>191.30 (+11.29%)</td><td>112.10 (-8.64%)</td><td>41.28 (+8.37%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>218.40 (n/a)</td><td>173.54 (n/a)</td><td>171.90 (n/a)</td><td>122.70 (n/a)</td><td>38.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (-17.48%)</td><td>0.13 (-1.29%)</td><td>0.13 (+8.44%)</td><td>0.11 (-2.30%)</td><td>0.01 <b>(-47.22%)</b></td><td>223.50 (+2.38%)</td><td>194.16 (-0.40%)</td><td>189.30 (-7.79%)</td><td>169.70 <b>(+21.21%)</b></td><td>21.38 <b>(-32.55%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>218.30 (n/a)</td><td>194.94 (n/a)</td><td>205.30 (n/a)</td><td>140.00 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (-11.23%)</td><td>0.13 (-8.88%)</td><td>0.13 (-10.44%)</td><td>0.12 (+5.54%)</td><td>0.02 <b>(-32.52%)</b></td><td>205.40 (-5.21%)</td><td>186.66 (+7.76%)</td><td>191.70 (+11.65%)</td><td>143.20 (+12.67%)</td><td>25.04 <b>(-29.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.70 (n/a)</td><td>173.22 (n/a)</td><td>171.70 (n/a)</td><td>127.10 (n/a)</td><td>35.60 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 <b>(-20.39%)</b></td><td>0.12 (-15.53%)</td><td>0.12 (-13.02%)</td><td>0.09 <b>(-24.58%)</b></td><td>0.02 (-16.40%)</td><td>288.60 <b>(+32.57%)</b></td><td>218.10 (+18.80%)</td><td>204.20 (+14.98%)</td><td>181.40 <b>(+25.62%)</b></td><td>42.69 <b>(+38.51%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.70 (n/a)</td><td>183.58 (n/a)</td><td>177.60 (n/a)</td><td>144.40 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 <b>(-29.50%)</b></td><td>0.11 (-11.58%)</td><td>0.11 (-15.73%)</td><td>0.08 (+8.93%)</td><td>0.02 <b>(-50.09%)</b></td><td>309.40 (-8.22%)</td><td>232.06 (+6.68%)</td><td>231.00 (+18.64%)</td><td>191.30 <b>(+41.91%)</b></td><td>47.61 <b>(-36.69%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>337.10 (n/a)</td><td>217.52 (n/a)</td><td>194.70 (n/a)</td><td>134.80 (n/a)</td><td>75.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.32 <b>(-32.25%)</b></td><td>0.28 (-14.75%)</td><td>0.28 (-5.98%)</td><td>0.25 (-8.46%)</td><td>0.03 <b>(-66.61%)</b></td><td>200.50 (+9.26%)</td><td>175.02 (+13.47%)</td><td>174.00 (+6.36%)</td><td>154.70 <b>(+47.61%)</b></td><td>17.31 <b>(-45.28%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.08 (n/a)</td><td>183.50 (n/a)</td><td>154.24 (n/a)</td><td>163.60 (n/a)</td><td>104.80 (n/a)</td><td>31.63 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.30 (-8.83%)</td><td>0.27 (+9.75%)</td><td>0.26 (-3.96%)</td><td>0.25 <b>(+80.53%)</b></td><td>0.02 <b>(-68.09%)</b></td><td>195.50 <b>(-44.62%)</b></td><td>182.16 (-15.83%)</td><td>189.90 (+4.11%)</td><td>165.40 (+9.68%)</td><td>14.54 <b>(-81.78%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>353.00 (n/a)</td><td>216.42 (n/a)</td><td>182.40 (n/a)</td><td>150.80 (n/a)</td><td>79.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.37 <b>(+20.68%)</b></td><td>0.31 (+16.33%)</td><td>0.29 (+5.45%)</td><td>0.24 (+9.90%)</td><td>0.05 <b>(+55.56%)</b></td><td>203.60 (-8.99%)</td><td>164.20 (-13.17%)</td><td>170.30 (-5.18%)</td><td>133.00 (-17.13%)</td><td>28.11 (+14.73%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>223.70 (n/a)</td><td>189.10 (n/a)</td><td>179.60 (n/a)</td><td>160.50 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.39 (+12.31%)</td><td>0.32 (+9.91%)</td><td>0.30 (+7.57%)</td><td>0.25 (+7.34%)</td><td>0.06 (+11.32%)</td><td>195.90 (-6.80%)</td><td>156.28 (-8.92%)</td><td>164.20 (-7.07%)</td><td>124.90 (-10.98%)</td><td>28.63 (-6.12%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>210.20 (n/a)</td><td>171.58 (n/a)</td><td>176.70 (n/a)</td><td>140.30 (n/a)</td><td>30.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 <b>(-22.95%)</b></td><td>0.25 (-18.34%)</td><td>0.25 (-16.72%)</td><td>0.22 <b>(-21.26%)</b></td><td>0.01 <b>(-27.71%)</b></td><td>223.00 <b>(+26.99%)</b></td><td>200.80 <b>(+22.41%)</b></td><td>197.20 <b>(+20.10%)</b></td><td>191.60 <b>(+29.81%)</b></td><td>12.77 <b>(+21.03%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.02 (n/a)</td><td>175.60 (n/a)</td><td>164.04 (n/a)</td><td>164.20 (n/a)</td><td>147.60 (n/a)</td><td>10.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.38 (+1.88%)</td><td>0.28 (-4.48%)</td><td>0.28 (+0.73%)</td><td>0.22 (+7.74%)</td><td>0.06 (-4.54%)</td><td>218.90 (-7.17%)</td><td>179.34 (+4.04%)</td><td>173.30 (-0.74%)</td><td>130.80 (-1.80%)</td><td>34.97 (-12.73%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>235.80 (n/a)</td><td>172.38 (n/a)</td><td>174.60 (n/a)</td><td>133.20 (n/a)</td><td>40.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (-10.61%)</td><td>0.24 (-9.78%)</td><td>0.24 <b>(-21.33%)</b></td><td>0.19 (-3.22%)</td><td>0.04 <b>(-35.47%)</b></td><td>260.10 (+3.34%)</td><td>208.34 (+8.70%)</td><td>207.80 <b>(+27.09%)</b></td><td>176.40 (+11.86%)</td><td>33.06 <b>(-24.03%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>251.70 (n/a)</td><td>191.66 (n/a)</td><td>163.50 (n/a)</td><td>157.70 (n/a)</td><td>43.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.31 (+11.37%)</td><td>0.25 (+4.17%)</td><td>0.25 (-0.13%)</td><td>0.19 (-9.90%)</td><td>0.05 <b>(+41.51%)</b></td><td>261.70 (+11.03%)</td><td>198.92 (-2.60%)</td><td>194.40 (+0.10%)</td><td>157.20 (-10.22%)</td><td>40.19 <b>(+39.61%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>235.70 (n/a)</td><td>204.22 (n/a)</td><td>194.20 (n/a)</td><td>175.10 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (-0.89%)</td><td>0.02 (+16.05%)</td><td>0.02 <b>(+35.83%)</b></td><td>0.01 <b>(+38.53%)</b></td><td>0.00 <b>(-25.18%)</b></td><td>192.30 <b>(-27.82%)</b></td><td>161.52 (-16.26%)</td><td>142.90 <b>(-26.38%)</b></td><td>140.10 (+0.94%)</td><td>27.08 <b>(-45.01%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>266.40 (n/a)</td><td>192.88 (n/a)</td><td>194.10 (n/a)</td><td>138.80 (n/a)</td><td>49.25 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (-17.21%)</td><td>0.02 (-8.21%)</td><td>0.02 (-11.29%)</td><td>0.01 (+8.48%)</td><td>0.00 <b>(-42.67%)</b></td><td>210.70 (-7.83%)</td><td>161.72 (+5.12%)</td><td>154.60 (+12.76%)</td><td>136.10 <b>(+20.76%)</b></td><td>28.65 <b>(-36.29%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>228.60 (n/a)</td><td>153.84 (n/a)</td><td>137.10 (n/a)</td><td>112.70 (n/a)</td><td>44.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 <b>(-22.05%)</b></td><td>0.02 (-11.88%)</td><td>0.02 (-8.35%)</td><td>0.01 (-6.62%)</td><td>0.00 <b>(-47.04%)</b></td><td>179.30 (+7.11%)</td><td>155.38 (+11.59%)</td><td>155.80 (+9.10%)</td><td>130.80 <b>(+28.36%)</b></td><td>18.20 <b>(-25.68%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>167.40 (n/a)</td><td>139.24 (n/a)</td><td>142.80 (n/a)</td><td>101.90 (n/a)</td><td>24.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (-11.27%)</td><td>0.01 (-13.36%)</td><td>0.02 (-9.06%)</td><td>0.01 (-16.30%)</td><td>0.00 (+14.24%)</td><td>228.20 (+19.48%)</td><td>182.86 (+16.92%)</td><td>167.70 (+9.97%)</td><td>145.60 (+12.69%)</td><td>35.98 <b>(+55.39%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>191.00 (n/a)</td><td>156.40 (n/a)</td><td>152.50 (n/a)</td><td>129.20 (n/a)</td><td>23.15 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 <b>(-25.57%)</b></td><td>0.02 <b>(-26.36%)</b></td><td>0.01 <b>(-28.58%)</b></td><td>0.01 <b>(-28.24%)</b></td><td>0.00 (-19.84%)</td><td>205.00 <b>(+39.36%)</b></td><td>177.34 <b>(+36.33%)</b></td><td>190.20 <b>(+40.06%)</b></td><td>134.00 <b>(+34.40%)</b></td><td>27.85 <b>(+50.82%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>147.10 (n/a)</td><td>130.08 (n/a)</td><td>135.80 (n/a)</td><td>99.70 (n/a)</td><td>18.47 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (-3.78%)</td><td>0.01 (+0.75%)</td><td>0.02 (+3.39%)</td><td>0.01 (-5.57%)</td><td>0.00 (-9.54%)</td><td>220.90 (+5.90%)</td><td>179.68 (-0.87%)</td><td>170.70 (-3.29%)</td><td>160.80 (+3.94%)</td><td>23.74 (+1.01%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.60 (n/a)</td><td>181.26 (n/a)</td><td>176.50 (n/a)</td><td>154.70 (n/a)</td><td>23.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (-17.87%)</td><td>0.01 (-12.08%)</td><td>0.01 (-11.00%)</td><td>0.01 (+7.76%)</td><td>0.00 <b>(-51.10%)</b></td><td>215.10 (-7.20%)</td><td>189.10 (+11.29%)</td><td>182.10 (+12.41%)</td><td>172.20 <b>(+21.70%)</b></td><td>19.03 <b>(-46.94%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>231.80 (n/a)</td><td>169.92 (n/a)</td><td>162.00 (n/a)</td><td>141.50 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.01 (-15.92%)</td><td>0.01 (-14.54%)</td><td>0.01 (-15.77%)</td><td>0.01 (-7.10%)</td><td>0.00 <b>(-62.01%)</b></td><td>224.30 (+7.63%)</td><td>212.54 (+16.56%)</td><td>211.40 (+18.76%)</td><td>205.50 (+18.92%)</td><td>7.13 <b>(-51.74%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>182.34 (n/a)</td><td>178.00 (n/a)</td><td>172.80 (n/a)</td><td>14.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-11.13%)</td><td>0.03 (-17.27%)</td><td>0.04 (-16.72%)</td><td>0.03 <b>(-28.91%)</b></td><td>0.01 <b>(+80.64%)</b></td><td>199.20 <b>(+40.68%)</b></td><td>154.74 <b>(+23.40%)</b></td><td>146.40 <b>(+20.10%)</b></td><td>128.70 (+12.50%)</td><td>29.01 <b>(+181.86%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>141.60 (n/a)</td><td>125.40 (n/a)</td><td>121.90 (n/a)</td><td>114.40 (n/a)</td><td>10.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-10.37%)</td><td>0.03 (-10.12%)</td><td>0.03 (-19.66%)</td><td>0.03 (+0.92%)</td><td>0.00 <b>(-41.76%)</b></td><td>201.10 (-0.89%)</td><td>172.00 (+9.33%)</td><td>173.00 <b>(+24.46%)</b></td><td>146.60 (+11.57%)</td><td>20.06 <b>(-35.09%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>157.32 (n/a)</td><td>139.00 (n/a)</td><td>131.40 (n/a)</td><td>30.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-5.94%)</td><td>0.03 (-4.61%)</td><td>0.03 (+0.74%)</td><td>0.03 (-11.03%)</td><td>0.00 (-6.12%)</td><td>190.30 (+12.40%)</td><td>157.16 (+4.90%)</td><td>150.80 (-0.72%)</td><td>134.50 (+6.24%)</td><td>22.04 (+11.83%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>169.30 (n/a)</td><td>149.82 (n/a)</td><td>151.90 (n/a)</td><td>126.60 (n/a)</td><td>19.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (+9.17%)</td><td>0.03 (+0.64%)</td><td>0.03 (+12.23%)</td><td>0.02 <b>(-24.19%)</b></td><td>0.01 <b>(+70.77%)</b></td><td>281.10 <b>(+31.91%)</b></td><td>190.52 (+3.26%)</td><td>167.70 (-10.89%)</td><td>142.20 (-8.38%)</td><td>53.92 <b>(+116.26%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>184.50 (n/a)</td><td>188.20 (n/a)</td><td>155.20 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (+2.39%)</td><td>0.03 (+10.24%)</td><td>0.03 (+7.44%)</td><td>0.02 (-1.17%)</td><td>0.01 (+13.47%)</td><td>224.70 (+1.22%)</td><td>169.04 (-8.28%)</td><td>172.30 (-6.92%)</td><td>122.90 (-2.31%)</td><td>41.48 (+14.46%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.00 (n/a)</td><td>184.30 (n/a)</td><td>185.10 (n/a)</td><td>125.80 (n/a)</td><td>36.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-1.38%)</td><td>0.03 (+12.09%)</td><td>0.03 <b>(+27.26%)</b></td><td>0.03 <b>(+68.99%)</b></td><td>0.01 <b>(-50.39%)</b></td><td>191.10 <b>(-40.82%)</b></td><td>171.84 (-18.67%)</td><td>178.80 <b>(-21.41%)</b></td><td>131.20 (+1.39%)</td><td>23.39 <b>(-69.93%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>322.90 (n/a)</td><td>211.30 (n/a)</td><td>227.50 (n/a)</td><td>129.40 (n/a)</td><td>77.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-7.86%)</td><td>0.03 (+8.38%)</td><td>0.03 (+4.16%)</td><td>0.03 <b>(+33.86%)</b></td><td>0.00 <b>(-58.35%)</b></td><td>181.10 <b>(-25.32%)</b></td><td>168.30 (-11.22%)</td><td>170.60 (-4.00%)</td><td>144.70 (+8.47%)</td><td>14.41 <b>(-66.93%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.50 (n/a)</td><td>189.56 (n/a)</td><td>177.70 (n/a)</td><td>133.40 (n/a)</td><td>43.57 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+5.21%)</td><td>0.02 (-6.67%)</td><td>0.02 (-7.79%)</td><td>0.02 <b>(-26.91%)</b></td><td>0.01 <b>(+99.04%)</b></td><td>330.40 <b>(+36.81%)</b></td><td>226.24 (+12.45%)</td><td>211.30 (+8.47%)</td><td>162.90 (-4.96%)</td><td>65.96 <b>(+157.47%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.50 (n/a)</td><td>201.20 (n/a)</td><td>194.80 (n/a)</td><td>171.40 (n/a)</td><td>25.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (+7.96%)</td><td>0.07 (+4.45%)</td><td>0.07 (+3.68%)</td><td>0.05 (-7.66%)</td><td>0.02 <b>(+42.22%)</b></td><td>204.70 (+8.31%)</td><td>156.00 (-2.35%)</td><td>157.60 (-3.55%)</td><td>119.90 (-7.41%)</td><td>35.32 <b>(+39.39%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>159.76 (n/a)</td><td>163.40 (n/a)</td><td>129.50 (n/a)</td><td>25.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (-14.39%)</td><td>0.06 (-7.05%)</td><td>0.06 (-3.22%)</td><td>0.05 (-16.46%)</td><td>0.01 (+0.27%)</td><td>229.80 (+19.75%)</td><td>183.80 (+8.45%)</td><td>183.40 (+3.32%)</td><td>150.00 (+16.82%)</td><td>34.13 <b>(+41.54%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>169.48 (n/a)</td><td>177.50 (n/a)</td><td>128.40 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (+17.87%)</td><td>0.06 (-4.02%)</td><td>0.07 (-3.81%)</td><td>0.05 (-16.20%)</td><td>0.01 <b>(+118.38%)</b></td><td>231.70 (+19.37%)</td><td>176.66 (+7.97%)</td><td>160.10 (+3.96%)</td><td>127.70 (-15.15%)</td><td>41.91 <b>(+126.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>163.62 (n/a)</td><td>154.00 (n/a)</td><td>150.50 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (+13.31%)</td><td>0.06 (+8.55%)</td><td>0.06 (+9.32%)</td><td>0.05 (+3.91%)</td><td>0.01 (+13.46%)</td><td>205.30 (-3.75%)</td><td>166.62 (-7.70%)</td><td>167.20 (-8.48%)</td><td>134.80 (-11.72%)</td><td>25.37 (-1.47%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>180.52 (n/a)</td><td>182.70 (n/a)</td><td>152.70 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (-15.26%)</td><td>0.07 (+5.40%)</td><td>0.06 (+7.74%)</td><td>0.06 (+13.60%)</td><td>0.01 <b>(-41.39%)</b></td><td>187.00 (-11.96%)</td><td>157.86 (-8.15%)</td><td>162.90 (-7.18%)</td><td>129.50 (+17.94%)</td><td>24.38 <b>(-37.46%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>171.86 (n/a)</td><td>175.50 (n/a)</td><td>109.80 (n/a)</td><td>38.98 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+1.34%)</td><td>0.06 (+11.25%)</td><td>0.06 (+6.25%)</td><td>0.05 <b>(+38.34%)</b></td><td>0.01 (-10.89%)</td><td>222.20 <b>(-27.72%)</b></td><td>181.68 (-12.47%)</td><td>188.30 (-5.90%)</td><td>142.50 (-1.32%)</td><td>36.40 <b>(-40.03%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.40 (n/a)</td><td>207.56 (n/a)</td><td>200.10 (n/a)</td><td>144.40 (n/a)</td><td>60.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (+4.05%)</td><td>0.07 <b>(+20.52%)</b></td><td>0.08 <b>(+34.36%)</b></td><td>0.05 (+1.17%)</td><td>0.02 (+18.16%)</td><td>222.30 (-1.16%)</td><td>152.80 (-15.91%)</td><td>134.80 <b>(-25.57%)</b></td><td>123.00 (-3.83%)</td><td>41.25 (+17.01%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>181.72 (n/a)</td><td>181.10 (n/a)</td><td>127.90 (n/a)</td><td>35.25 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 <b>(+20.87%)</b></td><td>0.06 (+11.34%)</td><td>0.06 (+14.30%)</td><td>0.04 (+6.10%)</td><td>0.01 <b>(+47.64%)</b></td><td>239.50 (-5.75%)</td><td>193.72 (-8.99%)</td><td>190.30 (-12.51%)</td><td>149.70 (-17.25%)</td><td>37.82 (+19.44%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>254.10 (n/a)</td><td>212.86 (n/a)</td><td>217.50 (n/a)</td><td>180.90 (n/a)</td><td>31.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (-14.72%)</td><td>0.11 (-19.76%)</td><td>0.12 <b>(-20.45%)</b></td><td>0.09 (-19.91%)</td><td>0.02 (-11.44%)</td><td>222.00 <b>(+24.86%)</b></td><td>188.74 <b>(+24.96%)</b></td><td>179.70 <b>(+25.75%)</b></td><td>152.70 (+17.28%)</td><td>28.99 <b>(+31.71%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>177.80 (n/a)</td><td>151.04 (n/a)</td><td>142.90 (n/a)</td><td>130.20 (n/a)</td><td>22.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (+7.49%)</td><td>0.12 (+15.12%)</td><td>0.12 (+16.82%)</td><td>0.10 <b>(+41.51%)</b></td><td>0.01 <b>(-37.91%)</b></td><td>204.70 <b>(-29.34%)</b></td><td>179.26 (-16.00%)</td><td>170.20 (-14.39%)</td><td>155.30 (-6.95%)</td><td>22.68 <b>(-57.17%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>289.70 (n/a)</td><td>213.40 (n/a)</td><td>198.80 (n/a)</td><td>166.90 (n/a)</td><td>52.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (+9.40%)</td><td>0.12 (-4.71%)</td><td>0.12 (-0.14%)</td><td>0.10 (-14.84%)</td><td>0.02 <b>(+105.74%)</b></td><td>218.40 (+17.42%)</td><td>183.16 (+7.56%)</td><td>177.90 (+0.11%)</td><td>136.10 (-8.66%)</td><td>35.37 <b>(+128.91%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>170.28 (n/a)</td><td>177.70 (n/a)</td><td>149.00 (n/a)</td><td>15.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (+16.58%)</td><td>0.12 (+9.62%)</td><td>0.12 (+7.90%)</td><td>0.11 (+8.63%)</td><td>0.02 <b>(+35.59%)</b></td><td>196.80 (-7.95%)</td><td>173.18 (-8.37%)</td><td>178.00 (-7.34%)</td><td>135.10 (-14.28%)</td><td>22.79 (+3.99%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>189.00 (n/a)</td><td>192.10 (n/a)</td><td>157.60 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (+16.77%)</td><td>0.12 <b>(+23.01%)</b></td><td>0.13 (+16.00%)</td><td>0.10 <b>(+31.44%)</b></td><td>0.01 <b>(-20.14%)</b></td><td>201.20 <b>(-23.90%)</b></td><td>170.70 <b>(-20.05%)</b></td><td>167.00 (-13.78%)</td><td>149.80 (-14.35%)</td><td>21.14 <b>(-48.83%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>264.40 (n/a)</td><td>213.52 (n/a)</td><td>193.70 (n/a)</td><td>174.90 (n/a)</td><td>41.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (+14.43%)</td><td>0.12 (+12.56%)</td><td>0.12 <b>(+20.76%)</b></td><td>0.10 (+16.28%)</td><td>0.02 (+9.35%)</td><td>216.90 (-14.00%)</td><td>185.54 (-11.37%)</td><td>182.20 (-17.18%)</td><td>140.80 (-12.60%)</td><td>29.43 (-17.85%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>252.20 (n/a)</td><td>209.34 (n/a)</td><td>220.00 (n/a)</td><td>161.10 (n/a)</td><td>35.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 <b>(+34.75%)</b></td><td>0.12 (+9.61%)</td><td>0.11 (-2.82%)</td><td>0.10 (-5.13%)</td><td>0.03 <b>(+252.29%)</b></td><td>218.80 (+5.45%)</td><td>180.30 (-4.37%)</td><td>199.50 (+2.89%)</td><td>126.20 <b>(-25.81%)</b></td><td>43.54 <b>(+182.57%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>188.54 (n/a)</td><td>193.90 (n/a)</td><td>170.10 (n/a)</td><td>15.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (-0.48%)</td><td>0.09 (-3.38%)</td><td>0.10 (-0.73%)</td><td>0.08 (-9.59%)</td><td>0.01 <b>(+52.23%)</b></td><td>247.20 (+10.60%)</td><td>222.68 (+3.84%)</td><td>220.90 (+0.73%)</td><td>199.10 (+0.50%)</td><td>18.53 <b>(+68.48%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>214.44 (n/a)</td><td>219.30 (n/a)</td><td>198.10 (n/a)</td><td>11.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>176.80 (n/a)</td><td>159.34 (n/a)</td><td>170.80 (n/a)</td><td>138.20 (n/a)</td><td>18.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>159.24 (n/a)</td><td>155.00 (n/a)</td><td>129.60 (n/a)</td><td>25.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>161.20 (n/a)</td><td>164.30 (n/a)</td><td>117.00 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>219.20 (n/a)</td><td>196.58 (n/a)</td><td>193.00 (n/a)</td><td>180.90 (n/a)</td><td>16.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.20 (n/a)</td><td>173.30 (n/a)</td><td>168.90 (n/a)</td><td>155.90 (n/a)</td><td>15.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.10 (n/a)</td><td>159.44 (n/a)</td><td>159.20 (n/a)</td><td>116.50 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>177.46 (n/a)</td><td>174.60 (n/a)</td><td>156.60 (n/a)</td><td>19.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>279.20 (n/a)</td><td>194.12 (n/a)</td><td>175.50 (n/a)</td><td>141.80 (n/a)</td><td>51.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>199.10 (n/a)</td><td>171.56 (n/a)</td><td>182.90 (n/a)</td><td>128.70 (n/a)</td><td>26.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>183.70 (n/a)</td><td>155.16 (n/a)</td><td>150.10 (n/a)</td><td>119.30 (n/a)</td><td>25.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>169.32 (n/a)</td><td>168.60 (n/a)</td><td>145.20 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>222.70 (n/a)</td><td>179.38 (n/a)</td><td>177.20 (n/a)</td><td>141.90 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.38 (-0.73%)</td><td>0.33 (+2.03%)</td><td>0.34 (-1.83%)</td><td>0.29 (+18.96%)</td><td>0.04 <b>(-30.07%)</b></td><td>171.50 (-15.97%)</td><td>151.10 (-3.60%)</td><td>143.80 (+1.91%)</td><td>130.90 (+0.77%)</td><td>19.17 <b>(-39.04%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>204.10 (n/a)</td><td>156.74 (n/a)</td><td>141.10 (n/a)</td><td>129.90 (n/a)</td><td>31.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>194.50 (n/a)</td><td>162.06 (n/a)</td><td>149.30 (n/a)</td><td>132.90 (n/a)</td><td>29.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>205.50 (n/a)</td><td>176.18 (n/a)</td><td>175.60 (n/a)</td><td>146.40 (n/a)</td><td>21.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>316.30 (n/a)</td><td>244.82 (n/a)</td><td>224.70 (n/a)</td><td>171.30 (n/a)</td><td>60.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>142.42 (n/a)</td><td>132.90 (n/a)</td><td>121.60 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>168.70 (n/a)</td><td>150.88 (n/a)</td><td>153.80 (n/a)</td><td>133.50 (n/a)</td><td>16.23 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>172.00 (n/a)</td><td>151.92 (n/a)</td><td>153.10 (n/a)</td><td>135.80 (n/a)</td><td>14.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.40 (n/a)</td><td>170.70 (n/a)</td><td>166.60 (n/a)</td><td>161.30 (n/a)</td><td>10.87 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>178.60 (n/a)</td><td>148.36 (n/a)</td><td>142.30 (n/a)</td><td>129.30 (n/a)</td><td>19.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>245.90 (n/a)</td><td>187.60 (n/a)</td><td>179.50 (n/a)</td><td>131.60 (n/a)</td><td>43.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>160.34 (n/a)</td><td>152.10 (n/a)</td><td>135.40 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>306.30 (n/a)</td><td>205.70 (n/a)</td><td>206.70 (n/a)</td><td>131.70 (n/a)</td><td>69.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>201.40 (n/a)</td><td>165.96 (n/a)</td><td>166.40 (n/a)</td><td>138.90 (n/a)</td><td>23.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>208.70 (n/a)</td><td>176.96 (n/a)</td><td>175.30 (n/a)</td><td>152.50 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>239.20 (n/a)</td><td>181.24 (n/a)</td><td>169.10 (n/a)</td><td>156.90 (n/a)</td><td>33.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>249.10 (n/a)</td><td>203.82 (n/a)</td><td>193.10 (n/a)</td><td>191.20 (n/a)</td><td>25.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>202.90 (n/a)</td><td>172.94 (n/a)</td><td>176.30 (n/a)</td><td>138.90 (n/a)</td><td>24.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>186.00 (n/a)</td><td>165.00 (n/a)</td><td>168.70 (n/a)</td><td>134.30 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>223.40 (n/a)</td><td>191.70 (n/a)</td><td>199.00 (n/a)</td><td>160.00 (n/a)</td><td>29.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>14.67 (+4.59%)</td><td>14.02 (+2.85%)</td><td>14.04 (+0.78%)</td><td>12.80 (-0.23%)</td><td>0.76 <b>(+50.53%)</b></td><td>4352.90 (+0.23%)</td><td>3982.22 (-2.64%)</td><td>3967.40 (-0.78%)</td><td>3797.30 (-4.39%)</td><td>226.25 <b>(+44.32%)</b></td><td>14138.10 (+4.59%)</td><td>13515.06 (+2.85%)</td><td>13531.90 (+0.78%)</td><td>12333.66 (-0.23%)</td><td>734.91 <b>(+50.53%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.03 (n/a)</td><td>13.63 (n/a)</td><td>13.93 (n/a)</td><td>12.83 (n/a)</td><td>0.51 (n/a)</td><td>4343.00 (n/a)</td><td>4090.38 (n/a)</td><td>3998.60 (n/a)</td><td>3971.70 (n/a)</td><td>156.78 (n/a)</td><td>13517.38 (n/a)</td><td>13140.21 (n/a)</td><td>13426.58 (n/a)</td><td>12361.80 (n/a)</td><td>488.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>18.74 (-15.20%)</td><td>15.49 (-14.55%)</td><td>16.04 (-6.97%)</td><td>12.49 <b>(-25.13%)</b></td><td>2.47 (+9.56%)</td><td>1049.00 <b>(+33.55%)</b></td><td>863.84 (+18.20%)</td><td>817.30 (+7.50%)</td><td>699.60 (+17.94%)</td><td>139.84 <b>(+76.83%)</b></td><td>12279.21 (-15.20%)</td><td>10152.26 (-14.55%)</td><td>10509.94 (-6.97%)</td><td>8188.41 <b>(-25.13%)</b></td><td>1619.19 (+9.56%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>22.09 (n/a)</td><td>18.13 (n/a)</td><td>17.24 (n/a)</td><td>16.69 (n/a)</td><td>2.26 (n/a)</td><td>785.50 (n/a)</td><td>730.84 (n/a)</td><td>760.30 (n/a)</td><td>593.20 (n/a)</td><td>79.08 (n/a)</td><td>14479.96 (n/a)</td><td>11881.00 (n/a)</td><td>11297.83 (n/a)</td><td>10936.13 (n/a)</td><td>1477.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>14.15 (+0.82%)</td><td>13.68 (+5.78%)</td><td>13.88 (+8.73%)</td><td>12.86 (+3.42%)</td><td>0.55 (-13.49%)</td><td>4332.90 (-3.31%)</td><td>4078.64 (-5.51%)</td><td>4013.00 (-8.03%)</td><td>3937.00 (-0.82%)</td><td>167.48 (-16.33%)</td><td>13636.61 (+0.82%)</td><td>13180.33 (+5.78%)</td><td>13378.38 (+8.73%)</td><td>12390.65 (+3.42%)</td><td>528.13 (-13.49%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.03 (n/a)</td><td>12.93 (n/a)</td><td>12.77 (n/a)</td><td>12.43 (n/a)</td><td>0.63 (n/a)</td><td>4481.10 (n/a)</td><td>4316.70 (n/a)</td><td>4363.50 (n/a)</td><td>3969.50 (n/a)</td><td>200.17 (n/a)</td><td>13525.06 (n/a)</td><td>12459.79 (n/a)</td><td>12303.69 (n/a)</td><td>11980.87 (n/a)</td><td>610.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>18.93 (-1.87%)</td><td>16.23 (-1.36%)</td><td>16.59 (-5.36%)</td><td>11.79 (+6.56%)</td><td>2.67 (-15.57%)</td><td>1514.50 (-6.16%)</td><td>1129.38 (+0.15%)</td><td>1076.20 (+5.67%)</td><td>943.20 (+1.89%)</td><td>222.62 (-19.65%)</td><td>14229.36 (-1.87%)</td><td>12198.38 (-1.36%)</td><td>12471.60 (-5.36%)</td><td>8862.23 (+6.56%)</td><td>2007.75 (-15.57%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>19.29 (n/a)</td><td>16.45 (n/a)</td><td>17.53 (n/a)</td><td>11.07 (n/a)</td><td>3.16 (n/a)</td><td>1613.90 (n/a)</td><td>1127.64 (n/a)</td><td>1018.50 (n/a)</td><td>925.70 (n/a)</td><td>277.06 (n/a)</td><td>14499.82 (n/a)</td><td>12366.82 (n/a)</td><td>13177.36 (n/a)</td><td>8316.51 (n/a)</td><td>2377.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>10.98 (+0.07%)</td><td>10.62 (-1.33%)</td><td>10.74 (-0.43%)</td><td>9.98 (-4.71%)</td><td>0.42 <b>(+103.94%)</b></td><td>8209.30 (+4.95%)</td><td>7724.88 (+1.45%)</td><td>7628.30 (+0.43%)</td><td>7461.60 (-0.07%)</td><td>312.26 <b>(+113.68%)</b></td><td>14390.20 (+0.07%)</td><td>13917.49 (-1.33%)</td><td>14075.80 (-0.43%)</td><td>13079.53 (-4.71%)</td><td>548.40 <b>(+103.94%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>10.97 (n/a)</td><td>10.76 (n/a)</td><td>10.79 (n/a)</td><td>10.47 (n/a)</td><td>0.21 (n/a)</td><td>7822.30 (n/a)</td><td>7614.30 (n/a)</td><td>7595.50 (n/a)</td><td>7467.00 (n/a)</td><td>146.13 (n/a)</td><td>14379.85 (n/a)</td><td>14105.78 (n/a)</td><td>14136.62 (n/a)</td><td>13726.67 (n/a)</td><td>268.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>19.96 (+0.16%)</td><td>18.37 (+5.26%)</td><td>18.06 (-0.57%)</td><td>17.68 <b>(+40.21%)</b></td><td>0.91 <b>(-67.81%)</b></td><td>1215.50 <b>(-28.68%)</b></td><td>1172.00 (-7.25%)</td><td>1190.60 (+0.58%)</td><td>1076.70 (-0.16%)</td><td>54.67 <b>(-78.20%)</b></td><td>15956.06 (+0.16%)</td><td>14685.55 (+5.26%)</td><td>14430.13 (-0.57%)</td><td>14133.85 <b>(+40.21%)</b></td><td>725.13 <b>(-67.81%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>19.93 (n/a)</td><td>17.46 (n/a)</td><td>18.16 (n/a)</td><td>12.61 (n/a)</td><td>2.82 (n/a)</td><td>1704.20 (n/a)</td><td>1263.62 (n/a)</td><td>1183.70 (n/a)</td><td>1078.40 (n/a)</td><td>250.74 (n/a)</td><td>15931.01 (n/a)</td><td>13951.67 (n/a)</td><td>14513.19 (n/a)</td><td>10080.76 (n/a)</td><td>2252.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.51 (-6.50%)</td><td>12.28 (-0.50%)</td><td>12.40 (-0.20%)</td><td>11.72 (+5.81%)</td><td>0.32 <b>(-61.27%)</b></td><td>6987.50 (-5.49%)</td><td>6672.12 (+0.19%)</td><td>6609.00 (+0.20%)</td><td>6548.20 (+6.95%)</td><td>178.42 <b>(-61.09%)</b></td><td>16397.62 (-6.50%)</td><td>16101.92 (-0.50%)</td><td>16246.72 (-0.20%)</td><td>15366.71 (+5.81%)</td><td>416.57 <b>(-61.27%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.38 (n/a)</td><td>12.35 (n/a)</td><td>12.42 (n/a)</td><td>11.08 (n/a)</td><td>0.82 (n/a)</td><td>7393.70 (n/a)</td><td>6659.14 (n/a)</td><td>6595.70 (n/a)</td><td>6122.50 (n/a)</td><td>458.54 (n/a)</td><td>17537.63 (n/a)</td><td>16183.44 (n/a)</td><td>16279.39 (n/a)</td><td>14522.42 (n/a)</td><td>1075.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>4.71 (-8.33%)</td><td>3.70 (-9.04%)</td><td>3.70 (-5.88%)</td><td>2.99 (-4.50%)</td><td>0.71 <b>(-27.19%)</b></td><td>460.80 (+4.70%)</td><td>382.38 (+8.02%)</td><td>371.80 (+6.23%)</td><td>292.00 (+9.08%)</td><td>70.28 (-15.82%)</td><td>919.25 (-8.33%)</td><td>722.02 (-9.04%)</td><td>721.96 (-5.88%)</td><td>582.56 (-4.50%)</td><td>137.60 <b>(-27.19%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.14 (n/a)</td><td>4.07 (n/a)</td><td>3.93 (n/a)</td><td>3.13 (n/a)</td><td>0.97 (n/a)</td><td>440.10 (n/a)</td><td>354.00 (n/a)</td><td>350.00 (n/a)</td><td>267.70 (n/a)</td><td>83.48 (n/a)</td><td>1002.75 (n/a)</td><td>793.78 (n/a)</td><td>767.03 (n/a)</td><td>609.99 (n/a)</td><td>188.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.82 (+8.78%)</td><td>4.17 (+0.21%)</td><td>3.53 (-1.86%)</td><td>3.46 (-0.65%)</td><td>1.48 <b>(+24.30%)</b></td><td>398.10 (+0.66%)</td><td>354.32 (+1.94%)</td><td>389.70 (+1.91%)</td><td>201.70 (-8.07%)</td><td>85.41 (+15.69%)</td><td>1330.64 (+8.78%)</td><td>813.37 (+0.21%)</td><td>688.84 (-1.86%)</td><td>674.30 (-0.65%)</td><td>289.25 <b>(+24.30%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>6.27 (n/a)</td><td>4.16 (n/a)</td><td>3.60 (n/a)</td><td>3.48 (n/a)</td><td>1.19 (n/a)</td><td>395.50 (n/a)</td><td>347.56 (n/a)</td><td>382.40 (n/a)</td><td>219.40 (n/a)</td><td>73.83 (n/a)</td><td>1223.24 (n/a)</td><td>811.66 (n/a)</td><td>701.89 (n/a)</td><td>678.74 (n/a)</td><td>232.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.17 <b>(-22.35%)</b></td><td>4.72 (-4.35%)</td><td>5.25 <b>(+34.06%)</b></td><td>3.40 (-5.84%)</td><td>1.21 <b>(-33.16%)</b></td><td>404.70 (+6.22%)</td><td>308.62 (+1.52%)</td><td>262.20 <b>(-25.41%)</b></td><td>223.10 <b>(+28.81%)</b></td><td>83.53 (-3.90%)</td><td>1203.13 <b>(-22.35%)</b></td><td>920.61 (-4.35%)</td><td>1023.86 <b>(+34.06%)</b></td><td>663.36 (-5.84%)</td><td>236.53 <b>(-33.16%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.94 (n/a)</td><td>4.93 (n/a)</td><td>3.92 (n/a)</td><td>3.61 (n/a)</td><td>1.81 (n/a)</td><td>381.00 (n/a)</td><td>304.00 (n/a)</td><td>351.50 (n/a)</td><td>173.20 (n/a)</td><td>86.93 (n/a)</td><td>1549.41 (n/a)</td><td>962.43 (n/a)</td><td>763.73 (n/a)</td><td>704.47 (n/a)</td><td>353.87 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.97 <b>(-33.61%)</b></td><td>4.14 <b>(-24.36%)</b></td><td>3.65 <b>(-33.97%)</b></td><td>3.55 (+3.00%)</td><td>1.03 <b>(-54.12%)</b></td><td>387.30 (-2.91%)</td><td>345.00 <b>(+21.48%)</b></td><td>377.00 <b>(+51.41%)</b></td><td>230.30 <b>(+50.62%)</b></td><td>65.34 <b>(-37.49%)</b></td><td>1165.40 <b>(-33.61%)</b></td><td>808.45 <b>(-24.36%)</b></td><td>711.96 <b>(-33.97%)</b></td><td>693.17 (+3.00%)</td><td>201.09 <b>(-54.12%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>9.00 (n/a)</td><td>5.48 (n/a)</td><td>5.53 (n/a)</td><td>3.45 (n/a)</td><td>2.25 (n/a)</td><td>398.90 (n/a)</td><td>284.00 (n/a)</td><td>249.00 (n/a)</td><td>152.90 (n/a)</td><td>104.52 (n/a)</td><td>1755.50 (n/a)</td><td>1068.83 (n/a)</td><td>1078.21 (n/a)</td><td>672.99 (n/a)</td><td>438.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.53 (+15.97%)</td><td>4.31 (+14.49%)</td><td>3.97 (+18.80%)</td><td>3.22 (+0.44%)</td><td>1.34 <b>(+27.89%)</b></td><td>427.80 (-0.44%)</td><td>340.30 (-11.09%)</td><td>346.70 (-15.83%)</td><td>210.80 (-13.78%)</td><td>86.92 (+11.41%)</td><td>1273.47 (+15.97%)</td><td>840.98 (+14.49%)</td><td>774.19 (+18.80%)</td><td>627.50 (+0.44%)</td><td>260.77 <b>(+27.89%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.63 (n/a)</td><td>3.77 (n/a)</td><td>3.34 (n/a)</td><td>3.20 (n/a)</td><td>1.05 (n/a)</td><td>429.70 (n/a)</td><td>382.74 (n/a)</td><td>411.90 (n/a)</td><td>244.50 (n/a)</td><td>78.02 (n/a)</td><td>1098.09 (n/a)</td><td>734.56 (n/a)</td><td>651.69 (n/a)</td><td>624.77 (n/a)</td><td>203.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.48 (+4.98%)</td><td>3.65 (-10.42%)</td><td>3.20 <b>(-28.18%)</b></td><td>3.05 (+2.36%)</td><td>1.03 (+6.30%)</td><td>450.80 (-2.30%)</td><td>395.58 (+11.60%)</td><td>430.60 <b>(+39.22%)</b></td><td>251.00 (-4.74%)</td><td>83.11 (-6.66%)</td><td>1069.39 (+4.98%)</td><td>712.33 (-10.42%)</td><td>623.33 <b>(-28.18%)</b></td><td>595.48 (+2.36%)</td><td>201.68 (+6.30%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.22 (n/a)</td><td>4.08 (n/a)</td><td>4.45 (n/a)</td><td>2.98 (n/a)</td><td>0.97 (n/a)</td><td>461.40 (n/a)</td><td>354.46 (n/a)</td><td>309.30 (n/a)</td><td>263.50 (n/a)</td><td>89.04 (n/a)</td><td>1018.65 (n/a)</td><td>795.18 (n/a)</td><td>867.89 (n/a)</td><td>581.77 (n/a)</td><td>189.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.15 <b>(+60.63%)</b></td><td>4.56 <b>(+32.48%)</b></td><td>4.12 <b>(+28.04%)</b></td><td>3.16 (+1.13%)</td><td>1.66 <b>(+192.69%)</b></td><td>435.50 (-1.11%)</td><td>331.08 (-18.62%)</td><td>333.80 <b>(-21.90%)</b></td><td>192.60 <b>(-37.73%)</b></td><td>104.23 <b>(+88.12%)</b></td><td>1393.85 <b>(+60.63%)</b></td><td>890.03 <b>(+32.48%)</b></td><td>804.24 <b>(+28.04%)</b></td><td>616.33 (+1.13%)</td><td>323.32 <b>(+192.69%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>4.45 (n/a)</td><td>3.44 (n/a)</td><td>3.22 (n/a)</td><td>3.12 (n/a)</td><td>0.57 (n/a)</td><td>440.40 (n/a)</td><td>406.82 (n/a)</td><td>427.40 (n/a)</td><td>309.30 (n/a)</td><td>55.41 (n/a)</td><td>867.75 (n/a)</td><td>671.85 (n/a)</td><td>628.12 (n/a)</td><td>609.47 (n/a)</td><td>110.46 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.90 (-6.32%)</td><td>1.64 (+2.49%)</td><td>1.62 (+3.04%)</td><td>1.30 (+6.36%)</td><td>0.24 (-16.55%)</td><td>308.40 (-5.98%)</td><td>248.92 (-3.16%)</td><td>247.30 (-2.94%)</td><td>211.50 (+6.76%)</td><td>38.62 (-17.01%)</td><td>158.67 (-6.32%)</td><td>137.27 (+2.49%)</td><td>135.68 (+3.04%)</td><td>108.81 (+6.36%)</td><td>19.97 (-16.55%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>2.03 (n/a)</td><td>1.60 (n/a)</td><td>1.58 (n/a)</td><td>1.22 (n/a)</td><td>0.29 (n/a)</td><td>328.00 (n/a)</td><td>257.04 (n/a)</td><td>254.80 (n/a)</td><td>198.10 (n/a)</td><td>46.53 (n/a)</td><td>169.38 (n/a)</td><td>133.94 (n/a)</td><td>131.68 (n/a)</td><td>102.31 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.25 (-13.93%)</td><td>5.54 (-8.26%)</td><td>5.50 (-0.44%)</td><td>4.93 (-4.99%)</td><td>0.56 <b>(-44.27%)</b></td><td>392.40 (+5.26%)</td><td>351.94 (+7.59%)</td><td>351.80 (+0.46%)</td><td>309.50 (+16.18%)</td><td>35.19 <b>(-31.64%)</b></td><td>1301.07 (-13.93%)</td><td>1153.39 (-8.26%)</td><td>1144.62 (-0.44%)</td><td>1026.19 (-4.99%)</td><td>116.30 <b>(-44.27%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.26 (n/a)</td><td>6.04 (n/a)</td><td>5.52 (n/a)</td><td>5.19 (n/a)</td><td>1.00 (n/a)</td><td>372.80 (n/a)</td><td>327.10 (n/a)</td><td>350.20 (n/a)</td><td>266.40 (n/a)</td><td>51.48 (n/a)</td><td>1511.59 (n/a)</td><td>1257.17 (n/a)</td><td>1149.63 (n/a)</td><td>1080.11 (n/a)</td><td>208.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>17.56 (+10.46%)</td><td>14.97 (+13.95%)</td><td>16.81 <b>(+32.74%)</b></td><td>11.53 (+1.27%)</td><td>3.12 <b>(+70.56%)</b></td><td>477.50 (-1.26%)</td><td>382.14 (-10.15%)</td><td>327.40 <b>(-24.68%)</b></td><td>313.60 (-9.47%)</td><td>86.02 <b>(+54.28%)</b></td><td>6848.59 (+10.46%)</td><td>5838.67 (+13.95%)</td><td>6558.34 <b>(+32.74%)</b></td><td>4496.90 (+1.27%)</td><td>1218.13 <b>(+70.56%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>15.89 (n/a)</td><td>13.13 (n/a)</td><td>12.67 (n/a)</td><td>11.38 (n/a)</td><td>1.83 (n/a)</td><td>483.60 (n/a)</td><td>425.32 (n/a)</td><td>434.70 (n/a)</td><td>346.40 (n/a)</td><td>55.75 (n/a)</td><td>6199.81 (n/a)</td><td>5123.82 (n/a)</td><td>4940.64 (n/a)</td><td>4440.53 (n/a)</td><td>714.19 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>10.91 (+0.71%)</td><td>8.93 (+0.39%)</td><td>8.05 (-6.83%)</td><td>7.46 (-6.53%)</td><td>1.75 <b>(+53.05%)</b></td><td>737.80 (+6.97%)</td><td>635.00 (+1.38%)</td><td>684.20 (+7.33%)</td><td>504.60 (-0.71%)</td><td>117.79 <b>(+63.18%)</b></td><td>4255.39 (+0.71%)</td><td>3483.19 (+0.39%)</td><td>3138.81 (-6.83%)</td><td>2910.49 (-6.53%)</td><td>684.30 <b>(+53.05%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>10.83 (n/a)</td><td>8.89 (n/a)</td><td>8.64 (n/a)</td><td>7.98 (n/a)</td><td>1.15 (n/a)</td><td>689.70 (n/a)</td><td>626.36 (n/a)</td><td>637.50 (n/a)</td><td>508.20 (n/a)</td><td>72.18 (n/a)</td><td>4225.36 (n/a)</td><td>3469.65 (n/a)</td><td>3368.85 (n/a)</td><td>3113.77 (n/a)</td><td>447.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.33 (-17.37%)</td><td>9.82 (-4.82%)</td><td>9.42 (-0.96%)</td><td>8.79 (+0.58%)</td><td>1.44 <b>(-44.64%)</b></td><td>659.70 (-0.57%)</td><td>599.64 (+2.49%)</td><td>615.40 (+0.97%)</td><td>470.30 <b>(+21.02%)</b></td><td>75.73 <b>(-33.10%)</b></td><td>5136.81 (-17.37%)</td><td>4089.50 (-4.82%)</td><td>3925.57 (-0.96%)</td><td>3662.07 (+0.58%)</td><td>601.15 <b>(-44.64%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.92 (n/a)</td><td>10.31 (n/a)</td><td>9.52 (n/a)</td><td>8.74 (n/a)</td><td>2.61 (n/a)</td><td>663.50 (n/a)</td><td>585.06 (n/a)</td><td>609.50 (n/a)</td><td>388.60 (n/a)</td><td>113.20 (n/a)</td><td>6216.52 (n/a)</td><td>4296.49 (n/a)</td><td>3963.58 (n/a)</td><td>3641.05 (n/a)</td><td>1085.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.90 (n/a)</td><td>180.36 (n/a)</td><td>175.60 (n/a)</td><td>126.20 (n/a)</td><td>37.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.50 (n/a)</td><td>176.36 (n/a)</td><td>161.70 (n/a)</td><td>142.70 (n/a)</td><td>33.98 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.40 (n/a)</td><td>175.20 (n/a)</td><td>182.30 (n/a)</td><td>118.30 (n/a)</td><td>48.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.40 (n/a)</td><td>180.00 (n/a)</td><td>167.70 (n/a)</td><td>148.30 (n/a)</td><td>34.47 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>371.10 (n/a)</td><td>222.84 (n/a)</td><td>214.10 (n/a)</td><td>125.00 (n/a)</td><td>94.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>257.10 (n/a)</td><td>212.98 (n/a)</td><td>222.90 (n/a)</td><td>154.30 (n/a)</td><td>42.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.80 (n/a)</td><td>199.00 (n/a)</td><td>185.30 (n/a)</td><td>150.50 (n/a)</td><td>48.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>354.00 (n/a)</td><td>269.88 (n/a)</td><td>253.30 (n/a)</td><td>207.80 (n/a)</td><td>61.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>194.90 (n/a)</td><td>194.10 (n/a)</td><td>163.90 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>178.50 (n/a)</td><td>174.90 (n/a)</td><td>145.50 (n/a)</td><td>25.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.90 (n/a)</td><td>172.26 (n/a)</td><td>183.70 (n/a)</td><td>143.80 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.70 (n/a)</td><td>181.94 (n/a)</td><td>173.00 (n/a)</td><td>146.60 (n/a)</td><td>36.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>160.74 (n/a)</td><td>175.10 (n/a)</td><td>112.00 (n/a)</td><td>40.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>183.96 (n/a)</td><td>190.10 (n/a)</td><td>153.40 (n/a)</td><td>20.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.20 (n/a)</td><td>195.80 (n/a)</td><td>197.50 (n/a)</td><td>123.00 (n/a)</td><td>48.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>229.90 (n/a)</td><td>201.88 (n/a)</td><td>206.20 (n/a)</td><td>176.10 (n/a)</td><td>23.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>205.30 (n/a)</td><td>168.14 (n/a)</td><td>190.90 (n/a)</td><td>116.30 (n/a)</td><td>42.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.10 (n/a)</td><td>160.00 (n/a)</td><td>166.50 (n/a)</td><td>122.90 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.20 (n/a)</td><td>167.30 (n/a)</td><td>172.00 (n/a)</td><td>142.20 (n/a)</td><td>15.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.00 (n/a)</td><td>156.92 (n/a)</td><td>147.40 (n/a)</td><td>120.60 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.10 (n/a)</td><td>156.32 (n/a)</td><td>170.20 (n/a)</td><td>126.10 (n/a)</td><td>28.19 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.50 (n/a)</td><td>153.80 (n/a)</td><td>159.20 (n/a)</td><td>118.40 (n/a)</td><td>28.05 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>163.32 (n/a)</td><td>154.60 (n/a)</td><td>144.40 (n/a)</td><td>24.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>279.50 (n/a)</td><td>228.58 (n/a)</td><td>218.30 (n/a)</td><td>194.60 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>232.80 (n/a)</td><td>179.86 (n/a)</td><td>181.60 (n/a)</td><td>127.10 (n/a)</td><td>38.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.10 (n/a)</td><td>180.10 (n/a)</td><td>183.40 (n/a)</td><td>136.80 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.20 (n/a)</td><td>174.40 (n/a)</td><td>181.70 (n/a)</td><td>131.20 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>198.30 (n/a)</td><td>177.40 (n/a)</td><td>187.50 (n/a)</td><td>150.90 (n/a)</td><td>22.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.70 (n/a)</td><td>172.72 (n/a)</td><td>178.70 (n/a)</td><td>127.90 (n/a)</td><td>31.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>225.70 (n/a)</td><td>193.24 (n/a)</td><td>184.70 (n/a)</td><td>176.70 (n/a)</td><td>20.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>293.40 (n/a)</td><td>210.46 (n/a)</td><td>194.70 (n/a)</td><td>129.90 (n/a)</td><td>69.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>255.10 (n/a)</td><td>228.68 (n/a)</td><td>231.20 (n/a)</td><td>184.80 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>4.12 (-1.75%)</td><td>4.09 (-0.46%)</td><td>4.08 (-0.53%)</td><td>4.07 (+0.10%)</td><td>0.02 <b>(-52.79%)</b></td><td>19306.30 (-0.10%)</td><td>19213.72 (+0.46%)</td><td>19256.30 (+0.53%)</td><td>19096.20 (+1.78%)</td><td>105.49 <b>(-51.93%)</b></td><td>2811.40 (-1.75%)</td><td>2794.27 (-0.46%)</td><td>2788.03 (-0.53%)</td><td>2780.80 (+0.10%)</td><td>15.37 <b>(-52.79%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>4.19 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>4.07 (n/a)</td><td>0.05 (n/a)</td><td>19325.90 (n/a)</td><td>19126.68 (n/a)</td><td>19154.10 (n/a)</td><td>18762.20 (n/a)</td><td>219.46 (n/a)</td><td>2861.45 (n/a)</td><td>2807.22 (n/a)</td><td>2802.90 (n/a)</td><td>2777.99 (n/a)</td><td>32.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>4.21 (-14.99%)</td><td>4.09 (-5.34%)</td><td>4.08 (-2.80%)</td><td>4.00 (-1.55%)</td><td>0.08 <b>(-78.02%)</b></td><td>2353.60 (+1.58%)</td><td>2302.00 (+5.12%)</td><td>2307.00 (+2.88%)</td><td>2233.00 (+17.63%)</td><td>44.69 <b>(-73.46%)</b></td><td>1656.65 (-14.99%)</td><td>1607.52 (-5.34%)</td><td>1603.54 (-2.80%)</td><td>1571.79 (-1.55%)</td><td>31.52 <b>(-78.02%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>4.95 (n/a)</td><td>4.32 (n/a)</td><td>4.19 (n/a)</td><td>4.06 (n/a)</td><td>0.36 (n/a)</td><td>2317.00 (n/a)</td><td>2189.86 (n/a)</td><td>2242.40 (n/a)</td><td>1898.40 (n/a)</td><td>168.37 (n/a)</td><td>1948.69 (n/a)</td><td>1698.13 (n/a)</td><td>1649.77 (n/a)</td><td>1596.60 (n/a)</td><td>143.40 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.03 <b>(-21.32%)</b></td><td>0.93 (-12.38%)</td><td>0.98 (-2.17%)</td><td>0.70 <b>(-22.83%)</b></td><td>0.13 <b>(-22.85%)</b></td><td>315.90 <b>(+29.63%)</b></td><td>242.68 (+14.15%)</td><td>225.00 (+2.23%)</td><td>214.10 <b>(+27.14%)</b></td><td>41.51 <b>(+30.00%)</b></td><td>44.08 <b>(-21.32%)</b></td><td>39.66 (-12.38%)</td><td>41.94 (-2.17%)</td><td>29.88 <b>(-22.83%)</b></td><td>5.62 <b>(-22.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.31 (n/a)</td><td>1.06 (n/a)</td><td>1.00 (n/a)</td><td>0.91 (n/a)</td><td>0.17 (n/a)</td><td>243.70 (n/a)</td><td>212.60 (n/a)</td><td>220.10 (n/a)</td><td>168.40 (n/a)</td><td>31.93 (n/a)</td><td>56.03 (n/a)</td><td>45.26 (n/a)</td><td>42.87 (n/a)</td><td>38.72 (n/a)</td><td>7.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.16 (-11.90%)</td><td>0.97 (-0.46%)</td><td>0.96 (-0.45%)</td><td>0.69 (+0.24%)</td><td>0.20 (-12.11%)</td><td>320.00 (-0.25%)</td><td>236.16 (-0.08%)</td><td>231.60 (+0.48%)</td><td>190.10 (+13.49%)</td><td>53.20 (-2.70%)</td><td>49.63 (-11.90%)</td><td>41.46 (-0.46%)</td><td>40.75 (-0.45%)</td><td>29.49 (+0.24%)</td><td>8.42 (-12.11%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.32 (n/a)</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.69 (n/a)</td><td>0.22 (n/a)</td><td>320.80 (n/a)</td><td>236.34 (n/a)</td><td>230.50 (n/a)</td><td>167.50 (n/a)</td><td>54.67 (n/a)</td><td>56.34 (n/a)</td><td>41.65 (n/a)</td><td>40.94 (n/a)</td><td>29.42 (n/a)</td><td>9.58 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.53 (+0.08%)</td><td>0.53 (+0.05%)</td><td>0.53 (+0.09%)</td><td>0.53 (+0.01%)</td><td>0.00 <b>(+30.77%)</b></td><td>47830.40 (-0.01%)</td><td>47790.88 (-0.05%)</td><td>47786.20 (-0.09%)</td><td>47738.60 (-0.08%)</td><td>34.74 <b>(+30.78%)</b></td><td>359.87 (+0.08%)</td><td>359.48 (+0.05%)</td><td>359.51 (+0.09%)</td><td>359.18 (+0.01%)</td><td>0.26 <b>(+30.78%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47837.50 (n/a)</td><td>47813.92 (n/a)</td><td>47828.80 (n/a)</td><td>47776.40 (n/a)</td><td>26.57 (n/a)</td><td>359.59 (n/a)</td><td>359.31 (n/a)</td><td>359.19 (n/a)</td><td>359.13 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.21 (-0.82%)</td><td>0.21 (-0.81%)</td><td>0.21 (-1.04%)</td><td>0.21 (-0.64%)</td><td>0.00 <b>(-30.14%)</b></td><td>120393.30 (+0.65%)</td><td>119876.60 (+0.82%)</td><td>119996.10 (+1.05%)</td><td>119169.30 (+0.83%)</td><td>462.11 <b>(-29.20%)</b></td><td>144.16 (-0.82%)</td><td>143.31 (-0.81%)</td><td>143.17 (-1.04%)</td><td>142.70 (-0.64%)</td><td>0.55 <b>(-30.15%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119618.90 (n/a)</td><td>118904.72 (n/a)</td><td>118747.70 (n/a)</td><td>118192.10 (n/a)</td><td>652.66 (n/a)</td><td>145.36 (n/a)</td><td>144.49 (n/a)</td><td>144.68 (n/a)</td><td>143.62 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.91 (+0.79%)</td><td>0.91 (+0.20%)</td><td>0.90 (-0.02%)</td><td>0.90 (+0.26%)</td><td>0.00 <b>(+76.50%)</b></td><td>27919.60 (-0.26%)</td><td>27801.88 (-0.20%)</td><td>27858.00 (+0.02%)</td><td>27559.30 (-0.79%)</td><td>143.29 <b>(+74.47%)</b></td><td>623.38 (+0.79%)</td><td>617.95 (+0.20%)</td><td>616.70 (-0.02%)</td><td>615.33 (+0.26%)</td><td>3.20 <b>(+76.50%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>27992.80 (n/a)</td><td>27857.14 (n/a)</td><td>27852.40 (n/a)</td><td>27777.50 (n/a)</td><td>82.13 (n/a)</td><td>618.48 (n/a)</td><td>616.72 (n/a)</td><td>616.82 (n/a)</td><td>613.72 (n/a)</td><td>1.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.68 (+0.80%)</td><td>3.54 (-1.59%)</td><td>3.58 (-1.05%)</td><td>3.38 (-1.92%)</td><td>0.13 <b>(+56.33%)</b></td><td>7454.30 (+1.96%)</td><td>7126.86 (+1.68%)</td><td>7021.00 (+1.06%)</td><td>6843.50 (-0.79%)</td><td>269.12 <b>(+58.06%)</b></td><td>2510.39 (+0.80%)</td><td>2413.31 (-1.59%)</td><td>2446.93 (-1.05%)</td><td>2304.70 (-1.92%)</td><td>90.31 <b>(+56.33%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>3.65 (n/a)</td><td>3.59 (n/a)</td><td>3.62 (n/a)</td><td>3.44 (n/a)</td><td>0.08 (n/a)</td><td>7311.10 (n/a)</td><td>7008.92 (n/a)</td><td>6947.60 (n/a)</td><td>6898.30 (n/a)</td><td>170.27 (n/a)</td><td>2490.44 (n/a)</td><td>2452.27 (n/a)</td><td>2472.79 (n/a)</td><td>2349.84 (n/a)</td><td>57.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>2.93 (-1.38%)</td><td>2.87 (-1.25%)</td><td>2.86 (-2.34%)</td><td>2.79 (-0.43%)</td><td>0.06 (-11.95%)</td><td>9020.00 (+0.43%)</td><td>8769.70 (+1.25%)</td><td>8802.10 (+2.40%)</td><td>8594.70 (+1.39%)</td><td>176.56 (-10.83%)</td><td>1998.88 (-1.38%)</td><td>1959.63 (-1.25%)</td><td>1951.78 (-2.34%)</td><td>1904.63 (-0.43%)</td><td>39.25 (-11.95%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>2.97 (n/a)</td><td>2.91 (n/a)</td><td>2.93 (n/a)</td><td>2.80 (n/a)</td><td>0.07 (n/a)</td><td>8981.20 (n/a)</td><td>8661.22 (n/a)</td><td>8596.00 (n/a)</td><td>8476.50 (n/a)</td><td>198.01 (n/a)</td><td>2026.77 (n/a)</td><td>1984.36 (n/a)</td><td>1998.60 (n/a)</td><td>1912.88 (n/a)</td><td>44.57 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.34 (-2.07%)</td><td>3.25 (+0.95%)</td><td>3.27 (+2.88%)</td><td>3.13 (-0.24%)</td><td>0.09 (-18.28%)</td><td>8036.40 (+0.24%)</td><td>7746.42 (-0.97%)</td><td>7689.00 (-2.80%)</td><td>7543.70 (+2.11%)</td><td>211.34 (-16.02%)</td><td>2277.39 (-2.07%)</td><td>2219.09 (+0.95%)</td><td>2234.34 (+2.88%)</td><td>2137.74 (-0.24%)</td><td>59.98 (-18.28%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>3.41 (n/a)</td><td>3.22 (n/a)</td><td>3.18 (n/a)</td><td>3.14 (n/a)</td><td>0.11 (n/a)</td><td>8017.50 (n/a)</td><td>7822.18 (n/a)</td><td>7910.40 (n/a)</td><td>7387.60 (n/a)</td><td>251.66 (n/a)</td><td>2325.49 (n/a)</td><td>2198.19 (n/a)</td><td>2171.82 (n/a)</td><td>2142.81 (n/a)</td><td>73.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.80 (-0.27%)</td><td>0.80 (-0.06%)</td><td>0.80 (+0.00%)</td><td>0.80 (+0.02%)</td><td>0.00 <b>(-68.90%)</b></td><td>94874.20 (-0.02%)</td><td>94802.46 (+0.06%)</td><td>94775.10 (-0.00%)</td><td>94773.40 (+0.27%)</td><td>43.71 <b>(-68.80%)</b></td><td>725.09 (-0.27%)</td><td>724.87 (-0.06%)</td><td>725.08 (+0.00%)</td><td>724.32 (+0.02%)</td><td>0.33 <b>(-68.89%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94896.90 (n/a)</td><td>94745.20 (n/a)</td><td>94778.70 (n/a)</td><td>94516.20 (n/a)</td><td>140.07 (n/a)</td><td>727.07 (n/a)</td><td>725.31 (n/a)</td><td>725.05 (n/a)</td><td>724.15 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.73 (-0.01%)</td><td>0.73 (-0.04%)</td><td>0.73 (+0.00%)</td><td>0.73 (-0.24%)</td><td>0.00 <b>(+402.88%)</b></td><td>103579.00 (+0.24%)</td><td>103351.08 (+0.04%)</td><td>103308.50 (-0.00%)</td><td>103276.20 (+0.01%)</td><td>128.55 <b>(+404.68%)</b></td><td>665.40 (-0.01%)</td><td>664.91 (-0.04%)</td><td>665.19 (+0.00%)</td><td>663.45 (-0.24%)</td><td>0.83 <b>(+402.87%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103332.90 (n/a)</td><td>103307.96 (n/a)</td><td>103309.80 (n/a)</td><td>103267.60 (n/a)</td><td>25.47 (n/a)</td><td>665.45 (n/a)</td><td>665.19 (n/a)</td><td>665.18 (n/a)</td><td>665.03 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.69 (-0.03%)</td><td>0.68 (-0.17%)</td><td>0.68 (-0.22%)</td><td>0.68 (-0.23%)</td><td>0.00 <b>(+41.68%)</b></td><td>110865.80 (+0.23%)</td><td>110530.80 (+0.17%)</td><td>110579.00 (+0.22%)</td><td>110185.40 (+0.03%)</td><td>284.65 <b>(+42.08%)</b></td><td>623.67 (-0.03%)</td><td>621.73 (-0.17%)</td><td>621.45 (-0.22%)</td><td>619.84 (-0.23%)</td><td>1.60 <b>(+41.69%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110611.60 (n/a)</td><td>110341.70 (n/a)</td><td>110340.70 (n/a)</td><td>110148.70 (n/a)</td><td>200.35 (n/a)</td><td>623.88 (n/a)</td><td>622.79 (n/a)</td><td>622.79 (n/a)</td><td>621.27 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>2.82 (+0.68%)</td><td>2.80 (+0.17%)</td><td>2.80 (+0.04%)</td><td>2.79 (+0.08%)</td><td>0.01 <b>(+116.09%)</b></td><td>37602.70 (-0.08%)</td><td>37456.68 (-0.17%)</td><td>37479.70 (-0.04%)</td><td>37233.50 (-0.67%)</td><td>136.24 <b>(+114.29%)</b></td><td>2883.80 (+0.68%)</td><td>2866.65 (+0.17%)</td><td>2864.86 (+0.04%)</td><td>2855.49 (+0.08%)</td><td>10.46 <b>(+116.10%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>0.00 (n/a)</td><td>37633.70 (n/a)</td><td>37520.36 (n/a)</td><td>37492.90 (n/a)</td><td>37485.90 (n/a)</td><td>63.58 (n/a)</td><td>2864.39 (n/a)</td><td>2861.76 (n/a)</td><td>2863.86 (n/a)</td><td>2853.14 (n/a)</td><td>4.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.67 (+0.43%)</td><td>7.42 (+1.78%)</td><td>7.41 (-0.90%)</td><td>7.04 (+4.75%)</td><td>0.24 <b>(-35.72%)</b></td><td>1265.40 (-4.53%)</td><td>1201.98 (-1.87%)</td><td>1202.70 (+0.91%)</td><td>1161.60 (-0.43%)</td><td>39.97 <b>(-38.79%)</b></td><td>462.17 (+0.43%)</td><td>447.05 (+1.78%)</td><td>446.40 (-0.90%)</td><td>424.28 (+4.75%)</td><td>14.56 <b>(-35.72%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.64 (n/a)</td><td>7.29 (n/a)</td><td>7.48 (n/a)</td><td>6.72 (n/a)</td><td>0.38 (n/a)</td><td>1325.50 (n/a)</td><td>1224.92 (n/a)</td><td>1191.80 (n/a)</td><td>1166.60 (n/a)</td><td>65.30 (n/a)</td><td>460.19 (n/a)</td><td>439.25 (n/a)</td><td>450.46 (n/a)</td><td>405.02 (n/a)</td><td>22.64 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.05 (-1.41%)</td><td>6.49 (-2.32%)</td><td>6.61 (-1.24%)</td><td>5.49 (-6.30%)</td><td>0.62 <b>(+30.37%)</b></td><td>1622.00 (+6.72%)</td><td>1384.66 (+2.74%)</td><td>1347.70 (+1.26%)</td><td>1264.70 (+1.44%)</td><td>143.29 <b>(+39.81%)</b></td><td>424.52 (-1.41%)</td><td>390.81 (-2.32%)</td><td>398.36 (-1.24%)</td><td>330.99 (-6.30%)</td><td>37.24 <b>(+30.37%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.15 (n/a)</td><td>6.64 (n/a)</td><td>6.70 (n/a)</td><td>5.86 (n/a)</td><td>0.47 (n/a)</td><td>1519.80 (n/a)</td><td>1347.76 (n/a)</td><td>1330.90 (n/a)</td><td>1246.80 (n/a)</td><td>102.49 (n/a)</td><td>430.61 (n/a)</td><td>400.08 (n/a)</td><td>403.38 (n/a)</td><td>353.26 (n/a)</td><td>28.56 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.22 (+4.52%)</td><td>6.45 (+5.38%)</td><td>6.82 (+3.45%)</td><td>4.80 (+2.29%)</td><td>1.00 (+10.31%)</td><td>1857.70 (-2.24%)</td><td>1413.48 (-4.84%)</td><td>1307.30 (-3.33%)</td><td>1234.50 (-4.32%)</td><td>259.89 (+3.27%)</td><td>434.87 (+4.52%)</td><td>388.66 (+5.38%)</td><td>410.68 (+3.45%)</td><td>289.00 (+2.29%)</td><td>60.41 (+10.31%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>6.91 (n/a)</td><td>6.12 (n/a)</td><td>6.59 (n/a)</td><td>4.69 (n/a)</td><td>0.91 (n/a)</td><td>1900.20 (n/a)</td><td>1485.38 (n/a)</td><td>1352.40 (n/a)</td><td>1290.30 (n/a)</td><td>251.66 (n/a)</td><td>416.08 (n/a)</td><td>368.83 (n/a)</td><td>396.96 (n/a)</td><td>282.54 (n/a)</td><td>54.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>8.07 (-5.84%)</td><td>7.76 (-5.52%)</td><td>7.92 (-1.91%)</td><td>7.41 (-5.33%)</td><td>0.32 (-0.17%)</td><td>4705.50 (+5.64%)</td><td>4501.74 (+5.86%)</td><td>4403.90 (+1.95%)</td><td>4322.10 (+6.20%)</td><td>186.91 (+13.58%)</td><td>496.87 (-5.84%)</td><td>477.69 (-5.52%)</td><td>487.63 (-1.91%)</td><td>456.38 (-5.33%)</td><td>19.60 (-0.17%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.57 (n/a)</td><td>8.21 (n/a)</td><td>8.07 (n/a)</td><td>7.83 (n/a)</td><td>0.32 (n/a)</td><td>4454.40 (n/a)</td><td>4252.72 (n/a)</td><td>4319.60 (n/a)</td><td>4069.70 (n/a)</td><td>164.56 (n/a)</td><td>527.68 (n/a)</td><td>505.57 (n/a)</td><td>497.15 (n/a)</td><td>482.10 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.94 (-0.46%)</td><td>7.65 (+1.54%)</td><td>7.63 (+0.66%)</td><td>7.46 (+6.10%)</td><td>0.18 <b>(-48.14%)</b></td><td>4670.90 (-5.75%)</td><td>4560.46 (-1.65%)</td><td>4569.40 (-0.66%)</td><td>4392.10 (+0.46%)</td><td>107.14 <b>(-51.15%)</b></td><td>488.95 (-0.46%)</td><td>471.10 (+1.54%)</td><td>469.97 (+0.66%)</td><td>459.76 (+6.10%)</td><td>11.24 <b>(-48.14%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.97 (n/a)</td><td>7.53 (n/a)</td><td>7.58 (n/a)</td><td>7.03 (n/a)</td><td>0.35 (n/a)</td><td>4956.00 (n/a)</td><td>4636.78 (n/a)</td><td>4599.70 (n/a)</td><td>4371.90 (n/a)</td><td>219.33 (n/a)</td><td>491.20 (n/a)</td><td>463.96 (n/a)</td><td>466.87 (n/a)</td><td>433.31 (n/a)</td><td>21.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.55 (-4.21%)</td><td>7.31 (-0.98%)</td><td>7.35 (-0.08%)</td><td>6.95 (+1.21%)</td><td>0.24 <b>(-33.18%)</b></td><td>5019.20 (-1.20%)</td><td>4776.52 (+0.89%)</td><td>4745.90 (+0.08%)</td><td>4619.70 (+4.40%)</td><td>160.98 <b>(-31.23%)</b></td><td>464.85 (-4.21%)</td><td>449.99 (-0.98%)</td><td>452.49 (-0.08%)</td><td>427.86 (+1.21%)</td><td>14.91 <b>(-33.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.88 (n/a)</td><td>7.38 (n/a)</td><td>7.35 (n/a)</td><td>6.86 (n/a)</td><td>0.36 (n/a)</td><td>5080.10 (n/a)</td><td>4734.52 (n/a)</td><td>4742.20 (n/a)</td><td>4425.00 (n/a)</td><td>234.09 (n/a)</td><td>485.30 (n/a)</td><td>454.46 (n/a)</td><td>452.84 (n/a)</td><td>422.72 (n/a)</td><td>22.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.80 (+0.00%)</td><td>0.80 (-0.08%)</td><td>0.80 (-0.03%)</td><td>0.80 (-0.19%)</td><td>0.00 <b>(+411.50%)</b></td><td>94259.90 (+0.19%)</td><td>94125.56 (+0.08%)</td><td>94083.80 (+0.03%)</td><td>94030.90 (-0.00%)</td><td>98.71 <b>(+412.55%)</b></td><td>730.82 (+0.00%)</td><td>730.08 (-0.08%)</td><td>730.41 (-0.03%)</td><td>729.04 (-0.19%)</td><td>0.77 <b>(+411.52%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94079.30 (n/a)</td><td>94053.26 (n/a)</td><td>94055.50 (n/a)</td><td>94034.20 (n/a)</td><td>19.26 (n/a)</td><td>730.79 (n/a)</td><td>730.64 (n/a)</td><td>730.63 (n/a)</td><td>730.44 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.74 (+0.02%)</td><td>0.74 (+0.01%)</td><td>0.74 (+0.01%)</td><td>0.74 (-0.01%)</td><td>0.00 <b>(+55.29%)</b></td><td>102617.60 (+0.01%)</td><td>102589.52 (-0.01%)</td><td>102583.70 (-0.01%)</td><td>102567.30 (-0.02%)</td><td>20.34 <b>(+55.68%)</b></td><td>669.99 (+0.02%)</td><td>669.85 (+0.01%)</td><td>669.89 (+0.01%)</td><td>669.67 (-0.01%)</td><td>0.13 <b>(+55.26%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102611.80 (n/a)</td><td>102597.08 (n/a)</td><td>102589.90 (n/a)</td><td>102586.40 (n/a)</td><td>13.06 (n/a)</td><td>669.87 (n/a)</td><td>669.80 (n/a)</td><td>669.85 (n/a)</td><td>669.70 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.71 (-0.13%)</td><td>0.71 (+0.01%)</td><td>0.71 (+0.02%)</td><td>0.71 (+0.15%)</td><td>0.00 <b>(-66.79%)</b></td><td>105954.00 (-0.15%)</td><td>105893.64 (-0.01%)</td><td>105889.10 (-0.02%)</td><td>105811.50 (+0.13%)</td><td>53.62 <b>(-66.80%)</b></td><td>649.45 (-0.13%)</td><td>648.95 (+0.01%)</td><td>648.98 (+0.02%)</td><td>648.58 (+0.15%)</td><td>0.33 <b>(-66.79%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106114.00 (n/a)</td><td>105904.26 (n/a)</td><td>105912.40 (n/a)</td><td>105672.40 (n/a)</td><td>161.52 (n/a)</td><td>650.31 (n/a)</td><td>648.88 (n/a)</td><td>648.83 (n/a)</td><td>647.60 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.99 (-7.94%)</td><td>3.37 (-0.69%)</td><td>3.19 (+0.97%)</td><td>3.04 (+10.87%)</td><td>0.41 <b>(-34.57%)</b></td><td>2651.00 (-9.80%)</td><td>2419.54 (-0.71%)</td><td>2527.20 (-0.96%)</td><td>2017.90 (+8.63%)</td><td>270.62 <b>(-34.53%)</b></td><td>1047.59 (-7.94%)</td><td>883.18 (-0.69%)</td><td>836.46 (+0.97%)</td><td>797.41 (+10.87%)</td><td>106.25 <b>(-34.57%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>4.34 (n/a)</td><td>3.39 (n/a)</td><td>3.16 (n/a)</td><td>2.74 (n/a)</td><td>0.62 (n/a)</td><td>2939.00 (n/a)</td><td>2436.88 (n/a)</td><td>2551.80 (n/a)</td><td>1857.60 (n/a)</td><td>413.38 (n/a)</td><td>1138.00 (n/a)</td><td>889.30 (n/a)</td><td>828.42 (n/a)</td><td>719.26 (n/a)</td><td>162.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.36 <b>(-38.81%)</b></td><td>0.33 <b>(-22.04%)</b></td><td>0.33 (-9.80%)</td><td>0.32 (-3.68%)</td><td>0.01 <b>(-86.52%)</b></td><td>3876.40 (+3.81%)</td><td>3766.56 <b>(+22.52%)</b></td><td>3820.90 (+10.86%)</td><td>3493.10 <b>(+63.44%)</b></td><td>158.32 <b>(-77.37%)</b></td><td>19.21 <b>(-38.81%)</b></td><td>17.84 <b>(-22.04%)</b></td><td>17.56 (-9.80%)</td><td>17.31 (-3.68%)</td><td>0.79 <b>(-86.52%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.58 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.11 (n/a)</td><td>3734.00 (n/a)</td><td>3074.28 (n/a)</td><td>3446.60 (n/a)</td><td>2137.20 (n/a)</td><td>699.69 (n/a)</td><td>31.40 (n/a)</td><td>22.89 (n/a)</td><td>19.47 (n/a)</td><td>17.97 (n/a)</td><td>5.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.29 (+4.24%)</td><td>4.86 (+5.36%)</td><td>4.84 (-0.06%)</td><td>3.45 (-5.31%)</td><td>1.01 (+2.17%)</td><td>1927.00 (+5.61%)</td><td>1418.40 (-4.99%)</td><td>1374.10 (+0.05%)</td><td>1057.50 (-4.06%)</td><td>315.86 (+1.99%)</td><td>1943.45 (+4.24%)</td><td>1503.10 (+5.36%)</td><td>1495.65 (-0.06%)</td><td>1066.54 (-5.31%)</td><td>311.45 (+2.17%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>6.03 (n/a)</td><td>4.62 (n/a)</td><td>4.84 (n/a)</td><td>3.65 (n/a)</td><td>0.99 (n/a)</td><td>1824.60 (n/a)</td><td>1492.92 (n/a)</td><td>1373.40 (n/a)</td><td>1102.30 (n/a)</td><td>309.71 (n/a)</td><td>1864.42 (n/a)</td><td>1426.66 (n/a)</td><td>1496.47 (n/a)</td><td>1126.37 (n/a)</td><td>304.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.33 (n/a)</td><td>12.48 (n/a)</td><td>12.31 (n/a)</td><td>11.71 (n/a)</td><td>0.66 (n/a)</td><td>13.33 (n/a)</td><td>12.47 (n/a)</td><td>12.31 (n/a)</td><td>11.70 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>25.37 (+4.42%)</td><td>24.23 (+9.11%)</td><td>24.02 (+0.12%)</td><td>23.27 <b>(+48.96%)</b></td><td>0.79 <b>(-78.60%)</b></td><td>25.35 (+4.42%)</td><td>24.21 (+9.11%)</td><td>24.00 (+0.12%)</td><td>23.25 <b>(+48.96%)</b></td><td>0.79 <b>(-78.60%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>24.30 (n/a)</td><td>22.20 (n/a)</td><td>23.99 (n/a)</td><td>15.62 (n/a)</td><td>3.71 (n/a)</td><td>24.28 (n/a)</td><td>22.19 (n/a)</td><td>23.97 (n/a)</td><td>15.61 (n/a)</td><td>3.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>41.50 (+0.81%)</td><td>40.15 (-1.00%)</td><td>39.92 (-1.23%)</td><td>39.46 (-1.36%)</td><td>0.78 <b>(+46.03%)</b></td><td>41.48 (+0.81%)</td><td>40.13 (-1.00%)</td><td>39.89 (-1.23%)</td><td>39.44 (-1.36%)</td><td>0.78 <b>(+46.03%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>41.17 (n/a)</td><td>40.56 (n/a)</td><td>40.42 (n/a)</td><td>40.01 (n/a)</td><td>0.53 (n/a)</td><td>41.15 (n/a)</td><td>40.54 (n/a)</td><td>40.39 (n/a)</td><td>39.98 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>45.28 (+0.32%)</td><td>43.06 (-2.29%)</td><td>42.46 (-3.20%)</td><td>41.72 (-3.41%)</td><td>1.57 <b>(+87.18%)</b></td><td>45.25 (+0.32%)</td><td>43.03 (-2.29%)</td><td>42.43 (-3.20%)</td><td>41.70 (-3.41%)</td><td>1.57 <b>(+87.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>45.14 (n/a)</td><td>44.06 (n/a)</td><td>43.86 (n/a)</td><td>43.19 (n/a)</td><td>0.84 (n/a)</td><td>45.11 (n/a)</td><td>44.04 (n/a)</td><td>43.83 (n/a)</td><td>43.17 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.22 (n/a)</td><td>12.23 (n/a)</td><td>12.30 (n/a)</td><td>11.05 (n/a)</td><td>0.78 (n/a)</td><td>13.21 (n/a)</td><td>12.23 (n/a)</td><td>12.29 (n/a)</td><td>11.04 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>25.18 (+2.02%)</td><td>23.22 (+1.54%)</td><td>24.37 (+0.36%)</td><td>18.60 (+8.56%)</td><td>2.66 (-17.76%)</td><td>25.16 (+2.02%)</td><td>23.21 (+1.54%)</td><td>24.35 (+0.36%)</td><td>18.59 (+8.56%)</td><td>2.66 (-17.76%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>24.68 (n/a)</td><td>22.87 (n/a)</td><td>24.28 (n/a)</td><td>17.13 (n/a)</td><td>3.23 (n/a)</td><td>24.66 (n/a)</td><td>22.86 (n/a)</td><td>24.26 (n/a)</td><td>17.12 (n/a)</td><td>3.23 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>41.50 (-6.47%)</td><td>39.86 (-0.76%)</td><td>39.88 (+1.42%)</td><td>38.44 (+8.58%)</td><td>1.11 <b>(-68.17%)</b></td><td>41.48 (-6.47%)</td><td>39.84 (-0.76%)</td><td>39.85 (+1.42%)</td><td>38.41 (+8.58%)</td><td>1.11 <b>(-68.17%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>44.37 (n/a)</td><td>40.17 (n/a)</td><td>39.32 (n/a)</td><td>35.40 (n/a)</td><td>3.49 (n/a)</td><td>44.34 (n/a)</td><td>40.14 (n/a)</td><td>39.30 (n/a)</td><td>35.38 (n/a)</td><td>3.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>44.86 (-1.59%)</td><td>41.85 (-5.29%)</td><td>42.92 (-3.23%)</td><td>35.01 (-18.28%)</td><td>3.96 <b>(+209.66%)</b></td><td>44.83 (-1.59%)</td><td>41.83 (-5.29%)</td><td>42.89 (-3.23%)</td><td>34.99 (-18.28%)</td><td>3.96 <b>(+209.66%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>45.59 (n/a)</td><td>44.19 (n/a)</td><td>44.35 (n/a)</td><td>42.85 (n/a)</td><td>1.28 (n/a)</td><td>45.56 (n/a)</td><td>44.16 (n/a)</td><td>44.32 (n/a)</td><td>42.82 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.22 (+5.27%)</td><td>8.48 (+2.42%)</td><td>8.58 (+4.51%)</td><td>7.75 (-0.13%)</td><td>0.54 <b>(+32.82%)</b></td><td>9.21 (+5.27%)</td><td>8.46 (+2.42%)</td><td>8.56 (+4.51%)</td><td>7.74 (-0.13%)</td><td>0.54 <b>(+32.82%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.76 (n/a)</td><td>8.28 (n/a)</td><td>8.21 (n/a)</td><td>7.76 (n/a)</td><td>0.41 (n/a)</td><td>8.75 (n/a)</td><td>8.26 (n/a)</td><td>8.19 (n/a)</td><td>7.75 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.91 (+2.60%)</td><td>0.84 (-0.43%)</td><td>0.86 (+1.30%)</td><td>0.75 (-0.43%)</td><td>0.06 (+14.08%)</td><td>0.90 (+2.60%)</td><td>0.82 (-0.43%)</td><td>0.85 (+1.30%)</td><td>0.74 (-0.43%)</td><td>0.06 (+14.08%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.89 (n/a)</td><td>0.84 (n/a)</td><td>0.85 (n/a)</td><td>0.76 (n/a)</td><td>0.06 (n/a)</td><td>0.87 (n/a)</td><td>0.83 (n/a)</td><td>0.84 (n/a)</td><td>0.74 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.10 <b>(-20.98%)</b></td><td>1.06 (-8.23%)</td><td>1.08 (-14.47%)</td><td>0.97 (+16.76%)</td><td>0.05 <b>(-78.12%)</b></td><td>1.08 <b>(-20.98%)</b></td><td>1.05 (-8.23%)</td><td>1.07 (-14.47%)</td><td>0.96 (+16.76%)</td><td>0.05 <b>(-78.12%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.39 (n/a)</td><td>1.16 (n/a)</td><td>1.27 (n/a)</td><td>0.83 (n/a)</td><td>0.23 (n/a)</td><td>1.37 (n/a)</td><td>1.14 (n/a)</td><td>1.25 (n/a)</td><td>0.82 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>17.75 (-3.52%)</td><td>15.98 (-1.62%)</td><td>16.45 (+1.15%)</td><td>13.76 (-3.85%)</td><td>1.60 (-1.57%)</td><td>17.55 (-3.52%)</td><td>15.80 (-1.62%)</td><td>16.26 (+1.15%)</td><td>13.60 (-3.85%)</td><td>1.59 (-1.57%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>18.40 (n/a)</td><td>16.24 (n/a)</td><td>16.26 (n/a)</td><td>14.31 (n/a)</td><td>1.63 (n/a)</td><td>18.19 (n/a)</td><td>16.06 (n/a)</td><td>16.07 (n/a)</td><td>14.14 (n/a)</td><td>1.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.90 (+1.83%)</td><td>13.26 (+2.30%)</td><td>13.28 (+1.09%)</td><td>12.54 (+6.80%)</td><td>0.49 <b>(-32.43%)</b></td><td>13.66 (+1.83%)</td><td>13.03 (+2.30%)</td><td>13.05 (+1.09%)</td><td>12.32 (+6.80%)</td><td>0.48 <b>(-32.43%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.65 (n/a)</td><td>12.96 (n/a)</td><td>13.14 (n/a)</td><td>11.74 (n/a)</td><td>0.73 (n/a)</td><td>13.41 (n/a)</td><td>12.74 (n/a)</td><td>12.91 (n/a)</td><td>11.53 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>8.41 (+6.38%)</td><td>7.58 (+1.68%)</td><td>7.35 (-1.94%)</td><td>7.00 (+1.79%)</td><td>0.54 <b>(+29.76%)</b></td><td>8.26 (+6.38%)</td><td>7.45 (+1.68%)</td><td>7.23 (-1.94%)</td><td>6.88 (+1.79%)</td><td>0.53 <b>(+29.76%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.90 (n/a)</td><td>7.46 (n/a)</td><td>7.50 (n/a)</td><td>6.88 (n/a)</td><td>0.42 (n/a)</td><td>7.77 (n/a)</td><td>7.33 (n/a)</td><td>7.37 (n/a)</td><td>6.76 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.38 (-10.68%)</td><td>5.45 (-5.88%)</td><td>5.51 (+1.89%)</td><td>3.96 <b>(-23.95%)</b></td><td>0.93 (+18.46%)</td><td>6.27 (-10.68%)</td><td>5.37 (-5.88%)</td><td>5.42 (+1.89%)</td><td>3.89 <b>(-23.95%)</b></td><td>0.91 (+18.46%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>7.14 (n/a)</td><td>5.79 (n/a)</td><td>5.41 (n/a)</td><td>5.20 (n/a)</td><td>0.78 (n/a)</td><td>7.02 (n/a)</td><td>5.70 (n/a)</td><td>5.32 (n/a)</td><td>5.12 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.41 (n/a)</td><td>12.79 (n/a)</td><td>12.77 (n/a)</td><td>11.74 (n/a)</td><td>0.66 (n/a)</td><td>13.40 (n/a)</td><td>12.78 (n/a)</td><td>12.76 (n/a)</td><td>11.74 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.26 (n/a)</td><td>12.72 (n/a)</td><td>12.58 (n/a)</td><td>12.37 (n/a)</td><td>0.36 (n/a)</td><td>13.26 (n/a)</td><td>12.72 (n/a)</td><td>12.58 (n/a)</td><td>12.36 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>163.86 (n/a)</td><td>145.30 (n/a)</td><td>126.60 (n/a)</td><td>42.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.50 (n/a)</td><td>185.98 (n/a)</td><td>177.10 (n/a)</td><td>158.70 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>167.38 (n/a)</td><td>177.80 (n/a)</td><td>130.30 (n/a)</td><td>31.94 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>185.38 (n/a)</td><td>218.40 (n/a)</td><td>129.90 (n/a)</td><td>46.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.00 (n/a)</td><td>164.90 (n/a)</td><td>158.90 (n/a)</td><td>135.00 (n/a)</td><td>29.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.40 (n/a)</td><td>178.02 (n/a)</td><td>178.60 (n/a)</td><td>141.80 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>255.30 (n/a)</td><td>194.20 (n/a)</td><td>173.00 (n/a)</td><td>144.40 (n/a)</td><td>47.27 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>343.40 (n/a)</td><td>233.28 (n/a)</td><td>226.30 (n/a)</td><td>181.40 (n/a)</td><td>65.57 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>270.60 (n/a)</td><td>201.10 (n/a)</td><td>181.40 (n/a)</td><td>137.40 (n/a)</td><td>58.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>166.80 (n/a)</td><td>144.56 (n/a)</td><td>155.70 (n/a)</td><td>96.20 (n/a)</td><td>29.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>166.68 (n/a)</td><td>164.20 (n/a)</td><td>140.30 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.80 (n/a)</td><td>177.30 (n/a)</td><td>161.20 (n/a)</td><td>128.90 (n/a)</td><td>40.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>183.38 (n/a)</td><td>190.20 (n/a)</td><td>127.40 (n/a)</td><td>39.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>175.86 (n/a)</td><td>192.90 (n/a)</td><td>126.30 (n/a)</td><td>45.43 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>173.66 (n/a)</td><td>183.40 (n/a)</td><td>121.50 (n/a)</td><td>35.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>199.06 (n/a)</td><td>200.60 (n/a)</td><td>141.50 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>173.80 (n/a)</td><td>155.56 (n/a)</td><td>151.80 (n/a)</td><td>137.40 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>273.70 (n/a)</td><td>218.06 (n/a)</td><td>252.40 (n/a)</td><td>139.00 (n/a)</td><td>64.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>325.00 (n/a)</td><td>197.88 (n/a)</td><td>172.20 (n/a)</td><td>141.60 (n/a)</td><td>74.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.60 (n/a)</td><td>155.32 (n/a)</td><td>154.60 (n/a)</td><td>130.10 (n/a)</td><td>23.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>163.04 (n/a)</td><td>159.90 (n/a)</td><td>153.80 (n/a)</td><td>12.54 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>191.86 (n/a)</td><td>199.20 (n/a)</td><td>162.40 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>229.50 (n/a)</td><td>189.82 (n/a)</td><td>201.60 (n/a)</td><td>133.70 (n/a)</td><td>43.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>330.10 (n/a)</td><td>221.60 (n/a)</td><td>199.00 (n/a)</td><td>183.00 (n/a)</td><td>61.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>379.30 (n/a)</td><td>219.32 (n/a)</td><td>207.80 (n/a)</td><td>133.60 (n/a)</td><td>96.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.50 (n/a)</td><td>165.54 (n/a)</td><td>170.40 (n/a)</td><td>141.10 (n/a)</td><td>23.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.40 (n/a)</td><td>172.62 (n/a)</td><td>166.10 (n/a)</td><td>132.30 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>352.30 (n/a)</td><td>247.12 (n/a)</td><td>192.30 (n/a)</td><td>149.40 (n/a)</td><td>96.92 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>193.80 (n/a)</td><td>160.40 (n/a)</td><td>161.40 (n/a)</td><td>112.90 (n/a)</td><td>33.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>186.00 (n/a)</td><td>165.50 (n/a)</td><td>164.00 (n/a)</td><td>148.80 (n/a)</td><td>16.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>172.92 (n/a)</td><td>173.60 (n/a)</td><td>160.30 (n/a)</td><td>11.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>283.90 (n/a)</td><td>221.56 (n/a)</td><td>212.10 (n/a)</td><td>179.70 (n/a)</td><td>40.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (+5.22%)</td><td>0.02 (-10.83%)</td><td>0.02 (-7.17%)</td><td>0.02 <b>(-33.19%)</b></td><td>0.01 <b>(+70.10%)</b></td><td>258.40 <b>(+49.71%)</b></td><td>179.72 (+17.93%)</td><td>174.60 (+7.71%)</td><td>113.40 (-4.95%)</td><td>51.66 <b>(+140.83%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.60 (n/a)</td><td>152.40 (n/a)</td><td>162.10 (n/a)</td><td>119.30 (n/a)</td><td>21.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-19.62%)</td><td>0.03 (-5.69%)</td><td>0.02 (-4.97%)</td><td>0.02 (+8.49%)</td><td>0.00 <b>(-41.38%)</b></td><td>213.40 (-7.82%)</td><td>165.72 (+2.03%)</td><td>166.10 (+5.26%)</td><td>136.70 <b>(+24.39%)</b></td><td>30.91 <b>(-33.74%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>162.42 (n/a)</td><td>157.80 (n/a)</td><td>109.90 (n/a)</td><td>46.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 <b>(-25.18%)</b></td><td>0.02 (-13.31%)</td><td>0.02 (-11.47%)</td><td>0.02 (-1.85%)</td><td>0.00 <b>(-47.47%)</b></td><td>234.20 (+1.87%)</td><td>195.90 (+12.43%)</td><td>189.40 (+12.94%)</td><td>165.10 <b>(+33.58%)</b></td><td>28.33 <b>(-27.92%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>174.24 (n/a)</td><td>167.70 (n/a)</td><td>123.60 (n/a)</td><td>39.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 <b>(-21.50%)</b></td><td>0.02 <b>(-20.06%)</b></td><td>0.02 <b>(-23.52%)</b></td><td>0.02 (-3.30%)</td><td>0.00 <b>(-52.79%)</b></td><td>224.70 (+3.41%)</td><td>201.54 <b>(+22.65%)</b></td><td>206.90 <b>(+30.70%)</b></td><td>173.50 <b>(+27.39%)</b></td><td>20.04 <b>(-38.46%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.30 (n/a)</td><td>164.32 (n/a)</td><td>158.30 (n/a)</td><td>136.20 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+4.95%)</td><td>0.02 (-10.09%)</td><td>0.02 (-18.32%)</td><td>0.02 (-10.78%)</td><td>0.00 <b>(+22.43%)</b></td><td>216.40 (+12.07%)</td><td>187.76 (+12.53%)</td><td>206.50 <b>(+22.41%)</b></td><td>133.70 (-4.70%)</td><td>34.09 <b>(+30.73%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.10 (n/a)</td><td>166.86 (n/a)</td><td>168.70 (n/a)</td><td>140.30 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+1.86%)</td><td>0.02 (-0.68%)</td><td>0.02 (-2.80%)</td><td>0.02 (+10.45%)</td><td>0.00 (-7.47%)</td><td>229.40 (-9.44%)</td><td>195.18 (+0.01%)</td><td>196.50 (+2.88%)</td><td>152.20 (-1.87%)</td><td>28.36 <b>(-21.24%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>253.30 (n/a)</td><td>195.16 (n/a)</td><td>191.00 (n/a)</td><td>155.10 (n/a)</td><td>36.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+16.28%)</td><td>0.02 (+13.27%)</td><td>0.03 <b>(+21.05%)</b></td><td>0.02 (+0.84%)</td><td>0.01 <b>(+81.18%)</b></td><td>209.60 (-0.85%)</td><td>171.86 (-9.70%)</td><td>161.50 (-17.39%)</td><td>132.50 (-14.02%)</td><td>35.60 <b>(+65.64%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.40 (n/a)</td><td>190.32 (n/a)</td><td>195.50 (n/a)</td><td>154.10 (n/a)</td><td>21.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 <b>(-32.58%)</b></td><td>0.02 (-7.91%)</td><td>0.02 (+1.15%)</td><td>0.02 (+18.44%)</td><td>0.00 <b>(-80.82%)</b></td><td>245.80 (-15.56%)</td><td>222.90 (+2.91%)</td><td>220.20 (-1.17%)</td><td>211.20 <b>(+48.31%)</b></td><td>13.62 <b>(-75.29%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>291.10 (n/a)</td><td>216.60 (n/a)</td><td>222.80 (n/a)</td><td>142.40 (n/a)</td><td>55.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 <b>(+27.73%)</b></td><td>0.05 (+4.96%)</td><td>0.05 (-8.12%)</td><td>0.05 (+4.83%)</td><td>0.01 <b>(+82.87%)</b></td><td>180.40 (-4.60%)</td><td>161.32 (-3.12%)</td><td>169.90 (+8.84%)</td><td>113.90 <b>(-21.72%)</b></td><td>27.28 <b>(+30.11%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>166.52 (n/a)</td><td>156.10 (n/a)</td><td>145.50 (n/a)</td><td>20.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 <b>(-29.78%)</b></td><td>0.04 <b>(-29.92%)</b></td><td>0.04 <b>(-34.82%)</b></td><td>0.04 (-15.79%)</td><td>0.00 <b>(-65.96%)</b></td><td>210.50 (+18.79%)</td><td>194.90 <b>(+40.64%)</b></td><td>196.40 <b>(+53.44%)</b></td><td>176.00 <b>(+42.39%)</b></td><td>12.81 <b>(-43.09%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.20 (n/a)</td><td>138.58 (n/a)</td><td>128.00 (n/a)</td><td>123.60 (n/a)</td><td>22.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (-1.62%)</td><td>0.05 (-17.52%)</td><td>0.05 (-17.46%)</td><td>0.04 <b>(-28.06%)</b></td><td>0.01 <b>(+71.51%)</b></td><td>222.20 <b>(+39.05%)</b></td><td>176.34 <b>(+24.67%)</b></td><td>170.40 <b>(+21.11%)</b></td><td>125.30 (+1.62%)</td><td>36.57 <b>(+139.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>159.80 (n/a)</td><td>141.44 (n/a)</td><td>140.70 (n/a)</td><td>123.30 (n/a)</td><td>15.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (-6.02%)</td><td>0.05 (-4.14%)</td><td>0.05 (+2.10%)</td><td>0.03 <b>(-20.07%)</b></td><td>0.01 (+3.20%)</td><td>234.20 <b>(+25.11%)</b></td><td>179.54 (+5.28%)</td><td>178.10 (-2.04%)</td><td>133.70 (+6.36%)</td><td>35.82 <b>(+40.19%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.20 (n/a)</td><td>170.54 (n/a)</td><td>181.80 (n/a)</td><td>125.70 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+10.67%)</td><td>0.05 (-11.17%)</td><td>0.03 <b>(-32.50%)</b></td><td>0.03 <b>(-27.66%)</b></td><td>0.02 <b>(+196.55%)</b></td><td>264.90 <b>(+38.26%)</b></td><td>201.32 <b>(+24.50%)</b></td><td>237.00 <b>(+48.12%)</b></td><td>124.30 (-9.67%)</td><td>68.98 <b>(+257.51%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>161.70 (n/a)</td><td>160.00 (n/a)</td><td>137.60 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (-1.28%)</td><td>0.05 (-1.14%)</td><td>0.05 (+2.55%)</td><td>0.04 (-3.68%)</td><td>0.01 (-4.13%)</td><td>220.00 (+3.82%)</td><td>176.00 (+1.07%)</td><td>172.50 (-2.49%)</td><td>136.10 (+1.34%)</td><td>30.82 (+1.07%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.90 (n/a)</td><td>174.14 (n/a)</td><td>176.90 (n/a)</td><td>134.30 (n/a)</td><td>30.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 <b>(-22.99%)</b></td><td>0.05 <b>(-21.01%)</b></td><td>0.04 <b>(-20.68%)</b></td><td>0.04 (-18.86%)</td><td>0.01 <b>(-28.89%)</b></td><td>218.70 <b>(+23.21%)</b></td><td>182.32 <b>(+25.77%)</b></td><td>187.00 <b>(+26.10%)</b></td><td>136.70 <b>(+29.82%)</b></td><td>32.70 (+13.82%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>144.96 (n/a)</td><td>148.30 (n/a)</td><td>105.30 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (-19.71%)</td><td>0.05 (+1.51%)</td><td>0.04 (-0.93%)</td><td>0.04 <b>(+23.10%)</b></td><td>0.01 <b>(-48.86%)</b></td><td>206.00 (-18.77%)</td><td>174.48 (-5.77%)</td><td>184.00 (+0.93%)</td><td>145.90 <b>(+24.59%)</b></td><td>25.50 <b>(-47.71%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.60 (n/a)</td><td>185.16 (n/a)</td><td>182.30 (n/a)</td><td>117.10 (n/a)</td><td>48.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (-6.56%)</td><td>0.05 (-7.51%)</td><td>0.04 (-3.28%)</td><td>0.03 <b>(-20.83%)</b></td><td>0.01 (+15.86%)</td><td>237.50 <b>(+26.33%)</b></td><td>182.56 (+10.28%)</td><td>183.10 (+3.39%)</td><td>131.10 (+7.02%)</td><td>42.67 <b>(+56.06%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>165.54 (n/a)</td><td>177.10 (n/a)</td><td>122.50 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 <b>(-39.41%)</b></td><td>0.04 (-13.74%)</td><td>0.04 (-2.47%)</td><td>0.03 (-3.83%)</td><td>0.00 <b>(-91.48%)</b></td><td>240.30 (+3.98%)</td><td>230.44 (+11.49%)</td><td>229.40 (+2.55%)</td><td>225.60 <b>(+65.03%)</b></td><td>5.91 <b>(-85.01%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>206.70 (n/a)</td><td>223.70 (n/a)</td><td>136.70 (n/a)</td><td>39.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (-14.32%)</td><td>0.09 (-12.57%)</td><td>0.09 (-12.07%)</td><td>0.07 <b>(-21.14%)</b></td><td>0.01 (-4.06%)</td><td>242.50 <b>(+26.76%)</b></td><td>193.86 (+14.89%)</td><td>187.30 (+13.72%)</td><td>165.10 (+16.76%)</td><td>28.97 <b>(+44.97%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>168.74 (n/a)</td><td>164.70 (n/a)</td><td>141.40 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (+13.54%)</td><td>0.10 (-1.04%)</td><td>0.10 (-0.70%)</td><td>0.08 (-19.83%)</td><td>0.02 <b>(+267.41%)</b></td><td>208.50 <b>(+24.70%)</b></td><td>164.28 (+3.79%)</td><td>161.70 (+0.75%)</td><td>129.00 (-11.89%)</td><td>31.33 <b>(+304.52%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>167.20 (n/a)</td><td>158.28 (n/a)</td><td>160.50 (n/a)</td><td>146.40 (n/a)</td><td>7.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (-14.08%)</td><td>0.09 (-6.31%)</td><td>0.09 (-7.22%)</td><td>0.08 (-0.90%)</td><td>0.01 <b>(-35.12%)</b></td><td>211.00 (+0.91%)</td><td>185.82 (+5.03%)</td><td>189.70 (+7.78%)</td><td>147.40 (+16.43%)</td><td>25.03 <b>(-24.29%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.10 (n/a)</td><td>176.92 (n/a)</td><td>176.00 (n/a)</td><td>126.60 (n/a)</td><td>33.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (-12.74%)</td><td>0.08 (-14.59%)</td><td>0.09 (-7.61%)</td><td>0.05 <b>(-44.61%)</b></td><td>0.02 <b>(+134.62%)</b></td><td>353.50 <b>(+80.54%)</b></td><td>218.70 <b>(+24.57%)</b></td><td>190.60 (+8.23%)</td><td>177.80 (+14.56%)</td><td>75.59 <b>(+401.78%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>175.56 (n/a)</td><td>176.10 (n/a)</td><td>155.20 (n/a)</td><td>15.06 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (-14.67%)</td><td>0.08 (-16.96%)</td><td>0.09 (-15.17%)</td><td>0.06 <b>(-27.68%)</b></td><td>0.01 (+9.76%)</td><td>266.70 <b>(+38.26%)</b></td><td>208.00 <b>(+21.87%)</b></td><td>192.50 (+17.88%)</td><td>166.90 (+17.21%)</td><td>38.06 <b>(+76.29%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>170.68 (n/a)</td><td>163.30 (n/a)</td><td>142.40 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (+14.51%)</td><td>0.09 (+5.88%)</td><td>0.09 (+9.00%)</td><td>0.06 (-9.63%)</td><td>0.02 <b>(+67.59%)</b></td><td>254.00 (+10.63%)</td><td>195.60 (-3.83%)</td><td>189.10 (-8.25%)</td><td>152.10 (-12.69%)</td><td>38.18 <b>(+63.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>203.40 (n/a)</td><td>206.10 (n/a)</td><td>174.20 (n/a)</td><td>23.33 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (-2.88%)</td><td>0.08 (-7.02%)</td><td>0.08 (-11.91%)</td><td>0.08 (-8.56%)</td><td>0.01 <b>(+36.04%)</b></td><td>217.90 (+9.39%)</td><td>200.60 (+7.93%)</td><td>209.80 (+13.53%)</td><td>174.50 (+2.95%)</td><td>18.05 <b>(+52.70%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>185.86 (n/a)</td><td>184.80 (n/a)</td><td>169.50 (n/a)</td><td>11.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (-13.08%)</td><td>0.07 (-1.90%)</td><td>0.07 (+1.41%)</td><td>0.06 <b>(+24.22%)</b></td><td>0.01 <b>(-56.28%)</b></td><td>267.20 (-19.49%)</td><td>227.84 (-1.84%)</td><td>222.40 (-1.42%)</td><td>206.30 (+15.06%)</td><td>24.18 <b>(-59.87%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>331.90 (n/a)</td><td>232.10 (n/a)</td><td>225.60 (n/a)</td><td>179.30 (n/a)</td><td>60.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 <b>(+37.91%)</b></td><td>0.21 <b>(+22.21%)</b></td><td>0.18 (+4.15%)</td><td>0.16 <b>(+33.45%)</b></td><td>0.04 <b>(+62.81%)</b></td><td>198.90 <b>(-25.08%)</b></td><td>164.08 (-17.44%)</td><td>180.80 (-3.98%)</td><td>126.40 <b>(-27.48%)</b></td><td>32.16 (-15.27%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>265.50 (n/a)</td><td>198.74 (n/a)</td><td>188.30 (n/a)</td><td>174.30 (n/a)</td><td>37.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 <b>(+25.77%)</b></td><td>0.22 (+17.28%)</td><td>0.22 (+18.43%)</td><td>0.16 (+1.76%)</td><td>0.05 <b>(+102.79%)</b></td><td>211.10 (-1.72%)</td><td>157.74 (-12.48%)</td><td>149.30 (-15.55%)</td><td>122.00 <b>(-20.47%)</b></td><td>35.62 <b>(+57.40%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.80 (n/a)</td><td>180.24 (n/a)</td><td>176.80 (n/a)</td><td>153.40 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (+1.21%)</td><td>0.20 (+5.47%)</td><td>0.20 (+6.59%)</td><td>0.15 (-0.44%)</td><td>0.03 (+10.86%)</td><td>214.40 (+0.47%)</td><td>169.42 (-4.82%)</td><td>167.30 (-6.17%)</td><td>143.00 (-1.17%)</td><td>27.95 (+11.29%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.40 (n/a)</td><td>178.00 (n/a)</td><td>178.30 (n/a)</td><td>144.70 (n/a)</td><td>25.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (+16.74%)</td><td>0.20 (+2.43%)</td><td>0.20 (+3.50%)</td><td>0.13 <b>(-27.47%)</b></td><td>0.06 <b>(+214.25%)</b></td><td>257.70 <b>(+37.88%)</b></td><td>173.06 (+4.03%)</td><td>160.40 (-3.37%)</td><td>126.20 (-14.38%)</td><td>54.27 <b>(+262.58%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>166.36 (n/a)</td><td>166.00 (n/a)</td><td>147.40 (n/a)</td><td>14.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 <b>(-41.99%)</b></td><td>0.15 <b>(-24.70%)</b></td><td>0.15 <b>(-27.28%)</b></td><td>0.13 (-2.87%)</td><td>0.01 <b>(-77.24%)</b></td><td>245.00 (+2.94%)</td><td>214.54 <b>(+23.73%)</b></td><td>217.10 <b>(+37.49%)</b></td><td>191.20 <b>(+72.41%)</b></td><td>20.80 <b>(-60.89%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>238.00 (n/a)</td><td>173.40 (n/a)</td><td>157.90 (n/a)</td><td>110.90 (n/a)</td><td>53.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (-17.54%)</td><td>0.16 (-8.33%)</td><td>0.17 (-4.97%)</td><td>0.12 (-17.16%)</td><td>0.03 (-19.25%)</td><td>277.50 <b>(+20.70%)</b></td><td>204.94 (+9.00%)</td><td>191.40 (+5.22%)</td><td>170.20 <b>(+21.23%)</b></td><td>42.67 <b>(+20.80%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>229.90 (n/a)</td><td>188.02 (n/a)</td><td>181.90 (n/a)</td><td>140.40 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (-15.84%)</td><td>0.14 (-8.49%)</td><td>0.15 (-2.41%)</td><td>0.11 (-10.52%)</td><td>0.02 (-14.38%)</td><td>311.30 (+11.78%)</td><td>242.78 (+9.23%)</td><td>224.30 (+2.47%)</td><td>216.30 (+18.85%)</td><td>39.97 (+12.46%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>278.50 (n/a)</td><td>222.26 (n/a)</td><td>218.90 (n/a)</td><td>182.00 (n/a)</td><td>35.54 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-9.93%)</td><td>0.02 (+6.92%)</td><td>0.02 (-13.22%)</td><td>0.02 <b>(+94.29%)</b></td><td>0.00 <b>(-55.89%)</b></td><td>192.10 <b>(-48.54%)</b></td><td>169.18 <b>(-20.18%)</b></td><td>176.50 (+15.21%)</td><td>127.40 (+11.07%)</td><td>25.65 <b>(-75.94%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>373.30 (n/a)</td><td>211.94 (n/a)</td><td>153.20 (n/a)</td><td>114.70 (n/a)</td><td>106.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (+2.56%)</td><td>0.03 (-3.40%)</td><td>0.03 (-8.73%)</td><td>0.02 (-11.10%)</td><td>0.01 <b>(+35.83%)</b></td><td>198.80 (+12.44%)</td><td>154.14 (+6.48%)</td><td>157.60 (+9.60%)</td><td>107.20 (-2.46%)</td><td>39.62 <b>(+48.73%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>176.80 (n/a)</td><td>144.76 (n/a)</td><td>143.80 (n/a)</td><td>109.90 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 <b>(+22.14%)</b></td><td>0.02 <b>(+31.39%)</b></td><td>0.02 <b>(+29.32%)</b></td><td>0.02 <b>(+47.27%)</b></td><td>0.00 (+4.63%)</td><td>226.60 <b>(-32.09%)</b></td><td>177.00 <b>(-25.21%)</b></td><td>174.30 <b>(-22.67%)</b></td><td>143.10 (-18.09%)</td><td>33.08 <b>(-43.96%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>333.70 (n/a)</td><td>236.66 (n/a)</td><td>225.40 (n/a)</td><td>174.70 (n/a)</td><td>59.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 <b>(+32.22%)</b></td><td>0.02 (+15.69%)</td><td>0.02 (+14.38%)</td><td>0.02 (-6.37%)</td><td>0.00 <b>(+303.77%)</b></td><td>225.20 (+6.78%)</td><td>171.64 (-11.36%)</td><td>167.20 (-12.60%)</td><td>139.00 <b>(-24.37%)</b></td><td>33.35 <b>(+226.38%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.90 (n/a)</td><td>193.64 (n/a)</td><td>191.30 (n/a)</td><td>183.80 (n/a)</td><td>10.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 <b>(+28.18%)</b></td><td>0.03 <b>(+20.44%)</b></td><td>0.03 (+7.02%)</td><td>0.02 <b>(+30.83%)</b></td><td>0.01 <b>(+46.41%)</b></td><td>176.30 <b>(-23.58%)</b></td><td>146.64 (-16.42%)</td><td>147.70 (-6.58%)</td><td>117.40 <b>(-21.94%)</b></td><td>28.84 (-13.92%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.70 (n/a)</td><td>175.44 (n/a)</td><td>158.10 (n/a)</td><td>150.40 (n/a)</td><td>33.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-9.20%)</td><td>0.03 (-3.58%)</td><td>0.03 (-3.62%)</td><td>0.02 <b>(+23.18%)</b></td><td>0.00 <b>(-55.32%)</b></td><td>173.90 (-18.81%)</td><td>151.32 (-0.22%)</td><td>149.00 (+3.76%)</td><td>131.10 (+10.08%)</td><td>16.10 <b>(-59.06%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>151.66 (n/a)</td><td>143.60 (n/a)</td><td>119.10 (n/a)</td><td>39.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-2.29%)</td><td>0.02 (-5.66%)</td><td>0.02 (-14.77%)</td><td>0.02 (-17.30%)</td><td>0.01 <b>(+37.93%)</b></td><td>243.10 <b>(+20.95%)</b></td><td>184.80 (+9.71%)</td><td>205.60 (+17.35%)</td><td>127.80 (+2.32%)</td><td>48.93 <b>(+69.31%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.00 (n/a)</td><td>168.44 (n/a)</td><td>175.20 (n/a)</td><td>124.90 (n/a)</td><td>28.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-8.45%)</td><td>0.03 (+2.64%)</td><td>0.03 (+14.42%)</td><td>0.02 (-17.83%)</td><td>0.01 (+14.88%)</td><td>213.80 <b>(+21.68%)</b></td><td>143.98 (-0.40%)</td><td>118.30 (-12.63%)</td><td>116.60 (+9.28%)</td><td>41.90 <b>(+46.26%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>175.70 (n/a)</td><td>144.56 (n/a)</td><td>135.40 (n/a)</td><td>106.70 (n/a)</td><td>28.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-13.99%)</td><td>0.03 (-3.32%)</td><td>0.03 (+3.49%)</td><td>0.02 (+8.97%)</td><td>0.00 <b>(-53.41%)</b></td><td>181.90 (-8.22%)</td><td>161.60 (+0.34%)</td><td>163.80 (-3.36%)</td><td>139.90 (+16.29%)</td><td>17.40 <b>(-49.96%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>161.06 (n/a)</td><td>169.50 (n/a)</td><td>120.30 (n/a)</td><td>34.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 <b>(-21.03%)</b></td><td>0.02 <b>(-30.62%)</b></td><td>0.02 <b>(-26.53%)</b></td><td>0.01 <b>(-48.47%)</b></td><td>0.01 <b>(+114.04%)</b></td><td>360.10 <b>(+94.02%)</b></td><td>260.08 <b>(+57.24%)</b></td><td>229.30 <b>(+36.08%)</b></td><td>177.00 <b>(+26.61%)</b></td><td>90.76 <b>(+443.97%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.60 (n/a)</td><td>165.40 (n/a)</td><td>168.50 (n/a)</td><td>139.80 (n/a)</td><td>16.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-7.05%)</td><td>0.03 (+3.72%)</td><td>0.02 (+3.81%)</td><td>0.02 <b>(+20.13%)</b></td><td>0.00 <b>(-46.32%)</b></td><td>173.90 (-16.79%)</td><td>160.00 (-5.22%)</td><td>165.30 (-3.67%)</td><td>142.60 (+7.54%)</td><td>13.74 <b>(-51.86%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>168.82 (n/a)</td><td>171.60 (n/a)</td><td>132.60 (n/a)</td><td>28.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-9.19%)</td><td>0.03 (-10.14%)</td><td>0.03 (-11.00%)</td><td>0.02 (-1.39%)</td><td>0.00 <b>(-34.80%)</b></td><td>181.10 (+1.40%)</td><td>160.60 (+10.14%)</td><td>161.40 (+12.32%)</td><td>134.70 (+10.05%)</td><td>16.64 <b>(-27.84%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.60 (n/a)</td><td>145.82 (n/a)</td><td>143.70 (n/a)</td><td>122.40 (n/a)</td><td>23.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+15.71%)</td><td>0.03 (+4.88%)</td><td>0.03 (+2.73%)</td><td>0.02 (+2.19%)</td><td>0.00 <b>(+43.54%)</b></td><td>190.20 (-2.16%)</td><td>154.86 (-4.02%)</td><td>151.50 (-2.70%)</td><td>127.70 (-13.54%)</td><td>22.58 <b>(+20.08%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.40 (n/a)</td><td>161.34 (n/a)</td><td>155.70 (n/a)</td><td>147.70 (n/a)</td><td>18.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (+11.70%)</td><td>0.03 (+6.19%)</td><td>0.03 (+9.19%)</td><td>0.02 (-7.13%)</td><td>0.00 <b>(+90.21%)</b></td><td>178.10 (+7.68%)</td><td>146.40 (-4.19%)</td><td>142.80 (-8.40%)</td><td>116.40 (-10.46%)</td><td>25.25 <b>(+88.97%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>165.40 (n/a)</td><td>152.80 (n/a)</td><td>155.90 (n/a)</td><td>130.00 (n/a)</td><td>13.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+11.95%)</td><td>0.03 (+4.75%)</td><td>0.02 (-6.53%)</td><td>0.02 (+18.01%)</td><td>0.00 (-14.18%)</td><td>188.60 (-15.27%)</td><td>162.20 (-6.28%)</td><td>167.40 (+7.03%)</td><td>122.30 (-10.66%)</td><td>25.36 <b>(-36.58%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>173.06 (n/a)</td><td>156.40 (n/a)</td><td>136.90 (n/a)</td><td>39.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+12.30%)</td><td>0.03 <b>(+26.98%)</b></td><td>0.03 <b>(+39.56%)</b></td><td>0.02 (+10.00%)</td><td>0.00 <b>(+22.34%)</b></td><td>187.10 (-9.13%)</td><td>142.96 <b>(-20.92%)</b></td><td>130.90 <b>(-28.35%)</b></td><td>124.10 (-10.91%)</td><td>26.52 (-1.17%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.90 (n/a)</td><td>180.78 (n/a)</td><td>182.70 (n/a)</td><td>139.30 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 <b>(+28.66%)</b></td><td>0.06 <b>(+23.50%)</b></td><td>0.06 <b>(+22.39%)</b></td><td>0.05 (+14.34%)</td><td>0.01 <b>(+157.63%)</b></td><td>155.30 (-12.56%)</td><td>136.04 (-17.99%)</td><td>138.60 (-18.28%)</td><td>115.70 <b>(-22.30%)</b></td><td>19.31 <b>(+75.57%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.60 (n/a)</td><td>165.88 (n/a)</td><td>169.60 (n/a)</td><td>148.90 (n/a)</td><td>11.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+0.80%)</td><td>0.06 <b>(+23.57%)</b></td><td>0.07 <b>(+45.84%)</b></td><td>0.06 <b>(+45.26%)</b></td><td>0.01 <b>(-48.51%)</b></td><td>146.30 <b>(-31.15%)</b></td><td>130.14 <b>(-22.09%)</b></td><td>120.50 <b>(-31.42%)</b></td><td>119.40 (-0.75%)</td><td>13.91 <b>(-64.46%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>167.04 (n/a)</td><td>175.70 (n/a)</td><td>120.30 (n/a)</td><td>39.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (+16.75%)</td><td>0.04 (+16.16%)</td><td>0.04 (+13.95%)</td><td>0.04 <b>(+29.09%)</b></td><td>0.00 (-4.44%)</td><td>233.70 <b>(-22.54%)</b></td><td>204.68 (-14.48%)</td><td>203.10 (-12.23%)</td><td>177.40 (-14.34%)</td><td>22.54 <b>(-38.36%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>301.70 (n/a)</td><td>239.34 (n/a)</td><td>231.40 (n/a)</td><td>207.10 (n/a)</td><td>36.58 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (-2.67%)</td><td>0.04 (-7.55%)</td><td>0.04 (-10.31%)</td><td>0.03 (-19.42%)</td><td>0.01 <b>(+55.88%)</b></td><td>290.60 <b>(+24.08%)</b></td><td>216.90 (+10.99%)</td><td>213.50 (+11.49%)</td><td>172.10 (+2.75%)</td><td>49.57 <b>(+90.96%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>195.42 (n/a)</td><td>191.50 (n/a)</td><td>167.50 (n/a)</td><td>25.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+8.69%)</td><td>0.06 (+12.51%)</td><td>0.05 (+10.92%)</td><td>0.05 (+17.20%)</td><td>0.01 (-16.66%)</td><td>176.40 (-14.66%)</td><td>149.48 (-12.10%)</td><td>149.50 (-9.83%)</td><td>123.70 (-7.96%)</td><td>19.06 <b>(-35.37%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>170.06 (n/a)</td><td>165.80 (n/a)</td><td>134.40 (n/a)</td><td>29.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+7.05%)</td><td>0.06 (+18.61%)</td><td>0.06 <b>(+25.17%)</b></td><td>0.05 <b>(+42.61%)</b></td><td>0.01 <b>(-37.82%)</b></td><td>155.50 <b>(-29.89%)</b></td><td>135.80 (-18.74%)</td><td>133.90 <b>(-20.06%)</b></td><td>113.60 (-6.58%)</td><td>17.44 <b>(-58.12%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>167.12 (n/a)</td><td>167.50 (n/a)</td><td>121.60 (n/a)</td><td>41.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 <b>(+25.63%)</b></td><td>0.06 <b>(+20.28%)</b></td><td>0.06 (+19.45%)</td><td>0.05 <b>(+30.62%)</b></td><td>0.01 (+12.20%)</td><td>154.30 <b>(-23.42%)</b></td><td>134.92 (-17.34%)</td><td>140.80 (-16.24%)</td><td>103.30 <b>(-20.42%)</b></td><td>20.81 <b>(-30.28%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>163.22 (n/a)</td><td>168.10 (n/a)</td><td>129.80 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 <b>(-37.72%)</b></td><td>0.05 (-9.76%)</td><td>0.05 (-4.85%)</td><td>0.04 (+6.64%)</td><td>0.01 <b>(-67.23%)</b></td><td>196.80 (-6.24%)</td><td>165.86 (+2.26%)</td><td>174.60 (+5.05%)</td><td>137.00 <b>(+60.61%)</b></td><td>24.41 <b>(-48.04%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>209.90 (n/a)</td><td>162.20 (n/a)</td><td>166.20 (n/a)</td><td>85.30 (n/a)</td><td>46.98 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (-6.30%)</td><td>0.05 (+9.96%)</td><td>0.05 <b>(+21.05%)</b></td><td>0.04 (-2.01%)</td><td>0.01 (-18.34%)</td><td>206.80 (+2.07%)</td><td>157.52 (-9.84%)</td><td>149.50 (-17.40%)</td><td>125.60 (+6.80%)</td><td>31.27 (-5.87%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>174.72 (n/a)</td><td>181.00 (n/a)</td><td>117.60 (n/a)</td><td>33.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (+12.25%)</td><td>0.05 (-4.29%)</td><td>0.04 (-19.25%)</td><td>0.04 (-5.72%)</td><td>0.01 <b>(+41.45%)</b></td><td>220.70 (+6.05%)</td><td>174.86 (+6.36%)</td><td>183.00 <b>(+23.82%)</b></td><td>127.10 (-10.93%)</td><td>37.31 <b>(+33.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>164.40 (n/a)</td><td>147.80 (n/a)</td><td>142.70 (n/a)</td><td>28.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (+0.62%)</td><td>0.05 (+3.40%)</td><td>0.05 (+7.38%)</td><td>0.05 (-1.38%)</td><td>0.00 (-5.34%)</td><td>180.70 (+1.40%)</td><td>161.62 (-3.33%)</td><td>159.90 (-6.87%)</td><td>147.60 (-0.61%)</td><td>12.25 (-4.33%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.20 (n/a)</td><td>167.18 (n/a)</td><td>171.70 (n/a)</td><td>148.50 (n/a)</td><td>12.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 <b>(-21.86%)</b></td><td>0.05 (-14.48%)</td><td>0.06 (-4.46%)</td><td>0.04 (+4.41%)</td><td>0.01 <b>(-28.80%)</b></td><td>223.50 (-4.20%)</td><td>164.26 (+13.08%)</td><td>137.10 (+4.66%)</td><td>116.20 <b>(+27.97%)</b></td><td>48.40 (-11.59%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>233.30 (n/a)</td><td>145.26 (n/a)</td><td>131.00 (n/a)</td><td>90.80 (n/a)</td><td>54.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 <b>(+53.68%)</b></td><td>0.05 <b>(+22.40%)</b></td><td>0.04 (+12.06%)</td><td>0.03 (-5.14%)</td><td>0.01 <b>(+234.72%)</b></td><td>248.50 (+5.43%)</td><td>175.92 (-13.60%)</td><td>182.70 (-10.75%)</td><td>116.20 <b>(-34.94%)</b></td><td>49.76 <b>(+127.61%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.70 (n/a)</td><td>203.62 (n/a)</td><td>204.70 (n/a)</td><td>178.60 (n/a)</td><td>21.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (-9.22%)</td><td>0.05 (-10.74%)</td><td>0.05 (-13.65%)</td><td>0.04 (-13.52%)</td><td>0.01 (-1.21%)</td><td>210.80 (+15.63%)</td><td>176.26 (+12.28%)</td><td>175.40 (+15.78%)</td><td>152.30 (+10.12%)</td><td>22.21 <b>(+26.31%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>156.98 (n/a)</td><td>151.50 (n/a)</td><td>138.30 (n/a)</td><td>17.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (+9.89%)</td><td>0.04 (-6.24%)</td><td>0.04 (-15.43%)</td><td>0.03 (-16.91%)</td><td>0.01 <b>(+97.78%)</b></td><td>243.80 <b>(+20.34%)</b></td><td>194.06 (+10.54%)</td><td>203.00 (+18.23%)</td><td>134.70 (-8.99%)</td><td>44.72 <b>(+115.84%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>175.56 (n/a)</td><td>171.70 (n/a)</td><td>148.00 (n/a)</td><td>20.72 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (-0.80%)</td><td>0.05 (+4.37%)</td><td>0.05 (-0.03%)</td><td>0.04 (+18.65%)</td><td>0.01 (-19.04%)</td><td>188.10 (-15.73%)</td><td>164.24 (-5.73%)</td><td>174.30 (+0.00%)</td><td>123.40 (+0.82%)</td><td>24.79 <b>(-31.38%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.20 (n/a)</td><td>174.22 (n/a)</td><td>174.30 (n/a)</td><td>122.40 (n/a)</td><td>36.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 <b>(+27.82%)</b></td><td>0.11 (+13.67%)</td><td>0.12 (+18.57%)</td><td>0.09 (+4.52%)</td><td>0.02 <b>(+130.10%)</b></td><td>183.10 (-4.29%)</td><td>148.82 (-10.08%)</td><td>135.40 (-15.69%)</td><td>116.90 <b>(-21.75%)</b></td><td>28.64 <b>(+75.80%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>165.50 (n/a)</td><td>160.60 (n/a)</td><td>149.40 (n/a)</td><td>16.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (+13.38%)</td><td>0.10 (+9.21%)</td><td>0.10 (+11.03%)</td><td>0.08 (-5.47%)</td><td>0.02 <b>(+59.39%)</b></td><td>198.20 (+5.82%)</td><td>159.80 (-7.36%)</td><td>158.30 (-9.95%)</td><td>127.40 (-11.77%)</td><td>25.58 <b>(+51.26%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>187.30 (n/a)</td><td>172.50 (n/a)</td><td>175.80 (n/a)</td><td>144.40 (n/a)</td><td>16.91 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 <b>(+25.22%)</b></td><td>0.09 (+17.41%)</td><td>0.09 (+17.70%)</td><td>0.07 (+6.65%)</td><td>0.01 <b>(+105.32%)</b></td><td>231.30 (-6.20%)</td><td>187.90 (-13.77%)</td><td>182.10 (-15.03%)</td><td>155.80 <b>(-20.14%)</b></td><td>28.88 <b>(+53.90%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>246.60 (n/a)</td><td>217.90 (n/a)</td><td>214.30 (n/a)</td><td>195.10 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (-2.58%)</td><td>0.09 (+4.50%)</td><td>0.09 (+2.47%)</td><td>0.08 <b>(+23.11%)</b></td><td>0.01 <b>(-43.92%)</b></td><td>211.10 (-18.78%)</td><td>176.16 (-6.85%)</td><td>173.00 (-2.43%)</td><td>156.20 (+2.70%)</td><td>20.78 <b>(-52.32%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>259.90 (n/a)</td><td>189.12 (n/a)</td><td>177.30 (n/a)</td><td>152.10 (n/a)</td><td>43.58 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (+11.00%)</td><td>0.12 <b>(+21.81%)</b></td><td>0.13 <b>(+47.33%)</b></td><td>0.08 (-11.04%)</td><td>0.03 <b>(+35.80%)</b></td><td>217.50 (+12.40%)</td><td>142.32 (-15.78%)</td><td>125.60 <b>(-32.11%)</b></td><td>113.90 (-9.89%)</td><td>42.55 <b>(+41.72%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.50 (n/a)</td><td>168.98 (n/a)</td><td>185.00 (n/a)</td><td>126.40 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (+1.34%)</td><td>0.11 (+2.71%)</td><td>0.10 (+3.63%)</td><td>0.08 (-6.35%)</td><td>0.03 <b>(+20.30%)</b></td><td>200.50 (+6.76%)</td><td>160.00 (-1.10%)</td><td>163.10 (-3.49%)</td><td>115.10 (-1.29%)</td><td>35.93 <b>(+31.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.80 (n/a)</td><td>161.78 (n/a)</td><td>169.00 (n/a)</td><td>116.60 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 <b>(+60.15%)</b></td><td>0.11 <b>(+26.77%)</b></td><td>0.10 (+16.88%)</td><td>0.08 <b>(+36.61%)</b></td><td>0.03 <b>(+119.80%)</b></td><td>199.30 <b>(-26.81%)</b></td><td>164.16 (-18.43%)</td><td>167.80 (-14.48%)</td><td>98.40 <b>(-37.56%)</b></td><td>40.67 (-4.91%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>272.30 (n/a)</td><td>201.24 (n/a)</td><td>196.20 (n/a)</td><td>157.60 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (+2.44%)</td><td>0.11 (+17.27%)</td><td>0.11 <b>(+23.83%)</b></td><td>0.10 <b>(+27.46%)</b></td><td>0.01 <b>(-38.66%)</b></td><td>156.40 <b>(-21.53%)</b></td><td>143.82 (-16.19%)</td><td>144.20 (-19.26%)</td><td>124.10 (-2.36%)</td><td>13.56 <b>(-51.43%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.30 (n/a)</td><td>171.60 (n/a)</td><td>178.60 (n/a)</td><td>127.10 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (+7.20%)</td><td>0.10 (+2.51%)</td><td>0.10 (+1.65%)</td><td>0.09 (-0.27%)</td><td>0.01 <b>(+21.96%)</b></td><td>187.30 (+0.27%)</td><td>159.58 (-2.07%)</td><td>157.90 (-1.68%)</td><td>133.60 (-6.70%)</td><td>21.20 (+14.57%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.80 (n/a)</td><td>162.96 (n/a)</td><td>160.60 (n/a)</td><td>143.20 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 <b>(+23.52%)</b></td><td>0.10 (+12.34%)</td><td>0.10 (+5.83%)</td><td>0.08 (+3.16%)</td><td>0.02 <b>(+97.40%)</b></td><td>195.60 (-3.07%)</td><td>163.90 (-9.54%)</td><td>168.20 (-5.51%)</td><td>128.70 (-19.06%)</td><td>27.96 <b>(+52.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>181.18 (n/a)</td><td>178.00 (n/a)</td><td>159.00 (n/a)</td><td>18.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (+8.05%)</td><td>0.09 (-2.78%)</td><td>0.11 (+5.38%)</td><td>0.06 <b>(-23.65%)</b></td><td>0.02 <b>(+122.00%)</b></td><td>262.40 <b>(+31.00%)</b></td><td>183.12 (+7.65%)</td><td>149.70 (-5.13%)</td><td>145.00 (-7.47%)</td><td>51.56 <b>(+166.48%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.30 (n/a)</td><td>170.10 (n/a)</td><td>157.80 (n/a)</td><td>156.70 (n/a)</td><td>19.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 <b>(+35.56%)</b></td><td>0.11 (+5.37%)</td><td>0.10 (-3.77%)</td><td>0.07 (-16.36%)</td><td>0.03 <b>(+232.07%)</b></td><td>222.40 (+19.57%)</td><td>165.94 (+1.69%)</td><td>166.40 (+3.94%)</td><td>104.60 <b>(-26.18%)</b></td><td>49.03 <b>(+195.13%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>163.18 (n/a)</td><td>160.10 (n/a)</td><td>141.70 (n/a)</td><td>16.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (+12.37%)</td><td>0.10 (+14.54%)</td><td>0.10 <b>(+25.26%)</b></td><td>0.05 <b>(-27.90%)</b></td><td>0.03 <b>(+78.41%)</b></td><td>301.20 <b>(+38.74%)</b></td><td>180.86 (-6.95%)</td><td>159.30 <b>(-20.19%)</b></td><td>129.80 (-11.03%)</td><td>68.55 <b>(+144.11%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>194.36 (n/a)</td><td>199.60 (n/a)</td><td>145.90 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (+6.16%)</td><td>0.10 (+17.28%)</td><td>0.10 (+11.86%)</td><td>0.08 <b>(+21.32%)</b></td><td>0.01 (-17.14%)</td><td>207.80 (-17.57%)</td><td>171.22 (-16.08%)</td><td>171.50 (-10.58%)</td><td>140.60 (-5.83%)</td><td>25.95 <b>(-36.32%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>252.10 (n/a)</td><td>204.02 (n/a)</td><td>191.80 (n/a)</td><td>149.30 (n/a)</td><td>40.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 <b>(+40.43%)</b></td><td>0.11 <b>(+27.74%)</b></td><td>0.10 <b>(+21.79%)</b></td><td>0.10 <b>(+34.94%)</b></td><td>0.01 <b>(+72.74%)</b></td><td>169.00 <b>(-25.88%)</b></td><td>156.38 <b>(-21.50%)</b></td><td>159.50 (-17.91%)</td><td>130.90 <b>(-28.78%)</b></td><td>14.87 (-12.23%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>199.20 (n/a)</td><td>194.30 (n/a)</td><td>183.80 (n/a)</td><td>16.94 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (+18.13%)</td><td>0.09 (+3.42%)</td><td>0.09 (+8.28%)</td><td>0.05 <b>(-36.26%)</b></td><td>0.03 <b>(+170.80%)</b></td><td>362.40 <b>(+56.88%)</b></td><td>217.60 (+10.56%)</td><td>181.50 (-7.68%)</td><td>132.90 (-15.35%)</td><td>98.92 <b>(+248.44%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>231.00 (n/a)</td><td>196.82 (n/a)</td><td>196.60 (n/a)</td><td>157.00 (n/a)</td><td>28.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (-8.38%)</td><td>0.21 (-14.45%)</td><td>0.20 <b>(-23.02%)</b></td><td>0.18 (+11.37%)</td><td>0.03 <b>(-44.51%)</b></td><td>185.80 (-10.20%)</td><td>159.46 (+13.45%)</td><td>162.60 <b>(+29.87%)</b></td><td>131.50 (+9.13%)</td><td>19.59 <b>(-47.36%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>206.90 (n/a)</td><td>140.56 (n/a)</td><td>125.20 (n/a)</td><td>120.50 (n/a)</td><td>37.21 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (-3.11%)</td><td>0.20 (-7.07%)</td><td>0.20 (-8.45%)</td><td>0.16 (-3.92%)</td><td>0.03 (-9.94%)</td><td>204.30 (+4.08%)</td><td>166.00 (+7.30%)</td><td>161.30 (+9.21%)</td><td>133.30 (+3.25%)</td><td>28.79 (-0.63%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>196.30 (n/a)</td><td>154.70 (n/a)</td><td>147.70 (n/a)</td><td>129.10 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (-19.97%)</td><td>0.17 (-12.09%)</td><td>0.17 (-10.67%)</td><td>0.15 (-4.34%)</td><td>0.01 <b>(-53.06%)</b></td><td>212.80 (+4.52%)</td><td>198.44 (+12.88%)</td><td>196.90 (+11.94%)</td><td>183.90 <b>(+24.93%)</b></td><td>12.59 <b>(-37.88%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.60 (n/a)</td><td>175.80 (n/a)</td><td>175.90 (n/a)</td><td>147.20 (n/a)</td><td>20.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (+17.52%)</td><td>0.19 (-1.24%)</td><td>0.19 (-0.31%)</td><td>0.15 (-19.83%)</td><td>0.03 <b>(+943.53%)</b></td><td>222.00 <b>(+24.72%)</b></td><td>180.00 (+3.16%)</td><td>173.90 (+0.35%)</td><td>146.30 (-14.89%)</td><td>28.03 <b>(+1008.35%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>178.00 (n/a)</td><td>174.48 (n/a)</td><td>173.30 (n/a)</td><td>171.90 (n/a)</td><td>2.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (+10.27%)</td><td>0.21 (-1.24%)</td><td>0.21 (-2.68%)</td><td>0.16 (-3.79%)</td><td>0.05 <b>(+48.74%)</b></td><td>203.80 (+3.98%)</td><td>161.16 (+3.25%)</td><td>156.80 (+2.75%)</td><td>116.70 (-9.32%)</td><td>34.44 <b>(+38.33%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.00 (n/a)</td><td>156.08 (n/a)</td><td>152.60 (n/a)</td><td>128.70 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (-18.26%)</td><td>0.19 (-19.60%)</td><td>0.20 (-15.51%)</td><td>0.14 <b>(-20.96%)</b></td><td>0.04 (-4.31%)</td><td>233.40 <b>(+26.50%)</b></td><td>182.42 <b>(+25.67%)</b></td><td>160.40 (+18.38%)</td><td>150.00 <b>(+22.35%)</b></td><td>39.52 <b>(+48.94%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>184.50 (n/a)</td><td>145.16 (n/a)</td><td>135.50 (n/a)</td><td>122.60 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (-10.73%)</td><td>0.22 (-3.78%)</td><td>0.24 (+9.54%)</td><td>0.13 <b>(-30.06%)</b></td><td>0.06 <b>(+23.45%)</b></td><td>244.10 <b>(+43.00%)</b></td><td>160.34 (+8.19%)</td><td>138.50 (-8.70%)</td><td>119.40 (+12.01%)</td><td>51.09 <b>(+106.86%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>170.70 (n/a)</td><td>148.20 (n/a)</td><td>151.70 (n/a)</td><td>106.60 (n/a)</td><td>24.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 <b>(+23.37%)</b></td><td>0.21 (+12.29%)</td><td>0.20 (+7.78%)</td><td>0.18 (+5.90%)</td><td>0.04 <b>(+81.58%)</b></td><td>177.70 (-5.58%)</td><td>156.42 (-9.82%)</td><td>161.20 (-7.25%)</td><td>118.00 (-18.96%)</td><td>23.58 <b>(+37.10%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.20 (n/a)</td><td>173.46 (n/a)</td><td>173.80 (n/a)</td><td>145.60 (n/a)</td><td>17.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (-12.71%)</td><td>0.21 (+4.39%)</td><td>0.22 (+16.50%)</td><td>0.16 (+15.26%)</td><td>0.03 <b>(-42.72%)</b></td><td>200.60 (-13.27%)</td><td>160.46 (-6.71%)</td><td>150.70 (-14.18%)</td><td>144.60 (+14.58%)</td><td>22.82 <b>(-41.89%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>231.30 (n/a)</td><td>172.00 (n/a)</td><td>175.60 (n/a)</td><td>126.20 (n/a)</td><td>39.27 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.24 (-3.67%)</td><td>0.19 (-2.92%)</td><td>0.19 (-0.48%)</td><td>0.15 (-12.56%)</td><td>0.04 (+11.93%)</td><td>223.30 (+14.40%)</td><td>173.72 (+4.02%)</td><td>174.90 (+0.46%)</td><td>134.70 (+3.78%)</td><td>34.16 <b>(+34.16%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.20 (n/a)</td><td>167.00 (n/a)</td><td>174.10 (n/a)</td><td>129.80 (n/a)</td><td>25.46 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (-3.93%)</td><td>0.20 (-10.02%)</td><td>0.21 (+6.06%)</td><td>0.13 <b>(-25.26%)</b></td><td>0.06 <b>(+21.33%)</b></td><td>245.10 <b>(+33.79%)</b></td><td>175.12 (+15.20%)</td><td>155.00 (-5.72%)</td><td>117.60 (+4.07%)</td><td>52.51 <b>(+73.64%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>183.20 (n/a)</td><td>152.02 (n/a)</td><td>164.40 (n/a)</td><td>113.00 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (-12.16%)</td><td>0.20 (-11.02%)</td><td>0.19 (-6.27%)</td><td>0.19 (-1.83%)</td><td>0.02 <b>(-41.31%)</b></td><td>177.10 (+1.90%)</td><td>166.98 (+11.04%)</td><td>174.20 (+6.67%)</td><td>139.40 (+13.80%)</td><td>15.75 <b>(-31.76%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>173.80 (n/a)</td><td>150.38 (n/a)</td><td>163.30 (n/a)</td><td>122.50 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.24 (+10.99%)</td><td>0.20 (+14.52%)</td><td>0.19 (+4.87%)</td><td>0.16 <b>(+29.52%)</b></td><td>0.03 <b>(-23.26%)</b></td><td>209.40 <b>(-22.79%)</b></td><td>169.32 (-15.20%)</td><td>170.10 (-4.65%)</td><td>139.20 (-9.90%)</td><td>27.87 <b>(-46.24%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>271.20 (n/a)</td><td>199.68 (n/a)</td><td>178.40 (n/a)</td><td>154.50 (n/a)</td><td>51.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (+10.92%)</td><td>0.21 (+8.72%)</td><td>0.19 (+4.86%)</td><td>0.18 <b>(+27.90%)</b></td><td>0.04 (-12.16%)</td><td>186.30 <b>(-21.82%)</b></td><td>162.20 (-9.75%)</td><td>169.80 (-4.66%)</td><td>121.80 (-9.84%)</td><td>26.05 <b>(-37.76%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>238.30 (n/a)</td><td>179.72 (n/a)</td><td>178.10 (n/a)</td><td>135.10 (n/a)</td><td>41.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (+19.19%)</td><td>0.21 (+5.26%)</td><td>0.19 (-4.99%)</td><td>0.18 (+7.96%)</td><td>0.04 <b>(+39.36%)</b></td><td>183.50 (-7.37%)</td><td>161.60 (-4.28%)</td><td>172.60 (+5.24%)</td><td>123.40 (-16.11%)</td><td>25.10 (+9.64%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>198.10 (n/a)</td><td>168.82 (n/a)</td><td>164.00 (n/a)</td><td>147.10 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 <b>(+38.53%)</b></td><td>0.21 (+9.30%)</td><td>0.20 (+3.14%)</td><td>0.15 (-15.27%)</td><td>0.05 <b>(+326.73%)</b></td><td>223.90 (+18.03%)</td><td>162.88 (-4.70%)</td><td>160.70 (-3.02%)</td><td>118.30 <b>(-27.82%)</b></td><td>39.15 <b>(+265.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>170.92 (n/a)</td><td>165.70 (n/a)</td><td>163.90 (n/a)</td><td>10.72 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (-0.10%)</td><td>0.18 (+0.02%)</td><td>0.18 (+0.09%)</td><td>0.18 (+0.20%)</td><td>0.00 <b>(-35.54%)</b></td><td>47655.20 (-0.20%)</td><td>47550.58 (-0.02%)</td><td>47517.90 (-0.09%)</td><td>47464.50 (+0.10%)</td><td>76.99 <b>(-35.59%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47748.40 (n/a)</td><td>47561.68 (n/a)</td><td>47560.80 (n/a)</td><td>47418.60 (n/a)</td><td>119.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (+0.01%)</td><td>0.18 (-0.22%)</td><td>0.18 (-0.24%)</td><td>0.18 (-0.25%)</td><td>0.00 <b>(+97.61%)</b></td><td>47700.80 (+0.25%)</td><td>47633.58 (+0.22%)</td><td>47667.90 (+0.24%)</td><td>47475.90 (-0.01%)</td><td>91.83 <b>(+98.01%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47582.70 (n/a)</td><td>47530.50 (n/a)</td><td>47552.20 (n/a)</td><td>47479.20 (n/a)</td><td>46.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (-0.01%)</td><td>0.11 (-0.02%)</td><td>0.11 (+0.03%)</td><td>0.11 (-0.05%)</td><td>0.00 (+18.22%)</td><td>375811.40 (+0.05%)</td><td>375571.50 (+0.02%)</td><td>375515.70 (-0.03%)</td><td>375315.20 (+0.01%)</td><td>201.78 (+18.28%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>375637.20 (n/a)</td><td>375506.92 (n/a)</td><td>375617.30 (n/a)</td><td>375287.30 (n/a)</td><td>170.60 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (+10.51%)</td><td>0.17 (+0.93%)</td><td>0.18 (+11.38%)</td><td>0.09 <b>(-26.04%)</b></td><td>0.05 <b>(+48.43%)</b></td><td>269.70 <b>(+35.19%)</b></td><td>158.38 (+5.36%)</td><td>134.70 (-10.20%)</td><td>109.90 (-9.55%)</td><td>63.75 <b>(+99.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>199.50 (n/a)</td><td>150.32 (n/a)</td><td>150.00 (n/a)</td><td>121.50 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.38 (-1.83%)</td><td>0.33 (-6.78%)</td><td>0.32 (-12.89%)</td><td>0.29 (-8.39%)</td><td>0.03 (+7.87%)</td><td>169.80 (+9.13%)</td><td>149.78 (+7.45%)</td><td>151.90 (+14.81%)</td><td>130.90 (+1.79%)</td><td>14.72 (+19.60%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.03 (n/a)</td><td>155.60 (n/a)</td><td>139.40 (n/a)</td><td>132.30 (n/a)</td><td>128.60 (n/a)</td><td>12.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.18 (-3.49%)</td><td>13.02 (-0.11%)</td><td>13.04 (+1.70%)</td><td>12.90 (+2.15%)</td><td>0.12 <b>(-71.58%)</b></td><td>812.80 (-2.11%)</td><td>805.50 (+0.03%)</td><td>804.20 (-1.68%)</td><td>795.60 (+3.62%)</td><td>7.34 <b>(-71.03%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.66 (n/a)</td><td>13.03 (n/a)</td><td>12.82 (n/a)</td><td>12.63 (n/a)</td><td>0.42 (n/a)</td><td>830.30 (n/a)</td><td>805.24 (n/a)</td><td>817.90 (n/a)</td><td>767.80 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.30 (+1.31%)</td><td>0.26 (+4.64%)</td><td>0.27 (+10.48%)</td><td>0.17 <b>(-23.14%)</b></td><td>0.05 <b>(+84.59%)</b></td><td>235.80 <b>(+30.13%)</b></td><td>162.20 (-1.23%)</td><td>151.30 (-9.46%)</td><td>134.30 (-1.32%)</td><td>42.02 <b>(+149.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>181.20 (n/a)</td><td>164.22 (n/a)</td><td>167.10 (n/a)</td><td>136.10 (n/a)</td><td>16.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-9.39%)</td><td>0.03 (-19.77%)</td><td>0.03 <b>(-20.24%)</b></td><td>0.02 <b>(-32.74%)</b></td><td>0.01 <b>(+48.35%)</b></td><td>241.70 <b>(+48.74%)</b></td><td>169.42 <b>(+28.56%)</b></td><td>157.00 <b>(+25.40%)</b></td><td>132.80 (+10.39%)</td><td>42.82 <b>(+146.36%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>162.50 (n/a)</td><td>131.78 (n/a)</td><td>125.20 (n/a)</td><td>120.30 (n/a)</td><td>17.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (+18.57%)</td><td>0.03 (-1.69%)</td><td>0.02 (-3.36%)</td><td>0.02 (-14.64%)</td><td>0.01 <b>(+129.97%)</b></td><td>200.10 (+17.15%)</td><td>164.56 (+5.26%)</td><td>166.10 (+3.42%)</td><td>110.60 (-15.70%)</td><td>34.71 <b>(+125.70%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.80 (n/a)</td><td>156.34 (n/a)</td><td>160.60 (n/a)</td><td>131.20 (n/a)</td><td>15.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (-19.44%)</td><td>0.03 (-14.91%)</td><td>0.04 (+2.86%)</td><td>0.02 <b>(-32.88%)</b></td><td>0.01 <b>(+29.28%)</b></td><td>285.60 <b>(+48.98%)</b></td><td>206.40 <b>(+21.61%)</b></td><td>170.40 (-2.80%)</td><td>164.00 <b>(+24.15%)</b></td><td>54.74 <b>(+139.93%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>169.72 (n/a)</td><td>175.30 (n/a)</td><td>132.10 (n/a)</td><td>22.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+4.21%)</td><td>0.03 (+4.00%)</td><td>0.03 (+6.82%)</td><td>0.02 (+8.50%)</td><td>0.00 (-11.24%)</td><td>200.90 (-7.84%)</td><td>157.48 (-4.73%)</td><td>154.30 (-6.37%)</td><td>127.10 (-4.00%)</td><td>28.29 (-19.08%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.00 (n/a)</td><td>165.30 (n/a)</td><td>164.80 (n/a)</td><td>132.40 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-13.04%)</td><td>0.03 (+1.39%)</td><td>0.03 (+1.80%)</td><td>0.03 <b>(+24.13%)</b></td><td>0.00 <b>(-53.97%)</b></td><td>193.70 (-19.43%)</td><td>175.94 (-4.09%)</td><td>170.30 (-1.79%)</td><td>156.80 (+14.96%)</td><td>16.79 <b>(-56.66%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>183.44 (n/a)</td><td>173.40 (n/a)</td><td>136.40 (n/a)</td><td>38.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+1.02%)</td><td>0.02 (-13.92%)</td><td>0.02 <b>(-27.47%)</b></td><td>0.02 <b>(-25.64%)</b></td><td>0.01 <b>(+81.29%)</b></td><td>262.30 <b>(+34.44%)</b></td><td>196.56 <b>(+21.29%)</b></td><td>208.20 <b>(+37.88%)</b></td><td>141.90 (-1.05%)</td><td>51.49 <b>(+131.98%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>162.06 (n/a)</td><td>151.00 (n/a)</td><td>143.40 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 <b>(+28.44%)</b></td><td>0.03 <b>(+26.53%)</b></td><td>0.03 (+3.97%)</td><td>0.03 <b>(+64.72%)</b></td><td>0.01 (-16.06%)</td><td>182.20 <b>(-39.29%)</b></td><td>155.26 <b>(-24.43%)</b></td><td>164.50 (-3.80%)</td><td>118.60 <b>(-22.13%)</b></td><td>25.18 <b>(-60.45%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>300.10 (n/a)</td><td>205.44 (n/a)</td><td>171.00 (n/a)</td><td>152.30 (n/a)</td><td>63.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 <b>(+27.85%)</b></td><td>0.02 (+10.04%)</td><td>0.02 (+2.33%)</td><td>0.02 (+7.45%)</td><td>0.01 <b>(+77.74%)</b></td><td>212.80 (-6.95%)</td><td>176.16 (-7.04%)</td><td>175.10 (-2.29%)</td><td>123.90 <b>(-21.78%)</b></td><td>37.55 <b>(+31.23%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>228.70 (n/a)</td><td>189.50 (n/a)</td><td>179.20 (n/a)</td><td>158.40 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 <b>(+47.04%)</b></td><td>0.03 <b>(+26.11%)</b></td><td>0.03 (+16.10%)</td><td>0.02 (+15.72%)</td><td>0.01 <b>(+86.11%)</b></td><td>219.80 (-13.57%)</td><td>152.58 (-18.01%)</td><td>150.90 (-13.87%)</td><td>94.90 <b>(-31.97%)</b></td><td>44.73 (+5.01%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.30 (n/a)</td><td>186.10 (n/a)</td><td>175.20 (n/a)</td><td>139.50 (n/a)</td><td>42.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 <b>(-32.03%)</b></td><td>0.02 (-8.76%)</td><td>0.02 (+0.03%)</td><td>0.02 (-6.10%)</td><td>0.00 <b>(-58.52%)</b></td><td>208.70 (+6.53%)</td><td>174.84 (+4.74%)</td><td>179.70 (-0.06%)</td><td>146.40 <b>(+47.14%)</b></td><td>25.88 <b>(-34.37%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>166.92 (n/a)</td><td>179.80 (n/a)</td><td>99.50 (n/a)</td><td>39.44 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-5.60%)</td><td>0.03 (-2.04%)</td><td>0.03 (-7.16%)</td><td>0.02 (+0.73%)</td><td>0.00 <b>(-24.74%)</b></td><td>216.30 (-0.73%)</td><td>178.28 (+1.24%)</td><td>176.20 (+7.70%)</td><td>158.80 (+5.94%)</td><td>23.32 <b>(-20.57%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.90 (n/a)</td><td>176.10 (n/a)</td><td>163.60 (n/a)</td><td>149.90 (n/a)</td><td>29.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-9.01%)</td><td>0.02 (-19.77%)</td><td>0.02 <b>(-24.12%)</b></td><td>0.01 <b>(-25.69%)</b></td><td>0.01 (+15.95%)</td><td>295.90 <b>(+34.62%)</b></td><td>209.16 <b>(+29.83%)</b></td><td>206.90 <b>(+31.78%)</b></td><td>123.60 (+9.87%)</td><td>64.71 <b>(+68.44%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>161.10 (n/a)</td><td>157.00 (n/a)</td><td>112.50 (n/a)</td><td>38.42 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 <b>(-21.16%)</b></td><td>0.02 <b>(-22.27%)</b></td><td>0.02 <b>(-24.68%)</b></td><td>0.02 <b>(-20.82%)</b></td><td>0.00 <b>(-23.39%)</b></td><td>244.50 <b>(+26.36%)</b></td><td>226.98 <b>(+28.62%)</b></td><td>231.40 <b>(+32.76%)</b></td><td>206.50 <b>(+26.84%)</b></td><td>15.44 <b>(+22.64%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.50 (n/a)</td><td>176.48 (n/a)</td><td>174.30 (n/a)</td><td>162.80 (n/a)</td><td>12.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-18.90%)</td><td>0.02 (-13.25%)</td><td>0.02 (-13.77%)</td><td>0.02 (-0.92%)</td><td>0.00 <b>(-39.98%)</b></td><td>216.60 (+0.93%)</td><td>187.54 (+13.26%)</td><td>179.80 (+15.93%)</td><td>155.80 <b>(+23.26%)</b></td><td>25.55 <b>(-24.61%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>165.58 (n/a)</td><td>155.10 (n/a)</td><td>126.40 (n/a)</td><td>33.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (-0.58%)</td><td>0.02 (-4.01%)</td><td>0.02 (-2.95%)</td><td>0.01 (-16.21%)</td><td>0.00 <b>(+22.11%)</b></td><td>311.70 (+19.38%)</td><td>233.52 (+5.59%)</td><td>228.40 (+3.07%)</td><td>188.90 (+0.59%)</td><td>47.85 <b>(+50.99%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>261.10 (n/a)</td><td>221.16 (n/a)</td><td>221.60 (n/a)</td><td>187.80 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (-6.38%)</td><td>0.02 (-4.42%)</td><td>0.02 (-0.61%)</td><td>0.01 (-16.70%)</td><td>0.00 (+11.82%)</td><td>310.60 <b>(+20.02%)</b></td><td>235.40 (+5.65%)</td><td>224.90 (+0.58%)</td><td>193.70 (+6.84%)</td><td>44.79 <b>(+48.13%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.80 (n/a)</td><td>222.82 (n/a)</td><td>223.60 (n/a)</td><td>181.30 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+3.24%)</td><td>0.05 (-10.27%)</td><td>0.05 (-15.82%)</td><td>0.04 (-9.86%)</td><td>0.01 <b>(+39.15%)</b></td><td>191.10 (+10.98%)</td><td>170.02 (+12.84%)</td><td>175.60 (+18.81%)</td><td>123.90 (-3.13%)</td><td>26.91 <b>(+44.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.20 (n/a)</td><td>150.68 (n/a)</td><td>147.80 (n/a)</td><td>127.90 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (-10.67%)</td><td>0.07 (+9.58%)</td><td>0.08 (+6.72%)</td><td>0.06 <b>(+52.45%)</b></td><td>0.01 <b>(-65.04%)</b></td><td>197.60 <b>(-34.40%)</b></td><td>168.78 (-14.46%)</td><td>161.40 (-6.27%)</td><td>157.80 (+11.91%)</td><td>16.37 <b>(-74.46%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>301.20 (n/a)</td><td>197.30 (n/a)</td><td>172.20 (n/a)</td><td>141.00 (n/a)</td><td>64.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (-2.58%)</td><td>0.05 (+3.25%)</td><td>0.05 (+8.36%)</td><td>0.04 (+3.48%)</td><td>0.01 (-15.94%)</td><td>206.00 (-3.38%)</td><td>162.58 (-4.31%)</td><td>165.30 (-7.76%)</td><td>124.00 (+2.65%)</td><td>30.76 (-16.17%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>169.90 (n/a)</td><td>179.20 (n/a)</td><td>120.80 (n/a)</td><td>36.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (-16.77%)</td><td>0.06 (+4.33%)</td><td>0.06 (+8.99%)</td><td>0.06 <b>(+40.59%)</b></td><td>0.00 <b>(-71.39%)</b></td><td>182.60 <b>(-28.89%)</b></td><td>167.20 (-9.11%)</td><td>166.50 (-8.26%)</td><td>154.90 <b>(+20.08%)</b></td><td>12.12 <b>(-75.64%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>256.80 (n/a)</td><td>183.96 (n/a)</td><td>181.50 (n/a)</td><td>129.00 (n/a)</td><td>49.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+9.37%)</td><td>0.06 (+14.39%)</td><td>0.06 <b>(+23.64%)</b></td><td>0.04 (+3.39%)</td><td>0.01 <b>(+39.73%)</b></td><td>187.80 (-3.30%)</td><td>147.86 (-11.29%)</td><td>140.70 (-19.14%)</td><td>118.50 (-8.56%)</td><td>31.71 <b>(+21.60%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.20 (n/a)</td><td>166.68 (n/a)</td><td>174.00 (n/a)</td><td>129.60 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (+2.62%)</td><td>0.07 (+5.34%)</td><td>0.06 (+7.34%)</td><td>0.05 (+9.36%)</td><td>0.01 <b>(-25.06%)</b></td><td>190.00 (-8.57%)</td><td>159.82 (-6.81%)</td><td>165.20 (-6.88%)</td><td>127.70 (-2.59%)</td><td>23.58 <b>(-33.87%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>171.50 (n/a)</td><td>177.40 (n/a)</td><td>131.10 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+10.79%)</td><td>0.05 (+2.88%)</td><td>0.05 (-7.95%)</td><td>0.04 (+8.48%)</td><td>0.01 <b>(+41.95%)</b></td><td>210.90 (-7.82%)</td><td>165.06 (-0.73%)</td><td>170.50 (+8.60%)</td><td>118.10 (-9.71%)</td><td>42.35 (+12.98%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.80 (n/a)</td><td>166.28 (n/a)</td><td>157.00 (n/a)</td><td>130.80 (n/a)</td><td>37.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (-16.86%)</td><td>0.06 (+4.90%)</td><td>0.06 <b>(+26.83%)</b></td><td>0.05 (+17.47%)</td><td>0.01 <b>(-62.58%)</b></td><td>185.70 (-14.86%)</td><td>162.68 (-9.38%)</td><td>158.70 <b>(-21.16%)</b></td><td>145.50 <b>(+20.25%)</b></td><td>16.98 <b>(-62.72%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>218.10 (n/a)</td><td>179.52 (n/a)</td><td>201.30 (n/a)</td><td>121.00 (n/a)</td><td>45.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (-18.12%)</td><td>0.05 (-0.42%)</td><td>0.04 (-2.02%)</td><td>0.03 (-0.18%)</td><td>0.01 <b>(-20.42%)</b></td><td>238.40 (+0.17%)</td><td>182.36 (-1.11%)</td><td>203.00 (+2.06%)</td><td>130.60 <b>(+22.06%)</b></td><td>47.90 (-2.39%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>238.00 (n/a)</td><td>184.40 (n/a)</td><td>198.90 (n/a)</td><td>107.00 (n/a)</td><td>49.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+11.51%)</td><td>0.06 <b>(+21.82%)</b></td><td>0.06 (+13.52%)</td><td>0.05 <b>(+59.44%)</b></td><td>0.01 <b>(-28.88%)</b></td><td>193.80 <b>(-37.30%)</b></td><td>163.14 <b>(-22.37%)</b></td><td>162.70 (-11.91%)</td><td>125.10 (-10.32%)</td><td>26.49 <b>(-60.98%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>309.10 (n/a)</td><td>210.16 (n/a)</td><td>184.70 (n/a)</td><td>139.50 (n/a)</td><td>67.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (+12.58%)</td><td>0.05 (+17.49%)</td><td>0.05 <b>(+32.83%)</b></td><td>0.04 (+2.15%)</td><td>0.01 <b>(+38.20%)</b></td><td>227.60 (-2.11%)</td><td>178.82 (-13.41%)</td><td>161.10 <b>(-24.68%)</b></td><td>135.10 (-11.18%)</td><td>40.36 <b>(+28.14%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.50 (n/a)</td><td>206.52 (n/a)</td><td>213.90 (n/a)</td><td>152.10 (n/a)</td><td>31.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (+9.98%)</td><td>0.05 (+8.98%)</td><td>0.05 (+5.64%)</td><td>0.04 (+12.09%)</td><td>0.00 <b>(+21.30%)</b></td><td>216.90 (-10.78%)</td><td>193.54 (-8.14%)</td><td>191.50 (-5.34%)</td><td>174.90 (-9.05%)</td><td>18.92 (-3.82%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>243.10 (n/a)</td><td>210.68 (n/a)</td><td>202.30 (n/a)</td><td>192.30 (n/a)</td><td>19.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (+6.13%)</td><td>0.04 (-3.98%)</td><td>0.04 (-6.36%)</td><td>0.03 (-18.49%)</td><td>0.02 <b>(+35.91%)</b></td><td>310.40 <b>(+22.69%)</b></td><td>215.36 (+9.41%)</td><td>211.60 (+6.76%)</td><td>125.70 (-5.77%)</td><td>70.92 <b>(+58.93%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.00 (n/a)</td><td>196.84 (n/a)</td><td>198.20 (n/a)</td><td>133.40 (n/a)</td><td>44.63 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 <b>(-22.54%)</b></td><td>0.05 (-0.06%)</td><td>0.04 (+3.39%)</td><td>0.04 <b>(+29.28%)</b></td><td>0.00 <b>(-75.61%)</b></td><td>204.50 <b>(-22.66%)</b></td><td>192.26 (-4.40%)</td><td>197.40 (-3.28%)</td><td>176.90 <b>(+29.12%)</b></td><td>11.76 <b>(-75.30%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>264.40 (n/a)</td><td>201.10 (n/a)</td><td>204.10 (n/a)</td><td>137.00 (n/a)</td><td>47.64 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (+6.21%)</td><td>0.04 (+7.19%)</td><td>0.04 (+13.44%)</td><td>0.03 (-4.80%)</td><td>0.01 <b>(+27.55%)</b></td><td>327.00 (+5.04%)</td><td>241.00 (-5.58%)</td><td>210.00 (-11.84%)</td><td>204.40 (-5.85%)</td><td>52.58 <b>(+25.21%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.30 (n/a)</td><td>255.24 (n/a)</td><td>238.20 (n/a)</td><td>217.10 (n/a)</td><td>41.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (-14.84%)</td><td>0.10 (+5.65%)</td><td>0.11 <b>(+22.28%)</b></td><td>0.09 <b>(+20.06%)</b></td><td>0.01 <b>(-52.21%)</b></td><td>180.60 (-16.70%)</td><td>161.48 (-7.95%)</td><td>152.30 (-18.21%)</td><td>144.30 (+17.41%)</td><td>17.26 <b>(-50.84%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.80 (n/a)</td><td>175.42 (n/a)</td><td>186.20 (n/a)</td><td>122.90 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.20 <b>(+23.17%)</b></td><td>0.17 <b>(+24.12%)</b></td><td>0.16 (+16.33%)</td><td>0.15 <b>(+35.93%)</b></td><td>0.02 (-6.51%)</td><td>169.10 <b>(-26.41%)</b></td><td>149.24 <b>(-20.18%)</b></td><td>153.80 (-14.03%)</td><td>125.10 (-18.82%)</td><td>16.17 <b>(-45.36%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>229.80 (n/a)</td><td>186.98 (n/a)</td><td>178.90 (n/a)</td><td>154.10 (n/a)</td><td>29.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (+5.42%)</td><td>0.09 (+6.93%)</td><td>0.09 (+5.18%)</td><td>0.09 (+15.33%)</td><td>0.01 <b>(-30.38%)</b></td><td>190.30 (-13.26%)</td><td>173.64 (-6.97%)</td><td>175.30 (-4.93%)</td><td>159.60 (-5.11%)</td><td>11.56 <b>(-42.95%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.40 (n/a)</td><td>186.64 (n/a)</td><td>184.40 (n/a)</td><td>168.20 (n/a)</td><td>20.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (+19.37%)</td><td>0.14 <b>(+25.18%)</b></td><td>0.13 <b>(+25.40%)</b></td><td>0.12 <b>(+23.40%)</b></td><td>0.02 (+13.74%)</td><td>177.90 (-18.95%)</td><td>153.20 <b>(-20.30%)</b></td><td>159.60 <b>(-20.28%)</b></td><td>120.90 (-16.22%)</td><td>23.00 <b>(-21.20%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>219.50 (n/a)</td><td>192.22 (n/a)</td><td>200.20 (n/a)</td><td>144.30 (n/a)</td><td>29.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (-9.67%)</td><td>0.08 (-11.84%)</td><td>0.09 (-10.66%)</td><td>0.05 <b>(-29.69%)</b></td><td>0.02 (+8.83%)</td><td>321.80 <b>(+42.20%)</b></td><td>207.50 (+17.05%)</td><td>191.70 (+11.97%)</td><td>147.40 (+10.66%)</td><td>66.52 <b>(+81.64%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.30 (n/a)</td><td>177.28 (n/a)</td><td>171.20 (n/a)</td><td>133.20 (n/a)</td><td>36.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (+11.96%)</td><td>0.12 (+0.04%)</td><td>0.13 (+8.12%)</td><td>0.10 (-4.60%)</td><td>0.03 <b>(+75.26%)</b></td><td>209.10 (+4.86%)</td><td>170.92 (+2.21%)</td><td>155.40 (-7.50%)</td><td>130.10 (-10.71%)</td><td>35.05 <b>(+70.53%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>167.22 (n/a)</td><td>168.00 (n/a)</td><td>145.70 (n/a)</td><td>20.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 <b>(-23.05%)</b></td><td>0.09 (-9.53%)</td><td>0.10 (-1.90%)</td><td>0.08 (+8.14%)</td><td>0.01 <b>(-67.74%)</b></td><td>197.10 (-7.55%)</td><td>175.08 (+7.21%)</td><td>170.10 (+1.92%)</td><td>161.60 <b>(+30.01%)</b></td><td>13.64 <b>(-60.53%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.20 (n/a)</td><td>163.30 (n/a)</td><td>166.90 (n/a)</td><td>124.30 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 <b>(-22.71%)</b></td><td>0.12 (+0.20%)</td><td>0.12 (+7.70%)</td><td>0.10 (+13.80%)</td><td>0.02 <b>(-50.09%)</b></td><td>177.90 (-12.15%)</td><td>152.60 (-5.18%)</td><td>154.40 (-7.16%)</td><td>120.20 <b>(+29.39%)</b></td><td>25.55 <b>(-39.45%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>202.50 (n/a)</td><td>160.94 (n/a)</td><td>166.30 (n/a)</td><td>92.90 (n/a)</td><td>42.19 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (-14.70%)</td><td>0.10 (+5.47%)</td><td>0.10 <b>(+25.39%)</b></td><td>0.07 (-7.76%)</td><td>0.02 <b>(-30.09%)</b></td><td>230.50 (+8.42%)</td><td>172.24 (-6.51%)</td><td>161.40 <b>(-20.26%)</b></td><td>143.30 (+17.27%)</td><td>34.37 (-6.39%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.60 (n/a)</td><td>184.24 (n/a)</td><td>202.40 (n/a)</td><td>122.20 (n/a)</td><td>36.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (-6.51%)</td><td>0.12 (+2.84%)</td><td>0.12 (+15.13%)</td><td>0.10 <b>(+49.62%)</b></td><td>0.02 <b>(-56.68%)</b></td><td>175.80 <b>(-33.16%)</b></td><td>157.88 (-9.72%)</td><td>157.70 (-13.16%)</td><td>128.00 (+7.02%)</td><td>19.46 <b>(-67.03%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>263.00 (n/a)</td><td>174.88 (n/a)</td><td>181.60 (n/a)</td><td>119.60 (n/a)</td><td>59.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 <b>(-25.57%)</b></td><td>0.09 (-17.85%)</td><td>0.09 <b>(-20.79%)</b></td><td>0.08 (-2.53%)</td><td>0.01 <b>(-63.07%)</b></td><td>204.50 (+2.61%)</td><td>187.96 (+19.19%)</td><td>186.60 <b>(+26.25%)</b></td><td>166.20 <b>(+34.36%)</b></td><td>14.46 <b>(-49.90%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.30 (n/a)</td><td>157.70 (n/a)</td><td>147.80 (n/a)</td><td>123.70 (n/a)</td><td>28.87 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 <b>(-23.12%)</b></td><td>0.09 (-10.02%)</td><td>0.09 (+1.20%)</td><td>0.05 <b>(-30.96%)</b></td><td>0.03 <b>(-24.53%)</b></td><td>344.10 <b>(+44.88%)</b></td><td>204.94 (+12.64%)</td><td>186.00 (-1.22%)</td><td>131.00 <b>(+30.09%)</b></td><td>82.13 <b>(+56.36%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>237.50 (n/a)</td><td>181.94 (n/a)</td><td>188.30 (n/a)</td><td>100.70 (n/a)</td><td>52.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (-5.77%)</td><td>0.09 (-7.33%)</td><td>0.08 (-19.67%)</td><td>0.08 <b>(+34.32%)</b></td><td>0.01 <b>(-54.00%)</b></td><td>211.00 <b>(-25.55%)</b></td><td>188.66 (+2.86%)</td><td>193.80 <b>(+24.47%)</b></td><td>159.20 (+6.13%)</td><td>20.16 <b>(-64.52%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>283.40 (n/a)</td><td>183.42 (n/a)</td><td>155.70 (n/a)</td><td>150.00 (n/a)</td><td>56.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 <b>(+74.70%)</b></td><td>0.11 <b>(+47.04%)</b></td><td>0.11 <b>(+41.31%)</b></td><td>0.08 <b>(+58.09%)</b></td><td>0.03 <b>(+97.75%)</b></td><td>211.70 <b>(-36.73%)</b></td><td>161.78 <b>(-31.24%)</b></td><td>153.90 <b>(-29.24%)</b></td><td>110.00 <b>(-42.74%)</b></td><td>37.93 <b>(-32.93%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>334.60 (n/a)</td><td>235.28 (n/a)</td><td>217.50 (n/a)</td><td>192.10 (n/a)</td><td>56.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (-3.23%)</td><td>0.08 (+6.38%)</td><td>0.08 <b>(+24.25%)</b></td><td>0.05 (+2.86%)</td><td>0.02 <b>(-21.27%)</b></td><td>334.20 (-2.79%)</td><td>226.96 (-8.20%)</td><td>198.80 (-19.51%)</td><td>177.30 (+3.32%)</td><td>62.98 (-15.10%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>343.80 (n/a)</td><td>247.24 (n/a)</td><td>247.00 (n/a)</td><td>171.60 (n/a)</td><td>74.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (-15.78%)</td><td>0.18 (-10.02%)</td><td>0.18 (-11.44%)</td><td>0.15 (+2.57%)</td><td>0.02 <b>(-45.50%)</b></td><td>221.60 (-2.51%)</td><td>186.50 (+9.31%)</td><td>180.10 (+12.92%)</td><td>168.80 (+18.71%)</td><td>20.34 <b>(-37.99%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>227.30 (n/a)</td><td>170.62 (n/a)</td><td>159.50 (n/a)</td><td>142.20 (n/a)</td><td>32.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (+8.40%)</td><td>0.18 (-7.11%)</td><td>0.16 <b>(-21.79%)</b></td><td>0.11 (+1.98%)</td><td>0.06 (+10.87%)</td><td>310.70 (-1.93%)</td><td>202.46 (+8.20%)</td><td>204.60 <b>(+27.87%)</b></td><td>126.20 (-7.68%)</td><td>72.26 (-3.38%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>316.80 (n/a)</td><td>187.12 (n/a)</td><td>160.00 (n/a)</td><td>136.70 (n/a)</td><td>74.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.33 <b>(+23.67%)</b></td><td>0.24 (+12.98%)</td><td>0.22 (+5.18%)</td><td>0.20 <b>(+22.57%)</b></td><td>0.05 <b>(+30.58%)</b></td><td>202.40 (-18.42%)</td><td>176.10 (-11.20%)</td><td>187.50 (-4.97%)</td><td>123.70 (-19.15%)</td><td>32.06 (-14.84%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>248.10 (n/a)</td><td>198.30 (n/a)</td><td>197.30 (n/a)</td><td>153.00 (n/a)</td><td>37.64 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 <b>(-25.22%)</b></td><td>0.16 <b>(-27.08%)</b></td><td>0.17 <b>(-22.11%)</b></td><td>0.10 <b>(-46.55%)</b></td><td>0.04 (+9.20%)</td><td>320.60 <b>(+87.05%)</b></td><td>212.12 <b>(+42.06%)</b></td><td>197.00 <b>(+28.42%)</b></td><td>169.00 <b>(+33.70%)</b></td><td>61.92 <b>(+187.84%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>171.40 (n/a)</td><td>149.32 (n/a)</td><td>153.40 (n/a)</td><td>126.40 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (-6.47%)</td><td>0.24 (+2.64%)</td><td>0.24 (+3.62%)</td><td>0.22 <b>(+21.82%)</b></td><td>0.02 <b>(-49.66%)</b></td><td>185.90 (-17.89%)</td><td>170.32 (-4.85%)</td><td>172.50 (-3.52%)</td><td>151.20 (+6.93%)</td><td>15.95 <b>(-54.74%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>226.40 (n/a)</td><td>179.00 (n/a)</td><td>178.80 (n/a)</td><td>141.40 (n/a)</td><td>35.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (-13.11%)</td><td>0.17 (-10.89%)</td><td>0.15 <b>(-24.76%)</b></td><td>0.15 <b>(+40.31%)</b></td><td>0.04 <b>(-40.50%)</b></td><td>221.80 <b>(-28.73%)</b></td><td>198.94 (+4.65%)</td><td>219.30 <b>(+32.91%)</b></td><td>141.10 (+15.09%)</td><td>34.73 <b>(-52.81%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>311.20 (n/a)</td><td>190.10 (n/a)</td><td>165.00 (n/a)</td><td>122.60 (n/a)</td><td>73.60 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.37 <b>(+58.22%)</b></td><td>0.24 (+15.89%)</td><td>0.22 (+4.92%)</td><td>0.18 (+8.54%)</td><td>0.07 <b>(+199.43%)</b></td><td>200.40 (-7.86%)</td><td>161.94 (-9.58%)</td><td>166.30 (-4.70%)</td><td>99.30 <b>(-36.79%)</b></td><td>38.33 <b>(+63.53%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>217.50 (n/a)</td><td>179.10 (n/a)</td><td>174.50 (n/a)</td><td>157.10 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (-5.43%)</td><td>0.20 (-8.19%)</td><td>0.20 (-16.61%)</td><td>0.17 (+2.72%)</td><td>0.04 (-19.69%)</td><td>197.00 (-2.67%)</td><td>166.84 (+7.44%)</td><td>167.80 (+19.86%)</td><td>125.20 (+5.74%)</td><td>28.12 (-19.39%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>202.40 (n/a)</td><td>155.28 (n/a)</td><td>140.00 (n/a)</td><td>118.40 (n/a)</td><td>34.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (-14.66%)</td><td>0.22 (-0.13%)</td><td>0.23 (+2.39%)</td><td>0.18 <b>(+33.83%)</b></td><td>0.03 <b>(-47.16%)</b></td><td>208.40 <b>(-25.28%)</b></td><td>170.02 (-5.31%)</td><td>159.80 (-2.38%)</td><td>142.40 (+17.20%)</td><td>26.60 <b>(-55.36%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>278.90 (n/a)</td><td>179.56 (n/a)</td><td>163.70 (n/a)</td><td>121.50 (n/a)</td><td>59.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (-14.30%)</td><td>0.18 (-7.47%)</td><td>0.18 (-7.20%)</td><td>0.14 (-6.19%)</td><td>0.03 <b>(-31.42%)</b></td><td>237.30 (+6.60%)</td><td>189.64 (+6.31%)</td><td>178.40 (+7.73%)</td><td>152.30 (+16.70%)</td><td>32.43 (-16.37%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>222.60 (n/a)</td><td>178.38 (n/a)</td><td>165.60 (n/a)</td><td>130.50 (n/a)</td><td>38.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (+7.31%)</td><td>0.18 (+1.18%)</td><td>0.19 (+5.69%)</td><td>0.11 <b>(-25.43%)</b></td><td>0.04 <b>(+103.18%)</b></td><td>304.30 <b>(+34.11%)</b></td><td>200.50 (+3.41%)</td><td>182.80 (-5.38%)</td><td>157.70 (-6.80%)</td><td>60.07 <b>(+161.35%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>226.90 (n/a)</td><td>193.88 (n/a)</td><td>193.20 (n/a)</td><td>169.20 (n/a)</td><td>22.98 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.24 (+4.28%)</td><td>0.22 (+19.32%)</td><td>0.21 <b>(+26.81%)</b></td><td>0.20 <b>(+32.46%)</b></td><td>0.02 <b>(-44.03%)</b></td><td>162.90 <b>(-24.48%)</b></td><td>151.22 (-17.98%)</td><td>156.90 <b>(-21.16%)</b></td><td>134.20 (-4.14%)</td><td>13.38 <b>(-59.34%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>215.70 (n/a)</td><td>184.36 (n/a)</td><td>199.00 (n/a)</td><td>140.00 (n/a)</td><td>32.91 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (+10.86%)</td><td>0.17 (+4.01%)</td><td>0.20 (+16.74%)</td><td>0.10 <b>(-31.19%)</b></td><td>0.05 <b>(+145.04%)</b></td><td>338.50 <b>(+45.34%)</b></td><td>215.30 (+2.54%)</td><td>176.10 (-14.35%)</td><td>160.20 (-9.80%)</td><td>73.45 <b>(+223.22%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>209.96 (n/a)</td><td>205.60 (n/a)</td><td>177.60 (n/a)</td><td>22.72 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 <b>(+30.72%)</b></td><td>0.17 (+5.67%)</td><td>0.16 (-0.66%)</td><td>0.13 (-4.25%)</td><td>0.04 <b>(+179.13%)</b></td><td>248.30 (+4.46%)</td><td>202.04 (-2.85%)</td><td>206.50 (+0.68%)</td><td>146.50 <b>(-23.50%)</b></td><td>38.07 <b>(+115.16%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>207.96 (n/a)</td><td>205.10 (n/a)</td><td>191.50 (n/a)</td><td>17.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (-19.95%)</td><td>0.12 (-9.67%)</td><td>0.12 (-4.77%)</td><td>0.11 (-2.44%)</td><td>0.01 <b>(-47.28%)</b></td><td>187.80 (+2.51%)</td><td>167.58 (+9.02%)</td><td>169.60 (+5.02%)</td><td>149.10 <b>(+24.98%)</b></td><td>17.40 <b>(-32.88%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>183.20 (n/a)</td><td>153.72 (n/a)</td><td>161.50 (n/a)</td><td>119.30 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (+5.77%)</td><td>0.11 (-2.14%)</td><td>0.12 (-3.04%)</td><td>0.09 (+15.20%)</td><td>0.02 (-9.59%)</td><td>235.10 (-13.22%)</td><td>186.32 (+0.71%)</td><td>173.50 (+3.15%)</td><td>146.10 (-5.50%)</td><td>35.70 <b>(-26.77%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>270.90 (n/a)</td><td>185.00 (n/a)</td><td>168.20 (n/a)</td><td>154.60 (n/a)</td><td>48.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (-10.40%)</td><td>0.12 (-11.22%)</td><td>0.12 (-17.53%)</td><td>0.11 (+0.69%)</td><td>0.01 <b>(-36.08%)</b></td><td>187.90 (-0.69%)</td><td>173.28 (+11.52%)</td><td>177.50 <b>(+21.24%)</b></td><td>147.10 (+11.61%)</td><td>17.17 <b>(-28.84%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.20 (n/a)</td><td>155.38 (n/a)</td><td>146.40 (n/a)</td><td>131.80 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 <b>(-26.89%)</b></td><td>0.11 (-19.16%)</td><td>0.11 (-11.66%)</td><td>0.10 (-14.23%)</td><td>0.01 <b>(-61.43%)</b></td><td>210.60 (+16.55%)</td><td>187.70 <b>(+21.99%)</b></td><td>180.70 (+13.22%)</td><td>176.60 <b>(+36.79%)</b></td><td>14.40 <b>(-37.25%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>180.70 (n/a)</td><td>153.86 (n/a)</td><td>159.60 (n/a)</td><td>129.10 (n/a)</td><td>22.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (-3.10%)</td><td>0.15 (+17.55%)</td><td>0.15 <b>(+32.64%)</b></td><td>0.12 <b>(+24.43%)</b></td><td>0.02 <b>(-46.89%)</b></td><td>167.90 (-19.63%)</td><td>138.34 (-18.19%)</td><td>135.60 <b>(-24.58%)</b></td><td>122.90 (+3.19%)</td><td>17.96 <b>(-56.12%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>208.90 (n/a)</td><td>169.10 (n/a)</td><td>179.80 (n/a)</td><td>119.10 (n/a)</td><td>40.92 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (+0.11%)</td><td>0.14 (+12.36%)</td><td>0.14 <b>(+33.26%)</b></td><td>0.12 (+11.84%)</td><td>0.02 <b>(-43.73%)</b></td><td>171.20 (-10.55%)</td><td>143.32 (-13.36%)</td><td>142.30 <b>(-24.95%)</b></td><td>127.20 (-0.16%)</td><td>17.35 <b>(-49.43%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>191.40 (n/a)</td><td>165.42 (n/a)</td><td>189.60 (n/a)</td><td>127.40 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (-3.36%)</td><td>0.11 (+9.75%)</td><td>0.11 (+15.30%)</td><td>0.10 <b>(+40.29%)</b></td><td>0.01 <b>(-46.31%)</b></td><td>209.60 <b>(-28.71%)</b></td><td>184.86 (-12.13%)</td><td>181.40 (-13.25%)</td><td>158.40 (+3.46%)</td><td>20.81 <b>(-60.66%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>294.00 (n/a)</td><td>210.38 (n/a)</td><td>209.10 (n/a)</td><td>153.10 (n/a)</td><td>52.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (+0.16%)</td><td>0.12 <b>(+23.25%)</b></td><td>0.12 <b>(+22.45%)</b></td><td>0.10 <b>(+40.20%)</b></td><td>0.01 <b>(-44.59%)</b></td><td>199.00 <b>(-28.65%)</b></td><td>171.72 <b>(-21.26%)</b></td><td>173.80 (-18.33%)</td><td>154.50 (-0.19%)</td><td>18.26 <b>(-60.57%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>278.90 (n/a)</td><td>218.08 (n/a)</td><td>212.80 (n/a)</td><td>154.80 (n/a)</td><td>46.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (-4.32%)</td><td>0.15 (-2.83%)</td><td>0.15 (+4.98%)</td><td>0.13 (+5.28%)</td><td>0.02 <b>(-32.77%)</b></td><td>183.00 (-4.98%)</td><td>166.00 (+1.52%)</td><td>166.10 (-4.70%)</td><td>135.60 (+4.47%)</td><td>18.77 <b>(-33.13%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.60 (n/a)</td><td>163.52 (n/a)</td><td>174.30 (n/a)</td><td>129.80 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (-17.13%)</td><td>0.14 (-13.36%)</td><td>0.14 (-8.45%)</td><td>0.11 (-5.96%)</td><td>0.02 <b>(-35.39%)</b></td><td>215.00 (+6.33%)</td><td>177.50 (+13.68%)</td><td>171.50 (+9.24%)</td><td>145.00 <b>(+20.63%)</b></td><td>27.24 (-15.80%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>202.20 (n/a)</td><td>156.14 (n/a)</td><td>157.00 (n/a)</td><td>120.20 (n/a)</td><td>32.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (-0.69%)</td><td>0.15 (+2.78%)</td><td>0.15 (+8.48%)</td><td>0.10 (-14.61%)</td><td>0.03 <b>(+21.42%)</b></td><td>239.00 (+17.10%)</td><td>170.82 (-0.99%)</td><td>167.60 (-7.81%)</td><td>134.10 (+0.68%)</td><td>41.36 <b>(+46.28%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>204.10 (n/a)</td><td>172.52 (n/a)</td><td>181.80 (n/a)</td><td>133.20 (n/a)</td><td>28.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 <b>(+22.00%)</b></td><td>0.18 (+10.95%)</td><td>0.17 (+14.02%)</td><td>0.14 (+2.86%)</td><td>0.03 <b>(+39.17%)</b></td><td>172.90 (-2.81%)</td><td>141.98 (-9.06%)</td><td>144.20 (-12.29%)</td><td>106.20 (-18.06%)</td><td>25.14 (+9.79%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>177.90 (n/a)</td><td>156.12 (n/a)</td><td>164.40 (n/a)</td><td>129.60 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (+12.48%)</td><td>0.13 (-6.39%)</td><td>0.15 (-0.14%)</td><td>0.07 <b>(-41.57%)</b></td><td>0.04 <b>(+147.78%)</b></td><td>368.10 <b>(+71.13%)</b></td><td>213.22 (+19.12%)</td><td>167.50 (+0.12%)</td><td>141.50 (-11.06%)</td><td>93.94 <b>(+283.47%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>179.00 (n/a)</td><td>167.30 (n/a)</td><td>159.10 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (+12.82%)</td><td>0.16 (+16.56%)</td><td>0.14 (+2.93%)</td><td>0.12 (+17.43%)</td><td>0.04 <b>(+21.04%)</b></td><td>197.50 (-14.83%)</td><td>160.30 (-13.75%)</td><td>174.70 (-2.84%)</td><td>114.00 (-11.35%)</td><td>36.44 (-7.53%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>231.90 (n/a)</td><td>185.86 (n/a)</td><td>179.80 (n/a)</td><td>128.60 (n/a)</td><td>39.40 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (-18.26%)</td><td>0.14 (-5.84%)</td><td>0.13 (-0.21%)</td><td>0.11 (+9.63%)</td><td>0.03 <b>(-39.11%)</b></td><td>219.20 (-8.78%)</td><td>185.52 (+1.77%)</td><td>193.30 (+0.26%)</td><td>130.00 <b>(+22.30%)</b></td><td>34.77 <b>(-30.22%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>240.30 (n/a)</td><td>182.30 (n/a)</td><td>192.80 (n/a)</td><td>106.30 (n/a)</td><td>49.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 <b>(-25.54%)</b></td><td>0.12 (-11.06%)</td><td>0.12 (-8.80%)</td><td>0.11 (+10.22%)</td><td>0.01 <b>(-61.17%)</b></td><td>218.50 (-9.26%)</td><td>202.98 (+8.45%)</td><td>213.30 (+9.67%)</td><td>169.30 <b>(+34.26%)</b></td><td>20.25 <b>(-51.20%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>240.80 (n/a)</td><td>187.16 (n/a)</td><td>194.50 (n/a)</td><td>126.10 (n/a)</td><td>41.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 <b>(+33.46%)</b></td><td>0.11 (+10.60%)</td><td>0.12 (+13.86%)</td><td>0.08 (-8.29%)</td><td>0.03 <b>(+174.40%)</b></td><td>230.70 (+9.03%)</td><td>171.04 (-5.17%)</td><td>159.70 (-12.20%)</td><td>120.00 <b>(-25.09%)</b></td><td>45.89 <b>(+127.44%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>180.36 (n/a)</td><td>181.90 (n/a)</td><td>160.20 (n/a)</td><td>20.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 <b>(+76.27%)</b></td><td>0.11 (+11.87%)</td><td>0.10 (-2.45%)</td><td>0.08 (-8.13%)</td><td>0.04 <b>(+482.83%)</b></td><td>224.90 (+8.86%)</td><td>175.10 (-3.46%)</td><td>181.10 (+2.49%)</td><td>97.80 <b>(-43.27%)</b></td><td>47.08 <b>(+231.27%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>181.38 (n/a)</td><td>176.70 (n/a)</td><td>172.40 (n/a)</td><td>14.21 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (+5.71%)</td><td>0.11 (+0.50%)</td><td>0.11 (+3.81%)</td><td>0.09 (-9.60%)</td><td>0.02 <b>(+84.14%)</b></td><td>207.30 (+10.62%)</td><td>169.10 (+1.37%)</td><td>161.10 (-3.65%)</td><td>138.00 (-5.41%)</td><td>30.68 <b>(+93.82%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>187.40 (n/a)</td><td>166.82 (n/a)</td><td>167.20 (n/a)</td><td>145.90 (n/a)</td><td>15.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (+5.22%)</td><td>0.11 (-3.72%)</td><td>0.10 (-8.57%)</td><td>0.09 (-5.15%)</td><td>0.02 <b>(+30.86%)</b></td><td>208.40 (+5.47%)</td><td>170.46 (+5.13%)</td><td>180.60 (+9.32%)</td><td>127.20 (-4.93%)</td><td>31.54 <b>(+29.57%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>197.60 (n/a)</td><td>162.14 (n/a)</td><td>165.20 (n/a)</td><td>133.80 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (+12.02%)</td><td>0.10 (+8.40%)</td><td>0.10 (+9.49%)</td><td>0.08 (-10.03%)</td><td>0.02 <b>(+135.00%)</b></td><td>236.50 (+11.14%)</td><td>187.32 (-6.19%)</td><td>184.80 (-8.65%)</td><td>159.00 (-10.72%)</td><td>31.29 <b>(+133.58%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>199.68 (n/a)</td><td>202.30 (n/a)</td><td>178.10 (n/a)</td><td>13.40 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (-4.80%)</td><td>0.11 (+8.45%)</td><td>0.11 (+12.27%)</td><td>0.09 (+17.24%)</td><td>0.02 <b>(-26.13%)</b></td><td>213.30 (-14.68%)</td><td>172.66 (-9.81%)</td><td>172.90 (-10.92%)</td><td>135.80 (+5.03%)</td><td>29.59 <b>(-31.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>250.00 (n/a)</td><td>191.44 (n/a)</td><td>194.10 (n/a)</td><td>129.30 (n/a)</td><td>43.42 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (+0.94%)</td><td>0.10 (+4.64%)</td><td>0.11 (+7.79%)</td><td>0.09 (+6.98%)</td><td>0.01 (-4.28%)</td><td>208.00 (-6.52%)</td><td>182.34 (-4.64%)</td><td>167.60 (-7.20%)</td><td>164.40 (-0.96%)</td><td>22.51 (-11.91%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>191.22 (n/a)</td><td>180.60 (n/a)</td><td>166.00 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 <b>(+47.47%)</b></td><td>0.10 <b>(+22.86%)</b></td><td>0.10 (+9.10%)</td><td>0.08 <b>(+21.29%)</b></td><td>0.02 <b>(+89.48%)</b></td><td>243.60 (-17.56%)</td><td>186.36 (-17.13%)</td><td>193.30 (-8.35%)</td><td>134.20 <b>(-32.22%)</b></td><td>40.46 (+1.51%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>295.50 (n/a)</td><td>224.88 (n/a)</td><td>210.90 (n/a)</td><td>198.00 (n/a)</td><td>39.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.79 (+6.57%)</td><td>0.60 (-4.95%)</td><td>0.59 (-11.01%)</td><td>0.45 (-8.62%)</td><td>0.13 (+17.30%)</td><td>216.70 (+9.44%)</td><td>169.90 (+6.21%)</td><td>167.80 (+12.39%)</td><td>124.10 (-6.20%)</td><td>34.58 (+19.53%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.74 (n/a)</td><td>0.63 (n/a)</td><td>0.66 (n/a)</td><td>0.50 (n/a)</td><td>0.11 (n/a)</td><td>198.00 (n/a)</td><td>159.96 (n/a)</td><td>149.30 (n/a)</td><td>132.30 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.74 (+0.49%)</td><td>0.56 (-4.25%)</td><td>0.55 (-5.27%)</td><td>0.41 <b>(-20.59%)</b></td><td>0.12 <b>(+34.65%)</b></td><td>239.50 <b>(+25.92%)</b></td><td>181.54 (+6.64%)</td><td>179.80 (+5.58%)</td><td>132.10 (-0.45%)</td><td>39.47 <b>(+68.83%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.74 (n/a)</td><td>0.59 (n/a)</td><td>0.58 (n/a)</td><td>0.52 (n/a)</td><td>0.09 (n/a)</td><td>190.20 (n/a)</td><td>170.24 (n/a)</td><td>170.30 (n/a)</td><td>132.70 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.77 (+9.37%)</td><td>0.61 (-2.44%)</td><td>0.61 (+1.62%)</td><td>0.40 <b>(-27.96%)</b></td><td>0.16 <b>(+126.09%)</b></td><td>243.60 <b>(+38.80%)</b></td><td>171.18 (+7.84%)</td><td>162.30 (-1.64%)</td><td>127.40 (-8.61%)</td><td>48.92 <b>(+179.47%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.71 (n/a)</td><td>0.63 (n/a)</td><td>0.60 (n/a)</td><td>0.56 (n/a)</td><td>0.07 (n/a)</td><td>175.50 (n/a)</td><td>158.74 (n/a)</td><td>165.00 (n/a)</td><td>139.40 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.61 (+16.47%)</td><td>0.48 (+8.06%)</td><td>0.50 (+6.50%)</td><td>0.32 (-0.55%)</td><td>0.11 <b>(+38.21%)</b></td><td>304.40 (+0.53%)</td><td>216.66 (-5.74%)</td><td>197.20 (-6.14%)</td><td>160.60 (-14.16%)</td><td>55.84 <b>(+20.35%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>302.80 (n/a)</td><td>229.86 (n/a)</td><td>210.10 (n/a)</td><td>187.10 (n/a)</td><td>46.40 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.45 <b>(-29.27%)</b></td><td>0.43 (-13.89%)</td><td>0.42 (-11.26%)</td><td>0.42 (-0.26%)</td><td>0.01 <b>(-82.88%)</b></td><td>177.60 (+0.28%)</td><td>172.82 (+13.98%)</td><td>174.60 (+12.72%)</td><td>163.80 <b>(+41.33%)</b></td><td>5.58 <b>(-74.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.64 (n/a)</td><td>0.50 (n/a)</td><td>0.48 (n/a)</td><td>0.42 (n/a)</td><td>0.08 (n/a)</td><td>177.10 (n/a)</td><td>151.62 (n/a)</td><td>154.90 (n/a)</td><td>115.90 (n/a)</td><td>22.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.59 (+1.60%)</td><td>0.37 (-16.59%)</td><td>0.34 <b>(-29.84%)</b></td><td>0.25 (-19.76%)</td><td>0.14 <b>(+29.03%)</b></td><td>299.90 <b>(+24.59%)</b></td><td>215.74 <b>(+25.24%)</b></td><td>217.60 <b>(+42.50%)</b></td><td>125.50 (-1.57%)</td><td>68.21 <b>(+53.45%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.48 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>240.70 (n/a)</td><td>172.26 (n/a)</td><td>152.70 (n/a)</td><td>127.50 (n/a)</td><td>44.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.64 <b>(+62.29%)</b></td><td>0.53 <b>(+50.46%)</b></td><td>0.60 <b>(+68.19%)</b></td><td>0.38 <b>(+23.07%)</b></td><td>0.13 <b>(+292.64%)</b></td><td>196.30 (-18.75%)</td><td>146.28 <b>(-30.51%)</b></td><td>122.90 <b>(-40.57%)</b></td><td>115.30 <b>(-38.38%)</b></td><td>38.56 <b>(+92.55%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.03 (n/a)</td><td>241.60 (n/a)</td><td>210.50 (n/a)</td><td>206.80 (n/a)</td><td>187.10 (n/a)</td><td>20.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.60 <b>(+63.45%)</b></td><td>0.46 <b>(+45.86%)</b></td><td>0.44 <b>(+26.31%)</b></td><td>0.37 <b>(+69.53%)</b></td><td>0.09 <b>(+37.00%)</b></td><td>201.50 <b>(-41.03%)</b></td><td>163.74 <b>(-32.36%)</b></td><td>166.20 <b>(-20.82%)</b></td><td>122.70 <b>(-38.83%)</b></td><td>28.13 <b>(-52.16%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>341.70 (n/a)</td><td>242.06 (n/a)</td><td>209.90 (n/a)</td><td>200.60 (n/a)</td><td>58.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (-5.32%)</td><td>0.22 (-10.67%)</td><td>0.22 (-9.32%)</td><td>0.18 (-9.38%)</td><td>0.04 (+4.19%)</td><td>202.20 (+10.37%)</td><td>171.86 (+12.62%)</td><td>167.10 (+10.30%)</td><td>137.30 (+5.62%)</td><td>29.30 <b>(+27.79%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>183.20 (n/a)</td><td>152.60 (n/a)</td><td>151.50 (n/a)</td><td>130.00 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.21 <b>(-25.67%)</b></td><td>0.18 (-19.34%)</td><td>0.18 (-16.15%)</td><td>0.16 (+1.84%)</td><td>0.02 <b>(-54.68%)</b></td><td>233.30 (-1.81%)</td><td>202.88 (+19.98%)</td><td>200.40 (+19.29%)</td><td>173.30 <b>(+34.55%)</b></td><td>25.69 <b>(-39.95%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>237.60 (n/a)</td><td>169.10 (n/a)</td><td>168.00 (n/a)</td><td>128.80 (n/a)</td><td>42.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 <b>(+23.47%)</b></td><td>0.21 (+0.81%)</td><td>0.22 (+1.40%)</td><td>0.17 (-15.23%)</td><td>0.04 <b>(+226.75%)</b></td><td>222.80 (+17.95%)</td><td>180.04 (+1.99%)</td><td>169.30 (-1.40%)</td><td>134.60 (-19.01%)</td><td>34.67 <b>(+213.02%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>176.52 (n/a)</td><td>171.70 (n/a)</td><td>166.20 (n/a)</td><td>11.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.30 (+14.84%)</td><td>0.25 (+15.17%)</td><td>0.29 <b>(+39.22%)</b></td><td>0.17 (-9.69%)</td><td>0.07 <b>(+129.36%)</b></td><td>221.40 (+10.76%)</td><td>159.40 (-8.37%)</td><td>126.00 <b>(-28.16%)</b></td><td>122.30 (-12.89%)</td><td>48.09 <b>(+122.48%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>199.90 (n/a)</td><td>173.96 (n/a)</td><td>175.40 (n/a)</td><td>140.40 (n/a)</td><td>21.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.34 (+16.07%)</td><td>0.22 (+0.35%)</td><td>0.20 (-5.06%)</td><td>0.15 (-13.83%)</td><td>0.07 <b>(+61.63%)</b></td><td>244.60 (+16.03%)</td><td>179.78 (+4.17%)</td><td>181.30 (+5.35%)</td><td>107.50 (-13.86%)</td><td>50.21 <b>(+60.20%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>210.80 (n/a)</td><td>172.58 (n/a)</td><td>172.10 (n/a)</td><td>124.80 (n/a)</td><td>31.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (-13.19%)</td><td>0.22 (-4.05%)</td><td>0.22 (-1.59%)</td><td>0.19 (-3.70%)</td><td>0.03 <b>(-38.60%)</b></td><td>198.50 (+3.87%)</td><td>167.64 (+2.80%)</td><td>167.10 (+1.58%)</td><td>144.80 (+15.19%)</td><td>20.33 <b>(-27.48%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>191.10 (n/a)</td><td>163.08 (n/a)</td><td>164.50 (n/a)</td><td>125.70 (n/a)</td><td>28.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.40 <b>(+52.30%)</b></td><td>0.24 <b>(+29.71%)</b></td><td>0.19 (+14.40%)</td><td>0.17 (+19.18%)</td><td>0.09 <b>(+104.96%)</b></td><td>212.30 (-16.09%)</td><td>171.98 (-18.77%)</td><td>189.30 (-12.60%)</td><td>92.90 <b>(-34.35%)</b></td><td>48.82 (+16.08%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>253.00 (n/a)</td><td>211.72 (n/a)</td><td>216.60 (n/a)</td><td>141.50 (n/a)</td><td>42.06 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 <b>(+34.12%)</b></td><td>0.22 <b>(+25.16%)</b></td><td>0.23 <b>(+27.68%)</b></td><td>0.18 (+10.75%)</td><td>0.03 <b>(+91.34%)</b></td><td>208.50 (-9.70%)</td><td>169.66 (-19.19%)</td><td>163.00 <b>(-21.67%)</b></td><td>135.60 <b>(-25.45%)</b></td><td>26.60 <b>(+27.20%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>230.90 (n/a)</td><td>209.94 (n/a)</td><td>208.10 (n/a)</td><td>181.90 (n/a)</td><td>20.91 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (-3.33%)</td><td>0.24 (+0.31%)</td><td>0.25 (+2.16%)</td><td>0.19 (-1.63%)</td><td>0.04 (+1.27%)</td><td>219.30 (+1.67%)</td><td>175.66 (-0.14%)</td><td>165.00 (-2.08%)</td><td>144.30 (+3.44%)</td><td>33.17 (+4.64%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>215.70 (n/a)</td><td>175.90 (n/a)</td><td>168.50 (n/a)</td><td>139.50 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.33 <b>(+22.61%)</b></td><td>0.22 (-10.81%)</td><td>0.22 (-14.87%)</td><td>0.10 <b>(-51.42%)</b></td><td>0.08 <b>(+209.96%)</b></td><td>404.40 <b>(+105.80%)</b></td><td>218.16 <b>(+28.28%)</b></td><td>186.70 (+17.42%)</td><td>125.80 (-18.47%)</td><td>107.42 <b>(+469.95%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>196.50 (n/a)</td><td>170.06 (n/a)</td><td>159.00 (n/a)</td><td>154.30 (n/a)</td><td>18.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.38 <b>(+31.67%)</b></td><td>0.26 <b>(+29.27%)</b></td><td>0.24 <b>(+23.21%)</b></td><td>0.17 (+9.76%)</td><td>0.09 <b>(+67.40%)</b></td><td>246.80 (-8.90%)</td><td>170.30 (-19.27%)</td><td>167.60 (-18.84%)</td><td>108.10 <b>(-24.03%)</b></td><td>56.18 (+17.02%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>270.90 (n/a)</td><td>210.96 (n/a)</td><td>206.50 (n/a)</td><td>142.30 (n/a)</td><td>48.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (+2.52%)</td><td>0.23 (-3.20%)</td><td>0.24 (+2.72%)</td><td>0.16 (-17.00%)</td><td>0.04 <b>(+93.41%)</b></td><td>251.00 <b>(+20.50%)</b></td><td>188.20 (+6.14%)</td><td>167.60 (-2.67%)</td><td>153.80 (-2.47%)</td><td>41.60 <b>(+120.99%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>208.30 (n/a)</td><td>177.32 (n/a)</td><td>172.20 (n/a)</td><td>157.70 (n/a)</td><td>18.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.35 <b>(+30.65%)</b></td><td>0.26 (+12.88%)</td><td>0.25 (+9.65%)</td><td>0.21 (+8.84%)</td><td>0.05 <b>(+70.33%)</b></td><td>195.40 (-8.13%)</td><td>160.20 (-10.16%)</td><td>160.80 (-8.79%)</td><td>116.40 <b>(-23.42%)</b></td><td>28.40 (+15.86%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>212.70 (n/a)</td><td>178.32 (n/a)</td><td>176.30 (n/a)</td><td>152.00 (n/a)</td><td>24.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.35 (-4.55%)</td><td>0.30 (+6.11%)</td><td>0.32 (+16.77%)</td><td>0.20 (-5.24%)</td><td>0.06 (+15.35%)</td><td>203.20 (+5.50%)</td><td>144.94 (-4.46%)</td><td>127.50 (-14.37%)</td><td>118.20 (+4.79%)</td><td>36.33 <b>(+26.49%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>192.60 (n/a)</td><td>151.70 (n/a)</td><td>148.90 (n/a)</td><td>112.80 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (-5.95%)</td><td>0.21 (-2.07%)</td><td>0.20 (-4.36%)</td><td>0.17 (-2.51%)</td><td>0.03 (-6.28%)</td><td>238.60 (+2.58%)</td><td>195.38 (+2.08%)</td><td>201.80 (+4.61%)</td><td>157.40 (+6.35%)</td><td>31.21 (+3.23%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>232.60 (n/a)</td><td>191.40 (n/a)</td><td>192.90 (n/a)</td><td>148.00 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.30 (+9.34%)</td><td>0.23 (+8.29%)</td><td>0.22 (+8.13%)</td><td>0.18 (+0.41%)</td><td>0.04 <b>(+27.53%)</b></td><td>225.40 (-0.40%)</td><td>180.66 (-6.81%)</td><td>182.40 (-7.51%)</td><td>138.50 (-8.52%)</td><td>33.29 (+17.30%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>226.30 (n/a)</td><td>193.86 (n/a)</td><td>197.20 (n/a)</td><td>151.40 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 <b>(-25.42%)</b></td><td>0.19 (-17.75%)</td><td>0.18 (-12.46%)</td><td>0.17 (-2.20%)</td><td>0.02 <b>(-57.65%)</b></td><td>203.60 (+2.26%)</td><td>182.58 (+17.84%)</td><td>191.60 (+14.25%)</td><td>159.80 <b>(+34.06%)</b></td><td>21.05 <b>(-39.75%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>199.10 (n/a)</td><td>154.94 (n/a)</td><td>167.70 (n/a)</td><td>119.20 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.20 <b>(-35.66%)</b></td><td>0.19 (-16.86%)</td><td>0.19 (-6.37%)</td><td>0.18 (+8.24%)</td><td>0.01 <b>(-85.42%)</b></td><td>197.60 (-7.62%)</td><td>185.36 (+13.80%)</td><td>182.10 (+6.80%)</td><td>175.10 <b>(+55.51%)</b></td><td>8.95 <b>(-78.73%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>213.90 (n/a)</td><td>162.88 (n/a)</td><td>170.50 (n/a)</td><td>112.60 (n/a)</td><td>42.09 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (-9.81%)</td><td>0.18 (-4.09%)</td><td>0.18 (-0.20%)</td><td>0.15 (+0.34%)</td><td>0.03 <b>(-25.08%)</b></td><td>232.00 (-0.30%)</td><td>192.98 (+2.94%)</td><td>190.70 (+0.21%)</td><td>151.10 (+10.86%)</td><td>31.27 (-16.57%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>232.70 (n/a)</td><td>187.46 (n/a)</td><td>190.30 (n/a)</td><td>136.30 (n/a)</td><td>37.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (-6.88%)</td><td>0.19 (-11.53%)</td><td>0.18 (-9.49%)</td><td>0.14 <b>(-23.82%)</b></td><td>0.05 (+12.79%)</td><td>250.40 <b>(+31.24%)</b></td><td>194.62 (+15.11%)</td><td>192.60 (+10.50%)</td><td>132.30 (+7.39%)</td><td>42.60 <b>(+56.96%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>190.80 (n/a)</td><td>169.08 (n/a)</td><td>174.30 (n/a)</td><td>123.20 (n/a)</td><td>27.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (-19.62%)</td><td>0.20 (-13.95%)</td><td>0.19 (-17.83%)</td><td>0.17 (+11.90%)</td><td>0.04 <b>(-37.19%)</b></td><td>205.60 (-10.61%)</td><td>179.60 (+12.08%)</td><td>187.60 <b>(+21.66%)</b></td><td>126.60 <b>(+24.36%)</b></td><td>31.79 <b>(-30.72%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>230.00 (n/a)</td><td>160.24 (n/a)</td><td>154.20 (n/a)</td><td>101.80 (n/a)</td><td>45.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.29 <b>(+22.46%)</b></td><td>0.21 (+10.82%)</td><td>0.21 (+6.14%)</td><td>0.17 (+19.05%)</td><td>0.05 <b>(+31.60%)</b></td><td>203.80 (-16.03%)</td><td>167.30 (-9.35%)</td><td>168.30 (-5.77%)</td><td>122.00 (-18.34%)</td><td>32.19 (-11.24%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>242.70 (n/a)</td><td>184.56 (n/a)</td><td>178.60 (n/a)</td><td>149.40 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.24 <b>(+21.81%)</b></td><td>0.21 (+12.79%)</td><td>0.21 (+14.03%)</td><td>0.17 (+11.97%)</td><td>0.03 <b>(+45.23%)</b></td><td>205.30 (-10.70%)</td><td>170.72 (-10.90%)</td><td>164.10 (-12.29%)</td><td>142.80 (-17.93%)</td><td>23.26 (+5.11%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>229.90 (n/a)</td><td>191.60 (n/a)</td><td>187.10 (n/a)</td><td>174.00 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (+10.48%)</td><td>0.20 <b>(+24.56%)</b></td><td>0.21 <b>(+45.18%)</b></td><td>0.17 (+19.85%)</td><td>0.03 (-0.07%)</td><td>207.20 (-16.55%)</td><td>174.58 <b>(-20.13%)</b></td><td>162.30 <b>(-31.11%)</b></td><td>149.00 (-9.48%)</td><td>26.33 <b>(-23.11%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>248.30 (n/a)</td><td>218.58 (n/a)</td><td>235.60 (n/a)</td><td>164.60 (n/a)</td><td>34.25 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.88 (-3.32%)</td><td>0.77 (-6.77%)</td><td>0.82 (-1.11%)</td><td>0.61 (-16.57%)</td><td>0.11 <b>(+67.42%)</b></td><td>215.40 (+19.87%)</td><td>173.52 (+8.59%)</td><td>160.10 (+1.07%)</td><td>149.20 (+3.47%)</td><td>26.57 <b>(+107.69%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.91 (n/a)</td><td>0.82 (n/a)</td><td>0.83 (n/a)</td><td>0.73 (n/a)</td><td>0.06 (n/a)</td><td>179.70 (n/a)</td><td>159.80 (n/a)</td><td>158.40 (n/a)</td><td>144.20 (n/a)</td><td>12.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.86 (-12.96%)</td><td>0.78 (+1.22%)</td><td>0.82 (+16.46%)</td><td>0.67 (+4.29%)</td><td>0.08 <b>(-38.46%)</b></td><td>194.20 (-4.10%)</td><td>170.14 (-2.44%)</td><td>160.40 (-14.13%)</td><td>152.40 (+14.93%)</td><td>18.98 <b>(-30.82%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.99 (n/a)</td><td>0.77 (n/a)</td><td>0.70 (n/a)</td><td>0.65 (n/a)</td><td>0.14 (n/a)</td><td>202.50 (n/a)</td><td>174.40 (n/a)</td><td>186.80 (n/a)</td><td>132.60 (n/a)</td><td>27.44 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.02 (-3.25%)</td><td>0.87 (+3.95%)</td><td>0.89 (+4.56%)</td><td>0.64 (+7.54%)</td><td>0.15 (-13.44%)</td><td>205.40 (-7.02%)</td><td>155.56 (-4.83%)</td><td>146.90 (-4.36%)</td><td>128.20 (+3.30%)</td><td>30.91 (-17.26%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.06 (n/a)</td><td>0.83 (n/a)</td><td>0.85 (n/a)</td><td>0.59 (n/a)</td><td>0.18 (n/a)</td><td>220.90 (n/a)</td><td>163.46 (n/a)</td><td>153.60 (n/a)</td><td>124.10 (n/a)</td><td>37.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-13.48%)</td><td>0.02 (-16.13%)</td><td>0.02 (-11.81%)</td><td>0.02 (-13.69%)</td><td>0.00 <b>(-20.96%)</b></td><td>211.00 (+15.87%)</td><td>187.82 (+18.99%)</td><td>185.60 (+13.45%)</td><td>153.90 (+15.63%)</td><td>23.50 (+8.56%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.10 (n/a)</td><td>157.84 (n/a)</td><td>163.60 (n/a)</td><td>133.10 (n/a)</td><td>21.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-4.07%)</td><td>0.03 (+13.17%)</td><td>0.03 <b>(+31.10%)</b></td><td>0.02 (+13.33%)</td><td>0.00 (-16.18%)</td><td>211.00 (-11.75%)</td><td>163.20 (-12.83%)</td><td>144.00 <b>(-23.73%)</b></td><td>141.40 (+4.28%)</td><td>30.56 <b>(-23.92%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.10 (n/a)</td><td>187.22 (n/a)</td><td>188.80 (n/a)</td><td>135.60 (n/a)</td><td>40.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-8.17%)</td><td>0.02 (-7.07%)</td><td>0.02 (-9.34%)</td><td>0.02 (-9.73%)</td><td>0.01 (-6.57%)</td><td>208.40 (+10.79%)</td><td>182.78 (+7.83%)</td><td>198.20 (+10.29%)</td><td>127.80 (+8.86%)</td><td>34.13 (+14.93%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.10 (n/a)</td><td>169.50 (n/a)</td><td>179.70 (n/a)</td><td>117.40 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.87 <b>(-20.58%)</b></td><td>12.15 (-17.17%)</td><td>12.52 (-17.89%)</td><td>9.30 (-19.50%)</td><td>1.70 <b>(-36.45%)</b></td><td>225.60 <b>(+24.23%)</b></td><td>175.82 (+19.59%)</td><td>167.60 <b>(+21.80%)</b></td><td>151.30 <b>(+25.98%)</b></td><td>28.71 (+2.86%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>17.46 (n/a)</td><td>14.67 (n/a)</td><td>15.25 (n/a)</td><td>11.55 (n/a)</td><td>2.67 (n/a)</td><td>181.60 (n/a)</td><td>147.02 (n/a)</td><td>137.60 (n/a)</td><td>120.10 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.06 (+2.61%)</td><td>0.87 (-1.63%)</td><td>0.90 (-7.29%)</td><td>0.67 (-6.27%)</td><td>0.14 (-3.84%)</td><td>195.80 (+6.70%)</td><td>154.98 (+1.53%)</td><td>147.60 (+7.89%)</td><td>124.50 (-2.58%)</td><td>26.36 (-0.64%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.03 (n/a)</td><td>0.89 (n/a)</td><td>0.97 (n/a)</td><td>0.72 (n/a)</td><td>0.15 (n/a)</td><td>183.50 (n/a)</td><td>152.64 (n/a)</td><td>136.80 (n/a)</td><td>127.80 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.97 (-17.41%)</td><td>0.84 (+2.82%)</td><td>0.82 (+7.35%)</td><td>0.74 (+19.37%)</td><td>0.10 <b>(-51.67%)</b></td><td>177.70 (-16.22%)</td><td>158.62 (-6.09%)</td><td>161.00 (-6.83%)</td><td>135.60 <b>(+21.07%)</b></td><td>19.18 <b>(-48.86%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.18 (n/a)</td><td>0.82 (n/a)</td><td>0.76 (n/a)</td><td>0.62 (n/a)</td><td>0.22 (n/a)</td><td>212.10 (n/a)</td><td>168.90 (n/a)</td><td>172.80 (n/a)</td><td>112.00 (n/a)</td><td>37.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.92 (+2.20%)</td><td>0.73 (-3.92%)</td><td>0.76 (+1.18%)</td><td>0.50 <b>(-24.76%)</b></td><td>0.16 <b>(+78.70%)</b></td><td>262.30 <b>(+32.94%)</b></td><td>188.76 (+7.41%)</td><td>174.60 (-1.13%)</td><td>143.70 (-2.11%)</td><td>45.46 <b>(+142.23%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.90 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.09 (n/a)</td><td>197.30 (n/a)</td><td>175.74 (n/a)</td><td>176.60 (n/a)</td><td>146.80 (n/a)</td><td>18.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.03 (-9.10%)</td><td>0.84 (+4.53%)</td><td>0.77 (-4.47%)</td><td>0.70 <b>(+32.27%)</b></td><td>0.15 <b>(-37.25%)</b></td><td>189.00 <b>(-24.40%)</b></td><td>161.14 (-8.95%)</td><td>170.90 (+4.65%)</td><td>127.90 (+10.07%)</td><td>27.69 <b>(-48.75%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.14 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.53 (n/a)</td><td>0.24 (n/a)</td><td>250.00 (n/a)</td><td>176.98 (n/a)</td><td>163.30 (n/a)</td><td>116.20 (n/a)</td><td>54.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.05 (+9.32%)</td><td>0.82 (+0.43%)</td><td>0.81 (-7.61%)</td><td>0.64 (-4.64%)</td><td>0.15 (+13.52%)</td><td>205.00 (+4.86%)</td><td>164.56 (-0.07%)</td><td>163.40 (+8.28%)</td><td>125.60 (-8.52%)</td><td>28.29 (+4.62%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.96 (n/a)</td><td>0.82 (n/a)</td><td>0.88 (n/a)</td><td>0.68 (n/a)</td><td>0.13 (n/a)</td><td>195.50 (n/a)</td><td>164.68 (n/a)</td><td>150.90 (n/a)</td><td>137.30 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (+1.27%)</td><td>0.02 (+6.66%)</td><td>0.02 (+5.15%)</td><td>0.02 (+10.49%)</td><td>0.00 (-10.93%)</td><td>212.20 (-9.47%)</td><td>181.02 (-6.63%)</td><td>181.90 (-4.91%)</td><td>158.90 (-1.24%)</td><td>20.70 <b>(-21.05%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.40 (n/a)</td><td>193.88 (n/a)</td><td>191.30 (n/a)</td><td>160.90 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (-4.63%)</td><td>0.02 (-15.75%)</td><td>0.02 (-13.53%)</td><td>0.01 <b>(-39.37%)</b></td><td>0.01 <b>(+76.40%)</b></td><td>274.00 <b>(+64.96%)</b></td><td>185.78 <b>(+25.97%)</b></td><td>174.40 (+15.65%)</td><td>129.10 (+4.87%)</td><td>58.72 <b>(+197.28%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.10 (n/a)</td><td>147.48 (n/a)</td><td>150.80 (n/a)</td><td>123.10 (n/a)</td><td>19.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.00 (-6.67%)</td><td>0.00 (-2.37%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.50%)</td><td>0.00 <b>(-32.22%)</b></td><td>1043.79 (+3.10%)</td><td>996.35 (+2.85%)</td><td>985.03 (+1.69%)</td><td>969.62 (+5.77%)</td><td>29.42 <b>(-25.38%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1012.45 (n/a)</td><td>968.79 (n/a)</td><td>968.69 (n/a)</td><td>916.70 (n/a)</td><td>39.43 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.01 (-1.18%)</td><td>0.01 (-2.22%)</td><td>0.01 (-3.61%)</td><td>0.01 (+2.78%)</td><td>0.00 <b>(-32.02%)</b></td><td>1102.08 (-2.75%)</td><td>1032.09 (+1.84%)</td><td>1024.17 (+3.42%)</td><td>979.86 (+1.27%)</td><td>44.17 <b>(-34.90%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1133.19 (n/a)</td><td>1013.40 (n/a)</td><td>990.30 (n/a)</td><td>967.55 (n/a)</td><td>67.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.97 (+0.86%)</td><td>0.95 (-0.27%)</td><td>0.95 (-0.22%)</td><td>0.93 (-0.81%)</td><td>0.02 <b>(+80.91%)</b></td><td>2248.81 (+0.81%)</td><td>2206.35 (+0.29%)</td><td>2208.73 (+0.22%)</td><td>2152.84 (-0.86%)</td><td>39.82 <b>(+80.82%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2230.65 (n/a)</td><td>2200.07 (n/a)</td><td>2203.86 (n/a)</td><td>2171.44 (n/a)</td><td>22.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.90 (+2.39%)</td><td>4.87 (-4.70%)</td><td>4.52 (-15.36%)</td><td>3.55 (-12.56%)</td><td>1.01 <b>(+55.98%)</b></td><td>295.50 (+14.36%)</td><td>223.48 (+7.25%)</td><td>231.80 (+18.14%)</td><td>177.80 (-2.36%)</td><td>48.63 <b>(+63.73%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.76 (n/a)</td><td>5.11 (n/a)</td><td>5.34 (n/a)</td><td>4.06 (n/a)</td><td>0.65 (n/a)</td><td>258.40 (n/a)</td><td>208.38 (n/a)</td><td>196.20 (n/a)</td><td>182.10 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.92 (+2.34%)</td><td>5.19 (+7.37%)</td><td>5.71 (+9.76%)</td><td>4.00 <b>(+34.62%)</b></td><td>0.87 <b>(-24.14%)</b></td><td>261.90 <b>(-25.72%)</b></td><td>207.16 (-10.04%)</td><td>183.80 (-8.87%)</td><td>177.00 (-2.32%)</td><td>37.87 <b>(-46.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.79 (n/a)</td><td>4.83 (n/a)</td><td>5.20 (n/a)</td><td>2.97 (n/a)</td><td>1.14 (n/a)</td><td>352.60 (n/a)</td><td>230.28 (n/a)</td><td>201.70 (n/a)</td><td>181.20 (n/a)</td><td>71.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.95 (-0.55%)</td><td>4.96 (-5.79%)</td><td>4.50 (-10.27%)</td><td>4.07 (-13.10%)</td><td>0.89 <b>(+37.86%)</b></td><td>257.50 (+15.06%)</td><td>216.72 (+7.56%)</td><td>233.00 (+11.43%)</td><td>176.30 (+0.57%)</td><td>37.41 <b>(+55.16%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.98 (n/a)</td><td>5.27 (n/a)</td><td>5.02 (n/a)</td><td>4.69 (n/a)</td><td>0.65 (n/a)</td><td>223.80 (n/a)</td><td>201.48 (n/a)</td><td>209.10 (n/a)</td><td>175.30 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.97 (+14.32%)</td><td>5.15 (+0.66%)</td><td>4.70 (-10.22%)</td><td>3.43 (-11.67%)</td><td>1.37 <b>(+64.92%)</b></td><td>305.70 (+13.18%)</td><td>216.02 (+2.97%)</td><td>223.20 (+11.38%)</td><td>150.40 (-12.56%)</td><td>59.82 <b>(+59.09%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>6.10 (n/a)</td><td>5.12 (n/a)</td><td>5.23 (n/a)</td><td>3.88 (n/a)</td><td>0.83 (n/a)</td><td>270.10 (n/a)</td><td>209.78 (n/a)</td><td>200.40 (n/a)</td><td>172.00 (n/a)</td><td>37.60 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.29 (+8.23%)</td><td>7.69 (-1.55%)</td><td>7.13 (-12.51%)</td><td>6.96 (+8.98%)</td><td>1.00 (+16.45%)</td><td>301.30 (-8.25%)</td><td>276.20 (+1.73%)</td><td>294.10 (+14.30%)</td><td>225.80 (-7.57%)</td><td>32.56 (-2.49%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.58 (n/a)</td><td>7.81 (n/a)</td><td>8.15 (n/a)</td><td>6.39 (n/a)</td><td>0.86 (n/a)</td><td>328.40 (n/a)</td><td>271.50 (n/a)</td><td>257.30 (n/a)</td><td>244.30 (n/a)</td><td>33.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.52 (+9.88%)</td><td>8.55 (+6.09%)</td><td>8.60 (+1.28%)</td><td>7.55 (+5.17%)</td><td>0.88 <b>(+25.42%)</b></td><td>277.60 (-4.93%)</td><td>247.30 (-5.52%)</td><td>243.80 (-1.26%)</td><td>220.30 (-8.97%)</td><td>25.63 (+8.70%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.66 (n/a)</td><td>8.06 (n/a)</td><td>8.49 (n/a)</td><td>7.18 (n/a)</td><td>0.70 (n/a)</td><td>292.00 (n/a)</td><td>261.76 (n/a)</td><td>246.90 (n/a)</td><td>242.00 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>10.43 (+9.03%)</td><td>8.46 (+3.77%)</td><td>8.06 (+3.07%)</td><td>7.46 (+7.67%)</td><td>1.18 (+5.15%)</td><td>281.30 (-7.10%)</td><td>251.44 (-3.74%)</td><td>260.00 (-2.99%)</td><td>201.10 (-8.30%)</td><td>31.18 (-11.12%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>9.56 (n/a)</td><td>8.15 (n/a)</td><td>7.82 (n/a)</td><td>6.93 (n/a)</td><td>1.12 (n/a)</td><td>302.80 (n/a)</td><td>261.20 (n/a)</td><td>268.00 (n/a)</td><td>219.30 (n/a)</td><td>35.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.54 (-4.21%)</td><td>8.22 (-6.98%)</td><td>7.78 (-17.04%)</td><td>7.71 (+8.15%)</td><td>0.77 <b>(-35.64%)</b></td><td>272.10 (-7.51%)</td><td>256.62 (+6.47%)</td><td>269.40 <b>(+20.54%)</b></td><td>219.90 (+4.37%)</td><td>22.08 <b>(-37.63%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>9.96 (n/a)</td><td>8.84 (n/a)</td><td>9.38 (n/a)</td><td>7.13 (n/a)</td><td>1.20 (n/a)</td><td>294.20 (n/a)</td><td>241.02 (n/a)</td><td>223.50 (n/a)</td><td>210.70 (n/a)</td><td>35.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.10 (-16.26%)</td><td>8.36 (-7.70%)</td><td>8.72 (-5.94%)</td><td>7.19 (-1.25%)</td><td>0.85 <b>(-36.86%)</b></td><td>291.60 (+1.29%)</td><td>253.14 (+7.32%)</td><td>240.50 (+6.27%)</td><td>230.50 (+19.43%)</td><td>27.10 <b>(-24.81%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>10.87 (n/a)</td><td>9.05 (n/a)</td><td>9.27 (n/a)</td><td>7.28 (n/a)</td><td>1.35 (n/a)</td><td>287.90 (n/a)</td><td>235.88 (n/a)</td><td>226.30 (n/a)</td><td>193.00 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.06 (-14.93%)</td><td>8.25 (-10.83%)</td><td>8.13 (-15.66%)</td><td>7.89 (-0.24%)</td><td>0.47 <b>(-61.34%)</b></td><td>265.80 (+0.23%)</td><td>254.92 (+10.84%)</td><td>257.90 (+18.57%)</td><td>231.50 (+17.57%)</td><td>13.60 <b>(-55.88%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>10.65 (n/a)</td><td>9.25 (n/a)</td><td>9.64 (n/a)</td><td>7.91 (n/a)</td><td>1.21 (n/a)</td><td>265.20 (n/a)</td><td>229.98 (n/a)</td><td>217.50 (n/a)</td><td>196.90 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.00 (-1.32%)</td><td>11.34 (+2.09%)</td><td>11.37 (+5.94%)</td><td>10.43 (+0.19%)</td><td>0.61 <b>(-26.84%)</b></td><td>402.10 (-0.17%)</td><td>370.60 (-2.24%)</td><td>368.90 (-5.60%)</td><td>349.50 (+1.33%)</td><td>20.40 <b>(-26.13%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>12.16 (n/a)</td><td>11.11 (n/a)</td><td>10.73 (n/a)</td><td>10.41 (n/a)</td><td>0.83 (n/a)</td><td>402.80 (n/a)</td><td>379.10 (n/a)</td><td>390.80 (n/a)</td><td>344.90 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.26 (+2.39%)</td><td>11.66 (-1.49%)</td><td>11.65 (-2.30%)</td><td>10.65 (-2.04%)</td><td>0.99 <b>(+29.92%)</b></td><td>393.60 (+2.07%)</td><td>361.72 (+1.73%)</td><td>360.00 (+2.33%)</td><td>316.40 (-2.35%)</td><td>29.05 <b>(+28.58%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>12.95 (n/a)</td><td>11.83 (n/a)</td><td>11.92 (n/a)</td><td>10.88 (n/a)</td><td>0.76 (n/a)</td><td>385.60 (n/a)</td><td>355.56 (n/a)</td><td>351.80 (n/a)</td><td>324.00 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.06 (+3.37%)</td><td>11.25 (+0.23%)</td><td>11.46 (+3.00%)</td><td>10.31 (-6.80%)</td><td>0.73 <b>(+188.82%)</b></td><td>406.80 (+7.28%)</td><td>374.18 (+0.06%)</td><td>366.00 (-2.92%)</td><td>347.70 (-3.26%)</td><td>24.77 <b>(+201.22%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>11.67 (n/a)</td><td>11.22 (n/a)</td><td>11.13 (n/a)</td><td>11.06 (n/a)</td><td>0.25 (n/a)</td><td>379.20 (n/a)</td><td>373.94 (n/a)</td><td>377.00 (n/a)</td><td>359.40 (n/a)</td><td>8.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.82 (-7.49%)</td><td>12.09 (-10.09%)</td><td>12.11 (-11.45%)</td><td>11.04 (-10.27%)</td><td>0.69 (+7.23%)</td><td>379.80 (+11.44%)</td><td>347.96 (+11.32%)</td><td>346.50 (+12.94%)</td><td>327.20 (+8.13%)</td><td>20.54 <b>(+28.48%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>13.86 (n/a)</td><td>13.44 (n/a)</td><td>13.67 (n/a)</td><td>12.31 (n/a)</td><td>0.65 (n/a)</td><td>340.80 (n/a)</td><td>312.58 (n/a)</td><td>306.80 (n/a)</td><td>302.60 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>15.16 (+4.92%)</td><td>13.05 (+1.39%)</td><td>12.88 (-2.14%)</td><td>11.71 (+8.17%)</td><td>1.35 (-3.15%)</td><td>358.10 (-7.54%)</td><td>324.10 (-1.54%)</td><td>325.60 (+2.17%)</td><td>276.70 (-4.68%)</td><td>31.66 (-15.75%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.45 (n/a)</td><td>12.87 (n/a)</td><td>13.16 (n/a)</td><td>10.83 (n/a)</td><td>1.39 (n/a)</td><td>387.30 (n/a)</td><td>329.18 (n/a)</td><td>318.70 (n/a)</td><td>290.30 (n/a)</td><td>37.58 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.93 (-3.10%)</td><td>12.82 (-1.42%)</td><td>12.68 (-0.77%)</td><td>11.36 (-7.10%)</td><td>0.98 (+18.88%)</td><td>369.20 (+7.67%)</td><td>328.80 (+1.63%)</td><td>330.80 (+0.79%)</td><td>301.10 (+3.19%)</td><td>26.12 <b>(+34.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.37 (n/a)</td><td>13.00 (n/a)</td><td>12.78 (n/a)</td><td>12.23 (n/a)</td><td>0.83 (n/a)</td><td>342.90 (n/a)</td><td>323.52 (n/a)</td><td>328.20 (n/a)</td><td>291.80 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>14.62 (-3.79%)</td><td>13.63 (-0.45%)</td><td>13.87 (+3.30%)</td><td>12.15 (-5.50%)</td><td>0.95 (+2.11%)</td><td>345.20 (+5.82%)</td><td>309.10 (+0.51%)</td><td>302.40 (-3.17%)</td><td>287.00 (+3.95%)</td><td>22.61 (+13.68%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>15.19 (n/a)</td><td>13.69 (n/a)</td><td>13.43 (n/a)</td><td>12.86 (n/a)</td><td>0.93 (n/a)</td><td>326.20 (n/a)</td><td>307.52 (n/a)</td><td>312.30 (n/a)</td><td>276.10 (n/a)</td><td>19.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>15.07 (+6.92%)</td><td>13.10 (+6.51%)</td><td>13.17 (+2.47%)</td><td>10.25 (+4.60%)</td><td>1.89 (+10.29%)</td><td>409.20 (-4.39%)</td><td>326.04 (-5.98%)</td><td>318.50 (-2.42%)</td><td>278.30 (-6.49%)</td><td>51.58 (-1.37%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>14.09 (n/a)</td><td>12.30 (n/a)</td><td>12.85 (n/a)</td><td>9.80 (n/a)</td><td>1.71 (n/a)</td><td>428.00 (n/a)</td><td>346.78 (n/a)</td><td>326.40 (n/a)</td><td>297.60 (n/a)</td><td>52.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.12 (-9.35%)</td><td>2.91 (+0.22%)</td><td>2.96 (-1.89%)</td><td>2.63 (+7.04%)</td><td>0.20 <b>(-50.60%)</b></td><td>199.50 (-6.56%)</td><td>180.64 (-1.35%)</td><td>176.80 (+1.90%)</td><td>168.10 (+10.37%)</td><td>12.68 <b>(-49.78%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>3.44 (n/a)</td><td>2.91 (n/a)</td><td>3.02 (n/a)</td><td>2.46 (n/a)</td><td>0.40 (n/a)</td><td>213.50 (n/a)</td><td>183.12 (n/a)</td><td>173.50 (n/a)</td><td>152.30 (n/a)</td><td>25.25 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.58 (-5.88%)</td><td>5.08 (+2.08%)</td><td>5.07 (+6.58%)</td><td>4.62 (-0.57%)</td><td>0.41 <b>(-24.96%)</b></td><td>226.80 (+0.58%)</td><td>207.44 (-2.35%)</td><td>207.00 (-6.17%)</td><td>187.80 (+6.28%)</td><td>16.54 (-18.88%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>5.93 (n/a)</td><td>4.98 (n/a)</td><td>4.75 (n/a)</td><td>4.65 (n/a)</td><td>0.54 (n/a)</td><td>225.50 (n/a)</td><td>212.44 (n/a)</td><td>220.60 (n/a)</td><td>176.70 (n/a)</td><td>20.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.08 (+2.61%)</td><td>7.51 (-8.76%)</td><td>7.33 (-15.77%)</td><td>5.72 <b>(-21.45%)</b></td><td>1.35 <b>(+82.75%)</b></td><td>366.50 <b>(+27.30%)</b></td><td>286.80 (+11.87%)</td><td>286.20 (+18.71%)</td><td>230.90 (-2.53%)</td><td>53.95 <b>(+125.91%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>8.85 (n/a)</td><td>8.23 (n/a)</td><td>8.70 (n/a)</td><td>7.28 (n/a)</td><td>0.74 (n/a)</td><td>287.90 (n/a)</td><td>256.38 (n/a)</td><td>241.10 (n/a)</td><td>236.90 (n/a)</td><td>23.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.33 (-9.81%)</td><td>2.74 (-2.62%)</td><td>2.97 (+7.36%)</td><td>2.13 (+2.53%)</td><td>0.51 (-13.45%)</td><td>245.60 (-2.46%)</td><td>196.62 (+2.15%)</td><td>176.60 (-6.86%)</td><td>157.20 (+10.86%)</td><td>37.97 (-4.52%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>3.70 (n/a)</td><td>2.82 (n/a)</td><td>2.76 (n/a)</td><td>2.08 (n/a)</td><td>0.58 (n/a)</td><td>251.80 (n/a)</td><td>192.48 (n/a)</td><td>189.60 (n/a)</td><td>141.80 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (-0.73%)</td><td>0.23 (+12.56%)</td><td>0.24 <b>(+22.11%)</b></td><td>0.16 (-8.12%)</td><td>0.04 (+12.78%)</td><td>205.40 (+8.85%)</td><td>146.70 (-10.23%)</td><td>139.40 (-18.10%)</td><td>122.80 (+0.74%)</td><td>34.01 <b>(+26.30%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.70 (n/a)</td><td>163.42 (n/a)</td><td>170.20 (n/a)</td><td>121.90 (n/a)</td><td>26.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (+7.69%)</td><td>0.19 (+11.63%)</td><td>0.21 (+14.65%)</td><td>0.15 (+4.49%)</td><td>0.03 (+1.94%)</td><td>223.80 (-4.32%)</td><td>173.66 (-10.68%)</td><td>155.70 (-12.82%)</td><td>149.00 (-7.17%)</td><td>31.59 (-12.03%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>233.90 (n/a)</td><td>194.42 (n/a)</td><td>178.60 (n/a)</td><td>160.50 (n/a)</td><td>35.91 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.40 (-19.83%)</td><td>0.36 (-10.67%)</td><td>0.36 (+1.28%)</td><td>0.33 (-0.65%)</td><td>0.03 <b>(-66.88%)</b></td><td>197.90 (+0.61%)</td><td>182.22 (+8.98%)</td><td>181.60 (-1.30%)</td><td>163.80 <b>(+24.66%)</b></td><td>13.38 <b>(-57.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>196.70 (n/a)</td><td>167.20 (n/a)</td><td>184.00 (n/a)</td><td>131.40 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.50 (+11.45%)</td><td>0.39 (-0.62%)</td><td>0.36 (-7.96%)</td><td>0.33 (-4.68%)</td><td>0.07 <b>(+86.31%)</b></td><td>196.60 (+4.91%)</td><td>171.26 (+2.35%)</td><td>181.00 (+8.64%)</td><td>130.10 (-10.28%)</td><td>28.47 <b>(+77.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.04 (n/a)</td><td>187.40 (n/a)</td><td>167.32 (n/a)</td><td>166.60 (n/a)</td><td>145.00 (n/a)</td><td>16.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.56 <b>(+33.56%)</b></td><td>0.36 (+0.08%)</td><td>0.35 (+0.49%)</td><td>0.19 <b>(-42.16%)</b></td><td>0.15 <b>(+266.41%)</b></td><td>349.80 <b>(+72.91%)</b></td><td>210.28 (+14.33%)</td><td>186.60 (-0.48%)</td><td>117.80 <b>(-25.11%)</b></td><td>92.05 <b>(+372.65%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.04 (n/a)</td><td>202.30 (n/a)</td><td>183.92 (n/a)</td><td>187.50 (n/a)</td><td>157.30 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.95 (-7.33%)</td><td>0.70 <b>(-20.13%)</b></td><td>0.68 <b>(-28.54%)</b></td><td>0.52 <b>(-21.38%)</b></td><td>0.16 (-3.15%)</td><td>251.50 <b>(+27.21%)</b></td><td>194.48 <b>(+26.14%)</b></td><td>193.60 <b>(+39.99%)</b></td><td>137.90 (+7.90%)</td><td>40.64 <b>(+31.27%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.03 (n/a)</td><td>0.88 (n/a)</td><td>0.95 (n/a)</td><td>0.66 (n/a)</td><td>0.16 (n/a)</td><td>197.70 (n/a)</td><td>154.18 (n/a)</td><td>138.30 (n/a)</td><td>127.80 (n/a)</td><td>30.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.92 (+18.91%)</td><td>0.83 (+13.60%)</td><td>0.86 (+17.19%)</td><td>0.72 (+11.32%)</td><td>0.09 <b>(+83.12%)</b></td><td>183.10 (-10.16%)</td><td>160.54 (-11.38%)</td><td>152.40 (-14.67%)</td><td>142.40 (-15.89%)</td><td>18.99 <b>(+38.61%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.64 (n/a)</td><td>0.05 (n/a)</td><td>203.80 (n/a)</td><td>181.16 (n/a)</td><td>178.60 (n/a)</td><td>169.30 (n/a)</td><td>13.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.32 <b>(+29.24%)</b></td><td>0.98 <b>(+27.21%)</b></td><td>0.82 (+13.78%)</td><td>0.79 <b>(+20.03%)</b></td><td>0.25 <b>(+78.13%)</b></td><td>166.90 (-16.72%)</td><td>139.84 (-19.32%)</td><td>159.80 (-12.10%)</td><td>99.60 <b>(-22.61%)</b></td><td>32.54 <b>(+20.93%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>1.02 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.65 (n/a)</td><td>0.14 (n/a)</td><td>200.40 (n/a)</td><td>173.32 (n/a)</td><td>181.80 (n/a)</td><td>128.70 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.86 (-2.59%)</td><td>0.76 (+11.53%)</td><td>0.83 <b>(+28.66%)</b></td><td>0.60 <b>(+37.11%)</b></td><td>0.12 <b>(-37.14%)</b></td><td>219.70 <b>(-27.06%)</b></td><td>175.64 (-14.31%)</td><td>158.10 <b>(-22.31%)</b></td><td>151.50 (+2.64%)</td><td>29.40 <b>(-52.26%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.89 (n/a)</td><td>0.68 (n/a)</td><td>0.64 (n/a)</td><td>0.44 (n/a)</td><td>0.19 (n/a)</td><td>301.20 (n/a)</td><td>204.96 (n/a)</td><td>203.50 (n/a)</td><td>147.60 (n/a)</td><td>61.58 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (+8.90%)</td><td>0.10 (+13.02%)</td><td>0.10 (+16.63%)</td><td>0.07 (-0.49%)</td><td>0.02 <b>(+23.44%)</b></td><td>246.20 (+0.49%)</td><td>178.86 (-10.53%)</td><td>165.10 (-14.23%)</td><td>141.00 (-8.20%)</td><td>42.24 (+13.35%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:14:00</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.00 (n/a)</td><td>199.92 (n/a)</td><td>192.50 (n/a)</td><td>153.60 (n/a)</td><td>37.27 (n/a)</td>
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
