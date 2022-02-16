import sys

input = sys.stdin.readline

result=[]
while True:
    tmp=list(map(int,list(input().split())))
    k= tmp[0]
    s= tmp[1:]
    if k==0:
        break
    answer=[]
    def dfs(cnt,idx,s,k,arr):
        if cnt ==6:
            answer.append(arr)
            return
        if k-idx+len(arr)<0:
            return
        for i in range(idx+1,len(s)):
            if s[i] not in arr:
                t = arr[:]
                t.append(s[i])
                dfs(cnt + 1,i, s, k, t)
    for i in range(len(s)):
        dfs(1,i,s,k,[s[i]])
    result.append(answer)

for i in range(len(result)):
    for j in result[i]:
        print(*j)
    if i!=len(result)-1:
        print()
