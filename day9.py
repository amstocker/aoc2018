n_players = 463
n_marbles = 71787 + 1

scores = [0 for p in range(n_players)]

# cur_marble#: (prev_marble#, next_marble#)
circle = {0: (0, 0)}
get_prev = lambda i: circle[i][0]
get_next = lambda i: circle[i][1]
def insert(kp, k):
    kn = get_next(kp)
    circle[kp] = (get_prev(kp), v)
    circle[kn] = (v, get_next(kn))
    circle[k] = (kp, kn)

cur = 0
for i in range(1, n_marbles):
    if i % 10000 == 0:
        print(i)
    if i % 23 == 0:
        p = (i - 1) % n_players
        scores[p] += i
        new_cur = (cur - 7) % len(circle)
        scores[p] += circle.pop(new_cur)
        cur = new_cur
    else:
        new_cur = (cur + 1) % len(circle) + 1
        circle.insert(new_cur, i)
        cur = new_cur
    #print("{}: {}".format(i, circle))
print(max(scores))
