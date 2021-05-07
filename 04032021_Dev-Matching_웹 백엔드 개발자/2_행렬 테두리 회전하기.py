import copy


def solution(rows, columns, queries):
    array = [[0] * columns for i in range(rows)]
    answer = []
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            array[i][j] = cnt
            cnt += 1
            # print(queries[0])
    for i in range(len(queries)):
        array = cycle(array, queries[i], answer)
    return answer


def cycle(array, queries, answer):
    x1, y1, x2, y2 = queries
    graph = [[0] * (y2 - y1 + 1) for i in range(x2 - x1 + 1)]
    for i in range(x2 - x1 + 1):
        for j in range(y2 - y1 + 1):
            # print(graph[i][j])
            graph[i][j] = array[i + x1 - 1][j + y1 - 1]
    print(x2 - x1, y2 - y1)
    copygraph = copy.deepcopy(graph)
    minNum = 10001

    for i in range(x2 - x1 + 1):
        for j in range(y2 - y1 + 1):
            if i != x2 - x1 and j == 0:
                graph[i][j] = copygraph[i + 1][j]
                if graph[i][j] < minNum:
                    minNum = graph[i][j]
            if i == 0 and j != 0:
                graph[i][j] = copygraph[i][j - 1]
                if graph[i][j] < minNum:
                    minNum = graph[i][j]
            if i != 0 and j == y2 - y1:
                graph[i][j] = copygraph[i - 1][j]
                if graph[i][j] < minNum:
                    minNum = graph[i][j]
            if i == x2 - x1 and j != y2 - y1:
                graph[i][j] = copygraph[i][j + 1]
                if graph[i][j] < minNum:
                    minNum = graph[i][j]

    answer.append(minNum)
    for i in range(x2 - x1 + 1):
        for j in range(y2 - y1 + 1):
            array[i + x1 - 1][j + y1 - 1] = graph[i][j]
    return array