# https://www.hackerrank.com/challenges/counting-valleys
def countingValleys(n, s):
    pos_rel_to_sea_level = 0
    valleys = 0
    steps = list(s)
    for step in steps:
        # store position before step
        pos_before_step = pos_rel_to_sea_level
        if step == 'U':
            pos_rel_to_sea_level += 1
        elif step == 'D':
            pos_rel_to_sea_level -= 1
        # check if stepped from negative num to sea level
        if pos_before_step < 0 and pos_rel_to_sea_level == 0:
            valleys += 1
    return valleys
