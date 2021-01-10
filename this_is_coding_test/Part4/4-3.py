n,m = map(int,input().split())

d=[[0]*m for _ in range(n)]
x,y,direction= map(int,input().split())
d[x][y] =1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dx= [-1,0,1,0]
dy= [0,1,0,-1]

def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction =3

count =1
turn_time=0
while True:
    turn_left()
    nx= x+dx[direction]
    ny= y+dy[direction]


    print(d[nx][ny])
    print(array[nx][ny])
    if d[nx][ny]==0 and array[nx][ny]==0:
        print("회전한 이후에 정면에 가보지 않은 칸이 존재하는 경우 이동")
        d[nx][ny]=1
        x= nx
        y= ny
        count +=1
        turn_time =0
        continue
    else:
        print("회전한 이후 정면에 가보지않은 칸이 없거나 바다인 경우")
        turn_time+=1
    # 네방향 모두 갈수 없는 경우
    if turn_time ==4:
        nx= x -dx[direction]
        ny= y -dy[direction]
        if array[nx][ny]==0:
            print("뒤로 갈수있다면 이동")
            x = nx
            y = ny
        else:
            print("뒤가 바다로 막혀있는 경우")
            break
        turn_time=0

print(count)