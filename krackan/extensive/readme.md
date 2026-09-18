
# IRON

Tested on `2026_09_18_21_55_17` at commit `5320ada`.

<details>
<summary>iron/operators/axpy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>136.24</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>165.44</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>172.82</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>159.24</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]</td><td>✅ 5/5</td><td>150.80</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]</td><td>✅ 5/5</td><td>157.40</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0]</td><td>✅ 5/5</td><td>153.50</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0]</td><td>✅ 5/5</td><td>164.08</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>151.80</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>142.28</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>174.00</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>157.56</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>194.56</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>158.74</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0]</td><td>✅ 5/5</td><td>212.52</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0]</td><td>✅ 5/5</td><td>181.90</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>189.66</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>180.68</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>174.22</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>166.02</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>164.56</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>143.82</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>171.58</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>158.20</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]</td><td>✅ 5/5</td><td>153.12</td><td>0.33</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]</td><td>✅ 5/5</td><td>134.34</td><td>0.37</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>157.78</td><td>0.32</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>154.84</td><td>0.34</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>204.62</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>165.22</td><td>0.32</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>190.26</td><td>0.26</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>161.88</td><td>0.31</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/dequant</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>161.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>161.60</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>146.80</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>188.62</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>169.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>179.92</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>192.34</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32]</td><td>✅ 5/5</td><td>228.62</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>188.40</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>167.40</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>174.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>177.28</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>165.46</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>159.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>188.78</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>198.44</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>210.12</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>189.68</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>178.24</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>185.28</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>185.60</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>180.98</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>192.98</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>222.28</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]</td><td>✅ 5/5</td><td>177.04</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>183.34</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>201.42</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>177.20</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>188.92</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>185.36</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>212.94</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>216.44</td><td>0.10</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>146.64</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>169.72</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>199.66</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128]</td><td>✅ 5/5</td><td>197.00</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>164.00</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>184.08</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>187.04</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256]</td><td>✅ 5/5</td><td>177.90</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>152.78</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>165.00</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>172.32</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512]</td><td>✅ 5/5</td><td>220.12</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]</td><td>✅ 5/5</td><td>179.28</td><td>0.28</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>179.76</td><td>0.27</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>171.48</td><td>0.29</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024]</td><td>✅ 5/5</td><td>173.20</td><td>0.29</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>136.54</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>169.94</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>188.54</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128]</td><td>✅ 5/5</td><td>184.22</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>154.26</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>177.52</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>164.84</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256]</td><td>✅ 5/5</td><td>195.68</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>171.44</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>142.64</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>188.76</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512]</td><td>✅ 5/5</td><td>182.04</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>157.34</td><td>0.32</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>177.50</td><td>0.29</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024]</td><td>✅ 5/5</td><td>206.28</td><td>0.25</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>3951.16</td><td>14.13</td><td>13613.42</td></tr>
        <tr><td>test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>1092.16</td><td>12.51</td><td>8201.36</td></tr>
        <tr><td>test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>4163.74</td><td>13.54</td><td>13048.79</td></tr>
        <tr><td>test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>1562.22</td><td>11.98</td><td>9003.94</td></tr>
        <tr><td>test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>7753.82</td><td>10.57</td><td>13858.06</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>1646.76</td><td>13.34</td><td>10663.06</td></tr>
        <tr><td>test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>7643.34</td><td>10.72</td><td>14055.16</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>446.68</td><td>3.13</td><td>610.21</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even]</td><td>✅ 5/5</td><td>391.28</td><td>3.52</td><td>687.10</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>347.32</td><td>4.17</td><td>812.72</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor]</td><td>✅ 5/5</td><td>325.32</td><td>4.55</td><td>887.31</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>410.80</td><td>3.36</td><td>655.67</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>443.58</td><td>3.12</td><td>607.93</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor]</td><td>✅ 5/5</td><td>445.72</td><td>3.09</td><td>603.05</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>321.86</td><td>1.30</td><td>108.84</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>387.12</td><td>5.03</td><td>1047.18</td></tr>
        <tr><td>test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>416.56</td><td>13.95</td><td>5443.63</td></tr>
        <tr><td>test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even]</td><td>✅ 5/5</td><td>657.10</td><td>8.50</td><td>3315.08</td></tr>
        <tr><td>test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>663.74</td><td>8.79</td><td>3660.92</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma32]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma32]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma32]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn64-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn64-ma32-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn64-ma64]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/mm_prebuilt</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_mm_prebuilt[M_256-K_512-N_1024-epilogue_gelu-clamp_None]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mm_prebuilt[M_256-K_512-N_1024-epilogue_none-clamp_None]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mm_prebuilt[M_256-K_512-N_1024-epilogue_silu-clamp_None]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mm_prebuilt[M_256-K_512-N_1280-epilogue_none-clamp_None]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mm_prebuilt[M_256-K_512-N_640-epilogue_none-clamp_None]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mm_prebuilt[M_512-K_1024-N_2048-epilogue_none-clamp_None]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mm_prebuilt_epilogue_matches_accumulator[epilogue_gelu-clamp_None]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mm_prebuilt_epilogue_matches_accumulator[epilogue_none-clamp_(-2.0, 2.0)]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mm_prebuilt_epilogue_matches_accumulator[epilogue_sigmoid-clamp_None]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mm_prebuilt_epilogue_matches_accumulator[epilogue_silu-clamp_None]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gelu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>183.26</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>157.94</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>179.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>215.46</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>188.28</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>189.54</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>203.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>209.46</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>167.74</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>187.70</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>174.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>168.00</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>173.18</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>171.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>175.86</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>209.06</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>175.74</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>196.24</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>181.70</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>170.40</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>180.72</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>207.10</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>189.48</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>228.32</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 5/5</td><td>196.28</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>173.80</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>220.30</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>183.46</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>165.36</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>156.26</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>177.24</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>190.62</td><td>0.17</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gemm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>19151.38</td><td>4.11</td><td>2803.33</td></tr>
        <tr><td>test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>2199.46</td><td>4.28</td><td>1682.83</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>255.86</td><td>0.87</td><td>37.33</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>277.30</td><td>0.82</td><td>35.10</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>47697.24</td><td>0.53</td><td>360.19</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>118869.14</td><td>0.21</td><td>144.53</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>27893.64</td><td>0.90</td><td>615.92</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>7087.90</td><td>3.55</td><td>2425.45</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>8388.88</td><td>3.00</td><td>2051.03</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>7895.16</td><td>3.19</td><td>2176.15</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>94752.08</td><td>0.80</td><td>725.26</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>103341.44</td><td>0.73</td><td>664.97</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>110377.96</td><td>0.68</td><td>622.59</td></tr>
        <tr><td>test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>37485.04</td><td>2.80</td><td>2864.45</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1255.88</td><td>7.12</td><td>429.07</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1329.72</td><td>6.71</td><td>404.16</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1456.62</td><td>6.13</td><td>369.50</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4452.38</td><td>7.84</td><td>482.73</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4565.16</td><td>7.64</td><td>470.55</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4851.48</td><td>7.20</td><td>443.59</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>94254.90</td><td>0.80</td><td>729.08</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>102616.52</td><td>0.74</td><td>669.67</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>105964.96</td><td>0.71</td><td>648.51</td></tr>
        <tr><td>test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>2432.66</td><td>3.36</td><td>881.94</td></tr>
        <tr><td>test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4]</td><td>✅ 5/5</td><td>3502.38</td><td>0.39</td><td>20.77</td></tr>
        <tr><td>test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1404.06</td><td>4.91</td><td>1516.82</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gemv</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>n/a</td><td>0.24</td><td>0.23</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>n/a</td><td>12.30</td><td>12.30</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>23.20</td><td>23.19</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]</td><td>✅ 5/5</td><td>n/a</td><td>39.71</td><td>39.69</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256]</td><td>✅ 5/5</td><td>n/a</td><td>44.74</td><td>44.72</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>12.23</td><td>12.22</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>23.71</td><td>23.70</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>41.17</td><td>41.14</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>40.29</td><td>40.27</td></tr>
        <tr><td>test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]</td><td>✅ 5/5</td><td>n/a</td><td>8.98</td><td>8.96</td></tr>
        <tr><td>test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]</td><td>✅ 5/5</td><td>n/a</td><td>0.96</td><td>0.94</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 5/5</td><td>n/a</td><td>1.20</td><td>1.19</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100]</td><td>✅ 5/5</td><td>n/a</td><td>17.21</td><td>17.01</td></tr>
        <tr><td>test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192]</td><td>✅ 5/5</td><td>n/a</td><td>13.23</td><td>12.99</td></tr>
        <tr><td>test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32]</td><td>✅ 5/5</td><td>n/a</td><td>7.76</td><td>7.62</td></tr>
        <tr><td>test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]</td><td>✅ 5/5</td><td>n/a</td><td>6.04</td><td>5.95</td></tr>
        <tr><td>test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>n/a</td><td>0.19</td><td>0.19</td></tr>
        <tr><td>test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>n/a</td><td>12.37</td><td>12.36</td></tr>
        <tr><td>test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>12.58</td><td>12.57</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/layer_norm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>165.40</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>166.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>170.14</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>166.04</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>184.96</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>189.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>163.62</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>184.80</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>150.44</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>191.64</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>174.36</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>161.02</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>164.40</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>204.60</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>189.08</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>224.56</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>164.98</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>180.62</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>181.10</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>173.28</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>180.28</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>194.52</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>166.58</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>208.50</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 5/5</td><td>189.24</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>171.54</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>183.10</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>185.10</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>184.88</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>194.64</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>188.08</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>209.66</td><td>0.16</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>169.06</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>156.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>163.52</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>164.98</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>152.96</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>182.66</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>169.42</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01]</td><td>✅ 5/5</td><td>213.92</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>160.56</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]</td><td>✅ 5/5</td><td>176.92</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]</td><td>✅ 5/5</td><td>171.42</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>142.42</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>162.18</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>174.76</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>167.54</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>173.32</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>170.36</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>234.64</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>153.24</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>152.50</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>164.48</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>148.96</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>141.26</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>180.32</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>158.72</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>197.12</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>166.22</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>131.20</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>139.94</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>150.78</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>148.78</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>161.88</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>185.70</td><td>0.18</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/mem_copy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>146.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>152.78</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64]</td><td>❌ 0/5</td><td>4746043.57</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64]</td><td>✅ 5/5</td><td>174.88</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>164.46</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>185.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>148.30</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>168.00</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>187.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>196.50</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>179.28</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>175.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>181.20</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>169.92</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>178.18</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>172.58</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>164.94</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>178.32</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>204.72</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>193.66</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>151.60</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>174.56</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>187.06</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>174.84</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>188.12</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>182.82</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>170.70</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>170.86</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>179.90</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>174.80</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>204.60</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>174.56</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>167.78</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>174.84</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>198.18</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>179.06</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>189.88</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>153.10</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>170.38</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>172.46</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>201.92</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>162.80</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>145.16</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>150.66</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>183.58</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>187.70</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>171.62</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>188.42</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]</td><td>✅ 5/5</td><td>159.88</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]</td><td>✅ 5/5</td><td>139.98</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>207.02</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>201.46</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>165.28</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>140.40</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>182.86</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>154.14</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>182.66</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>157.04</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>176.96</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>161.76</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>165.56</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>168.88</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>195.50</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>183.12</td><td>0.18</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/mha</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0]</td><td>✅ 5/5</td><td>52335.40</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]</td><td>✅ 5/5</td><td>52262.94</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]</td><td>✅ 5/5</td><td>413130.76</td><td>0.10</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/relu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>158.18</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>145.64</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>181.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>215.02</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>181.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>196.54</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>194.56</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>210.96</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>190.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>193.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>197.92</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>178.72</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>180.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>193.42</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>187.28</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>243.06</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>174.44</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>146.74</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>176.16</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>170.86</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>147.62</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>182.78</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>193.46</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>228.88</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>175.94</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>181.82</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>167.34</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>204.62</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>165.60</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>173.96</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>233.80</td><td>0.15</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/repeat</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>164.70</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>165.46</td><td>0.30</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>844.66</td><td>12.42</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>191.02</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]</td><td>✅ 5/5</td><td>198.68</td><td>0.03</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/rms_norm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>143.22</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>159.18</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>155.56</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>192.54</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>175.38</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>170.98</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>175.54</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>201.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>165.24</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>209.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>185.86</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True]</td><td>✅ 5/5</td><td>194.82</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>172.98</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True]</td><td>✅ 5/5</td><td>200.08</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False]</td><td>✅ 5/5</td><td>189.70</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>162.16</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>189.52</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>174.34</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>173.62</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>144.98</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>154.04</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>157.50</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>180.54</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>166.02</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>176.00</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>203.36</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>219.62</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>196.72</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>193.24</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>216.26</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>169.80</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>191.22</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>153.46</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>161.46</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>250.30</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>162.68</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>194.66</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>174.96</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>211.20</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>174.64</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>209.08</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>175.80</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>208.14</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>176.12</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>248.80</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]</td><td>✅ 5/5</td><td>184.14</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>190.08</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>171.94</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>199.70</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>169.40</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>214.84</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>171.02</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>176.96</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>164.56</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>218.56</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>211.16</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>198.90</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>188.22</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>235.16</td><td>0.15</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/rope</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>149.28</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>146.58</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>181.52</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>201.20</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>175.68</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>174.42</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>178.98</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>178.92</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>141.48</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>151.96</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>185.46</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>157.86</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>183.24</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>198.26</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>175.80</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>189.00</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>179.82</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>157.44</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>182.08</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>165.70</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>173.84</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>164.62</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>230.02</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>203.46</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>163.92</td><td>0.62</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>203.30</td><td>0.50</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>189.60</td><td>0.52</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>162.96</td><td>0.62</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>153.08</td><td>0.50</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>178.56</td><td>0.43</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>239.30</td><td>0.33</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>209.92</td><td>0.35</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>175.10</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>177.48</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>185.04</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>158.94</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>160.96</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>195.62</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>204.34</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>192.76</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>170.16</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>184.36</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>181.32</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>194.38</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>184.40</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>187.94</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>207.32</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>183.32</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>173.08</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>180.50</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>176.48</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>176.72</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>169.88</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>161.36</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>217.28</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>206.40</td><td>0.17</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/sigmoid</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>155.26</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>178.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>154.48</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>182.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>167.00</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>179.58</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>175.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>225.38</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>172.02</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>186.50</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>170.14</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>189.56</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>169.56</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>175.02</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>179.76</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>209.48</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>195.26</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>140.82</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>158.02</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>170.30</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>156.58</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>164.56</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>199.56</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>187.36</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>166.12</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>168.28</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>178.68</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>159.04</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>166.90</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>172.82</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>234.44</td><td>0.15</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/silu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>168.60</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>150.42</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>166.34</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>166.60</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>159.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>179.28</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>149.30</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>169.50</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>146.90</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>134.96</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>150.98</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>159.74</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>169.44</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>184.22</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>197.80</td><td>0.17</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/softmax</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>158.36</td><td>0.85</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>152.30</td><td>0.88</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>138.74</td><td>0.96</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/strided_copy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_strided_copy[chunked_transfer]</td><td>✅ 5/5</td><td>136.44</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[contiguous]</td><td>✅ 5/5</td><td>143.16</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[four_channels]</td><td>✅ 5/5</td><td>172.16</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_llama_full]</td><td>✅ 5/5</td><td>151.90</td><td>14.20</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot0]</td><td>✅ 5/5</td><td>129.48</td><td>1.02</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5]</td><td>✅ 5/5</td><td>156.58</td><td>0.86</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_four_channels]</td><td>✅ 5/5</td><td>154.16</td><td>0.88</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_two_channels]</td><td>✅ 5/5</td><td>144.90</td><td>0.94</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot_last]</td><td>✅ 5/5</td><td>147.72</td><td>0.90</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels]</td><td>✅ 5/5</td><td>147.30</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels_chunked]</td><td>✅ 5/5</td><td>162.02</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]</td><td>✅ 5/5</td><td>934.26</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]</td><td>✅ 5/5</td><td>1023.82</td><td>0.01</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False]</td><td>✅ 5/5</td><td>2213.15</td><td>0.95</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/tanh</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>172.00</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>170.84</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>171.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>186.98</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>209.86</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>188.28</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>180.74</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>241.58</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>214.46</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>174.96</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>181.88</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>170.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>163.04</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>218.68</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>191.62</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>246.38</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>175.22</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>174.74</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>173.74</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>168.70</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>174.96</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>188.18</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>189.82</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>223.64</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>162.96</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>168.52</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>184.84</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>193.04</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>190.24</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>194.34</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>213.82</td><td>0.15</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/transpose</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tiling_that_fits_is_still_accepted[aie_columns_1]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tiling_that_fits_is_still_accepted[aie_columns_2]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tiling_that_fits_is_still_accepted[aie_columns_4]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>211.90</td><td>5.01</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>210.48</td><td>5.02</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>219.54</td><td>4.81</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>204.24</td><td>5.30</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>272.14</td><td>7.78</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>267.44</td><td>7.89</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>267.88</td><td>7.85</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>269.14</td><td>7.96</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>267.38</td><td>7.94</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>248.30</td><td>8.52</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>378.96</td><td>11.13</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>343.92</td><td>12.25</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>366.26</td><td>11.51</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>323.22</td><td>13.10</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>348.04</td><td>12.06</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>345.88</td><td>12.24</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>329.58</td><td>12.80</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>346.96</td><td>12.11</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>184.62</td><td>2.87</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]</td><td>✅ 5/5</td><td>242.54</td><td>4.48</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]</td><td>✅ 5/5</td><td>284.16</td><td>7.49</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>229.26</td><td>2.51</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>173.00</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>167.84</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>157.58</td><td>0.42</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>154.84</td><td>0.43</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>165.70</td><td>0.41</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>211.40</td><td>0.72</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>163.36</td><td>0.81</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>170.22</td><td>0.78</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>153.52</td><td>0.86</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>169.82</td><td>0.10</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

