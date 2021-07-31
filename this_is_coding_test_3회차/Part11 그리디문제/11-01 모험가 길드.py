# n= int(input())
# data=list(map(int,input().split()))

n=5
data=[2,3,1,2,2]
# data=[5,4,3,1,1]
data.sort()
cnt=0
result=0
for i in data:
    cnt+=1
    if cnt>=i:
        result+=1
        cnt=0
print(result)