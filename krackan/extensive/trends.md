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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 <b>(-26.90%)</b></td><td>0.04 (-18.06%)</td><td>0.04 (-14.18%)</td><td>0.03 (-15.55%)</td><td>0.00 <b>(-59.91%)</b></td><td>193.00 (+18.40%)</td><td>169.78 <b>(+20.26%)</b></td><td>165.70 (+16.53%)</td><td>155.10 <b>(+36.77%)</b></td><td>14.16 <b>(-35.35%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>163.00 (n/a)</td><td>141.18 (n/a)</td><td>142.20 (n/a)</td><td>113.40 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (+2.79%)</td><td>0.04 (+14.05%)</td><td>0.04 (+14.77%)</td><td>0.03 <b>(+21.86%)</b></td><td>0.00 <b>(-28.45%)</b></td><td>175.60 (-17.94%)</td><td>156.26 (-13.45%)</td><td>156.80 (-12.84%)</td><td>133.70 (-2.69%)</td><td>16.80 <b>(-41.92%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>180.54 (n/a)</td><td>179.90 (n/a)</td><td>137.40 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (-18.32%)</td><td>0.03 (-5.68%)</td><td>0.03 (-2.71%)</td><td>0.03 (-5.57%)</td><td>0.00 <b>(-35.75%)</b></td><td>208.70 (+5.89%)</td><td>184.12 (+4.97%)</td><td>192.80 (+2.83%)</td><td>161.00 <b>(+22.43%)</b></td><td>21.73 (-17.27%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>175.40 (n/a)</td><td>187.50 (n/a)</td><td>131.50 (n/a)</td><td>26.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (-11.91%)</td><td>0.03 (-12.34%)</td><td>0.03 (-7.43%)</td><td>0.03 (-7.50%)</td><td>0.01 <b>(-28.94%)</b></td><td>212.80 (+8.08%)</td><td>190.22 (+12.76%)</td><td>193.90 (+8.08%)</td><td>147.00 (+13.51%)</td><td>26.78 (-14.47%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.90 (n/a)</td><td>168.70 (n/a)</td><td>179.40 (n/a)</td><td>129.50 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 <b>(-30.98%)</b></td><td>0.03 (-15.21%)</td><td>0.03 (-8.12%)</td><td>0.02 (-18.18%)</td><td>0.01 <b>(-43.05%)</b></td><td>275.90 <b>(+22.24%)</b></td><td>197.88 (+15.14%)</td><td>190.60 (+8.85%)</td><td>153.00 <b>(+44.89%)</b></td><td>47.60 (+7.75%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>225.70 (n/a)</td><td>171.86 (n/a)</td><td>175.10 (n/a)</td><td>105.60 (n/a)</td><td>44.18 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (-12.40%)</td><td>0.04 (-8.12%)</td><td>0.03 (-9.18%)</td><td>0.03 (+10.36%)</td><td>0.00 <b>(-36.67%)</b></td><td>197.60 (-9.40%)</td><td>172.60 (+6.64%)</td><td>175.80 (+10.08%)</td><td>144.90 (+14.09%)</td><td>23.11 <b>(-34.85%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>161.86 (n/a)</td><td>159.70 (n/a)</td><td>127.00 (n/a)</td><td>35.47 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-19.72%)</td><td>0.03 (-17.53%)</td><td>0.03 <b>(-21.16%)</b></td><td>0.03 (-5.95%)</td><td>0.00 <b>(-57.15%)</b></td><td>221.60 (+6.33%)</td><td>209.98 <b>(+20.24%)</b></td><td>214.50 <b>(+26.85%)</b></td><td>195.10 <b>(+24.58%)</b></td><td>12.25 <b>(-42.93%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>174.64 (n/a)</td><td>169.10 (n/a)</td><td>156.60 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 <b>(-31.14%)</b></td><td>0.03 (-19.50%)</td><td>0.03 (-17.94%)</td><td>0.03 (+2.72%)</td><td>0.01 <b>(-54.12%)</b></td><td>223.30 (-2.62%)</td><td>205.08 (+18.61%)</td><td>217.90 <b>(+21.87%)</b></td><td>150.60 <b>(+45.23%)</b></td><td>30.63 <b>(-32.43%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>172.90 (n/a)</td><td>178.80 (n/a)</td><td>103.70 (n/a)</td><td>45.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 <b>(-20.85%)</b></td><td>0.07 (-12.08%)</td><td>0.07 (-6.20%)</td><td>0.05 <b>(-21.51%)</b></td><td>0.02 (-10.41%)</td><td>246.50 <b>(+27.39%)</b></td><td>176.88 (+14.83%)</td><td>169.50 (+6.60%)</td><td>141.30 <b>(+26.27%)</b></td><td>43.26 <b>(+44.68%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>193.50 (n/a)</td><td>154.04 (n/a)</td><td>159.00 (n/a)</td><td>111.90 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (-16.43%)</td><td>0.06 <b>(-28.33%)</b></td><td>0.05 <b>(-32.14%)</b></td><td>0.03 <b>(-56.44%)</b></td><td>0.02 <b>(+197.70%)</b></td><td>380.90 <b>(+129.60%)</b></td><td>237.60 <b>(+52.72%)</b></td><td>232.20 <b>(+47.43%)</b></td><td>164.80 (+19.68%)</td><td>88.21 <b>(+695.51%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>165.90 (n/a)</td><td>155.58 (n/a)</td><td>157.50 (n/a)</td><td>137.70 (n/a)</td><td>11.09 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (+5.75%)</td><td>0.08 (+2.88%)</td><td>0.07 (+1.53%)</td><td>0.07 (+1.10%)</td><td>0.01 (+12.73%)</td><td>186.20 (-1.06%)</td><td>165.60 (-2.66%)</td><td>168.80 (-1.52%)</td><td>136.00 (-5.42%)</td><td>18.26 (+2.63%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>170.12 (n/a)</td><td>171.40 (n/a)</td><td>143.80 (n/a)</td><td>17.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 <b>(+28.70%)</b></td><td>0.08 <b>(+23.00%)</b></td><td>0.08 <b>(+29.65%)</b></td><td>0.07 (+14.22%)</td><td>0.01 <b>(+178.87%)</b></td><td>168.70 (-12.45%)</td><td>151.66 (-18.13%)</td><td>145.90 <b>(-22.89%)</b></td><td>135.00 <b>(-22.28%)</b></td><td>15.81 <b>(+93.37%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>192.70 (n/a)</td><td>185.24 (n/a)</td><td>189.20 (n/a)</td><td>173.70 (n/a)</td><td>8.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (-10.41%)</td><td>0.08 (-1.05%)</td><td>0.08 (+12.69%)</td><td>0.06 (+1.31%)</td><td>0.01 <b>(-26.89%)</b></td><td>213.70 (-1.29%)</td><td>167.54 (-0.65%)</td><td>158.80 (-11.28%)</td><td>131.30 (+11.65%)</td><td>31.40 (-17.26%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>168.64 (n/a)</td><td>179.00 (n/a)</td><td>117.60 (n/a)</td><td>37.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 <b>(+28.97%)</b></td><td>0.07 (+6.09%)</td><td>0.08 (+18.69%)</td><td>0.05 <b>(-22.59%)</b></td><td>0.02 <b>(+395.68%)</b></td><td>262.20 <b>(+29.16%)</b></td><td>188.24 (+2.95%)</td><td>154.80 (-15.73%)</td><td>132.90 <b>(-22.46%)</b></td><td>65.56 <b>(+408.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>203.00 (n/a)</td><td>182.84 (n/a)</td><td>183.70 (n/a)</td><td>171.40 (n/a)</td><td>12.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 <b>(+41.10%)</b></td><td>0.07 <b>(+22.87%)</b></td><td>0.07 (+17.81%)</td><td>0.05 (-6.50%)</td><td>0.02 <b>(+223.38%)</b></td><td>242.20 (+6.98%)</td><td>177.66 (-14.14%)</td><td>177.30 (-15.13%)</td><td>124.20 <b>(-29.15%)</b></td><td>48.85 <b>(+143.08%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.40 (n/a)</td><td>206.92 (n/a)</td><td>208.90 (n/a)</td><td>175.30 (n/a)</td><td>20.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 <b>(+27.29%)</b></td><td>0.07 (+5.00%)</td><td>0.07 (+9.03%)</td><td>0.04 <b>(-26.93%)</b></td><td>0.02 <b>(+174.54%)</b></td><td>316.40 <b>(+36.85%)</b></td><td>195.38 (+2.41%)</td><td>168.00 (-8.30%)</td><td>137.40 <b>(-21.44%)</b></td><td>71.14 <b>(+205.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>190.78 (n/a)</td><td>183.20 (n/a)</td><td>174.90 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 <b>(+21.57%)</b></td><td>0.14 (+0.94%)</td><td>0.14 (-1.46%)</td><td>0.11 (-11.20%)</td><td>0.03 <b>(+120.94%)</b></td><td>231.00 (+12.57%)</td><td>177.68 (+1.83%)</td><td>175.30 (+1.51%)</td><td>127.90 (-17.70%)</td><td>37.01 <b>(+98.13%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>174.48 (n/a)</td><td>172.70 (n/a)</td><td>155.40 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (-3.67%)</td><td>0.15 (+3.03%)</td><td>0.16 (+7.92%)</td><td>0.12 (+14.60%)</td><td>0.02 (-19.34%)</td><td>204.30 (-12.73%)</td><td>168.46 (-4.08%)</td><td>157.10 (-7.32%)</td><td>149.00 (+3.83%)</td><td>24.39 <b>(-30.08%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>234.10 (n/a)</td><td>175.62 (n/a)</td><td>169.50 (n/a)</td><td>143.50 (n/a)</td><td>34.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (-3.37%)</td><td>0.16 (+1.64%)</td><td>0.17 (+13.05%)</td><td>0.12 (+6.36%)</td><td>0.03 <b>(-27.18%)</b></td><td>205.00 (-5.96%)</td><td>160.44 (-3.48%)</td><td>148.90 (-11.53%)</td><td>132.90 (+3.50%)</td><td>28.80 <b>(-25.17%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>218.00 (n/a)</td><td>166.22 (n/a)</td><td>168.30 (n/a)</td><td>128.40 (n/a)</td><td>38.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (+5.72%)</td><td>0.14 (-5.93%)</td><td>0.13 (-15.42%)</td><td>0.11 (-6.46%)</td><td>0.03 <b>(+22.27%)</b></td><td>230.10 (+6.92%)</td><td>183.60 (+7.39%)</td><td>186.10 (+18.23%)</td><td>133.20 (-5.40%)</td><td>35.75 <b>(+20.12%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>215.20 (n/a)</td><td>170.96 (n/a)</td><td>157.40 (n/a)</td><td>140.80 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (-9.29%)</td><td>0.16 (+9.78%)</td><td>0.15 (+8.29%)</td><td>0.11 (+5.38%)</td><td>0.03 <b>(-21.98%)</b></td><td>216.40 (-5.09%)</td><td>161.28 (-10.44%)</td><td>163.10 (-7.64%)</td><td>129.50 (+10.21%)</td><td>34.68 (-16.36%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>228.00 (n/a)</td><td>180.08 (n/a)</td><td>176.60 (n/a)</td><td>117.50 (n/a)</td><td>41.47 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (+0.77%)</td><td>0.16 (+13.95%)</td><td>0.16 <b>(+26.10%)</b></td><td>0.12 (+8.75%)</td><td>0.03 (-11.64%)</td><td>206.60 (-8.06%)</td><td>154.26 (-13.28%)</td><td>152.20 <b>(-20.69%)</b></td><td>127.90 (-0.78%)</td><td>32.04 (-18.79%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>224.70 (n/a)</td><td>177.88 (n/a)</td><td>191.90 (n/a)</td><td>128.90 (n/a)</td><td>39.45 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 <b>(+26.94%)</b></td><td>0.14 (+5.29%)</td><td>0.13 (-3.25%)</td><td>0.12 (+4.92%)</td><td>0.03 <b>(+121.62%)</b></td><td>213.20 (-4.69%)</td><td>185.62 (-2.91%)</td><td>195.70 (+3.38%)</td><td>132.70 <b>(-21.20%)</b></td><td>33.26 <b>(+63.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>191.18 (n/a)</td><td>189.30 (n/a)</td><td>168.40 (n/a)</td><td>20.36 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (+13.27%)</td><td>0.13 (+13.66%)</td><td>0.13 (+16.01%)</td><td>0.12 <b>(+21.17%)</b></td><td>0.01 <b>(-25.79%)</b></td><td>203.10 (-17.47%)</td><td>186.10 (-12.96%)</td><td>187.60 (-13.79%)</td><td>158.50 (-11.70%)</td><td>16.79 <b>(-46.76%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>246.10 (n/a)</td><td>213.80 (n/a)</td><td>217.60 (n/a)</td><td>179.50 (n/a)</td><td>31.53 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.38 (+7.70%)</td><td>0.27 (-14.15%)</td><td>0.26 <b>(-23.95%)</b></td><td>0.19 <b>(-27.20%)</b></td><td>0.07 <b>(+74.15%)</b></td><td>258.40 <b>(+37.37%)</b></td><td>188.26 <b>(+20.85%)</b></td><td>189.00 <b>(+31.52%)</b></td><td>129.80 (-7.15%)</td><td>47.10 <b>(+123.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>188.10 (n/a)</td><td>155.78 (n/a)</td><td>143.70 (n/a)</td><td>139.80 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.39 (-12.44%)</td><td>0.32 (+1.03%)</td><td>0.29 (+2.91%)</td><td>0.25 (-2.15%)</td><td>0.06 <b>(-23.44%)</b></td><td>200.10 (+2.20%)</td><td>159.94 (-2.20%)</td><td>169.40 (-2.81%)</td><td>125.00 (+14.26%)</td><td>30.18 (-8.69%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>195.80 (n/a)</td><td>163.54 (n/a)</td><td>174.30 (n/a)</td><td>109.40 (n/a)</td><td>33.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.38 (+5.69%)</td><td>0.28 (-1.68%)</td><td>0.26 (-0.62%)</td><td>0.21 (-7.47%)</td><td>0.07 <b>(+34.19%)</b></td><td>233.50 (+8.05%)</td><td>187.00 (+4.16%)</td><td>190.10 (+0.64%)</td><td>129.30 (-5.41%)</td><td>45.37 <b>(+41.50%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>216.10 (n/a)</td><td>179.54 (n/a)</td><td>188.90 (n/a)</td><td>136.70 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.39 (+4.40%)</td><td>0.28 (-17.67%)</td><td>0.27 <b>(-20.66%)</b></td><td>0.19 <b>(-28.96%)</b></td><td>0.07 <b>(+86.51%)</b></td><td>255.70 <b>(+40.73%)</b></td><td>188.00 <b>(+26.74%)</b></td><td>180.50 <b>(+26.05%)</b></td><td>125.10 (-4.21%)</td><td>48.17 <b>(+143.17%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>181.70 (n/a)</td><td>148.34 (n/a)</td><td>143.20 (n/a)</td><td>130.60 (n/a)</td><td>19.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.39 <b>(+27.56%)</b></td><td>0.32 <b>(+21.76%)</b></td><td>0.29 (+16.18%)</td><td>0.25 (+12.02%)</td><td>0.06 <b>(+106.30%)</b></td><td>196.90 (-10.70%)</td><td>160.68 (-16.19%)</td><td>169.40 (-13.92%)</td><td>127.00 <b>(-21.60%)</b></td><td>30.91 <b>(+41.04%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>220.50 (n/a)</td><td>191.72 (n/a)</td><td>196.80 (n/a)</td><td>162.00 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.41 <b>(+51.50%)</b></td><td>0.30 <b>(+24.74%)</b></td><td>0.28 (+10.80%)</td><td>0.23 <b>(+24.63%)</b></td><td>0.07 <b>(+108.34%)</b></td><td>211.80 (-19.74%)</td><td>168.56 (-18.06%)</td><td>177.80 (-9.75%)</td><td>118.70 <b>(-33.98%)</b></td><td>35.95 (+6.32%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>263.90 (n/a)</td><td>205.72 (n/a)</td><td>197.00 (n/a)</td><td>179.80 (n/a)</td><td>33.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.35 <b>(+26.73%)</b></td><td>0.27 (+6.08%)</td><td>0.28 (+8.18%)</td><td>0.17 <b>(-25.40%)</b></td><td>0.07 <b>(+269.27%)</b></td><td>282.20 <b>(+34.06%)</b></td><td>194.40 (-0.54%)</td><td>177.00 (-7.52%)</td><td>141.20 <b>(-21.12%)</b></td><td>55.43 <b>(+292.51%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>210.50 (n/a)</td><td>195.46 (n/a)</td><td>191.40 (n/a)</td><td>179.00 (n/a)</td><td>14.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.31 (-14.39%)</td><td>0.27 (-8.94%)</td><td>0.27 (-8.18%)</td><td>0.23 (-2.74%)</td><td>0.03 <b>(-32.19%)</b></td><td>211.30 (+2.82%)</td><td>183.64 (+8.93%)</td><td>181.80 (+8.93%)</td><td>157.30 (+16.78%)</td><td>20.78 (-18.15%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>205.50 (n/a)</td><td>168.58 (n/a)</td><td>166.90 (n/a)</td><td>134.70 (n/a)</td><td>25.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (+0.26%)</td><td>0.01 (-4.12%)</td><td>0.01 (-10.08%)</td><td>0.01 <b>(+26.61%)</b></td><td>0.00 <b>(-38.27%)</b></td><td>197.60 <b>(-20.99%)</b></td><td>180.50 (+1.71%)</td><td>182.50 (+11.21%)</td><td>148.50 (-0.27%)</td><td>19.75 <b>(-52.68%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>250.10 (n/a)</td><td>177.46 (n/a)</td><td>164.10 (n/a)</td><td>148.90 (n/a)</td><td>41.74 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (+9.30%)</td><td>0.02 (-5.93%)</td><td>0.01 (-9.40%)</td><td>0.01 <b>(-25.44%)</b></td><td>0.00 <b>(+69.37%)</b></td><td>269.30 <b>(+34.11%)</b></td><td>184.28 (+11.66%)</td><td>185.60 (+10.34%)</td><td>117.90 (-8.53%)</td><td>55.00 <b>(+110.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>200.80 (n/a)</td><td>165.04 (n/a)</td><td>168.20 (n/a)</td><td>128.90 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (-4.46%)</td><td>0.01 (-16.87%)</td><td>0.01 <b>(-20.63%)</b></td><td>0.01 <b>(-27.65%)</b></td><td>0.00 <b>(+57.18%)</b></td><td>275.70 <b>(+38.26%)</b></td><td>204.26 <b>(+24.06%)</b></td><td>206.40 <b>(+25.93%)</b></td><td>149.10 (+4.71%)</td><td>48.27 <b>(+123.61%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>199.40 (n/a)</td><td>164.64 (n/a)</td><td>163.90 (n/a)</td><td>142.40 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (-13.99%)</td><td>0.01 (-2.33%)</td><td>0.01 (-1.95%)</td><td>0.01 <b>(+33.60%)</b></td><td>0.00 <b>(-75.73%)</b></td><td>193.60 <b>(-25.16%)</b></td><td>184.26 (-2.20%)</td><td>187.40 (+1.96%)</td><td>166.90 (+16.23%)</td><td>10.19 <b>(-78.58%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>258.70 (n/a)</td><td>188.40 (n/a)</td><td>183.80 (n/a)</td><td>143.60 (n/a)</td><td>47.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (-11.50%)</td><td>0.01 (-14.74%)</td><td>0.01 <b>(-21.16%)</b></td><td>0.01 (+0.19%)</td><td>0.00 (-13.33%)</td><td>230.30 (-0.22%)</td><td>202.88 (+16.61%)</td><td>218.70 <b>(+26.86%)</b></td><td>139.60 (+13.04%)</td><td>36.81 (-3.96%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>230.80 (n/a)</td><td>173.98 (n/a)</td><td>172.40 (n/a)</td><td>123.50 (n/a)</td><td>38.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (-2.36%)</td><td>0.01 (-7.90%)</td><td>0.01 (-12.17%)</td><td>0.01 (-0.32%)</td><td>0.00 (-0.91%)</td><td>236.50 (+0.34%)</td><td>203.02 (+8.51%)</td><td>209.60 (+13.85%)</td><td>147.90 (+2.35%)</td><td>33.35 (-1.83%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>235.70 (n/a)</td><td>187.10 (n/a)</td><td>184.10 (n/a)</td><td>144.50 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (-17.09%)</td><td>0.01 <b>(-20.78%)</b></td><td>0.01 <b>(-23.60%)</b></td><td>0.01 (-15.20%)</td><td>0.00 <b>(-21.90%)</b></td><td>253.40 (+17.97%)</td><td>217.68 <b>(+25.78%)</b></td><td>226.40 <b>(+30.94%)</b></td><td>164.70 <b>(+20.66%)</b></td><td>33.73 (+8.98%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>214.80 (n/a)</td><td>173.06 (n/a)</td><td>172.90 (n/a)</td><td>136.50 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.01 (-18.84%)</td><td>0.01 (-16.33%)</td><td>0.01 (-14.46%)</td><td>0.01 <b>(-27.11%)</b></td><td>0.00 (-7.54%)</td><td>341.00 <b>(+37.17%)</b></td><td>241.80 <b>(+20.96%)</b></td><td>225.60 (+16.89%)</td><td>195.90 <b>(+23.21%)</b></td><td>56.92 <b>(+63.48%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>248.60 (n/a)</td><td>199.90 (n/a)</td><td>193.00 (n/a)</td><td>159.00 (n/a)</td><td>34.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-12.33%)</td><td>0.03 (+0.58%)</td><td>0.03 (+1.81%)</td><td>0.03 (+4.05%)</td><td>0.00 <b>(-38.36%)</b></td><td>201.70 (-3.91%)</td><td>172.74 (-1.82%)</td><td>175.30 (-1.74%)</td><td>153.70 (+14.02%)</td><td>19.12 <b>(-31.52%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>175.94 (n/a)</td><td>178.40 (n/a)</td><td>134.80 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 <b>(-34.93%)</b></td><td>0.03 (-10.62%)</td><td>0.03 (-11.32%)</td><td>0.02 <b>(+42.69%)</b></td><td>0.01 <b>(-56.27%)</b></td><td>228.70 <b>(-29.93%)</b></td><td>190.68 (-1.38%)</td><td>207.20 (+12.73%)</td><td>142.80 <b>(+53.71%)</b></td><td>41.17 <b>(-52.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>326.40 (n/a)</td><td>193.34 (n/a)</td><td>183.80 (n/a)</td><td>92.90 (n/a)</td><td>86.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-8.10%)</td><td>0.03 (-3.28%)</td><td>0.03 (-2.58%)</td><td>0.03 (-6.83%)</td><td>0.00 (-1.31%)</td><td>208.40 (+7.37%)</td><td>179.66 (+3.53%)</td><td>172.60 (+2.62%)</td><td>158.20 (+8.80%)</td><td>22.92 (+13.21%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.10 (n/a)</td><td>173.54 (n/a)</td><td>168.20 (n/a)</td><td>145.40 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 <b>(-20.27%)</b></td><td>0.03 (-12.22%)</td><td>0.03 (-6.38%)</td><td>0.02 <b>(-31.17%)</b></td><td>0.01 (-9.60%)</td><td>312.50 <b>(+45.28%)</b></td><td>198.84 (+16.87%)</td><td>178.90 (+6.81%)</td><td>143.40 <b>(+25.35%)</b></td><td>66.86 <b>(+75.07%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>170.14 (n/a)</td><td>167.50 (n/a)</td><td>114.40 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 <b>(-23.62%)</b></td><td>0.03 (-7.39%)</td><td>0.03 (+5.01%)</td><td>0.02 (-4.77%)</td><td>0.00 <b>(-49.66%)</b></td><td>223.60 (+5.03%)</td><td>184.26 (+5.10%)</td><td>176.30 (-4.75%)</td><td>153.10 <b>(+30.97%)</b></td><td>26.50 <b>(-27.50%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>175.32 (n/a)</td><td>185.10 (n/a)</td><td>116.90 (n/a)</td><td>36.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+11.20%)</td><td>0.03 (+8.48%)</td><td>0.03 (+13.12%)</td><td>0.02 (-5.07%)</td><td>0.00 <b>(+51.13%)</b></td><td>234.80 (+5.34%)</td><td>188.84 (-6.77%)</td><td>190.20 (-11.58%)</td><td>155.60 (-10.06%)</td><td>31.29 <b>(+41.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.90 (n/a)</td><td>202.56 (n/a)</td><td>215.10 (n/a)</td><td>173.00 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 <b>(+29.73%)</b></td><td>0.03 (+12.13%)</td><td>0.03 (+6.67%)</td><td>0.02 (-6.72%)</td><td>0.01 <b>(+150.13%)</b></td><td>252.60 (+7.17%)</td><td>186.94 (-8.25%)</td><td>186.90 (-6.27%)</td><td>143.20 <b>(-22.89%)</b></td><td>41.14 <b>(+108.49%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.70 (n/a)</td><td>203.74 (n/a)</td><td>199.40 (n/a)</td><td>185.70 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-8.55%)</td><td>0.02 (-6.27%)</td><td>0.02 (-0.50%)</td><td>0.02 (+2.48%)</td><td>0.00 <b>(-35.46%)</b></td><td>263.60 (-2.41%)</td><td>228.64 (+5.08%)</td><td>228.60 (+0.53%)</td><td>188.10 (+9.36%)</td><td>28.03 <b>(-30.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.10 (n/a)</td><td>217.58 (n/a)</td><td>227.40 (n/a)</td><td>172.00 (n/a)</td><td>40.24 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 <b>(+30.75%)</b></td><td>0.06 (+15.92%)</td><td>0.05 (-2.06%)</td><td>0.05 <b>(+49.62%)</b></td><td>0.01 <b>(+21.69%)</b></td><td>221.30 <b>(-33.18%)</b></td><td>183.64 (-15.06%)</td><td>202.80 (+2.06%)</td><td>127.20 <b>(-23.51%)</b></td><td>39.64 <b>(-40.24%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>331.20 (n/a)</td><td>216.20 (n/a)</td><td>198.70 (n/a)</td><td>166.30 (n/a)</td><td>66.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 <b>(+38.96%)</b></td><td>0.06 <b>(+23.48%)</b></td><td>0.06 (+17.24%)</td><td>0.04 (-10.56%)</td><td>0.02 <b>(+134.78%)</b></td><td>262.90 (+11.82%)</td><td>174.90 (-14.40%)</td><td>175.70 (-14.71%)</td><td>124.50 <b>(-28.03%)</b></td><td>55.76 <b>(+84.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>235.10 (n/a)</td><td>204.32 (n/a)</td><td>206.00 (n/a)</td><td>173.00 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (+13.77%)</td><td>0.06 (+8.14%)</td><td>0.06 (+8.06%)</td><td>0.05 (-1.90%)</td><td>0.01 <b>(+53.54%)</b></td><td>216.80 (+1.93%)</td><td>167.74 (-5.94%)</td><td>167.60 (-7.45%)</td><td>129.10 (-12.12%)</td><td>34.24 <b>(+37.50%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>178.34 (n/a)</td><td>181.10 (n/a)</td><td>146.90 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 <b>(+24.26%)</b></td><td>0.07 (+9.21%)</td><td>0.06 (-3.62%)</td><td>0.05 (-7.49%)</td><td>0.02 <b>(+108.57%)</b></td><td>222.10 (+8.13%)</td><td>169.52 (-4.97%)</td><td>172.00 (+3.74%)</td><td>122.60 (-19.50%)</td><td>42.40 <b>(+73.48%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>178.38 (n/a)</td><td>165.80 (n/a)</td><td>152.30 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 <b>(+22.33%)</b></td><td>0.06 (+2.89%)</td><td>0.05 (-12.50%)</td><td>0.05 (-7.22%)</td><td>0.01 <b>(+185.28%)</b></td><td>211.20 (+7.81%)</td><td>175.84 (+0.79%)</td><td>193.60 (+14.29%)</td><td>131.70 (-18.25%)</td><td>38.68 <b>(+151.70%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>174.46 (n/a)</td><td>169.40 (n/a)</td><td>161.10 (n/a)</td><td>15.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-19.83%)</td><td>0.05 <b>(-23.80%)</b></td><td>0.05 <b>(-22.01%)</b></td><td>0.03 <b>(-37.88%)</b></td><td>0.01 <b>(+33.20%)</b></td><td>318.60 <b>(+60.99%)</b></td><td>232.10 <b>(+35.54%)</b></td><td>222.80 <b>(+28.19%)</b></td><td>174.10 <b>(+24.71%)</b></td><td>57.12 <b>(+173.14%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>171.24 (n/a)</td><td>173.80 (n/a)</td><td>139.60 (n/a)</td><td>20.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (-11.86%)</td><td>0.06 (-11.04%)</td><td>0.06 (-9.17%)</td><td>0.04 (-13.61%)</td><td>0.01 (-18.30%)</td><td>252.20 (+15.74%)</td><td>194.40 (+11.83%)</td><td>189.90 (+10.09%)</td><td>144.30 (+13.44%)</td><td>39.24 (+6.54%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>173.84 (n/a)</td><td>172.50 (n/a)</td><td>127.20 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (-3.80%)</td><td>0.05 (-8.41%)</td><td>0.05 (-6.65%)</td><td>0.04 (-15.21%)</td><td>0.01 (+7.60%)</td><td>274.10 (+17.94%)</td><td>217.32 (+10.21%)</td><td>221.80 (+7.10%)</td><td>153.10 (+4.01%)</td><td>43.00 <b>(+28.87%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.40 (n/a)</td><td>197.18 (n/a)</td><td>207.10 (n/a)</td><td>147.20 (n/a)</td><td>33.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (+7.24%)</td><td>0.12 (-9.23%)</td><td>0.12 (-15.34%)</td><td>0.11 (-11.61%)</td><td>0.02 <b>(+122.98%)</b></td><td>193.80 (+13.13%)</td><td>172.78 (+11.89%)</td><td>178.10 (+18.18%)</td><td>132.90 (-6.74%)</td><td>24.94 <b>(+132.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>171.30 (n/a)</td><td>154.42 (n/a)</td><td>150.70 (n/a)</td><td>142.50 (n/a)</td><td>10.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (+13.15%)</td><td>0.13 <b>(+34.99%)</b></td><td>0.14 <b>(+53.43%)</b></td><td>0.09 <b>(+25.52%)</b></td><td>0.02 (-3.42%)</td><td>230.70 <b>(-20.34%)</b></td><td>166.28 <b>(-26.86%)</b></td><td>154.00 <b>(-34.80%)</b></td><td>133.10 (-11.62%)</td><td>37.61 <b>(-25.85%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>289.60 (n/a)</td><td>227.36 (n/a)</td><td>236.20 (n/a)</td><td>150.60 (n/a)</td><td>50.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (+3.09%)</td><td>0.13 (+1.14%)</td><td>0.12 (+0.17%)</td><td>0.10 (+14.89%)</td><td>0.02 (+0.43%)</td><td>202.20 (-12.96%)</td><td>171.26 (-1.54%)</td><td>171.00 (-0.18%)</td><td>135.00 (-3.02%)</td><td>30.23 (-15.24%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>232.30 (n/a)</td><td>173.94 (n/a)</td><td>171.30 (n/a)</td><td>139.20 (n/a)</td><td>35.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (-0.77%)</td><td>0.11 (-6.43%)</td><td>0.12 (-7.07%)</td><td>0.09 (-1.84%)</td><td>0.01 (+2.83%)</td><td>222.80 (+1.87%)</td><td>193.52 (+7.05%)</td><td>180.20 (+7.58%)</td><td>163.60 (+0.80%)</td><td>26.78 (+9.82%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>180.78 (n/a)</td><td>167.50 (n/a)</td><td>162.30 (n/a)</td><td>24.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (-11.12%)</td><td>0.13 (-15.43%)</td><td>0.11 <b>(-28.17%)</b></td><td>0.09 (-18.45%)</td><td>0.04 (+0.40%)</td><td>234.10 <b>(+22.63%)</b></td><td>177.36 <b>(+20.31%)</b></td><td>184.10 <b>(+39.26%)</b></td><td>116.90 (+12.51%)</td><td>50.89 <b>(+31.95%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>190.90 (n/a)</td><td>147.42 (n/a)</td><td>132.20 (n/a)</td><td>103.90 (n/a)</td><td>38.57 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (+2.03%)</td><td>0.11 (-11.12%)</td><td>0.10 (-14.63%)</td><td>0.07 <b>(-32.43%)</b></td><td>0.03 <b>(+71.86%)</b></td><td>307.60 <b>(+47.96%)</b></td><td>211.44 (+19.74%)</td><td>212.80 (+17.12%)</td><td>135.80 (-1.95%)</td><td>67.69 <b>(+147.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>207.90 (n/a)</td><td>176.58 (n/a)</td><td>181.70 (n/a)</td><td>138.50 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (-12.37%)</td><td>0.11 (-17.87%)</td><td>0.11 (-12.01%)</td><td>0.06 <b>(-41.37%)</b></td><td>0.03 <b>(+34.06%)</b></td><td>327.20 <b>(+70.59%)</b></td><td>214.24 <b>(+28.03%)</b></td><td>193.80 (+13.67%)</td><td>147.80 (+14.13%)</td><td>68.80 <b>(+168.81%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>191.80 (n/a)</td><td>167.34 (n/a)</td><td>170.50 (n/a)</td><td>129.50 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (+17.25%)</td><td>0.10 (+2.71%)</td><td>0.09 (-12.96%)</td><td>0.08 (-11.54%)</td><td>0.03 <b>(+110.44%)</b></td><td>267.10 (+13.03%)</td><td>213.46 (+0.80%)</td><td>237.20 (+14.92%)</td><td>150.90 (-14.70%)</td><td>48.68 <b>(+97.72%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>211.76 (n/a)</td><td>206.40 (n/a)</td><td>176.90 (n/a)</td><td>24.62 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>163.98 (n/a)</td><td>160.40 (n/a)</td><td>124.80 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>168.62 (n/a)</td><td>164.10 (n/a)</td><td>139.70 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>172.20 (n/a)</td><td>144.06 (n/a)</td><td>143.80 (n/a)</td><td>111.60 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.30 (n/a)</td><td>166.58 (n/a)</td><td>167.50 (n/a)</td><td>108.80 (n/a)</td><td>44.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>171.26 (n/a)</td><td>186.60 (n/a)</td><td>129.80 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>184.42 (n/a)</td><td>176.10 (n/a)</td><td>161.40 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>182.36 (n/a)</td><td>165.80 (n/a)</td><td>143.40 (n/a)</td><td>38.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>248.60 (n/a)</td><td>198.58 (n/a)</td><td>204.00 (n/a)</td><td>156.20 (n/a)</td><td>39.47 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>187.30 (n/a)</td><td>161.66 (n/a)</td><td>166.10 (n/a)</td><td>128.80 (n/a)</td><td>21.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>177.90 (n/a)</td><td>160.00 (n/a)</td><td>171.10 (n/a)</td><td>126.30 (n/a)</td><td>20.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.30 (n/a)</td><td>162.22 (n/a)</td><td>156.90 (n/a)</td><td>119.60 (n/a)</td><td>32.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>224.70 (n/a)</td><td>187.46 (n/a)</td><td>175.10 (n/a)</td><td>140.90 (n/a)</td><td>35.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.37 (-6.10%)</td><td>0.32 (+9.65%)</td><td>0.32 (+18.87%)</td><td>0.27 (+11.00%)</td><td>0.04 <b>(-34.74%)</b></td><td>184.10 (-9.89%)</td><td>154.26 (-10.38%)</td><td>155.80 (-15.83%)</td><td>133.30 (+6.47%)</td><td>19.85 <b>(-36.58%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>204.30 (n/a)</td><td>172.12 (n/a)</td><td>185.10 (n/a)</td><td>125.20 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.09 (n/a)</td><td>204.60 (n/a)</td><td>160.14 (n/a)</td><td>163.10 (n/a)</td><td>105.00 (n/a)</td><td>37.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.44 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>186.10 (n/a)</td><td>164.34 (n/a)</td><td>180.00 (n/a)</td><td>112.00 (n/a)</td><td>31.40 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.03 (n/a)</td><td>165.90 (n/a)</td><td>155.90 (n/a)</td><td>161.20 (n/a)</td><td>135.60 (n/a)</td><td>12.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>172.44 (n/a)</td><td>164.40 (n/a)</td><td>150.40 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>160.94 (n/a)</td><td>156.80 (n/a)</td><td>137.00 (n/a)</td><td>26.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>207.50 (n/a)</td><td>185.76 (n/a)</td><td>187.00 (n/a)</td><td>161.80 (n/a)</td><td>17.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>294.40 (n/a)</td><td>216.16 (n/a)</td><td>189.30 (n/a)</td><td>163.80 (n/a)</td><td>53.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>369.20 (n/a)</td><td>255.82 (n/a)</td><td>192.00 (n/a)</td><td>174.40 (n/a)</td><td>103.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>165.76 (n/a)</td><td>165.50 (n/a)</td><td>144.50 (n/a)</td><td>14.57 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>182.62 (n/a)</td><td>176.60 (n/a)</td><td>156.50 (n/a)</td><td>23.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>269.20 (n/a)</td><td>195.42 (n/a)</td><td>182.70 (n/a)</td><td>150.70 (n/a)</td><td>44.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>188.30 (n/a)</td><td>165.04 (n/a)</td><td>160.60 (n/a)</td><td>142.80 (n/a)</td><td>18.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.10 (n/a)</td><td>164.98 (n/a)</td><td>162.70 (n/a)</td><td>133.10 (n/a)</td><td>27.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>233.40 (n/a)</td><td>164.12 (n/a)</td><td>154.30 (n/a)</td><td>117.90 (n/a)</td><td>42.53 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>350.70 (n/a)</td><td>218.28 (n/a)</td><td>179.60 (n/a)</td><td>163.00 (n/a)</td><td>77.09 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>215.30 (n/a)</td><td>177.14 (n/a)</td><td>174.60 (n/a)</td><td>155.40 (n/a)</td><td>22.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>207.80 (n/a)</td><td>176.68 (n/a)</td><td>187.60 (n/a)</td><td>138.20 (n/a)</td><td>27.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>252.30 (n/a)</td><td>202.76 (n/a)</td><td>181.00 (n/a)</td><td>166.80 (n/a)</td><td>39.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.61 (+1.58%)</td><td>13.41 (-1.51%)</td><td>13.13 (-0.61%)</td><td>13.04 (-0.09%)</td><td>0.67 (-2.10%)</td><td>4270.80 (+0.09%)</td><td>4161.04 (+1.52%)</td><td>4243.70 (+0.61%)</td><td>3813.70 (-1.56%)</td><td>195.01 (-3.66%)</td><td>14077.29 (+1.58%)</td><td>12926.46 (-1.51%)</td><td>12650.93 (-0.61%)</td><td>12570.71 (-0.09%)</td><td>645.57 (-2.10%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>14.38 (n/a)</td><td>13.62 (n/a)</td><td>13.21 (n/a)</td><td>13.06 (n/a)</td><td>0.68 (n/a)</td><td>4267.00 (n/a)</td><td>4098.74 (n/a)</td><td>4217.80 (n/a)</td><td>3874.00 (n/a)</td><td>202.41 (n/a)</td><td>13858.35 (n/a)</td><td>13124.49 (n/a)</td><td>12728.63 (n/a)</td><td>12582.04 (n/a)</td><td>659.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>15.14 (-9.80%)</td><td>14.32 (+3.16%)</td><td>14.54 (+1.83%)</td><td>12.91 <b>(+35.79%)</b></td><td>0.84 <b>(-68.97%)</b></td><td>1015.50 <b>(-26.35%)</b></td><td>918.14 (-6.32%)</td><td>901.40 (-1.80%)</td><td>865.50 (+10.86%)</td><td>56.99 <b>(-75.44%)</b></td><td>9924.97 (-9.80%)</td><td>9383.19 (+3.16%)</td><td>9529.50 (+1.83%)</td><td>8459.22 <b>(+35.79%)</b></td><td>548.70 <b>(-68.97%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>16.79 (n/a)</td><td>13.88 (n/a)</td><td>14.28 (n/a)</td><td>9.51 (n/a)</td><td>2.70 (n/a)</td><td>1378.90 (n/a)</td><td>980.06 (n/a)</td><td>917.90 (n/a)</td><td>780.70 (n/a)</td><td>232.03 (n/a)</td><td>11002.71 (n/a)</td><td>9095.52 (n/a)</td><td>9358.24 (n/a)</td><td>6229.62 (n/a)</td><td>1768.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.13 (-1.89%)</td><td>13.34 (-0.18%)</td><td>13.12 (+0.04%)</td><td>12.73 (+0.88%)</td><td>0.62 <b>(-22.88%)</b></td><td>4377.10 (-0.87%)</td><td>4183.46 (+0.07%)</td><td>4246.40 (-0.04%)</td><td>3941.50 (+1.93%)</td><td>191.16 <b>(-22.39%)</b></td><td>13621.08 (-1.89%)</td><td>12854.91 (-0.18%)</td><td>12642.99 (+0.04%)</td><td>12265.37 (+0.88%)</td><td>595.30 <b>(-22.88%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>14.41 (n/a)</td><td>13.36 (n/a)</td><td>13.11 (n/a)</td><td>12.62 (n/a)</td><td>0.80 (n/a)</td><td>4415.60 (n/a)</td><td>4180.70 (n/a)</td><td>4248.20 (n/a)</td><td>3866.90 (n/a)</td><td>246.30 (n/a)</td><td>13883.66 (n/a)</td><td>12878.02 (n/a)</td><td>12637.62 (n/a)</td><td>12158.57 (n/a)</td><td>771.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>16.39 (-1.63%)</td><td>14.66 (-3.31%)</td><td>15.30 (+1.09%)</td><td>10.69 <b>(-22.49%)</b></td><td>2.27 <b>(+123.51%)</b></td><td>1670.10 <b>(+29.02%)</b></td><td>1247.44 (+5.56%)</td><td>1167.50 (-1.08%)</td><td>1089.50 (+1.66%)</td><td>238.78 <b>(+203.01%)</b></td><td>12318.94 (-1.63%)</td><td>11020.21 (-3.31%)</td><td>11496.54 (+1.09%)</td><td>8036.47 <b>(-22.49%)</b></td><td>1706.60 <b>(+123.51%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>16.66 (n/a)</td><td>15.17 (n/a)</td><td>15.13 (n/a)</td><td>13.80 (n/a)</td><td>1.02 (n/a)</td><td>1294.50 (n/a)</td><td>1181.76 (n/a)</td><td>1180.20 (n/a)</td><td>1071.70 (n/a)</td><td>78.80 (n/a)</td><td>12523.43 (n/a)</td><td>11397.81 (n/a)</td><td>11372.49 (n/a)</td><td>10367.95 (n/a)</td><td>763.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.71 (-3.35%)</td><td>10.47 (-2.52%)</td><td>10.61 (-0.18%)</td><td>9.81 (-6.45%)</td><td>0.37 <b>(+33.74%)</b></td><td>8347.90 (+6.90%)</td><td>7829.32 (+2.64%)</td><td>7718.10 (+0.18%)</td><td>7651.20 (+3.46%)</td><td>291.30 <b>(+48.74%)</b></td><td>14033.60 (-3.35%)</td><td>13728.83 (-2.52%)</td><td>13911.95 (-0.18%)</td><td>12862.38 (-6.45%)</td><td>487.14 <b>(+33.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>11.08 (n/a)</td><td>10.75 (n/a)</td><td>10.63 (n/a)</td><td>10.49 (n/a)</td><td>0.28 (n/a)</td><td>7809.30 (n/a)</td><td>7627.88 (n/a)</td><td>7703.90 (n/a)</td><td>7395.10 (n/a)</td><td>195.85 (n/a)</td><td>14519.63 (n/a)</td><td>14084.05 (n/a)</td><td>13937.58 (n/a)</td><td>13749.61 (n/a)</td><td>364.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>11.80 <b>(-21.75%)</b></td><td>11.05 (-14.94%)</td><td>11.08 (-15.49%)</td><td>10.24 (-10.12%)</td><td>0.66 <b>(-54.95%)</b></td><td>2099.10 (+11.26%)</td><td>1950.14 (+16.75%)</td><td>1939.60 (+18.33%)</td><td>1820.90 <b>(+27.79%)</b></td><td>116.37 <b>(-36.34%)</b></td><td>9434.59 <b>(-21.75%)</b></td><td>8834.48 (-14.94%)</td><td>8857.47 (-15.49%)</td><td>8184.27 (-10.12%)</td><td>523.60 <b>(-54.95%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.09 (n/a)</td><td>13.00 (n/a)</td><td>13.11 (n/a)</td><td>11.39 (n/a)</td><td>1.45 (n/a)</td><td>1886.70 (n/a)</td><td>1670.34 (n/a)</td><td>1639.10 (n/a)</td><td>1424.90 (n/a)</td><td>182.79 (n/a)</td><td>12056.70 (n/a)</td><td>10386.46 (n/a)</td><td>10481.22 (n/a)</td><td>9105.55 (n/a)</td><td>1162.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.62 (-2.28%)</td><td>10.40 (-1.70%)</td><td>10.45 (+0.37%)</td><td>10.09 (-2.62%)</td><td>0.21 (-17.87%)</td><td>8119.30 (+2.69%)</td><td>7878.34 (+1.72%)</td><td>7837.70 (-0.37%)</td><td>7717.30 (+2.34%)</td><td>160.82 (-13.42%)</td><td>13913.39 (-2.28%)</td><td>13633.51 (-1.70%)</td><td>13699.70 (+0.37%)</td><td>13224.49 (-2.62%)</td><td>275.44 (-17.87%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>10.86 (n/a)</td><td>10.58 (n/a)</td><td>10.41 (n/a)</td><td>10.36 (n/a)</td><td>0.26 (n/a)</td><td>7906.80 (n/a)</td><td>7745.46 (n/a)</td><td>7867.10 (n/a)</td><td>7541.10 (n/a)</td><td>185.75 (n/a)</td><td>14238.47 (n/a)</td><td>13869.31 (n/a)</td><td>13648.54 (n/a)</td><td>13579.97 (n/a)</td><td>335.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.06 (-8.39%)</td><td>3.48 (-0.49%)</td><td>3.74 (+15.05%)</td><td>2.87 (+6.41%)</td><td>0.55 <b>(-29.00%)</b></td><td>479.90 (-6.03%)</td><td>403.50 (-1.27%)</td><td>367.70 (-13.09%)</td><td>338.80 (+9.15%)</td><td>67.15 <b>(-23.88%)</b></td><td>792.28 (-8.39%)</td><td>679.63 (-0.49%)</td><td>729.96 (+15.05%)</td><td>559.35 (+6.41%)</td><td>108.14 <b>(-29.00%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.43 (n/a)</td><td>3.50 (n/a)</td><td>3.25 (n/a)</td><td>2.69 (n/a)</td><td>0.78 (n/a)</td><td>510.70 (n/a)</td><td>408.68 (n/a)</td><td>423.10 (n/a)</td><td>310.40 (n/a)</td><td>88.21 (n/a)</td><td>864.86 (n/a)</td><td>682.99 (n/a)</td><td>634.46 (n/a)</td><td>525.64 (n/a)</td><td>152.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.71 (-8.96%)</td><td>3.51 (-7.89%)</td><td>3.49 (-12.26%)</td><td>3.29 (-3.96%)</td><td>0.17 <b>(-41.70%)</b></td><td>418.00 (+4.14%)</td><td>392.88 (+8.26%)</td><td>393.90 (+13.98%)</td><td>370.90 (+9.86%)</td><td>18.88 <b>(-33.42%)</b></td><td>723.77 (-8.96%)</td><td>684.50 (-7.89%)</td><td>681.45 (-12.26%)</td><td>642.21 (-3.96%)</td><td>32.77 <b>(-41.70%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.08 (n/a)</td><td>3.81 (n/a)</td><td>3.98 (n/a)</td><td>3.43 (n/a)</td><td>0.29 (n/a)</td><td>401.40 (n/a)</td><td>362.90 (n/a)</td><td>345.60 (n/a)</td><td>337.60 (n/a)</td><td>28.36 (n/a)</td><td>795.01 (n/a)</td><td>743.16 (n/a)</td><td>776.71 (n/a)</td><td>668.70 (n/a)</td><td>56.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>5.27 <b>(-27.89%)</b></td><td>3.88 <b>(-28.42%)</b></td><td>3.59 <b>(-37.00%)</b></td><td>3.41 (-0.17%)</td><td>0.78 <b>(-56.62%)</b></td><td>403.90 (+0.17%)</td><td>363.94 <b>(+29.94%)</b></td><td>383.30 <b>(+58.72%)</b></td><td>261.40 <b>(+38.67%)</b></td><td>58.73 <b>(-41.31%)</b></td><td>1026.96 <b>(-27.89%)</b></td><td>757.21 <b>(-28.42%)</b></td><td>700.27 <b>(-37.00%)</b></td><td>664.58 (-0.17%)</td><td>152.52 <b>(-56.62%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.30 (n/a)</td><td>5.42 (n/a)</td><td>5.70 (n/a)</td><td>3.41 (n/a)</td><td>1.80 (n/a)</td><td>403.20 (n/a)</td><td>280.08 (n/a)</td><td>241.50 (n/a)</td><td>188.50 (n/a)</td><td>100.07 (n/a)</td><td>1424.23 (n/a)</td><td>1057.85 (n/a)</td><td>1111.54 (n/a)</td><td>665.69 (n/a)</td><td>351.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.40 (-6.00%)</td><td>4.53 (+3.34%)</td><td>4.29 (+11.27%)</td><td>3.51 (-3.70%)</td><td>1.19 (-11.90%)</td><td>392.20 (+3.84%)</td><td>319.04 (-3.81%)</td><td>320.80 (-10.14%)</td><td>215.20 (+6.38%)</td><td>74.81 (+2.61%)</td><td>1247.43 (-6.00%)</td><td>884.38 (+3.34%)</td><td>836.77 (+11.27%)</td><td>684.46 (-3.70%)</td><td>232.68 (-11.90%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.80 (n/a)</td><td>4.39 (n/a)</td><td>3.86 (n/a)</td><td>3.64 (n/a)</td><td>1.35 (n/a)</td><td>377.70 (n/a)</td><td>331.66 (n/a)</td><td>357.00 (n/a)</td><td>202.30 (n/a)</td><td>72.91 (n/a)</td><td>1327.03 (n/a)</td><td>855.77 (n/a)</td><td>751.99 (n/a)</td><td>710.77 (n/a)</td><td>264.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.12 <b>(-25.08%)</b></td><td>3.41 (-15.17%)</td><td>3.30 (+0.05%)</td><td>3.12 (+5.94%)</td><td>0.41 <b>(-65.58%)</b></td><td>441.70 (-5.62%)</td><td>408.02 (+11.59%)</td><td>416.50 (-0.05%)</td><td>334.40 <b>(+33.49%)</b></td><td>42.81 <b>(-56.40%)</b></td><td>802.72 <b>(-25.08%)</b></td><td>664.54 (-15.17%)</td><td>644.58 (+0.05%)</td><td>607.72 (+5.94%)</td><td>79.17 <b>(-65.58%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>5.49 (n/a)</td><td>4.02 (n/a)</td><td>3.30 (n/a)</td><td>2.94 (n/a)</td><td>1.18 (n/a)</td><td>468.00 (n/a)</td><td>365.64 (n/a)</td><td>416.70 (n/a)</td><td>250.50 (n/a)</td><td>98.19 (n/a)</td><td>1071.49 (n/a)</td><td>783.36 (n/a)</td><td>644.24 (n/a)</td><td>573.63 (n/a)</td><td>230.00 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.25 (-1.93%)</td><td>3.08 (-0.47%)</td><td>3.08 (+0.99%)</td><td>2.96 (+4.63%)</td><td>0.12 <b>(-37.40%)</b></td><td>464.90 (-4.42%)</td><td>447.04 (+0.29%)</td><td>446.30 (-0.98%)</td><td>424.10 (+1.97%)</td><td>16.91 <b>(-38.65%)</b></td><td>633.00 (-1.93%)</td><td>601.18 (-0.47%)</td><td>601.46 (+0.99%)</td><td>577.46 (+4.63%)</td><td>22.94 <b>(-37.40%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.31 (n/a)</td><td>3.10 (n/a)</td><td>3.05 (n/a)</td><td>2.83 (n/a)</td><td>0.19 (n/a)</td><td>486.40 (n/a)</td><td>445.74 (n/a)</td><td>450.70 (n/a)</td><td>415.90 (n/a)</td><td>27.56 (n/a)</td><td>645.44 (n/a)</td><td>604.02 (n/a)</td><td>595.54 (n/a)</td><td>551.90 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.81 (+19.78%)</td><td>3.24 (+6.98%)</td><td>3.09 (+1.27%)</td><td>3.01 (+4.74%)</td><td>0.34 <b>(+148.47%)</b></td><td>457.30 (-4.51%)</td><td>428.58 (-5.93%)</td><td>444.70 (-1.24%)</td><td>360.80 (-16.50%)</td><td>40.30 <b>(+96.12%)</b></td><td>744.09 (+19.78%)</td><td>631.32 (+6.98%)</td><td>603.64 (+1.27%)</td><td>587.04 (+4.74%)</td><td>65.86 <b>(+148.47%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.18 (n/a)</td><td>3.03 (n/a)</td><td>3.06 (n/a)</td><td>2.87 (n/a)</td><td>0.14 (n/a)</td><td>478.90 (n/a)</td><td>455.58 (n/a)</td><td>450.30 (n/a)</td><td>432.10 (n/a)</td><td>20.55 (n/a)</td><td>621.21 (n/a)</td><td>590.14 (n/a)</td><td>596.07 (n/a)</td><td>560.48 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.31 (+3.49%)</td><td>1.14 (+0.49%)</td><td>1.13 (+3.96%)</td><td>1.01 (-4.80%)</td><td>0.11 <b>(+26.26%)</b></td><td>397.20 (+5.02%)</td><td>355.46 (-0.23%)</td><td>355.00 (-3.79%)</td><td>307.40 (-3.39%)</td><td>32.57 <b>(+26.54%)</b></td><td>109.14 (+3.49%)</td><td>95.06 (+0.49%)</td><td>94.53 (+3.96%)</td><td>84.47 (-4.80%)</td><td>9.04 <b>(+26.26%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.26 (n/a)</td><td>1.13 (n/a)</td><td>1.09 (n/a)</td><td>1.06 (n/a)</td><td>0.09 (n/a)</td><td>378.20 (n/a)</td><td>356.28 (n/a)</td><td>369.00 (n/a)</td><td>318.20 (n/a)</td><td>25.74 (n/a)</td><td>105.46 (n/a)</td><td>94.59 (n/a)</td><td>90.93 (n/a)</td><td>88.73 (n/a)</td><td>7.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>5.27 (-15.76%)</td><td>4.78 (-9.35%)</td><td>4.82 (-5.84%)</td><td>4.34 (-2.11%)</td><td>0.35 <b>(-58.33%)</b></td><td>445.20 (+2.16%)</td><td>406.08 (+8.62%)</td><td>401.30 (+6.22%)</td><td>367.10 (+18.69%)</td><td>29.25 <b>(-49.39%)</b></td><td>1096.76 (-15.76%)</td><td>995.68 (-9.35%)</td><td>1003.44 (-5.84%)</td><td>904.44 (-2.11%)</td><td>71.98 <b>(-58.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.25 (n/a)</td><td>5.27 (n/a)</td><td>5.12 (n/a)</td><td>4.44 (n/a)</td><td>0.83 (n/a)</td><td>435.80 (n/a)</td><td>373.84 (n/a)</td><td>377.80 (n/a)</td><td>309.30 (n/a)</td><td>57.79 (n/a)</td><td>1301.96 (n/a)</td><td>1098.40 (n/a)</td><td>1065.65 (n/a)</td><td>923.95 (n/a)</td><td>172.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>16.82 (-13.33%)</td><td>11.89 (-8.50%)</td><td>10.82 (-8.77%)</td><td>10.17 (-0.19%)</td><td>2.78 <b>(-24.77%)</b></td><td>541.60 (+0.20%)</td><td>479.20 (+7.51%)</td><td>509.00 (+9.63%)</td><td>327.30 (+15.37%)</td><td>86.39 (-12.00%)</td><td>6561.55 (-13.33%)</td><td>4637.37 (-8.50%)</td><td>4219.12 (-8.77%)</td><td>3965.36 (-0.19%)</td><td>1082.98 <b>(-24.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>19.41 (n/a)</td><td>12.99 (n/a)</td><td>11.86 (n/a)</td><td>10.18 (n/a)</td><td>3.69 (n/a)</td><td>540.50 (n/a)</td><td>445.74 (n/a)</td><td>464.30 (n/a)</td><td>283.70 (n/a)</td><td>98.16 (n/a)</td><td>7570.41 (n/a)</td><td>5068.42 (n/a)</td><td>4624.90 (n/a)</td><td>3972.96 (n/a)</td><td>1439.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.34 (-12.92%)</td><td>7.91 (-6.93%)</td><td>7.73 (-4.99%)</td><td>7.07 (-5.33%)</td><td>0.86 <b>(-32.61%)</b></td><td>779.00 (+5.64%)</td><td>701.74 (+6.72%)</td><td>712.00 (+5.25%)</td><td>589.60 (+14.84%)</td><td>70.32 (-17.05%)</td><td>3642.20 (-12.92%)</td><td>3086.95 (-6.93%)</td><td>3015.94 (-4.99%)</td><td>2756.75 (-5.33%)</td><td>335.03 <b>(-32.61%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>10.72 (n/a)</td><td>8.50 (n/a)</td><td>8.14 (n/a)</td><td>7.47 (n/a)</td><td>1.27 (n/a)</td><td>737.40 (n/a)</td><td>657.56 (n/a)</td><td>676.50 (n/a)</td><td>513.40 (n/a)</td><td>84.78 (n/a)</td><td>4182.51 (n/a)</td><td>3316.76 (n/a)</td><td>3174.20 (n/a)</td><td>2912.09 (n/a)</td><td>497.18 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.03 (-3.05%)</td><td>8.79 (+1.96%)</td><td>8.61 (-3.70%)</td><td>7.98 <b>(+62.76%)</b></td><td>0.75 <b>(-65.60%)</b></td><td>726.50 <b>(-38.56%)</b></td><td>663.18 (-8.47%)</td><td>673.30 (+3.84%)</td><td>578.50 (+3.14%)</td><td>53.65 <b>(-79.33%)</b></td><td>4175.88 (-3.05%)</td><td>3663.00 (+1.96%)</td><td>3587.96 (-3.70%)</td><td>3325.37 <b>(+62.76%)</b></td><td>313.26 <b>(-65.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>10.34 (n/a)</td><td>8.62 (n/a)</td><td>8.94 (n/a)</td><td>4.90 (n/a)</td><td>2.19 (n/a)</td><td>1182.50 (n/a)</td><td>724.54 (n/a)</td><td>648.40 (n/a)</td><td>560.90 (n/a)</td><td>259.59 (n/a)</td><td>4307.11 (n/a)</td><td>3592.50 (n/a)</td><td>3725.69 (n/a)</td><td>2043.06 (n/a)</td><td>910.65 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>167.76 (n/a)</td><td>158.20 (n/a)</td><td>122.20 (n/a)</td><td>41.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>142.12 (n/a)</td><td>124.60 (n/a)</td><td>117.60 (n/a)</td><td>39.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>292.40 (n/a)</td><td>169.18 (n/a)</td><td>146.30 (n/a)</td><td>117.00 (n/a)</td><td>70.00 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.20 (n/a)</td><td>166.88 (n/a)</td><td>163.90 (n/a)</td><td>147.30 (n/a)</td><td>17.13 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.70 (n/a)</td><td>159.08 (n/a)</td><td>156.00 (n/a)</td><td>129.70 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.60 (n/a)</td><td>179.92 (n/a)</td><td>171.50 (n/a)</td><td>146.50 (n/a)</td><td>35.09 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>173.70 (n/a)</td><td>165.70 (n/a)</td><td>134.40 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>320.70 (n/a)</td><td>219.22 (n/a)</td><td>202.80 (n/a)</td><td>174.80 (n/a)</td><td>59.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.50 (n/a)</td><td>164.66 (n/a)</td><td>169.10 (n/a)</td><td>141.20 (n/a)</td><td>14.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>310.60 (n/a)</td><td>194.58 (n/a)</td><td>184.10 (n/a)</td><td>106.50 (n/a)</td><td>73.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.60 (n/a)</td><td>221.42 (n/a)</td><td>186.60 (n/a)</td><td>139.60 (n/a)</td><td>81.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>173.76 (n/a)</td><td>154.30 (n/a)</td><td>149.40 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>353.70 (n/a)</td><td>191.44 (n/a)</td><td>167.60 (n/a)</td><td>122.20 (n/a)</td><td>94.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.60 (n/a)</td><td>168.30 (n/a)</td><td>164.50 (n/a)</td><td>152.90 (n/a)</td><td>15.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>364.00 (n/a)</td><td>203.60 (n/a)</td><td>169.40 (n/a)</td><td>128.90 (n/a)</td><td>93.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.60 (n/a)</td><td>210.28 (n/a)</td><td>202.00 (n/a)</td><td>165.50 (n/a)</td><td>52.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.90 (n/a)</td><td>171.92 (n/a)</td><td>162.80 (n/a)</td><td>150.60 (n/a)</td><td>21.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>185.42 (n/a)</td><td>184.80 (n/a)</td><td>157.80 (n/a)</td><td>22.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>165.70 (n/a)</td><td>156.00 (n/a)</td><td>158.20 (n/a)</td><td>137.40 (n/a)</td><td>11.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>223.20 (n/a)</td><td>198.62 (n/a)</td><td>190.40 (n/a)</td><td>171.90 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.80 (n/a)</td><td>167.46 (n/a)</td><td>166.40 (n/a)</td><td>123.60 (n/a)</td><td>31.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>190.02 (n/a)</td><td>195.50 (n/a)</td><td>173.80 (n/a)</td><td>15.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>294.90 (n/a)</td><td>204.12 (n/a)</td><td>198.00 (n/a)</td><td>151.30 (n/a)</td><td>55.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>339.60 (n/a)</td><td>252.30 (n/a)</td><td>230.00 (n/a)</td><td>181.70 (n/a)</td><td>66.50 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>214.10 (n/a)</td><td>158.16 (n/a)</td><td>152.30 (n/a)</td><td>123.30 (n/a)</td><td>35.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>164.20 (n/a)</td><td>144.30 (n/a)</td><td>153.30 (n/a)</td><td>104.00 (n/a)</td><td>23.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>266.10 (n/a)</td><td>178.26 (n/a)</td><td>172.30 (n/a)</td><td>125.40 (n/a)</td><td>56.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>167.70 (n/a)</td><td>145.74 (n/a)</td><td>157.00 (n/a)</td><td>114.90 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.50 (n/a)</td><td>158.14 (n/a)</td><td>158.00 (n/a)</td><td>133.60 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>221.50 (n/a)</td><td>182.54 (n/a)</td><td>204.40 (n/a)</td><td>139.90 (n/a)</td><td>39.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>193.10 (n/a)</td><td>156.46 (n/a)</td><td>143.00 (n/a)</td><td>120.20 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>337.30 (n/a)</td><td>222.84 (n/a)</td><td>188.70 (n/a)</td><td>184.80 (n/a)</td><td>65.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.21 (+0.69%)</td><td>4.12 (+0.12%)</td><td>4.11 (-0.07%)</td><td>4.07 (-0.07%)</td><td>0.05 <b>(+30.81%)</b></td><td>19325.80 (+0.07%)</td><td>19089.66 (-0.12%)</td><td>19132.80 (+0.07%)</td><td>18668.70 (-0.69%)</td><td>250.48 <b>(+29.89%)</b></td><td>2875.78 (+0.69%)</td><td>2812.76 (+0.12%)</td><td>2806.03 (-0.07%)</td><td>2778.01 (-0.07%)</td><td>37.37 <b>(+30.81%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.18 (n/a)</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.07 (n/a)</td><td>0.04 (n/a)</td><td>19311.40 (n/a)</td><td>19112.10 (n/a)</td><td>19119.90 (n/a)</td><td>18797.70 (n/a)</td><td>192.84 (n/a)</td><td>2856.04 (n/a)</td><td>2809.29 (n/a)</td><td>2807.91 (n/a)</td><td>2780.07 (n/a)</td><td>28.57 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.96 (+11.16%)</td><td>4.39 (+10.62%)</td><td>4.29 (+4.00%)</td><td>4.14 (+18.04%)</td><td>0.33 <b>(-23.01%)</b></td><td>2273.10 (-15.28%)</td><td>2149.48 (-10.07%)</td><td>2194.40 (-3.85%)</td><td>1895.70 (-10.04%)</td><td>147.64 <b>(-43.26%)</b></td><td>1951.46 (+11.16%)</td><td>1728.11 (+10.62%)</td><td>1685.80 (+4.00%)</td><td>1627.44 (+18.04%)</td><td>128.58 <b>(-23.01%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.46 (n/a)</td><td>3.97 (n/a)</td><td>4.12 (n/a)</td><td>3.50 (n/a)</td><td>0.42 (n/a)</td><td>2683.20 (n/a)</td><td>2390.26 (n/a)</td><td>2282.30 (n/a)</td><td>2107.20 (n/a)</td><td>260.22 (n/a)</td><td>1755.62 (n/a)</td><td>1562.23 (n/a)</td><td>1620.90 (n/a)</td><td>1378.72 (n/a)</td><td>167.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.33 <b>(+23.60%)</b></td><td>1.00 (+7.72%)</td><td>1.07 (+3.11%)</td><td>0.58 (-7.78%)</td><td>0.28 <b>(+50.32%)</b></td><td>379.60 (+8.43%)</td><td>239.04 (-3.51%)</td><td>207.60 (-3.04%)</td><td>166.30 (-19.08%)</td><td>83.27 <b>(+37.54%)</b></td><td>56.76 <b>(+23.60%)</b></td><td>42.69 (+7.72%)</td><td>45.46 (+3.11%)</td><td>24.86 (-7.78%)</td><td>11.87 <b>(+50.32%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.08 (n/a)</td><td>0.93 (n/a)</td><td>1.03 (n/a)</td><td>0.63 (n/a)</td><td>0.19 (n/a)</td><td>350.10 (n/a)</td><td>247.74 (n/a)</td><td>214.10 (n/a)</td><td>205.50 (n/a)</td><td>60.54 (n/a)</td><td>45.92 (n/a)</td><td>39.63 (n/a)</td><td>44.09 (n/a)</td><td>26.96 (n/a)</td><td>7.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.24 (+19.16%)</td><td>1.06 (+15.86%)</td><td>1.04 (+8.98%)</td><td>0.88 <b>(+37.87%)</b></td><td>0.17 (+4.75%)</td><td>251.70 <b>(-27.46%)</b></td><td>212.80 (-14.66%)</td><td>211.90 (-8.23%)</td><td>178.70 (-16.10%)</td><td>33.69 <b>(-39.10%)</b></td><td>52.80 (+19.16%)</td><td>45.25 (+15.86%)</td><td>44.53 (+8.98%)</td><td>37.49 <b>(+37.87%)</b></td><td>7.17 (+4.75%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.04 (n/a)</td><td>0.92 (n/a)</td><td>0.96 (n/a)</td><td>0.64 (n/a)</td><td>0.16 (n/a)</td><td>347.00 (n/a)</td><td>249.36 (n/a)</td><td>230.90 (n/a)</td><td>213.00 (n/a)</td><td>55.31 (n/a)</td><td>44.31 (n/a)</td><td>39.05 (n/a)</td><td>40.86 (n/a)</td><td>27.20 (n/a)</td><td>6.84 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.53 (+0.09%)</td><td>0.53 (-0.01%)</td><td>0.53 (+0.03%)</td><td>0.53 (-0.10%)</td><td>0.00 <b>(+143.57%)</b></td><td>47890.90 (+0.10%)</td><td>47809.30 (+0.01%)</td><td>47788.20 (-0.03%)</td><td>47739.50 (-0.09%)</td><td>57.92 <b>(+143.59%)</b></td><td>359.87 (+0.09%)</td><td>359.34 (-0.01%)</td><td>359.50 (+0.03%)</td><td>358.73 (-0.10%)</td><td>0.44 <b>(+143.57%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47842.50 (n/a)</td><td>47806.62 (n/a)</td><td>47800.50 (n/a)</td><td>47784.10 (n/a)</td><td>23.78 (n/a)</td><td>359.53 (n/a)</td><td>359.36 (n/a)</td><td>359.41 (n/a)</td><td>359.09 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.22 (+2.17%)</td><td>0.21 (+0.19%)</td><td>0.21 (+0.41%)</td><td>0.21 (-0.84%)</td><td>0.00 <b>(+165.65%)</b></td><td>120761.60 (+0.85%)</td><td>118716.76 (-0.17%)</td><td>118820.30 (-0.41%)</td><td>115483.70 (-2.12%)</td><td>2024.29 <b>(+161.92%)</b></td><td>148.76 (+2.17%)</td><td>144.75 (+0.19%)</td><td>144.59 (+0.41%)</td><td>142.26 (-0.84%)</td><td>2.50 <b>(+165.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119741.30 (n/a)</td><td>118919.66 (n/a)</td><td>119307.60 (n/a)</td><td>117988.20 (n/a)</td><td>772.86 (n/a)</td><td>145.61 (n/a)</td><td>144.47 (n/a)</td><td>144.00 (n/a)</td><td>143.47 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.91 (+0.79%)</td><td>0.90 (+0.59%)</td><td>0.90 (+0.34%)</td><td>0.90 (+0.73%)</td><td>0.01 (-2.99%)</td><td>28023.30 (-0.72%)</td><td>27847.10 (-0.59%)</td><td>27849.80 (-0.34%)</td><td>27625.60 (-0.78%)</td><td>154.66 (-4.47%)</td><td>621.88 (+0.79%)</td><td>616.95 (+0.59%)</td><td>616.88 (+0.34%)</td><td>613.06 (+0.73%)</td><td>3.43 (-3.00%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28227.50 (n/a)</td><td>28012.46 (n/a)</td><td>27945.00 (n/a)</td><td>27843.30 (n/a)</td><td>161.90 (n/a)</td><td>617.02 (n/a)</td><td>613.31 (n/a)</td><td>614.77 (n/a)</td><td>608.62 (n/a)</td><td>3.54 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.64 (-1.72%)</td><td>3.54 (-1.84%)</td><td>3.61 (-1.20%)</td><td>3.40 (-2.77%)</td><td>0.11 <b>(+28.85%)</b></td><td>7406.00 (+2.85%)</td><td>7105.46 (+1.91%)</td><td>6974.20 (+1.21%)</td><td>6916.30 (+1.75%)</td><td>227.04 <b>(+34.43%)</b></td><td>2483.98 (-1.72%)</td><td>2419.79 (-1.84%)</td><td>2463.33 (-1.20%)</td><td>2319.73 (-2.77%)</td><td>76.29 <b>(+28.85%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.70 (n/a)</td><td>3.61 (n/a)</td><td>3.65 (n/a)</td><td>3.49 (n/a)</td><td>0.09 (n/a)</td><td>7200.60 (n/a)</td><td>6972.16 (n/a)</td><td>6890.60 (n/a)</td><td>6797.40 (n/a)</td><td>168.89 (n/a)</td><td>2527.43 (n/a)</td><td>2465.22 (n/a)</td><td>2493.24 (n/a)</td><td>2385.90 (n/a)</td><td>59.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>2.88 (-10.50%)</td><td>2.85 (-6.02%)</td><td>2.86 (-5.70%)</td><td>2.78 (-2.12%)</td><td>0.04 <b>(-67.63%)</b></td><td>9056.20 (+2.17%)</td><td>8832.38 (+6.25%)</td><td>8785.00 (+6.05%)</td><td>8723.80 (+11.73%)</td><td>139.24 <b>(-63.13%)</b></td><td>1969.30 (-10.50%)</td><td>1945.48 (-6.02%)</td><td>1955.58 (-5.70%)</td><td>1897.02 (-2.12%)</td><td>30.29 <b>(-67.63%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.22 (n/a)</td><td>3.03 (n/a)</td><td>3.04 (n/a)</td><td>2.84 (n/a)</td><td>0.14 (n/a)</td><td>8864.20 (n/a)</td><td>8313.04 (n/a)</td><td>8284.00 (n/a)</td><td>7807.80 (n/a)</td><td>377.60 (n/a)</td><td>2200.35 (n/a)</td><td>2070.01 (n/a)</td><td>2073.86 (n/a)</td><td>1938.11 (n/a)</td><td>93.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.28 (+2.95%)</td><td>3.21 (+1.87%)</td><td>3.18 (+0.52%)</td><td>3.14 (+1.30%)</td><td>0.06 <b>(+110.66%)</b></td><td>8003.60 (-1.28%)</td><td>7839.66 (-1.81%)</td><td>7924.20 (-0.52%)</td><td>7669.90 (-2.86%)</td><td>155.72 <b>(+100.78%)</b></td><td>2239.91 (+2.95%)</td><td>2192.10 (+1.87%)</td><td>2168.04 (+0.52%)</td><td>2146.53 (+1.30%)</td><td>43.75 <b>(+110.65%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.19 (n/a)</td><td>3.15 (n/a)</td><td>3.16 (n/a)</td><td>3.10 (n/a)</td><td>0.03 (n/a)</td><td>8107.60 (n/a)</td><td>7984.10 (n/a)</td><td>7965.60 (n/a)</td><td>7895.80 (n/a)</td><td>77.55 (n/a)</td><td>2175.81 (n/a)</td><td>2151.92 (n/a)</td><td>2156.75 (n/a)</td><td>2118.99 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.80 (+0.32%)</td><td>0.80 (+0.05%)</td><td>0.80 (+0.04%)</td><td>0.79 (-0.16%)</td><td>0.00 <b>(+352.30%)</b></td><td>94997.00 (+0.16%)</td><td>94758.26 (-0.05%)</td><td>94786.20 (-0.04%)</td><td>94445.20 (-0.32%)</td><td>198.57 <b>(+351.26%)</b></td><td>727.61 (+0.32%)</td><td>725.21 (+0.05%)</td><td>724.99 (+0.04%)</td><td>723.39 (-0.16%)</td><td>1.52 <b>(+352.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94846.30 (n/a)</td><td>94802.32 (n/a)</td><td>94819.80 (n/a)</td><td>94752.00 (n/a)</td><td>44.00 (n/a)</td><td>725.26 (n/a)</td><td>724.87 (n/a)</td><td>724.74 (n/a)</td><td>724.54 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.73 (-0.03%)</td><td>0.73 (-0.07%)</td><td>0.73 (-0.04%)</td><td>0.73 (-0.10%)</td><td>0.00 <b>(+82.35%)</b></td><td>103486.80 (+0.10%)</td><td>103381.12 (+0.07%)</td><td>103337.40 (+0.04%)</td><td>103303.60 (+0.03%)</td><td>82.35 <b>(+82.49%)</b></td><td>665.22 (-0.03%)</td><td>664.72 (-0.07%)</td><td>665.00 (-0.04%)</td><td>664.04 (-0.10%)</td><td>0.53 <b>(+82.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103383.70 (n/a)</td><td>103312.48 (n/a)</td><td>103299.80 (n/a)</td><td>103267.60 (n/a)</td><td>45.12 (n/a)</td><td>665.45 (n/a)</td><td>665.16 (n/a)</td><td>665.24 (n/a)</td><td>664.70 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.69 (+0.09%)</td><td>0.69 (+0.20%)</td><td>0.69 (+0.17%)</td><td>0.69 (+0.64%)</td><td>0.00 <b>(-45.45%)</b></td><td>110084.50 (-0.64%)</td><td>109870.14 (-0.20%)</td><td>109898.80 (-0.17%)</td><td>109442.90 (-0.09%)</td><td>255.43 <b>(-45.87%)</b></td><td>627.90 (+0.09%)</td><td>625.46 (+0.20%)</td><td>625.30 (+0.17%)</td><td>624.24 (+0.64%)</td><td>1.46 <b>(-45.45%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110789.50 (n/a)</td><td>110090.12 (n/a)</td><td>110087.00 (n/a)</td><td>109539.10 (n/a)</td><td>471.92 (n/a)</td><td>627.35 (n/a)</td><td>624.22 (n/a)</td><td>624.23 (n/a)</td><td>620.27 (n/a)</td><td>2.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>2.80 (-0.00%)</td><td>2.79 (+0.05%)</td><td>2.79 (+0.03%)</td><td>2.79 (+0.07%)</td><td>0.01 <b>(-21.57%)</b></td><td>37646.90 (-0.07%)</td><td>37551.28 (-0.05%)</td><td>37516.80 (-0.03%)</td><td>37493.90 (+0.00%)</td><td>68.25 <b>(-21.63%)</b></td><td>2863.78 (-0.00%)</td><td>2859.41 (+0.05%)</td><td>2862.03 (+0.03%)</td><td>2852.14 (+0.07%)</td><td>5.19 <b>(-21.56%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>2.79 (n/a)</td><td>2.78 (n/a)</td><td>0.01 (n/a)</td><td>37675.10 (n/a)</td><td>37569.84 (n/a)</td><td>37526.90 (n/a)</td><td>37493.00 (n/a)</td><td>87.08 (n/a)</td><td>2863.85 (n/a)</td><td>2858.00 (n/a)</td><td>2861.26 (n/a)</td><td>2850.00 (n/a)</td><td>6.62 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.53 (+1.42%)</td><td>6.87 (+0.06%)</td><td>6.72 (-5.79%)</td><td>6.41 (+2.83%)</td><td>0.46 (-11.69%)</td><td>1391.40 (-2.75%)</td><td>1301.60 (-0.18%)</td><td>1326.80 (+6.14%)</td><td>1182.90 (-1.40%)</td><td>84.14 (-16.14%)</td><td>453.87 (+1.42%)</td><td>413.89 (+0.06%)</td><td>404.62 (-5.79%)</td><td>385.84 (+2.83%)</td><td>27.52 (-11.69%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.43 (n/a)</td><td>6.87 (n/a)</td><td>7.13 (n/a)</td><td>6.23 (n/a)</td><td>0.52 (n/a)</td><td>1430.80 (n/a)</td><td>1304.00 (n/a)</td><td>1250.10 (n/a)</td><td>1199.70 (n/a)</td><td>100.33 (n/a)</td><td>447.50 (n/a)</td><td>413.63 (n/a)</td><td>429.47 (n/a)</td><td>375.23 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.03 (+2.51%)</td><td>6.76 (+3.58%)</td><td>6.86 (+4.92%)</td><td>6.41 (+6.23%)</td><td>0.29 (-10.90%)</td><td>1391.30 (-5.87%)</td><td>1321.34 (-3.50%)</td><td>1299.00 (-4.68%)</td><td>1268.70 (-2.45%)</td><td>56.60 (-18.39%)</td><td>423.18 (+2.51%)</td><td>406.90 (+3.58%)</td><td>413.30 (+4.92%)</td><td>385.88 (+6.23%)</td><td>17.21 (-10.90%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.85 (n/a)</td><td>6.52 (n/a)</td><td>6.54 (n/a)</td><td>6.03 (n/a)</td><td>0.32 (n/a)</td><td>1478.00 (n/a)</td><td>1369.32 (n/a)</td><td>1362.80 (n/a)</td><td>1300.50 (n/a)</td><td>69.35 (n/a)</td><td>412.81 (n/a)</td><td>392.85 (n/a)</td><td>393.93 (n/a)</td><td>363.24 (n/a)</td><td>19.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.15 (-0.13%)</td><td>6.38 (+0.47%)</td><td>6.88 (-1.41%)</td><td>4.53 (-0.21%)</td><td>1.10 (-1.06%)</td><td>1967.40 (+0.21%)</td><td>1437.52 (-0.49%)</td><td>1295.60 (+1.43%)</td><td>1245.90 (+0.14%)</td><td>304.49 (+0.12%)</td><td>430.92 (-0.13%)</td><td>384.60 (+0.47%)</td><td>414.37 (-1.41%)</td><td>272.88 (-0.21%)</td><td>65.97 (-1.06%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.16 (n/a)</td><td>6.35 (n/a)</td><td>6.98 (n/a)</td><td>4.54 (n/a)</td><td>1.11 (n/a)</td><td>1963.30 (n/a)</td><td>1444.66 (n/a)</td><td>1277.30 (n/a)</td><td>1244.20 (n/a)</td><td>304.14 (n/a)</td><td>431.49 (n/a)</td><td>382.79 (n/a)</td><td>420.30 (n/a)</td><td>273.45 (n/a)</td><td>66.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>8.13 (-0.13%)</td><td>7.80 (-0.73%)</td><td>7.88 (-0.99%)</td><td>7.32 (-2.08%)</td><td>0.30 (+2.00%)</td><td>4762.50 (+2.13%)</td><td>4474.44 (+0.75%)</td><td>4422.50 (+1.00%)</td><td>4287.80 (+0.13%)</td><td>178.74 (+5.10%)</td><td>500.83 (-0.13%)</td><td>480.54 (-0.73%)</td><td>485.58 (-0.99%)</td><td>450.92 (-2.08%)</td><td>18.68 (+2.00%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>8.14 (n/a)</td><td>7.86 (n/a)</td><td>7.96 (n/a)</td><td>7.48 (n/a)</td><td>0.30 (n/a)</td><td>4663.20 (n/a)</td><td>4441.20 (n/a)</td><td>4378.60 (n/a)</td><td>4282.40 (n/a)</td><td>170.06 (n/a)</td><td>501.47 (n/a)</td><td>484.10 (n/a)</td><td>490.45 (n/a)</td><td>460.52 (n/a)</td><td>18.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.76 (+1.32%)</td><td>7.62 (+2.11%)</td><td>7.60 (+0.85%)</td><td>7.50 (+6.65%)</td><td>0.12 <b>(-51.60%)</b></td><td>4650.20 (-6.24%)</td><td>4575.52 (-2.14%)</td><td>4586.10 (-0.84%)</td><td>4495.20 (-1.30%)</td><td>71.79 <b>(-55.56%)</b></td><td>477.72 (+1.32%)</td><td>469.43 (+2.11%)</td><td>468.26 (+0.85%)</td><td>461.80 (+6.65%)</td><td>7.38 <b>(-51.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.66 (n/a)</td><td>7.46 (n/a)</td><td>7.54 (n/a)</td><td>7.03 (n/a)</td><td>0.25 (n/a)</td><td>4959.60 (n/a)</td><td>4675.52 (n/a)</td><td>4625.00 (n/a)</td><td>4554.30 (n/a)</td><td>161.54 (n/a)</td><td>471.52 (n/a)</td><td>459.72 (n/a)</td><td>464.32 (n/a)</td><td>432.99 (n/a)</td><td>15.24 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.46 (-5.75%)</td><td>7.32 (-1.11%)</td><td>7.33 (-0.33%)</td><td>7.15 (+4.08%)</td><td>0.11 <b>(-70.53%)</b></td><td>4878.60 (-3.92%)</td><td>4765.22 (+0.93%)</td><td>4756.60 (+0.33%)</td><td>4675.10 (+6.10%)</td><td>72.82 <b>(-69.94%)</b></td><td>459.34 (-5.75%)</td><td>450.74 (-1.11%)</td><td>451.47 (-0.33%)</td><td>440.19 (+4.08%)</td><td>6.84 <b>(-70.53%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>7.91 (n/a)</td><td>7.40 (n/a)</td><td>7.35 (n/a)</td><td>6.87 (n/a)</td><td>0.38 (n/a)</td><td>5077.40 (n/a)</td><td>4721.30 (n/a)</td><td>4741.00 (n/a)</td><td>4406.50 (n/a)</td><td>242.24 (n/a)</td><td>487.35 (n/a)</td><td>455.80 (n/a)</td><td>452.96 (n/a)</td><td>422.95 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.80 (-0.01%)</td><td>0.80 (-0.02%)</td><td>0.80 (-0.03%)</td><td>0.80 (-0.03%)</td><td>0.00 <b>(+65.57%)</b></td><td>94111.40 (+0.03%)</td><td>94073.62 (+0.02%)</td><td>94071.80 (+0.03%)</td><td>94044.80 (+0.01%)</td><td>26.32 <b>(+65.66%)</b></td><td>730.71 (-0.01%)</td><td>730.49 (-0.02%)</td><td>730.50 (-0.03%)</td><td>730.19 (-0.03%)</td><td>0.20 <b>(+65.56%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94079.00 (n/a)</td><td>94051.02 (n/a)</td><td>94045.20 (n/a)</td><td>94039.50 (n/a)</td><td>15.89 (n/a)</td><td>730.75 (n/a)</td><td>730.66 (n/a)</td><td>730.71 (n/a)</td><td>730.44 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.74 (+0.36%)</td><td>0.74 (+0.06%)</td><td>0.74 (-0.01%)</td><td>0.73 (-0.03%)</td><td>0.00 <b>(+134.98%)</b></td><td>102834.80 (+0.03%)</td><td>102570.24 (-0.06%)</td><td>102611.80 (+0.01%)</td><td>102185.80 (-0.36%)</td><td>236.72 <b>(+134.00%)</b></td><td>672.50 (+0.36%)</td><td>669.98 (+0.06%)</td><td>669.70 (-0.01%)</td><td>668.25 (-0.03%)</td><td>1.55 <b>(+134.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102804.40 (n/a)</td><td>102627.72 (n/a)</td><td>102599.60 (n/a)</td><td>102550.10 (n/a)</td><td>101.16 (n/a)</td><td>670.11 (n/a)</td><td>669.60 (n/a)</td><td>669.78 (n/a)</td><td>668.45 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.71 (-0.14%)</td><td>0.71 (-0.08%)</td><td>0.71 (-0.06%)</td><td>0.71 (-0.11%)</td><td>0.00 (-7.24%)</td><td>106099.30 (+0.11%)</td><td>105957.28 (+0.08%)</td><td>105950.80 (+0.06%)</td><td>105865.50 (+0.14%)</td><td>88.78 (-6.98%)</td><td>649.12 (-0.14%)</td><td>648.56 (-0.08%)</td><td>648.60 (-0.06%)</td><td>647.69 (-0.11%)</td><td>0.54 (-7.24%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>105980.00 (n/a)</td><td>105869.14 (n/a)</td><td>105882.00 (n/a)</td><td>105717.50 (n/a)</td><td>95.44 (n/a)</td><td>650.03 (n/a)</td><td>649.10 (n/a)</td><td>649.02 (n/a)</td><td>648.42 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>4.33 (+15.38%)</td><td>3.75 (+16.05%)</td><td>3.86 <b>(+21.45%)</b></td><td>3.07 (+4.88%)</td><td>0.56 <b>(+73.13%)</b></td><td>2627.70 (-4.65%)</td><td>2191.46 (-12.87%)</td><td>2089.70 (-17.66%)</td><td>1862.30 (-13.33%)</td><td>338.17 <b>(+44.10%)</b></td><td>1135.14 (+15.38%)</td><td>982.64 (+16.05%)</td><td>1011.60 <b>(+21.45%)</b></td><td>804.49 (+4.88%)</td><td>146.33 <b>(+73.13%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.75 (n/a)</td><td>3.23 (n/a)</td><td>3.18 (n/a)</td><td>2.93 (n/a)</td><td>0.32 (n/a)</td><td>2755.80 (n/a)</td><td>2515.28 (n/a)</td><td>2537.80 (n/a)</td><td>2148.70 (n/a)</td><td>234.68 (n/a)</td><td>983.81 (n/a)</td><td>846.72 (n/a)</td><td>832.96 (n/a)</td><td>767.08 (n/a)</td><td>84.52 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.50 (-8.18%)</td><td>0.39 (+3.75%)</td><td>0.34 (+3.55%)</td><td>0.28 (-10.91%)</td><td>0.10 (+2.97%)</td><td>4406.50 (+12.24%)</td><td>3409.80 (-2.55%)</td><td>3675.80 (-3.43%)</td><td>2484.20 (+8.90%)</td><td>849.99 <b>(+23.70%)</b></td><td>27.01 (-8.18%)</td><td>20.76 (+3.75%)</td><td>18.26 (+3.55%)</td><td>15.23 (-10.91%)</td><td>5.44 (+2.97%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.55 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.10 (n/a)</td><td>3925.80 (n/a)</td><td>3498.96 (n/a)</td><td>3806.20 (n/a)</td><td>2281.10 (n/a)</td><td>687.14 (n/a)</td><td>29.42 (n/a)</td><td>20.01 (n/a)</td><td>17.63 (n/a)</td><td>17.09 (n/a)</td><td>5.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.44 <b>(+33.48%)</b></td><td>5.05 <b>(+29.27%)</b></td><td>4.78 <b>(+40.72%)</b></td><td>4.57 <b>(+40.63%)</b></td><td>0.78 (-3.06%)</td><td>1455.40 <b>(-28.89%)</b></td><td>1338.06 <b>(-23.88%)</b></td><td>1391.00 <b>(-28.93%)</b></td><td>1032.70 <b>(-25.08%)</b></td><td>173.29 <b>(-48.84%)</b></td><td>1990.22 <b>(+33.48%)</b></td><td>1561.01 <b>(+29.27%)</b></td><td>1477.53 <b>(+40.72%)</b></td><td>1412.15 <b>(+40.63%)</b></td><td>241.87 (-3.06%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>4.83 (n/a)</td><td>3.91 (n/a)</td><td>3.40 (n/a)</td><td>3.25 (n/a)</td><td>0.81 (n/a)</td><td>2046.70 (n/a)</td><td>1757.86 (n/a)</td><td>1957.30 (n/a)</td><td>1378.40 (n/a)</td><td>338.70 (n/a)</td><td>1491.04 (n/a)</td><td>1207.60 (n/a)</td><td>1050.00 (n/a)</td><td>1004.18 (n/a)</td><td>249.51 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.43 (n/a)</td><td>13.16 (n/a)</td><td>13.22 (n/a)</td><td>12.70 (n/a)</td><td>0.30 (n/a)</td><td>13.42 (n/a)</td><td>13.15 (n/a)</td><td>13.22 (n/a)</td><td>12.70 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>24.45 (+1.79%)</td><td>23.86 (+3.64%)</td><td>24.15 (+2.92%)</td><td>22.68 (+10.50%)</td><td>0.71 <b>(-50.03%)</b></td><td>24.44 (+1.79%)</td><td>23.84 (+3.64%)</td><td>24.14 (+2.92%)</td><td>22.67 (+10.50%)</td><td>0.71 <b>(-50.03%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>24.02 (n/a)</td><td>23.02 (n/a)</td><td>23.47 (n/a)</td><td>20.53 (n/a)</td><td>1.42 (n/a)</td><td>24.01 (n/a)</td><td>23.01 (n/a)</td><td>23.45 (n/a)</td><td>20.52 (n/a)</td><td>1.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>40.70 (-0.84%)</td><td>39.33 (+0.25%)</td><td>39.02 (-0.15%)</td><td>38.38 (+2.46%)</td><td>1.03 <b>(-21.90%)</b></td><td>40.68 (-0.84%)</td><td>39.30 (+0.25%)</td><td>39.00 (-0.15%)</td><td>38.36 (+2.46%)</td><td>1.03 <b>(-21.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>41.05 (n/a)</td><td>39.23 (n/a)</td><td>39.08 (n/a)</td><td>37.46 (n/a)</td><td>1.32 (n/a)</td><td>41.02 (n/a)</td><td>39.21 (n/a)</td><td>39.05 (n/a)</td><td>37.44 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>45.72 (+3.20%)</td><td>42.51 (-2.56%)</td><td>42.05 (-3.74%)</td><td>40.04 (-6.64%)</td><td>2.25 <b>(+308.14%)</b></td><td>45.70 (+3.20%)</td><td>42.49 (-2.56%)</td><td>42.02 (-3.74%)</td><td>40.01 (-6.64%)</td><td>2.25 <b>(+308.15%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>44.31 (n/a)</td><td>43.63 (n/a)</td><td>43.68 (n/a)</td><td>42.88 (n/a)</td><td>0.55 (n/a)</td><td>44.28 (n/a)</td><td>43.60 (n/a)</td><td>43.66 (n/a)</td><td>42.86 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.47 (n/a)</td><td>12.64 (n/a)</td><td>12.64 (n/a)</td><td>11.80 (n/a)</td><td>0.70 (n/a)</td><td>13.46 (n/a)</td><td>12.64 (n/a)</td><td>12.63 (n/a)</td><td>11.80 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>24.91 (+1.80%)</td><td>24.07 (+1.34%)</td><td>24.10 (+0.75%)</td><td>23.39 (+6.04%)</td><td>0.56 <b>(-43.47%)</b></td><td>24.89 (+1.80%)</td><td>24.05 (+1.34%)</td><td>24.08 (+0.75%)</td><td>23.37 (+6.04%)</td><td>0.56 <b>(-43.47%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>24.47 (n/a)</td><td>23.75 (n/a)</td><td>23.92 (n/a)</td><td>22.05 (n/a)</td><td>0.99 (n/a)</td><td>24.45 (n/a)</td><td>23.73 (n/a)</td><td>23.90 (n/a)</td><td>22.04 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>41.13 (+2.74%)</td><td>39.87 (+3.74%)</td><td>40.90 (+7.97%)</td><td>37.95 (+3.50%)</td><td>1.59 (+6.11%)</td><td>41.11 (+2.74%)</td><td>39.85 (+3.74%)</td><td>40.87 (+7.97%)</td><td>37.93 (+3.50%)</td><td>1.58 (+6.11%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>40.04 (n/a)</td><td>38.43 (n/a)</td><td>37.88 (n/a)</td><td>36.67 (n/a)</td><td>1.49 (n/a)</td><td>40.01 (n/a)</td><td>38.41 (n/a)</td><td>37.85 (n/a)</td><td>36.65 (n/a)</td><td>1.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>43.15 (+1.22%)</td><td>40.90 (-3.24%)</td><td>40.86 (-3.77%)</td><td>37.54 (-9.60%)</td><td>2.17 <b>(+398.48%)</b></td><td>43.13 (+1.22%)</td><td>40.87 (-3.24%)</td><td>40.83 (-3.77%)</td><td>37.52 (-9.60%)</td><td>2.17 <b>(+398.48%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>42.63 (n/a)</td><td>42.27 (n/a)</td><td>42.46 (n/a)</td><td>41.52 (n/a)</td><td>0.44 (n/a)</td><td>42.61 (n/a)</td><td>42.24 (n/a)</td><td>42.43 (n/a)</td><td>41.50 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.39 (+11.51%)</td><td>9.37 (+10.44%)</td><td>9.02 (+3.11%)</td><td>8.70 <b>(+22.12%)</b></td><td>0.71 (-13.98%)</td><td>10.37 (+11.51%)</td><td>9.36 (+10.44%)</td><td>9.00 (+3.11%)</td><td>8.68 <b>(+22.12%)</b></td><td>0.70 (-13.98%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.32 (n/a)</td><td>8.49 (n/a)</td><td>8.75 (n/a)</td><td>7.12 (n/a)</td><td>0.82 (n/a)</td><td>9.30 (n/a)</td><td>8.47 (n/a)</td><td>8.73 (n/a)</td><td>7.11 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.04 (+10.40%)</td><td>0.88 (+3.98%)</td><td>0.89 (+7.43%)</td><td>0.76 (-5.41%)</td><td>0.11 <b>(+95.70%)</b></td><td>1.03 (+10.40%)</td><td>0.87 (+3.98%)</td><td>0.88 (+7.43%)</td><td>0.75 (-5.41%)</td><td>0.11 <b>(+95.70%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.94 (n/a)</td><td>0.85 (n/a)</td><td>0.83 (n/a)</td><td>0.80 (n/a)</td><td>0.06 (n/a)</td><td>0.93 (n/a)</td><td>0.83 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.39 (+2.12%)</td><td>1.20 (+4.47%)</td><td>1.15 (-0.28%)</td><td>1.10 (+19.29%)</td><td>0.11 <b>(-28.57%)</b></td><td>1.37 (+2.12%)</td><td>1.19 (+4.47%)</td><td>1.14 (-0.28%)</td><td>1.09 (+19.29%)</td><td>0.11 <b>(-28.57%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.36 (n/a)</td><td>1.15 (n/a)</td><td>1.16 (n/a)</td><td>0.93 (n/a)</td><td>0.16 (n/a)</td><td>1.35 (n/a)</td><td>1.14 (n/a)</td><td>1.14 (n/a)</td><td>0.91 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>19.98 (+12.83%)</td><td>17.96 (+12.94%)</td><td>17.69 (+11.26%)</td><td>16.55 (+15.67%)</td><td>1.25 (-3.47%)</td><td>19.75 (+12.83%)</td><td>17.76 (+12.94%)</td><td>17.49 (+11.26%)</td><td>16.36 (+15.67%)</td><td>1.24 (-3.47%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>17.71 (n/a)</td><td>15.91 (n/a)</td><td>15.90 (n/a)</td><td>14.31 (n/a)</td><td>1.29 (n/a)</td><td>17.50 (n/a)</td><td>15.72 (n/a)</td><td>15.72 (n/a)</td><td>14.14 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>15.02 (+11.45%)</td><td>14.20 (+6.61%)</td><td>14.16 (+5.88%)</td><td>13.71 (+5.42%)</td><td>0.53 <b>(+181.92%)</b></td><td>14.75 (+11.45%)</td><td>13.95 (+6.61%)</td><td>13.91 (+5.88%)</td><td>13.47 (+5.42%)</td><td>0.52 <b>(+181.92%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>13.47 (n/a)</td><td>13.32 (n/a)</td><td>13.37 (n/a)</td><td>13.00 (n/a)</td><td>0.19 (n/a)</td><td>13.24 (n/a)</td><td>13.09 (n/a)</td><td>13.13 (n/a)</td><td>12.77 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.16 (+7.67%)</td><td>8.10 (+2.33%)</td><td>8.39 (+5.82%)</td><td>6.68 (-9.14%)</td><td>1.03 <b>(+137.58%)</b></td><td>9.00 (+7.67%)</td><td>7.96 (+2.33%)</td><td>8.25 (+5.82%)</td><td>6.56 (-9.14%)</td><td>1.02 <b>(+137.58%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>8.51 (n/a)</td><td>7.91 (n/a)</td><td>7.93 (n/a)</td><td>7.35 (n/a)</td><td>0.43 (n/a)</td><td>8.36 (n/a)</td><td>7.78 (n/a)</td><td>7.79 (n/a)</td><td>7.22 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.44 (+11.29%)</td><td>5.86 (+11.08%)</td><td>5.86 (+8.76%)</td><td>5.24 (+13.34%)</td><td>0.46 (+0.94%)</td><td>6.34 (+11.29%)</td><td>5.77 (+11.08%)</td><td>5.76 (+8.76%)</td><td>5.15 (+13.34%)</td><td>0.45 (+0.94%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>5.79 (n/a)</td><td>5.28 (n/a)</td><td>5.38 (n/a)</td><td>4.62 (n/a)</td><td>0.45 (n/a)</td><td>5.70 (n/a)</td><td>5.19 (n/a)</td><td>5.30 (n/a)</td><td>4.55 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.46 (n/a)</td><td>12.50 (n/a)</td><td>12.85 (n/a)</td><td>10.93 (n/a)</td><td>1.04 (n/a)</td><td>13.45 (n/a)</td><td>12.49 (n/a)</td><td>12.84 (n/a)</td><td>10.92 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.54 (n/a)</td><td>12.35 (n/a)</td><td>12.62 (n/a)</td><td>10.74 (n/a)</td><td>1.13 (n/a)</td><td>13.53 (n/a)</td><td>12.35 (n/a)</td><td>12.61 (n/a)</td><td>10.73 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>159.86 (n/a)</td><td>171.40 (n/a)</td><td>112.70 (n/a)</td><td>41.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.90 (n/a)</td><td>171.76 (n/a)</td><td>150.80 (n/a)</td><td>124.70 (n/a)</td><td>52.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.90 (n/a)</td><td>188.06 (n/a)</td><td>164.10 (n/a)</td><td>144.00 (n/a)</td><td>43.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>273.90 (n/a)</td><td>214.02 (n/a)</td><td>194.10 (n/a)</td><td>162.60 (n/a)</td><td>51.41 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.90 (n/a)</td><td>166.02 (n/a)</td><td>172.20 (n/a)</td><td>140.50 (n/a)</td><td>15.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>351.60 (n/a)</td><td>209.22 (n/a)</td><td>187.10 (n/a)</td><td>145.80 (n/a)</td><td>81.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.00 (n/a)</td><td>158.48 (n/a)</td><td>155.70 (n/a)</td><td>121.10 (n/a)</td><td>25.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.70 (n/a)</td><td>217.02 (n/a)</td><td>213.40 (n/a)</td><td>172.50 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>189.90 (n/a)</td><td>185.00 (n/a)</td><td>149.70 (n/a)</td><td>35.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>175.26 (n/a)</td><td>188.60 (n/a)</td><td>135.50 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.60 (n/a)</td><td>186.50 (n/a)</td><td>182.70 (n/a)</td><td>148.40 (n/a)</td><td>30.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.10 (n/a)</td><td>173.94 (n/a)</td><td>174.80 (n/a)</td><td>156.40 (n/a)</td><td>11.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>192.72 (n/a)</td><td>192.60 (n/a)</td><td>144.00 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>185.68 (n/a)</td><td>179.70 (n/a)</td><td>165.20 (n/a)</td><td>16.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>181.32 (n/a)</td><td>188.00 (n/a)</td><td>139.40 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>318.40 (n/a)</td><td>227.36 (n/a)</td><td>227.00 (n/a)</td><td>175.40 (n/a)</td><td>58.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.40 (n/a)</td><td>185.40 (n/a)</td><td>171.20 (n/a)</td><td>150.10 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.60 (n/a)</td><td>169.06 (n/a)</td><td>175.20 (n/a)</td><td>122.40 (n/a)</td><td>32.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>235.70 (n/a)</td><td>162.50 (n/a)</td><td>154.80 (n/a)</td><td>120.00 (n/a)</td><td>45.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.10 (n/a)</td><td>167.04 (n/a)</td><td>156.70 (n/a)</td><td>121.20 (n/a)</td><td>37.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>321.80 (n/a)</td><td>197.80 (n/a)</td><td>188.90 (n/a)</td><td>120.10 (n/a)</td><td>76.77 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>211.90 (n/a)</td><td>171.08 (n/a)</td><td>172.40 (n/a)</td><td>110.20 (n/a)</td><td>37.78 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>317.80 (n/a)</td><td>221.34 (n/a)</td><td>198.80 (n/a)</td><td>179.10 (n/a)</td><td>55.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>314.70 (n/a)</td><td>237.42 (n/a)</td><td>212.70 (n/a)</td><td>188.70 (n/a)</td><td>56.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>209.90 (n/a)</td><td>157.74 (n/a)</td><td>145.20 (n/a)</td><td>118.70 (n/a)</td><td>35.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>178.60 (n/a)</td><td>164.74 (n/a)</td><td>177.30 (n/a)</td><td>125.00 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>254.60 (n/a)</td><td>173.74 (n/a)</td><td>165.10 (n/a)</td><td>123.90 (n/a)</td><td>48.68 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>248.20 (n/a)</td><td>190.06 (n/a)</td><td>185.60 (n/a)</td><td>130.90 (n/a)</td><td>45.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>198.50 (n/a)</td><td>160.40 (n/a)</td><td>167.10 (n/a)</td><td>104.00 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>209.50 (n/a)</td><td>179.76 (n/a)</td><td>180.70 (n/a)</td><td>147.30 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.10 (n/a)</td><td>180.70 (n/a)</td><td>192.70 (n/a)</td><td>126.00 (n/a)</td><td>33.78 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.29 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>323.00 (n/a)</td><td>224.02 (n/a)</td><td>199.10 (n/a)</td><td>113.80 (n/a)</td><td>92.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-7.29%)</td><td>0.03 (-0.05%)</td><td>0.03 (+1.93%)</td><td>0.02 (+11.16%)</td><td>0.01 <b>(-24.02%)</b></td><td>185.80 (-10.02%)</td><td>150.48 (-2.04%)</td><td>148.70 (-1.85%)</td><td>121.50 (+7.81%)</td><td>28.18 <b>(-26.40%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>153.62 (n/a)</td><td>151.50 (n/a)</td><td>112.70 (n/a)</td><td>38.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (+11.97%)</td><td>0.02 (-18.30%)</td><td>0.02 <b>(-37.83%)</b></td><td>0.02 (-8.78%)</td><td>0.01 (+18.11%)</td><td>251.90 (+9.62%)</td><td>190.42 <b>(+25.23%)</b></td><td>206.80 <b>(+60.93%)</b></td><td>94.70 (-10.66%)</td><td>58.23 (+8.08%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>152.06 (n/a)</td><td>128.50 (n/a)</td><td>106.00 (n/a)</td><td>53.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+10.71%)</td><td>0.03 (+16.98%)</td><td>0.03 (+12.17%)</td><td>0.02 <b>(+52.09%)</b></td><td>0.01 (-19.35%)</td><td>202.60 <b>(-34.24%)</b></td><td>159.48 (-18.46%)</td><td>161.00 (-10.85%)</td><td>119.10 (-9.70%)</td><td>29.75 <b>(-55.17%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>308.10 (n/a)</td><td>195.58 (n/a)</td><td>180.60 (n/a)</td><td>131.90 (n/a)</td><td>66.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (+19.93%)</td><td>0.02 (-5.76%)</td><td>0.02 (-17.45%)</td><td>0.02 (-10.74%)</td><td>0.01 <b>(+83.72%)</b></td><td>238.50 (+12.02%)</td><td>183.98 (+10.10%)</td><td>189.70 <b>(+21.14%)</b></td><td>116.30 (-16.63%)</td><td>44.60 <b>(+59.71%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>167.10 (n/a)</td><td>156.60 (n/a)</td><td>139.50 (n/a)</td><td>27.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-11.05%)</td><td>0.02 <b>(-21.13%)</b></td><td>0.02 <b>(-21.87%)</b></td><td>0.01 <b>(-48.72%)</b></td><td>0.01 <b>(+91.41%)</b></td><td>323.30 <b>(+94.99%)</b></td><td>198.96 <b>(+36.26%)</b></td><td>182.90 <b>(+27.99%)</b></td><td>141.40 (+12.40%)</td><td>72.55 <b>(+331.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>165.80 (n/a)</td><td>146.02 (n/a)</td><td>142.90 (n/a)</td><td>125.80 (n/a)</td><td>16.80 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-14.01%)</td><td>0.02 (-15.96%)</td><td>0.02 (-3.14%)</td><td>0.01 <b>(-34.00%)</b></td><td>0.00 (+5.25%)</td><td>311.00 <b>(+51.49%)</b></td><td>208.86 <b>(+22.38%)</b></td><td>191.10 (+3.24%)</td><td>156.20 (+16.31%)</td><td>60.86 <b>(+95.68%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.30 (n/a)</td><td>170.66 (n/a)</td><td>185.10 (n/a)</td><td>134.30 (n/a)</td><td>31.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 <b>(+26.21%)</b></td><td>0.03 <b>(+32.69%)</b></td><td>0.02 <b>(+23.38%)</b></td><td>0.02 <b>(+56.03%)</b></td><td>0.00 (+12.53%)</td><td>182.10 <b>(-35.90%)</b></td><td>162.06 <b>(-25.42%)</b></td><td>177.40 (-18.96%)</td><td>129.50 <b>(-20.75%)</b></td><td>25.27 <b>(-42.18%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>284.10 (n/a)</td><td>217.30 (n/a)</td><td>218.90 (n/a)</td><td>163.40 (n/a)</td><td>43.70 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (-12.40%)</td><td>0.02 (-9.27%)</td><td>0.02 (-8.92%)</td><td>0.02 (-10.38%)</td><td>0.00 (-19.58%)</td><td>240.30 (+11.61%)</td><td>214.84 (+9.86%)</td><td>226.80 (+9.78%)</td><td>169.40 (+14.15%)</td><td>28.41 (+2.52%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.30 (n/a)</td><td>195.56 (n/a)</td><td>206.60 (n/a)</td><td>148.40 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-15.77%)</td><td>0.05 (-2.46%)</td><td>0.05 (-6.84%)</td><td>0.05 <b>(+34.37%)</b></td><td>0.00 <b>(-74.95%)</b></td><td>160.20 <b>(-25.59%)</b></td><td>152.40 (-1.24%)</td><td>156.40 (+7.34%)</td><td>140.90 (+18.70%)</td><td>7.86 <b>(-78.65%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>154.32 (n/a)</td><td>145.70 (n/a)</td><td>118.70 (n/a)</td><td>36.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (+1.68%)</td><td>0.05 (+2.10%)</td><td>0.05 (+9.75%)</td><td>0.04 (-13.34%)</td><td>0.01 (+3.62%)</td><td>226.60 (+15.38%)</td><td>163.92 (-1.37%)</td><td>171.40 (-8.93%)</td><td>123.20 (-1.60%)</td><td>42.10 (+14.31%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>166.20 (n/a)</td><td>188.20 (n/a)</td><td>125.20 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (+11.62%)</td><td>0.06 (+11.62%)</td><td>0.07 <b>(+32.71%)</b></td><td>0.04 (-2.17%)</td><td>0.01 <b>(+76.62%)</b></td><td>192.90 (+2.23%)</td><td>147.78 (-8.14%)</td><td>124.10 <b>(-24.61%)</b></td><td>123.30 (-10.39%)</td><td>33.74 <b>(+59.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>160.88 (n/a)</td><td>164.60 (n/a)</td><td>137.60 (n/a)</td><td>21.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-3.97%)</td><td>0.05 (+9.17%)</td><td>0.06 <b>(+21.53%)</b></td><td>0.03 (-6.29%)</td><td>0.01 (+7.48%)</td><td>262.80 (+6.74%)</td><td>171.60 (-7.25%)</td><td>144.80 (-17.73%)</td><td>142.40 (+4.09%)</td><td>51.84 (+19.77%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.20 (n/a)</td><td>185.02 (n/a)</td><td>176.00 (n/a)</td><td>136.80 (n/a)</td><td>43.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (+14.46%)</td><td>0.05 (+13.55%)</td><td>0.06 <b>(+22.86%)</b></td><td>0.04 (+9.62%)</td><td>0.01 (+18.63%)</td><td>187.20 (-8.77%)</td><td>153.24 (-11.75%)</td><td>141.90 (-18.64%)</td><td>131.00 (-12.67%)</td><td>22.60 (-2.84%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>173.64 (n/a)</td><td>174.40 (n/a)</td><td>150.00 (n/a)</td><td>23.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (-6.48%)</td><td>0.05 (-1.21%)</td><td>0.06 (-7.58%)</td><td>0.04 (+8.87%)</td><td>0.01 <b>(-26.64%)</b></td><td>201.90 (-8.14%)</td><td>157.24 (-1.75%)</td><td>147.40 (+8.22%)</td><td>125.90 (+6.88%)</td><td>32.67 <b>(-29.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>160.04 (n/a)</td><td>136.20 (n/a)</td><td>117.80 (n/a)</td><td>46.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (+6.55%)</td><td>0.05 (-2.90%)</td><td>0.05 (-3.03%)</td><td>0.05 (-1.16%)</td><td>0.01 <b>(+29.10%)</b></td><td>176.90 (+1.20%)</td><td>155.18 (+3.66%)</td><td>157.80 (+3.07%)</td><td>121.20 (-6.19%)</td><td>22.23 <b>(+23.24%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.80 (n/a)</td><td>149.70 (n/a)</td><td>153.10 (n/a)</td><td>129.20 (n/a)</td><td>18.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (-12.00%)</td><td>0.05 (-1.50%)</td><td>0.05 (+3.25%)</td><td>0.04 (+3.03%)</td><td>0.01 <b>(-35.27%)</b></td><td>203.20 (-2.91%)</td><td>165.84 (+0.16%)</td><td>155.20 (-3.12%)</td><td>149.20 (+13.63%)</td><td>21.82 <b>(-27.73%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>165.58 (n/a)</td><td>160.20 (n/a)</td><td>131.30 (n/a)</td><td>30.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (+8.05%)</td><td>0.05 (+7.77%)</td><td>0.05 (+11.24%)</td><td>0.04 (+6.62%)</td><td>0.01 <b>(+29.24%)</b></td><td>206.30 (-6.18%)</td><td>172.26 (-6.72%)</td><td>154.50 (-10.07%)</td><td>153.00 (-7.44%)</td><td>25.91 (+10.82%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>184.66 (n/a)</td><td>171.80 (n/a)</td><td>165.30 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (+8.18%)</td><td>0.04 (-10.15%)</td><td>0.04 (-11.04%)</td><td>0.03 <b>(-26.99%)</b></td><td>0.01 <b>(+108.98%)</b></td><td>314.20 <b>(+36.97%)</b></td><td>234.10 (+15.26%)</td><td>212.90 (+12.41%)</td><td>173.40 (-7.57%)</td><td>55.46 <b>(+171.30%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>229.40 (n/a)</td><td>203.10 (n/a)</td><td>189.40 (n/a)</td><td>187.60 (n/a)</td><td>20.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (-14.39%)</td><td>0.11 (+1.22%)</td><td>0.11 (-4.55%)</td><td>0.10 <b>(+22.48%)</b></td><td>0.01 <b>(-70.51%)</b></td><td>160.50 (-18.36%)</td><td>149.90 (-4.51%)</td><td>150.20 (+4.74%)</td><td>135.90 (+16.85%)</td><td>9.09 <b>(-72.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.60 (n/a)</td><td>156.98 (n/a)</td><td>143.40 (n/a)</td><td>116.30 (n/a)</td><td>33.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (+3.82%)</td><td>0.09 (-3.91%)</td><td>0.09 (-7.89%)</td><td>0.06 <b>(-38.19%)</b></td><td>0.03 <b>(+153.15%)</b></td><td>290.30 <b>(+61.82%)</b></td><td>187.78 (+11.73%)</td><td>186.30 (+8.57%)</td><td>134.30 (-3.73%)</td><td>63.54 <b>(+286.57%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.40 (n/a)</td><td>168.06 (n/a)</td><td>171.60 (n/a)</td><td>139.50 (n/a)</td><td>16.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 <b>(+30.75%)</b></td><td>0.11 (+13.58%)</td><td>0.11 <b>(+25.20%)</b></td><td>0.07 (-12.23%)</td><td>0.03 <b>(+279.28%)</b></td><td>221.20 (+13.90%)</td><td>164.24 (-7.66%)</td><td>145.30 <b>(-20.12%)</b></td><td>125.10 <b>(-23.53%)</b></td><td>43.11 <b>(+233.75%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.20 (n/a)</td><td>177.86 (n/a)</td><td>181.90 (n/a)</td><td>163.60 (n/a)</td><td>12.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 <b>(+48.41%)</b></td><td>0.11 <b>(+20.77%)</b></td><td>0.11 (+12.14%)</td><td>0.08 (+3.61%)</td><td>0.02 <b>(+212.92%)</b></td><td>193.20 (-3.45%)</td><td>147.82 (-14.78%)</td><td>149.60 (-10.79%)</td><td>109.40 <b>(-32.64%)</b></td><td>30.67 <b>(+100.67%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>173.46 (n/a)</td><td>167.70 (n/a)</td><td>162.40 (n/a)</td><td>15.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (+5.57%)</td><td>0.11 (+11.88%)</td><td>0.11 (+14.96%)</td><td>0.08 (+11.62%)</td><td>0.02 (-7.65%)</td><td>200.30 (-10.42%)</td><td>152.44 (-11.41%)</td><td>149.00 (-13.02%)</td><td>126.70 (-5.24%)</td><td>29.27 <b>(-20.01%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.60 (n/a)</td><td>172.08 (n/a)</td><td>171.30 (n/a)</td><td>133.70 (n/a)</td><td>36.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (-4.87%)</td><td>0.09 (+11.16%)</td><td>0.09 (+6.15%)</td><td>0.08 <b>(+35.65%)</b></td><td>0.01 <b>(-40.13%)</b></td><td>214.70 <b>(-26.30%)</b></td><td>178.60 (-13.50%)</td><td>183.20 (-5.81%)</td><td>153.40 (+5.14%)</td><td>25.01 <b>(-55.03%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>291.30 (n/a)</td><td>206.48 (n/a)</td><td>194.50 (n/a)</td><td>145.90 (n/a)</td><td>55.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (+5.41%)</td><td>0.09 (-11.51%)</td><td>0.08 (-19.49%)</td><td>0.05 <b>(-33.04%)</b></td><td>0.03 <b>(+60.52%)</b></td><td>327.10 <b>(+49.36%)</b></td><td>213.38 <b>(+21.46%)</b></td><td>215.20 <b>(+24.18%)</b></td><td>125.90 (-5.20%)</td><td>76.21 <b>(+125.54%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.00 (n/a)</td><td>175.68 (n/a)</td><td>173.30 (n/a)</td><td>132.80 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.09 <b>(-25.76%)</b></td><td>0.07 (+1.43%)</td><td>0.08 (+15.19%)</td><td>0.06 (+11.26%)</td><td>0.01 <b>(-55.25%)</b></td><td>292.50 (-10.14%)</td><td>225.64 (-8.68%)</td><td>208.70 (-13.19%)</td><td>180.50 <b>(+34.70%)</b></td><td>43.00 <b>(-45.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>325.50 (n/a)</td><td>247.10 (n/a)</td><td>240.40 (n/a)</td><td>134.00 (n/a)</td><td>79.09 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (-11.71%)</td><td>0.22 (-7.05%)</td><td>0.21 (-9.76%)</td><td>0.18 (-3.04%)</td><td>0.03 <b>(-37.47%)</b></td><td>183.70 (+3.14%)</td><td>153.76 (+5.46%)</td><td>153.80 (+10.81%)</td><td>124.80 (+13.25%)</td><td>21.32 <b>(-30.06%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>178.10 (n/a)</td><td>145.80 (n/a)</td><td>138.80 (n/a)</td><td>110.20 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (-9.61%)</td><td>0.21 (-8.71%)</td><td>0.21 (-12.78%)</td><td>0.18 (+0.82%)</td><td>0.02 <b>(-33.74%)</b></td><td>179.10 (-0.83%)</td><td>157.82 (+8.33%)</td><td>156.30 (+14.67%)</td><td>133.00 (+10.65%)</td><td>17.35 <b>(-28.44%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>180.60 (n/a)</td><td>145.68 (n/a)</td><td>136.30 (n/a)</td><td>120.20 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 <b>(-28.72%)</b></td><td>0.19 <b>(-24.78%)</b></td><td>0.18 <b>(-25.20%)</b></td><td>0.14 <b>(-24.98%)</b></td><td>0.03 <b>(-30.49%)</b></td><td>226.80 <b>(+33.33%)</b></td><td>179.88 <b>(+32.64%)</b></td><td>179.60 <b>(+33.63%)</b></td><td>155.80 <b>(+40.23%)</b></td><td>28.76 <b>(+28.61%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>170.10 (n/a)</td><td>135.62 (n/a)</td><td>134.40 (n/a)</td><td>111.10 (n/a)</td><td>22.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.24 (-16.45%)</td><td>0.19 <b>(-20.84%)</b></td><td>0.19 <b>(-21.58%)</b></td><td>0.14 <b>(-22.59%)</b></td><td>0.04 (-11.71%)</td><td>234.60 <b>(+29.19%)</b></td><td>178.08 <b>(+27.09%)</b></td><td>174.20 <b>(+27.53%)</b></td><td>139.10 (+19.71%)</td><td>37.40 <b>(+38.97%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>181.60 (n/a)</td><td>140.12 (n/a)</td><td>136.60 (n/a)</td><td>116.20 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.29 (+16.85%)</td><td>0.19 (-5.10%)</td><td>0.18 (-3.36%)</td><td>0.12 <b>(-23.04%)</b></td><td>0.06 <b>(+52.41%)</b></td><td>264.90 <b>(+29.98%)</b></td><td>187.24 (+9.83%)</td><td>185.00 (+3.47%)</td><td>114.30 (-14.45%)</td><td>53.51 <b>(+65.63%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>203.80 (n/a)</td><td>170.48 (n/a)</td><td>178.80 (n/a)</td><td>133.60 (n/a)</td><td>32.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.22 <b>(-28.22%)</b></td><td>0.19 (-7.99%)</td><td>0.20 (-1.78%)</td><td>0.15 (+5.16%)</td><td>0.03 <b>(-53.55%)</b></td><td>215.90 (-4.93%)</td><td>173.64 (+4.43%)</td><td>165.70 (+1.84%)</td><td>150.20 <b>(+39.33%)</b></td><td>26.96 <b>(-37.15%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>227.10 (n/a)</td><td>166.28 (n/a)</td><td>162.70 (n/a)</td><td>107.80 (n/a)</td><td>42.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (+3.73%)</td><td>0.18 (+11.59%)</td><td>0.20 <b>(+25.56%)</b></td><td>0.14 (+0.69%)</td><td>0.03 <b>(+26.82%)</b></td><td>236.50 (-0.71%)</td><td>184.62 (-9.50%)</td><td>160.90 <b>(-20.35%)</b></td><td>155.90 (-3.59%)</td><td>37.32 (+17.28%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>238.20 (n/a)</td><td>204.00 (n/a)</td><td>202.00 (n/a)</td><td>161.70 (n/a)</td><td>31.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 <b>(+20.20%)</b></td><td>0.03 (+13.10%)</td><td>0.03 <b>(+23.15%)</b></td><td>0.02 (+18.46%)</td><td>0.01 <b>(+46.80%)</b></td><td>189.10 (-15.58%)</td><td>140.74 (-9.65%)</td><td>122.00 (-18.77%)</td><td>104.20 (-16.84%)</td><td>40.92 (+2.56%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>155.78 (n/a)</td><td>150.20 (n/a)</td><td>125.30 (n/a)</td><td>39.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+2.69%)</td><td>0.03 (+2.75%)</td><td>0.03 (-4.15%)</td><td>0.02 (+11.34%)</td><td>0.01 (-5.01%)</td><td>210.30 (-10.17%)</td><td>153.96 (-3.79%)</td><td>149.30 (+4.33%)</td><td>118.00 (-2.64%)</td><td>35.91 (-19.03%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.10 (n/a)</td><td>160.02 (n/a)</td><td>143.10 (n/a)</td><td>121.20 (n/a)</td><td>44.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.00 (-0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 <b>(-44.43%)</b></td><td>4746071.60 (+0.00%)</td><td>4746048.43 (+0.00%)</td><td>4746054.20 (+0.00%)</td><td>4746019.50 (+0.00%)</td><td>26.52 <b>(-44.67%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4746009.70 (n/a)</td><td>4745975.80 (n/a)</td><td>4745975.80 (n/a)</td><td>4745941.90 (n/a)</td><td>47.94 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (-12.33%)</td><td>0.02 (-10.40%)</td><td>0.02 (-11.84%)</td><td>0.02 (+2.68%)</td><td>0.00 (-17.12%)</td><td>234.50 (-2.58%)</td><td>198.60 (+10.84%)</td><td>188.70 (+13.40%)</td><td>168.40 (+14.09%)</td><td>33.10 (-9.72%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.70 (n/a)</td><td>179.18 (n/a)</td><td>166.40 (n/a)</td><td>147.60 (n/a)</td><td>36.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 <b>(+20.53%)</b></td><td>0.02 (+14.29%)</td><td>0.02 (+13.57%)</td><td>0.02 (-8.00%)</td><td>0.01 <b>(+93.10%)</b></td><td>259.20 (+8.68%)</td><td>178.38 (-9.73%)</td><td>164.00 (-11.92%)</td><td>141.60 (-17.05%)</td><td>46.85 <b>(+78.67%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.50 (n/a)</td><td>197.60 (n/a)</td><td>186.20 (n/a)</td><td>170.70 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-4.76%)</td><td>0.03 (-5.67%)</td><td>0.02 (-0.13%)</td><td>0.02 (-2.24%)</td><td>0.00 (-17.46%)</td><td>209.70 (+2.29%)</td><td>165.50 (+5.01%)</td><td>166.80 (+0.18%)</td><td>126.00 (+5.00%)</td><td>31.11 (-9.50%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>157.60 (n/a)</td><td>166.50 (n/a)</td><td>120.00 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+15.78%)</td><td>0.03 <b>(+28.38%)</b></td><td>0.03 <b>(+34.77%)</b></td><td>0.02 <b>(+26.97%)</b></td><td>0.00 (+10.42%)</td><td>204.20 <b>(-21.25%)</b></td><td>146.72 <b>(-22.54%)</b></td><td>133.10 <b>(-25.81%)</b></td><td>127.40 (-13.63%)</td><td>32.36 <b>(-24.67%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>259.30 (n/a)</td><td>189.42 (n/a)</td><td>179.40 (n/a)</td><td>147.50 (n/a)</td><td>42.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 <b>(+28.27%)</b></td><td>0.03 <b>(+32.99%)</b></td><td>0.02 (+8.27%)</td><td>0.02 <b>(+69.68%)</b></td><td>0.01 (-1.72%)</td><td>210.20 <b>(-41.07%)</b></td><td>164.54 <b>(-28.36%)</b></td><td>175.80 (-7.62%)</td><td>120.30 <b>(-22.03%)</b></td><td>35.23 <b>(-56.54%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>356.70 (n/a)</td><td>229.68 (n/a)</td><td>190.30 (n/a)</td><td>154.30 (n/a)</td><td>81.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-7.61%)</td><td>0.03 (+8.15%)</td><td>0.02 (+4.02%)</td><td>0.02 (+3.46%)</td><td>0.01 (-9.52%)</td><td>199.90 (-3.38%)</td><td>158.08 (-8.28%)</td><td>166.60 (-3.87%)</td><td>118.20 (+8.24%)</td><td>36.68 (-7.48%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>172.36 (n/a)</td><td>173.30 (n/a)</td><td>109.20 (n/a)</td><td>39.65 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-0.47%)</td><td>0.02 (-4.02%)</td><td>0.02 (-6.28%)</td><td>0.02 (-4.09%)</td><td>0.00 (+5.08%)</td><td>209.90 (+4.27%)</td><td>188.82 (+4.33%)</td><td>188.10 (+6.69%)</td><td>154.30 (+0.52%)</td><td>21.69 (+6.53%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.30 (n/a)</td><td>180.98 (n/a)</td><td>176.30 (n/a)</td><td>153.50 (n/a)</td><td>20.36 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-11.16%)</td><td>0.03 (-11.50%)</td><td>0.03 (-15.06%)</td><td>0.02 (-10.71%)</td><td>0.01 (-13.78%)</td><td>242.70 (+12.00%)</td><td>170.56 (+12.66%)</td><td>160.40 (+17.68%)</td><td>125.90 (+12.51%)</td><td>43.36 (+9.20%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>151.40 (n/a)</td><td>136.30 (n/a)</td><td>111.90 (n/a)</td><td>39.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-0.28%)</td><td>0.02 (-12.78%)</td><td>0.02 (-17.95%)</td><td>0.02 (-17.73%)</td><td>0.01 <b>(+51.39%)</b></td><td>224.70 <b>(+21.53%)</b></td><td>183.42 (+17.62%)</td><td>194.80 <b>(+21.90%)</b></td><td>130.50 (+0.23%)</td><td>38.94 <b>(+85.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.90 (n/a)</td><td>155.94 (n/a)</td><td>159.80 (n/a)</td><td>130.20 (n/a)</td><td>21.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+4.27%)</td><td>0.03 (+12.78%)</td><td>0.03 (+2.61%)</td><td>0.02 <b>(+53.49%)</b></td><td>0.00 <b>(-48.05%)</b></td><td>174.40 <b>(-34.85%)</b></td><td>145.56 (-16.49%)</td><td>146.40 (-2.53%)</td><td>124.00 (-4.02%)</td><td>18.90 <b>(-67.19%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>267.70 (n/a)</td><td>174.30 (n/a)</td><td>150.20 (n/a)</td><td>129.20 (n/a)</td><td>57.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 <b>(+48.76%)</b></td><td>0.03 <b>(+25.88%)</b></td><td>0.03 <b>(+20.75%)</b></td><td>0.02 (+8.33%)</td><td>0.01 <b>(+156.28%)</b></td><td>214.20 (-7.71%)</td><td>164.62 (-18.59%)</td><td>159.40 (-17.19%)</td><td>124.50 <b>(-32.78%)</b></td><td>33.63 <b>(+61.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.10 (n/a)</td><td>202.20 (n/a)</td><td>192.50 (n/a)</td><td>185.20 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 <b>(-21.41%)</b></td><td>0.02 (-3.43%)</td><td>0.02 (-2.68%)</td><td>0.02 (+12.28%)</td><td>0.00 <b>(-69.30%)</b></td><td>186.50 (-10.94%)</td><td>167.30 (+0.66%)</td><td>164.20 (+2.75%)</td><td>158.10 <b>(+27.29%)</b></td><td>11.41 <b>(-65.15%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>166.20 (n/a)</td><td>159.80 (n/a)</td><td>124.20 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+8.56%)</td><td>0.03 (+3.37%)</td><td>0.03 (+7.66%)</td><td>0.02 (-0.48%)</td><td>0.00 <b>(+28.73%)</b></td><td>179.60 (+0.50%)</td><td>156.38 (-2.72%)</td><td>150.60 (-7.15%)</td><td>127.80 (-7.93%)</td><td>21.82 <b>(+20.48%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.70 (n/a)</td><td>160.76 (n/a)</td><td>162.20 (n/a)</td><td>138.80 (n/a)</td><td>18.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-6.07%)</td><td>0.05 (+1.19%)</td><td>0.05 (+0.36%)</td><td>0.04 (+1.27%)</td><td>0.01 (-15.73%)</td><td>184.10 (-1.23%)</td><td>158.64 (-1.88%)</td><td>168.90 (-0.35%)</td><td>126.50 (+6.48%)</td><td>24.87 (-12.30%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.40 (n/a)</td><td>161.68 (n/a)</td><td>169.50 (n/a)</td><td>118.80 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-17.21%)</td><td>0.05 (-9.99%)</td><td>0.05 (-10.64%)</td><td>0.04 (-9.19%)</td><td>0.01 <b>(-23.26%)</b></td><td>193.80 (+10.18%)</td><td>159.98 (+10.50%)</td><td>162.10 (+11.95%)</td><td>131.00 <b>(+20.74%)</b></td><td>25.79 (+2.56%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.90 (n/a)</td><td>144.78 (n/a)</td><td>144.80 (n/a)</td><td>108.50 (n/a)</td><td>25.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 <b>(+38.97%)</b></td><td>0.05 <b>(+25.64%)</b></td><td>0.05 <b>(+30.47%)</b></td><td>0.03 (+2.94%)</td><td>0.01 <b>(+122.60%)</b></td><td>297.90 (-2.84%)</td><td>193.16 (-15.64%)</td><td>170.70 <b>(-23.38%)</b></td><td>137.20 <b>(-28.02%)</b></td><td>67.37 <b>(+47.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>306.60 (n/a)</td><td>228.96 (n/a)</td><td>222.80 (n/a)</td><td>190.60 (n/a)</td><td>45.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (-8.36%)</td><td>0.05 (+2.95%)</td><td>0.04 (-3.60%)</td><td>0.04 <b>(+37.05%)</b></td><td>0.01 <b>(-55.47%)</b></td><td>206.50 <b>(-27.03%)</b></td><td>180.24 (-7.66%)</td><td>185.90 (+3.74%)</td><td>155.10 (+9.15%)</td><td>19.89 <b>(-64.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.00 (n/a)</td><td>195.20 (n/a)</td><td>179.20 (n/a)</td><td>142.10 (n/a)</td><td>56.68 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 <b>(+39.96%)</b></td><td>0.05 (+12.03%)</td><td>0.05 (+16.70%)</td><td>0.04 (-5.39%)</td><td>0.01 <b>(+312.34%)</b></td><td>193.30 (+5.69%)</td><td>159.94 (-7.32%)</td><td>152.50 (-14.33%)</td><td>112.00 <b>(-28.53%)</b></td><td>34.24 <b>(+220.53%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>182.90 (n/a)</td><td>172.58 (n/a)</td><td>178.00 (n/a)</td><td>156.70 (n/a)</td><td>10.68 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-19.35%)</td><td>0.05 (-4.49%)</td><td>0.05 (-3.26%)</td><td>0.04 (+4.34%)</td><td>0.01 <b>(-37.07%)</b></td><td>206.60 (-4.17%)</td><td>164.16 (+2.25%)</td><td>160.50 (+3.35%)</td><td>137.90 <b>(+24.01%)</b></td><td>28.17 <b>(-25.52%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>160.54 (n/a)</td><td>155.30 (n/a)</td><td>111.20 (n/a)</td><td>37.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-12.65%)</td><td>0.05 (-0.32%)</td><td>0.05 (+4.35%)</td><td>0.05 (+19.67%)</td><td>0.00 <b>(-55.76%)</b></td><td>171.80 (-16.44%)</td><td>157.98 (-1.81%)</td><td>156.00 (-4.18%)</td><td>145.50 (+14.48%)</td><td>12.64 <b>(-57.69%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>160.90 (n/a)</td><td>162.80 (n/a)</td><td>127.10 (n/a)</td><td>29.87 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (-11.58%)</td><td>0.05 (-12.67%)</td><td>0.05 (-18.09%)</td><td>0.05 (+8.02%)</td><td>0.01 <b>(-32.14%)</b></td><td>173.90 (-7.40%)</td><td>159.58 (+12.48%)</td><td>166.40 <b>(+22.08%)</b></td><td>123.10 (+13.14%)</td><td>21.01 <b>(-30.70%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>141.88 (n/a)</td><td>136.30 (n/a)</td><td>108.80 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (+12.53%)</td><td>0.05 (-5.56%)</td><td>0.05 (-14.29%)</td><td>0.04 (-4.20%)</td><td>0.01 <b>(+47.75%)</b></td><td>197.60 (+4.38%)</td><td>164.24 (+7.81%)</td><td>163.90 (+16.65%)</td><td>117.70 (-11.17%)</td><td>32.93 <b>(+38.96%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>152.34 (n/a)</td><td>140.50 (n/a)</td><td>132.50 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 <b>(-38.66%)</b></td><td>0.05 <b>(-20.95%)</b></td><td>0.05 <b>(-21.38%)</b></td><td>0.05 (+12.19%)</td><td>0.00 <b>(-88.36%)</b></td><td>171.70 (-10.90%)</td><td>162.44 (+18.31%)</td><td>161.70 <b>(+27.12%)</b></td><td>153.30 <b>(+63.09%)</b></td><td>6.76 <b>(-83.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>192.70 (n/a)</td><td>137.30 (n/a)</td><td>127.20 (n/a)</td><td>94.00 (n/a)</td><td>40.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (+14.85%)</td><td>0.06 (+6.07%)</td><td>0.06 (+7.94%)</td><td>0.04 (-4.52%)</td><td>0.01 <b>(+52.40%)</b></td><td>199.90 (+4.77%)</td><td>151.36 (-4.07%)</td><td>147.10 (-7.37%)</td><td>112.90 (-12.95%)</td><td>31.42 <b>(+40.05%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>157.78 (n/a)</td><td>158.80 (n/a)</td><td>129.70 (n/a)</td><td>22.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-14.08%)</td><td>0.05 (-6.14%)</td><td>0.05 (-10.11%)</td><td>0.05 (+1.28%)</td><td>0.00 <b>(-48.01%)</b></td><td>180.00 (-1.26%)</td><td>166.66 (+5.43%)</td><td>172.70 (+11.28%)</td><td>148.40 (+16.39%)</td><td>12.66 <b>(-40.43%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>158.08 (n/a)</td><td>155.20 (n/a)</td><td>127.50 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 <b>(+29.06%)</b></td><td>0.05 <b>(+27.69%)</b></td><td>0.05 <b>(+29.03%)</b></td><td>0.04 (+10.06%)</td><td>0.01 <b>(+69.14%)</b></td><td>201.80 (-9.14%)</td><td>153.78 <b>(-20.49%)</b></td><td>157.60 <b>(-22.52%)</b></td><td>123.90 <b>(-22.51%)</b></td><td>31.29 (+17.94%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.10 (n/a)</td><td>193.42 (n/a)</td><td>203.40 (n/a)</td><td>159.90 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (+17.36%)</td><td>0.05 (+12.08%)</td><td>0.05 (+8.06%)</td><td>0.05 (+18.81%)</td><td>0.00 (+1.76%)</td><td>173.90 (-15.83%)</td><td>157.70 (-10.94%)</td><td>158.30 (-7.48%)</td><td>139.40 (-14.79%)</td><td>12.37 <b>(-28.56%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.60 (n/a)</td><td>177.08 (n/a)</td><td>171.10 (n/a)</td><td>163.60 (n/a)</td><td>17.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-11.26%)</td><td>0.05 (+5.50%)</td><td>0.05 (+12.64%)</td><td>0.05 (+18.06%)</td><td>0.00 <b>(-59.08%)</b></td><td>175.70 (-15.33%)</td><td>163.16 (-7.26%)</td><td>160.20 (-11.25%)</td><td>146.30 (+12.71%)</td><td>11.90 <b>(-59.95%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>175.94 (n/a)</td><td>180.50 (n/a)</td><td>129.80 (n/a)</td><td>29.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 <b>(+42.28%)</b></td><td>0.06 <b>(+35.92%)</b></td><td>0.06 <b>(+26.18%)</b></td><td>0.05 <b>(+55.38%)</b></td><td>0.01 <b>(+30.32%)</b></td><td>153.60 <b>(-35.62%)</b></td><td>136.40 <b>(-26.75%)</b></td><td>139.30 <b>(-20.76%)</b></td><td>114.50 <b>(-29.75%)</b></td><td>18.10 <b>(-41.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.60 (n/a)</td><td>186.20 (n/a)</td><td>175.80 (n/a)</td><td>163.00 (n/a)</td><td>30.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 <b>(+29.78%)</b></td><td>0.12 <b>(+23.26%)</b></td><td>0.12 (+19.05%)</td><td>0.09 (+8.84%)</td><td>0.02 <b>(+108.17%)</b></td><td>175.80 (-8.10%)</td><td>141.46 (-17.64%)</td><td>138.90 (-16.02%)</td><td>116.40 <b>(-22.96%)</b></td><td>24.26 <b>(+44.49%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>171.76 (n/a)</td><td>165.40 (n/a)</td><td>151.10 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (+13.62%)</td><td>0.11 (+1.34%)</td><td>0.10 (-1.06%)</td><td>0.10 (+8.64%)</td><td>0.02 (+9.29%)</td><td>170.80 (-7.92%)</td><td>152.82 (-1.36%)</td><td>165.80 (+1.10%)</td><td>110.00 (-12.00%)</td><td>25.21 (-9.70%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.50 (n/a)</td><td>154.92 (n/a)</td><td>164.00 (n/a)</td><td>125.00 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (-18.12%)</td><td>0.08 (+3.16%)</td><td>0.08 (+8.54%)</td><td>0.07 <b>(+56.95%)</b></td><td>0.01 <b>(-62.00%)</b></td><td>222.80 <b>(-36.29%)</b></td><td>203.32 (-10.74%)</td><td>214.20 (-7.83%)</td><td>167.60 <b>(+22.16%)</b></td><td>23.53 <b>(-70.25%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>349.70 (n/a)</td><td>227.78 (n/a)</td><td>232.40 (n/a)</td><td>137.20 (n/a)</td><td>79.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (+10.60%)</td><td>0.09 (+19.03%)</td><td>0.09 (+15.79%)</td><td>0.08 <b>(+41.30%)</b></td><td>0.01 <b>(-22.88%)</b></td><td>203.80 <b>(-29.24%)</b></td><td>185.32 (-17.38%)</td><td>192.30 (-13.65%)</td><td>156.90 (-9.62%)</td><td>20.78 <b>(-50.43%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>288.00 (n/a)</td><td>224.30 (n/a)</td><td>222.70 (n/a)</td><td>173.60 (n/a)</td><td>41.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (+0.84%)</td><td>0.10 (+3.92%)</td><td>0.09 (+4.60%)</td><td>0.08 (+7.68%)</td><td>0.01 (-13.63%)</td><td>197.10 (-7.16%)</td><td>171.60 (-4.27%)</td><td>176.00 (-4.40%)</td><td>147.90 (-0.80%)</td><td>20.51 <b>(-20.57%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>179.26 (n/a)</td><td>184.10 (n/a)</td><td>149.10 (n/a)</td><td>25.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (+0.99%)</td><td>0.11 (+18.06%)</td><td>0.11 <b>(+29.56%)</b></td><td>0.10 <b>(+21.16%)</b></td><td>0.02 <b>(-28.59%)</b></td><td>167.40 (-17.46%)</td><td>147.16 (-16.81%)</td><td>146.00 <b>(-22.79%)</b></td><td>121.00 (-0.98%)</td><td>19.48 <b>(-38.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.80 (n/a)</td><td>176.90 (n/a)</td><td>189.10 (n/a)</td><td>122.20 (n/a)</td><td>31.56 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 <b>(-26.28%)</b></td><td>0.11 (+1.80%)</td><td>0.11 (+11.65%)</td><td>0.10 <b>(+23.08%)</b></td><td>0.01 <b>(-76.25%)</b></td><td>164.80 (-18.78%)</td><td>152.40 (-6.77%)</td><td>149.50 (-10.43%)</td><td>141.30 <b>(+35.73%)</b></td><td>10.42 <b>(-73.35%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>202.90 (n/a)</td><td>163.46 (n/a)</td><td>166.90 (n/a)</td><td>104.10 (n/a)</td><td>39.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (+18.51%)</td><td>0.10 (+9.66%)</td><td>0.10 (+9.79%)</td><td>0.08 <b>(+27.99%)</b></td><td>0.02 (+2.51%)</td><td>194.90 <b>(-21.85%)</b></td><td>161.48 (-9.97%)</td><td>161.60 (-8.91%)</td><td>119.40 (-15.62%)</td><td>27.46 <b>(-35.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>249.40 (n/a)</td><td>179.36 (n/a)</td><td>177.40 (n/a)</td><td>141.50 (n/a)</td><td>42.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (+4.40%)</td><td>0.11 (+6.57%)</td><td>0.10 <b>(+24.21%)</b></td><td>0.08 (+12.98%)</td><td>0.03 (-17.50%)</td><td>200.80 (-11.46%)</td><td>162.96 (-9.84%)</td><td>166.20 (-19.48%)</td><td>106.20 (-4.24%)</td><td>35.08 <b>(-35.62%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>226.80 (n/a)</td><td>180.74 (n/a)</td><td>206.40 (n/a)</td><td>110.90 (n/a)</td><td>54.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (-10.44%)</td><td>0.08 (-14.17%)</td><td>0.09 (-0.89%)</td><td>0.06 <b>(-30.60%)</b></td><td>0.02 <b>(+20.24%)</b></td><td>266.10 <b>(+44.07%)</b></td><td>200.06 (+18.50%)</td><td>185.00 (+0.93%)</td><td>160.90 (+11.66%)</td><td>40.89 <b>(+96.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>168.82 (n/a)</td><td>183.30 (n/a)</td><td>144.10 (n/a)</td><td>20.84 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (-4.55%)</td><td>0.10 (+0.86%)</td><td>0.10 (+5.12%)</td><td>0.09 (-2.46%)</td><td>0.01 (+2.43%)</td><td>184.20 (+2.50%)</td><td>162.54 (-0.72%)</td><td>163.60 (-4.83%)</td><td>140.90 (+4.76%)</td><td>20.76 (+9.15%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.70 (n/a)</td><td>163.72 (n/a)</td><td>171.90 (n/a)</td><td>134.50 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (+0.73%)</td><td>0.10 (-2.75%)</td><td>0.10 (-0.80%)</td><td>0.08 (-6.57%)</td><td>0.01 (+5.80%)</td><td>207.10 (+7.03%)</td><td>174.36 (+3.09%)</td><td>170.90 (+0.77%)</td><td>139.40 (-0.71%)</td><td>26.05 (+10.79%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>169.14 (n/a)</td><td>169.60 (n/a)</td><td>140.40 (n/a)</td><td>23.51 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (+0.46%)</td><td>0.09 (+0.69%)</td><td>0.10 (+0.06%)</td><td>0.05 (-10.77%)</td><td>0.03 (+9.68%)</td><td>332.00 (+12.09%)</td><td>196.44 (+1.85%)</td><td>170.30 (-0.06%)</td><td>133.80 (-0.45%)</td><td>77.71 <b>(+26.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>296.20 (n/a)</td><td>192.88 (n/a)</td><td>170.40 (n/a)</td><td>134.40 (n/a)</td><td>61.54 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (+6.90%)</td><td>0.11 (+2.33%)</td><td>0.10 (-3.93%)</td><td>0.10 (+7.53%)</td><td>0.01 <b>(+25.19%)</b></td><td>170.90 (-6.97%)</td><td>155.30 (-2.08%)</td><td>160.90 (+4.08%)</td><td>138.40 (-6.49%)</td><td>15.62 (+6.72%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>158.60 (n/a)</td><td>154.60 (n/a)</td><td>148.00 (n/a)</td><td>14.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (+2.92%)</td><td>0.10 (+13.48%)</td><td>0.10 (+3.48%)</td><td>0.08 <b>(+52.76%)</b></td><td>0.01 <b>(-48.35%)</b></td><td>198.60 <b>(-34.52%)</b></td><td>167.46 (-16.62%)</td><td>162.20 (-3.34%)</td><td>146.70 (-2.85%)</td><td>20.91 <b>(-67.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>303.30 (n/a)</td><td>200.84 (n/a)</td><td>167.80 (n/a)</td><td>151.00 (n/a)</td><td>63.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (-19.50%)</td><td>0.09 (-9.91%)</td><td>0.09 (-3.77%)</td><td>0.08 (-0.35%)</td><td>0.01 <b>(-50.29%)</b></td><td>207.80 (+0.39%)</td><td>181.92 (+9.04%)</td><td>179.00 (+3.95%)</td><td>162.00 <b>(+24.23%)</b></td><td>18.79 <b>(-37.44%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.00 (n/a)</td><td>166.84 (n/a)</td><td>172.20 (n/a)</td><td>130.40 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (-3.96%)</td><td>0.20 (-4.21%)</td><td>0.20 (-3.54%)</td><td>0.14 (-11.46%)</td><td>0.04 (+2.46%)</td><td>228.70 (+12.94%)</td><td>167.34 (+5.11%)</td><td>161.50 (+3.66%)</td><td>132.80 (+4.08%)</td><td>36.25 <b>(+25.19%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>202.50 (n/a)</td><td>159.20 (n/a)</td><td>155.80 (n/a)</td><td>127.60 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (+16.44%)</td><td>0.24 <b>(+24.22%)</b></td><td>0.24 <b>(+28.43%)</b></td><td>0.21 <b>(+46.32%)</b></td><td>0.02 <b>(-31.32%)</b></td><td>156.10 <b>(-31.65%)</b></td><td>139.20 <b>(-20.82%)</b></td><td>133.80 <b>(-22.16%)</b></td><td>127.70 (-14.12%)</td><td>12.56 <b>(-60.25%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>228.40 (n/a)</td><td>175.80 (n/a)</td><td>171.90 (n/a)</td><td>148.70 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.22 (+15.14%)</td><td>0.17 (+15.45%)</td><td>0.16 (+3.70%)</td><td>0.15 <b>(+56.71%)</b></td><td>0.03 <b>(-20.07%)</b></td><td>219.90 <b>(-36.19%)</b></td><td>192.88 (-16.49%)</td><td>207.30 (-3.58%)</td><td>149.30 (-13.15%)</td><td>28.51 <b>(-57.68%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>344.60 (n/a)</td><td>230.96 (n/a)</td><td>215.00 (n/a)</td><td>171.90 (n/a)</td><td>67.36 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (-13.41%)</td><td>0.16 (-12.70%)</td><td>0.15 (-13.02%)</td><td>0.15 (+4.46%)</td><td>0.02 <b>(-47.14%)</b></td><td>220.00 (-4.26%)</td><td>207.96 (+12.63%)</td><td>217.10 (+14.99%)</td><td>174.00 (+15.46%)</td><td>19.38 <b>(-40.57%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>229.80 (n/a)</td><td>184.64 (n/a)</td><td>188.80 (n/a)</td><td>150.70 (n/a)</td><td>32.62 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (+11.23%)</td><td>0.21 (+8.36%)</td><td>0.20 (+7.03%)</td><td>0.16 (+3.08%)</td><td>0.04 (+17.76%)</td><td>204.50 (-2.99%)</td><td>161.30 (-7.27%)</td><td>161.80 (-6.58%)</td><td>116.40 (-10.12%)</td><td>31.16 (+1.40%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.80 (n/a)</td><td>173.94 (n/a)</td><td>173.20 (n/a)</td><td>129.50 (n/a)</td><td>30.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (-7.70%)</td><td>0.21 (-5.07%)</td><td>0.21 (-9.47%)</td><td>0.18 (+17.32%)</td><td>0.03 <b>(-42.96%)</b></td><td>178.60 (-14.75%)</td><td>158.42 (+2.46%)</td><td>158.70 (+10.44%)</td><td>132.30 (+8.35%)</td><td>19.59 <b>(-46.11%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>209.50 (n/a)</td><td>154.62 (n/a)</td><td>143.70 (n/a)</td><td>122.10 (n/a)</td><td>36.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (-4.52%)</td><td>0.20 (-11.44%)</td><td>0.20 (-4.08%)</td><td>0.14 <b>(-28.39%)</b></td><td>0.04 <b>(+20.04%)</b></td><td>239.00 <b>(+39.68%)</b></td><td>173.08 (+15.25%)</td><td>166.80 (+4.25%)</td><td>129.30 (+4.70%)</td><td>40.10 <b>(+81.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>171.10 (n/a)</td><td>150.18 (n/a)</td><td>160.00 (n/a)</td><td>123.50 (n/a)</td><td>22.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.20 <b>(-29.86%)</b></td><td>0.18 (-16.09%)</td><td>0.19 (-10.35%)</td><td>0.16 (+8.36%)</td><td>0.02 <b>(-70.71%)</b></td><td>204.30 (-7.72%)</td><td>179.84 (+14.04%)</td><td>172.60 (+11.57%)</td><td>165.10 <b>(+42.57%)</b></td><td>15.83 <b>(-61.43%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>221.40 (n/a)</td><td>157.70 (n/a)</td><td>154.70 (n/a)</td><td>115.80 (n/a)</td><td>41.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (-3.02%)</td><td>0.18 (-19.27%)</td><td>0.17 <b>(-29.60%)</b></td><td>0.10 <b>(-32.46%)</b></td><td>0.06 <b>(+20.18%)</b></td><td>332.90 <b>(+48.02%)</b></td><td>204.66 <b>(+31.09%)</b></td><td>195.80 <b>(+41.99%)</b></td><td>120.30 (+3.08%)</td><td>79.78 <b>(+83.86%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>224.90 (n/a)</td><td>156.12 (n/a)</td><td>137.90 (n/a)</td><td>116.70 (n/a)</td><td>43.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.20 <b>(-29.97%)</b></td><td>0.16 <b>(-27.98%)</b></td><td>0.17 (-15.81%)</td><td>0.09 <b>(-45.45%)</b></td><td>0.04 (-10.93%)</td><td>356.40 <b>(+83.33%)</b></td><td>222.92 <b>(+44.15%)</b></td><td>193.80 (+18.75%)</td><td>168.00 <b>(+42.74%)</b></td><td>75.88 <b>(+152.30%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.40 (n/a)</td><td>154.64 (n/a)</td><td>163.20 (n/a)</td><td>117.70 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (-17.81%)</td><td>0.18 (-14.42%)</td><td>0.18 (-13.87%)</td><td>0.16 (-8.08%)</td><td>0.02 <b>(-48.77%)</b></td><td>210.90 (+8.77%)</td><td>182.24 (+14.76%)</td><td>178.00 (+16.11%)</td><td>158.40 <b>(+21.66%)</b></td><td>20.52 <b>(-31.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>193.90 (n/a)</td><td>158.80 (n/a)</td><td>153.30 (n/a)</td><td>130.20 (n/a)</td><td>29.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 <b>(-33.58%)</b></td><td>0.17 <b>(-24.34%)</b></td><td>0.18 (-17.37%)</td><td>0.16 (-19.03%)</td><td>0.01 <b>(-70.08%)</b></td><td>209.40 <b>(+23.54%)</b></td><td>192.20 <b>(+30.54%)</b></td><td>186.60 <b>(+21.01%)</b></td><td>182.20 <b>(+50.58%)</b></td><td>11.08 <b>(-43.83%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>169.50 (n/a)</td><td>147.24 (n/a)</td><td>154.20 (n/a)</td><td>121.00 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (-8.89%)</td><td>0.18 (-8.13%)</td><td>0.19 (-5.12%)</td><td>0.15 (-6.38%)</td><td>0.03 (-10.70%)</td><td>218.70 (+6.79%)</td><td>184.60 (+8.74%)</td><td>176.20 (+5.38%)</td><td>152.60 (+9.78%)</td><td>27.72 (+6.04%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>204.80 (n/a)</td><td>169.76 (n/a)</td><td>167.20 (n/a)</td><td>139.00 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 <b>(-27.27%)</b></td><td>0.17 (-18.39%)</td><td>0.17 (-17.15%)</td><td>0.16 (+2.97%)</td><td>0.01 <b>(-75.55%)</b></td><td>207.10 (-2.91%)</td><td>195.92 (+18.87%)</td><td>194.90 <b>(+20.68%)</b></td><td>179.10 <b>(+37.56%)</b></td><td>11.28 <b>(-66.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>213.30 (n/a)</td><td>164.82 (n/a)</td><td>161.50 (n/a)</td><td>130.20 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 <b>(-22.72%)</b></td><td>0.16 <b>(-24.63%)</b></td><td>0.17 (-19.39%)</td><td>0.11 <b>(-37.29%)</b></td><td>0.03 (+14.60%)</td><td>297.00 <b>(+59.51%)</b></td><td>212.88 <b>(+35.83%)</b></td><td>195.60 <b>(+24.11%)</b></td><td>170.60 <b>(+29.44%)</b></td><td>49.70 <b>(+144.42%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>186.20 (n/a)</td><td>156.72 (n/a)</td><td>157.60 (n/a)</td><td>131.80 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (+5.72%)</td><td>0.19 (+8.38%)</td><td>0.17 (+5.70%)</td><td>0.15 (-1.03%)</td><td>0.05 <b>(+24.63%)</b></td><td>221.30 (+1.05%)</td><td>178.26 (-6.32%)</td><td>189.60 (-5.39%)</td><td>127.80 (-5.40%)</td><td>40.65 <b>(+21.40%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>219.00 (n/a)</td><td>190.28 (n/a)</td><td>200.40 (n/a)</td><td>135.10 (n/a)</td><td>33.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (-8.59%)</td><td>0.16 (-8.46%)</td><td>0.16 (-8.39%)</td><td>0.16 (-8.40%)</td><td>0.00 <b>(-57.60%)</b></td><td>52300.00 (+9.17%)</td><td>52258.18 (+9.24%)</td><td>52255.20 (+9.16%)</td><td>52202.50 (+9.40%)</td><td>38.18 <b>(-49.37%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47908.80 (n/a)</td><td>47838.74 (n/a)</td><td>47868.80 (n/a)</td><td>47717.90 (n/a)</td><td>75.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52316.20 (n/a)</td><td>52249.88 (n/a)</td><td>52244.30 (n/a)</td><td>52209.90 (n/a)</td><td>39.96 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>413361.00 (n/a)</td><td>413148.70 (n/a)</td><td>413144.50 (n/a)</td><td>412987.90 (n/a)</td><td>137.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (+1.51%)</td><td>0.14 (-12.98%)</td><td>0.12 <b>(-24.63%)</b></td><td>0.11 (-6.94%)</td><td>0.03 (+17.28%)</td><td>232.40 (+7.44%)</td><td>185.08 (+16.42%)</td><td>201.10 <b>(+32.74%)</b></td><td>131.50 (-1.50%)</td><td>41.26 <b>(+21.79%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.30 (n/a)</td><td>158.98 (n/a)</td><td>151.50 (n/a)</td><td>133.50 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.43 (+14.39%)</td><td>0.31 (+4.49%)</td><td>0.30 (+2.77%)</td><td>0.19 (-19.17%)</td><td>0.09 <b>(+53.88%)</b></td><td>261.20 <b>(+23.73%)</b></td><td>171.00 (-0.15%)</td><td>161.40 (-2.71%)</td><td>114.10 (-12.57%)</td><td>54.41 <b>(+72.15%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>211.10 (n/a)</td><td>171.26 (n/a)</td><td>165.90 (n/a)</td><td>130.50 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.30 (+1.07%)</td><td>12.60 (-3.27%)</td><td>12.77 (-2.36%)</td><td>11.68 (-9.22%)</td><td>0.75 <b>(+514.33%)</b></td><td>897.80 (+10.16%)</td><td>834.56 (+3.67%)</td><td>821.00 (+2.42%)</td><td>788.70 (-1.05%)</td><td>50.13 <b>(+563.80%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>13.15 (n/a)</td><td>13.03 (n/a)</td><td>13.08 (n/a)</td><td>12.87 (n/a)</td><td>0.12 (n/a)</td><td>815.00 (n/a)</td><td>805.04 (n/a)</td><td>801.60 (n/a)</td><td>797.10 (n/a)</td><td>7.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (+4.19%)</td><td>0.25 (+2.70%)</td><td>0.24 (-3.60%)</td><td>0.23 (+9.52%)</td><td>0.02 (-12.21%)</td><td>179.50 (-8.70%)</td><td>167.82 (-2.88%)</td><td>172.90 (+3.72%)</td><td>146.50 (-4.00%)</td><td>13.01 <b>(-24.44%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>196.60 (n/a)</td><td>172.80 (n/a)</td><td>166.70 (n/a)</td><td>152.60 (n/a)</td><td>17.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (-2.70%)</td><td>0.03 (-0.33%)</td><td>0.03 (+4.03%)</td><td>0.03 (+10.01%)</td><td>0.00 <b>(-26.57%)</b></td><td>186.90 (-9.10%)</td><td>166.42 (-0.51%)</td><td>162.70 (-3.90%)</td><td>145.90 (+2.75%)</td><td>17.43 <b>(-30.36%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>167.28 (n/a)</td><td>169.30 (n/a)</td><td>142.00 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (+18.03%)</td><td>0.03 (+6.07%)</td><td>0.03 (-3.93%)</td><td>0.02 (+13.22%)</td><td>0.01 <b>(+36.83%)</b></td><td>171.20 (-11.66%)</td><td>143.44 (-4.63%)</td><td>147.50 (+4.09%)</td><td>97.00 (-15.28%)</td><td>29.86 (+0.81%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>150.40 (n/a)</td><td>141.70 (n/a)</td><td>114.50 (n/a)</td><td>29.62 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (+2.28%)</td><td>0.04 <b>(+31.83%)</b></td><td>0.04 <b>(+43.56%)</b></td><td>0.04 <b>(+91.35%)</b></td><td>0.00 <b>(-60.68%)</b></td><td>169.70 <b>(-47.72%)</b></td><td>151.12 <b>(-30.53%)</b></td><td>149.20 <b>(-30.35%)</b></td><td>134.50 (-2.25%)</td><td>15.48 <b>(-79.48%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>324.60 (n/a)</td><td>217.52 (n/a)</td><td>214.20 (n/a)</td><td>137.60 (n/a)</td><td>75.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-14.91%)</td><td>0.03 (-8.83%)</td><td>0.03 (-2.36%)</td><td>0.02 (-12.44%)</td><td>0.00 <b>(-28.74%)</b></td><td>189.40 (+14.23%)</td><td>149.44 (+8.86%)</td><td>143.40 (+2.43%)</td><td>125.30 (+17.43%)</td><td>23.97 (-1.13%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>165.80 (n/a)</td><td>137.28 (n/a)</td><td>140.00 (n/a)</td><td>106.70 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (+11.42%)</td><td>0.04 <b>(+25.85%)</b></td><td>0.03 <b>(+32.09%)</b></td><td>0.03 <b>(+41.81%)</b></td><td>0.01 (-15.00%)</td><td>178.80 <b>(-29.50%)</b></td><td>149.20 <b>(-23.18%)</b></td><td>149.80 <b>(-24.27%)</b></td><td>106.50 (-10.20%)</td><td>27.29 <b>(-45.30%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.60 (n/a)</td><td>194.22 (n/a)</td><td>197.80 (n/a)</td><td>118.60 (n/a)</td><td>49.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+3.02%)</td><td>0.03 (-12.91%)</td><td>0.02 (-19.62%)</td><td>0.02 (-12.36%)</td><td>0.01 <b>(+28.88%)</b></td><td>188.90 (+14.07%)</td><td>165.78 (+16.11%)</td><td>170.00 <b>(+24.36%)</b></td><td>119.70 (-2.92%)</td><td>27.11 <b>(+37.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>165.60 (n/a)</td><td>142.78 (n/a)</td><td>136.70 (n/a)</td><td>123.30 (n/a)</td><td>19.77 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (+5.96%)</td><td>0.03 (+3.04%)</td><td>0.03 (+3.34%)</td><td>0.03 (-1.38%)</td><td>0.01 <b>(+24.85%)</b></td><td>203.00 (+1.40%)</td><td>163.28 (-1.75%)</td><td>168.30 (-3.28%)</td><td>125.90 (-5.62%)</td><td>35.09 (+19.26%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>166.18 (n/a)</td><td>174.00 (n/a)</td><td>133.40 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-3.76%)</td><td>0.03 (+18.70%)</td><td>0.03 (+14.42%)</td><td>0.02 <b>(+88.01%)</b></td><td>0.00 <b>(-61.57%)</b></td><td>183.20 <b>(-46.82%)</b></td><td>157.18 <b>(-26.61%)</b></td><td>159.80 (-12.63%)</td><td>128.60 (+3.96%)</td><td>19.85 <b>(-79.05%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>344.50 (n/a)</td><td>214.18 (n/a)</td><td>182.90 (n/a)</td><td>123.70 (n/a)</td><td>94.74 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (+15.89%)</td><td>0.03 (+13.49%)</td><td>0.02 (+10.44%)</td><td>0.02 (+4.98%)</td><td>0.01 <b>(+61.44%)</b></td><td>211.10 (-4.74%)</td><td>174.04 (-9.66%)</td><td>188.10 (-9.44%)</td><td>126.90 (-13.73%)</td><td>40.14 <b>(+34.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.60 (n/a)</td><td>192.64 (n/a)</td><td>207.70 (n/a)</td><td>147.10 (n/a)</td><td>29.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+12.47%)</td><td>0.03 (+18.52%)</td><td>0.03 (+14.11%)</td><td>0.02 <b>(+51.45%)</b></td><td>0.01 <b>(-25.21%)</b></td><td>193.50 <b>(-33.96%)</b></td><td>139.46 <b>(-20.32%)</b></td><td>127.40 (-12.32%)</td><td>117.30 (-11.14%)</td><td>30.70 <b>(-54.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>293.00 (n/a)</td><td>175.02 (n/a)</td><td>145.30 (n/a)</td><td>132.00 (n/a)</td><td>67.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.04 (+11.69%)</td><td>0.03 (+15.27%)</td><td>0.03 (+7.60%)</td><td>0.02 (+19.85%)</td><td>0.01 <b>(+30.96%)</b></td><td>203.70 (-16.58%)</td><td>165.16 (-12.72%)</td><td>171.10 (-7.06%)</td><td>130.80 (-10.47%)</td><td>32.86 (-6.57%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.20 (n/a)</td><td>189.22 (n/a)</td><td>184.10 (n/a)</td><td>146.10 (n/a)</td><td>35.18 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-0.66%)</td><td>0.03 (+9.90%)</td><td>0.03 <b>(+20.92%)</b></td><td>0.02 (+14.48%)</td><td>0.00 <b>(-20.70%)</b></td><td>220.50 (-12.67%)</td><td>168.34 (-11.10%)</td><td>160.90 (-17.28%)</td><td>130.70 (+0.69%)</td><td>34.32 <b>(-28.71%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.50 (n/a)</td><td>189.36 (n/a)</td><td>194.50 (n/a)</td><td>129.80 (n/a)</td><td>48.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+14.91%)</td><td>0.02 (+13.69%)</td><td>0.03 <b>(+22.82%)</b></td><td>0.02 (-1.28%)</td><td>0.00 <b>(+109.04%)</b></td><td>214.40 (+1.28%)</td><td>177.76 (-11.29%)</td><td>167.40 (-18.62%)</td><td>158.40 (-12.97%)</td><td>22.42 <b>(+86.35%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.70 (n/a)</td><td>200.38 (n/a)</td><td>205.70 (n/a)</td><td>182.00 (n/a)</td><td>12.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-10.51%)</td><td>0.02 (-7.48%)</td><td>0.02 (-4.26%)</td><td>0.02 (+4.64%)</td><td>0.01 <b>(-23.51%)</b></td><td>209.20 (-4.43%)</td><td>182.92 (+5.92%)</td><td>189.50 (+4.47%)</td><td>125.20 (+11.69%)</td><td>34.01 (-18.74%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>172.70 (n/a)</td><td>181.40 (n/a)</td><td>112.10 (n/a)</td><td>41.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-4.08%)</td><td>0.02 (-0.89%)</td><td>0.02 (-5.51%)</td><td>0.02 (-9.77%)</td><td>0.00 <b>(+26.75%)</b></td><td>237.30 (+10.84%)</td><td>193.98 (+1.97%)</td><td>203.10 (+5.84%)</td><td>160.10 (+4.23%)</td><td>33.00 <b>(+43.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.10 (n/a)</td><td>190.24 (n/a)</td><td>191.90 (n/a)</td><td>153.60 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.02 (+0.99%)</td><td>0.02 (+0.47%)</td><td>0.02 (-8.58%)</td><td>0.02 <b>(+39.53%)</b></td><td>0.00 <b>(-41.55%)</b></td><td>240.70 <b>(-28.32%)</b></td><td>216.88 (-4.43%)</td><td>219.50 (+9.37%)</td><td>174.90 (-1.02%)</td><td>26.35 <b>(-59.39%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>335.80 (n/a)</td><td>226.94 (n/a)</td><td>200.70 (n/a)</td><td>176.70 (n/a)</td><td>64.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (+11.71%)</td><td>0.05 (+0.42%)</td><td>0.05 (-12.67%)</td><td>0.04 <b>(+24.77%)</b></td><td>0.01 (-5.12%)</td><td>194.00 (-19.87%)</td><td>158.14 (-2.29%)</td><td>163.10 (+14.46%)</td><td>116.30 (-10.47%)</td><td>31.12 <b>(-33.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.10 (n/a)</td><td>161.84 (n/a)</td><td>142.50 (n/a)</td><td>129.90 (n/a)</td><td>46.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (+15.43%)</td><td>0.08 (+18.30%)</td><td>0.08 <b>(+21.18%)</b></td><td>0.06 (+14.51%)</td><td>0.02 (+8.59%)</td><td>213.80 (-12.66%)</td><td>156.96 (-15.77%)</td><td>149.60 (-17.48%)</td><td>118.70 (-13.36%)</td><td>35.07 (-15.77%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>244.80 (n/a)</td><td>186.34 (n/a)</td><td>181.30 (n/a)</td><td>137.00 (n/a)</td><td>41.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 <b>(+22.71%)</b></td><td>0.05 (+11.10%)</td><td>0.05 (+4.52%)</td><td>0.04 (-3.79%)</td><td>0.01 <b>(+96.36%)</b></td><td>221.20 (+3.90%)</td><td>167.50 (-7.07%)</td><td>176.10 (-4.29%)</td><td>123.30 (-18.51%)</td><td>40.23 <b>(+62.92%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>180.24 (n/a)</td><td>184.00 (n/a)</td><td>151.30 (n/a)</td><td>24.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (-8.52%)</td><td>0.06 (-12.32%)</td><td>0.06 (-9.21%)</td><td>0.04 <b>(-29.24%)</b></td><td>0.01 <b>(+22.25%)</b></td><td>281.00 <b>(+41.28%)</b></td><td>193.66 (+17.28%)</td><td>170.90 (+10.12%)</td><td>151.80 (+9.29%)</td><td>53.10 <b>(+89.53%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>165.12 (n/a)</td><td>155.20 (n/a)</td><td>138.90 (n/a)</td><td>28.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-0.30%)</td><td>0.05 (-5.07%)</td><td>0.05 (-6.72%)</td><td>0.03 (-10.38%)</td><td>0.01 (+15.34%)</td><td>237.30 (+11.57%)</td><td>176.54 (+6.45%)</td><td>173.10 (+7.25%)</td><td>141.70 (+0.35%)</td><td>37.16 <b>(+30.14%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>165.84 (n/a)</td><td>161.40 (n/a)</td><td>141.20 (n/a)</td><td>28.56 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 (-0.14%)</td><td>0.07 (-2.93%)</td><td>0.07 (-4.04%)</td><td>0.04 <b>(-32.73%)</b></td><td>0.02 <b>(+74.57%)</b></td><td>261.30 <b>(+48.63%)</b></td><td>165.98 (+8.26%)</td><td>149.20 (+4.19%)</td><td>130.50 (+0.15%)</td><td>54.29 <b>(+160.12%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>153.32 (n/a)</td><td>143.20 (n/a)</td><td>130.30 (n/a)</td><td>20.87 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-4.40%)</td><td>0.05 (+8.84%)</td><td>0.06 (+13.37%)</td><td>0.04 (+7.71%)</td><td>0.01 (-13.07%)</td><td>183.60 (-7.18%)</td><td>152.68 (-8.67%)</td><td>148.10 (-11.79%)</td><td>129.80 (+4.59%)</td><td>23.54 (-13.88%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.80 (n/a)</td><td>167.18 (n/a)</td><td>167.90 (n/a)</td><td>124.10 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 (-18.93%)</td><td>0.06 (+15.77%)</td><td>0.06 <b>(+34.97%)</b></td><td>0.04 <b>(+45.67%)</b></td><td>0.01 <b>(-47.58%)</b></td><td>223.00 <b>(-31.34%)</b></td><td>162.82 <b>(-21.77%)</b></td><td>157.10 <b>(-25.93%)</b></td><td>126.60 <b>(+23.39%)</b></td><td>37.59 <b>(-52.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>324.80 (n/a)</td><td>208.14 (n/a)</td><td>212.10 (n/a)</td><td>102.60 (n/a)</td><td>79.54 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (-0.39%)</td><td>0.05 (+0.55%)</td><td>0.06 <b>(+31.20%)</b></td><td>0.02 <b>(-45.55%)</b></td><td>0.02 <b>(+87.60%)</b></td><td>357.90 <b>(+83.63%)</b></td><td>192.46 (+11.95%)</td><td>141.80 <b>(-23.76%)</b></td><td>130.70 (+0.38%)</td><td>96.07 <b>(+244.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>171.92 (n/a)</td><td>186.00 (n/a)</td><td>130.20 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 <b>(+29.24%)</b></td><td>0.05 (+18.19%)</td><td>0.06 <b>(+42.57%)</b></td><td>0.04 (-12.06%)</td><td>0.02 <b>(+185.51%)</b></td><td>257.40 (+13.74%)</td><td>181.50 (-9.92%)</td><td>146.40 <b>(-29.89%)</b></td><td>133.30 <b>(-22.63%)</b></td><td>57.17 <b>(+152.54%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>201.48 (n/a)</td><td>208.80 (n/a)</td><td>172.30 (n/a)</td><td>22.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 (+12.05%)</td><td>0.05 <b>(+21.01%)</b></td><td>0.05 <b>(+27.11%)</b></td><td>0.04 <b>(+38.40%)</b></td><td>0.01 (-17.80%)</td><td>225.00 <b>(-27.72%)</b></td><td>165.48 <b>(-20.09%)</b></td><td>155.40 <b>(-21.32%)</b></td><td>136.30 (-10.80%)</td><td>34.56 <b>(-45.25%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.30 (n/a)</td><td>207.08 (n/a)</td><td>197.50 (n/a)</td><td>152.80 (n/a)</td><td>63.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 <b>(+43.60%)</b></td><td>0.05 <b>(+28.16%)</b></td><td>0.05 <b>(+34.95%)</b></td><td>0.04 (+10.22%)</td><td>0.01 <b>(+545.24%)</b></td><td>200.00 (-9.30%)</td><td>170.18 <b>(-20.71%)</b></td><td>160.70 <b>(-25.88%)</b></td><td>145.00 <b>(-30.36%)</b></td><td>24.78 <b>(+314.04%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>214.64 (n/a)</td><td>216.80 (n/a)</td><td>208.20 (n/a)</td><td>5.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.07 <b>(+22.61%)</b></td><td>0.05 (+6.36%)</td><td>0.04 (-8.13%)</td><td>0.04 (+0.59%)</td><td>0.01 <b>(+139.74%)</b></td><td>198.30 (-0.60%)</td><td>171.06 (-3.43%)</td><td>192.00 (+8.84%)</td><td>125.20 (-18.49%)</td><td>33.24 <b>(+99.48%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.50 (n/a)</td><td>177.14 (n/a)</td><td>176.40 (n/a)</td><td>153.60 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.06 <b>(+35.73%)</b></td><td>0.05 <b>(+27.63%)</b></td><td>0.04 (+4.44%)</td><td>0.04 <b>(+46.26%)</b></td><td>0.01 <b>(+25.35%)</b></td><td>226.20 <b>(-31.62%)</b></td><td>190.90 <b>(-22.20%)</b></td><td>204.80 (-4.25%)</td><td>150.10 <b>(-26.31%)</b></td><td>34.76 <b>(-36.70%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>330.80 (n/a)</td><td>245.36 (n/a)</td><td>213.90 (n/a)</td><td>203.70 (n/a)</td><td>54.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.05 (-10.20%)</td><td>0.04 (+9.32%)</td><td>0.04 (+16.54%)</td><td>0.04 <b>(+45.38%)</b></td><td>0.01 <b>(-47.89%)</b></td><td>228.60 <b>(-31.23%)</b></td><td>198.18 (-13.00%)</td><td>196.00 (-14.19%)</td><td>172.40 (+11.37%)</td><td>26.01 <b>(-60.94%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>332.40 (n/a)</td><td>227.80 (n/a)</td><td>228.40 (n/a)</td><td>154.80 (n/a)</td><td>66.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (-12.07%)</td><td>0.11 (+8.52%)</td><td>0.10 (+7.42%)</td><td>0.09 <b>(+75.24%)</b></td><td>0.02 <b>(-42.12%)</b></td><td>188.80 <b>(-42.93%)</b></td><td>158.60 (-16.42%)</td><td>161.00 (-6.88%)</td><td>124.80 (+13.76%)</td><td>30.07 <b>(-64.02%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>330.80 (n/a)</td><td>189.76 (n/a)</td><td>172.90 (n/a)</td><td>109.70 (n/a)</td><td>83.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (+10.91%)</td><td>0.15 (+7.93%)</td><td>0.14 (-2.60%)</td><td>0.13 (+9.82%)</td><td>0.03 <b>(+32.54%)</b></td><td>192.90 (-8.92%)</td><td>166.72 (-6.69%)</td><td>181.80 (+2.65%)</td><td>132.40 (-9.81%)</td><td>27.20 (+8.45%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>211.80 (n/a)</td><td>178.68 (n/a)</td><td>177.10 (n/a)</td><td>146.80 (n/a)</td><td>25.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (-15.99%)</td><td>0.11 (-1.20%)</td><td>0.11 (+11.92%)</td><td>0.08 (-5.82%)</td><td>0.02 <b>(-25.76%)</b></td><td>202.50 (+6.19%)</td><td>155.06 (-0.40%)</td><td>143.90 (-10.62%)</td><td>123.20 (+19.03%)</td><td>33.82 (-8.21%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>190.70 (n/a)</td><td>155.68 (n/a)</td><td>161.00 (n/a)</td><td>103.50 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (+6.01%)</td><td>0.13 (+9.49%)</td><td>0.12 (+10.13%)</td><td>0.10 (+9.70%)</td><td>0.02 (-5.99%)</td><td>201.80 (-8.85%)</td><td>165.44 (-9.36%)</td><td>172.10 (-9.23%)</td><td>127.20 (-5.64%)</td><td>27.58 (-19.81%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>221.40 (n/a)</td><td>182.52 (n/a)</td><td>189.60 (n/a)</td><td>134.80 (n/a)</td><td>34.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 <b>(-24.73%)</b></td><td>0.08 <b>(-29.26%)</b></td><td>0.07 <b>(-38.31%)</b></td><td>0.07 (-13.52%)</td><td>0.01 <b>(-41.48%)</b></td><td>245.10 (+15.61%)</td><td>217.80 <b>(+38.15%)</b></td><td>230.60 <b>(+62.17%)</b></td><td>158.60 <b>(+32.94%)</b></td><td>34.50 (-13.07%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>212.00 (n/a)</td><td>157.66 (n/a)</td><td>142.20 (n/a)</td><td>119.30 (n/a)</td><td>39.68 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (+2.26%)</td><td>0.12 (+2.91%)</td><td>0.12 (-5.03%)</td><td>0.08 (+0.02%)</td><td>0.03 (-9.56%)</td><td>245.70 (+0.00%)</td><td>183.56 (-4.08%)</td><td>177.40 (+5.28%)</td><td>135.10 (-2.17%)</td><td>41.92 (-15.96%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>245.70 (n/a)</td><td>191.36 (n/a)</td><td>168.50 (n/a)</td><td>138.10 (n/a)</td><td>49.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 <b>(+20.23%)</b></td><td>0.10 (+6.29%)</td><td>0.09 (-2.43%)</td><td>0.08 (+12.47%)</td><td>0.02 <b>(+22.05%)</b></td><td>208.70 (-11.12%)</td><td>174.26 (-5.69%)</td><td>179.50 (+2.51%)</td><td>128.00 (-16.83%)</td><td>31.06 (-9.88%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.80 (n/a)</td><td>184.78 (n/a)</td><td>175.10 (n/a)</td><td>153.90 (n/a)</td><td>34.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (-0.88%)</td><td>0.10 (+9.27%)</td><td>0.11 (+9.10%)</td><td>0.09 <b>(+26.90%)</b></td><td>0.01 <b>(-32.45%)</b></td><td>212.90 <b>(-21.18%)</b></td><td>179.56 (-10.98%)</td><td>166.70 (-8.36%)</td><td>157.50 (+0.90%)</td><td>26.08 <b>(-46.59%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>270.10 (n/a)</td><td>201.70 (n/a)</td><td>181.90 (n/a)</td><td>156.10 (n/a)</td><td>48.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 <b>(-36.22%)</b></td><td>0.09 (-15.29%)</td><td>0.09 (+1.14%)</td><td>0.08 (+9.55%)</td><td>0.01 <b>(-76.44%)</b></td><td>195.90 (-8.71%)</td><td>179.14 (+11.36%)</td><td>172.60 (-1.15%)</td><td>163.30 <b>(+56.72%)</b></td><td>15.00 <b>(-65.03%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>214.60 (n/a)</td><td>160.86 (n/a)</td><td>174.60 (n/a)</td><td>104.20 (n/a)</td><td>42.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.11 (-19.27%)</td><td>0.10 (+2.26%)</td><td>0.11 <b>(+27.13%)</b></td><td>0.09 <b>(+29.02%)</b></td><td>0.01 <b>(-72.39%)</b></td><td>208.80 <b>(-22.49%)</b></td><td>181.58 (-8.81%)</td><td>173.40 <b>(-21.36%)</b></td><td>167.20 <b>(+23.85%)</b></td><td>16.54 <b>(-71.81%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>269.40 (n/a)</td><td>199.12 (n/a)</td><td>220.50 (n/a)</td><td>135.00 (n/a)</td><td>58.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.10 (-16.54%)</td><td>0.08 (-16.09%)</td><td>0.08 (-9.45%)</td><td>0.06 <b>(-20.06%)</b></td><td>0.02 (-7.27%)</td><td>289.80 <b>(+25.13%)</b></td><td>223.56 <b>(+20.75%)</b></td><td>197.40 (+10.40%)</td><td>170.00 (+19.80%)</td><td>60.84 <b>(+41.11%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.60 (n/a)</td><td>185.14 (n/a)</td><td>178.80 (n/a)</td><td>141.90 (n/a)</td><td>43.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (+17.09%)</td><td>0.10 (+12.00%)</td><td>0.09 (-4.84%)</td><td>0.08 <b>(+39.76%)</b></td><td>0.02 (-4.26%)</td><td>229.10 <b>(-28.45%)</b></td><td>188.58 (-13.44%)</td><td>198.70 (+5.13%)</td><td>132.40 (-14.58%)</td><td>40.81 <b>(-41.06%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>320.20 (n/a)</td><td>217.86 (n/a)</td><td>189.00 (n/a)</td><td>155.00 (n/a)</td><td>69.24 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (+8.15%)</td><td>0.08 (-9.46%)</td><td>0.08 (-11.43%)</td><td>0.06 (-5.35%)</td><td>0.03 (+16.28%)</td><td>288.70 (+5.63%)</td><td>216.32 (+12.70%)</td><td>206.10 (+12.93%)</td><td>134.80 (-7.54%)</td><td>63.24 (+19.45%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>273.30 (n/a)</td><td>191.94 (n/a)</td><td>182.50 (n/a)</td><td>145.80 (n/a)</td><td>52.94 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 (-12.53%)</td><td>0.09 (+13.19%)</td><td>0.08 <b>(+45.49%)</b></td><td>0.08 <b>(+47.69%)</b></td><td>0.02 <b>(-46.39%)</b></td><td>222.30 <b>(-32.29%)</b></td><td>194.92 <b>(-22.64%)</b></td><td>210.80 <b>(-31.27%)</b></td><td>130.10 (+14.32%)</td><td>37.24 <b>(-61.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>328.30 (n/a)</td><td>251.96 (n/a)</td><td>306.70 (n/a)</td><td>113.80 (n/a)</td><td>97.09 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.08 <b>(-23.68%)</b></td><td>0.07 (-14.23%)</td><td>0.07 (-9.11%)</td><td>0.05 (-12.08%)</td><td>0.01 <b>(-34.47%)</b></td><td>344.30 (+13.71%)</td><td>256.16 (+15.01%)</td><td>235.20 (+10.06%)</td><td>216.80 <b>(+31.00%)</b></td><td>51.14 (-0.89%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>302.80 (n/a)</td><td>222.72 (n/a)</td><td>213.70 (n/a)</td><td>165.50 (n/a)</td><td>51.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (+12.68%)</td><td>0.20 (+5.78%)</td><td>0.20 (+7.12%)</td><td>0.16 (-3.93%)</td><td>0.03 <b>(+50.96%)</b></td><td>207.20 (+4.07%)</td><td>169.44 (-4.37%)</td><td>161.50 (-6.65%)</td><td>133.60 (-11.29%)</td><td>28.40 <b>(+37.79%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>199.10 (n/a)</td><td>177.18 (n/a)</td><td>173.00 (n/a)</td><td>150.60 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (-19.98%)</td><td>0.19 (-9.22%)</td><td>0.20 (-11.97%)</td><td>0.16 (+13.86%)</td><td>0.02 <b>(-58.92%)</b></td><td>204.80 (-12.18%)</td><td>172.36 (+5.21%)</td><td>164.30 (+13.62%)</td><td>154.00 <b>(+25.00%)</b></td><td>20.85 <b>(-54.73%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>233.20 (n/a)</td><td>163.82 (n/a)</td><td>144.60 (n/a)</td><td>123.20 (n/a)</td><td>46.06 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.35 <b>(+27.62%)</b></td><td>0.25 (+3.03%)</td><td>0.23 (-5.70%)</td><td>0.22 (-0.83%)</td><td>0.05 <b>(+131.36%)</b></td><td>188.90 (+0.85%)</td><td>166.52 (-0.75%)</td><td>176.40 (+6.07%)</td><td>118.50 <b>(-21.68%)</b></td><td>28.82 <b>(+81.36%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>187.30 (n/a)</td><td>167.78 (n/a)</td><td>166.30 (n/a)</td><td>151.30 (n/a)</td><td>15.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (-6.95%)</td><td>0.20 (-2.32%)</td><td>0.22 (+5.15%)</td><td>0.16 (+4.19%)</td><td>0.03 <b>(-21.68%)</b></td><td>204.20 (-4.00%)</td><td>163.98 (+1.41%)</td><td>151.60 (-4.89%)</td><td>142.90 (+7.44%)</td><td>24.63 (-19.93%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>212.70 (n/a)</td><td>161.70 (n/a)</td><td>159.40 (n/a)</td><td>133.00 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.34 (-5.77%)</td><td>0.28 (+19.45%)</td><td>0.27 (+10.52%)</td><td>0.23 <b>(+67.97%)</b></td><td>0.04 <b>(-51.36%)</b></td><td>174.60 <b>(-40.47%)</b></td><td>148.26 <b>(-24.54%)</b></td><td>152.50 (-9.50%)</td><td>119.10 (+6.15%)</td><td>22.38 <b>(-70.57%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.37 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>293.30 (n/a)</td><td>196.48 (n/a)</td><td>168.50 (n/a)</td><td>112.20 (n/a)</td><td>76.07 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 <b>(-24.21%)</b></td><td>0.19 (-2.00%)</td><td>0.19 (+2.67%)</td><td>0.17 (+7.22%)</td><td>0.02 <b>(-67.03%)</b></td><td>197.80 (-6.74%)</td><td>174.58 (-1.72%)</td><td>172.10 (-2.60%)</td><td>155.90 <b>(+31.90%)</b></td><td>15.48 <b>(-58.41%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>212.10 (n/a)</td><td>177.64 (n/a)</td><td>176.70 (n/a)</td><td>118.20 (n/a)</td><td>37.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (+16.55%)</td><td>0.22 (+10.13%)</td><td>0.23 (+14.77%)</td><td>0.18 (+5.73%)</td><td>0.03 <b>(+77.69%)</b></td><td>205.80 (-5.38%)</td><td>171.08 (-8.13%)</td><td>157.10 (-12.92%)</td><td>143.80 (-14.15%)</td><td>26.96 <b>(+43.42%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>217.50 (n/a)</td><td>186.22 (n/a)</td><td>180.40 (n/a)</td><td>167.50 (n/a)</td><td>18.80 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (+15.03%)</td><td>0.20 (+6.89%)</td><td>0.20 (+10.44%)</td><td>0.12 (-3.22%)</td><td>0.06 <b>(+28.88%)</b></td><td>282.00 (+3.33%)</td><td>180.08 (-3.45%)</td><td>163.60 (-9.41%)</td><td>117.60 (-13.02%)</td><td>65.72 (+18.22%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>272.90 (n/a)</td><td>186.52 (n/a)</td><td>180.60 (n/a)</td><td>135.20 (n/a)</td><td>55.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.32 <b>(+48.23%)</b></td><td>0.23 (+18.64%)</td><td>0.23 (+15.41%)</td><td>0.16 (+2.05%)</td><td>0.07 <b>(+172.28%)</b></td><td>236.00 (-1.99%)</td><td>170.22 (-10.23%)</td><td>157.20 (-13.39%)</td><td>113.90 <b>(-32.52%)</b></td><td>53.69 <b>(+80.95%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>240.80 (n/a)</td><td>189.62 (n/a)</td><td>181.50 (n/a)</td><td>168.80 (n/a)</td><td>29.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.26 (-8.60%)</td><td>0.21 (+16.30%)</td><td>0.21 <b>(+28.00%)</b></td><td>0.16 <b>(+38.82%)</b></td><td>0.04 <b>(-44.43%)</b></td><td>207.70 <b>(-27.96%)</b></td><td>162.40 (-19.94%)</td><td>154.60 <b>(-21.88%)</b></td><td>128.30 (+9.38%)</td><td>29.77 <b>(-55.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>288.30 (n/a)</td><td>202.86 (n/a)</td><td>197.90 (n/a)</td><td>117.30 (n/a)</td><td>66.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (+12.93%)</td><td>0.21 (+19.53%)</td><td>0.20 <b>(+23.37%)</b></td><td>0.18 <b>(+26.81%)</b></td><td>0.03 (-13.34%)</td><td>189.30 <b>(-21.16%)</b></td><td>171.50 (-17.18%)</td><td>173.70 (-18.91%)</td><td>141.20 (-11.47%)</td><td>19.96 <b>(-39.00%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>240.10 (n/a)</td><td>207.08 (n/a)</td><td>214.20 (n/a)</td><td>159.50 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.24 (-0.53%)</td><td>0.20 <b>(+25.48%)</b></td><td>0.21 <b>(+33.43%)</b></td><td>0.18 <b>(+38.27%)</b></td><td>0.02 <b>(-46.93%)</b></td><td>181.80 <b>(-27.68%)</b></td><td>161.62 <b>(-23.42%)</b></td><td>158.30 <b>(-25.08%)</b></td><td>135.70 (+0.52%)</td><td>18.54 <b>(-60.51%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>251.40 (n/a)</td><td>211.06 (n/a)</td><td>211.30 (n/a)</td><td>135.00 (n/a)</td><td>46.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (-2.58%)</td><td>0.20 (+9.80%)</td><td>0.22 (+17.90%)</td><td>0.14 <b>(+23.01%)</b></td><td>0.04 (-17.00%)</td><td>250.50 (-18.72%)</td><td>182.38 (-11.17%)</td><td>160.60 (-15.16%)</td><td>153.60 (+2.67%)</td><td>40.42 <b>(-33.54%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>308.20 (n/a)</td><td>205.32 (n/a)</td><td>189.30 (n/a)</td><td>149.60 (n/a)</td><td>60.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 <b>(-30.23%)</b></td><td>0.15 (-14.41%)</td><td>0.15 (-0.00%)</td><td>0.13 (-7.44%)</td><td>0.02 <b>(-59.97%)</b></td><td>253.10 (+8.02%)</td><td>216.90 (+11.94%)</td><td>215.80 (+0.00%)</td><td>176.20 <b>(+43.25%)</b></td><td>28.52 <b>(-38.39%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>234.30 (n/a)</td><td>193.76 (n/a)</td><td>215.80 (n/a)</td><td>123.00 (n/a)</td><td>46.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (-5.53%)</td><td>0.13 (+0.01%)</td><td>0.13 (-1.27%)</td><td>0.11 (+5.36%)</td><td>0.02 (-4.45%)</td><td>188.80 (-5.08%)</td><td>163.20 (-0.13%)</td><td>163.80 (+1.30%)</td><td>138.40 (+5.89%)</td><td>23.29 (-4.13%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>198.90 (n/a)</td><td>163.42 (n/a)</td><td>161.70 (n/a)</td><td>130.70 (n/a)</td><td>24.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (-13.84%)</td><td>0.12 (-5.57%)</td><td>0.12 (-4.91%)</td><td>0.10 (+0.50%)</td><td>0.02 <b>(-21.15%)</b></td><td>207.00 (-0.53%)</td><td>173.36 (+5.09%)</td><td>171.80 (+5.21%)</td><td>147.30 (+16.08%)</td><td>26.77 (-10.87%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>208.10 (n/a)</td><td>164.96 (n/a)</td><td>163.30 (n/a)</td><td>126.90 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (-11.20%)</td><td>0.14 (-2.37%)</td><td>0.15 (-5.44%)</td><td>0.09 (-10.25%)</td><td>0.03 (-18.86%)</td><td>225.30 (+11.42%)</td><td>154.80 (+1.71%)</td><td>140.00 (+5.74%)</td><td>129.20 (+12.54%)</td><td>39.68 (+4.43%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>202.20 (n/a)</td><td>152.20 (n/a)</td><td>132.40 (n/a)</td><td>114.80 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (-1.58%)</td><td>0.12 (-6.14%)</td><td>0.12 (-1.91%)</td><td>0.10 (+1.01%)</td><td>0.02 (-15.44%)</td><td>198.50 (-1.00%)</td><td>168.50 (+5.71%)</td><td>170.50 (+1.97%)</td><td>128.60 (+1.66%)</td><td>28.52 (-10.75%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>200.50 (n/a)</td><td>159.40 (n/a)</td><td>167.20 (n/a)</td><td>126.50 (n/a)</td><td>31.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 <b>(+21.07%)</b></td><td>0.15 (+7.99%)</td><td>0.13 (-2.67%)</td><td>0.12 <b>(+45.90%)</b></td><td>0.04 (-4.11%)</td><td>165.20 <b>(-31.45%)</b></td><td>143.84 (-10.40%)</td><td>154.90 (+2.79%)</td><td>96.20 (-17.42%)</td><td>28.70 <b>(-44.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>241.00 (n/a)</td><td>160.54 (n/a)</td><td>150.70 (n/a)</td><td>116.50 (n/a)</td><td>51.56 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.17 (+15.06%)</td><td>0.12 (+2.91%)</td><td>0.13 (+6.22%)</td><td>0.08 (-14.95%)</td><td>0.03 <b>(+80.82%)</b></td><td>241.30 (+17.59%)</td><td>172.28 (+0.58%)</td><td>157.00 (-5.88%)</td><td>123.40 (-13.04%)</td><td>44.50 <b>(+87.52%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>205.20 (n/a)</td><td>171.28 (n/a)</td><td>166.80 (n/a)</td><td>141.90 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.17 (-2.23%)</td><td>0.12 (-9.61%)</td><td>0.11 (-9.49%)</td><td>0.09 (-14.35%)</td><td>0.03 (+15.78%)</td><td>232.50 (+16.78%)</td><td>179.00 (+12.49%)</td><td>178.80 (+10.51%)</td><td>119.60 (+2.22%)</td><td>40.87 <b>(+36.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>199.10 (n/a)</td><td>159.12 (n/a)</td><td>161.80 (n/a)</td><td>117.00 (n/a)</td><td>29.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 (+12.52%)</td><td>0.13 (+16.71%)</td><td>0.13 <b>(+21.17%)</b></td><td>0.10 <b>(+46.44%)</b></td><td>0.03 (-8.00%)</td><td>202.40 <b>(-31.74%)</b></td><td>163.50 (-16.84%)</td><td>152.10 (-17.47%)</td><td>125.00 (-11.16%)</td><td>33.72 <b>(-44.13%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>296.50 (n/a)</td><td>196.62 (n/a)</td><td>184.30 (n/a)</td><td>140.70 (n/a)</td><td>60.36 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 (+17.78%)</td><td>0.15 (+2.24%)</td><td>0.14 (+10.59%)</td><td>0.12 (+1.39%)</td><td>0.04 <b>(+20.20%)</b></td><td>204.80 (-1.40%)</td><td>171.32 (-1.61%)</td><td>172.80 (-9.58%)</td><td>117.10 (-15.08%)</td><td>33.45 (+0.42%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>207.70 (n/a)</td><td>174.12 (n/a)</td><td>191.10 (n/a)</td><td>137.90 (n/a)</td><td>33.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (-0.01%)</td><td>0.16 (+1.76%)</td><td>0.15 (+5.59%)</td><td>0.13 (+3.80%)</td><td>0.02 <b>(-29.73%)</b></td><td>194.20 (-3.62%)</td><td>161.14 (-3.58%)</td><td>160.10 (-5.32%)</td><td>130.40 (+0.00%)</td><td>23.52 <b>(-32.52%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>201.50 (n/a)</td><td>167.12 (n/a)</td><td>169.10 (n/a)</td><td>130.40 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (-6.14%)</td><td>0.16 (+16.26%)</td><td>0.17 <b>(+24.73%)</b></td><td>0.13 (+16.78%)</td><td>0.02 <b>(-32.54%)</b></td><td>184.60 (-14.34%)</td><td>152.72 (-15.87%)</td><td>143.30 (-19.81%)</td><td>134.20 (+6.51%)</td><td>22.16 <b>(-39.54%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>215.50 (n/a)</td><td>181.52 (n/a)</td><td>178.70 (n/a)</td><td>126.00 (n/a)</td><td>36.65 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.18 (-8.39%)</td><td>0.15 (-3.28%)</td><td>0.14 (-7.01%)</td><td>0.13 (+5.79%)</td><td>0.02 <b>(-33.86%)</b></td><td>186.90 (-5.46%)</td><td>168.10 (+1.80%)</td><td>177.20 (+7.59%)</td><td>138.10 (+9.17%)</td><td>20.36 <b>(-32.81%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.70 (n/a)</td><td>165.12 (n/a)</td><td>164.70 (n/a)</td><td>126.50 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 (-2.46%)</td><td>0.15 (+1.85%)</td><td>0.14 (-10.52%)</td><td>0.14 <b>(+36.85%)</b></td><td>0.02 <b>(-46.30%)</b></td><td>176.50 <b>(-26.92%)</b></td><td>161.42 (-6.31%)</td><td>170.60 (+11.80%)</td><td>128.80 (+2.47%)</td><td>19.30 <b>(-60.50%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>241.50 (n/a)</td><td>172.30 (n/a)</td><td>152.60 (n/a)</td><td>125.70 (n/a)</td><td>48.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.17 (-16.37%)</td><td>0.16 (+12.83%)</td><td>0.16 (+14.56%)</td><td>0.14 <b>(+40.25%)</b></td><td>0.01 <b>(-73.11%)</b></td><td>171.50 <b>(-28.72%)</b></td><td>155.16 (-15.87%)</td><td>150.10 (-12.73%)</td><td>145.20 (+19.60%)</td><td>10.62 <b>(-76.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>240.60 (n/a)</td><td>184.42 (n/a)</td><td>172.00 (n/a)</td><td>121.40 (n/a)</td><td>46.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 <b>(-26.89%)</b></td><td>0.13 (-19.35%)</td><td>0.14 (-6.73%)</td><td>0.12 <b>(-21.91%)</b></td><td>0.02 <b>(-33.77%)</b></td><td>210.80 <b>(+28.07%)</b></td><td>186.02 <b>(+23.60%)</b></td><td>173.30 (+7.24%)</td><td>163.90 <b>(+36.81%)</b></td><td>22.85 (+17.73%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>164.60 (n/a)</td><td>150.50 (n/a)</td><td>161.60 (n/a)</td><td>119.80 (n/a)</td><td>19.41 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 <b>(-31.44%)</b></td><td>0.12 <b>(-22.43%)</b></td><td>0.12 (-18.29%)</td><td>0.10 <b>(-25.00%)</b></td><td>0.01 <b>(-52.08%)</b></td><td>236.30 <b>(+33.35%)</b></td><td>209.78 <b>(+28.15%)</b></td><td>207.40 <b>(+22.36%)</b></td><td>194.70 <b>(+45.84%)</b></td><td>16.84 (-6.02%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>177.20 (n/a)</td><td>163.70 (n/a)</td><td>169.50 (n/a)</td><td>133.50 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (-15.89%)</td><td>0.11 (-13.04%)</td><td>0.12 (-13.06%)</td><td>0.09 (-13.96%)</td><td>0.01 <b>(-23.51%)</b></td><td>199.40 (+16.27%)</td><td>166.74 (+14.77%)</td><td>159.40 (+15.01%)</td><td>155.00 (+18.87%)</td><td>18.68 (+7.46%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>171.50 (n/a)</td><td>145.28 (n/a)</td><td>138.60 (n/a)</td><td>130.40 (n/a)</td><td>17.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 (-1.31%)</td><td>0.12 (-2.92%)</td><td>0.12 (-17.39%)</td><td>0.10 <b>(+35.70%)</b></td><td>0.02 <b>(-33.05%)</b></td><td>181.80 <b>(-26.31%)</b></td><td>152.82 (-1.56%)</td><td>157.40 <b>(+20.98%)</b></td><td>122.60 (+1.32%)</td><td>24.95 <b>(-52.18%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>246.70 (n/a)</td><td>155.24 (n/a)</td><td>130.10 (n/a)</td><td>121.00 (n/a)</td><td>52.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.13 <b>(-27.50%)</b></td><td>0.10 (-11.36%)</td><td>0.10 (+7.48%)</td><td>0.07 (+2.91%)</td><td>0.02 <b>(-46.76%)</b></td><td>253.00 (-2.84%)</td><td>188.38 (+6.02%)</td><td>179.30 (-6.95%)</td><td>144.40 <b>(+37.92%)</b></td><td>44.62 <b>(-27.43%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>260.40 (n/a)</td><td>177.68 (n/a)</td><td>192.70 (n/a)</td><td>104.70 (n/a)</td><td>61.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (+3.50%)</td><td>0.11 (+9.55%)</td><td>0.11 (-3.62%)</td><td>0.07 <b>(+39.26%)</b></td><td>0.03 <b>(-23.49%)</b></td><td>251.90 <b>(-28.17%)</b></td><td>174.84 (-14.58%)</td><td>166.60 (+3.74%)</td><td>128.70 (-3.38%)</td><td>46.46 <b>(-46.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>350.70 (n/a)</td><td>204.68 (n/a)</td><td>160.60 (n/a)</td><td>133.20 (n/a)</td><td>87.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (-1.15%)</td><td>0.12 (+5.12%)</td><td>0.12 (+15.37%)</td><td>0.09 (-13.58%)</td><td>0.02 <b>(+33.05%)</b></td><td>211.30 (+15.72%)</td><td>162.26 (-3.59%)</td><td>151.70 (-13.36%)</td><td>136.00 (+1.12%)</td><td>30.75 <b>(+59.76%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>168.30 (n/a)</td><td>175.10 (n/a)</td><td>134.50 (n/a)</td><td>19.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.16 <b>(+22.50%)</b></td><td>0.12 <b>(+24.51%)</b></td><td>0.12 <b>(+34.07%)</b></td><td>0.08 (+7.75%)</td><td>0.03 <b>(+35.81%)</b></td><td>220.30 (-7.20%)</td><td>158.66 (-18.52%)</td><td>148.80 <b>(-25.41%)</b></td><td>112.20 (-18.40%)</td><td>39.33 (+9.12%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>237.40 (n/a)</td><td>194.72 (n/a)</td><td>199.50 (n/a)</td><td>137.50 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.14 (+2.47%)</td><td>0.11 (-3.26%)</td><td>0.10 (-12.19%)</td><td>0.09 (+3.37%)</td><td>0.02 (-1.82%)</td><td>196.50 (-3.25%)</td><td>170.96 (+3.12%)</td><td>182.30 (+13.87%)</td><td>130.00 (-2.40%)</td><td>28.10 (-7.38%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>203.10 (n/a)</td><td>165.78 (n/a)</td><td>160.10 (n/a)</td><td>133.20 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.15 <b>(+31.21%)</b></td><td>0.11 (+1.89%)</td><td>0.10 (-8.53%)</td><td>0.09 (-4.76%)</td><td>0.02 <b>(+191.05%)</b></td><td>208.00 (+5.00%)</td><td>174.36 (+0.72%)</td><td>182.80 (+9.33%)</td><td>126.00 <b>(-23.82%)</b></td><td>31.81 <b>(+127.12%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>173.12 (n/a)</td><td>167.20 (n/a)</td><td>165.40 (n/a)</td><td>14.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.77 (+6.20%)</td><td>0.67 (+17.28%)</td><td>0.63 (+10.17%)</td><td>0.58 <b>(+49.87%)</b></td><td>0.08 <b>(-49.49%)</b></td><td>170.40 <b>(-33.25%)</b></td><td>149.22 (-19.58%)</td><td>155.10 (-9.25%)</td><td>126.90 (-5.86%)</td><td>17.94 <b>(-67.73%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.73 (n/a)</td><td>0.57 (n/a)</td><td>0.58 (n/a)</td><td>0.39 (n/a)</td><td>0.16 (n/a)</td><td>255.30 (n/a)</td><td>185.56 (n/a)</td><td>170.90 (n/a)</td><td>134.80 (n/a)</td><td>55.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.62 <b>(-34.07%)</b></td><td>0.56 (-12.85%)</td><td>0.56 (-2.49%)</td><td>0.51 (+14.31%)</td><td>0.04 <b>(-79.01%)</b></td><td>191.80 (-12.50%)</td><td>175.96 (+7.53%)</td><td>174.70 (+2.52%)</td><td>159.60 <b>(+51.71%)</b></td><td>12.89 <b>(-71.80%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.93 (n/a)</td><td>0.64 (n/a)</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.20 (n/a)</td><td>219.20 (n/a)</td><td>163.64 (n/a)</td><td>170.40 (n/a)</td><td>105.20 (n/a)</td><td>45.70 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.63 <b>(-22.09%)</b></td><td>0.53 (-0.71%)</td><td>0.52 (+9.23%)</td><td>0.47 <b>(+51.91%)</b></td><td>0.07 <b>(-66.38%)</b></td><td>209.30 <b>(-34.18%)</b></td><td>187.44 (-8.91%)</td><td>190.70 (-8.45%)</td><td>155.10 <b>(+28.29%)</b></td><td>22.21 <b>(-71.03%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.81 (n/a)</td><td>0.53 (n/a)</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>318.00 (n/a)</td><td>205.78 (n/a)</td><td>208.30 (n/a)</td><td>120.90 (n/a)</td><td>76.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.62 (-17.66%)</td><td>0.53 (-5.25%)</td><td>0.53 (-8.92%)</td><td>0.40 <b>(+37.45%)</b></td><td>0.08 <b>(-52.02%)</b></td><td>243.10 <b>(-27.26%)</b></td><td>189.58 (-2.47%)</td><td>183.90 (+9.79%)</td><td>158.50 <b>(+21.46%)</b></td><td>32.06 <b>(-59.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.75 (n/a)</td><td>0.56 (n/a)</td><td>0.59 (n/a)</td><td>0.29 (n/a)</td><td>0.17 (n/a)</td><td>334.20 (n/a)</td><td>194.38 (n/a)</td><td>167.50 (n/a)</td><td>130.50 (n/a)</td><td>79.97 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.55 (-5.39%)</td><td>0.48 (+7.96%)</td><td>0.50 (+12.21%)</td><td>0.39 <b>(+22.71%)</b></td><td>0.07 <b>(-27.60%)</b></td><td>190.40 (-18.49%)</td><td>156.84 (-9.23%)</td><td>146.90 (-10.86%)</td><td>135.30 (+5.70%)</td><td>23.61 <b>(-38.81%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.58 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>233.60 (n/a)</td><td>172.78 (n/a)</td><td>164.80 (n/a)</td><td>128.00 (n/a)</td><td>38.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.46 <b>(-34.44%)</b></td><td>0.36 <b>(-25.19%)</b></td><td>0.37 <b>(-22.80%)</b></td><td>0.26 (-9.82%)</td><td>0.09 <b>(-43.74%)</b></td><td>281.70 (+10.91%)</td><td>215.82 <b>(+28.43%)</b></td><td>199.50 <b>(+29.55%)</b></td><td>160.50 <b>(+52.57%)</b></td><td>55.61 (-4.41%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.70 (n/a)</td><td>0.48 (n/a)</td><td>0.48 (n/a)</td><td>0.29 (n/a)</td><td>0.16 (n/a)</td><td>254.00 (n/a)</td><td>168.04 (n/a)</td><td>154.00 (n/a)</td><td>105.20 (n/a)</td><td>58.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.54 (+11.03%)</td><td>0.44 (+18.91%)</td><td>0.44 <b>(+25.50%)</b></td><td>0.38 <b>(+22.80%)</b></td><td>0.06 (-9.35%)</td><td>193.50 (-18.56%)</td><td>168.10 (-16.58%)</td><td>165.80 <b>(-20.29%)</b></td><td>137.40 (-9.96%)</td><td>21.12 <b>(-31.71%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.48 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>237.60 (n/a)</td><td>201.50 (n/a)</td><td>208.00 (n/a)</td><td>152.60 (n/a)</td><td>30.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.48 <b>(-23.40%)</b></td><td>0.38 <b>(-27.35%)</b></td><td>0.41 <b>(-24.02%)</b></td><td>0.22 <b>(-50.44%)</b></td><td>0.10 <b>(+40.02%)</b></td><td>342.00 <b>(+101.77%)</b></td><td>207.96 <b>(+46.55%)</b></td><td>179.00 <b>(+31.62%)</b></td><td>155.20 <b>(+30.53%)</b></td><td>75.95 <b>(+291.08%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.62 (n/a)</td><td>0.53 (n/a)</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.07 (n/a)</td><td>169.50 (n/a)</td><td>141.90 (n/a)</td><td>136.00 (n/a)</td><td>118.90 (n/a)</td><td>19.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (-11.04%)</td><td>0.22 (-13.92%)</td><td>0.21 <b>(-20.91%)</b></td><td>0.18 (-5.96%)</td><td>0.03 <b>(-30.05%)</b></td><td>202.90 (+6.34%)</td><td>171.78 (+14.67%)</td><td>175.40 <b>(+26.37%)</b></td><td>135.30 (+12.38%)</td><td>24.16 (-18.69%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>190.80 (n/a)</td><td>149.80 (n/a)</td><td>138.80 (n/a)</td><td>120.40 (n/a)</td><td>29.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.25 (-17.95%)</td><td>0.19 (-15.19%)</td><td>0.18 (-13.62%)</td><td>0.16 (-15.15%)</td><td>0.04 <b>(-25.76%)</b></td><td>235.20 (+17.84%)</td><td>195.58 (+17.07%)</td><td>199.70 (+15.77%)</td><td>147.50 <b>(+21.90%)</b></td><td>33.43 (+5.35%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>199.60 (n/a)</td><td>167.06 (n/a)</td><td>172.50 (n/a)</td><td>121.00 (n/a)</td><td>31.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 <b>(-22.82%)</b></td><td>0.20 (-6.50%)</td><td>0.21 (-5.32%)</td><td>0.18 <b>(+53.98%)</b></td><td>0.03 <b>(-65.29%)</b></td><td>210.50 <b>(-35.05%)</b></td><td>182.16 (-3.54%)</td><td>174.70 (+5.62%)</td><td>157.50 <b>(+29.63%)</b></td><td>23.05 <b>(-71.40%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>324.10 (n/a)</td><td>188.84 (n/a)</td><td>165.40 (n/a)</td><td>121.50 (n/a)</td><td>80.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (+0.46%)</td><td>0.20 (-4.83%)</td><td>0.21 (+0.43%)</td><td>0.18 (-12.70%)</td><td>0.02 <b>(+97.75%)</b></td><td>206.30 (+14.55%)</td><td>183.00 (+5.99%)</td><td>177.70 (-0.45%)</td><td>157.70 (-0.50%)</td><td>21.73 <b>(+129.84%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>172.66 (n/a)</td><td>178.50 (n/a)</td><td>158.50 (n/a)</td><td>9.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.20 <b>(-25.92%)</b></td><td>0.19 (-17.98%)</td><td>0.19 (-15.61%)</td><td>0.17 (-11.18%)</td><td>0.01 <b>(-60.73%)</b></td><td>216.00 (+12.62%)</td><td>198.72 <b>(+20.86%)</b></td><td>195.60 (+18.47%)</td><td>185.00 <b>(+35.04%)</b></td><td>11.76 <b>(-39.57%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>191.80 (n/a)</td><td>164.42 (n/a)</td><td>165.10 (n/a)</td><td>137.00 (n/a)</td><td>19.45 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.30 (+6.55%)</td><td>0.21 (-8.96%)</td><td>0.21 (-3.58%)</td><td>0.14 <b>(-29.62%)</b></td><td>0.06 <b>(+75.90%)</b></td><td>267.40 <b>(+42.08%)</b></td><td>188.32 (+15.08%)</td><td>176.70 (+3.70%)</td><td>122.70 (-6.19%)</td><td>52.47 <b>(+136.68%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>188.20 (n/a)</td><td>163.64 (n/a)</td><td>170.40 (n/a)</td><td>130.80 (n/a)</td><td>22.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (-18.56%)</td><td>0.19 (-16.86%)</td><td>0.19 (-14.91%)</td><td>0.14 <b>(-31.15%)</b></td><td>0.03 <b>(+22.74%)</b></td><td>257.70 <b>(+45.26%)</b></td><td>198.26 <b>(+22.43%)</b></td><td>197.10 (+17.53%)</td><td>163.00 <b>(+22.83%)</b></td><td>38.72 <b>(+116.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>177.40 (n/a)</td><td>161.94 (n/a)</td><td>167.70 (n/a)</td><td>132.70 (n/a)</td><td>17.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 <b>(+22.79%)</b></td><td>0.20 (-3.51%)</td><td>0.19 (-16.04%)</td><td>0.13 <b>(-27.92%)</b></td><td>0.06 <b>(+160.45%)</b></td><td>273.20 <b>(+38.75%)</b></td><td>191.44 (+9.24%)</td><td>194.90 (+19.13%)</td><td>130.70 (-18.57%)</td><td>53.84 <b>(+194.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>196.90 (n/a)</td><td>175.24 (n/a)</td><td>163.60 (n/a)</td><td>160.50 (n/a)</td><td>18.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.33 (-3.30%)</td><td>0.27 (+9.19%)</td><td>0.25 (+5.35%)</td><td>0.24 (+10.55%)</td><td>0.04 (-13.17%)</td><td>170.40 (-9.55%)</td><td>151.98 (-9.02%)</td><td>166.50 (-5.07%)</td><td>125.50 (+3.38%)</td><td>22.14 (-15.37%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>188.40 (n/a)</td><td>167.04 (n/a)</td><td>175.40 (n/a)</td><td>121.40 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.31 (-8.68%)</td><td>0.25 (-3.95%)</td><td>0.25 (+1.69%)</td><td>0.18 (-6.75%)</td><td>0.05 (-7.15%)</td><td>229.50 (+7.24%)</td><td>171.72 (+4.25%)</td><td>161.40 (-1.65%)</td><td>133.60 (+9.51%)</td><td>36.85 (+11.25%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>214.00 (n/a)</td><td>164.72 (n/a)</td><td>164.10 (n/a)</td><td>122.00 (n/a)</td><td>33.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.31 (+6.13%)</td><td>0.26 (+9.28%)</td><td>0.25 (-1.13%)</td><td>0.24 <b>(+36.77%)</b></td><td>0.03 <b>(-30.45%)</b></td><td>172.20 <b>(-26.91%)</b></td><td>158.56 (-10.36%)</td><td>166.10 (+1.16%)</td><td>131.00 (-5.76%)</td><td>17.00 <b>(-53.51%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>235.60 (n/a)</td><td>176.88 (n/a)</td><td>164.20 (n/a)</td><td>139.00 (n/a)</td><td>36.56 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (-11.18%)</td><td>0.23 (-3.39%)</td><td>0.24 (-0.77%)</td><td>0.15 <b>(-20.29%)</b></td><td>0.05 (+5.49%)</td><td>274.10 <b>(+25.45%)</b></td><td>184.96 (+5.38%)</td><td>167.30 (+0.78%)</td><td>150.30 (+12.58%)</td><td>50.39 <b>(+56.66%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>218.50 (n/a)</td><td>175.52 (n/a)</td><td>166.00 (n/a)</td><td>133.50 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (-2.44%)</td><td>0.24 (-0.34%)</td><td>0.27 (+6.10%)</td><td>0.17 (+4.60%)</td><td>0.05 (-1.98%)</td><td>239.30 (-4.39%)</td><td>175.40 (-0.05%)</td><td>151.90 (-5.77%)</td><td>148.00 (+2.56%)</td><td>39.42 (-8.46%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>250.30 (n/a)</td><td>175.48 (n/a)</td><td>161.20 (n/a)</td><td>144.30 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.33 (-6.69%)</td><td>0.26 (-6.41%)</td><td>0.26 (+3.31%)</td><td>0.18 (-16.24%)</td><td>0.05 (-6.28%)</td><td>223.50 (+19.39%)</td><td>165.48 (+7.30%)</td><td>157.50 (-3.20%)</td><td>122.60 (+7.17%)</td><td>36.83 <b>(+22.42%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>187.20 (n/a)</td><td>154.22 (n/a)</td><td>162.70 (n/a)</td><td>114.40 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (-6.55%)</td><td>0.21 (-15.10%)</td><td>0.21 (-16.39%)</td><td>0.17 (-14.07%)</td><td>0.04 (+16.18%)</td><td>248.20 (+16.36%)</td><td>204.88 (+19.12%)</td><td>196.70 (+19.57%)</td><td>151.50 (+6.99%)</td><td>37.37 <b>(+41.84%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>213.30 (n/a)</td><td>172.00 (n/a)</td><td>164.50 (n/a)</td><td>141.60 (n/a)</td><td>26.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (+6.78%)</td><td>0.22 (-3.72%)</td><td>0.21 (-13.64%)</td><td>0.20 (+2.31%)</td><td>0.03 <b>(+41.41%)</b></td><td>203.20 (-2.26%)</td><td>184.68 (+4.52%)</td><td>197.40 (+15.78%)</td><td>150.50 (-6.35%)</td><td>23.45 <b>(+28.45%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>207.90 (n/a)</td><td>176.70 (n/a)</td><td>170.50 (n/a)</td><td>160.70 (n/a)</td><td>18.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.21 <b>(-21.59%)</b></td><td>0.19 (-15.18%)</td><td>0.21 (-17.33%)</td><td>0.14 (-0.53%)</td><td>0.03 <b>(-42.08%)</b></td><td>246.60 (+0.53%)</td><td>184.70 (+14.39%)</td><td>169.00 <b>(+20.97%)</b></td><td>167.90 <b>(+27.49%)</b></td><td>34.63 <b>(-27.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>245.30 (n/a)</td><td>161.46 (n/a)</td><td>139.70 (n/a)</td><td>131.70 (n/a)</td><td>47.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.27 (-11.64%)</td><td>0.22 (-2.88%)</td><td>0.21 (+8.85%)</td><td>0.18 (-1.54%)</td><td>0.04 <b>(-36.53%)</b></td><td>195.90 (+1.56%)</td><td>162.40 (+0.43%)</td><td>167.10 (-8.14%)</td><td>131.30 (+13.19%)</td><td>25.94 <b>(-28.85%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>192.90 (n/a)</td><td>161.70 (n/a)</td><td>181.90 (n/a)</td><td>116.00 (n/a)</td><td>36.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (+3.54%)</td><td>0.20 (-2.51%)</td><td>0.19 (-3.10%)</td><td>0.15 (-12.98%)</td><td>0.05 <b>(+33.66%)</b></td><td>225.90 (+14.90%)</td><td>178.26 (+4.80%)</td><td>179.60 (+3.16%)</td><td>123.60 (-3.44%)</td><td>39.73 <b>(+50.30%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>196.60 (n/a)</td><td>170.10 (n/a)</td><td>174.10 (n/a)</td><td>128.00 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (+2.81%)</td><td>0.22 (-0.33%)</td><td>0.21 (+1.92%)</td><td>0.19 (+6.52%)</td><td>0.04 (-17.38%)</td><td>185.00 (-6.09%)</td><td>163.92 (-1.01%)</td><td>169.30 (-1.86%)</td><td>123.30 (-2.76%)</td><td>24.21 <b>(-27.14%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>197.00 (n/a)</td><td>165.60 (n/a)</td><td>172.50 (n/a)</td><td>126.80 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 <b>(+25.10%)</b></td><td>0.19 (+4.26%)</td><td>0.17 (-11.81%)</td><td>0.15 (+5.61%)</td><td>0.06 <b>(+72.81%)</b></td><td>239.10 (-5.31%)</td><td>192.14 (-1.16%)</td><td>208.90 (+13.41%)</td><td>122.60 <b>(-20.08%)</b></td><td>46.03 <b>(+25.63%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>252.50 (n/a)</td><td>194.40 (n/a)</td><td>184.20 (n/a)</td><td>153.40 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.28 (+5.46%)</td><td>0.23 <b>(+29.53%)</b></td><td>0.24 <b>(+53.26%)</b></td><td>0.18 <b>(+50.07%)</b></td><td>0.04 <b>(-25.27%)</b></td><td>195.20 <b>(-33.38%)</b></td><td>158.60 <b>(-25.97%)</b></td><td>145.60 <b>(-34.77%)</b></td><td>126.50 (-5.17%)</td><td>29.35 <b>(-50.39%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>293.00 (n/a)</td><td>214.24 (n/a)</td><td>223.20 (n/a)</td><td>133.40 (n/a)</td><td>59.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.23 (-6.46%)</td><td>0.21 (-5.79%)</td><td>0.22 (-0.05%)</td><td>0.18 (-10.91%)</td><td>0.02 (+1.50%)</td><td>188.60 (+12.26%)</td><td>164.38 (+6.30%)</td><td>160.10 (+0.06%)</td><td>150.70 (+6.88%)</td><td>15.09 <b>(+24.21%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>168.00 (n/a)</td><td>154.64 (n/a)</td><td>160.00 (n/a)</td><td>141.00 (n/a)</td><td>12.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.29 <b>(+20.35%)</b></td><td>0.23 (+15.26%)</td><td>0.23 (+11.40%)</td><td>0.17 <b>(+44.46%)</b></td><td>0.05 (-1.89%)</td><td>206.90 <b>(-30.78%)</b></td><td>156.72 (-15.99%)</td><td>148.40 (-10.22%)</td><td>119.20 (-16.93%)</td><td>35.46 <b>(-44.93%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>298.90 (n/a)</td><td>186.56 (n/a)</td><td>165.30 (n/a)</td><td>143.50 (n/a)</td><td>64.40 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.78 (-19.52%)</td><td>0.63 (-12.59%)</td><td>0.64 (-5.13%)</td><td>0.46 <b>(-24.83%)</b></td><td>0.12 (-19.11%)</td><td>287.20 <b>(+33.02%)</b></td><td>214.70 (+14.86%)</td><td>203.60 (+5.44%)</td><td>167.70 <b>(+24.31%)</b></td><td>44.09 <b>(+43.83%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.97 (n/a)</td><td>0.72 (n/a)</td><td>0.68 (n/a)</td><td>0.61 (n/a)</td><td>0.14 (n/a)</td><td>215.90 (n/a)</td><td>186.92 (n/a)</td><td>193.10 (n/a)</td><td>134.90 (n/a)</td><td>30.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.10 (+20.00%)</td><td>0.80 (+9.27%)</td><td>0.74 (+5.60%)</td><td>0.67 (+7.18%)</td><td>0.17 <b>(+56.24%)</b></td><td>196.10 (-6.66%)</td><td>169.80 (-7.14%)</td><td>178.30 (-5.31%)</td><td>119.10 (-16.71%)</td><td>30.06 <b>(+21.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.92 (n/a)</td><td>0.73 (n/a)</td><td>0.70 (n/a)</td><td>0.62 (n/a)</td><td>0.11 (n/a)</td><td>210.10 (n/a)</td><td>182.86 (n/a)</td><td>188.30 (n/a)</td><td>143.00 (n/a)</td><td>24.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.84 (-15.26%)</td><td>0.76 (+3.00%)</td><td>0.76 (+12.52%)</td><td>0.66 (-0.23%)</td><td>0.06 <b>(-55.80%)</b></td><td>197.50 (+0.25%)</td><td>173.72 (-4.63%)</td><td>172.20 (-11.10%)</td><td>156.60 (+18.01%)</td><td>14.86 <b>(-46.35%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.99 (n/a)</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.67 (n/a)</td><td>0.14 (n/a)</td><td>197.00 (n/a)</td><td>182.16 (n/a)</td><td>193.70 (n/a)</td><td>132.70 (n/a)</td><td>27.70 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-6.76%)</td><td>0.03 (-5.30%)</td><td>0.02 (+3.04%)</td><td>0.02 (-1.80%)</td><td>0.00 <b>(-28.50%)</b></td><td>192.40 (+1.85%)</td><td>164.68 (+3.81%)</td><td>173.70 (-2.96%)</td><td>128.60 (+7.26%)</td><td>26.47 <b>(-21.20%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>158.64 (n/a)</td><td>179.00 (n/a)</td><td>119.90 (n/a)</td><td>33.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-8.16%)</td><td>0.03 (-1.58%)</td><td>0.03 (-9.93%)</td><td>0.02 (+16.32%)</td><td>0.00 <b>(-34.76%)</b></td><td>218.40 (-14.05%)</td><td>163.26 (-2.84%)</td><td>157.50 (+10.99%)</td><td>129.20 (+8.85%)</td><td>34.11 <b>(-38.47%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.10 (n/a)</td><td>168.04 (n/a)</td><td>141.90 (n/a)</td><td>118.70 (n/a)</td><td>55.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (-0.51%)</td><td>0.02 (-6.90%)</td><td>0.02 (-12.05%)</td><td>0.02 (+1.87%)</td><td>0.00 (+9.44%)</td><td>201.30 (-1.85%)</td><td>169.36 (+7.80%)</td><td>168.80 (+13.75%)</td><td>130.50 (+0.46%)</td><td>29.92 (+5.64%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.10 (n/a)</td><td>157.10 (n/a)</td><td>148.40 (n/a)</td><td>129.90 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>17.49 (+10.00%)</td><td>12.62 (-9.86%)</td><td>11.67 (-12.35%)</td><td>10.57 (-15.76%)</td><td>2.78 <b>(+67.08%)</b></td><td>198.60 (+18.71%)</td><td>171.54 (+13.23%)</td><td>179.80 (+14.09%)</td><td>119.90 (-9.10%)</td><td>30.27 <b>(+73.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.90 (n/a)</td><td>14.00 (n/a)</td><td>13.32 (n/a)</td><td>12.54 (n/a)</td><td>1.66 (n/a)</td><td>167.30 (n/a)</td><td>151.50 (n/a)</td><td>157.60 (n/a)</td><td>131.90 (n/a)</td><td>17.47 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.26 (+17.56%)</td><td>0.92 (-1.63%)</td><td>0.91 (-4.38%)</td><td>0.52 <b>(-30.29%)</b></td><td>0.26 <b>(+104.91%)</b></td><td>252.30 <b>(+43.43%)</b></td><td>156.08 (+8.71%)</td><td>145.40 (+4.60%)</td><td>105.10 (-14.90%)</td><td>56.35 <b>(+165.75%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.07 (n/a)</td><td>0.94 (n/a)</td><td>0.95 (n/a)</td><td>0.75 (n/a)</td><td>0.13 (n/a)</td><td>175.90 (n/a)</td><td>143.58 (n/a)</td><td>139.00 (n/a)</td><td>123.50 (n/a)</td><td>21.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.27 (+14.20%)</td><td>0.96 (+8.57%)</td><td>0.87 (-3.01%)</td><td>0.78 (+6.17%)</td><td>0.20 <b>(+31.53%)</b></td><td>169.60 (-5.83%)</td><td>142.28 (-7.08%)</td><td>151.30 (+3.14%)</td><td>104.00 (-12.38%)</td><td>26.27 (+6.13%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.11 (n/a)</td><td>0.88 (n/a)</td><td>0.90 (n/a)</td><td>0.73 (n/a)</td><td>0.15 (n/a)</td><td>180.10 (n/a)</td><td>153.12 (n/a)</td><td>146.70 (n/a)</td><td>118.70 (n/a)</td><td>24.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.00 (+10.44%)</td><td>0.79 (+9.01%)</td><td>0.87 (+10.57%)</td><td>0.42 <b>(+21.68%)</b></td><td>0.23 (+5.78%)</td><td>311.90 (-17.81%)</td><td>183.48 (-10.44%)</td><td>151.80 (-9.54%)</td><td>132.40 (-9.44%)</td><td>74.20 <b>(-24.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.90 (n/a)</td><td>0.73 (n/a)</td><td>0.79 (n/a)</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>379.50 (n/a)</td><td>204.86 (n/a)</td><td>167.80 (n/a)</td><td>146.20 (n/a)</td><td>98.06 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.07 (+4.97%)</td><td>0.93 (+4.16%)</td><td>0.88 (+4.87%)</td><td>0.78 (-1.93%)</td><td>0.12 (+12.88%)</td><td>170.10 (+1.98%)</td><td>144.84 (-3.76%)</td><td>150.70 (-4.62%)</td><td>123.70 (-4.77%)</td><td>19.39 (+8.02%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.02 (n/a)</td><td>0.89 (n/a)</td><td>0.84 (n/a)</td><td>0.79 (n/a)</td><td>0.11 (n/a)</td><td>166.80 (n/a)</td><td>150.50 (n/a)</td><td>158.00 (n/a)</td><td>129.90 (n/a)</td><td>17.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.07 (-3.87%)</td><td>0.95 (+5.63%)</td><td>1.02 (+7.16%)</td><td>0.81 <b>(+20.77%)</b></td><td>0.12 <b>(-39.59%)</b></td><td>163.80 (-17.23%)</td><td>141.20 (-8.20%)</td><td>130.10 (-6.67%)</td><td>123.50 (+4.04%)</td><td>19.35 <b>(-48.02%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.11 (n/a)</td><td>0.90 (n/a)</td><td>0.95 (n/a)</td><td>0.67 (n/a)</td><td>0.21 (n/a)</td><td>197.90 (n/a)</td><td>153.82 (n/a)</td><td>139.40 (n/a)</td><td>118.70 (n/a)</td><td>37.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 <b>(+40.67%)</b></td><td>0.03 <b>(+23.16%)</b></td><td>0.03 (+15.07%)</td><td>0.02 (-0.55%)</td><td>0.01 <b>(+198.54%)</b></td><td>203.20 (+0.54%)</td><td>152.98 (-15.60%)</td><td>149.00 (-13.12%)</td><td>117.50 <b>(-28.87%)</b></td><td>37.20 <b>(+104.18%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.10 (n/a)</td><td>181.26 (n/a)</td><td>171.50 (n/a)</td><td>165.20 (n/a)</td><td>18.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.03 (+5.33%)</td><td>0.03 (+6.19%)</td><td>0.03 (+3.30%)</td><td>0.02 (+16.12%)</td><td>0.00 (-9.09%)</td><td>166.50 (-13.86%)</td><td>145.16 (-6.55%)</td><td>146.40 (-3.24%)</td><td>122.40 (-5.04%)</td><td>21.47 <b>(-23.62%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.30 (n/a)</td><td>155.34 (n/a)</td><td>151.30 (n/a)</td><td>128.90 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.00 (+4.65%)</td><td>0.00 (+2.40%)</td><td>0.00 (+2.38%)</td><td>0.00 (-2.56%)</td><td>0.00 <b>(+78.15%)</b></td><td>1087.36 (+3.04%)</td><td>965.18 (-1.84%)</td><td>941.68 (-2.88%)</td><td>916.15 (-3.83%)</td><td>69.33 <b>(+69.40%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1055.26 (n/a)</td><td>983.28 (n/a)</td><td>969.58 (n/a)</td><td>952.66 (n/a)</td><td>40.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.01 (-3.57%)</td><td>0.01 (-2.24%)</td><td>0.01 (-2.44%)</td><td>0.01 (+0.00%)</td><td>0.00 <b>(-25.40%)</b></td><td>1132.32 (-0.92%)</td><td>1043.07 (+1.83%)</td><td>1021.79 (+1.78%)</td><td>1015.96 (+4.49%)</td><td>49.99 <b>(-28.55%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1142.80 (n/a)</td><td>1024.32 (n/a)</td><td>1003.90 (n/a)</td><td>972.29 (n/a)</td><td>69.97 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.99 (+3.20%)</td><td>0.98 (+2.60%)</td><td>0.99 (+3.35%)</td><td>0.96 (+1.75%)</td><td>0.01 <b>(+163.90%)</b></td><td>2175.99 (-1.72%)</td><td>2142.56 (-2.52%)</td><td>2124.80 (-3.25%)</td><td>2120.02 (-3.10%)</td><td>28.23 <b>(+151.40%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.00 (n/a)</td><td>2214.00 (n/a)</td><td>2198.03 (n/a)</td><td>2196.08 (n/a)</td><td>2187.86 (n/a)</td><td>11.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>5.70 (-7.36%)</td><td>5.00 (-9.27%)</td><td>5.04 (-7.67%)</td><td>4.41 (-11.50%)</td><td>0.53 <b>(+22.76%)</b></td><td>237.90 (+13.02%)</td><td>211.78 (+10.71%)</td><td>208.10 (+8.33%)</td><td>184.00 (+7.98%)</td><td>22.42 <b>(+51.97%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.15 (n/a)</td><td>5.51 (n/a)</td><td>5.46 (n/a)</td><td>4.98 (n/a)</td><td>0.43 (n/a)</td><td>210.50 (n/a)</td><td>191.30 (n/a)</td><td>192.10 (n/a)</td><td>170.40 (n/a)</td><td>14.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.04 (+6.36%)</td><td>4.97 (+0.63%)</td><td>4.52 (-9.26%)</td><td>4.19 (+11.62%)</td><td>0.85 (+10.61%)</td><td>250.50 (-10.41%)</td><td>215.78 (-0.59%)</td><td>232.00 (+10.21%)</td><td>173.50 (-6.01%)</td><td>35.00 (-8.05%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>5.68 (n/a)</td><td>4.94 (n/a)</td><td>4.98 (n/a)</td><td>3.75 (n/a)</td><td>0.77 (n/a)</td><td>279.60 (n/a)</td><td>217.06 (n/a)</td><td>210.50 (n/a)</td><td>184.60 (n/a)</td><td>38.07 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.44 (+5.25%)</td><td>5.04 (-2.76%)</td><td>5.14 (-1.89%)</td><td>3.73 (-10.97%)</td><td>1.05 <b>(+40.90%)</b></td><td>281.00 (+12.31%)</td><td>215.60 (+4.77%)</td><td>203.80 (+1.90%)</td><td>162.80 (-4.96%)</td><td>46.22 <b>(+50.86%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.12 (n/a)</td><td>5.18 (n/a)</td><td>5.24 (n/a)</td><td>4.19 (n/a)</td><td>0.75 (n/a)</td><td>250.20 (n/a)</td><td>205.78 (n/a)</td><td>200.00 (n/a)</td><td>171.30 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>6.22 (-0.96%)</td><td>5.00 (-1.12%)</td><td>4.91 (-0.20%)</td><td>3.65 (-13.84%)</td><td>1.05 <b>(+39.06%)</b></td><td>287.10 (+16.09%)</td><td>217.60 (+3.26%)</td><td>213.50 (+0.19%)</td><td>168.60 (+0.96%)</td><td>47.94 <b>(+64.45%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>6.28 (n/a)</td><td>5.06 (n/a)</td><td>4.92 (n/a)</td><td>4.24 (n/a)</td><td>0.76 (n/a)</td><td>247.30 (n/a)</td><td>210.74 (n/a)</td><td>213.10 (n/a)</td><td>167.00 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.06 (-3.15%)</td><td>8.29 (-1.50%)</td><td>8.29 (-2.23%)</td><td>7.78 (+3.64%)</td><td>0.50 <b>(-37.62%)</b></td><td>269.70 (-3.51%)</td><td>253.84 (+1.06%)</td><td>252.90 (+2.26%)</td><td>231.50 (+3.26%)</td><td>14.97 <b>(-38.17%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.35 (n/a)</td><td>8.41 (n/a)</td><td>8.48 (n/a)</td><td>7.50 (n/a)</td><td>0.80 (n/a)</td><td>279.50 (n/a)</td><td>251.18 (n/a)</td><td>247.30 (n/a)</td><td>224.20 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>8.50 (-13.46%)</td><td>8.00 (-1.70%)</td><td>8.14 (+3.10%)</td><td>7.09 (+1.65%)</td><td>0.55 <b>(-48.30%)</b></td><td>296.00 (-1.63%)</td><td>263.30 (+0.84%)</td><td>257.80 (-3.01%)</td><td>246.80 (+15.54%)</td><td>19.30 <b>(-39.55%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.82 (n/a)</td><td>8.13 (n/a)</td><td>7.89 (n/a)</td><td>6.97 (n/a)</td><td>1.06 (n/a)</td><td>300.90 (n/a)</td><td>261.10 (n/a)</td><td>265.80 (n/a)</td><td>213.60 (n/a)</td><td>31.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>8.90 (-3.27%)</td><td>7.67 (-7.84%)</td><td>7.20 (-10.53%)</td><td>6.96 (-11.33%)</td><td>0.83 <b>(+52.79%)</b></td><td>301.40 (+12.76%)</td><td>276.00 (+9.12%)</td><td>291.30 (+11.78%)</td><td>235.60 (+3.38%)</td><td>28.12 <b>(+79.69%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.20 (n/a)</td><td>8.32 (n/a)</td><td>8.05 (n/a)</td><td>7.85 (n/a)</td><td>0.54 (n/a)</td><td>267.30 (n/a)</td><td>252.94 (n/a)</td><td>260.60 (n/a)</td><td>227.90 (n/a)</td><td>15.65 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.05 (-7.50%)</td><td>8.53 (-5.42%)</td><td>8.61 (-4.06%)</td><td>7.62 (-1.36%)</td><td>0.54 <b>(-33.99%)</b></td><td>275.10 (+1.36%)</td><td>246.58 (+5.34%)</td><td>243.60 (+4.24%)</td><td>231.80 (+8.12%)</td><td>16.68 <b>(-26.88%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.78 (n/a)</td><td>9.02 (n/a)</td><td>8.97 (n/a)</td><td>7.73 (n/a)</td><td>0.82 (n/a)</td><td>271.40 (n/a)</td><td>234.08 (n/a)</td><td>233.70 (n/a)</td><td>214.40 (n/a)</td><td>22.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>10.40 (+3.20%)</td><td>8.58 (-8.60%)</td><td>8.87 (-7.43%)</td><td>5.45 <b>(-37.21%)</b></td><td>1.93 <b>(+249.35%)</b></td><td>384.50 <b>(+59.28%)</b></td><td>257.50 (+14.95%)</td><td>236.50 (+8.04%)</td><td>201.60 (-3.08%)</td><td>73.71 <b>(+455.38%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>10.08 (n/a)</td><td>9.39 (n/a)</td><td>9.58 (n/a)</td><td>8.69 (n/a)</td><td>0.55 (n/a)</td><td>241.40 (n/a)</td><td>224.02 (n/a)</td><td>218.90 (n/a)</td><td>208.00 (n/a)</td><td>13.27 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>9.64 (+2.52%)</td><td>9.03 (+9.44%)</td><td>9.07 (+14.61%)</td><td>8.35 (+12.00%)</td><td>0.50 <b>(-37.57%)</b></td><td>251.10 (-10.70%)</td><td>232.90 (-9.07%)</td><td>231.30 (-12.75%)</td><td>217.60 (-2.47%)</td><td>13.15 <b>(-45.37%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.40 (n/a)</td><td>8.25 (n/a)</td><td>7.91 (n/a)</td><td>7.46 (n/a)</td><td>0.81 (n/a)</td><td>281.20 (n/a)</td><td>256.12 (n/a)</td><td>265.10 (n/a)</td><td>223.10 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.18 (+13.42%)</td><td>11.68 (+8.06%)</td><td>11.57 (+7.25%)</td><td>10.60 (+5.25%)</td><td>1.01 <b>(+80.83%)</b></td><td>395.80 (-4.99%)</td><td>361.18 (-7.11%)</td><td>362.70 (-6.74%)</td><td>318.20 (-11.83%)</td><td>30.44 <b>(+51.30%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>11.62 (n/a)</td><td>10.81 (n/a)</td><td>10.78 (n/a)</td><td>10.07 (n/a)</td><td>0.56 (n/a)</td><td>416.60 (n/a)</td><td>388.84 (n/a)</td><td>388.90 (n/a)</td><td>360.90 (n/a)</td><td>20.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>12.74 (+3.30%)</td><td>12.03 (+6.56%)</td><td>11.90 (+6.81%)</td><td>11.48 (+12.72%)</td><td>0.48 <b>(-44.90%)</b></td><td>365.20 (-11.29%)</td><td>349.08 (-6.49%)</td><td>352.40 (-6.38%)</td><td>329.20 (-3.20%)</td><td>13.70 <b>(-52.61%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>12.33 (n/a)</td><td>11.29 (n/a)</td><td>11.14 (n/a)</td><td>10.19 (n/a)</td><td>0.87 (n/a)</td><td>411.70 (n/a)</td><td>373.32 (n/a)</td><td>376.40 (n/a)</td><td>340.10 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>12.17 (-1.65%)</td><td>11.55 (+0.20%)</td><td>11.65 (+1.90%)</td><td>10.70 (-4.02%)</td><td>0.56 (+14.45%)</td><td>391.90 (+4.20%)</td><td>363.74 (-0.14%)</td><td>360.20 (-1.85%)</td><td>344.70 (+1.68%)</td><td>18.01 <b>(+22.78%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>12.37 (n/a)</td><td>11.53 (n/a)</td><td>11.43 (n/a)</td><td>11.15 (n/a)</td><td>0.49 (n/a)</td><td>376.10 (n/a)</td><td>364.26 (n/a)</td><td>367.00 (n/a)</td><td>339.00 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.08 (-0.07%)</td><td>13.14 (+8.31%)</td><td>13.49 (+6.37%)</td><td>12.22 <b>(+27.45%)</b></td><td>0.81 <b>(-55.02%)</b></td><td>343.30 <b>(-21.55%)</b></td><td>320.30 (-9.14%)</td><td>310.80 (-5.99%)</td><td>297.90 (+0.07%)</td><td>19.94 <b>(-64.58%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>14.09 (n/a)</td><td>12.13 (n/a)</td><td>12.69 (n/a)</td><td>9.59 (n/a)</td><td>1.80 (n/a)</td><td>437.60 (n/a)</td><td>352.52 (n/a)</td><td>330.60 (n/a)</td><td>297.70 (n/a)</td><td>56.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>13.79 (-9.46%)</td><td>13.18 (-0.61%)</td><td>13.18 (-0.30%)</td><td>12.59 (+6.78%)</td><td>0.48 <b>(-63.45%)</b></td><td>333.00 (-6.36%)</td><td>318.68 (-0.05%)</td><td>318.20 (+0.28%)</td><td>304.00 (+10.42%)</td><td>11.65 <b>(-62.03%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.24 (n/a)</td><td>13.26 (n/a)</td><td>13.22 (n/a)</td><td>11.79 (n/a)</td><td>1.32 (n/a)</td><td>355.60 (n/a)</td><td>318.84 (n/a)</td><td>317.30 (n/a)</td><td>275.30 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.24 (-1.07%)</td><td>12.74 (+2.22%)</td><td>12.94 (+3.71%)</td><td>11.11 (+1.03%)</td><td>1.13 (-13.07%)</td><td>377.50 (-1.02%)</td><td>331.32 (-2.36%)</td><td>324.00 (-3.57%)</td><td>294.50 (+1.10%)</td><td>30.26 (-12.26%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>14.40 (n/a)</td><td>12.47 (n/a)</td><td>12.48 (n/a)</td><td>11.00 (n/a)</td><td>1.30 (n/a)</td><td>381.40 (n/a)</td><td>339.34 (n/a)</td><td>336.00 (n/a)</td><td>291.30 (n/a)</td><td>34.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.85 (-2.94%)</td><td>13.37 (-2.27%)</td><td>14.43 (+12.53%)</td><td>11.17 (-10.07%)</td><td>1.68 (+18.92%)</td><td>375.60 (+11.19%)</td><td>317.98 (+2.85%)</td><td>290.60 (-11.13%)</td><td>282.40 (+3.03%)</td><td>42.33 <b>(+36.95%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.30 (n/a)</td><td>13.68 (n/a)</td><td>12.83 (n/a)</td><td>12.42 (n/a)</td><td>1.41 (n/a)</td><td>337.80 (n/a)</td><td>309.16 (n/a)</td><td>327.00 (n/a)</td><td>274.10 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>14.06 (-6.35%)</td><td>11.99 (-12.23%)</td><td>11.79 (-12.56%)</td><td>10.44 (-17.61%)</td><td>1.31 <b>(+25.97%)</b></td><td>401.80 <b>(+21.39%)</b></td><td>352.94 (+14.46%)</td><td>355.70 (+14.37%)</td><td>298.40 (+6.76%)</td><td>36.91 <b>(+60.22%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>15.01 (n/a)</td><td>13.66 (n/a)</td><td>13.49 (n/a)</td><td>12.67 (n/a)</td><td>1.04 (n/a)</td><td>331.00 (n/a)</td><td>308.36 (n/a)</td><td>311.00 (n/a)</td><td>279.50 (n/a)</td><td>23.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.55 (+5.13%)</td><td>2.93 (-3.93%)</td><td>2.64 (-11.07%)</td><td>2.38 (-14.81%)</td><td>0.55 <b>(+129.94%)</b></td><td>220.20 (+17.38%)</td><td>184.16 (+6.46%)</td><td>198.40 (+12.41%)</td><td>147.60 (-4.84%)</td><td>32.97 <b>(+149.39%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.38 (n/a)</td><td>3.05 (n/a)</td><td>2.97 (n/a)</td><td>2.79 (n/a)</td><td>0.24 (n/a)</td><td>187.60 (n/a)</td><td>172.98 (n/a)</td><td>176.50 (n/a)</td><td>155.10 (n/a)</td><td>13.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>5.87 (+2.57%)</td><td>5.31 (+5.81%)</td><td>5.36 (+7.74%)</td><td>4.22 (-8.63%)</td><td>0.66 <b>(+48.62%)</b></td><td>248.30 (+9.43%)</td><td>200.34 (-4.72%)</td><td>195.60 (-7.17%)</td><td>178.80 (-2.51%)</td><td>28.28 <b>(+59.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>5.72 (n/a)</td><td>5.02 (n/a)</td><td>4.98 (n/a)</td><td>4.62 (n/a)</td><td>0.45 (n/a)</td><td>226.90 (n/a)</td><td>210.26 (n/a)</td><td>210.70 (n/a)</td><td>183.40 (n/a)</td><td>17.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>7.75 (-15.54%)</td><td>7.21 (-11.04%)</td><td>7.46 (-8.46%)</td><td>5.80 <b>(-21.14%)</b></td><td>0.80 (+15.37%)</td><td>361.30 <b>(+26.77%)</b></td><td>294.22 (+13.07%)</td><td>281.10 (+9.25%)</td><td>270.70 (+18.42%)</td><td>37.96 <b>(+76.14%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>9.17 (n/a)</td><td>8.11 (n/a)</td><td>8.15 (n/a)</td><td>7.36 (n/a)</td><td>0.70 (n/a)</td><td>285.00 (n/a)</td><td>260.22 (n/a)</td><td>257.30 (n/a)</td><td>228.60 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>3.45 (-6.65%)</td><td>2.92 (-1.74%)</td><td>3.06 (+5.76%)</td><td>1.91 (-5.63%)</td><td>0.59 (-8.01%)</td><td>274.20 (+5.95%)</td><td>187.60 (+1.80%)</td><td>171.10 (-5.42%)</td><td>151.80 (+7.13%)</td><td>49.11 (+8.16%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>3.70 (n/a)</td><td>2.97 (n/a)</td><td>2.90 (n/a)</td><td>2.03 (n/a)</td><td>0.64 (n/a)</td><td>258.80 (n/a)</td><td>184.28 (n/a)</td><td>180.90 (n/a)</td><td>141.70 (n/a)</td><td>45.41 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.30 (+17.01%)</td><td>0.24 <b>(+25.51%)</b></td><td>0.25 <b>(+28.33%)</b></td><td>0.17 <b>(+91.16%)</b></td><td>0.05 <b>(-27.18%)</b></td><td>187.40 <b>(-47.68%)</b></td><td>144.00 <b>(-27.94%)</b></td><td>129.90 <b>(-22.12%)</b></td><td>110.70 (-14.52%)</td><td>30.81 <b>(-67.18%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>358.20 (n/a)</td><td>199.82 (n/a)</td><td>166.80 (n/a)</td><td>129.50 (n/a)</td><td>93.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.19 <b>(-22.25%)</b></td><td>0.17 (-12.93%)</td><td>0.18 (-17.55%)</td><td>0.14 (-6.23%)</td><td>0.02 <b>(-51.31%)</b></td><td>231.50 (+6.68%)</td><td>189.82 (+12.39%)</td><td>182.90 <b>(+21.29%)</b></td><td>172.50 <b>(+28.64%)</b></td><td>23.73 <b>(-32.36%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.00 (n/a)</td><td>168.90 (n/a)</td><td>150.80 (n/a)</td><td>134.10 (n/a)</td><td>35.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.46 (-15.19%)</td><td>0.39 (-9.95%)</td><td>0.38 (-1.94%)</td><td>0.33 (-2.48%)</td><td>0.05 <b>(-52.35%)</b></td><td>198.00 (+2.54%)</td><td>171.02 (+7.97%)</td><td>172.20 (+1.95%)</td><td>142.60 (+17.95%)</td><td>19.66 <b>(-41.82%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>193.10 (n/a)</td><td>158.40 (n/a)</td><td>168.90 (n/a)</td><td>120.90 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.53 (-4.03%)</td><td>0.44 (+2.22%)</td><td>0.43 (+12.82%)</td><td>0.37 (+12.54%)</td><td>0.06 <b>(-40.80%)</b></td><td>178.80 (-11.13%)</td><td>152.08 (-4.94%)</td><td>153.70 (-11.36%)</td><td>123.30 (+4.23%)</td><td>19.76 <b>(-44.69%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>201.20 (n/a)</td><td>159.98 (n/a)</td><td>173.40 (n/a)</td><td>118.30 (n/a)</td><td>35.72 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.51 (-4.00%)</td><td>0.41 (-2.69%)</td><td>0.39 (-0.97%)</td><td>0.34 (-7.46%)</td><td>0.06 (-0.60%)</td><td>190.50 (+8.05%)</td><td>163.36 (+2.95%)</td><td>168.60 (+1.02%)</td><td>128.30 (+4.14%)</td><td>23.83 (+12.54%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.53 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.07 (n/a)</td><td>176.30 (n/a)</td><td>158.68 (n/a)</td><td>166.90 (n/a)</td><td>123.20 (n/a)</td><td>21.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>1.03 (-0.68%)</td><td>0.78 (-7.98%)</td><td>0.79 (-10.99%)</td><td>0.56 (-10.33%)</td><td>0.17 (-14.36%)</td><td>233.20 (+11.53%)</td><td>174.62 (+7.74%)</td><td>165.00 (+12.32%)</td><td>127.40 (+0.71%)</td><td>38.58 (-3.34%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.04 (n/a)</td><td>0.85 (n/a)</td><td>0.89 (n/a)</td><td>0.63 (n/a)</td><td>0.20 (n/a)</td><td>209.10 (n/a)</td><td>162.08 (n/a)</td><td>146.90 (n/a)</td><td>126.50 (n/a)</td><td>39.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.80 <b>(-26.33%)</b></td><td>0.72 (-16.92%)</td><td>0.75 (-9.92%)</td><td>0.57 (-6.68%)</td><td>0.10 <b>(-46.73%)</b></td><td>229.00 (+7.16%)</td><td>185.30 (+17.73%)</td><td>174.80 (+11.05%)</td><td>164.10 <b>(+35.73%)</b></td><td>27.37 <b>(-23.61%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.08 (n/a)</td><td>0.87 (n/a)</td><td>0.83 (n/a)</td><td>0.61 (n/a)</td><td>0.18 (n/a)</td><td>213.70 (n/a)</td><td>157.40 (n/a)</td><td>157.40 (n/a)</td><td>120.90 (n/a)</td><td>35.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.86 (-18.29%)</td><td>0.77 (-7.99%)</td><td>0.75 (-17.86%)</td><td>0.71 <b>(+42.28%)</b></td><td>0.06 <b>(-75.52%)</b></td><td>183.50 <b>(-29.72%)</b></td><td>170.66 (+0.66%)</td><td>174.90 <b>(+21.71%)</b></td><td>151.90 <b>(+22.40%)</b></td><td>12.51 <b>(-78.55%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.06 (n/a)</td><td>0.84 (n/a)</td><td>0.91 (n/a)</td><td>0.50 (n/a)</td><td>0.24 (n/a)</td><td>261.10 (n/a)</td><td>169.54 (n/a)</td><td>143.70 (n/a)</td><td>124.10 (n/a)</td><td>58.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.74 <b>(-27.23%)</b></td><td>0.65 <b>(-21.74%)</b></td><td>0.67 (-18.52%)</td><td>0.49 <b>(-21.54%)</b></td><td>0.09 <b>(-45.77%)</b></td><td>264.90 <b>(+27.48%)</b></td><td>205.92 <b>(+25.84%)</b></td><td>196.30 <b>(+22.76%)</b></td><td>177.00 <b>(+37.42%)</b></td><td>34.00 (+0.10%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>1.02 (n/a)</td><td>0.83 (n/a)</td><td>0.82 (n/a)</td><td>0.63 (n/a)</td><td>0.17 (n/a)</td><td>207.80 (n/a)</td><td>163.64 (n/a)</td><td>159.90 (n/a)</td><td>128.80 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:38:32</td><td>0.12 (-18.74%)</td><td>0.10 (-2.31%)</td><td>0.10 (+6.15%)</td><td>0.08 (-4.99%)</td><td>0.02 <b>(-40.62%)</b></td><td>203.30 (+5.28%)</td><td>162.94 (+0.07%)</td><td>165.20 (-5.82%)</td><td>137.50 <b>(+22.99%)</b></td><td>26.00 <b>(-23.62%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:07:43</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>193.10 (n/a)</td><td>162.82 (n/a)</td><td>175.40 (n/a)</td><td>111.80 (n/a)</td><td>34.04 (n/a)</td>
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
