import math

DIRECTION = \
      ["N", "NbE", "NNE", "NEbN", "NE", "NEbE", "ENE", "EbN",
       "E", "EbS", "ESE", "SEbE", "SE", "SEbS", "SSE", "SbE",
       "S", "SbW", "SSW", "SWbS", "SW", "SWbW", "WSW", "WbS",
       "W", "WbN", "WNW", "NWbW", "NW", "NWbN", "NNW", "NbW"]

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def compass_direction(deg, num_directions, show_dev, round_dev):
    section_size = 360.0/num_directions; # Span of degrees for each used direction
    rot = section_size/2; # Rotate compass by this much to have North section start at 0.
    moddeg = deg + rot if deg + rot < 360 else deg + rot - 360 # Bearing in rotated compass
    secval = moddeg/section_size; # Normalize to [0, num_directions)
    direction_pos = math.floor(secval)*len(DIRECTION)/num_directions; # Find closest position in DIRECTION vector
    direction = DIRECTION[int(direction_pos)]; # This is the closest direction using num_directions different directions
    direction_deg = direction_pos/(len(DIRECTION)/num_directions) * section_size + rot; # Value of closest direction in rotated compass
    dev = moddeg - direction_deg; # Deviation from closest direction

    # Build return string
    if round_dev:
        dev = int(round(dev)) # round to zero decimals

    if not show_dev:
        return direction;
    elif dev >= 0:
        return direction + " +" + str(dev)
    else:
        return direction + " " + str(dev)



if __name__ == "__main__":
    step_reply = raw_input("Table granularity in degrees (default 1): ")
    if step_reply == "":
        step = 1
    else:
        step = float(step_reply)

    show_dev_reply = raw_input("Show deviation [Y/n]: ")
    show_dev = show_dev_reply != "n" and show_dev_reply != "N"

    if show_dev:
        round_dev_reply = raw_input("Round deviation to integer [y/N]: ")
        round_dev = round_dev_reply == "y" or round_dev_reply == "Y"
    else:
        round_dev = False
            
    degs = [x for x in frange(0.0, 360.0, step)]
    dir2 = [compass_direction(deg, 2, show_dev, round_dev) for deg in degs];
    dir4 = [compass_direction(deg, 4, show_dev, round_dev) for deg in degs];
    dir8 = [compass_direction(deg, 8, show_dev, round_dev) for deg in degs];
    dir16 = [compass_direction(deg, 16, show_dev, round_dev) for deg in degs];
    dir32 = [compass_direction(deg, 32, show_dev, round_dev) for deg in degs];

    for (d, d2, d4, d8, d16, d32) in zip(degs, dir2, dir4, dir8, dir16, dir32):
        print str(d) + "\t" + d2 + "\t" + d4 + "\t" + d8 + "\t" + d16 + "\t" + d32

