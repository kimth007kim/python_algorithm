from collections import deque


dx= [1,0,-1,0]
dy=[0,1,0,-1]

def checker(graph):
    for x in range(n):
        for y in range(m):
            if x==0 or y==0 or x==n-1 or y==m-1:
                if graph[x][y]=="J":
                    return True
    return False


def bfs():
    q=deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j]=="J":
                q.append((i,j,"J",0))
                jvisited[i][j]=True
            elif graph[i][j]=="F":
                q.append((i,j,"F",0))
                fvisited[i][j] = True

    previous=1
    while q:
        print("전",q)
        # for i in graph:
        #     print(i)
        x,y,team,time= q.popleft()
        if previous!=time:
            if checker(graph):
                return time+1
            else:
                previous=time
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==".":
                    if team=="F" and not fvisited[nx][ny]:
                        graph[nx][ny]="F"
                        fvisited[nx][ny]=True
                        q.append((nx,ny,team,time+1))
                    elif team=="J" and not jvisited[nx][ny]:
                        graph[nx][ny]="J"
                        jvisited[nx][ny]=True
                        q.append((nx,ny,team,time+1))
                elif graph[nx][ny]=="J" and team=="F":
                    graph[nx][ny] = "F"
                    fvisited[nx][ny] = True
                    q.append((nx, ny, team, time + 1))

    return -1






n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(input()))


fvisited=[[False]*m for _ in range(n)]
jvisited=[[False]*m for _ in range(n)]


a=bfs()
if a==-1:
    print("IMPOSSIBLE")
else:
    print(a)