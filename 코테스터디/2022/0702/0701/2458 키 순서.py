import sys

input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]


for i in range(m):
    a,b = map(int,input().split())
    graph[a][b]= 1
    graph[b][a]=-1


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][k]==1 and graph[k][b]==1:
                graph[a][b]=1
            if graph[a][k]==-1 and graph[k][b]==-1:
                graph[a][b]=-1

answer=0
for i in range(1,n+1):
    cnt=0
    for j in range(1,n+1):
        if graph[i][j]==0:
            cnt+=1
    if cnt==1:
        answer+=1


print(answer)