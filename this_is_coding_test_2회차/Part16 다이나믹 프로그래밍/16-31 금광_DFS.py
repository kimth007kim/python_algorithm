# t=int(input())
n,m = map(int,input().split())
graph=[[] for _ in range(n)]
d=[0]*(10001)
data=list(map(int,input().split()))
for i in range(n):
    for j in range(m):
        graph[i].append(data[j+(i*m)])
MAXVALUE=0

def dfs(cnt,x,y,result):
    global MAXVALUE
    if cnt == m-1:
        print("끝",result)
        MAXVALUE= max(result,MAXVALUE)
        return
    print("x,y",x,y)
    for i in [-1,0,1]:
        nx = x+i
        ny = y+1
        if nx >=0 and nx<n and ny<m:
            dfs(cnt+1,nx,ny,result+graph[nx][ny])


for i in range(n):
    dfs(0,i,0,graph[i][0])

print(MAXVALUE)


print(graph)