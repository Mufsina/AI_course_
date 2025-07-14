def dls(graph, node, goal, limit):
    if node == goal:
        return [node]
    if limit <= 0:
        return None
    for neighbor in graph[node]:
        path = dls(graph, neighbor, goal, limit - 1)
        if path:
            return [node] + path
    return None
