from collections import deque

def bfs():
    q=deque()
    day = -1
    for j in tomato:
        q.append(j)
    while q:
        print(q)
        day+=1
        for _ in range(len(q)):
            x, y = q.popleft()
            print("자른 x,y",x,y)
            for j in graph:
                print(j)
            print()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                print(nx,ny)
                print("day",day)
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if graph[nx][ny]==-1:
                    continue
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    for j in graph:
                        print(j)
                    print()
                    q.append((nx,ny))
    for b in graph:
        if 0 in b:
            return -1
    return day
graph=[]
m,n=map(int,input().split())
for i in range(n):
    graph.append(list(map(int,input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
tomato=[]

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            tomato.append((i,j))


print(bfs())