
n= int(input())
dp=[0]*(36)

dp[0]=1
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    tmp=0
    for j in range(i//2):
        a,b= j, i-1-j
        tmp+=(2*dp[a]*dp[b])
    if i%2!=0:
        tmp+=dp[i//2]**2
    dp[i]=tmp
print(dp[n])