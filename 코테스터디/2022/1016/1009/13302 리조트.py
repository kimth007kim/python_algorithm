def dfs(day,cnt,total):
    global answer
    if total>answer:
        return
    if day >= n:
        answer = min(answer, total)
        return
    if day+1 in arr:
        dfs(day+1,cnt,total)
    else:
        if cnt>=3:
            dfs(day+1,cnt-3,total)
        for a1,b1,c1 in ticket:
            dfs(day+a1,cnt+b1,total+c1)
    # print(day,cnt,total)


n,m= map(int,input().split())
arr= set(list(map(int,input().split())))
ticket = [[1,0,10000],[3,1,25000],[5,2,37000]]
answer=int(1e11)
for a,b,c in ticket:
    if a>=n:
        answer= min(answer,c)
        continue
    dfs(a,b,c)

print(answer)