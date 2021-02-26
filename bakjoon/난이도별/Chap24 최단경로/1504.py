INF=801
n,e = map(int,input().split())
graph=[[INF]*(n+1) for i in range(n+1)]

for _ in range(e):
    a,b,c= map(int,input().split())
    graph[a][b]=c
    graph[b][a]=c

po1,po2= map(int,input().split())

for a in range(1,n+1):
    for b in range(1,n+1):
        if a ==b:
            graph[a][b]=0



for k in range(1,n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])


dd=graph[1][po1]+graph[po1][po2]+graph[po2][n]

if dd>=INF:
    print(-1)
else:
    print(dd)