from collections import deque

n,k,r = map(int,input().split())
road= [[[]for _ in range(n)] for _ in range(n)]
cow_map = [ [False]*n for _ in range(n)]
cow_list=[]

dx=[0,1,0,-1]
dy=[-1,0,1,0]
result=0
for i in range(r):
    x1,y1,x2,y2= map(int,input().split())
    road[x1-1][y1-1].append([x2-1,y2-1])
    road[x2-1][y2-1].append([x1-1,y1-1])
for i in range(k):
    x,y= map(int,input().split())
    cow_list.append([x-1,y-1])
    cow_map[x-1][y-1] = True

for r,c in cow_list:
    if cow_map[r][c]:
        visited = [[True for _ in range(n)] for _ in range(n)]
        k-=1
        cnt=0
        q=deque()
        q.append([r,c])
        cow_map[r][c]=False
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx=dx[i]+x
                ny=dy[i]+y
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]==True:
                    if [nx,ny] not in road[x][y]:
                        visited[nx][ny]=False
                        q.append([nx,ny])
                        if cow_map[nx][ny]==True:
                            cnt+=1
        result += k - cnt
print(result)



