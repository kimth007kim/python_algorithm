from collections import defaultdict, deque
import sys

input =sys.stdin.readline

def bfs(s):
    node = -1
    value = -1

    q = deque()
    visited = set()
    visited.add(s)
    q.append([s, 0])

    while q:
        now, dist = q.popleft()
        if dist>=value:
            value =dist
            node = now
        for n, d in dict[now]:
            if n not in visited:
                visited.add(n)
                q.append([n,dist+d])

    return node,value

dict = defaultdict(list)

while True:
    try:
        a, b, c = map(int, input().split())
        dict[a].append([b, c])
        dict[b].append([a, c])
    except:
        break
dist = 0
start = -1
for i in dict:
    if len(dict[i]) == 1:
        start = i
        break

node,value =bfs(start)
n,d=bfs(node)

print(d)