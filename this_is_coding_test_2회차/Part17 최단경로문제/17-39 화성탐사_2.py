import heapq

INF= int(1e9)
answer=[]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for _ in range(int(input())):
    n= int(input())
    graph=[]
    for i in range(n):
        graph.append(list(map(int,input().split())))

    distance=[[INF]*n for _ in range(n)]

    q=[]
    heapq.heappush(q,(graph[0][0],0,0))
    distance[0][0]=graph[0][0]

    while q:
        cost,x,y=heapq.heappop(q)
        for i in range(4):
            nx= dx[i]+x
            ny= dy[i]+y
            if nx>=0 and ny>=0 and nx<n and ny<n:
                if distance[nx][ny]> graph[nx][ny]+distance[x][y]:
                    distance[nx][ny]= graph[nx][ny]+distance[x][y]
                    q.append((distance[nx][ny],nx,ny))

    answer.append(distance[n-1][n-1])

for k in answer:
    print(k)