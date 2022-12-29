import sys
from collections import deque
input =sys.stdin.readline

n,k= map(int,input().split())
arr= list(map(int,input().split()))

# n,k= 657 ,3
# arr= [1, 5, 7]


q=deque()
answer=-1

for i in range(k):
    if arr[i]<=n:
        answer=max(answer,arr[i])
        q.append([arr[i],1])

while q:
    now, cnt = q.popleft()
    for i in range(k):
        tmp = now+arr[i]*10**(cnt)
        if tmp<=n:
            answer=max(answer,tmp)
            q.append([tmp,cnt+1])

print(answer)