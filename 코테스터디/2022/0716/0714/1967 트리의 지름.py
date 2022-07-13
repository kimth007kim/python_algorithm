from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

def get_distance(start):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    q = deque()
    q.append([start, 0])
    while q:
        now, d = q.popleft()
        distance[now] = d
        for _next, _d in tree[now]:
            if distance[_next] == INF:
                q.append([_next, d + _d])

    return distance
n = int(input())

tree = defaultdict(list)
for i in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])




root_distance = get_distance(1)

idx=0
MAX=-1
for i in range(1,n+1):
    if root_distance[i]>MAX:
        MAX=root_distance[i]
        idx=i

next_distance= get_distance(idx)
print(max(next_distance[1:]))