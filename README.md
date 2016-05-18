# compass
Convert numeric bearing to cardinal directions of the compass


The function `compass_direction` takes
* `deg` Bearing in degrees
* `num_directions` How many different directions to use (2, 4, 8, 16 or 32)
* `show_dev` True if deviation from direction should be included
* `round_dev` True if the deviation should be rounded to nearest integer

and returns
* A string with a compass direction, e.g. "N", "SSE", "SE -2.5"



Running compass.py prints a table with generated compass directions for
all possible number of directions. First column is bearing, second is N/S,
third is N/S/E/W, fourth adds NW etc, fifth adds NNW etc and sixth uses
all possible 32 directions including EbN etc.

The user is asked for how granular to make the table and if `show_dev` and
`round_dev` should be used.



### Example run 1
```
% python compass.py
Table granularity in degrees (default 1): 15
Show deviation [Y/n]: n
0.0     N       N       N       N       N
15.0    N       N       N       NNE     NbE
30.0    N       N       NE      NNE     NEbN
45.0    N       E       NE      NE      NE
60.0    N       E       NE      ENE     NEbE
75.0    N       E       E       ENE     EbN
90.0    S       E       E       E       E
105.0   S       E       E       ESE     EbS
120.0   S       E       SE      ESE     SEbE
135.0   S       S       SE      SE      SE
150.0   S       S       SE      SSE     SEbS
165.0   S       S       S       SSE     SbE
180.0   S       S       S       S       S
195.0   S       S       S       SSW     SbW
210.0   S       S       SW      SSW     SWbS
225.0   S       W       SW      SW      SW
240.0   S       W       SW      WSW     SWbW
255.0   S       W       W       WSW     WbS
270.0   N       W       W       W       W
285.0   N       W       W       WNW     WbN
300.0   N       W       NW      WNW     NWbW
315.0   N       N       NW      NW      NW
330.0   N       N       NW      NNW     NWbN
345.0   N       N       N       NNW     NbW
```

### Example run 2
```
% python compass.py
Table granularity in degrees (default 1): 30
Show deviation [Y/n]:
Round deviation to integer [y/N]: y
0.0     N +0    N +0    N +0    N +0    N +0
30.0    N +30   N +30   NE -15  NNE +8  NEbN -4
60.0    N +60   E -30   NE +15  ENE -8  NEbE +4
90.0    S -90   E +0    E +0    E +0    E +0
120.0   S -60   E +30   SE -15  ESE +8  SEbE -4
150.0   S -30   S -30   SE +15  SSE -8  SEbS +4
180.0   S +0    S +0    S +0    S +0    S +0
210.0   S +30   S +30   SW -15  SSW +8  SWbS -4
240.0   S +60   W -30   SW +15  WSW -8  SWbW +4
270.0   N -90   W +0    W +0    W +0    W +0
300.0   N -60   W +30   NW -15  WNW +8  NWbW -4
330.0   N -30   N -30   NW +15  NNW -8  NWbN +4
```

