n,m,h= map(int,input().split())
print(n,m,h)
arr=[]
for i in range(n):
    tmp = list(map(int,input().split()))
    # tmp+=[0]
    # if len(tmp)<m:
    #     tmp+=[0]*(m-len(tmp))
    # tmp.sort()
    arr.append(tmp)

print(arr)

dp=[[0]*(h+1) for _ in range(m+1)]

for i in range(m+1):
    dp[i][0]=1
for i in dp:
    print(i)
for i in range(1,m+1):
    for j in range(h+1):
        dp[i][j]=dp[i-1][j]
    for k in arr[i-1]:
        for j in range(k,h+1):
            dp[i][j]+=dp[i-1][j-k]
            # print(i,"  ",j,"  ",k)

for i in dp:
    print(i)
