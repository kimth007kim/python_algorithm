import sys

input =sys.stdin.readline

n,t = map(int,input().split())

answer=0

def dfs(idx,time,total):
    global answer
    if len(idx)==n or time<0:
        return
    answer= max(answer,total)
    for i in range(n):
        if i not in idx:
            if time-arr[i][0]>=0:
                dfs(idx+[i], t - arr[i][0], total+arr[i][1])

arr=[]
for i in range(n):
    k,s =map(int,input().split())
    arr.append([k,s])

for i in range(n):
    if t- arr[i][0]>=0:
        dfs([i],t-arr[i][0],arr[i][1])

print(answer)