# 국경선을 공유하는 두 나라의 인구 차이가 L명이상, R명 이하라면 두 나라가 공유하는 국경선을 하루동안 연다.
from collections import deque

dx=[0,1]
dy=[1,0]

n,l,r=map(int,input().split())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
block=1


def bfs(x,y,data,cnt):
    q=deque()
    point = []
    temp = []
    point.append((x,y))
    temp.append(data[x][y])
    cnt = 0
    q.append((data[x][y], x, y))
    while q:
        print(q)
        now,x,y = q.popleft()
        # if previous==now:
        #     print("같음")
        # else:
        #     previous=now
        #     print(temp)

        for i in range(2):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx>=0 and ny>=0 and nx<n and ny<n:
                if abs(data[nx][ny]-data[x][y])>=l and abs(data[nx][ny]-data[x][y])<=r:
                    if (data[nx][ny]+1,nx,ny) in q:
                        continue
                    q.append((data[nx][ny],nx,ny))
                    temp.append(data[nx][ny])
                    point.append((nx,ny))
    for x,y in point:
        data[x][y]=sum(temp)//len(temp)
    if len(temp)<1:
        return cnt
    else:
       bfs(0,0,data,cnt+1)
bfs(0,0,data,0)

print(data)