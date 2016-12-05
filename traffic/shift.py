# Shift Traffic Pattern
#   Input Fields:
#     start      = first rank
#     end        = last rank
#     iterations = number of communications from each rank
#     shift      = number of indicies to shift by

# shift right with wrap around
def right(src, shift, start, end):
    dst = src + (shift % (end - start + 1))
    if dst > end:
        dst -= end - start
    return dst

# the function called by parse_line
def shift_right(job):
    traffic = {}
    for src in xrange(job['start'], job['end'] + 1):
        traffic[src] = [right(src, job['shift'], job['start'], job['end'])] * job['iterations']
    return traffic

# shift left with wrap around
def left(src, shift, start, end):
    dst = src - (shift % (end - start + 1))
    if dst < start:
        dst = end - start + dst + 1
    return dst

# the function called by parse_line
def shift_left(job):
    traffic = {}
    for src in xrange(job['start'], job['end'] + 1):
        traffic[src] = [left(src, job['shift'], job['start'], job['end'])] * job['iterations']
    return traffic
