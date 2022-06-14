n= int(input())
arr = list(map(int,input().split()))
answer=0

def dfs(arr,result):
    global answer
    if len(arr)==2:
        answer= max(answer,result)
        return
    for now in range(1, len(arr)-1):
        dfs(arr[:now]+arr[now+1:],result+arr[now-1]*arr[now+1])

dfs(arr,0)

print(answer)