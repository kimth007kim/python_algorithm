# n개의 도시
# 양방향 도로
n= int(input())
road= []
INF=int(1e9)

graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
MAX=0
SUM=int(1e9)
for i in range(1,n+1):
    tmp_sum=0
    tmp_mx=-1
    for j in range(1,n+1):
        tmp_sum+=graph[i][j]
        tmp_mx=max(graph[i][j],tmp_mx)
    if SUM>tmp_sum:
        SUM=tmp_sum
        MAX=tmp_mx
print(MAX)