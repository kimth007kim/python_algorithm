import sys
input = sys.stdin.readline


def copy_graph(graph):
    x= len(graph)
    y=len(graph[0])
    copied= [ [0]*y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            copied[i][j]= graph[i][j]

    return copied

def calc(graph):
    result=[]
    x=len(graph)
    y=len(graph[0])
    for i in range(x):
        total=0
        for j in range(y):
            total+=graph[i][j]
        result.append(total)
    return min(result)

def turn(graph,point):
    if (point[0]>=point[2] and point[1]>=point[3]) or (point[0]>=len(graph) or (point[1]>=len(graph)) or (point[3]<0) or (point[2]<0)) :
        return graph
    x1, y1, x2, y2=point
    prev  =graph[x1+1][y1]
    for i in range(y1,y2+1):
        now = graph[x1][i]
        graph[x1][i]= prev
        prev=now
    for i in range(x1+1,x2+1):
        now = graph[i][y2]
        graph[i][y2]=prev
        prev = now
    for i in range(y2-1,y1-1,-1):
        now = graph[x2][i]
        graph[x2][i] = prev
        prev = now
    for i in range(x2-1,x1-1,-1):
        now = graph[i][y1]
        graph[i][y1]=prev
        prev=now
    x1,y1,x2,y2=x1+1,y1+1,x2-1,y2-1
    return turn(graph,[x1,y1,x2,y2])

def dfs(now,arr,graph):
    global answer
    # print(now,arr,graph)
    next=turn(graph,now)
    if len(arr)==k:

        answer.append(calc(next))

        return
    for i in cand:
        if i not in arr:
            arr.append(i)
            copy= copy_graph(next)
            dfs(i,arr,copy)
            arr.pop()
answer=[]
n,m,k = map(int,input().split())
graph= [list(map(int,input().split())) for _ in range(n)]
cand=[]
for i in range(k):
    x,y,z = map(int,input().split())
    x1,y1,x2,y2 = x - z - 1,y - z - 1, x + z - 1,y + z - 1
    cand.append([x1,y1,x2,y2])


for i in cand:
    dfs(i,[i],copy_graph(graph))

print(min(answer))