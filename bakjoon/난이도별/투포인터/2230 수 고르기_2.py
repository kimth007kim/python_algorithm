import sys

input= sys.stdin.readline


n,m= map(int,input().split())
data=[]
for i in range(n):
    data.append(int(input()))
# print(data)

# if m ==0:
#     print(0)
# else:
MIN_VALUE= int(1e15)
data.sort()
interval_sum=-1
end=1
left,right =0,0
while left <n and right<n:
    if data[right]-data[left]<m:
        right+=1
    else:
        MIN_VALUE = min(MIN_VALUE,data[right]-data[left])
        left+=1
    print(left,right)


# for start in range(n-1):
#     while interval_sum<m and end<n:
#         # print(data[end],data[start])
#         interval_sum=data[end]-data[start]
#         # print(interval_sum,"end[",end,"]=", data[end], "start[",start,"]=",data[start])
#         end+=1
#
#     if interval_sum>=m:
#         MIN_VALUE=min(MIN_VALUE,interval_sum)
#     interval_sum=-1

print(MIN_VALUE)