# PerfStat

Python program for capturing performance statistics

This is a simple module that can be run from a command line or
inside another python program. 
The program returns the measured times for program execution
and statistics.

# Installation 

Installation is simple, over PyPI. Additional library needed
is pandas

``` console
pip install perfstat
```

# Running

Default configurations for running are set initially for two
performance recording programs (`likwid` and `perf`) for Linux.

If you use one of these two programs you can just supply the 
command for the performance of a program (here as an example is taken the `ls` command). 
The metrics are auto-generated and the files with the results are saved at the given locations.

The most simple case is the default (the command requires sudo, so initially the system will ask 
for credentials):

``` console
user@pc:~/Documents$ python -m perfstat
Run command: 'sudo likwid-perfctr -C 0 -g CLOCK ls'
Run count: 10
Measuring: ['Runtime (RDTSC) [s]', 'Runtime unhalted [s]', 'Clock [MHz]', 'Uncore Clock [MHz]', 'CPI', 'Energy [J]', 'Power [W]']
Separator: '|'
Measurements file: ''
Statistics file: ''
Float format: '%.4e'
[sudo] password for user: 
Done: 100%
        Runtime (RDTSC) [s]  Runtime unhalted [s]  Clock [MHz]  Uncore Clock [MHz]     CPI  Energy [J]  Power [W]
Run ID                                                                                                           
0                    0.0014                0.0002    3562.9367                 0.0  1.4209      0.0219    15.8320
1                    0.0015                0.0002    2999.8756                 0.0  1.3766      0.0425    28.9588
2                    0.0016                0.0002    2600.1929                 0.0  1.3642      0.0240    14.8284
3                    0.0016                0.0002    2801.0958                 0.0  1.5310      0.0625    38.9571
4                    0.0017                0.0002    2299.3991                 0.0  1.3631      0.0339    19.4133
5                    0.0014                0.0002    3199.4962                 0.0  1.4354      0.0240    16.8569
6                    0.0013                0.0002    3995.2261                 0.0  1.5017      0.0587    44.6264
7                    0.0017                0.0002    2399.9842                 0.0  1.4123      0.0219    12.7339
8                    0.0024                0.0002    1701.8149                 0.0  1.4640      0.0479    19.7376
9                    0.0014                0.0002    3670.1753                 0.0  1.7845      0.0601    41.5754
                        Runtime (RDTSC) [s]  Runtime unhalted [s]  Clock [MHz]  Uncore Clock [MHz]       CPI  Energy [J]  Power [W]
Mean                               0.001600                0.0002  2923.019680                 0.0  1.465370    0.039740  25.351980
Std. dev.                          0.000313                0.0000   704.950781                 0.0  0.125495    0.016774  12.167161
Std. error                         0.000099                0.0000   222.925011                 0.0  0.039685    0.005304   3.847594
Conf. inter. 90% (min)             0.001419                0.0002  2514.372960                 0.0  1.392623    0.030016  18.298905
Conf. inter. 90% (max)             0.001781                0.0002  3331.666400                 0.0  1.538117    0.049464  32.405055
Conf. inter. 95% (min)             0.001376                0.0002  2418.728270                 0.0  1.375597    0.027740  16.648117
Conf. inter. 95% (max)             0.001824                0.0002  3427.311090                 0.0  1.555143    0.051740  34.055843
Conf. inter. 99% (min)             0.001279                0.0002  2198.550056                 0.0  1.336401    0.022501  12.847931
Conf. inter. 99% (max)             0.001921                0.0002  3647.489304                 0.0  1.594339    0.056979  37.856029
```

## Flags

There are the following flags that can be supplied from the command line.

- **-c "command to run"** The -c flag sets the command to run the performance metrics on. 
    (Default: `"sudo likwid-perfctr -C 0 -g CLOCK ls"`).

- **-r num_of_runs** This flag sets the number of runs of the above-defined command. Affects 
    the metric's statistics. Run counts up to 30 are treated by the Student's t-distribution, 
    and above 30 are treated as a regular normal distribution (z-statistics). (Default: 10).

