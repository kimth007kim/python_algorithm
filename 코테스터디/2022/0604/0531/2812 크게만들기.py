n, m = map(int,input().split())
num = list(map(int,list(input())))
stack = []
cnt = m


for i in range(n):
    while stack and cnt>0 and stack[-1]<num[i]:
        stack.pop()
        cnt-=1
    stack.append(num[i])
    print(stack)