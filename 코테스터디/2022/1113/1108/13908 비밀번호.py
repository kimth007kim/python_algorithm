def dfs(cnt,password):
    global answer
    if cnt==n:
        tmp = set(password)
        for i in arr:
            if i not in tmp:
                return
        answer+=1
        return
    for i in number:
        dfs(cnt+1,password+[i])



n, m = map(int, input().split())
if m==0:
    arr=[]
else:
    arr = list(map(int, input().split()))
number = [i for i in range(10)]
answer=0

for i in number:
    dfs(1,[i])
print(answer)