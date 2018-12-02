with open("day2_input.txt") as f:
    l = f.read().split()

    print(
        (lambda l: sum([int(t[0]) for t in l]) * sum([int(t[1]) for t in l]))(
            (lambda count, check, i1, i2: [(check(i1, d), check(i2, d)) for d in map(count, l)])(
                lambda w: (lambda d, w: [d.update({c: d.get(c,0)+1}) for c in w] and d)({}, w),
                lambda i, d: any(d[c] == i for c in d),
                2,
                3
            )
        )
    )
