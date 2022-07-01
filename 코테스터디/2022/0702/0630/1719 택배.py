n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
distance = [[j for j in range(n+1)] for _ in range(n + 1)]


#
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
            distance[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for i in graph:
    print(i)


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            tmp = graph[a][k] + graph[k][b]
            if graph[a][b] > tmp:
                distance[a][b] = distance[a][k]
                graph[a][b]=tmp
                print("여기")


for i in distance:
    print(i)
