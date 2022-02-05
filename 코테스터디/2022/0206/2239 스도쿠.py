from collections import deque

def dimension_check(x,y):
    if 0<=x<3:
        if 0<=y<3:
            return 0,3,0,3
        elif 3<=y<6:
            return 0,3,3,6
        elif 6<=y<9:
            return 0,3,6,9
    elif 3<=x<6:
        if 0<=y<3:
            return 3,6,0,3
        elif 3<=y<6:
            return 3,6,3,6
        elif 6<=y<9:
            return 3,6,6,9
    else:
        if 0<=y<3:
            return 6,9,0,3
        elif 3<=y<6:
            return 6,9,3,6
        elif 6<=y<9:
            return 6,9,6,9




graph = []
q = deque()
ALL= {"1","2","3","4","5","6","7","8","9"}
# print(ALL)

for i in range(9):
    tmp = list(input())
    for j in range(9):
        if tmp[j]=='0':
            q.append([i,j])
    graph.append(tmp)

while q:
    x,y= q.popleft()
    candidate=[]
    sx,ex,sy,ey=dimension_check(x, y)
    for i in range(sx,ex):
        for j in range(sy,ey):
            if graph[i][j]!="0":
                candidate.append(graph[i][j])

    for i in range(9):
        if graph[x][i] !="0":
            candidate.append(graph[x][i])
    for i in range(9):
        if graph[i][y] !="0":
            candidate.append(graph[i][y])

    can= set(candidate)
    result = ALL-can
    if len(result)==1:
        graph[x][y]=list(result)[0]
    else:
        q.append([x,y])

for i in graph:
    print("".join(i))