### Example run 3
```
% python compass.py
Table granularity in degrees (default 1): 5
Show deviation [Y/n]:
Round deviation to integer [y/N]:
0.0     N +0.0  N +0.0  N +0.0  N +0.0  N +0.0
5.0     N +5.0  N +5.0  N +5.0  N +5.0  N +5.0
10.0    N +10.0 N +10.0 N +10.0 N +10.0 NbE -1.25
15.0    N +15.0 N +15.0 N +15.0 NNE -7.5        NbE +3.75
20.0    N +20.0 N +20.0 N +20.0 NNE -2.5        NNE -2.5
25.0    N +25.0 N +25.0 NE -20.0        NNE +2.5        NNE +2.5
30.0    N +30.0 N +30.0 NE -15.0        NNE +7.5        NEbN -3.75
35.0    N +35.0 N +35.0 NE -10.0        NE -10.0        NEbN +1.25
40.0    N +40.0 N +40.0 NE -5.0 NE -5.0 NE -5.0
45.0    N +45.0 E -45.0 NE +0.0 NE +0.0 NE +0.0
50.0    N +50.0 E -40.0 NE +5.0 NE +5.0 NE +5.0
55.0    N +55.0 E -35.0 NE +10.0        NE +10.0        NEbE -1.25
60.0    N +60.0 E -30.0 NE +15.0        ENE -7.5        NEbE +3.75
65.0    N +65.0 E -25.0 NE +20.0        ENE -2.5        ENE -2.5
70.0    N +70.0 E -20.0 E -20.0 ENE +2.5        ENE +2.5
75.0    N +75.0 E -15.0 E -15.0 ENE +7.5        EbN -3.75
80.0    N +80.0 E -10.0 E -10.0 E -10.0 EbN +1.25
85.0    N +85.0 E -5.0  E -5.0  E -5.0  E -5.0
90.0    S -90.0 E +0.0  E +0.0  E +0.0  E +0.0
95.0    S -85.0 E +5.0  E +5.0  E +5.0  E +5.0
100.0   S -80.0 E +10.0 E +10.0 E +10.0 EbS -1.25
105.0   S -75.0 E +15.0 E +15.0 ESE -7.5        EbS +3.75
110.0   S -70.0 E +20.0 E +20.0 ESE -2.5        ESE -2.5
115.0   S -65.0 E +25.0 SE -20.0        ESE +2.5        ESE +2.5
120.0   S -60.0 E +30.0 SE -15.0        ESE +7.5        SEbE -3.75
125.0   S -55.0 E +35.0 SE -10.0        SE -10.0        SEbE +1.25
130.0   S -50.0 E +40.0 SE -5.0 SE -5.0 SE -5.0
135.0   S -45.0 S -45.0 SE +0.0 SE +0.0 SE +0.0
140.0   S -40.0 S -40.0 SE +5.0 SE +5.0 SE +5.0
145.0   S -35.0 S -35.0 SE +10.0        SE +10.0        SEbS -1.25
150.0   S -30.0 S -30.0 SE +15.0        SSE -7.5        SEbS +3.75
155.0   S -25.0 S -25.0 SE +20.0        SSE -2.5        SSE -2.5
160.0   S -20.0 S -20.0 S -20.0 SSE +2.5        SSE +2.5
165.0   S -15.0 S -15.0 S -15.0 SSE +7.5        SbE -3.75
170.0   S -10.0 S -10.0 S -10.0 S -10.0 SbE +1.25
175.0   S -5.0  S -5.0  S -5.0  S -5.0  S -5.0
180.0   S +0.0  S +0.0  S +0.0  S +0.0  S +0.0
185.0   S +5.0  S +5.0  S +5.0  S +5.0  S +5.0
190.0   S +10.0 S +10.0 S +10.0 S +10.0 SbW -1.25
195.0   S +15.0 S +15.0 S +15.0 SSW -7.5        SbW +3.75
200.0   S +20.0 S +20.0 S +20.0 SSW -2.5        SSW -2.5
205.0   S +25.0 S +25.0 SW -20.0        SSW +2.5        SSW +2.5
210.0   S +30.0 S +30.0 SW -15.0        SSW +7.5        SWbS -3.75
215.0   S +35.0 S +35.0 SW -10.0        SW -10.0        SWbS +1.25
220.0   S +40.0 S +40.0 SW -5.0 SW -5.0 SW -5.0
225.0   S +45.0 W -45.0 SW +0.0 SW +0.0 SW +0.0
230.0   S +50.0 W -40.0 SW +5.0 SW +5.0 SW +5.0
235.0   S +55.0 W -35.0 SW +10.0        SW +10.0        SWbW -1.25
240.0   S +60.0 W -30.0 SW +15.0        WSW -7.5        SWbW +3.75
245.0   S +65.0 W -25.0 SW +20.0        WSW -2.5        WSW -2.5
250.0   S +70.0 W -20.0 W -20.0 WSW +2.5        WSW +2.5
255.0   S +75.0 W -15.0 W -15.0 WSW +7.5        WbS -3.75
260.0   S +80.0 W -10.0 W -10.0 W -10.0 WbS +1.25
265.0   S +85.0 W -5.0  W -5.0  W -5.0  W -5.0
270.0   N -90.0 W +0.0  W +0.0  W +0.0  W +0.0
275.0   N -85.0 W +5.0  W +5.0  W +5.0  W +5.0
280.0   N -80.0 W +10.0 W +10.0 W +10.0 WbN -1.25
285.0   N -75.0 W +15.0 W +15.0 WNW -7.5        WbN +3.75
290.0   N -70.0 W +20.0 W +20.0 WNW -2.5        WNW -2.5
295.0   N -65.0 W +25.0 NW -20.0        WNW +2.5        WNW +2.5
300.0   N -60.0 W +30.0 NW -15.0        WNW +7.5        NWbW -3.75
305.0   N -55.0 W +35.0 NW -10.0        NW -10.0        NWbW +1.25
310.0   N -50.0 W +40.0 NW -5.0 NW -5.0 NW -5.0
315.0   N -45.0 N -45.0 NW +0.0 NW +0.0 NW +0.0
320.0   N -40.0 N -40.0 NW +5.0 NW +5.0 NW +5.0
325.0   N -35.0 N -35.0 NW +10.0        NW +10.0        NWbN -1.25
330.0   N -30.0 N -30.0 NW +15.0        NNW -7.5        NWbN +3.75
335.0   N -25.0 N -25.0 NW +20.0        NNW -2.5        NNW -2.5
340.0   N -20.0 N -20.0 N -20.0 NNW +2.5        NNW +2.5
345.0   N -15.0 N -15.0 N -15.0 NNW +7.5        NbW -3.75
350.0   N -10.0 N -10.0 N -10.0 N -10.0 NbW +1.25
355.0   N -5.0  N -5.0  N -5.0  N -5.0  N -5.0
```
