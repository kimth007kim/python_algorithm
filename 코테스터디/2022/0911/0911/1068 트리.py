from collections import defaultdict, deque
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
target = int(input())
root = 0


tree = defaultdict(list)

for i in range(len(arr)):
    if arr[i] == -1:
        root=i
    if i== target or arr[i]==target:
        continue
    tree[arr[i]].append(i)
cnt = 0

q = deque()
visited = [False] * (n)
visited[target] = True
visited[root] = True
q.append(root)
while q:
    # print(q)
    now = q.popleft()
    if now == target:
        continue




    if now not in tree:
        cnt += 1
        continue
    for i in tree[now]:
        if visited[i] == False:
            visited[i] = True
            q.append(i)
print(cnt)
