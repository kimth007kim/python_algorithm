from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]
n,l,r=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs(x,y):
    summary=0
    summary+=graph[x][y]
    count=0
    tmp=[]
    tmp.append((x,y))
    q=deque()
    q.append((x,y))
    while q:
        # print(q)
        x,y=q.popleft()
        point=graph[x][y]
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if nx>=0 and ny >= 0 and nx<n and ny<n and (nx,ny) not in tmp:
                if abs(point-graph[nx][ny]) >= l and abs(point-graph[nx][ny])<= r:

                    summary+=graph[nx][ny]
                    count+=1
                    q.append((nx,ny))
                    tmp.append((nx,ny))
    for x,y in tmp:
        graph[x][y]= summary//count

    print(graph)

union=[[-1]*(n) for i in range(n)]
for i in range(n):
    for j in range(n):
         bfs(i,j)
         union[i][j]+=1
         break