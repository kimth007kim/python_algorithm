from collections import deque
import sys

input =sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
SET= set()
q=deque()
for i in range(n):
    q.append([arr[i],i])

while q:
    now, num = q.popleft()
    SET.add(now)
    for i in range(num+1,n):
        _next = now+arr[i]
        q.append([_next,i])

MAX= max(SET)
# print(SET)
answer=0
for i in range(1,MAX+2):
    if i not in SET:
        answer=i
        break
print(answer)