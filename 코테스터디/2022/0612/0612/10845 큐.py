from collections import deque
import sys

input = sys.stdin.readline

result=[]

n= int(input())
q=deque()

for i in range(n):
    com=input().strip()
    if com =="pop":
        if len(q) == 0:
            result.append(-1)
        else:
            result.append(q.popleft())
    elif com =="size":
        result.append(len(q))
    elif com =="empty":
        if len(q) == 0:
            result.append(1)
        else:
            result.append(0)
    elif com =="front":
        if len(q)==0:
            result.append(-1)
        else:
            result.append(q[0])
    elif com =="back":
        if len(q) == 0:
            result.append(-1)
        else:
            result.append(q[len(q)-1])
    else:
        a,b= map(str,com.split())
        q.append(int(b))

for i in result:
    print(i)