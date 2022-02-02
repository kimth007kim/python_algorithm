import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

x = [-1, 1, 2]
ll = []

def bfs(now,target):
    queue = deque([])
    visited = [0 for _ in range(300009)]
    queue.append([now,0])
    while queue:
        q,c = queue.popleft()
        visited[q] = 1
        if q == target:
            count = c
            ll.append(count)
        for i in range(3):
            if i == 2:
                a = q * 2
                if visited[a] == 0 and 0<=a<=100000:
                    queue.append([a,c])
            else:
                a = q + x[i]
                if visited[a] == 0 and 0<=a<=100000:
                    queue.append([a,c+1])

if n>k:
    print(n-k)
else:
    bfs(n,k)
    print(min(ll))