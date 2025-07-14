from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    front = {start: [start]}
    back = {goal: [goal]}
    front_q = deque([start])
    back_q = deque([goal])

    while front_q and back_q:
        f_curr = front_q.popleft()
        for neighbor in graph[f_curr]:
            if neighbor not in front:
                front[neighbor] = front[f_curr] + [neighbor]
                front_q.append(neighbor)
                if neighbor in back:
                    return front[neighbor] + back[neighbor][::-1][1:]

        b_curr = back_q.popleft()
        for neighbor in graph[b_curr]:
            if neighbor not in back:
                back[neighbor] = back[b_curr] + [neighbor]
                back_q.append(neighbor)
                if neighbor in front:
                    return front[neighbor] + back[neighbor][::-1][1:]

    return None
