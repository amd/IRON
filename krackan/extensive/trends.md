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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (+5.98%)</td><td>0.04 (-12.83%)</td><td>0.04 <b>(-24.07%)</b></td><td>0.03 (-1.69%)</td><td>0.01 <b>(+27.73%)</b></td><td>177.10 (+1.72%)</td><td>161.46 (+15.49%)</td><td>173.30 <b>(+31.69%)</b></td><td>122.00 (-5.65%)</td><td>23.08 (+19.98%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>174.10 (n/a)</td><td>139.80 (n/a)</td><td>131.60 (n/a)</td><td>129.30 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (+3.52%)</td><td>0.04 (+2.86%)</td><td>0.04 (-3.35%)</td><td>0.03 (+0.94%)</td><td>0.01 (-3.78%)</td><td>196.80 (-0.91%)</td><td>148.36 (-3.01%)</td><td>145.40 (+3.49%)</td><td>122.90 (-3.38%)</td><td>28.92 (-4.82%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>152.96 (n/a)</td><td>140.50 (n/a)</td><td>127.20 (n/a)</td><td>30.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (+17.31%)</td><td>0.04 (+4.77%)</td><td>0.04 (+1.17%)</td><td>0.03 (-1.55%)</td><td>0.01 <b>(+49.80%)</b></td><td>212.10 (+1.58%)</td><td>165.34 (-2.43%)</td><td>173.20 (-1.14%)</td><td>111.50 (-14.76%)</td><td>37.60 <b>(+27.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>169.46 (n/a)</td><td>175.20 (n/a)</td><td>130.80 (n/a)</td><td>29.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (-15.56%)</td><td>0.04 (-11.24%)</td><td>0.04 (-17.00%)</td><td>0.03 (+3.11%)</td><td>0.00 <b>(-59.12%)</b></td><td>182.90 (-3.02%)</td><td>162.80 (+10.19%)</td><td>158.80 <b>(+20.49%)</b></td><td>146.30 (+18.46%)</td><td>13.59 <b>(-52.49%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>147.74 (n/a)</td><td>131.80 (n/a)</td><td>123.50 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 <b>(+29.39%)</b></td><td>0.03 (+3.66%)</td><td>0.03 (-10.93%)</td><td>0.03 (+10.88%)</td><td>0.01 <b>(+81.75%)</b></td><td>220.90 (-9.80%)</td><td>187.52 (-1.16%)</td><td>202.80 (+12.23%)</td><td>120.90 <b>(-22.70%)</b></td><td>38.97 (+17.39%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.90 (n/a)</td><td>189.72 (n/a)</td><td>180.70 (n/a)</td><td>156.40 (n/a)</td><td>33.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 <b>(-24.57%)</b></td><td>0.04 (-18.70%)</td><td>0.03 <b>(-26.45%)</b></td><td>0.03 (+14.11%)</td><td>0.01 <b>(-55.92%)</b></td><td>195.60 (-12.37%)</td><td>170.46 (+16.77%)</td><td>179.30 <b>(+36.04%)</b></td><td>137.50 <b>(+32.59%)</b></td><td>22.66 <b>(-51.19%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.20 (n/a)</td><td>145.98 (n/a)</td><td>131.80 (n/a)</td><td>103.70 (n/a)</td><td>46.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (+12.28%)</td><td>0.04 (+10.29%)</td><td>0.04 (+10.09%)</td><td>0.03 (+0.64%)</td><td>0.01 <b>(+42.75%)</b></td><td>209.50 (-0.62%)</td><td>165.66 (-8.06%)</td><td>152.80 (-9.16%)</td><td>133.00 (-10.98%)</td><td>34.08 <b>(+22.93%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>180.18 (n/a)</td><td>168.20 (n/a)</td><td>149.40 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (-11.58%)</td><td>0.03 (-8.19%)</td><td>0.03 (-12.55%)</td><td>0.03 (-8.42%)</td><td>0.01 (-0.69%)</td><td>228.10 (+9.19%)</td><td>190.90 (+9.27%)</td><td>201.80 (+14.33%)</td><td>159.60 (+13.11%)</td><td>29.29 (+19.91%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>174.70 (n/a)</td><td>176.50 (n/a)</td><td>141.10 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (-5.44%)</td><td>0.08 (+0.09%)</td><td>0.08 (-5.05%)</td><td>0.06 (+9.22%)</td><td>0.01 <b>(-40.74%)</b></td><td>190.80 (-8.45%)</td><td>154.20 (-2.97%)</td><td>147.60 (+5.35%)</td><td>130.50 (+5.75%)</td><td>22.52 <b>(-41.88%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>208.40 (n/a)</td><td>158.92 (n/a)</td><td>140.10 (n/a)</td><td>123.40 (n/a)</td><td>38.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (-3.49%)</td><td>0.07 (-10.39%)</td><td>0.07 (-9.82%)</td><td>0.06 (-16.03%)</td><td>0.01 <b>(+29.84%)</b></td><td>205.80 (+19.10%)</td><td>179.34 (+12.27%)</td><td>181.50 (+10.87%)</td><td>150.30 (+3.58%)</td><td>21.64 <b>(+60.92%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>172.80 (n/a)</td><td>159.74 (n/a)</td><td>163.70 (n/a)</td><td>145.10 (n/a)</td><td>13.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (-3.47%)</td><td>0.08 (-2.76%)</td><td>0.07 (-8.93%)</td><td>0.07 (+6.05%)</td><td>0.01 (-12.96%)</td><td>178.90 (-5.74%)</td><td>161.78 (+2.47%)</td><td>170.80 (+9.84%)</td><td>136.20 (+3.65%)</td><td>17.83 (-15.78%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>157.88 (n/a)</td><td>155.50 (n/a)</td><td>131.40 (n/a)</td><td>21.17 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (-8.14%)</td><td>0.08 (-5.77%)</td><td>0.08 (-5.12%)</td><td>0.07 (-6.01%)</td><td>0.01 (-15.30%)</td><td>180.00 (+6.38%)</td><td>154.78 (+5.75%)</td><td>152.00 (+5.41%)</td><td>125.70 (+8.83%)</td><td>21.50 (-2.71%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>169.20 (n/a)</td><td>146.36 (n/a)</td><td>144.20 (n/a)</td><td>115.50 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (-16.95%)</td><td>0.07 (-13.38%)</td><td>0.07 (-5.17%)</td><td>0.05 (-6.50%)</td><td>0.01 (-4.45%)</td><td>236.90 (+6.95%)</td><td>189.16 (+15.99%)</td><td>164.20 (+5.46%)</td><td>155.80 <b>(+20.40%)</b></td><td>41.15 (+18.84%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>163.08 (n/a)</td><td>155.70 (n/a)</td><td>129.40 (n/a)</td><td>34.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 <b>(+24.75%)</b></td><td>0.07 (+7.76%)</td><td>0.07 (+6.36%)</td><td>0.06 (-0.71%)</td><td>0.02 <b>(+98.97%)</b></td><td>219.30 (+0.69%)</td><td>175.38 (-4.98%)</td><td>172.90 (-5.98%)</td><td>128.20 (-19.82%)</td><td>35.49 <b>(+59.89%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>184.58 (n/a)</td><td>183.90 (n/a)</td><td>159.90 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (+10.68%)</td><td>0.07 (+0.36%)</td><td>0.07 (-5.23%)</td><td>0.05 (-6.88%)</td><td>0.01 <b>(+76.23%)</b></td><td>225.60 (+7.38%)</td><td>187.70 (+1.59%)</td><td>187.30 (+5.52%)</td><td>145.00 (-9.66%)</td><td>35.24 <b>(+71.63%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>184.76 (n/a)</td><td>177.50 (n/a)</td><td>160.50 (n/a)</td><td>20.53 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (-7.90%)</td><td>0.07 (-10.39%)</td><td>0.08 (-5.11%)</td><td>0.05 <b>(-23.07%)</b></td><td>0.01 (+14.61%)</td><td>246.00 <b>(+29.95%)</b></td><td>179.26 (+13.56%)</td><td>161.50 (+5.42%)</td><td>142.00 (+8.56%)</td><td>41.66 <b>(+63.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>157.86 (n/a)</td><td>153.20 (n/a)</td><td>130.80 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (-3.89%)</td><td>0.15 (+4.59%)</td><td>0.16 (+9.01%)</td><td>0.10 (-14.21%)</td><td>0.03 (+16.16%)</td><td>244.30 (+16.61%)</td><td>169.44 (-2.69%)</td><td>155.70 (-8.25%)</td><td>136.40 (+4.04%)</td><td>43.55 <b>(+46.81%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>209.50 (n/a)</td><td>174.12 (n/a)</td><td>169.70 (n/a)</td><td>131.10 (n/a)</td><td>29.66 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (-11.89%)</td><td>0.16 (-4.12%)</td><td>0.16 (+3.89%)</td><td>0.11 (-11.96%)</td><td>0.04 (+4.28%)</td><td>216.90 (+13.56%)</td><td>163.52 (+5.67%)</td><td>151.50 (-3.75%)</td><td>126.70 (+13.43%)</td><td>39.38 <b>(+37.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.00 (n/a)</td><td>154.74 (n/a)</td><td>157.40 (n/a)</td><td>111.70 (n/a)</td><td>28.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 <b>(+33.16%)</b></td><td>0.18 <b>(+28.07%)</b></td><td>0.19 <b>(+24.25%)</b></td><td>0.14 <b>(+42.37%)</b></td><td>0.03 <b>(+22.38%)</b></td><td>181.20 <b>(-29.77%)</b></td><td>138.28 <b>(-22.63%)</b></td><td>130.80 (-19.51%)</td><td>115.00 <b>(-24.89%)</b></td><td>27.59 <b>(-38.07%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>258.00 (n/a)</td><td>178.72 (n/a)</td><td>162.50 (n/a)</td><td>153.10 (n/a)</td><td>44.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 (+2.55%)</td><td>0.16 (+13.92%)</td><td>0.16 <b>(+26.77%)</b></td><td>0.12 (+9.76%)</td><td>0.03 (-3.38%)</td><td>209.50 (-8.91%)</td><td>162.96 (-12.60%)</td><td>153.50 <b>(-21.12%)</b></td><td>125.40 (-2.49%)</td><td>33.39 (-9.40%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>230.00 (n/a)</td><td>186.46 (n/a)</td><td>194.60 (n/a)</td><td>128.60 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (-2.17%)</td><td>0.14 (-4.45%)</td><td>0.14 (-9.94%)</td><td>0.12 (-1.98%)</td><td>0.02 (-12.03%)</td><td>207.70 (+2.06%)</td><td>176.18 (+4.40%)</td><td>174.20 (+11.03%)</td><td>151.80 (+2.22%)</td><td>21.02 (-7.86%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.50 (n/a)</td><td>168.76 (n/a)</td><td>156.90 (n/a)</td><td>148.50 (n/a)</td><td>22.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (-16.32%)</td><td>0.14 (-13.00%)</td><td>0.14 (-13.32%)</td><td>0.12 (-6.57%)</td><td>0.01 <b>(-34.24%)</b></td><td>207.50 (+7.01%)</td><td>179.42 (+14.08%)</td><td>172.30 (+15.41%)</td><td>156.30 (+19.50%)</td><td>19.75 (-16.59%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>193.90 (n/a)</td><td>157.28 (n/a)</td><td>149.30 (n/a)</td><td>130.80 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 <b>(-20.41%)</b></td><td>0.12 (+1.41%)</td><td>0.12 (+10.91%)</td><td>0.11 (+16.76%)</td><td>0.01 <b>(-68.60%)</b></td><td>218.40 (-14.39%)</td><td>200.46 (-4.79%)</td><td>199.70 (-9.84%)</td><td>178.40 <b>(+25.63%)</b></td><td>14.76 <b>(-64.77%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>255.10 (n/a)</td><td>210.54 (n/a)</td><td>221.50 (n/a)</td><td>142.00 (n/a)</td><td>41.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (-8.60%)</td><td>0.11 (-18.83%)</td><td>0.12 (-12.86%)</td><td>0.07 <b>(-38.08%)</b></td><td>0.02 <b>(+76.78%)</b></td><td>328.80 <b>(+61.49%)</b></td><td>228.88 <b>(+28.05%)</b></td><td>208.80 (+14.79%)</td><td>174.90 (+9.45%)</td><td>60.10 <b>(+227.69%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>178.74 (n/a)</td><td>181.90 (n/a)</td><td>159.80 (n/a)</td><td>18.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 <b>(-24.32%)</b></td><td>0.27 <b>(-20.23%)</b></td><td>0.28 <b>(-24.53%)</b></td><td>0.22 (-19.10%)</td><td>0.03 <b>(-44.01%)</b></td><td>220.70 <b>(+23.64%)</b></td><td>181.42 <b>(+24.12%)</b></td><td>173.70 <b>(+32.49%)</b></td><td>164.90 <b>(+32.13%)</b></td><td>22.60 (-6.76%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.05 (n/a)</td><td>178.50 (n/a)</td><td>146.16 (n/a)</td><td>131.10 (n/a)</td><td>124.80 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.34 (+1.36%)</td><td>0.29 (+4.03%)</td><td>0.28 (+2.33%)</td><td>0.25 (+5.41%)</td><td>0.04 (-11.02%)</td><td>199.10 (-5.15%)</td><td>171.78 (-4.34%)</td><td>174.80 (-2.29%)</td><td>145.70 (-1.35%)</td><td>21.75 (-17.86%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>209.90 (n/a)</td><td>179.58 (n/a)</td><td>178.90 (n/a)</td><td>147.70 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.40 (+5.21%)</td><td>0.30 (+1.39%)</td><td>0.28 (+2.25%)</td><td>0.27 (+6.30%)</td><td>0.05 (+5.65%)</td><td>182.70 (-5.92%)</td><td>165.06 (-1.40%)</td><td>173.90 (-2.19%)</td><td>123.50 (-5.00%)</td><td>23.68 (-7.23%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>194.20 (n/a)</td><td>167.40 (n/a)</td><td>177.80 (n/a)</td><td>130.00 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.39 (+0.32%)</td><td>0.28 (-16.72%)</td><td>0.25 <b>(-33.11%)</b></td><td>0.19 (-8.17%)</td><td>0.08 (+1.05%)</td><td>254.20 (+8.91%)</td><td>188.38 <b>(+20.56%)</b></td><td>195.40 <b>(+49.50%)</b></td><td>126.50 (-0.32%)</td><td>48.66 (+7.89%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.38 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>233.40 (n/a)</td><td>156.26 (n/a)</td><td>130.70 (n/a)</td><td>126.90 (n/a)</td><td>45.10 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.36 (-11.49%)</td><td>0.29 (-7.70%)</td><td>0.28 (-11.43%)</td><td>0.24 (-12.49%)</td><td>0.05 (+6.73%)</td><td>204.60 (+14.30%)</td><td>172.48 (+9.28%)</td><td>178.60 (+12.90%)</td><td>138.40 (+12.98%)</td><td>30.81 <b>(+37.40%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>179.00 (n/a)</td><td>157.84 (n/a)</td><td>158.20 (n/a)</td><td>122.50 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.39 (+0.39%)</td><td>0.33 (+2.99%)</td><td>0.36 (+7.74%)</td><td>0.27 (-0.77%)</td><td>0.05 <b>(+23.13%)</b></td><td>181.60 (+0.78%)</td><td>151.44 (-2.15%)</td><td>138.00 (-7.20%)</td><td>127.00 (-0.39%)</td><td>25.62 <b>(+25.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>180.20 (n/a)</td><td>154.76 (n/a)</td><td>148.70 (n/a)</td><td>127.50 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 <b>(-20.93%)</b></td><td>0.29 (-1.45%)</td><td>0.30 (+7.07%)</td><td>0.28 (+8.48%)</td><td>0.01 <b>(-81.42%)</b></td><td>174.20 (-7.78%)</td><td>168.46 (-0.31%)</td><td>166.20 (-6.63%)</td><td>162.70 <b>(+26.42%)</b></td><td>5.30 <b>(-77.33%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>188.90 (n/a)</td><td>168.98 (n/a)</td><td>178.00 (n/a)</td><td>128.70 (n/a)</td><td>23.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.29 (-6.64%)</td><td>0.26 (-3.06%)</td><td>0.27 (-0.08%)</td><td>0.22 (-4.60%)</td><td>0.03 <b>(-34.29%)</b></td><td>220.90 (+4.84%)</td><td>188.00 (+2.29%)</td><td>184.10 (+0.05%)</td><td>167.80 (+7.08%)</td><td>19.92 <b>(-24.72%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>210.70 (n/a)</td><td>183.80 (n/a)</td><td>184.00 (n/a)</td><td>156.70 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 <b>(+23.32%)</b></td><td>0.02 (+7.97%)</td><td>0.02 (-5.13%)</td><td>0.02 <b>(+38.23%)</b></td><td>0.00 (+15.82%)</td><td>168.90 <b>(-27.67%)</b></td><td>151.16 (-8.27%)</td><td>162.10 (+5.40%)</td><td>107.10 (-18.86%)</td><td>25.52 <b>(-36.09%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.50 (n/a)</td><td>164.78 (n/a)</td><td>153.80 (n/a)</td><td>132.00 (n/a)</td><td>39.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-9.80%)</td><td>0.02 (+1.10%)</td><td>0.02 (+14.86%)</td><td>0.02 (+5.20%)</td><td>0.00 <b>(-27.68%)</b></td><td>173.90 (-4.92%)</td><td>146.82 (-2.69%)</td><td>143.60 (-12.97%)</td><td>117.70 (+10.83%)</td><td>24.22 <b>(-21.52%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>182.90 (n/a)</td><td>150.88 (n/a)</td><td>165.00 (n/a)</td><td>106.20 (n/a)</td><td>30.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-4.29%)</td><td>0.02 (-2.38%)</td><td>0.02 (+4.96%)</td><td>0.01 (+3.13%)</td><td>0.00 <b>(-34.38%)</b></td><td>206.80 (-3.00%)</td><td>169.88 (+0.75%)</td><td>166.70 (-4.74%)</td><td>141.40 (+4.51%)</td><td>23.49 <b>(-29.55%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>213.20 (n/a)</td><td>168.62 (n/a)</td><td>175.00 (n/a)</td><td>135.30 (n/a)</td><td>33.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+4.67%)</td><td>0.02 (+4.82%)</td><td>0.01 (+1.97%)</td><td>0.01 (-10.54%)</td><td>0.01 (+14.53%)</td><td>237.70 (+11.75%)</td><td>172.58 (-2.56%)</td><td>180.60 (-1.95%)</td><td>104.20 (-4.49%)</td><td>50.65 <b>(+23.18%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>212.70 (n/a)</td><td>177.12 (n/a)</td><td>184.20 (n/a)</td><td>109.10 (n/a)</td><td>41.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (+13.29%)</td><td>0.01 (-9.57%)</td><td>0.01 (-17.09%)</td><td>0.01 (-3.98%)</td><td>0.00 <b>(+54.19%)</b></td><td>215.80 (+4.15%)</td><td>187.84 (+12.80%)</td><td>192.70 <b>(+20.59%)</b></td><td>126.60 (-11.72%)</td><td>35.89 <b>(+38.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>207.20 (n/a)</td><td>166.52 (n/a)</td><td>159.80 (n/a)</td><td>143.40 (n/a)</td><td>25.99 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 <b>(-24.29%)</b></td><td>0.01 (-13.67%)</td><td>0.01 (-5.18%)</td><td>0.01 (-9.84%)</td><td>0.00 <b>(-50.00%)</b></td><td>231.40 (+10.93%)</td><td>190.22 (+12.11%)</td><td>185.90 (+5.51%)</td><td>151.10 <b>(+32.08%)</b></td><td>28.86 <b>(-28.54%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.60 (n/a)</td><td>169.68 (n/a)</td><td>176.20 (n/a)</td><td>114.40 (n/a)</td><td>40.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.01 (-4.97%)</td><td>0.01 (-7.13%)</td><td>0.01 (-8.99%)</td><td>0.01 (-10.50%)</td><td>0.00 <b>(+43.24%)</b></td><td>232.70 (+11.77%)</td><td>212.02 (+8.06%)</td><td>218.10 (+9.87%)</td><td>192.10 (+5.20%)</td><td>18.43 <b>(+66.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.20 (n/a)</td><td>196.20 (n/a)</td><td>198.50 (n/a)</td><td>182.60 (n/a)</td><td>11.08 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.01 (+4.09%)</td><td>0.01 (+7.59%)</td><td>0.01 (-5.61%)</td><td>0.01 <b>(+60.45%)</b></td><td>0.00 <b>(-51.70%)</b></td><td>231.90 <b>(-37.66%)</b></td><td>210.68 (-11.74%)</td><td>219.40 (+5.94%)</td><td>179.00 (-3.92%)</td><td>20.44 <b>(-72.96%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>372.00 (n/a)</td><td>238.70 (n/a)</td><td>207.10 (n/a)</td><td>186.30 (n/a)</td><td>75.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+14.07%)</td><td>0.03 (+4.06%)</td><td>0.03 (+2.62%)</td><td>0.02 (-2.70%)</td><td>0.00 <b>(+54.92%)</b></td><td>236.80 (+2.78%)</td><td>183.10 (-2.70%)</td><td>173.50 (-2.53%)</td><td>151.30 (-12.34%)</td><td>33.20 <b>(+39.30%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.40 (n/a)</td><td>188.18 (n/a)</td><td>178.00 (n/a)</td><td>172.60 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (+17.86%)</td><td>0.03 (+10.15%)</td><td>0.03 (-1.22%)</td><td>0.03 <b>(+22.50%)</b></td><td>0.00 <b>(+23.31%)</b></td><td>198.60 (-18.37%)</td><td>172.74 (-9.21%)</td><td>182.60 (+1.22%)</td><td>141.60 (-15.16%)</td><td>24.78 (-18.05%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.30 (n/a)</td><td>190.26 (n/a)</td><td>180.40 (n/a)</td><td>166.90 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (+15.10%)</td><td>0.03 (-1.39%)</td><td>0.03 (-1.95%)</td><td>0.02 <b>(-26.54%)</b></td><td>0.01 <b>(+92.24%)</b></td><td>286.80 <b>(+36.12%)</b></td><td>197.04 (+6.99%)</td><td>201.00 (+2.03%)</td><td>127.40 (-13.16%)</td><td>59.07 <b>(+128.79%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>184.16 (n/a)</td><td>197.00 (n/a)</td><td>146.70 (n/a)</td><td>25.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 <b>(+35.42%)</b></td><td>0.03 <b>(+22.70%)</b></td><td>0.04 <b>(+33.73%)</b></td><td>0.02 (-3.18%)</td><td>0.01 <b>(+106.45%)</b></td><td>243.30 (+3.27%)</td><td>165.26 (-14.84%)</td><td>147.10 <b>(-25.18%)</b></td><td>114.00 <b>(-26.17%)</b></td><td>49.14 <b>(+62.56%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.60 (n/a)</td><td>194.06 (n/a)</td><td>196.60 (n/a)</td><td>154.40 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (+9.62%)</td><td>0.03 (+5.00%)</td><td>0.03 (-2.04%)</td><td>0.02 (-4.05%)</td><td>0.01 <b>(+37.82%)</b></td><td>212.90 (+4.21%)</td><td>170.30 (-3.30%)</td><td>177.60 (+2.07%)</td><td>128.10 (-8.76%)</td><td>35.44 <b>(+25.64%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>176.12 (n/a)</td><td>174.00 (n/a)</td><td>140.40 (n/a)</td><td>28.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 <b>(+68.89%)</b></td><td>0.03 <b>(+50.68%)</b></td><td>0.03 <b>(+33.99%)</b></td><td>0.03 <b>(+49.83%)</b></td><td>0.01 <b>(+117.43%)</b></td><td>199.40 <b>(-33.27%)</b></td><td>160.08 <b>(-32.34%)</b></td><td>176.30 <b>(-25.36%)</b></td><td>114.40 <b>(-40.79%)</b></td><td>35.09 (-14.95%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>298.80 (n/a)</td><td>236.58 (n/a)</td><td>236.20 (n/a)</td><td>193.20 (n/a)</td><td>41.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (-1.73%)</td><td>0.03 (+16.29%)</td><td>0.03 <b>(+22.62%)</b></td><td>0.02 <b>(+61.58%)</b></td><td>0.00 <b>(-44.91%)</b></td><td>214.20 <b>(-38.13%)</b></td><td>186.66 (-18.81%)</td><td>181.50 (-18.43%)</td><td>152.10 (+1.74%)</td><td>24.49 <b>(-65.94%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>346.20 (n/a)</td><td>229.90 (n/a)</td><td>222.50 (n/a)</td><td>149.50 (n/a)</td><td>71.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+11.72%)</td><td>0.02 (+15.73%)</td><td>0.02 (+9.85%)</td><td>0.02 <b>(+34.16%)</b></td><td>0.00 <b>(-41.47%)</b></td><td>233.30 <b>(-25.46%)</b></td><td>212.42 (-14.63%)</td><td>210.10 (-8.97%)</td><td>197.70 (-10.50%)</td><td>14.26 <b>(-61.71%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>313.00 (n/a)</td><td>248.82 (n/a)</td><td>230.80 (n/a)</td><td>220.90 (n/a)</td><td>37.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (-5.41%)</td><td>0.06 (+4.48%)</td><td>0.07 (+10.71%)</td><td>0.04 (-1.18%)</td><td>0.01 (+1.91%)</td><td>238.20 (+1.19%)</td><td>171.30 (-3.84%)</td><td>157.60 (-9.68%)</td><td>136.70 (+5.72%)</td><td>41.36 (+9.61%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>235.40 (n/a)</td><td>178.14 (n/a)</td><td>174.50 (n/a)</td><td>129.30 (n/a)</td><td>37.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (-1.31%)</td><td>0.06 (-2.34%)</td><td>0.06 (-4.80%)</td><td>0.05 (-4.52%)</td><td>0.01 (-2.80%)</td><td>212.50 (+4.73%)</td><td>183.22 (+2.33%)</td><td>187.90 (+5.03%)</td><td>147.80 (+1.30%)</td><td>23.74 (+0.19%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>179.04 (n/a)</td><td>178.90 (n/a)</td><td>145.90 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 <b>(-20.42%)</b></td><td>0.06 (-3.76%)</td><td>0.06 (-0.93%)</td><td>0.05 (+3.43%)</td><td>0.01 <b>(-47.49%)</b></td><td>196.00 (-3.31%)</td><td>175.18 (+1.81%)</td><td>185.20 (+0.93%)</td><td>153.20 <b>(+25.68%)</b></td><td>19.98 <b>(-35.29%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.70 (n/a)</td><td>172.06 (n/a)</td><td>183.50 (n/a)</td><td>121.90 (n/a)</td><td>30.88 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (+0.04%)</td><td>0.06 (-5.01%)</td><td>0.06 (-6.72%)</td><td>0.05 (-4.79%)</td><td>0.02 (+8.40%)</td><td>228.80 (+5.00%)</td><td>183.46 (+6.07%)</td><td>183.00 (+7.21%)</td><td>121.70 (-0.08%)</td><td>39.31 (+11.41%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>172.96 (n/a)</td><td>170.70 (n/a)</td><td>121.80 (n/a)</td><td>35.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (+6.90%)</td><td>0.07 (+8.85%)</td><td>0.07 (+10.58%)</td><td>0.06 (+15.30%)</td><td>0.01 (-3.04%)</td><td>184.70 (-13.29%)</td><td>161.78 (-8.46%)</td><td>160.20 (-9.59%)</td><td>137.30 (-6.47%)</td><td>19.05 <b>(-21.37%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>176.74 (n/a)</td><td>177.20 (n/a)</td><td>146.80 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (+9.77%)</td><td>0.06 (+4.59%)</td><td>0.05 (+0.01%)</td><td>0.05 (+9.28%)</td><td>0.01 <b>(+22.52%)</b></td><td>209.80 (-8.46%)</td><td>190.36 (-4.23%)</td><td>197.50 (+0.00%)</td><td>162.50 (-8.91%)</td><td>19.36 (+0.97%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>229.20 (n/a)</td><td>198.76 (n/a)</td><td>197.50 (n/a)</td><td>178.40 (n/a)</td><td>19.17 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 <b>(-28.22%)</b></td><td>0.06 (-15.06%)</td><td>0.06 (-11.02%)</td><td>0.05 (+10.53%)</td><td>0.00 <b>(-80.75%)</b></td><td>196.00 (-9.51%)</td><td>180.58 (+11.75%)</td><td>180.10 (+12.42%)</td><td>166.40 <b>(+39.36%)</b></td><td>10.64 <b>(-74.85%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>216.60 (n/a)</td><td>161.60 (n/a)</td><td>160.20 (n/a)</td><td>119.40 (n/a)</td><td>42.30 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-17.20%)</td><td>0.05 (-6.38%)</td><td>0.05 (-7.00%)</td><td>0.05 (+17.45%)</td><td>0.01 <b>(-62.75%)</b></td><td>231.40 (-14.86%)</td><td>197.78 (+1.73%)</td><td>199.20 (+7.56%)</td><td>175.60 <b>(+20.77%)</b></td><td>21.41 <b>(-60.06%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>271.80 (n/a)</td><td>194.42 (n/a)</td><td>185.20 (n/a)</td><td>145.40 (n/a)</td><td>53.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (+1.10%)</td><td>0.12 (-12.78%)</td><td>0.11 <b>(-20.40%)</b></td><td>0.09 (-16.60%)</td><td>0.03 <b>(+43.20%)</b></td><td>228.80 (+19.92%)</td><td>181.98 (+17.27%)</td><td>188.70 <b>(+25.63%)</b></td><td>125.10 (-1.11%)</td><td>38.07 <b>(+62.80%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>190.80 (n/a)</td><td>155.18 (n/a)</td><td>150.20 (n/a)</td><td>126.50 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 (-7.56%)</td><td>0.11 (-18.06%)</td><td>0.12 (-15.22%)</td><td>0.06 <b>(-48.54%)</b></td><td>0.04 <b>(+99.09%)</b></td><td>348.00 <b>(+94.30%)</b></td><td>209.62 <b>(+33.81%)</b></td><td>175.40 (+17.96%)</td><td>144.30 (+8.17%)</td><td>84.71 <b>(+301.95%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>179.10 (n/a)</td><td>156.66 (n/a)</td><td>148.70 (n/a)</td><td>133.40 (n/a)</td><td>21.07 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (+10.68%)</td><td>0.12 (+8.69%)</td><td>0.11 (+9.33%)</td><td>0.11 (+13.17%)</td><td>0.03 (+10.06%)</td><td>197.30 (-11.64%)</td><td>179.12 (-8.11%)</td><td>192.60 (-8.50%)</td><td>123.30 (-9.67%)</td><td>31.44 (-13.19%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>223.30 (n/a)</td><td>194.92 (n/a)</td><td>210.50 (n/a)</td><td>136.50 (n/a)</td><td>36.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (-7.16%)</td><td>0.12 (+9.72%)</td><td>0.12 (+14.64%)</td><td>0.10 <b>(+34.57%)</b></td><td>0.02 <b>(-49.05%)</b></td><td>206.90 <b>(-25.68%)</b></td><td>178.82 (-12.96%)</td><td>180.60 (-12.80%)</td><td>146.10 (+7.74%)</td><td>21.82 <b>(-59.42%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>278.40 (n/a)</td><td>205.44 (n/a)</td><td>207.10 (n/a)</td><td>135.60 (n/a)</td><td>53.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (+3.01%)</td><td>0.12 (-0.10%)</td><td>0.11 (+0.49%)</td><td>0.10 (-0.23%)</td><td>0.03 (+2.13%)</td><td>219.50 (+0.23%)</td><td>179.78 (+0.07%)</td><td>186.00 (-0.48%)</td><td>123.50 (-2.91%)</td><td>38.68 (-2.57%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>219.00 (n/a)</td><td>179.66 (n/a)</td><td>186.90 (n/a)</td><td>127.20 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 <b>(+25.73%)</b></td><td>0.11 (-5.41%)</td><td>0.10 (-16.74%)</td><td>0.08 (-15.74%)</td><td>0.03 <b>(+131.40%)</b></td><td>259.30 (+18.67%)</td><td>205.74 (+9.48%)</td><td>209.70 <b>(+20.10%)</b></td><td>137.00 <b>(-20.44%)</b></td><td>44.26 <b>(+110.93%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>187.92 (n/a)</td><td>174.60 (n/a)</td><td>172.20 (n/a)</td><td>20.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 <b>(+34.46%)</b></td><td>0.12 (+10.97%)</td><td>0.11 (+7.32%)</td><td>0.08 (-12.89%)</td><td>0.04 <b>(+117.52%)</b></td><td>260.30 (+14.77%)</td><td>188.88 (-5.26%)</td><td>185.50 (-6.83%)</td><td>115.50 <b>(-25.63%)</b></td><td>51.91 <b>(+77.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>226.80 (n/a)</td><td>199.36 (n/a)</td><td>199.10 (n/a)</td><td>155.30 (n/a)</td><td>29.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (+13.68%)</td><td>0.10 (+14.14%)</td><td>0.10 (+12.57%)</td><td>0.09 <b>(+20.64%)</b></td><td>0.01 (+5.67%)</td><td>222.50 (-17.10%)</td><td>206.76 (-12.47%)</td><td>210.50 (-11.14%)</td><td>187.80 (-12.00%)</td><td>16.55 <b>(-22.84%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>268.40 (n/a)</td><td>236.22 (n/a)</td><td>236.90 (n/a)</td><td>213.40 (n/a)</td><td>21.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>166.24 (n/a)</td><td>177.40 (n/a)</td><td>116.80 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>372.40 (n/a)</td><td>226.10 (n/a)</td><td>164.20 (n/a)</td><td>155.00 (n/a)</td><td>95.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>165.42 (n/a)</td><td>167.50 (n/a)</td><td>127.00 (n/a)</td><td>29.27 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.80 (n/a)</td><td>194.22 (n/a)</td><td>172.40 (n/a)</td><td>161.60 (n/a)</td><td>40.49 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>175.10 (n/a)</td><td>148.98 (n/a)</td><td>149.90 (n/a)</td><td>112.10 (n/a)</td><td>26.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>208.20 (n/a)</td><td>166.88 (n/a)</td><td>162.70 (n/a)</td><td>101.80 (n/a)</td><td>42.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>203.20 (n/a)</td><td>168.02 (n/a)</td><td>187.10 (n/a)</td><td>108.60 (n/a)</td><td>40.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>199.52 (n/a)</td><td>194.70 (n/a)</td><td>172.80 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>178.70 (n/a)</td><td>151.12 (n/a)</td><td>156.30 (n/a)</td><td>125.00 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>240.70 (n/a)</td><td>176.86 (n/a)</td><td>169.50 (n/a)</td><td>138.20 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>209.80 (n/a)</td><td>162.92 (n/a)</td><td>158.10 (n/a)</td><td>125.30 (n/a)</td><td>31.77 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>262.10 (n/a)</td><td>198.02 (n/a)</td><td>178.10 (n/a)</td><td>122.30 (n/a)</td><td>61.28 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.36 (+12.74%)</td><td>0.31 (+11.03%)</td><td>0.30 (+4.31%)</td><td>0.26 <b>(+22.85%)</b></td><td>0.04 (+1.35%)</td><td>192.20 (-18.59%)</td><td>163.26 (-10.44%)</td><td>165.30 (-4.17%)</td><td>137.70 (-11.28%)</td><td>21.72 <b>(-30.19%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>236.10 (n/a)</td><td>182.30 (n/a)</td><td>172.50 (n/a)</td><td>155.20 (n/a)</td><td>31.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>204.60 (n/a)</td><td>163.54 (n/a)</td><td>162.80 (n/a)</td><td>127.10 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>226.00 (n/a)</td><td>179.96 (n/a)</td><td>188.40 (n/a)</td><td>119.90 (n/a)</td><td>38.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>213.50 (n/a)</td><td>172.38 (n/a)</td><td>171.80 (n/a)</td><td>125.80 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>170.54 (n/a)</td><td>187.40 (n/a)</td><td>131.90 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>163.80 (n/a)</td><td>183.00 (n/a)</td><td>111.70 (n/a)</td><td>46.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>262.00 (n/a)</td><td>185.68 (n/a)</td><td>180.70 (n/a)</td><td>132.40 (n/a)</td><td>49.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.30 (n/a)</td><td>212.38 (n/a)</td><td>213.10 (n/a)</td><td>160.90 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>176.10 (n/a)</td><td>147.56 (n/a)</td><td>150.30 (n/a)</td><td>125.30 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>157.54 (n/a)</td><td>158.30 (n/a)</td><td>122.40 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.20 (n/a)</td><td>161.48 (n/a)</td><td>160.60 (n/a)</td><td>132.30 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>267.10 (n/a)</td><td>194.34 (n/a)</td><td>206.40 (n/a)</td><td>140.90 (n/a)</td><td>53.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>242.20 (n/a)</td><td>185.08 (n/a)</td><td>200.20 (n/a)</td><td>129.40 (n/a)</td><td>44.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>369.10 (n/a)</td><td>223.62 (n/a)</td><td>202.30 (n/a)</td><td>153.60 (n/a)</td><td>84.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.70 (n/a)</td><td>161.52 (n/a)</td><td>160.90 (n/a)</td><td>134.90 (n/a)</td><td>19.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>167.92 (n/a)</td><td>161.10 (n/a)</td><td>143.80 (n/a)</td><td>22.03 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>212.40 (n/a)</td><td>170.42 (n/a)</td><td>170.80 (n/a)</td><td>134.40 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>211.20 (n/a)</td><td>172.20 (n/a)</td><td>168.00 (n/a)</td><td>133.10 (n/a)</td><td>29.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>205.60 (n/a)</td><td>171.74 (n/a)</td><td>178.00 (n/a)</td><td>120.40 (n/a)</td><td>35.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>137.92 (n/a)</td><td>113.60 (n/a)</td><td>105.90 (n/a)</td><td>37.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>157.52 (n/a)</td><td>164.80 (n/a)</td><td>117.00 (n/a)</td><td>35.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>264.90 (n/a)</td><td>181.86 (n/a)</td><td>170.70 (n/a)</td><td>135.60 (n/a)</td><td>49.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>173.58 (n/a)</td><td>190.50 (n/a)</td><td>121.00 (n/a)</td><td>43.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>165.36 (n/a)</td><td>172.90 (n/a)</td><td>109.30 (n/a)</td><td>38.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.00 (n/a)</td><td>179.84 (n/a)</td><td>183.80 (n/a)</td><td>135.30 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.40 (n/a)</td><td>155.00 (n/a)</td><td>154.70 (n/a)</td><td>109.80 (n/a)</td><td>29.59 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.20 (n/a)</td><td>195.08 (n/a)</td><td>193.20 (n/a)</td><td>149.40 (n/a)</td><td>44.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>147.64 (n/a)</td><td>145.80 (n/a)</td><td>109.50 (n/a)</td><td>27.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.20 (n/a)</td><td>159.76 (n/a)</td><td>159.70 (n/a)</td><td>135.40 (n/a)</td><td>18.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>300.10 (n/a)</td><td>222.14 (n/a)</td><td>220.10 (n/a)</td><td>134.60 (n/a)</td><td>68.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>160.64 (n/a)</td><td>135.80 (n/a)</td><td>114.20 (n/a)</td><td>46.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>167.92 (n/a)</td><td>171.60 (n/a)</td><td>134.50 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.40 (n/a)</td><td>158.82 (n/a)</td><td>161.60 (n/a)</td><td>130.70 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.90 (n/a)</td><td>180.08 (n/a)</td><td>178.50 (n/a)</td><td>134.90 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>200.90 (n/a)</td><td>210.10 (n/a)</td><td>152.20 (n/a)</td><td>36.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>238.90 (n/a)</td><td>192.08 (n/a)</td><td>192.90 (n/a)</td><td>134.60 (n/a)</td><td>38.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.60 (n/a)</td><td>188.04 (n/a)</td><td>196.20 (n/a)</td><td>133.50 (n/a)</td><td>38.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>318.60 (n/a)</td><td>196.58 (n/a)</td><td>167.00 (n/a)</td><td>142.90 (n/a)</td><td>71.56 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.10 (n/a)</td><td>156.88 (n/a)</td><td>151.20 (n/a)</td><td>132.80 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.40 (n/a)</td><td>163.22 (n/a)</td><td>149.90 (n/a)</td><td>134.10 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>174.70 (n/a)</td><td>161.80 (n/a)</td><td>150.30 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.40 (n/a)</td><td>182.92 (n/a)</td><td>166.80 (n/a)</td><td>144.90 (n/a)</td><td>35.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>207.04 (n/a)</td><td>198.50 (n/a)</td><td>186.30 (n/a)</td><td>18.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>182.90 (n/a)</td><td>153.78 (n/a)</td><td>156.00 (n/a)</td><td>116.60 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>169.10 (n/a)</td><td>157.02 (n/a)</td><td>163.50 (n/a)</td><td>135.20 (n/a)</td><td>14.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.90 (n/a)</td><td>163.98 (n/a)</td><td>153.50 (n/a)</td><td>124.10 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.30 (n/a)</td><td>172.14 (n/a)</td><td>179.10 (n/a)</td><td>130.40 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>189.10 (n/a)</td><td>165.58 (n/a)</td><td>167.10 (n/a)</td><td>140.10 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.70 (n/a)</td><td>167.46 (n/a)</td><td>169.80 (n/a)</td><td>138.20 (n/a)</td><td>24.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.10 (n/a)</td><td>162.30 (n/a)</td><td>162.00 (n/a)</td><td>138.40 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>232.60 (n/a)</td><td>207.56 (n/a)</td><td>210.80 (n/a)</td><td>165.80 (n/a)</td><td>26.95 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>4.43 (+4.30%)</td><td>3.98 (-2.31%)</td><td>4.04 (-4.53%)</td><td>3.60 (+2.99%)</td><td>0.37 (+13.22%)</td><td>2612.10 (-2.90%)</td><td>2381.68 (+2.49%)</td><td>2325.80 (+4.75%)</td><td>2122.20 (-4.12%)</td><td>220.74 (+6.97%)</td><td>1743.20 (+4.30%)</td><td>1563.97 (-2.31%)</td><td>1590.59 (-4.53%)</td><td>1416.25 (+2.99%)</td><td>144.49 (+13.22%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>4.25 (n/a)</td><td>4.07 (n/a)</td><td>4.24 (n/a)</td><td>3.50 (n/a)</td><td>0.32 (n/a)</td><td>2690.20 (n/a)</td><td>2323.88 (n/a)</td><td>2220.30 (n/a)</td><td>2213.40 (n/a)</td><td>206.36 (n/a)</td><td>1671.38 (n/a)</td><td>1600.97 (n/a)</td><td>1666.13 (n/a)</td><td>1375.15 (n/a)</td><td>127.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.30 (+16.70%)</td><td>0.86 (-5.47%)</td><td>0.81 (-14.50%)</td><td>0.65 (+6.87%)</td><td>0.27 <b>(+41.13%)</b></td><td>341.60 (-6.41%)</td><td>275.64 (+8.13%)</td><td>273.10 (+16.96%)</td><td>170.50 (-14.32%)</td><td>70.74 (+9.56%)</td><td>55.35 (+16.70%)</td><td>36.51 (-5.47%)</td><td>34.55 (-14.50%)</td><td>27.63 (+6.87%)</td><td>11.34 <b>(+41.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.11 (n/a)</td><td>0.91 (n/a)</td><td>0.95 (n/a)</td><td>0.61 (n/a)</td><td>0.19 (n/a)</td><td>365.00 (n/a)</td><td>254.92 (n/a)</td><td>233.50 (n/a)</td><td>199.00 (n/a)</td><td>64.56 (n/a)</td><td>47.43 (n/a)</td><td>38.62 (n/a)</td><td>40.41 (n/a)</td><td>25.85 (n/a)</td><td>8.03 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.06 (-13.13%)</td><td>0.98 (+13.39%)</td><td>0.98 <b>(+20.84%)</b></td><td>0.85 <b>(+37.16%)</b></td><td>0.08 <b>(-62.86%)</b></td><td>260.10 <b>(-27.08%)</b></td><td>226.72 (-15.35%)</td><td>225.40 (-17.25%)</td><td>209.60 (+15.10%)</td><td>20.09 <b>(-67.93%)</b></td><td>45.02 (-13.13%)</td><td>41.87 (+13.39%)</td><td>41.86 <b>(+20.84%)</b></td><td>36.28 <b>(+37.16%)</b></td><td>3.46 <b>(-62.86%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.21 (n/a)</td><td>0.87 (n/a)</td><td>0.81 (n/a)</td><td>0.62 (n/a)</td><td>0.22 (n/a)</td><td>356.70 (n/a)</td><td>267.84 (n/a)</td><td>272.40 (n/a)</td><td>182.10 (n/a)</td><td>62.64 (n/a)</td><td>51.83 (n/a)</td><td>36.93 (n/a)</td><td>34.64 (n/a)</td><td>26.45 (n/a)</td><td>9.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.52 (+0.03%)</td><td>0.52 (-0.05%)</td><td>0.52 (+0.03%)</td><td>0.52 (-0.26%)</td><td>0.00 <b>(+128.05%)</b></td><td>48635.70 (+0.26%)</td><td>48503.20 (+0.05%)</td><td>48486.80 (-0.03%)</td><td>48422.10 (-0.03%)</td><td>79.17 <b>(+128.65%)</b></td><td>354.79 (+0.03%)</td><td>354.20 (-0.05%)</td><td>354.32 (+0.03%)</td><td>353.24 (-0.26%)</td><td>0.58 <b>(+128.03%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48507.60 (n/a)</td><td>48479.12 (n/a)</td><td>48502.40 (n/a)</td><td>48438.90 (n/a)</td><td>34.62 (n/a)</td><td>354.67 (n/a)</td><td>354.38 (n/a)</td><td>354.21 (n/a)</td><td>354.17 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 (+0.60%)</td><td>0.21 (+0.52%)</td><td>0.21 (+0.34%)</td><td>0.21 (+0.74%)</td><td>0.00 (-8.35%)</td><td>119063.00 (-0.74%)</td><td>118423.08 (-0.51%)</td><td>118604.60 (-0.34%)</td><td>117281.00 (-0.59%)</td><td>689.55 (-9.65%)</td><td>146.48 (+0.60%)</td><td>145.08 (+0.52%)</td><td>144.85 (+0.34%)</td><td>144.29 (+0.74%)</td><td>0.85 (-8.35%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119947.90 (n/a)</td><td>119035.94 (n/a)</td><td>119003.80 (n/a)</td><td>117982.50 (n/a)</td><td>763.21 (n/a)</td><td>145.61 (n/a)</td><td>144.33 (n/a)</td><td>144.36 (n/a)</td><td>143.23 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.90 (+0.45%)</td><td>0.89 (+0.19%)</td><td>0.89 (+0.14%)</td><td>0.88 (-0.49%)</td><td>0.01 <b>(+50.61%)</b></td><td>28754.00 (+0.50%)</td><td>28175.68 (-0.18%)</td><td>28132.30 (-0.14%)</td><td>27884.00 (-0.45%)</td><td>341.57 <b>(+50.65%)</b></td><td>616.12 (+0.45%)</td><td>609.81 (+0.19%)</td><td>610.68 (+0.14%)</td><td>597.48 (-0.49%)</td><td>7.31 <b>(+50.61%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28611.80 (n/a)</td><td>28226.70 (n/a)</td><td>28172.70 (n/a)</td><td>28010.20 (n/a)</td><td>226.73 (n/a)</td><td>613.34 (n/a)</td><td>608.67 (n/a)</td><td>609.80 (n/a)</td><td>600.45 (n/a)</td><td>4.85 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>3.57 (-1.51%)</td><td>3.44 (-1.20%)</td><td>3.42 (-1.69%)</td><td>3.35 (-0.55%)</td><td>0.09 (-11.47%)</td><td>7521.80 (+0.55%)</td><td>7325.30 (+1.20%)</td><td>7362.30 (+1.72%)</td><td>7048.30 (+1.54%)</td><td>198.15 (-9.64%)</td><td>2437.45 (-1.51%)</td><td>2346.66 (-1.20%)</td><td>2333.50 (-1.69%)</td><td>2284.00 (-0.55%)</td><td>64.13 (-11.47%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.63 (n/a)</td><td>3.48 (n/a)</td><td>3.48 (n/a)</td><td>3.36 (n/a)</td><td>0.11 (n/a)</td><td>7480.70 (n/a)</td><td>7238.22 (n/a)</td><td>7237.90 (n/a)</td><td>6941.60 (n/a)</td><td>219.28 (n/a)</td><td>2474.90 (n/a)</td><td>2375.25 (n/a)</td><td>2373.60 (n/a)</td><td>2296.56 (n/a)</td><td>72.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>2.84 (-11.94%)</td><td>2.79 (-4.02%)</td><td>2.81 (-1.40%)</td><td>2.73 (-0.90%)</td><td>0.05 <b>(-74.94%)</b></td><td>9205.80 (+0.91%)</td><td>9014.08 (+3.91%)</td><td>8958.80 (+1.42%)</td><td>8864.80 (+13.56%)</td><td>147.25 <b>(-70.86%)</b></td><td>1938.00 (-11.94%)</td><td>1906.30 (-4.02%)</td><td>1917.65 (-1.40%)</td><td>1866.20 (-0.90%)</td><td>30.99 <b>(-74.94%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.22 (n/a)</td><td>2.91 (n/a)</td><td>2.85 (n/a)</td><td>2.76 (n/a)</td><td>0.18 (n/a)</td><td>9122.60 (n/a)</td><td>8675.10 (n/a)</td><td>8833.50 (n/a)</td><td>7806.60 (n/a)</td><td>505.40 (n/a)</td><td>2200.70 (n/a)</td><td>1986.12 (n/a)</td><td>1944.86 (n/a)</td><td>1883.21 (n/a)</td><td>123.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>3.33 (+0.83%)</td><td>3.22 (+0.31%)</td><td>3.21 (+0.95%)</td><td>3.07 (-1.86%)</td><td>0.10 <b>(+32.60%)</b></td><td>8185.40 (+1.89%)</td><td>7828.12 (-0.27%)</td><td>7849.10 (-0.95%)</td><td>7550.60 (-0.82%)</td><td>256.91 <b>(+33.68%)</b></td><td>2275.31 (+0.83%)</td><td>2196.51 (+0.31%)</td><td>2188.77 (+0.95%)</td><td>2098.84 (-1.86%)</td><td>71.60 <b>(+32.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.31 (n/a)</td><td>3.21 (n/a)</td><td>3.18 (n/a)</td><td>3.13 (n/a)</td><td>0.08 (n/a)</td><td>8033.60 (n/a)</td><td>7849.24 (n/a)</td><td>7924.10 (n/a)</td><td>7613.00 (n/a)</td><td>192.18 (n/a)</td><td>2256.64 (n/a)</td><td>2189.79 (n/a)</td><td>2168.07 (n/a)</td><td>2138.51 (n/a)</td><td>54.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.79 (-0.30%)</td><td>0.79 (-0.09%)</td><td>0.79 (-0.01%)</td><td>0.78 (-0.15%)</td><td>0.00 <b>(-43.38%)</b></td><td>96293.50 (+0.15%)</td><td>96155.28 (+0.09%)</td><td>96126.60 (+0.01%)</td><td>96107.60 (+0.30%)</td><td>78.06 <b>(-43.12%)</b></td><td>715.03 (-0.30%)</td><td>714.67 (-0.09%)</td><td>714.89 (-0.01%)</td><td>713.65 (-0.15%)</td><td>0.58 <b>(-43.38%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>96153.20 (n/a)</td><td>96066.40 (n/a)</td><td>96116.40 (n/a)</td><td>95822.90 (n/a)</td><td>137.25 (n/a)</td><td>717.15 (n/a)</td><td>715.33 (n/a)</td><td>714.96 (n/a)</td><td>714.69 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.73 (-0.01%)</td><td>0.73 (+0.01%)</td><td>0.73 (+0.01%)</td><td>0.73 (+0.01%)</td><td>0.00 (-7.60%)</td><td>103435.30 (-0.01%)</td><td>103340.78 (-0.01%)</td><td>103316.50 (-0.01%)</td><td>103295.30 (+0.01%)</td><td>55.79 (-7.55%)</td><td>665.27 (-0.01%)</td><td>664.98 (+0.01%)</td><td>665.14 (+0.01%)</td><td>664.37 (+0.01%)</td><td>0.36 (-7.60%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103448.20 (n/a)</td><td>103347.40 (n/a)</td><td>103327.50 (n/a)</td><td>103287.60 (n/a)</td><td>60.34 (n/a)</td><td>665.32 (n/a)</td><td>664.94 (n/a)</td><td>665.07 (n/a)</td><td>664.29 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.69 (-0.89%)</td><td>0.69 (-0.51%)</td><td>0.69 (-0.66%)</td><td>0.69 (-0.34%)</td><td>0.00 <b>(-53.34%)</b></td><td>109147.40 (+0.34%)</td><td>108899.30 (+0.51%)</td><td>108975.90 (+0.66%)</td><td>108677.50 (+0.89%)</td><td>206.23 <b>(-52.81%)</b></td><td>632.33 (-0.89%)</td><td>631.04 (-0.51%)</td><td>630.59 (-0.66%)</td><td>629.60 (-0.34%)</td><td>1.20 <b>(-53.34%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108772.50 (n/a)</td><td>108347.34 (n/a)</td><td>108262.00 (n/a)</td><td>107713.60 (n/a)</td><td>436.99 (n/a)</td><td>637.98 (n/a)</td><td>634.26 (n/a)</td><td>634.75 (n/a)</td><td>631.77 (n/a)</td><td>2.56 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>7.79 (+2.74%)</td><td>7.01 (-3.16%)</td><td>6.83 (-5.83%)</td><td>6.47 (-5.44%)</td><td>0.56 <b>(+67.99%)</b></td><td>1377.70 (+5.76%)</td><td>1278.46 (+3.60%)</td><td>1305.20 (+6.18%)</td><td>1144.40 (-2.67%)</td><td>99.92 <b>(+73.97%)</b></td><td>469.13 (+2.74%)</td><td>422.05 (-3.16%)</td><td>411.32 (-5.83%)</td><td>389.68 (-5.44%)</td><td>33.94 <b>(+67.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>7.58 (n/a)</td><td>7.24 (n/a)</td><td>7.25 (n/a)</td><td>6.84 (n/a)</td><td>0.34 (n/a)</td><td>1302.70 (n/a)</td><td>1234.00 (n/a)</td><td>1229.20 (n/a)</td><td>1175.80 (n/a)</td><td>57.44 (n/a)</td><td>456.60 (n/a)</td><td>435.82 (n/a)</td><td>436.77 (n/a)</td><td>412.12 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>7.08 (+1.94%)</td><td>6.76 (+16.47%)</td><td>6.89 <b>(+26.09%)</b></td><td>6.37 <b>(+32.95%)</b></td><td>0.29 <b>(-70.88%)</b></td><td>1399.90 <b>(-24.78%)</b></td><td>1321.16 (-15.92%)</td><td>1294.40 <b>(-20.69%)</b></td><td>1259.50 (-1.91%)</td><td>56.60 <b>(-78.04%)</b></td><td>426.26 (+1.94%)</td><td>406.95 (+16.47%)</td><td>414.77 <b>(+26.09%)</b></td><td>383.51 <b>(+32.95%)</b></td><td>17.18 <b>(-70.88%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>6.94 (n/a)</td><td>5.80 (n/a)</td><td>5.46 (n/a)</td><td>4.79 (n/a)</td><td>0.98 (n/a)</td><td>1861.10 (n/a)</td><td>1571.28 (n/a)</td><td>1632.10 (n/a)</td><td>1284.00 (n/a)</td><td>257.74 (n/a)</td><td>418.13 (n/a)</td><td>349.40 (n/a)</td><td>328.94 (n/a)</td><td>288.47 (n/a)</td><td>59.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>6.69 (-5.48%)</td><td>6.06 (-9.11%)</td><td>6.21 (-5.44%)</td><td>4.73 <b>(-24.65%)</b></td><td>0.77 <b>(+155.85%)</b></td><td>1882.50 <b>(+32.71%)</b></td><td>1494.16 (+11.54%)</td><td>1435.70 (+5.75%)</td><td>1333.30 (+5.80%)</td><td>222.66 <b>(+267.99%)</b></td><td>402.67 (-5.48%)</td><td>364.85 (-9.11%)</td><td>373.94 (-5.44%)</td><td>285.19 <b>(-24.65%)</b></td><td>46.59 <b>(+155.85%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>7.07 (n/a)</td><td>6.66 (n/a)</td><td>6.56 (n/a)</td><td>6.28 (n/a)</td><td>0.30 (n/a)</td><td>1418.50 (n/a)</td><td>1339.58 (n/a)</td><td>1357.70 (n/a)</td><td>1260.20 (n/a)</td><td>60.51 (n/a)</td><td>426.02 (n/a)</td><td>401.44 (n/a)</td><td>395.44 (n/a)</td><td>378.49 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>8.09 (-5.18%)</td><td>7.95 (-1.85%)</td><td>8.00 (-0.21%)</td><td>7.77 (-1.81%)</td><td>0.13 <b>(-45.62%)</b></td><td>4490.00 (+1.84%)</td><td>4386.42 (+1.83%)</td><td>4357.00 (+0.21%)</td><td>4310.90 (+5.46%)</td><td>74.43 <b>(-41.20%)</b></td><td>498.15 (-5.18%)</td><td>489.69 (-1.85%)</td><td>492.89 (-0.21%)</td><td>478.28 (-1.81%)</td><td>8.25 <b>(-45.62%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>8.53 (n/a)</td><td>8.10 (n/a)</td><td>8.02 (n/a)</td><td>7.91 (n/a)</td><td>0.25 (n/a)</td><td>4408.70 (n/a)</td><td>4307.40 (n/a)</td><td>4347.80 (n/a)</td><td>4087.60 (n/a)</td><td>126.58 (n/a)</td><td>525.36 (n/a)</td><td>498.91 (n/a)</td><td>493.93 (n/a)</td><td>487.11 (n/a)</td><td>15.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>7.56 (-3.84%)</td><td>7.37 (-1.89%)</td><td>7.53 (-0.37%)</td><td>7.09 (+0.86%)</td><td>0.24 <b>(-20.35%)</b></td><td>4914.30 (-0.86%)</td><td>4733.46 (+1.88%)</td><td>4630.00 (+0.37%)</td><td>4614.30 (+3.99%)</td><td>154.56 (-18.62%)</td><td>465.40 (-3.84%)</td><td>454.06 (-1.89%)</td><td>463.82 (-0.37%)</td><td>436.98 (+0.86%)</td><td>14.65 <b>(-20.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>7.86 (n/a)</td><td>7.51 (n/a)</td><td>7.56 (n/a)</td><td>7.03 (n/a)</td><td>0.30 (n/a)</td><td>4956.80 (n/a)</td><td>4646.00 (n/a)</td><td>4613.00 (n/a)</td><td>4437.20 (n/a)</td><td>189.92 (n/a)</td><td>483.97 (n/a)</td><td>462.82 (n/a)</td><td>465.53 (n/a)</td><td>433.24 (n/a)</td><td>18.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>7.35 (+0.53%)</td><td>7.20 (+2.50%)</td><td>7.27 (+5.09%)</td><td>6.83 (+2.31%)</td><td>0.21 <b>(-22.54%)</b></td><td>5101.40 (-2.26%)</td><td>4846.16 (-2.49%)</td><td>4793.30 (-4.85%)</td><td>4746.60 (-0.52%)</td><td>146.25 <b>(-23.78%)</b></td><td>452.42 (+0.53%)</td><td>443.44 (+2.50%)</td><td>448.02 (+5.09%)</td><td>420.96 (+2.31%)</td><td>12.92 <b>(-22.54%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>7.31 (n/a)</td><td>7.02 (n/a)</td><td>6.92 (n/a)</td><td>6.68 (n/a)</td><td>0.27 (n/a)</td><td>5219.40 (n/a)</td><td>4969.70 (n/a)</td><td>5037.50 (n/a)</td><td>4771.60 (n/a)</td><td>191.88 (n/a)</td><td>450.06 (n/a)</td><td>432.63 (n/a)</td><td>426.30 (n/a)</td><td>411.44 (n/a)</td><td>16.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.79 (-0.00%)</td><td>0.79 (-0.07%)</td><td>0.79 (-0.09%)</td><td>0.79 (-0.15%)</td><td>0.00 <b>(+107.98%)</b></td><td>95679.50 (+0.15%)</td><td>95516.90 (+0.07%)</td><td>95516.70 (+0.09%)</td><td>95409.70 (+0.00%)</td><td>110.59 <b>(+108.31%)</b></td><td>720.26 (-0.00%)</td><td>719.45 (-0.07%)</td><td>719.45 (-0.09%)</td><td>718.23 (-0.15%)</td><td>0.83 <b>(+107.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95540.70 (n/a)</td><td>95450.80 (n/a)</td><td>95428.60 (n/a)</td><td>95405.40 (n/a)</td><td>53.09 (n/a)</td><td>720.29 (n/a)</td><td>719.95 (n/a)</td><td>720.11 (n/a)</td><td>719.27 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.74 (+0.01%)</td><td>0.74 (-0.03%)</td><td>0.74 (-0.00%)</td><td>0.73 (-0.10%)</td><td>0.00 <b>(+124.15%)</b></td><td>102755.40 (+0.10%)</td><td>102624.24 (+0.03%)</td><td>102585.90 (+0.00%)</td><td>102539.80 (-0.01%)</td><td>85.57 <b>(+124.32%)</b></td><td>670.17 (+0.01%)</td><td>669.62 (-0.03%)</td><td>669.87 (-0.00%)</td><td>668.77 (-0.10%)</td><td>0.56 <b>(+124.14%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102650.10 (n/a)</td><td>102591.10 (n/a)</td><td>102582.30 (n/a)</td><td>102549.60 (n/a)</td><td>38.15 (n/a)</td><td>670.11 (n/a)</td><td>669.84 (n/a)</td><td>669.90 (n/a)</td><td>669.45 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.70 (-0.02%)</td><td>0.70 (-0.13%)</td><td>0.70 (-0.16%)</td><td>0.70 (-0.28%)</td><td>0.00 <b>(+142.41%)</b></td><td>107698.80 (+0.29%)</td><td>107437.62 (+0.13%)</td><td>107426.60 (+0.16%)</td><td>107257.20 (+0.02%)</td><td>171.77 <b>(+143.26%)</b></td><td>640.70 (-0.02%)</td><td>639.62 (-0.13%)</td><td>639.69 (-0.16%)</td><td>638.07 (-0.28%)</td><td>1.02 <b>(+142.39%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107392.50 (n/a)</td><td>107293.72 (n/a)</td><td>107254.60 (n/a)</td><td>107237.70 (n/a)</td><td>70.61 (n/a)</td><td>640.81 (n/a)</td><td>640.48 (n/a)</td><td>640.71 (n/a)</td><td>639.89 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>4.25 (+17.66%)</td><td>3.57 (+9.18%)</td><td>3.73 (+15.97%)</td><td>2.96 (-0.55%)</td><td>0.51 <b>(+71.50%)</b></td><td>2721.50 (+0.55%)</td><td>2296.92 (-7.50%)</td><td>2163.90 (-13.77%)</td><td>1898.00 (-15.01%)</td><td>329.22 <b>(+47.91%)</b></td><td>1113.77 (+17.66%)</td><td>935.53 (+9.18%)</td><td>976.89 (+15.97%)</td><td>776.75 (-0.55%)</td><td>133.25 <b>(+71.50%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.61 (n/a)</td><td>3.27 (n/a)</td><td>3.21 (n/a)</td><td>2.98 (n/a)</td><td>0.30 (n/a)</td><td>2706.50 (n/a)</td><td>2483.22 (n/a)</td><td>2509.40 (n/a)</td><td>2233.10 (n/a)</td><td>222.59 (n/a)</td><td>946.63 (n/a)</td><td>856.85 (n/a)</td><td>842.40 (n/a)</td><td>781.07 (n/a)</td><td>77.70 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.41 (+18.86%)</td><td>0.33 (+1.49%)</td><td>0.31 (-6.29%)</td><td>0.27 (-5.44%)</td><td>0.05 <b>(+118.99%)</b></td><td>4542.10 (+5.76%)</td><td>3857.44 (-0.16%)</td><td>3969.00 (+6.71%)</td><td>3029.50 (-15.87%)</td><td>545.66 <b>(+89.90%)</b></td><td>22.15 (+18.86%)</td><td>17.70 (+1.49%)</td><td>16.91 (-6.29%)</td><td>14.77 (-5.44%)</td><td>2.73 <b>(+118.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.02 (n/a)</td><td>4294.90 (n/a)</td><td>3863.72 (n/a)</td><td>3719.30 (n/a)</td><td>3601.00 (n/a)</td><td>287.35 (n/a)</td><td>18.64 (n/a)</td><td>17.44 (n/a)</td><td>18.04 (n/a)</td><td>15.63 (n/a)</td><td>1.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.00 (+1.95%)</td><td>4.59 (+13.38%)</td><td>4.82 <b>(+31.60%)</b></td><td>3.53 (+6.27%)</td><td>0.60 (-17.36%)</td><td>1881.80 (-5.90%)</td><td>1474.26 (-12.52%)</td><td>1381.30 <b>(-24.01%)</b></td><td>1330.20 (-1.92%)</td><td>229.41 <b>(-20.08%)</b></td><td>1545.02 (+1.95%)</td><td>1416.94 (+13.38%)</td><td>1487.89 <b>(+31.60%)</b></td><td>1092.13 (+6.27%)</td><td>183.99 (-17.36%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>4.90 (n/a)</td><td>4.04 (n/a)</td><td>3.66 (n/a)</td><td>3.33 (n/a)</td><td>0.72 (n/a)</td><td>1999.80 (n/a)</td><td>1685.30 (n/a)</td><td>1817.80 (n/a)</td><td>1356.20 (n/a)</td><td>287.07 (n/a)</td><td>1515.41 (n/a)</td><td>1249.75 (n/a)</td><td>1130.63 (n/a)</td><td>1027.69 (n/a)</td><td>222.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.38 (n/a)</td><td>12.63 (n/a)</td><td>12.48 (n/a)</td><td>11.92 (n/a)</td><td>0.69 (n/a)</td><td>13.38 (n/a)</td><td>12.62 (n/a)</td><td>12.47 (n/a)</td><td>11.91 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>25.54 (+2.47%)</td><td>23.95 (-1.34%)</td><td>24.22 (-0.12%)</td><td>21.53 (-9.74%)</td><td>1.48 <b>(+233.58%)</b></td><td>25.53 (+2.47%)</td><td>23.94 (-1.34%)</td><td>24.21 (-0.12%)</td><td>21.52 (-9.74%)</td><td>1.48 <b>(+233.58%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>24.93 (n/a)</td><td>24.28 (n/a)</td><td>24.25 (n/a)</td><td>23.86 (n/a)</td><td>0.44 (n/a)</td><td>24.91 (n/a)</td><td>24.26 (n/a)</td><td>24.24 (n/a)</td><td>23.84 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>43.66 (+6.70%)</td><td>41.06 (+2.63%)</td><td>40.50 (+1.42%)</td><td>39.09 (+0.76%)</td><td>1.70 <b>(+111.24%)</b></td><td>43.63 (+6.70%)</td><td>41.04 (+2.63%)</td><td>40.48 (+1.42%)</td><td>39.07 (+0.76%)</td><td>1.70 <b>(+111.24%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>40.91 (n/a)</td><td>40.01 (n/a)</td><td>39.93 (n/a)</td><td>38.80 (n/a)</td><td>0.80 (n/a)</td><td>40.89 (n/a)</td><td>39.99 (n/a)</td><td>39.91 (n/a)</td><td>38.77 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>45.44 (-0.93%)</td><td>42.65 (-0.58%)</td><td>42.39 (-0.11%)</td><td>40.34 (-1.60%)</td><td>1.90 (+2.23%)</td><td>45.42 (-0.93%)</td><td>42.63 (-0.58%)</td><td>42.36 (-0.11%)</td><td>40.31 (-1.60%)</td><td>1.90 (+2.23%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>45.87 (n/a)</td><td>42.90 (n/a)</td><td>42.43 (n/a)</td><td>40.99 (n/a)</td><td>1.86 (n/a)</td><td>45.84 (n/a)</td><td>42.87 (n/a)</td><td>42.41 (n/a)</td><td>40.97 (n/a)</td><td>1.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.40 (n/a)</td><td>12.24 (n/a)</td><td>11.74 (n/a)</td><td>11.01 (n/a)</td><td>1.07 (n/a)</td><td>13.39 (n/a)</td><td>12.23 (n/a)</td><td>11.73 (n/a)</td><td>11.01 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>25.16 (+2.16%)</td><td>24.41 (+2.41%)</td><td>24.41 (+2.36%)</td><td>23.71 (+2.72%)</td><td>0.54 (-2.15%)</td><td>25.14 (+2.16%)</td><td>24.39 (+2.41%)</td><td>24.39 (+2.36%)</td><td>23.70 (+2.72%)</td><td>0.54 (-2.15%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>24.63 (n/a)</td><td>23.83 (n/a)</td><td>23.84 (n/a)</td><td>23.09 (n/a)</td><td>0.55 (n/a)</td><td>24.61 (n/a)</td><td>23.82 (n/a)</td><td>23.83 (n/a)</td><td>23.07 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>41.76 (+1.68%)</td><td>38.91 (-3.50%)</td><td>40.38 (-0.89%)</td><td>34.05 (-12.94%)</td><td>3.10 <b>(+259.59%)</b></td><td>41.74 (+1.68%)</td><td>38.88 (-3.50%)</td><td>40.35 (-0.89%)</td><td>34.03 (-12.94%)</td><td>3.10 <b>(+259.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>41.07 (n/a)</td><td>40.32 (n/a)</td><td>40.74 (n/a)</td><td>39.12 (n/a)</td><td>0.86 (n/a)</td><td>41.05 (n/a)</td><td>40.30 (n/a)</td><td>40.72 (n/a)</td><td>39.09 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>43.49 (-10.16%)</td><td>41.48 (-3.27%)</td><td>42.54 (-0.64%)</td><td>37.63 (-3.45%)</td><td>2.30 <b>(-41.57%)</b></td><td>43.46 (-10.16%)</td><td>41.46 (-3.27%)</td><td>42.51 (-0.64%)</td><td>37.61 (-3.45%)</td><td>2.30 <b>(-41.57%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>48.41 (n/a)</td><td>42.88 (n/a)</td><td>42.81 (n/a)</td><td>38.98 (n/a)</td><td>3.94 (n/a)</td><td>48.38 (n/a)</td><td>42.86 (n/a)</td><td>42.78 (n/a)</td><td>38.96 (n/a)</td><td>3.94 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.20 (+6.24%)</td><td>8.67 (+1.95%)</td><td>8.67 (+1.60%)</td><td>7.93 (-5.23%)</td><td>0.48 <b>(+317.58%)</b></td><td>9.19 (+6.24%)</td><td>8.66 (+1.95%)</td><td>8.65 (+1.60%)</td><td>7.91 (-5.23%)</td><td>0.48 <b>(+317.58%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>8.66 (n/a)</td><td>8.51 (n/a)</td><td>8.53 (n/a)</td><td>8.36 (n/a)</td><td>0.11 (n/a)</td><td>8.65 (n/a)</td><td>8.49 (n/a)</td><td>8.52 (n/a)</td><td>8.35 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.12 <b>(+21.90%)</b></td><td>0.94 (+11.00%)</td><td>0.93 (+6.45%)</td><td>0.84 (+9.45%)</td><td>0.11 <b>(+78.12%)</b></td><td>1.10 <b>(+21.90%)</b></td><td>0.92 (+11.00%)</td><td>0.91 (+6.45%)</td><td>0.82 (+9.45%)</td><td>0.11 <b>(+78.12%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.92 (n/a)</td><td>0.84 (n/a)</td><td>0.87 (n/a)</td><td>0.77 (n/a)</td><td>0.06 (n/a)</td><td>0.90 (n/a)</td><td>0.83 (n/a)</td><td>0.86 (n/a)</td><td>0.75 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.33 (-3.28%)</td><td>1.21 (-0.43%)</td><td>1.24 (+2.30%)</td><td>1.06 (-5.48%)</td><td>0.11 (+4.91%)</td><td>1.32 (-3.28%)</td><td>1.19 (-0.43%)</td><td>1.22 (+2.30%)</td><td>1.05 (-5.48%)</td><td>0.11 (+4.91%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.38 (n/a)</td><td>1.21 (n/a)</td><td>1.21 (n/a)</td><td>1.12 (n/a)</td><td>0.10 (n/a)</td><td>1.36 (n/a)</td><td>1.20 (n/a)</td><td>1.19 (n/a)</td><td>1.11 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>16.30 (-8.61%)</td><td>14.80 (-11.15%)</td><td>15.21 (-8.46%)</td><td>12.46 <b>(-21.58%)</b></td><td>1.62 <b>(+121.38%)</b></td><td>16.11 (-8.61%)</td><td>14.63 (-11.15%)</td><td>15.03 (-8.46%)</td><td>12.32 <b>(-21.58%)</b></td><td>1.60 <b>(+121.38%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>17.83 (n/a)</td><td>16.66 (n/a)</td><td>16.62 (n/a)</td><td>15.89 (n/a)</td><td>0.73 (n/a)</td><td>17.62 (n/a)</td><td>16.47 (n/a)</td><td>16.42 (n/a)</td><td>15.71 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>14.29 (+2.37%)</td><td>13.53 (+0.01%)</td><td>13.66 (+1.36%)</td><td>12.16 (-7.88%)</td><td>0.84 <b>(+204.69%)</b></td><td>14.04 (+2.37%)</td><td>13.29 (+0.01%)</td><td>13.42 (+1.36%)</td><td>11.95 (-7.88%)</td><td>0.83 <b>(+204.68%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.96 (n/a)</td><td>13.53 (n/a)</td><td>13.47 (n/a)</td><td>13.21 (n/a)</td><td>0.28 (n/a)</td><td>13.72 (n/a)</td><td>13.29 (n/a)</td><td>13.24 (n/a)</td><td>12.97 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>8.83 (-12.46%)</td><td>7.68 (-10.01%)</td><td>7.13 (-11.53%)</td><td>6.84 (-9.63%)</td><td>1.00 (-10.86%)</td><td>8.68 (-12.46%)</td><td>7.55 (-10.01%)</td><td>7.01 (-11.53%)</td><td>6.72 (-9.63%)</td><td>0.98 (-10.86%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>10.09 (n/a)</td><td>8.53 (n/a)</td><td>8.06 (n/a)</td><td>7.57 (n/a)</td><td>1.12 (n/a)</td><td>9.91 (n/a)</td><td>8.39 (n/a)</td><td>7.92 (n/a)</td><td>7.44 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>6.49 (+11.26%)</td><td>5.68 (+6.62%)</td><td>5.48 (-0.48%)</td><td>4.98 (+6.78%)</td><td>0.59 <b>(+31.81%)</b></td><td>6.38 (+11.26%)</td><td>5.59 (+6.62%)</td><td>5.39 (-0.48%)</td><td>4.90 (+6.78%)</td><td>0.58 <b>(+31.81%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.83 (n/a)</td><td>5.33 (n/a)</td><td>5.51 (n/a)</td><td>4.66 (n/a)</td><td>0.45 (n/a)</td><td>5.74 (n/a)</td><td>5.25 (n/a)</td><td>5.42 (n/a)</td><td>4.59 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.09 (n/a)</td><td>12.47 (n/a)</td><td>12.95 (n/a)</td><td>10.87 (n/a)</td><td>0.93 (n/a)</td><td>13.09 (n/a)</td><td>12.46 (n/a)</td><td>12.94 (n/a)</td><td>10.86 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.48 (n/a)</td><td>12.83 (n/a)</td><td>13.14 (n/a)</td><td>12.11 (n/a)</td><td>0.62 (n/a)</td><td>13.47 (n/a)</td><td>12.83 (n/a)</td><td>13.13 (n/a)</td><td>12.10 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>172.74 (n/a)</td><td>160.50 (n/a)</td><td>140.80 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>316.40 (n/a)</td><td>192.02 (n/a)</td><td>164.60 (n/a)</td><td>151.00 (n/a)</td><td>70.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>168.64 (n/a)</td><td>186.40 (n/a)</td><td>125.80 (n/a)</td><td>39.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>363.90 (n/a)</td><td>190.60 (n/a)</td><td>147.30 (n/a)</td><td>122.60 (n/a)</td><td>100.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>173.34 (n/a)</td><td>179.20 (n/a)</td><td>125.80 (n/a)</td><td>37.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.50 (n/a)</td><td>181.46 (n/a)</td><td>181.60 (n/a)</td><td>173.60 (n/a)</td><td>6.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.60 (n/a)</td><td>187.74 (n/a)</td><td>179.80 (n/a)</td><td>146.60 (n/a)</td><td>37.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.90 (n/a)</td><td>217.48 (n/a)</td><td>205.50 (n/a)</td><td>191.20 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.80 (n/a)</td><td>187.42 (n/a)</td><td>185.60 (n/a)</td><td>145.70 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>354.60 (n/a)</td><td>214.82 (n/a)</td><td>220.90 (n/a)</td><td>92.30 (n/a)</td><td>95.95 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>170.20 (n/a)</td><td>166.40 (n/a)</td><td>145.30 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.90 (n/a)</td><td>189.28 (n/a)</td><td>203.80 (n/a)</td><td>133.20 (n/a)</td><td>52.05 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>167.14 (n/a)</td><td>177.70 (n/a)</td><td>121.20 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>290.10 (n/a)</td><td>205.26 (n/a)</td><td>205.20 (n/a)</td><td>151.00 (n/a)</td><td>52.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>182.32 (n/a)</td><td>177.70 (n/a)</td><td>151.00 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.70 (n/a)</td><td>182.42 (n/a)</td><td>179.40 (n/a)</td><td>170.80 (n/a)</td><td>10.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>182.50 (n/a)</td><td>151.94 (n/a)</td><td>155.00 (n/a)</td><td>124.40 (n/a)</td><td>21.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>191.36 (n/a)</td><td>188.90 (n/a)</td><td>166.00 (n/a)</td><td>24.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>230.30 (n/a)</td><td>171.06 (n/a)</td><td>180.30 (n/a)</td><td>124.70 (n/a)</td><td>45.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.30 (n/a)</td><td>151.32 (n/a)</td><td>139.60 (n/a)</td><td>131.80 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.50 (n/a)</td><td>156.12 (n/a)</td><td>148.60 (n/a)</td><td>125.40 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>170.74 (n/a)</td><td>180.50 (n/a)</td><td>140.50 (n/a)</td><td>19.41 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>175.12 (n/a)</td><td>185.90 (n/a)</td><td>148.20 (n/a)</td><td>22.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>325.00 (n/a)</td><td>242.50 (n/a)</td><td>246.80 (n/a)</td><td>182.10 (n/a)</td><td>61.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>222.00 (n/a)</td><td>160.76 (n/a)</td><td>145.70 (n/a)</td><td>128.90 (n/a)</td><td>38.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>221.70 (n/a)</td><td>164.48 (n/a)</td><td>162.60 (n/a)</td><td>124.80 (n/a)</td><td>37.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>222.30 (n/a)</td><td>183.64 (n/a)</td><td>181.70 (n/a)</td><td>150.80 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>225.00 (n/a)</td><td>191.46 (n/a)</td><td>187.60 (n/a)</td><td>170.10 (n/a)</td><td>21.96 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.00 (n/a)</td><td>201.22 (n/a)</td><td>217.30 (n/a)</td><td>140.10 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>250.50 (n/a)</td><td>185.54 (n/a)</td><td>170.90 (n/a)</td><td>158.20 (n/a)</td><td>37.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>243.60 (n/a)</td><td>190.94 (n/a)</td><td>202.90 (n/a)</td><td>134.80 (n/a)</td><td>43.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>329.40 (n/a)</td><td>241.18 (n/a)</td><td>232.20 (n/a)</td><td>180.80 (n/a)</td><td>55.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (-1.90%)</td><td>0.03 (+1.55%)</td><td>0.03 (-1.27%)</td><td>0.02 (+5.55%)</td><td>0.00 (-3.44%)</td><td>174.80 (-5.26%)</td><td>148.16 (-1.71%)</td><td>145.90 (+1.25%)</td><td>125.00 (+1.96%)</td><td>21.29 (-7.65%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.50 (n/a)</td><td>150.74 (n/a)</td><td>144.10 (n/a)</td><td>122.60 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 <b>(-20.74%)</b></td><td>0.02 (-5.53%)</td><td>0.02 (-4.02%)</td><td>0.02 (+7.87%)</td><td>0.00 <b>(-62.61%)</b></td><td>188.00 (-7.34%)</td><td>172.64 (+3.89%)</td><td>169.10 (+4.19%)</td><td>161.30 <b>(+26.21%)</b></td><td>11.97 <b>(-55.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.90 (n/a)</td><td>166.18 (n/a)</td><td>162.30 (n/a)</td><td>127.80 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 <b>(-20.70%)</b></td><td>0.02 (-13.69%)</td><td>0.02 (-11.55%)</td><td>0.02 (-17.12%)</td><td>0.00 <b>(-34.81%)</b></td><td>212.20 <b>(+20.64%)</b></td><td>179.46 (+14.91%)</td><td>181.10 (+13.05%)</td><td>144.70 <b>(+26.16%)</b></td><td>24.53 (-0.07%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>175.90 (n/a)</td><td>156.18 (n/a)</td><td>160.20 (n/a)</td><td>114.70 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 <b>(-22.52%)</b></td><td>0.02 (-8.17%)</td><td>0.02 (+1.04%)</td><td>0.02 (+9.67%)</td><td>0.00 <b>(-50.73%)</b></td><td>238.90 (-8.82%)</td><td>185.32 (+4.22%)</td><td>175.70 (-1.01%)</td><td>159.60 <b>(+29.13%)</b></td><td>31.07 <b>(-41.00%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>262.00 (n/a)</td><td>177.82 (n/a)</td><td>177.50 (n/a)</td><td>123.60 (n/a)</td><td>52.66 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+11.51%)</td><td>0.02 (+8.64%)</td><td>0.02 (+9.22%)</td><td>0.02 (+12.39%)</td><td>0.00 (+11.86%)</td><td>199.90 (-11.00%)</td><td>167.94 (-7.99%)</td><td>164.50 (-8.46%)</td><td>132.30 (-10.37%)</td><td>25.08 (-11.90%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.60 (n/a)</td><td>182.52 (n/a)</td><td>179.70 (n/a)</td><td>147.60 (n/a)</td><td>28.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+0.21%)</td><td>0.02 (-5.90%)</td><td>0.02 (-10.48%)</td><td>0.01 (-12.08%)</td><td>0.01 <b>(+27.58%)</b></td><td>287.30 (+13.74%)</td><td>206.54 (+8.85%)</td><td>191.70 (+11.71%)</td><td>157.20 (-0.19%)</td><td>56.20 <b>(+40.79%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.60 (n/a)</td><td>189.74 (n/a)</td><td>171.60 (n/a)</td><td>157.50 (n/a)</td><td>39.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 <b>(-23.40%)</b></td><td>0.02 (+4.20%)</td><td>0.02 <b>(+20.26%)</b></td><td>0.02 <b>(+21.02%)</b></td><td>0.00 <b>(-57.78%)</b></td><td>221.50 (-17.38%)</td><td>183.40 (-8.67%)</td><td>169.90 (-16.88%)</td><td>161.50 <b>(+30.56%)</b></td><td>24.79 <b>(-51.66%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.10 (n/a)</td><td>200.80 (n/a)</td><td>204.40 (n/a)</td><td>123.70 (n/a)</td><td>51.27 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-17.66%)</td><td>0.02 <b>(-20.53%)</b></td><td>0.02 (-17.76%)</td><td>0.02 <b>(-23.84%)</b></td><td>0.00 (-6.48%)</td><td>271.50 <b>(+31.29%)</b></td><td>235.88 <b>(+26.29%)</b></td><td>231.60 <b>(+21.57%)</b></td><td>195.00 <b>(+21.42%)</b></td><td>29.63 <b>(+48.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.80 (n/a)</td><td>186.78 (n/a)</td><td>190.50 (n/a)</td><td>160.60 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-6.24%)</td><td>0.05 (-4.87%)</td><td>0.05 (-1.53%)</td><td>0.02 <b>(-34.82%)</b></td><td>0.02 <b>(+27.64%)</b></td><td>372.90 <b>(+53.46%)</b></td><td>194.70 (+14.54%)</td><td>151.50 (+1.54%)</td><td>137.40 (+6.68%)</td><td>100.24 <b>(+117.08%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.00 (n/a)</td><td>169.98 (n/a)</td><td>149.20 (n/a)</td><td>128.80 (n/a)</td><td>46.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (+4.47%)</td><td>0.05 (+9.25%)</td><td>0.05 (+13.94%)</td><td>0.05 (+19.71%)</td><td>0.01 <b>(-24.93%)</b></td><td>171.00 (-16.46%)</td><td>152.00 (-10.08%)</td><td>159.90 (-12.24%)</td><td>124.00 (-4.25%)</td><td>20.45 <b>(-38.65%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>169.04 (n/a)</td><td>182.20 (n/a)</td><td>129.50 (n/a)</td><td>33.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 <b>(+47.23%)</b></td><td>0.05 <b>(+26.62%)</b></td><td>0.05 (+18.93%)</td><td>0.04 <b>(+22.29%)</b></td><td>0.01 <b>(+94.80%)</b></td><td>199.40 (-18.25%)</td><td>159.64 <b>(-20.12%)</b></td><td>159.60 (-15.91%)</td><td>125.50 <b>(-32.09%)</b></td><td>26.76 (+7.05%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>243.90 (n/a)</td><td>199.84 (n/a)</td><td>189.80 (n/a)</td><td>184.80 (n/a)</td><td>25.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 <b>(+38.34%)</b></td><td>0.06 <b>(+21.72%)</b></td><td>0.05 (+9.17%)</td><td>0.05 (+4.51%)</td><td>0.01 <b>(+202.01%)</b></td><td>176.50 (-4.28%)</td><td>147.80 (-15.35%)</td><td>164.50 (-8.36%)</td><td>108.50 <b>(-27.71%)</b></td><td>29.45 <b>(+112.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>184.40 (n/a)</td><td>174.60 (n/a)</td><td>179.50 (n/a)</td><td>150.10 (n/a)</td><td>13.88 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 <b>(+20.92%)</b></td><td>0.05 (+6.58%)</td><td>0.05 (+4.58%)</td><td>0.04 (-11.63%)</td><td>0.01 <b>(+133.54%)</b></td><td>212.60 (+13.15%)</td><td>163.48 (-3.65%)</td><td>163.20 (-4.39%)</td><td>122.60 (-17.27%)</td><td>33.43 <b>(+119.06%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>169.68 (n/a)</td><td>170.70 (n/a)</td><td>148.20 (n/a)</td><td>15.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-17.03%)</td><td>0.05 (-0.89%)</td><td>0.05 (+0.31%)</td><td>0.04 <b>(+71.23%)</b></td><td>0.01 <b>(-66.31%)</b></td><td>201.30 <b>(-41.60%)</b></td><td>178.22 (-10.46%)</td><td>178.80 (-0.28%)</td><td>148.90 <b>(+20.57%)</b></td><td>20.98 <b>(-76.33%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>344.70 (n/a)</td><td>199.04 (n/a)</td><td>179.30 (n/a)</td><td>123.50 (n/a)</td><td>88.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (+4.94%)</td><td>0.05 (+1.88%)</td><td>0.04 (-11.17%)</td><td>0.04 (-2.37%)</td><td>0.01 <b>(+44.90%)</b></td><td>206.60 (+2.43%)</td><td>172.94 (+0.53%)</td><td>197.60 (+12.59%)</td><td>123.80 (-4.77%)</td><td>38.67 <b>(+48.82%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>172.02 (n/a)</td><td>175.50 (n/a)</td><td>130.00 (n/a)</td><td>25.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (-12.31%)</td><td>0.05 (-5.72%)</td><td>0.05 (+11.73%)</td><td>0.03 (-15.09%)</td><td>0.01 (-5.91%)</td><td>234.90 (+17.74%)</td><td>184.58 (+6.46%)</td><td>165.70 (-10.53%)</td><td>155.20 (+14.03%)</td><td>35.93 <b>(+23.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>173.38 (n/a)</td><td>185.20 (n/a)</td><td>136.10 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 <b>(+25.58%)</b></td><td>0.04 (+1.13%)</td><td>0.04 (-13.99%)</td><td>0.03 (+12.31%)</td><td>0.02 <b>(+45.14%)</b></td><td>304.40 (-10.97%)</td><td>211.04 (+1.82%)</td><td>203.40 (+16.30%)</td><td>124.70 <b>(-20.37%)</b></td><td>74.65 (-2.07%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>341.90 (n/a)</td><td>207.26 (n/a)</td><td>174.90 (n/a)</td><td>156.60 (n/a)</td><td>76.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (-3.68%)</td><td>0.04 (-5.58%)</td><td>0.04 (+4.44%)</td><td>0.03 <b>(-27.35%)</b></td><td>0.01 <b>(+28.35%)</b></td><td>325.70 <b>(+37.66%)</b></td><td>226.24 (+8.66%)</td><td>210.60 (-4.23%)</td><td>172.20 (+3.86%)</td><td>58.11 <b>(+92.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.60 (n/a)</td><td>208.20 (n/a)</td><td>219.90 (n/a)</td><td>165.80 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (+13.13%)</td><td>0.11 (+17.40%)</td><td>0.10 <b>(+22.42%)</b></td><td>0.09 (+12.49%)</td><td>0.02 (+7.13%)</td><td>192.70 (-11.12%)</td><td>155.64 (-15.03%)</td><td>158.40 (-18.35%)</td><td>123.10 (-11.57%)</td><td>26.00 (-15.27%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.80 (n/a)</td><td>183.16 (n/a)</td><td>194.00 (n/a)</td><td>139.20 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (-3.63%)</td><td>0.10 (-6.25%)</td><td>0.10 (-6.01%)</td><td>0.07 <b>(-23.25%)</b></td><td>0.03 <b>(+55.19%)</b></td><td>241.80 <b>(+30.28%)</b></td><td>174.68 (+11.26%)</td><td>164.50 (+6.40%)</td><td>126.60 (+3.77%)</td><td>49.14 <b>(+110.52%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.60 (n/a)</td><td>157.00 (n/a)</td><td>154.60 (n/a)</td><td>122.00 (n/a)</td><td>23.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 <b>(+27.87%)</b></td><td>0.13 <b>(+40.19%)</b></td><td>0.13 <b>(+39.52%)</b></td><td>0.11 <b>(+44.50%)</b></td><td>0.01 (-18.80%)</td><td>144.50 <b>(-30.76%)</b></td><td>129.82 <b>(-29.22%)</b></td><td>130.20 <b>(-28.34%)</b></td><td>119.70 <b>(-21.76%)</b></td><td>9.79 <b>(-56.44%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>183.42 (n/a)</td><td>181.70 (n/a)</td><td>153.00 (n/a)</td><td>22.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (+8.53%)</td><td>0.10 (+5.65%)</td><td>0.09 (+9.86%)</td><td>0.08 (+2.59%)</td><td>0.02 (+10.41%)</td><td>206.20 (-2.55%)</td><td>175.22 (-5.14%)</td><td>188.00 (-8.96%)</td><td>127.30 (-7.89%)</td><td>33.32 (-2.69%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.60 (n/a)</td><td>184.72 (n/a)</td><td>206.50 (n/a)</td><td>138.20 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 <b>(-25.48%)</b></td><td>0.09 (-8.30%)</td><td>0.09 (+1.93%)</td><td>0.08 (-6.66%)</td><td>0.01 <b>(-60.20%)</b></td><td>214.40 (+7.15%)</td><td>190.24 (+7.32%)</td><td>183.80 (-1.92%)</td><td>178.20 <b>(+34.19%)</b></td><td>15.37 <b>(-41.20%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.10 (n/a)</td><td>177.26 (n/a)</td><td>187.40 (n/a)</td><td>132.80 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (+7.69%)</td><td>0.11 <b>(+22.25%)</b></td><td>0.11 <b>(+35.00%)</b></td><td>0.09 <b>(+23.92%)</b></td><td>0.01 (-19.56%)</td><td>178.10 (-19.30%)</td><td>152.80 (-19.32%)</td><td>147.40 <b>(-25.89%)</b></td><td>126.20 (-7.14%)</td><td>20.38 <b>(-37.22%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.70 (n/a)</td><td>189.38 (n/a)</td><td>198.90 (n/a)</td><td>135.90 (n/a)</td><td>32.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (+17.49%)</td><td>0.09 (+2.20%)</td><td>0.09 (-2.29%)</td><td>0.07 (-3.66%)</td><td>0.01 <b>(+91.04%)</b></td><td>226.80 (+3.80%)</td><td>190.74 (-1.05%)</td><td>191.50 (+2.35%)</td><td>151.90 (-14.85%)</td><td>26.75 <b>(+65.24%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>192.76 (n/a)</td><td>187.10 (n/a)</td><td>178.40 (n/a)</td><td>16.19 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (+12.92%)</td><td>0.09 (+13.31%)</td><td>0.08 (+11.60%)</td><td>0.07 <b>(+37.20%)</b></td><td>0.01 (-9.72%)</td><td>224.90 <b>(-27.12%)</b></td><td>196.68 (-13.41%)</td><td>207.40 (-10.41%)</td><td>151.40 (-11.46%)</td><td>31.41 <b>(-41.05%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>308.60 (n/a)</td><td>227.14 (n/a)</td><td>231.50 (n/a)</td><td>171.00 (n/a)</td><td>53.27 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (-0.85%)</td><td>0.21 (+13.17%)</td><td>0.20 (+12.84%)</td><td>0.16 <b>(+26.21%)</b></td><td>0.03 <b>(-27.85%)</b></td><td>199.40 <b>(-20.75%)</b></td><td>162.92 (-13.90%)</td><td>167.50 (-11.42%)</td><td>132.80 (+0.84%)</td><td>25.64 <b>(-42.05%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>251.60 (n/a)</td><td>189.22 (n/a)</td><td>189.10 (n/a)</td><td>131.70 (n/a)</td><td>44.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (+1.50%)</td><td>0.19 (-1.75%)</td><td>0.18 (+0.71%)</td><td>0.13 <b>(-25.26%)</b></td><td>0.05 <b>(+44.08%)</b></td><td>246.90 <b>(+33.82%)</b></td><td>176.98 (+4.93%)</td><td>178.30 (-0.67%)</td><td>126.90 (-1.48%)</td><td>44.78 <b>(+95.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.50 (n/a)</td><td>168.66 (n/a)</td><td>179.50 (n/a)</td><td>128.80 (n/a)</td><td>22.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (+13.51%)</td><td>0.20 (-4.93%)</td><td>0.20 (-8.13%)</td><td>0.14 <b>(-21.00%)</b></td><td>0.05 <b>(+111.41%)</b></td><td>240.60 <b>(+26.56%)</b></td><td>172.60 (+8.98%)</td><td>166.30 (+8.84%)</td><td>126.40 (-11.92%)</td><td>42.77 <b>(+134.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>190.10 (n/a)</td><td>158.38 (n/a)</td><td>152.80 (n/a)</td><td>143.50 (n/a)</td><td>18.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (-12.14%)</td><td>0.20 (-10.95%)</td><td>0.22 (-6.31%)</td><td>0.13 <b>(-25.14%)</b></td><td>0.04 (-2.20%)</td><td>251.90 <b>(+33.56%)</b></td><td>170.62 (+14.04%)</td><td>150.20 (+6.68%)</td><td>139.10 (+13.74%)</td><td>46.82 <b>(+54.81%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.60 (n/a)</td><td>149.62 (n/a)</td><td>140.80 (n/a)</td><td>122.30 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (+15.49%)</td><td>0.19 (+15.18%)</td><td>0.19 <b>(+22.77%)</b></td><td>0.12 (+11.86%)</td><td>0.06 <b>(+22.41%)</b></td><td>272.50 (-10.63%)</td><td>182.52 (-12.25%)</td><td>174.00 (-18.58%)</td><td>128.10 (-13.45%)</td><td>60.58 (-5.49%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>304.90 (n/a)</td><td>208.00 (n/a)</td><td>213.70 (n/a)</td><td>148.00 (n/a)</td><td>64.10 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (+0.63%)</td><td>0.19 (+3.72%)</td><td>0.19 (+1.58%)</td><td>0.12 (+1.48%)</td><td>0.04 (+7.15%)</td><td>270.10 (-1.46%)</td><td>184.52 (-3.10%)</td><td>172.90 (-1.54%)</td><td>139.00 (-0.64%)</td><td>51.56 (+2.98%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>274.10 (n/a)</td><td>190.42 (n/a)</td><td>175.60 (n/a)</td><td>139.90 (n/a)</td><td>50.07 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (-3.93%)</td><td>0.16 (+5.04%)</td><td>0.17 (+6.01%)</td><td>0.14 <b>(+30.23%)</b></td><td>0.02 <b>(-46.43%)</b></td><td>231.70 <b>(-23.23%)</b></td><td>201.58 (-7.44%)</td><td>192.10 (-5.69%)</td><td>182.00 (+4.12%)</td><td>21.07 <b>(-58.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>301.80 (n/a)</td><td>217.78 (n/a)</td><td>203.70 (n/a)</td><td>174.80 (n/a)</td><td>50.33 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (-13.89%)</td><td>0.02 (-4.64%)</td><td>0.03 (+10.31%)</td><td>0.02 (-2.91%)</td><td>0.00 <b>(-39.41%)</b></td><td>205.60 (+3.01%)</td><td>173.10 (+2.95%)</td><td>160.50 (-9.32%)</td><td>150.10 (+16.09%)</td><td>24.03 <b>(-27.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.60 (n/a)</td><td>168.14 (n/a)</td><td>177.00 (n/a)</td><td>129.30 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+11.69%)</td><td>0.02 (-3.28%)</td><td>0.02 (-3.20%)</td><td>0.02 (-17.35%)</td><td>0.01 <b>(+79.76%)</b></td><td>236.00 <b>(+20.96%)</b></td><td>174.12 (+6.40%)</td><td>168.30 (+3.25%)</td><td>124.60 (-10.49%)</td><td>40.02 <b>(+94.01%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>163.64 (n/a)</td><td>163.00 (n/a)</td><td>139.20 (n/a)</td><td>20.63 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-3.65%)</td><td>0.02 (-12.82%)</td><td>0.02 (-16.94%)</td><td>0.01 <b>(-33.41%)</b></td><td>0.00 <b>(+75.97%)</b></td><td>349.70 <b>(+50.15%)</b></td><td>235.70 <b>(+20.23%)</b></td><td>234.50 <b>(+20.38%)</b></td><td>172.30 (+3.80%)</td><td>69.55 <b>(+176.49%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.90 (n/a)</td><td>196.04 (n/a)</td><td>194.80 (n/a)</td><td>166.00 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-2.42%)</td><td>0.02 (-5.48%)</td><td>0.02 (+0.41%)</td><td>0.02 (-2.78%)</td><td>0.00 (+1.39%)</td><td>249.50 (+2.89%)</td><td>216.10 (+6.04%)</td><td>211.40 (-0.38%)</td><td>166.00 (+2.47%)</td><td>34.43 (+9.53%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.50 (n/a)</td><td>203.80 (n/a)</td><td>212.20 (n/a)</td><td>162.00 (n/a)</td><td>31.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 <b>(-21.98%)</b></td><td>0.02 (-15.96%)</td><td>0.02 <b>(-21.48%)</b></td><td>0.02 (-7.16%)</td><td>0.00 <b>(-44.50%)</b></td><td>205.30 (+7.71%)</td><td>187.02 (+17.20%)</td><td>196.90 <b>(+27.36%)</b></td><td>160.80 <b>(+28.23%)</b></td><td>21.53 <b>(-25.01%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.60 (n/a)</td><td>159.58 (n/a)</td><td>154.60 (n/a)</td><td>125.40 (n/a)</td><td>28.71 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 <b>(+31.01%)</b></td><td>0.03 (+1.06%)</td><td>0.02 (-7.09%)</td><td>0.02 (-7.10%)</td><td>0.01 <b>(+112.59%)</b></td><td>220.60 (+7.61%)</td><td>167.64 (+3.37%)</td><td>171.80 (+7.64%)</td><td>106.60 <b>(-23.69%)</b></td><td>43.37 <b>(+68.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>162.18 (n/a)</td><td>159.60 (n/a)</td><td>139.70 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 <b>(+40.64%)</b></td><td>0.03 <b>(+20.49%)</b></td><td>0.03 (+8.37%)</td><td>0.02 (+15.23%)</td><td>0.01 <b>(+85.77%)</b></td><td>199.40 (-13.23%)</td><td>158.24 (-14.52%)</td><td>153.60 (-7.75%)</td><td>107.90 <b>(-28.92%)</b></td><td>40.40 (+18.06%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.80 (n/a)</td><td>185.12 (n/a)</td><td>166.50 (n/a)</td><td>151.80 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+16.69%)</td><td>0.03 (+4.63%)</td><td>0.02 (+6.62%)</td><td>0.02 (-11.15%)</td><td>0.00 <b>(+92.76%)</b></td><td>223.90 (+12.57%)</td><td>168.92 (-2.27%)</td><td>164.20 (-6.23%)</td><td>129.20 (-14.27%)</td><td>34.34 <b>(+89.70%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.90 (n/a)</td><td>172.84 (n/a)</td><td>175.10 (n/a)</td><td>150.70 (n/a)</td><td>18.10 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+12.39%)</td><td>0.02 (+12.63%)</td><td>0.02 (+10.95%)</td><td>0.02 (+7.84%)</td><td>0.01 <b>(+24.69%)</b></td><td>237.40 (-7.27%)</td><td>186.58 (-10.38%)</td><td>204.80 (-9.86%)</td><td>137.80 (-11.04%)</td><td>43.60 (+0.66%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.00 (n/a)</td><td>208.20 (n/a)</td><td>227.20 (n/a)</td><td>154.90 (n/a)</td><td>43.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-19.08%)</td><td>0.02 (-8.12%)</td><td>0.02 (-4.16%)</td><td>0.02 (+0.48%)</td><td>0.00 <b>(-58.64%)</b></td><td>208.70 (-0.48%)</td><td>188.38 (+6.57%)</td><td>191.00 (+4.37%)</td><td>168.50 <b>(+23.62%)</b></td><td>15.80 <b>(-49.62%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.70 (n/a)</td><td>176.76 (n/a)</td><td>183.00 (n/a)</td><td>136.30 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 <b>(-24.19%)</b></td><td>0.02 (-8.53%)</td><td>0.03 (+1.46%)</td><td>0.02 (-4.41%)</td><td>0.00 <b>(-46.56%)</b></td><td>212.70 (+4.62%)</td><td>167.64 (+6.44%)</td><td>163.10 (-1.39%)</td><td>143.00 <b>(+31.92%)</b></td><td>27.47 <b>(-23.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>157.50 (n/a)</td><td>165.40 (n/a)</td><td>108.40 (n/a)</td><td>36.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+17.68%)</td><td>0.03 (+7.66%)</td><td>0.02 (-1.32%)</td><td>0.02 (+0.59%)</td><td>0.01 <b>(+52.60%)</b></td><td>215.00 (-0.60%)</td><td>167.58 (-4.66%)</td><td>182.30 (+1.33%)</td><td>121.40 (-15.05%)</td><td>41.74 <b>(+28.61%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.30 (n/a)</td><td>175.78 (n/a)</td><td>179.90 (n/a)</td><td>142.90 (n/a)</td><td>32.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (-1.31%)</td><td>0.02 (+1.34%)</td><td>0.02 (-7.94%)</td><td>0.02 <b>(+39.54%)</b></td><td>0.01 <b>(-21.56%)</b></td><td>211.70 <b>(-28.36%)</b></td><td>186.96 (-5.31%)</td><td>201.30 (+8.58%)</td><td>128.00 (+1.35%)</td><td>34.53 <b>(-44.81%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>295.50 (n/a)</td><td>197.44 (n/a)</td><td>185.40 (n/a)</td><td>126.30 (n/a)</td><td>62.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-18.35%)</td><td>0.02 (-19.82%)</td><td>0.02 <b>(-23.56%)</b></td><td>0.02 (-3.82%)</td><td>0.00 <b>(-42.17%)</b></td><td>222.30 (+3.98%)</td><td>205.28 <b>(+22.86%)</b></td><td>211.60 <b>(+30.86%)</b></td><td>166.40 <b>(+22.44%)</b></td><td>22.50 <b>(-27.51%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.80 (n/a)</td><td>167.08 (n/a)</td><td>161.70 (n/a)</td><td>135.90 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-14.91%)</td><td>0.02 (-10.38%)</td><td>0.02 (-8.93%)</td><td>0.02 (-1.22%)</td><td>0.00 <b>(-31.21%)</b></td><td>244.90 (+1.24%)</td><td>211.74 (+10.47%)</td><td>211.70 (+9.80%)</td><td>180.70 (+17.49%)</td><td>27.11 (-18.62%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.90 (n/a)</td><td>191.68 (n/a)</td><td>192.80 (n/a)</td><td>153.80 (n/a)</td><td>33.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-13.81%)</td><td>0.02 (-12.86%)</td><td>0.02 (-0.62%)</td><td>0.02 (-14.76%)</td><td>0.00 (-9.09%)</td><td>256.80 (+17.31%)</td><td>204.68 (+15.16%)</td><td>186.00 (+0.65%)</td><td>172.90 (+16.04%)</td><td>37.07 <b>(+26.88%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.90 (n/a)</td><td>177.74 (n/a)</td><td>184.80 (n/a)</td><td>149.00 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 <b>(+24.86%)</b></td><td>0.04 (-5.50%)</td><td>0.05 (+14.55%)</td><td>0.02 <b>(-45.32%)</b></td><td>0.02 <b>(+130.59%)</b></td><td>399.80 <b>(+82.89%)</b></td><td>230.24 <b>(+22.39%)</b></td><td>180.10 (-12.70%)</td><td>123.30 (-19.88%)</td><td>110.94 <b>(+256.37%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>188.12 (n/a)</td><td>206.30 (n/a)</td><td>153.90 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-8.27%)</td><td>0.05 (-3.90%)</td><td>0.05 (+2.59%)</td><td>0.04 (-4.07%)</td><td>0.01 <b>(-23.14%)</b></td><td>184.90 (+4.23%)</td><td>159.80 (+3.51%)</td><td>156.40 (-2.55%)</td><td>138.50 (+8.97%)</td><td>18.56 (-11.96%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.40 (n/a)</td><td>154.38 (n/a)</td><td>160.50 (n/a)</td><td>127.10 (n/a)</td><td>21.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (+18.14%)</td><td>0.04 (+12.23%)</td><td>0.04 (+5.08%)</td><td>0.04 <b>(+73.18%)</b></td><td>0.01 (-13.54%)</td><td>222.80 <b>(-42.26%)</b></td><td>197.38 (-15.84%)</td><td>207.50 (-4.86%)</td><td>136.90 (-15.39%)</td><td>34.38 <b>(-61.11%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>385.90 (n/a)</td><td>234.52 (n/a)</td><td>218.10 (n/a)</td><td>161.80 (n/a)</td><td>88.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (+0.07%)</td><td>0.04 (+7.51%)</td><td>0.04 (+10.34%)</td><td>0.03 (+7.34%)</td><td>0.01 (-2.02%)</td><td>235.90 (-6.83%)</td><td>204.06 (-7.12%)</td><td>208.50 (-9.35%)</td><td>174.60 (-0.06%)</td><td>27.08 (-8.65%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.20 (n/a)</td><td>219.70 (n/a)</td><td>230.00 (n/a)</td><td>174.70 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 <b>(+29.95%)</b></td><td>0.05 (+8.73%)</td><td>0.05 (+2.02%)</td><td>0.03 (-5.12%)</td><td>0.01 <b>(+112.37%)</b></td><td>241.20 (+5.42%)</td><td>181.04 (-5.51%)</td><td>179.40 (-1.97%)</td><td>131.00 <b>(-23.03%)</b></td><td>39.49 <b>(+70.64%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>228.80 (n/a)</td><td>191.60 (n/a)</td><td>183.00 (n/a)</td><td>170.20 (n/a)</td><td>23.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 <b>(+26.73%)</b></td><td>0.05 (+17.87%)</td><td>0.05 (+11.21%)</td><td>0.04 (+7.29%)</td><td>0.01 <b>(+55.30%)</b></td><td>210.30 (-6.78%)</td><td>163.28 (-13.73%)</td><td>159.20 (-10.11%)</td><td>118.30 <b>(-21.08%)</b></td><td>36.37 (+11.08%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>189.26 (n/a)</td><td>177.10 (n/a)</td><td>149.90 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (+17.42%)</td><td>0.06 <b>(+26.32%)</b></td><td>0.06 <b>(+37.33%)</b></td><td>0.04 (+9.32%)</td><td>0.01 <b>(+25.65%)</b></td><td>184.60 (-8.52%)</td><td>143.76 <b>(-20.54%)</b></td><td>137.80 <b>(-27.17%)</b></td><td>124.70 (-14.82%)</td><td>23.88 (-1.22%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>180.92 (n/a)</td><td>189.20 (n/a)</td><td>146.40 (n/a)</td><td>24.17 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (+12.16%)</td><td>0.05 (+13.80%)</td><td>0.05 (-6.69%)</td><td>0.04 <b>(+84.11%)</b></td><td>0.01 (-19.09%)</td><td>208.50 <b>(-45.69%)</b></td><td>173.12 <b>(-20.02%)</b></td><td>181.00 (+7.16%)</td><td>116.00 (-10.84%)</td><td>38.59 <b>(-61.97%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>383.90 (n/a)</td><td>216.46 (n/a)</td><td>168.90 (n/a)</td><td>130.10 (n/a)</td><td>101.48 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (+3.95%)</td><td>0.04 (-13.94%)</td><td>0.04 <b>(-20.21%)</b></td><td>0.03 <b>(-35.01%)</b></td><td>0.01 <b>(+243.73%)</b></td><td>267.90 <b>(+53.88%)</b></td><td>195.58 <b>(+21.72%)</b></td><td>201.20 <b>(+25.36%)</b></td><td>141.50 (-3.81%)</td><td>49.21 <b>(+404.32%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>174.10 (n/a)</td><td>160.68 (n/a)</td><td>160.50 (n/a)</td><td>147.10 (n/a)</td><td>9.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (+6.91%)</td><td>0.05 (+0.65%)</td><td>0.05 (+4.56%)</td><td>0.04 (-12.99%)</td><td>0.01 <b>(+80.85%)</b></td><td>204.70 (+14.94%)</td><td>163.90 (+1.17%)</td><td>159.40 (-4.32%)</td><td>133.70 (-6.50%)</td><td>29.70 <b>(+93.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.10 (n/a)</td><td>162.00 (n/a)</td><td>166.60 (n/a)</td><td>143.00 (n/a)</td><td>15.35 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 <b>(+34.94%)</b></td><td>0.05 <b>(+21.54%)</b></td><td>0.05 (+9.05%)</td><td>0.04 <b>(+60.45%)</b></td><td>0.01 (+7.69%)</td><td>222.60 <b>(-37.66%)</b></td><td>165.10 <b>(-21.42%)</b></td><td>163.30 (-8.26%)</td><td>112.40 <b>(-25.91%)</b></td><td>39.03 <b>(-53.58%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>357.10 (n/a)</td><td>210.10 (n/a)</td><td>178.00 (n/a)</td><td>151.70 (n/a)</td><td>84.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (+5.33%)</td><td>0.05 (+4.46%)</td><td>0.05 (+6.18%)</td><td>0.05 (+2.84%)</td><td>0.01 (+11.88%)</td><td>178.80 (-2.72%)</td><td>156.76 (-4.04%)</td><td>156.70 (-5.83%)</td><td>124.00 (-5.05%)</td><td>21.14 (+4.20%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.80 (n/a)</td><td>163.36 (n/a)</td><td>166.40 (n/a)</td><td>130.60 (n/a)</td><td>20.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-4.21%)</td><td>0.04 (+0.71%)</td><td>0.04 (-12.25%)</td><td>0.04 <b>(+61.15%)</b></td><td>0.01 <b>(-41.02%)</b></td><td>220.80 <b>(-37.94%)</b></td><td>187.96 (-9.27%)</td><td>200.10 (+13.95%)</td><td>137.60 (+4.32%)</td><td>31.70 <b>(-64.27%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>355.80 (n/a)</td><td>207.16 (n/a)</td><td>175.60 (n/a)</td><td>131.90 (n/a)</td><td>88.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-5.07%)</td><td>0.05 (+2.88%)</td><td>0.05 (+8.25%)</td><td>0.04 <b>(+46.82%)</b></td><td>0.01 <b>(-37.19%)</b></td><td>200.50 <b>(-31.90%)</b></td><td>170.24 (-8.83%)</td><td>172.40 (-7.66%)</td><td>127.70 (+5.28%)</td><td>30.30 <b>(-54.77%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>294.40 (n/a)</td><td>186.72 (n/a)</td><td>186.70 (n/a)</td><td>121.30 (n/a)</td><td>66.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 <b>(+25.61%)</b></td><td>0.05 (+16.26%)</td><td>0.05 (+15.52%)</td><td>0.04 <b>(+24.34%)</b></td><td>0.01 <b>(+26.02%)</b></td><td>209.50 (-19.58%)</td><td>176.02 (-14.02%)</td><td>175.20 (-13.44%)</td><td>133.00 <b>(-20.41%)</b></td><td>28.12 <b>(-21.82%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.50 (n/a)</td><td>204.72 (n/a)</td><td>202.40 (n/a)</td><td>167.10 (n/a)</td><td>35.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (-7.76%)</td><td>0.04 (-0.68%)</td><td>0.04 (-6.70%)</td><td>0.04 (+6.15%)</td><td>0.01 <b>(-31.58%)</b></td><td>205.80 (-5.77%)</td><td>184.50 (-0.50%)</td><td>194.80 (+7.15%)</td><td>162.30 (+8.42%)</td><td>20.46 <b>(-32.98%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>185.42 (n/a)</td><td>181.80 (n/a)</td><td>149.70 (n/a)</td><td>30.53 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (-12.52%)</td><td>0.10 (-11.43%)</td><td>0.10 (-13.85%)</td><td>0.10 (+3.54%)</td><td>0.01 <b>(-53.87%)</b></td><td>170.80 (-3.39%)</td><td>160.90 (+11.80%)</td><td>159.00 (+16.14%)</td><td>147.40 (+14.35%)</td><td>9.88 <b>(-49.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.80 (n/a)</td><td>143.92 (n/a)</td><td>136.90 (n/a)</td><td>128.90 (n/a)</td><td>19.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (+16.48%)</td><td>0.11 (+9.50%)</td><td>0.10 (+5.14%)</td><td>0.09 (+3.98%)</td><td>0.02 <b>(+52.92%)</b></td><td>176.90 (-3.81%)</td><td>154.88 (-8.00%)</td><td>162.00 (-4.93%)</td><td>122.40 (-14.17%)</td><td>20.75 <b>(+23.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>168.34 (n/a)</td><td>170.40 (n/a)</td><td>142.60 (n/a)</td><td>16.78 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (-5.84%)</td><td>0.07 (-7.97%)</td><td>0.07 (-8.09%)</td><td>0.06 (-14.76%)</td><td>0.01 (+14.99%)</td><td>295.40 (+17.32%)</td><td>235.32 (+9.78%)</td><td>224.50 (+8.77%)</td><td>187.50 (+6.23%)</td><td>43.51 <b>(+42.33%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>251.80 (n/a)</td><td>214.36 (n/a)</td><td>206.40 (n/a)</td><td>176.50 (n/a)</td><td>30.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (-12.02%)</td><td>0.08 (-9.48%)</td><td>0.08 (-9.39%)</td><td>0.05 <b>(-23.74%)</b></td><td>0.02 (+5.09%)</td><td>313.70 <b>(+31.09%)</b></td><td>209.00 (+13.34%)</td><td>197.40 (+10.34%)</td><td>149.40 (+13.61%)</td><td>63.60 <b>(+63.09%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.30 (n/a)</td><td>184.40 (n/a)</td><td>178.90 (n/a)</td><td>131.50 (n/a)</td><td>39.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (-6.63%)</td><td>0.10 (+0.07%)</td><td>0.10 (-5.45%)</td><td>0.08 (+11.70%)</td><td>0.01 <b>(-40.40%)</b></td><td>200.80 (-10.48%)</td><td>163.46 (-3.04%)</td><td>158.70 (+5.73%)</td><td>142.20 (+7.08%)</td><td>24.05 <b>(-42.47%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.30 (n/a)</td><td>168.58 (n/a)</td><td>150.10 (n/a)</td><td>132.80 (n/a)</td><td>41.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (+13.92%)</td><td>0.10 (+16.88%)</td><td>0.10 (+14.86%)</td><td>0.09 <b>(+26.80%)</b></td><td>0.01 (-15.29%)</td><td>177.40 <b>(-21.16%)</b></td><td>159.06 (-15.32%)</td><td>164.50 (-12.92%)</td><td>133.40 (-12.24%)</td><td>17.40 <b>(-41.51%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>187.84 (n/a)</td><td>188.90 (n/a)</td><td>152.00 (n/a)</td><td>29.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (-8.80%)</td><td>0.10 (-1.73%)</td><td>0.09 (-4.66%)</td><td>0.08 (+14.32%)</td><td>0.02 <b>(-33.87%)</b></td><td>201.40 (-12.51%)</td><td>171.50 (-0.78%)</td><td>174.50 (+4.87%)</td><td>133.30 (+9.71%)</td><td>24.80 <b>(-37.96%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.20 (n/a)</td><td>172.84 (n/a)</td><td>166.40 (n/a)</td><td>121.50 (n/a)</td><td>39.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (+12.09%)</td><td>0.10 (+7.26%)</td><td>0.10 (-0.18%)</td><td>0.09 <b>(+27.20%)</b></td><td>0.02 (-2.84%)</td><td>187.30 <b>(-21.40%)</b></td><td>162.04 (-8.07%)</td><td>165.50 (+0.18%)</td><td>118.50 (-10.77%)</td><td>27.49 <b>(-33.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>238.30 (n/a)</td><td>176.26 (n/a)</td><td>165.20 (n/a)</td><td>132.80 (n/a)</td><td>41.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (+6.73%)</td><td>0.09 (-1.37%)</td><td>0.09 (-1.89%)</td><td>0.07 (-3.81%)</td><td>0.01 <b>(+45.33%)</b></td><td>223.00 (+3.96%)</td><td>191.10 (+2.02%)</td><td>183.20 (+1.95%)</td><td>163.20 (-6.31%)</td><td>23.49 <b>(+42.06%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>187.32 (n/a)</td><td>179.70 (n/a)</td><td>174.20 (n/a)</td><td>16.53 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (+1.59%)</td><td>0.11 (+20.00%)</td><td>0.10 (+12.88%)</td><td>0.08 (+15.73%)</td><td>0.03 (-2.10%)</td><td>204.20 (-13.58%)</td><td>155.10 (-17.67%)</td><td>166.40 (-11.40%)</td><td>116.00 (-1.61%)</td><td>37.55 (-19.65%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>236.30 (n/a)</td><td>188.38 (n/a)</td><td>187.80 (n/a)</td><td>117.90 (n/a)</td><td>46.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 <b>(+31.22%)</b></td><td>0.10 (+8.88%)</td><td>0.10 (+2.78%)</td><td>0.08 (+2.26%)</td><td>0.02 <b>(+129.21%)</b></td><td>200.40 (-2.24%)</td><td>167.62 (-6.18%)</td><td>169.80 (-2.69%)</td><td>123.00 <b>(-23.79%)</b></td><td>30.11 <b>(+69.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>178.66 (n/a)</td><td>174.50 (n/a)</td><td>161.40 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (-5.45%)</td><td>0.11 (+17.81%)</td><td>0.11 (+0.06%)</td><td>0.10 <b>(+90.61%)</b></td><td>0.01 <b>(-60.75%)</b></td><td>162.60 <b>(-47.51%)</b></td><td>147.26 <b>(-23.02%)</b></td><td>155.80 (-0.06%)</td><td>125.90 (+5.80%)</td><td>15.85 <b>(-78.86%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>309.80 (n/a)</td><td>191.30 (n/a)</td><td>155.90 (n/a)</td><td>119.00 (n/a)</td><td>74.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (+2.91%)</td><td>0.10 (+1.42%)</td><td>0.09 (-2.50%)</td><td>0.09 (+19.66%)</td><td>0.02 <b>(-22.00%)</b></td><td>189.50 (-16.45%)</td><td>166.82 (-3.65%)</td><td>175.90 (+2.57%)</td><td>124.50 (-2.81%)</td><td>25.95 <b>(-37.06%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.80 (n/a)</td><td>173.14 (n/a)</td><td>171.50 (n/a)</td><td>128.10 (n/a)</td><td>41.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 <b>(-23.95%)</b></td><td>0.09 (-11.20%)</td><td>0.09 (-16.14%)</td><td>0.08 (+9.72%)</td><td>0.01 <b>(-69.48%)</b></td><td>201.40 (-8.87%)</td><td>180.62 (+7.76%)</td><td>176.00 (+19.24%)</td><td>165.70 <b>(+31.51%)</b></td><td>15.26 <b>(-64.26%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.00 (n/a)</td><td>167.62 (n/a)</td><td>147.60 (n/a)</td><td>126.00 (n/a)</td><td>42.70 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (+19.19%)</td><td>0.10 (+5.63%)</td><td>0.09 (-7.42%)</td><td>0.08 (+3.73%)</td><td>0.02 <b>(+44.91%)</b></td><td>207.40 (-3.58%)</td><td>172.14 (-3.94%)</td><td>172.80 (+8.00%)</td><td>129.00 (-16.12%)</td><td>35.26 (+19.74%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>179.20 (n/a)</td><td>160.00 (n/a)</td><td>153.80 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 <b>(-26.39%)</b></td><td>0.09 (-6.93%)</td><td>0.09 (+2.54%)</td><td>0.09 (+3.25%)</td><td>0.01 <b>(-75.27%)</b></td><td>192.60 (-3.12%)</td><td>180.06 (+4.31%)</td><td>182.50 (-2.46%)</td><td>165.70 <b>(+35.82%)</b></td><td>10.33 <b>(-67.26%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.80 (n/a)</td><td>172.62 (n/a)</td><td>187.10 (n/a)</td><td>122.00 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (+19.82%)</td><td>0.20 (+18.31%)</td><td>0.19 (+4.79%)</td><td>0.17 <b>(+86.46%)</b></td><td>0.04 <b>(-25.99%)</b></td><td>196.20 <b>(-46.36%)</b></td><td>168.70 <b>(-21.87%)</b></td><td>170.30 (-4.54%)</td><td>123.70 (-16.53%)</td><td>28.06 <b>(-68.40%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>365.80 (n/a)</td><td>215.92 (n/a)</td><td>178.40 (n/a)</td><td>148.20 (n/a)</td><td>88.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (+19.97%)</td><td>0.23 <b>(+23.51%)</b></td><td>0.25 <b>(+32.72%)</b></td><td>0.19 <b>(+21.06%)</b></td><td>0.03 <b>(+21.70%)</b></td><td>173.50 (-17.42%)</td><td>142.32 (-19.02%)</td><td>130.60 <b>(-24.68%)</b></td><td>128.20 (-16.64%)</td><td>19.40 (-15.98%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.10 (n/a)</td><td>175.74 (n/a)</td><td>173.40 (n/a)</td><td>153.80 (n/a)</td><td>23.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 <b>(+27.41%)</b></td><td>0.16 (+8.62%)</td><td>0.14 (-1.45%)</td><td>0.14 (+2.22%)</td><td>0.02 <b>(+298.34%)</b></td><td>232.20 (-2.19%)</td><td>211.14 (-6.47%)</td><td>230.50 (+1.45%)</td><td>167.80 <b>(-21.52%)</b></td><td>29.38 <b>(+212.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>225.74 (n/a)</td><td>227.20 (n/a)</td><td>213.80 (n/a)</td><td>9.41 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 <b>(-27.94%)</b></td><td>0.15 (-12.42%)</td><td>0.17 (+1.19%)</td><td>0.11 <b>(-29.37%)</b></td><td>0.03 <b>(-26.00%)</b></td><td>309.50 <b>(+41.58%)</b></td><td>220.32 (+14.59%)</td><td>197.60 (-1.20%)</td><td>189.30 <b>(+38.78%)</b></td><td>50.47 <b>(+52.05%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.60 (n/a)</td><td>192.26 (n/a)</td><td>200.00 (n/a)</td><td>136.40 (n/a)</td><td>33.19 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (+2.75%)</td><td>0.18 (-15.48%)</td><td>0.18 (-7.30%)</td><td>0.11 <b>(-38.97%)</b></td><td>0.06 <b>(+108.63%)</b></td><td>296.60 <b>(+63.87%)</b></td><td>205.82 <b>(+28.61%)</b></td><td>182.40 (+7.87%)</td><td>127.10 (-2.68%)</td><td>71.63 <b>(+244.52%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>181.00 (n/a)</td><td>160.04 (n/a)</td><td>169.10 (n/a)</td><td>130.60 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (+9.30%)</td><td>0.20 (-0.51%)</td><td>0.18 (-3.64%)</td><td>0.14 (-17.85%)</td><td>0.05 <b>(+66.21%)</b></td><td>236.00 <b>(+21.71%)</b></td><td>177.02 (+4.15%)</td><td>182.30 (+3.76%)</td><td>125.60 (-8.52%)</td><td>45.46 <b>(+78.71%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.90 (n/a)</td><td>169.96 (n/a)</td><td>175.70 (n/a)</td><td>137.30 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (+1.71%)</td><td>0.19 (-6.39%)</td><td>0.21 (-0.54%)</td><td>0.15 <b>(-20.67%)</b></td><td>0.03 <b>(+116.59%)</b></td><td>222.20 <b>(+26.11%)</b></td><td>174.66 (+9.20%)</td><td>159.20 (+0.51%)</td><td>142.50 (-1.66%)</td><td>32.88 <b>(+170.53%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>176.20 (n/a)</td><td>159.94 (n/a)</td><td>158.40 (n/a)</td><td>144.90 (n/a)</td><td>12.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 (-1.25%)</td><td>0.16 (-19.84%)</td><td>0.16 (-17.67%)</td><td>0.09 <b>(-50.85%)</b></td><td>0.05 <b>(+291.11%)</b></td><td>353.80 <b>(+103.45%)</b></td><td>224.28 <b>(+34.77%)</b></td><td>205.90 <b>(+21.47%)</b></td><td>152.60 (+1.26%)</td><td>77.70 <b>(+744.79%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>173.90 (n/a)</td><td>166.42 (n/a)</td><td>169.50 (n/a)</td><td>150.70 (n/a)</td><td>9.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (-10.81%)</td><td>0.21 (+15.44%)</td><td>0.21 (+19.07%)</td><td>0.19 <b>(+36.76%)</b></td><td>0.02 <b>(-65.83%)</b></td><td>171.80 <b>(-26.86%)</b></td><td>154.76 (-16.88%)</td><td>155.50 (-15.99%)</td><td>140.10 (+12.17%)</td><td>11.90 <b>(-71.34%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>234.90 (n/a)</td><td>186.18 (n/a)</td><td>185.10 (n/a)</td><td>124.90 (n/a)</td><td>41.53 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 <b>(+40.99%)</b></td><td>0.19 (+13.59%)</td><td>0.16 (-3.43%)</td><td>0.15 (+5.24%)</td><td>0.04 <b>(+188.54%)</b></td><td>216.20 (-4.97%)</td><td>181.62 (-9.25%)</td><td>200.60 (+3.56%)</td><td>127.30 <b>(-29.08%)</b></td><td>36.10 <b>(+91.61%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>227.50 (n/a)</td><td>200.14 (n/a)</td><td>193.70 (n/a)</td><td>179.50 (n/a)</td><td>18.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (+1.81%)</td><td>0.21 (+10.92%)</td><td>0.21 (+9.31%)</td><td>0.17 <b>(+21.79%)</b></td><td>0.03 (-17.53%)</td><td>196.30 (-17.87%)</td><td>159.96 (-11.33%)</td><td>159.70 (-8.48%)</td><td>126.80 (-1.78%)</td><td>26.26 <b>(-33.16%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>239.00 (n/a)</td><td>180.40 (n/a)</td><td>174.50 (n/a)</td><td>129.10 (n/a)</td><td>39.28 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 <b>(+36.56%)</b></td><td>0.21 <b>(+20.45%)</b></td><td>0.18 (+13.34%)</td><td>0.18 <b>(+21.92%)</b></td><td>0.04 <b>(+69.15%)</b></td><td>180.40 (-17.96%)</td><td>161.82 (-16.18%)</td><td>177.30 (-11.75%)</td><td>122.00 <b>(-26.77%)</b></td><td>25.02 (+4.27%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.90 (n/a)</td><td>193.06 (n/a)</td><td>200.90 (n/a)</td><td>166.60 (n/a)</td><td>24.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.22 (+5.32%)</td><td>0.19 (+17.72%)</td><td>0.21 <b>(+55.05%)</b></td><td>0.13 (-0.89%)</td><td>0.04 (+10.61%)</td><td>255.90 (+0.91%)</td><td>184.08 (-14.66%)</td><td>156.10 <b>(-35.50%)</b></td><td>151.70 (-5.07%)</td><td>45.64 (+2.12%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>253.60 (n/a)</td><td>215.70 (n/a)</td><td>242.00 (n/a)</td><td>159.80 (n/a)</td><td>44.69 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (+1.36%)</td><td>0.18 (-0.43%)</td><td>0.17 (-6.35%)</td><td>0.13 (-18.77%)</td><td>0.05 <b>(+60.61%)</b></td><td>251.10 <b>(+23.09%)</b></td><td>187.84 (+4.03%)</td><td>198.20 (+6.79%)</td><td>139.20 (-1.35%)</td><td>48.22 <b>(+81.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>204.00 (n/a)</td><td>180.56 (n/a)</td><td>185.60 (n/a)</td><td>141.10 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 <b>(+21.76%)</b></td><td>0.19 (-1.68%)</td><td>0.17 (-8.00%)</td><td>0.14 (-19.18%)</td><td>0.05 <b>(+194.67%)</b></td><td>229.70 <b>(+23.76%)</b></td><td>179.98 (+6.35%)</td><td>189.50 (+8.66%)</td><td>121.50 (-17.85%)</td><td>42.55 <b>(+198.38%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.60 (n/a)</td><td>169.24 (n/a)</td><td>174.40 (n/a)</td><td>147.90 (n/a)</td><td>14.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (-7.28%)</td><td>0.21 (+7.22%)</td><td>0.22 (+5.48%)</td><td>0.19 <b>(+23.90%)</b></td><td>0.02 <b>(-53.25%)</b></td><td>172.60 (-19.31%)</td><td>155.58 (-9.00%)</td><td>149.90 (-5.19%)</td><td>143.10 (+7.84%)</td><td>13.36 <b>(-60.00%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>213.90 (n/a)</td><td>170.96 (n/a)</td><td>158.10 (n/a)</td><td>132.70 (n/a)</td><td>33.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (+0.79%)</td><td>0.18 (+0.17%)</td><td>0.18 (-0.18%)</td><td>0.18 (+0.11%)</td><td>0.00 <b>(+114.45%)</b></td><td>47457.20 (-0.11%)</td><td>47299.24 (-0.16%)</td><td>47412.90 (+0.18%)</td><td>46868.90 (-0.78%)</td><td>247.09 <b>(+112.31%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47510.10 (n/a)</td><td>47376.88 (n/a)</td><td>47326.50 (n/a)</td><td>47239.10 (n/a)</td><td>116.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (+0.04%)</td><td>0.18 (+0.01%)</td><td>0.18 (+0.00%)</td><td>0.18 (+0.01%)</td><td>0.00 (+10.79%)</td><td>47485.90 (-0.01%)</td><td>47391.12 (-0.01%)</td><td>47392.80 (-0.00%)</td><td>47312.20 (-0.04%)</td><td>65.21 (+10.77%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47491.20 (n/a)</td><td>47396.56 (n/a)</td><td>47393.40 (n/a)</td><td>47330.60 (n/a)</td><td>58.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (-0.01%)</td><td>0.11 (-0.02%)</td><td>0.11 (-0.03%)</td><td>0.11 (-0.04%)</td><td>0.00 <b>(+95.11%)</b></td><td>374624.10 (+0.04%)</td><td>374448.72 (+0.02%)</td><td>374463.50 (+0.03%)</td><td>374264.70 (+0.01%)</td><td>172.78 <b>(+94.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374462.50 (n/a)</td><td>374367.42 (n/a)</td><td>374368.90 (n/a)</td><td>374238.70 (n/a)</td><td>88.65 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (+11.24%)</td><td>0.17 (+16.01%)</td><td>0.18 <b>(+21.05%)</b></td><td>0.12 (+8.29%)</td><td>0.03 <b>(+29.19%)</b></td><td>198.80 (-7.66%)</td><td>149.60 (-13.23%)</td><td>134.00 (-17.39%)</td><td>131.00 (-10.09%)</td><td>28.86 (+5.75%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>215.30 (n/a)</td><td>172.40 (n/a)</td><td>162.20 (n/a)</td><td>145.70 (n/a)</td><td>27.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.39 <b>(+21.87%)</b></td><td>0.31 (+15.17%)</td><td>0.34 (+13.67%)</td><td>0.19 (-7.69%)</td><td>0.08 <b>(+50.94%)</b></td><td>260.50 (+8.36%)</td><td>172.88 (-10.14%)</td><td>144.80 (-12.03%)</td><td>126.70 (-17.94%)</td><td>56.04 <b>(+30.08%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>240.40 (n/a)</td><td>192.38 (n/a)</td><td>164.60 (n/a)</td><td>154.40 (n/a)</td><td>43.08 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.33 (+1.48%)</td><td>13.09 (+10.57%)</td><td>13.09 (+2.52%)</td><td>12.85 <b>(+60.46%)</b></td><td>0.22 <b>(-89.78%)</b></td><td>816.20 <b>(-37.68%)</b></td><td>801.16 (-12.69%)</td><td>800.80 (-2.46%)</td><td>786.40 (-1.45%)</td><td>13.49 <b>(-93.86%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.14 (n/a)</td><td>11.84 (n/a)</td><td>12.77 (n/a)</td><td>8.01 (n/a)</td><td>2.16 (n/a)</td><td>1309.70 (n/a)</td><td>917.64 (n/a)</td><td>821.00 (n/a)</td><td>798.00 (n/a)</td><td>219.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 (-4.12%)</td><td>0.25 (-4.94%)</td><td>0.24 (-5.47%)</td><td>0.23 (-0.61%)</td><td>0.03 (-11.14%)</td><td>181.50 (+0.61%)</td><td>163.84 (+4.94%)</td><td>173.20 (+5.80%)</td><td>134.60 (+4.34%)</td><td>18.97 (-6.64%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>180.40 (n/a)</td><td>156.12 (n/a)</td><td>163.70 (n/a)</td><td>129.00 (n/a)</td><td>20.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (-0.65%)</td><td>0.03 (-5.24%)</td><td>0.03 (-7.86%)</td><td>0.02 (-17.76%)</td><td>0.01 <b>(+77.02%)</b></td><td>223.50 <b>(+21.60%)</b></td><td>177.32 (+9.67%)</td><td>182.30 (+8.51%)</td><td>131.80 (+0.61%)</td><td>44.23 <b>(+113.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>183.80 (n/a)</td><td>161.68 (n/a)</td><td>168.00 (n/a)</td><td>131.00 (n/a)</td><td>20.71 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (-9.71%)</td><td>0.03 (-2.00%)</td><td>0.03 (-3.69%)</td><td>0.02 <b>(+29.54%)</b></td><td>0.01 <b>(-34.86%)</b></td><td>172.10 <b>(-22.83%)</b></td><td>144.44 (-2.63%)</td><td>155.20 (+3.88%)</td><td>111.00 (+10.78%)</td><td>26.34 <b>(-44.68%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>148.34 (n/a)</td><td>149.40 (n/a)</td><td>100.20 (n/a)</td><td>47.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (+17.33%)</td><td>0.04 (+13.69%)</td><td>0.04 (+1.94%)</td><td>0.03 <b>(+32.80%)</b></td><td>0.01 (+8.07%)</td><td>189.90 <b>(-24.67%)</b></td><td>162.34 (-12.72%)</td><td>170.40 (-1.90%)</td><td>132.60 (-14.73%)</td><td>24.93 <b>(-34.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.10 (n/a)</td><td>186.00 (n/a)</td><td>173.70 (n/a)</td><td>155.50 (n/a)</td><td>37.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (-11.39%)</td><td>0.03 (-9.67%)</td><td>0.02 <b>(-26.12%)</b></td><td>0.02 (+3.21%)</td><td>0.01 (-16.17%)</td><td>183.50 (-3.06%)</td><td>158.96 (+9.67%)</td><td>177.40 <b>(+35.32%)</b></td><td>123.50 (+12.89%)</td><td>30.18 (-9.54%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>144.94 (n/a)</td><td>131.10 (n/a)</td><td>109.40 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 <b>(+23.41%)</b></td><td>0.03 (+15.85%)</td><td>0.04 <b>(+30.24%)</b></td><td>0.03 (-5.03%)</td><td>0.01 <b>(+193.28%)</b></td><td>204.30 (+5.31%)</td><td>159.02 (-10.48%)</td><td>137.60 <b>(-23.26%)</b></td><td>125.90 (-18.93%)</td><td>37.51 <b>(+156.44%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.00 (n/a)</td><td>177.64 (n/a)</td><td>179.30 (n/a)</td><td>155.30 (n/a)</td><td>14.63 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (-0.14%)</td><td>0.03 (-7.82%)</td><td>0.03 (-16.63%)</td><td>0.02 (-7.01%)</td><td>0.00 (-14.47%)</td><td>184.50 (+7.58%)</td><td>157.32 (+8.00%)</td><td>155.90 (+19.92%)</td><td>127.40 (+0.16%)</td><td>20.96 (-9.49%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.50 (n/a)</td><td>145.66 (n/a)</td><td>130.00 (n/a)</td><td>127.20 (n/a)</td><td>23.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (+7.58%)</td><td>0.04 (+14.62%)</td><td>0.04 <b>(+27.07%)</b></td><td>0.03 (+5.18%)</td><td>0.01 <b>(+24.50%)</b></td><td>182.10 (-4.96%)</td><td>148.64 (-12.33%)</td><td>139.20 <b>(-21.31%)</b></td><td>128.10 (-7.04%)</td><td>23.53 (+9.45%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.60 (n/a)</td><td>169.54 (n/a)</td><td>176.90 (n/a)</td><td>137.80 (n/a)</td><td>21.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (-2.60%)</td><td>0.02 (-7.49%)</td><td>0.02 (-19.04%)</td><td>0.02 (+8.25%)</td><td>0.00 (-19.97%)</td><td>204.60 (-7.63%)</td><td>175.08 (+6.42%)</td><td>190.60 <b>(+23.53%)</b></td><td>133.10 (+2.70%)</td><td>30.51 <b>(-22.21%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>164.52 (n/a)</td><td>154.30 (n/a)</td><td>129.60 (n/a)</td><td>39.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (-17.83%)</td><td>0.03 (-3.01%)</td><td>0.03 <b>(+31.66%)</b></td><td>0.02 (-7.74%)</td><td>0.01 <b>(-31.52%)</b></td><td>295.90 (+8.39%)</td><td>190.22 (+0.27%)</td><td>158.50 <b>(-24.02%)</b></td><td>154.10 <b>(+21.72%)</b></td><td>60.47 (-2.22%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>273.00 (n/a)</td><td>189.70 (n/a)</td><td>208.60 (n/a)</td><td>126.60 (n/a)</td><td>61.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+6.99%)</td><td>0.02 (+2.42%)</td><td>0.02 (-3.71%)</td><td>0.02 (+6.39%)</td><td>0.00 <b>(+31.42%)</b></td><td>193.90 (-6.01%)</td><td>171.66 (-1.73%)</td><td>185.90 (+3.85%)</td><td>139.00 (-6.59%)</td><td>25.69 (+16.77%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.30 (n/a)</td><td>174.68 (n/a)</td><td>179.00 (n/a)</td><td>148.80 (n/a)</td><td>22.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (-2.54%)</td><td>0.03 (-0.62%)</td><td>0.03 (+0.11%)</td><td>0.02 (-6.98%)</td><td>0.01 (+5.57%)</td><td>216.40 (+7.50%)</td><td>167.26 (+1.30%)</td><td>169.80 (-0.12%)</td><td>126.30 (+2.60%)</td><td>37.79 (+13.30%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>165.12 (n/a)</td><td>170.00 (n/a)</td><td>123.10 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+14.69%)</td><td>0.02 (+4.46%)</td><td>0.03 (+12.00%)</td><td>0.02 <b>(-20.41%)</b></td><td>0.00 <b>(+251.43%)</b></td><td>231.90 <b>(+25.62%)</b></td><td>171.30 (-1.78%)</td><td>156.20 (-10.69%)</td><td>144.10 (-12.77%)</td><td>34.93 <b>(+300.65%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.60 (n/a)</td><td>174.40 (n/a)</td><td>174.90 (n/a)</td><td>165.20 (n/a)</td><td>8.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+18.82%)</td><td>0.02 (-6.78%)</td><td>0.02 (-11.78%)</td><td>0.01 <b>(-30.50%)</b></td><td>0.01 <b>(+171.61%)</b></td><td>332.10 <b>(+43.89%)</b></td><td>236.14 (+12.86%)</td><td>227.90 (+13.33%)</td><td>160.80 (-15.86%)</td><td>64.07 <b>(+227.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.80 (n/a)</td><td>209.24 (n/a)</td><td>201.10 (n/a)</td><td>191.10 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+12.97%)</td><td>0.02 (-4.14%)</td><td>0.02 (+0.92%)</td><td>0.01 <b>(-32.12%)</b></td><td>0.01 <b>(+107.63%)</b></td><td>303.40 <b>(+47.28%)</b></td><td>198.02 (+11.45%)</td><td>180.20 (-0.93%)</td><td>135.50 (-11.44%)</td><td>66.95 <b>(+179.43%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.00 (n/a)</td><td>177.68 (n/a)</td><td>181.90 (n/a)</td><td>153.00 (n/a)</td><td>23.96 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 <b>(+40.21%)</b></td><td>0.02 (+17.74%)</td><td>0.02 (+10.54%)</td><td>0.02 (-5.83%)</td><td>0.01 <b>(+399.81%)</b></td><td>244.80 (+6.20%)</td><td>194.74 (-11.50%)</td><td>200.00 (-9.54%)</td><td>143.10 <b>(-28.70%)</b></td><td>44.28 <b>(+279.94%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.50 (n/a)</td><td>220.04 (n/a)</td><td>221.10 (n/a)</td><td>200.70 (n/a)</td><td>11.65 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (-4.28%)</td><td>0.02 (-7.45%)</td><td>0.02 (-6.12%)</td><td>0.01 <b>(-30.48%)</b></td><td>0.00 <b>(+71.10%)</b></td><td>316.00 <b>(+43.83%)</b></td><td>222.94 (+12.10%)</td><td>219.20 (+6.51%)</td><td>173.10 (+4.47%)</td><td>58.23 <b>(+148.92%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.70 (n/a)</td><td>198.88 (n/a)</td><td>205.80 (n/a)</td><td>165.70 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-16.19%)</td><td>0.05 (-2.68%)</td><td>0.06 (+8.22%)</td><td>0.04 (-7.47%)</td><td>0.01 <b>(-20.71%)</b></td><td>218.70 (+8.05%)</td><td>161.12 (+1.79%)</td><td>141.70 (-7.57%)</td><td>127.90 (+19.31%)</td><td>38.52 (+1.18%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>158.28 (n/a)</td><td>153.30 (n/a)</td><td>107.20 (n/a)</td><td>38.08 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (+16.25%)</td><td>0.07 (-7.71%)</td><td>0.06 (-19.65%)</td><td>0.05 (-15.31%)</td><td>0.02 <b>(+108.66%)</b></td><td>232.80 (+18.11%)</td><td>184.70 (+11.86%)</td><td>197.50 <b>(+24.45%)</b></td><td>127.70 (-13.95%)</td><td>39.63 <b>(+104.57%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>165.12 (n/a)</td><td>158.70 (n/a)</td><td>148.40 (n/a)</td><td>19.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (+15.09%)</td><td>0.05 <b>(+21.70%)</b></td><td>0.05 (+9.17%)</td><td>0.04 <b>(+69.27%)</b></td><td>0.01 (-15.97%)</td><td>198.80 <b>(-40.92%)</b></td><td>158.28 <b>(-22.49%)</b></td><td>160.00 (-8.41%)</td><td>126.20 (-13.15%)</td><td>31.89 <b>(-59.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>336.50 (n/a)</td><td>204.20 (n/a)</td><td>174.70 (n/a)</td><td>145.30 (n/a)</td><td>78.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-10.42%)</td><td>0.05 (-13.52%)</td><td>0.05 (+2.54%)</td><td>0.04 <b>(-30.20%)</b></td><td>0.01 <b>(+40.20%)</b></td><td>285.10 <b>(+43.27%)</b></td><td>211.92 (+19.42%)</td><td>187.20 (-2.50%)</td><td>165.50 (+11.67%)</td><td>53.66 <b>(+122.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>177.46 (n/a)</td><td>192.00 (n/a)</td><td>148.20 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (+8.83%)</td><td>0.05 <b>(+22.70%)</b></td><td>0.05 <b>(+31.40%)</b></td><td>0.05 <b>(+33.72%)</b></td><td>0.00 <b>(-44.51%)</b></td><td>162.30 <b>(-25.21%)</b></td><td>150.52 (-19.65%)</td><td>150.00 <b>(-23.90%)</b></td><td>135.40 (-8.14%)</td><td>10.48 <b>(-61.29%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>187.34 (n/a)</td><td>197.10 (n/a)</td><td>147.40 (n/a)</td><td>27.06 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-17.04%)</td><td>0.05 (-5.98%)</td><td>0.05 (-6.49%)</td><td>0.04 (-1.61%)</td><td>0.01 <b>(-41.07%)</b></td><td>230.90 (+1.63%)</td><td>190.30 (+4.73%)</td><td>188.80 (+6.97%)</td><td>166.00 <b>(+20.55%)</b></td><td>24.63 <b>(-26.16%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>181.70 (n/a)</td><td>176.50 (n/a)</td><td>137.70 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (-0.24%)</td><td>0.05 (+6.67%)</td><td>0.05 (+0.46%)</td><td>0.04 (-1.46%)</td><td>0.01 (+6.84%)</td><td>213.00 (+1.48%)</td><td>160.16 (-5.73%)</td><td>165.80 (-0.48%)</td><td>122.80 (+0.24%)</td><td>35.43 (+9.87%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>169.90 (n/a)</td><td>166.60 (n/a)</td><td>122.50 (n/a)</td><td>32.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-10.42%)</td><td>0.05 (-1.53%)</td><td>0.05 (+1.95%)</td><td>0.03 (-4.26%)</td><td>0.01 (-18.33%)</td><td>265.10 (+4.45%)</td><td>191.66 (+0.80%)</td><td>177.10 (-1.88%)</td><td>157.20 (+11.65%)</td><td>42.55 (-1.73%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>253.80 (n/a)</td><td>190.14 (n/a)</td><td>180.50 (n/a)</td><td>140.80 (n/a)</td><td>43.30 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 <b>(-34.49%)</b></td><td>0.05 (-6.82%)</td><td>0.05 (-1.08%)</td><td>0.05 (+14.71%)</td><td>0.00 <b>(-83.70%)</b></td><td>165.90 (-12.87%)</td><td>155.90 (+1.98%)</td><td>154.40 (+1.05%)</td><td>148.40 <b>(+52.67%)</b></td><td>7.89 <b>(-77.48%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>190.40 (n/a)</td><td>152.88 (n/a)</td><td>152.80 (n/a)</td><td>97.20 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-0.26%)</td><td>0.05 (-0.27%)</td><td>0.05 (-0.28%)</td><td>0.03 (-7.68%)</td><td>0.01 (+15.90%)</td><td>276.80 (+8.29%)</td><td>200.72 (+1.38%)</td><td>187.70 (+0.32%)</td><td>159.40 (+0.25%)</td><td>45.32 <b>(+27.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>255.60 (n/a)</td><td>197.98 (n/a)</td><td>187.10 (n/a)</td><td>159.00 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-5.85%)</td><td>0.05 (+1.05%)</td><td>0.04 (+4.30%)</td><td>0.04 (+7.60%)</td><td>0.01 <b>(-21.52%)</b></td><td>207.30 (-7.04%)</td><td>178.50 (-2.58%)</td><td>189.60 (-4.15%)</td><td>130.90 (+6.16%)</td><td>29.64 <b>(-21.33%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>183.22 (n/a)</td><td>197.80 (n/a)</td><td>123.30 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 <b>(+20.63%)</b></td><td>0.05 <b>(+30.69%)</b></td><td>0.05 <b>(+21.05%)</b></td><td>0.04 <b>(+64.74%)</b></td><td>0.01 <b>(-34.61%)</b></td><td>230.40 <b>(-39.30%)</b></td><td>191.58 <b>(-26.41%)</b></td><td>185.70 (-17.36%)</td><td>170.00 (-17.11%)</td><td>23.52 <b>(-67.11%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>379.60 (n/a)</td><td>260.32 (n/a)</td><td>224.70 (n/a)</td><td>205.10 (n/a)</td><td>71.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (-3.60%)</td><td>0.05 (+0.36%)</td><td>0.05 (-3.10%)</td><td>0.04 (+3.67%)</td><td>0.01 (-15.38%)</td><td>203.50 (-3.51%)</td><td>171.56 (-1.12%)</td><td>179.10 (+3.23%)</td><td>140.30 (+3.77%)</td><td>26.07 (-16.72%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>173.50 (n/a)</td><td>173.50 (n/a)</td><td>135.20 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 <b>(+39.97%)</b></td><td>0.05 <b>(+29.81%)</b></td><td>0.05 <b>(+37.39%)</b></td><td>0.04 <b>(+21.42%)</b></td><td>0.01 <b>(+79.43%)</b></td><td>226.00 (-17.64%)</td><td>175.34 <b>(-21.87%)</b></td><td>165.50 <b>(-27.22%)</b></td><td>134.80 <b>(-28.56%)</b></td><td>34.55 (+6.07%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.40 (n/a)</td><td>224.42 (n/a)</td><td>227.40 (n/a)</td><td>188.70 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 <b>(-21.02%)</b></td><td>0.04 (-0.93%)</td><td>0.04 (-0.62%)</td><td>0.04 <b>(+51.55%)</b></td><td>0.00 <b>(-68.80%)</b></td><td>215.60 <b>(-34.03%)</b></td><td>194.94 (-6.13%)</td><td>188.70 (+0.59%)</td><td>178.10 <b>(+26.58%)</b></td><td>17.94 <b>(-74.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>326.80 (n/a)</td><td>207.66 (n/a)</td><td>187.60 (n/a)</td><td>140.70 (n/a)</td><td>71.48 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (+11.60%)</td><td>0.11 (+0.32%)</td><td>0.10 (-7.02%)</td><td>0.08 (-6.37%)</td><td>0.02 <b>(+38.92%)</b></td><td>201.40 (+6.84%)</td><td>160.82 (+1.28%)</td><td>168.70 (+7.59%)</td><td>113.10 (-10.38%)</td><td>32.36 <b>(+28.11%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.50 (n/a)</td><td>158.78 (n/a)</td><td>156.80 (n/a)</td><td>126.20 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 (+4.65%)</td><td>0.17 (+18.90%)</td><td>0.17 (+13.79%)</td><td>0.13 <b>(+32.17%)</b></td><td>0.03 <b>(-32.41%)</b></td><td>186.10 <b>(-24.35%)</b></td><td>144.96 (-19.34%)</td><td>142.90 (-12.06%)</td><td>120.00 (-4.38%)</td><td>25.06 <b>(-51.05%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>246.00 (n/a)</td><td>179.72 (n/a)</td><td>162.50 (n/a)</td><td>125.50 (n/a)</td><td>51.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (-4.74%)</td><td>0.11 (-3.22%)</td><td>0.12 (-3.46%)</td><td>0.08 (-0.80%)</td><td>0.02 (-13.36%)</td><td>194.70 (+0.78%)</td><td>153.72 (+2.59%)</td><td>139.40 (+3.57%)</td><td>124.20 (+4.99%)</td><td>29.20 (-8.42%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.20 (n/a)</td><td>149.84 (n/a)</td><td>134.60 (n/a)</td><td>118.30 (n/a)</td><td>31.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 <b>(+42.23%)</b></td><td>0.14 (+17.18%)</td><td>0.14 (+12.55%)</td><td>0.11 (-8.55%)</td><td>0.03 <b>(+328.79%)</b></td><td>193.90 (+9.36%)</td><td>147.30 (-11.47%)</td><td>151.00 (-11.18%)</td><td>107.50 <b>(-29.69%)</b></td><td>32.75 <b>(+228.37%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>177.30 (n/a)</td><td>166.38 (n/a)</td><td>170.00 (n/a)</td><td>152.90 (n/a)</td><td>9.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (-1.26%)</td><td>0.11 (-2.74%)</td><td>0.10 (-1.81%)</td><td>0.09 (-4.92%)</td><td>0.02 (-6.29%)</td><td>186.10 (+5.14%)</td><td>158.38 (+2.59%)</td><td>171.40 (+1.84%)</td><td>122.10 (+1.33%)</td><td>26.74 (-2.13%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>177.00 (n/a)</td><td>154.38 (n/a)</td><td>168.30 (n/a)</td><td>120.50 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (+8.43%)</td><td>0.14 (+15.73%)</td><td>0.14 <b>(+20.17%)</b></td><td>0.11 (+17.07%)</td><td>0.02 (+0.22%)</td><td>189.50 (-14.60%)</td><td>149.32 (-14.01%)</td><td>141.40 (-16.82%)</td><td>125.40 (-7.79%)</td><td>24.58 <b>(-20.26%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>221.90 (n/a)</td><td>173.64 (n/a)</td><td>170.00 (n/a)</td><td>136.00 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (-17.29%)</td><td>0.09 (-2.00%)</td><td>0.09 (-10.16%)</td><td>0.07 <b>(+64.50%)</b></td><td>0.01 <b>(-64.30%)</b></td><td>226.90 <b>(-39.20%)</b></td><td>184.02 (-10.38%)</td><td>183.00 (+11.31%)</td><td>158.50 <b>(+20.90%)</b></td><td>26.40 <b>(-73.58%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>373.20 (n/a)</td><td>205.34 (n/a)</td><td>164.40 (n/a)</td><td>131.10 (n/a)</td><td>99.94 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 <b>(+22.57%)</b></td><td>0.10 (+11.90%)</td><td>0.11 <b>(+20.07%)</b></td><td>0.06 (-13.87%)</td><td>0.03 <b>(+162.77%)</b></td><td>285.00 (+16.09%)</td><td>194.42 (-5.92%)</td><td>168.30 (-16.72%)</td><td>146.80 (-18.44%)</td><td>57.84 <b>(+142.74%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>245.50 (n/a)</td><td>206.66 (n/a)</td><td>202.10 (n/a)</td><td>180.00 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (-8.94%)</td><td>0.10 (-2.30%)</td><td>0.10 (+17.53%)</td><td>0.08 (+2.16%)</td><td>0.02 <b>(-32.13%)</b></td><td>195.40 (-2.10%)</td><td>165.74 (+0.17%)</td><td>159.40 (-14.90%)</td><td>133.10 (+9.82%)</td><td>28.24 <b>(-24.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>199.60 (n/a)</td><td>165.46 (n/a)</td><td>187.30 (n/a)</td><td>121.20 (n/a)</td><td>37.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (+17.24%)</td><td>0.11 (+14.31%)</td><td>0.11 (+14.30%)</td><td>0.10 (+17.80%)</td><td>0.02 (+16.17%)</td><td>186.00 (-15.15%)</td><td>163.28 (-12.53%)</td><td>172.10 (-12.51%)</td><td>130.30 (-14.67%)</td><td>23.29 (-14.92%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>219.20 (n/a)</td><td>186.68 (n/a)</td><td>196.70 (n/a)</td><td>152.70 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (+14.06%)</td><td>0.11 (+5.41%)</td><td>0.11 (+13.97%)</td><td>0.07 (-16.29%)</td><td>0.03 <b>(+55.68%)</b></td><td>231.80 (+19.48%)</td><td>162.56 (-1.85%)</td><td>152.90 (-12.28%)</td><td>115.70 (-12.28%)</td><td>45.11 <b>(+65.33%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.00 (n/a)</td><td>165.62 (n/a)</td><td>174.30 (n/a)</td><td>131.90 (n/a)</td><td>27.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (+3.16%)</td><td>0.09 (+0.51%)</td><td>0.08 (-11.29%)</td><td>0.08 (+0.27%)</td><td>0.02 (+9.88%)</td><td>230.90 (-0.26%)</td><td>193.70 (-0.22%)</td><td>207.50 (+12.71%)</td><td>150.60 (-3.03%)</td><td>32.91 (+2.96%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>194.12 (n/a)</td><td>184.10 (n/a)</td><td>155.30 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (+6.08%)</td><td>0.09 (-10.57%)</td><td>0.08 (-16.75%)</td><td>0.08 <b>(-20.66%)</b></td><td>0.02 <b>(+211.88%)</b></td><td>217.40 <b>(+26.03%)</b></td><td>189.30 (+14.71%)</td><td>204.40 <b>(+20.16%)</b></td><td>142.90 (-5.74%)</td><td>33.57 <b>(+276.86%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>172.50 (n/a)</td><td>165.02 (n/a)</td><td>170.10 (n/a)</td><td>151.60 (n/a)</td><td>8.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (+1.20%)</td><td>0.09 (-0.67%)</td><td>0.09 (+8.55%)</td><td>0.05 (-9.67%)</td><td>0.03 (+3.90%)</td><td>325.10 (+10.73%)</td><td>204.60 (+2.16%)</td><td>186.20 (-7.87%)</td><td>130.50 (-1.21%)</td><td>72.72 (+18.49%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>293.60 (n/a)</td><td>200.28 (n/a)</td><td>202.10 (n/a)</td><td>132.10 (n/a)</td><td>61.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (-1.98%)</td><td>0.08 (+11.13%)</td><td>0.09 (+16.11%)</td><td>0.07 <b>(+32.55%)</b></td><td>0.01 <b>(-44.68%)</b></td><td>250.10 <b>(-24.56%)</b></td><td>198.26 (-13.97%)</td><td>190.80 (-13.90%)</td><td>174.40 (+2.05%)</td><td>29.90 <b>(-54.82%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>331.50 (n/a)</td><td>230.46 (n/a)</td><td>221.60 (n/a)</td><td>170.90 (n/a)</td><td>66.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (+15.26%)</td><td>0.21 <b>(+22.85%)</b></td><td>0.21 <b>(+25.15%)</b></td><td>0.16 (+19.84%)</td><td>0.04 <b>(+20.56%)</b></td><td>206.70 (-16.55%)</td><td>162.28 (-18.47%)</td><td>156.70 <b>(-20.09%)</b></td><td>132.80 (-13.26%)</td><td>29.68 (-12.09%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>247.70 (n/a)</td><td>199.04 (n/a)</td><td>196.10 (n/a)</td><td>153.10 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (+20.00%)</td><td>0.17 (-8.48%)</td><td>0.17 (-13.48%)</td><td>0.09 <b>(-23.85%)</b></td><td>0.05 <b>(+63.37%)</b></td><td>345.90 <b>(+31.32%)</b></td><td>214.56 (+16.03%)</td><td>192.30 (+15.56%)</td><td>133.10 (-16.71%)</td><td>79.53 <b>(+80.70%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>263.40 (n/a)</td><td>184.92 (n/a)</td><td>166.40 (n/a)</td><td>159.80 (n/a)</td><td>44.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.33 (+4.27%)</td><td>0.28 <b>(+27.57%)</b></td><td>0.27 <b>(+30.26%)</b></td><td>0.23 <b>(+68.35%)</b></td><td>0.04 <b>(-40.14%)</b></td><td>181.50 <b>(-40.59%)</b></td><td>149.52 <b>(-26.55%)</b></td><td>150.50 <b>(-23.21%)</b></td><td>123.40 (-4.12%)</td><td>22.62 <b>(-66.18%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>305.50 (n/a)</td><td>203.58 (n/a)</td><td>196.00 (n/a)</td><td>128.70 (n/a)</td><td>66.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 (-5.05%)</td><td>0.18 (-2.28%)</td><td>0.18 (+2.38%)</td><td>0.16 (-4.95%)</td><td>0.02 (-10.11%)</td><td>202.00 (+5.21%)</td><td>182.06 (+2.26%)</td><td>181.10 (-2.32%)</td><td>158.70 (+5.31%)</td><td>16.39 (+0.84%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>192.00 (n/a)</td><td>178.04 (n/a)</td><td>185.40 (n/a)</td><td>150.70 (n/a)</td><td>16.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.31 (+1.92%)</td><td>0.25 (-0.82%)</td><td>0.23 (-12.09%)</td><td>0.21 (+19.96%)</td><td>0.04 <b>(-26.03%)</b></td><td>198.80 (-16.65%)</td><td>166.72 (-1.66%)</td><td>175.40 (+13.75%)</td><td>131.90 (-1.93%)</td><td>26.31 <b>(-39.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>238.50 (n/a)</td><td>169.54 (n/a)</td><td>154.20 (n/a)</td><td>134.50 (n/a)</td><td>43.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 (+15.66%)</td><td>0.20 (-1.62%)</td><td>0.19 (-7.72%)</td><td>0.16 (+7.62%)</td><td>0.06 <b>(+43.69%)</b></td><td>209.90 (-7.08%)</td><td>172.34 (+3.71%)</td><td>170.90 (+8.37%)</td><td>109.70 (-13.55%)</td><td>40.35 (+10.97%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.90 (n/a)</td><td>166.18 (n/a)</td><td>157.70 (n/a)</td><td>126.90 (n/a)</td><td>36.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.28 (+0.24%)</td><td>0.25 (+2.54%)</td><td>0.25 (-3.16%)</td><td>0.20 (+9.46%)</td><td>0.03 <b>(-33.77%)</b></td><td>181.80 (-8.64%)</td><td>151.94 (-4.02%)</td><td>147.10 (+3.23%)</td><td>131.90 (-0.23%)</td><td>18.52 <b>(-38.34%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>199.00 (n/a)</td><td>158.30 (n/a)</td><td>142.50 (n/a)</td><td>132.20 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (-8.05%)</td><td>0.20 (+9.67%)</td><td>0.20 (-4.29%)</td><td>0.16 <b>(+67.95%)</b></td><td>0.04 <b>(-48.94%)</b></td><td>205.70 <b>(-40.46%)</b></td><td>166.04 (-19.70%)</td><td>165.90 (+4.47%)</td><td>131.50 (+8.77%)</td><td>30.88 <b>(-67.70%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>345.50 (n/a)</td><td>206.78 (n/a)</td><td>158.80 (n/a)</td><td>120.90 (n/a)</td><td>95.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.29 (+8.33%)</td><td>0.25 (+14.20%)</td><td>0.25 (+6.11%)</td><td>0.18 <b>(+20.98%)</b></td><td>0.04 (-13.02%)</td><td>203.90 (-17.35%)</td><td>154.14 (-14.07%)</td><td>147.20 (-5.76%)</td><td>127.30 (-7.69%)</td><td>30.16 <b>(-33.05%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>246.70 (n/a)</td><td>179.38 (n/a)</td><td>156.20 (n/a)</td><td>137.90 (n/a)</td><td>45.05 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (+12.26%)</td><td>0.19 (+0.77%)</td><td>0.21 (-1.25%)</td><td>0.14 (+5.45%)</td><td>0.05 (+19.51%)</td><td>226.30 (-5.16%)</td><td>177.24 (+0.21%)</td><td>156.30 (+1.23%)</td><td>129.80 (-10.97%)</td><td>43.07 (+7.32%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>238.60 (n/a)</td><td>176.86 (n/a)</td><td>154.40 (n/a)</td><td>145.80 (n/a)</td><td>40.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (-13.64%)</td><td>0.21 (-1.09%)</td><td>0.22 (+0.95%)</td><td>0.16 (-9.35%)</td><td>0.03 (-15.64%)</td><td>222.50 (+10.31%)</td><td>168.92 (+0.97%)</td><td>159.60 (-0.93%)</td><td>150.30 (+15.79%)</td><td>30.26 (+10.36%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>201.70 (n/a)</td><td>167.30 (n/a)</td><td>161.10 (n/a)</td><td>129.80 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 <b>(+30.97%)</b></td><td>0.21 <b>(+20.30%)</b></td><td>0.21 (+19.97%)</td><td>0.17 (+14.02%)</td><td>0.03 <b>(+97.68%)</b></td><td>195.20 (-12.31%)</td><td>159.84 (-16.03%)</td><td>152.80 (-16.64%)</td><td>136.90 <b>(-23.65%)</b></td><td>23.67 <b>(+30.68%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>190.36 (n/a)</td><td>183.30 (n/a)</td><td>179.30 (n/a)</td><td>18.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.22 (-7.28%)</td><td>0.19 (+3.64%)</td><td>0.20 (+15.90%)</td><td>0.13 (-12.98%)</td><td>0.04 (+8.72%)</td><td>266.50 (+14.92%)</td><td>192.18 (-2.30%)</td><td>175.00 (-13.71%)</td><td>157.00 (+7.83%)</td><td>45.31 <b>(+37.77%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>231.90 (n/a)</td><td>196.70 (n/a)</td><td>202.80 (n/a)</td><td>145.60 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (+1.41%)</td><td>0.16 (+17.00%)</td><td>0.15 <b>(+20.14%)</b></td><td>0.13 <b>(+38.30%)</b></td><td>0.02 <b>(-33.13%)</b></td><td>250.00 <b>(-27.70%)</b></td><td>211.12 (-17.49%)</td><td>215.30 (-16.74%)</td><td>172.50 (-1.37%)</td><td>30.82 <b>(-52.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>345.80 (n/a)</td><td>255.86 (n/a)</td><td>258.60 (n/a)</td><td>174.90 (n/a)</td><td>64.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 <b>(+22.20%)</b></td><td>0.13 <b>(+20.28%)</b></td><td>0.13 (+12.75%)</td><td>0.10 (+19.50%)</td><td>0.02 (+19.60%)</td><td>199.80 (-16.33%)</td><td>161.16 (-16.89%)</td><td>161.00 (-11.34%)</td><td>137.20 (-18.14%)</td><td>25.03 (-18.01%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>238.80 (n/a)</td><td>193.92 (n/a)</td><td>181.60 (n/a)</td><td>167.60 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 <b>(+32.84%)</b></td><td>0.12 (+17.86%)</td><td>0.12 (+12.51%)</td><td>0.09 (+10.85%)</td><td>0.03 <b>(+92.51%)</b></td><td>215.80 (-9.78%)</td><td>171.80 (-13.50%)</td><td>177.50 (-11.12%)</td><td>129.50 <b>(-24.75%)</b></td><td>34.04 <b>(+29.43%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>198.62 (n/a)</td><td>199.70 (n/a)</td><td>172.10 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (+18.36%)</td><td>0.12 (-0.62%)</td><td>0.12 (-3.26%)</td><td>0.09 (-15.56%)</td><td>0.02 <b>(+290.23%)</b></td><td>222.00 (+18.40%)</td><td>179.30 (+2.46%)</td><td>177.80 (+3.31%)</td><td>142.90 (-15.49%)</td><td>28.22 <b>(+288.42%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>187.50 (n/a)</td><td>175.00 (n/a)</td><td>172.10 (n/a)</td><td>169.10 (n/a)</td><td>7.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 <b>(-44.33%)</b></td><td>0.10 <b>(-21.63%)</b></td><td>0.11 (-8.47%)</td><td>0.09 (-11.92%)</td><td>0.01 <b>(-74.39%)</b></td><td>236.30 (+13.50%)</td><td>200.12 (+19.80%)</td><td>188.20 (+9.23%)</td><td>180.10 <b>(+79.56%)</b></td><td>23.34 <b>(-48.44%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>208.20 (n/a)</td><td>167.04 (n/a)</td><td>172.30 (n/a)</td><td>100.30 (n/a)</td><td>45.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (+5.86%)</td><td>0.14 (+4.68%)</td><td>0.14 (+0.10%)</td><td>0.11 (+6.64%)</td><td>0.02 (+3.04%)</td><td>185.60 (-6.26%)</td><td>154.38 (-4.67%)</td><td>151.60 (-0.07%)</td><td>119.20 (-5.55%)</td><td>27.24 (-9.79%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>198.00 (n/a)</td><td>161.94 (n/a)</td><td>151.70 (n/a)</td><td>126.20 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (-8.73%)</td><td>0.13 (-1.78%)</td><td>0.12 (-2.53%)</td><td>0.11 (+7.30%)</td><td>0.02 <b>(-29.72%)</b></td><td>189.90 (-6.77%)</td><td>165.06 (-0.72%)</td><td>171.40 (+2.63%)</td><td>121.60 (+9.55%)</td><td>26.76 <b>(-31.02%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>203.70 (n/a)</td><td>166.26 (n/a)</td><td>167.00 (n/a)</td><td>111.00 (n/a)</td><td>38.78 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (+7.47%)</td><td>0.12 (+8.50%)</td><td>0.12 (+6.41%)</td><td>0.10 (+17.51%)</td><td>0.01 (-3.87%)</td><td>208.80 (-14.88%)</td><td>176.96 (-8.33%)</td><td>170.90 (-6.05%)</td><td>152.10 (-6.97%)</td><td>23.32 <b>(-25.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>245.30 (n/a)</td><td>193.04 (n/a)</td><td>181.90 (n/a)</td><td>163.50 (n/a)</td><td>31.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 <b>(+20.81%)</b></td><td>0.13 (+14.65%)</td><td>0.12 (+7.66%)</td><td>0.11 (+14.62%)</td><td>0.02 <b>(+48.72%)</b></td><td>190.30 (-12.75%)</td><td>164.66 (-12.13%)</td><td>174.70 (-7.12%)</td><td>128.20 (-17.18%)</td><td>24.46 (+7.11%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>187.40 (n/a)</td><td>188.10 (n/a)</td><td>154.80 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (-1.64%)</td><td>0.16 (+13.69%)</td><td>0.17 <b>(+29.48%)</b></td><td>0.12 (+8.30%)</td><td>0.03 (-16.54%)</td><td>200.60 (-7.69%)</td><td>160.50 (-13.14%)</td><td>148.30 <b>(-22.76%)</b></td><td>127.10 (+1.68%)</td><td>29.87 (-19.02%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>217.30 (n/a)</td><td>184.78 (n/a)</td><td>192.00 (n/a)</td><td>125.00 (n/a)</td><td>36.88 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 <b>(-25.66%)</b></td><td>0.14 (-7.31%)</td><td>0.14 (-4.71%)</td><td>0.11 (+4.04%)</td><td>0.02 <b>(-53.26%)</b></td><td>218.50 (-3.87%)</td><td>179.00 (+3.55%)</td><td>180.50 (+4.94%)</td><td>147.80 <b>(+34.49%)</b></td><td>27.08 <b>(-37.58%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>227.30 (n/a)</td><td>172.86 (n/a)</td><td>172.00 (n/a)</td><td>109.90 (n/a)</td><td>43.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 <b>(-31.85%)</b></td><td>0.13 (-12.91%)</td><td>0.13 (-1.60%)</td><td>0.11 (-16.18%)</td><td>0.02 <b>(-58.34%)</b></td><td>232.10 (+19.33%)</td><td>187.68 (+10.96%)</td><td>185.40 (+1.64%)</td><td>155.50 <b>(+46.70%)</b></td><td>27.76 <b>(-23.09%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>194.50 (n/a)</td><td>169.14 (n/a)</td><td>182.40 (n/a)</td><td>106.00 (n/a)</td><td>36.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (-19.64%)</td><td>0.14 (-11.15%)</td><td>0.13 (+1.61%)</td><td>0.11 (-4.60%)</td><td>0.02 <b>(-43.08%)</b></td><td>216.10 (+4.80%)</td><td>182.70 (+9.47%)</td><td>185.30 (-1.59%)</td><td>146.10 <b>(+24.45%)</b></td><td>29.02 <b>(-25.37%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>206.20 (n/a)</td><td>166.90 (n/a)</td><td>188.30 (n/a)</td><td>117.40 (n/a)</td><td>38.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 <b>(+33.09%)</b></td><td>0.15 (+17.51%)</td><td>0.14 (+12.08%)</td><td>0.13 (+16.72%)</td><td>0.02 <b>(+92.75%)</b></td><td>182.90 (-14.33%)</td><td>168.36 (-14.33%)</td><td>174.40 (-10.79%)</td><td>135.20 <b>(-24.89%)</b></td><td>19.02 <b>(+21.36%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>196.52 (n/a)</td><td>195.50 (n/a)</td><td>180.00 (n/a)</td><td>15.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 <b>(-35.52%)</b></td><td>0.13 <b>(-26.66%)</b></td><td>0.12 <b>(-30.48%)</b></td><td>0.11 (-8.33%)</td><td>0.02 <b>(-65.58%)</b></td><td>222.30 (+9.08%)</td><td>196.50 <b>(+28.55%)</b></td><td>200.60 <b>(+43.90%)</b></td><td>158.20 <b>(+55.10%)</b></td><td>25.27 <b>(-44.93%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>203.80 (n/a)</td><td>152.86 (n/a)</td><td>139.40 (n/a)</td><td>102.00 (n/a)</td><td>45.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 <b>(+27.55%)</b></td><td>0.13 (+18.36%)</td><td>0.12 (+11.53%)</td><td>0.11 <b>(+31.58%)</b></td><td>0.02 (+11.70%)</td><td>214.80 <b>(-24.02%)</b></td><td>193.40 (-15.95%)</td><td>199.90 (-10.32%)</td><td>152.40 <b>(-21.60%)</b></td><td>23.83 <b>(-34.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>282.70 (n/a)</td><td>230.10 (n/a)</td><td>222.90 (n/a)</td><td>194.40 (n/a)</td><td>36.66 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 (-6.68%)</td><td>0.13 (+2.20%)</td><td>0.12 (-0.37%)</td><td>0.11 <b>(+40.59%)</b></td><td>0.01 <b>(-56.81%)</b></td><td>225.80 <b>(-28.86%)</b></td><td>195.42 (-7.59%)</td><td>199.60 (+0.35%)</td><td>168.30 (+7.13%)</td><td>22.10 <b>(-66.44%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>317.40 (n/a)</td><td>211.46 (n/a)</td><td>198.90 (n/a)</td><td>157.10 (n/a)</td><td>65.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 <b>(+22.61%)</b></td><td>0.13 <b>(+25.28%)</b></td><td>0.14 <b>(+24.03%)</b></td><td>0.11 <b>(+36.25%)</b></td><td>0.02 (+7.23%)</td><td>167.60 <b>(-26.62%)</b></td><td>139.32 <b>(-20.86%)</b></td><td>133.50 (-19.38%)</td><td>114.60 (-18.43%)</td><td>21.49 <b>(-36.29%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>228.40 (n/a)</td><td>176.04 (n/a)</td><td>165.60 (n/a)</td><td>140.50 (n/a)</td><td>33.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 (+13.33%)</td><td>0.13 (+18.62%)</td><td>0.12 (+15.45%)</td><td>0.11 <b>(+41.87%)</b></td><td>0.01 <b>(-22.20%)</b></td><td>164.30 <b>(-29.52%)</b></td><td>147.94 (-17.13%)</td><td>154.20 (-13.42%)</td><td>126.50 (-11.72%)</td><td>16.53 <b>(-52.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>233.10 (n/a)</td><td>178.52 (n/a)</td><td>178.10 (n/a)</td><td>143.30 (n/a)</td><td>34.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (+14.42%)</td><td>0.11 (+11.23%)</td><td>0.11 <b>(+20.21%)</b></td><td>0.09 (+4.75%)</td><td>0.03 (+11.10%)</td><td>216.00 (-4.55%)</td><td>169.58 (-10.27%)</td><td>174.10 (-16.82%)</td><td>114.10 (-12.63%)</td><td>37.14 (-12.04%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>226.30 (n/a)</td><td>188.98 (n/a)</td><td>209.30 (n/a)</td><td>130.60 (n/a)</td><td>42.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (-17.69%)</td><td>0.09 (-14.70%)</td><td>0.08 <b>(-29.65%)</b></td><td>0.08 (+3.34%)</td><td>0.02 <b>(-32.69%)</b></td><td>229.00 (-3.25%)</td><td>204.10 (+15.19%)</td><td>224.30 <b>(+42.14%)</b></td><td>167.40 <b>(+21.48%)</b></td><td>31.49 <b>(-21.50%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>236.70 (n/a)</td><td>177.18 (n/a)</td><td>157.80 (n/a)</td><td>137.80 (n/a)</td><td>40.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (+6.15%)</td><td>0.10 (+6.02%)</td><td>0.10 (+12.21%)</td><td>0.08 (-7.09%)</td><td>0.02 <b>(+31.11%)</b></td><td>233.80 (+7.64%)</td><td>180.82 (-4.68%)</td><td>178.00 (-10.91%)</td><td>148.70 (-5.77%)</td><td>33.03 <b>(+35.34%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>189.70 (n/a)</td><td>199.80 (n/a)</td><td>157.80 (n/a)</td><td>24.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (+8.89%)</td><td>0.12 (+1.47%)</td><td>0.11 (+9.69%)</td><td>0.09 (+4.50%)</td><td>0.03 (-3.58%)</td><td>214.70 (-4.32%)</td><td>167.92 (-2.61%)</td><td>170.90 (-8.85%)</td><td>110.00 (-8.18%)</td><td>40.03 (-14.35%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>224.40 (n/a)</td><td>172.42 (n/a)</td><td>187.50 (n/a)</td><td>119.80 (n/a)</td><td>46.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (+1.52%)</td><td>0.11 (+11.08%)</td><td>0.11 (+8.49%)</td><td>0.09 <b>(+23.80%)</b></td><td>0.02 <b>(-23.63%)</b></td><td>196.30 (-19.22%)</td><td>169.34 (-11.50%)</td><td>173.70 (-7.85%)</td><td>138.70 (-1.49%)</td><td>23.07 <b>(-38.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>243.00 (n/a)</td><td>191.34 (n/a)</td><td>188.50 (n/a)</td><td>140.80 (n/a)</td><td>37.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (-19.85%)</td><td>0.10 (-7.37%)</td><td>0.10 (-4.06%)</td><td>0.08 (-6.33%)</td><td>0.01 <b>(-42.08%)</b></td><td>238.10 (+6.77%)</td><td>196.06 (+5.81%)</td><td>187.00 (+4.24%)</td><td>165.10 <b>(+24.79%)</b></td><td>28.75 <b>(-23.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>223.00 (n/a)</td><td>185.30 (n/a)</td><td>179.40 (n/a)</td><td>132.30 (n/a)</td><td>37.78 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.69 (-14.39%)</td><td>0.55 (-7.20%)</td><td>0.53 (-9.50%)</td><td>0.43 (+0.28%)</td><td>0.12 (-14.36%)</td><td>228.70 (-0.26%)</td><td>186.10 (+7.26%)</td><td>185.50 (+10.48%)</td><td>143.30 (+16.88%)</td><td>39.13 (+1.05%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.80 (n/a)</td><td>0.59 (n/a)</td><td>0.59 (n/a)</td><td>0.43 (n/a)</td><td>0.14 (n/a)</td><td>229.30 (n/a)</td><td>173.50 (n/a)</td><td>167.90 (n/a)</td><td>122.60 (n/a)</td><td>38.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.62 (+4.34%)</td><td>0.52 (-2.99%)</td><td>0.50 (-9.90%)</td><td>0.42 (-4.55%)</td><td>0.08 <b>(+22.64%)</b></td><td>233.90 (+4.75%)</td><td>194.28 (+3.76%)</td><td>195.10 (+10.98%)</td><td>157.80 (-4.13%)</td><td>30.26 <b>(+22.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.60 (n/a)</td><td>0.53 (n/a)</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.07 (n/a)</td><td>223.30 (n/a)</td><td>187.24 (n/a)</td><td>175.80 (n/a)</td><td>164.60 (n/a)</td><td>24.71 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.97 <b>(+22.31%)</b></td><td>0.63 (-1.55%)</td><td>0.56 (-3.05%)</td><td>0.46 (-6.36%)</td><td>0.20 <b>(+58.77%)</b></td><td>211.70 (+6.81%)</td><td>167.72 (+5.04%)</td><td>176.30 (+3.16%)</td><td>101.00 (-18.22%)</td><td>41.53 <b>(+34.40%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.80 (n/a)</td><td>0.64 (n/a)</td><td>0.58 (n/a)</td><td>0.50 (n/a)</td><td>0.13 (n/a)</td><td>198.20 (n/a)</td><td>159.68 (n/a)</td><td>170.90 (n/a)</td><td>123.50 (n/a)</td><td>30.90 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.59 (+2.17%)</td><td>0.53 (+7.76%)</td><td>0.54 (+5.50%)</td><td>0.47 <b>(+23.14%)</b></td><td>0.05 <b>(-32.11%)</b></td><td>208.80 (-18.79%)</td><td>188.48 (-8.44%)</td><td>182.10 (-5.21%)</td><td>167.80 (-2.10%)</td><td>19.05 <b>(-45.34%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.57 (n/a)</td><td>0.49 (n/a)</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>257.10 (n/a)</td><td>205.86 (n/a)</td><td>192.10 (n/a)</td><td>171.40 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.62 <b>(+33.30%)</b></td><td>0.55 <b>(+43.37%)</b></td><td>0.56 <b>(+42.81%)</b></td><td>0.46 <b>(+48.34%)</b></td><td>0.07 (+14.71%)</td><td>161.90 <b>(-32.57%)</b></td><td>135.68 <b>(-30.68%)</b></td><td>131.10 <b>(-29.97%)</b></td><td>119.40 <b>(-25.00%)</b></td><td>17.32 <b>(-42.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.46 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.06 (n/a)</td><td>240.10 (n/a)</td><td>195.74 (n/a)</td><td>187.20 (n/a)</td><td>159.20 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.54 <b>(+24.87%)</b></td><td>0.43 (+15.87%)</td><td>0.41 (+13.78%)</td><td>0.33 (+10.43%)</td><td>0.09 <b>(+77.28%)</b></td><td>221.30 (-9.41%)</td><td>178.58 (-12.06%)</td><td>178.80 (-12.09%)</td><td>136.30 (-19.92%)</td><td>36.13 <b>(+28.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.05 (n/a)</td><td>244.30 (n/a)</td><td>203.06 (n/a)</td><td>203.40 (n/a)</td><td>170.20 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.62 (+3.06%)</td><td>0.44 (+3.30%)</td><td>0.40 (-7.68%)</td><td>0.34 <b>(+35.40%)</b></td><td>0.12 (-5.53%)</td><td>215.80 <b>(-26.15%)</b></td><td>174.72 (-5.86%)</td><td>183.90 (+8.30%)</td><td>118.70 (-2.94%)</td><td>41.95 <b>(-34.28%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.60 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>292.20 (n/a)</td><td>185.60 (n/a)</td><td>169.80 (n/a)</td><td>122.30 (n/a)</td><td>63.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.48 (+4.79%)</td><td>0.40 (+1.72%)</td><td>0.43 (+4.35%)</td><td>0.25 (-12.51%)</td><td>0.09 <b>(+45.68%)</b></td><td>293.90 (+14.31%)</td><td>195.58 (+1.42%)</td><td>172.90 (-4.16%)</td><td>154.50 (-4.57%)</td><td>58.19 <b>(+54.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.06 (n/a)</td><td>257.10 (n/a)</td><td>192.84 (n/a)</td><td>180.40 (n/a)</td><td>161.90 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 <b>(+22.58%)</b></td><td>0.20 (+4.08%)</td><td>0.20 (+3.82%)</td><td>0.17 (-4.81%)</td><td>0.03 <b>(+237.22%)</b></td><td>215.80 (+5.01%)</td><td>186.44 (-2.09%)</td><td>183.10 (-3.68%)</td><td>147.50 (-18.42%)</td><td>29.52 <b>(+197.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>190.42 (n/a)</td><td>190.10 (n/a)</td><td>180.80 (n/a)</td><td>9.94 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.36 <b>(+66.13%)</b></td><td>0.22 (+10.91%)</td><td>0.19 (-7.70%)</td><td>0.18 (+5.18%)</td><td>0.07 <b>(+309.75%)</b></td><td>206.00 (-4.89%)</td><td>175.72 (-4.41%)</td><td>191.80 (+8.36%)</td><td>103.50 <b>(-39.83%)</b></td><td>42.22 <b>(+126.48%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>216.60 (n/a)</td><td>183.82 (n/a)</td><td>177.00 (n/a)</td><td>172.00 (n/a)</td><td>18.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (-8.57%)</td><td>0.21 (-9.54%)</td><td>0.21 (-8.05%)</td><td>0.17 (-14.05%)</td><td>0.04 (+13.80%)</td><td>220.60 (+16.35%)</td><td>182.68 (+11.98%)</td><td>174.50 (+8.79%)</td><td>139.70 (+9.31%)</td><td>35.50 <b>(+52.29%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>189.60 (n/a)</td><td>163.14 (n/a)</td><td>160.40 (n/a)</td><td>127.80 (n/a)</td><td>23.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.34 <b>(+39.44%)</b></td><td>0.22 (-0.49%)</td><td>0.20 (-9.63%)</td><td>0.14 <b>(-28.84%)</b></td><td>0.08 <b>(+334.26%)</b></td><td>260.50 <b>(+40.51%)</b></td><td>188.40 (+10.20%)</td><td>186.80 (+10.60%)</td><td>108.90 <b>(-28.26%)</b></td><td>61.56 <b>(+335.04%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>185.40 (n/a)</td><td>170.96 (n/a)</td><td>168.90 (n/a)</td><td>151.80 (n/a)</td><td>14.15 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (-2.45%)</td><td>0.20 (-3.47%)</td><td>0.20 (-5.28%)</td><td>0.13 (-9.34%)</td><td>0.04 (+11.09%)</td><td>290.10 (+10.30%)</td><td>196.86 (+4.91%)</td><td>180.10 (+5.57%)</td><td>158.40 (+2.52%)</td><td>53.81 <b>(+24.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>263.00 (n/a)</td><td>187.64 (n/a)</td><td>170.60 (n/a)</td><td>154.50 (n/a)</td><td>43.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (-6.12%)</td><td>0.20 (-12.64%)</td><td>0.21 (-5.41%)</td><td>0.16 <b>(-24.55%)</b></td><td>0.03 <b>(+66.80%)</b></td><td>232.10 <b>(+32.55%)</b></td><td>184.68 (+16.37%)</td><td>173.10 (+5.74%)</td><td>154.50 (+6.48%)</td><td>31.79 <b>(+141.42%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>175.10 (n/a)</td><td>158.70 (n/a)</td><td>163.70 (n/a)</td><td>145.10 (n/a)</td><td>13.17 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (+7.17%)</td><td>0.24 (+19.78%)</td><td>0.24 <b>(+23.91%)</b></td><td>0.21 <b>(+32.50%)</b></td><td>0.02 <b>(-39.31%)</b></td><td>175.60 <b>(-24.51%)</b></td><td>157.36 (-17.58%)</td><td>151.10 (-19.33%)</td><td>146.60 (-6.68%)</td><td>12.09 <b>(-57.38%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>232.60 (n/a)</td><td>190.92 (n/a)</td><td>187.30 (n/a)</td><td>157.10 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (-6.61%)</td><td>0.20 (+4.69%)</td><td>0.20 (-2.43%)</td><td>0.18 <b>(+38.40%)</b></td><td>0.02 <b>(-51.30%)</b></td><td>207.00 <b>(-27.72%)</b></td><td>181.86 (-8.93%)</td><td>180.30 (+2.50%)</td><td>151.20 (+7.08%)</td><td>20.64 <b>(-63.47%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>286.40 (n/a)</td><td>199.70 (n/a)</td><td>175.90 (n/a)</td><td>141.20 (n/a)</td><td>56.49 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 <b>(-33.62%)</b></td><td>0.24 (-11.90%)</td><td>0.24 (-4.68%)</td><td>0.22 (+7.51%)</td><td>0.01 <b>(-85.10%)</b></td><td>183.90 (-6.98%)</td><td>171.92 (+9.24%)</td><td>170.30 (+4.86%)</td><td>165.70 <b>(+50.64%)</b></td><td>7.12 <b>(-78.50%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>197.70 (n/a)</td><td>157.38 (n/a)</td><td>162.40 (n/a)</td><td>110.00 (n/a)</td><td>33.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.28 (-9.61%)</td><td>0.23 (-4.45%)</td><td>0.22 (-8.08%)</td><td>0.21 (+5.23%)</td><td>0.03 <b>(-26.35%)</b></td><td>193.70 (-4.96%)</td><td>176.64 (+3.91%)</td><td>187.10 (+8.78%)</td><td>148.80 (+10.63%)</td><td>19.66 <b>(-20.84%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>203.80 (n/a)</td><td>170.00 (n/a)</td><td>172.00 (n/a)</td><td>134.50 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.31 (+7.74%)</td><td>0.25 (+2.08%)</td><td>0.23 (-7.34%)</td><td>0.21 (+3.74%)</td><td>0.04 (+7.86%)</td><td>197.00 (-3.62%)</td><td>167.06 (-1.97%)</td><td>179.50 (+7.87%)</td><td>132.70 (-7.20%)</td><td>26.58 (-3.52%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>204.40 (n/a)</td><td>170.42 (n/a)</td><td>166.40 (n/a)</td><td>143.00 (n/a)</td><td>27.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 (-4.52%)</td><td>0.25 (-6.75%)</td><td>0.25 (-8.79%)</td><td>0.21 (+2.58%)</td><td>0.04 (-17.12%)</td><td>198.70 (-2.50%)</td><td>169.86 (+6.43%)</td><td>166.80 (+9.66%)</td><td>136.30 (+4.77%)</td><td>26.97 (-12.75%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>203.80 (n/a)</td><td>159.60 (n/a)</td><td>152.10 (n/a)</td><td>130.10 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.35 (+15.39%)</td><td>0.26 (+18.54%)</td><td>0.22 (-4.22%)</td><td>0.20 <b>(+30.49%)</b></td><td>0.07 <b>(+29.86%)</b></td><td>202.20 <b>(-23.38%)</b></td><td>164.66 (-15.07%)</td><td>190.10 (+4.39%)</td><td>116.10 (-13.36%)</td><td>40.82 (-14.11%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>263.90 (n/a)</td><td>193.88 (n/a)</td><td>182.10 (n/a)</td><td>134.00 (n/a)</td><td>47.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.31 (-1.62%)</td><td>0.25 (-6.15%)</td><td>0.26 (-11.84%)</td><td>0.20 (-1.35%)</td><td>0.04 (-11.90%)</td><td>208.10 (+1.36%)</td><td>168.92 (+5.89%)</td><td>159.20 (+13.47%)</td><td>131.20 (+1.63%)</td><td>29.95 (-9.02%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>205.30 (n/a)</td><td>159.52 (n/a)</td><td>140.30 (n/a)</td><td>129.10 (n/a)</td><td>32.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.33 <b>(+22.37%)</b></td><td>0.26 (+18.68%)</td><td>0.24 (+14.55%)</td><td>0.20 (+4.19%)</td><td>0.05 <b>(+70.27%)</b></td><td>205.90 (-4.01%)</td><td>164.90 (-14.22%)</td><td>171.10 (-12.70%)</td><td>125.30 (-18.26%)</td><td>32.50 <b>(+33.00%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>214.50 (n/a)</td><td>192.24 (n/a)</td><td>196.00 (n/a)</td><td>153.30 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 <b>(-21.44%)</b></td><td>0.24 (-3.05%)</td><td>0.23 (+1.32%)</td><td>0.21 (+1.67%)</td><td>0.03 <b>(-48.38%)</b></td><td>198.40 (-1.64%)</td><td>175.18 (+0.79%)</td><td>181.20 (-1.31%)</td><td>151.10 <b>(+27.30%)</b></td><td>21.40 <b>(-33.53%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>201.70 (n/a)</td><td>173.80 (n/a)</td><td>183.60 (n/a)</td><td>118.70 (n/a)</td><td>32.19 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (-13.75%)</td><td>0.20 (+1.71%)</td><td>0.20 (-0.77%)</td><td>0.18 (+18.50%)</td><td>0.02 <b>(-52.91%)</b></td><td>192.90 (-15.62%)</td><td>174.32 (-5.37%)</td><td>176.20 (+0.80%)</td><td>143.00 (+15.98%)</td><td>19.12 <b>(-55.33%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>228.60 (n/a)</td><td>184.22 (n/a)</td><td>174.80 (n/a)</td><td>123.30 (n/a)</td><td>42.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 (-13.62%)</td><td>0.21 (-6.15%)</td><td>0.20 (-11.17%)</td><td>0.17 (+12.36%)</td><td>0.04 <b>(-40.90%)</b></td><td>199.90 (-11.00%)</td><td>170.14 (+2.72%)</td><td>170.60 (+12.61%)</td><td>130.20 (+15.73%)</td><td>25.74 <b>(-41.28%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>224.60 (n/a)</td><td>165.64 (n/a)</td><td>151.50 (n/a)</td><td>112.50 (n/a)</td><td>43.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.22 (-5.78%)</td><td>0.18 (-9.51%)</td><td>0.18 (-13.10%)</td><td>0.15 (-13.48%)</td><td>0.03 (+5.81%)</td><td>237.90 (+15.54%)</td><td>193.70 (+11.14%)</td><td>188.80 (+15.05%)</td><td>155.70 (+6.13%)</td><td>32.85 <b>(+28.08%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>205.90 (n/a)</td><td>174.28 (n/a)</td><td>164.10 (n/a)</td><td>146.70 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (-15.51%)</td><td>0.18 (-14.61%)</td><td>0.16 <b>(-21.45%)</b></td><td>0.15 (-8.95%)</td><td>0.03 <b>(-20.36%)</b></td><td>226.80 (+9.83%)</td><td>200.26 (+16.57%)</td><td>215.40 <b>(+27.30%)</b></td><td>148.00 (+18.31%)</td><td>32.03 (+4.63%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>206.50 (n/a)</td><td>171.80 (n/a)</td><td>169.20 (n/a)</td><td>125.10 (n/a)</td><td>30.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (-10.51%)</td><td>0.20 (-3.89%)</td><td>0.18 (-6.59%)</td><td>0.16 (+12.80%)</td><td>0.05 <b>(-22.09%)</b></td><td>224.10 (-11.35%)</td><td>185.40 (+1.85%)</td><td>189.90 (+7.05%)</td><td>131.50 (+11.72%)</td><td>38.48 <b>(-20.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>252.80 (n/a)</td><td>182.04 (n/a)</td><td>177.40 (n/a)</td><td>117.70 (n/a)</td><td>48.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (-14.27%)</td><td>0.21 (-2.83%)</td><td>0.22 (-8.48%)</td><td>0.18 <b>(+26.85%)</b></td><td>0.02 <b>(-61.17%)</b></td><td>195.20 <b>(-21.16%)</b></td><td>167.48 (-1.51%)</td><td>160.10 (+9.28%)</td><td>152.80 (+16.73%)</td><td>16.69 <b>(-64.56%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>247.60 (n/a)</td><td>170.04 (n/a)</td><td>146.50 (n/a)</td><td>130.90 (n/a)</td><td>47.08 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (+1.05%)</td><td>0.20 (+10.01%)</td><td>0.20 (+17.80%)</td><td>0.18 (+15.45%)</td><td>0.02 <b>(-37.84%)</b></td><td>190.10 (-13.39%)</td><td>173.82 (-10.12%)</td><td>173.80 (-15.14%)</td><td>153.80 (-1.03%)</td><td>14.39 <b>(-46.70%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>219.50 (n/a)</td><td>193.40 (n/a)</td><td>204.80 (n/a)</td><td>155.40 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (-4.84%)</td><td>0.20 (+6.79%)</td><td>0.19 (+10.89%)</td><td>0.13 (+10.46%)</td><td>0.04 <b>(-21.61%)</b></td><td>266.70 (-9.47%)</td><td>184.40 (-9.00%)</td><td>179.00 (-9.82%)</td><td>148.00 (+5.11%)</td><td>48.64 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>294.60 (n/a)</td><td>202.64 (n/a)</td><td>198.50 (n/a)</td><td>140.80 (n/a)</td><td>63.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.66 (-19.34%)</td><td>0.63 (-10.47%)</td><td>0.64 (-4.07%)</td><td>0.59 (-2.43%)</td><td>0.03 <b>(-66.65%)</b></td><td>221.20 (+2.50%)</td><td>207.98 (+10.44%)</td><td>203.70 (+4.25%)</td><td>198.60 <b>(+23.97%)</b></td><td>10.27 <b>(-57.09%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.82 (n/a)</td><td>0.71 (n/a)</td><td>0.67 (n/a)</td><td>0.61 (n/a)</td><td>0.09 (n/a)</td><td>215.80 (n/a)</td><td>188.32 (n/a)</td><td>195.40 (n/a)</td><td>160.20 (n/a)</td><td>23.95 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.90 (-2.14%)</td><td>0.72 (-0.95%)</td><td>0.71 (-0.50%)</td><td>0.62 (+8.22%)</td><td>0.11 (-11.59%)</td><td>212.40 (-7.61%)</td><td>186.00 (+0.37%)</td><td>183.90 (+0.49%)</td><td>145.80 (+2.17%)</td><td>25.78 (-16.64%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.92 (n/a)</td><td>0.72 (n/a)</td><td>0.72 (n/a)</td><td>0.57 (n/a)</td><td>0.12 (n/a)</td><td>229.90 (n/a)</td><td>185.32 (n/a)</td><td>183.00 (n/a)</td><td>142.70 (n/a)</td><td>30.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.75 (-4.68%)</td><td>0.70 (+4.37%)</td><td>0.73 (+3.40%)</td><td>0.60 (+4.46%)</td><td>0.06 <b>(-31.39%)</b></td><td>220.10 (-4.30%)</td><td>187.38 (-4.96%)</td><td>178.70 (-3.25%)</td><td>174.60 (+4.86%)</td><td>18.76 <b>(-31.73%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.79 (n/a)</td><td>0.68 (n/a)</td><td>0.71 (n/a)</td><td>0.57 (n/a)</td><td>0.09 (n/a)</td><td>230.00 (n/a)</td><td>197.16 (n/a)</td><td>184.70 (n/a)</td><td>166.50 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+12.96%)</td><td>0.03 (+7.48%)</td><td>0.02 (+10.97%)</td><td>0.02 (+0.41%)</td><td>0.01 (+13.97%)</td><td>205.10 (-0.39%)</td><td>167.16 (-6.73%)</td><td>177.20 (-9.91%)</td><td>120.80 (-11.50%)</td><td>31.73 (-3.74%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.90 (n/a)</td><td>179.22 (n/a)</td><td>196.70 (n/a)</td><td>136.50 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+13.10%)</td><td>0.02 (+6.32%)</td><td>0.03 (+4.23%)</td><td>0.02 (+1.67%)</td><td>0.00 <b>(+89.45%)</b></td><td>188.20 (-1.67%)</td><td>166.62 (-5.14%)</td><td>163.10 (-4.06%)</td><td>143.00 (-11.56%)</td><td>20.83 <b>(+66.71%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.40 (n/a)</td><td>175.64 (n/a)</td><td>170.00 (n/a)</td><td>161.70 (n/a)</td><td>12.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+4.75%)</td><td>0.02 (-0.71%)</td><td>0.02 (-12.14%)</td><td>0.02 (+7.47%)</td><td>0.01 (+1.44%)</td><td>207.70 (-6.94%)</td><td>177.02 (+0.56%)</td><td>198.10 (+13.85%)</td><td>133.00 (-4.52%)</td><td>34.94 (-6.55%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.20 (n/a)</td><td>176.04 (n/a)</td><td>174.00 (n/a)</td><td>139.30 (n/a)</td><td>37.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>15.29 (-7.79%)</td><td>13.73 (-0.46%)</td><td>14.43 (+10.38%)</td><td>11.04 (-4.71%)</td><td>1.84 (-5.81%)</td><td>190.10 (+4.91%)</td><td>155.18 (+0.48%)</td><td>145.40 (-9.41%)</td><td>137.20 (+8.46%)</td><td>22.61 (+6.96%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>16.59 (n/a)</td><td>13.80 (n/a)</td><td>13.07 (n/a)</td><td>11.58 (n/a)</td><td>1.95 (n/a)</td><td>181.20 (n/a)</td><td>154.44 (n/a)</td><td>160.50 (n/a)</td><td>126.50 (n/a)</td><td>21.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.11 (+3.97%)</td><td>0.93 (+9.17%)</td><td>1.02 (+8.98%)</td><td>0.58 (-4.83%)</td><td>0.21 (+8.68%)</td><td>226.50 (+5.06%)</td><td>149.78 (-7.54%)</td><td>129.70 (-8.27%)</td><td>118.70 (-3.81%)</td><td>44.03 (+12.44%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.07 (n/a)</td><td>0.85 (n/a)</td><td>0.93 (n/a)</td><td>0.61 (n/a)</td><td>0.19 (n/a)</td><td>215.60 (n/a)</td><td>162.00 (n/a)</td><td>141.40 (n/a)</td><td>123.40 (n/a)</td><td>39.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.08 (-6.79%)</td><td>0.77 (+7.45%)</td><td>0.68 (-2.34%)</td><td>0.56 (+18.73%)</td><td>0.22 (-18.49%)</td><td>236.50 (-15.75%)</td><td>181.54 (-9.90%)</td><td>195.20 (+2.41%)</td><td>122.20 (+7.29%)</td><td>46.65 <b>(-24.63%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.16 (n/a)</td><td>0.72 (n/a)</td><td>0.69 (n/a)</td><td>0.47 (n/a)</td><td>0.27 (n/a)</td><td>280.70 (n/a)</td><td>201.48 (n/a)</td><td>190.60 (n/a)</td><td>113.90 (n/a)</td><td>61.90 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.92 (-6.13%)</td><td>0.76 (-2.99%)</td><td>0.74 (-17.36%)</td><td>0.69 <b>(+24.23%)</b></td><td>0.09 <b>(-52.62%)</b></td><td>192.40 (-19.50%)</td><td>175.82 (-1.61%)</td><td>179.40 <b>(+20.97%)</b></td><td>144.30 (+6.49%)</td><td>19.79 <b>(-60.06%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.98 (n/a)</td><td>0.78 (n/a)</td><td>0.89 (n/a)</td><td>0.55 (n/a)</td><td>0.20 (n/a)</td><td>239.00 (n/a)</td><td>178.70 (n/a)</td><td>148.30 (n/a)</td><td>135.50 (n/a)</td><td>49.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.88 (+8.21%)</td><td>0.78 (+5.79%)</td><td>0.77 (+2.81%)</td><td>0.64 (+8.56%)</td><td>0.09 (+4.02%)</td><td>205.00 (-7.87%)</td><td>171.18 (-5.57%)</td><td>170.90 (-2.73%)</td><td>150.90 (-7.59%)</td><td>20.76 (-12.29%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.81 (n/a)</td><td>0.74 (n/a)</td><td>0.75 (n/a)</td><td>0.59 (n/a)</td><td>0.08 (n/a)</td><td>222.50 (n/a)</td><td>181.28 (n/a)</td><td>175.70 (n/a)</td><td>163.30 (n/a)</td><td>23.67 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.95 (-8.89%)</td><td>0.79 (-7.71%)</td><td>0.79 (-1.89%)</td><td>0.56 <b>(-25.54%)</b></td><td>0.15 <b>(+23.67%)</b></td><td>235.60 <b>(+34.32%)</b></td><td>171.92 (+10.35%)</td><td>166.20 (+1.90%)</td><td>138.90 (+9.72%)</td><td>37.63 <b>(+88.86%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.04 (n/a)</td><td>0.86 (n/a)</td><td>0.81 (n/a)</td><td>0.75 (n/a)</td><td>0.12 (n/a)</td><td>175.40 (n/a)</td><td>155.80 (n/a)</td><td>163.10 (n/a)</td><td>126.60 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 <b>(+23.93%)</b></td><td>0.02 (+14.02%)</td><td>0.02 (+2.84%)</td><td>0.02 <b>(+29.08%)</b></td><td>0.00 (+10.96%)</td><td>181.20 <b>(-22.53%)</b></td><td>166.74 (-12.57%)</td><td>174.20 (-2.74%)</td><td>137.10 (-19.31%)</td><td>17.58 <b>(-32.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.90 (n/a)</td><td>190.72 (n/a)</td><td>179.10 (n/a)</td><td>169.90 (n/a)</td><td>26.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (+6.09%)</td><td>0.02 (+1.88%)</td><td>0.02 (+2.93%)</td><td>0.02 (-4.64%)</td><td>0.00 <b>(+30.96%)</b></td><td>229.60 (+4.89%)</td><td>187.86 (-1.10%)</td><td>184.60 (-2.84%)</td><td>151.70 (-5.72%)</td><td>28.78 <b>(+30.09%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.90 (n/a)</td><td>189.94 (n/a)</td><td>190.00 (n/a)</td><td>160.90 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.00 (+2.27%)</td><td>0.00 (+2.40%)</td><td>0.00 (+2.38%)</td><td>0.00 (+8.11%)</td><td>0.00 <b>(-32.76%)</b></td><td>1022.30 (-6.58%)</td><td>965.03 (-1.99%)</td><td>961.91 (-0.53%)</td><td>908.56 (-2.46%)</td><td>40.41 <b>(-36.87%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1094.26 (n/a)</td><td>984.59 (n/a)</td><td>967.08 (n/a)</td><td>931.49 (n/a)</td><td>64.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.01 (+2.47%)</td><td>0.01 (+3.32%)</td><td>0.01 (+1.25%)</td><td>0.01 (+8.22%)</td><td>0.00 <b>(-54.66%)</b></td><td>1032.11 (-8.23%)</td><td>1013.67 (-3.38%)</td><td>1017.03 (-0.91%)</td><td>984.75 (-2.73%)</td><td>18.92 <b>(-58.88%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1124.66 (n/a)</td><td>1049.10 (n/a)</td><td>1026.34 (n/a)</td><td>1012.34 (n/a)</td><td>46.03 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.98 (+1.75%)</td><td>0.96 (+1.20%)</td><td>0.96 (+0.82%)</td><td>0.95 (+2.81%)</td><td>0.01 <b>(-25.61%)</b></td><td>2211.25 (-2.73%)</td><td>2174.79 (-1.20%)</td><td>2175.75 (-0.81%)</td><td>2130.37 (-1.72%)</td><td>30.53 <b>(-29.01%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.96 (n/a)</td><td>0.92 (n/a)</td><td>0.02 (n/a)</td><td>2273.30 (n/a)</td><td>2201.27 (n/a)</td><td>2193.52 (n/a)</td><td>2167.57 (n/a)</td><td>43.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.41 (+1.22%)</td><td>0.39 (-0.39%)</td><td>0.39 (-1.17%)</td><td>0.37 (-3.08%)</td><td>0.02 <b>(+94.87%)</b></td><td>1400.71 (+3.18%)</td><td>1335.02 (+0.50%)</td><td>1353.72 (+1.18%)</td><td>1265.71 (-1.20%)</td><td>56.89 <b>(+98.38%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.01 (n/a)</td><td>1357.60 (n/a)</td><td>1328.44 (n/a)</td><td>1337.95 (n/a)</td><td>1281.11 (n/a)</td><td>28.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 (+0.42%)</td><td>0.25 (-3.95%)</td><td>0.24 (-5.95%)</td><td>0.24 (-6.20%)</td><td>0.01 <b>(+146.80%)</b></td><td>2193.20 (+6.62%)</td><td>2107.08 (+4.24%)</td><td>2152.16 (+6.33%)</td><td>1970.94 (-0.42%)</td><td>90.26 <b>(+161.53%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.00 (n/a)</td><td>2057.01 (n/a)</td><td>2021.31 (n/a)</td><td>2024.12 (n/a)</td><td>1979.34 (n/a)</td><td>34.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.37 (-1.20%)</td><td>0.36 (-0.67%)</td><td>0.37 (-0.49%)</td><td>0.36 (-0.86%)</td><td>0.01 (-17.50%)</td><td>1468.11 (+0.86%)</td><td>1437.17 (+0.66%)</td><td>1428.91 (+0.48%)</td><td>1416.92 (+1.21%)</td><td>21.81 (-16.02%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1455.66 (n/a)</td><td>1427.77 (n/a)</td><td>1422.14 (n/a)</td><td>1399.97 (n/a)</td><td>25.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.64 (-1.59%)</td><td>5.05 (+6.27%)</td><td>5.12 (-5.24%)</td><td>4.14 <b>(+23.47%)</b></td><td>0.60 <b>(-49.56%)</b></td><td>253.00 (-19.01%)</td><td>210.20 (-9.98%)</td><td>204.70 (+5.57%)</td><td>186.10 (+1.64%)</td><td>26.95 <b>(-58.09%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.73 (n/a)</td><td>4.75 (n/a)</td><td>5.41 (n/a)</td><td>3.36 (n/a)</td><td>1.19 (n/a)</td><td>312.40 (n/a)</td><td>233.50 (n/a)</td><td>193.90 (n/a)</td><td>183.10 (n/a)</td><td>64.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.70 (-2.66%)</td><td>4.58 (-14.57%)</td><td>3.91 <b>(-30.21%)</b></td><td>3.77 (-16.91%)</td><td>1.01 <b>(+76.95%)</b></td><td>278.50 <b>(+20.35%)</b></td><td>237.52 <b>(+20.28%)</b></td><td>268.50 <b>(+43.28%)</b></td><td>183.90 (+2.74%)</td><td>48.54 <b>(+116.76%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.86 (n/a)</td><td>5.36 (n/a)</td><td>5.60 (n/a)</td><td>4.53 (n/a)</td><td>0.57 (n/a)</td><td>231.40 (n/a)</td><td>197.48 (n/a)</td><td>187.40 (n/a)</td><td>179.00 (n/a)</td><td>22.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.62 (-6.62%)</td><td>4.92 (+5.76%)</td><td>4.79 (+9.35%)</td><td>4.12 (+1.72%)</td><td>0.58 <b>(-26.21%)</b></td><td>254.50 (-1.70%)</td><td>215.68 (-6.17%)</td><td>219.10 (-8.56%)</td><td>186.70 (+7.11%)</td><td>26.04 (-19.58%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>6.02 (n/a)</td><td>4.65 (n/a)</td><td>4.38 (n/a)</td><td>4.05 (n/a)</td><td>0.78 (n/a)</td><td>258.90 (n/a)</td><td>229.86 (n/a)</td><td>239.60 (n/a)</td><td>174.30 (n/a)</td><td>32.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.68 (+5.88%)</td><td>5.22 (+5.87%)</td><td>5.19 (-1.92%)</td><td>4.66 (+15.62%)</td><td>0.41 <b>(-30.62%)</b></td><td>224.90 (-13.50%)</td><td>201.98 (-6.25%)</td><td>202.00 (+1.97%)</td><td>184.80 (-5.52%)</td><td>16.01 <b>(-42.88%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.36 (n/a)</td><td>4.93 (n/a)</td><td>5.29 (n/a)</td><td>4.03 (n/a)</td><td>0.58 (n/a)</td><td>260.00 (n/a)</td><td>215.44 (n/a)</td><td>198.10 (n/a)</td><td>195.60 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.57 (+5.10%)</td><td>8.48 (+0.70%)</td><td>8.22 (-3.12%)</td><td>7.60 (-1.08%)</td><td>0.81 <b>(+40.40%)</b></td><td>275.90 (+1.10%)</td><td>249.18 (-0.36%)</td><td>255.20 (+3.24%)</td><td>219.10 (-4.86%)</td><td>23.31 <b>(+34.39%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.11 (n/a)</td><td>8.42 (n/a)</td><td>8.48 (n/a)</td><td>7.68 (n/a)</td><td>0.58 (n/a)</td><td>272.90 (n/a)</td><td>250.08 (n/a)</td><td>247.20 (n/a)</td><td>230.30 (n/a)</td><td>17.35 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.95 (+8.37%)</td><td>8.45 (+5.01%)</td><td>7.83 (+2.72%)</td><td>7.46 (+4.63%)</td><td>1.12 (+11.40%)</td><td>281.10 (-4.42%)</td><td>251.52 (-4.63%)</td><td>268.00 (-2.62%)</td><td>210.80 (-7.71%)</td><td>31.64 (-0.72%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.18 (n/a)</td><td>8.05 (n/a)</td><td>7.62 (n/a)</td><td>7.13 (n/a)</td><td>1.00 (n/a)</td><td>294.10 (n/a)</td><td>263.74 (n/a)</td><td>275.20 (n/a)</td><td>228.40 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.34 (+2.74%)</td><td>7.81 (-0.60%)</td><td>7.21 (-12.22%)</td><td>6.69 (+1.67%)</td><td>1.14 (+9.10%)</td><td>313.30 (-1.63%)</td><td>273.08 (+0.78%)</td><td>291.00 (+13.94%)</td><td>224.50 (-2.65%)</td><td>37.95 (+2.40%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.09 (n/a)</td><td>7.85 (n/a)</td><td>8.21 (n/a)</td><td>6.58 (n/a)</td><td>1.04 (n/a)</td><td>318.50 (n/a)</td><td>270.96 (n/a)</td><td>255.40 (n/a)</td><td>230.60 (n/a)</td><td>37.06 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>8.30 (-14.47%)</td><td>7.88 (-4.53%)</td><td>8.12 (+3.05%)</td><td>7.37 (+4.87%)</td><td>0.45 <b>(-60.72%)</b></td><td>284.60 (-4.66%)</td><td>266.86 (+3.46%)</td><td>258.20 (-2.93%)</td><td>252.50 (+16.90%)</td><td>15.44 <b>(-55.54%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.71 (n/a)</td><td>8.25 (n/a)</td><td>7.88 (n/a)</td><td>7.03 (n/a)</td><td>1.14 (n/a)</td><td>298.50 (n/a)</td><td>257.94 (n/a)</td><td>266.00 (n/a)</td><td>216.00 (n/a)</td><td>34.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.08 (-8.50%)</td><td>7.90 (-2.21%)</td><td>7.70 (-1.26%)</td><td>7.21 <b>(+30.83%)</b></td><td>0.71 <b>(-59.43%)</b></td><td>290.90 <b>(-23.57%)</b></td><td>267.20 (-1.47%)</td><td>272.40 (+1.30%)</td><td>230.90 (+9.28%)</td><td>22.34 <b>(-66.76%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>9.93 (n/a)</td><td>8.07 (n/a)</td><td>7.80 (n/a)</td><td>5.51 (n/a)</td><td>1.75 (n/a)</td><td>380.60 (n/a)</td><td>271.18 (n/a)</td><td>268.90 (n/a)</td><td>211.30 (n/a)</td><td>67.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>10.62 <b>(+20.85%)</b></td><td>8.67 (+7.24%)</td><td>8.89 (+11.31%)</td><td>6.86 (-2.13%)</td><td>1.37 <b>(+90.16%)</b></td><td>305.50 (+2.17%)</td><td>246.76 (-5.46%)</td><td>235.90 (-10.17%)</td><td>197.50 (-17.26%)</td><td>39.77 <b>(+62.71%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>8.78 (n/a)</td><td>8.09 (n/a)</td><td>7.99 (n/a)</td><td>7.01 (n/a)</td><td>0.72 (n/a)</td><td>299.00 (n/a)</td><td>261.02 (n/a)</td><td>262.60 (n/a)</td><td>238.70 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>11.98 (-4.44%)</td><td>11.41 (+0.99%)</td><td>11.70 (-0.40%)</td><td>10.68 (+16.37%)</td><td>0.64 <b>(-53.21%)</b></td><td>392.70 (-14.07%)</td><td>368.42 (-2.01%)</td><td>358.60 (+0.42%)</td><td>350.20 (+4.63%)</td><td>21.08 <b>(-57.96%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>12.53 (n/a)</td><td>11.30 (n/a)</td><td>11.74 (n/a)</td><td>9.18 (n/a)</td><td>1.37 (n/a)</td><td>457.00 (n/a)</td><td>375.98 (n/a)</td><td>357.10 (n/a)</td><td>334.70 (n/a)</td><td>50.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.26 (-0.86%)</td><td>12.44 (+1.48%)</td><td>12.92 (+8.27%)</td><td>10.78 (-4.27%)</td><td>1.05 (+8.88%)</td><td>389.00 (+4.46%)</td><td>339.32 (-1.34%)</td><td>324.60 (-7.65%)</td><td>316.20 (+0.86%)</td><td>30.75 (+15.21%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.38 (n/a)</td><td>12.26 (n/a)</td><td>11.93 (n/a)</td><td>11.26 (n/a)</td><td>0.97 (n/a)</td><td>372.40 (n/a)</td><td>343.92 (n/a)</td><td>351.50 (n/a)</td><td>313.50 (n/a)</td><td>26.69 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>11.71 (-13.54%)</td><td>11.02 (-7.04%)</td><td>11.15 (-9.82%)</td><td>10.14 (+2.60%)</td><td>0.62 <b>(-60.44%)</b></td><td>413.60 (-2.54%)</td><td>381.62 (+6.28%)</td><td>376.10 (+10.88%)</td><td>358.30 (+15.66%)</td><td>21.92 <b>(-55.56%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>13.54 (n/a)</td><td>11.85 (n/a)</td><td>12.37 (n/a)</td><td>9.88 (n/a)</td><td>1.57 (n/a)</td><td>424.40 (n/a)</td><td>359.08 (n/a)</td><td>339.20 (n/a)</td><td>309.80 (n/a)</td><td>49.33 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>14.37 (-17.16%)</td><td>13.02 (-7.41%)</td><td>12.83 (-1.95%)</td><td>12.27 (-3.18%)</td><td>0.88 <b>(-55.01%)</b></td><td>342.00 (+3.29%)</td><td>323.26 (+6.91%)</td><td>327.00 (+2.00%)</td><td>291.90 <b>(+20.72%)</b></td><td>21.13 <b>(-43.48%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>17.35 (n/a)</td><td>14.06 (n/a)</td><td>13.08 (n/a)</td><td>12.67 (n/a)</td><td>1.96 (n/a)</td><td>331.10 (n/a)</td><td>302.38 (n/a)</td><td>320.60 (n/a)</td><td>241.80 (n/a)</td><td>37.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>14.95 (+0.92%)</td><td>12.92 (-2.38%)</td><td>13.74 (-2.77%)</td><td>9.56 (-6.78%)</td><td>2.08 (+6.72%)</td><td>438.80 (+7.29%)</td><td>332.76 (+2.94%)</td><td>305.30 (+2.83%)</td><td>280.60 (-0.88%)</td><td>62.70 (+17.31%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>14.81 (n/a)</td><td>13.23 (n/a)</td><td>14.13 (n/a)</td><td>10.25 (n/a)</td><td>1.95 (n/a)</td><td>409.00 (n/a)</td><td>323.26 (n/a)</td><td>296.90 (n/a)</td><td>283.10 (n/a)</td><td>53.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>15.32 (+5.60%)</td><td>13.63 (+2.37%)</td><td>13.56 (-3.36%)</td><td>11.88 (+17.55%)</td><td>1.23 <b>(-32.76%)</b></td><td>353.20 (-14.93%)</td><td>309.70 (-3.45%)</td><td>309.20 (+3.48%)</td><td>273.70 (-5.29%)</td><td>28.54 <b>(-46.44%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>14.51 (n/a)</td><td>13.32 (n/a)</td><td>14.04 (n/a)</td><td>10.10 (n/a)</td><td>1.83 (n/a)</td><td>415.20 (n/a)</td><td>320.78 (n/a)</td><td>298.80 (n/a)</td><td>289.00 (n/a)</td><td>53.28 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>15.54 (+0.21%)</td><td>13.50 (-5.37%)</td><td>13.03 (-13.13%)</td><td>12.13 (+3.14%)</td><td>1.37 (-8.69%)</td><td>345.70 (-3.03%)</td><td>313.06 (+5.45%)</td><td>321.80 (+15.09%)</td><td>269.90 (-0.22%)</td><td>30.30 (-13.12%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>15.51 (n/a)</td><td>14.27 (n/a)</td><td>15.00 (n/a)</td><td>11.76 (n/a)</td><td>1.50 (n/a)</td><td>356.50 (n/a)</td><td>296.88 (n/a)</td><td>279.60 (n/a)</td><td>270.50 (n/a)</td><td>34.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.61 (-6.99%)</td><td>12.38 (+2.71%)</td><td>12.86 (+7.01%)</td><td>10.49 (+13.92%)</td><td>1.24 <b>(-46.85%)</b></td><td>400.00 (-12.22%)</td><td>341.82 (-4.82%)</td><td>326.20 (-6.56%)</td><td>308.20 (+7.54%)</td><td>36.72 <b>(-48.85%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>14.63 (n/a)</td><td>12.05 (n/a)</td><td>12.02 (n/a)</td><td>9.20 (n/a)</td><td>2.34 (n/a)</td><td>455.70 (n/a)</td><td>359.12 (n/a)</td><td>349.10 (n/a)</td><td>286.60 (n/a)</td><td>71.79 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>2.92 (-3.81%)</td><td>2.67 (+2.13%)</td><td>2.61 (-1.64%)</td><td>2.51 (+15.46%)</td><td>0.16 <b>(-48.86%)</b></td><td>209.10 (-13.38%)</td><td>196.76 (-3.00%)</td><td>201.00 (+1.67%)</td><td>179.50 (+4.00%)</td><td>11.68 <b>(-54.54%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.04 (n/a)</td><td>2.62 (n/a)</td><td>2.65 (n/a)</td><td>2.17 (n/a)</td><td>0.32 (n/a)</td><td>241.40 (n/a)</td><td>202.84 (n/a)</td><td>197.70 (n/a)</td><td>172.60 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>6.12 (+2.68%)</td><td>4.42 (-17.46%)</td><td>4.31 <b>(-20.20%)</b></td><td>3.30 <b>(-31.04%)</b></td><td>1.09 <b>(+113.46%)</b></td><td>318.00 <b>(+45.01%)</b></td><td>248.02 <b>(+25.75%)</b></td><td>243.60 <b>(+25.31%)</b></td><td>171.30 (-2.62%)</td><td>55.90 <b>(+196.65%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>5.96 (n/a)</td><td>5.36 (n/a)</td><td>5.39 (n/a)</td><td>4.78 (n/a)</td><td>0.51 (n/a)</td><td>219.30 (n/a)</td><td>197.24 (n/a)</td><td>194.40 (n/a)</td><td>175.90 (n/a)</td><td>18.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>8.20 (-0.04%)</td><td>6.97 (-8.36%)</td><td>7.07 (-9.69%)</td><td>5.87 (-13.95%)</td><td>0.97 <b>(+58.84%)</b></td><td>357.30 (+16.23%)</td><td>305.58 (+10.27%)</td><td>296.60 (+10.75%)</td><td>255.60 (+0.04%)</td><td>42.84 <b>(+86.90%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>8.21 (n/a)</td><td>7.61 (n/a)</td><td>7.83 (n/a)</td><td>6.82 (n/a)</td><td>0.61 (n/a)</td><td>307.40 (n/a)</td><td>277.12 (n/a)</td><td>267.80 (n/a)</td><td>255.50 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>2.86 (-12.63%)</td><td>2.68 (-7.64%)</td><td>2.84 (-5.15%)</td><td>2.29 (-4.82%)</td><td>0.25 <b>(-28.85%)</b></td><td>228.90 (+5.10%)</td><td>197.46 (+7.74%)</td><td>184.80 (+5.42%)</td><td>183.40 (+14.48%)</td><td>20.05 (-15.51%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>3.27 (n/a)</td><td>2.90 (n/a)</td><td>2.99 (n/a)</td><td>2.41 (n/a)</td><td>0.36 (n/a)</td><td>217.80 (n/a)</td><td>183.28 (n/a)</td><td>175.30 (n/a)</td><td>160.20 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (-3.25%)</td><td>0.21 (-7.48%)</td><td>0.22 (-14.58%)</td><td>0.17 (+5.51%)</td><td>0.04 (-17.39%)</td><td>197.60 (-5.18%)</td><td>158.66 (+6.76%)</td><td>150.70 (+17.09%)</td><td>128.10 (+3.31%)</td><td>29.41 (-18.07%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>208.40 (n/a)</td><td>148.62 (n/a)</td><td>128.70 (n/a)</td><td>124.00 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (-7.10%)</td><td>0.19 (-10.80%)</td><td>0.18 (-1.92%)</td><td>0.16 (+0.58%)</td><td>0.04 <b>(-22.66%)</b></td><td>211.00 (-0.61%)</td><td>180.92 (+10.45%)</td><td>179.90 (+1.93%)</td><td>131.30 (+7.62%)</td><td>32.97 (-13.27%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>212.30 (n/a)</td><td>163.80 (n/a)</td><td>176.50 (n/a)</td><td>122.00 (n/a)</td><td>38.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.49 (-6.58%)</td><td>0.38 (-19.95%)</td><td>0.40 (-13.96%)</td><td>0.30 <b>(-32.16%)</b></td><td>0.08 <b>(+163.54%)</b></td><td>220.60 <b>(+47.36%)</b></td><td>178.34 <b>(+29.16%)</b></td><td>162.70 (+16.30%)</td><td>134.40 (+7.01%)</td><td>38.17 <b>(+335.68%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.52 (n/a)</td><td>0.48 (n/a)</td><td>0.47 (n/a)</td><td>0.44 (n/a)</td><td>0.03 (n/a)</td><td>149.70 (n/a)</td><td>138.08 (n/a)</td><td>139.90 (n/a)</td><td>125.60 (n/a)</td><td>8.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.44 (-18.09%)</td><td>0.36 <b>(-20.03%)</b></td><td>0.35 <b>(-27.56%)</b></td><td>0.30 (-15.83%)</td><td>0.05 <b>(-40.31%)</b></td><td>219.20 (+18.81%)</td><td>185.16 <b>(+23.23%)</b></td><td>185.60 <b>(+38.10%)</b></td><td>150.00 <b>(+22.15%)</b></td><td>24.50 (-16.55%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.49 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>184.50 (n/a)</td><td>150.26 (n/a)</td><td>134.40 (n/a)</td><td>122.80 (n/a)</td><td>29.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.36 <b>(-30.66%)</b></td><td>0.33 <b>(-24.16%)</b></td><td>0.34 (-18.07%)</td><td>0.28 (-19.42%)</td><td>0.04 <b>(-42.20%)</b></td><td>232.50 <b>(+24.13%)</b></td><td>200.54 <b>(+30.92%)</b></td><td>190.30 <b>(+22.07%)</b></td><td>180.50 <b>(+44.17%)</b></td><td>23.56 (+2.36%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.06 (n/a)</td><td>187.30 (n/a)</td><td>153.18 (n/a)</td><td>155.90 (n/a)</td><td>125.20 (n/a)</td><td>23.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.14 (+5.56%)</td><td>0.81 (-7.56%)</td><td>0.73 (-16.41%)</td><td>0.57 (-5.04%)</td><td>0.24 (+18.77%)</td><td>228.10 (+5.26%)</td><td>174.34 (+10.50%)</td><td>179.00 (+19.65%)</td><td>115.40 (-5.25%)</td><td>48.95 <b>(+22.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>1.08 (n/a)</td><td>0.87 (n/a)</td><td>0.88 (n/a)</td><td>0.60 (n/a)</td><td>0.20 (n/a)</td><td>216.70 (n/a)</td><td>157.78 (n/a)</td><td>149.60 (n/a)</td><td>121.80 (n/a)</td><td>39.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.04 <b>(+30.57%)</b></td><td>0.77 (+5.97%)</td><td>0.69 (-9.89%)</td><td>0.62 (+1.11%)</td><td>0.18 <b>(+135.97%)</b></td><td>210.30 (-1.13%)</td><td>176.26 (-2.85%)</td><td>189.60 (+10.94%)</td><td>126.60 <b>(-23.41%)</b></td><td>36.35 <b>(+81.30%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.79 (n/a)</td><td>0.73 (n/a)</td><td>0.77 (n/a)</td><td>0.62 (n/a)</td><td>0.08 (n/a)</td><td>212.70 (n/a)</td><td>181.44 (n/a)</td><td>170.90 (n/a)</td><td>165.30 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.80 (-18.59%)</td><td>0.75 (-7.52%)</td><td>0.77 (-2.80%)</td><td>0.66 (-7.09%)</td><td>0.05 <b>(-49.33%)</b></td><td>199.90 (+7.65%)</td><td>175.60 (+7.22%)</td><td>170.60 (+2.90%)</td><td>164.00 <b>(+22.85%)</b></td><td>13.99 <b>(-31.36%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.98 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.71 (n/a)</td><td>0.11 (n/a)</td><td>185.70 (n/a)</td><td>163.78 (n/a)</td><td>165.80 (n/a)</td><td>133.50 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.06 <b>(+26.58%)</b></td><td>0.77 (+3.58%)</td><td>0.73 (-4.65%)</td><td>0.64 (+3.37%)</td><td>0.16 <b>(+105.86%)</b></td><td>203.20 (-3.28%)</td><td>174.42 (-1.48%)</td><td>180.00 (+4.90%)</td><td>124.00 <b>(-21.02%)</b></td><td>30.89 <b>(+51.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.83 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.62 (n/a)</td><td>0.08 (n/a)</td><td>210.10 (n/a)</td><td>177.04 (n/a)</td><td>171.60 (n/a)</td><td>157.00 (n/a)</td><td>20.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (-16.94%)</td><td>0.08 <b>(-25.83%)</b></td><td>0.07 <b>(-34.81%)</b></td><td>0.06 <b>(-26.20%)</b></td><td>0.02 (-1.05%)</td><td>272.80 <b>(+35.52%)</b></td><td>214.10 <b>(+36.72%)</b></td><td>224.80 <b>(+53.34%)</b></td><td>159.20 <b>(+20.42%)</b></td><td>45.99 <b>(+59.78%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:49:19</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.30 (n/a)</td><td>156.60 (n/a)</td><td>146.60 (n/a)</td><td>132.20 (n/a)</td><td>28.79 (n/a)</td>
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
