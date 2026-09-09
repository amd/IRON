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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (-12.32%)</td><td>0.04 (+2.63%)</td><td>0.04 <b>(+22.24%)</b></td><td>0.03 (-13.65%)</td><td>0.01 (-14.38%)</td><td>225.80 (+15.85%)</td><td>154.08 (-2.56%)</td><td>138.50 (-18.19%)</td><td>127.80 (+14.11%)</td><td>40.83 (+16.34%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>158.12 (n/a)</td><td>169.30 (n/a)</td><td>112.00 (n/a)</td><td>35.10 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (+6.81%)</td><td>0.04 (+3.70%)</td><td>0.04 (-8.59%)</td><td>0.04 <b>(+22.28%)</b></td><td>0.00 <b>(-37.47%)</b></td><td>152.90 (-18.19%)</td><td>144.40 (-5.40%)</td><td>149.00 (+9.40%)</td><td>120.20 (-6.39%)</td><td>13.68 <b>(-52.79%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>152.64 (n/a)</td><td>136.20 (n/a)</td><td>128.40 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (+12.71%)</td><td>0.04 (+9.59%)</td><td>0.04 (-2.02%)</td><td>0.04 <b>(+27.56%)</b></td><td>0.01 (-10.85%)</td><td>168.40 <b>(-21.64%)</b></td><td>143.34 (-10.21%)</td><td>147.70 (+2.07%)</td><td>113.40 (-11.34%)</td><td>21.78 <b>(-38.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>159.64 (n/a)</td><td>144.70 (n/a)</td><td>127.90 (n/a)</td><td>35.55 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (-4.46%)</td><td>0.04 (-4.87%)</td><td>0.04 (+1.68%)</td><td>0.03 (+8.36%)</td><td>0.01 <b>(-21.32%)</b></td><td>194.60 (-7.73%)</td><td>164.04 (+3.80%)</td><td>152.30 (-1.61%)</td><td>132.50 (+4.66%)</td><td>27.64 (-19.84%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>158.04 (n/a)</td><td>154.80 (n/a)</td><td>126.60 (n/a)</td><td>34.48 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (-12.83%)</td><td>0.03 (-12.48%)</td><td>0.03 (-17.72%)</td><td>0.03 (-9.22%)</td><td>0.01 (-14.23%)</td><td>208.30 (+10.15%)</td><td>181.58 (+14.04%)</td><td>204.20 <b>(+21.55%)</b></td><td>135.00 (+14.70%)</td><td>34.31 (+9.71%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>159.22 (n/a)</td><td>168.00 (n/a)</td><td>117.70 (n/a)</td><td>31.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (+18.52%)</td><td>0.04 (+8.21%)</td><td>0.04 (+5.78%)</td><td>0.02 (-13.90%)</td><td>0.01 <b>(+102.31%)</b></td><td>250.60 (+16.18%)</td><td>169.02 (-2.66%)</td><td>159.20 (-5.46%)</td><td>123.00 (-15.64%)</td><td>52.90 <b>(+91.28%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>173.64 (n/a)</td><td>168.40 (n/a)</td><td>145.80 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (-10.20%)</td><td>0.03 (+2.45%)</td><td>0.03 (+13.31%)</td><td>0.03 <b>(+23.20%)</b></td><td>0.01 <b>(-36.72%)</b></td><td>221.90 (-18.84%)</td><td>182.48 (-7.46%)</td><td>191.10 (-11.73%)</td><td>129.80 (+11.32%)</td><td>33.96 <b>(-43.20%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>273.40 (n/a)</td><td>197.20 (n/a)</td><td>216.50 (n/a)</td><td>116.60 (n/a)</td><td>59.80 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (+9.22%)</td><td>0.03 (+9.76%)</td><td>0.03 (+2.04%)</td><td>0.03 <b>(+49.44%)</b></td><td>0.01 (-15.77%)</td><td>215.10 <b>(-33.09%)</b></td><td>186.28 (-12.53%)</td><td>207.30 (-1.99%)</td><td>132.70 (-8.42%)</td><td>36.20 <b>(-47.47%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>321.50 (n/a)</td><td>212.96 (n/a)</td><td>211.50 (n/a)</td><td>144.90 (n/a)</td><td>68.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (+17.15%)</td><td>0.08 (+3.36%)</td><td>0.08 (-3.02%)</td><td>0.07 (-2.41%)</td><td>0.02 <b>(+91.28%)</b></td><td>183.60 (+2.46%)</td><td>150.96 (-0.78%)</td><td>157.80 (+3.07%)</td><td>111.60 (-14.61%)</td><td>31.23 <b>(+68.02%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.20 (n/a)</td><td>152.14 (n/a)</td><td>153.10 (n/a)</td><td>130.70 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (+8.91%)</td><td>0.08 (+16.32%)</td><td>0.08 (+6.96%)</td><td>0.07 <b>(+34.16%)</b></td><td>0.01 (-13.39%)</td><td>187.50 <b>(-25.48%)</b></td><td>155.26 (-15.68%)</td><td>163.10 (-6.48%)</td><td>126.20 (-8.22%)</td><td>24.41 <b>(-42.66%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>251.60 (n/a)</td><td>184.14 (n/a)</td><td>174.40 (n/a)</td><td>137.50 (n/a)</td><td>42.58 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (+4.21%)</td><td>0.09 (+13.56%)</td><td>0.09 (+18.34%)</td><td>0.07 (+10.63%)</td><td>0.01 (-4.90%)</td><td>181.10 (-9.59%)</td><td>145.02 (-12.22%)</td><td>138.50 (-15.50%)</td><td>126.00 (-4.04%)</td><td>21.09 (-14.05%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.30 (n/a)</td><td>165.20 (n/a)</td><td>163.90 (n/a)</td><td>131.30 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 <b>(+23.42%)</b></td><td>0.09 <b>(+20.29%)</b></td><td>0.09 (+17.38%)</td><td>0.07 <b>(+23.18%)</b></td><td>0.02 <b>(+21.36%)</b></td><td>165.60 (-18.82%)</td><td>135.20 (-16.96%)</td><td>132.00 (-14.84%)</td><td>105.20 (-18.95%)</td><td>23.00 <b>(-20.89%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>162.82 (n/a)</td><td>155.00 (n/a)</td><td>129.80 (n/a)</td><td>29.08 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (-1.97%)</td><td>0.08 (+3.06%)</td><td>0.08 (+6.59%)</td><td>0.07 (-0.38%)</td><td>0.01 (-8.35%)</td><td>184.70 (+0.38%)</td><td>155.16 (-3.15%)</td><td>154.90 (-6.18%)</td><td>134.20 (+1.98%)</td><td>19.24 (-4.71%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.00 (n/a)</td><td>160.20 (n/a)</td><td>165.10 (n/a)</td><td>131.60 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 <b>(+32.49%)</b></td><td>0.09 (+9.61%)</td><td>0.08 (+2.42%)</td><td>0.07 <b>(+33.83%)</b></td><td>0.02 <b>(+28.61%)</b></td><td>176.80 <b>(-25.27%)</b></td><td>145.48 (-9.14%)</td><td>147.90 (-2.38%)</td><td>96.30 <b>(-24.47%)</b></td><td>31.92 <b>(-28.86%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>236.60 (n/a)</td><td>160.12 (n/a)</td><td>151.50 (n/a)</td><td>127.50 (n/a)</td><td>44.87 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (-1.79%)</td><td>0.08 (+13.96%)</td><td>0.08 <b>(+28.73%)</b></td><td>0.07 <b>(+35.47%)</b></td><td>0.01 <b>(-56.14%)</b></td><td>173.40 <b>(-26.21%)</b></td><td>157.58 (-15.63%)</td><td>157.50 <b>(-22.34%)</b></td><td>137.60 (+1.85%)</td><td>14.48 <b>(-66.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>235.00 (n/a)</td><td>186.78 (n/a)</td><td>202.80 (n/a)</td><td>135.10 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 <b>(+37.04%)</b></td><td>0.08 (+8.08%)</td><td>0.06 (-13.36%)</td><td>0.06 <b>(+38.32%)</b></td><td>0.02 <b>(+42.57%)</b></td><td>213.40 <b>(-27.71%)</b></td><td>174.76 (-7.59%)</td><td>190.60 (+15.38%)</td><td>103.50 <b>(-27.01%)</b></td><td>42.25 <b>(-31.61%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>295.20 (n/a)</td><td>189.12 (n/a)</td><td>165.20 (n/a)</td><td>141.80 (n/a)</td><td>61.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (+0.25%)</td><td>0.17 (-4.11%)</td><td>0.17 (-8.92%)</td><td>0.14 (-0.02%)</td><td>0.02 (-3.86%)</td><td>180.80 (+0.00%)</td><td>151.10 (+4.15%)</td><td>143.90 (+9.76%)</td><td>126.40 (-0.24%)</td><td>22.44 (-2.69%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>180.80 (n/a)</td><td>145.08 (n/a)</td><td>131.10 (n/a)</td><td>126.70 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (+0.40%)</td><td>0.16 (-3.03%)</td><td>0.15 (-14.84%)</td><td>0.15 <b>(+31.01%)</b></td><td>0.02 <b>(-37.39%)</b></td><td>168.30 <b>(-23.67%)</b></td><td>155.60 (-0.01%)</td><td>161.50 (+17.45%)</td><td>123.40 (-0.40%)</td><td>18.52 <b>(-53.39%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>220.50 (n/a)</td><td>155.62 (n/a)</td><td>137.50 (n/a)</td><td>123.90 (n/a)</td><td>39.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (-3.14%)</td><td>0.16 (-12.38%)</td><td>0.17 (-13.44%)</td><td>0.12 <b>(-24.25%)</b></td><td>0.03 <b>(+36.54%)</b></td><td>213.50 <b>(+32.03%)</b></td><td>160.06 (+16.39%)</td><td>148.10 (+15.52%)</td><td>127.20 (+3.25%)</td><td>33.82 <b>(+91.36%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>161.70 (n/a)</td><td>137.52 (n/a)</td><td>128.20 (n/a)</td><td>123.20 (n/a)</td><td>17.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (-10.09%)</td><td>0.16 (-9.36%)</td><td>0.15 <b>(-21.14%)</b></td><td>0.14 (+8.11%)</td><td>0.02 <b>(-24.57%)</b></td><td>176.10 (-7.51%)</td><td>157.86 (+9.09%)</td><td>169.00 <b>(+26.88%)</b></td><td>131.00 (+11.21%)</td><td>21.47 <b>(-23.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>190.40 (n/a)</td><td>144.70 (n/a)</td><td>133.20 (n/a)</td><td>117.80 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (-19.13%)</td><td>0.14 <b>(-23.22%)</b></td><td>0.14 <b>(-26.47%)</b></td><td>0.12 (-14.26%)</td><td>0.02 <b>(-32.36%)</b></td><td>200.20 (+16.60%)</td><td>176.80 <b>(+29.54%)</b></td><td>173.80 <b>(+35.99%)</b></td><td>149.80 <b>(+23.70%)</b></td><td>19.12 (-5.43%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>171.70 (n/a)</td><td>136.48 (n/a)</td><td>127.80 (n/a)</td><td>121.10 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (+6.34%)</td><td>0.16 (-2.88%)</td><td>0.17 (+5.25%)</td><td>0.06 <b>(-51.59%)</b></td><td>0.06 <b>(+111.63%)</b></td><td>401.40 <b>(+106.59%)</b></td><td>192.44 <b>(+22.70%)</b></td><td>148.60 (-4.99%)</td><td>113.10 (-5.99%)</td><td>118.79 <b>(+348.88%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>194.30 (n/a)</td><td>156.84 (n/a)</td><td>156.40 (n/a)</td><td>120.30 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (+19.90%)</td><td>0.14 (+1.56%)</td><td>0.15 (+4.95%)</td><td>0.09 <b>(-25.14%)</b></td><td>0.04 <b>(+173.59%)</b></td><td>283.80 <b>(+33.62%)</b></td><td>195.78 (+6.01%)</td><td>165.10 (-4.73%)</td><td>137.70 (-16.65%)</td><td>65.91 <b>(+203.67%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>184.68 (n/a)</td><td>173.30 (n/a)</td><td>165.20 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (-19.56%)</td><td>0.13 (-17.72%)</td><td>0.14 (-5.13%)</td><td>0.10 <b>(-22.30%)</b></td><td>0.02 (-13.94%)</td><td>235.00 <b>(+28.70%)</b></td><td>194.60 <b>(+22.04%)</b></td><td>180.80 (+5.42%)</td><td>164.80 <b>(+24.38%)</b></td><td>34.10 <b>(+40.08%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>182.60 (n/a)</td><td>159.46 (n/a)</td><td>171.50 (n/a)</td><td>132.50 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.38 (-6.87%)</td><td>0.32 (-6.79%)</td><td>0.32 (-14.65%)</td><td>0.28 (+7.22%)</td><td>0.04 <b>(-42.64%)</b></td><td>176.00 (-6.73%)</td><td>156.08 (+4.67%)</td><td>152.80 (+17.18%)</td><td>129.70 (+7.37%)</td><td>19.05 <b>(-42.35%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>188.70 (n/a)</td><td>149.12 (n/a)</td><td>130.40 (n/a)</td><td>120.80 (n/a)</td><td>33.04 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.38 (-1.55%)</td><td>0.32 (-5.47%)</td><td>0.34 (+1.91%)</td><td>0.22 <b>(-21.25%)</b></td><td>0.06 <b>(+50.34%)</b></td><td>220.70 <b>(+26.99%)</b></td><td>158.70 (+8.28%)</td><td>143.10 (-1.85%)</td><td>130.50 (+1.56%)</td><td>36.48 <b>(+99.96%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>173.80 (n/a)</td><td>146.56 (n/a)</td><td>145.80 (n/a)</td><td>128.50 (n/a)</td><td>18.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.39 (-2.77%)</td><td>0.29 (-14.04%)</td><td>0.28 (-9.09%)</td><td>0.20 <b>(-29.06%)</b></td><td>0.06 <b>(+21.32%)</b></td><td>240.60 <b>(+40.95%)</b></td><td>178.84 (+18.78%)</td><td>178.40 (+9.99%)</td><td>127.40 (+2.82%)</td><td>40.47 <b>(+76.40%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>170.70 (n/a)</td><td>150.56 (n/a)</td><td>162.20 (n/a)</td><td>123.90 (n/a)</td><td>22.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.36 (+7.27%)</td><td>0.31 (+0.96%)</td><td>0.33 (+1.05%)</td><td>0.26 (-6.08%)</td><td>0.04 <b>(+47.32%)</b></td><td>186.90 (+6.44%)</td><td>159.32 (-0.30%)</td><td>149.30 (-1.06%)</td><td>138.20 (-6.75%)</td><td>20.19 <b>(+46.49%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>175.60 (n/a)</td><td>159.80 (n/a)</td><td>150.90 (n/a)</td><td>148.20 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.39 (-5.50%)</td><td>0.32 (-4.26%)</td><td>0.34 (+4.25%)</td><td>0.25 (+0.36%)</td><td>0.06 (-5.88%)</td><td>193.50 (-0.36%)</td><td>156.40 (+4.35%)</td><td>142.70 (-4.03%)</td><td>127.40 (+5.81%)</td><td>29.81 (+1.50%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>194.20 (n/a)</td><td>149.88 (n/a)</td><td>148.70 (n/a)</td><td>120.40 (n/a)</td><td>29.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.42 (-10.57%)</td><td>0.33 (-6.15%)</td><td>0.36 (-3.17%)</td><td>0.21 (-7.98%)</td><td>0.09 (-5.65%)</td><td>239.60 (+8.66%)</td><td>157.02 (+7.01%)</td><td>137.70 (+3.22%)</td><td>115.70 (+11.79%)</td><td>49.51 (+12.54%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.47 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>220.50 (n/a)</td><td>146.74 (n/a)</td><td>133.40 (n/a)</td><td>103.50 (n/a)</td><td>44.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.41 (+13.08%)</td><td>0.31 (-3.43%)</td><td>0.31 (-11.30%)</td><td>0.19 (-9.11%)</td><td>0.08 <b>(+25.06%)</b></td><td>259.90 (+9.99%)</td><td>171.08 (+5.83%)</td><td>158.30 (+12.75%)</td><td>118.90 (-11.60%)</td><td>53.18 <b>(+24.50%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.35 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>236.30 (n/a)</td><td>161.66 (n/a)</td><td>140.40 (n/a)</td><td>134.50 (n/a)</td><td>42.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.38 (+3.02%)</td><td>0.32 (+6.29%)</td><td>0.33 (+18.02%)</td><td>0.23 (+1.87%)</td><td>0.06 (-7.60%)</td><td>212.70 (-1.85%)</td><td>158.32 (-6.37%)</td><td>148.80 (-15.26%)</td><td>127.90 (-2.96%)</td><td>32.64 (-6.64%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>216.70 (n/a)</td><td>169.10 (n/a)</td><td>175.60 (n/a)</td><td>131.80 (n/a)</td><td>34.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (-1.14%)</td><td>0.02 (-10.41%)</td><td>0.02 (-19.30%)</td><td>0.01 (-8.07%)</td><td>0.00 (-5.24%)</td><td>208.80 (+8.81%)</td><td>167.04 (+11.45%)</td><td>170.30 <b>(+23.94%)</b></td><td>119.40 (+1.19%)</td><td>33.85 (+2.00%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>191.90 (n/a)</td><td>149.88 (n/a)</td><td>137.40 (n/a)</td><td>118.00 (n/a)</td><td>33.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 <b>(-21.90%)</b></td><td>0.02 (-4.04%)</td><td>0.02 (-8.64%)</td><td>0.01 <b>(+61.17%)</b></td><td>0.00 <b>(-66.50%)</b></td><td>176.30 <b>(-37.97%)</b></td><td>160.80 (-4.71%)</td><td>164.60 (+9.44%)</td><td>139.00 <b>(+27.99%)</b></td><td>16.79 <b>(-74.96%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>284.20 (n/a)</td><td>168.74 (n/a)</td><td>150.40 (n/a)</td><td>108.60 (n/a)</td><td>67.07 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (+10.63%)</td><td>0.02 (+18.77%)</td><td>0.02 <b>(+28.70%)</b></td><td>0.01 <b>(+32.48%)</b></td><td>0.00 (-17.99%)</td><td>202.20 <b>(-24.52%)</b></td><td>154.40 (-18.85%)</td><td>150.10 <b>(-22.31%)</b></td><td>120.00 (-9.57%)</td><td>33.06 <b>(-41.79%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>267.90 (n/a)</td><td>190.26 (n/a)</td><td>193.20 (n/a)</td><td>132.70 (n/a)</td><td>56.80 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (-10.24%)</td><td>0.02 (-10.35%)</td><td>0.02 <b>(-22.52%)</b></td><td>0.01 (+18.95%)</td><td>0.00 <b>(-32.62%)</b></td><td>187.90 (-15.93%)</td><td>161.70 (+7.80%)</td><td>171.70 <b>(+29.10%)</b></td><td>121.40 (+11.48%)</td><td>26.80 <b>(-39.67%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.50 (n/a)</td><td>150.00 (n/a)</td><td>133.00 (n/a)</td><td>108.90 (n/a)</td><td>44.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (-15.64%)</td><td>0.01 (-16.05%)</td><td>0.01 (-12.38%)</td><td>0.01 (-14.74%)</td><td>0.00 <b>(-26.97%)</b></td><td>204.20 (+17.29%)</td><td>183.42 (+18.52%)</td><td>191.20 (+14.08%)</td><td>149.60 (+18.54%)</td><td>23.27 (+1.49%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.10 (n/a)</td><td>154.76 (n/a)</td><td>167.60 (n/a)</td><td>126.20 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (-1.90%)</td><td>0.01 <b>(-22.88%)</b></td><td>0.01 <b>(-43.02%)</b></td><td>0.01 <b>(-35.88%)</b></td><td>0.00 <b>(+91.49%)</b></td><td>306.20 <b>(+55.99%)</b></td><td>232.38 <b>(+41.52%)</b></td><td>268.90 <b>(+75.52%)</b></td><td>142.50 (+1.93%)</td><td>78.13 <b>(+198.86%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>196.30 (n/a)</td><td>164.20 (n/a)</td><td>153.20 (n/a)</td><td>139.80 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (+1.42%)</td><td>0.02 (+3.58%)</td><td>0.02 (+5.90%)</td><td>0.01 (+12.81%)</td><td>0.00 <b>(-26.13%)</b></td><td>206.50 (-11.34%)</td><td>164.06 (-5.91%)</td><td>153.10 (-5.55%)</td><td>129.80 (-1.37%)</td><td>29.41 <b>(-34.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>232.90 (n/a)</td><td>174.36 (n/a)</td><td>162.10 (n/a)</td><td>131.60 (n/a)</td><td>44.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (+15.67%)</td><td>0.02 (+11.60%)</td><td>0.02 (+12.93%)</td><td>0.01 (-0.66%)</td><td>0.00 <b>(+59.00%)</b></td><td>210.90 (+0.67%)</td><td>170.56 (-9.57%)</td><td>171.30 (-11.43%)</td><td>144.50 (-13.58%)</td><td>25.47 <b>(+40.87%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>209.50 (n/a)</td><td>188.62 (n/a)</td><td>193.40 (n/a)</td><td>167.20 (n/a)</td><td>18.08 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (-8.88%)</td><td>0.04 (+19.03%)</td><td>0.04 <b>(+21.81%)</b></td><td>0.03 <b>(+70.49%)</b></td><td>0.01 <b>(-37.41%)</b></td><td>203.80 <b>(-41.35%)</b></td><td>155.50 <b>(-23.79%)</b></td><td>142.60 (-17.90%)</td><td>124.00 (+9.73%)</td><td>34.37 <b>(-61.15%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>347.50 (n/a)</td><td>204.04 (n/a)</td><td>173.70 (n/a)</td><td>113.00 (n/a)</td><td>88.45 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (-1.83%)</td><td>0.04 (-1.74%)</td><td>0.04 (+7.17%)</td><td>0.02 <b>(-20.83%)</b></td><td>0.01 <b>(+23.17%)</b></td><td>241.00 <b>(+26.31%)</b></td><td>158.94 (+4.95%)</td><td>128.80 (-6.73%)</td><td>124.10 (+1.80%)</td><td>50.73 <b>(+53.67%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>151.44 (n/a)</td><td>138.10 (n/a)</td><td>121.90 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (+1.14%)</td><td>0.04 (+8.54%)</td><td>0.04 <b>(+21.09%)</b></td><td>0.03 (+11.59%)</td><td>0.00 <b>(-32.43%)</b></td><td>178.00 (-10.42%)</td><td>149.06 (-9.43%)</td><td>145.60 (-17.41%)</td><td>126.20 (-1.17%)</td><td>18.65 <b>(-38.59%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>164.58 (n/a)</td><td>176.30 (n/a)</td><td>127.70 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (-17.83%)</td><td>0.03 <b>(-25.73%)</b></td><td>0.03 <b>(-28.50%)</b></td><td>0.02 <b>(-34.20%)</b></td><td>0.01 (-1.36%)</td><td>255.80 <b>(+51.99%)</b></td><td>196.58 <b>(+36.59%)</b></td><td>193.60 <b>(+39.88%)</b></td><td>146.40 <b>(+21.70%)</b></td><td>40.52 <b>(+78.94%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>168.30 (n/a)</td><td>143.92 (n/a)</td><td>138.40 (n/a)</td><td>120.30 (n/a)</td><td>22.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 <b>(-22.33%)</b></td><td>0.03 (-5.79%)</td><td>0.03 (-3.46%)</td><td>0.03 (+11.84%)</td><td>0.00 <b>(-59.50%)</b></td><td>200.50 (-10.57%)</td><td>182.20 (+2.03%)</td><td>185.80 (+3.63%)</td><td>150.40 <b>(+28.77%)</b></td><td>19.06 <b>(-52.94%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>178.58 (n/a)</td><td>179.30 (n/a)</td><td>116.80 (n/a)</td><td>40.50 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (-1.73%)</td><td>0.03 (-8.38%)</td><td>0.03 (-4.55%)</td><td>0.02 (-5.53%)</td><td>0.01 (+17.55%)</td><td>224.50 (+5.85%)</td><td>175.16 (+10.76%)</td><td>162.50 (+4.77%)</td><td>127.00 (+1.76%)</td><td>41.43 <b>(+26.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>158.14 (n/a)</td><td>155.10 (n/a)</td><td>124.80 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 <b>(+39.04%)</b></td><td>0.03 (+6.24%)</td><td>0.04 (+8.21%)</td><td>0.02 (+2.03%)</td><td>0.01 <b>(+103.45%)</b></td><td>217.50 (-1.98%)</td><td>163.26 (-1.07%)</td><td>148.20 (-7.55%)</td><td>99.50 <b>(-28.05%)</b></td><td>47.84 <b>(+43.14%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>165.02 (n/a)</td><td>160.30 (n/a)</td><td>138.30 (n/a)</td><td>33.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+0.88%)</td><td>0.03 (-0.59%)</td><td>0.02 (-12.54%)</td><td>0.02 (+11.19%)</td><td>0.00 (-15.47%)</td><td>232.80 (-10.05%)</td><td>208.52 (+0.00%)</td><td>220.60 (+14.36%)</td><td>181.00 (-0.88%)</td><td>23.04 <b>(-25.99%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.80 (n/a)</td><td>208.52 (n/a)</td><td>192.90 (n/a)</td><td>182.60 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (-17.44%)</td><td>0.06 (-7.80%)</td><td>0.06 (-1.34%)</td><td>0.05 (-7.09%)</td><td>0.01 <b>(-37.61%)</b></td><td>213.40 (+7.61%)</td><td>180.60 (+7.40%)</td><td>174.70 (+1.39%)</td><td>159.00 <b>(+21.19%)</b></td><td>21.42 (-17.44%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>168.16 (n/a)</td><td>172.30 (n/a)</td><td>131.20 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 <b>(-23.86%)</b></td><td>0.06 (-16.25%)</td><td>0.05 (-16.78%)</td><td>0.04 <b>(-20.44%)</b></td><td>0.01 <b>(-32.98%)</b></td><td>240.20 <b>(+25.69%)</b></td><td>193.82 (+18.65%)</td><td>192.80 <b>(+20.12%)</b></td><td>164.10 <b>(+31.39%)</b></td><td>29.70 (+9.46%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>163.36 (n/a)</td><td>160.50 (n/a)</td><td>124.90 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (+7.43%)</td><td>0.07 (+4.62%)</td><td>0.07 (+2.76%)</td><td>0.06 (+13.25%)</td><td>0.01 (-14.77%)</td><td>181.30 (-11.73%)</td><td>154.56 (-5.87%)</td><td>160.40 (-2.73%)</td><td>116.80 (-6.93%)</td><td>23.52 <b>(-32.05%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>164.20 (n/a)</td><td>164.90 (n/a)</td><td>125.50 (n/a)</td><td>34.61 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (-10.43%)</td><td>0.05 (-18.92%)</td><td>0.05 (-18.59%)</td><td>0.05 <b>(-20.18%)</b></td><td>0.01 (+8.94%)</td><td>226.20 <b>(+25.32%)</b></td><td>198.84 <b>(+24.56%)</b></td><td>209.50 <b>(+22.80%)</b></td><td>145.40 (+11.67%)</td><td>32.53 <b>(+49.88%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>159.64 (n/a)</td><td>170.60 (n/a)</td><td>130.20 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (+15.06%)</td><td>0.06 (-2.08%)</td><td>0.06 (-7.45%)</td><td>0.05 (-1.93%)</td><td>0.01 <b>(+62.16%)</b></td><td>201.30 (+1.98%)</td><td>169.68 (+4.09%)</td><td>176.60 (+8.08%)</td><td>118.10 (-13.10%)</td><td>31.98 <b>(+38.80%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.40 (n/a)</td><td>163.02 (n/a)</td><td>163.40 (n/a)</td><td>135.90 (n/a)</td><td>23.04 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 <b>(-21.44%)</b></td><td>0.06 (-9.70%)</td><td>0.07 (-1.75%)</td><td>0.05 (-1.19%)</td><td>0.01 <b>(-41.90%)</b></td><td>207.30 (+1.22%)</td><td>169.02 (+8.03%)</td><td>157.80 (+1.81%)</td><td>139.20 <b>(+27.36%)</b></td><td>27.76 <b>(-23.96%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>204.80 (n/a)</td><td>156.46 (n/a)</td><td>155.00 (n/a)</td><td>109.30 (n/a)</td><td>36.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (+0.04%)</td><td>0.06 (+1.41%)</td><td>0.07 (+8.36%)</td><td>0.05 (-2.91%)</td><td>0.01 (-16.83%)</td><td>213.50 (+2.99%)</td><td>166.08 (-2.39%)</td><td>159.00 (-7.72%)</td><td>130.30 (+0.00%)</td><td>30.37 (-13.61%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>170.14 (n/a)</td><td>172.30 (n/a)</td><td>130.30 (n/a)</td><td>35.16 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 <b>(+28.37%)</b></td><td>0.05 (+6.06%)</td><td>0.05 (+0.07%)</td><td>0.04 (-19.89%)</td><td>0.01 <b>(+230.81%)</b></td><td>281.90 <b>(+24.84%)</b></td><td>203.80 (-1.34%)</td><td>206.10 (-0.10%)</td><td>142.30 <b>(-22.11%)</b></td><td>51.66 <b>(+224.79%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>225.80 (n/a)</td><td>206.56 (n/a)</td><td>206.30 (n/a)</td><td>182.70 (n/a)</td><td>15.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (+15.28%)</td><td>0.15 (+3.34%)</td><td>0.14 (-10.07%)</td><td>0.11 (-8.40%)</td><td>0.03 <b>(+56.82%)</b></td><td>199.10 (+9.16%)</td><td>151.04 (-0.76%)</td><td>152.10 (+11.18%)</td><td>111.60 (-13.22%)</td><td>36.21 <b>(+43.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>182.40 (n/a)</td><td>152.20 (n/a)</td><td>136.80 (n/a)</td><td>128.60 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (-0.76%)</td><td>0.12 (-11.21%)</td><td>0.11 (-11.83%)</td><td>0.06 <b>(-45.11%)</b></td><td>0.04 <b>(+126.15%)</b></td><td>335.80 <b>(+82.20%)</b></td><td>199.80 <b>(+23.29%)</b></td><td>191.10 (+13.41%)</td><td>136.40 (+0.74%)</td><td>80.33 <b>(+324.64%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>184.30 (n/a)</td><td>162.06 (n/a)</td><td>168.50 (n/a)</td><td>135.40 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (+7.00%)</td><td>0.14 (+5.42%)</td><td>0.14 (+18.52%)</td><td>0.11 (+13.80%)</td><td>0.03 (-7.42%)</td><td>189.30 (-12.16%)</td><td>155.12 (-6.23%)</td><td>148.10 (-15.66%)</td><td>114.50 (-6.53%)</td><td>32.65 (-17.83%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>215.50 (n/a)</td><td>165.42 (n/a)</td><td>175.60 (n/a)</td><td>122.50 (n/a)</td><td>39.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.17 (-1.69%)</td><td>0.14 (-1.11%)</td><td>0.13 (-2.43%)</td><td>0.10 (+0.86%)</td><td>0.03 (+12.49%)</td><td>200.00 (-0.84%)</td><td>159.86 (+2.03%)</td><td>161.00 (+2.48%)</td><td>122.80 (+1.66%)</td><td>36.63 (+12.38%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>201.70 (n/a)</td><td>156.68 (n/a)</td><td>157.10 (n/a)</td><td>120.80 (n/a)</td><td>32.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.17 (+15.75%)</td><td>0.14 (+13.13%)</td><td>0.14 (+16.09%)</td><td>0.10 <b>(+38.04%)</b></td><td>0.03 (-6.57%)</td><td>203.70 <b>(-27.56%)</b></td><td>159.70 (-13.85%)</td><td>148.40 (-13.87%)</td><td>124.40 (-13.61%)</td><td>31.85 <b>(-42.62%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>281.20 (n/a)</td><td>185.38 (n/a)</td><td>172.30 (n/a)</td><td>144.00 (n/a)</td><td>55.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.17 (+7.23%)</td><td>0.13 (+6.14%)</td><td>0.13 (+16.62%)</td><td>0.10 (+5.77%)</td><td>0.03 (-13.44%)</td><td>210.30 (-5.48%)</td><td>160.42 (-7.07%)</td><td>158.50 (-14.28%)</td><td>121.50 (-6.75%)</td><td>32.08 (-19.37%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>222.50 (n/a)</td><td>172.62 (n/a)</td><td>184.90 (n/a)</td><td>130.30 (n/a)</td><td>39.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (-0.88%)</td><td>0.12 (-0.57%)</td><td>0.14 (+11.43%)</td><td>0.09 (-10.38%)</td><td>0.03 <b>(+24.39%)</b></td><td>235.90 (+11.59%)</td><td>179.54 (+2.51%)</td><td>155.30 (-10.28%)</td><td>137.50 (+0.88%)</td><td>43.56 <b>(+41.62%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.40 (n/a)</td><td>175.14 (n/a)</td><td>173.10 (n/a)</td><td>136.30 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (+19.64%)</td><td>0.11 (+3.86%)</td><td>0.10 (-1.26%)</td><td>0.08 (-10.49%)</td><td>0.03 <b>(+95.60%)</b></td><td>265.40 (+11.70%)</td><td>205.32 (-0.61%)</td><td>213.20 (+1.28%)</td><td>139.80 (-16.39%)</td><td>45.84 <b>(+81.72%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>237.60 (n/a)</td><td>206.58 (n/a)</td><td>210.50 (n/a)</td><td>167.20 (n/a)</td><td>25.23 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>216.30 (n/a)</td><td>172.52 (n/a)</td><td>165.60 (n/a)</td><td>136.60 (n/a)</td><td>29.27 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>183.16 (n/a)</td><td>166.30 (n/a)</td><td>147.70 (n/a)</td><td>36.07 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.10 (n/a)</td><td>202.74 (n/a)</td><td>195.70 (n/a)</td><td>180.70 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>226.50 (n/a)</td><td>194.76 (n/a)</td><td>184.00 (n/a)</td><td>166.90 (n/a)</td><td>29.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>173.70 (n/a)</td><td>163.16 (n/a)</td><td>166.80 (n/a)</td><td>144.00 (n/a)</td><td>12.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>169.82 (n/a)</td><td>168.20 (n/a)</td><td>125.70 (n/a)</td><td>28.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>388.00 (n/a)</td><td>212.40 (n/a)</td><td>181.00 (n/a)</td><td>142.50 (n/a)</td><td>99.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>227.80 (n/a)</td><td>180.56 (n/a)</td><td>181.20 (n/a)</td><td>126.90 (n/a)</td><td>45.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>189.30 (n/a)</td><td>160.38 (n/a)</td><td>166.70 (n/a)</td><td>134.90 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>246.20 (n/a)</td><td>167.68 (n/a)</td><td>152.00 (n/a)</td><td>128.20 (n/a)</td><td>49.25 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>227.00 (n/a)</td><td>184.62 (n/a)</td><td>171.90 (n/a)</td><td>163.60 (n/a)</td><td>27.30 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.80 (n/a)</td><td>176.88 (n/a)</td><td>182.90 (n/a)</td><td>150.30 (n/a)</td><td>22.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.38 (-4.64%)</td><td>0.30 (-7.05%)</td><td>0.30 (-2.66%)</td><td>0.23 (-18.28%)</td><td>0.06 (+13.32%)</td><td>215.40 <b>(+22.32%)</b></td><td>170.12 (+8.69%)</td><td>165.80 (+2.73%)</td><td>128.90 (+4.88%)</td><td>31.01 <b>(+45.66%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.05 (n/a)</td><td>176.10 (n/a)</td><td>156.52 (n/a)</td><td>161.40 (n/a)</td><td>122.90 (n/a)</td><td>21.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>251.00 (n/a)</td><td>181.80 (n/a)</td><td>165.20 (n/a)</td><td>145.40 (n/a)</td><td>41.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>262.30 (n/a)</td><td>175.08 (n/a)</td><td>166.30 (n/a)</td><td>130.10 (n/a)</td><td>51.58 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>219.50 (n/a)</td><td>181.66 (n/a)</td><td>175.90 (n/a)</td><td>142.70 (n/a)</td><td>33.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>182.78 (n/a)</td><td>184.30 (n/a)</td><td>152.00 (n/a)</td><td>20.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.70 (n/a)</td><td>181.62 (n/a)</td><td>178.30 (n/a)</td><td>139.80 (n/a)</td><td>38.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>172.82 (n/a)</td><td>185.00 (n/a)</td><td>127.70 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.50 (n/a)</td><td>203.12 (n/a)</td><td>190.00 (n/a)</td><td>159.70 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>170.46 (n/a)</td><td>164.60 (n/a)</td><td>147.00 (n/a)</td><td>18.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>166.28 (n/a)</td><td>157.10 (n/a)</td><td>149.00 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>173.72 (n/a)</td><td>179.80 (n/a)</td><td>140.50 (n/a)</td><td>22.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>183.00 (n/a)</td><td>181.00 (n/a)</td><td>146.50 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>205.50 (n/a)</td><td>160.56 (n/a)</td><td>155.80 (n/a)</td><td>119.30 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>215.80 (n/a)</td><td>171.68 (n/a)</td><td>178.30 (n/a)</td><td>120.20 (n/a)</td><td>38.39 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>221.00 (n/a)</td><td>180.42 (n/a)</td><td>168.00 (n/a)</td><td>149.60 (n/a)</td><td>31.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>310.40 (n/a)</td><td>205.38 (n/a)</td><td>200.30 (n/a)</td><td>120.10 (n/a)</td><td>69.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>231.10 (n/a)</td><td>181.28 (n/a)</td><td>202.60 (n/a)</td><td>104.90 (n/a)</td><td>49.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>186.60 (n/a)</td><td>158.78 (n/a)</td><td>152.90 (n/a)</td><td>123.30 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>250.20 (n/a)</td><td>197.98 (n/a)</td><td>186.00 (n/a)</td><td>164.60 (n/a)</td><td>36.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>175.46 (n/a)</td><td>171.80 (n/a)</td><td>118.30 (n/a)</td><td>38.50 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>277.20 (n/a)</td><td>181.20 (n/a)</td><td>177.70 (n/a)</td><td>109.50 (n/a)</td><td>60.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.20 (n/a)</td><td>160.82 (n/a)</td><td>153.50 (n/a)</td><td>147.40 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.10 (n/a)</td><td>180.98 (n/a)</td><td>180.40 (n/a)</td><td>163.00 (n/a)</td><td>12.46 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>170.80 (n/a)</td><td>161.70 (n/a)</td><td>144.40 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>321.10 (n/a)</td><td>211.66 (n/a)</td><td>184.70 (n/a)</td><td>151.50 (n/a)</td><td>68.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.80 (n/a)</td><td>188.82 (n/a)</td><td>189.00 (n/a)</td><td>155.90 (n/a)</td><td>25.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.30 (n/a)</td><td>217.02 (n/a)</td><td>220.90 (n/a)</td><td>186.70 (n/a)</td><td>19.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>176.04 (n/a)</td><td>184.20 (n/a)</td><td>136.50 (n/a)</td><td>26.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>177.80 (n/a)</td><td>168.50 (n/a)</td><td>157.30 (n/a)</td><td>22.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>169.08 (n/a)</td><td>163.10 (n/a)</td><td>137.00 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>164.30 (n/a)</td><td>171.50 (n/a)</td><td>127.90 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>172.72 (n/a)</td><td>170.90 (n/a)</td><td>135.10 (n/a)</td><td>27.89 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.00 (n/a)</td><td>184.98 (n/a)</td><td>160.50 (n/a)</td><td>121.60 (n/a)</td><td>66.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>194.66 (n/a)</td><td>182.60 (n/a)</td><td>154.10 (n/a)</td><td>35.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.60 (n/a)</td><td>241.02 (n/a)</td><td>242.80 (n/a)</td><td>188.00 (n/a)</td><td>40.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.40 (n/a)</td><td>162.54 (n/a)</td><td>154.10 (n/a)</td><td>128.50 (n/a)</td><td>25.88 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>175.20 (n/a)</td><td>161.16 (n/a)</td><td>166.00 (n/a)</td><td>133.40 (n/a)</td><td>16.25 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.60 (n/a)</td><td>165.82 (n/a)</td><td>160.80 (n/a)</td><td>132.30 (n/a)</td><td>24.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.90 (n/a)</td><td>162.96 (n/a)</td><td>148.00 (n/a)</td><td>126.60 (n/a)</td><td>36.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.10 (n/a)</td><td>168.58 (n/a)</td><td>171.60 (n/a)</td><td>137.90 (n/a)</td><td>21.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.80 (n/a)</td><td>177.84 (n/a)</td><td>167.80 (n/a)</td><td>146.40 (n/a)</td><td>36.69 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>176.02 (n/a)</td><td>173.10 (n/a)</td><td>145.90 (n/a)</td><td>20.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.20 (n/a)</td><td>199.96 (n/a)</td><td>198.10 (n/a)</td><td>171.50 (n/a)</td><td>22.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.00 (n/a)</td><td>171.50 (n/a)</td><td>161.10 (n/a)</td><td>153.00 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>183.90 (n/a)</td><td>155.56 (n/a)</td><td>148.00 (n/a)</td><td>125.80 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>193.50 (n/a)</td><td>177.62 (n/a)</td><td>182.30 (n/a)</td><td>153.80 (n/a)</td><td>15.55 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>203.10 (n/a)</td><td>164.86 (n/a)</td><td>165.30 (n/a)</td><td>135.80 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>170.44 (n/a)</td><td>157.80 (n/a)</td><td>148.00 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.50 (n/a)</td><td>178.90 (n/a)</td><td>186.70 (n/a)</td><td>155.20 (n/a)</td><td>22.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>232.10 (n/a)</td><td>185.48 (n/a)</td><td>183.00 (n/a)</td><td>144.70 (n/a)</td><td>31.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>280.30 (n/a)</td><td>221.66 (n/a)</td><td>221.80 (n/a)</td><td>189.30 (n/a)</td><td>36.82 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>4.84 (+15.05%)</td><td>4.16 (+1.02%)</td><td>4.12 (+0.08%)</td><td>3.78 (-6.84%)</td><td>0.42 <b>(+635.07%)</b></td><td>2489.70 (+7.34%)</td><td>2276.84 (-0.26%)</td><td>2280.40 (-0.09%)</td><td>1943.70 (-13.08%)</td><td>216.10 <b>(+584.21%)</b></td><td>1903.25 (+15.05%)</td><td>1637.32 (+1.02%)</td><td>1622.21 (+0.08%)</td><td>1485.87 (-6.84%)</td><td>165.65 <b>(+635.07%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>4.21 (n/a)</td><td>4.12 (n/a)</td><td>4.12 (n/a)</td><td>4.05 (n/a)</td><td>0.06 (n/a)</td><td>2319.40 (n/a)</td><td>2282.88 (n/a)</td><td>2282.40 (n/a)</td><td>2236.20 (n/a)</td><td>31.58 (n/a)</td><td>1654.31 (n/a)</td><td>1620.74 (n/a)</td><td>1620.84 (n/a)</td><td>1594.99 (n/a)</td><td>22.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.08 (-9.70%)</td><td>0.94 (+6.26%)</td><td>0.95 (+2.42%)</td><td>0.70 (+12.41%)</td><td>0.16 <b>(-38.18%)</b></td><td>317.30 (-11.02%)</td><td>241.34 (-9.85%)</td><td>232.60 (-2.35%)</td><td>204.70 (+10.77%)</td><td>45.76 <b>(-41.82%)</b></td><td>46.11 (-9.70%)</td><td>40.10 (+6.26%)</td><td>40.57 (+2.42%)</td><td>29.74 (+12.41%)</td><td>6.63 <b>(-38.18%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.20 (n/a)</td><td>0.88 (n/a)</td><td>0.93 (n/a)</td><td>0.62 (n/a)</td><td>0.25 (n/a)</td><td>356.60 (n/a)</td><td>267.72 (n/a)</td><td>238.20 (n/a)</td><td>184.80 (n/a)</td><td>78.65 (n/a)</td><td>51.06 (n/a)</td><td>37.74 (n/a)</td><td>39.61 (n/a)</td><td>26.46 (n/a)</td><td>10.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.06 (-18.37%)</td><td>0.92 (-7.58%)</td><td>0.96 (+9.03%)</td><td>0.62 (-12.65%)</td><td>0.17 <b>(-33.33%)</b></td><td>357.80 (+14.46%)</td><td>250.76 (+6.36%)</td><td>231.10 (-8.26%)</td><td>208.60 <b>(+22.56%)</b></td><td>60.86 (+1.10%)</td><td>45.25 (-18.37%)</td><td>39.07 (-7.58%)</td><td>40.84 (+9.03%)</td><td>26.37 (-12.65%)</td><td>7.41 <b>(-33.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.30 (n/a)</td><td>0.99 (n/a)</td><td>0.88 (n/a)</td><td>0.71 (n/a)</td><td>0.26 (n/a)</td><td>312.60 (n/a)</td><td>235.76 (n/a)</td><td>251.90 (n/a)</td><td>170.20 (n/a)</td><td>60.20 (n/a)</td><td>55.43 (n/a)</td><td>42.27 (n/a)</td><td>37.46 (n/a)</td><td>30.19 (n/a)</td><td>11.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.52 (-0.05%)</td><td>0.52 (-0.12%)</td><td>0.52 (-0.08%)</td><td>0.52 (-0.35%)</td><td>0.00 <b>(+78.87%)</b></td><td>48728.90 (+0.35%)</td><td>48542.48 (+0.12%)</td><td>48489.90 (+0.08%)</td><td>48458.20 (+0.05%)</td><td>109.21 <b>(+79.63%)</b></td><td>354.53 (-0.05%)</td><td>353.92 (-0.12%)</td><td>354.30 (-0.08%)</td><td>352.56 (-0.35%)</td><td>0.79 <b>(+78.86%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48557.30 (n/a)</td><td>48486.46 (n/a)</td><td>48450.40 (n/a)</td><td>48433.80 (n/a)</td><td>60.80 (n/a)</td><td>354.71 (n/a)</td><td>354.32 (n/a)</td><td>354.59 (n/a)</td><td>353.81 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (+2.88%)</td><td>0.21 (+0.42%)</td><td>0.21 (-0.36%)</td><td>0.21 (-0.63%)</td><td>0.00 <b>(+279.24%)</b></td><td>120268.80 (+0.64%)</td><td>118379.04 (-0.39%)</td><td>119171.60 (+0.36%)</td><td>114792.00 (-2.80%)</td><td>2164.83 <b>(+269.87%)</b></td><td>149.66 (+2.88%)</td><td>145.17 (+0.42%)</td><td>144.16 (-0.36%)</td><td>142.85 (-0.63%)</td><td>2.70 <b>(+279.23%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119505.70 (n/a)</td><td>118843.18 (n/a)</td><td>118740.00 (n/a)</td><td>118101.40 (n/a)</td><td>585.29 (n/a)</td><td>145.47 (n/a)</td><td>144.56 (n/a)</td><td>144.68 (n/a)</td><td>143.76 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.90 (-0.12%)</td><td>0.89 (+0.43%)</td><td>0.89 (+0.35%)</td><td>0.88 (+0.74%)</td><td>0.01 <b>(-21.81%)</b></td><td>28553.60 (-0.74%)</td><td>28199.94 (-0.43%)</td><td>28214.50 (-0.35%)</td><td>27928.50 (+0.12%)</td><td>239.31 <b>(-22.30%)</b></td><td>615.14 (-0.12%)</td><td>609.25 (+0.43%)</td><td>608.90 (+0.35%)</td><td>601.67 (+0.74%)</td><td>5.15 <b>(-21.81%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28765.60 (n/a)</td><td>28321.40 (n/a)</td><td>28314.30 (n/a)</td><td>27894.80 (n/a)</td><td>307.99 (n/a)</td><td>615.88 (n/a)</td><td>606.66 (n/a)</td><td>606.76 (n/a)</td><td>597.24 (n/a)</td><td>6.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.54 (+1.06%)</td><td>3.48 (+2.98%)</td><td>3.53 (+4.78%)</td><td>3.34 (+1.09%)</td><td>0.09 (+18.08%)</td><td>7540.80 (-1.08%)</td><td>7232.20 (-2.88%)</td><td>7127.80 (-4.56%)</td><td>7116.80 (-1.05%)</td><td>181.93 (+16.06%)</td><td>2413.99 (+1.06%)</td><td>2376.64 (+2.98%)</td><td>2410.28 (+4.78%)</td><td>2278.24 (+1.09%)</td><td>58.27 (+18.08%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.50 (n/a)</td><td>3.38 (n/a)</td><td>3.37 (n/a)</td><td>3.30 (n/a)</td><td>0.07 (n/a)</td><td>7623.10 (n/a)</td><td>7446.60 (n/a)</td><td>7468.50 (n/a)</td><td>7192.50 (n/a)</td><td>156.75 (n/a)</td><td>2388.59 (n/a)</td><td>2307.91 (n/a)</td><td>2300.30 (n/a)</td><td>2253.65 (n/a)</td><td>49.35 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.04 (+3.29%)</td><td>2.87 (+1.78%)</td><td>2.84 (+0.80%)</td><td>2.82 (+2.82%)</td><td>0.09 <b>(+22.31%)</b></td><td>8931.60 (-2.74%)</td><td>8767.14 (-1.72%)</td><td>8868.90 (-0.80%)</td><td>8285.10 (-3.18%)</td><td>270.89 (+15.02%)</td><td>2073.59 (+3.29%)</td><td>1961.13 (+1.78%)</td><td>1937.10 (+0.80%)</td><td>1923.49 (+2.82%)</td><td>63.15 <b>(+22.31%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>2.94 (n/a)</td><td>2.82 (n/a)</td><td>2.81 (n/a)</td><td>2.74 (n/a)</td><td>0.08 (n/a)</td><td>9183.50 (n/a)</td><td>8920.94 (n/a)</td><td>8940.20 (n/a)</td><td>8557.40 (n/a)</td><td>235.52 (n/a)</td><td>2007.60 (n/a)</td><td>1926.88 (n/a)</td><td>1921.63 (n/a)</td><td>1870.73 (n/a)</td><td>51.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.31 (+0.73%)</td><td>3.21 (+2.68%)</td><td>3.19 (+1.55%)</td><td>3.15 (+8.90%)</td><td>0.06 <b>(-57.57%)</b></td><td>7985.80 (-8.18%)</td><td>7854.12 (-2.75%)</td><td>7878.60 (-1.53%)</td><td>7613.70 (-0.72%)</td><td>143.96 <b>(-61.82%)</b></td><td>2256.45 (+0.73%)</td><td>2187.98 (+2.68%)</td><td>2180.59 (+1.55%)</td><td>2151.31 (+8.90%)</td><td>40.81 <b>(-57.57%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.28 (n/a)</td><td>3.12 (n/a)</td><td>3.15 (n/a)</td><td>2.89 (n/a)</td><td>0.14 (n/a)</td><td>8696.90 (n/a)</td><td>8075.92 (n/a)</td><td>8000.90 (n/a)</td><td>7669.00 (n/a)</td><td>377.09 (n/a)</td><td>2240.18 (n/a)</td><td>2130.89 (n/a)</td><td>2147.24 (n/a)</td><td>1975.41 (n/a)</td><td>96.17 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.79 (+0.00%)</td><td>0.79 (+0.04%)</td><td>0.79 (-0.03%)</td><td>0.79 (+0.16%)</td><td>0.00 <b>(-74.26%)</b></td><td>96155.90 (-0.16%)</td><td>96131.64 (-0.04%)</td><td>96143.30 (+0.03%)</td><td>96097.90 (-0.00%)</td><td>24.14 <b>(-74.29%)</b></td><td>715.10 (+0.00%)</td><td>714.85 (+0.04%)</td><td>714.76 (-0.03%)</td><td>714.67 (+0.16%)</td><td>0.18 <b>(-74.26%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96313.40 (n/a)</td><td>96170.74 (n/a)</td><td>96112.20 (n/a)</td><td>96099.70 (n/a)</td><td>93.88 (n/a)</td><td>715.09 (n/a)</td><td>714.56 (n/a)</td><td>714.99 (n/a)</td><td>713.50 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.73 (-0.00%)</td><td>0.73 (-0.06%)</td><td>0.73 (-0.01%)</td><td>0.73 (-0.10%)</td><td>0.00 <b>(+23.49%)</b></td><td>103559.40 (+0.10%)</td><td>103314.98 (+0.06%)</td><td>103307.10 (+0.01%)</td><td>102971.20 (+0.00%)</td><td>219.71 <b>(+23.63%)</b></td><td>667.37 (-0.00%)</td><td>665.15 (-0.06%)</td><td>665.20 (-0.01%)</td><td>663.58 (-0.10%)</td><td>1.42 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103456.20 (n/a)</td><td>103256.14 (n/a)</td><td>103293.20 (n/a)</td><td>102967.70 (n/a)</td><td>177.72 (n/a)</td><td>667.39 (n/a)</td><td>665.53 (n/a)</td><td>665.29 (n/a)</td><td>664.24 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.70 (-0.34%)</td><td>0.69 (-0.33%)</td><td>0.69 (-0.20%)</td><td>0.69 (-0.23%)</td><td>0.00 <b>(-27.08%)</b></td><td>108984.60 (+0.23%)</td><td>108800.78 (+0.33%)</td><td>108776.80 (+0.20%)</td><td>108495.90 (+0.34%)</td><td>201.46 <b>(-26.62%)</b></td><td>633.38 (-0.34%)</td><td>631.61 (-0.33%)</td><td>631.75 (-0.20%)</td><td>630.54 (-0.23%)</td><td>1.17 <b>(-27.08%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108732.40 (n/a)</td><td>108446.74 (n/a)</td><td>108556.50 (n/a)</td><td>108128.70 (n/a)</td><td>274.56 (n/a)</td><td>635.53 (n/a)</td><td>633.67 (n/a)</td><td>633.03 (n/a)</td><td>632.01 (n/a)</td><td>1.61 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.35 (+8.19%)</td><td>6.44 (+3.63%)</td><td>6.68 (+3.45%)</td><td>4.88 (+0.08%)</td><td>0.94 <b>(+22.20%)</b></td><td>1827.90 (-0.08%)</td><td>1411.62 (-2.96%)</td><td>1333.70 (-3.34%)</td><td>1212.20 (-7.56%)</td><td>241.90 (+13.84%)</td><td>442.90 (+8.19%)</td><td>388.07 (+3.63%)</td><td>402.54 (+3.45%)</td><td>293.72 (+0.08%)</td><td>56.80 <b>(+22.20%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>6.80 (n/a)</td><td>6.22 (n/a)</td><td>6.46 (n/a)</td><td>4.87 (n/a)</td><td>0.77 (n/a)</td><td>1829.30 (n/a)</td><td>1454.70 (n/a)</td><td>1379.80 (n/a)</td><td>1311.40 (n/a)</td><td>212.48 (n/a)</td><td>409.38 (n/a)</td><td>374.48 (n/a)</td><td>389.10 (n/a)</td><td>293.48 (n/a)</td><td>46.48 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.07 (+0.43%)</td><td>6.51 (+9.41%)</td><td>6.75 (+6.38%)</td><td>5.74 <b>(+34.07%)</b></td><td>0.57 <b>(-51.53%)</b></td><td>1551.90 <b>(-25.41%)</b></td><td>1377.56 (-11.23%)</td><td>1320.80 (-5.99%)</td><td>1261.00 (-0.43%)</td><td>125.53 <b>(-63.62%)</b></td><td>425.76 (+0.43%)</td><td>392.24 (+9.41%)</td><td>406.48 (+6.38%)</td><td>345.95 <b>(+34.07%)</b></td><td>34.46 <b>(-51.53%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>7.04 (n/a)</td><td>5.95 (n/a)</td><td>6.34 (n/a)</td><td>4.28 (n/a)</td><td>1.18 (n/a)</td><td>2080.60 (n/a)</td><td>1551.90 (n/a)</td><td>1405.00 (n/a)</td><td>1266.40 (n/a)</td><td>345.05 (n/a)</td><td>423.94 (n/a)</td><td>358.49 (n/a)</td><td>382.10 (n/a)</td><td>258.04 (n/a)</td><td>71.10 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>6.88 (+1.97%)</td><td>6.06 (-5.64%)</td><td>6.19 (-4.76%)</td><td>4.58 <b>(-22.68%)</b></td><td>0.88 <b>(+176.22%)</b></td><td>1947.40 <b>(+29.34%)</b></td><td>1501.60 (+7.89%)</td><td>1440.40 (+5.00%)</td><td>1295.70 (-1.94%)</td><td>257.01 <b>(+260.05%)</b></td><td>414.34 (+1.97%)</td><td>364.74 (-5.64%)</td><td>372.73 (-4.76%)</td><td>275.68 <b>(-22.68%)</b></td><td>52.90 <b>(+176.22%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>6.75 (n/a)</td><td>6.42 (n/a)</td><td>6.50 (n/a)</td><td>5.92 (n/a)</td><td>0.32 (n/a)</td><td>1505.70 (n/a)</td><td>1391.80 (n/a)</td><td>1371.80 (n/a)</td><td>1321.30 (n/a)</td><td>71.38 (n/a)</td><td>406.32 (n/a)</td><td>386.53 (n/a)</td><td>391.37 (n/a)</td><td>356.57 (n/a)</td><td>19.15 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.99 (+0.14%)</td><td>7.78 (+0.39%)</td><td>7.89 (-0.47%)</td><td>7.22 (+2.82%)</td><td>0.32 <b>(-21.51%)</b></td><td>4826.50 (-2.74%)</td><td>4487.98 (-0.48%)</td><td>4421.20 (+0.47%)</td><td>4365.80 (-0.14%)</td><td>193.17 <b>(-23.85%)</b></td><td>491.88 (+0.14%)</td><td>479.17 (+0.39%)</td><td>485.72 (-0.47%)</td><td>444.93 (+2.82%)</td><td>19.61 <b>(-21.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>7.97 (n/a)</td><td>7.75 (n/a)</td><td>7.92 (n/a)</td><td>7.03 (n/a)</td><td>0.41 (n/a)</td><td>4962.50 (n/a)</td><td>4509.74 (n/a)</td><td>4400.50 (n/a)</td><td>4371.90 (n/a)</td><td>253.68 (n/a)</td><td>491.20 (n/a)</td><td>477.31 (n/a)</td><td>488.01 (n/a)</td><td>432.75 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.98 (+3.75%)</td><td>7.64 (+1.68%)</td><td>7.57 (-0.54%)</td><td>7.52 (+6.55%)</td><td>0.19 <b>(-26.72%)</b></td><td>4638.70 (-6.15%)</td><td>4565.14 (-1.71%)</td><td>4604.30 (+0.54%)</td><td>4369.90 (-3.62%)</td><td>110.21 <b>(-34.39%)</b></td><td>491.43 (+3.75%)</td><td>470.64 (+1.68%)</td><td>466.41 (-0.54%)</td><td>462.95 (+6.55%)</td><td>11.72 <b>(-26.72%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>7.69 (n/a)</td><td>7.51 (n/a)</td><td>7.61 (n/a)</td><td>7.05 (n/a)</td><td>0.26 (n/a)</td><td>4942.50 (n/a)</td><td>4644.46 (n/a)</td><td>4579.50 (n/a)</td><td>4533.80 (n/a)</td><td>167.97 (n/a)</td><td>473.67 (n/a)</td><td>462.84 (n/a)</td><td>468.93 (n/a)</td><td>434.49 (n/a)</td><td>16.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.78 (+0.47%)</td><td>7.08 (-3.37%)</td><td>6.77 (-7.64%)</td><td>6.72 (-1.77%)</td><td>0.48 <b>(+46.43%)</b></td><td>5189.80 (+1.80%)</td><td>4939.14 (+3.68%)</td><td>5146.40 (+8.27%)</td><td>4483.40 (-0.47%)</td><td>321.95 <b>(+48.76%)</b></td><td>478.98 (+0.47%)</td><td>436.33 (-3.37%)</td><td>417.28 (-7.64%)</td><td>413.79 (-1.77%)</td><td>29.49 <b>(+46.43%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>7.74 (n/a)</td><td>7.33 (n/a)</td><td>7.33 (n/a)</td><td>6.84 (n/a)</td><td>0.33 (n/a)</td><td>5097.90 (n/a)</td><td>4763.82 (n/a)</td><td>4753.40 (n/a)</td><td>4504.60 (n/a)</td><td>216.42 (n/a)</td><td>476.73 (n/a)</td><td>451.52 (n/a)</td><td>451.78 (n/a)</td><td>421.25 (n/a)</td><td>20.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.79 (-0.00%)</td><td>0.79 (-0.04%)</td><td>0.79 (-0.02%)</td><td>0.79 (-0.09%)</td><td>0.00 <b>(+124.16%)</b></td><td>95537.40 (+0.09%)</td><td>95449.74 (+0.04%)</td><td>95406.80 (+0.02%)</td><td>95388.40 (+0.00%)</td><td>76.00 <b>(+124.40%)</b></td><td>720.42 (-0.00%)</td><td>719.95 (-0.04%)</td><td>720.28 (-0.02%)</td><td>719.29 (-0.09%)</td><td>0.57 <b>(+124.14%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95449.60 (n/a)</td><td>95412.38 (n/a)</td><td>95392.30 (n/a)</td><td>95384.90 (n/a)</td><td>33.87 (n/a)</td><td>720.44 (n/a)</td><td>720.24 (n/a)</td><td>720.39 (n/a)</td><td>719.96 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.74 (+0.37%)</td><td>0.74 (+0.07%)</td><td>0.74 (+0.00%)</td><td>0.74 (-0.01%)</td><td>0.00 <b>(+400.20%)</b></td><td>102678.60 (+0.01%)</td><td>102524.20 (-0.07%)</td><td>102583.00 (-0.00%)</td><td>102188.50 (-0.37%)</td><td>192.20 <b>(+398.23%)</b></td><td>672.48 (+0.37%)</td><td>670.28 (+0.07%)</td><td>669.89 (+0.00%)</td><td>669.27 (-0.01%)</td><td>1.26 <b>(+400.21%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102665.80 (n/a)</td><td>102598.92 (n/a)</td><td>102584.60 (n/a)</td><td>102569.40 (n/a)</td><td>38.58 (n/a)</td><td>669.98 (n/a)</td><td>669.79 (n/a)</td><td>669.88 (n/a)</td><td>669.35 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.70 (-0.02%)</td><td>0.70 (+0.03%)</td><td>0.70 (+0.01%)</td><td>0.70 (+0.10%)</td><td>0.00 <b>(-67.69%)</b></td><td>107381.30 (-0.10%)</td><td>107350.58 (-0.03%)</td><td>107355.70 (-0.01%)</td><td>107325.00 (+0.02%)</td><td>23.76 <b>(-67.71%)</b></td><td>640.29 (-0.02%)</td><td>640.14 (+0.03%)</td><td>640.11 (+0.01%)</td><td>639.96 (+0.10%)</td><td>0.14 <b>(-67.69%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107485.30 (n/a)</td><td>107380.30 (n/a)</td><td>107364.30 (n/a)</td><td>107308.70 (n/a)</td><td>73.59 (n/a)</td><td>640.39 (n/a)</td><td>639.96 (n/a)</td><td>640.06 (n/a)</td><td>639.34 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>4.20 (+14.77%)</td><td>3.51 (+5.27%)</td><td>3.61 (+14.30%)</td><td>3.01 (-3.35%)</td><td>0.47 <b>(+73.62%)</b></td><td>2676.20 (+3.47%)</td><td>2327.84 (-4.15%)</td><td>2231.90 (-12.51%)</td><td>1918.20 (-12.87%)</td><td>305.37 <b>(+58.16%)</b></td><td>1102.03 (+14.77%)</td><td>921.10 (+5.27%)</td><td>947.16 (+14.30%)</td><td>789.90 (-3.35%)</td><td>124.39 <b>(+73.62%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.66 (n/a)</td><td>3.34 (n/a)</td><td>3.16 (n/a)</td><td>3.12 (n/a)</td><td>0.27 (n/a)</td><td>2586.50 (n/a)</td><td>2428.62 (n/a)</td><td>2551.10 (n/a)</td><td>2201.50 (n/a)</td><td>193.07 (n/a)</td><td>960.21 (n/a)</td><td>874.98 (n/a)</td><td>828.63 (n/a)</td><td>817.28 (n/a)</td><td>71.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.48 <b>(+25.10%)</b></td><td>0.35 (+1.20%)</td><td>0.33 (-5.88%)</td><td>0.28 (-5.29%)</td><td>0.08 <b>(+137.05%)</b></td><td>4460.00 (+5.59%)</td><td>3681.18 (+1.40%)</td><td>3774.00 (+6.25%)</td><td>2570.90 <b>(-20.06%)</b></td><td>687.04 <b>(+87.41%)</b></td><td>26.10 <b>(+25.10%)</b></td><td>18.85 (+1.20%)</td><td>17.78 (-5.88%)</td><td>15.05 (-5.29%)</td><td>4.22 <b>(+137.05%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.03 (n/a)</td><td>4224.00 (n/a)</td><td>3630.26 (n/a)</td><td>3552.00 (n/a)</td><td>3216.10 (n/a)</td><td>366.59 (n/a)</td><td>20.87 (n/a)</td><td>18.63 (n/a)</td><td>18.89 (n/a)</td><td>15.89 (n/a)</td><td>1.78 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>4.93 (-0.74%)</td><td>4.05 (-5.70%)</td><td>3.64 <b>(-21.80%)</b></td><td>3.48 (+10.62%)</td><td>0.66 (-15.20%)</td><td>1911.20 (-9.60%)</td><td>1675.02 (+5.00%)</td><td>1829.00 <b>(+27.88%)</b></td><td>1350.20 (+0.75%)</td><td>255.81 <b>(-22.05%)</b></td><td>1522.16 (-0.74%)</td><td>1251.81 (-5.70%)</td><td>1123.70 <b>(-21.80%)</b></td><td>1075.36 (+10.62%)</td><td>203.56 (-15.20%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>4.96 (n/a)</td><td>4.30 (n/a)</td><td>4.65 (n/a)</td><td>3.15 (n/a)</td><td>0.78 (n/a)</td><td>2114.10 (n/a)</td><td>1595.32 (n/a)</td><td>1430.30 (n/a)</td><td>1340.20 (n/a)</td><td>328.16 (n/a)</td><td>1533.56 (n/a)</td><td>1327.53 (n/a)</td><td>1436.87 (n/a)</td><td>972.14 (n/a)</td><td>240.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.51 (n/a)</td><td>12.87 (n/a)</td><td>13.07 (n/a)</td><td>12.14 (n/a)</td><td>0.64 (n/a)</td><td>13.50 (n/a)</td><td>12.87 (n/a)</td><td>13.07 (n/a)</td><td>12.14 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>25.21 (+2.84%)</td><td>24.51 (+3.19%)</td><td>25.06 (+3.32%)</td><td>22.45 (+1.86%)</td><td>1.17 (+15.61%)</td><td>25.20 (+2.84%)</td><td>24.49 (+3.19%)</td><td>25.05 (+3.32%)</td><td>22.44 (+1.86%)</td><td>1.17 (+15.61%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>24.52 (n/a)</td><td>23.75 (n/a)</td><td>24.26 (n/a)</td><td>22.04 (n/a)</td><td>1.01 (n/a)</td><td>24.50 (n/a)</td><td>23.74 (n/a)</td><td>24.24 (n/a)</td><td>22.03 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>42.56 (+4.14%)</td><td>41.84 (+4.57%)</td><td>41.89 (+5.08%)</td><td>40.70 (+3.34%)</td><td>0.77 <b>(+21.48%)</b></td><td>42.53 (+4.14%)</td><td>41.81 (+4.57%)</td><td>41.86 (+5.08%)</td><td>40.68 (+3.34%)</td><td>0.77 <b>(+21.48%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>40.86 (n/a)</td><td>40.01 (n/a)</td><td>39.86 (n/a)</td><td>39.39 (n/a)</td><td>0.64 (n/a)</td><td>40.84 (n/a)</td><td>39.98 (n/a)</td><td>39.84 (n/a)</td><td>39.36 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>46.13 (+6.99%)</td><td>43.15 (+1.92%)</td><td>45.49 (+7.53%)</td><td>34.43 (-17.86%)</td><td>4.97 <b>(+941.35%)</b></td><td>46.10 (+6.99%)</td><td>43.12 (+1.92%)</td><td>45.46 (+7.53%)</td><td>34.41 (-17.86%)</td><td>4.97 <b>(+941.35%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>43.12 (n/a)</td><td>42.34 (n/a)</td><td>42.30 (n/a)</td><td>41.92 (n/a)</td><td>0.48 (n/a)</td><td>43.09 (n/a)</td><td>42.31 (n/a)</td><td>42.28 (n/a)</td><td>41.89 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.48 (n/a)</td><td>12.92 (n/a)</td><td>13.33 (n/a)</td><td>11.57 (n/a)</td><td>0.81 (n/a)</td><td>13.47 (n/a)</td><td>12.91 (n/a)</td><td>13.32 (n/a)</td><td>11.56 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>25.22 (+4.17%)</td><td>24.88 (+3.95%)</td><td>24.99 (+4.59%)</td><td>24.45 (+3.57%)</td><td>0.29 (+12.63%)</td><td>25.20 (+4.17%)</td><td>24.86 (+3.95%)</td><td>24.97 (+4.59%)</td><td>24.44 (+3.57%)</td><td>0.29 (+12.63%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>24.21 (n/a)</td><td>23.93 (n/a)</td><td>23.89 (n/a)</td><td>23.61 (n/a)</td><td>0.26 (n/a)</td><td>24.19 (n/a)</td><td>23.92 (n/a)</td><td>23.88 (n/a)</td><td>23.60 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>43.15 (+7.11%)</td><td>41.60 (+14.47%)</td><td>41.67 (+5.49%)</td><td>40.09 <b>(+73.83%)</b></td><td>1.22 <b>(-83.60%)</b></td><td>43.12 (+7.11%)</td><td>41.58 (+14.47%)</td><td>41.64 (+5.49%)</td><td>40.07 <b>(+73.83%)</b></td><td>1.22 <b>(-83.60%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>40.28 (n/a)</td><td>36.34 (n/a)</td><td>39.50 (n/a)</td><td>23.07 (n/a)</td><td>7.44 (n/a)</td><td>40.26 (n/a)</td><td>36.32 (n/a)</td><td>39.48 (n/a)</td><td>23.05 (n/a)</td><td>7.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>48.36 (+9.73%)</td><td>45.51 (+17.85%)</td><td>45.23 (+7.92%)</td><td>43.80 <b>(+85.43%)</b></td><td>1.84 <b>(-78.24%)</b></td><td>48.33 (+9.73%)</td><td>45.48 (+17.85%)</td><td>45.20 (+7.92%)</td><td>43.77 <b>(+85.43%)</b></td><td>1.84 <b>(-78.24%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>44.08 (n/a)</td><td>38.62 (n/a)</td><td>41.91 (n/a)</td><td>23.62 (n/a)</td><td>8.45 (n/a)</td><td>44.05 (n/a)</td><td>38.60 (n/a)</td><td>41.89 (n/a)</td><td>23.61 (n/a)</td><td>8.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.36 (-4.16%)</td><td>8.90 (-0.97%)</td><td>9.01 (-1.89%)</td><td>8.09 (+1.16%)</td><td>0.53 (-19.46%)</td><td>9.34 (-4.16%)</td><td>8.88 (-0.97%)</td><td>8.99 (-1.89%)</td><td>8.07 (+1.16%)</td><td>0.53 (-19.46%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>9.77 (n/a)</td><td>8.98 (n/a)</td><td>9.19 (n/a)</td><td>8.00 (n/a)</td><td>0.66 (n/a)</td><td>9.75 (n/a)</td><td>8.97 (n/a)</td><td>9.17 (n/a)</td><td>7.98 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.09 (+4.37%)</td><td>0.93 (+1.57%)</td><td>0.95 (+7.47%)</td><td>0.70 (-18.25%)</td><td>0.16 <b>(+93.60%)</b></td><td>1.07 (+4.37%)</td><td>0.92 (+1.57%)</td><td>0.93 (+7.47%)</td><td>0.68 (-18.25%)</td><td>0.16 <b>(+93.60%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.04 (n/a)</td><td>0.92 (n/a)</td><td>0.88 (n/a)</td><td>0.85 (n/a)</td><td>0.08 (n/a)</td><td>1.02 (n/a)</td><td>0.90 (n/a)</td><td>0.87 (n/a)</td><td>0.84 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.53 (+15.47%)</td><td>1.25 (+2.13%)</td><td>1.13 (-8.26%)</td><td>1.05 (-2.97%)</td><td>0.22 <b>(+136.20%)</b></td><td>1.51 (+15.47%)</td><td>1.23 (+2.13%)</td><td>1.11 (-8.26%)</td><td>1.03 (-2.97%)</td><td>0.22 <b>(+136.20%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.33 (n/a)</td><td>1.22 (n/a)</td><td>1.23 (n/a)</td><td>1.08 (n/a)</td><td>0.09 (n/a)</td><td>1.31 (n/a)</td><td>1.21 (n/a)</td><td>1.21 (n/a)</td><td>1.07 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>18.02 (-1.76%)</td><td>16.51 (-0.63%)</td><td>17.33 (+7.11%)</td><td>12.78 <b>(-20.02%)</b></td><td>2.14 <b>(+117.43%)</b></td><td>17.81 (-1.76%)</td><td>16.32 (-0.63%)</td><td>17.13 (+7.11%)</td><td>12.63 <b>(-20.02%)</b></td><td>2.12 <b>(+117.43%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>18.34 (n/a)</td><td>16.61 (n/a)</td><td>16.18 (n/a)</td><td>15.98 (n/a)</td><td>0.98 (n/a)</td><td>18.13 (n/a)</td><td>16.42 (n/a)</td><td>16.00 (n/a)</td><td>15.80 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.85 (-3.39%)</td><td>12.28 (-9.96%)</td><td>13.52 (+1.09%)</td><td>7.50 <b>(-42.64%)</b></td><td>2.70 <b>(+376.67%)</b></td><td>13.61 (-3.39%)</td><td>12.06 (-9.96%)</td><td>13.28 (+1.09%)</td><td>7.37 <b>(-42.64%)</b></td><td>2.65 <b>(+376.67%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>14.34 (n/a)</td><td>13.63 (n/a)</td><td>13.37 (n/a)</td><td>13.07 (n/a)</td><td>0.57 (n/a)</td><td>14.09 (n/a)</td><td>13.39 (n/a)</td><td>13.14 (n/a)</td><td>12.84 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>8.61 (-10.92%)</td><td>7.80 (-3.67%)</td><td>7.59 (-6.06%)</td><td>7.54 (+12.35%)</td><td>0.46 <b>(-62.77%)</b></td><td>8.46 (-10.92%)</td><td>7.67 (-3.67%)</td><td>7.46 (-6.06%)</td><td>7.41 (+12.35%)</td><td>0.45 <b>(-62.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>9.67 (n/a)</td><td>8.10 (n/a)</td><td>8.08 (n/a)</td><td>6.71 (n/a)</td><td>1.22 (n/a)</td><td>9.50 (n/a)</td><td>7.96 (n/a)</td><td>7.94 (n/a)</td><td>6.60 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>6.51 (+0.69%)</td><td>5.58 (-0.46%)</td><td>5.34 (-2.30%)</td><td>4.67 (-2.55%)</td><td>0.74 (+13.63%)</td><td>6.40 (+0.69%)</td><td>5.49 (-0.46%)</td><td>5.26 (-2.30%)</td><td>4.60 (-2.55%)</td><td>0.72 (+13.63%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>6.46 (n/a)</td><td>5.60 (n/a)</td><td>5.47 (n/a)</td><td>4.80 (n/a)</td><td>0.65 (n/a)</td><td>6.36 (n/a)</td><td>5.51 (n/a)</td><td>5.38 (n/a)</td><td>4.72 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.29 (n/a)</td><td>12.04 (n/a)</td><td>12.28 (n/a)</td><td>10.78 (n/a)</td><td>1.02 (n/a)</td><td>13.28 (n/a)</td><td>12.03 (n/a)</td><td>12.27 (n/a)</td><td>10.77 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.34 (n/a)</td><td>12.18 (n/a)</td><td>11.99 (n/a)</td><td>11.15 (n/a)</td><td>1.07 (n/a)</td><td>13.33 (n/a)</td><td>12.18 (n/a)</td><td>11.98 (n/a)</td><td>11.14 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.00 (n/a)</td><td>166.66 (n/a)</td><td>167.50 (n/a)</td><td>129.50 (n/a)</td><td>23.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>162.64 (n/a)</td><td>163.10 (n/a)</td><td>120.60 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.10 (n/a)</td><td>148.34 (n/a)</td><td>143.20 (n/a)</td><td>120.70 (n/a)</td><td>28.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.30 (n/a)</td><td>192.82 (n/a)</td><td>189.80 (n/a)</td><td>181.20 (n/a)</td><td>11.66 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>165.94 (n/a)</td><td>168.70 (n/a)</td><td>103.20 (n/a)</td><td>40.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.10 (n/a)</td><td>198.20 (n/a)</td><td>195.60 (n/a)</td><td>175.20 (n/a)</td><td>17.57 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.60 (n/a)</td><td>188.00 (n/a)</td><td>186.30 (n/a)</td><td>167.50 (n/a)</td><td>20.15 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.30 (n/a)</td><td>211.58 (n/a)</td><td>212.70 (n/a)</td><td>190.30 (n/a)</td><td>20.17 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.20 (n/a)</td><td>159.00 (n/a)</td><td>164.30 (n/a)</td><td>137.40 (n/a)</td><td>14.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>177.70 (n/a)</td><td>153.90 (n/a)</td><td>141.40 (n/a)</td><td>42.80 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>159.02 (n/a)</td><td>157.70 (n/a)</td><td>128.90 (n/a)</td><td>22.55 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>168.56 (n/a)</td><td>184.10 (n/a)</td><td>117.30 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>190.14 (n/a)</td><td>191.90 (n/a)</td><td>136.30 (n/a)</td><td>36.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>179.64 (n/a)</td><td>175.20 (n/a)</td><td>149.10 (n/a)</td><td>24.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>171.78 (n/a)</td><td>167.70 (n/a)</td><td>123.90 (n/a)</td><td>42.99 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>243.10 (n/a)</td><td>213.44 (n/a)</td><td>219.20 (n/a)</td><td>176.00 (n/a)</td><td>24.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>184.68 (n/a)</td><td>187.30 (n/a)</td><td>153.50 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.10 (n/a)</td><td>194.90 (n/a)</td><td>191.20 (n/a)</td><td>163.30 (n/a)</td><td>23.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>169.88 (n/a)</td><td>174.50 (n/a)</td><td>154.60 (n/a)</td><td>12.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>172.64 (n/a)</td><td>165.00 (n/a)</td><td>139.80 (n/a)</td><td>25.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.00 (n/a)</td><td>172.66 (n/a)</td><td>168.10 (n/a)</td><td>134.30 (n/a)</td><td>29.87 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>178.70 (n/a)</td><td>173.30 (n/a)</td><td>156.90 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>219.80 (n/a)</td><td>170.58 (n/a)</td><td>184.80 (n/a)</td><td>102.40 (n/a)</td><td>48.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>231.50 (n/a)</td><td>220.82 (n/a)</td><td>222.50 (n/a)</td><td>207.80 (n/a)</td><td>9.39 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>374.60 (n/a)</td><td>191.40 (n/a)</td><td>146.10 (n/a)</td><td>132.00 (n/a)</td><td>103.50 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>226.10 (n/a)</td><td>164.52 (n/a)</td><td>152.80 (n/a)</td><td>108.90 (n/a)</td><td>44.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>285.00 (n/a)</td><td>185.16 (n/a)</td><td>162.70 (n/a)</td><td>148.90 (n/a)</td><td>57.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.20 (n/a)</td><td>163.58 (n/a)</td><td>157.40 (n/a)</td><td>145.10 (n/a)</td><td>17.22 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>208.40 (n/a)</td><td>173.50 (n/a)</td><td>180.10 (n/a)</td><td>136.60 (n/a)</td><td>27.69 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>189.80 (n/a)</td><td>154.94 (n/a)</td><td>151.60 (n/a)</td><td>120.70 (n/a)</td><td>28.19 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>180.10 (n/a)</td><td>159.48 (n/a)</td><td>152.50 (n/a)</td><td>143.50 (n/a)</td><td>15.48 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>272.00 (n/a)</td><td>211.50 (n/a)</td><td>200.20 (n/a)</td><td>186.00 (n/a)</td><td>35.23 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-6.00%)</td><td>0.02 (-17.41%)</td><td>0.02 <b>(-26.32%)</b></td><td>0.02 <b>(-20.04%)</b></td><td>0.00 (+4.31%)</td><td>217.90 <b>(+25.01%)</b></td><td>176.76 <b>(+21.95%)</b></td><td>178.00 <b>(+35.67%)</b></td><td>134.30 (+6.42%)</td><td>30.63 <b>(+37.26%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.30 (n/a)</td><td>144.94 (n/a)</td><td>131.20 (n/a)</td><td>126.20 (n/a)</td><td>22.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-1.72%)</td><td>0.02 (-9.44%)</td><td>0.02 (-14.55%)</td><td>0.02 (-6.92%)</td><td>0.00 (+13.87%)</td><td>214.50 (+7.46%)</td><td>179.36 (+11.07%)</td><td>184.80 (+17.04%)</td><td>137.80 (+1.77%)</td><td>28.44 (+19.86%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.60 (n/a)</td><td>161.48 (n/a)</td><td>157.90 (n/a)</td><td>135.40 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-16.98%)</td><td>0.02 (-5.40%)</td><td>0.02 (-2.23%)</td><td>0.02 <b>(+58.08%)</b></td><td>0.00 <b>(-61.26%)</b></td><td>206.60 <b>(-36.74%)</b></td><td>174.28 (-6.25%)</td><td>175.30 (+2.28%)</td><td>137.90 <b>(+20.54%)</b></td><td>24.60 <b>(-71.06%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>326.60 (n/a)</td><td>185.90 (n/a)</td><td>171.40 (n/a)</td><td>114.40 (n/a)</td><td>84.99 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-2.30%)</td><td>0.03 (-2.63%)</td><td>0.03 (-0.90%)</td><td>0.02 (-16.82%)</td><td>0.01 (+15.13%)</td><td>239.30 <b>(+20.25%)</b></td><td>166.20 (+4.61%)</td><td>156.40 (+0.90%)</td><td>132.10 (+2.40%)</td><td>43.95 <b>(+43.97%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.00 (n/a)</td><td>158.88 (n/a)</td><td>155.00 (n/a)</td><td>129.00 (n/a)</td><td>30.53 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (+17.77%)</td><td>0.03 (-3.94%)</td><td>0.02 (-9.24%)</td><td>0.02 (-4.59%)</td><td>0.01 <b>(+52.55%)</b></td><td>216.60 (+4.84%)</td><td>165.04 (+6.74%)</td><td>164.50 (+10.18%)</td><td>107.50 (-15.09%)</td><td>39.67 <b>(+27.78%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.60 (n/a)</td><td>154.62 (n/a)</td><td>149.30 (n/a)</td><td>126.60 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-11.34%)</td><td>0.02 (+2.81%)</td><td>0.02 (+0.57%)</td><td>0.02 <b>(+41.32%)</b></td><td>0.00 <b>(-44.16%)</b></td><td>211.00 <b>(-29.24%)</b></td><td>180.32 (-8.00%)</td><td>178.30 (-0.56%)</td><td>146.70 (+12.85%)</td><td>28.04 <b>(-55.97%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>298.20 (n/a)</td><td>196.00 (n/a)</td><td>179.30 (n/a)</td><td>130.00 (n/a)</td><td>63.69 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-13.32%)</td><td>0.02 (-18.55%)</td><td>0.02 <b>(-24.49%)</b></td><td>0.01 <b>(-37.93%)</b></td><td>0.01 <b>(+53.47%)</b></td><td>311.10 <b>(+61.11%)</b></td><td>208.46 <b>(+29.64%)</b></td><td>203.90 <b>(+32.40%)</b></td><td>150.80 (+15.38%)</td><td>65.98 <b>(+171.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.10 (n/a)</td><td>160.80 (n/a)</td><td>154.00 (n/a)</td><td>130.70 (n/a)</td><td>24.32 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (+1.18%)</td><td>0.02 (-1.75%)</td><td>0.02 (-6.25%)</td><td>0.01 (+1.67%)</td><td>0.00 (-6.48%)</td><td>332.60 (-1.63%)</td><td>222.90 (+0.92%)</td><td>201.00 (+6.69%)</td><td>164.00 (-1.15%)</td><td>65.46 (-6.96%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>338.10 (n/a)</td><td>220.86 (n/a)</td><td>188.40 (n/a)</td><td>165.90 (n/a)</td><td>70.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (-10.11%)</td><td>0.05 (-3.69%)</td><td>0.05 (+4.02%)</td><td>0.04 (+0.51%)</td><td>0.01 <b>(-22.52%)</b></td><td>191.90 (-0.47%)</td><td>156.40 (+2.36%)</td><td>156.60 (-3.87%)</td><td>117.20 (+11.30%)</td><td>29.96 (-12.72%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>152.80 (n/a)</td><td>162.90 (n/a)</td><td>105.30 (n/a)</td><td>34.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (-15.93%)</td><td>0.05 (-5.91%)</td><td>0.05 (-2.83%)</td><td>0.05 (+14.38%)</td><td>0.00 <b>(-62.26%)</b></td><td>176.00 (-12.61%)</td><td>160.44 (+3.14%)</td><td>159.10 (+2.91%)</td><td>141.30 (+18.94%)</td><td>12.87 <b>(-60.82%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>155.56 (n/a)</td><td>154.60 (n/a)</td><td>118.80 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (+3.93%)</td><td>0.05 (+13.14%)</td><td>0.05 <b>(+20.72%)</b></td><td>0.05 <b>(+28.59%)</b></td><td>0.01 <b>(-45.27%)</b></td><td>179.90 <b>(-22.26%)</b></td><td>158.32 (-13.86%)</td><td>157.90 (-17.16%)</td><td>138.10 (-3.76%)</td><td>15.68 <b>(-57.92%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>183.80 (n/a)</td><td>190.60 (n/a)</td><td>143.50 (n/a)</td><td>37.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 <b>(-36.71%)</b></td><td>0.04 (-19.22%)</td><td>0.04 (-18.09%)</td><td>0.04 (-8.54%)</td><td>0.00 <b>(-71.74%)</b></td><td>210.00 (+9.38%)</td><td>191.02 (+19.27%)</td><td>193.70 <b>(+22.05%)</b></td><td>168.30 <b>(+58.03%)</b></td><td>16.80 <b>(-50.19%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>160.16 (n/a)</td><td>158.70 (n/a)</td><td>106.50 (n/a)</td><td>33.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (+4.32%)</td><td>0.05 (-9.48%)</td><td>0.05 <b>(-20.29%)</b></td><td>0.04 (-16.05%)</td><td>0.01 <b>(+32.70%)</b></td><td>225.50 (+19.12%)</td><td>176.38 (+13.46%)</td><td>181.30 <b>(+25.47%)</b></td><td>113.50 (-4.14%)</td><td>43.54 <b>(+44.45%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>155.46 (n/a)</td><td>144.50 (n/a)</td><td>118.40 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 <b>(-21.10%)</b></td><td>0.04 <b>(-22.52%)</b></td><td>0.04 <b>(-23.60%)</b></td><td>0.04 (-8.23%)</td><td>0.01 <b>(-39.27%)</b></td><td>227.20 (+8.97%)</td><td>198.20 <b>(+26.79%)</b></td><td>196.30 <b>(+30.95%)</b></td><td>153.50 <b>(+26.75%)</b></td><td>28.58 (-17.38%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>156.32 (n/a)</td><td>149.90 (n/a)</td><td>121.10 (n/a)</td><td>34.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (+12.45%)</td><td>0.05 (-6.25%)</td><td>0.05 (-9.29%)</td><td>0.04 (-12.11%)</td><td>0.01 <b>(+59.37%)</b></td><td>208.60 (+13.80%)</td><td>166.74 (+8.88%)</td><td>171.80 (+10.20%)</td><td>119.00 (-11.06%)</td><td>32.71 <b>(+60.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.30 (n/a)</td><td>153.14 (n/a)</td><td>155.90 (n/a)</td><td>133.80 (n/a)</td><td>20.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 <b>(+29.26%)</b></td><td>0.05 (+10.63%)</td><td>0.05 (+6.52%)</td><td>0.04 (+9.23%)</td><td>0.01 <b>(+88.25%)</b></td><td>192.80 (-8.45%)</td><td>164.14 (-8.33%)</td><td>169.60 (-6.09%)</td><td>122.60 <b>(-22.65%)</b></td><td>26.51 <b>(+29.96%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>179.06 (n/a)</td><td>180.60 (n/a)</td><td>158.50 (n/a)</td><td>20.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 <b>(+27.56%)</b></td><td>0.06 <b>(+24.62%)</b></td><td>0.06 <b>(+21.80%)</b></td><td>0.05 <b>(+22.86%)</b></td><td>0.01 <b>(+31.81%)</b></td><td>179.60 (-18.62%)</td><td>147.10 (-19.64%)</td><td>146.60 (-17.92%)</td><td>119.20 <b>(-21.63%)</b></td><td>22.07 (-16.14%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>183.06 (n/a)</td><td>178.60 (n/a)</td><td>152.10 (n/a)</td><td>26.32 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (-6.79%)</td><td>0.04 (-5.40%)</td><td>0.04 (-7.60%)</td><td>0.03 (-5.26%)</td><td>0.00 (-17.42%)</td><td>240.40 (+5.58%)</td><td>219.24 (+5.53%)</td><td>222.40 (+8.22%)</td><td>192.40 (+7.25%)</td><td>17.26 (-7.05%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>227.70 (n/a)</td><td>207.76 (n/a)</td><td>205.50 (n/a)</td><td>179.40 (n/a)</td><td>18.57 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (+6.11%)</td><td>0.10 (+0.55%)</td><td>0.10 (+1.32%)</td><td>0.08 (-14.37%)</td><td>0.02 <b>(+69.42%)</b></td><td>210.70 (+16.80%)</td><td>161.70 (+1.84%)</td><td>160.70 (-1.29%)</td><td>123.90 (-5.78%)</td><td>34.10 <b>(+88.54%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>158.78 (n/a)</td><td>162.80 (n/a)</td><td>131.50 (n/a)</td><td>18.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (-8.99%)</td><td>0.09 (-6.63%)</td><td>0.09 (-17.98%)</td><td>0.06 (+8.49%)</td><td>0.02 <b>(-24.25%)</b></td><td>277.00 (-7.82%)</td><td>184.76 (+3.10%)</td><td>174.40 <b>(+21.96%)</b></td><td>140.60 (+9.84%)</td><td>54.09 <b>(-23.43%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>300.50 (n/a)</td><td>179.20 (n/a)</td><td>143.00 (n/a)</td><td>128.00 (n/a)</td><td>70.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (-9.95%)</td><td>0.09 (-10.44%)</td><td>0.11 (-2.09%)</td><td>0.06 <b>(-32.55%)</b></td><td>0.02 <b>(+45.76%)</b></td><td>275.80 <b>(+48.20%)</b></td><td>186.38 (+16.75%)</td><td>155.60 (+2.10%)</td><td>141.10 (+11.01%)</td><td>56.97 <b>(+134.11%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.10 (n/a)</td><td>159.64 (n/a)</td><td>152.40 (n/a)</td><td>127.10 (n/a)</td><td>24.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (+4.14%)</td><td>0.10 (-7.90%)</td><td>0.09 (-13.38%)</td><td>0.08 (+0.02%)</td><td>0.02 (+14.77%)</td><td>201.10 (+0.00%)</td><td>176.12 (+9.21%)</td><td>185.20 (+15.46%)</td><td>124.50 (-3.94%)</td><td>30.45 (+7.64%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.10 (n/a)</td><td>161.26 (n/a)</td><td>160.40 (n/a)</td><td>129.60 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (-15.51%)</td><td>0.10 (-10.45%)</td><td>0.10 (-8.94%)</td><td>0.08 (-4.91%)</td><td>0.02 <b>(-31.68%)</b></td><td>203.60 (+5.17%)</td><td>164.62 (+9.98%)</td><td>164.80 (+9.79%)</td><td>128.20 (+18.37%)</td><td>26.88 (-14.78%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.60 (n/a)</td><td>149.68 (n/a)</td><td>150.10 (n/a)</td><td>108.30 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (-14.21%)</td><td>0.09 (-1.74%)</td><td>0.09 (+2.33%)</td><td>0.07 (-9.21%)</td><td>0.01 <b>(-20.20%)</b></td><td>237.10 (+10.13%)</td><td>184.08 (+1.47%)</td><td>177.40 (-2.31%)</td><td>160.90 (+16.51%)</td><td>30.51 (+8.14%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.30 (n/a)</td><td>181.42 (n/a)</td><td>181.60 (n/a)</td><td>138.10 (n/a)</td><td>28.22 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (-11.44%)</td><td>0.09 (-13.17%)</td><td>0.09 (-13.04%)</td><td>0.08 (-12.56%)</td><td>0.01 (-11.88%)</td><td>205.30 (+14.37%)</td><td>180.12 (+15.14%)</td><td>178.50 (+14.94%)</td><td>157.80 (+12.88%)</td><td>16.96 (+13.46%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>156.44 (n/a)</td><td>155.30 (n/a)</td><td>139.80 (n/a)</td><td>14.95 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (+19.84%)</td><td>0.08 (+1.70%)</td><td>0.08 (-5.08%)</td><td>0.06 (-13.07%)</td><td>0.01 <b>(+233.66%)</b></td><td>258.40 (+15.05%)</td><td>212.04 (+0.19%)</td><td>217.40 (+5.38%)</td><td>167.40 (-16.55%)</td><td>33.67 <b>(+216.08%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>224.60 (n/a)</td><td>211.64 (n/a)</td><td>206.30 (n/a)</td><td>200.60 (n/a)</td><td>10.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (-5.11%)</td><td>0.20 (-12.55%)</td><td>0.20 (-13.41%)</td><td>0.16 (-8.29%)</td><td>0.05 (+2.03%)</td><td>207.10 (+9.06%)</td><td>169.26 (+14.97%)</td><td>166.70 (+15.52%)</td><td>116.40 (+5.34%)</td><td>34.36 (+14.20%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>189.90 (n/a)</td><td>147.22 (n/a)</td><td>144.30 (n/a)</td><td>110.50 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (+6.73%)</td><td>0.18 (+7.81%)</td><td>0.20 (+19.44%)</td><td>0.09 <b>(-23.12%)</b></td><td>0.05 <b>(+57.73%)</b></td><td>366.70 <b>(+30.08%)</b></td><td>200.76 (-0.03%)</td><td>163.60 (-16.27%)</td><td>152.50 (-6.33%)</td><td>92.97 <b>(+94.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>281.90 (n/a)</td><td>200.82 (n/a)</td><td>195.40 (n/a)</td><td>162.80 (n/a)</td><td>47.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.23 (-8.74%)</td><td>0.20 (-0.55%)</td><td>0.19 (+1.34%)</td><td>0.17 (+7.80%)</td><td>0.03 <b>(-36.17%)</b></td><td>190.80 (-7.24%)</td><td>167.38 (-1.48%)</td><td>172.20 (-1.32%)</td><td>139.70 (+9.57%)</td><td>22.12 <b>(-35.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.70 (n/a)</td><td>169.90 (n/a)</td><td>174.50 (n/a)</td><td>127.50 (n/a)</td><td>34.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (+2.72%)</td><td>0.23 (+11.37%)</td><td>0.25 <b>(+26.13%)</b></td><td>0.17 (+0.23%)</td><td>0.04 (+12.29%)</td><td>193.00 (-0.21%)</td><td>146.82 (-9.65%)</td><td>133.30 <b>(-20.75%)</b></td><td>119.40 (-2.69%)</td><td>30.16 (+11.64%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>193.40 (n/a)</td><td>162.50 (n/a)</td><td>168.20 (n/a)</td><td>122.70 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 <b>(+46.93%)</b></td><td>0.21 <b>(+23.61%)</b></td><td>0.21 <b>(+21.54%)</b></td><td>0.15 (-5.69%)</td><td>0.05 <b>(+322.85%)</b></td><td>216.20 (+6.03%)</td><td>159.26 (-15.90%)</td><td>156.80 (-17.73%)</td><td>119.70 <b>(-31.95%)</b></td><td>37.70 <b>(+206.57%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>189.36 (n/a)</td><td>190.60 (n/a)</td><td>175.90 (n/a)</td><td>12.30 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (-0.48%)</td><td>0.21 (+0.35%)</td><td>0.21 (-2.27%)</td><td>0.18 (+11.94%)</td><td>0.03 <b>(-22.33%)</b></td><td>181.90 (-10.66%)</td><td>159.64 (-1.60%)</td><td>159.00 (+2.32%)</td><td>131.10 (+0.54%)</td><td>22.26 <b>(-28.60%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>203.60 (n/a)</td><td>162.24 (n/a)</td><td>155.40 (n/a)</td><td>130.40 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (+1.57%)</td><td>0.17 (+11.96%)</td><td>0.16 (+0.67%)</td><td>0.14 <b>(+48.93%)</b></td><td>0.02 <b>(-42.18%)</b></td><td>230.30 <b>(-32.84%)</b></td><td>200.52 (-15.01%)</td><td>205.40 (-0.68%)</td><td>166.30 (-1.54%)</td><td>26.55 <b>(-62.31%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>342.90 (n/a)</td><td>235.94 (n/a)</td><td>206.80 (n/a)</td><td>168.90 (n/a)</td><td>70.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (+7.88%)</td><td>0.03 (-4.43%)</td><td>0.03 (+0.70%)</td><td>0.02 (-6.31%)</td><td>0.01 <b>(+38.63%)</b></td><td>190.90 (+6.77%)</td><td>162.92 (+6.29%)</td><td>161.40 (-0.68%)</td><td>116.70 (-7.31%)</td><td>30.68 <b>(+40.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.80 (n/a)</td><td>153.28 (n/a)</td><td>162.50 (n/a)</td><td>125.90 (n/a)</td><td>21.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+11.07%)</td><td>0.03 (-7.20%)</td><td>0.02 (-13.80%)</td><td>0.02 (-9.24%)</td><td>0.00 <b>(+124.24%)</b></td><td>187.40 (+10.17%)</td><td>166.46 (+9.27%)</td><td>172.20 (+16.04%)</td><td>129.70 (-9.99%)</td><td>23.02 <b>(+118.87%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.10 (n/a)</td><td>152.34 (n/a)</td><td>148.40 (n/a)</td><td>144.10 (n/a)</td><td>10.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (-3.75%)</td><td>0.02 (-8.69%)</td><td>0.02 (-9.60%)</td><td>0.02 (-9.82%)</td><td>0.00 (+2.63%)</td><td>244.30 (+10.89%)</td><td>208.02 (+9.84%)</td><td>216.00 (+10.60%)</td><td>165.90 (+3.88%)</td><td>30.17 (+18.56%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.30 (n/a)</td><td>189.38 (n/a)</td><td>195.30 (n/a)</td><td>159.70 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-7.44%)</td><td>0.02 (+3.94%)</td><td>0.02 (+2.51%)</td><td>0.02 (+6.30%)</td><td>0.00 <b>(-36.79%)</b></td><td>236.80 (-5.92%)</td><td>186.94 (-6.35%)</td><td>183.10 (-2.45%)</td><td>159.20 (+8.01%)</td><td>30.00 <b>(-36.67%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>251.70 (n/a)</td><td>199.62 (n/a)</td><td>187.70 (n/a)</td><td>147.40 (n/a)</td><td>47.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+0.80%)</td><td>0.02 (-1.86%)</td><td>0.02 (-3.42%)</td><td>0.02 (-2.49%)</td><td>0.00 (+16.94%)</td><td>192.90 (+2.55%)</td><td>171.38 (+2.51%)</td><td>177.70 (+3.55%)</td><td>131.30 (-0.83%)</td><td>25.60 <b>(+23.30%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.10 (n/a)</td><td>167.18 (n/a)</td><td>171.60 (n/a)</td><td>132.40 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-3.36%)</td><td>0.03 (-7.96%)</td><td>0.03 (+0.62%)</td><td>0.02 <b>(-29.25%)</b></td><td>0.01 <b>(+65.39%)</b></td><td>234.90 <b>(+41.34%)</b></td><td>170.42 (+12.59%)</td><td>162.00 (-0.61%)</td><td>130.80 (+3.48%)</td><td>43.47 <b>(+132.80%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.20 (n/a)</td><td>151.36 (n/a)</td><td>163.00 (n/a)</td><td>126.40 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+15.61%)</td><td>0.02 (+2.75%)</td><td>0.02 (+3.34%)</td><td>0.02 (-10.87%)</td><td>0.01 <b>(+77.05%)</b></td><td>213.80 (+12.17%)</td><td>172.78 (-0.67%)</td><td>175.40 (-3.25%)</td><td>125.50 (-13.45%)</td><td>32.57 <b>(+66.27%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.60 (n/a)</td><td>173.94 (n/a)</td><td>181.30 (n/a)</td><td>145.00 (n/a)</td><td>19.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 <b>(-20.21%)</b></td><td>0.02 <b>(-23.02%)</b></td><td>0.02 <b>(-28.55%)</b></td><td>0.02 (-13.25%)</td><td>0.00 <b>(-22.79%)</b></td><td>227.10 (+15.28%)</td><td>191.80 <b>(+29.40%)</b></td><td>206.50 <b>(+40.00%)</b></td><td>152.60 <b>(+25.29%)</b></td><td>34.29 (+11.56%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>148.22 (n/a)</td><td>147.50 (n/a)</td><td>121.80 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 <b>(-35.93%)</b></td><td>0.02 <b>(-29.05%)</b></td><td>0.02 <b>(-31.68%)</b></td><td>0.01 <b>(-30.72%)</b></td><td>0.00 <b>(-47.84%)</b></td><td>296.40 <b>(+44.30%)</b></td><td>224.68 <b>(+38.95%)</b></td><td>217.30 <b>(+46.33%)</b></td><td>193.10 <b>(+56.10%)</b></td><td>41.55 (+17.54%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>161.70 (n/a)</td><td>148.50 (n/a)</td><td>123.70 (n/a)</td><td>35.35 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+11.30%)</td><td>0.02 (-0.17%)</td><td>0.03 (+1.46%)</td><td>0.02 (-10.62%)</td><td>0.00 <b>(+46.24%)</b></td><td>222.50 (+11.87%)</td><td>170.10 (+1.86%)</td><td>163.50 (-1.45%)</td><td>129.60 (-10.12%)</td><td>34.30 <b>(+50.55%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.90 (n/a)</td><td>167.00 (n/a)</td><td>165.90 (n/a)</td><td>144.20 (n/a)</td><td>22.78 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 (-14.11%)</td><td>0.02 (-10.49%)</td><td>0.02 (-19.11%)</td><td>0.02 (-4.33%)</td><td>0.00 <b>(-36.94%)</b></td><td>204.20 (+4.56%)</td><td>185.02 (+10.72%)</td><td>190.40 <b>(+23.64%)</b></td><td>165.00 (+16.36%)</td><td>18.23 <b>(-25.99%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.30 (n/a)</td><td>167.10 (n/a)</td><td>154.00 (n/a)</td><td>141.80 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+0.79%)</td><td>0.02 (-5.41%)</td><td>0.02 (-6.62%)</td><td>0.02 (-8.57%)</td><td>0.00 <b>(+28.46%)</b></td><td>213.50 (+9.38%)</td><td>181.84 (+6.49%)</td><td>183.40 (+7.06%)</td><td>142.70 (-0.76%)</td><td>25.36 <b>(+37.07%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.20 (n/a)</td><td>170.76 (n/a)</td><td>171.30 (n/a)</td><td>143.80 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 <b>(-20.46%)</b></td><td>0.02 (-15.23%)</td><td>0.02 (-14.49%)</td><td>0.01 (-17.82%)</td><td>0.00 <b>(-25.29%)</b></td><td>300.50 <b>(+21.71%)</b></td><td>226.92 (+17.33%)</td><td>230.80 (+16.92%)</td><td>161.50 <b>(+25.68%)</b></td><td>50.68 (+18.49%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.90 (n/a)</td><td>193.40 (n/a)</td><td>197.40 (n/a)</td><td>128.50 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-4.35%)</td><td>0.02 (-7.40%)</td><td>0.02 (-6.60%)</td><td>0.02 (+7.51%)</td><td>0.00 <b>(-27.24%)</b></td><td>207.80 (-6.98%)</td><td>181.76 (+6.68%)</td><td>180.30 (+7.07%)</td><td>149.30 (+4.55%)</td><td>22.21 <b>(-30.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>170.38 (n/a)</td><td>168.40 (n/a)</td><td>142.80 (n/a)</td><td>31.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+9.49%)</td><td>0.02 <b>(+22.59%)</b></td><td>0.03 <b>(+39.38%)</b></td><td>0.02 <b>(+28.62%)</b></td><td>0.00 <b>(-37.15%)</b></td><td>199.70 <b>(-22.27%)</b></td><td>167.06 <b>(-20.26%)</b></td><td>160.80 <b>(-28.25%)</b></td><td>148.70 (-8.72%)</td><td>19.29 <b>(-53.00%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.90 (n/a)</td><td>209.50 (n/a)</td><td>224.10 (n/a)</td><td>162.90 (n/a)</td><td>41.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-3.49%)</td><td>0.02 (-5.91%)</td><td>0.02 (+0.87%)</td><td>0.02 (-7.05%)</td><td>0.00 (-4.05%)</td><td>208.40 (+7.59%)</td><td>182.40 (+6.28%)</td><td>179.30 (-0.88%)</td><td>143.70 (+3.60%)</td><td>25.25 (+5.31%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.70 (n/a)</td><td>171.62 (n/a)</td><td>180.90 (n/a)</td><td>138.70 (n/a)</td><td>23.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (-6.09%)</td><td>0.05 (-13.44%)</td><td>0.05 (-3.06%)</td><td>0.03 (-14.10%)</td><td>0.01 (+12.21%)</td><td>234.20 (+16.40%)</td><td>184.58 (+17.75%)</td><td>165.20 (+3.12%)</td><td>134.00 (+6.52%)</td><td>45.24 <b>(+49.16%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>156.76 (n/a)</td><td>160.20 (n/a)</td><td>125.80 (n/a)</td><td>30.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (-12.00%)</td><td>0.05 (+0.32%)</td><td>0.05 (+0.14%)</td><td>0.04 (+18.48%)</td><td>0.01 <b>(-44.20%)</b></td><td>193.20 (-15.60%)</td><td>161.90 (-2.87%)</td><td>159.90 (-0.12%)</td><td>143.40 (+13.63%)</td><td>19.68 <b>(-48.00%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.90 (n/a)</td><td>166.68 (n/a)</td><td>160.10 (n/a)</td><td>126.20 (n/a)</td><td>37.85 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (+15.61%)</td><td>0.04 (-3.96%)</td><td>0.04 (-4.43%)</td><td>0.03 (-5.31%)</td><td>0.01 <b>(+59.94%)</b></td><td>236.20 (+5.59%)</td><td>209.20 (+5.83%)</td><td>219.30 (+4.68%)</td><td>148.30 (-13.48%)</td><td>35.05 <b>(+44.82%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>197.68 (n/a)</td><td>209.50 (n/a)</td><td>171.40 (n/a)</td><td>24.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (-11.92%)</td><td>0.04 (-10.80%)</td><td>0.04 (-2.63%)</td><td>0.03 (-18.17%)</td><td>0.01 (+11.32%)</td><td>279.50 <b>(+22.21%)</b></td><td>213.66 (+13.94%)</td><td>197.90 (+2.70%)</td><td>168.40 (+13.48%)</td><td>48.49 <b>(+54.60%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>187.52 (n/a)</td><td>192.70 (n/a)</td><td>148.40 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (-17.47%)</td><td>0.04 (-17.29%)</td><td>0.04 (-13.63%)</td><td>0.03 <b>(-32.22%)</b></td><td>0.01 (-7.98%)</td><td>301.70 <b>(+47.53%)</b></td><td>205.06 <b>(+23.44%)</b></td><td>200.10 (+15.80%)</td><td>141.00 <b>(+21.13%)</b></td><td>60.38 <b>(+67.84%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>166.12 (n/a)</td><td>172.80 (n/a)</td><td>116.40 (n/a)</td><td>35.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (+8.98%)</td><td>0.05 (+7.95%)</td><td>0.05 (+13.55%)</td><td>0.03 (-18.15%)</td><td>0.01 <b>(+67.69%)</b></td><td>249.50 <b>(+22.18%)</b></td><td>170.92 (-4.33%)</td><td>162.80 (-11.95%)</td><td>133.30 (-8.26%)</td><td>45.80 <b>(+97.26%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>178.66 (n/a)</td><td>184.90 (n/a)</td><td>145.30 (n/a)</td><td>23.22 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 <b>(+43.76%)</b></td><td>0.05 (+10.98%)</td><td>0.05 <b>(+21.72%)</b></td><td>0.03 <b>(-29.60%)</b></td><td>0.02 <b>(+212.37%)</b></td><td>326.90 <b>(+42.07%)</b></td><td>197.06 (+0.45%)</td><td>167.00 (-17.86%)</td><td>114.00 <b>(-30.45%)</b></td><td>81.37 <b>(+219.82%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>196.18 (n/a)</td><td>203.30 (n/a)</td><td>163.90 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (+10.82%)</td><td>0.06 (+16.01%)</td><td>0.06 <b>(+23.43%)</b></td><td>0.04 (+19.97%)</td><td>0.01 (+12.08%)</td><td>189.60 (-16.66%)</td><td>153.94 (-13.81%)</td><td>139.80 (-18.96%)</td><td>117.60 (-9.75%)</td><td>33.45 (-11.70%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>178.60 (n/a)</td><td>172.50 (n/a)</td><td>130.30 (n/a)</td><td>37.88 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (-9.69%)</td><td>0.05 (-5.36%)</td><td>0.05 (-0.12%)</td><td>0.04 (-12.17%)</td><td>0.01 (-3.80%)</td><td>210.00 (+13.82%)</td><td>176.68 (+5.99%)</td><td>171.40 (+0.12%)</td><td>143.80 (+10.70%)</td><td>26.86 <b>(+25.87%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>166.70 (n/a)</td><td>171.20 (n/a)</td><td>129.90 (n/a)</td><td>21.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (+9.61%)</td><td>0.05 (+3.47%)</td><td>0.05 (+1.00%)</td><td>0.04 (-6.46%)</td><td>0.01 <b>(+78.92%)</b></td><td>195.40 (+6.89%)</td><td>161.88 (-2.03%)</td><td>169.90 (-0.99%)</td><td>135.20 (-8.77%)</td><td>25.66 <b>(+71.42%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>182.80 (n/a)</td><td>165.24 (n/a)</td><td>171.60 (n/a)</td><td>148.20 (n/a)</td><td>14.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 <b>(+23.79%)</b></td><td>0.05 (+13.86%)</td><td>0.04 (+0.96%)</td><td>0.04 (+15.64%)</td><td>0.01 <b>(+26.03%)</b></td><td>205.20 (-13.53%)</td><td>176.88 (-12.10%)</td><td>184.00 (-0.97%)</td><td>136.00 (-19.24%)</td><td>26.07 (-16.19%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>201.22 (n/a)</td><td>185.80 (n/a)</td><td>168.40 (n/a)</td><td>31.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (-5.71%)</td><td>0.05 (-6.83%)</td><td>0.04 (-11.13%)</td><td>0.04 (+3.31%)</td><td>0.01 (-13.79%)</td><td>225.20 (-3.22%)</td><td>185.12 (+6.33%)</td><td>194.60 (+12.49%)</td><td>138.40 (+6.05%)</td><td>34.07 (-12.74%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.70 (n/a)</td><td>174.10 (n/a)</td><td>173.00 (n/a)</td><td>130.50 (n/a)</td><td>39.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (-2.72%)</td><td>0.05 (-6.00%)</td><td>0.05 (-0.75%)</td><td>0.03 (-18.52%)</td><td>0.01 <b>(+27.56%)</b></td><td>244.30 <b>(+22.70%)</b></td><td>184.04 (+8.21%)</td><td>175.90 (+0.74%)</td><td>149.50 (+2.82%)</td><td>39.22 <b>(+62.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.10 (n/a)</td><td>170.08 (n/a)</td><td>174.60 (n/a)</td><td>145.40 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (+2.22%)</td><td>0.04 (-12.64%)</td><td>0.04 <b>(-26.46%)</b></td><td>0.03 <b>(-22.72%)</b></td><td>0.01 <b>(+76.01%)</b></td><td>255.50 <b>(+29.37%)</b></td><td>195.34 (+19.61%)</td><td>218.40 <b>(+35.99%)</b></td><td>134.60 (-2.18%)</td><td>51.14 <b>(+117.02%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.50 (n/a)</td><td>163.32 (n/a)</td><td>160.60 (n/a)</td><td>137.60 (n/a)</td><td>23.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (+14.19%)</td><td>0.04 (-9.63%)</td><td>0.04 <b>(-22.76%)</b></td><td>0.04 (+3.32%)</td><td>0.01 <b>(+39.73%)</b></td><td>231.80 (-3.22%)</td><td>206.16 (+11.86%)</td><td>222.20 <b>(+29.49%)</b></td><td>145.30 (-12.42%)</td><td>35.32 (+13.61%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>184.30 (n/a)</td><td>171.60 (n/a)</td><td>165.90 (n/a)</td><td>31.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (+9.03%)</td><td>0.05 (-3.92%)</td><td>0.05 (-6.01%)</td><td>0.04 (-12.64%)</td><td>0.01 <b>(+107.25%)</b></td><td>204.90 (+14.47%)</td><td>175.36 (+5.40%)</td><td>179.30 (+6.41%)</td><td>138.40 (-8.28%)</td><td>23.93 <b>(+112.18%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>179.00 (n/a)</td><td>166.38 (n/a)</td><td>168.50 (n/a)</td><td>150.90 (n/a)</td><td>11.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 <b>(+24.34%)</b></td><td>0.10 (+17.45%)</td><td>0.09 (-6.18%)</td><td>0.06 <b>(+38.25%)</b></td><td>0.04 <b>(+35.10%)</b></td><td>279.70 <b>(-27.67%)</b></td><td>188.78 (-14.95%)</td><td>184.40 (+6.59%)</td><td>118.90 (-19.55%)</td><td>70.75 <b>(-27.45%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>386.70 (n/a)</td><td>221.96 (n/a)</td><td>173.00 (n/a)</td><td>147.80 (n/a)</td><td>97.53 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (+8.92%)</td><td>0.11 (+2.87%)</td><td>0.10 (+0.30%)</td><td>0.09 (+8.58%)</td><td>0.02 (+6.46%)</td><td>186.60 (-7.90%)</td><td>158.98 (-2.79%)</td><td>168.20 (-0.30%)</td><td>119.30 (-8.23%)</td><td>29.51 (-6.01%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.60 (n/a)</td><td>163.54 (n/a)</td><td>168.70 (n/a)</td><td>130.00 (n/a)</td><td>31.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (-11.92%)</td><td>0.07 (-17.51%)</td><td>0.07 <b>(-24.92%)</b></td><td>0.06 (-12.55%)</td><td>0.01 (-8.35%)</td><td>257.00 (+14.37%)</td><td>225.76 <b>(+21.35%)</b></td><td>237.40 <b>(+33.22%)</b></td><td>168.80 (+13.52%)</td><td>33.54 (+14.06%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>186.04 (n/a)</td><td>178.20 (n/a)</td><td>148.70 (n/a)</td><td>29.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.09 (-3.68%)</td><td>0.09 (-3.60%)</td><td>0.09 (-5.10%)</td><td>0.08 (+2.43%)</td><td>0.00 <b>(-40.76%)</b></td><td>198.60 (-2.36%)</td><td>185.54 (+3.47%)</td><td>183.50 (+5.40%)</td><td>178.20 (+3.85%)</td><td>8.10 <b>(-40.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>179.32 (n/a)</td><td>174.10 (n/a)</td><td>171.60 (n/a)</td><td>13.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (+1.98%)</td><td>0.10 (-11.71%)</td><td>0.10 (-10.26%)</td><td>0.05 <b>(-28.63%)</b></td><td>0.04 <b>(+67.84%)</b></td><td>314.90 <b>(+40.08%)</b></td><td>205.50 <b>(+29.33%)</b></td><td>161.80 (+11.43%)</td><td>116.60 (-2.02%)</td><td>98.76 <b>(+138.02%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.80 (n/a)</td><td>158.90 (n/a)</td><td>145.20 (n/a)</td><td>119.00 (n/a)</td><td>41.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 <b>(-23.07%)</b></td><td>0.09 (-14.02%)</td><td>0.09 (-10.64%)</td><td>0.07 (-16.99%)</td><td>0.01 <b>(-35.81%)</b></td><td>229.90 <b>(+20.43%)</b></td><td>183.12 (+15.27%)</td><td>173.80 (+11.91%)</td><td>159.30 <b>(+30.04%)</b></td><td>28.07 (+0.85%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.90 (n/a)</td><td>158.86 (n/a)</td><td>155.30 (n/a)</td><td>122.50 (n/a)</td><td>27.84 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 <b>(-24.67%)</b></td><td>0.11 (-9.68%)</td><td>0.11 (-11.74%)</td><td>0.09 (+1.99%)</td><td>0.01 <b>(-50.78%)</b></td><td>177.70 (-1.93%)</td><td>154.66 (+7.37%)</td><td>153.60 (+13.27%)</td><td>131.30 <b>(+32.76%)</b></td><td>20.93 <b>(-35.88%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>181.20 (n/a)</td><td>144.04 (n/a)</td><td>135.60 (n/a)</td><td>98.90 (n/a)</td><td>32.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 <b>(-23.51%)</b></td><td>0.09 <b>(-24.56%)</b></td><td>0.10 <b>(-25.75%)</b></td><td>0.07 (-16.94%)</td><td>0.01 <b>(-28.28%)</b></td><td>223.70 <b>(+20.40%)</b></td><td>182.46 <b>(+31.84%)</b></td><td>172.10 <b>(+34.66%)</b></td><td>156.90 <b>(+30.75%)</b></td><td>29.12 (+8.13%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.80 (n/a)</td><td>138.40 (n/a)</td><td>127.80 (n/a)</td><td>120.00 (n/a)</td><td>26.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (-17.02%)</td><td>0.09 <b>(-31.69%)</b></td><td>0.09 <b>(-30.94%)</b></td><td>0.06 <b>(-49.01%)</b></td><td>0.02 <b>(+68.75%)</b></td><td>291.20 <b>(+96.09%)</b></td><td>198.36 <b>(+53.62%)</b></td><td>190.80 <b>(+44.76%)</b></td><td>139.30 <b>(+20.50%)</b></td><td>56.40 <b>(+318.83%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>148.50 (n/a)</td><td>129.12 (n/a)</td><td>131.80 (n/a)</td><td>115.60 (n/a)</td><td>13.47 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (-3.34%)</td><td>0.09 (-19.07%)</td><td>0.09 <b>(-26.91%)</b></td><td>0.07 (-15.66%)</td><td>0.02 (+15.46%)</td><td>228.10 (+18.56%)</td><td>187.24 <b>(+24.99%)</b></td><td>187.60 <b>(+36.83%)</b></td><td>134.20 (+3.47%)</td><td>35.11 <b>(+36.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.40 (n/a)</td><td>149.80 (n/a)</td><td>137.10 (n/a)</td><td>129.70 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (+11.40%)</td><td>0.11 (+3.53%)</td><td>0.10 (+4.76%)</td><td>0.08 (-14.03%)</td><td>0.03 <b>(+53.93%)</b></td><td>211.00 (+16.32%)</td><td>159.94 (-0.66%)</td><td>163.80 (-4.55%)</td><td>111.80 (-10.20%)</td><td>38.46 <b>(+57.52%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>181.40 (n/a)</td><td>161.00 (n/a)</td><td>171.60 (n/a)</td><td>124.50 (n/a)</td><td>24.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (+2.38%)</td><td>0.10 (+7.85%)</td><td>0.08 (-8.20%)</td><td>0.07 (+3.38%)</td><td>0.03 <b>(+29.15%)</b></td><td>231.20 (-3.30%)</td><td>176.02 (-4.45%)</td><td>201.00 (+8.94%)</td><td>117.10 (-2.34%)</td><td>53.00 <b>(+21.18%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>239.10 (n/a)</td><td>184.22 (n/a)</td><td>184.50 (n/a)</td><td>119.90 (n/a)</td><td>43.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (+6.51%)</td><td>0.09 (-3.05%)</td><td>0.08 (-13.08%)</td><td>0.06 (-17.76%)</td><td>0.03 <b>(+43.22%)</b></td><td>283.30 <b>(+21.59%)</b></td><td>193.78 (+7.81%)</td><td>204.30 (+15.03%)</td><td>126.90 (-6.14%)</td><td>61.71 <b>(+60.06%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.00 (n/a)</td><td>179.74 (n/a)</td><td>177.60 (n/a)</td><td>135.20 (n/a)</td><td>38.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (-14.10%)</td><td>0.09 (+5.64%)</td><td>0.09 (+0.36%)</td><td>0.08 <b>(+86.14%)</b></td><td>0.01 <b>(-78.31%)</b></td><td>204.90 <b>(-46.29%)</b></td><td>183.90 (-15.63%)</td><td>180.50 (-0.39%)</td><td>169.80 (+16.38%)</td><td>12.92 <b>(-86.59%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>381.50 (n/a)</td><td>217.98 (n/a)</td><td>181.20 (n/a)</td><td>145.90 (n/a)</td><td>96.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 <b>(-31.22%)</b></td><td>0.08 <b>(-25.26%)</b></td><td>0.08 <b>(-22.17%)</b></td><td>0.08 (-16.85%)</td><td>0.01 <b>(-55.35%)</b></td><td>217.60 <b>(+20.29%)</b></td><td>196.54 <b>(+31.99%)</b></td><td>197.30 <b>(+28.45%)</b></td><td>169.00 <b>(+45.44%)</b></td><td>18.53 <b>(-21.46%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.90 (n/a)</td><td>148.90 (n/a)</td><td>153.60 (n/a)</td><td>116.20 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (-18.10%)</td><td>0.08 <b>(-26.83%)</b></td><td>0.08 <b>(-31.45%)</b></td><td>0.07 <b>(-24.81%)</b></td><td>0.02 (+0.61%)</td><td>232.10 <b>(+33.01%)</b></td><td>200.90 <b>(+38.09%)</b></td><td>202.40 <b>(+45.93%)</b></td><td>146.80 <b>(+22.13%)</b></td><td>34.24 <b>(+60.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>174.50 (n/a)</td><td>145.48 (n/a)</td><td>138.70 (n/a)</td><td>120.20 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 <b>(-25.50%)</b></td><td>0.18 <b>(-20.63%)</b></td><td>0.19 <b>(-25.41%)</b></td><td>0.17 (-1.38%)</td><td>0.01 <b>(-72.48%)</b></td><td>194.10 (+1.41%)</td><td>179.82 <b>(+23.11%)</b></td><td>176.60 <b>(+34.09%)</b></td><td>166.80 <b>(+34.30%)</b></td><td>10.56 <b>(-62.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>191.40 (n/a)</td><td>146.06 (n/a)</td><td>131.70 (n/a)</td><td>124.20 (n/a)</td><td>28.07 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (+1.70%)</td><td>0.20 (-12.24%)</td><td>0.19 <b>(-24.43%)</b></td><td>0.13 (-8.79%)</td><td>0.05 (-4.07%)</td><td>250.50 (+9.63%)</td><td>174.34 (+13.87%)</td><td>174.40 <b>(+32.32%)</b></td><td>117.60 (-1.67%)</td><td>48.55 (+5.64%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>228.50 (n/a)</td><td>153.10 (n/a)</td><td>131.80 (n/a)</td><td>119.60 (n/a)</td><td>45.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 <b>(+46.86%)</b></td><td>0.18 (+18.88%)</td><td>0.18 (+18.49%)</td><td>0.10 <b>(-22.19%)</b></td><td>0.06 <b>(+298.79%)</b></td><td>315.10 <b>(+28.51%)</b></td><td>202.78 (-7.36%)</td><td>183.90 (-15.60%)</td><td>133.00 <b>(-31.93%)</b></td><td>76.14 <b>(+241.56%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>245.20 (n/a)</td><td>218.88 (n/a)</td><td>217.90 (n/a)</td><td>195.40 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (-6.83%)</td><td>0.18 (-0.24%)</td><td>0.16 (-4.45%)</td><td>0.15 (-2.20%)</td><td>0.03 (-4.96%)</td><td>221.50 (+2.26%)</td><td>190.80 (+0.30%)</td><td>207.40 (+4.64%)</td><td>147.90 (+7.33%)</td><td>33.56 (+7.51%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.60 (n/a)</td><td>190.22 (n/a)</td><td>198.20 (n/a)</td><td>137.80 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 <b>(+28.25%)</b></td><td>0.20 (+10.19%)</td><td>0.19 (+1.99%)</td><td>0.13 <b>(+33.24%)</b></td><td>0.06 <b>(+23.48%)</b></td><td>244.60 <b>(-24.97%)</b></td><td>176.48 (-10.74%)</td><td>173.30 (-1.98%)</td><td>111.10 <b>(-22.04%)</b></td><td>47.71 <b>(-34.78%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>326.00 (n/a)</td><td>197.72 (n/a)</td><td>176.80 (n/a)</td><td>142.50 (n/a)</td><td>73.16 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (+2.32%)</td><td>0.22 (-11.86%)</td><td>0.23 (-9.19%)</td><td>0.16 <b>(-21.01%)</b></td><td>0.05 <b>(+71.01%)</b></td><td>198.80 <b>(+26.54%)</b></td><td>152.02 (+16.29%)</td><td>139.70 (+10.09%)</td><td>115.30 (-2.29%)</td><td>32.28 <b>(+109.84%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>157.10 (n/a)</td><td>130.72 (n/a)</td><td>126.90 (n/a)</td><td>118.00 (n/a)</td><td>15.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 <b>(-21.25%)</b></td><td>0.18 (-11.91%)</td><td>0.18 (-6.21%)</td><td>0.16 (+15.36%)</td><td>0.02 <b>(-63.09%)</b></td><td>210.40 (-13.31%)</td><td>187.86 (+8.40%)</td><td>186.00 (+6.65%)</td><td>165.40 <b>(+27.04%)</b></td><td>20.04 <b>(-57.12%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>242.70 (n/a)</td><td>173.30 (n/a)</td><td>174.40 (n/a)</td><td>130.20 (n/a)</td><td>46.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 <b>(-26.47%)</b></td><td>0.18 <b>(-20.81%)</b></td><td>0.17 <b>(-20.32%)</b></td><td>0.16 (-9.85%)</td><td>0.01 <b>(-59.90%)</b></td><td>200.40 (+10.90%)</td><td>183.58 <b>(+24.48%)</b></td><td>188.90 <b>(+25.51%)</b></td><td>167.40 <b>(+35.99%)</b></td><td>14.02 <b>(-39.35%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>180.70 (n/a)</td><td>147.48 (n/a)</td><td>150.50 (n/a)</td><td>123.10 (n/a)</td><td>23.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (-2.02%)</td><td>0.20 (+0.31%)</td><td>0.20 (-2.82%)</td><td>0.15 (-1.96%)</td><td>0.04 (+5.46%)</td><td>216.50 (+2.03%)</td><td>169.32 (+0.07%)</td><td>166.70 (+2.90%)</td><td>134.10 (+2.05%)</td><td>33.08 (+8.67%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.20 (n/a)</td><td>169.20 (n/a)</td><td>162.00 (n/a)</td><td>131.40 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (-9.34%)</td><td>0.20 (+1.57%)</td><td>0.19 (+11.42%)</td><td>0.17 (+9.73%)</td><td>0.03 <b>(-40.55%)</b></td><td>191.10 (-8.87%)</td><td>168.96 (-3.96%)</td><td>171.10 (-10.23%)</td><td>137.00 (+10.31%)</td><td>21.36 <b>(-40.74%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>209.70 (n/a)</td><td>175.92 (n/a)</td><td>190.60 (n/a)</td><td>124.20 (n/a)</td><td>36.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (-12.53%)</td><td>0.18 (+5.78%)</td><td>0.19 (+15.73%)</td><td>0.15 <b>(+50.01%)</b></td><td>0.02 <b>(-54.92%)</b></td><td>212.80 <b>(-33.33%)</b></td><td>188.32 (-10.67%)</td><td>176.10 (-13.59%)</td><td>169.10 (+14.33%)</td><td>22.45 <b>(-66.01%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>319.20 (n/a)</td><td>210.82 (n/a)</td><td>203.80 (n/a)</td><td>147.90 (n/a)</td><td>66.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (-5.34%)</td><td>0.20 (+1.15%)</td><td>0.20 (+1.15%)</td><td>0.19 (+7.27%)</td><td>0.01 <b>(-42.04%)</b></td><td>172.80 (-6.80%)</td><td>161.82 (-1.77%)</td><td>160.70 (-1.11%)</td><td>147.10 (+5.68%)</td><td>10.09 <b>(-42.84%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.40 (n/a)</td><td>164.74 (n/a)</td><td>162.50 (n/a)</td><td>139.20 (n/a)</td><td>17.66 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (-2.40%)</td><td>0.17 (+4.63%)</td><td>0.16 (+8.30%)</td><td>0.16 <b>(+42.40%)</b></td><td>0.02 <b>(-48.39%)</b></td><td>210.20 <b>(-29.77%)</b></td><td>197.52 (-8.52%)</td><td>205.50 (-7.64%)</td><td>159.40 (+2.51%)</td><td>21.41 <b>(-62.57%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>299.30 (n/a)</td><td>215.92 (n/a)</td><td>222.50 (n/a)</td><td>155.50 (n/a)</td><td>57.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (+17.67%)</td><td>0.19 (+2.26%)</td><td>0.18 (-1.70%)</td><td>0.14 (-5.22%)</td><td>0.04 <b>(+57.77%)</b></td><td>237.40 (+5.51%)</td><td>183.04 (-0.45%)</td><td>180.30 (+1.75%)</td><td>133.70 (-15.00%)</td><td>37.04 <b>(+39.17%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>225.00 (n/a)</td><td>183.86 (n/a)</td><td>177.20 (n/a)</td><td>157.30 (n/a)</td><td>26.61 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (-13.96%)</td><td>0.15 (-19.97%)</td><td>0.16 (-13.47%)</td><td>0.11 <b>(-36.60%)</b></td><td>0.03 <b>(+148.65%)</b></td><td>288.40 <b>(+57.77%)</b></td><td>224.54 <b>(+28.48%)</b></td><td>205.60 (+15.57%)</td><td>183.50 (+16.21%)</td><td>45.32 <b>(+358.63%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>182.80 (n/a)</td><td>174.76 (n/a)</td><td>177.90 (n/a)</td><td>157.90 (n/a)</td><td>9.88 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (+12.30%)</td><td>0.17 (+2.33%)</td><td>0.16 (-7.58%)</td><td>0.13 (-9.28%)</td><td>0.03 <b>(+97.76%)</b></td><td>244.40 (+10.19%)</td><td>194.10 (+0.00%)</td><td>201.60 (+8.21%)</td><td>154.20 (-10.97%)</td><td>38.56 <b>(+86.18%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.80 (n/a)</td><td>194.10 (n/a)</td><td>186.30 (n/a)</td><td>173.20 (n/a)</td><td>20.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (+0.13%)</td><td>0.18 (-0.21%)</td><td>0.18 (-0.31%)</td><td>0.18 (-0.47%)</td><td>0.00 <b>(+238.38%)</b></td><td>47695.60 (+0.48%)</td><td>47515.50 (+0.21%)</td><td>47549.50 (+0.31%)</td><td>47299.20 (-0.13%)</td><td>155.33 <b>(+239.44%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47469.50 (n/a)</td><td>47414.92 (n/a)</td><td>47403.90 (n/a)</td><td>47358.40 (n/a)</td><td>45.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (-0.97%)</td><td>0.18 (-0.56%)</td><td>0.18 (-0.59%)</td><td>0.18 (-0.18%)</td><td>0.00 <b>(-74.43%)</b></td><td>47662.10 (+0.19%)</td><td>47589.98 (+0.56%)</td><td>47583.20 (+0.59%)</td><td>47530.20 (+0.98%)</td><td>47.46 <b>(-74.14%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47574.00 (n/a)</td><td>47325.96 (n/a)</td><td>47304.70 (n/a)</td><td>47068.60 (n/a)</td><td>183.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (-0.28%)</td><td>0.11 (-0.30%)</td><td>0.11 (-0.29%)</td><td>0.11 (-0.35%)</td><td>0.00 <b>(+113.55%)</b></td><td>375832.60 (+0.35%)</td><td>375530.42 (+0.30%)</td><td>375479.00 (+0.30%)</td><td>375393.50 (+0.28%)</td><td>177.47 <b>(+114.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374533.90 (n/a)</td><td>374401.68 (n/a)</td><td>374372.50 (n/a)</td><td>374335.20 (n/a)</td><td>82.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 <b>(+39.30%)</b></td><td>0.19 <b>(+50.32%)</b></td><td>0.19 <b>(+47.57%)</b></td><td>0.17 <b>(+60.95%)</b></td><td>0.02 <b>(-29.39%)</b></td><td>144.70 <b>(-37.87%)</b></td><td>127.94 <b>(-34.64%)</b></td><td>127.20 <b>(-32.23%)</b></td><td>115.90 <b>(-28.19%)</b></td><td>10.46 <b>(-68.61%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>195.74 (n/a)</td><td>187.70 (n/a)</td><td>161.40 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.42 <b>(+25.48%)</b></td><td>0.38 <b>(+32.40%)</b></td><td>0.38 <b>(+38.01%)</b></td><td>0.33 <b>(+44.19%)</b></td><td>0.03 (-10.91%)</td><td>147.30 <b>(-30.68%)</b></td><td>130.90 <b>(-25.11%)</b></td><td>128.30 <b>(-27.51%)</b></td><td>116.90 <b>(-20.31%)</b></td><td>12.09 <b>(-50.97%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>212.50 (n/a)</td><td>174.80 (n/a)</td><td>177.00 (n/a)</td><td>146.70 (n/a)</td><td>24.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.67 (+7.68%)</td><td>13.35 (+11.88%)</td><td>13.29 (+7.17%)</td><td>13.10 <b>(+36.00%)</b></td><td>0.21 <b>(-83.69%)</b></td><td>800.60 <b>(-26.48%)</b></td><td>785.66 (-11.58%)</td><td>788.70 (-6.70%)</td><td>767.30 (-7.13%)</td><td>12.32 <b>(-89.03%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>12.69 (n/a)</td><td>11.93 (n/a)</td><td>12.40 (n/a)</td><td>9.63 (n/a)</td><td>1.29 (n/a)</td><td>1088.90 (n/a)</td><td>888.60 (n/a)</td><td>845.30 (n/a)</td><td>826.20 (n/a)</td><td>112.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.34 <b>(+42.67%)</b></td><td>0.32 <b>(+43.10%)</b></td><td>0.32 <b>(+38.82%)</b></td><td>0.27 <b>(+39.32%)</b></td><td>0.03 <b>(+44.88%)</b></td><td>152.00 <b>(-28.23%)</b></td><td>130.36 <b>(-30.09%)</b></td><td>127.60 <b>(-27.99%)</b></td><td>119.70 <b>(-29.92%)</b></td><td>12.72 <b>(-26.11%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>211.80 (n/a)</td><td>186.48 (n/a)</td><td>177.20 (n/a)</td><td>170.80 (n/a)</td><td>17.21 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 <b>(+39.67%)</b></td><td>0.04 <b>(+31.41%)</b></td><td>0.04 <b>(+35.40%)</b></td><td>0.03 <b>(+29.36%)</b></td><td>0.00 <b>(+130.19%)</b></td><td>150.80 <b>(-22.71%)</b></td><td>134.04 <b>(-23.41%)</b></td><td>126.80 <b>(-26.15%)</b></td><td>117.90 <b>(-28.42%)</b></td><td>14.97 <b>(+28.28%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>175.02 (n/a)</td><td>171.70 (n/a)</td><td>164.70 (n/a)</td><td>11.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (-3.16%)</td><td>0.03 (+11.12%)</td><td>0.03 <b>(+23.60%)</b></td><td>0.03 (+9.01%)</td><td>0.00 <b>(-21.06%)</b></td><td>161.30 (-8.25%)</td><td>136.38 (-10.92%)</td><td>127.90 (-19.10%)</td><td>115.90 (+3.30%)</td><td>19.59 <b>(-23.49%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>153.10 (n/a)</td><td>158.10 (n/a)</td><td>112.20 (n/a)</td><td>25.61 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (-19.39%)</td><td>0.04 (-18.82%)</td><td>0.04 <b>(-23.16%)</b></td><td>0.03 (-14.69%)</td><td>0.01 <b>(-34.72%)</b></td><td>205.20 (+17.26%)</td><td>172.96 <b>(+21.84%)</b></td><td>169.20 <b>(+30.15%)</b></td><td>138.40 <b>(+24.01%)</b></td><td>24.59 (-7.97%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>175.00 (n/a)</td><td>141.96 (n/a)</td><td>130.00 (n/a)</td><td>111.60 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 <b>(+39.43%)</b></td><td>0.03 <b>(+48.80%)</b></td><td>0.03 <b>(+47.85%)</b></td><td>0.03 <b>(+68.09%)</b></td><td>0.00 (-14.73%)</td><td>138.10 <b>(-40.53%)</b></td><td>125.50 <b>(-34.18%)</b></td><td>132.90 <b>(-32.37%)</b></td><td>107.20 <b>(-28.29%)</b></td><td>13.39 <b>(-63.14%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.20 (n/a)</td><td>190.66 (n/a)</td><td>196.50 (n/a)</td><td>149.50 (n/a)</td><td>36.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (-5.62%)</td><td>0.03 (-14.31%)</td><td>0.02 <b>(-26.56%)</b></td><td>0.02 (+3.34%)</td><td>0.01 (-11.31%)</td><td>230.40 (-3.23%)</td><td>195.78 (+15.78%)</td><td>209.00 <b>(+36.16%)</b></td><td>145.00 (+5.99%)</td><td>36.03 (-11.25%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.10 (n/a)</td><td>169.10 (n/a)</td><td>153.50 (n/a)</td><td>136.80 (n/a)</td><td>40.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 <b>(+35.12%)</b></td><td>0.03 (+17.33%)</td><td>0.03 (+14.15%)</td><td>0.02 (-10.15%)</td><td>0.01 <b>(+191.75%)</b></td><td>238.20 (+11.31%)</td><td>160.40 (-10.22%)</td><td>153.00 (-12.42%)</td><td>119.60 <b>(-25.99%)</b></td><td>47.88 <b>(+133.34%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.00 (n/a)</td><td>178.66 (n/a)</td><td>174.70 (n/a)</td><td>161.60 (n/a)</td><td>20.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 (+14.30%)</td><td>0.03 (+8.85%)</td><td>0.03 (+13.02%)</td><td>0.03 (-0.52%)</td><td>0.00 <b>(+74.65%)</b></td><td>190.60 (+0.53%)</td><td>160.28 (-7.50%)</td><td>154.10 (-11.49%)</td><td>139.20 (-12.51%)</td><td>19.13 <b>(+56.55%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.60 (n/a)</td><td>173.28 (n/a)</td><td>174.10 (n/a)</td><td>159.10 (n/a)</td><td>12.22 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 <b>(+23.51%)</b></td><td>0.03 (+16.74%)</td><td>0.03 (+14.89%)</td><td>0.02 (+10.42%)</td><td>0.00 <b>(+49.59%)</b></td><td>181.50 (-9.43%)</td><td>151.18 (-13.94%)</td><td>148.10 (-12.98%)</td><td>130.20 (-19.03%)</td><td>18.76 (+12.30%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.40 (n/a)</td><td>175.66 (n/a)</td><td>170.20 (n/a)</td><td>160.80 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 <b>(-23.69%)</b></td><td>0.02 (-16.19%)</td><td>0.02 <b>(-20.86%)</b></td><td>0.02 (-10.54%)</td><td>0.00 <b>(-53.85%)</b></td><td>249.90 (+11.76%)</td><td>207.70 (+16.87%)</td><td>200.30 <b>(+26.37%)</b></td><td>190.30 <b>(+31.06%)</b></td><td>24.24 <b>(-31.90%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>177.72 (n/a)</td><td>158.50 (n/a)</td><td>145.20 (n/a)</td><td>35.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.04 <b>(+51.95%)</b></td><td>0.03 <b>(+34.58%)</b></td><td>0.03 <b>(+31.63%)</b></td><td>0.02 (+6.22%)</td><td>0.01 <b>(+130.22%)</b></td><td>230.30 (-5.85%)</td><td>153.48 <b>(-22.34%)</b></td><td>149.70 <b>(-24.01%)</b></td><td>108.10 <b>(-34.21%)</b></td><td>46.69 <b>(+47.49%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.60 (n/a)</td><td>197.62 (n/a)</td><td>197.00 (n/a)</td><td>164.30 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 <b>(-24.01%)</b></td><td>0.02 (-16.70%)</td><td>0.02 (-16.97%)</td><td>0.02 (-6.37%)</td><td>0.00 <b>(-48.35%)</b></td><td>251.50 (+6.79%)</td><td>215.50 (+18.00%)</td><td>218.00 <b>(+20.44%)</b></td><td>186.60 <b>(+31.59%)</b></td><td>24.88 <b>(-28.12%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.50 (n/a)</td><td>182.62 (n/a)</td><td>181.00 (n/a)</td><td>141.80 (n/a)</td><td>34.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 <b>(+24.93%)</b></td><td>0.03 <b>(+26.23%)</b></td><td>0.03 (+16.15%)</td><td>0.02 <b>(+48.75%)</b></td><td>0.00 <b>(-32.28%)</b></td><td>164.90 <b>(-32.78%)</b></td><td>149.22 <b>(-22.10%)</b></td><td>152.60 (-13.88%)</td><td>132.10 (-19.94%)</td><td>12.43 <b>(-63.40%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>245.30 (n/a)</td><td>191.56 (n/a)</td><td>177.20 (n/a)</td><td>165.00 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+8.35%)</td><td>0.02 (+18.00%)</td><td>0.02 (+16.98%)</td><td>0.02 <b>(+34.84%)</b></td><td>0.00 <b>(-23.00%)</b></td><td>222.80 <b>(-25.83%)</b></td><td>187.20 (-17.19%)</td><td>186.20 (-14.51%)</td><td>155.10 (-7.68%)</td><td>26.72 <b>(-47.64%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>300.40 (n/a)</td><td>226.06 (n/a)</td><td>217.80 (n/a)</td><td>168.00 (n/a)</td><td>51.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+18.38%)</td><td>0.03 (+9.74%)</td><td>0.03 (+13.83%)</td><td>0.02 (-13.89%)</td><td>0.01 <b>(+123.22%)</b></td><td>228.70 (+16.15%)</td><td>165.72 (-6.24%)</td><td>156.90 (-12.15%)</td><td>128.20 (-15.49%)</td><td>37.50 <b>(+132.04%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.90 (n/a)</td><td>176.74 (n/a)</td><td>178.60 (n/a)</td><td>151.70 (n/a)</td><td>16.16 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-9.53%)</td><td>0.02 (-10.87%)</td><td>0.02 (-14.23%)</td><td>0.02 (-19.93%)</td><td>0.00 (+17.32%)</td><td>241.90 <b>(+24.88%)</b></td><td>190.26 (+13.85%)</td><td>196.20 (+16.65%)</td><td>145.80 (+10.54%)</td><td>36.91 <b>(+65.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.70 (n/a)</td><td>167.12 (n/a)</td><td>168.20 (n/a)</td><td>131.90 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 <b>(+25.06%)</b></td><td>0.02 <b>(+20.46%)</b></td><td>0.02 <b>(+24.27%)</b></td><td>0.01 (-11.14%)</td><td>0.00 <b>(+153.12%)</b></td><td>307.30 (+12.52%)</td><td>207.72 (-13.72%)</td><td>191.70 (-19.52%)</td><td>166.40 <b>(-20.04%)</b></td><td>56.64 <b>(+140.79%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>273.10 (n/a)</td><td>240.76 (n/a)</td><td>238.20 (n/a)</td><td>208.10 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 <b>(+35.12%)</b></td><td>0.06 <b>(+31.92%)</b></td><td>0.06 <b>(+44.14%)</b></td><td>0.05 <b>(+24.93%)</b></td><td>0.01 <b>(+88.49%)</b></td><td>171.00 (-19.98%)</td><td>143.76 <b>(-23.48%)</b></td><td>133.50 <b>(-30.61%)</b></td><td>124.60 <b>(-26.01%)</b></td><td>21.87 (+13.80%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.70 (n/a)</td><td>187.88 (n/a)</td><td>192.40 (n/a)</td><td>168.40 (n/a)</td><td>19.21 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 <b>(+21.17%)</b></td><td>0.09 (+19.27%)</td><td>0.09 <b>(+29.19%)</b></td><td>0.07 (+11.48%)</td><td>0.02 <b>(+96.91%)</b></td><td>182.10 (-10.30%)</td><td>147.88 (-14.63%)</td><td>133.60 <b>(-22.64%)</b></td><td>123.40 (-17.46%)</td><td>28.33 <b>(+45.20%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>173.22 (n/a)</td><td>172.70 (n/a)</td><td>149.50 (n/a)</td><td>19.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 <b>(+31.84%)</b></td><td>0.05 <b>(+26.04%)</b></td><td>0.06 <b>(+23.35%)</b></td><td>0.04 <b>(+32.78%)</b></td><td>0.01 (+19.65%)</td><td>210.80 <b>(-24.69%)</b></td><td>154.38 <b>(-21.17%)</b></td><td>143.90 (-18.93%)</td><td>126.30 <b>(-24.14%)</b></td><td>32.82 <b>(-30.84%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>279.90 (n/a)</td><td>195.84 (n/a)</td><td>177.50 (n/a)</td><td>166.50 (n/a)</td><td>47.46 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 (-2.46%)</td><td>0.06 (-3.58%)</td><td>0.06 (+1.72%)</td><td>0.04 <b>(-35.16%)</b></td><td>0.02 <b>(+71.59%)</b></td><td>278.40 <b>(+54.24%)</b></td><td>180.56 (+10.37%)</td><td>171.30 (-1.66%)</td><td>128.10 (+2.48%)</td><td>61.28 <b>(+167.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>163.60 (n/a)</td><td>174.20 (n/a)</td><td>125.00 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 <b>(+20.75%)</b></td><td>0.06 (+13.66%)</td><td>0.05 (-1.97%)</td><td>0.05 <b>(+33.51%)</b></td><td>0.01 (+11.13%)</td><td>175.40 <b>(-25.11%)</b></td><td>149.94 (-12.93%)</td><td>159.00 (+1.99%)</td><td>107.50 (-17.18%)</td><td>27.26 <b>(-33.06%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>172.20 (n/a)</td><td>155.90 (n/a)</td><td>129.80 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (+13.29%)</td><td>0.06 (+16.04%)</td><td>0.06 (+7.25%)</td><td>0.05 <b>(+53.75%)</b></td><td>0.01 <b>(-47.85%)</b></td><td>190.50 <b>(-34.96%)</b></td><td>166.08 (-16.82%)</td><td>164.30 (-6.75%)</td><td>150.60 (-11.72%)</td><td>15.43 <b>(-70.55%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.90 (n/a)</td><td>199.66 (n/a)</td><td>176.20 (n/a)</td><td>170.60 (n/a)</td><td>52.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (-17.33%)</td><td>0.05 (+3.47%)</td><td>0.05 (+11.24%)</td><td>0.04 (+10.60%)</td><td>0.01 <b>(-49.22%)</b></td><td>190.90 (-9.61%)</td><td>161.68 (-5.82%)</td><td>151.40 (-10.10%)</td><td>144.80 <b>(+20.97%)</b></td><td>19.48 <b>(-43.07%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>171.68 (n/a)</td><td>168.40 (n/a)</td><td>119.70 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (-5.37%)</td><td>0.05 (-13.49%)</td><td>0.05 (-11.83%)</td><td>0.03 <b>(-22.42%)</b></td><td>0.02 <b>(+35.93%)</b></td><td>293.60 <b>(+28.88%)</b></td><td>196.12 <b>(+22.10%)</b></td><td>171.70 (+13.41%)</td><td>129.50 (+5.71%)</td><td>69.75 <b>(+76.39%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>160.62 (n/a)</td><td>151.40 (n/a)</td><td>122.50 (n/a)</td><td>39.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.06 (+4.97%)</td><td>0.05 (+13.55%)</td><td>0.05 (+13.48%)</td><td>0.05 <b>(+33.88%)</b></td><td>0.01 <b>(-28.05%)</b></td><td>176.20 <b>(-25.31%)</b></td><td>158.56 (-13.82%)</td><td>163.60 (-11.90%)</td><td>129.20 (-4.72%)</td><td>19.68 <b>(-48.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>183.98 (n/a)</td><td>185.70 (n/a)</td><td>135.60 (n/a)</td><td>37.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.07 (+2.65%)</td><td>0.06 (+12.06%)</td><td>0.05 (+13.03%)</td><td>0.05 <b>(+35.59%)</b></td><td>0.01 <b>(-37.77%)</b></td><td>187.80 <b>(-26.24%)</b></td><td>165.22 (-14.57%)</td><td>169.40 (-11.49%)</td><td>128.40 (-2.58%)</td><td>22.12 <b>(-57.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>254.60 (n/a)</td><td>193.40 (n/a)</td><td>191.40 (n/a)</td><td>131.80 (n/a)</td><td>51.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 <b>(+28.73%)</b></td><td>0.05 (+12.37%)</td><td>0.05 <b>(+28.86%)</b></td><td>0.04 (+8.21%)</td><td>0.02 <b>(+44.42%)</b></td><td>207.90 (-7.60%)</td><td>164.48 (-8.92%)</td><td>154.50 <b>(-22.40%)</b></td><td>100.00 <b>(-22.36%)</b></td><td>44.60 (+6.65%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>180.58 (n/a)</td><td>199.10 (n/a)</td><td>128.80 (n/a)</td><td>41.82 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 <b>(+43.38%)</b></td><td>0.05 (-0.02%)</td><td>0.04 (-18.08%)</td><td>0.03 <b>(-33.20%)</b></td><td>0.02 <b>(+235.76%)</b></td><td>305.80 <b>(+49.68%)</b></td><td>202.96 (+12.51%)</td><td>216.30 <b>(+22.13%)</b></td><td>105.40 <b>(-30.24%)</b></td><td>75.76 <b>(+233.30%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>180.40 (n/a)</td><td>177.10 (n/a)</td><td>151.10 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (-3.10%)</td><td>0.05 (+0.06%)</td><td>0.05 (+1.99%)</td><td>0.04 (-3.92%)</td><td>0.01 (-4.50%)</td><td>207.30 (+4.12%)</td><td>177.92 (-0.10%)</td><td>180.00 (-1.96%)</td><td>155.90 (+3.18%)</td><td>21.05 (+1.07%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.10 (n/a)</td><td>178.10 (n/a)</td><td>183.60 (n/a)</td><td>151.10 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.08 <b>(+46.77%)</b></td><td>0.05 (+8.00%)</td><td>0.05 (-0.68%)</td><td>0.04 (-12.95%)</td><td>0.02 <b>(+246.91%)</b></td><td>236.40 (+14.87%)</td><td>181.56 (-1.63%)</td><td>187.70 (+0.70%)</td><td>110.50 <b>(-31.87%)</b></td><td>48.04 <b>(+163.98%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.80 (n/a)</td><td>184.56 (n/a)</td><td>186.40 (n/a)</td><td>162.20 (n/a)</td><td>18.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.05 (+6.27%)</td><td>0.04 (+14.37%)</td><td>0.04 (+2.87%)</td><td>0.04 <b>(+39.96%)</b></td><td>0.00 <b>(-46.88%)</b></td><td>230.00 <b>(-28.55%)</b></td><td>199.46 (-16.28%)</td><td>200.60 (-2.81%)</td><td>167.70 (-5.89%)</td><td>22.10 <b>(-65.17%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>321.90 (n/a)</td><td>238.24 (n/a)</td><td>206.40 (n/a)</td><td>178.20 (n/a)</td><td>63.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 <b>(-24.08%)</b></td><td>0.09 (-17.18%)</td><td>0.09 (-11.75%)</td><td>0.07 (-13.57%)</td><td>0.01 <b>(-49.73%)</b></td><td>232.30 (+15.74%)</td><td>187.22 (+18.02%)</td><td>179.50 (+13.32%)</td><td>159.90 <b>(+31.71%)</b></td><td>27.32 <b>(-20.53%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.70 (n/a)</td><td>158.64 (n/a)</td><td>158.40 (n/a)</td><td>121.40 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (+7.44%)</td><td>0.16 (+8.40%)</td><td>0.17 <b>(+25.18%)</b></td><td>0.11 (-13.50%)</td><td>0.04 <b>(+50.94%)</b></td><td>225.70 (+15.62%)</td><td>162.34 (-5.27%)</td><td>146.30 <b>(-20.14%)</b></td><td>124.70 (-6.94%)</td><td>40.62 <b>(+65.97%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.20 (n/a)</td><td>171.38 (n/a)</td><td>183.20 (n/a)</td><td>134.00 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (+14.05%)</td><td>0.11 (+14.83%)</td><td>0.13 <b>(+30.35%)</b></td><td>0.08 (-1.83%)</td><td>0.03 <b>(+56.95%)</b></td><td>212.60 (+1.87%)</td><td>152.46 (-10.14%)</td><td>129.50 <b>(-23.28%)</b></td><td>111.90 (-12.30%)</td><td>42.01 <b>(+45.63%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.70 (n/a)</td><td>169.66 (n/a)</td><td>168.80 (n/a)</td><td>127.60 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 (+5.41%)</td><td>0.12 (-3.50%)</td><td>0.12 (+1.45%)</td><td>0.08 <b>(-20.49%)</b></td><td>0.04 <b>(+33.72%)</b></td><td>250.90 <b>(+25.76%)</b></td><td>179.24 (+7.24%)</td><td>170.50 (-1.45%)</td><td>113.80 (-5.09%)</td><td>50.51 <b>(+58.30%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>199.50 (n/a)</td><td>167.14 (n/a)</td><td>173.00 (n/a)</td><td>119.90 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (-11.63%)</td><td>0.11 (-2.87%)</td><td>0.11 (+10.04%)</td><td>0.09 (+3.54%)</td><td>0.01 <b>(-55.31%)</b></td><td>176.30 (-3.45%)</td><td>154.50 (+0.44%)</td><td>149.80 (-9.10%)</td><td>137.00 (+13.13%)</td><td>14.88 <b>(-49.95%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>182.60 (n/a)</td><td>153.82 (n/a)</td><td>164.80 (n/a)</td><td>121.10 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 <b>(+25.58%)</b></td><td>0.14 (+12.22%)</td><td>0.15 <b>(+22.16%)</b></td><td>0.10 (+4.35%)</td><td>0.03 <b>(+91.14%)</b></td><td>199.00 (-4.19%)</td><td>152.06 (-7.95%)</td><td>135.00 (-18.13%)</td><td>111.60 <b>(-20.40%)</b></td><td>38.75 <b>(+48.67%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>207.70 (n/a)</td><td>165.20 (n/a)</td><td>164.90 (n/a)</td><td>140.20 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (-3.29%)</td><td>0.10 (+1.92%)</td><td>0.11 (-2.80%)</td><td>0.07 (+4.82%)</td><td>0.02 <b>(-23.98%)</b></td><td>239.90 (-4.61%)</td><td>167.22 (-4.73%)</td><td>153.00 (+2.89%)</td><td>131.70 (+3.46%)</td><td>42.91 <b>(-22.26%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>251.50 (n/a)</td><td>175.52 (n/a)</td><td>148.70 (n/a)</td><td>127.30 (n/a)</td><td>55.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.18 <b>(+28.57%)</b></td><td>0.13 (+13.81%)</td><td>0.12 (+12.34%)</td><td>0.10 <b>(+27.22%)</b></td><td>0.03 <b>(+28.68%)</b></td><td>190.40 <b>(-21.39%)</b></td><td>152.58 (-11.84%)</td><td>150.40 (-11.01%)</td><td>102.80 <b>(-22.24%)</b></td><td>37.26 (-17.04%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>242.20 (n/a)</td><td>173.08 (n/a)</td><td>169.00 (n/a)</td><td>132.20 (n/a)</td><td>44.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (+7.52%)</td><td>0.11 (+19.58%)</td><td>0.11 <b>(+27.71%)</b></td><td>0.08 (+2.27%)</td><td>0.02 <b>(+21.61%)</b></td><td>196.80 (-2.19%)</td><td>150.70 (-15.76%)</td><td>145.40 <b>(-21.70%)</b></td><td>125.70 (-7.03%)</td><td>28.93 (+14.19%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.20 (n/a)</td><td>178.90 (n/a)</td><td>185.70 (n/a)</td><td>135.20 (n/a)</td><td>25.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (+1.98%)</td><td>0.12 (+8.96%)</td><td>0.12 (+11.53%)</td><td>0.10 (+12.19%)</td><td>0.02 (+3.69%)</td><td>191.30 (-10.86%)</td><td>153.76 (-8.39%)</td><td>150.60 (-10.36%)</td><td>128.00 (-1.92%)</td><td>26.78 (-11.86%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>167.84 (n/a)</td><td>168.00 (n/a)</td><td>130.50 (n/a)</td><td>30.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (-10.88%)</td><td>0.10 (-5.48%)</td><td>0.10 (+3.62%)</td><td>0.08 (+3.62%)</td><td>0.02 <b>(-34.92%)</b></td><td>202.80 (-3.52%)</td><td>168.88 (+3.30%)</td><td>161.90 (-3.52%)</td><td>132.80 (+12.16%)</td><td>26.75 <b>(-28.79%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.20 (n/a)</td><td>163.48 (n/a)</td><td>167.80 (n/a)</td><td>118.40 (n/a)</td><td>37.57 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (-18.70%)</td><td>0.10 (-7.34%)</td><td>0.11 (+16.19%)</td><td>0.06 <b>(-27.40%)</b></td><td>0.03 (-12.13%)</td><td>302.60 <b>(+37.73%)</b></td><td>186.36 (+10.42%)</td><td>156.40 (-13.92%)</td><td>130.60 <b>(+22.98%)</b></td><td>69.49 <b>(+56.05%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>219.70 (n/a)</td><td>168.78 (n/a)</td><td>181.70 (n/a)</td><td>106.20 (n/a)</td><td>44.53 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 <b>(+20.19%)</b></td><td>0.11 <b>(+25.31%)</b></td><td>0.12 <b>(+32.07%)</b></td><td>0.09 <b>(+28.04%)</b></td><td>0.02 <b>(+23.67%)</b></td><td>189.70 <b>(-21.90%)</b></td><td>153.00 <b>(-20.12%)</b></td><td>141.30 <b>(-24.28%)</b></td><td>119.70 (-16.82%)</td><td>29.85 (-17.24%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.90 (n/a)</td><td>191.54 (n/a)</td><td>186.60 (n/a)</td><td>143.90 (n/a)</td><td>36.07 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.11 (+11.05%)</td><td>0.09 <b>(+30.18%)</b></td><td>0.09 <b>(+51.67%)</b></td><td>0.08 <b>(+72.65%)</b></td><td>0.01 <b>(-47.07%)</b></td><td>214.80 <b>(-42.09%)</b></td><td>189.52 <b>(-28.32%)</b></td><td>187.90 <b>(-34.07%)</b></td><td>159.70 (-9.93%)</td><td>24.57 <b>(-70.23%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>370.90 (n/a)</td><td>264.38 (n/a)</td><td>285.00 (n/a)</td><td>177.30 (n/a)</td><td>82.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (+5.90%)</td><td>0.09 (+16.11%)</td><td>0.09 (+3.77%)</td><td>0.07 <b>(+57.88%)</b></td><td>0.01 <b>(-38.92%)</b></td><td>219.00 <b>(-36.67%)</b></td><td>190.34 (-17.62%)</td><td>192.40 (-3.61%)</td><td>163.40 (-5.60%)</td><td>23.78 <b>(-65.12%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>345.80 (n/a)</td><td>231.06 (n/a)</td><td>199.60 (n/a)</td><td>173.10 (n/a)</td><td>68.17 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 <b>(+20.25%)</b></td><td>0.21 (+5.94%)</td><td>0.21 (+6.75%)</td><td>0.15 (-9.76%)</td><td>0.05 <b>(+106.33%)</b></td><td>225.40 (+10.82%)</td><td>165.52 (-2.14%)</td><td>155.10 (-6.34%)</td><td>120.20 (-16.87%)</td><td>41.84 <b>(+89.63%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.40 (n/a)</td><td>169.14 (n/a)</td><td>165.60 (n/a)</td><td>144.60 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 <b>(+33.92%)</b></td><td>0.21 (+18.18%)</td><td>0.18 (+8.33%)</td><td>0.13 (-15.75%)</td><td>0.07 <b>(+159.23%)</b></td><td>251.10 (+18.72%)</td><td>170.74 (-9.45%)</td><td>179.00 (-7.68%)</td><td>111.20 <b>(-25.32%)</b></td><td>54.96 <b>(+131.54%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>211.50 (n/a)</td><td>188.56 (n/a)</td><td>193.90 (n/a)</td><td>148.90 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.33 <b>(+40.31%)</b></td><td>0.26 <b>(+21.93%)</b></td><td>0.27 <b>(+27.85%)</b></td><td>0.20 (-0.46%)</td><td>0.06 <b>(+399.07%)</b></td><td>202.40 (+0.45%)</td><td>161.86 (-14.63%)</td><td>150.50 <b>(-21.78%)</b></td><td>125.20 <b>(-28.70%)</b></td><td>37.54 <b>(+266.82%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>189.60 (n/a)</td><td>192.40 (n/a)</td><td>175.60 (n/a)</td><td>10.23 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 <b>(+22.50%)</b></td><td>0.21 (+10.52%)</td><td>0.23 (+19.76%)</td><td>0.14 (-10.45%)</td><td>0.05 <b>(+171.24%)</b></td><td>233.60 (+11.66%)</td><td>166.20 (-5.48%)</td><td>141.80 (-16.49%)</td><td>131.80 (-18.39%)</td><td>44.93 <b>(+135.81%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>209.20 (n/a)</td><td>175.84 (n/a)</td><td>169.80 (n/a)</td><td>161.50 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.31 (+7.03%)</td><td>0.24 (+14.95%)</td><td>0.26 <b>(+37.17%)</b></td><td>0.12 <b>(-25.94%)</b></td><td>0.07 <b>(+31.25%)</b></td><td>349.50 <b>(+34.99%)</b></td><td>192.62 (-7.17%)</td><td>158.60 <b>(-27.11%)</b></td><td>131.10 (-6.56%)</td><td>88.99 <b>(+77.27%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>258.90 (n/a)</td><td>207.50 (n/a)</td><td>217.60 (n/a)</td><td>140.30 (n/a)</td><td>50.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (+7.87%)</td><td>0.17 (-10.94%)</td><td>0.15 <b>(-20.31%)</b></td><td>0.15 (-11.72%)</td><td>0.04 <b>(+57.21%)</b></td><td>219.20 (+13.28%)</td><td>194.54 (+14.57%)</td><td>216.40 <b>(+25.45%)</b></td><td>137.50 (-7.28%)</td><td>35.63 <b>(+70.18%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>193.50 (n/a)</td><td>169.80 (n/a)</td><td>172.50 (n/a)</td><td>148.30 (n/a)</td><td>20.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.30 (-9.50%)</td><td>0.23 (+1.01%)</td><td>0.23 (+11.02%)</td><td>0.18 (-2.95%)</td><td>0.05 <b>(-23.49%)</b></td><td>203.10 (+3.04%)</td><td>165.08 (-2.37%)</td><td>158.80 (-9.93%)</td><td>122.00 (+10.51%)</td><td>30.98 (-10.57%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>197.10 (n/a)</td><td>169.08 (n/a)</td><td>176.30 (n/a)</td><td>110.40 (n/a)</td><td>34.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (+8.87%)</td><td>0.20 (+10.15%)</td><td>0.21 <b>(+20.79%)</b></td><td>0.16 (-4.84%)</td><td>0.04 <b>(+52.11%)</b></td><td>204.40 (+5.04%)</td><td>165.70 (-7.73%)</td><td>154.20 (-17.19%)</td><td>131.60 (-8.16%)</td><td>31.90 <b>(+52.09%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.60 (n/a)</td><td>179.58 (n/a)</td><td>186.20 (n/a)</td><td>143.30 (n/a)</td><td>20.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.30 <b>(+21.58%)</b></td><td>0.24 (+6.32%)</td><td>0.24 (+5.30%)</td><td>0.19 (-7.26%)</td><td>0.04 <b>(+116.78%)</b></td><td>198.30 (+7.83%)</td><td>159.42 (-4.10%)</td><td>154.40 (-5.04%)</td><td>122.10 (-17.72%)</td><td>28.23 <b>(+89.70%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>183.90 (n/a)</td><td>166.24 (n/a)</td><td>162.60 (n/a)</td><td>148.40 (n/a)</td><td>14.88 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 <b>(+44.10%)</b></td><td>0.20 (+9.27%)</td><td>0.17 (-2.82%)</td><td>0.16 (-6.70%)</td><td>0.05 <b>(+396.00%)</b></td><td>209.00 (+7.18%)</td><td>173.82 (-4.79%)</td><td>188.10 (+2.90%)</td><td>116.20 <b>(-30.59%)</b></td><td>35.66 <b>(+257.81%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>195.00 (n/a)</td><td>182.56 (n/a)</td><td>182.80 (n/a)</td><td>167.40 (n/a)</td><td>9.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 <b>(+31.68%)</b></td><td>0.22 <b>(+28.10%)</b></td><td>0.21 <b>(+25.40%)</b></td><td>0.19 <b>(+22.80%)</b></td><td>0.04 <b>(+55.52%)</b></td><td>187.30 (-18.57%)</td><td>161.94 <b>(-21.42%)</b></td><td>165.00 <b>(-20.25%)</b></td><td>126.30 <b>(-24.05%)</b></td><td>24.41 (-3.43%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>230.00 (n/a)</td><td>206.08 (n/a)</td><td>206.90 (n/a)</td><td>166.30 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 (+19.01%)</td><td>0.17 (-8.01%)</td><td>0.16 (-16.66%)</td><td>0.13 <b>(-20.56%)</b></td><td>0.05 <b>(+107.31%)</b></td><td>258.90 <b>(+25.86%)</b></td><td>199.30 (+13.35%)</td><td>206.70 (+19.97%)</td><td>129.50 (-15.96%)</td><td>48.34 <b>(+115.43%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>205.70 (n/a)</td><td>175.82 (n/a)</td><td>172.30 (n/a)</td><td>154.10 (n/a)</td><td>22.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.22 (-15.64%)</td><td>0.20 (-0.22%)</td><td>0.21 (-4.88%)</td><td>0.18 (+17.67%)</td><td>0.02 <b>(-61.71%)</b></td><td>194.40 (-15.03%)</td><td>171.20 (-2.88%)</td><td>168.50 (+5.12%)</td><td>158.30 (+18.49%)</td><td>14.53 <b>(-62.04%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>228.80 (n/a)</td><td>176.28 (n/a)</td><td>160.30 (n/a)</td><td>133.60 (n/a)</td><td>38.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.25 <b>(+31.41%)</b></td><td>0.17 (+4.71%)</td><td>0.16 (-5.10%)</td><td>0.15 (+7.33%)</td><td>0.04 <b>(+120.17%)</b></td><td>225.30 (-6.82%)</td><td>195.78 (-2.10%)</td><td>204.50 (+5.36%)</td><td>133.60 <b>(-23.92%)</b></td><td>36.79 <b>(+48.21%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>241.80 (n/a)</td><td>199.98 (n/a)</td><td>194.10 (n/a)</td><td>175.60 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 <b>(+30.13%)</b></td><td>0.13 (+14.41%)</td><td>0.13 (+14.76%)</td><td>0.09 (-8.08%)</td><td>0.02 <b>(+168.98%)</b></td><td>216.00 (+8.82%)</td><td>165.46 (-10.31%)</td><td>162.00 (-12.86%)</td><td>124.50 <b>(-23.20%)</b></td><td>33.02 <b>(+126.93%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>184.48 (n/a)</td><td>185.90 (n/a)</td><td>162.10 (n/a)</td><td>14.55 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (+17.24%)</td><td>0.13 (+12.91%)</td><td>0.12 (+14.33%)</td><td>0.10 (+1.94%)</td><td>0.02 <b>(+41.97%)</b></td><td>198.50 (-1.93%)</td><td>164.16 (-10.74%)</td><td>167.40 (-12.54%)</td><td>127.40 (-14.73%)</td><td>25.45 (+16.92%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>183.92 (n/a)</td><td>191.40 (n/a)</td><td>149.40 (n/a)</td><td>21.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (-8.08%)</td><td>0.14 (+2.27%)</td><td>0.15 (+7.56%)</td><td>0.10 (+15.41%)</td><td>0.03 <b>(-27.95%)</b></td><td>213.50 (-13.35%)</td><td>150.90 (-5.50%)</td><td>135.80 (-7.05%)</td><td>127.70 (+8.77%)</td><td>35.73 <b>(-31.25%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>246.40 (n/a)</td><td>159.68 (n/a)</td><td>146.10 (n/a)</td><td>117.40 (n/a)</td><td>51.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (-7.63%)</td><td>0.13 (-0.32%)</td><td>0.13 (-2.25%)</td><td>0.10 (+3.71%)</td><td>0.03 (-8.19%)</td><td>212.40 (-3.54%)</td><td>166.72 (-0.14%)</td><td>163.30 (+2.32%)</td><td>129.00 (+8.31%)</td><td>36.04 (-5.16%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>220.20 (n/a)</td><td>166.96 (n/a)</td><td>159.60 (n/a)</td><td>119.10 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (-3.17%)</td><td>0.11 (-11.97%)</td><td>0.11 (-1.71%)</td><td>0.08 (-18.32%)</td><td>0.03 (+4.71%)</td><td>253.30 <b>(+22.43%)</b></td><td>196.26 (+14.92%)</td><td>192.30 (+1.75%)</td><td>131.00 (+3.31%)</td><td>44.70 <b>(+29.22%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>206.90 (n/a)</td><td>170.78 (n/a)</td><td>189.00 (n/a)</td><td>126.80 (n/a)</td><td>34.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (+15.29%)</td><td>0.12 (-8.74%)</td><td>0.11 <b>(-20.23%)</b></td><td>0.10 (+18.98%)</td><td>0.04 (+15.02%)</td><td>202.40 (-15.95%)</td><td>174.12 (+9.21%)</td><td>189.60 <b>(+25.31%)</b></td><td>109.50 (-13.30%)</td><td>38.34 (-18.74%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>240.80 (n/a)</td><td>159.44 (n/a)</td><td>151.30 (n/a)</td><td>126.30 (n/a)</td><td>47.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (+13.40%)</td><td>0.12 (+14.27%)</td><td>0.12 <b>(+26.72%)</b></td><td>0.11 (+18.08%)</td><td>0.02 (-17.26%)</td><td>192.90 (-15.32%)</td><td>167.50 (-13.63%)</td><td>165.20 <b>(-21.07%)</b></td><td>136.20 (-11.84%)</td><td>21.61 <b>(-37.57%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>227.80 (n/a)</td><td>193.94 (n/a)</td><td>209.30 (n/a)</td><td>154.50 (n/a)</td><td>34.61 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (+19.37%)</td><td>0.14 <b>(+22.94%)</b></td><td>0.14 <b>(+20.29%)</b></td><td>0.11 (+19.25%)</td><td>0.01 (-7.65%)</td><td>178.40 (-16.13%)</td><td>149.14 (-19.16%)</td><td>143.60 (-16.90%)</td><td>135.10 (-16.24%)</td><td>17.01 <b>(-34.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>212.70 (n/a)</td><td>184.48 (n/a)</td><td>172.80 (n/a)</td><td>161.30 (n/a)</td><td>25.99 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.19 (+2.58%)</td><td>0.17 (+11.93%)</td><td>0.18 <b>(+34.20%)</b></td><td>0.13 (+8.55%)</td><td>0.03 (-12.89%)</td><td>188.80 (-7.86%)</td><td>148.04 (-11.51%)</td><td>134.70 <b>(-25.50%)</b></td><td>127.60 (-2.52%)</td><td>26.15 (-19.92%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>204.90 (n/a)</td><td>167.30 (n/a)</td><td>180.80 (n/a)</td><td>130.90 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 <b>(+23.27%)</b></td><td>0.17 <b>(+27.43%)</b></td><td>0.17 <b>(+35.38%)</b></td><td>0.15 <b>(+22.78%)</b></td><td>0.02 <b>(+25.42%)</b></td><td>169.20 (-18.58%)</td><td>145.34 <b>(-21.51%)</b></td><td>146.20 <b>(-26.12%)</b></td><td>124.00 (-18.90%)</td><td>19.58 (-18.13%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.80 (n/a)</td><td>185.18 (n/a)</td><td>197.90 (n/a)</td><td>152.90 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (-13.33%)</td><td>0.15 (-18.63%)</td><td>0.14 <b>(-24.38%)</b></td><td>0.12 <b>(-21.82%)</b></td><td>0.03 (+15.93%)</td><td>212.80 <b>(+27.88%)</b></td><td>171.42 <b>(+25.14%)</b></td><td>179.30 <b>(+32.23%)</b></td><td>125.70 (+15.32%)</td><td>35.66 <b>(+70.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>166.40 (n/a)</td><td>136.98 (n/a)</td><td>135.60 (n/a)</td><td>109.00 (n/a)</td><td>20.88 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (-13.85%)</td><td>0.14 (-13.58%)</td><td>0.15 (-9.77%)</td><td>0.11 (-11.46%)</td><td>0.02 (-7.10%)</td><td>217.50 (+12.93%)</td><td>180.32 (+16.08%)</td><td>160.20 (+10.79%)</td><td>154.30 (+16.10%)</td><td>32.62 <b>(+24.00%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.60 (n/a)</td><td>155.34 (n/a)</td><td>144.60 (n/a)</td><td>132.90 (n/a)</td><td>26.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 <b>(-20.02%)</b></td><td>0.13 (-14.71%)</td><td>0.12 (-0.85%)</td><td>0.11 (-5.73%)</td><td>0.02 <b>(-51.25%)</b></td><td>219.10 (+6.10%)</td><td>190.92 (+12.25%)</td><td>199.00 (+0.86%)</td><td>150.10 <b>(+25.08%)</b></td><td>30.01 <b>(-33.90%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>206.50 (n/a)</td><td>170.08 (n/a)</td><td>197.30 (n/a)</td><td>120.00 (n/a)</td><td>45.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.20 (-18.96%)</td><td>0.16 (-5.47%)</td><td>0.16 (+8.95%)</td><td>0.12 (-1.21%)</td><td>0.03 <b>(-33.14%)</b></td><td>202.00 (+1.20%)</td><td>156.50 (+2.83%)</td><td>154.00 (-8.22%)</td><td>125.00 <b>(+23.40%)</b></td><td>33.36 (-18.12%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>199.60 (n/a)</td><td>152.20 (n/a)</td><td>167.80 (n/a)</td><td>101.30 (n/a)</td><td>40.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (+9.12%)</td><td>0.15 <b>(+22.43%)</b></td><td>0.15 <b>(+33.04%)</b></td><td>0.12 <b>(+20.48%)</b></td><td>0.02 (-2.21%)</td><td>200.90 (-16.98%)</td><td>171.04 (-18.69%)</td><td>161.50 <b>(-24.85%)</b></td><td>150.10 (-8.31%)</td><td>22.69 <b>(-24.40%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>242.00 (n/a)</td><td>210.36 (n/a)</td><td>214.90 (n/a)</td><td>163.70 (n/a)</td><td>30.01 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.17 <b>(+25.22%)</b></td><td>0.14 (+19.56%)</td><td>0.17 <b>(+44.02%)</b></td><td>0.07 <b>(-31.27%)</b></td><td>0.05 <b>(+186.52%)</b></td><td>368.10 <b>(+45.49%)</b></td><td>200.48 (-5.82%)</td><td>146.00 <b>(-30.58%)</b></td><td>141.10 <b>(-20.15%)</b></td><td>97.24 <b>(+228.69%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>253.00 (n/a)</td><td>212.86 (n/a)</td><td>210.30 (n/a)</td><td>176.70 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.16 (+18.37%)</td><td>0.12 <b>(+24.95%)</b></td><td>0.11 (+14.78%)</td><td>0.10 <b>(+75.77%)</b></td><td>0.02 (-9.00%)</td><td>188.00 <b>(-43.12%)</b></td><td>163.18 <b>(-23.48%)</b></td><td>175.00 (-12.85%)</td><td>118.30 (-15.56%)</td><td>30.22 <b>(-57.27%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>330.50 (n/a)</td><td>213.26 (n/a)</td><td>200.80 (n/a)</td><td>140.10 (n/a)</td><td>70.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 <b>(+24.27%)</b></td><td>0.12 (+16.81%)</td><td>0.11 (+11.49%)</td><td>0.10 (+3.85%)</td><td>0.02 <b>(+96.58%)</b></td><td>191.90 (-3.71%)</td><td>159.80 (-13.09%)</td><td>165.00 (-10.33%)</td><td>125.40 (-19.56%)</td><td>26.55 <b>(+51.63%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>199.30 (n/a)</td><td>183.86 (n/a)</td><td>184.00 (n/a)</td><td>155.90 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.15 (+8.11%)</td><td>0.11 (+0.69%)</td><td>0.11 (-1.25%)</td><td>0.09 (-10.65%)</td><td>0.03 <b>(+82.90%)</b></td><td>211.80 (+11.95%)</td><td>169.00 (+2.74%)</td><td>170.20 (+1.25%)</td><td>122.90 (-7.45%)</td><td>40.01 <b>(+96.26%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>189.20 (n/a)</td><td>164.50 (n/a)</td><td>168.10 (n/a)</td><td>132.80 (n/a)</td><td>20.39 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (-1.53%)</td><td>0.11 (-11.20%)</td><td>0.12 (-9.97%)</td><td>0.08 <b>(-32.65%)</b></td><td>0.03 <b>(+101.79%)</b></td><td>244.10 <b>(+48.48%)</b></td><td>169.70 (+17.24%)</td><td>156.60 (+11.06%)</td><td>130.60 (+1.56%)</td><td>45.21 <b>(+208.47%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>164.40 (n/a)</td><td>144.74 (n/a)</td><td>141.00 (n/a)</td><td>128.60 (n/a)</td><td>14.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.14 (-12.48%)</td><td>0.12 (+7.62%)</td><td>0.11 (-0.39%)</td><td>0.09 <b>(+47.16%)</b></td><td>0.02 <b>(-45.12%)</b></td><td>194.10 <b>(-32.06%)</b></td><td>160.90 (-13.13%)</td><td>168.90 (+0.42%)</td><td>132.30 (+14.25%)</td><td>26.07 <b>(-59.29%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>285.70 (n/a)</td><td>185.22 (n/a)</td><td>168.20 (n/a)</td><td>115.80 (n/a)</td><td>64.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (+11.15%)</td><td>0.10 (+16.69%)</td><td>0.10 <b>(+27.00%)</b></td><td>0.08 <b>(+53.19%)</b></td><td>0.02 <b>(-30.74%)</b></td><td>230.70 <b>(-34.72%)</b></td><td>194.54 <b>(-20.03%)</b></td><td>189.10 <b>(-21.24%)</b></td><td>141.50 (-10.04%)</td><td>35.81 <b>(-57.64%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>353.40 (n/a)</td><td>243.26 (n/a)</td><td>240.10 (n/a)</td><td>157.30 (n/a)</td><td>84.53 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.10 (-12.90%)</td><td>0.10 (-8.07%)</td><td>0.10 (-12.95%)</td><td>0.09 (+0.85%)</td><td>0.01 <b>(-59.51%)</b></td><td>214.50 (-0.83%)</td><td>193.50 (+7.30%)</td><td>188.70 (+14.85%)</td><td>182.70 (+14.83%)</td><td>12.68 <b>(-52.98%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>216.30 (n/a)</td><td>180.34 (n/a)</td><td>164.30 (n/a)</td><td>159.10 (n/a)</td><td>26.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.12 (+0.97%)</td><td>0.09 (-4.30%)</td><td>0.09 (-14.12%)</td><td>0.06 (-18.36%)</td><td>0.02 <b>(+29.91%)</b></td><td>322.80 <b>(+22.50%)</b></td><td>215.56 (+7.74%)</td><td>212.80 (+16.41%)</td><td>157.70 (-0.94%)</td><td>64.96 <b>(+57.53%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>263.50 (n/a)</td><td>200.08 (n/a)</td><td>182.80 (n/a)</td><td>159.20 (n/a)</td><td>41.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.76 (+0.68%)</td><td>0.66 (+0.51%)</td><td>0.67 (+5.38%)</td><td>0.55 (-1.27%)</td><td>0.09 (+19.94%)</td><td>177.70 (+1.25%)</td><td>151.84 (-0.08%)</td><td>146.40 (-5.12%)</td><td>128.60 (-0.69%)</td><td>20.37 <b>(+22.01%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.76 (n/a)</td><td>0.65 (n/a)</td><td>0.64 (n/a)</td><td>0.56 (n/a)</td><td>0.07 (n/a)</td><td>175.50 (n/a)</td><td>151.96 (n/a)</td><td>154.30 (n/a)</td><td>129.50 (n/a)</td><td>16.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.64 (-14.48%)</td><td>0.54 (-14.47%)</td><td>0.61 (-3.66%)</td><td>0.31 <b>(-38.34%)</b></td><td>0.14 <b>(+22.28%)</b></td><td>320.70 <b>(+62.22%)</b></td><td>195.60 <b>(+22.86%)</b></td><td>160.50 (+3.82%)</td><td>153.40 (+16.92%)</td><td>70.87 <b>(+143.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.75 (n/a)</td><td>0.63 (n/a)</td><td>0.64 (n/a)</td><td>0.50 (n/a)</td><td>0.11 (n/a)</td><td>197.70 (n/a)</td><td>159.20 (n/a)</td><td>154.60 (n/a)</td><td>131.20 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.72 (+0.92%)</td><td>0.61 (+7.79%)</td><td>0.59 (+11.37%)</td><td>0.53 (+17.48%)</td><td>0.07 <b>(-25.14%)</b></td><td>186.30 (-14.89%)</td><td>163.40 (-8.40%)</td><td>166.40 (-10.25%)</td><td>136.50 (-0.94%)</td><td>19.20 <b>(-36.63%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.71 (n/a)</td><td>0.56 (n/a)</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.10 (n/a)</td><td>218.90 (n/a)</td><td>178.38 (n/a)</td><td>185.40 (n/a)</td><td>137.80 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.61 (-2.99%)</td><td>0.49 (-7.53%)</td><td>0.50 (-10.33%)</td><td>0.37 (-9.89%)</td><td>0.09 (+9.09%)</td><td>269.00 (+10.97%)</td><td>207.72 (+9.03%)</td><td>194.90 (+11.50%)</td><td>161.60 (+3.13%)</td><td>42.25 <b>(+24.40%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.63 (n/a)</td><td>0.53 (n/a)</td><td>0.56 (n/a)</td><td>0.41 (n/a)</td><td>0.09 (n/a)</td><td>242.40 (n/a)</td><td>190.52 (n/a)</td><td>174.80 (n/a)</td><td>156.70 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.59 <b>(+38.76%)</b></td><td>0.43 (+16.28%)</td><td>0.39 (+2.56%)</td><td>0.33 (+9.48%)</td><td>0.10 <b>(+97.06%)</b></td><td>222.00 (-8.68%)</td><td>176.94 (-11.99%)</td><td>186.70 (-2.51%)</td><td>125.70 <b>(-27.97%)</b></td><td>37.18 <b>(+28.39%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.05 (n/a)</td><td>243.10 (n/a)</td><td>201.04 (n/a)</td><td>191.50 (n/a)</td><td>174.50 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.52 <b>(-24.92%)</b></td><td>0.46 (-10.74%)</td><td>0.48 (+4.16%)</td><td>0.38 (-8.28%)</td><td>0.06 <b>(-49.32%)</b></td><td>193.60 (+9.07%)</td><td>163.00 (+9.75%)</td><td>153.70 (-4.00%)</td><td>141.90 <b>(+33.11%)</b></td><td>21.19 <b>(-24.88%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.69 (n/a)</td><td>0.51 (n/a)</td><td>0.46 (n/a)</td><td>0.42 (n/a)</td><td>0.11 (n/a)</td><td>177.50 (n/a)</td><td>148.52 (n/a)</td><td>160.10 (n/a)</td><td>106.60 (n/a)</td><td>28.21 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.55 <b>(+27.31%)</b></td><td>0.41 (+4.51%)</td><td>0.39 (-8.10%)</td><td>0.36 (+12.63%)</td><td>0.08 <b>(+58.56%)</b></td><td>204.80 (-11.23%)</td><td>183.00 (-3.36%)</td><td>188.60 (+8.83%)</td><td>134.10 <b>(-21.44%)</b></td><td>28.49 (+9.23%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.43 (n/a)</td><td>0.39 (n/a)</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>230.70 (n/a)</td><td>189.36 (n/a)</td><td>173.30 (n/a)</td><td>170.70 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.54 (+12.52%)</td><td>0.44 (+8.00%)</td><td>0.47 (+3.71%)</td><td>0.29 (-4.47%)</td><td>0.10 <b>(+31.15%)</b></td><td>256.60 (+4.65%)</td><td>174.00 (-5.66%)</td><td>157.00 (-3.56%)</td><td>137.10 (-11.15%)</td><td>48.00 <b>(+26.40%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.45 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>245.20 (n/a)</td><td>184.44 (n/a)</td><td>162.80 (n/a)</td><td>154.30 (n/a)</td><td>37.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 (+1.29%)</td><td>0.24 (-0.95%)</td><td>0.26 (+17.05%)</td><td>0.17 (-14.51%)</td><td>0.05 (+17.92%)</td><td>210.90 (+16.97%)</td><td>159.64 (+2.33%)</td><td>140.90 (-14.61%)</td><td>126.50 (-1.25%)</td><td>34.96 <b>(+39.22%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>180.30 (n/a)</td><td>156.00 (n/a)</td><td>165.00 (n/a)</td><td>128.10 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.28 (-4.39%)</td><td>0.20 <b>(-21.56%)</b></td><td>0.17 <b>(-39.20%)</b></td><td>0.14 <b>(-32.00%)</b></td><td>0.06 <b>(+41.53%)</b></td><td>259.00 <b>(+47.08%)</b></td><td>196.04 <b>(+33.00%)</b></td><td>214.50 <b>(+64.49%)</b></td><td>132.50 (+4.66%)</td><td>53.22 <b>(+110.41%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>176.10 (n/a)</td><td>147.40 (n/a)</td><td>130.40 (n/a)</td><td>126.60 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 (+2.85%)</td><td>0.25 (+8.71%)</td><td>0.27 (+17.88%)</td><td>0.20 <b>(+32.73%)</b></td><td>0.04 <b>(-26.79%)</b></td><td>183.50 <b>(-24.67%)</b></td><td>150.26 (-10.64%)</td><td>136.20 (-15.19%)</td><td>128.60 (-2.80%)</td><td>24.15 <b>(-46.50%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>243.60 (n/a)</td><td>168.16 (n/a)</td><td>160.60 (n/a)</td><td>132.30 (n/a)</td><td>45.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.26 (-9.81%)</td><td>0.23 (-4.78%)</td><td>0.24 (-5.54%)</td><td>0.19 (+15.45%)</td><td>0.03 <b>(-37.47%)</b></td><td>198.90 (-13.41%)</td><td>164.30 (+2.02%)</td><td>151.30 (+5.88%)</td><td>141.00 (+10.85%)</td><td>25.24 <b>(-40.15%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>229.70 (n/a)</td><td>161.04 (n/a)</td><td>142.90 (n/a)</td><td>127.20 (n/a)</td><td>42.17 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 <b>(-26.44%)</b></td><td>0.17 <b>(-24.93%)</b></td><td>0.18 <b>(-21.46%)</b></td><td>0.11 <b>(-38.27%)</b></td><td>0.04 (-0.81%)</td><td>329.00 <b>(+61.99%)</b></td><td>226.42 <b>(+37.07%)</b></td><td>203.10 <b>(+27.34%)</b></td><td>174.10 <b>(+36.02%)</b></td><td>63.61 <b>(+117.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>203.10 (n/a)</td><td>165.18 (n/a)</td><td>159.50 (n/a)</td><td>128.00 (n/a)</td><td>29.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.23 (-19.89%)</td><td>0.19 (-17.29%)</td><td>0.19 (-15.35%)</td><td>0.17 (-10.88%)</td><td>0.02 <b>(-46.21%)</b></td><td>222.90 (+12.18%)</td><td>191.92 (+18.75%)</td><td>196.90 (+18.12%)</td><td>160.20 <b>(+24.77%)</b></td><td>23.94 <b>(-23.04%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>198.70 (n/a)</td><td>161.62 (n/a)</td><td>166.70 (n/a)</td><td>128.40 (n/a)</td><td>31.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (+10.37%)</td><td>0.24 <b>(+22.45%)</b></td><td>0.24 (+14.30%)</td><td>0.19 <b>(+56.42%)</b></td><td>0.03 <b>(-32.38%)</b></td><td>198.50 <b>(-36.05%)</b></td><td>158.24 <b>(-22.08%)</b></td><td>155.90 (-12.51%)</td><td>137.60 (-9.41%)</td><td>24.50 <b>(-61.67%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>310.40 (n/a)</td><td>203.08 (n/a)</td><td>178.20 (n/a)</td><td>151.90 (n/a)</td><td>63.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (-19.96%)</td><td>0.25 (+17.32%)</td><td>0.25 <b>(+44.45%)</b></td><td>0.23 <b>(+35.94%)</b></td><td>0.02 <b>(-75.37%)</b></td><td>162.30 <b>(-26.43%)</b></td><td>150.30 <b>(-20.02%)</b></td><td>145.70 <b>(-30.78%)</b></td><td>137.40 <b>(+25.02%)</b></td><td>10.73 <b>(-76.53%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>220.60 (n/a)</td><td>187.92 (n/a)</td><td>210.50 (n/a)</td><td>109.90 (n/a)</td><td>45.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.32 (-5.51%)</td><td>0.26 (-1.13%)</td><td>0.24 (-0.51%)</td><td>0.23 (-1.52%)</td><td>0.04 (-13.23%)</td><td>181.70 (+1.57%)</td><td>160.60 (+0.78%)</td><td>169.70 (+0.53%)</td><td>127.10 (+5.83%)</td><td>22.28 (-5.27%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>178.90 (n/a)</td><td>159.36 (n/a)</td><td>168.80 (n/a)</td><td>120.10 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.33 (+7.10%)</td><td>0.28 (+10.77%)</td><td>0.31 <b>(+27.45%)</b></td><td>0.22 (+1.43%)</td><td>0.05 <b>(+35.04%)</b></td><td>184.50 (-1.39%)</td><td>150.34 (-8.61%)</td><td>131.90 <b>(-21.49%)</b></td><td>124.00 (-6.63%)</td><td>29.76 <b>(+24.83%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>187.10 (n/a)</td><td>164.50 (n/a)</td><td>168.00 (n/a)</td><td>132.80 (n/a)</td><td>23.84 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.32 <b>(-22.95%)</b></td><td>0.29 (-3.93%)</td><td>0.29 (-2.64%)</td><td>0.26 (+11.40%)</td><td>0.03 <b>(-63.20%)</b></td><td>158.80 (-10.23%)</td><td>141.74 (+0.24%)</td><td>139.20 (+2.73%)</td><td>126.80 <b>(+29.79%)</b></td><td>13.59 <b>(-57.54%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>176.90 (n/a)</td><td>141.40 (n/a)</td><td>135.50 (n/a)</td><td>97.70 (n/a)</td><td>32.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.32 (+7.71%)</td><td>0.22 (-10.66%)</td><td>0.19 <b>(-20.08%)</b></td><td>0.17 (-14.13%)</td><td>0.06 <b>(+35.84%)</b></td><td>246.90 (+16.46%)</td><td>194.58 (+15.14%)</td><td>213.80 <b>(+25.10%)</b></td><td>126.40 (-7.20%)</td><td>48.01 <b>(+49.07%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>212.00 (n/a)</td><td>169.00 (n/a)</td><td>170.90 (n/a)</td><td>136.20 (n/a)</td><td>32.21 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 <b>(-27.28%)</b></td><td>0.21 (-9.40%)</td><td>0.23 (-0.89%)</td><td>0.17 (+9.02%)</td><td>0.03 <b>(-52.69%)</b></td><td>243.30 (-8.26%)</td><td>194.44 (+5.49%)</td><td>177.90 (+0.91%)</td><td>170.80 <b>(+37.52%)</b></td><td>31.19 <b>(-41.41%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>265.20 (n/a)</td><td>184.32 (n/a)</td><td>176.30 (n/a)</td><td>124.20 (n/a)</td><td>53.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (-18.12%)</td><td>0.22 (-12.81%)</td><td>0.21 <b>(-22.15%)</b></td><td>0.20 (-1.55%)</td><td>0.02 <b>(-47.92%)</b></td><td>209.70 (+1.55%)</td><td>190.12 (+12.87%)</td><td>199.00 <b>(+28.47%)</b></td><td>170.10 <b>(+22.11%)</b></td><td>18.53 <b>(-37.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>206.50 (n/a)</td><td>168.44 (n/a)</td><td>154.90 (n/a)</td><td>139.30 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.37 <b>(+61.63%)</b></td><td>0.26 <b>(+28.15%)</b></td><td>0.25 (+19.36%)</td><td>0.19 <b>(+22.49%)</b></td><td>0.07 <b>(+127.67%)</b></td><td>220.00 (-18.37%)</td><td>165.80 (-19.64%)</td><td>165.30 (-16.22%)</td><td>109.80 <b>(-38.14%)</b></td><td>39.71 (+8.51%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>269.50 (n/a)</td><td>206.32 (n/a)</td><td>197.30 (n/a)</td><td>177.50 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 <b>(+30.36%)</b></td><td>0.23 (+17.76%)</td><td>0.26 <b>(+30.54%)</b></td><td>0.14 <b>(-23.52%)</b></td><td>0.05 <b>(+514.49%)</b></td><td>291.20 <b>(+30.76%)</b></td><td>187.60 (-10.14%)</td><td>159.30 <b>(-23.41%)</b></td><td>151.50 <b>(-23.29%)</b></td><td>58.65 <b>(+535.47%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>208.78 (n/a)</td><td>208.00 (n/a)</td><td>197.50 (n/a)</td><td>9.23 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (-5.08%)</td><td>0.21 (-3.72%)</td><td>0.21 (-3.01%)</td><td>0.16 (-13.43%)</td><td>0.04 (+1.51%)</td><td>219.90 (+15.49%)</td><td>169.56 (+4.50%)</td><td>169.30 (+3.11%)</td><td>128.80 (+5.40%)</td><td>32.82 <b>(+26.66%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>190.40 (n/a)</td><td>162.26 (n/a)</td><td>164.20 (n/a)</td><td>122.20 (n/a)</td><td>25.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (+5.11%)</td><td>0.21 (+2.64%)</td><td>0.20 (-1.33%)</td><td>0.16 (-2.22%)</td><td>0.04 (+19.09%)</td><td>218.70 (+2.24%)</td><td>174.28 (-1.70%)</td><td>174.10 (+1.34%)</td><td>128.70 (-4.81%)</td><td>34.37 (+16.02%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>213.90 (n/a)</td><td>177.30 (n/a)</td><td>171.80 (n/a)</td><td>135.20 (n/a)</td><td>29.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.29 (+6.57%)</td><td>0.23 (-2.51%)</td><td>0.22 (-14.89%)</td><td>0.17 (+2.13%)</td><td>0.05 (+11.27%)</td><td>208.30 (-2.07%)</td><td>160.26 (+3.02%)</td><td>158.70 (+17.47%)</td><td>122.00 (-6.15%)</td><td>35.44 (+1.53%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>212.70 (n/a)</td><td>155.56 (n/a)</td><td>135.10 (n/a)</td><td>130.00 (n/a)</td><td>34.90 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.27 (+4.02%)</td><td>0.22 (-3.97%)</td><td>0.22 (-4.13%)</td><td>0.17 (+0.06%)</td><td>0.04 (+5.90%)</td><td>205.70 (-0.10%)</td><td>162.82 (+4.25%)</td><td>156.60 (+4.26%)</td><td>127.60 (-3.84%)</td><td>29.25 (+0.16%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>205.90 (n/a)</td><td>156.18 (n/a)</td><td>150.20 (n/a)</td><td>132.70 (n/a)</td><td>29.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.23 (-19.60%)</td><td>0.21 (-12.43%)</td><td>0.22 (-5.89%)</td><td>0.16 <b>(-21.16%)</b></td><td>0.03 (-16.31%)</td><td>219.10 <b>(+26.79%)</b></td><td>172.12 (+14.40%)</td><td>159.00 (+6.28%)</td><td>148.50 <b>(+24.37%)</b></td><td>28.96 <b>(+30.90%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>172.80 (n/a)</td><td>150.46 (n/a)</td><td>149.60 (n/a)</td><td>119.40 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.24 (-5.11%)</td><td>0.18 (-7.63%)</td><td>0.18 (-9.70%)</td><td>0.13 (-16.83%)</td><td>0.04 (+6.19%)</td><td>266.00 <b>(+20.25%)</b></td><td>198.38 (+9.55%)</td><td>190.70 (+10.74%)</td><td>147.70 (+5.35%)</td><td>47.37 <b>(+30.56%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>221.20 (n/a)</td><td>181.08 (n/a)</td><td>172.20 (n/a)</td><td>140.20 (n/a)</td><td>36.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (+5.18%)</td><td>0.18 (+0.77%)</td><td>0.18 (-2.85%)</td><td>0.16 (+11.96%)</td><td>0.02 (-1.87%)</td><td>218.00 (-10.69%)</td><td>194.12 (-1.05%)</td><td>192.70 (+2.94%)</td><td>162.20 (-4.92%)</td><td>23.29 (-17.74%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>244.10 (n/a)</td><td>196.18 (n/a)</td><td>187.20 (n/a)</td><td>170.60 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.26 (+2.70%)</td><td>0.20 (+8.71%)</td><td>0.22 <b>(+27.93%)</b></td><td>0.11 <b>(-32.42%)</b></td><td>0.06 <b>(+58.51%)</b></td><td>310.00 <b>(+47.97%)</b></td><td>187.16 (-1.51%)</td><td>160.30 <b>(-21.84%)</b></td><td>132.00 (-2.58%)</td><td>72.92 <b>(+135.59%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>209.50 (n/a)</td><td>190.02 (n/a)</td><td>205.10 (n/a)</td><td>135.50 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.98 (-7.66%)</td><td>0.80 (+0.90%)</td><td>0.79 (+7.44%)</td><td>0.66 (+7.16%)</td><td>0.12 <b>(-30.78%)</b></td><td>199.60 (-6.69%)</td><td>167.14 (-2.54%)</td><td>166.10 (-6.89%)</td><td>134.40 (+8.30%)</td><td>23.80 <b>(-29.23%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.06 (n/a)</td><td>0.79 (n/a)</td><td>0.73 (n/a)</td><td>0.61 (n/a)</td><td>0.17 (n/a)</td><td>213.90 (n/a)</td><td>171.50 (n/a)</td><td>178.40 (n/a)</td><td>124.10 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.94 <b>(-27.99%)</b></td><td>0.80 (+3.18%)</td><td>0.81 <b>(+20.61%)</b></td><td>0.70 <b>(+65.01%)</b></td><td>0.09 <b>(-74.12%)</b></td><td>186.00 <b>(-39.39%)</b></td><td>164.76 (-15.00%)</td><td>162.80 (-17.11%)</td><td>139.80 <b>(+38.83%)</b></td><td>17.20 <b>(-77.94%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.30 (n/a)</td><td>0.78 (n/a)</td><td>0.67 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>306.90 (n/a)</td><td>193.84 (n/a)</td><td>196.40 (n/a)</td><td>100.70 (n/a)</td><td>77.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.05 (+15.34%)</td><td>0.92 <b>(+20.61%)</b></td><td>0.96 <b>(+31.68%)</b></td><td>0.69 (+12.48%)</td><td>0.13 (+7.17%)</td><td>188.90 (-11.11%)</td><td>145.68 (-17.20%)</td><td>137.00 <b>(-24.06%)</b></td><td>125.30 (-13.29%)</td><td>24.87 (-12.66%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.91 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.62 (n/a)</td><td>0.12 (n/a)</td><td>212.50 (n/a)</td><td>175.94 (n/a)</td><td>180.40 (n/a)</td><td>144.50 (n/a)</td><td>28.48 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+4.49%)</td><td>0.03 (-8.15%)</td><td>0.02 (-11.53%)</td><td>0.02 (-11.03%)</td><td>0.01 <b>(+62.28%)</b></td><td>189.20 (+12.42%)</td><td>162.12 (+10.84%)</td><td>169.30 (+13.02%)</td><td>118.80 (-4.35%)</td><td>28.25 <b>(+74.41%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>168.30 (n/a)</td><td>146.26 (n/a)</td><td>149.80 (n/a)</td><td>124.20 (n/a)</td><td>16.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.02 <b>(-23.59%)</b></td><td>0.02 <b>(-20.50%)</b></td><td>0.02 <b>(-21.68%)</b></td><td>0.02 (-12.21%)</td><td>0.00 <b>(-53.59%)</b></td><td>199.80 (+13.91%)</td><td>187.94 <b>(+24.38%)</b></td><td>193.70 <b>(+27.69%)</b></td><td>163.90 <b>(+30.91%)</b></td><td>14.79 <b>(-31.31%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.40 (n/a)</td><td>151.10 (n/a)</td><td>151.70 (n/a)</td><td>125.20 (n/a)</td><td>21.53 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 <b>(-21.78%)</b></td><td>0.02 (-18.70%)</td><td>0.02 <b>(-23.61%)</b></td><td>0.02 (-10.28%)</td><td>0.00 <b>(-44.03%)</b></td><td>201.40 (+11.46%)</td><td>181.50 <b>(+21.57%)</b></td><td>190.90 <b>(+30.93%)</b></td><td>157.80 <b>(+27.88%)</b></td><td>19.44 <b>(-20.52%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.70 (n/a)</td><td>149.30 (n/a)</td><td>145.80 (n/a)</td><td>123.40 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>15.86 (+0.61%)</td><td>13.01 (-2.32%)</td><td>12.12 (-3.41%)</td><td>11.81 (+4.59%)</td><td>1.68 (-9.04%)</td><td>177.60 (-4.41%)</td><td>163.18 (+2.05%)</td><td>173.10 (+3.53%)</td><td>132.30 (-0.60%)</td><td>18.72 (-13.21%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>15.76 (n/a)</td><td>13.32 (n/a)</td><td>12.55 (n/a)</td><td>11.29 (n/a)</td><td>1.85 (n/a)</td><td>185.80 (n/a)</td><td>159.90 (n/a)</td><td>167.20 (n/a)</td><td>133.10 (n/a)</td><td>21.57 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.81 (-17.91%)</td><td>0.73 (-12.38%)</td><td>0.77 (-7.68%)</td><td>0.60 (+4.81%)</td><td>0.08 <b>(-49.09%)</b></td><td>220.60 (-4.58%)</td><td>183.02 (+11.19%)</td><td>171.60 (+8.33%)</td><td>162.80 <b>(+21.86%)</b></td><td>23.00 <b>(-41.29%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.99 (n/a)</td><td>0.83 (n/a)</td><td>0.83 (n/a)</td><td>0.57 (n/a)</td><td>0.16 (n/a)</td><td>231.20 (n/a)</td><td>164.60 (n/a)</td><td>158.40 (n/a)</td><td>133.60 (n/a)</td><td>39.17 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.77 <b>(-26.71%)</b></td><td>0.75 (-12.89%)</td><td>0.75 (-9.13%)</td><td>0.71 (+10.92%)</td><td>0.02 <b>(-88.25%)</b></td><td>185.70 (-9.81%)</td><td>177.08 (+10.83%)</td><td>175.90 (+10.01%)</td><td>172.00 <b>(+36.40%)</b></td><td>5.13 <b>(-84.89%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.05 (n/a)</td><td>0.86 (n/a)</td><td>0.83 (n/a)</td><td>0.64 (n/a)</td><td>0.18 (n/a)</td><td>205.90 (n/a)</td><td>159.78 (n/a)</td><td>159.90 (n/a)</td><td>126.10 (n/a)</td><td>33.95 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.15 (+14.33%)</td><td>0.84 (+5.55%)</td><td>0.74 (-4.23%)</td><td>0.65 (-5.90%)</td><td>0.21 <b>(+61.39%)</b></td><td>204.30 (+6.30%)</td><td>163.36 (-2.84%)</td><td>179.00 (+4.43%)</td><td>114.50 (-12.53%)</td><td>35.95 <b>(+49.64%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.01 (n/a)</td><td>0.80 (n/a)</td><td>0.77 (n/a)</td><td>0.69 (n/a)</td><td>0.13 (n/a)</td><td>192.20 (n/a)</td><td>168.14 (n/a)</td><td>171.40 (n/a)</td><td>130.90 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.84 <b>(-24.91%)</b></td><td>0.75 (-13.86%)</td><td>0.77 (-5.28%)</td><td>0.58 <b>(-23.93%)</b></td><td>0.11 <b>(-27.78%)</b></td><td>229.10 <b>(+31.44%)</b></td><td>178.74 (+15.94%)</td><td>171.90 (+5.59%)</td><td>157.50 <b>(+33.14%)</b></td><td>29.23 <b>(+29.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.12 (n/a)</td><td>0.87 (n/a)</td><td>0.81 (n/a)</td><td>0.76 (n/a)</td><td>0.15 (n/a)</td><td>174.30 (n/a)</td><td>154.16 (n/a)</td><td>162.80 (n/a)</td><td>118.30 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.09 (+2.53%)</td><td>0.80 (-11.06%)</td><td>0.73 (-14.47%)</td><td>0.60 <b>(-21.93%)</b></td><td>0.21 <b>(+61.51%)</b></td><td>220.70 <b>(+28.09%)</b></td><td>173.80 (+16.63%)</td><td>181.80 (+16.91%)</td><td>121.40 (-2.41%)</td><td>42.85 <b>(+104.03%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.06 (n/a)</td><td>0.90 (n/a)</td><td>0.85 (n/a)</td><td>0.77 (n/a)</td><td>0.13 (n/a)</td><td>172.30 (n/a)</td><td>149.02 (n/a)</td><td>155.50 (n/a)</td><td>124.40 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (-11.16%)</td><td>0.02 (-10.26%)</td><td>0.02 (-19.12%)</td><td>0.02 (-10.69%)</td><td>0.00 <b>(-22.86%)</b></td><td>213.40 (+11.96%)</td><td>170.32 (+10.41%)</td><td>167.70 <b>(+23.58%)</b></td><td>143.00 (+12.60%)</td><td>29.68 (-6.78%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>154.26 (n/a)</td><td>135.70 (n/a)</td><td>127.00 (n/a)</td><td>31.84 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.03 (+0.78%)</td><td>0.03 (-2.57%)</td><td>0.02 <b>(-28.69%)</b></td><td>0.02 <b>(+37.57%)</b></td><td>0.01 <b>(-21.22%)</b></td><td>197.90 <b>(-27.32%)</b></td><td>161.76 (-2.38%)</td><td>180.10 <b>(+40.16%)</b></td><td>122.80 (-0.73%)</td><td>35.60 <b>(-44.11%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>272.30 (n/a)</td><td>165.70 (n/a)</td><td>128.50 (n/a)</td><td>123.70 (n/a)</td><td>63.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.00 (+2.38%)</td><td>0.00 (+3.92%)</td><td>0.00 (+4.88%)</td><td>0.00 (+7.89%)</td><td>0.00 <b>(-45.57%)</b></td><td>1006.46 (-6.81%)</td><td>971.04 (-3.05%)</td><td>961.93 (-3.31%)</td><td>956.32 (-1.20%)</td><td>20.29 <b>(-55.80%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1080.02 (n/a)</td><td>1001.57 (n/a)</td><td>994.86 (n/a)</td><td>967.89 (n/a)</td><td>45.90 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.01 (+2.44%)</td><td>0.01 (+2.54%)</td><td>0.01 (+3.85%)</td><td>0.01 (-1.30%)</td><td>0.00 <b>(+61.91%)</b></td><td>1083.96 (+1.50%)</td><td>1018.22 (-2.26%)</td><td>1009.16 (-3.47%)</td><td>979.74 (-2.33%)</td><td>40.81 <b>(+70.27%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1067.97 (n/a)</td><td>1041.75 (n/a)</td><td>1045.39 (n/a)</td><td>1003.13 (n/a)</td><td>23.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.97 (+1.72%)</td><td>0.96 (+1.96%)</td><td>0.96 (+1.36%)</td><td>0.96 (+2.87%)</td><td>0.01 <b>(-39.96%)</b></td><td>2186.11 (-2.80%)</td><td>2175.78 (-1.93%)</td><td>2184.75 (-1.35%)</td><td>2153.64 (-1.69%)</td><td>14.49 <b>(-42.71%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.93 (n/a)</td><td>0.01 (n/a)</td><td>2249.01 (n/a)</td><td>2218.57 (n/a)</td><td>2214.60 (n/a)</td><td>2190.76 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>5.34 (-4.24%)</td><td>5.00 (+5.97%)</td><td>4.95 (+5.20%)</td><td>4.70 <b>(+26.90%)</b></td><td>0.27 <b>(-60.87%)</b></td><td>223.20 <b>(-21.21%)</b></td><td>210.38 (-7.16%)</td><td>212.00 (-4.93%)</td><td>196.30 (+4.47%)</td><td>11.40 <b>(-68.30%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>5.58 (n/a)</td><td>4.72 (n/a)</td><td>4.70 (n/a)</td><td>3.70 (n/a)</td><td>0.70 (n/a)</td><td>283.30 (n/a)</td><td>226.60 (n/a)</td><td>223.00 (n/a)</td><td>187.90 (n/a)</td><td>35.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>5.19 (-12.74%)</td><td>4.81 (-5.10%)</td><td>4.86 (-5.24%)</td><td>4.27 <b>(+20.53%)</b></td><td>0.34 <b>(-64.75%)</b></td><td>245.60 (-17.03%)</td><td>218.82 (+2.20%)</td><td>215.70 (+5.53%)</td><td>201.90 (+14.65%)</td><td>16.32 <b>(-66.41%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>5.95 (n/a)</td><td>5.07 (n/a)</td><td>5.13 (n/a)</td><td>3.54 (n/a)</td><td>0.97 (n/a)</td><td>296.00 (n/a)</td><td>214.10 (n/a)</td><td>204.40 (n/a)</td><td>176.10 (n/a)</td><td>48.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>6.12 (+5.99%)</td><td>5.17 (+3.48%)</td><td>5.43 (+5.92%)</td><td>4.12 (-3.46%)</td><td>0.80 (+12.53%)</td><td>254.70 (+3.58%)</td><td>206.86 (-3.03%)</td><td>193.00 (-5.58%)</td><td>171.40 (-5.67%)</td><td>33.45 (+8.58%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>5.77 (n/a)</td><td>5.00 (n/a)</td><td>5.13 (n/a)</td><td>4.26 (n/a)</td><td>0.71 (n/a)</td><td>245.90 (n/a)</td><td>213.32 (n/a)</td><td>204.40 (n/a)</td><td>181.70 (n/a)</td><td>30.81 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>6.49 (+3.17%)</td><td>5.43 (+0.25%)</td><td>5.58 (+3.84%)</td><td>4.38 (+1.75%)</td><td>0.90 (+7.86%)</td><td>239.60 (-1.72%)</td><td>197.60 (+0.01%)</td><td>187.90 (-3.69%)</td><td>161.60 (-3.12%)</td><td>33.49 (+5.51%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>6.29 (n/a)</td><td>5.41 (n/a)</td><td>5.37 (n/a)</td><td>4.30 (n/a)</td><td>0.83 (n/a)</td><td>243.80 (n/a)</td><td>197.58 (n/a)</td><td>195.10 (n/a)</td><td>166.80 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.23 (+8.53%)</td><td>8.58 (+10.02%)</td><td>8.63 (+11.62%)</td><td>7.69 (+7.87%)</td><td>0.63 (+17.42%)</td><td>272.60 (-7.31%)</td><td>245.58 (-9.04%)</td><td>243.00 (-10.40%)</td><td>227.20 (-7.83%)</td><td>18.44 (+0.03%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>8.51 (n/a)</td><td>7.80 (n/a)</td><td>7.73 (n/a)</td><td>7.13 (n/a)</td><td>0.53 (n/a)</td><td>294.10 (n/a)</td><td>269.98 (n/a)</td><td>271.20 (n/a)</td><td>246.50 (n/a)</td><td>18.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.33 (-3.93%)</td><td>8.16 (+1.98%)</td><td>7.93 (+1.86%)</td><td>7.47 (+4.09%)</td><td>0.73 <b>(-25.83%)</b></td><td>280.90 (-3.93%)</td><td>258.44 (-2.41%)</td><td>264.30 (-1.86%)</td><td>224.90 (+4.12%)</td><td>21.97 <b>(-24.62%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>9.71 (n/a)</td><td>8.01 (n/a)</td><td>7.79 (n/a)</td><td>7.17 (n/a)</td><td>0.99 (n/a)</td><td>292.40 (n/a)</td><td>264.82 (n/a)</td><td>269.30 (n/a)</td><td>216.00 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.58 (+14.58%)</td><td>8.38 (+9.94%)</td><td>8.03 (+10.79%)</td><td>7.23 (+2.36%)</td><td>1.03 <b>(+69.28%)</b></td><td>289.90 (-2.29%)</td><td>253.22 (-8.41%)</td><td>261.20 (-9.74%)</td><td>218.90 (-12.72%)</td><td>30.58 <b>(+42.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>8.36 (n/a)</td><td>7.62 (n/a)</td><td>7.25 (n/a)</td><td>7.07 (n/a)</td><td>0.61 (n/a)</td><td>296.70 (n/a)</td><td>276.46 (n/a)</td><td>289.40 (n/a)</td><td>250.80 (n/a)</td><td>21.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.53 (+3.48%)</td><td>8.51 (+0.13%)</td><td>8.58 (+4.11%)</td><td>7.31 (-8.32%)</td><td>0.89 <b>(+48.18%)</b></td><td>287.00 (+9.08%)</td><td>248.60 (+0.38%)</td><td>244.40 (-3.93%)</td><td>220.00 (-3.38%)</td><td>26.82 <b>(+56.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>9.21 (n/a)</td><td>8.50 (n/a)</td><td>8.24 (n/a)</td><td>7.97 (n/a)</td><td>0.60 (n/a)</td><td>263.10 (n/a)</td><td>247.66 (n/a)</td><td>254.40 (n/a)</td><td>227.70 (n/a)</td><td>17.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.50 (-6.10%)</td><td>8.26 (-1.76%)</td><td>7.95 (-1.82%)</td><td>7.56 (+18.21%)</td><td>0.82 <b>(-47.38%)</b></td><td>277.40 (-15.40%)</td><td>255.80 (-0.34%)</td><td>263.80 (+1.85%)</td><td>220.80 (+6.51%)</td><td>24.12 <b>(-51.21%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>10.12 (n/a)</td><td>8.41 (n/a)</td><td>8.10 (n/a)</td><td>6.40 (n/a)</td><td>1.56 (n/a)</td><td>327.90 (n/a)</td><td>256.68 (n/a)</td><td>259.00 (n/a)</td><td>207.30 (n/a)</td><td>49.45 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>9.80 (-5.29%)</td><td>8.92 (+2.02%)</td><td>8.91 (-2.15%)</td><td>8.06 (+10.35%)</td><td>0.62 <b>(-51.71%)</b></td><td>260.10 (-9.40%)</td><td>235.94 (-3.33%)</td><td>235.30 (+2.17%)</td><td>214.00 (+5.57%)</td><td>16.45 <b>(-54.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>10.34 (n/a)</td><td>8.75 (n/a)</td><td>9.11 (n/a)</td><td>7.31 (n/a)</td><td>1.28 (n/a)</td><td>287.10 (n/a)</td><td>244.06 (n/a)</td><td>230.30 (n/a)</td><td>202.70 (n/a)</td><td>36.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>12.40 (+4.35%)</td><td>11.16 (-3.24%)</td><td>11.11 (-3.00%)</td><td>10.49 (-6.93%)</td><td>0.75 <b>(+167.86%)</b></td><td>399.80 (+7.47%)</td><td>377.16 (+3.66%)</td><td>377.50 (+3.11%)</td><td>338.10 (-4.19%)</td><td>24.04 <b>(+174.42%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>11.89 (n/a)</td><td>11.53 (n/a)</td><td>11.46 (n/a)</td><td>11.27 (n/a)</td><td>0.28 (n/a)</td><td>372.00 (n/a)</td><td>363.84 (n/a)</td><td>366.10 (n/a)</td><td>352.90 (n/a)</td><td>8.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>12.59 (-4.89%)</td><td>11.98 (+2.16%)</td><td>11.90 (+2.89%)</td><td>11.58 (+16.61%)</td><td>0.39 <b>(-71.54%)</b></td><td>362.20 (-14.25%)</td><td>350.30 (-3.11%)</td><td>352.40 (-2.79%)</td><td>333.20 (+5.14%)</td><td>11.12 <b>(-74.11%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>13.23 (n/a)</td><td>11.73 (n/a)</td><td>11.57 (n/a)</td><td>9.93 (n/a)</td><td>1.36 (n/a)</td><td>422.40 (n/a)</td><td>361.54 (n/a)</td><td>362.50 (n/a)</td><td>316.90 (n/a)</td><td>42.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>12.44 (-4.30%)</td><td>11.66 (+1.86%)</td><td>11.83 (+2.43%)</td><td>10.77 (+6.02%)</td><td>0.77 <b>(-31.36%)</b></td><td>389.30 (-5.67%)</td><td>361.04 (-2.23%)</td><td>354.60 (-2.39%)</td><td>337.10 (+4.49%)</td><td>24.14 <b>(-32.54%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>13.00 (n/a)</td><td>11.45 (n/a)</td><td>11.55 (n/a)</td><td>10.16 (n/a)</td><td>1.12 (n/a)</td><td>412.70 (n/a)</td><td>369.26 (n/a)</td><td>363.30 (n/a)</td><td>322.60 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>13.64 (-3.01%)</td><td>12.99 (+1.57%)</td><td>13.13 (+2.57%)</td><td>12.35 (+17.21%)</td><td>0.59 <b>(-57.42%)</b></td><td>339.70 (-14.69%)</td><td>323.44 (-2.40%)</td><td>319.40 (-2.53%)</td><td>307.60 (+3.12%)</td><td>14.78 <b>(-62.78%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>14.06 (n/a)</td><td>12.79 (n/a)</td><td>12.80 (n/a)</td><td>10.53 (n/a)</td><td>1.39 (n/a)</td><td>398.20 (n/a)</td><td>331.40 (n/a)</td><td>327.70 (n/a)</td><td>298.30 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>12.77 <b>(-22.80%)</b></td><td>12.15 (-4.06%)</td><td>12.34 (+3.09%)</td><td>11.33 (+4.57%)</td><td>0.56 <b>(-76.09%)</b></td><td>370.30 (-4.36%)</td><td>345.86 (+1.92%)</td><td>339.90 (-3.00%)</td><td>328.30 <b>(+29.51%)</b></td><td>16.35 <b>(-70.23%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>16.55 (n/a)</td><td>12.66 (n/a)</td><td>11.97 (n/a)</td><td>10.83 (n/a)</td><td>2.35 (n/a)</td><td>387.20 (n/a)</td><td>339.34 (n/a)</td><td>350.40 (n/a)</td><td>253.50 (n/a)</td><td>54.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>14.20 (-8.90%)</td><td>12.95 (+8.58%)</td><td>13.07 (+14.47%)</td><td>12.10 <b>(+21.17%)</b></td><td>0.87 <b>(-60.77%)</b></td><td>346.70 (-17.47%)</td><td>325.12 (-9.80%)</td><td>320.80 (-12.66%)</td><td>295.50 (+9.77%)</td><td>21.42 <b>(-63.56%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>15.58 (n/a)</td><td>11.92 (n/a)</td><td>11.42 (n/a)</td><td>9.98 (n/a)</td><td>2.21 (n/a)</td><td>420.10 (n/a)</td><td>360.44 (n/a)</td><td>367.30 (n/a)</td><td>269.20 (n/a)</td><td>58.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>15.12 (+0.49%)</td><td>13.37 (+2.82%)</td><td>13.19 (-1.59%)</td><td>11.79 <b>(+23.04%)</b></td><td>1.31 <b>(-38.98%)</b></td><td>355.70 (-18.72%)</td><td>316.10 (-4.46%)</td><td>318.00 (+1.60%)</td><td>277.40 (-0.50%)</td><td>30.74 <b>(-51.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>15.04 (n/a)</td><td>13.00 (n/a)</td><td>13.40 (n/a)</td><td>9.58 (n/a)</td><td>2.15 (n/a)</td><td>437.60 (n/a)</td><td>330.84 (n/a)</td><td>313.00 (n/a)</td><td>278.80 (n/a)</td><td>63.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>11.93 <b>(-20.94%)</b></td><td>10.35 <b>(-20.56%)</b></td><td>9.71 <b>(-26.76%)</b></td><td>9.49 (+1.12%)</td><td>1.11 <b>(-51.08%)</b></td><td>442.20 (-1.10%)</td><td>408.80 <b>(+23.36%)</b></td><td>432.00 <b>(+36.54%)</b></td><td>351.60 <b>(+26.47%)</b></td><td>41.83 <b>(-38.82%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>15.09 (n/a)</td><td>13.03 (n/a)</td><td>13.26 (n/a)</td><td>9.38 (n/a)</td><td>2.28 (n/a)</td><td>447.10 (n/a)</td><td>331.38 (n/a)</td><td>316.40 (n/a)</td><td>278.00 (n/a)</td><td>68.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.40 (+12.64%)</td><td>2.73 (+5.50%)</td><td>2.61 (+2.55%)</td><td>2.50 (+11.19%)</td><td>0.37 <b>(+32.21%)</b></td><td>210.00 (-10.06%)</td><td>194.28 (-4.87%)</td><td>200.70 (-2.48%)</td><td>154.40 (-11.21%)</td><td>22.67 (+4.21%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.02 (n/a)</td><td>2.59 (n/a)</td><td>2.55 (n/a)</td><td>2.25 (n/a)</td><td>0.28 (n/a)</td><td>233.50 (n/a)</td><td>204.22 (n/a)</td><td>205.80 (n/a)</td><td>173.90 (n/a)</td><td>21.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>5.19 (-11.40%)</td><td>4.49 (-3.87%)</td><td>4.52 (-1.51%)</td><td>3.92 (+2.60%)</td><td>0.48 <b>(-38.16%)</b></td><td>267.60 (-2.55%)</td><td>235.54 (+2.79%)</td><td>232.10 (+1.53%)</td><td>202.20 (+12.90%)</td><td>24.73 <b>(-31.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>5.85 (n/a)</td><td>4.67 (n/a)</td><td>4.59 (n/a)</td><td>3.82 (n/a)</td><td>0.78 (n/a)</td><td>274.60 (n/a)</td><td>229.14 (n/a)</td><td>228.60 (n/a)</td><td>179.10 (n/a)</td><td>36.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>7.45 (-16.90%)</td><td>7.12 (-10.16%)</td><td>7.17 (-13.78%)</td><td>6.45 (-4.33%)</td><td>0.40 <b>(-61.14%)</b></td><td>325.20 (+4.53%)</td><td>295.22 (+10.03%)</td><td>292.30 (+15.99%)</td><td>281.60 <b>(+20.34%)</b></td><td>17.68 <b>(-51.41%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>8.96 (n/a)</td><td>7.93 (n/a)</td><td>8.32 (n/a)</td><td>6.74 (n/a)</td><td>1.04 (n/a)</td><td>311.10 (n/a)</td><td>268.32 (n/a)</td><td>252.00 (n/a)</td><td>234.00 (n/a)</td><td>36.39 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>3.61 (+18.14%)</td><td>2.86 (+8.92%)</td><td>2.72 (+5.89%)</td><td>2.36 (+2.43%)</td><td>0.47 <b>(+41.25%)</b></td><td>222.50 (-2.37%)</td><td>186.96 (-7.53%)</td><td>192.50 (-5.54%)</td><td>145.10 (-15.34%)</td><td>28.04 (+12.94%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>3.06 (n/a)</td><td>2.63 (n/a)</td><td>2.57 (n/a)</td><td>2.30 (n/a)</td><td>0.33 (n/a)</td><td>227.90 (n/a)</td><td>202.18 (n/a)</td><td>203.80 (n/a)</td><td>171.40 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.26 (-8.25%)</td><td>0.20 (+2.37%)</td><td>0.18 (-12.77%)</td><td>0.16 <b>(+35.01%)</b></td><td>0.04 <b>(-31.70%)</b></td><td>207.90 <b>(-25.91%)</b></td><td>170.70 (-7.62%)</td><td>186.40 (+14.64%)</td><td>125.00 (+8.98%)</td><td>34.42 <b>(-46.15%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>280.60 (n/a)</td><td>184.78 (n/a)</td><td>162.60 (n/a)</td><td>114.70 (n/a)</td><td>63.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.21 (-19.58%)</td><td>0.18 (+2.21%)</td><td>0.17 (+5.65%)</td><td>0.15 (+8.04%)</td><td>0.02 <b>(-47.06%)</b></td><td>214.50 (-7.46%)</td><td>182.14 (-4.95%)</td><td>189.30 (-5.30%)</td><td>156.90 <b>(+24.33%)</b></td><td>24.61 <b>(-37.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>231.80 (n/a)</td><td>191.62 (n/a)</td><td>199.90 (n/a)</td><td>126.20 (n/a)</td><td>39.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.46 (+6.28%)</td><td>0.37 (+13.74%)</td><td>0.33 (+10.52%)</td><td>0.32 (+17.58%)</td><td>0.06 (-5.43%)</td><td>203.70 (-14.98%)</td><td>179.46 (-12.75%)</td><td>196.40 (-9.53%)</td><td>141.80 (-5.91%)</td><td>27.66 <b>(-23.29%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>239.60 (n/a)</td><td>205.68 (n/a)</td><td>217.10 (n/a)</td><td>150.70 (n/a)</td><td>36.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.48 (+17.48%)</td><td>0.38 (+10.42%)</td><td>0.34 (+2.66%)</td><td>0.33 (+16.65%)</td><td>0.06 <b>(+32.73%)</b></td><td>195.70 (-14.28%)</td><td>178.14 (-9.04%)</td><td>191.40 (-2.60%)</td><td>135.40 (-14.90%)</td><td>25.51 (-2.74%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>228.30 (n/a)</td><td>195.84 (n/a)</td><td>196.50 (n/a)</td><td>159.10 (n/a)</td><td>26.23 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.64 <b>(+31.76%)</b></td><td>0.39 (+8.70%)</td><td>0.34 (+3.73%)</td><td>0.31 (-3.82%)</td><td>0.14 <b>(+97.61%)</b></td><td>214.20 (+3.98%)</td><td>180.54 (-3.51%)</td><td>192.90 (-3.60%)</td><td>102.70 <b>(-24.09%)</b></td><td>44.61 <b>(+51.47%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.48 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>206.00 (n/a)</td><td>187.10 (n/a)</td><td>200.10 (n/a)</td><td>135.30 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.09 <b>(+23.91%)</b></td><td>0.77 (+3.60%)</td><td>0.72 (-4.92%)</td><td>0.36 <b>(-41.40%)</b></td><td>0.31 <b>(+181.84%)</b></td><td>359.80 <b>(+70.68%)</b></td><td>199.82 (+11.51%)</td><td>180.90 (+5.17%)</td><td>119.80 (-19.33%)</td><td>98.11 <b>(+267.09%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.88 (n/a)</td><td>0.74 (n/a)</td><td>0.76 (n/a)</td><td>0.62 (n/a)</td><td>0.11 (n/a)</td><td>210.80 (n/a)</td><td>179.20 (n/a)</td><td>172.00 (n/a)</td><td>148.50 (n/a)</td><td>26.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.08 <b>(+35.35%)</b></td><td>0.78 (+9.14%)</td><td>0.71 (-0.31%)</td><td>0.63 (+0.94%)</td><td>0.19 <b>(+154.57%)</b></td><td>209.10 (-0.95%)</td><td>173.98 (-5.49%)</td><td>185.10 (+0.33%)</td><td>121.10 <b>(-26.11%)</b></td><td>35.77 <b>(+86.65%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.71 (n/a)</td><td>0.62 (n/a)</td><td>0.07 (n/a)</td><td>211.10 (n/a)</td><td>184.08 (n/a)</td><td>184.50 (n/a)</td><td>163.90 (n/a)</td><td>19.16 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>1.09 <b>(-23.06%)</b></td><td>0.74 (-2.31%)</td><td>0.65 (+9.34%)</td><td>0.57 (+4.36%)</td><td>0.21 <b>(-43.03%)</b></td><td>231.40 (-4.18%)</td><td>187.84 (-4.87%)</td><td>202.60 (-8.53%)</td><td>119.80 <b>(+30.08%)</b></td><td>44.22 <b>(-26.98%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>1.42 (n/a)</td><td>0.75 (n/a)</td><td>0.59 (n/a)</td><td>0.54 (n/a)</td><td>0.38 (n/a)</td><td>241.50 (n/a)</td><td>197.46 (n/a)</td><td>221.50 (n/a)</td><td>92.10 (n/a)</td><td>60.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.90 <b>(+39.16%)</b></td><td>0.67 (+7.33%)</td><td>0.62 (-3.27%)</td><td>0.57 (-3.62%)</td><td>0.14 <b>(+405.62%)</b></td><td>229.70 (+3.75%)</td><td>201.44 (-4.28%)</td><td>211.70 (+3.37%)</td><td>145.10 <b>(-28.17%)</b></td><td>34.83 <b>(+274.18%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.65 (n/a)</td><td>0.62 (n/a)</td><td>0.64 (n/a)</td><td>0.59 (n/a)</td><td>0.03 (n/a)</td><td>221.40 (n/a)</td><td>210.44 (n/a)</td><td>204.80 (n/a)</td><td>202.00 (n/a)</td><td>9.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:12</td><td>0.13 (+5.07%)</td><td>0.10 (-6.08%)</td><td>0.10 (-7.88%)</td><td>0.09 (-9.43%)</td><td>0.01 <b>(+69.28%)</b></td><td>189.20 (+10.39%)</td><td>163.76 (+7.58%)</td><td>165.40 (+8.53%)</td><td>130.50 (-4.81%)</td><td>22.14 <b>(+74.25%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>171.40 (n/a)</td><td>152.22 (n/a)</td><td>152.40 (n/a)</td><td>137.10 (n/a)</td><td>12.71 (n/a)</td>
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
