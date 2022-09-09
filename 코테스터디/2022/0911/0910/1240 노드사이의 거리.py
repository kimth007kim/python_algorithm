from collections import defaultdict, deque
import sys

input =sys.stdin.readline

def bfs(start, end):
    visited = [False] * (n + 1)
    q = deque()
    q.append([start, 0])
    visited[start]=True
    while q:
        now, dist = q.popleft()
        if now == end:
            return dist
        for _next,_dist in tree[now]:
            if visited[_next]==False:
                q.append([_next,dist+_dist])
                visited[_next]=True


n, m = map(int, input().split())

tree = defaultdict(list)
for i in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

arr = []
for i in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e))
