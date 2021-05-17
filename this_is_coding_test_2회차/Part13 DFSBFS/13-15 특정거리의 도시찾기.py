INF=int(1e9)
n,m,k,x=map(int,input().split())
# k는 최단거리
# x는 출발도시
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1, n + 1):
        if a==b:
            graph[a][b]=0

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1


for t in range(1,n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # print(a,k,"  ",k,b)
            graph[a][b]=min(graph[a][b],graph[a][t]+graph[t][b])

answer=[]

for i in range(1,n+1):
    if graph[x][i]==k:
        answer.append(i)
if len(answer)==0:
    print(-1)
else:
    for i in answer:
        print(i)
