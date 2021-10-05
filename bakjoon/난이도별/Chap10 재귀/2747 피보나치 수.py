n=int(input())



# 재귀 형식으로 구현해보기

# def fibo(n):
#     if n==1 or n==2:
#         return 1
#
#     print(n)
#     return fibo(n-1)+fibo(n-2)
#
# print(fibo(n))

# dp 형식으로 구현해보기

dp = [0]*(46)
dp[1]=1
dp[2]=1
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])