n,m = map(int,input().split())
cnt=0
def dfs(cnt,arr):
    global result
    if cnt ==m-1:
        print(" ".join(map(str,arr)))
        return
    for i in range(len(number)):
        if number[i] not in arr:
            arr.append(number[i])
            dfs(cnt + 1, arr)
            arr.pop()


number=  [ i+1 for i in range(n)]
for i in range(len(number)):
    dfs(0,[number[i]])