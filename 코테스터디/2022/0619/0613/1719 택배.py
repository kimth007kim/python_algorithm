n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
distance = [[j for j in range(n+1)] for i in range(n+1)]

for i in range(m):
    a, b, d = map(int, input().split())
    graph[a][b] = d
    graph[b][a] = d

for i in range(1,n+1):
    distance[i][i]=0
    graph[i][i]=0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            tmp = graph[a][k]+graph[k][b]
            if graph[a][b]>tmp:
                distance[a][b]=distance[a][k]
                graph[a][b]=tmp

for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j]==0:
            print("-",end=" ")
        else:
            print(distance[i][j],end=" ")
    print()