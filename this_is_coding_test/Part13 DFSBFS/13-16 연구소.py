from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m= map(int,input().split())
virus=[]
graph=[]
zero=[]

result=0
for i in range(n):
    graph.append(list(map(int,input().split())))



for a in range(n):
    for b in range(m):
        if graph[a][b]==2:
            virus.append((a,b))
        if graph[a][b]==0:
            zero.append((a,b))

def bfs(graph):
    q=deque()
    for i in range(len(virus)):
        q.append(virus[i])
    cnt=0
    _graph=graph
    count=0
    while q:
        count+=1
        x,y= q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx>=n or ny>=m or nx<0 or ny<0:
                continue

            if _graph[nx][ny]==1 or _graph[nx][ny] == 2:
                continue

            if _graph[nx][ny]==0:
                _graph[nx][ny]=2
                q.append((nx,ny))

            print("count",count)
            if count==3:
                break
    for i in range(n):
        for j in range(m):
            if _graph[i][j]==0:
                cnt+=1




    print(_graph)
    print(cnt)
    return cnt


for i in range(len(zero)):
    for j in range(len(zero)):
        for k in range(len(zero)):
            if i==j or j==k or k==i:
                continue
            else:
                ix ,iy = zero[i]
                jx ,jy = zero[j]
                kx ,ky = zero[k]
                graph[ix][iy],graph[jx][jy],graph[kx][ky]=1,1,1
                result=max(result,bfs(graph))
                graph[ix][iy],graph[jx][jy],graph[kx][ky]=0,0,0

print(result)