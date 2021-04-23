dp=[0]*1001
dp[1]=1
cnt=1

n= int(input())

for i in range(2,20):

    if cnt==n:
        print(i-1)
        break
    if dp[i//2]!=0 and i %2 ==0:
        cnt += 1
        dp[i] = cnt
        continue
    if dp[i // 3] != 0 and i %3 ==0:
        cnt += 1
        dp[i] = cnt
        continue
    if dp[i // 5] != 0 and i %5 ==0:
        cnt += 1
        dp[i] = cnt
        continue

