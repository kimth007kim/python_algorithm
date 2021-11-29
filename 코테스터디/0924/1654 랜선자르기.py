# 가지고있는 랜선의 갯수 k
# 필요한 랜선의 개수 n

# k줄에 걸쳐 이미 가지고있는 각 랜선의 길이
import sys

input = sys.stdin.readline


def binary_search(data,start,end):
    mid = (start+ end)//2
    total=0
    while total!=n:
        total = 0
        for i in data:
            total += i // mid
        if total == n:
            return mid
        elif total<n:
            mid-=1
        elif total>n:
            mid+=1

k,n= map(int,input().split())
data = []
cnt=0

for i in range(k):
    tmp = int(input())
    data.append(tmp)
    cnt+=tmp
start ,end= 1, max(data)

# while start<= end:
#     mid = (start+ end)//2
#     lines =0
#     for i in data:
#         lines+= i// mid
#     print(mid,"      ",start,end,lines)
#     if lines >=n:
#         start = mid+1
#     else:
#         end=mid-1
# print(end)
print(binary_search(data,cnt//n,data[-1]))

