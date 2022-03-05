def dfs(cnt,arr):
    if cnt==m:
        tmp=arr[:]
        tmp.sort()
        if tmp not in result:
            result.append(tmp)
        return
    for i in range(len(number)):
        if number[i] not in arr:
            arr.append(number[i])
            dfs(cnt+1,arr)
            arr.pop()


n,m = map(int,input().split())
number= [ i for i in range(1,n+1)]
result = []

for i in range(len(number)):
    dfs(1,[number[i]])

for i in result:
    print(*i)