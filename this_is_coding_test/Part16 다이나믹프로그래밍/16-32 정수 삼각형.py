n=int(input())
data=[]
dp=[0]*(n+1)

for i in range(n):
    data.append(list(map(int,input().split())))
x,y=0,0
dp[1]=data[x][y]

for i in range(1,n):
    if y-1<0:
        left=0
    else:
        left=data[i][y-1]
    if y+1> i-1:
        right=0
    else:
        right=data[i][y]
    dp[i+1]=dp[i]+max(left,right)

print(dp[n])