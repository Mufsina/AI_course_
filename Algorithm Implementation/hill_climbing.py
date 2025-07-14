def hill_climbing(start, goal, graph, h):
    current = start
    path = [current]
    while current != goal:
        neighbors = graph[current]
        if not neighbors:
            return None
        next_node = min(neighbors, key=lambda x: h[x])
        if h[next_node] >= h[current]:
            return None
        current = next_node
        path.append(current)
    return path
