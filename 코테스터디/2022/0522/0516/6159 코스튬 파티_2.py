from itertools import combinations

n,s = map(int,input().split())
data=[]
for i in range(n):
    data.append(int(input()))
answer=0

data.sort()
start,end=0,n-1

while start<end:
    print(start,end,data[start]+data[end])
    if data[start]+data[end]<=s:
        answer+=+end-start
    else:
        end-=1
        start-=1
    start+=1
print(answer)