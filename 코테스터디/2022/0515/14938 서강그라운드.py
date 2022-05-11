import sys

input = sys.stdin.readline

n,m,r = map(int,input().split())
# n 지역의 개수
# m 수색범위
# r 길의 개수
INF=int(1e9)
items=[0]
items +=list(map(int,input().split()))
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0

for i in range(r):
    a,b,l = map(int,input().split())
    graph[a][b]=l
    graph[b][a]=l

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])

MAX=0
for i in range(1,n+1):
    tmp=0
    for j in range(1,n+1):
        distance=graph[i][j]
        if distance<=m:
            tmp+=items[j]

    MAX=max(tmp,MAX)

print(MAX)