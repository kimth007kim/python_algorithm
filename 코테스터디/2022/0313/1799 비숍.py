import sys
input = sys.stdin.readline
def judge(arr,n):
    dx= [1,1,-1,-1]
    dy=[1,-1,1,-1]
    effect=[]
    if len(arr)==1:
        return True
    for i in range(len(arr)):
        for j in range(4):
            x,y=arr[i]
            while 0<=x+dx[j]<n and 0<=y+dy[j]<n:
                x=x+dx[j]
                y=y+dy[j]
                if [x,y] in arr:
                    return False
    return True


def dfs(arr,now,point,n):
    global MAX
    if judge(arr,n)==False:
        return
    MAX=max(MAX,len(arr))
    for i in range(now+1,len(point)):
        if point[i] not in arr:
            arr.append(point[i])
            dfs(arr,i,point,n)
            arr.remove(point[i])

n= int(input())
graph=[list(map(int,input().split()))for _ in range(n)]

point =[]
MAX=0
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            point.append([i,j])

for i in range(len(point)):
    dfs([point[i]],i,point,n)
print(MAX)