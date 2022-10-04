n =int(input())
arr = list(map(int,input().split()))
cnt=0
for i in range(n):
    if arr[i]<0:
        cnt+=1
if cnt==n:
    print(max(arr))
else:
    start=0
    end=0
    total=0
    MAX=-int(1e11)

    for start in range(n):
        while total>=0 and end<n:
            total+=arr[end]
            end+=1
            MAX=max(MAX,total)
            # print(total,"   ",start," == ",end)
        total-=arr[start]
        MAX=max(MAX,total)
        # print(total,"   ",start," == ",end)
    print(MAX)