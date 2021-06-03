from collections import deque

n= int(input())
graph=[]
max_value=-1

dx=[0,1,0,-1]
dy=[1,0,-1,0]

start=0
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(n):
        start=max(start,tmp[j])
    graph.append(tmp)


def bfs(x,y,target):
    q=deque()
    q.append((x,y))
    ngraph[x][y]=10000
    while q:
        x,y=q.popleft()
        # print("left결과 ",x,y)
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx>=0 and ny>=0 and nx<n and ny<n:
                if ngraph[nx][ny]>target and ngraph[nx][ny]!=10000:
                    ngraph[nx][ny]=10000
                    q.append((nx,ny))

for target in range(start,-1,-1):
    cnt=0
    ngraph=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ngraph[i][j]=graph[i][j]
    for i in range(n):
        for j in range(n):
            if ngraph[i][j]!=10000 and ngraph[i][j]>target:
                    cnt+=1
                    bfs(i,j,target)
    max_value=max(max_value,cnt)
print(max_value)
