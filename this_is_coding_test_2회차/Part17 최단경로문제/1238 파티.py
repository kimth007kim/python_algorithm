import sys

input = sys.stdin.readline
n,m,x=map(int,input().split())      #n명학생 m개도로 x번에서 파티
INF=int(1e9)

graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j]=0

for i in range(m):
    a,b,c= map(int,input().split())
    graph[a][b]=c

for k in range(1,n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

value=0
for i in range(1,n+1):
    tmp = graph[i][x]+graph[x][i]
    value=max(value,tmp)

print(value)