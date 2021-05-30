from collections import deque


dx=[0,1,0,-1]
dy=[1,0,-1,0]
n,k=map(int,input().split())        #n개의 행 1~k개의 바이러스
graph=[]
virus=[]
for i in range(n):
    temp=list(map(int,input().split()))
    for j in range(n):
        if temp[j]!=0:
            virus.append((temp[j],0,i,j))
    graph.append(temp)

virus.sort()
Es,Ex,Ey=map(int,input().split())

q=deque(virus)
while q:
    print(q)
    v,cnt,x,y=q.popleft()
    if cnt==Es:
        break
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and ny>=0 and nx<n and ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=v
                q.append((v,cnt+1,nx,ny))
    for k in graph:
        print(k)
    print()

print(graph)
print(graph[Ex-1][Ey-1])