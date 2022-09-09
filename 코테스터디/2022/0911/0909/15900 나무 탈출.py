from collections import deque,defaultdict
import sys

input =sys.stdin.readline
tree= defaultdict(list)
parents= defaultdict(list)


n= int(input())
q=deque()
tree[1]
for i in range(n-1):
    a,b = map(int,input().split())
    if a in tree:
        tree[a].append(b)
        tree[b]
        parents[b]=a
    elif b in tree:
        tree[b].append(a)
        tree[a]
        parents[a]=b
    else:
        q.append([a,b])

while q:
    a,b = q.popleft()
    if a in tree:
        tree[a].append(b)
        tree[b]
        parents[b]=a
    elif b in tree:
        tree[b].append(a)
        tree[a]
        parents[a]=b
    else:
        q.append([a,b])
def dfs(now):
    global cnt
    if now==1:
        return
    cnt+=1
    dfs(parents[now])



cnt= 0
for i in tree:
    if len(tree[i])==0:
        dfs(i)

if cnt%2==0:
    print("No")
else:
    print("Yes")