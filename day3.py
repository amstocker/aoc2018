def rect(s):
    t = s.split()
    t0 = int(t[0][1:])
    t1 = t[2][:-1].split(',')
    t2 = t[3].split('x')
    ret = (t0, int(t1[0]), int(t1[1]), int(t2[0]), int(t2[1]))
    return ret

def add_rect(g, r, i):
    x0 = r[1]
    y0 = r[2]
    dx = r[3]
    dy = r[4]
    for x in range(x0, x0 + dx):
        for y in range(y0, y0 + dy):
            if (x,y) in g:
                g[(x,y)].append(i)
            else:
                g[(x,y)] = [i]


with open("day3_input.txt") as f:
    lines = f.read().rstrip().split('\n')
    rects = map(rect, lines)
    grid = {}
    for i in range(len(rects)):
        add_rect(grid, rects[i], i)

    # part 1
    print(sum(len(grid[t]) > 1 for t in grid))

    # part 2
    overlaps = [False for i in range(len(rects))]
    for t in grid:
        a = grid[t]
        if len(a) > 1:
            for i in a:
                overlaps[i] = True
    print(overlaps.index(min(overlaps))+1)
