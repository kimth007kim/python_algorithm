import sys

input = sys.stdin.readline

n= int(input())
data= list(map(int,input().split()))

answer= [-1]*n

for i in range(n-1):
    for j in range(i+1,n):
        if data[i]<data[j]:
            answer[i]=data[j]
            break
        answer[i]=-1
        # print(i,j,data[i],data[j])



result =""
for i in range(len(answer)):
    result+=str(answer[i])
    if i != len(answer)-1:
        result+=" "

print(result)