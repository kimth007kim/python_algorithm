from collections import deque
import sys
input = sys.stdin.readline

def proceed(cmd_q,num_q):
    flag = 0

    for c in cmd_q:
        if c== "R":
            flag+=1
        else:
            if len(num_q)<=0:
                return "error"
            else:
                if flag %2 ==0:
                    num_q.popleft()
                else:
                    num_q.pop()
    if flag %2 !=0:
        num_q.reverse()
    result = "["
    for j in range(len(num_q)):
        result += str(num_q[j])
        if len(num_q)-1!=j:
            result += ","
    result += "]"
    return result




answer=[]
for i in range(int(input())):
    D=0
    cmd = list(input().rstrip())
    for i in cmd:
        if i == "D":
            D+=1

    cmd_q = deque(cmd)
    length = int(input())
    arr = input().rstrip()
    if len(arr)==2:
        arr=[]
    else:
        arr= list(map(int,arr[1:-1].split(',')))
    num_q=deque(arr)
    if length<D:
        answer.append("error")
    else:
        answer.append(proceed(cmd_q,num_q))


for i in answer:
    print(i)
