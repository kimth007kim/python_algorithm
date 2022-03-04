from collections import deque

dx= [-1,-2,-2,-1,1,2,2,1]
dy= [-2,-1,1,2,2,1,-1,-2]
d_x= [0,1,-1,0]
d_y=[1,0,0,-1]

def bfs():
    if h ==1 and w==1 and graph[0][0]==1:
        return -1

    INF= int(1e9)
    visited=[[INF]*w for _ in range(h)]
    visited[0][0]=0
    q=deque()
    q.append([0,0,0,k])
    while q:
        x,y, move,cnt= q.popleft()
        for i in range(4):
            n_x = d_x[i]+x
            n_y = d_y[i]+y
            if 0<=n_x<h and 0<=n_y<w:
                if visited[n_x][n_y]>visited[x][y]+1 and graph[n_x][n_y]==0:
                    visited[n_x][n_y]=visited[x][y]+1
                    q.append([n_x,n_y,cnt])
        if cnt>0:
            for i in range(8):
                nx = dx[i]+x
                ny = dy[i]+y
                if 0<=nx<h and 0<=ny<w:
                    if visited[nx][ny]>visited[x][y]+1 and graph[nx][ny]==0:
                        visited[nx][ny]=visited[x][y]+1
                        q.append([nx,ny,cnt-1])
    if visited[h-1][w-1]==INF:
        return -1
    else:
        return visited[h-1][w-1]

k = int(input())
w,h = map(int,input().split())
graph=[]

for i in range(h):
    tmp = list(map(int,input().split()))
    graph.append(tmp)

print(bfs())

