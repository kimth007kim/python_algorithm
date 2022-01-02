from collections import deque
import sys

input =sys.stdin.readline
MAXIMUM= int(1e9)

def init_bfs(dx,dy,n,m,visited,next_move):
    cnt = 0
    q = deque()
    q.append([cnt, 0, 0])
    MAXIMUM = int(1e9)
    while q:
        cnt, x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return True
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < n and ny < m and nx >= 0 and ny >= 0:
                if graph[nx][ny] == "0":
                    if visited[nx][ny] == MAXIMUM:
                        visited[nx][ny] = cnt
                        q.append([cnt, nx, ny])
                else:
                    next_move.append([cnt+1, nx, ny])
                    visited[nx][ny]=cnt+1

def next_bfs(dx,dy,n,m,visited,next_move):
    q = deque(next_move)
    maximum= 1000001
    while q:

        cnt, x, y = q.popleft()
        if cnt <= maximum:
            if x == n - 1 and y == m - 1:
                maximum =cnt
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < n and ny < m and nx >= 0 and ny >= 0:
                    if graph[nx][ny] == "0":
                        if visited[nx][ny] > cnt:
                            visited[nx][ny] = cnt
                            q.append([cnt, nx, ny])
                    else:
                        if visited[nx][ny]>cnt+1:
                            visited[nx][ny]=cnt+1
                            q.append([cnt + 1, nx, ny])
    return maximum
dx= [1,0,-1,0]
dy= [0,1,0,-1]

m,n = map(int,input().split())
visited= [[MAXIMUM]*m for _ in range(n)]


graph=[]
next_move=[]

for i in range(n):
    graph.append(list(input().rstrip()))
if init_bfs(dx,dy,n,m,visited,next_move):
    print(0)
else:
    # for i in next_move:
    #     i.append([])
    print(next_bfs(dx,dy,n,m,visited,next_move))



