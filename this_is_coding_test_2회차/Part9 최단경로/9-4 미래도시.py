INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0


x,k=map(int,input().split())

for t in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][t]+graph[t][b],graph[a][b])

graph[1][x]= graph[1][k]+graph[k][x]
print(graph[1][x])

for i in graph:
    print(i)