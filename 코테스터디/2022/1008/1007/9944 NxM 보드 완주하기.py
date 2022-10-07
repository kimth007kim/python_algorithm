import sys
input = sys.stdin.readline

dx=[0,1,0,-1]
dy=[-1,0,1,0]

def check(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j]==".":
                return False
    return True
def bt(x,y,cnt):
    global answer
    # print(answer,cnt)
    # for i in graph:
    #     print(i)
    if check(graph)==True:
        # print("여기")
        answer=min(answer,cnt)
    if cnt<answer:
        for i in range(4):
            tx= dx[i]+x
            ty= dy[i]+y
            if 0<=tx<n and 0<=ty<m and graph[tx][ty]==".":
                tmp=[]
                nx= x
                ny= y
                while 0<=nx<n and 0<=ny<m:
                    nx=dx[i]+nx
                    ny=dy[i]+ny
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny]==".":
                        tmp.append([nx, ny])
                    else:
                        break
                    # graph[nx][ny]="*"
                # print(tmp)
                for px, py in tmp:
                    graph[px][py] = "*"
                graph[x][y]="*"
                if len(tmp)>=1:
                    bt(tmp[-1][0],tmp[-1][1],cnt+1)
                graph[x][y]="."
                for px, py in tmp:
                    graph[px][py] = "."
num=1
while True:
    answer=int(1e11)
    try:
        n, m = map(int, input().split())
    except:
        break
    graph=[]
    for i in range(n):
        graph.append(list(input().rstrip()))

    k=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==".":
                k+=1
    if k ==1:
        print("Case {}: {}".format(num,0))
        num += 1
        continue

    for i in range(n):
        for j in range(m):
            if graph[i][j]==".":
                bt(i,j,0)
                # print(i,j)
                # break
        # break
    if answer ==int(1e11):
        answer=-1
    print("Case {}: {}".format(num,answer))
    num+=1
