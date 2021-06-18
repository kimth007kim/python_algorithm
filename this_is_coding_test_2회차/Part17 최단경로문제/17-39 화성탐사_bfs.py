from collections import deque
INF=int(1e9)

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n=int(input())
distance=[[INF]*(n) for _ in range(n)]
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

q=deque()
q.append((graph[0][0],0,0))
while q:
    cost,x,y=q.popleft()
    if cost< distance[x][y]:
        distance[x][y]=cost
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and ny>=0 and nx<n and ny<n:
            if graph[nx][ny]+cost< distance[nx][ny]:
                distance[nx][ny]= graph[nx][ny]+cost
                print(distance[nx][ny])
                print(distance)
                q.append((distance[nx][ny],nx,ny))

print(distance)