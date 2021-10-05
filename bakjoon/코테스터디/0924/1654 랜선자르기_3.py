import sys

input = sys.stdin.readline

k,n = map(int,input().split())
data=[]
for i in range(k):
    data.append(int(input()))

# print(data)

start = 1
end = max(data)

# print(start,end)
MAX_NUM=0
while start<=end:
# for _ in range(4):
    mid = (start+end)//2
    total=0
    for i in data:
        total += i//mid
    if total<n:
        end=mid-1
    else:
        start=mid+1
        MAX_NUM= max(MAX_NUM,mid)
print(MAX_NUM)