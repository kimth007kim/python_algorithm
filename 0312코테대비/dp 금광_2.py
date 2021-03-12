# n,m = map(int,input().split())
# array= list(map(int,input().split()))
# n,m=3,4
# array=[1,3,3,2,2,1,3,1,0,6,4,7]
n,m=4,4
array=[1,3,1,5,2,2,4,1,5,0,2,3,0,6,1,2]
dp=[]

index=0
for i in range(n):
    dp.append(array[index:index+m])
    index+=m

for j in dp:
    print(j)

for j in range(1,m):
    for i in range(n):
        print(i,j,dp[i][j])
        if i==0:
            print("i==0인부분")
            left_up =0
        else:
            left_up= dp[i-1][j-1]
        if i == n-1:
            print("i==n-1인부분")
            left_down=0
        else:
            left_down=dp[i+1][j-1]
        left=dp[i][j-1]
        dp[i][j]= dp[i][j]+max(left_up,left_down,left)

for j in dp:
    print(j)
# dp[i][j]= dp[i][j]+max(low,lex,lem)