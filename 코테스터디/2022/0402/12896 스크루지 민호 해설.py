import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
node=[[] for _ in range(n)]
visited=[False for _ in range(n)]

dis=(-1,0)

for i in range(n-1):
    a,b= map(int,input().split())
    node[a-1].append(b-1)
    node[b-1].append(a-1)

def dfs(num,depth):
    global dis
    if dis[0]==-1 or depth>dis[0]:
        dis=(depth,num)
        print(dis)
    for i in node[num]:
        if visited[i]:
            continue
        visited[i]=True
        dfs(i,depth+1)
dfs(0, 0)
temp = dis[1]

dis = (-1, 0)
visited = [False for _ in range(n)]
dfs(temp, 0)
if dis[0] % 2 == 0:
    print(dis[0] // 2)
else:
    print(dis[0] // 2 + 1)