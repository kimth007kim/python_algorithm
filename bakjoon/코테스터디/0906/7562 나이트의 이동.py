# https://www.acmicpc.net/problem/7562

import sys
input =sys.stdin.readline

from collections import deque

dx=[-1,-2,-1,-2,1,2,1,2]
dy=[2,1,-2,-1,-2,-1,2,1]


def knight(sx,sy,ex, ey, n):
    if sx==ex and sy==ey:
        return 0
    q=deque([(sx,sy,0)])
    visited=[[False]*(n) for _ in range(n)]
    visited[sx][sy]=True
    while q:
        # print(q)
        x,y,cnt= q.popleft()
        if x==ex and y==ey:
            # print(x,y)
            return cnt
        for i in range(8):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx,ny,cnt+1))

t=int(input())
answer=[]
for i in range(t):
    n= int(input())
    sx,sy=map(int,input().split())
    ex,ey=map(int,input().split())
    answer.append(knight(sx,sy,ex, ey, n))

for i in answer:
    print(i)