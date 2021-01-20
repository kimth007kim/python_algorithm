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
    q= deque()
    q.append((x,y))
    graph[x][y] = 0
    cnt=1
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                cnt+=1
                q.append((nx,ny))
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            ans.append(bfs(i,j))

print(len(ans))
ans.sort()
for i in ans:
    print(i)