from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=[]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        y, x = q.popleft()
        graph[y][x] = 0
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx]==1:
                q.append((ny, nx))
                graph[ny][nx] = 0
    return 1
t = int(input())
for i in range(t):
    m, n, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1
    cnt = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                print("cnt=",cnt)
                print("bfs값=",bfs(y,x))
                cnt += bfs(y,x)
    ans.append(cnt)
for j in ans:
    print(j)