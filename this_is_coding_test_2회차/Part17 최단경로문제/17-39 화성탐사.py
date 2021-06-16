import heapq
INF=int(1e9)

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n=int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

distance=[[INF]*n for _ in range(n)]
x,y=0,0
q=[(graph[x][y],x,y)]
distance[x][y]=graph[x][y]

while q:
    dist,x,y = heapq.heappop(q)
    if distance[x][y]<dist:
        continue
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        cost=dist+graph[nx][ny]
        if cost<distance[nx][ny]:
            distance[nx][ny]=cost
            heapq.heappush(q,(cost,nx,ny))
    for k in distance:
        print(k)
    print()

print(distance[n-1][n-1])


print(distance)