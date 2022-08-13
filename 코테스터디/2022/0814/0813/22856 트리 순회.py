from collections import defaultdict
from collections import deque

n = int(input())

parents = defaultdict(int)
child = defaultdict(list)
visited = {}
parents[1]
for i in range(n):
    a, b, c = map(int, input().split())
    visited[a] = False
    if b != -1:
        parents[b] = a
        child[a].append(b)
        visited[b] = False
    if c != -1:
        parents[c] = a
        child[a].append(c)
        visited[c] = False
total = len(visited)-1
move = 0
visited[1] = True

q = deque()
q.append([1, move])
while total > 0:
    # print(q,total)
    now, m = q.popleft()
    move=m+1
    left = 0
    right = 0
    if len(child[now]) == 2:
        left = child[now][0]
        right = child[now][1]
        if visited[left] == False:
            visited[left]=True
            q.append([left,m+1])
            total-=1
        elif visited[right]==False:
            visited[right]=True
            q.append([right,m+1])
            total-=1
        elif parents[now]!=0:
            q.append([parents[now],m+1])
        else:
            break


    elif len(child[now]) == 1:
        left = child[now][0]
        if visited[left] == False:
            visited[left] = True
            q.append([left, m + 1])
            total-=1
        elif parents[now] != 0:
            q.append([parents[now], m + 1])
        else:
            break
    else:
        if parents[now] != 0:
            q.append([parents[now], m + 1])
        else:
            break

# print(parents)
# print(child)
# print(visited)
print(move)