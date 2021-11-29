import sys
input = sys.stdin.readline

arr =[]
MAX=-1
while True:
# for _ in range(6):
    n= input().rstrip()
    if n.isdigit():
        tmp=int(n)
        if MAX<tmp:
            MAX=tmp
        arr.append(tmp)
    else:
        break


dp = [0]*(MAX+1)
dp[0]=1
dp[1]=1
dp[2]=3
answer=[]
for i in range(3,MAX+1):
    dp[i]=dp[i-1]+dp[i-2]*2

for i in arr:
    print(dp[i])