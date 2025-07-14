def beam_search(start, goal, graph, h, beam_width):
    frontier = [(h[start], [start])]
    while frontier:
        new_frontier = []
        for _, path in frontier:
            current = path[-1]
            if current == goal:
                return path
            for neighbor in graph[current]:
                new_path = path + [neighbor]
                new_frontier.append((h[neighbor], new_path))
        frontier = sorted(new_frontier)[:beam_width]
    return None
