n_players = 463
n_marbles = 71787 + 1

scores = [0 for p in range(n_players)]
circle = [0]





cur = 0
for i in range(1, n_marbles):
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
print(max(scores))


class Node:
    def __init__(self, i):
        self.next
        self.prev


class Circle:
    def __init__(self, i):
        self.zero = Node(0)
