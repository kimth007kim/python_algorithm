# Dummy 라는 도스게임 
# 뱀은 매초마다 이동

# n번째 보드의 크기
# 6         n번째 보드의 크기
# 3         k개 사과의 갯수
# 3 4       사과위치1
# 2 5       사과위치2
# 5 3       사과위치3
# 3         방향변환정보 오른쪽D또는 왼쪽L 로 90도 회전
# 3 D       3초후에 오른쪽으로회전
# 15 L
# 17 D

# 방향변환정보
#  오른쪽D 로 90도 회전
#  왼쪽L 로 90도 회전

n= int(input())
k= int(input())
data = [[0]*(n+1) for _ in range(n+1)]
info=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for j in range(k):
    a,b = map(int,input().split())
    data[a][b]=1


l= int(input())
for i in range(l):
    c,d= map(str,input().split())
    c= int(c)
    info.append((c,d))

def turn(direction,c):
    if c=="L":
        direction=(direction-1) %4
    else:
        direction=(direction+1) %4
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
        ny =y+dy[direction]
        if 1 <=nx and nx<=n and 1 <=ny and ny<=n and data[nx][ny]!=2:
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
        if index<l and time == info[index][0]:
            direction =turn(direction,info[index][1])
            index+=1
    return time

print(simulate())
