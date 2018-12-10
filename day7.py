from copy import deepcopy


class Node:
    def __init__(self, label):
        self.label = label
        self.next = set()
        self.prev = set()

    def add_next(self, node):
        self.next.add(node)

    def add_prev(self, node):
        self.prev.add(node)

    def remove_next(self, node):
        self.next.remove(node)

    def remove_prev(self, node):
        self.prev.remove(node)

    def __str__(self):
        return "Node({}, prev={}, next={})".format(self.label, self.prev, self.next)
    
    def __repr__(self):
        return self.label

class Arrow:
    def __init__(self, src_label, trg_label):
        self.src_label = src_label
        self.trg_label = trg_label

class Worker:
    def __init__(self, n):
        self.n = n
        self.time = 0
        self.ready = True
        self.task_label = '.'
        self.on_complete = None

    def begin_task(self, label, on_complete):
        self.time = 60 + (ord(label) - 64)
        self.task_label = label
        self.ready = False
        self.on_complete = on_complete

    def complete(self):
        if self.on_complete:
            self.on_complete(self)
            self.on_complete = None
        self.task_label = '.'
        self.ready = True

    def tick(self):
        if self.time > 0:
            self.time -= 1
            if self.time == 0:
                self.complete()


def process_line(line):
    parts = line.split()
    return Arrow(parts[1], parts[7])

def make_dag(_arrows):
    arrows = deepcopy(_arrows)
    a = arrows.pop(0)
    src = Node(a.src_label)
    trg = Node(a.trg_label)
    nodes = {src.label: src,
             trg.label: trg}
    src.add_next(trg)
    trg.add_prev(src)
    while len(arrows) > 0:
        a = arrows.pop(0)
        if a.src_label in nodes:
            src = nodes[a.src_label]
            if a.trg_label in nodes:
                trg = nodes[a.trg_label]
            else:
                trg = Node(a.trg_label)
                nodes[trg.label] = trg
        elif a.trg_label in nodes:
            trg = nodes[a.trg_label]
            src = Node(a.src_label)
            nodes[src.label] = src
        else:
            arrows.append(a)
            continue
        src.add_next(trg)
        trg.add_prev(src)
    return nodes

def ready_tasks(nodes):
    return [n.label for n in nodes.values() if len(n.prev) == 0]

def get_ready(nodes):
    return sorted([n for n in nodes.values() if len(n.prev) == 0], key=lambda n: n.label)

def consume_ready_task(nodes, label=None):
    if label:
        node = [n for n in get_ready(nodes) if n.label == label][0]
    else:
        node = get_ready(nodes)[0]
    for t in node.next:
        t.remove_prev(node)
    nodes.pop(node.label)
    return node.label


with open("day7_input.txt") as f:
    arrows = list(map(process_line, f.read().rstrip().split('\n')))
    
    # part 1
    nodes = make_dag(arrows)
    completed = []
    while len(nodes) > 0:
        completed.append(consume_ready_task(nodes))
    print(''.join(completed))

    # part 2
    nodes = make_dag(arrows)
    in_progress = set()
    workers = [Worker(i) for i in range(5)]
    def on_complete(w):
        consume_ready_task(nodes, label=w.task_label)
        in_progress.remove(w.task_label)
    
    t = 0
    while len(nodes) > 0 or not all(w.ready for w in workers):
        ready = ready_tasks(nodes)
        for w in workers:
            for label in ready:
                if label not in in_progress and w.ready:
                    in_progress.add(label)
                    w.begin_task(label, on_complete)
        for w in workers:
            w.tick()
        t += 1
    print(t)
