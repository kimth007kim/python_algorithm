import sys

input =sys.stdin.readline

n,m = map(int,input().split())
arr= list(map(int,input().split()))

answer=0
# print(arr)
total=0
start=0
cnt=0
for end in range(n):
    total+=arr[end]
    cnt+=1
    # print(start,end,total,cnt)
    if cnt==m:
        answer=max(answer,total)
        total-=arr[start]
        # print("========= ",start,end,total,cnt)
        start+=1
        cnt-=1

print(answer)