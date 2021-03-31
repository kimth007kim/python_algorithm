from collections import deque

INF= int(1e9)

n,m,k,x =map(int,input().split())

graph= [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=INF

for j in range(m):
    a,b= map(int,input().split())
    graph[a][b]=1


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])

for i in graph:
    print(i)
