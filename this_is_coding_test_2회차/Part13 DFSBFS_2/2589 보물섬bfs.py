from collections import deque

n,m = map(int,input().split())
max_value=0
graph=[]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(x,y,cnt):
    global max_value
    q=deque()
    q.append((x,y,cnt))
    visited[x][y]=cnt
    while q:
        # print(q)
        x,y,cnt=q.popleft()
        max_value=max(max_value,cnt)
        for i in range(4):
            nx= dx[i]+x
            ny= dy[i]+y
            if nx>=0 and ny>=0 and nx<n and ny<m and graph[nx][ny]=="L" and visited[nx][ny]==0:
                visited[nx][ny]=cnt
                # if cnt>6:
                #     for j in visited:
                #         print(j)
                #     print()
                q.append((nx,ny,cnt+1))
        # if nx<0 or ny<0 or nx>=n or ny>=m:
        #     continue
        # if graph[nx][ny]=="W":
        #     continue
        # dfs(nx,ny,cnt)


for i in range(n):
    tmp=[]
    word= input()
    for j in range(len(word)):
        tmp.append(word[j])
    graph.append(tmp)

for i in range(n):
    for j in range(m):
        if graph[i][j]=="L":
            visited=[[0]*m for i in range(n)]
            bfs(i,j,1)

print(max_value-1)