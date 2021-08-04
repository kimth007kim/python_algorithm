import sys
sys.setrecursionlimit(3000000)
input = sys.stdin.readline


n,m = map(int,input().split())
# n이 가로 m 이 세로
w=b=0

dx= [1,0,-1,0]
dy = [0,1,0,-1]

visited= [[False]*n for _ in range(m)]

print(visited)


def dfs(x,y,cnt):
    c=graph[x][y]
    graph[x][y]=1
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if(0<= nx<m) and (0<= ny < n) and graph[nx][ny]==c:
            cnt=dfs(nx,ny,cnt+1)
    return cnt


graph =[]

for i in range(m):
    graph.append(list(input().strip()))



for i in range(m):
    for j in range(n):
        if graph[i][j]=="W":
            w+= dfs(i,j,1)**2
        elif graph[i][j]=="B":
            b+= dfs(i,j,1)**2
        print(w,b)

print(w,b)