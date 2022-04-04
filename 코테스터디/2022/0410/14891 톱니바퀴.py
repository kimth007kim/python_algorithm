from collections import deque
import sys
input =sys.stdin.readline
def turn(q,target,d,visted):
    now_6=q[target][6]
    now_2=q[target][2]
    if d==1:
        tmp=q[target].pop()
        q[target].appendleft(tmp)
    else:
        tmp = q[target].popleft()
        q[target].append(tmp)
    left,right = target-1,target+1
    if left>-1 and visited[left]==0:
        if now_6!=q[left][2]:
            visited[left] = 1
            turn(q,left, -d, visted)

    if right<4 and visited[right]==0:
        if now_2!=q[right][6]:
            visited[right] = 1
            turn(q, right, -d, visted)

q=[]
for i in range(4):
    tmp=deque(map(int,list(input().rstrip())))
    q.append(tmp)
k= int(input())
for i in range(k):
    visited=[0]*4
    target,d= map(int,input().split())
    target-=1
    visited[target]=1
    turn(q, target, d,visited)

total=0
score =1
for i in range(4):
    twelve = q[i][0]
    if twelve==1:
        total+=score
    score*=2

print(total)