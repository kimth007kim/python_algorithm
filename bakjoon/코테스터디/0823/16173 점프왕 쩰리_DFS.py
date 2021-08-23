import sys
sys.setrecursionlimit(100000)

input= sys.stdin.readline

dx=[0,1]
dy=[1,0]

def dfs(x,y):
    global cnt
    if x<0 or x>=n or y<0 or y>=n:
        return
    if x==n-1 and y ==n-1:
        # print("찾음",cnt)
        cnt+=1
        # print("바뀐",cnt)
        return
    dfs(x,y+graph[x][y])
    dfs(x+graph[x][y],y)
    return

n= int(input())
graph= []
for i in range(n):
    graph.append(list(map(int,input().split())))
cnt=0
dfs(0,0)
if cnt!=0:
    print("HaruHaru")
else:
    print("Hing")