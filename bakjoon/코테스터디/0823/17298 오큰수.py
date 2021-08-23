n= int(input())
data = list(map(int,input().split()))
answer= [-1]* n
stack=[]


stack.append(0)
for i in range(n):
    while stack and data[stack[-1]]<data[i]:
        answer[stack.pop()]=data[i]
    stack.append(i)

print(answer)