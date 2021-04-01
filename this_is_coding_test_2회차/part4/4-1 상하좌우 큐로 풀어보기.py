from collections import deque

queue=deque()
x,y=1,1
n=int(input())
plans=input().split()
for i in range(len(plans)):
    queue.append(plans[i])

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move=['L','R','U','D']


while queue:
    dir= queue.popleft()
    for i in range(len(move)):
        if move[i] == dir:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<=0 or nx>n or ny<=0 or ny>n:
        continue
    x,y=nx,ny

print(x,y)