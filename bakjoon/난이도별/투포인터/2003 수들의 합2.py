n,m  = map(int,input().split())
data = list(map(int,input().split()))

cnt= 0
interval_sum=0
end=0

for start in range(n):
    while interval_sum < m and end< n:
        interval_sum+= data[end]
        # print("data[",start,"]=",start ,"data[",end,"]=",end, interval_sum)
        end+=1
    if interval_sum==m:
        # print(interval_sum,"여기",start,end)
        cnt+=1
    interval_sum-=data[start]

print(cnt)