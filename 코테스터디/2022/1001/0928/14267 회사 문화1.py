from collections import defaultdict,deque
import sys

input=sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

parents=[-1]*(n+1)
child=defaultdict(list)
answer=defaultdict(int)
tree= defaultdict(list)
for i in range(1,n):
    parents[i+1]=arr[i]
    child[arr[i]].append(i+1)
for i in range(2,n+1):
    q=deque()
    q.append([i,i])
    while q:
        now ,start = q.popleft()
        tree[start].append(now)
        for c in child[now]:
            q.append([c,start])

for _ in range(m):
    a,b= map(int,input().split())
    for i in tree[a]:
        answer[i]+=b

result=[]
for i in range(1,n+1):
    if i not in answer:
        result.append(0)
    else:
        result.append(answer[i])
print(*result)