n,m= 5,5

data= [1,2,3,2,5]


interval_sum = 0
end =0
cnt= 0

for start in range(n):
    while end<n and interval_sum<m:
        interval_sum += data[end]
        end+=1
    if interval_sum==m:
        cnt+=1
    interval_sum-=data[start]

    print(start,end,interval_sum)

print(cnt)