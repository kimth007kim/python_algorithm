from collections import deque

n,l,r= map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def process(x,y,index):
    united=[]
    united.append((x,y))
    # print("united",united)
    q=deque()
    q.append((x,y))
    union[x][y]=index
    print("----------union---------",union)
    summary=graph[x][y]
    # print("united:",united,"    q:",q,"    union:",union,"  graph:",graph)
    count =1
    while q:
        print("x,y",x,y,"       ",q)
        x,y = q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny=y+dy[i]
            if 0 <= nx <n and 0<= ny <n and union[nx][ny]==-1:
                if l <= abs(graph[nx][ny]- graph[x][y])<=r:
                    print("index:",index)
                    # print(graph[nx][ny],"    ",nx,ny,"    index:",index)
                    q.append((nx,ny))
                    union[nx][ny]=index
                    print("----------union---------",union)
                    summary+=graph[nx][ny]
                    count+=1
                    united.append((nx,ny))

    for i,j in united:
        graph[i][j]=summary//count
    print("---------------------------- 바뀐 graph:",graph)

total_count=0

while True:
    union=[[-1]* n for _ in range(n)]
    index=0
    for i in range(n):
        for j in range(n):
            if union[i][j]== -1:
                print()
                print("  ---    ","i:", i, "j:",j,"index:",index,"   --- ")
                process(i,j,index)
                index+=1
    if index == n*n:
        break
    total_count+=1

print(total_count)
