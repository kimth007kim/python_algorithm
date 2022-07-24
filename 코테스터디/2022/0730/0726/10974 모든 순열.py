def dfs(arr):
    if len(arr)==n:
        answer.append(arr)
        return
    for i in range(1,n+1):
        if i not in arr:
            dfs(arr+[i])
answer=[]
n= int(input())

for i in range(1,n+1):
    dfs([i])

for i in answer:
    print(*i)