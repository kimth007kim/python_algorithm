n, m=map(int,input().split())
arr= list(map(int,list(input())))
cnt=m
stack=[]

for i in range(n):
    while cnt>0 and stack and stack[-1]<arr[i]:
        stack.pop()
        cnt-=1
    stack.append(arr[i])
stack=stack[:n-m]
answer="".join(list(map(str,stack)))
print(answer)