from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n,k= map(int,input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))
es,ex,ey = map(int, input().split())

answer=[]
answer.sort()

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            answer.append((graph[i][j],i,j,0))

q=deque(answer)
while q:
    v,x,y,s= q.popleft()
    if s== es:
        break
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=v
                q.append((v,nx,ny,s+1,))


print(graph[ex-1][ey-1])