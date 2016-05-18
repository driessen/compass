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
