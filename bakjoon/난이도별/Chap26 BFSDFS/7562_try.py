from collections import deque

def bfs(sx,sy,ex,ey):
    q=deque()
    q.append((sx,sy))
    cnt=0
    while q:
        print(q)
        cnt+=1
        print(cnt)
        for i in range((len(q))):
            x,y=q.popleft()
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=length or ny<0 or ny>= length:
                    continue
                else:
                    q.append((nx,ny))
                if (ex,ey) in q:
                    return cnt


ans=[]
dd=[]
dx=[1,2,2,1,-1,-2,-1,-2]
dy=[2,1,-1,-2,-2,-1,2,1]
# case= int(input())
# for i in range(case):
#     length=int(input())
#     sx,sy= map(int,input().split())
#     ex,ey= map(int,input().split())
#
#     dd.append((length,sx,sy,ex,ey))

length=int(input())
sx,sy= map(int,input().split())
ex,ey= map(int,input().split())


if sx == ex and sy== ey:
    ans.append(0)
else:
    ans.append(bfs(sx,sy,ex,ey))

for j in ans:
    print(j)