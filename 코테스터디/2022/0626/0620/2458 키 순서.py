
n,m = map(int,input().split())
height=[[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    tall,short=map(int,input().split())
    height [tall][short]=1


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if height[a][b]==1 or (height[a][k]==1 and height[k][b]):
                height[a][b]=1


for i in height:
    print(i)

answer= 0
for i in range(1,n+1):
    known_height = 0
    for j in range(1,n+1):
        known_height+=height[i][j]+height[j][i]

    if known_height == n-1:
        answer+=1
print(answer)