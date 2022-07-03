import sys

input =sys.stdin.readline

n= int(input())
m= int(input())

road = [0]*(n+1)
arr= list(map(int,input().split()))

num = []
for i in arr:
    num.append([0,i,0])
start=1
end= n
answer=int(1e9)
while start<=end:
    mid = (start+end)//2
    road = [0]*(n+1)
    for i in range(m):
        num[i][0]= num[i][1]-mid
        if num[i][0]<0:
            num[i][0]=0
        num[i][2]=num[i][1]+mid
        if num[i][2]>n:
            num[i][2]=n

    if num[0][0]!=0 or num[m-1][2]!=n:
        start=mid+1
        continue
    flag= True
    for i in range(1,m):
        prev=num[i-1][2]
        next=num[i][0]
        if prev<next:
            flag =False
            break
        # print("-------",prev,next)
    if flag ==False:
        start=mid+1
        continue



    answer=min(answer,mid)
    end=mid-1

print(answer)