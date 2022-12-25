import sys

input =sys.stdin.readline

n= int(input())
arr=[]
for i in range(n):
    a,b= map(int,input().split())
    arr.append([a,b])
arr.sort(key = lambda x:x[0])
dp=[]

for a,b in arr:
    flag= False
    idx=0
    for i in range(len(dp)):
        if dp[i]==a:
            flag=True
            idx=i
            break
    if flag==True:
        dp[idx]=b
    else:
        dp.append(b)

print(len(dp))