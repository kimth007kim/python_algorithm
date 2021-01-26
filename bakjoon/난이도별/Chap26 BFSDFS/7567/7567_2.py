from collections import deque

def bfs():
    cnt=-1
    q=deque()
    for i in tomato:
        q.append(i)
    while q:
        cnt+=1
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx= x+dx[i]
                ny= y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    q.append((nx,ny))
    for b in graph:
        if 0 in b:
            return -1
    return cnt






graph=[]
m,n=map(int,input().split())
for _ in range(n):
    graph.append(list(map(int,input().split())))
tomato=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            tomato.append((i,j))

print(bfs())