import math
from collections import defaultdict


EQUIDISTANT = "EQUIDISTANT"

def mdist(p1, p2):
    return math.fabs(p2[0]-p1[0]) + math.fabs(p2[1]-p1[1])

def get_min(c, points):
    dists = sorted(enumerate(map(lambda p: int(mdist(p, c)), points)),
                   key=lambda t: t[1])
    if dists[0][1] == dists[1][1]:
        return EQUIDISTANT, dists[0][1]
    return points[dists[0][0]], dists[0][1]

def get_boundary(points):
    xr = sorted(points, key=lambda p: p[0])
    yr = sorted(points, key=lambda p: p[1])
    return xr[0][0], xr[-1][0], yr[0][1], yr[-1][1]

def iter_boundary(b):
    return [(x, b[2]) for x in range(b[0], b[1]+1)] + \
           [(x, b[3]) for x in range(b[0], b[1]+1)] + \
           [(b[0], y) for y in range(b[2]+1, b[3])] + \
           [(b[1], y) for y in range(b[2]+1, b[3])]

def iter_interior(b):
    for y in range(b[2]+1, b[3]):
        for x in range(b[0]+1, b[1]):
            yield x, y

def finite_points(points, b):
    # Idea is that on the bounding square any point that is
    # the minimal distance will also be the minimal distance
    # for an infinity of points away from the bounding square.
    infinites = set(get_min(c, points)[0] for c in iter_boundary(b))
    return set(p for p in points if p not in infinites)


with open("day6_input.txt") as f:
    points = [tuple(map(int, l.split(','))) for l in f.read().rstrip().split('\n')]
    boundary = get_boundary(points)

    # part 1
    areas = defaultdict(int)
    finites = finite_points(points, boundary)
    for x, y in iter_interior(boundary):
        closest = get_min((x, y), points)[0]
        if closest in finites and \
           closest != EQUIDISTANT:
            areas[closest] += 1
    print(sorted(areas.items(), key=lambda t: t[1])[-1][1])

    # part 2
    area = 0
    assert(10000//len(points) < \
            min(boundary[1]-boundary[0], boundary[3]-boundary[2]))
    for x, y in iter_interior(boundary):
        if sum(mdist((x, y), p) for p in points) < 10000:
            area += 1
    print(area)
