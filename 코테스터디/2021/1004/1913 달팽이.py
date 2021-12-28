import sys

input = sys.stdin.readline
def Move(number,direction,x,y,start):
    global tx,ty
    # print(number,direction,x,y,start)
    x += dx[direction]
    y += dy[direction]
    for i in range(number):
        graph[x][y] = start
        if start == target:
            tx=x
            ty=y
        if i != n - 1:
            x += dx[direction]
            y += dy[direction]

        start -= 1

    # showGraph(graph)
    return x,y,start

n= int(input())
target = int(input())
tx=0
ty=0


dx=[0,-1,0,1]
dy=[1,0,-1,0]

start = n*n
graph=[[0]*(n) for _ in range(n)]
x=0
y=0
for i in range(n):
    graph[x][y]=start
    if start == target:
        tx = x
        ty = y
    if i !=n-1:
        x+=dx[3]
        y+=dy[3]
    start-=1

n-=1
direction=0
cnt=0
while n>0:
    x,y,start=Move(n,direction,x,y,start)
    cnt+=1
    if cnt %2==0:
        n-=1
    direction+=1
    if direction==4:
        direction=0

for i in graph:
    print(*i)
print(tx+1,ty+1)