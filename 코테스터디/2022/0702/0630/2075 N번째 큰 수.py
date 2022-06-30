import sys
import heapq


input =sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    arr = list(map(int, input().split()))
    if i == 0:
        for j in range(n):
            heapq.heappush(q, arr[j])
    else:
        for j in range(n):
            heapq.heappush(q, arr[j])
            heapq.heappop(q)

q.sort()
print(q[0])
