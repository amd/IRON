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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 <b>(+20.77%)</b></td><td>0.04 (+2.47%)</td><td>0.04 (+1.38%)</td><td>0.03 (-5.90%)</td><td>0.01 <b>(+158.89%)</b></td><td>205.10 (+6.27%)</td><td>169.98 (+0.12%)</td><td>163.50 (-1.33%)</td><td>128.40 (-17.21%)</td><td>32.72 <b>(+131.05%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.00 (n/a)</td><td>169.78 (n/a)</td><td>165.70 (n/a)</td><td>155.10 (n/a)</td><td>14.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (-8.94%)</td><td>0.03 (-19.27%)</td><td>0.03 <b>(-26.25%)</b></td><td>0.03 <b>(-25.25%)</b></td><td>0.01 <b>(+50.43%)</b></td><td>234.90 <b>(+33.77%)</b></td><td>197.80 <b>(+26.58%)</b></td><td>212.60 <b>(+35.59%)</b></td><td>146.80 (+9.80%)</td><td>37.05 <b>(+120.57%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>175.60 (n/a)</td><td>156.26 (n/a)</td><td>156.80 (n/a)</td><td>133.70 (n/a)</td><td>16.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-9.66%)</td><td>0.03 (-8.93%)</td><td>0.03 (-7.73%)</td><td>0.03 (-3.69%)</td><td>0.00 <b>(-31.80%)</b></td><td>216.80 (+3.88%)</td><td>201.14 (+9.24%)</td><td>208.90 (+8.35%)</td><td>178.20 (+10.68%)</td><td>17.61 (-18.94%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.70 (n/a)</td><td>184.12 (n/a)</td><td>192.80 (n/a)</td><td>161.00 (n/a)</td><td>21.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+5.91%)</td><td>0.04 (+12.34%)</td><td>0.04 (+14.90%)</td><td>0.03 (+8.87%)</td><td>0.01 (-0.76%)</td><td>195.50 (-8.13%)</td><td>168.92 (-11.20%)</td><td>168.70 (-13.00%)</td><td>138.80 (-5.58%)</td><td>23.30 (-12.98%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>190.22 (n/a)</td><td>193.90 (n/a)</td><td>147.00 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-17.66%)</td><td>0.03 (-7.48%)</td><td>0.03 (-3.42%)</td><td>0.02 (+11.46%)</td><td>0.00 <b>(-47.41%)</b></td><td>247.50 (-10.29%)</td><td>207.92 (+5.07%)</td><td>197.30 (+3.52%)</td><td>185.90 <b>(+21.50%)</b></td><td>26.44 <b>(-44.44%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>275.90 (n/a)</td><td>197.88 (n/a)</td><td>190.60 (n/a)</td><td>153.00 (n/a)</td><td>47.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 <b>(-20.95%)</b></td><td>0.03 (-15.72%)</td><td>0.03 (-7.09%)</td><td>0.03 (-14.71%)</td><td>0.00 <b>(-30.76%)</b></td><td>231.70 (+17.26%)</td><td>203.96 (+18.17%)</td><td>189.20 (+7.62%)</td><td>183.30 <b>(+26.50%)</b></td><td>23.94 (+3.59%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>197.60 (n/a)</td><td>172.60 (n/a)</td><td>175.80 (n/a)</td><td>144.90 (n/a)</td><td>23.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 <b>(+30.43%)</b></td><td>0.03 (+10.72%)</td><td>0.03 (+6.59%)</td><td>0.03 (-6.60%)</td><td>0.01 <b>(+242.98%)</b></td><td>237.30 (+7.08%)</td><td>194.12 (-7.55%)</td><td>201.30 (-6.15%)</td><td>149.50 <b>(-23.37%)</b></td><td>34.21 <b>(+179.23%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>221.60 (n/a)</td><td>209.98 (n/a)</td><td>214.50 (n/a)</td><td>195.10 (n/a)</td><td>12.25 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (-5.60%)</td><td>0.03 (+11.76%)</td><td>0.04 <b>(+27.10%)</b></td><td>0.03 (+1.70%)</td><td>0.00 (-17.21%)</td><td>219.50 (-1.70%)</td><td>182.34 (-11.09%)</td><td>171.40 <b>(-21.34%)</b></td><td>159.50 (+5.91%)</td><td>26.57 (-13.26%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>205.08 (n/a)</td><td>217.90 (n/a)</td><td>150.60 (n/a)</td><td>30.63 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 <b>(+23.05%)</b></td><td>0.07 (+1.10%)</td><td>0.07 (-5.86%)</td><td>0.06 (+15.40%)</td><td>0.02 <b>(+25.67%)</b></td><td>213.60 (-13.35%)</td><td>175.58 (-0.73%)</td><td>180.10 (+6.25%)</td><td>114.90 (-18.68%)</td><td>37.23 (-13.95%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>246.50 (n/a)</td><td>176.88 (n/a)</td><td>169.50 (n/a)</td><td>141.30 (n/a)</td><td>43.26 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (-1.27%)</td><td>0.07 <b>(+22.26%)</b></td><td>0.07 <b>(+33.76%)</b></td><td>0.06 <b>(+94.84%)</b></td><td>0.00 <b>(-75.00%)</b></td><td>195.50 <b>(-48.67%)</b></td><td>177.38 <b>(-25.35%)</b></td><td>173.60 <b>(-25.24%)</b></td><td>166.90 (+1.27%)</td><td>11.85 <b>(-86.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>380.90 (n/a)</td><td>237.60 (n/a)</td><td>232.20 (n/a)</td><td>164.80 (n/a)</td><td>88.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (-18.36%)</td><td>0.07 (-11.64%)</td><td>0.07 (-6.90%)</td><td>0.06 (-12.40%)</td><td>0.01 <b>(-32.65%)</b></td><td>212.50 (+14.12%)</td><td>186.70 (+12.74%)</td><td>181.30 (+7.41%)</td><td>166.50 <b>(+22.43%)</b></td><td>17.78 (-2.60%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.20 (n/a)</td><td>165.60 (n/a)</td><td>168.80 (n/a)</td><td>136.00 (n/a)</td><td>18.26 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (+12.73%)</td><td>0.07 (-12.58%)</td><td>0.07 <b>(-21.96%)</b></td><td>0.06 <b>(-21.58%)</b></td><td>0.02 <b>(+122.95%)</b></td><td>215.20 <b>(+27.56%)</b></td><td>180.06 (+18.73%)</td><td>187.00 <b>(+28.17%)</b></td><td>119.70 (-11.33%)</td><td>38.98 <b>(+146.65%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>168.70 (n/a)</td><td>151.66 (n/a)</td><td>145.90 (n/a)</td><td>135.00 (n/a)</td><td>15.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (-2.92%)</td><td>0.07 (-8.31%)</td><td>0.07 (-5.41%)</td><td>0.05 (-12.61%)</td><td>0.02 (+19.17%)</td><td>244.60 (+14.46%)</td><td>186.12 (+11.09%)</td><td>167.90 (+5.73%)</td><td>135.20 (+2.97%)</td><td>44.62 <b>(+42.09%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>167.54 (n/a)</td><td>158.80 (n/a)</td><td>131.30 (n/a)</td><td>31.40 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 <b>(+29.86%)</b></td><td>0.07 (+2.28%)</td><td>0.06 <b>(-24.49%)</b></td><td>0.05 (+16.83%)</td><td>0.03 <b>(+20.57%)</b></td><td>224.40 (-14.42%)</td><td>182.66 (-2.96%)</td><td>205.00 <b>(+32.43%)</b></td><td>102.30 <b>(-23.02%)</b></td><td>50.48 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>262.20 (n/a)</td><td>188.24 (n/a)</td><td>154.80 (n/a)</td><td>132.90 (n/a)</td><td>65.56 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 <b>(-29.71%)</b></td><td>0.06 (-15.99%)</td><td>0.06 (-15.49%)</td><td>0.05 (+8.12%)</td><td>0.01 <b>(-66.68%)</b></td><td>224.00 (-7.51%)</td><td>200.72 (+12.98%)</td><td>209.80 (+18.33%)</td><td>176.70 <b>(+42.27%)</b></td><td>21.40 <b>(-56.20%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>242.20 (n/a)</td><td>177.66 (n/a)</td><td>177.30 (n/a)</td><td>124.20 (n/a)</td><td>48.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 <b>(-22.77%)</b></td><td>0.06 (-13.98%)</td><td>0.06 <b>(-20.54%)</b></td><td>0.05 <b>(+33.99%)</b></td><td>0.01 <b>(-66.84%)</b></td><td>236.10 <b>(-25.38%)</b></td><td>210.88 (+7.93%)</td><td>211.50 <b>(+25.89%)</b></td><td>177.90 <b>(+29.48%)</b></td><td>21.48 <b>(-69.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>316.40 (n/a)</td><td>195.38 (n/a)</td><td>168.00 (n/a)</td><td>137.40 (n/a)</td><td>71.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (+15.31%)</td><td>0.16 (+8.95%)</td><td>0.13 (-6.21%)</td><td>0.10 (-3.06%)</td><td>0.05 <b>(+62.31%)</b></td><td>238.30 (+3.16%)</td><td>170.72 (-3.92%)</td><td>186.90 (+6.62%)</td><td>110.90 (-13.29%)</td><td>52.57 <b>(+42.04%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>231.00 (n/a)</td><td>177.68 (n/a)</td><td>175.30 (n/a)</td><td>127.90 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (-4.50%)</td><td>0.13 (-13.70%)</td><td>0.13 (-18.09%)</td><td>0.11 (-12.31%)</td><td>0.02 (+1.93%)</td><td>233.00 (+14.05%)</td><td>196.00 (+16.35%)</td><td>191.80 <b>(+22.09%)</b></td><td>156.00 (+4.70%)</td><td>30.25 <b>(+24.03%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>204.30 (n/a)</td><td>168.46 (n/a)</td><td>157.10 (n/a)</td><td>149.00 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (+8.82%)</td><td>0.14 (-8.71%)</td><td>0.14 (-12.34%)</td><td>0.09 <b>(-25.70%)</b></td><td>0.04 <b>(+55.48%)</b></td><td>275.90 <b>(+34.59%)</b></td><td>183.70 (+14.50%)</td><td>169.90 (+14.10%)</td><td>122.10 (-8.13%)</td><td>56.48 <b>(+96.07%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>205.00 (n/a)</td><td>160.44 (n/a)</td><td>148.90 (n/a)</td><td>132.90 (n/a)</td><td>28.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (-8.92%)</td><td>0.14 (+3.43%)</td><td>0.15 (+14.07%)</td><td>0.11 (+6.89%)</td><td>0.02 <b>(-24.33%)</b></td><td>215.20 (-6.48%)</td><td>175.26 (-4.54%)</td><td>163.10 (-12.36%)</td><td>146.20 (+9.76%)</td><td>28.54 <b>(-20.17%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>230.10 (n/a)</td><td>183.60 (n/a)</td><td>186.10 (n/a)</td><td>133.20 (n/a)</td><td>35.75 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 <b>(-21.44%)</b></td><td>0.13 (-18.11%)</td><td>0.13 (-16.43%)</td><td>0.11 (-4.29%)</td><td>0.02 <b>(-48.12%)</b></td><td>226.10 (+4.48%)</td><td>192.78 (+19.53%)</td><td>195.10 (+19.62%)</td><td>164.90 <b>(+27.34%)</b></td><td>23.97 <b>(-30.89%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.40 (n/a)</td><td>161.28 (n/a)</td><td>163.10 (n/a)</td><td>129.50 (n/a)</td><td>34.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (-6.14%)</td><td>0.14 (-11.78%)</td><td>0.14 (-16.22%)</td><td>0.11 (-6.64%)</td><td>0.03 (-0.03%)</td><td>221.30 (+7.12%)</td><td>175.54 (+13.79%)</td><td>181.70 (+19.38%)</td><td>136.30 (+6.57%)</td><td>35.90 (+12.07%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>206.60 (n/a)</td><td>154.26 (n/a)</td><td>152.20 (n/a)</td><td>127.90 (n/a)</td><td>32.04 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 <b>(-20.69%)</b></td><td>0.11 (-17.39%)</td><td>0.11 (-12.90%)</td><td>0.07 <b>(-36.34%)</b></td><td>0.03 (+8.65%)</td><td>334.90 <b>(+57.08%)</b></td><td>233.16 <b>(+25.61%)</b></td><td>224.60 (+14.77%)</td><td>167.30 <b>(+26.07%)</b></td><td>69.58 <b>(+109.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.20 (n/a)</td><td>185.62 (n/a)</td><td>195.70 (n/a)</td><td>132.70 (n/a)</td><td>33.26 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 <b>(+22.86%)</b></td><td>0.14 (+6.11%)</td><td>0.13 (+1.31%)</td><td>0.10 (-18.63%)</td><td>0.04 <b>(+178.48%)</b></td><td>249.60 <b>(+22.90%)</b></td><td>183.68 (-1.30%)</td><td>185.10 (-1.33%)</td><td>129.00 (-18.61%)</td><td>47.21 <b>(+181.20%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>186.10 (n/a)</td><td>187.60 (n/a)</td><td>158.50 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (-17.13%)</td><td>0.25 (-9.56%)</td><td>0.25 (-3.75%)</td><td>0.17 (-8.12%)</td><td>0.05 <b>(-28.51%)</b></td><td>281.30 (+8.86%)</td><td>205.14 (+8.97%)</td><td>196.30 (+3.86%)</td><td>156.60 <b>(+20.65%)</b></td><td>46.01 (-2.32%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>258.40 (n/a)</td><td>188.26 (n/a)</td><td>189.00 (n/a)</td><td>129.80 (n/a)</td><td>47.10 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 <b>(-22.40%)</b></td><td>0.25 (-19.76%)</td><td>0.25 (-14.69%)</td><td>0.21 (-13.57%)</td><td>0.04 <b>(-35.40%)</b></td><td>231.50 (+15.69%)</td><td>197.28 <b>(+23.35%)</b></td><td>198.60 (+17.24%)</td><td>161.10 <b>(+28.88%)</b></td><td>29.67 (-1.68%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>200.10 (n/a)</td><td>159.94 (n/a)</td><td>169.40 (n/a)</td><td>125.00 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.35 (-9.14%)</td><td>0.29 (+5.35%)</td><td>0.28 (+10.16%)</td><td>0.23 (+8.62%)</td><td>0.04 <b>(-38.63%)</b></td><td>215.00 (-7.92%)</td><td>171.96 (-8.04%)</td><td>172.50 (-9.26%)</td><td>142.30 (+10.05%)</td><td>27.77 <b>(-38.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>233.50 (n/a)</td><td>187.00 (n/a)</td><td>190.10 (n/a)</td><td>129.30 (n/a)</td><td>45.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.30 <b>(-23.48%)</b></td><td>0.25 (-9.28%)</td><td>0.24 (-13.27%)</td><td>0.21 (+8.82%)</td><td>0.04 <b>(-51.72%)</b></td><td>235.00 (-8.10%)</td><td>199.28 (+6.00%)</td><td>208.20 (+15.35%)</td><td>163.50 <b>(+30.70%)</b></td><td>27.96 <b>(-41.94%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>255.70 (n/a)</td><td>188.00 (n/a)</td><td>180.50 (n/a)</td><td>125.10 (n/a)</td><td>48.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.34 (-12.67%)</td><td>0.27 (-13.36%)</td><td>0.29 (-0.09%)</td><td>0.19 <b>(-23.55%)</b></td><td>0.07 (+5.21%)</td><td>257.50 <b>(+30.78%)</b></td><td>189.30 (+17.81%)</td><td>169.50 (+0.06%)</td><td>145.40 (+14.49%)</td><td>49.61 <b>(+60.53%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>196.90 (n/a)</td><td>160.68 (n/a)</td><td>169.40 (n/a)</td><td>127.00 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.29 <b>(-30.59%)</b></td><td>0.25 (-18.39%)</td><td>0.26 (-7.23%)</td><td>0.21 (-8.14%)</td><td>0.03 <b>(-54.79%)</b></td><td>230.50 (+8.83%)</td><td>201.12 (+19.32%)</td><td>191.70 (+7.82%)</td><td>171.00 <b>(+44.06%)</b></td><td>26.54 <b>(-26.17%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>211.80 (n/a)</td><td>168.56 (n/a)</td><td>177.80 (n/a)</td><td>118.70 (n/a)</td><td>35.95 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.33 (-4.74%)</td><td>0.23 (-15.15%)</td><td>0.22 (-19.98%)</td><td>0.15 (-13.12%)</td><td>0.07 (+0.42%)</td><td>324.90 (+15.13%)</td><td>231.32 (+18.99%)</td><td>221.20 <b>(+24.97%)</b></td><td>148.30 (+5.03%)</td><td>65.59 (+18.33%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>282.20 (n/a)</td><td>194.40 (n/a)</td><td>177.00 (n/a)</td><td>141.20 (n/a)</td><td>55.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.34 (+10.02%)</td><td>0.25 (-8.27%)</td><td>0.23 (-14.69%)</td><td>0.20 (-15.70%)</td><td>0.06 <b>(+88.46%)</b></td><td>250.60 (+18.60%)</td><td>205.72 (+12.02%)</td><td>213.10 (+17.22%)</td><td>143.00 (-9.09%)</td><td>41.11 <b>(+97.86%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>211.30 (n/a)</td><td>183.64 (n/a)</td><td>181.80 (n/a)</td><td>157.30 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 <b>(+22.46%)</b></td><td>0.02 <b>(+21.22%)</b></td><td>0.02 <b>(+26.19%)</b></td><td>0.01 (+9.86%)</td><td>0.00 <b>(+46.91%)</b></td><td>179.80 (-9.01%)</td><td>149.88 (-16.96%)</td><td>144.70 <b>(-20.71%)</b></td><td>121.30 (-18.32%)</td><td>21.65 (+9.60%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>197.60 (n/a)</td><td>180.50 (n/a)</td><td>182.50 (n/a)</td><td>148.50 (n/a)</td><td>19.75 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (-4.57%)</td><td>0.02 (+3.43%)</td><td>0.02 (+12.29%)</td><td>0.01 (+14.82%)</td><td>0.00 (-16.82%)</td><td>234.60 (-12.89%)</td><td>173.98 (-5.59%)</td><td>165.30 (-10.94%)</td><td>123.60 (+4.83%)</td><td>41.96 <b>(-23.71%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>269.30 (n/a)</td><td>184.28 (n/a)</td><td>185.60 (n/a)</td><td>117.90 (n/a)</td><td>55.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 <b>(+21.20%)</b></td><td>0.02 <b>(+26.39%)</b></td><td>0.02 <b>(+32.84%)</b></td><td>0.01 <b>(+36.78%)</b></td><td>0.00 (+8.66%)</td><td>201.50 <b>(-26.91%)</b></td><td>159.70 <b>(-21.82%)</b></td><td>155.40 <b>(-24.71%)</b></td><td>123.00 (-17.51%)</td><td>31.80 <b>(-34.11%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>275.70 (n/a)</td><td>204.26 (n/a)</td><td>206.40 (n/a)</td><td>149.10 (n/a)</td><td>48.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 <b>(+50.36%)</b></td><td>0.02 (+15.87%)</td><td>0.01 (+5.52%)</td><td>0.01 (-4.35%)</td><td>0.00 <b>(+412.24%)</b></td><td>202.40 (+4.55%)</td><td>166.02 (-9.90%)</td><td>177.60 (-5.23%)</td><td>111.00 <b>(-33.49%)</b></td><td>36.10 <b>(+254.21%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>193.60 (n/a)</td><td>184.26 (n/a)</td><td>187.40 (n/a)</td><td>166.90 (n/a)</td><td>10.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 <b>(+24.25%)</b></td><td>0.02 <b>(+31.27%)</b></td><td>0.02 <b>(+68.69%)</b></td><td>0.01 <b>(-37.85%)</b></td><td>0.01 <b>(+115.91%)</b></td><td>370.60 <b>(+60.92%)</b></td><td>181.12 (-10.73%)</td><td>129.60 <b>(-40.74%)</b></td><td>112.30 (-19.56%)</td><td>108.65 <b>(+195.19%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>230.30 (n/a)</td><td>202.88 (n/a)</td><td>218.70 (n/a)</td><td>139.60 (n/a)</td><td>36.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (-7.07%)</td><td>0.01 (+10.03%)</td><td>0.01 (+15.67%)</td><td>0.01 (+11.72%)</td><td>0.00 <b>(-38.05%)</b></td><td>211.70 (-10.49%)</td><td>181.62 (-10.54%)</td><td>181.20 (-13.55%)</td><td>159.20 (+7.64%)</td><td>20.61 <b>(-38.21%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>236.50 (n/a)</td><td>203.02 (n/a)</td><td>209.60 (n/a)</td><td>147.90 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (+6.44%)</td><td>0.01 (+14.33%)</td><td>0.02 <b>(+31.08%)</b></td><td>0.01 (-6.24%)</td><td>0.00 <b>(+50.69%)</b></td><td>270.20 (+6.63%)</td><td>195.64 (-10.12%)</td><td>172.70 <b>(-23.72%)</b></td><td>154.70 (-6.07%)</td><td>50.81 <b>(+50.61%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>253.40 (n/a)</td><td>217.68 (n/a)</td><td>226.40 (n/a)</td><td>164.70 (n/a)</td><td>33.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 <b>(+20.72%)</b></td><td>0.01 (+12.24%)</td><td>0.01 (+13.86%)</td><td>0.01 <b>(+20.48%)</b></td><td>0.00 <b>(+23.69%)</b></td><td>283.10 (-16.98%)</td><td>215.52 (-10.87%)</td><td>198.20 (-12.15%)</td><td>162.30 (-17.15%)</td><td>46.61 (-18.12%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>341.00 (n/a)</td><td>241.80 (n/a)</td><td>225.60 (n/a)</td><td>195.90 (n/a)</td><td>56.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 <b>(+20.69%)</b></td><td>0.03 (+12.01%)</td><td>0.03 (+13.22%)</td><td>0.03 (+16.25%)</td><td>0.00 <b>(+36.32%)</b></td><td>173.50 (-13.98%)</td><td>154.72 (-10.43%)</td><td>154.80 (-11.69%)</td><td>127.40 (-17.11%)</td><td>18.78 (-1.77%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.70 (n/a)</td><td>172.74 (n/a)</td><td>175.30 (n/a)</td><td>153.70 (n/a)</td><td>19.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+16.09%)</td><td>0.03 <b>(+20.49%)</b></td><td>0.04 <b>(+41.45%)</b></td><td>0.03 <b>(+20.65%)</b></td><td>0.01 (-12.33%)</td><td>189.60 (-17.10%)</td><td>155.42 (-18.49%)</td><td>146.50 <b>(-29.30%)</b></td><td>123.00 (-13.87%)</td><td>26.09 <b>(-36.63%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>190.68 (n/a)</td><td>207.20 (n/a)</td><td>142.80 (n/a)</td><td>41.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 <b>(+33.95%)</b></td><td>0.03 (+10.36%)</td><td>0.03 (+5.61%)</td><td>0.02 (-3.94%)</td><td>0.01 <b>(+107.51%)</b></td><td>216.90 (+4.08%)</td><td>167.42 (-6.81%)</td><td>163.50 (-5.27%)</td><td>118.10 <b>(-25.35%)</b></td><td>36.64 <b>(+59.90%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>179.66 (n/a)</td><td>172.60 (n/a)</td><td>158.20 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 <b>(+22.47%)</b></td><td>0.03 (+18.02%)</td><td>0.03 (+3.38%)</td><td>0.03 <b>(+58.18%)</b></td><td>0.01 (-5.93%)</td><td>197.60 <b>(-36.77%)</b></td><td>161.84 (-18.61%)</td><td>173.00 (-3.30%)</td><td>117.10 (-18.34%)</td><td>30.49 <b>(-54.41%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>312.50 (n/a)</td><td>198.84 (n/a)</td><td>178.90 (n/a)</td><td>143.40 (n/a)</td><td>66.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 <b>(+23.61%)</b></td><td>0.03 (+11.74%)</td><td>0.03 (+13.23%)</td><td>0.03 (+8.70%)</td><td>0.01 <b>(+73.92%)</b></td><td>205.70 (-8.01%)</td><td>168.34 (-8.64%)</td><td>155.70 (-11.68%)</td><td>123.80 (-19.14%)</td><td>35.43 <b>(+33.70%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.60 (n/a)</td><td>184.26 (n/a)</td><td>176.30 (n/a)</td><td>153.10 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 <b>(+30.02%)</b></td><td>0.03 (+15.39%)</td><td>0.03 (+19.38%)</td><td>0.02 (-7.38%)</td><td>0.01 <b>(+92.38%)</b></td><td>253.50 (+7.96%)</td><td>170.88 (-9.51%)</td><td>159.30 (-16.25%)</td><td>119.70 <b>(-23.07%)</b></td><td>51.47 <b>(+64.48%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.80 (n/a)</td><td>188.84 (n/a)</td><td>190.20 (n/a)</td><td>155.60 (n/a)</td><td>31.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (-3.73%)</td><td>0.03 (+2.87%)</td><td>0.03 (+14.46%)</td><td>0.02 (-6.78%)</td><td>0.01 (+8.05%)</td><td>271.00 (+7.28%)</td><td>183.80 (-1.68%)</td><td>163.30 (-12.63%)</td><td>148.70 (+3.84%)</td><td>50.21 <b>(+22.03%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.60 (n/a)</td><td>186.94 (n/a)</td><td>186.90 (n/a)</td><td>143.20 (n/a)</td><td>41.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (+10.77%)</td><td>0.03 (+19.94%)</td><td>0.03 <b>(+31.47%)</b></td><td>0.02 (+9.76%)</td><td>0.00 <b>(+31.32%)</b></td><td>240.10 (-8.92%)</td><td>191.62 (-16.19%)</td><td>173.80 <b>(-23.97%)</b></td><td>169.80 (-9.73%)</td><td>30.26 (+7.95%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>263.60 (n/a)</td><td>228.64 (n/a)</td><td>228.60 (n/a)</td><td>188.10 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (+3.14%)</td><td>0.06 (+7.99%)</td><td>0.06 <b>(+22.74%)</b></td><td>0.04 (-8.71%)</td><td>0.02 <b>(+30.99%)</b></td><td>242.40 (+9.53%)</td><td>175.68 (-4.33%)</td><td>165.30 (-18.49%)</td><td>123.30 (-3.07%)</td><td>54.11 <b>(+36.48%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>183.64 (n/a)</td><td>202.80 (n/a)</td><td>127.20 (n/a)</td><td>39.64 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 <b>(+39.81%)</b></td><td>0.07 (+10.71%)</td><td>0.06 (+3.84%)</td><td>0.05 <b>(+30.51%)</b></td><td>0.03 <b>(+46.67%)</b></td><td>201.40 <b>(-23.39%)</b></td><td>160.02 (-8.51%)</td><td>169.20 (-3.70%)</td><td>89.00 <b>(-28.51%)</b></td><td>44.78 (-19.69%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>262.90 (n/a)</td><td>174.90 (n/a)</td><td>175.70 (n/a)</td><td>124.50 (n/a)</td><td>55.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (+12.85%)</td><td>0.07 (+15.26%)</td><td>0.07 (+12.62%)</td><td>0.06 (+19.63%)</td><td>0.01 (+6.72%)</td><td>181.20 (-16.42%)</td><td>144.78 (-13.69%)</td><td>148.80 (-11.22%)</td><td>114.40 (-11.39%)</td><td>26.79 <b>(-21.77%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>167.74 (n/a)</td><td>167.60 (n/a)</td><td>129.10 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (-13.86%)</td><td>0.05 (-17.99%)</td><td>0.05 (-19.47%)</td><td>0.03 <b>(-30.42%)</b></td><td>0.02 (+1.50%)</td><td>319.10 <b>(+43.67%)</b></td><td>213.70 <b>(+26.06%)</b></td><td>213.60 <b>(+24.19%)</b></td><td>142.30 (+16.07%)</td><td>71.07 <b>(+67.62%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>222.10 (n/a)</td><td>169.52 (n/a)</td><td>172.00 (n/a)</td><td>122.60 (n/a)</td><td>42.40 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 <b>(+28.11%)</b></td><td>0.07 (+18.93%)</td><td>0.07 <b>(+20.89%)</b></td><td>0.06 (+15.63%)</td><td>0.02 <b>(+20.47%)</b></td><td>182.60 (-13.54%)</td><td>147.60 (-16.06%)</td><td>160.10 (-17.30%)</td><td>102.80 <b>(-21.94%)</b></td><td>31.18 (-19.39%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>175.84 (n/a)</td><td>193.60 (n/a)</td><td>131.70 (n/a)</td><td>38.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 <b>(+22.87%)</b></td><td>0.06 <b>(+23.91%)</b></td><td>0.06 <b>(+31.58%)</b></td><td>0.03 (-4.70%)</td><td>0.02 <b>(+60.46%)</b></td><td>334.30 (+4.93%)</td><td>197.38 (-14.96%)</td><td>169.30 <b>(-24.01%)</b></td><td>141.70 (-18.61%)</td><td>79.59 <b>(+39.34%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>318.60 (n/a)</td><td>232.10 (n/a)</td><td>222.80 (n/a)</td><td>174.10 (n/a)</td><td>57.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 <b>(+38.86%)</b></td><td>0.06 (+14.11%)</td><td>0.05 (-4.21%)</td><td>0.05 (+16.27%)</td><td>0.02 <b>(+94.95%)</b></td><td>216.90 (-14.00%)</td><td>177.84 (-8.52%)</td><td>198.20 (+4.37%)</td><td>103.90 <b>(-28.00%)</b></td><td>47.41 <b>(+20.83%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>252.20 (n/a)</td><td>194.40 (n/a)</td><td>189.90 (n/a)</td><td>144.30 (n/a)</td><td>39.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (+4.29%)</td><td>0.05 (+5.73%)</td><td>0.05 (-0.46%)</td><td>0.04 (+5.75%)</td><td>0.01 (+15.35%)</td><td>259.20 (-5.44%)</td><td>207.32 (-4.60%)</td><td>222.80 (+0.45%)</td><td>146.80 (-4.11%)</td><td>46.24 (+7.52%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>274.10 (n/a)</td><td>217.32 (n/a)</td><td>221.80 (n/a)</td><td>153.10 (n/a)</td><td>43.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (-3.42%)</td><td>0.11 (-7.55%)</td><td>0.11 (-3.80%)</td><td>0.09 <b>(-20.61%)</b></td><td>0.02 (+18.28%)</td><td>244.20 <b>(+26.01%)</b></td><td>189.62 (+9.75%)</td><td>185.10 (+3.93%)</td><td>137.60 (+3.54%)</td><td>38.06 <b>(+52.62%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>193.80 (n/a)</td><td>172.78 (n/a)</td><td>178.10 (n/a)</td><td>132.90 (n/a)</td><td>24.94 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (-10.03%)</td><td>0.12 (-9.79%)</td><td>0.12 (-10.51%)</td><td>0.09 (+3.01%)</td><td>0.02 (-15.19%)</td><td>223.90 (-2.95%)</td><td>182.78 (+9.92%)</td><td>172.00 (+11.69%)</td><td>147.90 (+11.12%)</td><td>33.33 (-11.38%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>230.70 (n/a)</td><td>166.28 (n/a)</td><td>154.00 (n/a)</td><td>133.10 (n/a)</td><td>37.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 <b>(+23.73%)</b></td><td>0.14 (+13.49%)</td><td>0.14 (+11.18%)</td><td>0.11 (+4.48%)</td><td>0.04 <b>(+54.56%)</b></td><td>193.50 (-4.30%)</td><td>154.06 (-10.04%)</td><td>153.80 (-10.06%)</td><td>109.10 (-19.19%)</td><td>36.02 (+19.15%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>202.20 (n/a)</td><td>171.26 (n/a)</td><td>171.00 (n/a)</td><td>135.00 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (+13.05%)</td><td>0.13 (+19.88%)</td><td>0.14 (+19.48%)</td><td>0.11 <b>(+21.80%)</b></td><td>0.01 (-8.98%)</td><td>183.00 (-17.86%)</td><td>160.44 (-17.09%)</td><td>150.80 (-16.32%)</td><td>144.70 (-11.55%)</td><td>17.24 <b>(-35.61%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>193.52 (n/a)</td><td>180.20 (n/a)</td><td>163.60 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 <b>(-21.19%)</b></td><td>0.12 (-4.18%)</td><td>0.13 (+13.73%)</td><td>0.10 (+10.98%)</td><td>0.02 <b>(-46.88%)</b></td><td>210.90 (-9.91%)</td><td>176.48 (-0.50%)</td><td>161.90 (-12.06%)</td><td>148.30 <b>(+26.86%)</b></td><td>31.51 <b>(-38.08%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>234.10 (n/a)</td><td>177.36 (n/a)</td><td>184.10 (n/a)</td><td>116.90 (n/a)</td><td>50.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (-11.80%)</td><td>0.12 (+8.75%)</td><td>0.13 <b>(+29.11%)</b></td><td>0.09 <b>(+26.35%)</b></td><td>0.02 <b>(-36.46%)</b></td><td>243.50 <b>(-20.84%)</b></td><td>184.70 (-12.65%)</td><td>164.80 <b>(-22.56%)</b></td><td>153.90 (+13.33%)</td><td>38.67 <b>(-42.87%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>307.60 (n/a)</td><td>211.44 (n/a)</td><td>212.80 (n/a)</td><td>135.80 (n/a)</td><td>67.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (-4.65%)</td><td>0.12 (+10.07%)</td><td>0.11 (+5.26%)</td><td>0.10 <b>(+49.98%)</b></td><td>0.01 <b>(-50.34%)</b></td><td>218.10 <b>(-33.34%)</b></td><td>183.60 (-14.30%)</td><td>184.10 (-5.01%)</td><td>155.00 (+4.87%)</td><td>23.15 <b>(-66.35%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>327.20 (n/a)</td><td>214.24 (n/a)</td><td>193.80 (n/a)</td><td>147.80 (n/a)</td><td>68.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (-8.89%)</td><td>0.11 (+4.14%)</td><td>0.11 <b>(+24.53%)</b></td><td>0.08 (+3.03%)</td><td>0.02 <b>(-28.05%)</b></td><td>259.30 (-2.92%)</td><td>200.92 (-5.87%)</td><td>190.50 (-19.69%)</td><td>165.60 (+9.74%)</td><td>37.81 <b>(-22.34%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>267.10 (n/a)</td><td>213.46 (n/a)</td><td>237.20 (n/a)</td><td>150.90 (n/a)</td><td>48.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>141.60 (n/a)</td><td>128.60 (n/a)</td><td>121.60 (n/a)</td><td>25.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>178.60 (n/a)</td><td>167.94 (n/a)</td><td>169.00 (n/a)</td><td>157.80 (n/a)</td><td>8.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>163.58 (n/a)</td><td>169.80 (n/a)</td><td>130.30 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>175.02 (n/a)</td><td>155.70 (n/a)</td><td>131.10 (n/a)</td><td>44.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.90 (n/a)</td><td>145.42 (n/a)</td><td>135.10 (n/a)</td><td>122.50 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>248.00 (n/a)</td><td>178.42 (n/a)</td><td>164.10 (n/a)</td><td>135.70 (n/a)</td><td>42.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>193.80 (n/a)</td><td>161.34 (n/a)</td><td>171.80 (n/a)</td><td>128.90 (n/a)</td><td>29.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>175.70 (n/a)</td><td>168.90 (n/a)</td><td>159.50 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.70 (n/a)</td><td>158.40 (n/a)</td><td>143.80 (n/a)</td><td>121.70 (n/a)</td><td>35.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>195.10 (n/a)</td><td>155.58 (n/a)</td><td>155.10 (n/a)</td><td>117.70 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.60 (n/a)</td><td>181.84 (n/a)</td><td>197.70 (n/a)</td><td>131.60 (n/a)</td><td>34.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.80 (n/a)</td><td>173.76 (n/a)</td><td>168.20 (n/a)</td><td>154.00 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.37 (+0.14%)</td><td>0.29 (-10.94%)</td><td>0.29 (-9.52%)</td><td>0.24 (-9.75%)</td><td>0.05 <b>(+26.39%)</b></td><td>204.00 (+10.81%)</td><td>174.82 (+13.33%)</td><td>172.10 (+10.46%)</td><td>133.10 (-0.15%)</td><td>27.62 <b>(+39.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>184.10 (n/a)</td><td>154.26 (n/a)</td><td>155.80 (n/a)</td><td>133.30 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>186.90 (n/a)</td><td>160.00 (n/a)</td><td>169.00 (n/a)</td><td>129.10 (n/a)</td><td>28.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>211.80 (n/a)</td><td>189.86 (n/a)</td><td>198.10 (n/a)</td><td>150.00 (n/a)</td><td>25.90 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>398.50 (n/a)</td><td>246.98 (n/a)</td><td>226.20 (n/a)</td><td>164.30 (n/a)</td><td>89.02 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.60 (n/a)</td><td>165.46 (n/a)</td><td>159.10 (n/a)</td><td>143.30 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.80 (n/a)</td><td>164.20 (n/a)</td><td>163.70 (n/a)</td><td>143.10 (n/a)</td><td>18.45 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>155.34 (n/a)</td><td>157.60 (n/a)</td><td>126.60 (n/a)</td><td>26.34 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>311.30 (n/a)</td><td>208.62 (n/a)</td><td>201.10 (n/a)</td><td>127.50 (n/a)</td><td>69.72 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>215.30 (n/a)</td><td>158.18 (n/a)</td><td>142.30 (n/a)</td><td>126.50 (n/a)</td><td>34.95 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>182.80 (n/a)</td><td>152.82 (n/a)</td><td>162.10 (n/a)</td><td>97.10 (n/a)</td><td>35.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>165.00 (n/a)</td><td>154.96 (n/a)</td><td>161.10 (n/a)</td><td>130.70 (n/a)</td><td>13.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>248.10 (n/a)</td><td>178.88 (n/a)</td><td>170.00 (n/a)</td><td>110.90 (n/a)</td><td>49.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>182.50 (n/a)</td><td>158.38 (n/a)</td><td>158.70 (n/a)</td><td>133.40 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>162.40 (n/a)</td><td>151.42 (n/a)</td><td>151.70 (n/a)</td><td>142.00 (n/a)</td><td>7.57 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>163.50 (n/a)</td><td>151.52 (n/a)</td><td>158.50 (n/a)</td><td>136.50 (n/a)</td><td>13.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>198.80 (n/a)</td><td>166.46 (n/a)</td><td>156.50 (n/a)</td><td>141.30 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>178.50 (n/a)</td><td>162.34 (n/a)</td><td>167.40 (n/a)</td><td>141.50 (n/a)</td><td>14.07 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>175.10 (n/a)</td><td>157.36 (n/a)</td><td>155.50 (n/a)</td><td>140.40 (n/a)</td><td>13.38 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>214.70 (n/a)</td><td>173.28 (n/a)</td><td>168.70 (n/a)</td><td>141.60 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.85 (+1.68%)</td><td>13.88 (+3.49%)</td><td>14.11 (+7.50%)</td><td>12.79 (-1.96%)</td><td>0.83 <b>(+24.12%)</b></td><td>4356.10 (+2.00%)</td><td>4024.90 (-3.27%)</td><td>3947.70 (-6.98%)</td><td>3750.80 (-1.65%)</td><td>244.66 <b>(+25.46%)</b></td><td>14313.37 (+1.68%)</td><td>13377.66 (+3.49%)</td><td>13599.66 (+7.50%)</td><td>12324.45 (-1.96%)</td><td>801.26 <b>(+24.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.61 (n/a)</td><td>13.41 (n/a)</td><td>13.13 (n/a)</td><td>13.04 (n/a)</td><td>0.67 (n/a)</td><td>4270.80 (n/a)</td><td>4161.04 (n/a)</td><td>4243.70 (n/a)</td><td>3813.70 (n/a)</td><td>195.01 (n/a)</td><td>14077.29 (n/a)</td><td>12926.46 (n/a)</td><td>12650.93 (n/a)</td><td>12570.71 (n/a)</td><td>645.57 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>16.61 (+9.68%)</td><td>14.15 (-1.19%)</td><td>14.57 (+0.18%)</td><td>11.25 (-12.82%)</td><td>2.07 <b>(+146.90%)</b></td><td>1164.70 (+14.69%)</td><td>943.46 (+2.76%)</td><td>899.80 (-0.18%)</td><td>789.10 (-8.83%)</td><td>146.36 <b>(+156.80%)</b></td><td>10885.83 (+9.68%)</td><td>9271.80 (-1.19%)</td><td>9546.77 (+0.18%)</td><td>7375.05 (-12.82%)</td><td>1354.76 <b>(+146.90%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>15.14 (n/a)</td><td>14.32 (n/a)</td><td>14.54 (n/a)</td><td>12.91 (n/a)</td><td>0.84 (n/a)</td><td>1015.50 (n/a)</td><td>918.14 (n/a)</td><td>901.40 (n/a)</td><td>865.50 (n/a)</td><td>56.99 (n/a)</td><td>9924.97 (n/a)</td><td>9383.19 (n/a)</td><td>9529.50 (n/a)</td><td>8459.22 (n/a)</td><td>548.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.35 (+1.55%)</td><td>13.73 (+2.96%)</td><td>13.84 (+5.51%)</td><td>12.53 (-1.58%)</td><td>0.71 (+15.51%)</td><td>4447.30 (+1.60%)</td><td>4065.48 (-2.82%)</td><td>4024.60 (-5.22%)</td><td>3881.40 (-1.52%)</td><td>223.13 (+16.73%)</td><td>13831.92 (+1.55%)</td><td>13235.79 (+2.96%)</td><td>13339.72 (+5.51%)</td><td>12071.89 (-1.58%)</td><td>687.62 (+15.51%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.13 (n/a)</td><td>13.34 (n/a)</td><td>13.12 (n/a)</td><td>12.73 (n/a)</td><td>0.62 (n/a)</td><td>4377.10 (n/a)</td><td>4183.46 (n/a)</td><td>4246.40 (n/a)</td><td>3941.50 (n/a)</td><td>191.16 (n/a)</td><td>13621.08 (n/a)</td><td>12854.91 (n/a)</td><td>12642.99 (n/a)</td><td>12265.37 (n/a)</td><td>595.30 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.86 (-9.33%)</td><td>12.97 (-11.51%)</td><td>13.04 (-14.75%)</td><td>10.64 (-0.51%)</td><td>1.84 (-18.89%)</td><td>1678.60 (+0.51%)</td><td>1399.60 (+12.20%)</td><td>1369.40 (+17.29%)</td><td>1201.60 (+10.29%)</td><td>204.93 (-14.18%)</td><td>11169.74 (-9.33%)</td><td>9751.24 (-11.51%)</td><td>9801.22 (-14.75%)</td><td>7995.83 (-0.51%)</td><td>1384.24 (-18.89%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>16.39 (n/a)</td><td>14.66 (n/a)</td><td>15.30 (n/a)</td><td>10.69 (n/a)</td><td>2.27 (n/a)</td><td>1670.10 (n/a)</td><td>1247.44 (n/a)</td><td>1167.50 (n/a)</td><td>1089.50 (n/a)</td><td>238.78 (n/a)</td><td>12318.94 (n/a)</td><td>11020.21 (n/a)</td><td>11496.54 (n/a)</td><td>8036.47 (n/a)</td><td>1706.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>11.15 (+4.12%)</td><td>10.75 (+2.64%)</td><td>10.63 (+0.15%)</td><td>10.58 (+7.86%)</td><td>0.23 <b>(-36.88%)</b></td><td>7739.70 (-7.29%)</td><td>7623.06 (-2.63%)</td><td>7706.60 (-0.15%)</td><td>7348.20 (-3.96%)</td><td>162.66 <b>(-44.16%)</b></td><td>14612.26 (+4.12%)</td><td>14090.68 (+2.64%)</td><td>13932.76 (+0.15%)</td><td>13873.10 (+7.86%)</td><td>307.46 <b>(-36.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.71 (n/a)</td><td>10.47 (n/a)</td><td>10.61 (n/a)</td><td>9.81 (n/a)</td><td>0.37 (n/a)</td><td>8347.90 (n/a)</td><td>7829.32 (n/a)</td><td>7718.10 (n/a)</td><td>7651.20 (n/a)</td><td>291.30 (n/a)</td><td>14033.60 (n/a)</td><td>13728.83 (n/a)</td><td>13911.95 (n/a)</td><td>12862.38 (n/a)</td><td>487.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>15.65 <b>(+32.59%)</b></td><td>14.62 <b>(+32.23%)</b></td><td>14.93 <b>(+34.70%)</b></td><td>12.60 <b>(+23.03%)</b></td><td>1.17 <b>(+78.54%)</b></td><td>1706.20 (-18.72%)</td><td>1478.96 <b>(-24.16%)</b></td><td>1439.90 <b>(-25.76%)</b></td><td>1373.30 <b>(-24.58%)</b></td><td>130.17 (+11.86%)</td><td>12509.77 <b>(+32.59%)</b></td><td>11681.89 <b>(+32.23%)</b></td><td>11931.11 <b>(+34.70%)</b></td><td>10068.96 <b>(+23.03%)</b></td><td>934.81 <b>(+78.54%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>11.80 (n/a)</td><td>11.05 (n/a)</td><td>11.08 (n/a)</td><td>10.24 (n/a)</td><td>0.66 (n/a)</td><td>2099.10 (n/a)</td><td>1950.14 (n/a)</td><td>1939.60 (n/a)</td><td>1820.90 (n/a)</td><td>116.37 (n/a)</td><td>9434.59 (n/a)</td><td>8834.48 (n/a)</td><td>8857.47 (n/a)</td><td>8184.27 (n/a)</td><td>523.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>10.46 (-1.42%)</td><td>10.41 (+0.08%)</td><td>10.41 (-0.45%)</td><td>10.33 (+2.40%)</td><td>0.05 <b>(-74.79%)</b></td><td>7929.30 (-2.34%)</td><td>7869.96 (-0.11%)</td><td>7872.90 (+0.45%)</td><td>7828.50 (+1.44%)</td><td>40.15 <b>(-75.04%)</b></td><td>13715.79 (-1.42%)</td><td>13643.86 (+0.08%)</td><td>13638.39 (-0.45%)</td><td>13541.49 (+2.40%)</td><td>69.45 <b>(-74.79%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.62 (n/a)</td><td>10.40 (n/a)</td><td>10.45 (n/a)</td><td>10.09 (n/a)</td><td>0.21 (n/a)</td><td>8119.30 (n/a)</td><td>7878.34 (n/a)</td><td>7837.70 (n/a)</td><td>7717.30 (n/a)</td><td>160.82 (n/a)</td><td>13913.39 (n/a)</td><td>13633.51 (n/a)</td><td>13699.70 (n/a)</td><td>13224.49 (n/a)</td><td>275.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.35 (-17.64%)</td><td>3.08 (-11.65%)</td><td>3.05 (-18.54%)</td><td>2.85 (-0.51%)</td><td>0.18 <b>(-68.20%)</b></td><td>482.40 (+0.52%)</td><td>448.24 (+11.09%)</td><td>451.50 <b>(+22.79%)</b></td><td>411.40 <b>(+21.43%)</b></td><td>25.30 <b>(-62.32%)</b></td><td>652.55 (-17.64%)</td><td>600.45 (-11.65%)</td><td>594.59 (-18.54%)</td><td>556.47 (-0.51%)</td><td>34.39 <b>(-68.20%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.06 (n/a)</td><td>3.48 (n/a)</td><td>3.74 (n/a)</td><td>2.87 (n/a)</td><td>0.55 (n/a)</td><td>479.90 (n/a)</td><td>403.50 (n/a)</td><td>367.70 (n/a)</td><td>338.80 (n/a)</td><td>67.15 (n/a)</td><td>792.28 (n/a)</td><td>679.63 (n/a)</td><td>729.96 (n/a)</td><td>559.35 (n/a)</td><td>108.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.88 (+4.49%)</td><td>3.63 (+3.36%)</td><td>3.64 (+4.25%)</td><td>3.32 (+0.84%)</td><td>0.20 (+18.47%)</td><td>414.50 (-0.84%)</td><td>380.38 (-3.18%)</td><td>377.90 (-4.06%)</td><td>355.00 (-4.29%)</td><td>21.46 (+13.63%)</td><td>756.25 (+4.49%)</td><td>707.48 (+3.36%)</td><td>710.43 (+4.25%)</td><td>647.63 (+0.84%)</td><td>38.83 (+18.47%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.71 (n/a)</td><td>3.51 (n/a)</td><td>3.49 (n/a)</td><td>3.29 (n/a)</td><td>0.17 (n/a)</td><td>418.00 (n/a)</td><td>392.88 (n/a)</td><td>393.90 (n/a)</td><td>370.90 (n/a)</td><td>18.88 (n/a)</td><td>723.77 (n/a)</td><td>684.50 (n/a)</td><td>681.45 (n/a)</td><td>642.21 (n/a)</td><td>32.77 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.01 (+14.23%)</td><td>4.71 <b>(+21.28%)</b></td><td>4.79 <b>(+33.43%)</b></td><td>3.62 (+6.39%)</td><td>1.02 <b>(+30.88%)</b></td><td>379.70 (-5.99%)</td><td>303.76 (-16.54%)</td><td>287.30 <b>(-25.05%)</b></td><td>228.80 (-12.47%)</td><td>66.43 (+13.11%)</td><td>1173.05 (+14.22%)</td><td>918.32 <b>(+21.28%)</b></td><td>934.38 <b>(+33.43%)</b></td><td>707.02 (+6.39%)</td><td>199.61 <b>(+30.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>5.27 (n/a)</td><td>3.88 (n/a)</td><td>3.59 (n/a)</td><td>3.41 (n/a)</td><td>0.78 (n/a)</td><td>403.90 (n/a)</td><td>363.94 (n/a)</td><td>383.30 (n/a)</td><td>261.40 (n/a)</td><td>58.73 (n/a)</td><td>1026.96 (n/a)</td><td>757.21 (n/a)</td><td>700.27 (n/a)</td><td>664.58 (n/a)</td><td>152.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.65 <b>(-27.27%)</b></td><td>3.96 (-12.66%)</td><td>3.73 (-13.07%)</td><td>3.54 (+0.97%)</td><td>0.45 <b>(-62.24%)</b></td><td>388.40 (-0.97%)</td><td>350.92 (+9.99%)</td><td>369.00 (+15.02%)</td><td>295.90 <b>(+37.50%)</b></td><td>37.40 <b>(-50.01%)</b></td><td>907.26 <b>(-27.27%)</b></td><td>772.44 (-12.66%)</td><td>727.40 (-13.07%)</td><td>691.10 (+0.97%)</td><td>87.86 <b>(-62.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.40 (n/a)</td><td>4.53 (n/a)</td><td>4.29 (n/a)</td><td>3.51 (n/a)</td><td>1.19 (n/a)</td><td>392.20 (n/a)</td><td>319.04 (n/a)</td><td>320.80 (n/a)</td><td>215.20 (n/a)</td><td>74.81 (n/a)</td><td>1247.43 (n/a)</td><td>884.38 (n/a)</td><td>836.77 (n/a)</td><td>684.46 (n/a)</td><td>232.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.84 (+17.53%)</td><td>3.51 (+3.15%)</td><td>3.27 (-1.19%)</td><td>3.03 (-2.71%)</td><td>0.75 <b>(+83.86%)</b></td><td>454.00 (+2.78%)</td><td>403.06 (-1.22%)</td><td>421.50 (+1.20%)</td><td>284.50 (-14.92%)</td><td>67.76 <b>(+58.29%)</b></td><td>943.43 (+17.53%)</td><td>685.49 (+3.15%)</td><td>636.88 (-1.19%)</td><td>591.22 (-2.71%)</td><td>145.57 <b>(+83.86%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.12 (n/a)</td><td>3.41 (n/a)</td><td>3.30 (n/a)</td><td>3.12 (n/a)</td><td>0.41 (n/a)</td><td>441.70 (n/a)</td><td>408.02 (n/a)</td><td>416.50 (n/a)</td><td>334.40 (n/a)</td><td>42.81 (n/a)</td><td>802.72 (n/a)</td><td>664.54 (n/a)</td><td>644.58 (n/a)</td><td>607.72 (n/a)</td><td>79.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.50 (+7.97%)</td><td>3.16 (+2.59%)</td><td>3.08 (-0.13%)</td><td>2.68 (-9.60%)</td><td>0.34 <b>(+192.74%)</b></td><td>514.20 (+10.60%)</td><td>439.56 (-1.67%)</td><td>446.90 (+0.13%)</td><td>392.80 (-7.38%)</td><td>49.76 <b>(+194.32%)</b></td><td>683.45 (+7.97%)</td><td>616.78 (+2.59%)</td><td>600.69 (-0.13%)</td><td>522.04 (-9.60%)</td><td>67.15 <b>(+192.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.25 (n/a)</td><td>3.08 (n/a)</td><td>3.08 (n/a)</td><td>2.96 (n/a)</td><td>0.12 (n/a)</td><td>464.90 (n/a)</td><td>447.04 (n/a)</td><td>446.30 (n/a)</td><td>424.10 (n/a)</td><td>16.91 (n/a)</td><td>633.00 (n/a)</td><td>601.18 (n/a)</td><td>601.46 (n/a)</td><td>577.46 (n/a)</td><td>22.94 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.64 (-4.51%)</td><td>3.24 (+0.25%)</td><td>3.37 (+8.95%)</td><td>2.82 (-6.33%)</td><td>0.33 (-3.62%)</td><td>488.20 (+6.76%)</td><td>427.66 (-0.21%)</td><td>408.20 (-8.21%)</td><td>377.80 (+4.71%)</td><td>43.95 (+9.05%)</td><td>710.50 (-4.51%)</td><td>632.90 (+0.25%)</td><td>657.64 (+8.95%)</td><td>549.88 (-6.33%)</td><td>63.47 (-3.62%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.81 (n/a)</td><td>3.24 (n/a)</td><td>3.09 (n/a)</td><td>3.01 (n/a)</td><td>0.34 (n/a)</td><td>457.30 (n/a)</td><td>428.58 (n/a)</td><td>444.70 (n/a)</td><td>360.80 (n/a)</td><td>40.30 (n/a)</td><td>744.09 (n/a)</td><td>631.32 (n/a)</td><td>603.64 (n/a)</td><td>587.04 (n/a)</td><td>65.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.31 (+0.37%)</td><td>1.12 (-1.29%)</td><td>1.08 (-4.86%)</td><td>1.02 (+1.36%)</td><td>0.11 (+3.84%)</td><td>391.90 (-1.33%)</td><td>360.24 (+1.34%)</td><td>373.10 (+5.10%)</td><td>306.30 (-0.36%)</td><td>33.05 (+1.49%)</td><td>109.55 (+0.37%)</td><td>93.83 (-1.29%)</td><td>89.93 (-4.86%)</td><td>85.62 (+1.36%)</td><td>9.38 (+3.84%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.31 (n/a)</td><td>1.14 (n/a)</td><td>1.13 (n/a)</td><td>1.01 (n/a)</td><td>0.11 (n/a)</td><td>397.20 (n/a)</td><td>355.46 (n/a)</td><td>355.00 (n/a)</td><td>307.40 (n/a)</td><td>32.57 (n/a)</td><td>109.14 (n/a)</td><td>95.06 (n/a)</td><td>94.53 (n/a)</td><td>84.47 (n/a)</td><td>9.04 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.74 <b>(+27.99%)</b></td><td>5.39 (+12.68%)</td><td>4.97 (+3.16%)</td><td>4.67 (+7.50%)</td><td>0.83 <b>(+141.13%)</b></td><td>414.10 (-6.99%)</td><td>365.12 (-10.09%)</td><td>389.00 (-3.07%)</td><td>286.80 <b>(-21.87%)</b></td><td>50.61 <b>(+73.05%)</b></td><td>1403.77 <b>(+27.99%)</b></td><td>1121.93 (+12.68%)</td><td>1035.15 (+3.16%)</td><td>972.29 (+7.50%)</td><td>173.56 <b>(+141.13%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>5.27 (n/a)</td><td>4.78 (n/a)</td><td>4.82 (n/a)</td><td>4.34 (n/a)</td><td>0.35 (n/a)</td><td>445.20 (n/a)</td><td>406.08 (n/a)</td><td>401.30 (n/a)</td><td>367.10 (n/a)</td><td>29.25 (n/a)</td><td>1096.76 (n/a)</td><td>995.68 (n/a)</td><td>1003.44 (n/a)</td><td>904.44 (n/a)</td><td>71.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>16.96 (+0.81%)</td><td>12.09 (+1.68%)</td><td>11.09 (+2.52%)</td><td>10.19 (+0.20%)</td><td>2.76 (-0.59%)</td><td>540.50 (-0.20%)</td><td>470.78 (-1.76%)</td><td>496.50 (-2.46%)</td><td>324.60 (-0.82%)</td><td>84.52 (-2.17%)</td><td>6615.01 (+0.81%)</td><td>4715.42 (+1.68%)</td><td>4325.55 (+2.52%)</td><td>3973.15 (+0.20%)</td><td>1076.57 (-0.59%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>16.82 (n/a)</td><td>11.89 (n/a)</td><td>10.82 (n/a)</td><td>10.17 (n/a)</td><td>2.78 (n/a)</td><td>541.60 (n/a)</td><td>479.20 (n/a)</td><td>509.00 (n/a)</td><td>327.30 (n/a)</td><td>86.39 (n/a)</td><td>6561.55 (n/a)</td><td>4637.37 (n/a)</td><td>4219.12 (n/a)</td><td>3965.36 (n/a)</td><td>1082.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.14 (-2.12%)</td><td>8.12 (+2.56%)</td><td>7.87 (+1.76%)</td><td>7.68 (+8.74%)</td><td>0.59 <b>(-31.22%)</b></td><td>716.40 (-8.04%)</td><td>680.98 (-2.96%)</td><td>699.80 (-1.71%)</td><td>602.40 (+2.17%)</td><td>45.85 <b>(-34.80%)</b></td><td>3564.90 (-2.12%)</td><td>3165.98 (+2.56%)</td><td>3068.92 (+1.76%)</td><td>2997.71 (+8.74%)</td><td>230.44 <b>(-31.22%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.34 (n/a)</td><td>7.91 (n/a)</td><td>7.73 (n/a)</td><td>7.07 (n/a)</td><td>0.86 (n/a)</td><td>779.00 (n/a)</td><td>701.74 (n/a)</td><td>712.00 (n/a)</td><td>589.60 (n/a)</td><td>70.32 (n/a)</td><td>3642.20 (n/a)</td><td>3086.95 (n/a)</td><td>3015.94 (n/a)</td><td>2756.75 (n/a)</td><td>335.03 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.69 (-3.36%)</td><td>8.89 (+1.08%)</td><td>9.01 (+4.64%)</td><td>8.23 (+3.14%)</td><td>0.62 (-17.73%)</td><td>704.40 (-3.04%)</td><td>655.02 (-1.23%)</td><td>643.50 (-4.43%)</td><td>598.60 (+3.47%)</td><td>45.53 (-15.12%)</td><td>4035.68 (-3.36%)</td><td>3702.62 (+1.08%)</td><td>3754.61 (+4.64%)</td><td>3429.94 (+3.14%)</td><td>257.72 (-17.73%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.03 (n/a)</td><td>8.79 (n/a)</td><td>8.61 (n/a)</td><td>7.98 (n/a)</td><td>0.75 (n/a)</td><td>726.50 (n/a)</td><td>663.18 (n/a)</td><td>673.30 (n/a)</td><td>578.50 (n/a)</td><td>53.65 (n/a)</td><td>4175.88 (n/a)</td><td>3663.00 (n/a)</td><td>3587.96 (n/a)</td><td>3325.37 (n/a)</td><td>313.26 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.90 (n/a)</td><td>154.56 (n/a)</td><td>146.80 (n/a)</td><td>139.90 (n/a)</td><td>15.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.10 (n/a)</td><td>162.48 (n/a)</td><td>158.80 (n/a)</td><td>141.50 (n/a)</td><td>17.77 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.60 (n/a)</td><td>166.92 (n/a)</td><td>179.30 (n/a)</td><td>142.50 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>271.60 (n/a)</td><td>173.80 (n/a)</td><td>155.50 (n/a)</td><td>124.20 (n/a)</td><td>57.38 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.50 (n/a)</td><td>180.34 (n/a)</td><td>178.70 (n/a)</td><td>146.10 (n/a)</td><td>33.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>171.88 (n/a)</td><td>189.50 (n/a)</td><td>95.80 (n/a)</td><td>45.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.30 (n/a)</td><td>179.70 (n/a)</td><td>175.60 (n/a)</td><td>130.60 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.50 (n/a)</td><td>216.80 (n/a)</td><td>211.70 (n/a)</td><td>193.90 (n/a)</td><td>20.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>169.48 (n/a)</td><td>168.30 (n/a)</td><td>109.70 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>176.04 (n/a)</td><td>166.10 (n/a)</td><td>121.00 (n/a)</td><td>43.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>166.48 (n/a)</td><td>178.10 (n/a)</td><td>132.80 (n/a)</td><td>21.18 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>245.30 (n/a)</td><td>191.06 (n/a)</td><td>197.90 (n/a)</td><td>113.50 (n/a)</td><td>47.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.60 (n/a)</td><td>177.20 (n/a)</td><td>175.10 (n/a)</td><td>125.10 (n/a)</td><td>43.41 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.80 (n/a)</td><td>195.60 (n/a)</td><td>195.30 (n/a)</td><td>128.70 (n/a)</td><td>56.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>169.56 (n/a)</td><td>191.10 (n/a)</td><td>130.90 (n/a)</td><td>33.64 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>312.30 (n/a)</td><td>227.24 (n/a)</td><td>221.70 (n/a)</td><td>174.60 (n/a)</td><td>52.64 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>336.70 (n/a)</td><td>208.24 (n/a)</td><td>170.00 (n/a)</td><td>161.80 (n/a)</td><td>73.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.80 (n/a)</td><td>185.88 (n/a)</td><td>181.20 (n/a)</td><td>145.80 (n/a)</td><td>40.47 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>186.30 (n/a)</td><td>168.40 (n/a)</td><td>164.90 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>235.00 (n/a)</td><td>200.18 (n/a)</td><td>186.00 (n/a)</td><td>168.30 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.70 (n/a)</td><td>174.24 (n/a)</td><td>181.80 (n/a)</td><td>137.50 (n/a)</td><td>20.65 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>262.90 (n/a)</td><td>201.14 (n/a)</td><td>195.70 (n/a)</td><td>112.70 (n/a)</td><td>59.83 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.00 (n/a)</td><td>188.38 (n/a)</td><td>193.90 (n/a)</td><td>126.30 (n/a)</td><td>38.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>259.80 (n/a)</td><td>220.40 (n/a)</td><td>210.20 (n/a)</td><td>198.00 (n/a)</td><td>24.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>215.00 (n/a)</td><td>162.08 (n/a)</td><td>162.30 (n/a)</td><td>110.70 (n/a)</td><td>38.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>195.70 (n/a)</td><td>154.56 (n/a)</td><td>168.70 (n/a)</td><td>101.60 (n/a)</td><td>39.66 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>290.40 (n/a)</td><td>181.12 (n/a)</td><td>175.70 (n/a)</td><td>119.20 (n/a)</td><td>65.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>199.10 (n/a)</td><td>171.90 (n/a)</td><td>188.00 (n/a)</td><td>131.70 (n/a)</td><td>30.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>185.30 (n/a)</td><td>152.58 (n/a)</td><td>148.10 (n/a)</td><td>123.00 (n/a)</td><td>22.53 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.30 (n/a)</td><td>163.38 (n/a)</td><td>160.50 (n/a)</td><td>139.00 (n/a)</td><td>23.02 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.90 (n/a)</td><td>175.50 (n/a)</td><td>163.10 (n/a)</td><td>151.90 (n/a)</td><td>27.83 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>317.60 (n/a)</td><td>226.88 (n/a)</td><td>211.30 (n/a)</td><td>176.20 (n/a)</td><td>54.67 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.11 (-2.32%)</td><td>4.10 (-0.39%)</td><td>4.10 (-0.14%)</td><td>4.09 (+0.45%)</td><td>0.01 <b>(-81.20%)</b></td><td>19238.30 (-0.45%)</td><td>19161.06 (+0.37%)</td><td>19160.50 (+0.14%)</td><td>19112.20 (+2.38%)</td><td>48.10 <b>(-80.80%)</b></td><td>2809.05 (-2.32%)</td><td>2801.90 (-0.39%)</td><td>2801.96 (-0.14%)</td><td>2790.63 (+0.45%)</td><td>7.03 <b>(-81.20%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.21 (n/a)</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.07 (n/a)</td><td>0.05 (n/a)</td><td>19325.80 (n/a)</td><td>19089.66 (n/a)</td><td>19132.80 (n/a)</td><td>18668.70 (n/a)</td><td>250.48 (n/a)</td><td>2875.78 (n/a)</td><td>2812.76 (n/a)</td><td>2806.03 (n/a)</td><td>2778.01 (n/a)</td><td>37.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.40 (-11.35%)</td><td>3.99 (-9.16%)</td><td>4.10 (-4.24%)</td><td>3.52 (-14.93%)</td><td>0.38 (+17.52%)</td><td>2672.10 (+17.55%)</td><td>2374.70 (+10.48%)</td><td>2291.50 (+4.42%)</td><td>2138.30 (+12.80%)</td><td>234.34 <b>(+58.73%)</b></td><td>1730.03 (-11.35%)</td><td>1569.73 (-9.16%)</td><td>1614.36 (-4.24%)</td><td>1384.44 (-14.93%)</td><td>151.11 (+17.52%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.96 (n/a)</td><td>4.39 (n/a)</td><td>4.29 (n/a)</td><td>4.14 (n/a)</td><td>0.33 (n/a)</td><td>2273.10 (n/a)</td><td>2149.48 (n/a)</td><td>2194.40 (n/a)</td><td>1895.70 (n/a)</td><td>147.64 (n/a)</td><td>1951.46 (n/a)</td><td>1728.11 (n/a)</td><td>1685.80 (n/a)</td><td>1627.44 (n/a)</td><td>128.58 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.04 <b>(-21.88%)</b></td><td>0.97 (-3.41%)</td><td>0.96 (-10.28%)</td><td>0.87 <b>(+49.02%)</b></td><td>0.07 <b>(-74.14%)</b></td><td>254.70 <b>(-32.90%)</b></td><td>229.90 (-3.82%)</td><td>231.40 (+11.46%)</td><td>212.80 <b>(+27.96%)</b></td><td>17.44 <b>(-79.06%)</b></td><td>44.34 <b>(-21.88%)</b></td><td>41.23 (-3.41%)</td><td>40.78 (-10.28%)</td><td>37.05 <b>(+49.02%)</b></td><td>3.07 <b>(-74.14%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.33 (n/a)</td><td>1.00 (n/a)</td><td>1.07 (n/a)</td><td>0.58 (n/a)</td><td>0.28 (n/a)</td><td>379.60 (n/a)</td><td>239.04 (n/a)</td><td>207.60 (n/a)</td><td>166.30 (n/a)</td><td>83.27 (n/a)</td><td>56.76 (n/a)</td><td>42.69 (n/a)</td><td>45.46 (n/a)</td><td>24.86 (n/a)</td><td>11.87 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.08 (-12.64%)</td><td>0.85 <b>(-20.27%)</b></td><td>0.77 <b>(-26.50%)</b></td><td>0.68 <b>(-22.81%)</b></td><td>0.19 (+12.88%)</td><td>326.10 <b>(+29.56%)</b></td><td>271.86 <b>(+27.75%)</b></td><td>288.30 <b>(+36.05%)</b></td><td>204.60 (+14.49%)</td><td>57.45 <b>(+70.55%)</b></td><td>46.13 (-12.64%)</td><td>36.08 <b>(-20.27%)</b></td><td>32.73 <b>(-26.50%)</b></td><td>28.94 <b>(-22.81%)</b></td><td>8.09 (+12.88%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.24 (n/a)</td><td>1.06 (n/a)</td><td>1.04 (n/a)</td><td>0.88 (n/a)</td><td>0.17 (n/a)</td><td>251.70 (n/a)</td><td>212.80 (n/a)</td><td>211.90 (n/a)</td><td>178.70 (n/a)</td><td>33.69 (n/a)</td><td>52.80 (n/a)</td><td>45.25 (n/a)</td><td>44.53 (n/a)</td><td>37.49 (n/a)</td><td>7.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.53 (-0.08%)</td><td>0.53 (-0.05%)</td><td>0.53 (-0.08%)</td><td>0.53 (-0.06%)</td><td>0.00 (-8.45%)</td><td>47918.00 (+0.06%)</td><td>47831.26 (+0.05%)</td><td>47827.30 (+0.08%)</td><td>47777.40 (+0.08%)</td><td>53.10 (-8.32%)</td><td>359.58 (-0.08%)</td><td>359.18 (-0.05%)</td><td>359.21 (-0.08%)</td><td>358.53 (-0.06%)</td><td>0.40 (-8.45%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47890.90 (n/a)</td><td>47809.30 (n/a)</td><td>47788.20 (n/a)</td><td>47739.50 (n/a)</td><td>57.92 (n/a)</td><td>359.87 (n/a)</td><td>359.34 (n/a)</td><td>359.50 (n/a)</td><td>358.73 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (-0.68%)</td><td>0.21 (+1.04%)</td><td>0.21 (+0.98%)</td><td>0.21 (+2.29%)</td><td>0.00 <b>(-65.31%)</b></td><td>118053.00 (-2.24%)</td><td>117465.60 (-1.05%)</td><td>117669.00 (-0.97%)</td><td>116273.80 (+0.68%)</td><td>691.52 <b>(-65.84%)</b></td><td>147.75 (-0.68%)</td><td>146.26 (+1.04%)</td><td>146.00 (+0.98%)</td><td>145.53 (+2.29%)</td><td>0.87 <b>(-65.31%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120761.60 (n/a)</td><td>118716.76 (n/a)</td><td>118820.30 (n/a)</td><td>115483.70 (n/a)</td><td>2024.29 (n/a)</td><td>148.76 (n/a)</td><td>144.75 (n/a)</td><td>144.59 (n/a)</td><td>142.26 (n/a)</td><td>2.50 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.90 (-0.80%)</td><td>0.90 (-0.65%)</td><td>0.90 (-0.70%)</td><td>0.89 (-0.71%)</td><td>0.00 (-4.12%)</td><td>28223.50 (+0.71%)</td><td>28027.88 (+0.65%)</td><td>28044.80 (+0.70%)</td><td>27849.50 (+0.81%)</td><td>150.53 (-2.67%)</td><td>616.88 (-0.80%)</td><td>612.97 (-0.65%)</td><td>612.59 (-0.70%)</td><td>608.71 (-0.71%)</td><td>3.29 (-4.12%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.01 (n/a)</td><td>28023.30 (n/a)</td><td>27847.10 (n/a)</td><td>27849.80 (n/a)</td><td>27625.60 (n/a)</td><td>154.66 (n/a)</td><td>621.88 (n/a)</td><td>616.95 (n/a)</td><td>616.88 (n/a)</td><td>613.06 (n/a)</td><td>3.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.63 (-0.20%)</td><td>3.55 (+0.04%)</td><td>3.62 (+0.28%)</td><td>3.41 (+0.35%)</td><td>0.11 (-0.38%)</td><td>7380.10 (-0.35%)</td><td>7102.68 (-0.04%)</td><td>6955.00 (-0.28%)</td><td>6930.30 (+0.20%)</td><td>225.69 (-0.60%)</td><td>2478.97 (-0.20%)</td><td>2420.72 (+0.04%)</td><td>2470.15 (+0.28%)</td><td>2327.86 (+0.35%)</td><td>75.99 (-0.38%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.64 (n/a)</td><td>3.54 (n/a)</td><td>3.61 (n/a)</td><td>3.40 (n/a)</td><td>0.11 (n/a)</td><td>7406.00 (n/a)</td><td>7105.46 (n/a)</td><td>6974.20 (n/a)</td><td>6916.30 (n/a)</td><td>227.04 (n/a)</td><td>2483.98 (n/a)</td><td>2419.79 (n/a)</td><td>2463.33 (n/a)</td><td>2319.73 (n/a)</td><td>76.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.29 (+14.07%)</td><td>2.92 (+2.52%)</td><td>2.89 (+1.04%)</td><td>2.66 (-4.25%)</td><td>0.25 <b>(+471.56%)</b></td><td>9457.90 (+4.44%)</td><td>8664.04 (-1.91%)</td><td>8694.60 (-1.03%)</td><td>7647.80 (-12.33%)</td><td>730.93 <b>(+424.96%)</b></td><td>2246.37 (+14.07%)</td><td>1994.55 (+2.52%)</td><td>1975.92 (+1.04%)</td><td>1816.45 (-4.25%)</td><td>173.15 <b>(+471.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>2.88 (n/a)</td><td>2.85 (n/a)</td><td>2.86 (n/a)</td><td>2.78 (n/a)</td><td>0.04 (n/a)</td><td>9056.20 (n/a)</td><td>8832.38 (n/a)</td><td>8785.00 (n/a)</td><td>8723.80 (n/a)</td><td>139.24 (n/a)</td><td>1969.30 (n/a)</td><td>1945.48 (n/a)</td><td>1955.58 (n/a)</td><td>1897.02 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.23 (-1.58%)</td><td>3.19 (-0.56%)</td><td>3.19 (+0.48%)</td><td>3.15 (+0.05%)</td><td>0.03 <b>(-48.54%)</b></td><td>7999.50 (-0.05%)</td><td>7882.12 (+0.54%)</td><td>7886.30 (-0.48%)</td><td>7792.70 (+1.60%)</td><td>81.64 <b>(-47.57%)</b></td><td>2204.62 (-1.58%)</td><td>2179.79 (-0.56%)</td><td>2178.46 (+0.48%)</td><td>2147.61 (+0.05%)</td><td>22.51 <b>(-48.54%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.28 (n/a)</td><td>3.21 (n/a)</td><td>3.18 (n/a)</td><td>3.14 (n/a)</td><td>0.06 (n/a)</td><td>8003.60 (n/a)</td><td>7839.66 (n/a)</td><td>7924.20 (n/a)</td><td>7669.90 (n/a)</td><td>155.72 (n/a)</td><td>2239.91 (n/a)</td><td>2192.10 (n/a)</td><td>2168.04 (n/a)</td><td>2146.53 (n/a)</td><td>43.75 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.80 (-0.34%)</td><td>0.80 (-0.07%)</td><td>0.80 (-0.04%)</td><td>0.80 (+0.13%)</td><td>0.00 <b>(-81.39%)</b></td><td>94871.30 (-0.13%)</td><td>94821.30 (+0.07%)</td><td>94827.90 (+0.04%)</td><td>94769.30 (+0.34%)</td><td>37.05 <b>(-81.34%)</b></td><td>725.12 (-0.34%)</td><td>724.73 (-0.07%)</td><td>724.68 (-0.04%)</td><td>724.34 (+0.13%)</td><td>0.28 <b>(-81.39%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>94997.00 (n/a)</td><td>94758.26 (n/a)</td><td>94786.20 (n/a)</td><td>94445.20 (n/a)</td><td>198.57 (n/a)</td><td>727.61 (n/a)</td><td>725.21 (n/a)</td><td>724.99 (n/a)</td><td>723.39 (n/a)</td><td>1.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.73 (+0.03%)</td><td>0.73 (+0.07%)</td><td>0.73 (+0.02%)</td><td>0.73 (+0.13%)</td><td>0.00 <b>(-64.61%)</b></td><td>103355.80 (-0.13%)</td><td>103312.74 (-0.07%)</td><td>103311.70 (-0.02%)</td><td>103273.90 (-0.03%)</td><td>29.11 <b>(-64.65%)</b></td><td>665.41 (+0.03%)</td><td>665.16 (+0.07%)</td><td>665.17 (+0.02%)</td><td>664.88 (+0.13%)</td><td>0.19 <b>(-64.61%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103486.80 (n/a)</td><td>103381.12 (n/a)</td><td>103337.40 (n/a)</td><td>103303.60 (n/a)</td><td>82.35 (n/a)</td><td>665.22 (n/a)</td><td>664.72 (n/a)</td><td>665.00 (n/a)</td><td>664.04 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.69 (-0.38%)</td><td>0.68 (-0.35%)</td><td>0.68 (-0.35%)</td><td>0.68 (-0.43%)</td><td>0.00 (+0.41%)</td><td>110564.10 (+0.44%)</td><td>110255.90 (+0.35%)</td><td>110285.80 (+0.35%)</td><td>109857.10 (+0.38%)</td><td>258.56 (+1.22%)</td><td>625.54 (-0.38%)</td><td>623.28 (-0.35%)</td><td>623.10 (-0.35%)</td><td>621.53 (-0.43%)</td><td>1.46 (+0.41%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>110084.50 (n/a)</td><td>109870.14 (n/a)</td><td>109898.80 (n/a)</td><td>109442.90 (n/a)</td><td>255.43 (n/a)</td><td>627.90 (n/a)</td><td>625.46 (n/a)</td><td>625.30 (n/a)</td><td>624.24 (n/a)</td><td>1.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>2.79 (-0.08%)</td><td>2.79 (-0.15%)</td><td>2.79 (-0.25%)</td><td>2.78 (-0.16%)</td><td>0.01 <b>(+21.99%)</b></td><td>37706.20 (+0.16%)</td><td>37606.28 (+0.15%)</td><td>37611.90 (+0.25%)</td><td>37522.20 (+0.08%)</td><td>83.43 <b>(+22.24%)</b></td><td>2861.61 (-0.08%)</td><td>2855.23 (-0.15%)</td><td>2854.79 (-0.25%)</td><td>2847.65 (-0.16%)</td><td>6.33 <b>(+21.99%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>2.79 (n/a)</td><td>2.79 (n/a)</td><td>0.01 (n/a)</td><td>37646.90 (n/a)</td><td>37551.28 (n/a)</td><td>37516.80 (n/a)</td><td>37493.90 (n/a)</td><td>68.25 (n/a)</td><td>2863.78 (n/a)</td><td>2859.41 (n/a)</td><td>2862.03 (n/a)</td><td>2852.14 (n/a)</td><td>5.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.74 (+2.71%)</td><td>7.13 (+3.70%)</td><td>6.99 (+4.13%)</td><td>6.43 (+0.33%)</td><td>0.54 (+19.25%)</td><td>1386.90 (-0.32%)</td><td>1256.80 (-3.44%)</td><td>1274.30 (-3.96%)</td><td>1151.60 (-2.65%)</td><td>96.72 (+14.95%)</td><td>466.18 (+2.71%)</td><td>429.19 (+3.70%)</td><td>421.32 (+4.13%)</td><td>387.10 (+0.33%)</td><td>32.81 (+19.25%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.53 (n/a)</td><td>6.87 (n/a)</td><td>6.72 (n/a)</td><td>6.41 (n/a)</td><td>0.46 (n/a)</td><td>1391.40 (n/a)</td><td>1301.60 (n/a)</td><td>1326.80 (n/a)</td><td>1182.90 (n/a)</td><td>84.14 (n/a)</td><td>453.87 (n/a)</td><td>413.89 (n/a)</td><td>404.62 (n/a)</td><td>385.84 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.10 (+1.12%)</td><td>6.56 (-2.92%)</td><td>6.82 (-0.67%)</td><td>5.10 <b>(-20.38%)</b></td><td>0.83 <b>(+188.84%)</b></td><td>1747.40 <b>(+25.59%)</b></td><td>1379.98 (+4.44%)</td><td>1307.70 (+0.67%)</td><td>1254.60 (-1.11%)</td><td>206.91 <b>(+265.57%)</b></td><td>427.92 (+1.12%)</td><td>395.00 (-2.92%)</td><td>410.54 (-0.67%)</td><td>307.25 <b>(-20.38%)</b></td><td>49.72 <b>(+188.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.03 (n/a)</td><td>6.76 (n/a)</td><td>6.86 (n/a)</td><td>6.41 (n/a)</td><td>0.29 (n/a)</td><td>1391.30 (n/a)</td><td>1321.34 (n/a)</td><td>1299.00 (n/a)</td><td>1268.70 (n/a)</td><td>56.60 (n/a)</td><td>423.18 (n/a)</td><td>406.90 (n/a)</td><td>413.30 (n/a)</td><td>385.88 (n/a)</td><td>17.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.90 (-3.52%)</td><td>6.47 (+1.28%)</td><td>6.39 (-7.14%)</td><td>6.10 <b>(+34.72%)</b></td><td>0.38 <b>(-65.48%)</b></td><td>1460.40 <b>(-25.77%)</b></td><td>1382.08 (-3.86%)</td><td>1395.30 (+7.70%)</td><td>1291.40 (+3.65%)</td><td>80.07 <b>(-73.70%)</b></td><td>415.74 (-3.52%)</td><td>389.51 (+1.28%)</td><td>384.78 (-7.14%)</td><td>367.62 <b>(+34.72%)</b></td><td>22.77 <b>(-65.48%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.15 (n/a)</td><td>6.38 (n/a)</td><td>6.88 (n/a)</td><td>4.53 (n/a)</td><td>1.10 (n/a)</td><td>1967.40 (n/a)</td><td>1437.52 (n/a)</td><td>1295.60 (n/a)</td><td>1245.90 (n/a)</td><td>304.49 (n/a)</td><td>430.92 (n/a)</td><td>384.60 (n/a)</td><td>414.37 (n/a)</td><td>272.88 (n/a)</td><td>65.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.95 (-2.24%)</td><td>7.77 (-0.40%)</td><td>7.93 (+0.64%)</td><td>7.37 (+0.64%)</td><td>0.26 (-14.98%)</td><td>4732.10 (-0.64%)</td><td>4490.84 (+0.37%)</td><td>4394.50 (-0.63%)</td><td>4385.90 (+2.29%)</td><td>152.86 (-14.48%)</td><td>489.63 (-2.24%)</td><td>478.62 (-0.40%)</td><td>488.67 (+0.64%)</td><td>453.81 (+0.64%)</td><td>15.88 (-14.98%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>8.13 (n/a)</td><td>7.80 (n/a)</td><td>7.88 (n/a)</td><td>7.32 (n/a)</td><td>0.30 (n/a)</td><td>4762.50 (n/a)</td><td>4474.44 (n/a)</td><td>4422.50 (n/a)</td><td>4287.80 (n/a)</td><td>178.74 (n/a)</td><td>500.83 (n/a)</td><td>480.54 (n/a)</td><td>485.58 (n/a)</td><td>450.92 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.59 (-2.12%)</td><td>7.30 (-4.16%)</td><td>7.27 (-4.37%)</td><td>7.03 (-6.20%)</td><td>0.26 <b>(+114.23%)</b></td><td>4957.40 (+6.61%)</td><td>4778.14 (+4.43%)</td><td>4795.90 (+4.57%)</td><td>4592.60 (+2.17%)</td><td>167.33 <b>(+133.08%)</b></td><td>467.60 (-2.12%)</td><td>449.88 (-4.16%)</td><td>447.77 (-4.37%)</td><td>433.19 (-6.20%)</td><td>15.81 <b>(+114.23%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.76 (n/a)</td><td>7.62 (n/a)</td><td>7.60 (n/a)</td><td>7.50 (n/a)</td><td>0.12 (n/a)</td><td>4650.20 (n/a)</td><td>4575.52 (n/a)</td><td>4586.10 (n/a)</td><td>4495.20 (n/a)</td><td>71.79 (n/a)</td><td>477.72 (n/a)</td><td>469.43 (n/a)</td><td>468.26 (n/a)</td><td>461.80 (n/a)</td><td>7.38 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.60 (+1.92%)</td><td>7.18 (-1.84%)</td><td>7.25 (-1.14%)</td><td>6.80 (-4.89%)</td><td>0.33 <b>(+193.51%)</b></td><td>5129.60 (+5.14%)</td><td>4861.46 (+2.02%)</td><td>4811.30 (+1.15%)</td><td>4587.00 (-1.88%)</td><td>220.74 <b>(+203.13%)</b></td><td>468.17 (+1.92%)</td><td>442.47 (-1.84%)</td><td>446.34 (-1.14%)</td><td>418.65 (-4.89%)</td><td>20.07 <b>(+193.51%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.46 (n/a)</td><td>7.32 (n/a)</td><td>7.33 (n/a)</td><td>7.15 (n/a)</td><td>0.11 (n/a)</td><td>4878.60 (n/a)</td><td>4765.22 (n/a)</td><td>4756.60 (n/a)</td><td>4675.10 (n/a)</td><td>72.82 (n/a)</td><td>459.34 (n/a)</td><td>450.74 (n/a)</td><td>451.47 (n/a)</td><td>440.19 (n/a)</td><td>6.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.80 (+0.01%)</td><td>0.80 (-0.07%)</td><td>0.80 (-0.04%)</td><td>0.80 (-0.21%)</td><td>0.00 <b>(+299.27%)</b></td><td>94310.80 (+0.21%)</td><td>94135.44 (+0.07%)</td><td>94112.80 (+0.04%)</td><td>94039.30 (-0.01%)</td><td>105.29 <b>(+300.09%)</b></td><td>730.75 (+0.01%)</td><td>730.01 (-0.07%)</td><td>730.18 (-0.04%)</td><td>728.65 (-0.21%)</td><td>0.82 <b>(+299.25%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94111.40 (n/a)</td><td>94073.62 (n/a)</td><td>94071.80 (n/a)</td><td>94044.80 (n/a)</td><td>26.32 (n/a)</td><td>730.71 (n/a)</td><td>730.49 (n/a)</td><td>730.50 (n/a)</td><td>730.19 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.74 (+0.00%)</td><td>0.74 (+0.05%)</td><td>0.74 (+0.02%)</td><td>0.74 (+0.19%)</td><td>0.00 (-19.77%)</td><td>102634.80 (-0.19%)</td><td>102519.86 (-0.05%)</td><td>102591.40 (-0.02%)</td><td>102182.40 (-0.00%)</td><td>189.61 (-19.90%)</td><td>672.52 (+0.00%)</td><td>670.31 (+0.05%)</td><td>669.84 (+0.02%)</td><td>669.55 (+0.19%)</td><td>1.24 (-19.77%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102834.80 (n/a)</td><td>102570.24 (n/a)</td><td>102611.80 (n/a)</td><td>102185.80 (n/a)</td><td>236.72 (n/a)</td><td>672.50 (n/a)</td><td>669.98 (n/a)</td><td>669.70 (n/a)</td><td>668.25 (n/a)</td><td>1.55 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.71 (-0.01%)</td><td>0.71 (-0.00%)</td><td>0.71 (+0.04%)</td><td>0.71 (-0.06%)</td><td>0.00 <b>(+31.87%)</b></td><td>106162.40 (+0.06%)</td><td>105960.66 (+0.00%)</td><td>105910.60 (-0.04%)</td><td>105874.20 (+0.01%)</td><td>117.15 <b>(+31.96%)</b></td><td>649.07 (-0.01%)</td><td>648.54 (-0.00%)</td><td>648.84 (+0.04%)</td><td>647.31 (-0.06%)</td><td>0.72 <b>(+31.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106099.30 (n/a)</td><td>105957.28 (n/a)</td><td>105950.80 (n/a)</td><td>105865.50 (n/a)</td><td>88.78 (n/a)</td><td>649.12 (n/a)</td><td>648.56 (n/a)</td><td>648.60 (n/a)</td><td>647.69 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.35 (+0.42%)</td><td>3.43 (-8.35%)</td><td>3.12 (-19.00%)</td><td>3.00 (-2.07%)</td><td>0.57 (+2.99%)</td><td>2683.20 (+2.11%)</td><td>2395.10 (+9.29%)</td><td>2579.70 <b>(+23.45%)</b></td><td>1854.50 (-0.42%)</td><td>358.13 (+5.90%)</td><td>1139.89 (+0.42%)</td><td>900.55 (-8.35%)</td><td>819.45 (-19.00%)</td><td>787.83 (-2.07%)</td><td>150.70 (+2.99%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.33 (n/a)</td><td>3.75 (n/a)</td><td>3.86 (n/a)</td><td>3.07 (n/a)</td><td>0.56 (n/a)</td><td>2627.70 (n/a)</td><td>2191.46 (n/a)</td><td>2089.70 (n/a)</td><td>1862.30 (n/a)</td><td>338.17 (n/a)</td><td>1135.14 (n/a)</td><td>982.64 (n/a)</td><td>1011.60 (n/a)</td><td>804.49 (n/a)</td><td>146.33 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.51 (+1.32%)</td><td>0.36 (-6.63%)</td><td>0.36 (+4.94%)</td><td>0.28 (+0.31%)</td><td>0.09 (-10.90%)</td><td>4393.00 (-0.31%)</td><td>3615.24 (+6.02%)</td><td>3502.80 (-4.71%)</td><td>2451.90 (-1.30%)</td><td>775.51 (-8.76%)</td><td>27.37 (+1.32%)</td><td>19.38 (-6.63%)</td><td>19.16 (+4.94%)</td><td>15.28 (+0.31%)</td><td>4.84 (-10.90%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>4406.50 (n/a)</td><td>3409.80 (n/a)</td><td>3675.80 (n/a)</td><td>2484.20 (n/a)</td><td>849.99 (n/a)</td><td>27.01 (n/a)</td><td>20.76 (n/a)</td><td>18.26 (n/a)</td><td>15.23 (n/a)</td><td>5.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.76 <b>(-26.04%)</b></td><td>3.94 <b>(-22.09%)</b></td><td>3.64 <b>(-23.80%)</b></td><td>3.24 <b>(-29.16%)</b></td><td>0.74 (-5.24%)</td><td>2054.60 <b>(+41.17%)</b></td><td>1736.98 <b>(+29.81%)</b></td><td>1825.40 <b>(+31.23%)</b></td><td>1396.20 <b>(+35.20%)</b></td><td>313.83 <b>(+81.10%)</b></td><td>1472.02 <b>(-26.04%)</b></td><td>1216.26 <b>(-22.09%)</b></td><td>1125.89 <b>(-23.80%)</b></td><td>1000.31 <b>(-29.16%)</b></td><td>229.19 (-5.24%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.44 (n/a)</td><td>5.05 (n/a)</td><td>4.78 (n/a)</td><td>4.57 (n/a)</td><td>0.78 (n/a)</td><td>1455.40 (n/a)</td><td>1338.06 (n/a)</td><td>1391.00 (n/a)</td><td>1032.70 (n/a)</td><td>173.29 (n/a)</td><td>1990.22 (n/a)</td><td>1561.01 (n/a)</td><td>1477.53 (n/a)</td><td>1412.15 (n/a)</td><td>241.87 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.40 (n/a)</td><td>12.13 (n/a)</td><td>12.07 (n/a)</td><td>10.82 (n/a)</td><td>1.19 (n/a)</td><td>13.39 (n/a)</td><td>12.12 (n/a)</td><td>12.06 (n/a)</td><td>10.81 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>24.59 (+0.58%)</td><td>24.01 (+0.66%)</td><td>24.01 (-0.58%)</td><td>23.35 (+2.92%)</td><td>0.46 <b>(-34.60%)</b></td><td>24.58 (+0.58%)</td><td>24.00 (+0.66%)</td><td>24.00 (-0.58%)</td><td>23.33 (+2.92%)</td><td>0.46 <b>(-34.60%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>24.45 (n/a)</td><td>23.86 (n/a)</td><td>24.15 (n/a)</td><td>22.68 (n/a)</td><td>0.71 (n/a)</td><td>24.44 (n/a)</td><td>23.84 (n/a)</td><td>24.14 (n/a)</td><td>22.67 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>42.68 (+4.86%)</td><td>40.28 (+2.42%)</td><td>40.39 (+3.51%)</td><td>38.50 (+0.31%)</td><td>1.56 <b>(+50.49%)</b></td><td>42.65 (+4.86%)</td><td>40.26 (+2.42%)</td><td>40.37 (+3.51%)</td><td>38.48 (+0.31%)</td><td>1.56 <b>(+50.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>40.70 (n/a)</td><td>39.33 (n/a)</td><td>39.02 (n/a)</td><td>38.38 (n/a)</td><td>1.03 (n/a)</td><td>40.68 (n/a)</td><td>39.30 (n/a)</td><td>39.00 (n/a)</td><td>38.36 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>44.07 (-3.61%)</td><td>38.04 (-10.53%)</td><td>41.29 (-1.80%)</td><td>23.57 <b>(-41.14%)</b></td><td>8.50 <b>(+277.52%)</b></td><td>44.05 (-3.61%)</td><td>38.01 (-10.53%)</td><td>41.27 (-1.80%)</td><td>23.55 <b>(-41.14%)</b></td><td>8.49 <b>(+277.52%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>45.72 (n/a)</td><td>42.51 (n/a)</td><td>42.05 (n/a)</td><td>40.04 (n/a)</td><td>2.25 (n/a)</td><td>45.70 (n/a)</td><td>42.49 (n/a)</td><td>42.02 (n/a)</td><td>40.01 (n/a)</td><td>2.25 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.31 (n/a)</td><td>12.35 (n/a)</td><td>12.60 (n/a)</td><td>10.68 (n/a)</td><td>1.07 (n/a)</td><td>13.30 (n/a)</td><td>12.34 (n/a)</td><td>12.59 (n/a)</td><td>10.67 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>24.51 (-1.61%)</td><td>24.07 (-0.01%)</td><td>24.23 (+0.54%)</td><td>23.07 (-1.37%)</td><td>0.57 (+2.53%)</td><td>24.49 (-1.61%)</td><td>24.05 (-0.01%)</td><td>24.21 (+0.54%)</td><td>23.05 (-1.37%)</td><td>0.57 (+2.53%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>24.91 (n/a)</td><td>24.07 (n/a)</td><td>24.10 (n/a)</td><td>23.39 (n/a)</td><td>0.56 (n/a)</td><td>24.89 (n/a)</td><td>24.05 (n/a)</td><td>24.08 (n/a)</td><td>23.37 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>41.40 (+0.65%)</td><td>38.37 (-3.76%)</td><td>39.73 (-2.84%)</td><td>31.76 (-16.31%)</td><td>3.81 <b>(+140.04%)</b></td><td>41.38 (+0.65%)</td><td>38.35 (-3.76%)</td><td>39.71 (-2.84%)</td><td>31.74 (-16.31%)</td><td>3.80 <b>(+140.04%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>41.13 (n/a)</td><td>39.87 (n/a)</td><td>40.90 (n/a)</td><td>37.95 (n/a)</td><td>1.59 (n/a)</td><td>41.11 (n/a)</td><td>39.85 (n/a)</td><td>40.87 (n/a)</td><td>37.93 (n/a)</td><td>1.58 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>44.53 (+3.19%)</td><td>42.85 (+4.78%)</td><td>42.77 (+4.68%)</td><td>41.69 (+11.05%)</td><td>1.16 <b>(-46.63%)</b></td><td>44.50 (+3.19%)</td><td>42.82 (+4.78%)</td><td>42.74 (+4.68%)</td><td>41.66 (+11.05%)</td><td>1.16 <b>(-46.63%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>43.15 (n/a)</td><td>40.90 (n/a)</td><td>40.86 (n/a)</td><td>37.54 (n/a)</td><td>2.17 (n/a)</td><td>43.13 (n/a)</td><td>40.87 (n/a)</td><td>40.83 (n/a)</td><td>37.52 (n/a)</td><td>2.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.40 (-9.50%)</td><td>8.68 (-7.36%)</td><td>8.81 (-2.30%)</td><td>7.84 (-9.86%)</td><td>0.57 (-19.71%)</td><td>9.39 (-9.50%)</td><td>8.67 (-7.36%)</td><td>8.79 (-2.30%)</td><td>7.82 (-9.86%)</td><td>0.57 (-19.71%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.39 (n/a)</td><td>9.37 (n/a)</td><td>9.02 (n/a)</td><td>8.70 (n/a)</td><td>0.71 (n/a)</td><td>10.37 (n/a)</td><td>9.36 (n/a)</td><td>9.00 (n/a)</td><td>8.68 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.04 (-0.32%)</td><td>0.85 (-3.63%)</td><td>0.88 (-1.92%)</td><td>0.70 (-8.14%)</td><td>0.15 <b>(+35.41%)</b></td><td>1.02 (-0.32%)</td><td>0.84 (-3.63%)</td><td>0.86 (-1.92%)</td><td>0.68 (-8.14%)</td><td>0.14 <b>(+35.41%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.04 (n/a)</td><td>0.88 (n/a)</td><td>0.89 (n/a)</td><td>0.76 (n/a)</td><td>0.11 (n/a)</td><td>1.03 (n/a)</td><td>0.87 (n/a)</td><td>0.88 (n/a)</td><td>0.75 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.50 (+8.06%)</td><td>1.13 (-6.34%)</td><td>1.09 (-5.51%)</td><td>0.89 (-19.11%)</td><td>0.23 <b>(+104.26%)</b></td><td>1.48 (+8.06%)</td><td>1.11 (-6.34%)</td><td>1.08 (-5.51%)</td><td>0.88 (-19.11%)</td><td>0.23 <b>(+104.26%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.39 (n/a)</td><td>1.20 (n/a)</td><td>1.15 (n/a)</td><td>1.10 (n/a)</td><td>0.11 (n/a)</td><td>1.37 (n/a)</td><td>1.19 (n/a)</td><td>1.14 (n/a)</td><td>1.09 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>18.87 (-5.53%)</td><td>17.83 (-0.74%)</td><td>18.25 (+3.16%)</td><td>15.56 (-6.00%)</td><td>1.32 (+5.38%)</td><td>18.66 (-5.53%)</td><td>17.63 (-0.74%)</td><td>18.04 (+3.16%)</td><td>15.38 (-6.00%)</td><td>1.30 (+5.38%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>19.98 (n/a)</td><td>17.96 (n/a)</td><td>17.69 (n/a)</td><td>16.55 (n/a)</td><td>1.25 (n/a)</td><td>19.75 (n/a)</td><td>17.76 (n/a)</td><td>17.49 (n/a)</td><td>16.36 (n/a)</td><td>1.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.17 (-5.62%)</td><td>13.73 (-3.31%)</td><td>13.72 (-3.09%)</td><td>13.22 (-3.57%)</td><td>0.44 (-17.70%)</td><td>13.92 (-5.62%)</td><td>13.49 (-3.31%)</td><td>13.48 (-3.09%)</td><td>12.99 (-3.57%)</td><td>0.43 (-17.70%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>15.02 (n/a)</td><td>14.20 (n/a)</td><td>14.16 (n/a)</td><td>13.71 (n/a)</td><td>0.53 (n/a)</td><td>14.75 (n/a)</td><td>13.95 (n/a)</td><td>13.91 (n/a)</td><td>13.47 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.79 (+6.93%)</td><td>8.27 (+2.11%)</td><td>7.96 (-5.10%)</td><td>5.98 (-10.43%)</td><td>1.55 <b>(+50.29%)</b></td><td>9.62 (+6.93%)</td><td>8.13 (+2.11%)</td><td>7.82 (-5.10%)</td><td>5.88 (-10.43%)</td><td>1.53 <b>(+50.29%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.16 (n/a)</td><td>8.10 (n/a)</td><td>8.39 (n/a)</td><td>6.68 (n/a)</td><td>1.03 (n/a)</td><td>9.00 (n/a)</td><td>7.96 (n/a)</td><td>8.25 (n/a)</td><td>6.56 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.11 (-5.07%)</td><td>5.59 (-4.65%)</td><td>5.57 (-4.88%)</td><td>4.85 (-7.40%)</td><td>0.50 (+9.90%)</td><td>6.02 (-5.07%)</td><td>5.50 (-4.65%)</td><td>5.48 (-4.88%)</td><td>4.77 (-7.40%)</td><td>0.50 (+9.90%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.44 (n/a)</td><td>5.86 (n/a)</td><td>5.86 (n/a)</td><td>5.24 (n/a)</td><td>0.46 (n/a)</td><td>6.34 (n/a)</td><td>5.77 (n/a)</td><td>5.76 (n/a)</td><td>5.15 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.50 (n/a)</td><td>12.45 (n/a)</td><td>12.81 (n/a)</td><td>10.96 (n/a)</td><td>1.07 (n/a)</td><td>13.49 (n/a)</td><td>12.44 (n/a)</td><td>12.80 (n/a)</td><td>10.96 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.38 (n/a)</td><td>12.39 (n/a)</td><td>12.62 (n/a)</td><td>10.85 (n/a)</td><td>1.09 (n/a)</td><td>13.37 (n/a)</td><td>12.39 (n/a)</td><td>12.61 (n/a)</td><td>10.84 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.60 (n/a)</td><td>177.10 (n/a)</td><td>170.70 (n/a)</td><td>150.20 (n/a)</td><td>28.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>148.66 (n/a)</td><td>149.60 (n/a)</td><td>103.60 (n/a)</td><td>49.90 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.80 (n/a)</td><td>148.20 (n/a)</td><td>150.00 (n/a)</td><td>121.80 (n/a)</td><td>21.74 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>155.50 (n/a)</td><td>150.60 (n/a)</td><td>134.70 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.40 (n/a)</td><td>167.56 (n/a)</td><td>160.90 (n/a)</td><td>123.60 (n/a)</td><td>43.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.90 (n/a)</td><td>175.80 (n/a)</td><td>163.00 (n/a)</td><td>133.60 (n/a)</td><td>35.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.60 (n/a)</td><td>189.36 (n/a)</td><td>180.10 (n/a)</td><td>140.30 (n/a)</td><td>38.48 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.50 (n/a)</td><td>204.22 (n/a)</td><td>203.60 (n/a)</td><td>176.90 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.40 (n/a)</td><td>157.04 (n/a)</td><td>166.50 (n/a)</td><td>129.40 (n/a)</td><td>22.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>184.60 (n/a)</td><td>168.00 (n/a)</td><td>171.20 (n/a)</td><td>145.30 (n/a)</td><td>14.58 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>163.74 (n/a)</td><td>168.70 (n/a)</td><td>116.40 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>165.20 (n/a)</td><td>165.40 (n/a)</td><td>117.00 (n/a)</td><td>42.50 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.90 (n/a)</td><td>189.36 (n/a)</td><td>182.10 (n/a)</td><td>167.00 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>177.44 (n/a)</td><td>195.20 (n/a)</td><td>115.30 (n/a)</td><td>37.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>166.02 (n/a)</td><td>163.20 (n/a)</td><td>132.00 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.70 (n/a)</td><td>193.94 (n/a)</td><td>192.20 (n/a)</td><td>169.20 (n/a)</td><td>20.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>291.10 (n/a)</td><td>177.30 (n/a)</td><td>149.00 (n/a)</td><td>135.40 (n/a)</td><td>65.05 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>181.76 (n/a)</td><td>188.30 (n/a)</td><td>155.00 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>216.60 (n/a)</td><td>172.42 (n/a)</td><td>182.40 (n/a)</td><td>124.20 (n/a)</td><td>43.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.40 (n/a)</td><td>163.54 (n/a)</td><td>162.20 (n/a)</td><td>131.70 (n/a)</td><td>35.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>275.40 (n/a)</td><td>206.58 (n/a)</td><td>227.50 (n/a)</td><td>119.70 (n/a)</td><td>59.65 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>189.44 (n/a)</td><td>188.60 (n/a)</td><td>169.50 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>225.30 (n/a)</td><td>198.68 (n/a)</td><td>193.60 (n/a)</td><td>156.60 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>228.40 (n/a)</td><td>213.84 (n/a)</td><td>209.00 (n/a)</td><td>202.30 (n/a)</td><td>10.90 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>209.10 (n/a)</td><td>192.18 (n/a)</td><td>195.10 (n/a)</td><td>170.80 (n/a)</td><td>16.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>236.70 (n/a)</td><td>180.96 (n/a)</td><td>180.80 (n/a)</td><td>130.60 (n/a)</td><td>44.31 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>178.10 (n/a)</td><td>152.06 (n/a)</td><td>151.30 (n/a)</td><td>127.20 (n/a)</td><td>21.13 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>195.00 (n/a)</td><td>155.70 (n/a)</td><td>151.80 (n/a)</td><td>119.40 (n/a)</td><td>33.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>308.10 (n/a)</td><td>212.86 (n/a)</td><td>230.20 (n/a)</td><td>104.30 (n/a)</td><td>74.56 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>235.00 (n/a)</td><td>182.08 (n/a)</td><td>177.40 (n/a)</td><td>130.40 (n/a)</td><td>39.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>223.00 (n/a)</td><td>163.58 (n/a)</td><td>154.90 (n/a)</td><td>117.70 (n/a)</td><td>42.20 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>258.50 (n/a)</td><td>219.94 (n/a)</td><td>217.60 (n/a)</td><td>165.80 (n/a)</td><td>37.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (+2.04%)</td><td>0.03 (+4.78%)</td><td>0.03 (+12.10%)</td><td>0.02 (+5.42%)</td><td>0.01 (+5.64%)</td><td>176.20 (-5.17%)</td><td>143.84 (-4.41%)</td><td>132.60 (-10.83%)</td><td>119.10 (-1.98%)</td><td>28.20 (+0.05%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>185.80 (n/a)</td><td>150.48 (n/a)</td><td>148.70 (n/a)</td><td>121.50 (n/a)</td><td>28.18 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (-17.52%)</td><td>0.03 (+10.21%)</td><td>0.03 <b>(+29.54%)</b></td><td>0.02 (+13.17%)</td><td>0.01 <b>(-41.73%)</b></td><td>222.60 (-11.63%)</td><td>161.58 (-15.15%)</td><td>159.60 <b>(-22.82%)</b></td><td>114.80 <b>(+21.22%)</b></td><td>39.82 <b>(-31.62%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>251.90 (n/a)</td><td>190.42 (n/a)</td><td>206.80 (n/a)</td><td>94.70 (n/a)</td><td>58.23 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-19.11%)</td><td>0.02 (-5.80%)</td><td>0.03 (-1.62%)</td><td>0.02 (+11.79%)</td><td>0.00 <b>(-55.45%)</b></td><td>181.20 (-10.56%)</td><td>165.64 (+3.86%)</td><td>163.70 (+1.68%)</td><td>147.30 <b>(+23.68%)</b></td><td>15.05 <b>(-49.42%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>159.48 (n/a)</td><td>161.00 (n/a)</td><td>119.10 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-16.53%)</td><td>0.02 (+1.23%)</td><td>0.02 (+4.12%)</td><td>0.02 (+14.39%)</td><td>0.00 <b>(-43.32%)</b></td><td>208.50 (-12.58%)</td><td>175.24 (-4.75%)</td><td>182.20 (-3.95%)</td><td>139.30 (+19.78%)</td><td>27.51 <b>(-38.32%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.50 (n/a)</td><td>183.98 (n/a)</td><td>189.70 (n/a)</td><td>116.30 (n/a)</td><td>44.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (+12.08%)</td><td>0.02 (+7.45%)</td><td>0.02 (+9.64%)</td><td>0.02 <b>(+38.39%)</b></td><td>0.01 (-5.49%)</td><td>233.60 <b>(-27.75%)</b></td><td>178.82 (-10.12%)</td><td>166.80 (-8.80%)</td><td>126.20 (-10.75%)</td><td>43.15 <b>(-40.52%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>323.30 (n/a)</td><td>198.96 (n/a)</td><td>182.90 (n/a)</td><td>141.40 (n/a)</td><td>72.55 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (+4.83%)</td><td>0.02 (+19.30%)</td><td>0.03 <b>(+21.13%)</b></td><td>0.02 <b>(+60.13%)</b></td><td>0.00 <b>(-42.15%)</b></td><td>194.20 <b>(-37.56%)</b></td><td>167.38 (-19.86%)</td><td>157.80 (-17.43%)</td><td>149.00 (-4.61%)</td><td>20.28 <b>(-66.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>311.00 (n/a)</td><td>208.86 (n/a)</td><td>191.10 (n/a)</td><td>156.20 (n/a)</td><td>60.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-14.56%)</td><td>0.02 (-10.75%)</td><td>0.02 (+2.15%)</td><td>0.02 <b>(-23.93%)</b></td><td>0.00 (-7.06%)</td><td>239.40 <b>(+31.47%)</b></td><td>182.74 (+12.76%)</td><td>173.70 (-2.09%)</td><td>151.60 (+17.07%)</td><td>35.52 <b>(+40.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.10 (n/a)</td><td>162.06 (n/a)</td><td>177.40 (n/a)</td><td>129.50 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 <b>(+26.25%)</b></td><td>0.02 (+12.56%)</td><td>0.02 (+3.58%)</td><td>0.02 (+4.28%)</td><td>0.01 <b>(+86.22%)</b></td><td>230.40 (-4.12%)</td><td>195.86 (-8.83%)</td><td>219.00 (-3.44%)</td><td>134.20 <b>(-20.78%)</b></td><td>40.85 <b>(+43.79%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.30 (n/a)</td><td>214.84 (n/a)</td><td>226.80 (n/a)</td><td>169.40 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (+8.25%)</td><td>0.05 (+1.01%)</td><td>0.06 (+5.75%)</td><td>0.04 (-13.31%)</td><td>0.01 <b>(+150.83%)</b></td><td>184.80 (+15.36%)</td><td>152.76 (+0.24%)</td><td>147.90 (-5.43%)</td><td>130.10 (-7.67%)</td><td>21.23 <b>(+170.18%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>160.20 (n/a)</td><td>152.40 (n/a)</td><td>156.40 (n/a)</td><td>140.90 (n/a)</td><td>7.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (-16.00%)</td><td>0.05 (-2.97%)</td><td>0.05 (+4.98%)</td><td>0.05 <b>(+26.88%)</b></td><td>0.00 <b>(-68.90%)</b></td><td>178.60 <b>(-21.18%)</b></td><td>161.42 (-1.53%)</td><td>163.30 (-4.73%)</td><td>146.60 (+18.99%)</td><td>12.68 <b>(-69.89%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.60 (n/a)</td><td>163.92 (n/a)</td><td>171.40 (n/a)</td><td>123.20 (n/a)</td><td>42.10 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (-7.17%)</td><td>0.05 (-7.14%)</td><td>0.05 (-18.52%)</td><td>0.04 (+5.56%)</td><td>0.01 <b>(-47.52%)</b></td><td>182.80 (-5.24%)</td><td>154.86 (+4.79%)</td><td>152.30 <b>(+22.72%)</b></td><td>132.80 (+7.70%)</td><td>18.76 <b>(-44.40%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>147.78 (n/a)</td><td>124.10 (n/a)</td><td>123.30 (n/a)</td><td>33.74 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (+11.87%)</td><td>0.05 (-3.89%)</td><td>0.05 <b>(-20.35%)</b></td><td>0.04 <b>(+33.19%)</b></td><td>0.01 (-15.66%)</td><td>197.30 <b>(-24.92%)</b></td><td>173.50 (+1.11%)</td><td>181.80 <b>(+25.55%)</b></td><td>127.30 (-10.60%)</td><td>29.14 <b>(-43.78%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>262.80 (n/a)</td><td>171.60 (n/a)</td><td>144.80 (n/a)</td><td>142.40 (n/a)</td><td>51.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (+8.49%)</td><td>0.06 (+9.38%)</td><td>0.07 (+12.96%)</td><td>0.04 (+1.66%)</td><td>0.01 <b>(+38.58%)</b></td><td>184.10 (-1.66%)</td><td>141.68 (-7.54%)</td><td>125.60 (-11.49%)</td><td>120.80 (-7.79%)</td><td>27.67 <b>(+22.44%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.20 (n/a)</td><td>153.24 (n/a)</td><td>141.90 (n/a)</td><td>131.00 (n/a)</td><td>22.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (+2.23%)</td><td>0.05 (-3.25%)</td><td>0.05 (-6.96%)</td><td>0.04 (+6.05%)</td><td>0.01 (-15.13%)</td><td>190.40 (-5.70%)</td><td>160.74 (+2.23%)</td><td>158.40 (+7.46%)</td><td>123.20 (-2.14%)</td><td>25.41 <b>(-22.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>157.24 (n/a)</td><td>147.40 (n/a)</td><td>125.90 (n/a)</td><td>32.67 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (-17.33%)</td><td>0.05 (-15.70%)</td><td>0.04 (-13.71%)</td><td>0.04 (-16.70%)</td><td>0.01 <b>(-22.23%)</b></td><td>212.30 <b>(+20.01%)</b></td><td>183.66 (+18.35%)</td><td>182.90 (+15.91%)</td><td>146.60 <b>(+20.96%)</b></td><td>24.95 (+12.20%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.90 (n/a)</td><td>155.18 (n/a)</td><td>157.80 (n/a)</td><td>121.20 (n/a)</td><td>22.23 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 <b>(+44.97%)</b></td><td>0.05 (+3.33%)</td><td>0.05 (-5.09%)</td><td>0.03 <b>(-34.07%)</b></td><td>0.02 <b>(+229.09%)</b></td><td>308.10 <b>(+51.62%)</b></td><td>179.66 (+8.33%)</td><td>163.50 (+5.35%)</td><td>102.90 <b>(-31.03%)</b></td><td>77.00 <b>(+252.91%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>165.84 (n/a)</td><td>155.20 (n/a)</td><td>149.20 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (+4.91%)</td><td>0.05 (+0.57%)</td><td>0.05 (-9.51%)</td><td>0.04 (+5.24%)</td><td>0.01 (-18.33%)</td><td>196.00 (-4.99%)</td><td>170.12 (-1.24%)</td><td>170.70 (+10.49%)</td><td>145.80 (-4.71%)</td><td>19.47 <b>(-24.85%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.30 (n/a)</td><td>172.26 (n/a)</td><td>154.50 (n/a)</td><td>153.00 (n/a)</td><td>25.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (-1.60%)</td><td>0.04 (+2.17%)</td><td>0.04 (-1.78%)</td><td>0.03 (-0.05%)</td><td>0.01 (-6.76%)</td><td>314.40 (+0.06%)</td><td>228.06 (-2.58%)</td><td>216.70 (+1.78%)</td><td>176.20 (+1.61%)</td><td>53.06 (-4.33%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>314.20 (n/a)</td><td>234.10 (n/a)</td><td>212.90 (n/a)</td><td>173.40 (n/a)</td><td>55.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (+16.96%)</td><td>0.10 (-11.57%)</td><td>0.09 (-18.22%)</td><td>0.07 <b>(-33.08%)</b></td><td>0.03 <b>(+298.24%)</b></td><td>239.90 <b>(+49.47%)</b></td><td>179.00 (+19.41%)</td><td>183.70 <b>(+22.30%)</b></td><td>116.20 (-14.50%)</td><td>45.45 <b>(+399.91%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>160.50 (n/a)</td><td>149.90 (n/a)</td><td>150.20 (n/a)</td><td>135.90 (n/a)</td><td>9.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (-0.06%)</td><td>0.10 (+4.90%)</td><td>0.10 (+9.27%)</td><td>0.09 <b>(+54.12%)</b></td><td>0.01 <b>(-49.45%)</b></td><td>188.30 <b>(-35.14%)</b></td><td>167.66 (-10.71%)</td><td>170.50 (-8.48%)</td><td>134.40 (+0.07%)</td><td>21.40 <b>(-66.32%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>290.30 (n/a)</td><td>187.78 (n/a)</td><td>186.30 (n/a)</td><td>134.30 (n/a)</td><td>63.54 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (-15.09%)</td><td>0.09 (-12.98%)</td><td>0.09 <b>(-23.22%)</b></td><td>0.08 (+5.23%)</td><td>0.01 <b>(-47.42%)</b></td><td>210.20 (-4.97%)</td><td>182.10 (+10.87%)</td><td>189.20 <b>(+30.21%)</b></td><td>147.30 (+17.75%)</td><td>25.22 <b>(-41.50%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>221.20 (n/a)</td><td>164.24 (n/a)</td><td>145.30 (n/a)</td><td>125.10 (n/a)</td><td>43.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 <b>(-23.84%)</b></td><td>0.09 <b>(-20.79%)</b></td><td>0.09 (-19.13%)</td><td>0.07 (-14.83%)</td><td>0.02 <b>(-35.10%)</b></td><td>226.80 (+17.39%)</td><td>184.42 <b>(+24.76%)</b></td><td>185.00 <b>(+23.66%)</b></td><td>143.70 <b>(+31.35%)</b></td><td>30.48 (-0.61%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.20 (n/a)</td><td>147.82 (n/a)</td><td>149.60 (n/a)</td><td>109.40 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (+12.02%)</td><td>0.09 (-18.27%)</td><td>0.09 <b>(-20.07%)</b></td><td>0.04 <b>(-45.54%)</b></td><td>0.04 <b>(+90.23%)</b></td><td>367.90 <b>(+83.67%)</b></td><td>209.04 <b>(+37.13%)</b></td><td>186.50 <b>(+25.17%)</b></td><td>113.10 (-10.73%)</td><td>94.63 <b>(+223.28%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.30 (n/a)</td><td>152.44 (n/a)</td><td>149.00 (n/a)</td><td>126.70 (n/a)</td><td>29.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (+6.42%)</td><td>0.09 (-3.40%)</td><td>0.09 (-1.48%)</td><td>0.07 (-2.81%)</td><td>0.01 (+17.10%)</td><td>221.00 (+2.93%)</td><td>185.80 (+4.03%)</td><td>186.00 (+1.53%)</td><td>144.10 (-6.06%)</td><td>28.41 (+13.58%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>178.60 (n/a)</td><td>183.20 (n/a)</td><td>153.40 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (-8.42%)</td><td>0.08 (-1.84%)</td><td>0.07 (-5.61%)</td><td>0.06 <b>(+22.82%)</b></td><td>0.02 <b>(-22.88%)</b></td><td>266.30 (-18.59%)</td><td>207.72 (-2.65%)</td><td>228.00 (+5.95%)</td><td>137.50 (+9.21%)</td><td>52.01 <b>(-31.75%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>327.10 (n/a)</td><td>213.38 (n/a)</td><td>215.20 (n/a)</td><td>125.90 (n/a)</td><td>76.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (-8.94%)</td><td>0.07 (-9.85%)</td><td>0.07 (-12.33%)</td><td>0.05 (-14.79%)</td><td>0.01 (-4.30%)</td><td>343.30 (+17.37%)</td><td>251.64 (+11.52%)</td><td>238.10 (+14.09%)</td><td>198.20 (+9.81%)</td><td>54.35 <b>(+26.42%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>292.50 (n/a)</td><td>225.64 (n/a)</td><td>208.70 (n/a)</td><td>180.50 (n/a)</td><td>43.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.35 <b>(+32.36%)</b></td><td>0.21 (-4.24%)</td><td>0.17 (-19.27%)</td><td>0.16 (-12.18%)</td><td>0.08 <b>(+162.96%)</b></td><td>209.10 (+13.83%)</td><td>172.72 (+12.33%)</td><td>190.60 <b>(+23.93%)</b></td><td>94.30 <b>(-24.44%)</b></td><td>47.83 <b>(+124.32%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.70 (n/a)</td><td>153.76 (n/a)</td><td>153.80 (n/a)</td><td>124.80 (n/a)</td><td>21.32 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 <b>(-22.89%)</b></td><td>0.18 (-13.80%)</td><td>0.19 (-11.26%)</td><td>0.16 (-12.11%)</td><td>0.01 <b>(-50.08%)</b></td><td>203.80 (+13.79%)</td><td>181.94 (+15.28%)</td><td>176.10 (+12.67%)</td><td>172.50 <b>(+29.70%)</b></td><td>12.92 <b>(-25.53%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>179.10 (n/a)</td><td>157.82 (n/a)</td><td>156.30 (n/a)</td><td>133.00 (n/a)</td><td>17.35 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.23 (+7.37%)</td><td>0.19 (+3.48%)</td><td>0.19 (+3.18%)</td><td>0.16 (+11.30%)</td><td>0.02 (-8.48%)</td><td>203.70 (-10.19%)</td><td>172.88 (-3.89%)</td><td>174.10 (-3.06%)</td><td>145.10 (-6.87%)</td><td>22.06 <b>(-23.31%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>226.80 (n/a)</td><td>179.88 (n/a)</td><td>179.60 (n/a)</td><td>155.80 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.29 <b>(+21.86%)</b></td><td>0.20 (+7.08%)</td><td>0.18 (-2.33%)</td><td>0.14 (+2.45%)</td><td>0.06 <b>(+55.29%)</b></td><td>229.00 (-2.39%)</td><td>171.18 (-3.87%)</td><td>178.30 (+2.35%)</td><td>114.10 (-17.97%)</td><td>45.91 <b>(+22.75%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>234.60 (n/a)</td><td>178.08 (n/a)</td><td>174.20 (n/a)</td><td>139.10 (n/a)</td><td>37.40 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 <b>(-23.70%)</b></td><td>0.17 (-7.08%)</td><td>0.17 (-2.54%)</td><td>0.14 (+10.58%)</td><td>0.03 <b>(-51.14%)</b></td><td>239.50 (-9.59%)</td><td>191.78 (+2.42%)</td><td>189.90 (+2.65%)</td><td>149.90 <b>(+31.15%)</b></td><td>31.98 <b>(-40.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>264.90 (n/a)</td><td>187.24 (n/a)</td><td>185.00 (n/a)</td><td>114.30 (n/a)</td><td>53.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (+2.77%)</td><td>0.17 (-12.40%)</td><td>0.18 (-7.13%)</td><td>0.10 <b>(-31.62%)</b></td><td>0.06 <b>(+111.58%)</b></td><td>315.80 <b>(+46.27%)</b></td><td>217.12 <b>(+25.04%)</b></td><td>178.40 (+7.66%)</td><td>146.10 (-2.73%)</td><td>82.14 <b>(+204.65%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.90 (n/a)</td><td>173.64 (n/a)</td><td>165.70 (n/a)</td><td>150.20 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (-7.96%)</td><td>0.15 (-17.37%)</td><td>0.15 <b>(-28.42%)</b></td><td>0.13 (-7.94%)</td><td>0.02 <b>(-26.11%)</b></td><td>256.90 (+8.63%)</td><td>220.98 (+19.69%)</td><td>224.70 <b>(+39.65%)</b></td><td>169.40 (+8.66%)</td><td>32.10 (-13.98%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.50 (n/a)</td><td>184.62 (n/a)</td><td>160.90 (n/a)</td><td>155.90 (n/a)</td><td>37.32 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 <b>(-24.79%)</b></td><td>0.03 (-17.15%)</td><td>0.02 <b>(-26.37%)</b></td><td>0.02 (+1.26%)</td><td>0.00 <b>(-63.40%)</b></td><td>186.70 (-1.27%)</td><td>161.10 (+14.47%)</td><td>165.70 <b>(+35.82%)</b></td><td>138.60 <b>(+33.01%)</b></td><td>19.17 <b>(-53.15%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>140.74 (n/a)</td><td>122.00 (n/a)</td><td>104.20 (n/a)</td><td>40.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-19.88%)</td><td>0.02 <b>(-20.46%)</b></td><td>0.02 <b>(-27.32%)</b></td><td>0.02 (-6.71%)</td><td>0.00 <b>(-29.03%)</b></td><td>225.40 (+7.18%)</td><td>191.08 <b>(+24.11%)</b></td><td>205.40 <b>(+37.58%)</b></td><td>147.30 <b>(+24.83%)</b></td><td>33.75 (-6.00%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>153.96 (n/a)</td><td>149.30 (n/a)</td><td>118.00 (n/a)</td><td>35.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-69.28%)</b></td><td>4746029.40 (-0.00%)</td><td>4746023.70 (-0.00%)</td><td>4746023.70 (-0.00%)</td><td>4746018.00 (-0.00%)</td><td>8.06 <b>(-69.61%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4746071.60 (n/a)</td><td>4746048.43 (n/a)</td><td>4746054.20 (n/a)</td><td>4746019.50 (n/a)</td><td>26.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (-2.75%)</td><td>0.02 (-1.44%)</td><td>0.02 (-6.80%)</td><td>0.02 (+4.29%)</td><td>0.00 <b>(-36.77%)</b></td><td>224.80 (-4.14%)</td><td>198.86 (+0.13%)</td><td>202.50 (+7.31%)</td><td>173.20 (+2.85%)</td><td>20.37 <b>(-38.45%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.50 (n/a)</td><td>198.60 (n/a)</td><td>188.70 (n/a)</td><td>168.40 (n/a)</td><td>33.10 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-3.36%)</td><td>0.02 (-0.51%)</td><td>0.02 (-5.88%)</td><td>0.02 <b>(+30.32%)</b></td><td>0.00 <b>(-44.55%)</b></td><td>198.90 <b>(-23.26%)</b></td><td>173.34 (-2.83%)</td><td>174.20 (+6.22%)</td><td>146.60 (+3.53%)</td><td>19.73 <b>(-57.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>259.20 (n/a)</td><td>178.38 (n/a)</td><td>164.00 (n/a)</td><td>141.60 (n/a)</td><td>46.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-13.00%)</td><td>0.02 (-4.47%)</td><td>0.02 (-0.58%)</td><td>0.02 (+5.36%)</td><td>0.00 <b>(-34.40%)</b></td><td>199.10 (-5.05%)</td><td>170.68 (+3.13%)</td><td>167.70 (+0.54%)</td><td>144.80 (+14.92%)</td><td>22.46 <b>(-27.81%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.70 (n/a)</td><td>165.50 (n/a)</td><td>166.80 (n/a)</td><td>126.00 (n/a)</td><td>31.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (+1.69%)</td><td>0.03 (-12.63%)</td><td>0.03 (-18.72%)</td><td>0.02 (-9.45%)</td><td>0.01 <b>(+21.45%)</b></td><td>225.50 (+10.43%)</td><td>170.68 (+16.33%)</td><td>163.80 <b>(+23.07%)</b></td><td>125.20 (-1.73%)</td><td>41.66 <b>(+28.75%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.20 (n/a)</td><td>146.72 (n/a)</td><td>133.10 (n/a)</td><td>127.40 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+4.53%)</td><td>0.03 (+10.74%)</td><td>0.03 <b>(+42.66%)</b></td><td>0.02 (+1.55%)</td><td>0.01 <b>(+39.68%)</b></td><td>207.00 (-1.52%)</td><td>153.84 (-6.50%)</td><td>123.20 <b>(-29.92%)</b></td><td>115.10 (-4.32%)</td><td>48.16 <b>(+36.72%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>164.54 (n/a)</td><td>175.80 (n/a)</td><td>120.30 (n/a)</td><td>35.23 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+15.61%)</td><td>0.02 (-8.41%)</td><td>0.02 (-10.57%)</td><td>0.02 (-2.85%)</td><td>0.01 <b>(+30.45%)</b></td><td>205.80 (+2.95%)</td><td>176.58 (+11.70%)</td><td>186.30 (+11.82%)</td><td>102.30 (-13.45%)</td><td>42.64 (+16.24%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>158.08 (n/a)</td><td>166.60 (n/a)</td><td>118.20 (n/a)</td><td>36.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (+11.30%)</td><td>0.02 (+11.32%)</td><td>0.02 (+6.13%)</td><td>0.02 (+4.27%)</td><td>0.00 <b>(+59.86%)</b></td><td>201.30 (-4.10%)</td><td>172.04 (-8.89%)</td><td>177.30 (-5.74%)</td><td>138.60 (-10.17%)</td><td>30.26 <b>(+39.51%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.90 (n/a)</td><td>188.82 (n/a)</td><td>188.10 (n/a)</td><td>154.30 (n/a)</td><td>21.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 <b>(+21.64%)</b></td><td>0.03 (+17.29%)</td><td>0.02 (-2.87%)</td><td>0.02 <b>(+33.05%)</b></td><td>0.01 <b>(+42.99%)</b></td><td>182.40 <b>(-24.85%)</b></td><td>146.90 (-13.87%)</td><td>165.20 (+2.99%)</td><td>103.50 (-17.79%)</td><td>36.43 (-15.99%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.70 (n/a)</td><td>170.56 (n/a)</td><td>160.40 (n/a)</td><td>125.90 (n/a)</td><td>43.36 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-5.06%)</td><td>0.02 (+2.84%)</td><td>0.02 (+11.85%)</td><td>0.02 (-2.31%)</td><td>0.01 (-7.92%)</td><td>230.10 (+2.40%)</td><td>177.72 (-3.11%)</td><td>174.10 (-10.63%)</td><td>137.50 (+5.36%)</td><td>38.32 (-1.59%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>183.42 (n/a)</td><td>194.80 (n/a)</td><td>130.50 (n/a)</td><td>38.94 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+7.72%)</td><td>0.02 (-12.92%)</td><td>0.02 (-18.64%)</td><td>0.02 <b>(-32.51%)</b></td><td>0.01 <b>(+115.98%)</b></td><td>258.50 <b>(+48.22%)</b></td><td>178.30 <b>(+22.49%)</b></td><td>179.90 <b>(+22.88%)</b></td><td>115.10 (-7.18%)</td><td>55.34 <b>(+192.85%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.40 (n/a)</td><td>145.56 (n/a)</td><td>146.40 (n/a)</td><td>124.00 (n/a)</td><td>18.90 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-3.61%)</td><td>0.02 (-9.57%)</td><td>0.02 (-8.18%)</td><td>0.02 (-10.25%)</td><td>0.01 (+18.41%)</td><td>238.70 (+11.44%)</td><td>186.04 (+13.01%)</td><td>173.60 (+8.91%)</td><td>129.10 (+3.69%)</td><td>47.76 <b>(+41.99%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>164.62 (n/a)</td><td>159.40 (n/a)</td><td>124.50 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (+7.68%)</td><td>0.02 (-12.50%)</td><td>0.02 (-16.16%)</td><td>0.01 <b>(-37.45%)</b></td><td>0.01 <b>(+258.26%)</b></td><td>298.20 <b>(+59.89%)</b></td><td>202.88 <b>(+21.27%)</b></td><td>195.80 (+19.24%)</td><td>146.80 (-7.15%)</td><td>60.19 <b>(+427.33%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.50 (n/a)</td><td>167.30 (n/a)</td><td>164.20 (n/a)</td><td>158.10 (n/a)</td><td>11.41 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (+9.02%)</td><td>0.02 (-10.19%)</td><td>0.02 <b>(-24.88%)</b></td><td>0.02 (-16.21%)</td><td>0.01 <b>(+75.51%)</b></td><td>214.30 (+19.32%)</td><td>180.50 (+15.42%)</td><td>200.50 <b>(+33.13%)</b></td><td>117.30 (-8.22%)</td><td>41.23 <b>(+88.97%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.60 (n/a)</td><td>156.38 (n/a)</td><td>150.60 (n/a)</td><td>127.80 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (-15.70%)</td><td>0.05 (-8.22%)</td><td>0.05 (+3.29%)</td><td>0.04 (-10.10%)</td><td>0.01 <b>(-37.91%)</b></td><td>204.80 (+11.24%)</td><td>171.08 (+7.84%)</td><td>163.50 (-3.20%)</td><td>150.00 (+18.58%)</td><td>20.83 (-16.25%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>158.64 (n/a)</td><td>168.90 (n/a)</td><td>126.50 (n/a)</td><td>24.87 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (+8.59%)</td><td>0.06 (+7.50%)</td><td>0.05 (+2.95%)</td><td>0.05 (+18.80%)</td><td>0.01 (-7.74%)</td><td>163.10 (-15.84%)</td><td>147.82 (-7.60%)</td><td>157.40 (-2.90%)</td><td>120.60 (-7.94%)</td><td>18.93 <b>(-26.60%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>159.98 (n/a)</td><td>162.10 (n/a)</td><td>131.00 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 <b>(-21.73%)</b></td><td>0.04 (-11.96%)</td><td>0.04 (-9.59%)</td><td>0.03 <b>(+25.13%)</b></td><td>0.01 <b>(-59.72%)</b></td><td>238.00 <b>(-20.11%)</b></td><td>204.64 (+5.94%)</td><td>188.80 (+10.60%)</td><td>175.30 <b>(+27.77%)</b></td><td>29.05 <b>(-56.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.90 (n/a)</td><td>193.16 (n/a)</td><td>170.70 (n/a)</td><td>137.20 (n/a)</td><td>67.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (-4.58%)</td><td>0.04 (-7.72%)</td><td>0.05 (+4.02%)</td><td>0.03 (-18.38%)</td><td>0.01 <b>(+64.82%)</b></td><td>253.00 <b>(+22.52%)</b></td><td>200.14 (+11.04%)</td><td>178.70 (-3.87%)</td><td>162.50 (+4.77%)</td><td>42.60 <b>(+114.18%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>180.24 (n/a)</td><td>185.90 (n/a)</td><td>155.10 (n/a)</td><td>19.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (-19.69%)</td><td>0.05 (-4.53%)</td><td>0.05 (-4.55%)</td><td>0.04 (+2.12%)</td><td>0.01 <b>(-52.21%)</b></td><td>189.30 (-2.07%)</td><td>162.68 (+1.71%)</td><td>159.80 (+4.79%)</td><td>139.40 <b>(+24.46%)</b></td><td>19.47 <b>(-43.13%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>159.94 (n/a)</td><td>152.50 (n/a)</td><td>112.00 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (+12.69%)</td><td>0.05 (+6.00%)</td><td>0.05 (+2.01%)</td><td>0.04 (+4.32%)</td><td>0.01 <b>(+21.46%)</b></td><td>198.10 (-4.11%)</td><td>155.76 (-5.12%)</td><td>157.40 (-1.93%)</td><td>122.30 (-11.31%)</td><td>29.37 (+4.27%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>164.16 (n/a)</td><td>160.50 (n/a)</td><td>137.90 (n/a)</td><td>28.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 <b>(+26.24%)</b></td><td>0.06 (+8.60%)</td><td>0.05 (+4.54%)</td><td>0.05 (-3.94%)</td><td>0.01 <b>(+120.88%)</b></td><td>178.90 (+4.13%)</td><td>147.64 (-6.55%)</td><td>149.20 (-4.36%)</td><td>115.30 <b>(-20.76%)</b></td><td>22.65 <b>(+79.20%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>171.80 (n/a)</td><td>157.98 (n/a)</td><td>156.00 (n/a)</td><td>145.50 (n/a)</td><td>12.64 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (-2.45%)</td><td>0.05 (+0.85%)</td><td>0.05 (+6.56%)</td><td>0.04 (-10.41%)</td><td>0.01 (+8.01%)</td><td>194.10 (+11.62%)</td><td>159.18 (-0.25%)</td><td>156.20 (-6.13%)</td><td>126.20 (+2.52%)</td><td>26.41 <b>(+25.71%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.90 (n/a)</td><td>159.58 (n/a)</td><td>166.40 (n/a)</td><td>123.10 (n/a)</td><td>21.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (-4.00%)</td><td>0.06 (+11.24%)</td><td>0.06 <b>(+24.71%)</b></td><td>0.04 (+1.01%)</td><td>0.01 (-13.06%)</td><td>195.60 (-1.01%)</td><td>146.52 (-10.79%)</td><td>131.40 (-19.83%)</td><td>122.60 (+4.16%)</td><td>29.59 (-10.15%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>164.24 (n/a)</td><td>163.90 (n/a)</td><td>117.70 (n/a)</td><td>32.93 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (+3.04%)</td><td>0.05 (+1.61%)</td><td>0.05 (+5.13%)</td><td>0.05 (-3.52%)</td><td>0.00 <b>(+100.07%)</b></td><td>178.00 (+3.67%)</td><td>160.54 (-1.17%)</td><td>153.90 (-4.82%)</td><td>148.70 (-3.00%)</td><td>13.63 <b>(+101.45%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>171.70 (n/a)</td><td>162.44 (n/a)</td><td>161.70 (n/a)</td><td>153.30 (n/a)</td><td>6.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (-9.19%)</td><td>0.05 (-8.44%)</td><td>0.05 (-10.84%)</td><td>0.04 (-3.15%)</td><td>0.01 (-12.20%)</td><td>206.40 (+3.25%)</td><td>164.62 (+8.76%)</td><td>165.00 (+12.17%)</td><td>124.30 (+10.10%)</td><td>30.92 (-1.60%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>151.36 (n/a)</td><td>147.10 (n/a)</td><td>112.90 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (+14.04%)</td><td>0.05 (+8.96%)</td><td>0.05 (+8.93%)</td><td>0.05 (+10.83%)</td><td>0.01 <b>(+34.12%)</b></td><td>162.40 (-9.78%)</td><td>153.24 (-8.05%)</td><td>158.50 (-8.22%)</td><td>130.10 (-12.33%)</td><td>13.39 (+5.77%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>180.00 (n/a)</td><td>166.66 (n/a)</td><td>172.70 (n/a)</td><td>148.40 (n/a)</td><td>12.66 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (+1.86%)</td><td>0.05 (-8.37%)</td><td>0.05 (+0.74%)</td><td>0.03 (-17.18%)</td><td>0.01 (+18.96%)</td><td>243.70 <b>(+20.76%)</b></td><td>171.52 (+11.54%)</td><td>156.50 (-0.70%)</td><td>121.60 (-1.86%)</td><td>45.89 <b>(+46.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>153.78 (n/a)</td><td>157.60 (n/a)</td><td>123.90 (n/a)</td><td>31.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (+2.33%)</td><td>0.05 (-1.16%)</td><td>0.06 (+7.84%)</td><td>0.04 (-17.33%)</td><td>0.01 <b>(+102.06%)</b></td><td>210.40 <b>(+20.99%)</b></td><td>162.70 (+3.17%)</td><td>146.80 (-7.26%)</td><td>136.20 (-2.30%)</td><td>30.14 <b>(+143.70%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>173.90 (n/a)</td><td>157.70 (n/a)</td><td>158.30 (n/a)</td><td>139.40 (n/a)</td><td>12.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 <b>(+41.63%)</b></td><td>0.05 (+6.70%)</td><td>0.05 (+3.26%)</td><td>0.03 <b>(-27.56%)</b></td><td>0.02 <b>(+333.55%)</b></td><td>242.60 <b>(+38.08%)</b></td><td>163.88 (+0.44%)</td><td>155.10 (-3.18%)</td><td>103.30 <b>(-29.39%)</b></td><td>50.22 <b>(+321.98%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>175.70 (n/a)</td><td>163.16 (n/a)</td><td>160.20 (n/a)</td><td>146.30 (n/a)</td><td>11.90 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (-11.84%)</td><td>0.05 (-17.60%)</td><td>0.05 (-15.93%)</td><td>0.04 <b>(-27.90%)</b></td><td>0.01 (+6.60%)</td><td>213.00 <b>(+38.67%)</b></td><td>167.32 <b>(+22.67%)</b></td><td>165.70 (+18.95%)</td><td>129.90 (+13.45%)</td><td>30.10 <b>(+66.30%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>153.60 (n/a)</td><td>136.40 (n/a)</td><td>139.30 (n/a)</td><td>114.50 (n/a)</td><td>18.10 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (-15.83%)</td><td>0.11 (-11.10%)</td><td>0.11 (-9.09%)</td><td>0.09 (-5.59%)</td><td>0.01 <b>(-42.76%)</b></td><td>186.20 (+5.92%)</td><td>157.08 (+11.04%)</td><td>152.80 (+10.01%)</td><td>138.30 (+18.81%)</td><td>17.93 <b>(-26.09%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>175.80 (n/a)</td><td>141.46 (n/a)</td><td>138.90 (n/a)</td><td>116.40 (n/a)</td><td>24.26 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (-0.22%)</td><td>0.12 (+6.02%)</td><td>0.12 <b>(+20.53%)</b></td><td>0.10 (+2.30%)</td><td>0.02 (-7.04%)</td><td>166.90 (-2.28%)</td><td>143.62 (-6.02%)</td><td>137.50 (-17.07%)</td><td>110.20 (+0.18%)</td><td>23.82 (-5.51%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>170.80 (n/a)</td><td>152.82 (n/a)</td><td>165.80 (n/a)</td><td>110.00 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (+13.67%)</td><td>0.08 (-0.56%)</td><td>0.07 (-2.25%)</td><td>0.06 <b>(-20.88%)</b></td><td>0.02 <b>(+109.91%)</b></td><td>281.60 <b>(+26.39%)</b></td><td>213.40 (+4.96%)</td><td>219.10 (+2.29%)</td><td>147.50 (-11.99%)</td><td>54.07 <b>(+129.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>203.32 (n/a)</td><td>214.20 (n/a)</td><td>167.60 (n/a)</td><td>23.53 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (+3.09%)</td><td>0.09 (-2.93%)</td><td>0.08 (-2.79%)</td><td>0.07 (-8.13%)</td><td>0.01 <b>(+35.12%)</b></td><td>221.80 (+8.83%)</td><td>192.80 (+4.04%)</td><td>197.80 (+2.86%)</td><td>152.20 (-3.00%)</td><td>29.67 <b>(+42.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>185.32 (n/a)</td><td>192.30 (n/a)</td><td>156.90 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 <b>(+45.77%)</b></td><td>0.10 (+4.02%)</td><td>0.09 (+1.27%)</td><td>0.05 <b>(-39.49%)</b></td><td>0.04 <b>(+257.26%)</b></td><td>325.80 <b>(+65.30%)</b></td><td>189.38 (+10.36%)</td><td>173.80 (-1.25%)</td><td>101.40 <b>(-31.44%)</b></td><td>85.46 <b>(+316.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>171.60 (n/a)</td><td>176.00 (n/a)</td><td>147.90 (n/a)</td><td>20.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (-11.83%)</td><td>0.10 (-13.05%)</td><td>0.10 (-8.70%)</td><td>0.08 <b>(-22.02%)</b></td><td>0.02 (+15.04%)</td><td>214.60 <b>(+28.20%)</b></td><td>171.46 (+16.51%)</td><td>159.90 (+9.52%)</td><td>137.30 (+13.47%)</td><td>32.40 <b>(+66.34%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>167.40 (n/a)</td><td>147.16 (n/a)</td><td>146.00 (n/a)</td><td>121.00 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (+8.91%)</td><td>0.10 (-2.99%)</td><td>0.10 (-6.86%)</td><td>0.09 (-9.41%)</td><td>0.01 <b>(+81.46%)</b></td><td>182.00 (+10.44%)</td><td>158.40 (+3.94%)</td><td>160.50 (+7.36%)</td><td>129.70 (-8.21%)</td><td>18.71 <b>(+79.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>164.80 (n/a)</td><td>152.40 (n/a)</td><td>149.50 (n/a)</td><td>141.30 (n/a)</td><td>10.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (-9.97%)</td><td>0.11 (+5.25%)</td><td>0.11 (+5.53%)</td><td>0.09 (+9.11%)</td><td>0.01 <b>(-36.65%)</b></td><td>178.60 (-8.36%)</td><td>151.16 (-6.39%)</td><td>153.10 (-5.26%)</td><td>132.60 (+11.06%)</td><td>18.17 <b>(-33.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.90 (n/a)</td><td>161.48 (n/a)</td><td>161.60 (n/a)</td><td>119.40 (n/a)</td><td>27.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (-16.77%)</td><td>0.10 (-9.38%)</td><td>0.09 (-9.50%)</td><td>0.07 (-9.94%)</td><td>0.02 <b>(-23.08%)</b></td><td>222.90 (+11.01%)</td><td>178.38 (+9.46%)</td><td>183.60 (+10.47%)</td><td>127.60 <b>(+20.15%)</b></td><td>37.54 (+7.03%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>200.80 (n/a)</td><td>162.96 (n/a)</td><td>166.20 (n/a)</td><td>106.20 (n/a)</td><td>35.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (+14.16%)</td><td>0.10 (+17.63%)</td><td>0.11 (+18.67%)</td><td>0.08 <b>(+36.56%)</b></td><td>0.01 (-6.79%)</td><td>194.90 <b>(-26.76%)</b></td><td>167.90 (-16.08%)</td><td>155.90 (-15.73%)</td><td>140.90 (-12.43%)</td><td>24.71 <b>(-39.57%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>266.10 (n/a)</td><td>200.06 (n/a)</td><td>185.00 (n/a)</td><td>160.90 (n/a)</td><td>40.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (+12.70%)</td><td>0.11 (+4.41%)</td><td>0.10 (-4.27%)</td><td>0.08 (-4.76%)</td><td>0.02 <b>(+59.68%)</b></td><td>193.40 (+4.99%)</td><td>158.36 (-2.57%)</td><td>170.90 (+4.46%)</td><td>125.10 (-11.21%)</td><td>30.03 <b>(+44.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>162.54 (n/a)</td><td>163.60 (n/a)</td><td>140.90 (n/a)</td><td>20.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (-8.69%)</td><td>0.10 (+2.65%)</td><td>0.11 (+10.11%)</td><td>0.08 (-2.02%)</td><td>0.01 (-15.07%)</td><td>211.40 (+2.08%)</td><td>169.28 (-2.91%)</td><td>155.20 (-9.19%)</td><td>152.60 (+9.47%)</td><td>24.81 (-4.74%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>174.36 (n/a)</td><td>170.90 (n/a)</td><td>139.40 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 <b>(-23.86%)</b></td><td>0.08 (-9.65%)</td><td>0.08 (-13.04%)</td><td>0.07 <b>(+45.01%)</b></td><td>0.01 <b>(-69.37%)</b></td><td>228.90 <b>(-31.05%)</b></td><td>199.68 (+1.65%)</td><td>195.80 (+14.97%)</td><td>175.70 <b>(+31.32%)</b></td><td>20.00 <b>(-74.27%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>332.00 (n/a)</td><td>196.44 (n/a)</td><td>170.30 (n/a)</td><td>133.80 (n/a)</td><td>77.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (+18.77%)</td><td>0.09 (-11.01%)</td><td>0.08 (-19.12%)</td><td>0.06 <b>(-36.71%)</b></td><td>0.03 <b>(+180.09%)</b></td><td>270.00 <b>(+57.99%)</b></td><td>187.62 <b>(+20.81%)</b></td><td>199.00 <b>(+23.68%)</b></td><td>116.50 (-15.82%)</td><td>58.10 <b>(+271.98%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>170.90 (n/a)</td><td>155.30 (n/a)</td><td>160.90 (n/a)</td><td>138.40 (n/a)</td><td>15.62 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (+14.26%)</td><td>0.09 (-8.50%)</td><td>0.08 <b>(-25.29%)</b></td><td>0.07 (-10.29%)</td><td>0.02 <b>(+102.68%)</b></td><td>221.40 (+11.48%)</td><td>189.80 (+13.34%)</td><td>217.10 <b>(+33.85%)</b></td><td>128.40 (-12.47%)</td><td>42.72 <b>(+104.29%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>167.46 (n/a)</td><td>162.20 (n/a)</td><td>146.70 (n/a)</td><td>20.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (+6.88%)</td><td>0.09 (-2.72%)</td><td>0.09 (-0.01%)</td><td>0.07 (-14.28%)</td><td>0.02 <b>(+88.38%)</b></td><td>242.40 (+16.65%)</td><td>191.50 (+5.27%)</td><td>179.00 (+0.00%)</td><td>151.60 (-6.42%)</td><td>38.97 <b>(+107.38%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>181.92 (n/a)</td><td>179.00 (n/a)</td><td>162.00 (n/a)</td><td>18.79 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (+14.07%)</td><td>0.20 (-1.55%)</td><td>0.19 (-5.63%)</td><td>0.15 (+5.12%)</td><td>0.05 <b>(+33.98%)</b></td><td>217.60 (-4.85%)</td><td>172.10 (+2.84%)</td><td>171.20 (+6.01%)</td><td>116.40 (-12.35%)</td><td>37.96 (+4.70%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>228.70 (n/a)</td><td>167.34 (n/a)</td><td>161.50 (n/a)</td><td>132.80 (n/a)</td><td>36.25 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (-1.16%)</td><td>0.21 (-9.91%)</td><td>0.21 (-13.78%)</td><td>0.17 (-19.73%)</td><td>0.04 <b>(+79.17%)</b></td><td>194.50 <b>(+24.60%)</b></td><td>157.42 (+13.09%)</td><td>155.20 (+15.99%)</td><td>129.20 (+1.17%)</td><td>27.94 <b>(+122.40%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>156.10 (n/a)</td><td>139.20 (n/a)</td><td>133.80 (n/a)</td><td>127.70 (n/a)</td><td>12.56 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (-5.67%)</td><td>0.18 (+2.07%)</td><td>0.18 (+10.80%)</td><td>0.14 (-4.26%)</td><td>0.03 (-7.93%)</td><td>229.70 (+4.46%)</td><td>188.76 (-2.14%)</td><td>187.10 (-9.74%)</td><td>158.30 (+6.03%)</td><td>29.03 (+1.83%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.90 (n/a)</td><td>192.88 (n/a)</td><td>207.30 (n/a)</td><td>149.30 (n/a)</td><td>28.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (+18.32%)</td><td>0.17 (+9.79%)</td><td>0.18 (+17.57%)</td><td>0.13 (-10.18%)</td><td>0.03 <b>(+94.85%)</b></td><td>244.90 (+11.32%)</td><td>193.18 (-7.11%)</td><td>184.60 (-14.97%)</td><td>147.10 (-15.46%)</td><td>35.78 <b>(+84.57%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>220.00 (n/a)</td><td>207.96 (n/a)</td><td>217.10 (n/a)</td><td>174.00 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.30 (+7.34%)</td><td>0.22 (+5.98%)</td><td>0.22 (+7.05%)</td><td>0.16 (-1.34%)</td><td>0.05 <b>(+21.82%)</b></td><td>207.20 (+1.32%)</td><td>154.28 (-4.35%)</td><td>151.20 (-6.55%)</td><td>108.50 (-6.79%)</td><td>36.65 (+17.62%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>204.50 (n/a)</td><td>161.30 (n/a)</td><td>161.80 (n/a)</td><td>116.40 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (+13.91%)</td><td>0.21 (+0.38%)</td><td>0.19 (-6.81%)</td><td>0.19 (+3.59%)</td><td>0.04 <b>(+50.03%)</b></td><td>172.40 (-3.47%)</td><td>159.56 (+0.72%)</td><td>170.30 (+7.31%)</td><td>116.10 (-12.24%)</td><td>24.41 <b>(+24.61%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>178.60 (n/a)</td><td>158.42 (n/a)</td><td>158.70 (n/a)</td><td>132.30 (n/a)</td><td>19.59 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (-2.63%)</td><td>0.20 (+1.26%)</td><td>0.19 (-0.93%)</td><td>0.16 (+18.83%)</td><td>0.03 <b>(-26.69%)</b></td><td>201.10 (-15.86%)</td><td>167.36 (-3.30%)</td><td>168.40 (+0.96%)</td><td>132.80 (+2.71%)</td><td>24.25 <b>(-39.53%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>239.00 (n/a)</td><td>173.08 (n/a)</td><td>166.80 (n/a)</td><td>129.30 (n/a)</td><td>40.10 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 <b>(+26.86%)</b></td><td>0.20 (+10.57%)</td><td>0.19 (+2.53%)</td><td>0.17 (+8.32%)</td><td>0.03 <b>(+106.98%)</b></td><td>188.60 (-7.68%)</td><td>164.64 (-8.45%)</td><td>168.30 (-2.49%)</td><td>130.20 <b>(-21.14%)</b></td><td>23.78 <b>(+50.23%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.30 (n/a)</td><td>179.84 (n/a)</td><td>172.60 (n/a)</td><td>165.10 (n/a)</td><td>15.83 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.26 (-5.99%)</td><td>0.21 (+15.02%)</td><td>0.20 (+19.77%)</td><td>0.12 <b>(+22.36%)</b></td><td>0.06 (-13.80%)</td><td>272.10 (-18.26%)</td><td>171.64 (-16.13%)</td><td>163.50 (-16.50%)</td><td>128.00 (+6.40%)</td><td>58.97 <b>(-26.08%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>332.90 (n/a)</td><td>204.66 (n/a)</td><td>195.80 (n/a)</td><td>120.30 (n/a)</td><td>79.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (+9.74%)</td><td>0.19 (+19.98%)</td><td>0.20 (+19.43%)</td><td>0.16 <b>(+73.80%)</b></td><td>0.02 <b>(-37.28%)</b></td><td>205.10 <b>(-42.45%)</b></td><td>175.92 <b>(-21.08%)</b></td><td>162.30 (-16.25%)</td><td>153.10 (-8.87%)</td><td>23.68 <b>(-68.79%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>356.40 (n/a)</td><td>222.92 (n/a)</td><td>193.80 (n/a)</td><td>168.00 (n/a)</td><td>75.88 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (+7.60%)</td><td>0.19 (+6.16%)</td><td>0.20 (+6.20%)</td><td>0.16 (+0.29%)</td><td>0.02 <b>(+20.19%)</b></td><td>210.30 (-0.28%)</td><td>172.28 (-5.47%)</td><td>167.60 (-5.84%)</td><td>147.20 (-7.07%)</td><td>23.26 (+13.38%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.90 (n/a)</td><td>182.24 (n/a)</td><td>178.00 (n/a)</td><td>158.40 (n/a)</td><td>20.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (+13.89%)</td><td>0.18 (+6.46%)</td><td>0.18 (+4.81%)</td><td>0.16 (+0.80%)</td><td>0.02 <b>(+76.66%)</b></td><td>207.70 (-0.81%)</td><td>181.32 (-5.66%)</td><td>178.00 (-4.61%)</td><td>160.00 (-12.18%)</td><td>17.14 <b>(+54.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>192.20 (n/a)</td><td>186.60 (n/a)</td><td>182.20 (n/a)</td><td>11.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (-10.05%)</td><td>0.17 (-4.44%)</td><td>0.17 (-9.21%)</td><td>0.14 (-4.78%)</td><td>0.02 <b>(-20.85%)</b></td><td>229.70 (+5.03%)</td><td>192.18 (+4.11%)</td><td>194.10 (+10.16%)</td><td>169.60 (+11.14%)</td><td>24.79 (-10.56%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>218.70 (n/a)</td><td>184.60 (n/a)</td><td>176.20 (n/a)</td><td>152.60 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (+9.06%)</td><td>0.18 (+6.66%)</td><td>0.19 (+11.40%)</td><td>0.15 (-5.03%)</td><td>0.02 <b>(+105.13%)</b></td><td>218.10 (+5.31%)</td><td>185.22 (-5.46%)</td><td>175.00 (-10.21%)</td><td>164.20 (-8.32%)</td><td>22.38 <b>(+98.38%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>195.92 (n/a)</td><td>194.90 (n/a)</td><td>179.10 (n/a)</td><td>11.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (+3.45%)</td><td>0.19 (+16.86%)</td><td>0.18 (+8.29%)</td><td>0.18 <b>(+63.59%)</b></td><td>0.01 <b>(-73.65%)</b></td><td>181.50 <b>(-38.89%)</b></td><td>175.86 (-17.39%)</td><td>180.60 (-7.67%)</td><td>164.90 (-3.34%)</td><td>7.51 <b>(-84.89%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>297.00 (n/a)</td><td>212.88 (n/a)</td><td>195.60 (n/a)</td><td>170.60 (n/a)</td><td>49.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.24 (-6.28%)</td><td>0.18 (-7.07%)</td><td>0.16 (-4.73%)</td><td>0.15 (-0.19%)</td><td>0.04 (-17.74%)</td><td>221.70 (+0.18%)</td><td>189.56 (+6.34%)</td><td>199.00 (+4.96%)</td><td>136.40 (+6.73%)</td><td>36.26 (-10.78%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>221.30 (n/a)</td><td>178.26 (n/a)</td><td>189.60 (n/a)</td><td>127.80 (n/a)</td><td>40.65 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (+0.59%)</td><td>0.16 (+0.05%)</td><td>0.16 (-0.03%)</td><td>0.16 (-0.23%)</td><td>0.00 <b>(+421.75%)</b></td><td>52419.70 (+0.23%)</td><td>52233.62 (-0.05%)</td><td>52268.80 (+0.03%)</td><td>51896.90 (-0.59%)</td><td>198.36 <b>(+419.47%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52300.00 (n/a)</td><td>52258.18 (n/a)</td><td>52255.20 (n/a)</td><td>52202.50 (n/a)</td><td>38.18 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52455.50 (n/a)</td><td>52292.42 (n/a)</td><td>52243.30 (n/a)</td><td>52193.70 (n/a)</td><td>104.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>413164.40 (n/a)</td><td>413129.86 (n/a)</td><td>413144.30 (n/a)</td><td>413074.50 (n/a)</td><td>35.41 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (+16.22%)</td><td>0.15 (+10.36%)</td><td>0.14 (+14.35%)</td><td>0.12 (+18.03%)</td><td>0.04 (+10.74%)</td><td>196.90 (-15.28%)</td><td>166.82 (-9.87%)</td><td>175.80 (-12.58%)</td><td>113.10 (-13.99%)</td><td>32.67 <b>(-20.81%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>232.40 (n/a)</td><td>185.08 (n/a)</td><td>201.10 (n/a)</td><td>131.50 (n/a)</td><td>41.26 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.40 (-6.92%)</td><td>0.32 (+3.01%)</td><td>0.29 (-4.78%)</td><td>0.25 <b>(+31.04%)</b></td><td>0.07 <b>(-20.48%)</b></td><td>199.30 <b>(-23.70%)</b></td><td>160.42 (-6.19%)</td><td>169.50 (+5.02%)</td><td>122.60 (+7.45%)</td><td>33.29 <b>(-38.82%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>261.20 (n/a)</td><td>171.00 (n/a)</td><td>161.40 (n/a)</td><td>114.10 (n/a)</td><td>54.41 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.41 (+0.87%)</td><td>12.46 (-1.12%)</td><td>12.40 (-2.93%)</td><td>10.80 (-7.49%)</td><td>1.04 <b>(+39.99%)</b></td><td>970.50 (+8.10%)</td><td>846.66 (+1.45%)</td><td>845.80 (+3.02%)</td><td>781.90 (-0.86%)</td><td>75.76 <b>(+51.13%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.30 (n/a)</td><td>12.60 (n/a)</td><td>12.77 (n/a)</td><td>11.68 (n/a)</td><td>0.75 (n/a)</td><td>897.80 (n/a)</td><td>834.56 (n/a)</td><td>821.00 (n/a)</td><td>788.70 (n/a)</td><td>50.13 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.34 <b>(+23.21%)</b></td><td>0.25 (+1.00%)</td><td>0.24 (+1.47%)</td><td>0.19 (-17.26%)</td><td>0.06 <b>(+215.42%)</b></td><td>217.00 <b>(+20.89%)</b></td><td>173.94 (+3.65%)</td><td>170.40 (-1.45%)</td><td>118.90 (-18.84%)</td><td>42.03 <b>(+222.99%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>179.50 (n/a)</td><td>167.82 (n/a)</td><td>172.90 (n/a)</td><td>146.50 (n/a)</td><td>13.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+9.18%)</td><td>0.03 (-0.69%)</td><td>0.03 (-2.60%)</td><td>0.03 (-4.54%)</td><td>0.00 <b>(+43.96%)</b></td><td>195.80 (+4.76%)</td><td>168.98 (+1.54%)</td><td>167.10 (+2.70%)</td><td>133.70 (-8.36%)</td><td>23.51 <b>(+34.89%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.90 (n/a)</td><td>166.42 (n/a)</td><td>162.70 (n/a)</td><td>145.90 (n/a)</td><td>17.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 <b>(-21.49%)</b></td><td>0.03 (-9.10%)</td><td>0.03 (-6.30%)</td><td>0.02 (+2.31%)</td><td>0.00 <b>(-52.93%)</b></td><td>167.30 (-2.28%)</td><td>153.12 (+6.75%)</td><td>157.40 (+6.71%)</td><td>123.60 <b>(+27.42%)</b></td><td>17.31 <b>(-42.01%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>171.20 (n/a)</td><td>143.44 (n/a)</td><td>147.50 (n/a)</td><td>97.00 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (+12.77%)</td><td>0.04 (-1.06%)</td><td>0.04 (-4.63%)</td><td>0.03 (-9.74%)</td><td>0.01 <b>(+95.53%)</b></td><td>188.00 (+10.78%)</td><td>156.32 (+3.44%)</td><td>156.50 (+4.89%)</td><td>119.30 (-11.30%)</td><td>30.24 <b>(+95.40%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>169.70 (n/a)</td><td>151.12 (n/a)</td><td>149.20 (n/a)</td><td>134.50 (n/a)</td><td>15.48 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+8.83%)</td><td>0.03 (-10.04%)</td><td>0.02 <b>(-21.32%)</b></td><td>0.02 (-3.21%)</td><td>0.01 <b>(+48.48%)</b></td><td>195.60 (+3.27%)</td><td>169.02 (+13.10%)</td><td>182.20 <b>(+27.06%)</b></td><td>115.20 (-8.06%)</td><td>31.54 <b>(+31.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.40 (n/a)</td><td>149.44 (n/a)</td><td>143.40 (n/a)</td><td>125.30 (n/a)</td><td>23.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (-17.70%)</td><td>0.03 (-12.29%)</td><td>0.03 (-4.55%)</td><td>0.02 <b>(-25.02%)</b></td><td>0.01 (-5.25%)</td><td>238.50 <b>(+33.39%)</b></td><td>172.78 (+15.80%)</td><td>156.90 (+4.74%)</td><td>129.40 <b>(+21.50%)</b></td><td>43.65 <b>(+59.92%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>149.20 (n/a)</td><td>149.80 (n/a)</td><td>106.50 (n/a)</td><td>27.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+3.22%)</td><td>0.03 (+2.48%)</td><td>0.02 (-0.11%)</td><td>0.02 (-7.15%)</td><td>0.01 (+13.76%)</td><td>203.50 (+7.73%)</td><td>163.20 (-1.56%)</td><td>170.20 (+0.12%)</td><td>115.90 (-3.17%)</td><td>32.38 (+19.44%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>165.78 (n/a)</td><td>170.00 (n/a)</td><td>119.70 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-16.94%)</td><td>0.03 (-3.65%)</td><td>0.03 (+6.31%)</td><td>0.03 (+12.59%)</td><td>0.00 <b>(-70.52%)</b></td><td>180.30 (-11.18%)</td><td>163.68 (+0.24%)</td><td>158.40 (-5.88%)</td><td>151.60 <b>(+20.41%)</b></td><td>11.39 <b>(-67.54%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>163.28 (n/a)</td><td>168.30 (n/a)</td><td>125.90 (n/a)</td><td>35.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (+9.40%)</td><td>0.03 (-0.47%)</td><td>0.03 (+2.00%)</td><td>0.02 (-5.87%)</td><td>0.01 <b>(+54.68%)</b></td><td>194.60 (+6.22%)</td><td>160.70 (+2.24%)</td><td>156.70 (-1.94%)</td><td>117.50 (-8.63%)</td><td>30.15 <b>(+51.86%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.20 (n/a)</td><td>157.18 (n/a)</td><td>159.80 (n/a)</td><td>128.60 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (-1.12%)</td><td>0.03 (+3.56%)</td><td>0.03 <b>(+34.32%)</b></td><td>0.02 (-19.91%)</td><td>0.01 (+18.44%)</td><td>263.60 <b>(+24.87%)</b></td><td>173.52 (-0.30%)</td><td>140.00 <b>(-25.57%)</b></td><td>128.40 (+1.18%)</td><td>58.60 <b>(+45.99%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>174.04 (n/a)</td><td>188.10 (n/a)</td><td>126.90 (n/a)</td><td>40.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-0.53%)</td><td>0.03 (-12.18%)</td><td>0.02 <b>(-22.68%)</b></td><td>0.02 (+8.28%)</td><td>0.00 (-11.87%)</td><td>178.70 (-7.65%)</td><td>157.20 (+12.72%)</td><td>164.70 <b>(+29.28%)</b></td><td>118.00 (+0.60%)</td><td>23.29 <b>(-24.14%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>139.46 (n/a)</td><td>127.40 (n/a)</td><td>117.30 (n/a)</td><td>30.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+6.45%)</td><td>0.03 (-10.00%)</td><td>0.02 (-13.66%)</td><td>0.02 (-7.05%)</td><td>0.01 (+14.98%)</td><td>219.20 (+7.61%)</td><td>185.60 (+12.38%)</td><td>198.10 (+15.78%)</td><td>122.90 (-6.04%)</td><td>38.83 (+18.15%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>165.16 (n/a)</td><td>171.10 (n/a)</td><td>130.80 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (+11.70%)</td><td>0.02 (-5.45%)</td><td>0.02 (-15.73%)</td><td>0.02 (+3.10%)</td><td>0.01 <b>(+35.69%)</b></td><td>213.90 (-2.99%)</td><td>181.12 (+7.59%)</td><td>190.90 (+18.65%)</td><td>117.00 (-10.48%)</td><td>39.30 (+14.50%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>168.34 (n/a)</td><td>160.90 (n/a)</td><td>130.70 (n/a)</td><td>34.32 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-1.12%)</td><td>0.02 (-9.02%)</td><td>0.02 (-18.42%)</td><td>0.02 (-5.66%)</td><td>0.00 <b>(+23.92%)</b></td><td>227.30 (+6.02%)</td><td>196.82 (+10.72%)</td><td>205.30 <b>(+22.64%)</b></td><td>160.20 (+1.14%)</td><td>29.43 <b>(+31.25%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.40 (n/a)</td><td>177.76 (n/a)</td><td>167.40 (n/a)</td><td>158.40 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-12.18%)</td><td>0.02 (+0.99%)</td><td>0.02 (-1.39%)</td><td>0.02 (-1.15%)</td><td>0.00 (-13.71%)</td><td>211.60 (+1.15%)</td><td>180.32 (-1.42%)</td><td>192.20 (+1.42%)</td><td>142.60 (+13.90%)</td><td>34.26 (+0.73%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>182.92 (n/a)</td><td>189.50 (n/a)</td><td>125.20 (n/a)</td><td>34.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (-18.58%)</td><td>0.02 (-13.92%)</td><td>0.02 (-0.98%)</td><td>0.01 <b>(-28.67%)</b></td><td>0.00 (-4.09%)</td><td>332.60 <b>(+40.16%)</b></td><td>228.96 (+18.03%)</td><td>205.10 (+0.98%)</td><td>196.60 <b>(+22.80%)</b></td><td>58.07 <b>(+75.97%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.30 (n/a)</td><td>193.98 (n/a)</td><td>203.10 (n/a)</td><td>160.10 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (-12.44%)</td><td>0.02 (-2.32%)</td><td>0.02 (-3.09%)</td><td>0.02 (+3.01%)</td><td>0.00 <b>(-53.33%)</b></td><td>233.70 (-2.91%)</td><td>219.88 (+1.38%)</td><td>226.50 (+3.19%)</td><td>199.80 (+14.24%)</td><td>13.67 <b>(-48.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.70 (n/a)</td><td>216.88 (n/a)</td><td>219.50 (n/a)</td><td>174.90 (n/a)</td><td>26.35 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (-8.83%)</td><td>0.05 (-13.55%)</td><td>0.04 (-15.17%)</td><td>0.04 (-16.31%)</td><td>0.01 (-4.12%)</td><td>231.90 (+19.54%)</td><td>183.92 (+16.30%)</td><td>192.30 (+17.90%)</td><td>127.60 (+9.72%)</td><td>38.03 <b>(+22.22%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>158.14 (n/a)</td><td>163.10 (n/a)</td><td>116.30 (n/a)</td><td>31.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 <b>(-22.85%)</b></td><td>0.07 (-14.18%)</td><td>0.06 <b>(-20.86%)</b></td><td>0.06 (+8.58%)</td><td>0.01 <b>(-52.75%)</b></td><td>196.90 (-7.90%)</td><td>178.10 (+13.47%)</td><td>189.10 <b>(+26.40%)</b></td><td>153.80 <b>(+29.57%)</b></td><td>19.20 <b>(-45.25%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.80 (n/a)</td><td>156.96 (n/a)</td><td>149.60 (n/a)</td><td>118.70 (n/a)</td><td>35.07 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (-12.53%)</td><td>0.05 (-11.59%)</td><td>0.05 (-3.14%)</td><td>0.04 (-0.52%)</td><td>0.01 <b>(-34.07%)</b></td><td>222.40 (+0.54%)</td><td>185.20 (+10.57%)</td><td>181.80 (+3.24%)</td><td>140.90 (+14.27%)</td><td>31.24 <b>(-22.36%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.20 (n/a)</td><td>167.50 (n/a)</td><td>176.10 (n/a)</td><td>123.30 (n/a)</td><td>40.23 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 <b>(+25.40%)</b></td><td>0.06 (+12.46%)</td><td>0.06 (-0.43%)</td><td>0.05 <b>(+44.31%)</b></td><td>0.01 (+0.54%)</td><td>194.80 <b>(-30.68%)</b></td><td>168.28 (-13.11%)</td><td>171.60 (+0.41%)</td><td>121.00 <b>(-20.29%)</b></td><td>28.35 <b>(-46.62%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>281.00 (n/a)</td><td>193.66 (n/a)</td><td>170.90 (n/a)</td><td>151.80 (n/a)</td><td>53.10 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (+10.20%)</td><td>0.05 (+3.32%)</td><td>0.06 (+17.65%)</td><td>0.03 (-15.25%)</td><td>0.01 <b>(+52.51%)</b></td><td>280.00 (+17.99%)</td><td>178.74 (+1.25%)</td><td>147.10 (-15.02%)</td><td>128.60 (-9.24%)</td><td>61.25 <b>(+64.83%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>176.54 (n/a)</td><td>173.10 (n/a)</td><td>141.70 (n/a)</td><td>37.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (-5.96%)</td><td>0.06 (-7.63%)</td><td>0.06 (-15.27%)</td><td>0.05 <b>(+27.63%)</b></td><td>0.01 <b>(-32.99%)</b></td><td>204.80 <b>(-21.62%)</b></td><td>172.60 (+3.99%)</td><td>176.10 (+18.03%)</td><td>138.80 (+6.36%)</td><td>29.23 <b>(-46.15%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>261.30 (n/a)</td><td>165.98 (n/a)</td><td>149.20 (n/a)</td><td>130.50 (n/a)</td><td>54.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (+3.74%)</td><td>0.05 (-4.25%)</td><td>0.05 (-4.07%)</td><td>0.04 (-7.66%)</td><td>0.01 (+11.00%)</td><td>198.90 (+8.33%)</td><td>160.34 (+5.02%)</td><td>154.40 (+4.25%)</td><td>125.10 (-3.62%)</td><td>27.65 (+17.44%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>152.68 (n/a)</td><td>148.10 (n/a)</td><td>129.80 (n/a)</td><td>23.54 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (-7.17%)</td><td>0.05 (-11.10%)</td><td>0.05 (-13.37%)</td><td>0.04 (+7.55%)</td><td>0.01 <b>(-24.39%)</b></td><td>207.30 (-7.04%)</td><td>180.14 (+10.64%)</td><td>181.40 (+15.47%)</td><td>136.40 (+7.74%)</td><td>27.74 <b>(-26.21%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>162.82 (n/a)</td><td>157.10 (n/a)</td><td>126.60 (n/a)</td><td>37.59 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (-14.61%)</td><td>0.05 (+0.62%)</td><td>0.05 (-14.58%)</td><td>0.05 <b>(+97.37%)</b></td><td>0.00 <b>(-82.26%)</b></td><td>181.40 <b>(-49.32%)</b></td><td>166.40 (-13.54%)</td><td>166.00 (+17.07%)</td><td>153.00 (+17.06%)</td><td>10.11 <b>(-89.48%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>357.90 (n/a)</td><td>192.46 (n/a)</td><td>141.80 (n/a)</td><td>130.70 (n/a)</td><td>96.07 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (+11.75%)</td><td>0.05 (-3.93%)</td><td>0.05 (-19.27%)</td><td>0.03 (-8.23%)</td><td>0.02 (+7.39%)</td><td>280.50 (+8.97%)</td><td>190.02 (+4.69%)</td><td>181.40 <b>(+23.91%)</b></td><td>119.30 (-10.50%)</td><td>59.97 (+4.89%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>257.40 (n/a)</td><td>181.50 (n/a)</td><td>146.40 (n/a)</td><td>133.30 (n/a)</td><td>57.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (-11.27%)</td><td>0.05 (-6.75%)</td><td>0.05 (-8.55%)</td><td>0.04 (+0.56%)</td><td>0.01 <b>(-26.63%)</b></td><td>223.70 (-0.58%)</td><td>175.38 (+5.98%)</td><td>169.90 (+9.33%)</td><td>153.70 (+12.77%)</td><td>27.95 (-19.13%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>165.48 (n/a)</td><td>155.40 (n/a)</td><td>136.30 (n/a)</td><td>34.56 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (-11.34%)</td><td>0.04 (-13.89%)</td><td>0.04 <b>(-20.98%)</b></td><td>0.04 (-14.11%)</td><td>0.01 (-11.85%)</td><td>232.90 (+16.45%)</td><td>197.62 (+16.12%)</td><td>203.30 <b>(+26.51%)</b></td><td>163.60 (+12.83%)</td><td>28.05 (+13.16%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>170.18 (n/a)</td><td>160.70 (n/a)</td><td>145.00 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (-0.95%)</td><td>0.06 (+13.76%)</td><td>0.06 <b>(+32.84%)</b></td><td>0.04 (+0.99%)</td><td>0.01 (-14.49%)</td><td>196.40 (-0.96%)</td><td>149.00 (-12.90%)</td><td>144.60 <b>(-24.69%)</b></td><td>126.50 (+1.04%)</td><td>28.16 (-15.27%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>171.06 (n/a)</td><td>192.00 (n/a)</td><td>125.20 (n/a)</td><td>33.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (+15.55%)</td><td>0.04 (-6.60%)</td><td>0.04 (+1.22%)</td><td>0.03 <b>(-33.81%)</b></td><td>0.02 <b>(+66.59%)</b></td><td>341.70 <b>(+51.06%)</b></td><td>218.62 (+14.52%)</td><td>202.30 (-1.22%)</td><td>129.90 (-13.46%)</td><td>77.40 <b>(+122.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>190.90 (n/a)</td><td>204.80 (n/a)</td><td>150.10 (n/a)</td><td>34.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (+14.17%)</td><td>0.04 (+4.61%)</td><td>0.04 (+3.70%)</td><td>0.03 (-5.80%)</td><td>0.01 <b>(+42.26%)</b></td><td>242.70 (+6.17%)</td><td>191.78 (-3.23%)</td><td>189.00 (-3.57%)</td><td>151.00 (-12.41%)</td><td>34.86 <b>(+34.02%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.60 (n/a)</td><td>198.18 (n/a)</td><td>196.00 (n/a)</td><td>172.40 (n/a)</td><td>26.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (-9.18%)</td><td>0.10 (-4.82%)</td><td>0.10 (-6.48%)</td><td>0.09 (+7.62%)</td><td>0.01 <b>(-46.33%)</b></td><td>175.40 (-7.10%)</td><td>163.18 (+2.89%)</td><td>172.20 (+6.96%)</td><td>137.40 (+10.10%)</td><td>16.49 <b>(-45.16%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.80 (n/a)</td><td>158.60 (n/a)</td><td>161.00 (n/a)</td><td>124.80 (n/a)</td><td>30.07 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (-1.23%)</td><td>0.14 (-5.72%)</td><td>0.13 (-3.55%)</td><td>0.10 <b>(-21.25%)</b></td><td>0.04 <b>(+41.98%)</b></td><td>244.90 <b>(+26.96%)</b></td><td>182.66 (+9.56%)</td><td>188.50 (+3.69%)</td><td>134.00 (+1.21%)</td><td>47.53 <b>(+74.73%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.90 (n/a)</td><td>166.72 (n/a)</td><td>181.80 (n/a)</td><td>132.40 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (-5.29%)</td><td>0.10 (-7.90%)</td><td>0.11 (-6.20%)</td><td>0.08 (-0.77%)</td><td>0.02 (-16.36%)</td><td>204.10 (+0.79%)</td><td>166.98 (+7.69%)</td><td>153.40 (+6.60%)</td><td>130.10 (+5.60%)</td><td>31.02 (-8.30%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.50 (n/a)</td><td>155.06 (n/a)</td><td>143.90 (n/a)</td><td>123.20 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (-3.46%)</td><td>0.12 (-5.41%)</td><td>0.13 (+10.71%)</td><td>0.08 (-19.66%)</td><td>0.03 <b>(+34.96%)</b></td><td>251.20 <b>(+24.48%)</b></td><td>180.70 (+9.22%)</td><td>155.50 (-9.65%)</td><td>131.70 (+3.54%)</td><td>49.55 <b>(+79.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>201.80 (n/a)</td><td>165.44 (n/a)</td><td>172.10 (n/a)</td><td>127.20 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (+18.42%)</td><td>0.09 (+19.03%)</td><td>0.11 <b>(+49.06%)</b></td><td>0.06 (-17.50%)</td><td>0.03 <b>(+88.34%)</b></td><td>297.10 <b>(+21.22%)</b></td><td>195.16 (-10.39%)</td><td>154.70 <b>(-32.91%)</b></td><td>133.90 (-15.57%)</td><td>69.02 <b>(+100.07%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>245.10 (n/a)</td><td>217.80 (n/a)</td><td>230.60 (n/a)</td><td>158.60 (n/a)</td><td>34.50 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (-4.67%)</td><td>0.12 (+2.50%)</td><td>0.12 (+4.48%)</td><td>0.10 (+14.68%)</td><td>0.02 (-19.58%)</td><td>214.20 (-12.82%)</td><td>176.26 (-3.98%)</td><td>169.80 (-4.28%)</td><td>141.70 (+4.89%)</td><td>30.95 <b>(-26.16%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>245.70 (n/a)</td><td>183.56 (n/a)</td><td>177.40 (n/a)</td><td>135.10 (n/a)</td><td>41.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 <b>(+20.01%)</b></td><td>0.12 <b>(+23.13%)</b></td><td>0.12 <b>(+29.65%)</b></td><td>0.08 (+8.04%)</td><td>0.03 <b>(+34.45%)</b></td><td>193.20 (-7.43%)</td><td>143.22 (-17.81%)</td><td>138.50 <b>(-22.84%)</b></td><td>106.70 (-16.64%)</td><td>33.00 (+6.26%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.70 (n/a)</td><td>174.26 (n/a)</td><td>179.50 (n/a)</td><td>128.00 (n/a)</td><td>31.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 <b>(+23.28%)</b></td><td>0.11 (+4.15%)</td><td>0.11 (-1.18%)</td><td>0.07 (-18.88%)</td><td>0.03 <b>(+96.95%)</b></td><td>262.40 <b>(+23.25%)</b></td><td>180.32 (+0.42%)</td><td>168.70 (+1.20%)</td><td>127.80 (-18.86%)</td><td>52.34 <b>(+100.73%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>179.56 (n/a)</td><td>166.70 (n/a)</td><td>157.50 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 <b>(+33.65%)</b></td><td>0.11 <b>(+21.12%)</b></td><td>0.11 (+16.36%)</td><td>0.08 (-0.33%)</td><td>0.02 <b>(+149.49%)</b></td><td>196.60 (+0.36%)</td><td>150.86 (-15.79%)</td><td>148.30 (-14.08%)</td><td>122.20 <b>(-25.17%)</b></td><td>28.23 <b>(+88.15%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>179.14 (n/a)</td><td>172.60 (n/a)</td><td>163.30 (n/a)</td><td>15.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 <b>(+76.04%)</b></td><td>0.13 <b>(+31.93%)</b></td><td>0.11 (+4.90%)</td><td>0.11 <b>(+24.79%)</b></td><td>0.04 <b>(+325.61%)</b></td><td>167.30 (-19.88%)</td><td>143.86 <b>(-20.77%)</b></td><td>165.30 (-4.67%)</td><td>95.00 <b>(-43.18%)</b></td><td>32.66 <b>(+97.46%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>181.58 (n/a)</td><td>173.40 (n/a)</td><td>167.20 (n/a)</td><td>16.54 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (+13.15%)</td><td>0.10 <b>(+26.57%)</b></td><td>0.10 <b>(+21.76%)</b></td><td>0.09 <b>(+51.41%)</b></td><td>0.01 <b>(-52.40%)</b></td><td>191.40 <b>(-33.95%)</b></td><td>168.14 <b>(-24.79%)</b></td><td>162.10 (-17.88%)</td><td>150.30 (-11.59%)</td><td>16.63 <b>(-72.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>289.80 (n/a)</td><td>223.56 (n/a)</td><td>197.40 (n/a)</td><td>170.00 (n/a)</td><td>60.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (-13.04%)</td><td>0.09 (-4.46%)</td><td>0.09 (+7.13%)</td><td>0.07 (-9.04%)</td><td>0.02 (-19.51%)</td><td>251.90 (+9.95%)</td><td>195.86 (+3.86%)</td><td>185.40 (-6.69%)</td><td>152.20 (+14.95%)</td><td>41.39 (+1.41%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>229.10 (n/a)</td><td>188.58 (n/a)</td><td>198.70 (n/a)</td><td>132.40 (n/a)</td><td>40.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 <b>(+23.37%)</b></td><td>0.11 <b>(+30.33%)</b></td><td>0.10 <b>(+31.86%)</b></td><td>0.08 <b>(+32.66%)</b></td><td>0.03 (+5.26%)</td><td>217.60 <b>(-24.63%)</b></td><td>161.74 <b>(-25.23%)</b></td><td>156.30 <b>(-24.16%)</b></td><td>109.30 (-18.92%)</td><td>39.18 <b>(-38.04%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>288.70 (n/a)</td><td>216.32 (n/a)</td><td>206.10 (n/a)</td><td>134.80 (n/a)</td><td>63.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 <b>(+29.23%)</b></td><td>0.11 (+18.59%)</td><td>0.10 <b>(+22.09%)</b></td><td>0.08 (-1.61%)</td><td>0.04 <b>(+60.37%)</b></td><td>226.00 (+1.66%)</td><td>170.26 (-12.65%)</td><td>172.60 (-18.12%)</td><td>100.70 <b>(-22.60%)</b></td><td>46.32 <b>(+24.36%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>194.92 (n/a)</td><td>210.80 (n/a)</td><td>130.10 (n/a)</td><td>37.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 <b>(+22.76%)</b></td><td>0.08 <b>(+26.61%)</b></td><td>0.09 <b>(+28.01%)</b></td><td>0.07 <b>(+47.89%)</b></td><td>0.01 (+2.80%)</td><td>232.80 <b>(-32.38%)</b></td><td>200.04 <b>(-21.91%)</b></td><td>183.70 <b>(-21.90%)</b></td><td>176.60 (-18.54%)</td><td>28.24 <b>(-44.78%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>344.30 (n/a)</td><td>256.16 (n/a)</td><td>235.20 (n/a)</td><td>216.80 (n/a)</td><td>51.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (+15.62%)</td><td>0.22 (+9.68%)</td><td>0.19 (-5.19%)</td><td>0.17 (+4.77%)</td><td>0.05 <b>(+62.96%)</b></td><td>197.80 (-4.54%)</td><td>158.50 (-6.46%)</td><td>170.30 (+5.45%)</td><td>115.60 (-13.47%)</td><td>37.31 <b>(+31.36%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>207.20 (n/a)</td><td>169.44 (n/a)</td><td>161.50 (n/a)</td><td>133.60 (n/a)</td><td>28.40 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.23 (+6.30%)</td><td>0.17 (-13.70%)</td><td>0.16 (-19.56%)</td><td>0.11 <b>(-33.90%)</b></td><td>0.04 <b>(+100.61%)</b></td><td>309.80 <b>(+51.27%)</b></td><td>209.90 <b>(+21.78%)</b></td><td>204.20 <b>(+24.28%)</b></td><td>144.80 (-5.97%)</td><td>61.26 <b>(+193.76%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.80 (n/a)</td><td>172.36 (n/a)</td><td>164.30 (n/a)</td><td>154.00 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.38 (+10.58%)</td><td>0.29 (+15.84%)</td><td>0.31 <b>(+32.02%)</b></td><td>0.19 (-11.54%)</td><td>0.07 <b>(+36.21%)</b></td><td>213.60 (+13.08%)</td><td>147.66 (-11.33%)</td><td>133.60 <b>(-24.26%)</b></td><td>107.20 (-9.54%)</td><td>41.55 <b>(+44.20%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>188.90 (n/a)</td><td>166.52 (n/a)</td><td>176.40 (n/a)</td><td>118.50 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.23 (+1.75%)</td><td>0.21 (+2.91%)</td><td>0.21 (-4.55%)</td><td>0.18 (+12.44%)</td><td>0.02 <b>(-27.89%)</b></td><td>181.60 (-11.07%)</td><td>157.94 (-3.68%)</td><td>158.80 (+4.75%)</td><td>140.40 (-1.75%)</td><td>15.43 <b>(-37.36%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>204.20 (n/a)</td><td>163.98 (n/a)</td><td>151.60 (n/a)</td><td>142.90 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.33 (-4.11%)</td><td>0.26 (-9.13%)</td><td>0.25 (-7.29%)</td><td>0.18 <b>(-25.23%)</b></td><td>0.06 <b>(+34.74%)</b></td><td>233.50 <b>(+33.73%)</b></td><td>167.86 (+13.22%)</td><td>164.50 (+7.87%)</td><td>124.20 (+4.28%)</td><td>42.44 <b>(+89.59%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>174.60 (n/a)</td><td>148.26 (n/a)</td><td>152.50 (n/a)</td><td>119.10 (n/a)</td><td>22.38 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 <b>(+35.21%)</b></td><td>0.24 <b>(+25.07%)</b></td><td>0.22 (+12.94%)</td><td>0.20 <b>(+23.37%)</b></td><td>0.04 <b>(+118.59%)</b></td><td>160.40 (-18.91%)</td><td>141.18 (-19.13%)</td><td>152.30 (-11.50%)</td><td>115.30 <b>(-26.04%)</b></td><td>20.16 <b>(+30.27%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>197.80 (n/a)</td><td>174.58 (n/a)</td><td>172.10 (n/a)</td><td>155.90 (n/a)</td><td>15.48 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (+9.46%)</td><td>0.21 (-2.92%)</td><td>0.22 (-6.49%)</td><td>0.15 (-15.66%)</td><td>0.05 <b>(+47.51%)</b></td><td>243.90 (+18.51%)</td><td>180.56 (+5.54%)</td><td>168.00 (+6.94%)</td><td>131.30 (-8.69%)</td><td>42.96 <b>(+59.33%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>205.80 (n/a)</td><td>171.08 (n/a)</td><td>157.10 (n/a)</td><td>143.80 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (-8.54%)</td><td>0.21 (+5.61%)</td><td>0.22 (+7.47%)</td><td>0.15 <b>(+32.50%)</b></td><td>0.04 <b>(-42.93%)</b></td><td>212.80 <b>(-24.54%)</b></td><td>159.30 (-11.54%)</td><td>152.20 (-6.97%)</td><td>128.50 (+9.27%)</td><td>31.95 <b>(-51.38%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>282.00 (n/a)</td><td>180.08 (n/a)</td><td>163.60 (n/a)</td><td>117.60 (n/a)</td><td>65.72 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (-2.86%)</td><td>0.27 (+16.02%)</td><td>0.29 <b>(+22.80%)</b></td><td>0.21 <b>(+33.72%)</b></td><td>0.04 <b>(-44.56%)</b></td><td>176.50 <b>(-25.21%)</b></td><td>138.18 (-18.82%)</td><td>128.10 (-18.51%)</td><td>117.20 (+2.90%)</td><td>23.09 <b>(-56.99%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>236.00 (n/a)</td><td>170.22 (n/a)</td><td>157.20 (n/a)</td><td>113.90 (n/a)</td><td>53.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 <b>(-20.51%)</b></td><td>0.19 (-9.57%)</td><td>0.19 (-9.64%)</td><td>0.17 (+6.06%)</td><td>0.01 <b>(-62.56%)</b></td><td>195.80 (-5.73%)</td><td>175.80 (+8.25%)</td><td>171.10 (+10.67%)</td><td>161.40 <b>(+25.80%)</b></td><td>13.15 <b>(-55.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.70 (n/a)</td><td>162.40 (n/a)</td><td>154.60 (n/a)</td><td>128.30 (n/a)</td><td>29.77 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (-11.72%)</td><td>0.19 (-6.12%)</td><td>0.20 (+0.50%)</td><td>0.15 (-15.97%)</td><td>0.03 (+5.67%)</td><td>225.30 (+19.02%)</td><td>183.68 (+7.10%)</td><td>172.80 (-0.52%)</td><td>160.00 (+13.31%)</td><td>27.95 <b>(+40.05%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>189.30 (n/a)</td><td>171.50 (n/a)</td><td>173.70 (n/a)</td><td>141.20 (n/a)</td><td>19.96 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (-10.00%)</td><td>0.19 (-8.34%)</td><td>0.20 (-1.34%)</td><td>0.15 (-15.89%)</td><td>0.03 <b>(+22.33%)</b></td><td>216.20 (+18.92%)</td><td>178.22 (+10.27%)</td><td>160.50 (+1.39%)</td><td>150.70 (+11.05%)</td><td>30.05 <b>(+62.06%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>181.80 (n/a)</td><td>161.62 (n/a)</td><td>158.30 (n/a)</td><td>135.70 (n/a)</td><td>18.54 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (-5.18%)</td><td>0.20 (+1.59%)</td><td>0.20 (-6.94%)</td><td>0.18 <b>(+27.23%)</b></td><td>0.01 <b>(-58.89%)</b></td><td>196.90 <b>(-21.40%)</b></td><td>174.52 (-4.31%)</td><td>172.60 (+7.47%)</td><td>161.90 (+5.40%)</td><td>13.78 <b>(-65.91%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>250.50 (n/a)</td><td>182.38 (n/a)</td><td>160.60 (n/a)</td><td>153.60 (n/a)</td><td>40.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (-1.26%)</td><td>0.16 (+4.55%)</td><td>0.16 (+7.07%)</td><td>0.14 (+8.36%)</td><td>0.02 <b>(-23.79%)</b></td><td>233.60 (-7.70%)</td><td>206.12 (-4.97%)</td><td>201.50 (-6.63%)</td><td>178.50 (+1.31%)</td><td>20.49 <b>(-28.16%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>253.10 (n/a)</td><td>216.90 (n/a)</td><td>215.80 (n/a)</td><td>176.20 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (+14.05%)</td><td>0.14 (+6.60%)</td><td>0.14 (+10.34%)</td><td>0.10 (-4.91%)</td><td>0.03 <b>(+65.01%)</b></td><td>198.60 (+5.19%)</td><td>156.96 (-3.82%)</td><td>148.40 (-9.40%)</td><td>121.40 (-12.28%)</td><td>35.88 <b>(+54.01%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>188.80 (n/a)</td><td>163.20 (n/a)</td><td>163.80 (n/a)</td><td>138.40 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (+13.22%)</td><td>0.13 (+4.13%)</td><td>0.11 (-6.54%)</td><td>0.10 (+1.43%)</td><td>0.03 <b>(+54.61%)</b></td><td>204.10 (-1.40%)</td><td>169.90 (-2.00%)</td><td>183.80 (+6.98%)</td><td>130.10 (-11.68%)</td><td>36.17 <b>(+35.11%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>207.00 (n/a)</td><td>173.36 (n/a)</td><td>171.80 (n/a)</td><td>147.30 (n/a)</td><td>26.77 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (+10.38%)</td><td>0.12 (-10.28%)</td><td>0.10 <b>(-31.33%)</b></td><td>0.09 (-1.24%)</td><td>0.04 <b>(+43.93%)</b></td><td>228.10 (+1.24%)</td><td>178.00 (+14.99%)</td><td>203.90 <b>(+45.64%)</b></td><td>117.10 (-9.37%)</td><td>49.67 <b>(+25.18%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>225.30 (n/a)</td><td>154.80 (n/a)</td><td>140.00 (n/a)</td><td>129.20 (n/a)</td><td>39.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 <b>(-24.12%)</b></td><td>0.11 (-13.63%)</td><td>0.11 (-8.66%)</td><td>0.09 (-12.11%)</td><td>0.01 <b>(-40.32%)</b></td><td>225.90 (+13.80%)</td><td>192.84 (+14.45%)</td><td>186.70 (+9.50%)</td><td>169.40 <b>(+31.73%)</b></td><td>25.13 (-11.87%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>198.50 (n/a)</td><td>168.50 (n/a)</td><td>170.50 (n/a)</td><td>128.60 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 <b>(-37.60%)</b></td><td>0.12 <b>(-21.87%)</b></td><td>0.12 (-6.08%)</td><td>0.08 <b>(-33.86%)</b></td><td>0.02 <b>(-45.79%)</b></td><td>249.70 <b>(+51.15%)</b></td><td>182.16 <b>(+26.64%)</b></td><td>164.90 (+6.46%)</td><td>154.20 <b>(+60.29%)</b></td><td>39.01 <b>(+35.93%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>165.20 (n/a)</td><td>143.84 (n/a)</td><td>154.90 (n/a)</td><td>96.20 (n/a)</td><td>28.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (-3.31%)</td><td>0.12 (-2.28%)</td><td>0.11 (-12.11%)</td><td>0.11 <b>(+27.23%)</b></td><td>0.02 <b>(-27.03%)</b></td><td>189.60 <b>(-21.43%)</b></td><td>171.42 (-0.50%)</td><td>178.70 (+13.82%)</td><td>127.60 (+3.40%)</td><td>25.47 <b>(-42.77%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>241.30 (n/a)</td><td>172.28 (n/a)</td><td>157.00 (n/a)</td><td>123.40 (n/a)</td><td>44.50 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 <b>(-36.73%)</b></td><td>0.10 (-18.93%)</td><td>0.10 (-14.47%)</td><td>0.09 (+0.42%)</td><td>0.01 <b>(-74.30%)</b></td><td>231.50 (-0.43%)</td><td>211.72 (+18.28%)</td><td>209.00 (+16.89%)</td><td>189.10 <b>(+58.11%)</b></td><td>17.18 <b>(-57.95%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>232.50 (n/a)</td><td>179.00 (n/a)</td><td>178.80 (n/a)</td><td>119.60 (n/a)</td><td>40.87 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 <b>(-22.49%)</b></td><td>0.10 <b>(-26.42%)</b></td><td>0.10 <b>(-28.90%)</b></td><td>0.08 <b>(-25.28%)</b></td><td>0.02 <b>(-25.41%)</b></td><td>270.90 <b>(+33.84%)</b></td><td>221.58 <b>(+35.52%)</b></td><td>213.90 <b>(+40.63%)</b></td><td>161.30 <b>(+29.04%)</b></td><td>41.59 <b>(+23.33%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>202.40 (n/a)</td><td>163.50 (n/a)</td><td>152.10 (n/a)</td><td>125.00 (n/a)</td><td>33.72 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (-0.68%)</td><td>0.17 (+15.62%)</td><td>0.19 <b>(+33.42%)</b></td><td>0.12 (-4.10%)</td><td>0.04 (+4.24%)</td><td>213.60 (+4.30%)</td><td>149.30 (-12.85%)</td><td>129.50 <b>(-25.06%)</b></td><td>117.90 (+0.68%)</td><td>38.73 (+15.78%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>204.80 (n/a)</td><td>171.32 (n/a)</td><td>172.80 (n/a)</td><td>117.10 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (+5.40%)</td><td>0.14 (-8.33%)</td><td>0.14 (-8.86%)</td><td>0.09 <b>(-32.62%)</b></td><td>0.04 <b>(+79.68%)</b></td><td>288.20 <b>(+48.40%)</b></td><td>186.48 (+15.73%)</td><td>175.70 (+9.74%)</td><td>123.70 (-5.14%)</td><td>61.76 <b>(+162.58%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>194.20 (n/a)</td><td>161.14 (n/a)</td><td>160.10 (n/a)</td><td>130.40 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (-2.04%)</td><td>0.15 (-9.17%)</td><td>0.14 (-16.05%)</td><td>0.11 (-13.94%)</td><td>0.03 (+18.30%)</td><td>214.50 (+16.20%)</td><td>169.84 (+11.21%)</td><td>170.70 (+19.12%)</td><td>137.00 (+2.09%)</td><td>31.10 <b>(+40.32%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>184.60 (n/a)</td><td>152.72 (n/a)</td><td>143.30 (n/a)</td><td>134.20 (n/a)</td><td>22.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (-15.20%)</td><td>0.13 (-14.20%)</td><td>0.13 (-6.48%)</td><td>0.10 <b>(-26.43%)</b></td><td>0.02 (+1.97%)</td><td>254.10 <b>(+35.96%)</b></td><td>197.64 (+17.57%)</td><td>189.40 (+6.88%)</td><td>162.90 (+17.96%)</td><td>34.22 <b>(+68.06%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>168.10 (n/a)</td><td>177.20 (n/a)</td><td>138.10 (n/a)</td><td>20.36 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 <b>(-31.80%)</b></td><td>0.12 (-19.85%)</td><td>0.12 (-13.98%)</td><td>0.11 (-18.06%)</td><td>0.01 <b>(-69.26%)</b></td><td>215.40 <b>(+22.04%)</b></td><td>199.22 <b>(+23.42%)</b></td><td>198.30 (+16.24%)</td><td>188.90 <b>(+46.66%)</b></td><td>10.75 <b>(-44.32%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>176.50 (n/a)</td><td>161.42 (n/a)</td><td>170.60 (n/a)</td><td>128.80 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (-4.99%)</td><td>0.12 <b>(-22.87%)</b></td><td>0.11 <b>(-30.09%)</b></td><td>0.11 <b>(-26.45%)</b></td><td>0.02 <b>(+111.14%)</b></td><td>233.30 <b>(+36.03%)</b></td><td>204.92 <b>(+32.07%)</b></td><td>214.70 <b>(+43.04%)</b></td><td>152.80 (+5.23%)</td><td>31.09 <b>(+192.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>171.50 (n/a)</td><td>155.16 (n/a)</td><td>150.10 (n/a)</td><td>145.20 (n/a)</td><td>10.62 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (+14.56%)</td><td>0.13 (-3.06%)</td><td>0.13 (-10.83%)</td><td>0.10 (-17.80%)</td><td>0.03 <b>(+71.85%)</b></td><td>256.50 <b>(+21.68%)</b></td><td>196.30 (+5.53%)</td><td>194.30 (+12.12%)</td><td>143.10 (-12.69%)</td><td>40.46 <b>(+77.08%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>210.80 (n/a)</td><td>186.02 (n/a)</td><td>173.30 (n/a)</td><td>163.90 (n/a)</td><td>22.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (+9.48%)</td><td>0.12 (+3.21%)</td><td>0.12 (+2.63%)</td><td>0.10 (+0.90%)</td><td>0.01 <b>(+35.31%)</b></td><td>234.20 (-0.89%)</td><td>203.90 (-2.80%)</td><td>202.10 (-2.56%)</td><td>177.80 (-8.68%)</td><td>20.74 <b>(+23.19%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>209.78 (n/a)</td><td>207.40 (n/a)</td><td>194.70 (n/a)</td><td>16.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 <b>(+28.39%)</b></td><td>0.12 (+5.49%)</td><td>0.12 (+1.68%)</td><td>0.09 (-5.95%)</td><td>0.02 <b>(+125.83%)</b></td><td>212.00 (+6.32%)</td><td>162.46 (-2.57%)</td><td>156.80 (-1.63%)</td><td>120.70 <b>(-22.13%)</b></td><td>34.78 <b>(+86.18%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>166.74 (n/a)</td><td>159.40 (n/a)</td><td>155.00 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (-3.86%)</td><td>0.11 (-8.80%)</td><td>0.11 (-6.10%)</td><td>0.08 <b>(-22.89%)</b></td><td>0.02 (+17.66%)</td><td>235.70 <b>(+29.65%)</b></td><td>170.84 (+11.79%)</td><td>167.70 (+6.54%)</td><td>127.60 (+4.08%)</td><td>40.61 <b>(+62.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>181.80 (n/a)</td><td>152.82 (n/a)</td><td>157.40 (n/a)</td><td>122.60 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (+10.39%)</td><td>0.11 (+7.74%)</td><td>0.11 (+3.22%)</td><td>0.09 <b>(+29.03%)</b></td><td>0.02 (-19.56%)</td><td>196.10 <b>(-22.49%)</b></td><td>170.84 (-9.31%)</td><td>173.70 (-3.12%)</td><td>130.80 (-9.42%)</td><td>24.76 <b>(-44.52%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>253.00 (n/a)</td><td>188.38 (n/a)</td><td>179.30 (n/a)</td><td>144.40 (n/a)</td><td>44.62 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (-16.99%)</td><td>0.10 (-11.43%)</td><td>0.10 (-13.06%)</td><td>0.08 (+14.14%)</td><td>0.01 <b>(-42.50%)</b></td><td>220.70 (-12.39%)</td><td>191.24 (+9.38%)</td><td>191.60 (+15.01%)</td><td>155.00 <b>(+20.44%)</b></td><td>27.49 <b>(-40.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>251.90 (n/a)</td><td>174.84 (n/a)</td><td>166.60 (n/a)</td><td>128.70 (n/a)</td><td>46.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (+0.53%)</td><td>0.11 (-8.84%)</td><td>0.10 (-17.72%)</td><td>0.08 (-5.86%)</td><td>0.02 (+1.76%)</td><td>224.40 (+6.20%)</td><td>178.34 (+9.91%)</td><td>184.40 <b>(+21.56%)</b></td><td>135.30 (-0.51%)</td><td>32.73 (+6.43%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>211.30 (n/a)</td><td>162.26 (n/a)</td><td>151.70 (n/a)</td><td>136.00 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 <b>(-23.33%)</b></td><td>0.10 (-17.91%)</td><td>0.10 <b>(-20.95%)</b></td><td>0.06 <b>(-23.69%)</b></td><td>0.03 (-12.43%)</td><td>288.70 <b>(+31.05%)</b></td><td>195.88 <b>(+23.46%)</b></td><td>188.30 <b>(+26.55%)</b></td><td>146.40 <b>(+30.48%)</b></td><td>57.46 <b>(+46.10%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>220.30 (n/a)</td><td>158.66 (n/a)</td><td>148.80 (n/a)</td><td>112.20 (n/a)</td><td>39.33 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (-15.55%)</td><td>0.08 <b>(-24.68%)</b></td><td>0.08 <b>(-22.21%)</b></td><td>0.05 <b>(-42.03%)</b></td><td>0.03 <b>(+34.24%)</b></td><td>338.90 <b>(+72.47%)</b></td><td>241.14 <b>(+41.05%)</b></td><td>234.40 <b>(+28.58%)</b></td><td>153.90 (+18.38%)</td><td>76.87 <b>(+173.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>196.50 (n/a)</td><td>170.96 (n/a)</td><td>182.30 (n/a)</td><td>130.00 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (-19.25%)</td><td>0.09 (-19.57%)</td><td>0.08 (-17.14%)</td><td>0.06 <b>(-35.36%)</b></td><td>0.02 (+6.88%)</td><td>321.80 <b>(+54.71%)</b></td><td>224.52 <b>(+28.77%)</b></td><td>220.60 <b>(+20.68%)</b></td><td>156.10 <b>(+23.89%)</b></td><td>65.69 <b>(+106.50%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>208.00 (n/a)</td><td>174.36 (n/a)</td><td>182.80 (n/a)</td><td>126.00 (n/a)</td><td>31.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.85 (+9.54%)</td><td>0.56 (-16.41%)</td><td>0.49 <b>(-22.02%)</b></td><td>0.44 <b>(-24.27%)</b></td><td>0.17 <b>(+100.89%)</b></td><td>225.00 <b>(+32.04%)</b></td><td>186.14 <b>(+24.74%)</b></td><td>198.90 <b>(+28.24%)</b></td><td>115.90 (-8.67%)</td><td>41.31 <b>(+130.21%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.77 (n/a)</td><td>0.67 (n/a)</td><td>0.63 (n/a)</td><td>0.58 (n/a)</td><td>0.08 (n/a)</td><td>170.40 (n/a)</td><td>149.22 (n/a)</td><td>155.10 (n/a)</td><td>126.90 (n/a)</td><td>17.94 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.78 <b>(+27.32%)</b></td><td>0.57 (+2.37%)</td><td>0.54 (-4.26%)</td><td>0.48 (-6.39%)</td><td>0.12 <b>(+195.43%)</b></td><td>204.90 (+6.83%)</td><td>176.36 (+0.23%)</td><td>182.50 (+4.46%)</td><td>125.30 <b>(-21.49%)</b></td><td>30.99 <b>(+140.45%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.62 (n/a)</td><td>0.56 (n/a)</td><td>0.56 (n/a)</td><td>0.51 (n/a)</td><td>0.04 (n/a)</td><td>191.80 (n/a)</td><td>175.96 (n/a)</td><td>174.70 (n/a)</td><td>159.60 (n/a)</td><td>12.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.61 (-3.08%)</td><td>0.53 (+0.78%)</td><td>0.54 (+4.07%)</td><td>0.48 (+2.85%)</td><td>0.05 (-18.34%)</td><td>203.50 (-2.77%)</td><td>185.28 (-1.15%)</td><td>183.20 (-3.93%)</td><td>160.10 (+3.22%)</td><td>18.37 (-17.29%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.63 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>0.47 (n/a)</td><td>0.07 (n/a)</td><td>209.30 (n/a)</td><td>187.44 (n/a)</td><td>190.70 (n/a)</td><td>155.10 (n/a)</td><td>22.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.62 (+0.50%)</td><td>0.45 (-14.14%)</td><td>0.44 (-18.45%)</td><td>0.35 (-13.67%)</td><td>0.11 <b>(+32.47%)</b></td><td>281.60 (+15.84%)</td><td>224.86 (+18.61%)</td><td>225.50 <b>(+22.62%)</b></td><td>157.70 (-0.50%)</td><td>46.73 <b>(+45.72%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.62 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.40 (n/a)</td><td>0.08 (n/a)</td><td>243.10 (n/a)</td><td>189.58 (n/a)</td><td>183.90 (n/a)</td><td>158.50 (n/a)</td><td>32.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.59 (+8.14%)</td><td>0.43 (-10.60%)</td><td>0.40 <b>(-21.04%)</b></td><td>0.36 (-6.00%)</td><td>0.09 <b>(+34.94%)</b></td><td>202.50 (+6.36%)</td><td>177.56 (+13.21%)</td><td>186.00 <b>(+26.62%)</b></td><td>125.10 (-7.54%)</td><td>30.13 <b>(+27.61%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.55 (n/a)</td><td>0.48 (n/a)</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>190.40 (n/a)</td><td>156.84 (n/a)</td><td>146.90 (n/a)</td><td>135.30 (n/a)</td><td>23.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.68 <b>(+47.93%)</b></td><td>0.37 (+3.68%)</td><td>0.32 (-13.49%)</td><td>0.22 (-17.15%)</td><td>0.18 <b>(+98.56%)</b></td><td>340.00 <b>(+20.70%)</b></td><td>226.72 (+5.05%)</td><td>230.60 (+15.59%)</td><td>108.50 <b>(-32.40%)</b></td><td>82.06 <b>(+47.58%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.09 (n/a)</td><td>281.70 (n/a)</td><td>215.82 (n/a)</td><td>199.50 (n/a)</td><td>160.50 (n/a)</td><td>55.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.59 (+9.41%)</td><td>0.42 (-5.81%)</td><td>0.36 (-19.65%)</td><td>0.27 <b>(-28.63%)</b></td><td>0.13 <b>(+125.42%)</b></td><td>271.10 <b>(+40.10%)</b></td><td>190.84 (+13.53%)</td><td>206.30 <b>(+24.43%)</b></td><td>125.60 (-8.59%)</td><td>59.21 <b>(+180.37%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.54 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.06 (n/a)</td><td>193.50 (n/a)</td><td>168.10 (n/a)</td><td>165.80 (n/a)</td><td>137.40 (n/a)</td><td>21.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.48 (+0.96%)</td><td>0.39 (+1.17%)</td><td>0.35 (-14.27%)</td><td>0.31 <b>(+44.29%)</b></td><td>0.07 <b>(-24.83%)</b></td><td>237.00 <b>(-30.70%)</b></td><td>195.76 (-5.87%)</td><td>208.80 (+16.65%)</td><td>153.70 (-0.97%)</td><td>35.94 <b>(-52.68%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.41 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>342.00 (n/a)</td><td>207.96 (n/a)</td><td>179.00 (n/a)</td><td>155.20 (n/a)</td><td>75.95 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (-19.02%)</td><td>0.20 (-9.39%)</td><td>0.20 (-6.62%)</td><td>0.17 (-7.53%)</td><td>0.02 <b>(-34.10%)</b></td><td>219.40 (+8.13%)</td><td>188.28 (+9.61%)</td><td>187.90 (+7.13%)</td><td>167.10 <b>(+23.50%)</b></td><td>21.50 (-11.01%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>202.90 (n/a)</td><td>171.78 (n/a)</td><td>175.40 (n/a)</td><td>135.30 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 <b>(-20.80%)</b></td><td>0.18 (-7.21%)</td><td>0.17 (-6.57%)</td><td>0.16 (+2.87%)</td><td>0.02 <b>(-52.76%)</b></td><td>228.70 (-2.76%)</td><td>206.96 (+5.82%)</td><td>213.70 (+7.01%)</td><td>186.20 <b>(+26.24%)</b></td><td>19.31 <b>(-42.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>235.20 (n/a)</td><td>195.58 (n/a)</td><td>199.70 (n/a)</td><td>147.50 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.27 (+14.66%)</td><td>0.21 (+4.41%)</td><td>0.21 (+0.61%)</td><td>0.17 (-5.45%)</td><td>0.05 <b>(+81.40%)</b></td><td>222.60 (+5.75%)</td><td>178.86 (-1.81%)</td><td>173.60 (-0.63%)</td><td>137.30 (-12.83%)</td><td>38.64 <b>(+67.60%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>210.50 (n/a)</td><td>182.16 (n/a)</td><td>174.70 (n/a)</td><td>157.50 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.24 (+3.64%)</td><td>0.21 (+2.00%)</td><td>0.21 (+2.65%)</td><td>0.17 (-7.58%)</td><td>0.03 (+16.23%)</td><td>223.30 (+8.24%)</td><td>180.24 (-1.51%)</td><td>173.10 (-2.59%)</td><td>152.20 (-3.49%)</td><td>26.43 <b>(+21.62%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>206.30 (n/a)</td><td>183.00 (n/a)</td><td>177.70 (n/a)</td><td>157.70 (n/a)</td><td>21.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (+6.17%)</td><td>0.17 (-9.64%)</td><td>0.16 (-13.23%)</td><td>0.14 (-17.24%)</td><td>0.03 <b>(+147.33%)</b></td><td>261.00 <b>(+20.83%)</b></td><td>223.40 (+12.42%)</td><td>225.40 (+15.24%)</td><td>174.20 (-5.84%)</td><td>32.32 <b>(+174.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>198.72 (n/a)</td><td>195.60 (n/a)</td><td>185.00 (n/a)</td><td>11.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (-8.36%)</td><td>0.20 (-4.73%)</td><td>0.18 (-14.69%)</td><td>0.16 (+17.85%)</td><td>0.05 <b>(-21.92%)</b></td><td>226.90 (-15.15%)</td><td>192.60 (+2.27%)</td><td>207.10 (+17.20%)</td><td>133.90 (+9.13%)</td><td>37.73 <b>(-28.10%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>267.40 (n/a)</td><td>188.32 (n/a)</td><td>176.70 (n/a)</td><td>122.70 (n/a)</td><td>52.47 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.33 <b>(+46.62%)</b></td><td>0.20 (+5.95%)</td><td>0.17 (-6.59%)</td><td>0.14 (-1.44%)</td><td>0.08 <b>(+126.99%)</b></td><td>261.40 (+1.44%)</td><td>200.84 (+1.30%)</td><td>211.00 (+7.05%)</td><td>111.10 <b>(-31.84%)</b></td><td>62.78 <b>(+62.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>257.70 (n/a)</td><td>198.26 (n/a)</td><td>197.10 (n/a)</td><td>163.00 (n/a)</td><td>38.72 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 <b>(-20.39%)</b></td><td>0.17 (-14.86%)</td><td>0.16 (-12.83%)</td><td>0.14 (+0.97%)</td><td>0.03 <b>(-40.33%)</b></td><td>270.50 (-0.99%)</td><td>217.46 (+13.59%)</td><td>223.60 (+14.73%)</td><td>164.20 <b>(+25.63%)</b></td><td>39.42 <b>(-26.77%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>273.20 (n/a)</td><td>191.44 (n/a)</td><td>194.90 (n/a)</td><td>130.70 (n/a)</td><td>53.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.35 (+6.47%)</td><td>0.24 (-11.72%)</td><td>0.21 (-13.25%)</td><td>0.21 (-13.73%)</td><td>0.06 <b>(+40.57%)</b></td><td>197.50 (+15.90%)</td><td>175.50 (+15.48%)</td><td>191.90 (+15.26%)</td><td>117.90 (-6.06%)</td><td>33.03 <b>(+49.21%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>170.40 (n/a)</td><td>151.98 (n/a)</td><td>166.50 (n/a)</td><td>125.50 (n/a)</td><td>22.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.26 (-14.21%)</td><td>0.23 (-8.13%)</td><td>0.22 (-12.14%)</td><td>0.20 (+13.22%)</td><td>0.02 <b>(-50.82%)</b></td><td>202.70 (-11.68%)</td><td>182.26 (+6.14%)</td><td>183.70 (+13.82%)</td><td>155.80 (+16.62%)</td><td>18.25 <b>(-50.47%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>229.50 (n/a)</td><td>171.72 (n/a)</td><td>161.40 (n/a)</td><td>133.60 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (-1.07%)</td><td>0.22 (-15.28%)</td><td>0.19 <b>(-23.24%)</b></td><td>0.18 <b>(-22.67%)</b></td><td>0.05 <b>(+74.34%)</b></td><td>222.70 <b>(+29.33%)</b></td><td>192.94 <b>(+21.68%)</b></td><td>216.40 <b>(+30.28%)</b></td><td>132.40 (+1.07%)</td><td>39.62 <b>(+133.11%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>172.20 (n/a)</td><td>158.56 (n/a)</td><td>166.10 (n/a)</td><td>131.00 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (+2.06%)</td><td>0.22 (-5.91%)</td><td>0.22 (-9.28%)</td><td>0.17 (+16.51%)</td><td>0.04 (-11.13%)</td><td>235.30 (-14.16%)</td><td>193.48 (+4.61%)</td><td>184.50 (+10.28%)</td><td>147.30 (-2.00%)</td><td>36.56 <b>(-27.44%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>274.10 (n/a)</td><td>184.96 (n/a)</td><td>167.30 (n/a)</td><td>150.30 (n/a)</td><td>50.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (+0.37%)</td><td>0.23 (-4.16%)</td><td>0.23 (-15.58%)</td><td>0.20 (+16.14%)</td><td>0.03 <b>(-35.22%)</b></td><td>206.00 (-13.92%)</td><td>179.00 (+2.05%)</td><td>179.90 (+18.43%)</td><td>147.40 (-0.41%)</td><td>22.08 <b>(-44.00%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>239.30 (n/a)</td><td>175.40 (n/a)</td><td>151.90 (n/a)</td><td>148.00 (n/a)</td><td>39.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (-8.54%)</td><td>0.25 (-4.57%)</td><td>0.24 (-6.57%)</td><td>0.21 (+14.58%)</td><td>0.04 <b>(-31.12%)</b></td><td>195.00 (-12.75%)</td><td>169.88 (+2.66%)</td><td>168.60 (+7.05%)</td><td>134.00 (+9.30%)</td><td>23.59 <b>(-35.95%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>223.50 (n/a)</td><td>165.48 (n/a)</td><td>157.50 (n/a)</td><td>122.60 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (+15.91%)</td><td>0.21 (+2.37%)</td><td>0.20 (-5.70%)</td><td>0.16 (-5.25%)</td><td>0.06 <b>(+50.63%)</b></td><td>262.00 (+5.56%)</td><td>205.88 (+0.49%)</td><td>208.60 (+6.05%)</td><td>130.70 (-13.73%)</td><td>50.08 <b>(+34.02%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>248.20 (n/a)</td><td>204.88 (n/a)</td><td>196.70 (n/a)</td><td>151.50 (n/a)</td><td>37.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.34 <b>(+25.92%)</b></td><td>0.25 (+12.25%)</td><td>0.26 <b>(+24.56%)</b></td><td>0.13 <b>(-33.59%)</b></td><td>0.09 <b>(+186.50%)</b></td><td>306.00 <b>(+50.59%)</b></td><td>183.24 (-0.78%)</td><td>158.50 (-19.71%)</td><td>119.50 <b>(-20.60%)</b></td><td>77.32 <b>(+229.75%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>203.20 (n/a)</td><td>184.68 (n/a)</td><td>197.40 (n/a)</td><td>150.50 (n/a)</td><td>23.45 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.24 (+14.01%)</td><td>0.18 (-5.46%)</td><td>0.17 (-16.43%)</td><td>0.16 (+14.34%)</td><td>0.03 (+5.81%)</td><td>215.70 (-12.53%)</td><td>194.60 (+5.36%)</td><td>202.20 (+19.64%)</td><td>147.30 (-12.27%)</td><td>27.11 <b>(-21.71%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>246.60 (n/a)</td><td>184.70 (n/a)</td><td>169.00 (n/a)</td><td>167.90 (n/a)</td><td>34.63 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (-4.26%)</td><td>0.19 (-11.60%)</td><td>0.18 (-11.36%)</td><td>0.15 (-18.26%)</td><td>0.04 (+16.79%)</td><td>239.60 <b>(+22.31%)</b></td><td>186.44 (+14.80%)</td><td>188.50 (+12.81%)</td><td>137.10 (+4.42%)</td><td>38.84 <b>(+49.75%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>195.90 (n/a)</td><td>162.40 (n/a)</td><td>167.10 (n/a)</td><td>131.30 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.27 (-3.22%)</td><td>0.19 (-4.79%)</td><td>0.18 (-5.67%)</td><td>0.14 (-9.50%)</td><td>0.05 (-0.11%)</td><td>249.70 (+10.54%)</td><td>188.20 (+5.58%)</td><td>190.40 (+6.01%)</td><td>127.70 (+3.32%)</td><td>44.88 (+12.96%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>225.90 (n/a)</td><td>178.26 (n/a)</td><td>179.60 (n/a)</td><td>123.60 (n/a)</td><td>39.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (+10.89%)</td><td>0.21 (-3.30%)</td><td>0.19 (-6.98%)</td><td>0.15 <b>(-21.03%)</b></td><td>0.07 <b>(+72.77%)</b></td><td>234.20 <b>(+26.59%)</b></td><td>177.82 (+8.48%)</td><td>182.00 (+7.50%)</td><td>111.20 (-9.81%)</td><td>48.44 <b>(+100.07%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>185.00 (n/a)</td><td>163.92 (n/a)</td><td>169.30 (n/a)</td><td>123.30 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.24 (-15.01%)</td><td>0.20 (+6.53%)</td><td>0.23 <b>(+40.09%)</b></td><td>0.14 (-1.32%)</td><td>0.05 (-18.96%)</td><td>242.30 (+1.34%)</td><td>178.30 (-7.20%)</td><td>149.10 <b>(-28.63%)</b></td><td>144.30 (+17.70%)</td><td>44.35 (-3.65%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>239.10 (n/a)</td><td>192.14 (n/a)</td><td>208.90 (n/a)</td><td>122.60 (n/a)</td><td>46.03 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (-8.16%)</td><td>0.19 (-16.58%)</td><td>0.19 <b>(-22.32%)</b></td><td>0.12 <b>(-31.69%)</b></td><td>0.05 (+15.12%)</td><td>285.80 <b>(+46.41%)</b></td><td>195.56 <b>(+23.30%)</b></td><td>187.50 <b>(+28.78%)</b></td><td>137.70 (+8.85%)</td><td>54.66 <b>(+86.28%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>195.20 (n/a)</td><td>158.60 (n/a)</td><td>145.60 (n/a)</td><td>126.50 (n/a)</td><td>29.35 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (-4.89%)</td><td>0.17 <b>(-20.87%)</b></td><td>0.16 <b>(-25.48%)</b></td><td>0.13 <b>(-27.32%)</b></td><td>0.03 <b>(+70.25%)</b></td><td>259.40 <b>(+37.54%)</b></td><td>211.64 <b>(+28.75%)</b></td><td>214.80 <b>(+34.17%)</b></td><td>158.50 (+5.18%)</td><td>35.93 <b>(+138.04%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>188.60 (n/a)</td><td>164.38 (n/a)</td><td>160.10 (n/a)</td><td>150.70 (n/a)</td><td>15.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.30 (+3.18%)</td><td>0.21 (-10.28%)</td><td>0.17 <b>(-29.15%)</b></td><td>0.14 (-16.76%)</td><td>0.07 <b>(+41.48%)</b></td><td>248.60 <b>(+20.15%)</b></td><td>183.20 (+16.90%)</td><td>209.40 <b>(+41.11%)</b></td><td>115.50 (-3.10%)</td><td>56.72 <b>(+59.93%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>206.90 (n/a)</td><td>156.72 (n/a)</td><td>148.40 (n/a)</td><td>119.20 (n/a)</td><td>35.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.76 (-3.24%)</td><td>0.69 (+9.24%)</td><td>0.70 (+8.96%)</td><td>0.58 <b>(+27.51%)</b></td><td>0.07 <b>(-41.74%)</b></td><td>225.20 <b>(-21.59%)</b></td><td>192.26 (-10.45%)</td><td>186.80 (-8.25%)</td><td>173.30 (+3.34%)</td><td>20.36 <b>(-53.82%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.78 (n/a)</td><td>0.63 (n/a)</td><td>0.64 (n/a)</td><td>0.46 (n/a)</td><td>0.12 (n/a)</td><td>287.20 (n/a)</td><td>214.70 (n/a)</td><td>203.60 (n/a)</td><td>167.70 (n/a)</td><td>44.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.77 <b>(-30.05%)</b></td><td>0.74 (-7.51%)</td><td>0.74 (+0.89%)</td><td>0.70 (+5.38%)</td><td>0.02 <b>(-86.14%)</b></td><td>186.10 (-5.10%)</td><td>178.08 (+4.88%)</td><td>176.70 (-0.90%)</td><td>170.30 <b>(+42.99%)</b></td><td>5.86 <b>(-80.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.10 (n/a)</td><td>0.80 (n/a)</td><td>0.74 (n/a)</td><td>0.67 (n/a)</td><td>0.17 (n/a)</td><td>196.10 (n/a)</td><td>169.80 (n/a)</td><td>178.30 (n/a)</td><td>119.10 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.91 (+8.87%)</td><td>0.68 (-10.32%)</td><td>0.67 (-12.24%)</td><td>0.50 <b>(-25.38%)</b></td><td>0.15 <b>(+145.61%)</b></td><td>264.60 <b>(+33.97%)</b></td><td>200.34 (+15.32%)</td><td>196.20 (+13.94%)</td><td>143.80 (-8.17%)</td><td>44.10 <b>(+196.75%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.84 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.66 (n/a)</td><td>0.06 (n/a)</td><td>197.50 (n/a)</td><td>173.72 (n/a)</td><td>172.20 (n/a)</td><td>156.60 (n/a)</td><td>14.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-6.87%)</td><td>0.02 (-2.94%)</td><td>0.03 (+8.11%)</td><td>0.02 (-15.48%)</td><td>0.00 (+3.73%)</td><td>227.60 (+18.30%)</td><td>171.08 (+3.89%)</td><td>160.70 (-7.48%)</td><td>138.10 (+7.39%)</td><td>35.41 <b>(+33.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.40 (n/a)</td><td>164.68 (n/a)</td><td>173.70 (n/a)</td><td>128.60 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-11.12%)</td><td>0.02 (-5.44%)</td><td>0.03 (-1.67%)</td><td>0.02 (-2.96%)</td><td>0.00 <b>(-21.51%)</b></td><td>225.10 (+3.07%)</td><td>171.22 (+4.88%)</td><td>160.20 (+1.71%)</td><td>145.40 (+12.54%)</td><td>31.41 (-7.92%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.40 (n/a)</td><td>163.26 (n/a)</td><td>157.50 (n/a)</td><td>129.20 (n/a)</td><td>34.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-3.67%)</td><td>0.03 (+6.70%)</td><td>0.03 (+7.49%)</td><td>0.02 (+17.16%)</td><td>0.00 <b>(-45.51%)</b></td><td>171.80 (-14.65%)</td><td>155.68 (-8.08%)</td><td>157.00 (-6.99%)</td><td>135.50 (+3.83%)</td><td>14.16 <b>(-52.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.30 (n/a)</td><td>169.36 (n/a)</td><td>168.80 (n/a)</td><td>130.50 (n/a)</td><td>29.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>16.36 (-6.51%)</td><td>13.78 (+9.18%)</td><td>12.68 (+8.63%)</td><td>12.03 (+13.87%)</td><td>2.05 <b>(-26.32%)</b></td><td>174.40 (-12.19%)</td><td>154.86 (-9.72%)</td><td>165.50 (-7.95%)</td><td>128.30 (+7.01%)</td><td>21.85 <b>(-27.81%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>17.49 (n/a)</td><td>12.62 (n/a)</td><td>11.67 (n/a)</td><td>10.57 (n/a)</td><td>2.78 (n/a)</td><td>198.60 (n/a)</td><td>171.54 (n/a)</td><td>179.80 (n/a)</td><td>119.90 (n/a)</td><td>30.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.05 (-16.82%)</td><td>0.85 (-8.07%)</td><td>0.79 (-12.87%)</td><td>0.74 <b>(+41.71%)</b></td><td>0.12 <b>(-53.80%)</b></td><td>178.00 <b>(-29.45%)</b></td><td>158.58 (+1.60%)</td><td>166.90 (+14.79%)</td><td>126.30 <b>(+20.17%)</b></td><td>20.57 <b>(-63.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.26 (n/a)</td><td>0.92 (n/a)</td><td>0.91 (n/a)</td><td>0.52 (n/a)</td><td>0.26 (n/a)</td><td>252.30 (n/a)</td><td>156.08 (n/a)</td><td>145.40 (n/a)</td><td>105.10 (n/a)</td><td>56.35 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.11 (-12.30%)</td><td>0.78 (-18.24%)</td><td>0.72 (-17.88%)</td><td>0.61 <b>(-21.89%)</b></td><td>0.20 (-1.57%)</td><td>217.20 <b>(+28.07%)</b></td><td>175.90 <b>(+23.63%)</b></td><td>184.20 <b>(+21.74%)</b></td><td>118.50 (+13.94%)</td><td>36.60 <b>(+39.35%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.27 (n/a)</td><td>0.96 (n/a)</td><td>0.87 (n/a)</td><td>0.78 (n/a)</td><td>0.20 (n/a)</td><td>169.60 (n/a)</td><td>142.28 (n/a)</td><td>151.30 (n/a)</td><td>104.00 (n/a)</td><td>26.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.06 (+5.83%)</td><td>0.84 (+6.12%)</td><td>0.80 (-7.97%)</td><td>0.63 <b>(+47.77%)</b></td><td>0.16 <b>(-30.43%)</b></td><td>211.10 <b>(-32.32%)</b></td><td>161.84 (-11.79%)</td><td>165.00 (+8.70%)</td><td>125.10 (-5.51%)</td><td>32.22 <b>(-56.59%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.00 (n/a)</td><td>0.79 (n/a)</td><td>0.87 (n/a)</td><td>0.42 (n/a)</td><td>0.23 (n/a)</td><td>311.90 (n/a)</td><td>183.48 (n/a)</td><td>151.80 (n/a)</td><td>132.40 (n/a)</td><td>74.20 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.20 (+12.21%)</td><td>0.86 (-7.44%)</td><td>0.83 (-4.86%)</td><td>0.61 <b>(-22.09%)</b></td><td>0.22 <b>(+76.78%)</b></td><td>218.30 <b>(+28.34%)</b></td><td>162.16 (+11.96%)</td><td>158.40 (+5.11%)</td><td>110.30 (-10.83%)</td><td>39.54 <b>(+103.87%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.07 (n/a)</td><td>0.93 (n/a)</td><td>0.88 (n/a)</td><td>0.78 (n/a)</td><td>0.12 (n/a)</td><td>170.10 (n/a)</td><td>144.84 (n/a)</td><td>150.70 (n/a)</td><td>123.70 (n/a)</td><td>19.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.96 (-10.11%)</td><td>0.80 (-15.97%)</td><td>0.83 (-18.10%)</td><td>0.59 <b>(-27.15%)</b></td><td>0.14 (+9.29%)</td><td>224.90 <b>(+37.30%)</b></td><td>170.08 <b>(+20.45%)</b></td><td>158.80 <b>(+22.06%)</b></td><td>137.40 (+11.26%)</td><td>32.95 <b>(+70.27%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.07 (n/a)</td><td>0.95 (n/a)</td><td>1.02 (n/a)</td><td>0.81 (n/a)</td><td>0.12 (n/a)</td><td>163.80 (n/a)</td><td>141.20 (n/a)</td><td>130.10 (n/a)</td><td>123.50 (n/a)</td><td>19.35 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-13.46%)</td><td>0.03 (-1.22%)</td><td>0.03 (+6.72%)</td><td>0.02 (+18.13%)</td><td>0.00 <b>(-58.09%)</b></td><td>172.00 (-15.35%)</td><td>149.08 (-2.55%)</td><td>139.70 (-6.24%)</td><td>135.70 (+15.49%)</td><td>15.75 <b>(-57.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>152.98 (n/a)</td><td>149.00 (n/a)</td><td>117.50 (n/a)</td><td>37.20 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (-2.60%)</td><td>0.03 (-2.75%)</td><td>0.03 (+0.65%)</td><td>0.02 (-2.64%)</td><td>0.00 <b>(-20.14%)</b></td><td>171.00 (+2.70%)</td><td>148.44 (+2.26%)</td><td>145.50 (-0.61%)</td><td>125.70 (+2.70%)</td><td>18.12 (-15.62%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.50 (n/a)</td><td>145.16 (n/a)</td><td>146.40 (n/a)</td><td>122.40 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.00 (+0.00%)</td><td>0.00 (+0.47%)</td><td>0.00 (+0.00%)</td><td>0.00 (+5.26%)</td><td>0.00 <b>(-28.81%)</b></td><td>1032.21 (-5.07%)</td><td>965.46 (+0.03%)</td><td>962.12 (+2.17%)</td><td>906.97 (-1.00%)</td><td>46.95 <b>(-32.28%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1087.36 (n/a)</td><td>965.18 (n/a)</td><td>941.68 (n/a)</td><td>916.15 (n/a)</td><td>69.33 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.01 (+4.94%)</td><td>0.01 (+3.31%)</td><td>0.01 (+0.00%)</td><td>0.01 (+11.11%)</td><td>0.00 <b>(-41.64%)</b></td><td>1028.46 (-9.17%)</td><td>1009.36 (-3.23%)</td><td>1019.04 (-0.27%)</td><td>964.09 (-5.11%)</td><td>25.74 <b>(-48.52%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1132.32 (n/a)</td><td>1043.07 (n/a)</td><td>1021.79 (n/a)</td><td>1015.96 (n/a)</td><td>49.99 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.97 (-2.07%)</td><td>0.96 (-2.10%)</td><td>0.96 (-3.12%)</td><td>0.95 (-1.14%)</td><td>0.01 <b>(-51.40%)</b></td><td>2201.13 (+1.16%)</td><td>2188.38 (+2.14%)</td><td>2193.32 (+3.22%)</td><td>2164.97 (+2.12%)</td><td>14.17 <b>(-49.83%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.99 (n/a)</td><td>0.98 (n/a)</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.01 (n/a)</td><td>2175.99 (n/a)</td><td>2142.56 (n/a)</td><td>2124.80 (n/a)</td><td>2120.02 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>5.97 (+4.67%)</td><td>5.37 (+7.42%)</td><td>5.50 (+9.18%)</td><td>4.83 (+9.58%)</td><td>0.48 (-9.77%)</td><td>217.10 (-8.74%)</td><td>196.64 (-7.15%)</td><td>190.60 (-8.41%)</td><td>175.80 (-4.46%)</td><td>17.68 <b>(-21.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>5.70 (n/a)</td><td>5.00 (n/a)</td><td>5.04 (n/a)</td><td>4.41 (n/a)</td><td>0.53 (n/a)</td><td>237.90 (n/a)</td><td>211.78 (n/a)</td><td>208.10 (n/a)</td><td>184.00 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.28 (+3.87%)</td><td>4.88 (-1.80%)</td><td>4.82 (+6.61%)</td><td>3.80 (-9.23%)</td><td>0.89 (+4.63%)</td><td>275.90 (+10.14%)</td><td>220.40 (+2.14%)</td><td>217.60 (-6.21%)</td><td>167.10 (-3.69%)</td><td>38.62 (+10.33%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.04 (n/a)</td><td>4.97 (n/a)</td><td>4.52 (n/a)</td><td>4.19 (n/a)</td><td>0.85 (n/a)</td><td>250.50 (n/a)</td><td>215.78 (n/a)</td><td>232.00 (n/a)</td><td>173.50 (n/a)</td><td>35.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>5.61 (-12.90%)</td><td>5.02 (-0.42%)</td><td>4.99 (-2.96%)</td><td>4.47 (+19.86%)</td><td>0.45 <b>(-56.86%)</b></td><td>234.50 (-16.55%)</td><td>210.22 (-2.50%)</td><td>210.00 (+3.04%)</td><td>186.80 (+14.74%)</td><td>18.95 <b>(-59.01%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.44 (n/a)</td><td>5.04 (n/a)</td><td>5.14 (n/a)</td><td>3.73 (n/a)</td><td>1.05 (n/a)</td><td>281.00 (n/a)</td><td>215.60 (n/a)</td><td>203.80 (n/a)</td><td>162.80 (n/a)</td><td>46.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.01 (-3.29%)</td><td>4.94 (-1.18%)</td><td>4.69 (-4.55%)</td><td>4.04 (+10.68%)</td><td>0.77 <b>(-26.85%)</b></td><td>259.40 (-9.65%)</td><td>216.20 (-0.64%)</td><td>223.70 (+4.78%)</td><td>174.40 (+3.44%)</td><td>32.86 <b>(-31.47%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.22 (n/a)</td><td>5.00 (n/a)</td><td>4.91 (n/a)</td><td>3.65 (n/a)</td><td>1.05 (n/a)</td><td>287.10 (n/a)</td><td>217.60 (n/a)</td><td>213.50 (n/a)</td><td>168.60 (n/a)</td><td>47.94 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.94 (+9.73%)</td><td>8.42 (+1.65%)</td><td>8.59 (+3.55%)</td><td>6.68 (-14.06%)</td><td>1.18 <b>(+134.59%)</b></td><td>313.80 (+16.35%)</td><td>253.22 (-0.24%)</td><td>244.30 (-3.40%)</td><td>211.00 (-8.86%)</td><td>37.90 <b>(+153.22%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.06 (n/a)</td><td>8.29 (n/a)</td><td>8.29 (n/a)</td><td>7.78 (n/a)</td><td>0.50 (n/a)</td><td>269.70 (n/a)</td><td>253.84 (n/a)</td><td>252.90 (n/a)</td><td>231.50 (n/a)</td><td>14.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.88 (-7.30%)</td><td>6.98 (-12.68%)</td><td>6.76 (-16.97%)</td><td>6.39 (-9.76%)</td><td>0.65 (+19.23%)</td><td>328.00 (+10.81%)</td><td>302.42 (+14.86%)</td><td>310.50 <b>(+20.44%)</b></td><td>266.30 (+7.90%)</td><td>27.34 <b>(+41.65%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>8.50 (n/a)</td><td>8.00 (n/a)</td><td>8.14 (n/a)</td><td>7.09 (n/a)</td><td>0.55 (n/a)</td><td>296.00 (n/a)</td><td>263.30 (n/a)</td><td>257.80 (n/a)</td><td>246.80 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.05 (+1.65%)</td><td>7.76 (+1.20%)</td><td>7.40 (+2.85%)</td><td>6.69 (-3.86%)</td><td>1.12 <b>(+34.90%)</b></td><td>313.50 (+4.01%)</td><td>274.74 (-0.46%)</td><td>283.20 (-2.78%)</td><td>231.80 (-1.61%)</td><td>38.47 <b>(+36.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>8.90 (n/a)</td><td>7.67 (n/a)</td><td>7.20 (n/a)</td><td>6.96 (n/a)</td><td>0.83 (n/a)</td><td>301.40 (n/a)</td><td>276.00 (n/a)</td><td>291.30 (n/a)</td><td>235.60 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>10.53 (+16.42%)</td><td>8.09 (-5.15%)</td><td>7.76 (-9.83%)</td><td>6.28 (-17.66%)</td><td>1.59 <b>(+193.92%)</b></td><td>334.10 <b>(+21.45%)</b></td><td>266.76 (+8.18%)</td><td>270.10 (+10.88%)</td><td>199.10 (-14.11%)</td><td>49.81 <b>(+198.58%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.05 (n/a)</td><td>8.53 (n/a)</td><td>8.61 (n/a)</td><td>7.62 (n/a)</td><td>0.54 (n/a)</td><td>275.10 (n/a)</td><td>246.58 (n/a)</td><td>243.60 (n/a)</td><td>231.80 (n/a)</td><td>16.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>8.58 (-17.55%)</td><td>7.75 (-9.72%)</td><td>7.86 (-11.38%)</td><td>6.72 <b>(+23.18%)</b></td><td>0.79 <b>(-59.18%)</b></td><td>312.10 (-18.83%)</td><td>273.04 (+6.03%)</td><td>266.80 (+12.81%)</td><td>244.50 <b>(+21.28%)</b></td><td>28.52 <b>(-61.31%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.40 (n/a)</td><td>8.58 (n/a)</td><td>8.87 (n/a)</td><td>5.45 (n/a)</td><td>1.93 (n/a)</td><td>384.50 (n/a)</td><td>257.50 (n/a)</td><td>236.50 (n/a)</td><td>201.60 (n/a)</td><td>73.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.77 (+1.33%)</td><td>8.82 (-2.33%)</td><td>8.67 (-4.38%)</td><td>7.95 (-4.86%)</td><td>0.73 <b>(+44.29%)</b></td><td>263.90 (+5.10%)</td><td>239.16 (+2.69%)</td><td>241.90 (+4.58%)</td><td>214.70 (-1.33%)</td><td>19.57 <b>(+48.81%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.64 (n/a)</td><td>9.03 (n/a)</td><td>9.07 (n/a)</td><td>8.35 (n/a)</td><td>0.50 (n/a)</td><td>251.10 (n/a)</td><td>232.90 (n/a)</td><td>231.30 (n/a)</td><td>217.60 (n/a)</td><td>13.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>12.51 (-5.08%)</td><td>11.43 (-2.17%)</td><td>11.18 (-3.30%)</td><td>11.07 (+4.46%)</td><td>0.61 <b>(-40.13%)</b></td><td>378.90 (-4.27%)</td><td>367.84 (+1.84%)</td><td>375.00 (+3.39%)</td><td>335.30 (+5.37%)</td><td>18.27 <b>(-39.97%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.18 (n/a)</td><td>11.68 (n/a)</td><td>11.57 (n/a)</td><td>10.60 (n/a)</td><td>1.01 (n/a)</td><td>395.80 (n/a)</td><td>361.18 (n/a)</td><td>362.70 (n/a)</td><td>318.20 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>12.67 (-0.54%)</td><td>11.56 (-3.91%)</td><td>11.24 (-5.60%)</td><td>10.94 (-4.75%)</td><td>0.76 <b>(+57.85%)</b></td><td>383.40 (+4.98%)</td><td>364.04 (+4.29%)</td><td>373.30 (+5.93%)</td><td>331.00 (+0.55%)</td><td>23.04 <b>(+68.17%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>12.74 (n/a)</td><td>12.03 (n/a)</td><td>11.90 (n/a)</td><td>11.48 (n/a)</td><td>0.48 (n/a)</td><td>365.20 (n/a)</td><td>349.08 (n/a)</td><td>352.40 (n/a)</td><td>329.20 (n/a)</td><td>13.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>12.95 (+6.41%)</td><td>11.30 (-2.17%)</td><td>11.33 (-2.68%)</td><td>9.62 (-10.14%)</td><td>1.26 <b>(+126.90%)</b></td><td>436.10 (+11.28%)</td><td>374.92 (+3.07%)</td><td>370.10 (+2.75%)</td><td>324.00 (-6.01%)</td><td>42.62 <b>(+136.61%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>12.17 (n/a)</td><td>11.55 (n/a)</td><td>11.65 (n/a)</td><td>10.70 (n/a)</td><td>0.56 (n/a)</td><td>391.90 (n/a)</td><td>363.74 (n/a)</td><td>360.20 (n/a)</td><td>344.70 (n/a)</td><td>18.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>16.89 (+19.95%)</td><td>13.30 (+1.28%)</td><td>12.45 (-7.73%)</td><td>12.30 (+0.68%)</td><td>2.00 <b>(+147.70%)</b></td><td>341.00 (-0.67%)</td><td>320.14 (-0.05%)</td><td>336.90 (+8.40%)</td><td>248.40 (-16.62%)</td><td>40.14 <b>(+101.35%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.08 (n/a)</td><td>13.14 (n/a)</td><td>13.49 (n/a)</td><td>12.22 (n/a)</td><td>0.81 (n/a)</td><td>343.30 (n/a)</td><td>320.30 (n/a)</td><td>310.80 (n/a)</td><td>297.90 (n/a)</td><td>19.94 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.65 (-1.03%)</td><td>12.53 (-4.90%)</td><td>12.61 (-4.34%)</td><td>11.33 (-10.07%)</td><td>1.03 <b>(+113.68%)</b></td><td>370.40 (+11.23%)</td><td>336.58 (+5.62%)</td><td>332.70 (+4.56%)</td><td>307.20 (+1.05%)</td><td>27.92 <b>(+139.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.79 (n/a)</td><td>13.18 (n/a)</td><td>13.18 (n/a)</td><td>12.59 (n/a)</td><td>0.48 (n/a)</td><td>333.00 (n/a)</td><td>318.68 (n/a)</td><td>318.20 (n/a)</td><td>304.00 (n/a)</td><td>11.65 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.58 (+2.37%)</td><td>13.32 (+4.53%)</td><td>13.26 (+2.44%)</td><td>11.68 (+5.10%)</td><td>1.12 (-0.91%)</td><td>359.20 (-4.85%)</td><td>316.78 (-4.39%)</td><td>316.30 (-2.38%)</td><td>287.60 (-2.34%)</td><td>27.73 (-8.36%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.24 (n/a)</td><td>12.74 (n/a)</td><td>12.94 (n/a)</td><td>11.11 (n/a)</td><td>1.13 (n/a)</td><td>377.50 (n/a)</td><td>331.32 (n/a)</td><td>324.00 (n/a)</td><td>294.50 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.74 (-7.49%)</td><td>12.54 (-6.23%)</td><td>12.51 (-13.33%)</td><td>11.43 (+2.33%)</td><td>0.82 <b>(-51.06%)</b></td><td>367.10 (-2.26%)</td><td>335.72 (+5.58%)</td><td>335.30 (+15.38%)</td><td>305.30 (+8.11%)</td><td>21.97 <b>(-48.09%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.85 (n/a)</td><td>13.37 (n/a)</td><td>14.43 (n/a)</td><td>11.17 (n/a)</td><td>1.68 (n/a)</td><td>375.60 (n/a)</td><td>317.98 (n/a)</td><td>290.60 (n/a)</td><td>282.40 (n/a)</td><td>42.33 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.89 (+5.95%)</td><td>12.36 (+3.08%)</td><td>12.54 (+6.37%)</td><td>8.84 (-15.32%)</td><td>2.21 <b>(+69.11%)</b></td><td>474.50 (+18.09%)</td><td>349.70 (-0.92%)</td><td>334.40 (-5.99%)</td><td>281.70 (-5.60%)</td><td>73.42 <b>(+98.89%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.06 (n/a)</td><td>11.99 (n/a)</td><td>11.79 (n/a)</td><td>10.44 (n/a)</td><td>1.31 (n/a)</td><td>401.80 (n/a)</td><td>352.94 (n/a)</td><td>355.70 (n/a)</td><td>298.40 (n/a)</td><td>36.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.57 (+0.53%)</td><td>2.94 (+0.55%)</td><td>2.97 (+12.25%)</td><td>2.38 (+0.02%)</td><td>0.44 (-19.57%)</td><td>220.20 (+0.00%)</td><td>181.48 (-1.46%)</td><td>176.80 (-10.89%)</td><td>146.80 (-0.54%)</td><td>27.25 (-17.34%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.55 (n/a)</td><td>2.93 (n/a)</td><td>2.64 (n/a)</td><td>2.38 (n/a)</td><td>0.55 (n/a)</td><td>220.20 (n/a)</td><td>184.16 (n/a)</td><td>198.40 (n/a)</td><td>147.60 (n/a)</td><td>32.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>5.74 (-2.09%)</td><td>4.70 (-11.51%)</td><td>4.55 (-15.13%)</td><td>3.85 (-8.86%)</td><td>0.74 (+11.26%)</td><td>272.50 (+9.75%)</td><td>227.56 (+13.59%)</td><td>230.40 (+17.79%)</td><td>182.60 (+2.13%)</td><td>34.82 <b>(+23.13%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>5.87 (n/a)</td><td>5.31 (n/a)</td><td>5.36 (n/a)</td><td>4.22 (n/a)</td><td>0.66 (n/a)</td><td>248.30 (n/a)</td><td>200.34 (n/a)</td><td>195.60 (n/a)</td><td>178.80 (n/a)</td><td>28.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.68 <b>(+24.90%)</b></td><td>7.79 (+8.07%)</td><td>7.49 (+0.34%)</td><td>6.12 (+5.49%)</td><td>1.40 <b>(+74.54%)</b></td><td>342.50 (-5.20%)</td><td>276.14 (-6.15%)</td><td>280.10 (-0.36%)</td><td>216.70 (-19.95%)</td><td>49.23 <b>(+29.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.75 (n/a)</td><td>7.21 (n/a)</td><td>7.46 (n/a)</td><td>5.80 (n/a)</td><td>0.80 (n/a)</td><td>361.30 (n/a)</td><td>294.22 (n/a)</td><td>281.10 (n/a)</td><td>270.70 (n/a)</td><td>37.96 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.44 (-0.47%)</td><td>3.09 (+6.05%)</td><td>3.15 (+2.89%)</td><td>2.68 <b>(+40.27%)</b></td><td>0.33 <b>(-43.25%)</b></td><td>195.50 <b>(-28.70%)</b></td><td>171.14 (-8.77%)</td><td>166.30 (-2.81%)</td><td>152.60 (+0.53%)</td><td>18.84 <b>(-61.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.45 (n/a)</td><td>2.92 (n/a)</td><td>3.06 (n/a)</td><td>1.91 (n/a)</td><td>0.59 (n/a)</td><td>274.20 (n/a)</td><td>187.60 (n/a)</td><td>171.10 (n/a)</td><td>151.80 (n/a)</td><td>49.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.26 (-12.51%)</td><td>0.19 (-17.38%)</td><td>0.20 (-19.66%)</td><td>0.14 <b>(-21.59%)</b></td><td>0.05 (-5.36%)</td><td>239.00 <b>(+27.53%)</b></td><td>176.00 <b>(+22.22%)</b></td><td>161.70 <b>(+24.48%)</b></td><td>126.50 (+14.27%)</td><td>42.33 <b>(+37.39%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>187.40 (n/a)</td><td>144.00 (n/a)</td><td>129.90 (n/a)</td><td>110.70 (n/a)</td><td>30.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.23 <b>(+22.83%)</b></td><td>0.21 <b>(+22.01%)</b></td><td>0.22 <b>(+23.77%)</b></td><td>0.19 <b>(+36.39%)</b></td><td>0.02 (-3.62%)</td><td>169.70 <b>(-26.70%)</b></td><td>154.80 (-18.45%)</td><td>147.80 (-19.19%)</td><td>140.40 (-18.61%)</td><td>13.55 <b>(-42.87%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>189.82 (n/a)</td><td>182.90 (n/a)</td><td>172.50 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.53 (+15.19%)</td><td>0.45 (+17.21%)</td><td>0.50 <b>(+31.32%)</b></td><td>0.33 (+0.48%)</td><td>0.09 <b>(+92.83%)</b></td><td>197.00 (-0.51%)</td><td>149.40 (-12.64%)</td><td>131.20 <b>(-23.81%)</b></td><td>123.80 (-13.18%)</td><td>32.51 <b>(+65.35%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>198.00 (n/a)</td><td>171.02 (n/a)</td><td>172.20 (n/a)</td><td>142.60 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.49 (-7.85%)</td><td>0.43 (-1.86%)</td><td>0.41 (-3.60%)</td><td>0.39 (+7.04%)</td><td>0.04 <b>(-35.78%)</b></td><td>167.00 (-6.60%)</td><td>153.70 (+1.07%)</td><td>159.40 (+3.71%)</td><td>133.80 (+8.52%)</td><td>12.94 <b>(-34.52%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.06 (n/a)</td><td>178.80 (n/a)</td><td>152.08 (n/a)</td><td>153.70 (n/a)</td><td>123.30 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.46 (-10.56%)</td><td>0.39 (-4.88%)</td><td>0.39 (-0.48%)</td><td>0.31 (-9.89%)</td><td>0.06 (-6.86%)</td><td>211.40 (+10.97%)</td><td>172.00 (+5.29%)</td><td>169.40 (+0.47%)</td><td>143.50 (+11.85%)</td><td>27.65 (+16.04%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>190.50 (n/a)</td><td>163.36 (n/a)</td><td>168.60 (n/a)</td><td>128.30 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.05 (+2.05%)</td><td>0.84 (+7.48%)</td><td>0.78 (-1.26%)</td><td>0.70 <b>(+24.21%)</b></td><td>0.14 (-17.68%)</td><td>187.80 (-19.47%)</td><td>159.64 (-8.58%)</td><td>167.10 (+1.27%)</td><td>124.80 (-2.04%)</td><td>24.65 <b>(-36.11%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.03 (n/a)</td><td>0.78 (n/a)</td><td>0.79 (n/a)</td><td>0.56 (n/a)</td><td>0.17 (n/a)</td><td>233.20 (n/a)</td><td>174.62 (n/a)</td><td>165.00 (n/a)</td><td>127.40 (n/a)</td><td>38.58 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.03 <b>(+28.37%)</b></td><td>0.88 <b>(+22.54%)</b></td><td>0.91 <b>(+21.93%)</b></td><td>0.68 (+19.12%)</td><td>0.13 <b>(+30.21%)</b></td><td>192.20 (-16.07%)</td><td>151.54 (-18.22%)</td><td>143.30 (-18.02%)</td><td>127.80 <b>(-22.12%)</b></td><td>24.25 (-11.40%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.75 (n/a)</td><td>0.57 (n/a)</td><td>0.10 (n/a)</td><td>229.00 (n/a)</td><td>185.30 (n/a)</td><td>174.80 (n/a)</td><td>164.10 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.90 (+3.79%)</td><td>0.81 (+5.62%)</td><td>0.81 (+8.55%)</td><td>0.76 (+6.16%)</td><td>0.06 (-2.87%)</td><td>172.90 (-5.78%)</td><td>161.50 (-5.37%)</td><td>161.20 (-7.83%)</td><td>146.30 (-3.69%)</td><td>11.21 (-10.42%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.86 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.71 (n/a)</td><td>0.06 (n/a)</td><td>183.50 (n/a)</td><td>170.66 (n/a)</td><td>174.90 (n/a)</td><td>151.90 (n/a)</td><td>12.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.85 (+14.83%)</td><td>0.76 (+17.58%)</td><td>0.77 (+15.53%)</td><td>0.64 <b>(+29.41%)</b></td><td>0.08 (-16.24%)</td><td>204.70 <b>(-22.73%)</b></td><td>173.40 (-15.79%)</td><td>169.90 (-13.45%)</td><td>154.10 (-12.94%)</td><td>18.84 <b>(-44.57%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.74 (n/a)</td><td>0.65 (n/a)</td><td>0.67 (n/a)</td><td>0.49 (n/a)</td><td>0.09 (n/a)</td><td>264.90 (n/a)</td><td>205.92 (n/a)</td><td>196.30 (n/a)</td><td>177.00 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (+13.16%)</td><td>0.11 (+6.04%)</td><td>0.11 (+14.43%)</td><td>0.08 (-3.62%)</td><td>0.02 <b>(+56.37%)</b></td><td>210.90 (+3.74%)</td><td>157.28 (-3.47%)</td><td>144.40 (-12.59%)</td><td>121.50 (-11.64%)</td><td>37.39 <b>(+43.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.30 (n/a)</td><td>162.94 (n/a)</td><td>165.20 (n/a)</td><td>137.50 (n/a)</td><td>26.00 (n/a)</td>
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
