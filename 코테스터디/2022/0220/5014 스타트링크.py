from collections import deque
import sys

input = sys.stdin.readline


f,s,g,up,down = map(int,input().split())

cnt=0
q=deque()
q.append([cnt,s])
visited= [int(1e9)]*(f+1)
visited[s]=0
answer=[]
while q:
    cnt,now=q.popleft()
    if now-down>=1:
        if visited[now-down]>cnt+1:
            visited[now-down]=cnt+1
            q.append([cnt+1,now-down])
    if now +up<=f:
        if visited[now+up]>cnt+1:
            visited[now+up]=cnt+1
            q.append([cnt+1,now+up])

if visited[g]==int(1e9):
    print("use the stairs")
else:
    print(visited[g])