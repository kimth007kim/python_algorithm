rows=6
columns=6
queries	=[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# queries	=[[2,2,5,4]]
result =[8, 10, 25]


def solution(rows, columns, queries):
    graph = [[0] * rows for _ in range(columns)]
    answer = []
    cnt = 1
    for i in range(columns):
        for j in range(rows):
            graph[i][j] = cnt
            cnt += 1
    for j in queries:

        x1, y1, x2, y2 = j
        if x1 > x2:
            dx = x1 - x2
        else:
            dx = x2 - x1
        if y1 > y2:
            dy = y1 - y2
        else:
            dy = y2 - y1
        total = getxy(x1, y1, x2, y2)
        answer.append(newxy(total, dx, dy, graph))
        for j in graph:
            print(j)
        print()

    return answer


def newxy(total, dx, dy, graph):
    minNum=10000
    copygraph = graph
    map = [[0] * (dy + 1) for i in range(dx + 1)]
    map1 =[[0] * (dy + 1) for i in range(dx + 1)]
    sx,sy=total[0]
    ex,ey=total[len(total)-1]
    nx,ny=sx-1,sy-1
    for a in range(sx-1,ex):
        for b in range(sy-1, ey):
            map[a-nx][b-ny]=graph[a][b]
            map1[a - nx][b - ny] = graph[a][b]
            if a==0 and b==0:
                minNum=map[a-nx][b-ny]
            if (a+1,b+1) in total:
                minNum=min(minNum,map[a-nx][b-ny])
    #             print(a+1,b+1)
    # print(minNum)
    # print(dx)
    for a in range(dx+1):
        for b in range(dy+1):
            if (a+nx+1,b+ny+1) in total:
                if a==dx and b !=0:
                    map[a][b-1]=map1[a][b]
                if a==0 and b !=dy:
                    map[a][b+1]=map1[a][b]
                if a!=dx and b ==dy:
                    map[a+1][b]=map1[a][b]
                if a!=0 and b ==0:
                    map[a-1][b]=map1[a][b]

    for a in range(sx-1,ex):
        for b in range(sy-1, ey):
            graph[a][b]=map[a-nx][b-ny]
            # map[a-nx][b-ny]=graph[a][b]
            # map1[a - nx][b - ny] = graph[a][b]
            # print(a,b)
    return minNum

def getxy(x1, y1, x2, y2):
    total = []
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if i == x1 or i == x2 or j == y1 or j == y2:
                total.append((i, j))
    return total

print(solution(rows, columns, queries))