- **-m "measure1,measure2,measure3"** Strings defining the measured values. These are keywords that
    define lines that have value. The default values are set for the `likwid-perfctr`, also
    a predefined set exists for the `perf stat` command. 
    (Default: `"Runtime (RDTSC) [s], Runtime unhalted [s], Clock [MHz], Uncore Clock [MHz], CPI, Energy [J], Power [W]"`. For the `perf stat` we have the following value: `"task-clock, context-switches,cpu-migrations, page-faults, cycles, instructions, branches, branch-misses"`.

- **-s "separator"** Separator between measure and values from above. (Default: `"|"`).

- **-fm "measurements_file"** Place where the measurements file will be recorded. (Default: `""` - no  
    file will be made ).

- **-fs "statistics_file"** Place where the statistics file will be recorded. (Default: `""` - no  
    file will be made ).

- **-g "float_format"** Format for the float value when recording files. (Default: `"%.4e"`).

- **-po print_output** Int (bool) that defines if the program will throw some info. (Default: 1)

- **-pc print_cmd_output** Int (bool) that defines if the program will print every stdout from calling the command. (Default: 0).

- **-pv print_csv** Int (bool) that defines if the program will print the measurements and statistics on the standard output. (Default: 1).

## Examples:

1. We want to run the `sudo perf stat ls` 30 times, on a smaller set of metrics than the default, and save the results in files. We don't need to define a separator since it is automatically set when
reading the command.

``` console
user@pc:~/Documents$ python -m perfstat -c "sudo perf stat ls" -r 30 -m "cycles,instructions" -fm "~/Documents/measurements.csv" -fs "~/Documents/stats.csv"
Run command: 'sudo perf stat ls'
Run count: 30
Measuring: ['cycles', 'instructions']
Separator: ' '
Measurements file: '~/Documents/measurements.csv'
Statistics file: '~/Documents/stats.csv'
Float format: '%.4e'
Done: 100%
           cycles  instructions
Run ID                         
0       2297607.0     1557603.0
1       2409217.0     1550675.0
2       2365400.0     1524057.0
3       2400169.0     1557315.0
4       2276937.0     1529382.0
5       2210214.0     1545919.0
6       2479832.0     1544244.0
7       2263966.0     1542431.0
8       2190710.0     1566473.0
9       2330062.0     1563216.0
10      2254009.0     1550485.0
11      2316403.0     1550825.0
12      2290797.0     1556676.0
13      2245716.0     1564225.0
14      1925554.0     1540289.0
15      2223343.0     1552700.0
16      2168010.0     1540918.0
17      2150624.0     1516970.0
18      2157178.0     1552543.0
19      2232088.0     1553093.0
20      2314820.0     1540224.0
21      2153573.0     1555339.0
22      2273797.0     1526145.0
23      2334992.0     1570076.0
24      2259947.0     1550779.0
25      2293618.0     1559691.0
26      2160072.0     1511287.0
27      2360356.0     1547945.0
28      1932100.0     1559604.0
29      2217976.0     1558192.0
                              cycles  instructions
Mean                    2.249636e+06  1.547977e+06
Std. dev.               1.191917e+05  1.442241e+04
Std. error              2.176133e+04  2.633160e+03
Conf. inter. 90% (min)  2.212661e+06  1.543503e+06
Conf. inter. 90% (max)  2.286611e+06  1.552451e+06
Conf. inter. 95% (min)  2.205129e+06  1.542592e+06
Conf. inter. 95% (max)  2.294143e+06  1.553363e+06
Conf. inter. 99% (min)  2.189654e+06  1.540719e+06
Conf. inter. 99% (max)  2.309619e+06  1.555235e+06
```

2. We want to print the results of `sudo likwid-perfctr -C 0 -g CLOCK ls` of 30 runs on screen:

```console
user@pc:~/Documents$ python -m perfstat -r 30
Run command: 'sudo likwid-perfctr -C 0 -g CLOCK ls'
Run count: 30
Measuring: ['Runtime (RDTSC) [s]', 'Runtime unhalted [s]', 'Clock [MHz]', 'Uncore Clock [MHz]', 'CPI', 'Energy [J]', 'Power [W]']
Separator: '|'
Measurements file: ''
Statistics file: ''
Float format: '%.4e'
Done: 100%
        Runtime (RDTSC) [s]  Runtime unhalted [s]  Clock [MHz]  Uncore Clock [MHz]     CPI  Energy [J]  Power [W]
Run ID                                                                                                           
0                    0.0018                0.0002    2226.0468                 0.0  1.3575      0.0349    19.2939
1                    0.0017                0.0002    2500.0245                 0.0  1.3986      0.0365    21.4518
2                    0.0015                0.0002    3581.5944                 0.0  1.4945      0.0455    29.8032
3                    0.0014                0.0002    3695.8744                 0.0  1.4639      0.0620    45.6367
4                    0.0014                0.0002    3994.0263                 0.0  1.8561      0.0469    33.3140
5                    0.0014                0.0002    3998.6654                 0.0  1.7200      0.0428    31.3381
6                    0.0016                0.0002    2800.4410                 0.0  1.5302      0.0183    11.2228
7                    0.0018                0.0002    2200.9816                 0.0  1.3852      0.0361    19.6812
8                    0.0015                0.0002    3001.8282                 0.0  1.3928      0.0435    28.8160
9                    0.0020                0.0002    2100.6110                 0.0  1.5094      0.0496    25.2147
10                   0.0016                0.0003    3888.9705                 0.0  1.0907      0.1007    62.9745
11                   0.0016                0.0002    3987.8630                 0.0  1.9548      0.0450    27.4019
12                   0.0019                0.0003    3848.1241                 0.0  1.7632      0.0914    48.0189
13                   0.0014                0.0002    3985.7676                 0.0  1.5378      0.0959    70.0341
14                   0.0014                0.0002    3900.1340                 0.0  1.6443      0.0457    33.6117
15                   0.0014                0.0002    3995.9067                 0.0  1.4920      0.0273    19.6689
16                   0.0023                0.0002    1900.0740                 0.0  1.1203      0.0399    17.4767
17                   0.0016                0.0002    3011.0410                 0.0  1.6138      0.0610    37.4662
18                   0.0013                0.0002    3987.2934                 0.0  1.5493      0.0955    71.1530
19                   0.0013                0.0002    3998.0156                 0.0  1.5539      0.0461    36.8038
20                   0.0016                0.0002    3998.0918                 0.0  1.9775      0.0359    22.0043
21                   0.0015                0.0002    3100.6407                 0.0  1.4444      0.0491    33.0547
22                   0.0016                0.0004    3933.7056                 0.0  1.9139      0.0477    29.5551
23                   0.0019                0.0002    2399.5110                 0.0  1.6705      0.0358    19.1972
24                   0.0021                0.0002    1833.1479                 0.0  1.3479      0.0303    14.5428
25                   0.0019                0.0002    2200.1844                 0.0  1.5328      0.0358    18.5442
26                   0.0018                0.0002    2300.1520                 0.0  1.4223      0.0354    19.6474
27                   0.0020                0.0002    2099.6418                 0.0  1.5320      0.0303    15.1852
28                   0.0015                0.0002    2899.9655                 0.0  1.4048      0.0470    30.4260
29                   0.0026                0.0007    3800.3073                 0.0  4.0811      0.1438    56.0181
                        Runtime (RDTSC) [s]  Runtime unhalted [s]  Clock [MHz]  Uncore Clock [MHz]       CPI  Energy [J]  Power [W]
Mean                               0.001680              0.000230  3172.287717                 0.0  1.625183    0.051857  31.618570
Std. dev.                          0.000307              0.000099   806.962293                 0.0  0.509394    0.027188  16.089802
Std. error                         0.000056              0.000018   147.330484                 0.0  0.093002    0.004964   2.937582
Conf. inter. 90% (min)             0.001585              0.000199  2921.954510                 0.0  1.467161    0.043422  26.627244
Conf. inter. 90% (max)             0.001775              0.000261  3422.620923                 0.0  1.783206    0.060291  36.609896
Conf. inter. 95% (min)             0.001565              0.000193  2870.963044                 0.0  1.434972    0.041704  25.610539
Conf. inter. 95% (max)             0.001795              0.000267  3473.612389                 0.0  1.815394    0.062009  37.626601
Conf. inter. 99% (min)             0.001526              0.000180  2766.188049                 0.0  1.368833    0.038174  23.521459
Conf. inter. 99% (max)             0.001834              0.000280  3578.387385                 0.0  1.881533    0.065539  39.715681
```
