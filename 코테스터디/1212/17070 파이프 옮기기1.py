from collections import deque
import sys

input = sys.stdin.readline

def judge_direction(sx,sy,ex,ey):
    x= ex-sx
    y= ey-sy

    if x==0 and y==1:
        # 가로
        return [0,1],[1,1]
    elif x==1 and y==0:
        # 세로
        return [1,1],[0,1]
    # else:
    elif x==1 and y==1:
        # 대각
        return [1,0,1],[0,1,1]

n= int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))


# n= 13
# graph=[[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0]]


q=deque()
q.append([0,0,0,1])
cnt=0



while q:
    # print(q)
    sx,sy,ex,ey=q.popleft()
    # print(sx,sy,ex,ey)
    if sx>n-1 or sy>n-1 or ex>n-1 or ey>n-1:
        continue
    if ex== n-1 and ey==n-1:
        cnt+=1
        continue
    dx,dy=judge_direction(sx,sy,ex,ey)

    for i in range(len(dx)):
        if dx[i]==1 and dy[i] ==1:
            if ex+1<n and ey+1<n:
                if graph[ex+1][ey] == 0 and graph[ex][ey+1] == 0 and graph[ex+1][ey+1] == 0:
                    q.append([ex,ey,ex+1,ey+1])
        else:
            nx = dx[i]+ex
            ny= dy[i]+ey
            if nx<n and ny<n and graph[nx][ny]==0:
                q.append([ex,ey,nx,ny])

print(cnt)