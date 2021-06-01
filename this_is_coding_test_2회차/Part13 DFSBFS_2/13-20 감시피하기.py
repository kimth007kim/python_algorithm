n=int(input())
graph=[]
teacher=[]

for i in range(n):
    temp= list(map(str,input().split()))
    for j in range(len(temp)):
        if temp[j]=="T":
            teacher.append((i,j))
    graph.append(temp)

def process():
    for x,y in teacher:
        for i in range(4):
            if watch(x,y,i):
                return True

def watch(x,y,direction):
    if direction==0:
        while y>=0:
            if graph[x][y]=='S':
                return True
            if graph[x][y] == 'O':
                return False
            y-=1
    if direction==1:
        while y<n:
            if graph[x][y]=='S':
                return True
            if graph[x][y] == 'O':
                return False
            y+=1
    if direction==2:
        while x>=0:
            if graph[x][y]=='S':
                return True
            if graph[x][y] == 'O':
                return False
            x-=1
    if direction==3:
        while x<n:
            if graph[x][y]=='S':
                return True
            if graph[x][y] == 'O':
                return False
            x+=1
    return False
find=False


def dfs(cnt):
    global find
    if cnt==3:
        if not process():
            find=True
        return
    for i in range(n):
        for j in range(n):
            if graph[i][j]=="X":
                graph[i][j]="O"
                cnt+=1
                dfs(cnt)
                cnt-=1
                graph[i][j]="X"

dfs(0)

if find:
    print("YES")
else:
    print("NO")