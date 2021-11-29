import sys
from collections import deque
input = sys.stdin.readline

n= int(input())
data= []

for i in range(n):
    tmp=list(map(int,input().split()))
    data.append(tmp)

dx=[0,1]
dy=[1,0]


# n=3
# data=[[1, 1, 10], [1, 5, 1], [2, 2, -1]]
visited=[[False]*n for _ in range(n)]

q=deque([(0,0)])
visited[0][0]=True
while q:
    x,y= q.popleft()
    if x==n-1 and y==n-1:
        break
    value= data[x][y]
    for i in range(2):
        nx=dx[i]*value+x
        ny=dy[i]*value+y
        # print(x,y,"  ",value,"  ",nx,ny)
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                visited[nx][ny]=True
                q.append((nx,ny))

if visited[n-1][n-1]:
    print("HaruHaru")
else:
    print("Hing")
# print(visited)

