from collections import defaultdict
import sys

input =sys.stdin.readline


tmp = defaultdict(list)
tree = defaultdict(list)
n, w = map(int, input().split())
for i in range(n - 1):
    u, v = map(int, input().split())
    tmp[u].append(v)
    tmp[v].append(u)

cnt=0
for i in tmp:
    if i == 1:
        continue
    if len(tmp[i])==1:
        cnt+=1

print(w/cnt)
