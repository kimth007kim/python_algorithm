from collections import deque


def bfs1(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for e in arr[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
               
def bfs2(arr,start,visited2):
    queue=deque([start])
    visited2[start]=True

    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in arr[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i]=True


n, m, v = map(int, input().split(' '))

arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split(' '))
    arr[x].append(y)
    arr[y].append(x)

for i in arr:
    i.sort()


visited = [False] * (n+1)
bfs1(v)
print()
visited2 = [False] * (n+1)
bfs2(arr,v,visited2)