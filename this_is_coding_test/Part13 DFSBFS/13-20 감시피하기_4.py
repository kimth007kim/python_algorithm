from itertools import combinations

n=int(input())
graph=[]
teacher=[]
space=[]

for i in range(n):
    graph.append(list(map(str,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j]=="T":
            teacher.append((i,j))
        if graph[i][j]=="X":
            space.append((i,j))

def check(x,y,direction):
    if direction==0:
        while y>=0:
            if graph[x][y]=="S":
                return True
            if graph[x][y]=="O":
                return False
            y-=1
    if direction==1:
        while y<n:
            if graph[x][y]=="S":
                return True
            if graph[x][y]=="O":
                return False
            y+=1
    if direction==2:
        while x>=0:
            if graph[x][y]=="S":
                return True
            if graph[x][y]=="O":
                return False
            x-=1
    if direction==3:
        while x < n:
            if graph[x][y] == "S":
                return True
            if graph[x][y] == "O":
                return False
            x += 1
    return False

def process():
    for x,y in teacher:
        for i in range(4):
            if check(x,y,i):
                return True
    return False

find = False

for data in combinations(space,3):
    for x,y in data:
        graph[x][y]="O"
    if not process():
        find=True
        break
    for x,y in data:
        graph[x][y]="X"

if find:
    print("YES")
else:
    print("NO")
