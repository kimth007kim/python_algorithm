from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

n,l,r=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs(x,y,index):
    tmp = []
    tmp.append((x,y))
    union[x][y]=index
    q=deque()
    summary=graph[x][y]
    q.append((x,y))
    cnt=1
    while q:
        print(q)
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx>=0 and ny>=0 and nx<n and ny<n and union[nx][ny]==-1:
                if l<=abs(graph[nx][ny]-graph[x][y])<= r:
                    q.append((nx,ny))
                    tmp.append((x,y))
                    summary+=graph[nx][ny]
                    union[nx][ny]=index
                    cnt+=1


    for x,y in tmp:
        graph[x][y]= summary//cnt


total_count=0
while True:
    index=0
    union= [[-1]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                bfs(i,j,index)
                print(union)
                index+=1
    if index == n*n:
        break
    total_count+=1

print(total_count)