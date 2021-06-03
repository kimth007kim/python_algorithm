from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]
n,l,r=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs(x,y,index):
    tmp=[]
    tmp.append((x,y))
    q=deque()
    q.append((x,y))
    union[x][y]=index
    summary=graph[x][y]
    count=1
    while q:
        x,y=q.popleft()
        point=graph[x][y]
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx>=0 and ny >= 0 and nx<n and ny<n and union[nx][ny]==-1:
                if abs(point-graph[nx][ny]) >= l and abs(point-graph[nx][ny])<= r:

                    q.append((nx,ny))
                    tmp.append((nx,ny))
                    summary+=graph[nx][ny]
                    union[nx][ny]=index
                    count+=1

    print(index,union)
    print(graph)
    print()
    for x,y in tmp:
        graph[x][y]= summary//count

total_count=0
while True:
    union=[[-1]*(n) for i in range(n)]
    index=0
    for i in range(n):
        for j in range(n):
             print(i,j)
             if union[i][j]==-1:
                 bfs(i,j,index)
                 index+=1
    if index == n* n:
        break
    total_count+=1
print(total_count)