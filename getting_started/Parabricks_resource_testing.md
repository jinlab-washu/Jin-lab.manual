# The resource testing result for Parabricks germline pipeline

Some testing result on compute1 around 2021 May

## Teala V100

### TEST - `pbrun germline`

| Test Run #  | GPU | CPU | MEM GB | Sample | Time_MAX | MEM_Max | Note |
| ----------- | --- | --- | ------ | ------ |  ------- | ------- | ---- |
| 1 | 2  | 24  | 256 | ERR1726424_wgs (33+38 GB) | 93 minutes 6 seconds | 235.26 GB | SUCCESSED |
| 2 | 2  | 24  | 256 | ERR1726424_wgs (33+38 GB)  | 295 minutes 46 seconds | 235.26 GB | SUCCESSED |
| 3 | 2  | 24  | 256 | ERR1726424_wgs (33+38 GB)  | 127 minutes 35 seconds | 236.74 GB | SUCCESSED |
| 4 | 2  | 24  | 256 | ERR1726424_wgs (33+38 GB)  | 170 minutes 14 seconds | 237.40 GB | SUCCESSED |
| 6 | 2  | 24  | 256 | NA12878_downsampling (32+35 GB) | 80 minutes 17 seconds | 70.58 GB | SUCCESSED |
| 7 | 2  | 24  | 256 | NA12878_downsampling (32+35 GB) | - | - | FAILD |
| 8 | 2  | 24  | 256 | NA12878_downsampling (32+35 GB) | 73 minutes 40 seconds | 82.64 GB | SUCCESSED |
| 9 | 2  | 24  | 256 | NA12878_Sample_U0a  (500 MB) | 3 minutes 7 seconds | 3.66 GB | SUCCESSED |
| 10 | 2  | 24  | 360 | NA12878_300X  (367+393 GB) | 563 minutes 38 seconds | 263.41 GB | SUCCESSED |
| 11 | 2  | 24  | 480 | NA12878_300X  (367+393 GB) | - | - | KILLED |
| 12 | 4  | 32  | 360 | NA12878_300X  (367+393 GB) | - | - | FAILD...NOT Enough MEM |
| 17 | 3  | 32  | 360 | NA12878_300X  (367+393 GB) | - | - | FAILD |
| 18 | 3  | 32  | 256 | NA12878_downsampling (32+35 GB) | - | - | FAILD |

### TEST - multiple steps

| GPU MODEL | OUTDIR | GZip | GPU | CPU | MEM | Sample | BWA Time | Sorting Time | BQSR MEM | BQSR Time | HaplotypeCaller Time | CollectWGSMetrics Time | collectmultiplemetrics Time | Note | Script |
| ------ | ------ | ---- | --- | --- | --- | ------ | -------- | ------------ | -------- | --------- | -------------------- | --------------- | ------------ | ---- | ------ | 
| TeslaV100_SXM2_32GB | Scratch1 | with gz | 2 | 24 | 256GB | CP, KRU-F309-001-U (22GB+22GB) | 55 minutes 41 seconds | 1 minute 21 seconds | 234.25 GB | 8 minutes 22 seconds | 46 minutes 29 seconds | 18 minutes 6 seconds | 7 minutes 15 seconds | SUCCESSED | pbrun_mutiSteps_v3.5.0.1_pfuTest_v9_CP_1Trios_Scratch1.sh |
| TeslaV100_SXM2_32GB | Scratch1 | with gz | 2 | 24 | 256GB | CP, KRU-F309-002-U (20GB+21GB) | 51 minutes 3 seconds | 1 minute 10 seconds | 227.81 GB | 7 minutes 52 seconds | 42 minutes 28 seconds | 16 minutes 28 seconds | 6 minutes 7 seconds | SUCCESSED | pbrun_mutiSteps_v3.5.0.1_pfuTest_v9_CP_1Trios_Scratch1.sh |
| TeslaV100_SXM2_32GB | Scratch1 | with gz | 2 | 24 | 256GB | CP, KRU-F309-003-A (24GB+26GB) | 62 minutes 15 seconds | 1 minute 31 seconds | 236.34 GB | 8 minutes 51 seconds | 50 minutes 9 seconds | 17 minutes 11 seconds | 7 minutes 46 seconds | SUCCESSED | pbrun_mutiSteps_v3.5.0.1_pfuTest_v9_CP_1Trios_Scratch1.sh |

