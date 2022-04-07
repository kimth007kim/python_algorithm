from collections import deque



row,column,m = map(int,input().split())
dx=[1,0,-1,0]
dy=[0,1,0,-1]
score=0
graph = [ [deque()  for _ in range(column)]for _ in range(row)]

def catch_shark(graph,now):
    for i in range(row):
        if len(graph[i][now])>0:
            r,c,s,d,z=graph[i][now].popleft()
            return z
    return 0

def move_shark(graph):
    move = deque()
    for i in range(row):
        for j in range(column):
            if len(graph[i][j])!=0:
                move.append(graph[i][j].popleft())

    while move:
        arr= move.popleft()
        r,c,s,d,z= arr
        # print(arr)
        for i in range(s):
            tx=r+dx[d]
            ty=c+dy[d]
            if tx<0 or tx>=row or ty<0 or ty>=column:
                d=(d+2)%4
                tx=r+dx[d]
                ty=c+dy[d]
            # print(r,c,"   ",d,"  ",tx,ty)
            r,c= tx,ty
        if len(graph[r][c])!=0:
            if graph[r][c][0][4]<z:
                graph[r][c].popleft()
                graph[r][c].append([r,c,s,d,z])
        else:
            graph[r][c].append([r,c,s,d,z])
        # print("------------변환------------")
        # for k in graph:
        #     print(k)
        # print("------------변환------------")
for i in range(m):
    r1,c1,s,d,z=map(int,input().split())
    if d==1:
        d=2
    elif d==2:
        d=0
    elif d==3:
        d=1
    elif d==4:
        d=3
    r1,c1=r1-1,c1-1
    graph[r1][c1].append([r1,c1,s,d,z])

if m==0:
    print(0)
else:
    # for k in graph:
    #     print(k)
    # print("------------초기------------")
    for i in range(column):
        score+=catch_shark(graph,i)
        
        # print("------------잡음------------")
        # for k in graph:
        #     print(k)
        # print("------------잡음------------")
        
        move_shark(graph)
        # for k in graph:
        #     print(k)
        # print("----끝",i,"------")
    print(score)
