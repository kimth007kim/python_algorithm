import sys
# input =sys.stdin.readline
def danger(wolf,graph):
    for x,y in wolf:
        for i in range(4):
            nx= dx[i]+x
            ny=dy[i]+y
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]=="S":
                return False
            if graph[nx][ny]==".":
                graph[nx][ny]="D"
    return True

def check(wolf,graph):
    for x, y in wolf:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 and nx >= n or ny >= m:
                continue
            if graph[nx][ny]=="S":
                return False
    return True

def bfs():

    global dx,dy,n,m
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    n,m=map(int,input().split())
    graph=[list(input()) for _ in range(n)]
    wolf =[]
    for i in range(n):
        for j in range(m):
            if graph[i][j]=="W":
                wolf.append((i,j))
    isDanger=danger(wolf,graph)
    if isDanger==False:
        print(0)
        return
    if check(wolf,graph)==False:
        print(0)
        return
    else:
        print(1)
        tmp=[]
        for g in graph:
            tmp.append("".join(g))
        for i in tmp:
            print(i)
        return
bfs()