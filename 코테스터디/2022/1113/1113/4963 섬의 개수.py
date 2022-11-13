from collections import deque
import sys

input =sys.stdin.readline
def bfs(a,b,t):
    global visited,arr,n,m
    dx=[0,1,0,-1,-1,-1,1,1]
    dy=[1,0,-1,0,-1,1,-1,1]
    q=deque()
    q.append([a,b])
    visited[a][b]=True
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx= x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==False and arr[nx][ny]==t:
                    visited[nx][ny]=True
                    q.append([nx,ny])


while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    l,s=0,0
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    visited=[[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j]==False:
                if arr[i][j]==0:
                    bfs(i,j,0)
                    s+=1
                else:
                    bfs(i,j,1)
                    l+=1

    print(l)