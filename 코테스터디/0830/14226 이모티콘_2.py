from collections import deque

#1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
#2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
#3. 화면에 있는 이모티콘 중 하나를 삭제한다.

n= int(input())
data= [[-1]*(n+1) for _ in range(n+1)]

def bfs():
    q= deque([(1,0)])
    data[1][0]=0
    while q:
        x,y = q.popleft()
        if data[x][x]==-1:
            data[x][x]=data[x][y]+1
            q.append((x,x))
        if x+y<=n and data[x+y][y]==-1:
            data[x+y][y]=data[x][y]+1
            q.append([x+y,y])
        if x-1>=0 and data[x-1][y]==-1:
            data[x-1][y]=data[x][y]+1
            q.append([x-1,y])
        for i in data:
            print(i)
        print()
bfs()
print(data)
r=data[n][1]
for i in range(1,n):
    if data[n][i]!= -1:
        r=min(r,data[n][i])
        print(r)
print(r)