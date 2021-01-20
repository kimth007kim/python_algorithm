from collections import deque
ans=[]
dy=[0,0,-1,1]
dx=[-1,1,0,0]

def dfs(x,y):
    q=deque()
    q.append((x,y))


t= int(input())
for _ in range(t):
    m,n,v= map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    for i in range(v):
        x,y= map(int,input().split())
        graph[y][x]=1

for i in range(n):
    for j in range(m):
        if