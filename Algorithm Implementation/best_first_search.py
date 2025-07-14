import heapq

def best_first_search(graph, start, goal, h):
    visited = set()
    heap = [(h[start], [start])]
    while heap:
        _, path = heapq.heappop(heap)
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                heapq.heappush(heap, (h[neighbor], path + [neighbor]))
    return None
