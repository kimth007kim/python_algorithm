def solution(info, edges):
    global max_sheep
    global global_info
    global global_graph_list

    max_sheep = 1
    graph_list = [[] for _ in range(len(info))]
    visited = [False] * len(info)

    for edge in edges:
        graph_list[edge[0]].append(edge[1])
        graph_list[edge[0]].append(edge[0])

    global_info = info
    global_graph_list = graph_list
    next_node_list = graph_list[0]
    bfs(0, 0, 0, visited, set(next_node_list))

    answer = max_sheep
    return answer


def bfs(node, sheep, wolf, visited, node_set):
    print(node, node_set)
    global max_sheep
    global global_info
    global global_graph_list

    if global_info[node] == 0:
        sheep += 1
        if max_sheep < sheep:
            max_sheep = sheep
    else:
        wolf += 1
        if wolf >= sheep:
            return
    next_visited = visited[:]
    next_visited[node] = True

    for next_node in node_set:
        if (next_visited[next_node] == False):
            next_node_set = node_set.copy() | set(global_graph_list[next_node])
            bfs(next_node, sheep, wolf, next_visited, next_node_set)

