from collections import deque


n,k= map(int,input().split())
data=[]
copy=[]
maxNum=0

for i in range(n):
    temp=list(map(int,input().split()))
    data.append(temp)
    copy.append(temp)
    maxNum=max(maxNum,max(temp))



s,x,y= map(int,input().split())

dx=[0,-1,0,1]
dy=[1,0,-1,0]

print(maxNum)
# print(data)

def bfs(cnt):
    for i in range(n):
        for j in range(k):
            if data[i][j]== cnt:
                for a in range(4):
                    nx=i+dx[a]
                    ny=j+dy[a]
                    if nx >=0 and nx<n and ny>=0 and ny<k and data[nx][ny]==0:
                        copy[nx][ny]=cnt



bfs(1)
print(copy)