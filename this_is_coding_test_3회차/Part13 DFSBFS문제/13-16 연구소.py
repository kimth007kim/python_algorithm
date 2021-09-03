from itertools import combinations
from collections import deque
import sys

input= sys.stdin.readline

def calc(cgraph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if cgraph[i][j]==0:
                cnt+=1
    return cnt

def spread(graph,virus):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    cgraph=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cgraph[i][j]=graph[i][j]
    q=deque(virus)

    while q:
        x,y =q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and cgraph[nx][ny]==0:
                cgraph[nx][ny]=2
                q.append((nx,ny))

    return calc(cgraph)

n,m=map(int,input().split())
graph=[]

virus=[]
space=[]
answer=[]

for i in range(n):
    tmp=list(map(int,input().split()))
    graph.append(tmp)
    for j in range(len(tmp)):
        if tmp[j]==0:
            space.append((i,j))
        elif tmp[j]==2:
            virus.append((i,j))

comb = combinations(space,3)
for i in list(comb):
    for x,y in i:
        graph[x][y]=1

    answer.append(spread(graph,virus))

    for x,y in i:
        graph[x][y]=0

print(max(answer))