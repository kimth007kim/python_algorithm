from collections import deque
import sys
input=sys.stdin.readline

m,n,h=map(int,input().split())
graph=[]
isnt=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
ax=[n,-n]
ay=[0,0]

tomato=[]

for i in range(n*h):
    tmp=list(map(int,input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j]==1:
            tomato.append((i,j))
    if 0 not in tmp:
        isnt+=1


if isnt==n*2:
    print(0)


else:
    find=False
    q=deque()
    for x,y in tomato:
        q.append((x,y,0))
    while q:
        x,y,cnt=q.popleft()
        for i in range(4):
            nx= dx[i]+x
            ny= dy[i]+y
            if nx>=0 and ny>=0 and nx<n*h and ny<m and (nx)//n == (x)//n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    q.append((nx,ny,cnt+1))
        for j in range(2):
            nx= ax[j]+x
            ny= ay[j]+y
            if nx>=0 and nx<n*h:
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    q.append((nx,ny,cnt+1))
    for i in range(n*h):
        if 0 in graph[i]:
            find = True
    if find==True:
        print(-1)
    else:
        print(cnt)
