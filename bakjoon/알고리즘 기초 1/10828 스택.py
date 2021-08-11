import sys
input = sys.stdin.readline


n=int(input())
stack=[]
logs=[]

for i in range(n):
    tmp = input().strip()
    if "push" in tmp:
        a,b = map(str,tmp.split())
        stack.append(int(b))
    elif tmp =="pop":
        if len(stack)==0:
            logs.append(-1)
        else:
            d=stack.pop()
            logs.append(d)
    elif tmp =="size":
        logs.append(len(stack))
    elif tmp =="empty":
        if len(stack)==0:
            logs.append(1)
        else:
            logs.append(0)
    elif tmp =="top":
        LEN= len(stack)
        if LEN==0:
            logs.append(-1)
        else:
            logs.append(stack[len(stack)-1])

for i in logs:
    print(i)