n,m = map(int,input().split())
data=list(map(int,input().split()))


end = 0
cnt= 0
interval_sum=0
for start in range(n):
    while interval_sum<m and end<n:
        interval_sum+=data[end]
        end+=1
    if interval_sum==m:
        cnt+=1
    interval_sum-=data[start]

print(cnt)