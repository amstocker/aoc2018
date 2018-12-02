def count(word):
    d = {}
    for c in word:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    two = 0
    three = 0
    for c in word:
        if d[c] == 2:
            two = 1
        if d[c] == 3:
            three = 1
    return (two, three)


def diff(w1, w2):
    diffs = []
    i = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            diffs.append((c1, c2))
        i += 1
    return diffs

with open("day2_input.txt") as f:
    l = f.read().split()
    twos = 0
    threes = 0
    
    # part 1
    for w in l:
        t = count(w)
        twos += t[0]
        threes += t[1]
    print(twos*threes)

    # part 2
    for w1 in l:
        for w2 in l:
            d = diff(w1, w2)
            if len(d) == 1:
                print(w1, w2, d)
