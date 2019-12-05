def twice(lst):
    f = 0
    s = set([f])
    stop = False
    while (not stop):
        for c in lst:
            f += c
            if f in s:
                print(f)
                stop = True
                break
            s.add(f)

with open("day1_input.txt") as f:
    l = map(int, f.read().split())
    print(sum(l))
    twice(l)


print("hello")