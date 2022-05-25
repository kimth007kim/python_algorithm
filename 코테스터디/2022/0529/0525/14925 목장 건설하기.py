n,m = map(int,input().split())
graph=[]

for i in range(m):
    tmp = list(map(int,input().split()))
    graph.append(tmp)
    # for j in range(len(tmp)):
    #     if tmp[j]>0:
    #         tmp[j]=-1
    # graph.append(tmp)

MAX= 0
dp=[[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        print(i,j,dp[i][j])
        if graph[i-1][j-1]==0:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
            MAX=max(dp[i][j],MAX)
        # if graph[i-2][j-1]==-1 or graph[i-2][j-2]==-1 or graph[i-1][j-2]==-1:
        #     print("여기")
        #     dp[i][j]=0
        # else:
        #     dp[i][j]= max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        # print(dp[i][j])

    print(dp[i])
print()
for i in dp:
    print(i)

print(MAX)