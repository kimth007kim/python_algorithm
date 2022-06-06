n,k= map(int,input().split())
num = list(input())
K, stack = k,[]

for i in range(n):
    print(stack,num)
    while K > 0 and stack and stack[-1]<num[i]:
        stack.pop()
        print(stack)
        K-=1
    stack.append(num[i])
