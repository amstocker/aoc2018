

class Node:
    def __init__(self, n):
        self.n = n
        self.next = None
        self.prev = None

class Circle:
    def __init__(self):
        self.zero = Node(0)
        self.zero.prev = self.zero
        self.zero.next = self.zero
        self.cur = self.zero

    def insert_cur(self, n):
        cur_prev = self.cur.prev
        cur_next = self.cur
        self.cur = Node(n)
        cur_prev.next = self.cur
        cur_next.prev = self.cur
        self.cur.prev = cur_prev
        self.cur.next = cur_next

    def remove_cur(self):
        tmp = self.cur.n
        cur_prev = self.cur.prev
        cur_next = self.cur.next
        cur_prev.next = cur_next
        cur_next.prev = cur_prev
        del self.cur
        self.cur = cur_next
        return tmp

    def move_forward(self, t=1):
        for i in range(t):
            self.cur = self.cur.next

    def move_back(self, t=1):
        for i in range(t):
            self.cur = self.cur.prev

    def listify(self):
        circle = [self.zero.n]
        cur = self.zero.next
        while cur != self.zero:
            circle.append(cur.n)
            cur = cur.next
        return circle

class Game:
    def __init__(self, players, marbles):
        self.players = players
        self.marbles = marbles

        self.circle = Circle()
        self.scores = [0 for p in range(self.players)]

    def play(self):
        for i in range(1, self.marbles + 1):
            self.update(i)

    def update(self, i):
        if i % 23 == 0:
            p = (i - 1) % self.players
            self.scores[p] += i
            self.circle.move_back(7)
            self.scores[p] += self.circle.remove_cur()
        else:
            self.circle.move_forward(2)
            self.circle.insert_cur(i)


if __name__ == "__main__":

    # part 1
    n_players = 463
    n_marbles = 71787
    g = Game(n_players, n_marbles)
    g.play()
    print("part 1: {}".format(max(g.scores)))

    # part 2
    n_players = 463
    n_marbles = 71787 * 100
    g = Game(n_players, n_marbles)
    g.play()
    print("part 2: {}".format(max(g.scores)))














