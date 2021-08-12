from collections import deque
import sys
input = sys.stdin.readline

def solution(data):
    q=deque()
    arr= list(data)
    for i in arr:
        q.append(i)
    cnt=0
    while q:
        a=q.popleft()
        if a=="(":
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            return False
    if cnt!=0:
        return False
    else:
        return True

answer=[]
n= int(input())
for i in range(n):
    data= list(input().strip())
    if len(data)%2!=0:
        answer.append("NO")
    else:
        if solution(data):
            answer.append("YES")
        else:
            answer.append("NO")

for i in answer:
    print(i)