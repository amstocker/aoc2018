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

def process_line(line):
    parts = line.split()
    return Arrow(parts[1], parts[7])

def make_dag(arrows):
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

def get_ready(nodes):
    return sorted([n for n in nodes.values() if len(n.prev) == 0], key=lambda n: n.label)

def consume_ready_task(nodes):
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
