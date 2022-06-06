n,k = map(int,input().split())
num= list(input())

K= k
stack=[]

for i in range(n):
    # print("-------",stack[-1],"  ",num[i])
    while K>0 and stack and stack[-1]<num[i]:
        print(" 매치 ",stack,stack[-1],"  ",num,i,num[i])
        stack.pop()
        K-=1
        print(stack,i)
    stack.append(num[i])
print(stack)
