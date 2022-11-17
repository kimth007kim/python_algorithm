import sys, heapq

input = sys.stdin.readline
INF = int(1e11)
n, m, x, y = map(int, input().split())
distance = [INF] * (n)
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

q = []
heapq.heappush(q, [0, y])
while q:
    dist, now = heapq.heappop(q)
    # print(dist, now)
    if dist < distance[now]:
        distance[now] = dist
    for node, d in graph[now]:
        # print(node,d)
        if distance[node] > dist + d:
            distance[node] = dist + d
            heapq.heappush(q, [dist + d, node])

day = 0
total = 0
result = True

distance.sort()

for i in distance:
    if i == 0:
        continue
    trip = i * 2
    if trip > x:
        result = False
        break
    if total + trip > x:
        day += 1
        total = trip
    else:
        total += trip

if result == False:
    print(-1)
else:
    print(day + 1)
