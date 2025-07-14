import heapq

def a_star(start, goal, graph, h):
    open_set = [(h[start], 0, start, [])]
    visited = set()

    while open_set:
        f, g, node, path = heapq.heappop(open_set)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(open_set, (g + cost + h[neighbor], g + cost, neighbor, path))
    return None
