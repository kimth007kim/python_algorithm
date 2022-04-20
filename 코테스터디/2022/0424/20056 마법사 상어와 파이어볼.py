from collections import deque



dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

where=[[0,2,4,6],[1,3,5,7]]

n,m,time=map(int,input().split())
def fireball_move(board):
    q=deque()
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 0:
                while board[i][j]:
                    tmp = board[i][j].popleft()
                    x,y,m,s,d= tmp
                    tx,ty=x,y
                    for _ in range(s):
                        tx+=dx[d]
                        ty+=dy[d]
                        # print(tx,ty,i)
                        if tx==-1:
                            tx=n-1
                        if tx==n:
                            tx=0
                        if ty==-1:
                            ty=n-1
                        if ty==n:
                            ty=0
                    q.append([tx,ty,m,s,d])
    while q:
        x1,y1,mass,speed,direction=q.popleft()
        board[x1][y1].append([x1,y1,mass,speed,direction])


def fire_split(q,arr,flag):
    size= arr[2]//5

    if size==0:
        return
    cnt= len(flag)

    result_speed=arr[3]//cnt
    prev=flag[0]%2
    direction=where[0]
    for i in range(1,cnt):
        now=flag[i]%2
        if now!=prev:
            direction=where[1]
            break
    for i in range(4):
        q.append([arr[0],arr[1],size,result_speed,direction[i]])

def fire_sum(board):
    q=deque()
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:
                flag=[]
                total_mass=0
                total_speed=0
                while board[i][j]:
                    r,c,m,s,d=board[i][j].popleft()
                    flag.append(d)
                    total_mass+=m
                    total_speed+=s

                fire_split(q,[r,c,total_mass,total_speed],flag)
    while q:
        tx,ty,tm,ts,td=q.popleft()
        board[tx][ty].append([tx,ty,tm,ts,td])



fire=[]
board= [[deque() for _ in range(n)] for _ in range(n)]
for i in range(m):
    r,c,m,s,d= map(int,input().split())
    board[r-1][c-1].append([r-1,c-1,m,s,d])

for i in range(time):
    fireball_move(board)
    fire_sum(board)
answer=0
for i in range(n):
    for j in range(n):
        for a,b,c,d,e in board[i][j]:
            answer+=c

print(answer)