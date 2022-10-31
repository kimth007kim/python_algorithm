from collections import deque
import sys

input = sys.stdin.readline



n,k = map(int,input().split())
arr= list(map(int,input().split()))
visit=set(arr)
cnt=0
result=0

q=deque()
d= [1,-1]
for i in d:
    for j in arr:
        q.append([j,j+i])

while q:
    if cnt == k:
        break
    now,_next = q.popleft()
    if _next not in visit:
        result+=abs(now-_next)
        visit.add(_next)
        cnt+=1
        for i in d:
            q.append([now,_next+i])

print(result)