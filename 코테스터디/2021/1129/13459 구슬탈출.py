from collections import deque
import sys
input = sys.stdin.readline


def SHOW(pp):
    for i in pp:
        print(i)
    print()

def Copy(n_graph,n,m):
    tmp = [["-"]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
              tmp[i][j]=n_graph[i][j]

    return tmp


def MOVE(n_graph,direction):
    global answer
    cgraph= Copy(n_graph,n,m)

    # direction= 0 위쪽으로 움직이기 구현 o

    blue_hole=False
    red_hole=False

    if direction == 0:
        for j in range(m):
            tmpq = deque()
            for i in range(n):
                ch = n_graph[i][j]
                if ch=="R" or ch =="B":
                    tmpq.append([ch,i,j])
            while tmpq:
                t_type,t_x,t_y=tmpq.popleft()
                next = t_x
                for k in range(t_x-1,-1,-1):
                    if n_graph[k][j]=="#" or n_graph[k][j]=="R" or n_graph[k][j]=="B":
                        break
                    if n_graph[k][j]=="O":
                        if t_type=="R":
                            red_hole=True
                            next = t_x
                        if t_type=="B":
                            next = t_x
                            blue_hole=True
                        n_graph[t_x][t_y]="."
                        break
                    else:
                        next=k
                if next!= t_x:
                    n_graph[next][t_y]=t_type
                    n_graph[t_x][t_y]="."




    # direction= 1 오른쪽 으로 움직이기 구현 x
    if direction == 1:
        for i in range(n):
            tmpq = deque()
            for j in range(m-1,-1,-1):
                ch = n_graph[i][j]
                if ch == "R" or ch == "B":
                    tmpq.append([ch, i, j])
            while tmpq:
                t_type, t_x, t_y = tmpq.popleft()
                next = t_y
                for k in range(t_y+1,m):

                    if n_graph[i][k] == "#" or n_graph[i][k] == "R" or n_graph[i][k] == "B":
                        break
                    if n_graph[i][k] == "O":
                        if t_type == "R":
                            red_hole = True
                            next = t_y
                        if t_type == "B":
                            blue_hole = True
                            next = t_y
                        n_graph[t_x][t_y] = "."
                        # SHOW(graph)
                        break
                    else:
                        next = k
                if t_y != next:
                    n_graph[t_x][next] = t_type
                    n_graph[t_x][t_y] = "."

    # direction= 2 아래쪽 으로 움직이기 구현 o
    if direction == 2:
        for j in range(m):
            tmpq = deque()
            for i in range(n-1,-1,-1):
                ch = n_graph[i][j]
                if ch == "R" or ch == "B":
                    tmpq.append([ch, i, j])

            while tmpq:
                t_type, t_x, t_y = tmpq.popleft()
                next = t_x
                for k in range(t_x+1,n):
                    if n_graph[k][j] == "#" or n_graph[k][j] == "R" or n_graph[k][j] == "B":
                        break
                    if n_graph[k][j] == "O":
                        if t_type == "R":
                            red_hole = True
                            next = t_x
                        if t_type == "B":
                            blue_hole = True
                            next=t_x
                        n_graph[t_x][t_y] = "."
                        break
                    else:
                        next = k
                if next != t_x:
                    n_graph[next][t_y] = t_type
                    n_graph[t_x][t_y] = "."


    # direction= 3 왼쪽으로 움직이기 구현 o
    if direction ==3:
        for i in range(n):
            tmpq = deque()
            for j in range(m):
                ch = n_graph[i][j]
                if ch == "R" or ch == "B":
                    tmpq.append([ch, i, j])
            while tmpq:
                t_type, t_x, t_y = tmpq.popleft()
                next = t_y
                for k in range(t_y - 1, -1, -1):
                    if n_graph[i][k] == "#" or n_graph[i][k] == "R" or n_graph[i][k] == "B":
                        break
                    if n_graph[i][k] == "O":
                        if t_type == "R":
                            red_hole = True
                            next=t_y
                        if t_type == "B":
                            blue_hole = True
                            next = t_y
                        n_graph[t_x][t_y] = "."
                        break
                    else:
                        next = k
                if t_y!= next:
                    n_graph[t_x][next] = t_type
                    n_graph[t_x][t_y] = "."

    if blue_hole ==False and red_hole==True:
        answer = 1
        return cgraph,cgraph,0

    elif (blue_hole== True and red_hole==False) or(blue_hole== True and red_hole==True):
        return cgraph,cgraph,1

    elif blue_hole==False and red_hole==False:
        return cgraph,n_graph,2



n,m = map(int,input().split())
answer=0
graph=[]
for i in range(n):
    graph.append(list(input().rstrip()))


def recur(graph,cnt,prev):
    global answer
    if cnt==0 or answer ==1:
        # print(cnt)
        return
    else:
        # print(cnt)

        for i in range(4):
            if prev != i:
                before_graph= Copy(graph,n,m)
                before,after,flag=MOVE(graph,i)
                if flag==0:

                    answer =1
                    return
                elif flag==1:
                    recur(before, cnt - 1, i)
                    graph= before_graph
                else:
                    # SHOW(after)
                    recur(after, cnt-1,i)
                    graph=before_graph

recur(graph,10,-1)
# for i in range(4):
#     MOVE(graph ,i)
#     SHOW(graph)

# MOVE(graph ,0)
# SHOW(graph)



print(answer)