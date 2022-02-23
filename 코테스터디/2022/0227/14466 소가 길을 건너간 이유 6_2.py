# https://ryu-e.tistory.com/36

import sys
from collections import deque

dx = [0,1,0,-1]
dy= [ 1,0,-1,0]

def bfs(r1,c1):
    dq= deque()
    dq.append((r1,c1))
    cow_visit[r1][c1]=True
    while dq:
        x,y = dq.popleft()
        for d in range(4):
            nx= dx[d]+x
            ny = dy[d]+y

            if nx<0 or ny <0 or nx>=n or ny>=n:
                continue
            if cow_visit[nx][ny]:
                continue
            if (nx,ny) in road[x][y]:
                continue
            dq.append((nx,ny))
            cow_visit[nx][ny]=True


n,k,r = map(int,sys.stdin.readline().split())

road = [ [[] for _ in range(n)] for _ in range(n)]
cow_visit = [[False]*n for _ in  range(n)]
count =0

for _ in range(r):
    r1,c1,r2,c2 = map(int,sys.stdin.readline().split())
    road[r1-1][c1-1].append((r2-1,c2-1))
    road[r2-1][c2-1].append((r1-1,c1-1))

cow_list=list()
for _ in range(k):
    a,b =map(int,sys.stdin.readline().split())
    cow_list.append((a-1,b-1))

for i,cow in enumerate(cow_list):
    cow_visit=[[False] * n for _ in range(n)]
    bfs(cow[0],cow[1])
    for r2,c2 in cow_list[i+1:]:
        if not cow_visit[r2][c2]:
            count+=1
print(count)