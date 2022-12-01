from collections import deque


def turn(num):
    if direction[num] == 1:
        direction[num] = 2
    elif direction[num] == 2:
        direction[num] = 1
    elif direction[num] == 3:
        direction[num] = 4
    elif direction[num] == 4:
        direction[num] = 3


def show(arr):
    for i in arr:
        print(i)


def blue(num, x, y, arr):
    print("blue 호출")
    print(arr)
    d = direction[num]
    tx = x + way[d][0]
    ty = y + way[d][1]
    if tx < 0 or ty < 0 or tx >= n or ty >= n:
        for i in arr:
            graph[x][y].append(i)
        return x, y
    else:
        if graph[tx][ty] == 0:
            white(tx, ty, arr)
            return tx, ty
        elif graph[tx][ty] == 1:
            red(tx, ty, arr)
            return tx, ty
        else:
            for i in arr:
                graph[x][y].append(i)
            return x, y



def red(x, y, arr):
    # print("red 호출")
    for i in range(len(arr) - 1, -1, -1):
        graph[x][y].append(arr[i])


def white(x, y, arr):
    # print("white 호출")
    for i in arr:
        graph[x][y].append(i)
    # print(graph[x][y])
    # show(graph)


def simulate(chess_set):
    cnt = 1
    show(graph)
    while cnt < 1001:
        new_one = []
        for num, x, y in chess_set:
            # print(num,x,y)
            d = direction[num]
            # 움직일 말들을 구하는 메서드
            now = 0

            for i in range(len(graph[x][y])):
                if graph[x][y][i] == num:
                    now = i
                    break
            # print(len(graph[x][y]),graph[x][y] ,[],len([]))
            # print(graph[x][y][:now],graph[x][y][now:])
            cand = graph[x][y][now:]
            tmp = graph[x][y][:now]
            # if cand[0]!=num:
            #     new_one.append([num, nx, ny])
            #     continue
            graph[x][y] = tmp
            print(cand,"     ======     ",tmp)
            # print(i,graph[x][y][i])
            # print(now, graph[x][y][i])
            # 움직일칸의 색깔 구분하는 메서드
            nx = x + way[d][0]
            ny = y + way[d][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                nx,ny= blue(num, x, y, cand)
                # turn(num)
            else:
                if board[nx][ny] == 0:
                    white(nx, ny, cand)
                if board[nx][ny] == 1:
                    red(nx, ny, cand)
                if board[nx][ny] == 2:
                    nx,ny=blue(num, x, y, cand)
            new_one.append([num, nx, ny])
            for i in graph[nx][ny]:
                # print(i)
                for j in range(len(chess_set)):
                    print(i,chess_set[j],nx,ny)
                    if i ==chess_set[j][0]:
                        if chess_set[j][1]!=nx or chess_set[j][2]!=ny:
                            chess_set[j][1]=nx
                            chess_set[j][2]=ny
                            print("=====",i,chess_set[j],nx,ny)
            # print(new_one)
            # nx,ny 의 4개이상이면 종료 시키기

            if len(graph[nx][ny]) >= 4:
                return cnt
        show(graph)
        print(new_one)
        print(cnt)
        cnt += 1
        chess_set = new_one
    return -1


way = {}
way[1] = [0, 1]
way[2] = [0, -1]
way[3] = [-1, 0]
way[4] = [1, 0]

direction = {}

n, k = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(n)]
board = []
chess_set = []
for i in range(n):
    board.append(list(map(int, input().split())))
for i in range(k):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    chess_set.append([i + 1, x, y])
    graph[x][y].append(i + 1)
    direction[i + 1] = d

answer = simulate(chess_set)

# show(graph)
# print(chess_set)
print(answer)
