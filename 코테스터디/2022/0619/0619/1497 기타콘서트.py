import sys

input = sys.stdin.readline


n, m = map(int, input().rstrip().split())
arr = []
cand= {}
MAX=-1

def dfs(cnt, idx, visited,num):
    global cand,MAX

    MAX=max(MAX,num)
    if num not in cand:
        cand[num]=cnt
    else:
        cand[num]=min(cand[num],cnt)
    if cnt==n:
        return
    for i in range(n):
        if i not in idx:
            tmp_visit= arr[i][2]
            tmp=0
            result = []
            for j in range(m):
                if tmp_visit[j]==True or visited[j]==True:
                    result.append(True)
                else:
                    result.append(False)

            for j in result:
                if j == True:
                    tmp += 1
            dfs(cnt+1,idx+[i],result,tmp)
for i in range(n):
    name, tmp = input().split()
    boo = []
    for j in tmp:
        if j == "Y":
            boo.append(True)
        else:
            boo.append(False)
    arr.append([i, name, boo])

for i in range(n):
    a, b, c = arr[i]
    cnt=0
    for i in c:
        if i == True:
            cnt+=1
    dfs(1,[a],c,cnt)


# print(cand)
# print(MAX)
if MAX==0:
    print(-1)
else:
    print(cand[MAX])
