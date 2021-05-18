from collections import deque
n,k= map(int,input().split())
graph=[]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

for i in range(n):
    graph.append(list(map(int,input().split())))

Es,Ex ,Ey=map(int,input().split())


virus=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            virus.append((graph[i][j],0,i,j))

virus.sort()
q=deque(virus)
while q:
    v,s,x,y=q.popleft()
    if s == Es:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=v
                q.append((v,s+1,nx,ny))
                print(graph)
                print(q)

for j in graph:
    print(j)

print(graph[Ex-1][Ey-1])