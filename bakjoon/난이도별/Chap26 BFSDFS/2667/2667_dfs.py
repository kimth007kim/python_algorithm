n= int(input())
graph=[]
cnt=0
ans=[]
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    global cnt
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if graph[x][y]==1:
        cnt+=1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            ans.append(cnt)
            cnt=0

ans.sort()
print(len(ans))
for i in ans:
    print(i)