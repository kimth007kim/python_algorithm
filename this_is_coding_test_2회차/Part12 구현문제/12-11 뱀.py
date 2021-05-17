

n=int(input())      #보드의 크기
k=int(input())      #사과의 갯수
data=[[0]*(n+1) for _ in range(n+1)]
info=[]

for i in range(k):
    a,b=map(int,input().split())
    data[a][b]=1
l=int(input())      #방향 변환 횟수

for i in range(l):
    a,b=map(str,input().split())
    info.append((int(a),b))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction,c):
    if c=="L":
        direction = (direction -1)%4
    else:
        direction = (direction +1)%4
    return direction

def simulate():
    x,y=1,1
    data[x][y]=2
    direction=0
    time=0
    index=0
    q=[(x,y)]
    while True:
        nx =x+dx[direction]
        ny= y+dy[direction]
        if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][ny]!=2:
            if data[nx][ny]==0:
                data[nx][ny]=2
                q.append((nx,ny))
                px,py=q.pop(0)
                data[px][py]=0
            if data[nx][ny]==1:
                data[nx][ny]=2
                q.append((nx,ny))
        else:
            time+=1
            break
        x,y=nx,ny
        time+=1
        if index <l and time == info[index][0]:
            direction = turn(direction,info[index][1])
            index+=1
    return time
print(simulate())