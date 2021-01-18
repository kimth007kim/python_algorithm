from collections import deque

n= int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

cnt=0
ans=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global cnt
    q= deque()
    q.append((x,y))
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                cnt+=1
                q.append((nx,ny))
                print(graph)

bfs(0,0)
