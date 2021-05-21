n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

cnt=0
def dfs(x,y):
    if x<=-1 or y<=-1 or x>=n or y>=m :
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            cnt+=1

print(cnt)
