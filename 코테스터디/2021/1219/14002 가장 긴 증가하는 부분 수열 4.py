n= int(input())
arr = list(map(int,input().split()))

dp= [1]*n

for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]= max(dp[i],dp[j]+1)
MX= max(dp)
cnt=MX
stack=[]
for i in range(n-1,-1,-1):
    if cnt == 1 and dp[i]==1:
        stack.append(i)
        break
    if dp[i]==cnt:
        stack.append(i)
        cnt-=1

answer=[]
while stack:
    tmp = stack.pop()
    # print(tmp,arr[tmp])
    answer.append(str(arr[tmp]))
print(len(answer))
print(' '.join(answer))