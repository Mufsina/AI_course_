class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.heuristic = 0
        self.solution = False

def ao_star(node):
    print(f"Expanding {node.name}")
    if not node.children:
        node.solution = True
        return node.heuristic
    min_cost = float('inf')
    best = None
    for child_group in node.children:
        cost = sum(c.heuristic for c in child_group)
        if cost < min_cost:
            min_cost = cost
            best = child_group
    for c in best:
        c.heuristic = ao_star(c)
    node.heuristic = min_cost
    node.solution = True
    return node.heuristic
