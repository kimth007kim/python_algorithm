from collections import deque

n = int(input())
graph=[]
visited=[[False]*n for _ in range(n)]
new_graph=[]
new_visited=[[False]*n for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(graph,visit,i,j):
    visit[i][j]=True
    check=graph[i][j]
    q=deque()
    q.append([i,j])
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx= dx[i]+x
            ny= dy[i]+y
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==check:
                if visit[nx][ny]==False:
                    visit[nx][ny]=True
                    q.append([nx,ny])

cnt_0=0
cnt_1=0
for _ in range(n):
    arr=list(input())
    tmp=[]
    for i in arr:
        if i =="R" or i =="G":
            tmp.append("R")
        else:
            tmp.append("B")
    graph.append(arr)
    new_graph.append(tmp)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph,visited,i,j)
            cnt_0+=1
        if not new_visited[i][j]:
            bfs(new_graph, new_visited, i, j)
            cnt_1+=1

print(cnt_0,cnt_1)
