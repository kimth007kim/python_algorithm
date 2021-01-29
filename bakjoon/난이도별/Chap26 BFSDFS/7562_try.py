from collections import deque

# def bfs(sx,sy,ex,ey):
def bfs():
    q=deque()
    q.append([sx,sy])
    done[sx][sy]=1
    while q:
        print(q)
        x,y=q.popleft()

        if(x,y)== (ex,ey):
            return(done[x][y]-1)
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if (0<=nx<length)and(0<=ny<length) and done[nx][ny]==0:
                q.append([nx,ny])
                done[nx][ny]=done[x][y]+1

# ans=[]
dx=[1,2,2,1,-1,-2,-1,-2]
dy=[2,1,-1,-2,-2,-1,2,1]
case= int(input())
for i in range(case):
    length=int(input())
    sx,sy= map(int,input().split())
    ex,ey= map(int,input().split())
    done= [[0]* length for _ in range(length)]

    if sx==ex and sy==ey:
        print(0)
        continue
    # ans=bfs(sx,sy,ex,ey)
    ans=bfs()
    print(ans)

# for j in ans:
#     print(j)