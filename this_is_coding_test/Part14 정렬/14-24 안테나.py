n=int(input())
array=list(map(int,input().split()))
marray=max(array)

answer=[]
for i in range(1,marray+1):
    result=0
    for j in array:
        if i>j:
            result+=i-j
        else:
            result+=j-i
    answer.append((i,result))

answer.sort(key=lambda x: ((x[1],x[0])))

print(answer[0][0])