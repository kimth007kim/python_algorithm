import sys

input = sys.stdin.readline


answer=set()
def dfs(cnt,visited):
    if cnt == k:
        tmp =""
        for j in visited:
            tmp+=arr[j]
        answer.add(tmp)
        return
    for i in range(n):
        if i not in visited:
            dfs(cnt+1,visited+[i])

n= int(input())
k= int(input())
arr = []

for i in range(n):
    arr.append((input().rstrip()))

for i in range(n):
    dfs(1,[i])

print(len(answer))