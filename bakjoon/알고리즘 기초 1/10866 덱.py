from collections import deque
import sys

input = sys.stdin.readline

result=[]

n= int(input())
q=deque()

for i in range(n):
    com=input().strip()
    if com =="front":
        if len(q) == 0:
            result.append(-1)
        else:
            result.append(q[0])
    if com == "back":
        if len(q) == 0:
            result.append(-1)
        else:
            result.append(q[len(q)-1])
    elif com =="size":
        result.append(len(q))
    elif com =="empty":
        if len(q) == 0:
            result.append(1)
        else:
            result.append(0)
    elif "push_front"in com:
        a,b= map(str,com.split())
        q.appendleft(b)
    elif "push_back" in com:
        a,b= map(str,com.split())
        q.append(b)
    elif com =="pop_front":
        if len(q)==0:
            result.append(-1)
        else:
            a=q.popleft()
            result.append(a)
    elif com =="pop_back":
        if len(q) == 0:
            result.append(-1)
        else:
            a = q.pop()
            result.append(a)

    # else:
    #     a,b= map(str,com.split())
    #     q.append(int(b))

for i in result:
    print(i)