import sys
inpuy = sys.stdin.readline

n,k= map(int,input().split())
data=[[0]*(k+1) for _ in range(n+1)]


# for d in data:
#     print(d)
#

for i in range(1,n+1):
    item,value = map(int,input().split())
    for j in range(k+1):
        if item>j:
            data[i][j]= data[i-1][j]
        else:
            data[i][j]=max(data[i-1][j],data[i-1][j-item]+value)

print(data[n][k])