--------------------------------------

## TEST - Teala A100

### TEST - Teala A100 v3.5.0.1 (1st RUN, OUT OF MEM)

> Output dir on SCRATCH1

| Test Run #  | gModel | GPU | CPU | MEM GB | Sample | Time_MAX | MEM_Max | Note |
| ----------- | ------ | --- | --- | ------ | ------ |  ------- | ------- | ---- |
| 1 | TeslaA100_SXM4_40GB | 4 | 32 | 360 | NA12878_300X  (367+393 GB) | ??? | ??? | OUT_OF_MEM |
| 2 | TeslaA100_SXM4_40GB | 2 | 24 | 360 | NA12878_300X  (367+393 GB) | ??? | ??? | OUT_OF_MEM |
| 3 | TeslaA100_SXM4_40GB | 4 | 32 | 256 | NA12878_downsampling (32+35 GB) | 27 minutes 37 seconds | 250.67 GB | OUT_OF_MEM |
| 4 | TeslaA100_SXM4_40GB | 2 | 24 | 196 | NA12878_downsampling (32+35 GB) | 51 minutes 43 seconds | 245.62 GB | OUT_OF_MEM |
| 5 | TeslaA100_SXM4_40GB | 4 | 32 | 256 | ERR1726424_wgs (33+38 GB) | 41 minutes 34 seconds | 248.70 GB | OUT_OF_MEM |
| 6 | TeslaA100_SXM4_40GB | 2 | 24 | 256 | ERR1726424_wgs (33+38 GB) | ??? | ??? | OUT_OF_MEM |

## TEST - Teala A100 v3.5.0.1 (2nd RUN, Add MORE MEM)

> Output dir on SCRATCH1

| Test Run #  | gModel | GPU | CPU | MEM GB | Sample | Time_MAX | MEM_Max | Note |
| ----------- | ------ | --- | --- | ------ | ------ |  ------- | ------- | ---- |
| 1 | TeslaA100_SXM4_40GB | 4 | 32 | 480 | NA12878_300X  (367+393 GB) | ??? | ??? | PENDING too long |
| 2 | TeslaA100_SXM4_40GB | 2 | 24 | 480 | NA12878_300X  (367+393 GB) | ??? | ??? | PENDING too long |
| 3 | TeslaA100_SXM4_40GB | 4 | 32 | 360 | NA12878_downsampling (32+35 GB) | - | - | Not enough free memory for these GPUs. |
| 4 | TeslaA100_SXM4_40GB | 2 | 24 | 360 | NA12878_downsampling (32+35 GB) | 63 minutes 28 seconds | 263.27 GB | SUCCESSED |
| 5 | TeslaA100_SXM4_40GB | 4 | 32 | 360 | ERR1726424_wgs (33+38 GB) | - | - | Not enough free memory for these GPUs. |
| 6 | TeslaA100_SXM4_40GB | 2 | 24 | 360 | ERR1726424_wgs (33+38 GB) | 92 minutes 55 seconds | 343.93 GB | SUCCESSED |
| 7 | TeslaA100_SXM4_40GB | 2 | 24 | 300 | Neuropathy 10001 (27+28 GB) | 59 minutes 55 seconds | 298.19 GB | OUT_OF_MEM |
| 8 | TeslaA100_SXM4_40GB | 2 | 24 | 300 | Neuropathy 10001 (28+30 GB) | 68 minutes 55 seconds | 282.26 GB | OUT_OF_MEM |
| 9 | TeslaA100_SXM4_40GB | 2 | 24 | 300 | Neuropathy 10001 (24+26 GB) | 55 minutes 17 seconds | 275.65 GB | SUCCESSED |
