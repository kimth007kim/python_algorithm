n, m = map(int,input().split())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()
print(data)

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum< m and end<n:
        interval_sum+= data[end]
        end+=1
    if interval_sum==m:
        count+=1
    interval_sum-=data[start]

print(count)