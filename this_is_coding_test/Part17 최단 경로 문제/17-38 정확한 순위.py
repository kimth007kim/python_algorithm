INF=int(1e9)

n,m= map(int,input().split())

graph=[[INF]*(n+1) for i in range(n+1)]
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0


for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1


for i in range(1,n+1):
    if i==1:
        if graph[i][n]==1 and graph[i][i+1]==1:
            cnt+=1

    elif i == n:
        if graph[i][i-1]==1 and graph[i][1]==1:
            cnt += 1
    else:
        if graph[i][i-1]==1 and graph[i][i+1]==1:
            cnt += 1


print(cnt)

for a in graph:
    print(a)