from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline


def bfs(start,end,road):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    sx,sy= start//n,start%n
    ex,ey= end//n,end%n
    visited=[[False] * n for _ in range(n)]
    visited[sx][sy]=True
    q=deque([[sx,sy]])
    while q:
        x,y= q.popleft()
        if x == ex and y==ey:
            return True
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0<=nx <n and 0<=ny<n:
                if visited[nx][ny]==False:
                    if [x,y,nx,ny] not in road:
                        visited[nx][ny]=True
                        q.append([nx,ny])
    return False

n,k,r = map(int,input().split())
road=[]
cow=[[0]*n for _ in range(n)]
graph=[[0]*n for _ in range(n)]
cand=[]
c=1


for i in range(n):
    for j in range(n):
        graph[i][j]=c
        c+=1


for i in range(r):
    r1,c1,r2,c2= map(int,input().split())
    road.append([r1-1,c1-1,r2-1,c2-1])
    road.append([r2-1,c2-1,r1-1,c1-1])


for i in range(k):
    r,c= map(int,input().split())
    cand.append((r-1)*n+c-1)
    cow[r-1][c-1] = 1

comb = list(combinations(cand,2))

answer = len(comb)
for start,end in (comb):
    if bfs(start,end,road)==True:
        answer-=1

print(answer)