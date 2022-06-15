from collections import deque
import sys
input =sys.stdin.readline
n,m = map(int,input().split())
arr= list(map(int,input().split()))
normal=[]
ten=[]
answer=0
for i in arr:
    if i==10:
        answer+=1
        continue
    if i<10:
        continue
    if i%10==0:
        ten.append(i)
    else:
        normal.append(i)

ten.sort()
normal.sort()
q=deque()
for i in ten:
    q.append(i)
for i in normal:
    q.append(i)
while m>0 and q:
    now = q.popleft()
    next =now-10
    answer+=1
    m-=1
    if next<10:
        continue
    elif next==10:
        answer+=1
    else:
        q.appendleft(next)

print(answer)

