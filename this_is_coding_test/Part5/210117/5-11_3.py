from collections import deque
graph=[]
n,m= map(int,input().split())
for _ in range(n):
    graph.append(list(map(int,input())))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]


def bfs(x,y):
    q= deque()
    q.append((x,y))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]

            if nx<0 or ny <0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
                print(nx,ny)
                for j in graph:
                    print(j)
    return graph[n-1][m-1]

print(bfs(0,0))