# https://landlordgang.tistory.com/100?category=458943

from collections import deque
import sys

n,k,r =map(int,input().split())


load= [[[]for _ in range(n)] for _ in range(n)]
cow_map= [[False for _ in range(n)] for _ in range(n)]
cow_list=[]


for i in range(r):
    x1,y1,x2,y2= map(int,input().split())
    load[x1-1][y1-1].append([x2-1,y2-1])
    load[x2-1][y2-1].append([x1-1,y1-1])

for i in load:
    print(i)
for i in range(k):
    x1,y1 = map(int,input().split())
    cow_list.append([x1-1,y1-1])
    cow_map[x1-1][y1-1]=True
print(cow_list)
dx= [-1,0,1,0]
dy= [0,1,0,-1]

result = 0
for r,c in cow_list:

    print("시작시작시작시작시작시작시작시작시작시작",r,c,"시작시작시작시작시작시작시작시작시작시작")
    if cow_map[r][c]:
        visited=[[True for _ in range(n)]for _ in range(n)]
        q=deque()
        q.append([r,c])
        print("=====================================")
        print("cow_map")
        for i in cow_map:
            print(i)
        print("=====================================")
        cow_map[r][c]=False
        cnt=0
        k-=1
        while q:
            x,y  = q.popleft()
            print("x,y",x,y)
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]:
                    if[nx,ny] not in load[x][y]:
                        print(nx,ny)
                        q.append([nx,ny])
                        visited[nx][ny]=False
                        print(" -------------------------------------- ")
                        print("visited")
                        for i in visited:
                            print(i)
                        print(" -------------------------------------- ")
                        if cow_map[nx][ny]:
                            cnt+=1
                            print(cnt)
    result +=k-cnt
    print("result = ",result)

print(result)