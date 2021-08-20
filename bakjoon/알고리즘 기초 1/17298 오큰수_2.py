import sys

input = sys.stdin.readline

n= int(input())
data= list(map(int,input().split()))

answer= [-1]*n
stack=[]
stack.append(0)
for i in range(n):
    print(i,"         ",stack)
    while stack and data[stack[-1]]<data[i]:
        print(i,"  ",stack,stack[-1],data[i])
        answer[stack.pop()]=data[i]
        print(answer)
    stack.append(i)

print(*answer)