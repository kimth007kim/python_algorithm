n,k= map(int,input().split())
INF = int(1e11)
graph=[[INF]*(n+1) for _ in range(n+1)]


for i in range(1,n+1):
    graph[i][i]=0

for i in range(k):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][b], graph[a][k]+graph[k][b])

# for i in graph:
#     print(i)
answer =True
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]>=7:
            answer = False


if answer == True:
    print("Small World!")
else:
    print("Big World!")